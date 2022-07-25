# Simple word game
name = input('Please enter your name: ')
print(f"Hello {name}, welcome to play this question game.")

ans = input("Are you ready to play this game.(yes/no):").lower()
print('Thanks your choice. Here you will get 4 questions. every question 25 marks. \nBe careful when you give the ans.')
print('game is staring now.....')

score = 0
t_score = 4
if ans == 'yes':
    ans = input("1. what is the best programming language for AI ?").lower()
    if ans == "python":
        score += 1
        print("correct")
    else:
        print(' sorry! your ans is wrong')

    ans = input('2. What is 2+8+9-1 ')
    if ans == '18':
        score += 1
        print("great")
    else:
        print('sorry! your ans is wrong')

    ans = input('3. which is a better graphics card, 1050ti or a 1060 ')
    if ans == '1050':
        score += 1
        print("great")
    else:
        print(' sorry! your ans is wrong')

    ans = input('4. who came second in the stanely cup finals.(nights or vegas)? ')
    if ans == 'nights' or 'vegas':
        score += 1
        print("great")
    else:
        print('sorry! your ans is wrong')
else:
    print('Thanks for comment')
print("Congratulations! you got", score, 'question correct')
percentage = (score / t_score) * 100
print("You final score:", percentage, '%')
