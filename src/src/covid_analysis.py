import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """Load and preprocess COVID-19 data"""
    df = pd.read_csv(filepath)
    
    # Convert date column
    df['Date'] = pd.to_datetime(df['Date'])
    
    return df

def analyze_global_trends(df):
    """Analyze global COVID-19 trends"""
    # Group by date and sum confirmed cases globally
    global_daily_cases = df.groupby('Date')['Confirmed'].sum().reset_index()
    
    # Plot global trend
    plt.figure(figsize=(12, 6))
    plt.plot(global_daily_cases['Date'], global_daily_cases['Confirmed'])
    plt.title('Global Cumulative COVID-19 Cases')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Confirmed Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('global_trend.png')
    plt.close()

def top_countries_analysis(df):
    """Analyze top countries by total cases"""
    # Group by country and get total confirmed cases
    country_totals = df.groupby('Country/Region')['Confirmed'].max().nlargest(10)
    
    # Plot top 10 countries
    plt.figure(figsize=(10, 6))
    country_totals.plot(kind='bar')
    plt.title('Top 10 Countries by Total Confirmed Cases')
    plt.xlabel('Country')
    plt.ylabel('Total Confirmed Cases')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('top_countries.png')
    plt.close()
    
    return country_totals

def main():
    print("Starting COVID analysis script...")
    # Load data
    filepath = r'C:\Users\DNA3Concierge\Data Analysis\Covid-19 Project\covid-data-analysis\data\covid_19_clean_complete.csv'

    df = load_data(filepath)
    
    # Perform analyses
    analyze_global_trends(df)
    top_countries = top_countries_analysis(df)
    
    # Print top countries
    print("Top 10 Countries by Total Confirmed Cases:")
    print(top_countries)

if __name__ == '__main__':
    main()