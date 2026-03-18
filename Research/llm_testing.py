from src.core.llm_provider import get_llm

prompt = "Tell me about LangChain"

llm = get_llm()

answer = llm.invoke(
    [
        ("system", "Respond in plain text. Do not use markdown, lists, or formatting."),
        ("human", prompt),
    ]
)

print(answer.content)


print("\n\n\n")


# for chunk in llm.stream(prompt):
#     if chunk.content:
#         print(chunk.content, end="", flush=True)


# print("\n\n\n")


# for chunk in llm.bind(temperature=0.2).stream(prompt):
#     if chunk.content:
#         print(chunk.content, end="", flush=True)
