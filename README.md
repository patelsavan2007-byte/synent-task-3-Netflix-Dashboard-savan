# Netflix Analytics Dashboard - Streamlit Application

## 📊 Overview
A comprehensive interactive dashboard built with Streamlit to analyze Netflix content data. The dashboard provides rich visualizations and filtering capabilities to explore movies, TV shows, ratings, genres, and more.

## 📸 Dashboard Screenshots & Features

### Screenshot 1️⃣ : Filters & Key Metrics
![Dashboard Filters & Metrics](https://raw.githubusercontent.com/patelsavan2007-byte/synent-task-3-Netflix-Dashboard-savan/main/screenshots/screenshot-1-filters-metrics.png)

**Features Shown:**
- **Left Sidebar Filters** - Interactive controls for:
  - Content Type (Movies/TV Shows)
  - Ratings (TV-MA, TV-14, PG-13, etc.)
  - Release Year Range (1925-2021)
- **Key Metrics Dashboard** - 5 cards displaying:
  - Total Content: 8,806
  - Movies: 6,130
  - TV Shows: 2,676
  - Average Release Year: 2014
  - Countries: 87+

### Screenshot 2️⃣ : Visualizations & Charts
![Dashboard Visualizations](https://raw.githubusercontent.com/patelsavan2007-byte/synent-task-3-Netflix-Dashboard-savan/main/screenshots/screenshot-2-visualizations.png)

**Features Shown:**
- **Movies vs TV Shows Distribution** (Pie Chart)
  - 69.6% Movies
  - 30.4% TV Shows
- **Top 10 Content Ratings** (Bar Chart)
  - TV-MA (Most common)
  - TV-14, TV-PG, R, PG-13, and more
- **Real-time Interactivity**
  - All filters update charts instantly
  - Responsive design scales to screen size

### Screenshot 3️⃣ : Data Tables & Search
![Dashboard Data Tables](https://raw.githubusercontent.com/patelsavan2007-byte/synent-task-3-Netflix-Dashboard-savan/main/screenshots/screenshot-3-data-tables.png)

**Features Shown:**
- **Data Tables Section** with 4 Tabs:
  1. **Full Dataset** - All 8,806 items with columns:
     - show_id, type, title, director, cast, country, date_added, release_year
  2. **Top Directors** - Directors ranked by content count
  3. **Top Cast Members** - Most frequently appearing actors
  4. **Dataset Info** - Statistics and metadata
- **Search Content** Section
  - Real-time title search
  - Instant results display
  - Filter matching rows

## ✨ Features

### 1. **Interactive Filters** (Sidebar)
- Filter by content type (Movies/TV Shows)
- Filter by rating (TV-MA, PG-13, etc.)
- Select release year range
- All metrics update dynamically based on filters

### 2. **Key Metrics Dashboard**
- Total content count
- Movie count
- TV Show count
- Average release year
- Number of countries

### 3. **Visualizations**
- **Movies vs TV Shows** - Pie chart showing distribution
- **Top Ratings** - Bar chart of most common content ratings
- **Release Year Trend** - Line chart showing content released over time
- **Top Countries** - Bar chart of countries with most content
- **Top Genres** - Bar chart of popular genres
- **Content Added by Year** - Bar chart showing when content was added to Netflix

### 4. **Data Tables**
- **Full Dataset** - Complete filtered data with all columns
- **Top Directors** - Directors with most content
- **Top Cast Members** - Most frequently appearing actors
- **Dataset Info** - Shape, missing values, and content type breakdown

### 5. **Search Functionality**
- Search content by title
- Real-time search results
- Quick preview of matching titles

## 📁 Files

```
d:\Projects\SYNENT-DS\TASK-4\
├── app.py                      # Main Streamlit application
├── netflix_titles.csv          # Netflix dataset
├── README.md                   # This file
└── Netflix_EDA_Streamlit_Updated.ipynb  # Original Jupyter notebook
```

## 📋 Dataset Structure

The Netflix dataset contains:
- **show_id** - Unique identifier
- **type** - Movie or TV Show
- **title** - Content title
- **director** - Director(s)
- **cast** - Cast members
- **country** - Production country/countries
- **date_added** - Date added to Netflix
- **release_year** - Original release year
- **rating** - Content rating (PG-13, TV-MA, etc.)
- **duration** - Duration (minutes for movies, seasons for TV shows)
- **listed_in** - Genre(s)
- **description** - Brief content description

## 🚀 Installation & Running

### Prerequisites
```bash
pip install streamlit pandas matplotlib seaborn numpy
```

### Run the Dashboard
```bash
cd d:\Projects\SYNENT-DS\TASK-4
streamlit run app.py
```

The dashboard will open at: **http://localhost:8501**

### Command Options
```bash
# Run on specific port
streamlit run app.py --server.port 8502

# Run in headless mode
streamlit run app.py --headless

# Run with specific logger level
streamlit run app.py --logger.level=error
```

## 📊 Data Processing

The application performs the following data preprocessing:
- Handles missing values with appropriate defaults
- Extracts first country from multi-country entries
- Extracts primary genre from multi-genre listings
- Parses release years and date_added fields
- Computes year_added from date_added column

## 🎨 Dashboard Sections

### Key Metrics Row
Shows 5 main KPIs at a glance

### Visualization Grid (Row 1)
- Movies vs TV Shows distribution (Pie chart)
- Top 10 Ratings (Bar chart)

### Visualization Grid (Row 2)
- Content Released by Year (Line chart with area fill)
- Top 10 Countries (Bar chart)

### Visualization Grid (Row 3)
- Top 10 Genres (Bar chart)
- Content Added to Netflix by Year (Bar chart)

### Data Tables Section
Multiple tabs for exploring detailed data:
- Full filtered dataset
- Director rankings
- Cast member rankings
- Dataset information

### Search Section
- Real-time title search
- Instant results display

## 🎯 Use Cases

1. **Content Strategy Analysis** - Understand Netflix's content distribution
2. **Production Trends** - See how content production has evolved
3. **Rating Analysis** - Understand rating distributions and trends
4. **Global Reach** - Identify top countries producing content
5. **Genre Insights** - See which genres are most prevalent
6. **Director/Actor Insights** - Find prolific directors and actors

## 💡 Performance Optimizations

- Data caching with `@st.cache_data` for efficient loading
- Vectorized pandas operations
- Minimal recalculations on filter changes
- Efficient matplotlib figure handling

## 🔧 Technical Stack

- **Streamlit** - Web framework for data apps
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Static visualizations
- **Seaborn** - Statistical data visualization
- **NumPy** - Numerical computing

## 📈 Future Enhancements

Potential features to add:
- Time series forecasting of content additions
- Recommendation engine based on genres/ratings
- Network graph of directors and actors
- Advanced filtering by multiple criteria
- Export filtered data to CSV/Excel
- Dark mode theme
- Interactive 3D visualizations

## 🐛 Troubleshooting

### Port already in use
```bash
# Run on different port
streamlit run app.py --server.port 8502
```

### Data file not found
Ensure `netflix_titles.csv` is in the same directory as `app.py`

### Missing values in visualizations
The app handles missing values gracefully with defaults like "Unknown"

## 📝 Notes

- The dashboard automatically caches data on first load for performance
- All visualizations are responsive and scale to the browser window
- Filters are applied in real-time to all charts and tables
- Missing director/cast information is labeled as "Unknown"

## 👨‍💻 Author & License

Created as part of Netflix EDA analysis project.
