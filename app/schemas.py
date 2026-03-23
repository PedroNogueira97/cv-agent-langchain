from pydantic import BaseModel, Field, model_validator
from typing import Optional

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
    job: Optional[str] = None
    vaga: Optional[str] = None
    thread_id: str

    @model_validator(mode='before')
    @classmethod
    def handle_vaga_alias(cls, data):
        if isinstance(data, dict):
            if 'vaga' in data and not data.get('job'):
                data['job'] = data['vaga']
            if 'job' in data and not data.get('vaga'):
                data['vaga'] = data['job']
        return data