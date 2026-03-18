# {
#     "messages": [
#         AIMessage(
#             content="",
#             additional_kwargs={
#                 "tool_calls": [
#                     {
#                         "id": "eafgbv42j",
#                         "function": {
#                             "arguments": '{"query":"Langchain","top_k":2}',
#                             "name": "search_repository",
#                         },
#                         "type": "function",
#                     }
#                 ]
#             },
#             response_metadata={
#                 "token_usage": {
#                     "completion_tokens": 21,
#                     "prompt_tokens": 284,
#                     "total_tokens": 305,
#                     "completion_time": 0.032804926,
#                     "completion_tokens_details": None,
#                     "prompt_time": 0.020339047,
#                     "prompt_tokens_details": None,
#                     "queue_time": 0.045903013,
#                     "total_time": 0.053143973,
#                 },
#                 "model_name": "llama-3.1-8b-instant",
#                 "system_fingerprint": "fp_4387d3edbb",
#                 "service_tier": "on_demand",
#                 "finish_reason": "tool_calls",
#                 "logprobs": None,
#                 "model_provider": "groq",
#             },
#             id="lc_run--019cffba-0b3a-7e60-839b-689255bd2f2f-0",
#             tool_calls=[
#                 {
#                     "name": "search_repository",
#                     "args": {"query": "Langchain", "top_k": 2},
#                     "id": "eafgbv42j",
#                     "type": "tool_call",
#                 }
#             ],
#             invalid_tool_calls=[],
#             usage_metadata={
#                 "input_tokens": 284,
#                 "output_tokens": 21,
#                 "total_tokens": 305,
#             },
#         )
#     ]
# }


# [
#     ToolMessage(
#         content="CallToolResult("
#         'content=[TextContent(type=\'text\', text=\'[\
#             {"name":"langchain","full_name":"langchain-ai/langchain","description":"The agent engineering platform","stars":130019,"url":"https://github.com/langchain-ai/langchain","language":"Python"},'
#         '{"name":"markitdown","full_name":"microsoft/markitdown","description":"Python tool for converting files and office documents to Markdown.","stars":90915,"url":"https://github.com/microsoft/markitdown","language":"Python"}]\', annotations=None, meta=None)], structured_content=None, meta=None, data=None, is_error=False)',
#         name="search_repository",
#         tool_call_id="g17wsphgq",
#     )
# ]
