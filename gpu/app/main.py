# Packages Import
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModel
import torch
# Custom Modules Import
from app.schemas import QueryInput

# Setting device as cpu/gpu
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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
tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-large-en-v1.5')
model = AutoModel.from_pretrained('BAAI/bge-large-en-v1.5').to(device)
model.eval()

def embedding_encode(data) -> list:
    encoded_input = tokenizer([data], padding=True, truncation=True, return_tensors='pt').to(device)
    with torch.no_grad():
        model_output = model(**encoded_input)
        sentence_embeddings = model_output[0][:, 0]
    sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1).tolist()
    return sentence_embeddings


@app.post("/predict")
async def predict(data : QueryInput):
    return embedding_encode(data.sentence)
