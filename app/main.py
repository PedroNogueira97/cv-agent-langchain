import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import ChatRequest
from .agent import run_agent

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
        job=request.job
    )
    return {"response": response}

