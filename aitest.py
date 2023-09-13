#chromadb = vectorel db 
import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

#db ye geçici olarak veri verdim(persist değil)
collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)
 
import os
#api_key
os.environ['OPENAI_API_KEY'] = "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"
 #pet klasörürün içine gir ve oradaki tüm txt dosyalarını parçala
def read_files_from_folder(folder_path):
    file_data = []
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path,file_name), 'r') as file:
                content = file.read()
                file_data.append({"file_name": file_name, "content":content})
    
    return file_data

folder_path = "pets"
file_data = read_files_from_folder(folder_path)


documents = []
metadatas = []
ids = []
#file_datadan gelen verileri ayıkla
for index,data in enumare(file_data):
    documents.append(data['content'])
    metadatas.append({'source': data['file_name']})
    ids.append(str(index+1))
#vector db'e bir collection aç
pet_collection = client.create_collection("pet_collection")
#collection bulunan verileri ekle

pet_collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

sor=input("Döküman ara : ")
results=pet_collection.query(
    query_texts=["Kediler neyi sever?"]
    n_results=1
)
print(results)