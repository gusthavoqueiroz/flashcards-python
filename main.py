import random
opc = 0
flashcards = []


def mostrar_palavras():
        print("LISTA DE PALAVRAS: ")
        for index, palavra in enumerate(flashcards, start=1):
            print(f'{index}. {palavra["palavra"]} - {palavra["traducao"]} - {palavra["dificuldade"]}')
        print()


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

    if opc == 1:
        tamanho_flashcards = len(flashcards)

        if tamanho_flashcards > 0:
            card_estudo = random.choice(flashcards)
            print(card_estudo["palavra"])

            input("Pressione ENTER para ver a tradução")
            print(f"TRADUÇÃO: {card_estudo["traducao"]}")

            print("""
            Qual a dificuldade que você teve em lembrar?
            1 - Muito fácil
            2 - Fácil
            3 - Médio
            4 - Difícil
            5 - Muito difícil 

            """)

            dificuldade_palavra = int(input("Resposta: "))

            while dificuldade_palavra > 5 or dificuldade_palavra < 1:
                print("Opção Inválida!")
                dificuldade_palavra = int(input("Resposta: "))

            card_estudo["dificuldade"] = dificuldade_palavra


        else:
            print("Adicione palavras para estudar!")
            continue
         

    elif opc == 2:
        card = {
            "palavra": input("Digite a palavra: "),
            "traducao": input("Digite a tradução: "),
            "dificuldade": 3
        }

        flashcards.append(card)
        print()


    elif opc == 3:
        mostrar_palavras()
        

    elif opc == 4:
        print("REMOVER PALAVRA:")
        mostrar_palavras()

        indice_remover = int(input("Digite o Número da palavra que deseja remover: "))

        tamanho_flashcards = len(flashcards)
        if tamanho_flashcards >= indice_remover and indice_remover >= 1:

            palavra_removida = flashcards[indice_remover-1]

            del flashcards[indice_remover-1]
            print(f"A palavra: {palavra_removida["palavra"]}, foi removida com sucesso!")
        else:
            print("Opção Inválida")
            continue







