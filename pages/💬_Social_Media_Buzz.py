import streamlit as st
import plotly.express as px
from utils.data_loader import get_social_data
from utils.styling import load_css

st.set_page_config(page_title="Social Media Buzz", page_icon="💬", layout="wide")
load_css("assets/style.css")

st.markdown('<div class="fade-in"><h1>💬 Social Media Buzz</h1></div>', unsafe_allow_html=True)
st.markdown("Track sentiment and trending topics around media content.")

df_sentiment, df_hashtags = get_social_data()

# ---- SENTIMENT OVER TIME ----
st.markdown('<div class="fade-in"><h2>📊 Daily Sentiment Score</h2></div>', unsafe_allow_html=True)
fig_line = px.line(df_sentiment, x='date', y='sentiment_score',
                   labels={'sentiment_score': 'Sentiment (-1 to +1)'},
                   template='plotly_dark', color_discrete_sequence=['#2ecc71'])
fig_line.add_hline(y=0, line_dash='dot', line_color='gray')
fig_line.update_traces(line_width=3, mode='lines+markers', marker=dict(size=5))
fig_line.update_layout(hovermode='x unified', margin=dict(l=0, r=0, t=30, b=0),
                       paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_line, use_container_width=True)

# ---- TRENDING HASHTAGS ----
st.markdown('<div class="fade-in"><h2>🔥 Trending Hashtags (Last 7 Days)</h2></div>', unsafe_allow_html=True)
fig_bar = px.bar(df_hashtags, x='count', y='hashtag', orientation='h',
                 labels={'count': 'Mentions'},
                 color='count', color_continuous_scale='OrRd',
                 template='plotly_dark')
fig_bar.update_layout(yaxis={'categoryorder': 'total ascending'},
                      margin=dict(l=0, r=0, t=30, b=0),
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      coloraxis_showscale=False)
st.plotly_chart(fig_bar, use_container_width=True)

# ---- METRIC CARDS ----
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Avg Sentiment", f"{df_sentiment['sentiment_score'].mean():.2f}", delta="+0.05")
with col2:
    st.metric("Total Mentions", "124.5K", delta="+8.2K")
with col3:
    st.metric("Top Hashtag", df_hashtags.iloc[0]['hashtag'])

st.caption("Data updated hourly (simulated)")
