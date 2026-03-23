from langchain.agents import create_agent
from .model import model
from .memory import memory
from .prompt import SYSTEM_PROMPT
from .tools import get_user_information, get_job_information
from .store import save_user_info, save_job_info

# Register tools
tools = [get_user_information, get_job_information]

agent = create_agent(
    model,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
    name="cv-agent",
    debug=False,
    checkpointer=memory
)

def run_agent(message: str, nome: str, email: str, telefone: str, linkedin: str, github: str, titulo: str, resumo: str, stack: str, projetos: str, experiencia: str, idiomas: str, cursos: str, formacao: str, thread_id: str, vaga: str):
    # Store session data for the tools to use
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
    
    save_user_info(thread_id, user_information)
    save_job_info(thread_id, vaga)
    
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }
    
    # Simplify the trigger message. The agent will use tools to get details.
    trigger_message = f"{message}\nUse as ferramentas disponíveis para obter as informações do meu perfil e da vaga que pretendo me candidatar."
    
    response = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": trigger_message}
            ]
        }, config=config
    )

    return response["messages"][-1].content

