num1 = input ("digite o primeiro numero:")
num2 = input ("digite o segundo numero:")

try: 
    num1 = int(num1)
    num2 = int (num2)

    print(f"a soma dos numeros e:{num1 + num2}")
except:
    print("digite um numero correto")