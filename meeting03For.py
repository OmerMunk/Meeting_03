# value of STOP is 30 (by default adds 1, starts from0)
for i in range(30):
    print(i)

# value of START is 3, STOP is 30 (by default adds 1)
for i in range(3, 30):
    print(i)

# value of START is 3, STOP is 30, STEP is 4
for i in range(3, 30, 4):
    print(i)

# deacrising - value of START is 30, STOP is 3, STEP is -4
for i in range(30, 3, -4):
    print(i)

for number in [1, 2, 3]:
    print(number)

my_name = 'Omer'
for letter in my_name:
    print(letter)

for i in range(50, 100, 5):
    print(i)


# it is possible to go down in range
for i in range(30, 3, -3):
    print(i)

#page 31
#Exercise 1
sum = 0
for i in range(10):
    num = int(input(f"Enter your {i+1} number"))
    sum += num
print(f"The sum of the number you have entered is:{sum}")

#  Exercise 2
print("This programm can get an unknown amount of numbers,")
print("the first input needs to be a positive integer,")
print("and it will be the amount of the inputs after it.")
print("Later, the program will calculate the average of the numbers typed after the first input")
count = int(input("Enter the amount of numbers"))
sum = 0
for i in range(count):
    num = float(input(f"enter the {i+1} number"))
    sum += num
average = sum / count
print(average)


# Exercise 3
print("This program can get 10 numbers and show you the biggest of them")
num = float(input("Enter the first number"))
max = num
for i in range(9):
    num = float(input(f"Enter the {i+2} number"))
    if (num > max) :
        max = num
print(f"The maximum number you have entered is {max}")

# Exercise 4
for i in range(100):
    print(i+1)


#page 31

# Exercise 2
print("This program gets 2 integers, and shows all the integers between them (included)")
first_int = int(input("Enter the first integer"))
second_int = int(input("Enter the first integer"))
for i in range(first_int, (second_int+1)):
    print(i)

# Exercise 3
print("This program gets a natural number, let it be x, and show you the result of x! (x factorial)")
num = int(input("Enter the x that you would like me to calculate x! for it"))
factorial = 1
for i in range(1, (num+1)):
    factorial *= i
print(f"the rusult of x! is: {factorial}")

# Exercise 4
print("This program gets natural nubmer,")
print("let him be x, and calculates the sum of the number between 1 and x,")
print("that can be divided by 3 without a remainder ")
num = int(input("Enter a natural number"))
sum = 0
for i in range(1, (num+1)):
    if (i % 3) == 0:
        sum = sum + i
print(f"The sum is: {sum}.")

# page 32

# Exercise 5
print("This program gets 15 numbers, sums up every third number, and show you the sum")
sum = 0
for i in range(1, 100):
    num = float(input(f"Enter the {i} number"))
    if (i % 3) == 0 :
        sum += num
print(f"The sum is {sum}.")

# Exercise 6
print("This program gets a natural number, let it be N, and shows you sum of the geometric sequence, with the first object 1, and the commun ratio 2, from 1 to x+1 ")
sum = 0
num = int(input("Enter a natural number"))
for i in range((num+1)):
    ##print(2**i) ##this row shows that sequence
    sum += 2**i
print(f"The sum is {sum}.")

# Exercise 7
print("This program gets a natural number, let it be N, and shows you 2 sequences.")
print("The first sequence will be all the natural numbers from 1 to N ")
print("The objects of the second sequence will be the objects of the first sequence, each of them multiplied by 2 ")
num = int(input("Enter the a natural number 'N'"))
print("The first sequence is:")
for i in range(1, (num+1)):
    print(i)
print("The second sequence is:")
for i in range(1, (num+1)):
    print(i*2)

# Exercise 8
print("This program gets natural nubmer,")
print("let him be N, and calculates the sum of the number between 1 and N,")
print("that can be divided by 4 or 7 without a remainder ")
num = int(input("Enter a natural number"))
sum = 0
for i in range(1, (num+1)):
    if ((i % 4) == 0) or ((i % 7) == 0):
        sum = sum + i
