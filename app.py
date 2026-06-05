import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# STYLING
# ==========================================
st.markdown("""
    <style>
    .main { padding: 0rem 1rem; }
    .metric-card { 
        background-color: #f0f2f6; 
        padding: 1rem; 
        border-radius: 0.5rem;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# LOAD DATA
# ==========================================
@st.cache_data
def load_data():
    df = pd.read_csv('netflix_titles.csv')
    return df

df = load_data()

# ==========================================
# DATA PREPROCESSING
# ==========================================
# Handle missing values
df['cast'] = df['cast'].fillna('Unknown')
df['director'] = df['director'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

# Extract first country for country analysis
df['first_country'] = df['country'].str.split(',').str[0]

# Extract genres (first genre from listed_in)
df['primary_genre'] = df['listed_in'].str.split(',').str[0]

# Extract year from release_year
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

# Parse date_added
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

# ==========================================
# HEADER
# ==========================================
st.title("🎬 Netflix Analytics Dashboard")
st.markdown("---")

# ==========================================
# SIDEBAR - FILTERS
# ==========================================
st.sidebar.title("🔍 Filters")

# Content Type Filter
content_type = st.sidebar.multiselect(
    "Select Content Type:",
    options=df['type'].unique(),
    default=df['type'].unique()
)

# Rating Filter
ratings = st.sidebar.multiselect(
    "Select Ratings:",
    options=sorted(df['rating'].unique()),
    default=sorted(df['rating'].unique())
)

# Release Year Range
year_range = st.sidebar.slider(
    "Select Release Year Range:",
    min_value=int(df['release_year'].min()),
    max_value=int(df['release_year'].max()),
    value=(int(df['release_year'].min()), int(df['release_year'].max()))
)

# Apply Filters
filtered_df = df[
    (df['type'].isin(content_type)) &
    (df['rating'].isin(ratings)) &
    (df['release_year'] >= year_range[0]) &
    (df['release_year'] <= year_range[1])
]

# ==========================================
# KEY METRICS
# ==========================================
st.subheader("📊 Key Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="Total Content",
        value=len(filtered_df),
        delta=f"of {len(df)} total"
    )

with col2:
    movies = len(filtered_df[filtered_df['type'] == 'Movie'])
    st.metric(
        label="Movies",
        value=movies
    )

with col3:
    tv_shows = len(filtered_df[filtered_df['type'] == 'TV Show'])
    st.metric(
        label="TV Shows",
        value=tv_shows
    )

with col4:
    avg_year = int(filtered_df['release_year'].mean())
    st.metric(
        label="Avg Release Year",
        value=avg_year
    )

with col5:
    countries = filtered_df['first_country'].nunique()
    st.metric(
        label="Countries",
        value=countries
    )

st.markdown("---")

# ==========================================
# VISUALIZATIONS - ROW 1
# ==========================================
st.subheader("📈 Content Distribution")

col1, col2 = st.columns(2)

# Movies vs TV Shows
with col1:
    fig, ax = plt.subplots(figsize=(8, 5))
    type_counts = filtered_df['type'].value_counts()
    colors = ['#E50914', '#221f1f']
    ax.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%',
           colors=colors, startangle=90, textprops={'fontsize': 12, 'weight': 'bold'})
    ax.set_title("Movies vs TV Shows Distribution", fontsize=14, fontweight='bold', pad=20)
    st.pyplot(fig)
    plt.close()

# Top 10 Ratings
with col2:
    fig, ax = plt.subplots(figsize=(8, 5))
    rating_counts = filtered_df['rating'].value_counts().head(10)
    sns.barplot(x=rating_counts.values, y=rating_counts.index, palette='coolwarm', ax=ax)
    ax.set_xlabel("Count", fontsize=12, fontweight='bold')
    ax.set_ylabel("Rating", fontsize=12, fontweight='bold')
    ax.set_title("Top 10 Content Ratings", fontsize=14, fontweight='bold', pad=20)
    st.pyplot(fig)
    plt.close()

st.markdown("---")

# ==========================================
# VISUALIZATIONS - ROW 2
# ==========================================
col1, col2 = st.columns(2)

# Release Year Trend
with col1:
    fig, ax = plt.subplots(figsize=(10, 5))
    year_counts = filtered_df['release_year'].value_counts().sort_index()
    ax.plot(year_counts.index, year_counts.values, marker='o', linewidth=2, 
            markersize=6, color='#E50914')
    ax.fill_between(year_counts.index, year_counts.values, alpha=0.3, color='#E50914')
    ax.set_xlabel("Release Year", fontsize=12, fontweight='bold')
    ax.set_ylabel("Number of Content", fontsize=12, fontweight='bold')
    ax.set_title("Content Released by Year", fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close()

# Top 10 Countries
with col2:
    fig, ax = plt.subplots(figsize=(10, 5))
    country_counts = filtered_df['first_country'].value_counts().head(10)
    sns.barplot(x=country_counts.values, y=country_counts.index, palette='viridis', ax=ax)
    ax.set_xlabel("Count", fontsize=12, fontweight='bold')
    ax.set_ylabel("Country", fontsize=12, fontweight='bold')
    ax.set_title("Top 10 Countries with Most Content", fontsize=14, fontweight='bold', pad=20)
    st.pyplot(fig)
    plt.close()

st.markdown("---")

# ==========================================
# VISUALIZATIONS - ROW 3
# ==========================================
col1, col2 = st.columns(2)

# Top 10 Genres
with col1:
    fig, ax = plt.subplots(figsize=(10, 5))
    genre_counts = filtered_df['primary_genre'].value_counts().head(10)
    sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='mako', ax=ax)
    ax.set_xlabel("Count", fontsize=12, fontweight='bold')
    ax.set_ylabel("Genre", fontsize=12, fontweight='bold')
    ax.set_title("Top 10 Content Genres", fontsize=14, fontweight='bold', pad=20)
    st.pyplot(fig)
    plt.close()

# Content Added by Year
with col2:
    fig, ax = plt.subplots(figsize=(10, 5))
    added_by_year = filtered_df['year_added'].value_counts().sort_index().dropna()
    ax.bar(added_by_year.index, added_by_year.values, color='#E50914', alpha=0.8, edgecolor='black')
    ax.set_xlabel("Year Added to Netflix", fontsize=12, fontweight='bold')
    ax.set_ylabel("Number of Content", fontsize=12, fontweight='bold')
    ax.set_title("Content Added to Netflix by Year", fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, axis='y')
    st.pyplot(fig)
    plt.close()

st.markdown("---")

# ==========================================
# DATA TABLES SECTION
# ==========================================
st.subheader("📋 Data Tables")

tab1, tab2, tab3, tab4 = st.tabs(["Full Dataset", "Top Directors", "Top Cast Members", "Dataset Info"])

with tab1:
    st.write(f"**Showing {len(filtered_df)} items**")
    st.dataframe(filtered_df, use_container_width=True)

with tab2:
    # Top Directors
    director_counts = filtered_df[filtered_df['director'] != 'Unknown']['director'].value_counts().head(10)
    st.write("**Top 10 Directors**")
    st.dataframe(director_counts, column_config={"value": "Count"}, use_container_width=True)

with tab3:
    # Top Cast Members
    from collections import Counter
    all_cast = []
    for cast_str in filtered_df[filtered_df['cast'] != 'Unknown']['cast']:
        cast_list = [c.strip() for c in str(cast_str).split(',')]
        all_cast.extend(cast_list)
    
    if all_cast:
        cast_counts = Counter(all_cast).most_common(10)
        cast_df = pd.DataFrame(cast_counts, columns=['Actor', 'Count'])
        st.dataframe(cast_df, use_container_width=True)
    else:
        st.write("No cast information available for selected filters.")

with tab4:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Dataset Shape:**")
        st.write(f"Rows: {filtered_df.shape[0]}")
        st.write(f"Columns: {filtered_df.shape[1]}")
    
    with col2:
        st.write("**Missing Values:**")
        missing = filtered_df.isnull().sum()
        st.write(missing[missing > 0])
    
    with col3:
        st.write("**Content Types:**")
        st.write(filtered_df['type'].value_counts())

st.markdown("---")

# ==========================================
# SEARCH & DETAILS
# ==========================================
st.subheader("🔎 Search Content")

search_title = st.text_input("Search by title:", placeholder="Enter title name...")

if search_title:
    search_results = filtered_df[filtered_df['title'].str.contains(search_title, case=False, na=False)]
    st.write(f"**Found {len(search_results)} results:**")
    if len(search_results) > 0:
        st.dataframe(search_results[['title', 'type', 'director', 'release_year', 'rating', 'listed_in']], 
                    use_container_width=True)
    else:
        st.write("No results found.")

st.markdown("---")

# Footer
st.markdown("""
    <div style='text-align: center; color: gray; margin-top: 3rem;'>
        <p>Netflix Analytics Dashboard | Data Source: netflix_titles.csv</p>
    </div>
    """, unsafe_allow_html=True)