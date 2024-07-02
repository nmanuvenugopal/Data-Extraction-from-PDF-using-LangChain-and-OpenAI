import os
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.vectorstores.faiss import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA


### Setting the environment variable
os.environ["OPENAI_API_KEY"] = "Your API key"

### We need to load the PDF first
document_loader = PyMuPDFLoader('/Users/manuvenugopal/Documents/Working on Docs/Input_files/ms-partner-agreement.pdf')
document = document_loader.load()
#print(document)

### We need to split the document into smaller chunks
text_splitter  = RecursiveCharacterTextSplitter(chunk_size =500, chunk_overlap = 64)
texts = text_splitter.split_documents(documents=document)
print(texts)

# After splitting the document we need to embedd it and store it in vector store
embedding = OpenAIEmbeddings()
index = FAISS.from_documents(texts, embedding=embedding)
retriever = index.as_retriever()

# Now we can ask questions and use defferent model to answer that question
llm_35 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
rqa_35 = RetrievalQA.from_chain_type(llm=llm_35, retriever=retriever, chain_type="stuff")

llm_4o = ChatOpenAI(model="gpt-4o", temperature=0)
rqa_4o = RetrievalQA.from_chain_type(llm=llm_4o, retriever=retriever, chain_type="stuff")

## Calling above function 

while True:
    input_query = input("Enter the query: ")
    if input_query.lower() == "exit":
        break
    else:
        prompt = f"### prompt: {input_query}"
        llm_response_35 = rqa_35(prompt)
        print(f"The output from GPT3.5 turbo model is: {llm_response_35['result']}")
        
        llm_response_4o = rqa_4o(prompt)
        print(f"The output from GPT4o model is {llm_response_4o['result']}")