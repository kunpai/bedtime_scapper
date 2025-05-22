import os
import openai
import json
import random
from judge import judge_story
from style import get_storyteller_intro
from dotenv import load_dotenv
load_dotenv()

"""
Before submitting the assignment, describe here in a few sentences what you would have built next if you spent 2 more hours on this project:
I would have added the following features:
    1. A story rating system where users can rate stories, 
    2. implemented story  saving functionality to build a personal library
    3. Created story variation features where users can request different versions of the same story with different characters or settings.
    4. Added a multimode llm so it can generate an image with regards to the story for kids.
"""

# Set up OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = "gpt-3.5-turbo"

# Load storytelling prompt instructions from file
with open('prompt.txt', 'r') as file:
    base_prompt = file.read()

# System message
system_message = {
    "role": "system", 
    "content": "You are a skilled storyteller specializing in children's bedtime stories for ages 5–10. Always create gentle, engaging stories perfect for winding down before sleep."
}

# To save convo history
conversation_history = [system_message]

def query_model(messages):
    """Send conversation messages to the GPT model and return the assistant's reply."""
    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            temperature=0.1,
            messages=messages
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def generate_story(user_request):
    """
    Create a bedtime story using the base prompt and user request.
    """
    style_prompt = get_storyteller_intro()
    full_prompt = style_prompt + "\n\n" + base_prompt + f'\n\nUser request: "{user_request}"'
    conversation_history.append({"role": "user", "content": full_prompt})
    response_text = query_model(conversation_history)
    conversation_history.append({"role": "assistant", "content": response_text})
    
    return response_text

