import os
import chainlit as cl
import pickle
from langchain import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.chains import RetrievalQAWithSourcesChain

# Import the OpenAI API key from a secret key file
from utils.secretkey import openai_api_key
os.environ["OPENAI_API_KEY"] = openai_api_key

# Initialize the Langchain model
llm = OpenAI(temperature=0.9, max_tokens=500)

import chainlit as cl
from langchain.agents import initialize_agent, Tool

# Path to the FAISS vectorstore pickle file
file_path = 'vectordb.pkl'

# Define a function to answer questions using the vectorstore
def answer(query):
    with open(file_path, "rb") as f:
        vectorstore = pickle.load(f)
        # Create a RetrievalQAWithSourcesChain using Langchain and the vectorstore
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
        # Execute the chain with a question and return the answer
        result = chain({"question": query}, return_only_outputs=True)
        return result["answer"]

# Define the main function for initializing the chatbot
@cl.on_chat_start
def main():
    # Define a list of tools, in this case, only one tool for answering questions
    tools = [
        Tool(
            name='search answer',
            func=answer,
            description="""Useful to get answers to the questions users ask. Call the function answer(query)"""
        ),
    ]

    # Initialize the chatbot agent with the defined tools and Langchain model
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="chat-zero-shot-react-description",
        verbose=True
    )
    cl.user_session.set("agent", agent)

# Define an asynchronous message handler
@cl.on_message
async def out(message):
    agent = cl.user_session.get('agent')
    cb = cl.LangchainCallbackHandler(stream_final_answer=True)
    await cl.make_async(agent.run)(message, callbacks=[cb])
