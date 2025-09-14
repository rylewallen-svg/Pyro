# ai_bot.py

# You must install CharacterAI first:
# pip install git+https://github.com/kramcat/CharacterAI.git

from characterai import Client  # Adjust if the library uses a different class or function

def main():
    # Initialize the CharacterAI client (modify as needed for your actual usage)
    cclient = Client()

    # Define Pyro's personality and intro
    personality = "fierce, loyal, cocky, jolly, a little quick temper"
    intro = "So trainer what crazy stuff do you have in mind?"

    print(f"Pyro: {intro}")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("Pyro: See you next time, trainer!")
            break

        # This is a placeholder for sending a message to the AI.
        # Replace 'chat' with the actual CharacterAI method.
        try:
            response = cclient.chat(
                character="Pyro",
                personality=personality,
                message=user_input
            )
            print(f"Pyro: {response}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()