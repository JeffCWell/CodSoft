import random

def getEmoji(choice):
    return {"rock": "🪨", "paper": "📄", "scissors": "✂️"}.get(choice, "")

def decideWinner(me, computer):
    if me == computer:
        return "tie"
    win = (me == "rock" and computer == "scissors") or \
          (me == "scissors" and computer == "paper") or \
          (me == "paper" and computer == "rock")
    return "me" if win else "computer"

def startGame():
    meScore, computerScore = 0, 0
    print("🎮 Welcome to Rock, Paper, Scissors Game!!!! 🎮")

    while True:
        me = input("\nrock, paper, scissors? (type 'quit' to end): ").lower()
        if me == "quit":
            print(f"\nFinal Score => Me: {meScore} | Computer: {computerScore}")
            if meScore > computerScore:
                print(" You won the game! 🎉")
            elif meScore < computerScore:
                print(" Computer won the game! 🤖")
            else:
                print(" It's a tie overall!")
            break
        if me not in ["rock", "paper", "scissors"]:
            print(" Invalid input.")
            continue

        computer = random.choice(["rock", "paper", "scissors"])
        print(f"You: {me} {getEmoji(me)} | Computer: {computer} {getEmoji(computer)}")

        result = decideWinner(me, computer)
        if result == "tie":
            print("It's a tie!")
        elif result == "me":
            print("You win this round! 🎉")
            meScore += 1
        else:
            print("Computer wins this round! 🤖")
            computerScore += 1

        print(f"Score => Me: {meScore} | Computer: {computerScore}")

if __name__ == "__main__":
    startGame()
