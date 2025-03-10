import openai
import key_retriever

# API key placeholder
openai.api_key = ""

def get_openai_response(users_prompt, system_content = "You are a helpful assistant.",model="gpt-3.5-turbo", max_tokens=150):
    """
    Function to get a response from OpenAI API
    Args:
        prompt (str): The input text to send to the API
        model (str): The model to use (default: gpt-3.5-turbo)
        max_tokens (int): Maximum length of the response
    Returns:
        str: The API response
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": users_prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

