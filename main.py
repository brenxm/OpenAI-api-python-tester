from openaiapi import get_openai_response
from prompts import system_guidelines


if __name__ == "__main__":

    # Initial description for curriculum generation
    # Choice to edit, revert, or move forward
    # IF edit, print -> what changes you want to make
    # IF revert, go back to Initial description
    # IF move forward, print -> describe the tone of the teacher
    # Can go back or generate final lecture object


    while True:

        # Initial description for curriculum generation
        prompt = input("What do you want to learn?\n")
        response = get_openai_response(prompt, system_guidelines["generate_curriculum"], model = "gpt-4o")

        # IF API returns error
        # Error occurs when a misunderstanding/misinterpretation on the AI's part (AI is not getting it)
        if "error" in response.content:
            print("Prompt can't be understood.")
            continue

        else:
            # If API returns valid list
            print("OpenAI Response:", response.content)
            prompt = input("Here is the generated list.\nWhat do you want to do now? Press:\n1 to move forward\n2 to make changes\n3 to Go back\n")

            # IF user's accepted the presented curriculum list
            if prompt == "1":
                break

            # IF user's wants to make changes   
            elif prompt == "2":
                while True:
                    prompt = input("What changes you want to apply?\n")
                    response = get_openai_response(prompt, system_guidelines["modify_curriculum"](response.content), model = "gpt-4o")
                    print(response.content)
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
        break



#### DEV NOTES #####
# Above code is CLI use only and for prototyping/testing prompts
# In production, each section will be divided into their respective function sections