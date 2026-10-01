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


def estudar():
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
    
    
        while True:
            try:
                dificuldade_palavra = int(input("Resposta: "))
                
                if dificuldade_palavra > 5 or dificuldade_palavra < 1:
                    print("Opção Inválida!")
                    continue
    
                break
    
            except ValueError:
                print("Digite um número válido!")
    
    
    else:
        print("Adicione palavras para estudar!")
        return
                
    
    card_estudo["dificuldade"] = dificuldade_palavra
                                    
    salvar_flashcards()



def adicionar_palavra():
    cancelado = False
    
    while True:
    
        palavra = input("Digite a palavra (ou 0 para voltar): ")
    
        # cancela com "0"
        if palavra == "0":
            cancelado = True
            break
    
        # repete quando vazio
        # strip -> remove espaços do começo e do fim
        palavra = palavra.strip()
        if not palavra:
            print("Digite uma palavra válida")
            continue
    
        cadastrada = False
    
        for card in flashcards:
            if card["palavra"].lower() == palavra.lower():
                cadastrada = True
                print("Essa palavra já está cadastrada!")
                break
    
        if cadastrada:
            continue # volta para o loop do while true
                
        break # sai desse loop e vai para o próximo
    
    
    if cancelado:
        return
    
    
    cancelado = False
    
    while True:
        traducao = input("Digite a tradução (ou 0 para voltar): ")
    
        # Cancela com 0
        if traducao == "0":
            cancelado = True
            break
    
        # repete quando vazio
        # strip -> remove espaços do começo e do fim
        traducao = traducao.strip()
        if not traducao:
            print("Digite uma tradução válida")
            continue
                
        break
    
                    
    if cancelado:
        return
    
    palavra = palavra.title()
    traducao = traducao.title()
    
    card = {
        "palavra": palavra,
        "traducao": traducao,
        "dificuldade": 3
        }
    
    flashcards.append(card)
    print()
    
    salvar_flashcards()
    

def remover_palavra():
    tamanho_flashcards = len(flashcards)
    if not tamanho_flashcards:
        print("Não tem nenhuma palavra cadastrada!")
        return

    print("REMOVER PALAVRA:")
    mostrar_palavras()
    
    while True:
        try:
            
            indice_remover = int(input("Digite o Número da palavra que deseja remover: "))


            if tamanho_flashcards >= indice_remover and indice_remover >= 1:
    
                card_removido = flashcards[indice_remover-1]
    
                del flashcards[indice_remover-1]
                print(f"A palavra: {card_removido["palavra"]}, foi removida com sucesso!")
    
                salvar_flashcards()
    
                break
    
            else:
                print("Opção Inválida")
                continue
                    
        except ValueError:
            print("Digite um número válido")
            continue
    

def editar_palavra():
    # verifica se existem flashcards
    tamanho_flashcards = len(flashcards)
    
    if not tamanho_flashcards:
            print("Não tem nenhuma palavra cadastrada!")
            return

    print("EDITAR PALAVRA:")
    # mostrar as palavras;
    mostrar_palavras()

    while True:
            try:
                
                indice_editar = int(input("Digite o Número da palavra que deseja editar: "))

                if tamanho_flashcards >= indice_editar and indice_editar >= 1:

                    card_editar = flashcards[indice_editar-1]

                    card_editar["palavra"] = input("Digite a palavra corretamente: ")

                    print("A palavra foi editada com sucesso!")

                    salvar_flashcards()

                    break

                else:
                    print("Opção Inválida")
                    continue

            except ValueError:
                print("Digite um número válido")
                continue

    



def mostrar_estatisticas():
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
        estudar()


    elif opc == 2:
        adicionar_palavra()


    elif opc == 3:
        mostrar_palavras()
        

    elif opc == 4:
        remover_palavra()                


    elif opc == 5:
        editar_palavra()


    elif opc == 6:
        mostrar_estatisticas()


    elif opc == 7:
        print("Saindo...")
        

    else:
        print("Opção Inválida")
        




