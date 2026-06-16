from deep_translator import GoogleTranslator

def translate_text(text, target_language):

    chunk_size = 4500

    chunks = [
        text[i:i+chunk_size]
        for i in range(0, len(text), chunk_size)
    ]

    translated_chunks = []

    for chunk in chunks:

        translated = GoogleTranslator(
            source="auto",
            target=target_language
        ).translate(chunk)

        translated_chunks.append(translated)

    return "\n".join(translated_chunks)