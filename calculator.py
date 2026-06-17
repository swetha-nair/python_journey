number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
operator = input("Enter the operator (+ - * / % **): ")

if operator == "+":
    print(f"{number_1} {operator} {number_2} = {number_1 + number_2}")

elif operator == "-":
    print(f"{number_1} {operator} {number_2} = {number_1 - number_2}")

elif operator == "*":
    print(f"{number_1} {operator} {number_2} = {number_1 * number_2}")

elif operator == "/":
    if number_2 != 0:
        print(f"{number_1} {operator} {number_2} = {number_1 / number_2}")
    else:
        print("Division is not possible. Input a valid second number.")

elif operator == "%":
    if number_2 != 0:
        print(f"{number_1} {operator} {number_2} = {number_1 % number_2}")
    else:
        print("Division is not possible. Input a valid second number.")

elif operator == "**":
    print(f"{number_1} {operator} {number_2} = {number_1 ** number_2}")

else:
    print("Invalid operator! Please enter + - * / %  **")
