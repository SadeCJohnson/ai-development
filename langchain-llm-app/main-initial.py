#from openai import OpenAI #Got this from OpenAI's quickstart guide: https://platform.openai.com/docs/quickstart?context=python 
#from langchain.llms import OpenAI #Got this from the LangChain tutorial: https://www.youtube.com/watch?v=lG7Uxts9SXs
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI 
llm = ChatOpenAI(openai_api_key="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")


load_dotenv()

#Generate pet names
# Below is the code that I saw from the youtube tutorial
""" def generate_pet_name():
  llm=OpenAI(temperature=0.7)

  name = llm("I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet.")

  return name

if __name__ =="__main__":
  print(generate_pet_name()) """

#corrected code
#Generate pet names
def generate_pet_name():
    prompt = "I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet."
    response = OpenAI.completions.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
    )
    return response.choices[0].text

if __name__ == "__main__":
    print(generate_pet_name())