print(f"The sum is: {sum}.")

#Exercise 9
print("This program calculates the value of y, for different values of x, by the equation (Y = X^2 +5)")
print("You choose the first value of X, the last value of X, and the steps between the values")
start_value = int(input("Enter the first value of X"))
last_value = int(input("Enter the last value of X"))
step = int(input("Enter the steps between the values of X"))

for i in range(start_value, (last_value+1), step):
    y_value = (i**2 + 5)
    print(y_value)

# Exercise 11
print("This program gets two different integers, and show you all the integers between them, from the smallest to the biggest and back to the smallest")
num1 = int(input("Enter the first natural number"))
num2 = int(input("Enter the second natural number"))
max_num = max(num1, num2)
min_num = min(num1, num2)
for i in range(min_num, (max_num)):
    print(i)
for i in range(max_num, (min_num-1), -1):
    print(i)

# Exercise 12
print("This program gets 100 integers, calculates the sum of the evens, and shows it to you.")
sum = 0
for i in range(10):
    num = int(input(f"Enter the {i+1} number"))
    if num % 2 == 0:
        sum += num
print(f"The sum of the even integers is {sum}")

# Exercise 13
print("This program gets 100 numbers, sums up the numbers with the even index, and shows you the sum")
sum = 0
for i in range(10):
    num = int(input(f"Enter the {i+1} number"))
    if (i+1) % 2 == 0:
        sum += num
print(f"The sum of the even integers is {sum}")

# Exercise 14
print("This program gets a main value, then gets another 100 numbers, and then shows you the indexes of the numbers that equal to the main value")
main_value = float(input("Choose the main value"))
index_list = []
for i in range(10):
    num = float(input(f"Enter the {i+1} number"))
    if num == main_value:
        index_list += [(i+1)]
print(index_list)

# Exercise 15
print("This program gets 10 couples of cards, each couple of cards contains a name of a student and his grade in the exam")
print("The program shows the names of the students that passed the exam, and the total average of the grades.")
passed_grade = 70
students_passed = []
sum = 0
count = 0
for i in range(10):
    student_name = input(f"Enter the {i+1} students name")
    student_grade = float(input((f"Enter {student_name}'s grade")))
    if student_grade >= passed_grade:
        students_passed += [student_name]
        sum += student_grade
        count += 1


average = sum/count
print("The names of the student that passed the exam are:")
print(students_passed)
print(f"The average grade is {average}")

# Exercise 16
print("This program has 2 stages:")
print("Stage 1: the program gets 5 numbers and calculate their sum")
print("Stage 2: the program gets 10 numbers and shows you the index of the numbers that equal to the sum from stage 1")
sum = 0
for i in range(5):
    num = float(input(f"Enter the {i+1} number"))
    sum += num

print(f"The sum from stage 1 is: {sum}")
index_list = []
for i in range(10):
    num = float(input(f"Enter the {i+1} number"))
    if num == sum:
        index_list += [(i+1)]
print(f"The indexes of the numbers got in stage 2 that equal to the sum from stage 1 are:{index_list} ")

# Exercise 17
print

# Exercise 18
print("This program")
amount = int(input("Enter the amount of numbers"))
if amount == 1:
    print("invalid input, you need to enter a minimum amount of 2")
    exit(1)
max_list = []
num = float(input("Enter the first number"))
last_big_index = 1
last_second_big_index = 0
max_list.insert(0, num)
max_list += [num]
for i in range(amount-1):
    num = float(input(f"Enter the {i+2} number"))
    if num > max_list[0] :
        max_list.insert(0, num)
        last_second_big_index = last_big_index
        last_big_index = i+2

    elif  ((num > max_list[1]) or max_list[0] == max_list[1]) and num != (max_list[0]):
            if max_list[0]==max_list[1]:
                max_list[1] = num
                last_second_big_index = (i + 2)
            else:
                max_list.insert(1, num)
                last_second_big_index = (i + 2)
    elif num == max_list[1]:
        last_second_big_index = (i+2)
