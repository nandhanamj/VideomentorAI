from ollama import chat

def generate_quiz(transcript):

    prompt = f"""
    Create 10 multiple-choice questions from the following transcript.

    Requirements:
    - Each question should have 4 options
    - Provide the correct answer
    - Focus on important concepts
    - Format neatly

    Transcript:
    {transcript}
    """

    response = chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]