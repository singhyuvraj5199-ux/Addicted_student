import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Social Media Addiction Dashboard",
    page_icon="📱",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 42px;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        padding: 20px;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .insight-box {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #1E88E5;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('Students Social Media Addiction.csv')
    return df

df = load_data()

# Title
st.markdown('<p class="main-header">📱 Social Media Addiction Analysis Dashboard</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar for filters and search
st.sidebar.header("🔍 Search & Filter Options")

# Search functionality
search_option = st.sidebar.selectbox(
    "Search by:",
    ["All Data", "Student ID", "Country", "Platform", "Academic Level", "Gender"]
)

if search_option == "Student ID":
    search_value = st.sidebar.number_input("Enter Student ID:", min_value=1, max_value=df['Student_ID'].max(), value=1)
    filtered_df = df[df['Student_ID'] == search_value]
elif search_option == "Country":
    search_value = st.sidebar.selectbox("Select Country:", sorted(df['Country'].unique()))
    filtered_df = df[df['Country'] == search_value]
elif search_option == "Platform":
    search_value = st.sidebar.selectbox("Select Platform:", sorted(df['Most_Used_Platform'].unique()))
    filtered_df = df[df['Most_Used_Platform'] == search_value]
elif search_option == "Academic Level":
    search_value = st.sidebar.selectbox("Select Academic Level:", sorted(df['Academic_Level'].unique()))
    filtered_df = df[df['Academic_Level'] == search_value]
elif search_option == "Gender":
    search_value = st.sidebar.selectbox("Select Gender:", df['Gender'].unique())
    filtered_df = df[df['Gender'] == search_value]
else:
    filtered_df = df

# Additional filters
st.sidebar.markdown("---")
st.sidebar.subheader("Additional Filters")

age_range = st.sidebar.slider(
    "Age Range:",
    int(df['Age'].min()),
    int(df['Age'].max()),
    (int(df['Age'].min()), int(df['Age'].max()))
)

addiction_threshold = st.sidebar.slider(
    "Minimum Addiction Score:",
    int(df['Addicted_Score'].min()),
    int(df['Addicted_Score'].max()),
    int(df['Addicted_Score'].min())
)

# Apply filters
filtered_df = filtered_df[
    (filtered_df['Age'] >= age_range[0]) & 
    (filtered_df['Age'] <= age_range[1]) &
    (filtered_df['Addicted_Score'] >= addiction_threshold)
]

# Define addiction severity categories
def categorize_addiction(score):
    if score <= 3:
        return "Low"
    elif score <= 6:
        return "Moderate"
    else:
        return "Severe"

df['Addiction_Level'] = df['Addicted_Score'].apply(categorize_addiction)
filtered_df['Addiction_Level'] = filtered_df['Addicted_Score'].apply(categorize_addiction)

# Main dashboard
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📊 Total Students", len(filtered_df))
with col2:
    avg_usage = filtered_df['Avg_Daily_Usage_Hours'].mean()
    st.metric("⏰ Avg Daily Usage", f"{avg_usage:.2f} hrs")
with col3:
    affected = (filtered_df['Affects_Academic_Performance'] == 'Yes').sum()
    st.metric("📚 Academic Impact", f"{affected} ({affected/len(filtered_df)*100:.1f}%)")
with col4:
    avg_addiction = filtered_df['Addicted_Score'].mean()
    st.metric("🎯 Avg Addiction Score", f"{avg_addiction:.2f}/10")

st.markdown("---")

# Key Insights Section
st.header("🔑 Key Insights")

col1, col2 = st.columns(2)

with col1:
    severe_count = (df['Addiction_Level'] == 'Severe').sum()
    moderate_count = (df['Addiction_Level'] == 'Moderate').sum()
    low_count = (df['Addiction_Level'] == 'Low').sum()
    
    st.markdown(f"""
    <div class="insight-box">
        <h3>Addiction Severity Distribution</h3>
        <ul>
            <li><b>Severe (Score 7-10):</b> {severe_count} students ({severe_count/len(df)*100:.1f}%)</li>
            <li><b>Moderate (Score 4-6):</b> {moderate_count} students ({moderate_count/len(df)*100:.1f}%)</li>
            <li><b>Low (Score 1-3):</b> {low_count} students ({low_count/len(df)*100:.1f}%)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    high_usage = (df['Avg_Daily_Usage_Hours'] > 5).sum()
    poor_sleep = (df['Sleep_Hours_Per_Night'] < 6).sum()
    poor_mental = (df['Mental_Health_Score'] < 6).sum()
    
    st.markdown(f"""
    <div class="insight-box">
        <h3>Health & Wellbeing Impact</h3>
        <ul>
            <li><b>High Usage (>5 hrs/day):</b> {high_usage} students ({high_usage/len(df)*100:.1f}%)</li>
            <li><b>Poor Sleep (<6 hrs):</b> {poor_sleep} students ({poor_sleep/len(df)*100:.1f}%)</li>
            <li><b>Low Mental Health (<6):</b> {poor_mental} students ({poor_mental/len(df)*100:.1f}%)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Visualization Section
st.header("📊 Visual Analytics")

# Row 1: Pie charts
col1, col2, col3 = st.columns(3)

with col1:
    addiction_dist = filtered_df['Addiction_Level'].value_counts()
    fig_pie1 = px.pie(
        values=addiction_dist.values,
        names=addiction_dist.index,
        title="Addiction Severity Distribution",
        color_discrete_sequence=['#4CAF50', '#FFC107', '#F44336'],
        hole=0.4
    )
    fig_pie1.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie1, use_container_width=True)

with col2:
    platform_dist = filtered_df['Most_Used_Platform'].value_counts()
    fig_pie2 = px.pie(
        values=platform_dist.values,
        names=platform_dist.index,
        title="Most Used Platforms",
        hole=0.4
    )
    st.plotly_chart(fig_pie2, use_container_width=True)

with col3:
    academic_impact = filtered_df['Affects_Academic_Performance'].value_counts()
    fig_pie3 = px.pie(
        values=academic_impact.values,
        names=academic_impact.index,
        title="Academic Performance Impact",
        color_discrete_sequence=['#F44336', '#4CAF50'],
        hole=0.4
    )
    st.plotly_chart(fig_pie3, use_container_width=True)

st.markdown("---")

# Row 2: Bar charts
col1, col2 = st.columns(2)

with col1:
    gender_addiction = filtered_df.groupby('Gender')['Addicted_Score'].mean().reset_index()
    fig_bar1 = px.bar(
        gender_addiction,
        x='Gender',
        y='Addicted_Score',
        title="Average Addiction Score by Gender",
        color='Gender',
        text_auto='.2f'
    )
    fig_bar1.update_traces(textposition='outside')
    st.plotly_chart(fig_bar1, use_container_width=True)

with col2:
    academic_addiction = filtered_df.groupby('Academic_Level')['Addicted_Score'].mean().reset_index()
    fig_bar2 = px.bar(
        academic_addiction,
        x='Academic_Level',
        y='Addicted_Score',
        title="Average Addiction Score by Academic Level",
        color='Academic_Level',
        text_auto='.2f'
    )
    fig_bar2.update_traces(textposition='outside')
    st.plotly_chart(fig_bar2, use_container_width=True)

st.markdown("---")

# Row 3: Scatter plots and correlation
col1, col2 = st.columns(2)

with col1:
    fig_scatter1 = px.scatter(
        filtered_df,
        x='Avg_Daily_Usage_Hours',
        y='Addicted_Score',
        color='Addiction_Level',
        size='Mental_Health_Score',
        hover_data=['Age', 'Gender', 'Most_Used_Platform'],
        title="Usage Hours vs Addiction Score",
        color_discrete_map={'Low': '#4CAF50', 'Moderate': '#FFC107', 'Severe': '#F44336'}
    )
    st.plotly_chart(fig_scatter1, use_container_width=True)

with col2:
    fig_scatter2 = px.scatter(
        filtered_df,
        x='Sleep_Hours_Per_Night',
        y='Mental_Health_Score',
        color='Addiction_Level',
        size='Addicted_Score',
        hover_data=['Age', 'Gender', 'Most_Used_Platform'],
        title="Sleep Hours vs Mental Health Score",
        color_discrete_map={'Low': '#4CAF50', 'Moderate': '#FFC107', 'Severe': '#F44336'}
    )
    st.plotly_chart(fig_scatter2, use_container_width=True)

st.markdown("---")

# Row 4: Box plots
col1, col2 = st.columns(2)

with col1:
    fig_box1 = px.box(
        filtered_df,
        x='Addiction_Level',
        y='Avg_Daily_Usage_Hours',
        color='Addiction_Level',
        title="Daily Usage Distribution by Addiction Level",
        color_discrete_map={'Low': '#4CAF50', 'Moderate': '#FFC107', 'Severe': '#F44336'}
    )
    st.plotly_chart(fig_box1, use_container_width=True)

with col2:
    fig_box2 = px.box(
        filtered_df,
        x='Most_Used_Platform',
        y='Addicted_Score',
        color='Most_Used_Platform',
        title="Addiction Score Distribution by Platform"
    )
    st.plotly_chart(fig_box2, use_container_width=True)

st.markdown("---")

# Histogram and Heatmap
col1, col2 = st.columns(2)

with col1:
    fig_hist = px.histogram(
        filtered_df,
        x='Addicted_Score',
        nbins=10,
        title="Distribution of Addiction Scores",
        color='Gender',
        barmode='group'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    # Correlation heatmap
    corr_columns = ['Age', 'Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night', 
                    'Mental_Health_Score', 'Conflicts_Over_Social_Media', 'Addicted_Score']
    corr_matrix = filtered_df[corr_columns].corr()
    
    fig_heatmap = px.imshow(
        corr_matrix,
        text_auto='.2f',
        aspect='auto',
        title="Correlation Heatmap",
        color_continuous_scale='RdBu_r'
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

st.markdown("---")

# Country-wise analysis
st.header("🌍 Geographic Analysis")
country_stats = filtered_df.groupby('Country').agg({
    'Addicted_Score': 'mean',
    'Student_ID': 'count',
    'Avg_Daily_Usage_Hours': 'mean'
}).round(2).reset_index()
country_stats.columns = ['Country', 'Avg Addiction Score', 'Student Count', 'Avg Daily Usage']

fig_map = px.bar(
    country_stats.sort_values('Avg Addiction Score', ascending=False).head(15),
    x='Country',
    y='Avg Addiction Score',
    color='Avg Addiction Score',
    title="Top 15 Countries by Average Addiction Score",
    text_auto='.2f',
    color_continuous_scale='Reds'
)
fig_map.update_traces(textposition='outside')
st.plotly_chart(fig_map, use_container_width=True)

st.markdown("---")

# Data Table
st.header("📋 Detailed Data View")
st.dataframe(
    filtered_df.style.background_gradient(subset=['Addicted_Score'], cmap='RdYlGn_r'),
    use_container_width=True,
    height=400
)

# Download filtered data
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_social_media_data.csv',
    mime='text/csv',
)

st.markdown("---")

# Statistical Summary
st.header("📈 Statistical Summary")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Addiction Score Statistics")
    st.write(filtered_df['Addicted_Score'].describe())

with col2:
    st.subheader("Usage Hours Statistics")
    st.write(filtered_df['Avg_Daily_Usage_Hours'].describe())

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>📱 Social Media Addiction Dashboard | Data Analysis & Insights</p>
        <p>Use the sidebar filters to explore different aspects of the data</p>
    </div>
""", unsafe_allow_html=True)
