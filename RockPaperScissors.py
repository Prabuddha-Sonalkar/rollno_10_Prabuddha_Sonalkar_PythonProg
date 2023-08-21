from guizero import App, Box, Text, PushButton
import random

# Function to determine the winner
def play(player_choice):
    computer_choice = random.choice(choices)
    result_text.value = f"Computer chose: {computer_choice}"
    
    if player_choice == computer_choice:
        outcome_text.value = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        outcome_text.value = "You win!"
    else:
        outcome_text.value = "Computer wins!"

# Create the app window
app = App("Rock, Paper, Scissors", width=300, height=200)

# Available choices
choices = ["Rock", "Paper", "Scissors"]

# Create GUI elements
instruction_text = Text(app, text="Choose your move:")
choice_box = Box(app, layout="grid")
result_text = Text(app, text="")
outcome_text = Text(app, text="")

# Create buttons for each choice
for index, choice in enumerate(choices):
    button = PushButton(choice_box, text=choice, grid=[index, 0], padx=10, pady=10,
                        command=play, args=[choice])

# Display the app window
app.display()
