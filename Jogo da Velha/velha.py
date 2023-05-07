# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 9)

# Função para verificar se houve um vencedor
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True
    
    # Verificar colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    
    return False

# Função para verificar se o tabuleiro está completamente preenchido
def tabuleiro_completo(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

# Função principal do jogo da velha
def jogar_jogo_da_velha():
    # Criar tabuleiro vazio
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # Variável para controlar o jogador atual (X ou O)
    jogador_atual = "X"

    # Loop principal do jogo
    while True:
        # Imprimir o tabuleiro
        imprimir_tabuleiro(tabuleiro)

        # Obter a posição desejada pelo jogador atual
        linha = int(input("Digite o número da linha (0 a 2): "))
        coluna = int(input("Digite o número da coluna (0 a 2): "))

        # Verificar se a posição é válida
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Posição inválida! Tente novamente.")
            continue
        
        # Verificar se a posição já está ocupada
        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada! Tente novamente.")
            continue

        # Preencher a posição com o símbolo do jogador atual
        tabuleiro[linha][coluna] = jogador_atual

        # Verificar se o jogador atual venceu
        if verificar_vencedor(tabuleiro, jogador_atual):
            print("Jogador", jogador_atual, "venceu!")
            break
        
        # Verificar se o tabuleiro está completo (empate)
        if tabuleiro_completo(tabuleiro):
            print("O jogo empatou!")
            break
        
        # Alternar para o próximo jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Executar o jogo
jogar_jogo_da_velha(2)