import os

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("Escolha uma das operações abaixo:")
opc = str(input("(+) , (-) , (*) , (/)\n"))

os.system('clear')

if (opc == "+"):
  soma = n1 + n2
  print(soma)
elif (opc == "-"):
  menos = n1 - n2
  print(menos)
elif (opc == "*"):
  mult = n1 * n2
  print(mult)
elif (opc == "/"):
  divs = n1 / n2
  print(divs)
else:
  print("Opção Indisponivel")

