
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Real-World Data Cleaning Pipeline",
    layout="wide"
)

st.title("Real-World Data Cleaning Pipeline")
st.write("Upload a CSV file to clean data, analyze missing values, and download the cleaned dataset.")

uploaded_file = st.file_uploader(
    "Upload NYC Airbnb Dataset",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Unable to read the file: {e}")
        st.stop()

    df_clean = df.copy()
    original_rows = len(df)
    missing_before = int(df.isnull().sum().sum())

    for column in ["name", "host_name"]:
        if column in df_clean.columns:
            df_clean[column] = df_clean[column].fillna("Unknown")

    if "reviews_per_month" in df_clean.columns:
        df_clean["reviews_per_month"] = pd.to_numeric(
            df_clean["reviews_per_month"], errors="coerce"
        ).fillna(0)

    invalid_prices = 0

    if "price" in df_clean.columns:
        df_clean["price"] = pd.to_numeric(
            df_clean["price"], errors="coerce"
        )
        invalid_mask = df_clean["price"].isna() | (df_clean["price"] <= 0)
        invalid_prices = int(invalid_mask.sum())
        df_clean = df_clean.loc[~invalid_mask].copy()

        q1 = df_clean["price"].quantile(0.25)
        q3 = df_clean["price"].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        df_clean["price_outlier"] = (
            (df_clean["price"] < lower) |
            (df_clean["price"] > upper)
        )

    if "last_review" in df_clean.columns:
        df_clean["last_review"] = pd.to_datetime(
            df_clean["last_review"], errors="coerce"
        )

    st.success("Data cleaning completed!")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Original Rows", original_rows)
    col2.metric("Cleaned Rows", len(df_clean))
    col3.metric("Missing Values Before", missing_before)
    col4.metric("Invalid Prices Removed", invalid_prices)

    st.subheader("Cleaned Dataset Preview")
    st.dataframe(df_clean.head(20), use_container_width=True)

    st.subheader("Data Quality Report")

    report = pd.DataFrame({
        "Metric": [
            "Original Rows",
            "Cleaned Rows",
            "Original Columns",
            "Cleaned Columns",
            "Missing Values Before",
            "Missing Values After",
            "Duplicate Rows",
            "Invalid Prices Removed"
        ],
        "Value": [
            original_rows,
            len(df_clean),
            len(df.columns),
            len(df_clean.columns),
            missing_before,
            int(df_clean.isnull().sum().sum()),
            int(df_clean.duplicated().sum()),
            invalid_prices
        ]
    })

    st.dataframe(report, use_container_width=True)

    st.subheader("Visualizations")

    if "price" in df_clean.columns:
        fig, ax = plt.subplots()
        ax.hist(df_clean["price"], bins=30)
        ax.set_title("Price Distribution")
        ax.set_xlabel("Price")
        ax.set_ylabel("Number of Listings")
        st.pyplot(fig)
        plt.close(fig)

    if "room_type" in df_clean.columns:
        st.write("Room Type Distribution")
        st.bar_chart(df_clean["room_type"].value_counts())

    csv_data = df_clean.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Cleaned Dataset",
        data=csv_data,
        file_name="cleaned_airbnb_data.csv",
        mime="text/csv"
    )

    report_data = report.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Data Quality Report",
        data=report_data,
        file_name="data_quality_report.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload the AB_NYC_2019.csv dataset to start.")

