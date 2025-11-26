while True:
    nota = float(input())
    while nota < 0 or nota > 10:  
        print("nota invalida")
        nota = float(input())

    nota2 = float(input())
    while nota2 < 0 or nota2 > 10:  
        print("nota invalida")
        nota2 = float(input())

    media = (nota + nota2) / 2
    print(f"media = {media:.2f}")

    print("novo calculo (1-sim 2-nao)")
    opcao = int(input())

    while opcao != 1 and opcao != 2: 
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())

    if opcao == 2:
        break