import streamlit as st
import plotly.graph_objects as go
import math

import streamlit as st

# Hide Streamlit default sidebar navigation
st.markdown("""
<style>
    [data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)

# Custom Sidebar
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


# ==============================
# Fungsi Haversine
# ==============================
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # radius Bumi dalam km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)   # <<< perbaikan di sini
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c



# ==============================
# Page Config
# ==============================
st.set_page_config(
    page_title="West Java Map (Light Mode)",
    page_icon="🗺️",
    layout="wide"
)


# ==============================
# Tema UI — Soft Modern Light
# ==============================
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .main {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0 0 25px rgba(0,0,0,0.1);
        }
        .title-text {
            font-size: 32px;
            font-weight: bold;
            color: #1a3d7c;
            text-align: center;
        }
        .subtitle-text {
            text-align: center;
            color: #555;
        }
        .stButton>button {
            background-color: #1a3d7c;
            color: white;
            padding: 8px 20px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #3059be;
            transform: scale(1.03);
        }
    </style>
""", unsafe_allow_html=True)


# ==============================
# Title
# ==============================
st.markdown("<p class='title-text'>🗺️ West Java City Connections</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>Choose cities to display their connections on a light map</p>", unsafe_allow_html=True)
st.write("")


# ==============================
# Data Kota
# ==============================
cities = {
    "Bandung": (-6.9175, 107.6191),
    "Bogor": (-6.5975, 106.8066),
    "Depok": (-6.4025, 106.7944),
    "Bekasi": (-6.234, 107.0057),
    "Cimahi": (-6.8996, 107.5422),
    "Sukabumi": (-6.9233, 106.9297),
    "Cirebon": (-6.732, 108.552),
    "Tasikmalaya": (-7.3274, 108.2207),
    "Banjar": (-7.3700, 108.5340)
}


# ==============================
# Sidebar
# ==============================
with st.sidebar:
   st.header("⚙️ Options")
   selected = st.multiselect("Select Cities:", list(cities.keys()))
   generate = st.button("Generate Map")


# ==============================
# Generate Map
# ==============================
if generate:
    if len(selected) < 2:
        st.warning("Please pick at least 2 cities.")
    else:
        # Ambil lat lon
        lats = [cities[c][0] for c in selected]
        lons = [cities[c][1] for c in selected]

        # Cari jarak terdekat
        min_dist = float("inf")
        closest = None
        edge_traces = []

        for i in range(len(selected)-1):
            for j in range(i+1, len(selected)):
                a, b = selected[i], selected[j]
                lat1, lon1 = cities[a]
                lat2, lon2 = cities[b]
                dist = haversine(lat1, lon1, lat2, lon2)

                if dist < min_dist:
                    min_dist = dist
                    closest = (a, b)

                # garis antar kota (abu-abu)
                edge_traces.append(
                    go.Scattermapbox(
                        lat=[lat1, lat2],
                        lon=[lon1, lon2],
                        mode="lines",
                        line=dict(color="#888", width=1.2)
                    )
                )

        # garis highlight merah
        lat1, lon1 = cities[closest[0]]
        lat2, lon2 = cities[closest[1]]

        edge_traces.append(
            go.Scattermapbox(
                lat=[lat1, lat2],
                lon=[lon1, lon2],
                mode="lines",
                line=dict(color="red", width=4)
            )
        )

        # titik kota
        node_trace = go.Scattermapbox(
            lat=lats,
            lon=lons,
            mode="markers+text",
            marker=dict(size=11, color="#1a3d7c"),
            text=[c for c in selected],
            textposition="top center"
        )

        fig = go.Figure(edge_traces + [node_trace])

        fig.update_layout(
            mapbox_style="open-street-map",  # MAP TERANG
            mapbox_zoom=7,
            mapbox_center={"lat": sum(lats)/len(lats), "lon": sum(lons)/len(lons)},
            margin={"l": 0, "r": 0, "t": 30, "b": 0},
            paper_bgcolor="#ffffff",
            font_color="#222"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Box info
        st.markdown(f"""
            <div style="
                background-color:#1a3d7c;
                padding: 15px;
                color:white;
                text-align:center;
                border-radius: 10px;
                margin-top:15px;">
                🔵 <b>Closest Cities:</b> {closest[0]} ↔ {closest[1]} <br>
                📏 <b>Distance:</b> {min_dist:.2f} km
            </div>
        """, unsafe_allow_html=True)
