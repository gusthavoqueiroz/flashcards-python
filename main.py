opc = 0
flashcards = []

while opc != 6:
    print("===========================")
    print("FLASHCARDS - Estudos inglês")
    print()
    print("1. Estudar")
    print("2. Adicionar palavra")
    print("3. Ver palavras")
    print("4. Remover palavra")
    print("5. Ver estatísticas")
    print("6. Sair")
    print()

    opc = int(input("Digite a sua opção: "))
    print()



    if opc == 2:
        palavra = {
            "palavra": input("Digite a palavra: "),
            "traducao": input("Digite a tradução: "),
            "dificuldade": 3
        }

        flashcards.append(palavra)
        print()


    elif opc == 3:
        print("LISTA DE PALAVRAS: ")
        for index, palavra in enumerate(flashcards, start=1):
            print(f'{index}. {palavra["palavra"]} - {palavra["traducao"]} - {palavra["dificuldade"]}')
        print()
