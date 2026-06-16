from ollama import chat

def generate_summary(transcript):

    prompt = f"""
    You are an educational assistant.

    Summarize the following video transcript.

    Requirements:
    - Maximum 10 bullet points
    - Focus on key concepts
    - Easy for students to understand
    - Remove unnecessary details

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