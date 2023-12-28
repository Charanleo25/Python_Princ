# Quiz Game
def run_quiz(questions):
    print("Answer each question by typing the full correct option.")

    score = 0
    total_questions = len(questions)

    for question, correct_answer in questions:
        print("\n" + question)
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print("\nQuiz completed!")
    print(f"Your score: {score}/{total_questions}")
    #print(100 *(score/total_questions))
    if score == total_questions:
        print("Great Job!, You did it.")
    elif  55 <= 100 *(score/total_questions):
        print("You have passed.")
    else:
        print("Needs some improvement, kindly retake the test.")
    
def admin_role(questions):
    #print("Want to add question? ")
    opt = 1
    while opt == 1:
    
        adding_q = input("Enter the question with options: ")
        adding_opt = input("Enter answer: ")
        simple_t = ()
        simple_t = simple_t + (adding_q,adding_opt,)
        questions.append(simple_t)
        opt = int(input("want to add 1 more question? \n Enter 1 for Yes \n Enter 0 for No \n Your Choice: "))
    
    
    print("admin role ended ... \n\n")
    main()
    
    
quiz_questions = [
        ("What is the capital of France? \n a)Paris b)Italy c)Dont know d)No capital", "paris"),
        ("Which programming language is this quiz written in? \n a)C++ b)C# c)Python d)Snake", "python"),
        ("What is the result of 2 + 2? \n a)22 b)2 c)4 d)2+2 ", "4"),
        ("In Python, how do you create a function? \n a)def b)func c)function d)fanta ", "def")
    ]   
def main():
    print("Welcome to the Python Quiz!")

    print("\t\t MENU \n 1. Admin\n 2. Participent ")
    user_mode = input("Choose 1 or 2 to select your role: ")
    if int(user_mode) == 2 :
        run_quiz(quiz_questions)
    elif int(user_mode) == 1:
        admin_role(quiz_questions)
    else:
        run_quiz(quiz_questions)

if __name__ == "__main__":
    main()
