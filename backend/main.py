from fastapi import FastAPI,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware

import os,random

BASE_DIR = os.path.dirname(os.path.abs.path(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "User_Uploads")

app = FastAPI()

origins = [
  "http://127.0.0.1:5500/"
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "API bağlantısı sağlandı."}

users= [
    {"id": 124, "name":"ömer", "role": "admin"},
    {"id": 12, "name":"ceren", "role": "user"},
    {"id": 132, "name":"kerem", "role": "user"},
]


@app.get("/users")
async def handle_users():
    
    return{"data": users}


#tekil kullanıcıyı al
@app.get("/users/{user_id}")
async def handle_single_user(user_id: str):
    
    if user_id:
        for user in users:
            if user['id'] == int(user_id):
                return {"data": user}
            else:
                return{"data": "User Bulunamadı"}
            
#dosya upload etme endpointi
@app.post("/upload")
async def handle_file(dosya: UploadFile):
   
   print("dosyanin adi:", dosya.filename)
   dosya_icerik = await dosya.read()
   dosya_metin = dosya_icerik.decode("utf-8")
   print("dosyanin iceriği:", dosya_metin)
   
   #dosya adi oluştur
   id=random.randint(10000,90000)
   new_file_name = "{}-{}".format(id,dosya.filename)
   #dosyayı kaydet
   file_name = os.path.join(UPLOAD_DIR,new_file_name)
   #dosyayi aç
   with open(file_name,"wb") as f:
       f.write(dosya_icerik)
   
   return {"data" : "POST İSTEĞİNİ ALDIM"}
              