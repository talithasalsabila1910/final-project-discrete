#import streamlit as st 

#st.title("Team Profile")

#import streamlit as st

#st.set_page_config(
    #page_title="Team Profile",
    #page_icon="👥",
    #layout="wide"
#)

# Hide Streamlit default sidebar navigation
#st.markdown("""
#<style>
    #[data-testid="stSidebarNav"] {display: none;}
#</style>
#""", unsafe_allow_html=True)

# Custom Sidebar
#with st.sidebar:
    #st.markdown("""
        #<h2 style='color:white; padding-bottom:5px;'>📁 Menu</h2>
        #<style>
            #.menu-btn {
                #background-color:#3a3f4b;
                #padding:10px 15px;
                #color:white;
                #border-radius:8px;
                #margin-bottom:8px;
                #ursor:pointer;
                #text-decoration:none;
                #isplay:block;
                #font-size:16px;
            #}
            #.menu-btn:hover {
                #background-color:#565c6b;
                #transform: scale(1.02);
            #}
        #</style>
    #""", unsafe_allow_html=True)

    #if st.button("🏠  Main Page"):
        #st.switch_page("main.py")

    #if st.button("🗺️  Map Visual"):
        #st.switch_page("pages/mapvisual.py")

    #if st.button("👥  Team Profile"):
        #st.switch_page("pages/teamprofile.py")

    #f st.button("📊 Graph Visual"):
        #st.switch_page("pages/graphvisual.py")


#team = [
    #{
        #"Name": "Talitha Syakirah Salsabila",
        #"Major": "Actuarial Science",
        #"Photo": "https://github.com/KemalRmadhn/photopython/blob/main/Talitha1.jpg?raw=true"
    #},
    #{
       #"Name": "Kezia Fransisca H",
        #"Major": "Actuarial Science",
        #"Photo": "https://github.com/KemalRmadhn/photopython/blob/main/Kezia2.jpg?raw=true"
    #},
    #{
        #"Name": "Carissa Isaiah S",
        #"Major": "Actuarial Science",
        #"Photo": "https://github.com/KemalRmadhn/photopython/blob/main/carissa1.jpg?raw=true"
    #}
#]

#cols = st.columns(3)
#for i, member in enumerate(team):
    #with cols[i % 3]:
        #st.image(member["Photo"], width=200)
        #st.markdown(f"**{member['Name']}**")
        #st.caption(member["Major"])

#with st.sidebar:
 #   st.header("Menu")
