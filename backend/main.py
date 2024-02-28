from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pickle
from io import BytesIO
import base64

app = FastAPI()

# CORS middleware'ini ekleyerek cross-origin isteklere izin ver
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Önceden eğitilmiş modeli yükle
with open("pipe.pkl", "rb") as file:
    loaded_pipe = pickle.load(file)

@app.get("/generate-image")
def generate_image(prompt: str = "Adolf Hitler"):
    image = loaded_pipe(prompt).images[0]
    
    # Görüntüyü bir BytesIO nesnesine kaydet
    image_bytes = BytesIO()
    image.save(image_bytes, format="PNG")
    
    # BytesIO nesnesini kullanarak base64'e kodla
    image_base64 = base64.b64encode(image_bytes.getvalue()).decode()
    
    # Base64 kodunu içeren bir JSON yanıtı döndür
    return {"image_base64": image_base64}
