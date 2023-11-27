import streamlit as st
import youtube_assistant as yta 
import textwrap #Gives the ability to wrap text so we don't have to scroll the page


st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key="my_form"):
        youtube_url = st.sidebar.text_area(
            label="Enter the url for the YouTube video: ",
            max_chars=50 #don't want the video url to exceed 50 characters
        )

        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
        )


        submit_button = st.form_submit_button(label='Submit')


if query and youtube_url: #if both of the paramaters exist
     db = yta.create_vector_db_from_youtube_url(youtube_url)
     response, docs = yta.get_response_from_query(db, query)
     st.subheader("Answer:")
     st.text(textwrap.fill(response, width = 85))