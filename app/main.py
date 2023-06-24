from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat_bot.qa_handler import ask_question
from pydantic import BaseModel, Field


app = FastAPI()

origins = ["http://localhost:8080"]

#CORSを回避
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str = Field(title="Request message to LLM.", max_length=1000)

class LLMResponse(BaseModel):
    text: str

@app.get("/test")
def test():
    return {}

@app.post("/llm")
def response (message:Message) ->LLMResponse:
    answer = ask_question(message.text)
    return LLMResponse(text=answer)
    