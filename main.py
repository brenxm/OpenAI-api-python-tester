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
                # TODO: Prompt for modifying the generated list, ensure to embed generated list + prompt
                print("good")

            # IF users wants to revert and generated another course outline 
            elif prompt == "3":
                break

            # If invalid input
            else:
                prompt = input("Invalid input, please press:\n1 to move forward\n2 to make changes\n3 to Go back\n")


    # Defining the tone of delivery
    while True:
        print("Entered Tone delivery section")
        break