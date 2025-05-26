import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib import rcParams

def load_movie_data():
    """Load movie data from CSV or generate sample data"""
    try:
        df = pd.read_csv('data/movie_ratings.csv')
    except FileNotFoundError:
        print("Using sample data as CSV not found")
        data = {
            'title': ['Inception', 'The Dark Knight', 'Pulp Fiction', 'Fight Club', 
                     'Parasite', 'Interstellar', 'The Godfather'],
            'genre': ['Sci-Fi', 'Action', 'Crime', 'Drama', 'Thriller', 'Sci-Fi', 'Crime'],
            'rating': [8.8, 9.0, 8.9, 8.8, 8.5, 8.6, 9.2],
            'watch_time_min': [148, 152, 154, 139, 132, 169, 175],
            'platform': ['Netflix', 'Prime', 'Netflix', 'Disney+', 'Hulu', 'Prime', 'HBO'],
            'year': [2010, 2008, 1994, 1999, 2019, 2014, 1972]
        }
        df = pd.DataFrame(data)
    return df

def create_visualizations(df):
    """Generate all visualizations"""
    # Setup style using seaborn
    rcParams['font.family'] = 'sans-serif'
    sns.set_style("whitegrid")  # Use Seaborn style here
    sns.set_palette("husl")
    
    # Create output directory
    os.makedirs('assets', exist_ok=True)
    
    # Visualization 1: Avg Rating by Genre (Bar Chart)
    plt.figure(figsize=(12, 6))
    genre_avg = df.groupby('genre')['rating'].mean().sort_values(ascending=False)
    genre_avg.plot(kind='bar', width=0.8)
    plt.title('Average Rating by Genre', fontsize=16, pad=20)
    plt.xlabel('Genre', fontsize=12)
    plt.ylabel('Average Rating (0-10)', fontsize=12)
    plt.ylim(7, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('assets/genre_ratings.png', dpi=120)
    plt.close()
    
    # Visualization 2: Rating vs Watch Time (Scatter Plot)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='watch_time_min', y='rating', 
                   hue='genre', size='year', sizes=(50, 200))
    plt.title('Rating vs Watch Time', fontsize=16, pad=20)
    plt.xlabel('Watch Time (minutes)', fontsize=12)
    plt.ylabel('Rating (0-10)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('assets/rating_vs_time.png', dpi=120, bbox_inches='tight')
    plt.close()
    
    # Visualization 3: Platform Comparison (Subplots)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Platform Comparison', fontsize=16, y=1.05)
    
    # Subplot 1: Avg Rating by Platform
    platform_avg = df.groupby('platform')['rating'].mean().sort_values(ascending=False)
    platform_avg.plot(kind='bar', ax=ax1, width=0.6)
    ax1.set_title('Average Rating by Platform')
    ax1.set_ylabel('Rating (0-10)')
    ax1.set_ylim(7, 10)
    ax1.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Subplot 2: Content Distribution by Platform
    platform_counts = df['platform'].value_counts()
    platform_counts.plot(kind='pie', ax=ax2, autopct='%1.1f%%', 
                        startangle=90, shadow=True)
    ax2.set_title('Content Distribution')
    ax2.set_ylabel('')

    plt.tight_layout()
    plt.savefig('assets/platform_comparison.png', dpi=120)
    plt.close()

if __name__ == "__main__":
    movie_df = load_movie_data()
    create_visualizations(movie_df)
    print("Visualizations saved to assets/ folder")
