from chromadb.config import Settings
import chromadb

# Railway project URL (exclude https://)
CHROMA_HOST = "your-project.up.railway.app"

client = chromadb.HttpClient(Settings(
    chroma_api_impl="rest",
    chroma_server_host=CHROMA_HOST,
    chroma_server_http_port=443,
    chroma_server_ssl_enabled=True
))

# collection = client.get_or_create_collection("example_collection")
# collection.add(documents=["Hello from Railway!"], ids=["1"])

# results = collection.query(query_texts=["Hello"], n_results=1)
# print(results)
