import requests
import json

def test_chat():
    url = "http://localhost:8000/chat"
    payload = {
        "message": "Teste de integração",
        "nome": "Usuário Teste",
        "email": "test@example.com",
        "telefone": "11999999999",
        "linkedin": "https://linkedin.com/in/test",
        "github": "https://github.com/test",
        "titulo": "Desenvolvedor",
        "resumo": "Resumo de teste",
        "stack": "Python, FastAPI",
        "projetos": "Projeto X",
        "experiencia": "Experiência Y",
        "idiomas": "Inglês",
        "cursos": "Curso Z",
        "formacao": "Formação W",
        "thread_id": "test-thread",
        "vaga": "Vaga de teste"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=60)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        if response.status_code == 200:
            print("[\u2713] Teste de integração passou!")
        else:
            print("[X] Teste de integração falhou!")
    except Exception as e:
        print(f"[X] Erro ao conectar com o servidor: {e}")

if __name__ == "__main__":
    # Certifique-se de que o servidor está rodando antes de executar este teste
    print("Iniciando teste de integração...")
    test_chat()
