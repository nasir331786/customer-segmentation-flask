# ClusterAI — AI-Powered Customer Segmentation

An AI-driven web application that segments e-commerce customers using K-Means clustering, and presents the results through an interactive Flask dashboard with rich visual analytics.

## Overview

ClusterAI analyzes customer attributes such as age, income, spending score, and purchase frequency to automatically identify distinct customer groups — Budget Shoppers, High Spenders, Occasional Buyers, and Loyal Customers.

The goal is to give businesses a data-driven decision-support tool that turns raw customer data into actionable insights via visual analytics, clustering reports, and downloadable summaries, enabling more effective marketing, retention, and resource allocation.

## Features

- Upload CSV files containing customer data through a responsive web interface
- Clean and preprocess data, including handling of missing values and feature scaling
- Segment customers using K-Means clustering
- Evaluate cluster quality with the Silhouette Score
- Determine the optimal number of clusters using the Elbow Method
- Label clusters with descriptive, business-friendly names (e.g. Budget Shoppers, High Spenders)
- Visualize results with pie charts, bar charts, pair plots, and 2D/3D PCA scatterplots
- Preview labeled customer records directly in the dashboard
- Download the full cluster-labeled dataset as a CSV file
- View segment-specific marketing tips and engagement strategies
- Toggle "Show Technical Details" for advanced clustering diagnostics

## Tech Stack

**Frontend**
- HTML
- CSS / Tailwind CSS
- Lottie Animations

**Backend**
- Python
- Flask

**Data Processing & Machine Learning**
- Pandas
- Scikit-learn (K-Means, StandardScaler, PCA, Silhouette Score)

**Visualization**
- Matplotlib
- Seaborn
- mpl_toolkits.mplot3d

**Storage**
- OS module for file/path management
- CSV files for input and labeled output

**Utilities**
- MarkupSafe for safe HTML rendering in templates

## Project Modules

| Module | Function | Key Tools |
|---|---|---|
| User Interface | Web-based interaction and file upload | HTML, CSS, Tailwind, Lottie, Flask Templates |
| Data Preprocessing | Cleans and scales numeric data | Python, Pandas, StandardScaler |
| Clustering Analysis | Groups customers and evaluates clusters | KMeans, Silhouette Score, Elbow Method |
| Visualization & Reporting | Generates charts, tables, and downloadable CSV | Matplotlib, Seaborn, PCA, Flask, CSV |

## Project Structure

```text
clusterai-customer-segmentation/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    └── uploads/              # Generated files; excluded from Git
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nasir331786/customer-segmentation-flask.git
   cd customer-segmentation-flask
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS/Linux:

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

   ```text
   http://127.0.0.1:5000
   ```

## Usage

1. Open the application in a browser.
2. Upload a CSV file containing customer data (e.g. Customer ID, Age, Income, Spending Score, Purchase Frequency).
3. Click **Analyze Data** to run the clustering pipeline.
4. Review the segmentation dashboard: pie/bar charts, segment descriptions, and marketing tips.
5. Expand **Show Technical Details** for the Elbow plot, pair plot, and PCA 2D/3D visualizations.
6. Download the full labeled CSV for further analysis.

## Output

- Elbow Method plot for optimal cluster selection
- Cluster pair plot showing feature separation
- PCA 2D and 3D cluster visualizations
- Customer distribution pie chart and count bar chart
- Segment-specific marketing recommendations
- Downloadable cluster-labeled customer CSV

## Key Learnings

- Building an end-to-end AI-powered Flask analytics application
- Preparing and scaling numerical data for unsupervised machine learning
- Implementing and evaluating K-Means clustering with Silhouette Score and the Elbow Method
- Applying PCA for dimensionality reduction and cluster visualization
- Translating clustering output into business-actionable customer segments
- Designing an accessible, in-memory data workflow without a persistent database

## Future Improvements

- Integration of additional ML techniques (DBSCAN, Hierarchical Clustering, SVM, Logistic Regression)
- Database connectivity to store user uploads and results
- Real-time integration with e-commerce platforms
- Mobile-friendly, fully responsive UI
- Downloadable PDF report with summary charts and insights

## Author

**Nasir Husain Tamanne**

A portfolio project demonstrating practical data analysis, machine learning, visualization, and full-stack Flask application development skills for data analyst, data science, and AI-focused roles.
