import ollama

print("Connected to Local AI Judge (Phi-3). Type 'quit' to exit.\n")
system_instruction = (
    "You are a strict but helpful Judge for the Supreme Court of India. "
    "You speak formally, reference Indian Laws (IPC, CrPC, Constitution), "
    "and provide clear legal reasoning."
)

while True:
    # 1. Get user input
    user_input = input("You: ")

    # Check if user wants to quit
    if user_input.lower() in ['quit', 'exit', 'q']:
        print("Court is adjourned.")
        break

    # 2. Send the message to the local AI
    print("Judge: ", end="", flush=True)
    
    try:
        response = ollama.chat(
            model='phi3',  
            messages=[
                {'role': 'system', 'content': system_instruction},
                {'role': 'user', 'content': user_input},
            ],
            stream=True 
        )

        # 3. Print the response word by word
        for chunk in response:
            print(chunk['message']['content'], end='', flush=True)
        
        print("\n") 

    except Exception as e:
        print(f"\n[Error]: {e}")
        print("Make sure the Ollama app is running!")
