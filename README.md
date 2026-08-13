# ClusterAI — AI-Powered Customer Segmentation

**An end-to-end Flask web application that transforms raw e-commerce customer data into actionable, business-ready segments using K-Means clustering.**

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Flask](https://img.shields.io/badge/Flask-Framework-black) ![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-orange) ![License](https://img.shields.io/badge/License-MIT-green)



---

## 🎯 Project Overview

Most businesses treat every customer the same way, even though spending habits, income, and purchase frequency vary significantly across a customer base. **ClusterAI** solves this by applying unsupervised machine learning to automatically group customers into meaningful, interpretable segments — **Budget Shoppers, High Spenders, Occasional Buyers, and Loyal Customers**.

Users upload a CSV of customer data, and the application handles the full pipeline: cleaning, scaling, clustering, evaluation, and visualization — surfaced through an interactive dashboard that requires no technical background to interpret.
<img width="1908" height="1420" alt="screencapture-127-0-0-1-5000-2025-09-28-16_45_00" src="https://github.com/user-attachments/assets/b5141711-a65f-47df-8627-e1233b3c95c1" />
<img width="1908" height="5590" alt="screencapture-127-0-0-1-5000-analyze-2025-09-28-17_20_30" src="https://github.com/user-attachments/assets/1c6423cd-6beb-4b67-b91d-1b3b7e0a4cd1" />


---

## ✨ Key Features

- 📤 Upload CSV files containing customer data through a responsive web interface
- 🧹 Automatic data cleaning and feature scaling (handles missing values, standardizes numeric features)
- 🧩 Customer segmentation using **K-Means clustering**
- 📏 Cluster quality evaluation via **Silhouette Score**
- 📉 Optimal cluster count determined using the **Elbow Method**
- 🏷️ Business-friendly cluster labels (e.g. "Budget Shoppers", "High Spenders")
- 📊 Visual analytics: pie charts, bar charts, pair plots, and 2D/3D PCA scatterplots
- 📋 In-dashboard preview of labeled customer records
- ⬇️ One-click download of the full cluster-labeled dataset as CSV
- 💡 Segment-specific marketing recommendations and engagement tips
- 🔍 Toggleable "Show Technical Details" panel for advanced clustering diagnostics

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Language** | Python |
| **Backend** | Flask |
| **Frontend** | HTML, CSS / Tailwind CSS, Lottie Animations |
| **Data Processing** | Pandas, StandardScaler |
| **Machine Learning** | Scikit-learn (K-Means, PCA, Silhouette Score) |
| **Visualization** | Matplotlib, Seaborn, mpl_toolkits.mplot3d |
| **Storage** | CSV files, OS module for file/path management |
| **Utilities** | MarkupSafe (safe HTML rendering) |

---

## 🏗️ How It Works

```
CSV Upload
   ↓
Data Cleaning & Feature Scaling (Pandas, StandardScaler)
   ↓
K-Means Clustering + Cluster Evaluation (Silhouette Score, Elbow Method)
   ↓
Dimensionality Reduction for Visualization (PCA)
   ↓
Interactive Dashboard (Flask + Matplotlib/Seaborn charts)
   ↓
Business Insights: Segment Labels, Marketing Tips, Downloadable CSV
```

---

## 📂 Project Structure

```
customer-segmentation-flask/
├── app.py                  # Flask application: routes, clustering pipeline, chart generation
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python runtime version (for deployment)
├── .gitignore              # Excludes venv, cache, and generated files
├── LICENSE                 # MIT License
├── README.md
├── templates/               # HTML templates (index.html, result.html)
├── static/                  # CSS, generated charts, uploaded files
├── data/                    # Sample customer datasets
└── outputs/                 # Example cluster-labeled output CSV
```

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nasir331786/customer-segmentation-flask.git
   cd customer-segmentation-flask
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   ```
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open the local URL shown in your terminal, usually:
   ```
   http://127.0.0.1:5000
   ```

---

## ▶️ Usage

1. Open the application in a browser.
2. Upload a CSV file containing customer data (e.g. Customer ID, Age, Income, Spending Score, Purchase Frequency).
3. Click **Analyze Data** to run the clustering pipeline.
4. Review the segmentation dashboard: pie/bar charts, segment descriptions, and marketing tips.
5. Expand **Show Technical Details** for the Elbow plot, pair plot, and PCA 2D/3D visualizations.
6. Download the full labeled CSV for further analysis.

---

## 📊 Results / Insights

On the included sample dataset (100 customers), the model identified 4 clusters with a **Silhouette Score of 0.661**, indicating well-separated, meaningful groups:

| Segment | Share of Customers | Recommended Action |
|---|---|---|
| Budget Shoppers | 28% | Discount coupons & flash sales |
| Occasional Buyers | 28% | Limited-time discounts, retargeting ads |
| High Spenders | 25% | VIP programs, early access, personalized messaging |
| Loyal Customers | 19% | Referral rewards, surprise gifts |

---

## 💡 Key Learnings

- Building an end-to-end AI-powered Flask analytics application
- Preparing and scaling numerical data for unsupervised machine learning
- Implementing and evaluating K-Means clustering with Silhouette Score and the Elbow Method
- Applying PCA for dimensionality reduction and cluster visualization
- Translating clustering output into business-actionable customer segments
- Designing an accessible, in-memory data workflow without a persistent database

---

## 🔮 Future Improvements

- Integration of additional ML techniques (DBSCAN, Hierarchical Clustering)
- Database connectivity to store user uploads and results
- Real-time integration with e-commerce platforms
- Mobile-friendly, fully responsive UI
- Downloadable PDF report with summary charts and insights

---

## 🤝 Contributing

Contributions, issues, and feature suggestions are welcome. Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Nasir Husain Tamanne**

A portfolio project demonstrating practical data analysis, machine learning, visualization, and full-stack Flask application development skills for data analyst, data science, and AI-focused roles.
