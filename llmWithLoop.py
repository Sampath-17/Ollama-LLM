from llm_axe import OnlineAgent, OllamaChat
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# ola = OllamaChat(model="tinyllama")
ola = OllamaChat(model="qwen3:4B")
ola = OnlineAgent(ola)
print(ola.search("Hello, how can I help you today?"))
while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "stop"]:
        print("Goodbye!")
        break
    response = ola.search(user_input)
    print("Assistant:", response)
