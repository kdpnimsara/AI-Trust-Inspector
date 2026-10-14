import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Trust Inspector",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Trust Inspector")
st.subheader("AI Model & Dataset Quality Dashboard")

st.write(
    "Upload a CSV dataset to inspect its quality "
    "and identify potential data problems."
)

uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        st.success("Dataset uploaded successfully!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Rows", data.shape[0])

        with col2:
            st.metric("Total Columns", data.shape[1])

        with col3:
            st.metric("Duplicate Rows", int(data.duplicated().sum()))

        st.header("📋 Dataset Preview")
        st.dataframe(data, use_container_width=True)

        st.header("🔎 Missing Values")

        missing = data.isnull().sum()

        missing_report = pd.DataFrame({
            "Column": data.columns,
            "Missing Values": missing.values,
            "Missing Percentage": (
                data.isnull().mean().values * 100
            ).round(2)
        })

        st.dataframe(
            missing_report,
            use_container_width=True
        )

        st.header("🧾 Column Data Types")

        type_report = pd.DataFrame({
            "Column": data.columns,
            "Data Type": data.dtypes.astype(str).values
        })

        st.dataframe(
            type_report,
            use_container_width=True
        )

        st.header("📊 Dataset Quality Summary")

        total_missing = int(data.isnull().sum().sum())
        total_duplicates = int(data.duplicated().sum())

        if total_missing == 0 and total_duplicates == 0:
            st.success("No missing values or duplicate rows found.")
        else:
            if total_missing > 0:
                st.warning(
                    f"Found {total_missing} missing values."
                )

            if total_duplicates > 0:
                st.warning(
                    f"Found {total_duplicates} duplicate rows."
                )

        st.download_button(
            "Download Missing Values Report",
            data=missing_report.to_csv(index=False),
            file_name="missing_values_report.csv",
            mime="text/csv"
        )

    except Exception as error:
        st.error(f"Could not inspect this dataset: {error}")

else:
    st.info("Please upload a CSV file to begin the inspection.")