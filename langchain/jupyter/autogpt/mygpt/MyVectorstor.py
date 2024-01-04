from langchain.embeddings import OpenAIEmbeddings
import faiss
from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore


class VectorStore:
    def __init__(self):
        self.embeddings_model = OpenAIEmbeddings()
        self.embedding_size = 1536
        self.index = faiss.IndexFlatL2(self.embedding_size)
        self.vectorstore = FAISS(self.embeddings_model.embed_query, self.index, InMemoryDocstore({}), {})
        

