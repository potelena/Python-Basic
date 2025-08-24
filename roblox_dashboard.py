import re
from urllib.parse import urlparse
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="My Roblox Links Dashboard",
    page_icon="🎮",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        .stApp {
            background-color: #E6D5B8; /* pastel brown background */
        }
        .game-card {
            background-color: #f9f3e7; /* lighter pastel box */
            border-radius: 15px;
            padding: 15px;
            margin: 10px 0;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.2s ease-in-out;
        }
        .game-card:hover {
            transform: scale(1.03);
            box-shadow: 4px 4px 14px rgba(0,0,0,0.15);
        }
        .game-title {
            font-size: 18px;
            font-weight: bold;
            color: #3e2f20;
            margin-bottom: 8px;
        }
        .game-link {
            background-color: #e6c3a2;
            color: #3e2f20;
            padding: 6px 12px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.2s;
        }
        .game-link:hover {
            background-color: #d9ad8c;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.title(" My Roblox Links Dashboard")

# --- DATA ---
LINKS = [
    "https://www.roblox.com/games/286090429/Arsenal",
    "https://www.roblox.com/games/142823291/Murder-Mystery-2",
    "https://www.roblox.com/games/126884695634066/Grow-a-Garden",
    "https://www.roblox.com/games/15101393044/LADY-GAGA-Dress-To-Impress",
    "https://www.roblox.com/games/79546208627805/99-Nights-in-the-Forest",
    "https://www.roblox.com/games/109983668079237/Steal-a-Brainrot",
    "https://www.roblox.com/games/9872472334/Evade",
    "https://www.roblox.com/games/6516141723/DOORS",
    "https://www.roblox.com/games/1962086868/Tower-of-Hell",
    "https://www.roblox.com/games/17625359962/RIVALS",
    "https://www.roblox.com/games/4375619868/Koha-Hibachi-Restaurant",
    "https://www.roblox.com/games/5985232436/Infectious-Smile-SUMMER",
    "https://www.roblox.com/games/6872265039/BedWars-NEW-ITEMS",
    "https://www.roblox.com/games/4738545896/SHOOT-OUT",
]

# --- HELPER FUNCTION ---
def extract_game_name(url: str) -> str:
    path = urlparse(url).path
    parts = path.strip("/").split("/")
    if len(parts) >= 3:
        return parts[2].replace("-", " ")
    return "Unknown Game"
st.markdown("""
    <style>
        /* Picnic blanket background */
        .stApp {
            background-color: #E6D5B8;  /* pastel base */
            background-image: 
                linear-gradient(45deg, #f5e6d3 25%, transparent 25%), 
                linear-gradient(-45deg, #f5e6d3 25%, transparent 25%),
                linear-gradient(45deg, transparent 75%, #f5e6d3 75%),
                linear-gradient(-45deg, transparent 75%, #f5e6d3 75%);
            background-size: 60px 60px;   /* bigger squares for aesthetic */
            background-position: 0 0, 0 30px, 30px -30px, -30px 0px;
        }
    </style>
""", unsafe_allow_html=True)

# --- LAYOUT: 3 per row ---
cols_per_row = 3
for i, link in enumerate(LINKS):
    if i % cols_per_row == 0:
        cols = st.columns(cols_per_row)
    with cols[i % cols_per_row]:
        game_name = extract_game_name(link)
        st.markdown(
            f"""
            <div class="game-card">
                <div class="game-title">{game_name}</div>
                <a href="{link}" target="_blank" class="game-link">👉 Play Now</a>
            </div>
            """,
            unsafe_allow_html=True
        )
st.markdown("""
    <style>
        /* Import a cute Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;700&display=swap');

        /* Apply font globally */
        .stApp, h1, h2, h3, h4, h5, h6, p, a {
            font-family: 'Baloo 2', cursive;
        }

        /* Optional: style game cards slightly with font */
        .game-card {
            font-family: 'Baloo 2', cursive;
        }
    </style>
""", unsafe_allow_html=True)


       # Sort options
sort_option = st.selectbox(
    "Sort games by:",
    ["Default", "A → Z", "Z → A"]
)

# Apply sorting
if sort_option == "A → Z":
    LINKS = sorted(LINKS, key=lambda x: extract_game_name(x).lower())
elif sort_option == "Z → A":
    LINKS = sorted(LINKS, key=lambda x: extract_game_name(x).lower(), reverse=True)
    
             