if max_list[0] == max_list[1]:
    print("There is no second biggest number")
else:
    print(max_list)
    print(f"the second biggest number is: {max_list[1]}")
    print(f"the index of the last time that number was entered is: {last_second_big_index} ")

# page 35

# Exercise 1

# Exercise 2

# Exercise 3

# Exercise 4
print("Welcome to the voting program of the UN")
print("voting codes are:")
print("1 - for")
print("2 - against ")
print("3 - abstain")
print("4 - veto")
print("Note 1: if you will vote a wrong number, your vote will not be counted, and it will be wasted")
print("Note 2: you can vote 4 only if you have a veto right")
count_for = int(0)
count_against = int(0)
count_abstained = int(0)
veto_list = ['china' , 'france', 'russia', 'uk', 'usa']
for_list = []
against_list = []
abstained_list = []
print(veto_list)
for i in range(10):
    country_name = input("Whats is the country name?")
    vote = int(input(f"Enter the country number {i+1} vote:"))
    if vote == 4 and country_name in veto_list:
        print(f"{country_name} has voted veto")
        exit(1)
    elif vote == 1:
        count_for += 1
        for_list += [country_name]
    elif vote == 2:
        count_against += 1
        against_list += [country_name]
    elif vote == 3:
        count_abstained += 1
        abstained_list += [country_name]

print(f"The number of country's that voted for is: {count_for}")
print(f"The number of country's that voted against is: {count_against} " )
print(f"The number of country's that voted abstained is: {count_abstained}")

print("Countrys voted for:")
print(for_list)
print()
print("Countrys voted for:")
print(against_list)
print()
print("Countrys voted for:")
print(against_list)
print()

# nestef loops
inner_loop_count = 0
for i in range(5):
    n = int(input("Enter number: "))

    while n >= 10:
        n = n // 10
        inner_loop_count += 1
    print ("Most significant digit: ", n)
print("Inner loop ran ", inner_loop_count)

# Example
for i in range(10):
    for j in range(10):
        print (i, " ", j)

# Page 29

#Exercise 3
num = int(input("Enter psitive integers, i will calculate for you the sum of the digits of each number, until you will enter a negative integer"))
sum = 0
while num>= 0:
    original_num = num
    while num>0:
        sum += num%10
        num = num//10
    print(f"The sum of the digits of the {original_num} is: {sum}")
    answer = input("Do you want another summary action to this sum?")
    if answer == 'yes':
        num = sum
        original_num = num
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        print(f"The sum of the digits of the {original_num} is: {sum}")
    sum = int(0)
    num = int(input("Enter another number"))

# page 38

# Exercise 8

print("Enter the length and width of a rectangle and the program will draw it for you ")
rows = int(input("What is the length?"))
columns = int(input("What is the width?"))
for i in range(rows):
    print()
    for j in range(columns):
        print('*', end= "")


# Exercise 9
print("This is the multiply board from 1 to 20")
for i in range(20):
    print()
    for j in range(20):
        print(((i+1)*(j+1)), end = "" + " ")

# Exercise 10
print("This program shows you the multiply board, to the number of rows and columns you choose")
columns  = int(input("Choose number of columns"))
rows = int(input("Choose number of rows"))
for i in range(rows):
    print()
    for j in range(columns):
        print(((i+1)*(j+1)), end = "" + " ")

#Exercise 15
print("This program")
most_rainy_month = int(0)
most_rainy_year = int(0)

for i in range(1991, 2001):
    yearly_sum = int(0)
    for j in range(12):
        rain_in_month = float(input(f"Enter the rain amount in month {j+1}, in year {i}"))
        if rain_in_month > most_rainy_month:
            most_rainy_month = rain_in_month
            index_most_rainy_month = f"The most rainy month was on {j+1}, {i}"
        yearly_sum += rain_in_month
    if yearly_sum > most_rainy_year:
        most_rainy_year = yearly_sum
        index_most_rainy_year = i

print(index_most_rainy_month)
print(f"The most rainy year was {index_most_rainy_year}")




