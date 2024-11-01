from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.schema.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain.vectorstores.chroma import Chroma

def load_documents(directory):
    document_loader = PyPDFDirectoryLoader(directory)
    return document_loader.load()

def split_documents(documents:list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=80,
        chunk_overlap=80,
        length_function = len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

def get_embedding_function():
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )
    return embeddings

def add_to_chroma(chunks: list[Document]):
    CHROMA_PATH = "chroma"
    db = Chroma (
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function()
    )

    db.add_documents(new_chunks,ids=new_chunk_ids)

documents_directory = 'recruiter_ai/CVs'

documents = load_documents(documents_directory)
chunks = split_documents(documents)

# print(documents)
# print(chunks[0])
last_page_id = None
current_chunk_index = 0

for chunk in chunks:
    source = chunk.metadata.get('source')
    page = chunk.metadata.get('page')
    current_page_id = f"{source}:{page}"

    if current_page_id == last_page_id:
        current_chunk_index += 1
    else:
        current_chunk_index = 0

    chunk_id = f"{current_page_id}:{current_chunk_index}"

    chunk.metadata['id'] = chunk_id  



