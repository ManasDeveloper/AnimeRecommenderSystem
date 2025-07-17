import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st 
from pipeline.pipeline import AnimeReccomendationPipeline 
from dotenv import load_dotenv




st.set_page_config(page_title="Anime Recommender",layout="wide")
load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeReccomendationPipeline(persist_dir="chroma_db")

pipeline = init_pipeline()

st.title("Anime Reccomender System")
query = st.text_input("Enter your anime preferences e.g : light hearted anime with school settings")

if query:
    with st.spinner("Fetching recommendations..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)