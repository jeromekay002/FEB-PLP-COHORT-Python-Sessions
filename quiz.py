def quiz():
    print("Welcome to the python Quiz")
    score = 0

    # question 1
    print("1. What is the correct file extension for python files?")
    print("a - .py")
    print("b - .python")
    print("c - .html")
    print("d - .pyt")
    answer = input("Your answer is (a,b,c,d): ").lower()

    # add if statements for checking  the right answer
    if answer == "a":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong answer!")

    # Question 2
    print("\n2) Which keyword is used to define a function in Python?")
    print("a) def")
    print("b) function")
    print("c) define")
    print("d) func")
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == "a":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! The correct answer is 'a'.")

    # display the final score
    print(f"\n🏆 Your final score: {score}/1")

    # ask to play again
    play_again = input("Do you want to try again? (yes/no): ").lower()
    if play_again == "yes":
        quiz()
    else:
        print("Thankyou for playing! ")
quiz()