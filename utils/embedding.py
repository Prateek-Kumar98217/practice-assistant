import os
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.embeddings import HuggingFaceEmbeddings

# Path to save/load FAISS index
VECTORSTORE_PATH = "faiss_index"

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Try loading existing index
if os.path.exists(VECTORSTORE_PATH):
    vectorstore = FAISS.load_local(VECTORSTORE_PATH, embedding_model, allow_dangerous_deserialization=True)
else:
    vectorstore = FAISS.from_documents([Document(page_content="")], embedding_model)
    vectorstore.save_local(VECTORSTORE_PATH)
