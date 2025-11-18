from langchain_ollama import ChatOllama
import time
llm = ChatOllama(
    model='llama3.1',
    temperature=0
)


while True:
    user_input = input("Your Input--> ")
    
    # Record the start time
    start_time = time.perf_counter()
    
    if user_input == 'exit':
        break
    
    result = llm.invoke(user_input)
    
    for i in range(10000):
        _ = i*2
    
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    print(result.content)
    
    
    