import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Settings
st.set_page_config(
    page_title="Netflix Dashboard",
    layout="wide"
)

# Title
st.title("🎬 Netflix Dashboard")

# Upload CSV File
uploaded_file = st.file_uploader(
    "Upload Netflix CSV File",
    type=["csv"]
)

# If file uploaded
if uploaded_file is not None:

    # Read Dataset
    df = pd.read_csv('netflix_titels')

    # -----------------------------------
    # Dataset Preview
    # -----------------------------------

    st.subheader("📄 Dataset Preview")

    st.write(df.head())

    # -----------------------------------
    # Dataset Information
    # -----------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Rows and Columns")
        st.write(df.shape)

    with col2:
        st.subheader("Missing Values")
        st.write(df.isnull().sum())

    # -----------------------------------
    # Movies vs TV Shows
    # -----------------------------------

    st.subheader("🎥 Movies vs TV Shows")

    fig1, ax1 = plt.subplots(figsize=(6,4))

    sns.countplot(
        x='type',
        data=df,
        ax=ax1
    )

    ax1.set_title("Movies vs TV Shows")

    st.pyplot(fig1)

    # -----------------------------------
    # Most Common Ratings
    # -----------------------------------

    st.subheader("⭐ Most Common Ratings")

    fig2, ax2 = plt.subplots(figsize=(10,5))

    sns.countplot(
        y='rating',
        data=df,
        order=df['rating'].value_counts().index,
        ax=ax2
    )

    ax2.set_title("Most Common Ratings")

    st.pyplot(fig2)

    # -----------------------------------
    # Top 10 Countries
    # -----------------------------------

    st.subheader("🌍 Top 10 Countries")

    fig3, ax3 = plt.subplots(figsize=(10,5))

    df['country'].value_counts().head(10).plot(
        kind='bar',
        ax=ax3
    )

    ax3.set_title("Top 10 Countries")

    st.pyplot(fig3)

    # -----------------------------------
    # Release Year Trend
    # -----------------------------------

    st.subheader("📅 Release Year Trend")

    fig4, ax4 = plt.subplots(figsize=(15,5))

    sns.countplot(
        x='release_year',
        data=df,
        ax=ax4
    )

    plt.xticks(rotation=90)

    ax4.set_title("Release Year Trend")

    st.pyplot(fig4)

    # -----------------------------------
    # Top 10 Genres
    # -----------------------------------

    st.subheader("🎭 Top 10 Genres")

    fig5, ax5 = plt.subplots(figsize=(12,5))

    df['listed_in'].value_counts().head(10).plot(
        kind='bar',
        ax=ax5
    )

    ax5.set_title("Top Genres")

    st.pyplot(fig5)

    # -----------------------------------
    # Show Raw Data
    # -----------------------------------

    if st.checkbox("Show Full Dataset"):
        st.write(df)

else:
    st.warning("Please upload a CSV file.")