# 📄🤖 ChatPDF

ChatPDF is a Streamlit-based application that enables users to interactively chat with the content of PDF documents.  
It leverages **Google PaLM (text-bison-001)** and **LangChain** to answer questions strictly based on the uploaded document.  
The system ensures contextual, document-grounded responses using vector search and retrieval.

---

## ✨ Features

- 📤 Upload PDF documents through a simple web interface  
- 📄 Extract and process text content from PDFs  
- 🧠 Generate FAISS vector embeddings for efficient semantic search  
- 💬 Ask natural language questions based only on the uploaded PDF  
- ⚡ Real-time responses powered by Google PaLM and LangChain  

---

## 🛠️ Tech Stack

| Component        | Technology Used                |
|------------------|--------------------------------|
| 🐍 Programming   | Python                          |
| 🤖 LLM           | Google PaLM (text-bison-001)    |
| 🔗 Framework     | LangChain                       |
| 📊 Vector DB     | FAISS                           |
| 🎨 Frontend     | Streamlit                       |
| 📄 PDF Parsing  | PyPDF / PDF loaders             |

---

## 📂 Project Structure

```text
ChatPDF/
├── app.py
├── requirements.txt
├── data/
│   └── uploads/
├── README.md
├── .env
```

---

## ⚙️ Installation & Setup (Using pip)

1. 📥 Clone the repository:
   ```bash
   git clone https://github.com/Sameer078/ChatPDF
   cd ChatPDF
   ```

2. 🧪 Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    
   ```
   On Windows: 
    ```bash
    venv\Scripts\activate
    ```

3. 📦 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. 🔑 Set your Google PaLM API key:
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```
   On Windows:
   ```bash
   set GOOGLE_API_KEY=your_api_key_here
   ```

---

## ⚡ Installation & Setup (Using uv)

`uv` is a fast Python package and environment manager.

1. 📥 Clone the repository:
   ```bash
   git clone https://github.com/Sameer078/ChatPDF
   cd ChatPDF
   ```

2. 📦 Initialize the project:
   ```bash
   uv init .
   ```

3. 🧪 Create a virtual environment using uv:
   ```bash
   uv venv
   ```

4. ▶️ Activate the virtual environment:
   ```bash
   .venv/Scripts/activate
   ```
   On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

5. 📦 Install dependencies from requirements.txt:
   ```bash
   uv add -r requirements.txt
   ```

6. 🔑 Set your Google PaLM API key:
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```
   On Windows:
   ```bash
   set GOOGLE_API_KEY=your_api_key_here
   ```

---



## ▶️ How to Run the Project

🚀 Run the Streamlit application:

```bash
streamlit run main.py
```

---


## 🔮 Future Enhancements

- 📚 Support for multiple PDF uploads  
- 💾 Persistent vector storage across sessions  
- 🧠 Conversation memory for follow-up questions  
- 🪄 Improved document chunking and metadata filtering  
- 🎨 Enhanced UI with response citations  

---

