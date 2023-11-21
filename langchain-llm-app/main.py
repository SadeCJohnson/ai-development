import pet_name_generator as pg #pg is short for pet generator; I didn't want to use png as that can be confusing with the PNG extension
import streamlit as st #st is short for streamlit

st.title("Pets name generator")

#allows the user to select the necessary types from a sidebar in the browser
user_animal_type = st.sidebar.selectbox("Select your pet of choice:", ("Cat", "Dog", "Cow",
                                                                  "Hamster", "Bird"))
#We selected the max character amount to be 15 so we won't be charged for too many characters
if user_animal_type == "Cat":
    pet_color = st.sidebar.text_area(label="What color is your cat?", max_chars=15)
if user_animal_type == "Dog":
    pet_color = st.sidebar.text_area(label="What color is your dog?", max_chars=15)
if user_animal_type == "Cow":
    pet_color = st.sidebar.text_area(label="What color is your cow?", max_chars=15)
if user_animal_type == "Hamster":
    pet_color = st.sidebar.text_area(label="What color is your hamster?", max_chars=15)
if user_animal_type == "Bird":
    pet_color = st.sidebar.text_area(label="What color is your bird?", max_chars=15)    


#We're going to send the info to the pet_name_generator helper file
if pet_color:
    response = pg.generate_pet_name(user_animal_type, pet_color)
    st.text(response['pet_name']) #this indexing allows us to access just the names from the response rather than the entire json response
