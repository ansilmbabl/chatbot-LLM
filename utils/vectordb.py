import pickle
import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Import the OpenAI API key from a secret key file
from .secretkey import openai_api_key
os.environ["OPENAI_API_KEY"] = openai_api_key

def create_vectordb(urls):
    # Initialize a loader to fetch content from the provided URLs
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    # Define a text splitter to split the loaded data into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    docs = text_splitter.split_documents(data)

    # Create embeddings using OpenAI's model
    embeddings = OpenAIEmbeddings()

    # Create a vector store using FAISS from the split documents and embeddings
    vectorstore_openai = FAISS.from_documents(docs, embeddings)

    # Define the file path to save the vector store
    file_path = 'vectordb.pkl' 

    # Serialize and save the vector store to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

def webscrap(url, query):
    # Import necessary modules and classes from Langchain
    from langchain.docstore.document import Document
    from langchain.indexes import VectorstoreIndexCreator
    from langchain.utilities import ApifyWrapper

    # Create an ApifyWrapper instance
    apify = ApifyWrapper()

    # Call an Apify actor to crawl website content based on the provided URL
    loader = apify.call_actor(
        actor_id="apify/website-content-crawler",
        run_input={"startUrls": [{"url": url}]},
        dataset_mapping_function=lambda item: Document(
            page_content=item["text"] or "", metadata={"source": item["url"]}
        ),
    )

    # Create a vector store based on the crawled data
    index = VectorstoreIndexCreator().from_loaders([loader])

    # Query the vector store using the provided query
    result = index.query(query)

    # Print the query result (you can modify this part to return or process the result differently)
    print(result)
