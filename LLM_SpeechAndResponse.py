from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def printandspeak(text):
    print(text)
    speak(text)
    return

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say Something")
        audio = r.listen(source)
        print("Listening....")
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        text = "Sorry, I did not understand that."
        printandspeak(text)
        return None
    except sr.RequestError as e:    
        text = "Could not request results; {0}".format(e)
        printandspeak(text)
        return None
# download and use tinyllamma if your laptop has issue with qwen3:4B
# llm = Ollama(model="tinyllama")
llm = Ollama(model="qwen3:4B")
template = PromptTemplate.from_template("You are a helpful assistant.Answer the question: {question}")
chain = LLMChain(llm=llm, prompt=template)

print("Assistant is ready to help you! Say quit to exit the loop.")
while True:
    user_input = listen()
    if user_input:
        print("User Input:", user_input)
        if user_input.lower() in ["quit", "exit", "stop"]:
            printandspeak("Goodbye!")
            break
        response = chain.run(user_input)
        printandspeak(response)
      
