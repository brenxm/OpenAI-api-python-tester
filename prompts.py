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
    "modify_curriculum": '''
    ''',

    ##### APPLY DELIVERY TONE #####
    "apply_delivery_tone": '''
    '''
}