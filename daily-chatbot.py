from langchain_ollama import OllamaLLM
from jinja2 import FileSystemLoader, Environment

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('daily-prompt.txt')

history = ""

#setting up the Ollama gemma:2b model
try:
    llm = OllamaLLM(model='gemma:2b', temperature=0.3)
    test_response = llm.invoke("Hello")
    print("✓ Connected to gemma:2b model successfully!")
except Exception as e:
    print(f"✗ Failed to connect to gemma:2b model: {str(e)}")
    print("\nPlease ensure Ollama is running and gemma:2b model is available.")
    print("Run: ollama serve (in another terminal)")
    input("Press Enter to exit...")
    exit()

print("Welcome to Dod Bot! I'm here to help with your daily enquiries.")
print("You can ask me any daily life-related questions. Type 'quit' or 'exit' to end the conversation.\n")

while True:
    user_input = input("User: ")
    if user_input.lower() == 'quit' or user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    else:
        print("Dod Bot is getting your response...")

    try:
        # Update the current question for this iteration
        current_prompt = template.render(question=user_input, history=history)
        response = llm.invoke(current_prompt)
        
        print(f"Dod Bot: {response}")
        history += f"Human: {user_input}\nDod Bot: {response}\n"
    except ConnectionError:
        print("Dod Bot: I'm having trouble connecting to the AI service. Please make sure Ollama is running.")
        print("You can start Ollama by running 'ollama serve' in a separate terminal.")
    except Exception as e:
        error_msg = str(e).lower()
        if "connection" in error_msg or "refused" in error_msg:
            print("Dod Bot: I can't connect to the AI service. Please ensure Ollama is running with the 'gemma:2b' model.")
            print("Try running: ollama serve (in another terminal)")
        elif "model" in error_msg:
            print("Dod Bot: The 'gemma:2b' model is not available. Please ensure it's installed.")
        else:
            print(f"Dod Bot: I encountered an error: {str(e)}")
            print("Please try rephrasing your question or check if Ollama is running.")
    
# print(history)