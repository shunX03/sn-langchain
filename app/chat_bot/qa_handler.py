from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
import os,app_const

os.environ["OPENAI_API_KEY"] = app_const.OPENAI_API_KEY

def ask_question(question: str) -> str:
    llm = OpenAI(temperature=0.9)
    template = """Question: {question}

    Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    answer = llm_chain.run(question)
    return answer