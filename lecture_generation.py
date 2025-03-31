from openaiapi import get_openai_response
from prompts import system_guidelines   

import asyncio
import random
import ast


## Creation topics bodies
# Returns the full completed lecture body
async def lecture_body_generation(curriculum_outline, tone_delivery_definition, tone_delivery_preview):
    '''
    Generate the bodies of all the topics
    Args:
        curriculum_outline (dict): The curriculum outline
        tone_deliver_definition (str): The instruction on how the bodies of the topics will be delivered based from the users prompt
        tone_delivery_preview (str): Preview/example of how the bodies will be written
    Returns:
        dict: The completed subject
    '''

    topics_count = len(curriculum_outline["topics"])

    async def generate_topic_body(index):

        print(f"generating topic number: {index + 1}")
        response = await get_openai_response(
            "",
            system_guidelines["generate_lecture"](curriculum_outline, index, tone_delivery_definition),
            model="gpt-4o",
            view_total_token=True
        )

        return response

    tasks = [generate_topic_body(i) for i in range(topics_count)]

    results = await asyncio.gather(*tasks)

    completed_subject = [ast.literal_eval(results[i][0].content) for i in range(topics_count)]

    total_token_used = sum([ float(results[i][1]) for i in range(topics_count)])

    return (completed_subject, total_token_used)