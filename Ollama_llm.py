from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# llm = Ollama(model="tinyllama")
llm = Ollama(model="qwen3:4B")
template = PromptTemplate.from_template("You are a helpful assistant.Answer the question: {question}")
chain = LLMChain(llm=llm, prompt=template)

print("Assistant is ready to help you! Say quit to exit the loop.")
while True:
    user_input = input("User: ")
    if user_input:
        if user_input.lower() in ["quit", "exit", "stop"]:
            print("Goodbye!")
            break
        response = chain.run(user_input)
        print("Assistant: "+response)
