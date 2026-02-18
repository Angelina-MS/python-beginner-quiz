score = 0

answer = input("What is 2 + 2? ")
if answer == "4":
    score += 1

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    score += 1

print("Your score is", score)
