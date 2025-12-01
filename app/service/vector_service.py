from typing import List, Dict, Any, Optional
from .embedding_service import EmbeddingService
from ..repository.vector_repo import VectorRepository


class VectorService:
    def __init__(self, vector_repository: VectorRepository, embedding_service: EmbeddingService):
        self.vector_repository = vector_repository
        self.embedding_service = embedding_service
    
    def add_documents(self, documents: List[str], metadatas: List[Dict[str, Any]] = None, ids: List[str] = None):
        embeddings = self.embedding_service.create_embeddings(documents)
        self.vector_repository.add_documents(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
    
    def search(self, query: str, n_results: int = 5) -> Dict[str, Any]:
        query_embedding = self.embedding_service.create_embedding(query)
        
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )
        
        return {
            "documents": results["documents"][0],
            "metadatas": results["metadatas"][0],
            "distances": results["distances"][0]
        }
    
    def delete_document(self, doc_id: str):
        self.collection.delete(ids=[doc_id])
    
    def get_collection_info(self) -> Dict[str, Any]:
        return {
            "name": self.collection.name,
            "count": self.collection.count(),
            "metadata": self.collection.metadata
        }