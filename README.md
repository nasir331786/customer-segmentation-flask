# Customer Segmentation with Flask

A web-based customer segmentation application that lets users upload a CSV file, automatically cluster numeric customer data using K-Means, and explore the results through downloadable outputs and visual analytics.

## Overview

Customer segmentation helps organizations identify meaningful groups within their customer base and support targeted marketing, retention, and business decisions.

This application provides an accessible workflow for uploading a CSV dataset, applying K-Means clustering to numeric fields, reviewing clustering quality, and visualizing customer groups in multiple formats.

## Features

- Upload and analyze CSV datasets
- Automatically select numeric columns for clustering
- Standardize numeric features using `StandardScaler`
- Segment records using K-Means clustering
- Generate a silhouette score for clustering evaluation
- Create an Elbow Method chart for cluster exploration
- Create a Seaborn pair plot by cluster
- Generate PCA-based 2D and 3D cluster visualizations
- Display customer distribution with pie and bar charts
- Preview the first 10 records from the uploaded dataset
- Download a CSV file containing assigned customer cluster labels

## Tech Stack

- Python
- Flask
- Pandas
- scikit-learn
- Matplotlib
- Seaborn
- HTML/CSS templates

## Project Structure

```text
customer-segmentation-flask/
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
2. Upload a CSV file containing customer data.
3. Ensure the dataset includes numeric columns for clustering.
4. Submit the file for analysis.
5. Review the silhouette score and generated cluster visualizations.
6. Download the labeled CSV output for further analysis.

## Output

The application generates the following analysis outputs:

- Elbow Method chart
- Cluster pair plot
- PCA 2D visualization
- PCA 3D visualization
- Customer distribution pie chart
- Customer count bar chart
- Downloadable labeled customer dataset

## Key Learnings

- Building an end-to-end Flask analytics application
- Preparing numerical data for unsupervised machine learning
- Applying feature scaling with `StandardScaler`
- Implementing K-Means clustering with scikit-learn
- Evaluating clusters using silhouette score and inertia
- Communicating clustering results with PCA and statistical visualizations
- Delivering downloadable analysis outputs in a web application

## Future Improvements

- Allow users to choose the number of clusters dynamically
- Recommend an optimal cluster count using silhouette analysis
- Support categorical features through preprocessing and encoding
- Add dataset validation and richer error messages
- Persist uploaded datasets and analysis history in a database
- Add authentication and user-specific project dashboards
- Deploy the application to a cloud hosting platform

## Author

**Nasir Husain Tamanne**

A portfolio project demonstrating practical data analysis, machine learning, visualization, and Flask application development skills for data analyst, data science, and AI-focused roles.
