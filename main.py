import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ChatRequest
from app.agent import run_agent
import sys
import os
import uvicorn

# Adiciona o diretório atual ao path para que o pacote 'api' seja encontrado
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: ChatRequest):
    logger.info(f"Received chat request for user: {request.nome}")
    response = run_agent(
        message=request.message,
        nome=request.nome,
        email=request.email,
        telefone=request.telefone,
        linkedin=request.linkedin,
        github=request.github,
        titulo=request.titulo,
        resumo=request.resumo,
        stack=request.stack,
        projetos=request.projetos,
        experiencia=request.experiencia,
        idiomas=request.idiomas,
        cursos=request.cursos,
        formacao=request.formacao,
        thread_id=request.thread_id,
        vaga=request.vaga
    )
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)