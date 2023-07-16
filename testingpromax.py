import sys
import os
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.retrieval_qa.base import RetrievalQA
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

documents = []
for file in os.listdir("files"):
    if file.endswith(".pdf"):
        pdf_path = "./files/" + file
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())
    elif file.endswith('.txt'):
        text_path = "./files/" + file
        loader = TextLoader(text_path)
        documents.extend(loader.load())

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
documents = text_splitter.split_documents(documents)

vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY), persist_directory="./data")
vectordb.persist()

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# llm = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.8) , vectordb.as_retriever(), memory=memory)
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo-16k",
    temperature=0,
    openai_api_key=OPENAI_API_KEY,
    max_tokens=4097,
)
prompt_template = """

I am athenabot, My name is athenabot.

Our Purpose, We are "Building a technology startup can be an exciting and rewarding journey. 
As a woman looking to convert your business idea into a technology business, 
it's essential to have a clear roadmap to guide you along the way. 
Here's our guide to help you build a technology startup 🏗️💻🚀"

When User Says Hi, Ask him these options / Message:

Remember the very 1st message should be "Welcome, I'm Athena and I'm here to help you and 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered 
 1: Learn 📚 
 2: Ask a question 🙋🏻‍♀️

When User Select 1st option which is learn show him these options:

1 - Idea Validation
2 - Business Planning
3 - Product Development
4 - User Acquisition
5 - Funding and Finance
6 - Growth and Scaling

And Furthure Explain from the data. If User says next go to the next throught the course. act like a fun teacher and use emoji's as well, don't act like a bot.

{context}

Question: {question}"""
SALES_PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

the_qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectordb.as_retriever(),
    chain_type_kwargs={"prompt": SALES_PROMPT},
    memory=memory
)

def chatbotHandler(message):
    query = message
    result = the_qa.run(query)
    text = result
    updated_text = text.replace("Answer", "", 1)
    return updated_text

