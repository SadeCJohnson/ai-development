import streamlit as st
import packaging.version
import virtual_health_coach as eHealthCoach 
import textwrap #Gives the ability to wrap text so we don't have to scroll the page


st.title(" :violet[Virtual Health Coach]")

with st.sidebar:
    with st.form(key="my_form"):
        query = st.sidebar.text_area(
            label="What is your health question?",
            max_chars=50,
            key="query"
        )
        #TODO: Implement this so the user can insert their own API key; as of now, it only pulls mine
        # openai_api_key = st.sidebar.text_input(
        #     label="Insert your [OpenAI API Key](https://platform.openai.com/api-keys):",
        #     key="youtube_assistant_search_openai_apikey",
        #     max_chars=60,
        #     type="password"
        # )
        submit_button = st.form_submit_button(label='Submit') 



if query: # and youtube_url: #if both of the paramaters exist
    # if not openai_api_key:
    #      st.info("Please insert your OpenAI API key in order to unleash the power of this Virtual Health Coach.")
    #      st.stop()
    # else:
     db = eHealthCoach.create_vector_db_from_youtube_url("https://www.youtube.com/watch?v=a3PjNwXd09M")
     response, docs = eHealthCoach.get_response_from_query(db, query)
     st.subheader("Answer:")
     st.text(textwrap.fill(response, width = 85))