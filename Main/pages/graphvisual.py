import streamlit as st
import networkx as nx
import plotly.graph_objects as go

st.set_page_config(page_title="Graph Visualization", page_icon="📊", layout="wide")

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

# ======== TITLE ========
st.markdown("<div class='main-title'>Graph Visualization</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Generate and visualize random graphs with a clean dark theme.</div>",
            unsafe_allow_html=True)

# ======== INPUTS ========
num_nodes = st.number_input("Enter the number of nodes:", min_value=1, value=5, step=1)
num_edges = st.number_input("Enter the number of edges:", min_value=0, value=4, step=1)

# ======== BUTTON ========
if st.button("Generate Graph"):
    # Create graph
    G = nx.gnm_random_graph(num_nodes, num_edges)

    # Node positions
    pos = nx.spring_layout(G, seed=42)

    # Edge coordinates
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1.5, color="#aaaaaa"),
        hoverinfo="none",
        mode="lines"
    )

    # Node coordinates
    node_x, node_y = [], []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    # Node trace with dark theme colors
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        hoverinfo="text",
        text=[str(i) for i in G.nodes()],
        textposition="top center",
        marker=dict(
            showscale=True,
            colorscale=[
                [0, "#eeeeee"],
                [0.5, "#888888"],
                [1, "#222222"]
            ],
            color=[G.degree(n) for n in G.nodes()],
            size=22,
            colorbar=dict(
                thickness=10,
                title=dict(text="Node Degree", side="right", font=dict(color="#eeeeee")),
                tickfont=dict(color="#eeeeee"),
                tickcolor="#eeeeee"
            ),
            line=dict(width=2, color="#000000")
        )
    )

    # Hover text
    node_trace.text = [
        f"Node {n} — Degree {G.degree(n)}" for n in G.nodes()
    ]

    # Figure layout
    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            showlegend=False,
            hovermode="closest",
            margin=dict(b=0, l=0, r=0, t=40),
            plot_bgcolor="#2b2b2b",
            paper_bgcolor="#2b2b2b",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            title=dict(text="Generated Graph", font=dict(color="#eeeeee"))
        )
    )

    # Display chart
    st.plotly_chart(fig, use_container_width=True)

    # Info Box
    st.markdown(
        f"""
        <div class="info-box">
            Graph with {num_nodes} nodes and {num_edges} edges generated successfully!
        </div>
        """,
        unsafe_allow_html=True
    )
