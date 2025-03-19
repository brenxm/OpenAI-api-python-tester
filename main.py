from lecture_generation import lecture_body_generation
from openaiapi import get_openai_response
from prompts import system_guidelines

import asyncio
import ast


### flow states ###
getting_curriculum_outline = True
modifying_curriculum_outline = False
getting_delivery_tone = False
ready_to_generate_entire_lecture = False


def get_curriculum_outline():
    global getting_curriculum_outline
    global getting_delivery_tone
    global modifying_curriculum_outline

    while True:
        prompt = input("What do you want to learn?\n")

        response = get_openai_response( prompt, system_guidelines["generate_curriculum"], model = "gpt-4o" )
        
        if "error" in response_dict:
            print("Prompt can't be understood.")
            continue

        print("This is the curriculum outline generated")
        print(response.content)
        
        # Getting the action prompt loop
        while True:
            action_prompt = input("What do you want to do now? Press:\n1 to move forward\n2 to make changes\n3 to redo")

            if action_prompt == "1":
                getting_curriculum_outline = False
                getting_delivery_tone = True
                return ast.literal_eval(response.content)
            
            elif action_prompt == "2":
                modifying_curriculum_outline = True
                getting_curriculum_outline = False
                return ast.literal_eval(response.content)
            
            elif action_prompt == "3":
                break

            else:
                print("Invalid prompt, try again.")


def modify_curriculum_outline():
    global getting_curriculum_outline
    global getting_delivery_tone
    global modifying_curriculum_outline

    while True:
        prompt = input("What changes you want to apply?\n")
        response = get_openai_response( prompt, system_guidelines["modify_curriculum"](response.content), model = "gpt-4o" )
        print(response.content)

        print("This is the modified list.\n")

        action = input("What do you want to do now?\n1 to move forward\n2 to make changes\n3 to create new curriculum\n")

        if action == "1":
            modifying_curriculum_outline = False
            getting_delivery_tone = True
            return ast.literal_eval( response.content )
        
        elif action == "2":
            continue
        
        elif action == "3":
            getting_curriculum_outline = True
            modifying_curriculum_outline = False
            break


def get_delivery_tone(response_obj):
    global getting_curriculum_outline
    global getting_delivery_tone
    global modifying_curriculum_outline
    global ready_to_generate_entire_lecture

    print("Entered Tone delivery section")

    while True:
        first_topic = response_obj["topics"][0]
        lecture_tone_prompt = input("Define on how the lecture body will be delivered.\n")
        preview_content = get_openai_response(lecture_tone_prompt, system_guidelines["apply_delivery_tone"](first_topic), model="gpt-4o")
        print(preview_content.content)
        print("This is the preview of how the body of the lecture will be written")
        action_prompt = input("What you want to do now? Press:\n1 To generate entire lecture \n2 To redo" )

        if action_prompt == "1":
            getting_delivery_tone = False
            ready_to_generate_entire_lecture = True
            break

        elif action_prompt == "2":
            continue

        else:
            print("Invalid input, try again")

        break


if __name__ == "__main__":
    while True:
        if getting_curriculum_outline:
            response_dict = get_curriculum_outline()
            
        elif modifying_curriculum_outline:
            response_dict = modify_curriculum_outline()

        elif getting_delivery_tone:
            delivery_tone = get_delivery_tone( response_dict )

        elif ready_to_generate_entire_lecture:
            lecture_obj = lecture_body_generation(response_dict, delivery_tone, "")
            break

    print("This is the generated lecture")
    print( lecture_obj )

#### DEV NOTES #####
# Above code is CLI use only and for prototyping/testing prompts
# In production, each section will be divided into their respective function sections