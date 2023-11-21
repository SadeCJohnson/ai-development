from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from dotenv import load_dotenv # This loads my OpenAI key that I have stored as an environment variable in a .env file

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)

   # Below is the hardcoded values -- because we don't want to move forward with this format, prompt templates and chains were introduced 
   # chains put the various llms components together
   # name = llm("I have a dog pet and I want a cool name for it. Suggest five cool names for my pet.")


    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it. It is {pet_color} in color. Suggest five cool names for my pet."
    )

    name_chain = LLMChain (llm=llm, prompt=prompt_template_name)

    #return name
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color}) #returns a json response
    return response


if __name__ == "__main__":
    print(generate_pet_name("cat", "black")) #returns a json response


