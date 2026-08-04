# PRECISO CRIAR UM INSERIR LISTA, APAGAR LISTA E MOSTRAR A LISTA COMPLETA E SEU INDICE.
import os


def Limpar():
    os.system("cls" if os.name == "nt" else "clear")


def apresentacao():
    print("BEM VINDO A LISTA DE SUPER MERCADOS!\n")
    print(
        "Esse supermercado você pode escolher qualquer coisa que quiser. Apenas obedeça as orientações e faça suas compras com moderação ^-^"
    )
    print("Coloque oque deseja: [a]dicionar, [d]eletar, [l]istar e [c]oncluir.\n")


Limpar()

tentativa = 0
lista_de_compras = []

while True:
    apresentacao()
    escolha = input("O que deseja fazer agora: ").lower()

    if len(escolha) > 1:
        Limpar()
        tentativa += 1
        if tentativa > 2:
            Limpar()
            print("Muitos erros, devido a isso o sistema se desligará.")
            break
        print("Porfavor, insira somente uma opção!")
        continue

    if escolha == "a":
        Limpar()
        print("Você entrou no carrinho de compras, adicione tudo que deseja comprar!\n")
        print("Quando terminar apenas digite [s]air")
        while True:
            produto = input("Digite o que deseja colocar: ").lower()
            if produto == "s" or produto == "sair":
                Limpar()
                break
            lista_de_compras.append(produto)

    elif escolha == "l":
        Limpar()
        print("Muito bem, aqui está a sua lista!\n")
        for i, listar in enumerate(lista_de_compras):
            i += 1
            print(f"{i}.{listar}")
        input("\nDigite qualquer coisa para voltar...")
        Limpar()
        continue

    elif escolha == "d":
        Limpar()
        print(
            "Agora você está na seção de remoção! Os seus produtos estão listados abaixo, depois escolha o número que deseja remover\n"
        )
        for i, listar in enumerate(lista_de_compras):
            i += 1
            print(f"{i}. {listar}")
        while True:
            try:
                deletar_lista = int(input("\nDigite o produto para deletar: "))
                deletar_lista -= 1
                if deletar_lista < 0 or deletar_lista >= len(lista_de_compras):
                    print("Digite a opção correta, porfavor.")
                    continue
            except ValueError:
                print("Digite a opção correta, porfavor.")
                continue
            lista_de_compras.pop(deletar_lista)
            Limpar()
            break
    elif escolha == "c":
        Limpar()
        if not lista_de_compras:
            Limpar()
            print("Obrigado pela visita!")
            break
        else:
            print("Obrigado pela(s) compra(s)! Leve seus produtos:\n")
            for listar in lista_de_compras:
                print(listar)
            break
    else:
        Limpar()
        tentativa += 1
        if tentativa > 2:
            Limpar()
            print("Muitos erros, devido a isso o sistema se desligará.")
            break
        continue
