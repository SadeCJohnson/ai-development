from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import OpenAIEmbeddings 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS # faiss -> Facebook AI Similarity Search library
from dotenv import load_dotenv
import newrelic.agent
from langchain.callbacks import StdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager

# New Relic AI Monitoring - STEP 1
from nr_openai_observability import monitor
from nr_openai_observability.langchain_callback import NewRelicCallbackHandler

load_dotenv()

# Initialize New Relic CallBack Handler, for the AI Monitoring - STEP 2
new_relic_monitor = NewRelicCallbackHandler()

embeddings = OpenAIEmbeddings()

#Youtube Video Topic: Simon Hill PROVES The Merits of A PLANT-BASED DIET | Rich Roll Podcast
video_url = "https://www.youtube.com/watch?v=a3PjNwXd09M"

@newrelic.agent.background_task()
def create_vector_db_from_youtube_url(video_url:str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url) #load the youtube video from the url
    transcript = loader.load()  #saves the video into the transcript variable

    #because there is a token limit on how much info we can send to openai, we split the amount of context we send for a youtube transcript
    #this demo uses the GPT3.5 model, specifically the gpt-3.5-turbo, which has a context window of 4096 tokens
    #so we're splitting it and storing it into vector stores
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db 

@newrelic.agent.background_task()
def get_response_from_query(db, query, k=4): #k represents the # of Documents to send to stay within the token context window
    #gpt-3.5-turbo has a context window of 4096 tokens

    docs = db.similarity_search(query, k=k) #this will only search the documents relevant to the user's query
    docs_page_content = " ".join([d.page_content for d in docs]) #combines the 4 docs into a single doc

    #Work with the LLM - 
    llm = ChatOpenAI(model="gpt-3.5-turbo") 
    #Work with the Prompt
    prompt = PromptTemplate(
        input_variables=["question", "docs"], #docs is the similarity search
        template="""
        You are a helpful  Virtual Health Coach that can answer questions about the plant based lifestyle
        based on the video's transcript.input_types=
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}

        Only use the factual information from the transcript to answer the question.input_types=
        
        
        Your answers should be detailed.
        """,
    )
#TODO: This belongs on line 66 to prevent the AI Hallucination: If you feel like you don't have enough information to answer the question, say "I don't know"

    #Work with the Chain component
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the Langchain module with the New Relic Callback - STEP 3
    response = chain.run(question=query, docs=docs_page_content, callbacks=[new_relic_monitor])
    response = response.replace("\n", "") #formatting
    return response, docs 