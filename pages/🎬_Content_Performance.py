import streamlit as st
import plotly.express as px
from utils.data_loader import get_content_data
from utils.styling import load_css

st.set_page_config(page_title="Content Performance", page_icon="🎬", layout="wide")
load_css("assets/style.css")

st.title("🎬 Content Performance")
st.markdown("Analyse movies & shows by genre, ratings, and box office.")

df = get_content_data()

# ---- TOP GENRES ----
st.subheader("🏆 Top Genres by Total Views")
genre_views = df.groupby('genre')['views_millions'].sum().reset_index().sort_values('views_millions', ascending=False)
fig_bar = px.bar(
    genre_views, x='views_millions', y='genre', orientation='h',
    labels={'views_millions': 'Total Views (Millions)'},
    color='views_millions', color_continuous_scale='bluered',
    template='plotly_dark'
)
fig_bar.update_layout(yaxis={'categoryorder': 'total ascending'}, margin=dict(l=0,r=0,t=30,b=0),
                      paper_bgcolor='rgba(0,0,0,0)', coloraxis_showscale=False)
st.plotly_chart(fig_bar, use_container_width=True)

# ---- SCATTER: RATING VS BOX OFFICE ----
st.subheader("⭐ Rating vs. Box Office (Bubble size = Views)")
fig_scatter = px.scatter(
    df, x='rating', y='box_office_millions', size='views_millions',
    color='genre', hover_name='title', template='plotly_dark',
    labels={'rating': 'IMDb Rating', 'box_office_millions': 'Box Office ($M)'}
)
fig_scatter.update_layout(margin=dict(l=0,r=0,t=30,b=0), paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_scatter, use_container_width=True)

# ---- TOP MOVIES TABLE ----
st.subheader("📋 Top 10 Movies by Box Office")
top10 = df.nlargest(10, 'box_office_millions')[['title','genre','rating','box_office_millions','views_millions']]
st.dataframe(
    top10.style.background_gradient(subset=['box_office_millions'], cmap='Reds'),
    use_container_width=True
)

st.caption("Data simulated · Genres: Action, Comedy, Drama, Sci-Fi, Horror")
