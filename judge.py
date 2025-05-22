import openai
import json
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = "gpt-3.5-turbo"

def judge_story(story_text):
    """
    Evaluates the generated story using an LLM-based judge. 
    """
    judge_prompt = f"""
        You are a bedtime story quality evaluator (LLM Judge). Please rate the following story on a scale of 1 to 10 for each category below, then provide a brief comment on how to improve it if needed.

        Evaluation Criteria:
        1. Age Appropriateness (5-10 years old)
        2. Story Structure (clear beginning, middle, end)
        3. Language Level (simple, age-appropriate vocabulary)
        4. Emotional Tone (calming, gentle)
        5. Length (suitable for bedtime: not too long or short)
        6. Moral/Lesson (positive values)
        7. Engagement (interesting, but not overstimulating)

        Story:
        \"\"\"{story_text}\"\"\"

        Respond in JSON format like:
        {{
        "scores": {{
            "age_appropriateness": <score>,
            "story_structure": <score>,
            "language_level": <score>,
            "emotional_tone": <score>,
            "length": <score>,
            "moral": <score>,
            "engagement": <score>
        }},
        "verdict": "Yes",  # or "No" if it shouldn't be shown to user
        "feedback": "The story is great, but could have a clearer moral."
        }}
        """
    messages = [
        {"role": "system", "content": "You are a helpful and strict story quality judge."},
        {"role": "user", "content": judge_prompt}
    ]

    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            temperature=0.3,
            messages=messages
        )
        return json.loads(response.choices[0].message["content"])
    except Exception as e:
        return {"error": str(e)}
