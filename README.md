# Chatbot-LLM

Chatbot-LLM is a small-scale chatbot application designed to provide customer support using a Language Model (LLM). It serves as a minimalist customer support chatbot enriched by OpenAI's Language Model, and it can answer user queries effectively.

## Features

- **Vector Database Integration**: Chatbot-LLM leverages a vector database that contains relevant information needed to respond to customer queries. You can easily create and update this database using functions provided in the 'utils' module. It supports two methods of populating the database:

  - **Web Scraping**: You can specify a website link, and the chatbot will extract and store the relevant information from the webpage.

  - **File Upload**: Alternatively, you can provide a file containing the necessary information, and the chatbot will use this data as a reference for answering user queries.

- **Web Search Integration**: In addition to the saved data in the vector database, the chatbot can perform web searches to retrieve information if needed. However, for simplicity, the chatbot primarily relies on the saved data.

- **User Interaction**: Users can interact with the chatbot by asking questions, and the chatbot will provide relevant answers based on the stored data.

- **Langchain and ChainLit Integration**: Chatbot-LLM is built using Langchain, a library for integrating LLMs, and ChainLit, a framework for creating conversational agents. These libraries enable seamless integration of language models and chatbot functionalities.

## Getting Started

To use Chatbot-LLM, follow these steps:

1. **Install Dependencies**: Make sure you have all the required dependencies installed. You may need libraries for web scraping, vector storage (e.g., FAISS), OpenAI's Language Model, Langchain, and ChainLit.

2. **Set Up OpenAI API Key**: Set your OpenAI API key as an environment variable to enable the chatbot to use the language model effectively.

3. **Create the Vector Database**:

   - Use the provided functions in the 'utils' module to populate the vector database. You can do this by specifying a website link or uploading a file with relevant information.

4. **Run the Chatbot**: Start the chatbot application, and it will use the vector database to respond to user queries.

## Usage

- Users can interact with the chatbot by entering questions or queries.
- The chatbot will search its vector database for relevant answers and respond accordingly.
- If the chatbot cannot find an answer in its database, it may perform web searches to retrieve information.
- For ease of use, web searches are limited to using the saved data.

## Contributing

If you want to contribute to Chatbot-LLM or have suggestions for improvements, please feel free to submit pull requests or open issues in the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to OpenAI for providing the language model used in this chatbot.
- Thanks to Langchain and ChainLit for enabling LLM integration and chatbot development.

Happy Chatbotting!
