# -*- coding: utf-8 -*-
#Author: Suellen Lima (@suejaspe) (@suellenlime)

def sum(x,y):
	return x + y

def subtraction(x,y):
	return x - y

def division(x,y):
	return x / y

def multiplication(x,y):
	return x * y

def exponentiation(x,y):
	return x ** y

def rest(x,y):
	return x % y


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
		operation = sum(num1,num2)

	#subtraction
	if oper == "-":
		operation = subtraction(num1,num2)

	#division
	if oper == "/":
		operation = division(num1,num2)

	#multiplication
	if oper == "*":
		operation = multiplication(num1,num2)

	#exponentiation
	if oper == "**":
		operation = exponentiation(num1,num2)

	#rest
	if oper == "%":
		operation = rest(num1,num2)

	print("Result: ")
	print(operation)

	test = input("Exit? (y/n) ")
	if test == "y":
		exit = True
	if test == "n":
		exite = False
