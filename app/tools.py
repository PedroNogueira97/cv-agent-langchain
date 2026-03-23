from langchain.tools import tool

@tool
def get_user_information(thread_id: str) -> str:
    """Get the user information from the thread id."""
    return f"John Doe {thread_id}"
