from pydantic import BaseModel, Field

class GenerateRequest(BaseModel):
    prompt: str = Field(..., description="Input prompts text", examples=["Hello"])
    client: str = Field(..., description="Client name", examples=["openai"])