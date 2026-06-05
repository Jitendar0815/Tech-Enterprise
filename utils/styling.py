import streamlit as st

def load_css(file_name: str):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def navbar():
    """Navbar using st.page_link for subpages, and a Home button on subpages only."""
    # Determine current page by checking the script path
    current_page = st.session_state.get("current_page", "")
    # We'll use a simple trick: check if we are NOT on the main app
    is_main = (st.script_runner.script_path.endswith("app.py") if hasattr(st, "script_runner") else False)
    # More robust: in Streamlit, the main script is just "app.py", while pages are under "pages/"
    # We can use st.experimental_get_query_params or simply check the module name
    # But easiest: only show the Home button if st.button is inside a page (not main)
    # We'll always show all links; Home will be a link to app.py using st.switch_page only on non-home pages.

    cols = st.columns([1, 1, 1, 1, 1])

    # Page links (works for files inside pages/)
    with cols[1]:
        st.page_link("pages/1_📊_Attention_Analytics.py", label="📊 Attention", use_container_width=True)
    with cols[2]:
        st.page_link("pages/2_🎬_Content_Performance.py", label="🎬 Content", use_container_width=True)
    with cols[3]:
        st.page_link("pages/3_💬_Social_Media_Buzz.py", label="💬 Social", use_container_width=True)
    with cols[4]:
        st.page_link("pages/4_👥_Audience_Insights.py", label="👥 Audience", use_container_width=True)

    # Home button – only if not already on home page
    # Detect by checking if the script path is not app.py (using hacky check)
    is_not_home = "pages/" in st.script_runner.script_path if hasattr(st, "script_runner") else True
    if is_not_home:
        with cols[0]:
            if st.button("🏠 Home", key="nav_home", use_container_width=True):
                st.switch_page("app.py")
    else:
        # On home page, just show a disabled button or placeholder
        with cols[0]:
            st.markdown('<div style="text-align: center; padding: 0.5rem; color: #ff4b6e; font-weight: 600;">🏠 Home</div>', unsafe_allow_html=True)
