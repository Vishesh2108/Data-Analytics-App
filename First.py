# import
import streamlit as st
import pandas as pd
import seaborn as sns

# Title and subholder

st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

# Upload Dataset

upload = st.file_uploader("Upload Your Dataset (In CSV Form)")
if upload is not None:
    data = pd.read_csv(upload)
    
# Show DataSet
if upload is not None:
    if st.checkbox("Previe Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
# Check DataType of Each Column

if upload is not None:
    if st.checkbox("DataType of Each Columns"):
        st.text("DataTypes")
        st.write(data.dtypes)
   
# Find Shape of Our Dataset (Number of Rows And Number of Columns)

if upload is not None:
    data_shape = st.radio("What Dimension Do You Want to Check?",('Rows','Columns'))
    
    if data_shape=='Rows':
        st.text('Number of Rows')
        st.write(data.shape[0])
    
    if data_shape=='Columns':
        st.text('Number of Rows')
        st.write(data.shape[1])
        
# Find Null Values in The Dataset

st.set_option('deprecation.showPyplotGlobalUse', False)

if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
        else:
            st.success("Congratulations!!,No Missing Values")

# Find Duplicate Values in the dataset

if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Data Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?"
                         ,("Select One","Yes","NO"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removes")
        if dup=="No":
            st.text("Okay No Problem")
            
# Get Overall Statistics

if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include='all'))

# About Sections
if upload is not None:
    if st.button("About App"):
        st.success("Built With Streamlit Thanks For Using App ")
       
     

    

    