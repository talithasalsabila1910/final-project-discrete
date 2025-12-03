import streamlit as st

# ============================
# CONFIG
# ============================
st.set_page_config(
    page_title="My Web App",
    page_icon="🌐",
    layout="wide"
)

# ============================
# HIDE DEFAULT SIDEBAR NAVIGATION
# ============================
hide_nav = """
<style>
    [data-testid="stSidebarNav"] {display: none;}
</style>
"""
st.markdown(hide_nav, unsafe_allow_html=True)

# ============================
# CUSTOM SIDEBAR
# ============================
with st.sidebar:
    st.markdown("""
        <h2 style='color:white; padding-bottom:5px;'>📁 Menu</h2>
        <style>
            .menu-btn {
                background-color:#3a3f4b;
                padding:10px 15px;
                color:white;
                border-radius:8px;
                margin-bottom:8px;
                cursor:pointer;
                text-decoration:none;
                display:block;
                font-size:16px;
            }
            .menu-btn:hover {
                background-color:#565c6b;
                transform: scale(1.02);
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("🏠  Main Page"):
        st.switch_page("main.py")

    if st.button("🗺️  Map Visual"):
        st.switch_page("pages/mapvisual.py")

    if st.button("👥  Team Profile"):
        st.switch_page("pages/teamprofile.py")

    if st.button("📊 Graph Visual"):
        st.switch_page("pages/graphvisual.py")

# ============================
# PAGE CONTENT
# ============================
st.title("Welcome to Our Web App 👋")
st.write("""
This is the main homepage.

Use the sidebar menu to navigate pages manually.
""")
