import chromadb
import uuid
from pathlib import Path
import os

_client = None
_collection = None


def get_client():
    global _client
    if _client is None:
        _client = chromadb.PersistentClient(path="./chroma_data")
    return _client

def get_collection():
    global _collection
    if _collection is None:
        client = get_client()
        name = "testMagenta"
        try:
            _collection = client.get_collection(name=name)
        except Exception:
            _collection = client.create_collection(name=name)
    return _collection

def index_documents(texts_directory: str = None):
    if texts_directory is None:
        texts_directory = "./texts"
    directory = Path(texts_directory)
    if not directory.is_dir():
        raise FileNotFoundError(f"Папка '{texts_directory}' не найдена")
    
    collection = get_collection()
    NAMESPACE = uuid.NAMESPACE_DNS
    ids=[]
    documents=[]
    metadatas=[]

    for file_path in directory.glob("*.md"):
        with file_path.open("r", encoding="utf-8") as f:
            content = f.read()
            doc_id = str(uuid.uuid5(NAMESPACE, file_path.name))
            ids.append(doc_id)
            documents.append(content)
            metadatas.append({"source": file_path.name})

    if documents:
        collection.upsert(ids=ids, documents=documents, metadatas=metadatas)
        return len(documents)
    return 0

def query_documents(question: str, n_results: int = None):
    if n_results is None:
        n_results = int(os.getenv("N_RESULTS", "3"))
    collection = get_collection()
    results = collection.query(query_texts=[question], n_results=n_results)
    return results["documents"][0] if results["documents"] else []


