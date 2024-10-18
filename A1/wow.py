# Glenn Raphael De Los Reyes
# 11189672
# gld141

# Initialize questions and their answers
questions = {
  "A list of actions that describe how to perform a task is called what?   " : "algorithm",
  "What is a name given to a particular value?   " : "variable",
  "What is the name of data that comes from outside the algorithm?   ": "input",
  "Algorithms written with plain words are called what?   ": "pseudocode",
  "Hiding details that are not currently important is called what?   ": "abstraction",
}

# Initialize score and their corresponding message
result = {
  0: "You have achieved greatness but in the other direction 🙌💯",
  1: "Admittedly not the best...",
  2: "Just shy of average! 🤏🤏",
  3: "Mid. Not bad, not good.",
  4: "Just a step away from greatness...",
  5: "You did pretty good kid...",
  6: "Maybe I'm the one who didn't do the reading..."
}

# Get user's name
name = input("Hello, what is your name? ")

def get_response():
  '''Get user response if they read the textbook'''
  return input(f"{name}, did you read chapter 1 of the assigned reading for this class (Intro to Computer Science)? [yes/no] ")

response = get_response()

# Ask for response until user gives the proper response
while (response != "yes" or response != "no"):
  if(response == "yes"):
    print("Cool, let's review what you learned. 👇\n\n")
    break
  elif(response == "no"):
    print("Uh oh, then good luck on this SURPRISE TEST! 😈\n\n")
    break
  else:
    print("Give me a simple yes or no.")
    response = get_response()

# Initialise score for quiz
score = 0

# Ask question, check answer, and give feedback
for question in questions:
  answer = input(question)
  if(answer.lower() == questions[question]):
    score += 1
    print("Correct. Your current score is", score, "\n")
  else:
    print("Wrong. Your current score is", score, "\n")

# Give quiz results
print("You scored", score, "out of 5.", result[score])