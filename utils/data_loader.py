import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit as st

np.random.seed(42)

@st.cache_data
def get_daily_summary():
    dates = pd.date_range(end=datetime.today(), periods=30).strftime('%Y-%m-%d')
    users = np.random.randint(8000, 15000, size=30).cumsum() // 10 + 5000
    attention = np.random.normal(12, 3, 30).clip(5, 20)
    content = np.random.randint(50, 100, 30)
    engagement = np.random.uniform(3.5, 8.0, 30)
    return pd.DataFrame({
        'date': dates,
        'total_users': users,
        'avg_attention_min': attention,
        'content_pieces': content,
        'engagement_rate': engagement
    })

@st.cache_data
def get_attention_data():
    dates = pd.date_range(end=datetime.today(), periods=30)
    hours = np.arange(24)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    records = []
    for d in dates:
        dow = d.dayofweek
        for h in hours:
            base = 0.5 + 0.3*np.sin((h-14)*np.pi/12) + 0.2*(1 if dow>=5 else 0)
            score = base + np.random.normal(0, 0.1)
            span = np.random.normal(10 + 3*base, 2)
            records.append({
                'date': d.strftime('%Y-%m-%d'),
                'hour': h,
                'day_name': days[dow],
                'attention_score': np.clip(score, 0, 1),
                'attention_span_min': max(1, span)
            })
    return pd.DataFrame(records)

@st.cache_data
def get_content_data():
    genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Horror']
    titles = [f"Movie {i}" for i in range(1, 31)]
    data = {
        'title': titles,
        'genre': np.random.choice(genres, 30),
        'rating': np.round(np.random.uniform(5.0, 9.5, 30), 1),
        'box_office_millions': np.random.uniform(10, 800, 30),
        'views_millions': np.random.uniform(5, 200, 30)
    }
    return pd.DataFrame(data)

@st.cache_data
def get_social_data():
    dates = pd.date_range(end=datetime.today(), periods=30).strftime('%Y-%m-%d')
    sentiment = np.cumsum(np.random.normal(0, 0.05, 30))
    sentiment = np.clip(sentiment, -0.8, 0.8)
    sentiment_df = pd.DataFrame({'date': dates, 'sentiment_score': sentiment})
    hashtags = ['#StreamingNow','#MovieNight','#BingeWatch','#BoxOffice','#NewRelease',
                '#MustWatch','#CriticsChoice','#FanFavorite','#WatchParty','#TrailerDrop']
    counts = np.random.randint(500, 10000, len(hashtags))
    hashtag_df = pd.DataFrame({'hashtag': hashtags, 'count': counts}).sort_values('count', ascending=False)
    return sentiment_df, hashtag_df

@st.cache_data
def get_audience_data():
    age = pd.DataFrame({
        'age_group': ['13-17','18-24','25-34','35-44','45-54','55+'],
        'percentage': [8, 25, 30, 20, 12, 5]
    })
    device = pd.DataFrame({
        'device': ['Mobile', 'Desktop', 'Tablet', 'Smart TV'],
        'users_percent': [45, 30, 15, 10]
    })
    countries = ['United States','India','Brazil','United Kingdom','Germany',
                 'France','Japan','South Korea','Canada','Australia','Mexico','Italy']
    viewers = np.random.uniform(5, 120, len(countries))
    geo = pd.DataFrame({
        'country': countries,
        'viewers_millions': viewers
    }).sort_values('viewers_millions', ascending=False)
    return age, device, geo
