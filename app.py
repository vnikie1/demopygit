

def show_grades(grades):
    for student_name in grades:
        print(f"Grade of {student_name} is {grades[student_name].title()}")


def fibonacii_of(n):
    if n in {0,1}:
        return n
    return fibonacii_of(n-1) + fibonacii_of(n-2)



grades = {"Vishal" : "A", "Monica" : "A", "Aral" : "A+", "Nitya": "B+", "Yukti" :"C"}
show_grades(grades)

grades["Rohit"] =  "B"
grades["Basanti"] = "A+"
del grades["Vishal"]
print("showing new Grade List")
show_grades(grades)
student_check = "asanti"
check_name = grades.get(student_check , "No student of this name is available")
print(f"Checking student with name {student_check} -> {check_name}")

user_0 = {
    "name" : "Vishal",
    "age" : "31",
    "date" : 30 ,
    "month" : 12,
    "year" : 1990,
    "DOB" : "30/12/1990",
    }

user_1 = {
    "name" : "Monica",
    "age" : "29",
    "date" : 31 ,
    "month" : 7,
    "year" : 1992,
    "DOB" : "31/07/1992",
    }

check_user = ["user_2", "user_1"]
users = {"user_0" : user_0, "user_1" : user_1}
#print(users.items())
for key,value in users.items():
    print(f"This is user {key}")
    print("Below are the user details")

    if key in check_user:
        for info,detail in value.items():
            print(f"{info} -> {detail} ")


fib_num= input("Enter fibonacci no. to find")
fib_num = int(fib_num)
fib_result = [fibonacii_of(n) for n in range(fib_num)]
print(fib_result)

temp_list = [n for n in range(5, fib_num)]
print(temp_list)
# aliens = []
# #alien_0 = { "color" : "green" , "speed" : "slow" , "points" : 10 }
#
# for alien in range(30):
#     new_alien = { "color" : "green" , "speed" : "slow" , "points" : 10 }
#     aliens.append(new_alien)
#
# for alien in aliens:
#     print(alien)

# num = 2
# while num != 0 :
#     num = input("Enter a number -> ")
#     num = int(num)
#     if num % 2 ==0 :
#         print("Its a Even number" )
#     else :
#         print("Its a ODD number")