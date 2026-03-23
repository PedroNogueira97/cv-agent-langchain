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

#print(run_agent("Dado as informações do usuário, gere um currículo otimizado para a vaga.", "Mariana", "[EMAIL_ADDRESS]", "123456789", "https://linkedin.com/in/mariana", "https://github.com/mariana", "Desenvolvedora Web", "Desenvolvedora Web com experiência em desenvolvimento web.", "Python, JavaScript, HTML, CSS", "Projeto 1, Projeto 2", "Experiência 1, Experiência 2", "Português, Inglês", "Curso 1, Curso 2", "Formação 1, Formação 2", "1", "Vaga de Desenvolvedor Web Python Pleno - FastAPI e javascript node.js"))