from langchain.tools import tool
from langchain_core.runnables import RunnableConfig
from .store import get_user_info, get_job_info

@tool
def get_user_information(config: RunnableConfig) -> str:
    """Get the user's personal and professional information (CV data)."""
    thread_id = config.get("configurable", {}).get("thread_id")
    if not thread_id:
        return "Error: No thread_id found in config."
    
    info = get_user_info(thread_id)
    if not info:
        return "No user information found for this session."
    return str(info)

@tool
def get_job_information(config: RunnableConfig) -> str:
    """Get the information about the job vacancy/position."""
    thread_id = config.get("configurable", {}).get("thread_id")
    if not thread_id:
        return "Error: No thread_id found in config."
    
    info = get_job_info(thread_id)
    if not info:
        return "No job information found for this session."
    return info
