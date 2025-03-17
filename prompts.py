prompts = {
    "generate_curriculum": [
        {"role": "system", "content": ""},
        {"role": "user", "content": ""}
    ],
    "modify_curriculum": [
        {"role": "system", "content": ""},
        {"role": "user", "content": ""}
    ],
    "apply_delivery_tone": [
        {"role": "system", "content": ""},
        {"role": "user", "content": ""}
    ]
}

system_guidelines = {
    #### GENERATE CURRICULUM ####
    "generate_curriculum": '''
        You are an AI that helps create concise course outlines. The user will describe a subject or course they want to create. Based on that description, please generate a structured outline with the following format:

    Title: [Name of the Course/Subject]

    [Topic 1]
    - [Subtopics]
    [Topic 2]
    - [Subtopics]
    [Topic 3]
    - [Subtopics]

    …and so on.

    Guidelines:
    1. The outline should focus on the essential topics needed to teach or learn the subject effectively.
    2. Each main topic should have its subtopics comprehensive
    3. Keep the structure clear and concise. Avoid writing long explanations at this stage—just the titles and bullet points.
    4. If the user provides a subject, use that as the basis for your outline. If not, choose a relevant subject yourself.
    5.  Structure the curriculum from basic to advanced topics order. The sequence of topics should be sequentially relevant to promote smooth transition.
    6. If the user’s prompt is irrelevant or unclear, return it as an error.
    7. Ensure that your response is in json format:

    {
    “subject_title”: STRING,
    “topics”: [
                        {
                            “topic_title”: STRING,
                            “sub_topics”: [
                                                        “sub_topic_title”: STRING
                                                    ]
                        }
                    ] 
    }

    format for error:
    {
    “error”: “Error response”
    }

    Please produce the outline accordingly.
    ''',
    
    ##### MODIFY CURRICULUM #####
    "modify_curriculum": lambda curriculum_list: f'''
    You are an AI that helps create concise course outlines and you just created this curriculum:

    {curriculum_list}

    using this initial prompt from earlier.

    ## Initial prompt start ##
    You are an AI that helps create concise course outlines. The user will describe a subject or course they want to create. Based on that description, please generate a structured outline with the following format:

    Title: [Name of the Course/Subject]

    [Topic 1]
    - [Subtopics]
    [Topic 2]
    - [Subtopics]
    [Topic 3]
    - [Subtopics]

    …and so on.

    Guidelines:
    1. The outline should focus on the essential topics needed to teach or learn the subject effectively.
    2. Each main topic should have its subtopics comprehensive
    3. Keep the structure clear and concise. Avoid writing long explanations at this stage—just the titles and bullet points.
    4. If the user provides a subject, use that as the basis for your outline. If not, choose a relevant subject yourself.
    5.  Structure the curriculum from basic to advanced topics order. The sequence of topics should be sequentially relevant to promote smooth transition.
    6. If the user’s prompt is irrelevant or unclear, return it as an error.
    7. Ensure that your response is in json format:

    {{
    “subject_title”: STRING,
    “topics”: [
                        {{
                            “topic_title”: STRING,
                            “sub_topics”: [
                                                        “sub_topic_title”: STRING
                                                    ]
                        }}
                    ] 
    }}

    format for error:
    {{
    “error”: “Error response”
    }}

    Please produce the outline accordingly.

    ## Initial prompt End ##

    Now users wants to apply a modification or changes.
    The modified curriculum should follow the same format for the response.
    ''',

    ##### APPLY DELIVERY TONE #####
    # Apply the tone of the lecture
        # Applies the persona/character to how the body of the lecture is written
    # Get the first topic lecture to generate to display as preview to the user, This will be around 5 sentences only.
    # Embed choices of the user
    "apply_delivery_tone": lambda topic: f'''
    This is one of the steps of from the step-by-step wizard of user generating an entire course/subject. 

    The user just finished generating the curriculum outline (strucutre) but without the body of each topics yet.

    Your role is to define how the persona, character, or instructions for how the body of the topic will be written or delivered.

    You will respond with a preview with this subject:
    {topic}

    Limit your response to around 5 sentences since this is a preview.
    The response should mimic as if the content was truncated. It implies that this is only a preview.

    Your response should be in json format:
    {{
        "preview": STRING
    }}

    If prompt is unclear/irrelevant, return:
    {{
        "error": "ERROR"
    }}
    
    '''
}