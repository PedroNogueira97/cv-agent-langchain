from fastapi import FastAPI
from .schemas import ChatRequest
from .agent import run_agent

app = FastAPI()

@app.post("/chat")
async def chat(request: ChatRequest):
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