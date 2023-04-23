# title = "********************CALCULATOR INCLUDING ALL TYOPE OF CALCULATIONS********************"

# def sum(m,n):
#     return m+n

# def product(m,n):
#     return m-n

# def product(m,n):
#     return m*n

# def divide(m,n):
#     return m/n

# def module(m,n):
#     return m%n

# def average(m):
    
#     total = sum(m)
#     lenght = len(m)
    
#     if lenght == 0:
#         return 0
#     else :
#         return total/lenght
    
# def number():
#     num_list = []
#     num_count = int(input("how many number do you want to find average:"))
#     for i in range(num_count):
#         num = float(input(f"enter number{i+1}:"))
#         num_list.append(num)
#     return num_list
    
# my_num = number()

# avg = average(my_num)
# print(f"average of {my_num} is {avg}")


# def temp(m):
#     return (m*9/5) + 32
     
# degree = int(input("enter the celsius you want to convert into farenheit:"))
# total = temp(degree)

# print(total)

# def fact(m):
#     if m == 0:
#         return 1
#     else :
#         return m * fact(m-1)

# user = int(input("enter the number for which you want to find factorial:"))

# total = fact(user)

# print(total)


# def fib(m):
#     if m == 0:
#         return 0
#     elif m == 1:
#         return 1
#     else :
#         return fib(m-1) + fib(m-2)
    
    
# user = int(input("enter the number for the fibonacci series"))
# for i in range(user):
#     series = fib(i)
#     print(series, end=' ')
    
    
    
def even(m):
    if (m % 2) == 0 :
        print("the number is EVEN")
    else :
        print("number is ODD")
        
user = int(input("enter the number:"))
user = even(user)






























# choice = input("what do you want to do : \n 'add' or 'multiply'")

# if choice == "add":
#     num1 =  int(input("enter 1st number:"))
#     num2 = int(input("enter 2nd number:"))
#     total = sum(num1,num2)
#     print(f"the sum of {num1} and {num2} is {total}")

# elif choice == "multiply":
#     num1 =  int(input("enter 1st number:"))
#     num2 = int(input("enter 2nd number:"))
#     total = product(num1,num2)
#     print(f"the sum of {num1} and {num2} is {total}")
    
# else:
#     print("invalid choice :\n choose the options:")
    