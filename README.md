# Bedtime Story Generator - Technical Documentation

## Overview
This project is a bedtime story generator designed for children ages 5–10. It utilizes OpenAI's GPT model to create gentle, imaginative stories. The system features a multi-agent design involving a Storyteller LLM, a Judge LLM for quality assurance, an optional stylistic module that introduces storytelling variation, and Valorant integration for live gaming-themed stories.

## Objective
To generate engaging and appropriate bedtime stories through a conversational interface that supports revisions and evaluates story quality using an LLM-based judge. The system can also incorporate live Valorant match data to create gaming-themed bedtime stories that are still gentle and appropriate for children.

## Architecture
![System Architecture Diagram](diagram.png)

### Agents
- **User**: Inputs a story idea and provides feedback for revisions.
- **Storyteller (LLM)**: Generates stories based on structured prompts.
- **Style Selector**: Randomly modifies the story generation prompt with a narrative voice (e.g., gentle, whimsical).
- **Judge (LLM)**: Scores and critiques the story on various criteria (tone, structure, moral, etc.).
- **Valorant Integration**: Fetches live match data when users request Valorant-themed stories.

### Flow
1. User provides a prompt.
2. System checks if the request is Valorant-related (contains keywords like "valorant", "agent", etc.).
3. If Valorant-related, fetches live match data and incorporates it into the story context.
4. Style Selector injects a random storytelling persona.
5. Storyteller LLM generates the story (with Valorant context if applicable).
6. Judge LLM evaluates the story.
7. User receives the story after being evaluated by the judge.
8. User can revise the story based on feedback.

## Prompting Strategy
- **Chain of Thought (CoT)**: Used in `prompt.txt` to break down storytelling into structured steps like character setup, setting, conflict, resolution, and moral guidance.

## Agent Design
- **Multi-Agent Architecture**: The system is built using a modular agent-based design. The **Storyteller LLM** is responsible solely for narrative generation, while the **Judge LLM** evaluates the output independently. This separation ensures better reliability and structured feedback.
- **Style Agent**: A lightweight style selector injects storytelling personality into the generation prompt, making the outputs more diverse and engaging.
- **User Role**: The user not only initiates the story but also provides direct revision instructions, forming a human-in-the-loop setup.


## File Structure
```
bedtime_story/
├── main.py                  # Main loop and user interaction
├── story_generator.py       # Story generation logic, API calls, conversation memory
├── judge.py                 # Story evaluation logic via LLM
├── style.py                 # Storyteller voice randomization
├── valo_story_utils.py      # Valorant integration utilities
├── prompt.txt               # Structured instructions for story creation
├── requirements.txt         # Has all the libraries
├── .env                     # API key storage (You need to make one)
├── valo_bot_scapper/        # Submodule for Valorant data scraping
└── README.md                # Documentation and explanation
```

## Technologies and Methods Used

- **OpenAI GPT (gpt-3.5-turbo)**: Used for both storytelling and judging
- **Chain of Thought Prompting (CoT)**: Guides the model to follow a structured storytelling format via `prompt.txt`
- **Multi-agent Design**: Separates concerns between Storyteller and Judge agents for better evaluation and control
- **Environment Variables**: API key stored securely in `.env`
- **Conversation Memory**: Maintains message history for continuity and improved revisions
- **Custom Styling Module**: Randomized storyteller voices through `get_storyteller_intro()` in `style.py`
- **Valorant Integration**: Real-time match data scraping via the `valo_bot_scapper` submodule
- **Web Scraping**: Uses `requests` and `BeautifulSoup` for fetching live Valorant match data from vlr.gg
- **Python + Modular Design**: Cleanly separated files for readability and maintainability

## Setup Instructions
1. Clone the repository
2. Add your API key in a `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```
3. Install required packages:
```
pip install -r requirements.txt
```
4. Run the app:
```
python main.py
```

## Example Usage

### Regular Story Generation
```
What kind of story would you like to hear? A story about a duck
Creating your bedtime story...

Judge Scores: {...}
Feedback: The story could use a clearer moral.

Would you like to revise the story?
> Add a moral about sharing

Revised Story...
Revised Scores...
Revised Feedback...
```

### Valorant-Themed Story Generation
```
What kind of story would you like to hear? Tell me a Valorant story
Creating your bedtime story...

[The system fetches live Valorant match data and incorporates it into the story]

Your Bedtime Story:
Once upon a time, in the exciting world of Valorant, there were brave agents having adventures right now! The Team Liquid agents were working together with the Fnatic agents to complete an important mission...

Judge Scores: {...}
Feedback: Great use of teamwork themes!
```

## Feature Summary
- Story generation tailored to young children
- Structured storytelling using CoT prompting
- Modular design using agent-based architecture
- Support for user-driven revision
- Automated story quality evaluation via LLM judge
- Optional personality styling for narrator voice
- **Valorant Integration**: Live match data incorporation for gaming-themed bedtime stories
- Child-friendly transformation of competitive gaming content into gentle bedtime narratives

## Future Enhancements
- Story rating system (1–5 stars)
- Personal story library for saved favorites
- Multimodal story illustrations (LLM + image generation)
- User-selectable storyteller styles

## Acknowledgments and Resources

This project was developed with support from publicly available resources, including:

- [OpenAI API documentation](https://platform.openai.com/docs)
- [Community blogs and articles on prompt engineering and storytelling with LLMs](https://www.promptingguide.ai/techniques)
- ChatGPT (Used interactively to refine architecture, design prompts, and validate implementation strategies)