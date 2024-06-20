def soma(a,b):
    return a + b

def subtrai(a,b):
    return a - b
def multiplica(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Erro : divisão por 0 !"
    else:
        return  a / b
    
    
    
    
print("Bem vindo a calculadora !")

while True:
        print("Escolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        escolha =input("Digite o numero da operação (1,2,3,4,5):")
        if escolha =='5':
            print("Obrigado por usar a calculadora!!")
            break
        
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        
        if escolha == '1':
            resultado = soma(num1+num2)
            print(f"O resultado é:{resultado}")
        elif escolha == '2':
            resultado =subtrai(num1,num2)
            print(f"O resultado é:{resultado}")
        elif escolha == '3':
            resultado = multiplica(num1,num2)
            print(f"O resultado é:{resultado}")
        elif escolha == '4':
            resultado = divide(num1,num2)
            print(f"O resultado é:{resultado}")
        else:
            print('Escolha invalida')
        

        

