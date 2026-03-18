from src.core.llm_provider import get_llm
from src.prompts.mcp_call_prompt import build_prompt

llm = get_llm(temperature=0.0)

query = "4 repositories on fastapi with supabase"


prompt = build_prompt(query)

mcp_call = llm.invoke(prompt)
print(mcp_call.content)
