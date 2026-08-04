# 🛒 Lista de Supermercado (CLI)

Um pequeno sistema de linha de comando para gerenciar uma lista de compras, feito em Python puro. Permite adicionar, remover, listar e concluir a compra, com validação de entradas e limite de tentativas para evitar loops indevidos.

## Funcionalidades

- **[a] Adicionar** — insere quantos produtos quiser na lista, um por vez, até digitar `s` ou `sair`.
- **[d] Deletar** — mostra a lista numerada e remove o item pelo número escolhido, com validação de índice inválido.
- **[l] Listar** — exibe todos os produtos da lista com seus respectivos índices.
- **[c] Concluir** — finaliza a sessão, exibindo os produtos levados (se houver) ou uma mensagem de despedida (se a lista estiver vazia).
- **Controle de erros** — entradas inválidas (mais de um caractere ou opção inexistente) contam como tentativa; após 3 erros, o sistema se desliga automaticamente.
- **Tela limpa automática** — a cada ação, o terminal é limpo (`cls`/`clear`) para manter a interface organizada.

## Requisitos

- Python 3.14+ (ou qualquer versão 3.x recente, sem dependências externas)

## Como executar

```bash
python main.py
```

Ou, se o projeto estiver usando [uv](https://docs.astral.sh/uv/):

```bash
uv run src/python/main.py
```

## Como usar

1. Ao iniciar, o programa exibe as instruções e pede uma opção.
2. Digite `a`, `d`, `l` ou `c` (letra única, minúscula ou maiúscula) para escolher a ação.
3. Siga as instruções na tela para adicionar, remover ou visualizar os itens.
4. Digite `c` a qualquer momento para concluir e ver o resumo da compra.

## Estrutura do projeto

```
.
├── main.py          # Lógica principal do programa (menu, loop e ações)
└── README.md
```
