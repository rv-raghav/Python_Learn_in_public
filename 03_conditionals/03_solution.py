score = int(input("Enter your score : "))

if score >= 101:
    print("please verify your grade")
    exit() # to exit a python program because if not used at 101 it will assign grade A 

if score >= 90:
    print("Your score is", score, "and your grade is A")
elif score < 90 and score>=80:
    print("Your score is", score, "and your grade is B")
elif score < 80 and score>=70:
    print("Your score is", score, "and your grade is C")
elif score < 70 and score>=60:
    print("Your score is", score, "and your grade is D")
else:
    print("Your score is", score, "and grade is F")