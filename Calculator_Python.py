# -*- coding: utf-8 -*-
#Author: Suellen Lima (@suejaspe) (@suellenlime)

print("------------- CALCULATOR ----------------")

exit = False

while exit == False:

	num1 = input("Enter the first number: ")
	num1 = int(num1)
	oper = input("Enter the operator: (+ - / * ** %): ")
	num2 = input("Enter the second number: ")
	num2 = int(num2)

	#sum
	if oper == "+":
		operation = num1 + num2

	#subtraction
	if oper == "-":
		operation = num1 - num2

	#division
	if oper == "/":
		operation = num1 / num2

	#multiplication
	if oper == "*":
		operation = num1 * num2

	#exponentiation
	if oper == "**":
		operation = num1 ** num2

	#rest
	if oper == "%":
		operation = num1 % num2

	print("Result: ")
	print(operation)

	test = input("Exit? (y/n) ")
	if test == "y":
		exit = True
	if test == "n":
		exite = False
