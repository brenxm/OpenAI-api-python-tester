from enum import Enum
import asyncio
import ast

from lecture_generation import lecture_body_generation
from openaiapi import get_openai_response
from prompts import system_guidelines


class State(Enum):
    GETTING_CURRICULUM_OUTLINE = 0
    MODIFYING_CURRICULUM_OUTLINE = 1
    GETTING_DELIVERY_TONE = 2
    READY_TO_GENERATE_ENTIRE_LECTURE = 3


current_state = State.GETTING_CURRICULUM_OUTLINE
total_token_used = 0



async def get_curriculum_outline():
    global current_state
    global total_token_used

    while True:
        prompt = input("What do you want to learn?\n")

        response = await get_openai_response( prompt, system_guidelines["generate_curriculum"], model = "gpt-4o" )

        response_dict = ast.literal_eval(response[0].content)
        
        if "error" in response_dict:
            print("Prompt can't be understood.")
            continue

        print("This is the curriculum outline generated")
        print(response[0].content)
        
        total_token_used = total_token_used + response[1]
        
        # Getting the action prompt loop
        while True:
            action_prompt = input("What do you want to do now? Press:\n1 to move forward\n2 to make changes\n3 to redo")

            if action_prompt == "1":
                current_state = State.GETTING_DELIVERY_TONE
                return response_dict
            
            elif action_prompt == "2":
                current_state = State.MODIFYING_CURRICULUM_OUTLINE
                return response[0].content
            
            elif action_prompt == "3":
                break

            else:
                print("Invalid prompt, try again.")


async def modify_curriculum_outline(response_obj):
    global current_state
    global total_token_used

    
    while True:
        prompt = input("What changes you want to apply?\n")
        response = await get_openai_response( prompt, system_guidelines["modify_curriculum"](response_obj), model = "gpt-4o" )
        print(response[0].content)

        print("This is the modified list.\n")

        total_token_used = total_token_used + response[1]

        action = input("What do you want to do now?\n1 to move forward\n2 to redo\n3 to create new curriculum\n")

        while True:
            if action == "1":
                current_state = State.GETTING_DELIVERY_TONE
                return ast.literal_eval( response[0].content )
            
            elif action == "2":
                break
            
            elif action == "3":
                current_state = State.GETTING_CURRICULUM_OUTLINE
                return

            else:
                print("Invalid input. Try again.")
                continue


async def get_delivery_tone(response_obj):
    global current_state
    global total_token_used

    print("Entered Tone delivery section")

    while True:
        first_topic = response_obj["topics"][0]
        lecture_tone_prompt = input("Define on how the lecture body will be delivered.\n")
        preview_content = await get_openai_response(lecture_tone_prompt, system_guidelines["apply_delivery_tone"](first_topic), model="gpt-4o")
        print(preview_content[0].content)
        print("This is the preview of how the body of the lecture will be written")

        total_token_used = total_token_used + preview_content[1]
        action_prompt = input("What you want to do now? Press:\n1 To generate entire lecture \n2 To redo" )

        while True:
            if action_prompt == "1":
                current_state = State.READY_TO_GENERATE_ENTIRE_LECTURE

                return lecture_tone_prompt

            elif action_prompt == "2":
                break

            else:
                print("Invalid input, try again")
                continue


async def main():
    while True:
        if current_state == State.GETTING_CURRICULUM_OUTLINE:
            response_dict = await get_curriculum_outline()
            
        elif current_state == State.MODIFYING_CURRICULUM_OUTLINE:
            response_dict = await modify_curriculum_outline(response_dict)

        elif current_state == State.GETTING_DELIVERY_TONE:
            delivery_tone = await get_delivery_tone( response_dict )

        elif current_state == State.READY_TO_GENERATE_ENTIRE_LECTURE:
            lecture_obj = await lecture_body_generation(response_dict, delivery_tone, "")
            break

    print("This is the generated lecture")
    print( lecture_obj[0] )
    print(f"Total token used: {total_token_used + lecture_obj[1]}")
    

if __name__ == "__main__":

    asyncio.run(main())


#### DEV NOTES #####
# Above code is CLI use only and for prototyping/testing prompts
# In production, each section will be divided into their respective function sections