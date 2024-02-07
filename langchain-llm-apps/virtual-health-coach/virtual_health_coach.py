from langchain.document_loaders import YoutubeLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.llms.openai import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores.faiss import FAISS # faiss -> Facebook AI Similarity Search library
from dotenv import load_dotenv

# New Relic AI Monitoring - STEP 1
from nr_openai_observability.langchain_callback import NewRelicCallbackHandler
#Instrument New Relic's OpenAAI Observability tool 
from nr_openai_observability import monitor

load_dotenv()

# Initialize New Relic CallBack Handler, for the AI Monitoring - STEP 2
new_relic_monitor = NewRelicCallbackHandler("SCJ's Virtual Health Coach", license_key="<INSERT YOUR KEY HERE>")

#Create model monitor
monitor.initialization(application_name="SCJ's Virtual Health Coach", license_key="<INSERT YOUR KEY HERE")

embeddings = OpenAIEmbeddings()

#Youtube Video Topic: Simon Hill PROVES The Merits of A PLANT-BASED DIET | Rich Roll Podcast
video_url = "https://www.youtube.com/watch?v=a3PjNwXd09M"


def create_vector_db_from_youtube_url(video_url:str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url) #load the youtube video from the url
    transcript = loader.load()  #saves the video into the transcript variable

    #because there is a token limit on how much info we can send to openai, we split the amount of context we send for a youtube transcript
    #this demo uses the GPT3.5 model, specifically the text-davinci-003, which has a context window of 4096 tokens
    #so we're splitting it and storing it into vector stores
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db #returns a hex value such as: <langchain.vectorstores.faiss.FAISS object at 0x123ec12d0>
    #return docs #returns the chunk of data

#print(create_vector_db_from_youtube_url(video_url)) #included for testing purposes


def get_response_from_query(db, query, k=4): #k represents the # of Documents to send to stay within the token context window
    #gpt-3.5-turbo-instruct has a context window of 4096 tokens

    docs = db.similarity_search(query, k=k) #this will only search the documents relevant to the user's query
    docs_page_content = " ".join([d.page_content for d in docs]) #combines the 4 docs into a single doc

    #Work with the LLM - 
    llm = OpenAI(model="gpt-3.5-turbo-instruct") 
    #Work with the Prompt
    prompt = PromptTemplate(
        input_variables=["question", "docs"], #docs is the similarity search
        template="""
        You are a helpful YouTube assistant that can answer questions about videos
        based on the video's transcript.input_types=
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}

        Only use the factual information from the transcript to answer the question.input_types=
        
        
        Your answers should be detailed.
        """,
    )
# This belongs on line 66 to prevent the AI Hallucination: If you feel like you don't have enough information to answer the question, say "I don't know"

    #Work with the Chain component
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the Langchain module with the New Relic Callback - STEP 3
    response = chain.run(question=query, docs=docs_page_content)
  #  print("Agent has successfully completed.")
    response = response.replace("\n", "") #formatting
    return response, docs 