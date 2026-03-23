# In-memory store for user and job data
# In a real application, this would be a database.

user_store = {}
job_store = {}

def save_user_info(thread_id: str, info: dict):
    user_store[thread_id] = info

def get_user_info(thread_id: str) -> dict:
    return user_store.get(thread_id, {})

def save_job_info(thread_id: str, info: str):
    job_store[thread_id] = info

def get_job_info(thread_id: str) -> str:
    return job_store.get(thread_id, "")
