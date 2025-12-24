import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set aesthetics for plots
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def run_analysis():
    # 1. Load and Preprocess Data
    try:
        df = pd.read_csv('hospital_opd_visits.csv')
    except FileNotFoundError:
        print("Data file not found. Please run the generator script first.")
        return

    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Date'] = df['Timestamp'].dt.date
    df['Hour'] = df['Timestamp'].dt.hour
    df['Day_Name'] = df['Timestamp'].dt.day_name()
    df['Month'] = df['Timestamp'].dt.month_name()
    
    # Define day order for plotting
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # 2. Summary Statistics
    print("-" * 30)
    print("SUMMARY STATISTICS")
    print("-" * 30)
    summary_stats = df[['Age', 'Consultation_Fee', 'Wait_Time_Min']].describe()
    print(summary_stats)
    
    # 3. Daily Trend (Line Plot)
    daily_visits = df.groupby('Date').size()
    
    plt.figure()
    daily_visits.plot(kind='line', color='#2c3e50', linewidth=2, marker='o', markersize=4)
    plt.title('Daily OPD Visit Volume (6-Month Trend)', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Number of Appointments')
    plt.tight_layout()
    plt.savefig('daily_trend.png')
    
    # 4. Weekly Trend (Bar/Line Plot)
    weekly_visits = df.groupby('Day_Name').size().reindex(day_order)
    
    plt.figure()
    sns.barplot(x=weekly_visits.index, y=weekly_visits.values, palette='viridis')
    plt.title('Average Visits by Day of the Week', fontsize=14)
    plt.ylabel('Total Visits')
    plt.savefig('weekly_trend.png')

    # 5. Department Breakdown (Pie Chart)
    plt.figure()
    df['Department'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Distribution of Visits by Department')
    plt.ylabel('')
    plt.savefig('dept_distribution.png')

    # 6. Hourly Heatmap (Advance Visual)
    pivot_table = df.pivot_table(index='Day_Name', columns='Hour', values='Patient_ID', aggfunc='count').reindex(day_order)
    
    plt.figure(figsize=(14, 7))
    sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap="YlGnBu")
    plt.title('OPD Density Heatmap: Day vs Hour', fontsize=14)
    plt.savefig('hourly_heatmap.png')

    print("\nAnalysis Complete. Graphs saved as PNG files.")

if __name__ == "__main__":
    run_analysis()

