
#38. Elabore um programa que:
# Leia o ano de nascimento de 5 pessoas
# Calcula a idade (anoATUAL – anoNASCIMENTO)
# Contabilize quantos são idosos (acima 60)

Anos1=int(input("Qual o Ano de nascimento da 1° pessoa? "))
Anos2=int(input("Qual o Ano de nascimento da 2° pessoa? "))
Anos3=int(input("Qual o Ano de nascimento da 3° pessoa? "))
Anos4=int(input("Qual o Ano de nascimento da 4° pessoa? "))
Anos5=int(input("Qual o Ano de nascimento da 5° pessoa? "))

Anos11 = (2022-Anos1)
Anos22 = (2022-Anos2)
Anos33 = (2022-Anos3)
Anos44 = (2022-Anos4)
Anos55 = (2022-Anos5)

print(f"\n1° pessoa tem {Anos11} Anos")
print(f"2° pessoa tem {Anos22} Anos")
print(f"3° pessoa tem {Anos33} Anos")
print(f"4° pessoa tem {Anos44} Anos")
print(f"5° pessoa tem {Anos55} Anos")

if (Anos11) >=60:
    valor11 = 1
else:
  valor11 = 0
if (Anos22) >=60:
    valor22 = 1
else:
  valor22 = 0

if (Anos33) >=60:
    valor33 = 1
else:
  valor33 = 0

if (Anos44) >=60:
    valor44 = 1
else:
  valor44 = 0

if (Anos55) >=60:
    valor55 = 1
else:
  valor55 = 0

total = (valor11+valor22+valor33+valor44+valor55)
print(f"\nTotal de {total} Pessoa tem 60 anos+\n")