from ollama import chat

def generate_notes(transcript):

    prompt = f"""
    You are an expert educational assistant.

    Create structured study notes from the following transcript.

    Format:

    # Topic

    ## Definitions

    ## Key Concepts

    ## Important Points

    ## Examples (if available)

    ## Quick Revision Notes

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