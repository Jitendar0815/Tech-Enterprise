import streamlit as st
import plotly.express as px
from utils.styling import load_css, navbar
from utils.data_loader import get_content_data

st.set_page_config(page_title="Content Performance", page_icon="🎬", layout="wide")
load_css("assets/style.css")
navbar()

st.markdown('<div class="fade-in"><h1>🎬 Content Performance</h1></div>', unsafe_allow_html=True)
st.markdown("Analyse movies & shows by genre, ratings, and box office.")

df = get_content_data()

# ---- TOP GENRES ----
st.markdown('<div class="fade-in"><h2>🏆 Top Genres by Total Views</h2></div>', unsafe_allow_html=True)
genre_views = df.groupby('genre')['views_millions'].sum().reset_index().sort_values('views_millions', ascending=False)
fig_bar = px.bar(genre_views, x='views_millions', y='genre', orientation='h',
                 labels={'views_millions': 'Total Views (Millions)'},
                 color='views_millions', color_continuous_scale='bluered',
                 template='plotly_dark')
fig_bar.update_layout(yaxis={'categoryorder': 'total ascending'},
                      margin=dict(l=0, r=0, t=30, b=0),
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      coloraxis_showscale=False)
st.plotly_chart(fig_bar, use_container_width=True)

# ---- SCATTER: RATING VS BOX OFFICE ----
st.markdown('<div class="fade-in"><h2>⭐ Rating vs. Box Office (Bubble size = Views)</h2></div>', unsafe_allow_html=True)
fig_scatter = px.scatter(df, x='rating', y='box_office_millions', size='views_millions',
                         color='genre', hover_name='title', template='plotly_dark',
                         labels={'rating': 'IMDb Rating', 'box_office_millions': 'Box Office ($M)'})
fig_scatter.update_traces(marker=dict(line=dict(width=1, color='white')))
fig_scatter.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                          paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_scatter, use_container_width=True)

# ---- TOP MOVIES TABLE ----
st.markdown('<div class="fade-in"><h2>📋 Top 10 Movies by Box Office</h2></div>', unsafe_allow_html=True)
top10 = df.nlargest(10, 'box_office_millions')[['title','genre','rating','box_office_millions','views_millions']]
st.dataframe(
    top10.style.background_gradient(subset=['box_office_millions'], cmap='OrRd')
    .format({'box_office_millions': '${:.1f}M', 'views_millions': '{:.1f}M'}),
    use_container_width=True
)

st.caption("Data simulated · Genres: Action, Comedy, Drama, Sci-Fi, Horror")
