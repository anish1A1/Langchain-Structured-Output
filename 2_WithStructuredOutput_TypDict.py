from typing import TypedDict
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "moonshotai/Kimi-K2-Thinking",
    task="text-generation"
)


model = ChatHuggingFace(llm=llm)

# schema
class Review(TypedDict):
    
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)



result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove, Also the UI looks outdated compared to other brands. Hoping for a software update to fix this""")

print(result)
print("\n", {result['summary']})
print(result['sentiment'])