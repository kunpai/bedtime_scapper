from story_generator import generate_story, query_model, conversation_history
from judge import judge_story

def main():
    print("Welcome to the Bedtime Story Generator!")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("What kind of story would you like to hear? Or would you like to exit?")
        if user_input.lower() in ["exit", "quit"]:
            print("Sweet dreams!")
            break

        print("\nCreating your bedtime story...\n")
        story = generate_story(user_input)

        # Judge the story
        judgement = judge_story(story)

        if judgement.get("verdict") == "Yes":
            print("Your Bedtime Story:\n")
            print(story)
            print("\nJudge Scores:", judgement["scores"])
            print("Feedback from Judge:", judgement["feedback"])

            while True:
                user_feedback = input("\nWould you like to revise the story? (e.g., 'make it shorter', 'add a dragon', or 'no'): ").strip()

                if user_feedback.lower() == "no":
                    break  # Exit revision loop, go back to main prompt

                revision_prompt = f"Please revise your last story. Feedback from the user: {user_feedback}"
                conversation_history.append({"role": "user", "content": revision_prompt})
                revised_story = query_model(conversation_history)
                conversation_history.append({"role": "assistant", "content": revised_story})

                print("\nRevised Story Based on Your Feedback:\n")
                print(revised_story)

                revised_judgement = judge_story(revised_story)
                print("\nJudge Scores (Revised Story):", revised_judgement["scores"])
                print("Feedback from Judge (Revised Story):", revised_judgement["feedback"])

        else:
            print("This story was judged not appropriate.")
            print("Judge Feedback:", judgement.get("feedback", "No feedback provided."))


if __name__ == "__main__":
    main()
