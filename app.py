import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def upload_and_visualize():
    st.title("CSV File Uploader and Data Visualization")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Check if a file is uploaded
    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)

        # Display CSV file content using pandas
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(df)

        # Data visualization using Altair
        st.subheader("Data Visualization")
        if not df.empty:
            # Assuming the CSV file has at least two numeric columns
            x_column = st.selectbox("Select X-axis column", df.select_dtypes(include=np.number).columns)
            y_column = st.selectbox("Select Y-axis column", df.select_dtypes(include=np.number).columns)
            color_column = st.selectbox("Select Color column", df.select_dtypes(include=np.number).columns)
            size_column = st.selectbox("Select Size column", df.select_dtypes(include=np.number).columns)

            scatter_chart = (
                alt.Chart(df)
                .mark_circle()
                .encode(x=x_column, y=y_column, color=color_column, size=size_column, tooltip=list(df.columns))
                .interactive()
            )

            st.write("Scatter Plot:")
            st.altair_chart(scatter_chart, use_container_width=True)
    else:
        st.write("Please upload a CSV file.")

def main():
    upload_and_visualize()

if __name__ == "__main__":
    main()
