# -*- coding: utf-8 -*-

print("------------- CALCULATOR ----------------")

num1 = input("Digite o primeiro número: ")
num1 = int(num1)
oper = input("Digite o operador: (+ - / * **): ")
num2 = input("Digite o segundo número: ")
num2 = int(num2)

#soma
if oper == "+":
	operacao = num1 + num2

#subtração
if oper == "-":
	operacao = num1 - num2

#divisão
if oper == "/":
	operacao = num1 / num2

#multiplicação
if oper == "*":
	operacao = num1 * num2

#exponenciação
if oper == "**":
	operacao = num1 ** num2

print("Resultado: ")
print(operacao)