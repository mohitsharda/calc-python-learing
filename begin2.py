# This is beginners learning code in which many maths calculation problems are solved with easy logic.
# Below are the mentiond topic of math which we have covered in this code :-
# ADDITION , SUBTRACTION , MULTIPLICATION , DIVIDE , MODULE , AVERAGE , TEMPERATURE TO FAHRENHEIT , FACTORIAL
# FIBONACCI , EVEN-ODD , PRIME NUMBER , SQUARE , CUBE 


title = "********************CALCULATOR INCLUDING ALL TYPE OF CALCULATIONS********************"
print(title)

# BELOW ARE THE BASE LOGIC 
# 1. ADDITION LOGIC
def Sum(m,n):
    return m+n

# 2. SUBTRACTION LOGIC
def difference(m,n):
    return m-n

# 3. MULTIPLICATION LOGIC
def product(m,n):
    return m*n

# 4. DIVIDE LOGIC
def divide(m,n):
    return m/n

# 5. MODULE LOGIC
def module(m,n):
    return m%n

# # 6. AVERAGE LOGIC
def average(a):
    total = sum(a)
    lenght = len(a)
    
    if lenght == 0:
        return 0
    else :
        return total/lenght
    
# 7. TEMPERATURE TO FAHRENHIET LOGIC
def temp(m):
    return (m*9/5) + 32

# 8. FACTORIAL LOGIC
def fact(m):
    if m == 0:
        return 1
    else :
        return m * fact(m-1)

# 9. FIBONACCI SERIES LOGIC
def fib(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else :
        return fib(m-1) + fib(m-2)
    
# 10. TO FIND ODD-EVEN LOGIC
def even(m):
    if (m % 2) == 0 :
        print("NUMBER IS EVEN")
    else :
        print("NUMBER IS ODD")
        
# 11. TO FIND PRIME OR NOT LOGIC        
def prime(m):
    if m < 2:
        return False
    for i in range(2 , m):
        if m%i == 0:
            return False
        else :
            return True

# 12. TO FIND SQUARE LOGIC   
def square(m):
    return m*m

# 13. TO FIND CUBE LOGIC
def cube(m):
    return m*m*m

# BELOW IS ALL THE CALLING AND PRINTING OF THE PROGRAM 

print("\n*********** WHICH CALCULATION YOU WANT TO DO*********** :\n")
print("*********** TYPE NUMBER FROM 1 TO 10 ACCORDIND TO YOUR CALCULATION CHOICE*********** :")
choice = input("\n 1 for Addition \n 2 for Subtraction \n 3 for multiplication \n 4 for divide \n 5 for module  \n 6 for average \n 7 for fahrenheit \n 8 for factorial \n 9 for fibonacci \n 10 for Odd-Even \n 11 for Prime \n 12 for Square  \n 13 for Cube \n***********ENTER YOUR CHOICE***********\n")
if choice == '1': 
     num1 =  int(input("enter 1st number:"))
     num2 = int(input("enter 2nd number:"))
     total = Sum(num1,num2)
     print(f"THE SUM OF {num1} AND {num2} IS {total}")

elif choice == '2': 
     num1 =  int(input("enter 1st number:"))
     num2 = int(input("enter 2nd number:"))
     total = difference(num1,num2)
     print(f"THE SUBTRACTION OF {num1} AND {num2} IS {total}")

elif choice == '3':
    num1 =  int(input("enter 1st number:"))
    num2 = int(input("enter 2nd number:"))
    total = product(num1,num2)
    print(f"THE MULTIPLICATION OF {num1} AND {num2} IS {total}")

elif choice == '4': 
     num1 =  int(input("enter 1st number:"))
     num2 = int(input("enter 2nd number:"))
     total = divide(num1,num2)
     print(f"THE DIVISION OF {num1} AND {num2} IS {total}")
    
elif choice == '5': 
     num1 =  int(input("enter 1st number:"))
     num2 = int(input("enter 2nd number:"))
     total = module(num1,num2)
     print(f"THE MODULE OF  {num1} AND {num2} IS {total}")
     
elif choice == '6':
    def number():
        num_list = []
        num_count = int(input("how many number do you want to find average:"))
        for i in range(num_count):
            num = float(input(f"enter number{i+1}:"))
            num_list.append(num)
        return num_list
   
    my_num = number()
    avg = average(my_num)
    print(f"average of {my_num} is {avg}")
    
elif choice == '7':
    degree = int(input("enter the celsius you want to convert into farenheit:"))
    total = temp(degree)
    print("THE TEMPERATURE IS :", degree,"\nFAHRENHEIT IS:",total)
    
elif choice == '8':
     user = int(input("enter the number for which you want to find factorial:"))
     print("FACTORIAL IS :", end=' ')
     total = fact(user)
     print(total)
    
elif choice == '9':
    user = int(input("enter the number for the fibonacci series"))
    print("FIBONACCI SERIES IS :")
    for i in range(user):
         series = fib(i)
         print(series, end=' ')
    
elif choice == '10':
     user = int(input("enter the number:"))
     user = even(user) 
    
elif choice == '11':
    user = int(input("enter the number"))
    ans =  prime(user)
    if prime(user):
         print("NUMBER IS PRIME")
    else :
         print("NOT PRIME")
    
elif choice == '12':
    user = int(input("enter the number"))
    total = square(user)
    print(f"square of {user} is : {total}")
      
elif choice == '13':
    user = int(input("enter the number"))
    total = cube(user)
    print(f"cube of {user} is : {total}")
    
else :
    print("||| ERROR ||| \nNOT A VALID OPTION ")











    