from dataclasses import dataclass

@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    punny_response: str
    user_information: str | None = None