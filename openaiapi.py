from openai import AsyncOpenAI
from key_retriever import load_api_key

client = AsyncOpenAI(api_key=load_api_key())

async def get_openai_response(users_prompt, system_content = "You are a helpful assistant.", model="gpt-4.5-preview", view_total_token = False):
    """
    Function to get a response from OpenAI API
    Args:
        users_prompt (str): The input text to send to the API
        system_content (str): System instruction
        model (str): The model to use (default: gpt-3.5-turbo)
        max_tokens (int): Maximum length of the response
    Returns:
        str: The API response
    """
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "developer", "content": system_content},
                {"role": "user", "content": users_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=1
        )

        if view_total_token:
            print(f"Total token used: {response.usage.total_tokens}")
            
        return (response.choices[0].message, response.usage.total_tokens)

    except Exception as e:
        return f"Error: {str(e)}"

