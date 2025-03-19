from lecture_generation import lecture_body_generation
from openaiapi import get_openai_response
from prompts import system_guidelines

import asyncio
import ast


def get_curriculum_outline():

    while True:
        prompt = input("What do you want to learn?\n")

        response = get_openai_response(prompt, system_guidelines["generate_curriculum"], model = "gpt-4o")
        
        if "error" in response_dict:
            print("Prompt can't be understood.")
            continue

        print("This is the curriculum outline generated")
        print(response.content)

        return ast.literal_eval(response.content)


def modify_curriculum_outline():
    while True:


getting_curriculum_outline = true
modifying_curriculum_outline = false
getting_delivery_tone = false

if __name__ == "__main__":


    while getting_curriculum_outline:

        response_dict = get_curriculum_outline()
           

        prompt = input("Here is the generated list.\nWhat do you want to do now? Press:\n1 to move forward\n2 to make changes\n3 to Go back\n")

        # IF user's accepted the presented curriculum list
        if prompt == "1":
            getting_curriculum_outline = false
            getting_delivery)tone = true
            break

        # IF user's wants to make changes   
        elif prompt == "2":
            while True:
                prompt = input("What changes you want to apply?\n")
                response = get_openai_response(prompt, system_guidelines["modify_curriculum"](response.content), model = "gpt-4o")
                print(response.content)

                response_dict = ast.literal_eval(response.content)

                print("This is the modified list.\n")
                action = input("What do you want to do now?\n1 to move forward\n2 to make changes\n3 to create new curriculum\n")

                if action == "1":
                    break

                elif action == "2":
                    continue

                elif action == "3":
                    break
                else:
                    print("Invalid input, try again")

            if action == "3":
                print("Reverting to a new curriculum.")
                continue

            elif action == "1":
                break

                
        # IF users wants to revert and generate another course outline 
        elif prompt == "3":
            print("Reverting...")
            continue

        # If invalid input
        else:
            prompt = input("Invalid input, please press:\n1 to move forward\n2 to make changes\n3 to Go back\n")


    # Defining the tone of delivery
    while True:
        print("Entered Tone delivery section")
        # Delivery selection mode

        # Takes the very first subtopic and generate a lecture content of it. The content should only be short (5 sentence) to act as a preview only.
        first_topic = response_dict["topics"][0]

        lecture_tone_prompt = input("Define on how the lecture body will be delivered.\n")

        preview_content = get_openai_response(lecture_tone_prompt, system_guidelines["apply_delivery_tone"](first_topic), model="gpt-4o")

        print(preview_content.content)
        print("This is the preview of how the body of the lecture will be written")

        action_prompt = input("What you want to do now? Press:\n1 To generate entire lecture \n2 To redo" )

        if action_prompt == "1":
            # Generates the entire lecture
            print("Generating the entire lecture")
            lecture_body_generation(response_dict, lecture_tone_prompt, preview_content.content)

        elif action_prompt == "2":
            continue

        else:
            print("Invalid input, try again")

        break



#### DEV NOTES #####
# Above code is CLI use only and for prototyping/testing prompts
# In production, each section will be divided into their respective function sections



