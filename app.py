import streamlit as st
import pandas as pd


st.title('DataDive')
st.write("""
###### Dive into the basic insights of your data in a single click!
""")
st.write("""## ![alt-text](https://cdn-icons-png.flaticon.com/128/14036/14036432.png) Data Enthusiast""")
st.write("""### Let's see what you've got today!""")
st.write("""###### *Navigate to data sidebar on the left to upload your dataset* """)

with st.sidebar:
        st.title("Data Sidebar")
        csv_file=st.file_uploader(label='# Upload Your Dataset Here (in .csv)', type=['csv'])


if csv_file is not None:
    df=pd.read_csv(csv_file)
    st.write("#### Leading 5 Rows of the Dataset:", df.head())
    st.write("#### Shape of the Dataset:", df.shape)
    st.write("#### Columns of Dataset:",df.columns)
    st.write("#### Data Types of Columns:",df.dtypes)
    st.write('#### Data Description:',df.describe())
