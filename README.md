# CV Project LangChain

Agente inteligente para otimização de currículos baseado em vagas específicas.

## Como Executar Localmente

1. Instale as dependências:

   ```bash
   uv sync
   ```

2. Configure as variáveis de ambiente:

   ```bash
   cp .env.example .env
   # Edite o .env com sua OPENAI_API_KEY
   ```

3. Execute o servidor:

   ```bash
   uv run run_backend.py
   ```

## Deploy com Docker

1. Certifique-se de ter o Docker instalado.
2. Build e execução:

   ```bash
   docker compose up --build
   ```

3. A API estará disponível em `http://localhost:8000`.

## Testes de Integração

Após iniciar o servidor, execute:

```bash
python test_integration.py
```
