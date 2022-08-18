


Peso = float(input("Digite seu peso em Kg: "))

Altura = float(input("Digite sua altura em metros: "))

IMC = Peso/(Altura**2) 

print("Seu IMC é: %.4f" % IMC)

if IMC < 16:
    print("Magreza grave")
elif IMC < 17:
    print("Magreza moderada")
elif IMC < 18.5:
    print("Magreza leve")
elif IMC < 25:
    print("Saudável")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 34:
    print("Obesidade Grau II (Severa)")
else:
    print("Obesidade grau III (móbida)")
