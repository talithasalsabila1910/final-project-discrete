import streamlit as st

# ============================
# CONFIG
# ============================
st.set_page_config(
    page_title="Our Web App",
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

    if st.button("📊 Graph Visual"):
        st.switch_page("pages/graphvisual.py")

# ============================
# PAGE CONTENT
# ============================
st.markdown(
    """
    <div style="text-align:center;">
        <h1>Hello, Welcome To Our Website 👋</h1>
        <p style="font-size:18px; color:gray;">
            Meet our amazing team
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

team = [
    {
        "Name": "Talitha Syakirah Salsabila",
        "Major": "Actuarial Science",
        "Photo": "https://github.com/KemalRmadhn/photopython/blob/main/Talitha1.jpg?raw=true",
        "Task": "Main.py and Mapvisual.py"
    },
    {
        "Name": "Kezia Fransisca H",
        "Major": "Actuarial Science",
        "Photo": "https://github.com/KemalRmadhn/photopython/blob/main/Kezia2.jpg?raw=true",
        "Task": "Presentation Video"
    },
    {
        "Name": "Carissa Isaiah S",
        "Major": "Actuarial Science",
        "Photo": "https://github.com/KemalRmadhn/photopython/blob/main/carissa1.jpg?raw=true",
        "Task": "Graphvisual.py"
    }
]

# Kolom kiri & kanan kosong agar konten ke tengah
left_space, col1, col2, col3, right_space = st.columns([1, 2, 2, 2, 1])

for member, col in zip(team, [col1, col2, col3]):
    with col:
        st.image(member["Photo"], width=200)
        st.markdown(f"**{member['Name']}**")
        st.caption(member["Major"])
        st.caption(f"Task : {member['Task']}")
