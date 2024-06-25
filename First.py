import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Title and subheader
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

# Upload Dataset
upload = st.file_uploader("Upload Your Dataset (In CSV Form)")
if upload is not None:
    data = pd.read_csv(upload)

    # Show Dataset
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

    # Check DataType of Each Column
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)

    # Find Shape of Our Dataset (Number of Rows And Number of Columns)
    data_shape = st.radio("What Dimension Do You Want to Check?", ('Rows', 'Columns'))

    if data_shape == 'Rows':
        st.text('Number of Rows')
        st.write(data.shape[0])

    if data_shape == 'Columns':
        st.text('Number of Columns')
        st.write(data.shape[1])

    # Find Null Values in The Dataset
    test = data.isnull().values.any()
    if test:
        if st.checkbox("Null Values in the dataset"):
            fig, ax = plt.subplots()
            sns.heatmap(data.isnull(), ax=ax)
            st.pyplot(fig)
        else:
            st.success("Congratulations!!, No Missing Values")

    # Find Duplicate Values in the dataset
    test = data.duplicated().any()
    if test:
        st.warning("This Data Contains Some Duplicate Values")
        dup = st.selectbox("Do You Want to Remove Duplicate Values?", ("Select One", "Yes", "No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup == "No":
            st.text("Okay No Problem")

    # Get Overall Statistics
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include='all'))

    # Data Filtering
    st.sidebar.header("Filter Data")
    for col in data.select_dtypes(include=['object']).columns:
        unique_values = data[col].unique()
        selected_values = st.sidebar.multiselect(f"Filter {col}", unique_values, default=unique_values)
        data = data[data[col].isin(selected_values)]

    # Correlation Matrix
    if st.checkbox("Correlation Matrix"):
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    # Scatter Plot
    if st.checkbox("Scatter Plot"):
        x_axis = st.selectbox("Select X-axis", data.columns)
        y_axis = st.selectbox("Select Y-axis", data.columns)
        fig = px.scatter(data, x=x_axis, y=y_axis)
        st.plotly_chart(fig)

    # Histogram
    if st.checkbox("Histogram"):
        column = st.selectbox("Select Column", data.columns)
        fig = px.histogram(data, x=column)
        st.plotly_chart(fig)

    # Pair Plot
    if st.checkbox("Pair Plot"):
        columns_to_plot = st.multiselect("Select Columns to Include in Pair Plot", data.columns)
        if len(columns_to_plot) > 1:
            fig = sns.pairplot(data[columns_to_plot])
            st.pyplot(fig)
        else:
            st.warning("Please select at least two columns for the pair plot.")

    # Box Plot
    if st.checkbox("Box Plot"):
        column = st.selectbox("Select Column for Box Plot", data.columns)
        fig = px.box(data, y=column)
        st.plotly_chart(fig)

    # Custom Aggregations
    if st.checkbox("Custom Aggregations"):
        group_by_col = st.selectbox("Select Column to Group By", data.columns)
        agg_col = st.selectbox("Select Column to Aggregate", data.columns)
        agg_func = st.selectbox("Select Aggregation Function", ['mean', 'sum', 'count', 'min', 'max'])
        agg_data = data.groupby(group_by_col)[agg_col].agg(agg_func).reset_index()
        st.write(agg_data)

    # Data Export
    if st.checkbox("Download Modified Data"):
        st.download_button("Download Data as CSV", data.to_csv(index=False).encode('utf-8'), "modified_data.csv")

    # About Section
    if st.button("About App"):
        st.markdown("""
            ### About This App
            - **App Name:** Data Analysis App
            - **Built with:** Streamlit, Pandas, Seaborn, Plotly, Matplotlib
            - **Purpose:** A simple app to analyze datasets by visualizing and summarizing the data.
            - **Developer:** Vishesh Devganiya
            - **Contact:** [visheshdsd234@gmail.com](mailto:visheshdsd234@gmail.com)

            Thank you for using the app! Feel free to reach out if you have any questions or feedback.
        """)
