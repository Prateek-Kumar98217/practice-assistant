from utils.embedding import vectorstore
from utils.logger import timed_node

class MemoryRetrieverNode:
    def __init__(self, k: int = 4):
        self.k = k

    @timed_node("memory_retriever")
    def __call__(self, state: dict) -> dict:
        user_input = state.messages[-1]
        docs = vectorstore.similarity_search(user_input, k=self.k)
        retrieved = "\n".join(doc.page_content for doc in docs)

        print(f"[Memory Retriever]: {retrieved}")

        return {
            **state.dict(),
            "memories": retrieved
        }
