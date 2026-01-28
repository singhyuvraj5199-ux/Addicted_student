# 📱 Social Media Addiction Dashboard

An interactive Python dashboard for analyzing student social media addiction patterns with comprehensive visualizations and insights.

## 🌟 Features

### 1. **Interactive Search & Filtering**
   - Search by Student ID, Country, Platform, Academic Level, or Gender
   - Filter by age range and addiction score threshold
   - Real-time data updates based on filters

### 2. **Key Metrics Dashboard**
   - Total students analyzed
   - Average daily social media usage
   - Academic performance impact percentage
   - Average addiction score

### 3. **Comprehensive Visualizations**

   **Pie Charts:**
   - Addiction severity distribution (Low/Moderate/Severe)
   - Most used social media platforms
   - Academic performance impact

   **Bar Charts:**
   - Average addiction score by gender
   - Average addiction score by academic level
   - Country-wise addiction comparison

   **Scatter Plots:**
   - Usage hours vs addiction score
   - Sleep hours vs mental health score
   - Interactive hover data with student details

   **Box Plots:**
   - Daily usage distribution by addiction level
   - Addiction score distribution by platform

   **Additional Charts:**
   - Addiction score histogram by gender
   - Correlation heatmap for key variables
   - Geographic analysis of top countries

### 4. **Addiction Severity Classification**
   - **Low (Score 1-3)**: Minimal addiction impact
   - **Moderate (Score 4-6)**: Moderate addiction concerns
   - **Severe (Score 7-10)**: Significant addiction issues

### 5. **Health & Wellbeing Insights**
   - Students with high daily usage (>5 hours)
   - Students with poor sleep (<6 hours)
   - Students with low mental health scores (<6)

### 6. **Data Export**
   - Download filtered data as CSV
   - Color-coded data table with addiction severity highlighting

## 📊 Key Insights Provided

The dashboard automatically analyzes:
- What percentage of students are severely addicted
- Which platforms are associated with higher addiction scores
- Correlation between usage time and addiction levels
- Impact on sleep patterns and mental health
- Academic performance implications
- Gender and academic level differences
- Geographic patterns in addiction rates

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Dashboard
```bash
streamlit run social_media_dashboard.py
```

### Step 3: Access the Dashboard
The dashboard will automatically open in your default browser at:
```
http://localhost:8501
```

## 📖 How to Use

### Search and Filter
1. Use the **sidebar** to select your search criteria
2. Choose specific values or apply range filters
3. The dashboard updates automatically

### Explore Visualizations
- **Hover** over charts for detailed information
- **Click** on legend items to show/hide categories
- **Zoom** and **pan** on interactive plots

### Download Data
- Scroll to the data table section
- Click **"Download Filtered Data as CSV"** button
- Save the filtered dataset for further analysis

## 📈 Dashboard Sections

1. **Key Metrics** - Quick overview of important statistics
2. **Key Insights** - Automated analysis of addiction patterns and health impacts
3. **Visual Analytics** - Interactive charts and graphs
4. **Geographic Analysis** - Country-wise addiction patterns
5. **Detailed Data View** - Searchable, sortable data table
6. **Statistical Summary** - Descriptive statistics for key variables

## 🎯 Analysis Variables

The dashboard analyzes the following data points:
- Student demographics (Age, Gender, Country, Academic Level)
- Social media usage (Hours per day, Platform preference)
- Impact metrics (Academic performance, Sleep hours, Mental health score)
- Relationship factors (Status, Conflicts over social media)
- Addiction score (1-10 scale)

## 💡 Tips for Best Results

1. Start with **"All Data"** to see overall patterns
2. Use **age and addiction filters** to focus on specific risk groups
3. Compare **different platforms** to identify high-risk apps
4. Examine **correlations** between usage, sleep, and mental health
5. Export filtered data for **external analysis** or reporting

## 🔍 Sample Queries You Can Run

- "Show me all students with severe addiction (score 7-10)"
- "Which country has the highest average addiction scores?"
- "How does Instagram usage compare to other platforms?"
- "What's the relationship between daily usage and mental health?"
- "Which academic level is most affected?"

## 🎨 Dashboard Features

- **Responsive design** that works on different screen sizes
- **Color-coded visualizations** for easy interpretation
- **Real-time filtering** without page reloads
- **Professional styling** with custom CSS
- **Interactive tooltips** for detailed information

## 📝 Data Requirements

The dashboard expects a CSV file with the following columns:
- Student_ID
- Age
- Gender
- Academic_Level
- Country
- Avg_Daily_Usage_Hours
- Most_Used_Platform
- Affects_Academic_Performance
- Sleep_Hours_Per_Night
- Mental_Health_Score
- Relationship_Status
- Conflicts_Over_Social_Media
- Addicted_Score

## 🤝 Support

If you encounter any issues:
1. Ensure all dependencies are installed correctly
2. Verify your CSV file path in the code
3. Check that your Python version is 3.8 or higher
4. Make sure the CSV file follows the expected format

## 📄 License

This dashboard is provided for educational and analytical purposes.

---

**Created for comprehensive social media addiction analysis and student wellbeing research.**
