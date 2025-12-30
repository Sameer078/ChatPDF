import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os
from langchain_google_genai import GoogleGenerativeAI
import PyPDF2
from dotenv import load_dotenv
load_dotenv() 

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ["GOOGLEAI_API"], temperature=0.1)

# Initialize instructor embeddings using the Hugging Face model
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
vectordb_file_path = "faiss_index"

def create_vector_db(data):
    # Create a FAISS instance for vector database from 'data'
    vectordb = FAISS.from_texts(data, embedding=instructor_embeddings)
    # Save vector database locally
    vectordb.save_local(vectordb_file_path)
    
def qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings,allow_dangerous_deserialization=True)
     # Create a retriever for querying the vector database (similarity search >70%)
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain


st.title("Chat with pdf - Google palm")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("Here is the PDF you uploaded:")
    st.write(uploaded_file)
    # Open and read the PDF file using PyPDF2
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    total_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num] 
        total_text += page.extract_text()

    btn = st.button("Create Knowledgebase(vectordb)")
    if btn:
        create_vector_db(total_text)

    question = st.text_input("Question: ")
    if question:
        chain = qa_chain()
        response = chain(question)

        st.header("Answer")
        st.write(response["result"])
