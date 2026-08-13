"""ClusterAI - AI-Powered Customer Segmentation

A Flask web application that segments e-commerce customers using K-Means
clustering. Users upload a CSV file of customer data, and the app returns
cluster labels, evaluation metrics, and visual analytics (Elbow plot, pair
plot, PCA 2D/3D scatterplots, and distribution charts).
"""

import os

import matplotlib
matplotlib.use('Agg')  # Non-GUI backend, required for server-side rendering

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from flask import Flask, render_template, request, url_for
from markupsafe import Markup, escape
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Number of clusters used for segmentation and the business-friendly names
# assigned to each cluster index produced by KMeans.
N_CLUSTERS = 4
CLUSTER_LABELS = {
    0: "Budget Shoppers",
    1: "High Spenders",
    2: "Occasional Buyers",
    3: "Loyal Customers",
}


@app.template_filter()
def strip_newlines(value):
    """Remove literal '\\n' sequences and real newline characters from a
    string, then return it as HTML-safe Markup for template rendering.
    """
    if not isinstance(value, str):
        return value
    s = escape(value)
    s = s.replace("\\n", "")
    s = s.replace("\n", "")
    return Markup(s)


def _static_url(path):
    """Convert an absolute/relative file path under static/ into a Flask
    static URL, normalizing Windows-style backslashes.
    """
    relative_path = os.path.relpath(path, 'static/').replace('\\', '/')
    return url_for('static', filename=relative_path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('file')
    if not file:
        return "No file uploaded", 400

    try:
        df = pd.read_csv(file)
    except Exception as e:
        return f"Error reading CSV: {e}", 400

    df_numeric = df.select_dtypes(include=['int64', 'float64']).dropna()
    if df_numeric.empty:
        return "No numeric data to analyze", 400

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_numeric)

    kmeans = KMeans(n_clusters=N_CLUSTERS, n_init=10, random_state=42)
    df['Cluster'] = kmeans.fit_predict(scaled_data)
    sil_score = silhouette_score(scaled_data, df['Cluster'])
    df['Cluster_Label'] = df['Cluster'].map(CLUSTER_LABELS)

    # Persist the full labeled dataset for download
    csv_full_path = os.path.join(UPLOAD_FOLDER, "clustered_customers_labeled.csv")
    df.to_csv(csv_full_path, index=False)

    # --- Elbow Method plot (optimal cluster count) ---
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

    # --- Pair plot of numeric features by cluster ---
    plot_data = df_numeric.copy()
    plot_data['Cluster'] = df['Cluster'].astype(str)
    sns.pairplot(plot_data, hue='Cluster', palette='Set2', diag_kind='hist')
    pairplot_path = os.path.join(UPLOAD_FOLDER, "pairplot.png")
    plt.savefig(pairplot_path)
    plt.close()

    # --- PCA 2D scatterplot ---
    pca_2d_vals = PCA(n_components=2).fit_transform(scaled_data)
    plt.figure()
    for cl in sorted(df['Cluster'].unique()):
        plt.scatter(
            pca_2d_vals[df['Cluster'] == cl, 0],
            pca_2d_vals[df['Cluster'] == cl, 1],
            label=CLUSTER_LABELS.get(cl, str(cl))
        )
    plt.legend()
    plt.title("PCA - 2D")
    plt.tight_layout()
    pca2d_path = os.path.join(UPLOAD_FOLDER, "pca_2d.png")
    plt.savefig(pca2d_path)
    plt.close()

    # --- PCA 3D scatterplot ---
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (enables 3D projection)
    pca_3d_vals = PCA(n_components=3).fit_transform(scaled_data)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for cl in sorted(df['Cluster'].unique()):
        ax.scatter(
            pca_3d_vals[df['Cluster'] == cl, 0],
            pca_3d_vals[df['Cluster'] == cl, 1],
            pca_3d_vals[df['Cluster'] == cl, 2],
            label=CLUSTER_LABELS.get(cl, str(cl))
        )
    ax.set_title("PCA - 3D")
    ax.legend()
    plt.tight_layout()
    pca3d_path = os.path.join(UPLOAD_FOLDER, "pca_3d.png")
    plt.savefig(pca3d_path)
    plt.close()

    # --- Cluster distribution pie chart ---
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

    # --- Cluster distribution bar chart ---
    bar_path = os.path.join(UPLOAD_FOLDER, "cluster_distribution_bar.png")
    plt.figure()
    plt.bar(cluster_counts.index, cluster_counts.values, color=plt.cm.Set3.colors)
    plt.title("Customer Count per Cluster")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(bar_path)
    plt.close()

    # Preview table of the first 10 labeled records
    raw_table_html = df.head(10).to_html(
        classes='table table-striped table-bordered',
        index=False
    )
    cleaned_html = raw_table_html.replace("\\n", "").replace("\n", "")
    table_html = Markup(cleaned_html)

    return render_template(
        "result.html",
        elbow_img=_static_url(elbow_path),
        cluster_img=_static_url(pairplot_path),
        pca_2d_img=_static_url(pca2d_path),
        pca_3d_img=_static_url(pca3d_path),
        pie_chart_img=_static_url(pie_path),
        bar_chart_img=_static_url(bar_path),
        silhouette_score=round(sil_score, 3),
        table_html=table_html,
        csv_path=_static_url(csv_full_path)
    )


if __name__ == "__main__":
    # Set FLASK_DEBUG=1 in your environment for local debugging.
    # Never run with debug mode enabled in production.
    debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug_mode)
