from modules.summarizer import generate_summary

text = """
Python functions are reusable blocks of code.
Functions help organize programs and reduce repetition.
"""

summary = generate_summary(text)

print(summary)