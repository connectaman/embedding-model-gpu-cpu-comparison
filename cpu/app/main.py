# Packages Import
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from deepsparse.sentence_transformers import DeepSparseSentenceTransformer
# Custom Modules Import
from app.schemas import QueryInput

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Loading the model in memory
model = DeepSparseSentenceTransformer('neuralmagic/bge-large-en-v1.5-quant', export=False)

def embedding_encode(data):
    embeddings = model.encode(data)
    return [embeddings.tolist()]


@app.post("/predict")
async def predict(data : QueryInput):
    return embedding_encode(data.sentence)
