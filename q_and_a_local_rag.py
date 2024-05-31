from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain import hub
from langchain.chains import RetrievalQA


loader = PyPDFLoader(
"https://d18rn0p25nwr6d.cloudfront.net/CIK-0001813756/975b3e9b-268e-4798-a9e4-2a9a7c92dc10.pdf"
)
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)
embedding_function = SentenceTransformerEmbeddings(model_name="BAAI/bge-small-en-v1.5")
vectorstore = Chroma(collection_name="sample_collection", embedding_function = embedding_function)
vectorstore.add_documents(all_splits)

retriever = vectorstore.as_retriever(k=7)

llm = Ollama(model="llama3",callback_manager=CallbackManager(
            [StreamingStdOutCallbackHandler()]),stop=["<|eot_id|>"],)

query = input("\nQuery: ")
prompt = hub.pull("rlm/rag-prompt")
qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever(), chain_type_kwargs={"prompt": prompt}
)
result = qa_chain({"query": query})
print(result)






