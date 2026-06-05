import streamlit as st
import plotly.express as px
import pandas as pd
from utils.styling import load_css
from utils.data_loader import (
    get_daily_summary,
    get_attention_data,
    get_content_data,
    get_social_data,
    get_audience_data,
)

st.set_page_config(
    page_title="Media Attention Analytics",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css("assets/style.css")

# =============================================================================
# HERO SECTION
# =============================================================================
st.markdown("""
<div class="fade-in" style="text-align: center; margin-top: -1rem;">
    <h1>🎬 Media, Entertainment & Attention Analytics</h1>
    <p class="hero-subtitle">Decode what captures the world's attention.</p>
</div>
<hr>
""", unsafe_allow_html=True)

# =============================================================================
# KPI METRICS
# =============================================================================
df_summary = get_daily_summary()
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(f"""
    <div class="metric-card fade-in" style="animation-delay: 0.1s">
        <div class="value">{df_summary['total_users'].iloc[-1]:,}</div>
        <div class="label">👥 Total Active Users</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="metric-card fade-in" style="animation-delay: 0.2s">
        <div class="value">{df_summary['avg_attention_min'].iloc[-1]:.1f} min</div>
        <div class="label">⏱️ Avg Attention Span</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="metric-card fade-in" style="animation-delay: 0.3s">
        <div class="value">{df_summary['content_pieces'].iloc[-1]}</div>
        <div class="label">🎞️ Content Pieces</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class="metric-card fade-in" style="animation-delay: 0.4s">
        <div class="value">{df_summary['engagement_rate'].iloc[-1]:.1f}%</div>
        <div class="label">📈 Engagement Rate</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# MAIN TREND CHART
# =============================================================================
st.markdown("""
<div class="fade-in" style="animation-delay: 0.5s">
    <h2>📅 Daily Active Users Trend</h2>
</div>
""", unsafe_allow_html=True)

fig = px.area(
    df_summary, x='date', y='total_users',
    labels={'date': '', 'total_users': 'Users'},
    template="plotly_dark",
    color_discrete_sequence=['#ff4b6e']
)
fig.update_traces(line=dict(width=3, shape='spline'), opacity=0.7,
                  fill='tozeroy', fillcolor='rgba(255,75,110,0.15)')
fig.update_layout(
    height=420,
    margin=dict(l=0, r=0, t=30, b=0),
    hovermode='x unified',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
)
st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# SECTION 1: ATTENTION ANALYTICS
# =============================================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="fade-in"><h2>📊 Attention Analytics</h2></div>', unsafe_allow_html=True)
st.markdown("Deep dive into how user attention fluctuates across hours and days.")

df_att = get_attention_data()

# Heatmap
heatmap_data = df_att.pivot_table(values='attention_score', index='day_name', columns='hour', aggfunc='mean')
day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
heatmap_data = heatmap_data.reindex(day_order)

fig_heat = px.imshow(
    heatmap_data,
    labels=dict(x="Hour of Day", y="Day of Week", color="Avg Attention"),
    x=[f"{h}:00" for h in range(24)],
    y=day_order,
    color_continuous_scale='OrRd',
    template='plotly_dark',
    aspect='auto'
)
fig_heat.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                       paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_heat, use_container_width=True)

# Attention trend line
daily_trend = df_att.groupby('date')['attention_score'].mean().reset_index()
fig_line_att = px.line(daily_trend, x='date', y='attention_score',
                       labels={'attention_score': 'Avg Attention Score'},
                       template='plotly_dark', color_discrete_sequence=['#ffd700'])
fig_line_att.update_traces(line_width=3)
fig_line_att.update_layout(hovermode='x unified', margin=dict(l=0, r=0, t=30, b=0),
                           paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_line_att, use_container_width=True)

# Histogram of attention spans
fig_hist = px.histogram(df_att, x='attention_span_min', nbins=35,
                        labels={'attention_span_min': 'Attention Span (min)'},
                        color_discrete_sequence=['#00b4d8'], template='plotly_dark')
fig_hist.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                       paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_hist, use_container_width=True)

# =============================================================================
# SECTION 2: CONTENT PERFORMANCE
# =============================================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="fade-in"><h2>🎬 Content Performance</h2></div>', unsafe_allow_html=True)
st.markdown("Analyse movies & shows by genre, ratings, and box office.")

df_content = get_content_data()

# Top genres bar
genre_views = df_content.groupby('genre')['views_millions'].sum().reset_index().sort_values('views_millions', ascending=False)
fig_bar_genre = px.bar(genre_views, x='views_millions', y='genre', orientation='h',
                       labels={'views_millions': 'Total Views (Millions)'},
                       color='views_millions', color_continuous_scale='bluered',
                       template='plotly_dark')
fig_bar_genre.update_layout(yaxis={'categoryorder': 'total ascending'},
                            margin=dict(l=0, r=0, t=30, b=0),
                            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            coloraxis_showscale=False)
st.plotly_chart(fig_bar_genre, use_container_width=True)

# Scatter: rating vs box office
fig_scatter = px.scatter(df_content, x='rating', y='box_office_millions', size='views_millions',
                         color='genre', hover_name='title', template='plotly_dark',
                         labels={'rating': 'IMDb Rating', 'box_office_millions': 'Box Office ($M)'})
fig_scatter.update_traces(marker=dict(line=dict(width=1, color='white')))
fig_scatter.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                          paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_scatter, use_container_width=True)

# Top 10 movies table
top10 = df_content.nlargest(10, 'box_office_millions').copy()
top10['box_office_millions'] = top10['box_office_millions'].apply(lambda x: f"${x:.1f}M")
top10['views_millions'] = top10['views_millions'].apply(lambda x: f"{x:.1f}M")
st.markdown("#### 📋 Top 10 Movies by Box Office")
st.dataframe(top10[['title','genre','rating','box_office_millions','views_millions']],
             use_container_width=True, hide_index=True)

# =============================================================================
# SECTION 3: SOCIAL MEDIA BUZZ
# =============================================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="fade-in"><h2>💬 Social Media Buzz</h2></div>', unsafe_allow_html=True)
st.markdown("Track sentiment and trending topics around media content.")

df_sentiment, df_hashtags = get_social_data()

# Sentiment line
fig_line_sent = px.line(df_sentiment, x='date', y='sentiment_score',
                        labels={'sentiment_score': 'Sentiment (-1 to +1)'},
                        template='plotly_dark', color_discrete_sequence=['#2ecc71'])
fig_line_sent.add_hline(y=0, line_dash='dot', line_color='gray')
fig_line_sent.update_traces(line_width=3, mode='lines+markers', marker=dict(size=5))
fig_line_sent.update_layout(hovermode='x unified', margin=dict(l=0, r=0, t=30, b=0),
                            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_line_sent, use_container_width=True)

# Hashtags bar
fig_bar_hash = px.bar(df_hashtags, x='count', y='hashtag', orientation='h',
                      labels={'count': 'Mentions'},
                      color='count', color_continuous_scale='OrRd',
                      template='plotly_dark')
fig_bar_hash.update_layout(yaxis={'categoryorder': 'total ascending'},
                           margin=dict(l=0, r=0, t=30, b=0),
                           paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                           coloraxis_showscale=False)
st.plotly_chart(fig_bar_hash, use_container_width=True)

# Metrics
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.metric("Avg Sentiment", f"{df_sentiment['sentiment_score'].mean():.2f}", delta="+0.05")
with col_s2:
    st.metric("Total Mentions", "124.5K", delta="+8.2K")
with col_s3:
    st.metric("Top Hashtag", df_hashtags.iloc[0]['hashtag'])

# =============================================================================
# SECTION 4: AUDIENCE INSIGHTS
# =============================================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="fade-in"><h2>👥 Audience Insights</h2></div>', unsafe_allow_html=True)
st.markdown("Who is watching, on what device, and from where.")

age_df, device_df, geo_df = get_audience_data()

# Age donut
fig_pie_age = px.pie(age_df, values='percentage', names='age_group',
                     hole=0.6, color_discrete_sequence=px.colors.sequential.RdBu,
                     template='plotly_dark')
fig_pie_age.update_traces(textinfo='percent+label', textfont_color='white')
fig_pie_age.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                          paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_pie_age, use_container_width=True)

# Device bar
fig_bar_dev = px.bar(device_df, x='device', y='users_percent',
                     labels={'users_percent': '% of Users'},
                     color='device', color_discrete_sequence=['#ff4b6e','#00b4d8','#ffd700','#2ecc71'],
                     template='plotly_dark')
fig_bar_dev.update_layout(showlegend=False, margin=dict(l=0, r=0, t=30, b=0),
                          paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_bar_dev, use_container_width=True)

# Top countries
fig_geo = px.bar(geo_df.head(12), x='country', y='viewers_millions',
                 labels={'viewers_millions': 'Viewers (Millions)'},
                 color='viewers_millions', color_continuous_scale='tealrose',
                 template='plotly_dark')
fig_geo.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      coloraxis_showscale=False)
st.plotly_chart(fig_geo, use_container_width=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("© 2026 Media Attention Analytics · Built with Streamlit & Passion")
