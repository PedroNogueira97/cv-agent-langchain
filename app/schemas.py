from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    nome: str
    email: str
    telefone: str
    linkedin: str
    github: str
    titulo: str
    resumo: str
    stack: str
    projetos: str
    experiencia: str
    idiomas: str
    cursos: str
    formacao: str
    vaga: str
    thread_id: str