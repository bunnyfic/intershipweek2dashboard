import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="EDA Analytics Dashboard",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #0e0e0e;
    color: white;
}

.stApp {
    background-color: #0e0e0e;
}

h1, h2, h3, h4 {
    color: #d4af37;
}

[data-testid="metric-container"] {
    background-color: #161616;
    border: 1px solid #d4af37;
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------

df = pd.read_excel("cleanEDAdata.xlsx")

# ---------------- DATE HANDLING ----------------

df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.month_name()

# ---------------- SIDEBAR FILTER ----------------

# ---------------- SIDEBAR FILTER ----------------

st.sidebar.header("Filters")

# Date range slider

min_date = df['Date'].min()
max_date = df['Date'].max()

date_range = st.sidebar.slider(
    "Select Date Range",
    min_value=min_date.to_pydatetime(),
    max_value=max_date.to_pydatetime(),
    value=(
        min_date.to_pydatetime(),
        max_date.to_pydatetime()
    ),
    format="DD/MM/YYYY"
)

# Filter dataframe based on slider

filtered_df = df[
    (df['Date'] >= pd.to_datetime(date_range[0])) &
    (df['Date'] <= pd.to_datetime(date_range[1]))
]

# ---------------- TITLE ----------------

st.markdown(
    "<h1 style='text-align:center;'>ANALYTICS DASHBOARD</h1>",
    unsafe_allow_html=True
)

st.markdown("##")

# ---------------- KPI SECTION ----------------

total_revenue = filtered_df['TotalPrice'].sum()
total_orders = filtered_df['OrderID'].nunique()
avg_order = filtered_df['TotalPrice'].mean()
top_product = filtered_df['Product'].mode()[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Avg Order Value", f"${avg_order:.2f}")
col4.metric("Top Product", top_product)

st.markdown("##")

# ---------------- ROW 1 ----------------

col1, col2 = st.columns([2,1])

with col1:

    monthly_sales = filtered_df.groupby(
        filtered_df['Date'].dt.month_name()
    )['TotalPrice'].sum().reset_index()

    fig = px.line(
        monthly_sales,
        x='Date',
        y='TotalPrice',
        markers=True,
        title="Monthly Revenue Trend"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0e0e0e",
        plot_bgcolor="#0e0e0e"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    referral = filtered_df['ReferralSource'].value_counts().reset_index()

    fig2 = px.pie(
        referral,
        names='ReferralSource',
        values='count',
        title="Referral Sources"
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0e0e0e"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------- ROW 2 ----------------

col3, col4 = st.columns(2)

with col3:

    product_sales = filtered_df.groupby('Product')['TotalPrice'].sum().reset_index()

    fig3 = px.bar(
        product_sales,
        x='Product',
        y='TotalPrice',
        title="Product-wise Revenue",
        color='Product'
    )

    fig3.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0e0e0e",
        plot_bgcolor="#0e0e0e"
    )

    st.plotly_chart(fig3, use_container_width=True)

with col4:

    payment = filtered_df['PaymentMethod'].value_counts().reset_index()

    fig4 = px.bar(
        payment,
        x='PaymentMethod',
        y='count',
        title="Payment Method Usage",
        color='PaymentMethod'
    )

    fig4.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0e0e0e",
        plot_bgcolor="#0e0e0e"
    )

    st.plotly_chart(fig4, use_container_width=True)

# ---------------- ROW 3 ----------------

col5, col6 = st.columns(2)

with col5:

    order_status = filtered_df['OrderStatus'].value_counts().reset_index()

    fig5 = px.bar(
        order_status,
        x='OrderStatus',
        y='count',
        title="Order Status Analysis",
        color='OrderStatus'
    )

    fig5.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0e0e0e",
        plot_bgcolor="#0e0e0e"
    )

    st.plotly_chart(fig5, use_container_width=True)

with col6:

    st.subheader("Correlation Heatmap")

    numeric_df = filtered_df.select_dtypes(include=['int64','float64'])

    corr = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(6,4))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    "<center>Built with Streamlit | EDA Internship Project</center>",
    unsafe_allow_html=True
)