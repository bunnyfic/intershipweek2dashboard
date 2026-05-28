# week 2 internship project
app link
https://intershipweek2dashboard-ey2hertfcxqwxbtpovx7yp.streamlit.app/

E-Commerce Exploratory Data Analysis (EDA) Project
Overview

This project focuses on performing Exploratory Data Analysis (EDA) on an E-Commerce dataset to uncover meaningful business insights, identify trends, detect anomalies, and build an interactive analytics dashboard.

The project demonstrates the complete EDA workflow including:

Data Cleaning
Data Transformation
Univariate Analysis
Bivariate Analysis
Outlier Detection
Correlation Analysis
Business Insight Generation
Interactive Dashboard Development using Streamlit
Objective

The main objective of this project is to analyze customer transactions and extract actionable business insights that can support better decision-making.

Key business questions explored:

Which products generate the highest revenue?
Which payment methods are most preferred?
What are the monthly sales trends?
Which referral sources bring the most customers?
Are there any outliers in transaction values?
How are numerical variables correlated?
Dataset Information

The dataset contains 1200 transaction records and 14 columns.

Features Included
Column Name	Description
OrderID	Unique order identifier
Date	Transaction date
CustomerID	Unique customer identifier
Product	Product purchased
Quantity	Quantity ordered
UnitPrice	Price per unit
ShippingAddress	Customer shipping location
PaymentMethod	Mode of payment
OrderStatus	Current order status
TrackingNumber	Shipment tracking ID
ItemsInCart	Number of items added
CouponCode	Applied discount coupon
ReferralSource	Customer acquisition source
TotalPrice	Final transaction value
Technologies Used
Programming & Libraries
Python
Pandas
NumPy
Matplotlib
Seaborn
Plotly
Streamlit
Tools
Jupyter Notebook
Streamlit Cloud
GitHub
Project Workflow
1. Data Cleaning

The dataset was cleaned and transformed before analysis.

Tasks Performed
Converted Date column into datetime format
Checked missing values
Verified data types
Removed inconsistencies
Created derived columns such as Month
Exploratory Data Analysis
Univariate Analysis

Performed distribution analysis on numerical variables.

Visualizations Used
Histogram
KDE Plot
Boxplot
Key Findings
TotalPrice distribution was positively skewed
Most transactions occurred in lower price ranges
Presence of high-value outliers was detected
Outlier Analysis

Outliers were analyzed using:

Boxplots
IQR Method
Insight

Certain products showed extreme transaction values which may indicate:

Premium purchases
Bulk orders
Unusual customer behavior
Bivariate Analysis

Relationships between variables were explored.

Visualizations Used
Correlation Heatmap
Revenue Trend Charts
Product-wise Revenue Analysis
Key Findings
Strong relationship observed between Quantity and TotalPrice
Product categories contributed differently to revenue generation
Business Insights
Product Analysis
Printer generated the highest number of orders
Tablets and Chairs also showed strong demand
Payment Analysis
Online payments were the most preferred payment method
Gift cards showed comparatively lower usage
Referral Source Analysis
Instagram generated the highest customer referrals
Social media channels played a major role in customer acquisition
Order Status Analysis
Cancelled and Returned orders formed a noticeable percentage
Indicates potential operational or customer satisfaction issues
Revenue Trend Analysis
Revenue fluctuated across months
Certain months experienced higher transaction volumes
Interactive Dashboard

An interactive dashboard was built using Streamlit.

Dashboard Features
Interactive Date Range Slider
KPI Cards
Monthly Revenue Trend
Product-wise Revenue Analysis
Referral Source Distribution
Payment Method Analysis
Order Status Visualization
Correlation Heatmap
Dashboard Preview

The dashboard includes:

Dark modern UI
Gold-accented KPI cards
Interactive Plotly charts
Dynamic filtering system
Key Learnings

Through this project, the following concepts were strengthened:

Data preprocessing
Exploratory data analysis
Statistical interpretation
Data visualization
Dashboard development
Business storytelling with data
Future Improvements

Possible enhancements include:

Predictive Analytics
Customer Segmentation
Sales Forecasting
Deployment with cloud database integration
Advanced Streamlit animations and responsiveness
How to Run the Project
Clone Repository
git clone <your-github-repo-link>
Install Dependencies
pip install -r requirements.txt
Run Streamlit App
streamlit run app.py
Project Structure
├── app.py
├── EDA_Final_Dataset.xlsx
├── requirements.txt
├── README.md
└── notebooks/
Conclusion

This project demonstrates how exploratory data analysis can transform raw transactional data into actionable business insights.

By combining:

statistical analysis,
data visualization,
and interactive dashboarding,

the project provides a complete end-to-end EDA workflow suitable for real-world analytics applications.
