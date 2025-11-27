# batalha_naval.py

import random

def criar_tabuleiro(size):
    return [['~'] * size for _ in range(size)]

def imprimir_tabuleiro(tab):
    size = len(tab)
    # cabeçalho com colunas
    letras = [chr(ord('A') + i) for i in range(size)]
    print('  ' + ' '.join(letras))
    for idx, linha in enumerate(tab):
        print(f"{idx+1:2d} " + ' '.join(linha))
    print()

def posicionar_navios(tab, navios):
    size = len(tab)
    for tam in navios:
        colocado = False
        while not colocado:
            orient = random.choice(['H','V'])
            if orient == 'H':
                row = random.randint(0, size-1)
                col = random.randint(0, size-tam)
                if all(tab[row][col+i] == '~' for i in range(tam)):
                    for i in range(tam):
                        tab[row][col+i] = 'N'
                    colocado = True
            else:  # vertical
                row = random.randint(0, size-tam)
                col = random.randint(0, size-1)
                if all(tab[row+i][col] == '~' for i in range(tam)):
                    for i in range(tam):
                        tab[row+i][col] = 'N'
                    colocado = True

def jogar():
    size = 8
    navios = [5, 4, 3, 3, 2]  # tamanhos típicos
    tab_oculto = criar_tabuleiro(size)
    tab_jogo = criar_tabuleiro(size)
    posicionar_navios(tab_oculto, navios)
    tiros = 0

    print("Bem-vindo à Batalha Naval!")
    while True:
        imprimir_tabuleiro(tab_jogo)
        jogada = input("Digite coordenada (Ex: A3): ").strip().upper()
        if len(jogada) < 2:
            print("Entrada inválida.")
            continue
        col = ord(jogada[0]) - ord('A')
        try:
            row = int(jogada[1:]) - 1
        except ValueError:
            print("Entrada inválida.")
            continue
        if not (0 <= row < size and 0 <= col < size):
            print("Coordenada fora do tabuleiro.")
            continue

        tiros += 1
        if tab_oculto[row][col] == 'N':
            print("💥 Acertou um navio!")
            tab_jogo[row][col] = 'X'
            tab_oculto[row][col] = '~'
        else:
            print("Água.")
            tab_jogo[row][col] = 'O'

        # checar vitória
        if all(tab_oculto[r][c] != 'N' for r in range(size) for c in range(size)):
            imprimir_tabuleiro(tab_jogo)
            print(f"Parabéns! Você afundou toda a frota em {tiros} tiros.")
            break

if __name__ == "__main__":
    jogar()
