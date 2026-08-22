import json
import random

opc = 0


def carregar_flashcards():
    try: 
        with open("flashcards.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return [] 


def salvar_flashcards():
    with open("flashcards.json", "w") as arquivo:
        json.dump(flashcards, arquivo) #(o que salvar, onde salvar)

def mostrar_palavras():
        print("LISTA DE PALAVRAS: ")
        for index, card in enumerate(flashcards, start=1):
            print(f'{index}. {card["palavra"]} - {card["traducao"]} - {card["dificuldade"]}')
        print()


flashcards = carregar_flashcards()


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

    try:
        opc = int(input("Digite a sua opção: "))
        print()

    except ValueError:
        print("Digite um número válido")
        continue



    if opc == 1:
        tamanho_flashcards = len(flashcards)

        if tamanho_flashcards > 0:

            cards_estudos = []

            # Repete os cards conforme a dificuldade
            for card in flashcards:
                for _ in range(card["dificuldade"]):
                    cards_estudos.append(card)

            card_estudo = random.choice(cards_estudos)

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

            salvar_flashcards()


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

        salvar_flashcards()


    elif opc == 3:
        mostrar_palavras()
        

    elif opc == 4:
        print("REMOVER PALAVRA:")
        mostrar_palavras()

        indice_remover = int(input("Digite o Número da palavra que deseja remover: "))

        tamanho_flashcards = len(flashcards)
        if tamanho_flashcards >= indice_remover and indice_remover >= 1:

            card_removido = flashcards[indice_remover-1]

            del flashcards[indice_remover-1]
            print(f"A palavra: {card_removido["palavra"]}, foi removida com sucesso!")

            salvar_flashcards()

        else:
            print("Opção Inválida")
            continue


    elif opc == 5:
        print("ESTATÍSTICAS: ")
        print(f"Total de palavras: {len(flashcards)}")

        dificuldade_1 = 0
        dificuldade_2 = 0
        dificuldade_3 = 0
        dificuldade_4 = 0
        dificuldade_5 = 0

        for card in flashcards:
            if card["dificuldade"] == 1:
                dificuldade_1+=1

            elif card["dificuldade"] == 2:
                dificuldade_2+=1

            elif card["dificuldade"] == 3:
                dificuldade_3+=1

            elif card["dificuldade"] == 4:
                dificuldade_4+=1

            elif card["dificuldade"] == 5:
                dificuldade_5+=1

        print()
        print(f"Muito fáceis (1): {dificuldade_1}")
        print(f"Fáceis (2): {dificuldade_2}")
        print(f"Médio (3): {dificuldade_3}")
        print(f"Difíceis (4): {dificuldade_4}")
        print(f"Muito difíceis (5): {dificuldade_5}")

    elif opc == 6:
        print("Saindo...")
        

    else:
        print("Opção Inválida")
        




