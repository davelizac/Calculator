from replit import clear
from art import logo
print(logo)

#add:
def add(n1, n2):
    return n1 + n2

#subs:
def subs(n1, n2):
    return n1 - n2

#mult:
def mult(n1, n2):
    return n1 * n2

#div:
def div(n1, n2):
    return n1 / n2

#exp:
def exp(n1, n2):
    return n1 ** n2


operations = {
 "+" : add,
 "-" : subs,
 "*" : mult,
 "/" : div,
 "**" : exp,   
}

def calculator(): #recursion starter
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
        
    run = True
    
    while run:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2) #In the last two lines of code it is important to not just assign a variable to the function that you're calling from the dictionary, but also create another variable that will encapsulate that called function, otherwise the final line of code will just return the position of the funtion in the dictionary, but will not execute the operation that it is supposed to execute.
        print(f"{num1} {operation_symbol} {num2} = {answer}") 
    
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            run = False
            clear()
            calculator() #recursion activator
     

calculator()

#What do I take from this part of the course?: Use while loops to reduce the lines of code!! you can updates variables with if statements and while loops!! You can use inputs combined with if statements!!

#Recursions are functions that are able to call themselves!!

