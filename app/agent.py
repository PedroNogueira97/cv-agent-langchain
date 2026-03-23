from langchain.agents import create_agent
from .model import model
from .memory import memory
from .prompt import SYSTEM_PROMPT

agent = create_agent(
    model,
    tools=[],
    system_prompt=SYSTEM_PROMPT,
    name="cv-agent",
    debug=False,
    checkpointer=memory
)

def run_agent(message: str, nome: str, email: str, telefone: str, linkedin: str, github: str, titulo: str, resumo: str, stack: str, projetos: str, experiencia: str, idiomas: str, cursos: str, formacao: str, thread_id: str, vaga: str):
    user_information = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "linkedin": linkedin,
        "github": github,
        "titulo": titulo,
        "resumo": resumo,
        "stack": stack,
        "projetos": projetos,
        "experiencia": experiencia,
        "idiomas": idiomas,
        "cursos": cursos,
        "formacao": formacao
    }
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }
    response = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": message + "\n\n" + str(user_information) + "\n\n" + vaga}
            ]
        }, config=config
    )

    return response["messages"][-1].content

