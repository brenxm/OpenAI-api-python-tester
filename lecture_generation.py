from openaiapi import get_openai_response
from prompts import system_guidelines   

import asyncio


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
        response = await get_openai_response(
            "",
            system_guidelines["generate_lecture"](curriculum_outline, index, tone_delivery_definition),
            model="gpt-4o",
            view_total_token=True
        )

        return response.content

    tasks = [generate_topic_body(i) for i in range(topics_count)]

    results = await asyncio.gather(*tasks)

    completed_subject = {f"topic_{i}": result for i, result in enumerate(results)}

    return completed_subject