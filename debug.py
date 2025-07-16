from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# 🔹 Step 1: Load HuggingFace embedding model
model_name = "sentence-transformers/all-MiniLM-L6-v2"  # ya jo bhi model use kiya tha
embedding_model = HuggingFaceEmbeddings(model_name=model_name)

# 🔹 Step 2: Load the FAISS index (path yahan daal de tu)
index_path = "faiss_index"
faiss_index = FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)

# 🔹 Step 3: Access documents and print content + metadata
print("\n🔍 Documents and Metadata:\n" + "="*60)
for doc_id, doc in faiss_index.docstore._dict.items():
    print(f"🆔 ID: {doc_id}")
    print(f"📄 Content: {doc.page_content}")
    print(f"📝 Metadata: {doc.metadata}")
    print("-" * 60)

# 🔹 Step 4: Access and print embeddings
print("\n🧠 Embeddings (Vectors):\n" + "="*60)
vectors = faiss_index.index.reconstruct_n(0, faiss_index.index.ntotal)

# Done
print(f"\n✅ Total documents: {len(faiss_index.docstore._dict)}")
print(f"✅ Total vectors: {faiss_index.index.ntotal}")
