from langchain.chat_models import init_chat_model

model = init_chat_model(
    "gpt-4o-mini",
    temperature=0.5,
    timeout=50,
    max_tokens=1000
)