from langchain_core.documents import Document
from utils.embedding import vectorstore
from utils.logger import timed_node

class MemoryUpdaterNode:
    def __init__(self):
        pass

    @timed_node("memory_updater")
    def __call__(self, state: dict) -> dict:
        memory = getattr(state, "structured_memory")
        if not memory:
            return state

        formatted = f"{memory['type']} | {memory['topic']} | {memory['content']} | source: {memory['source']}"
        doc = Document(page_content=formatted)
        vectorstore.add_documents([doc])
        vectorstore.save_local("faiss_index")

        print(f"[Memory Retriver]: Retrieved {doc}")

        return state
