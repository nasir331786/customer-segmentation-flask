import matplotlib
matplotlib.use('Agg')  # Set non-GUI backend to avoid warnings
from flask import Flask, render_template, request, url_for
from markupsafe import Markup, escape
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.template_filter()
def strip_newlines(value):
    """
    Remove literal backslash-n (\\n) and actual newline characters (\n)
    Then return an HTML-safe Markup string.
    """
    if not isinstance(value, str):
        return value
    # First escape any dangerous HTML
    s = escape(value)
    # Remove literal \n sequences
    s = s.replace("\\n", "")
    # Remove actual newline characters
    s = s.replace("\n", "")
    return Markup(s)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('file')
    if not file:
        return "No file uploaded", 400

    # Read CSV
    try:
        df = pd.read_csv(file)
    except Exception as e:
        return f"Error reading CSV: {e}", 400

    # Select numeric columns
    df_numeric = df.select_dtypes(include=['int64', 'float64']).dropna()
    if df_numeric.empty:
        return "No numeric data to analyze", 400

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_numeric)

    # KMeans clustering
    kmeans = KMeans(n_clusters=4, n_init=10, random_state=42)
    df['Cluster'] = kmeans.fit_predict(scaled_data)
    sil_score = silhouette_score(scaled_data, df['Cluster'])

    # Map cluster labels
    labels_map = {
        0: "Budget Shoppers",
        1: "High Spenders",
        2: "Occasional Buyers",
        3: "Loyal Customers"
    }
    df['Cluster_Label'] = df['Cluster'].map(labels_map)

    # Save full labeled CSV
    csv_full_path = os.path.join(UPLOAD_FOLDER, "clustered_customers_labeled.csv")
    df.to_csv(csv_full_path, index=False)

    # Generate plots etc.
    # Elbow
    sse = []
    for k in range(1, 11):
        km = KMeans(n_clusters=k, n_init=10, random_state=42)
        km.fit(scaled_data)
        sse.append(km.inertia_)
    plt.figure()
    plt.plot(range(1, 11), sse, marker='o', linestyle='--')
    plt.title("Elbow Method")
    plt.xlabel("k")
    plt.ylabel("SSE")
    plt.tight_layout()
    elbow_path = os.path.join(UPLOAD_FOLDER, "elbow.png")
    plt.savefig(elbow_path)
    plt.close()

    # Pairplot
    plot_data = df_numeric.copy()
    plot_data['Cluster'] = df['Cluster'].astype(str)
    sns.pairplot(plot_data, hue='Cluster', palette='Set2', diag_kind='hist')
    pairplot_path = os.path.join(UPLOAD_FOLDER, "pairplot.png")
    plt.savefig(pairplot_path)
    plt.close()

    # PCA 2D
    pca_2d_vals = PCA(n_components=2).fit_transform(scaled_data)
    plt.figure()
    for cl in sorted(df['Cluster'].unique()):
        plt.scatter(
            pca_2d_vals[df['Cluster'] == cl, 0],
            pca_2d_vals[df['Cluster'] == cl, 1],
            label=labels_map.get(cl, str(cl))
        )
    plt.legend()
    plt.title("PCA - 2D")
    plt.tight_layout()
    pca2d_path = os.path.join(UPLOAD_FOLDER, "pca_2d.png")
    plt.savefig(pca2d_path)
    plt.close()

    # PCA 3D
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    pca_3d_vals = PCA(n_components=3).fit_transform(scaled_data)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for cl in sorted(df['Cluster'].unique()):
        ax.scatter(
            pca_3d_vals[df['Cluster'] == cl, 0],
            pca_3d_vals[df['Cluster'] == cl, 1],
            pca_3d_vals[df['Cluster'] == cl, 2],
            label=labels_map.get(cl, str(cl))
        )
    ax.set_title("PCA - 3D")
    ax.legend()
    plt.tight_layout()
    pca3d_path = os.path.join(UPLOAD_FOLDER, "pca_3d.png")
    plt.savefig(pca3d_path)
    plt.close()

    # Pie chart
    cluster_counts = df['Cluster_Label'].value_counts()
    pie_path = os.path.join(UPLOAD_FOLDER, "cluster_distribution_pie.png")
    plt.figure()
    plt.pie(
        cluster_counts,
        labels=cluster_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Set3.colors
    )
    plt.title("Customer Distribution")
    plt.tight_layout()
    plt.savefig(pie_path)
    plt.close()

    # Bar chart
    bar_path = os.path.join(UPLOAD_FOLDER, "cluster_distribution_bar.png")
    plt.figure()
    plt.bar(cluster_counts.index, cluster_counts.values, color=plt.cm.Set3.colors)
    plt.title("Customer Count per Cluster")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(bar_path)
    plt.close()

    # Build table HTML
    raw_table_html = df.head(10).to_html(
        classes='table table-striped table-bordered',
        index=False
    )
    # Debug prints (optional)
    print("=== RAW TABLE HTML (repr) ===")
    print(repr(raw_table_html))
    cleaned_html = raw_table_html.replace("\\n", "").replace("\n", "")
    print("=== CLEANED TABLE HTML (repr) ===")
    print(repr(cleaned_html))
    table_html = Markup(cleaned_html)

    return render_template(
        "result.html",
        elbow_img=url_for('static', filename=os.path.relpath(elbow_path, 'static/').replace('\\', '/')),
        cluster_img=url_for('static', filename=os.path.relpath(pairplot_path, 'static/').replace('\\', '/')),
        pca_2d_img=url_for('static', filename=os.path.relpath(pca2d_path, 'static/').replace('\\', '/')),
        pca_3d_img=url_for('static', filename=os.path.relpath(pca3d_path, 'static/').replace('\\', '/')),
        pie_chart_img=url_for('static', filename=os.path.relpath(pie_path, 'static/').replace('\\', '/')),
        bar_chart_img=url_for('static', filename=os.path.relpath(bar_path, 'static/').replace('\\', '/')),
        silhouette_score=round(sil_score, 3),
        table_html=table_html,
        csv_path=url_for('static', filename=os.path.relpath(csv_full_path, 'static/').replace('\\', '/'))
    )


if __name__ == "__main__":
    app.run(debug=True)
