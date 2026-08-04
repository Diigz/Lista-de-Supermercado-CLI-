import os


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def apresentacao():
    print("BEM VINDO A LISTA DE SUPER MERCADOS!\n")
    print(
        "Esse supermercado você pode escolher qualquer coisa que quiser. Apenas obedeça as orientações e faça suas compras com moderação ^-^"
    )
    print("Coloque oque deseja: [a]dicionar, [d]eletar, [l]istar e [c]oncluir.\n")


def adicionar(lista_de_compras):
    limpar()
    print("Você entrou no carrinho de compras, adicione tudo que deseja comprar!\n")
    print("Quando terminar apenas digite [s]air")
    while True:
        produto = input("Digite o que deseja colocar: ").strip().lower()
        if produto == "s" or produto == "sair":
            limpar()
            break
        if not produto:
            print("Digite um produto válido.")
            continue
        lista_de_compras.append(produto)


def listar(lista_de_compras):
    limpar()
    print("Muito bem, aqui está a sua lista!\n")
    if not lista_de_compras:
        print("Sua lista está vazia.")
    else:
        for i, item in enumerate(lista_de_compras, start=1):
            print(f"{i}.{item}")
    input("\nDigite qualquer coisa para voltar...")
    limpar()


def deletar(lista_de_compras):
    limpar()
    if not lista_de_compras:
        print("Sua lista está vazia, não há o que deletar.\n")
        input("Digite qualquer coisa para voltar...")
        limpar()
        return

    print(
        "Agora você está na seção de remoção! Os seus produtos estão listados abaixo, depois escolha o número que deseja remover\n"
    )
    for i, item in enumerate(lista_de_compras, start=1):
        print(f"{i}. {item}")

    while True:
        entrada = (
            input("\nDigite o número do produto para deletar (ou [s]air): ")
            .strip()
            .lower()
        )
        if entrada == "s" or entrada == "sair":
            limpar()
            return
        try:
            indice = int(entrada) - 1
            if indice < 0 or indice >= len(lista_de_compras):
                print("Digite a opção correta, porfavor.")
                continue
        except ValueError:
            print("Digite a opção correta, porfavor.")
            continue
        lista_de_compras.pop(indice)
        limpar()
        break


def concluir(lista_de_compras):
    limpar()
    if not lista_de_compras:
        print("Obrigado pela visita!")
    else:
        print("Obrigado pela(s) compra(s)! Leve seus produtos:\n")
        for item in lista_de_compras:
            print(item)


def main():
    limpar()

    tentativa = 0
    lista_de_compras = []

    while True:
        apresentacao()
        escolha = input("O que deseja fazer agora: ").strip().lower()

        if len(escolha) != 1:
            limpar()
            tentativa += 1
            if tentativa > 2:
                limpar()
                print("Muitos erros, devido a isso o sistema se desligará.")
                break
            print("Porfavor, insira somente uma opção!")
            continue

        if escolha == "a":
            adicionar(lista_de_compras)
        elif escolha == "l":
            listar(lista_de_compras)
        elif escolha == "d":
            deletar(lista_de_compras)
        elif escolha == "c":
            concluir(lista_de_compras)
            break
        else:
            limpar()
            tentativa += 1
            if tentativa > 2:
                limpar()
                print("Muitos erros, devido a isso o sistema se desligará.")
                break
            continue


if __name__ == "__main__":
    main()
