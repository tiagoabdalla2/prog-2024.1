import random

from jogo.personagens.monstro import Monstro
from jogo.personagens.aventureiro import Aventureiro
from jogo.personagens.tesouro import Tesouro

from jogo import mapa

def iniciar_combate(aventureiro, monstro):
    """
    Executa um loop infinito, que possui as seguintes etapas:
    - Calcula o dano causado pelo aventureiro
    - Monstro faz a sua defesa
    - Exibe na tela o dano causado pelo aventureiro e a vida atual do monstro
    - Se o monstro não está mais vivo, retorna True
    - Calcula o dano causado pelo monstro
    - Aventureiro faz sua defesa
    - Exibe na tela o dano causado pelo monstro e a vida atual do aventureiro
    - Se o aventureiro não está mais vivo, retorna False
    """
    while True:
        dano = aventureiro.atacar()
        monstro.defender(dano)
        print(f"{aventureiro.nome} causa {dano} de dano! Vida do monstro: {monstro.vida}")
        if not monstro.esta_vivo():
            print("Monstro foi derrotado!")
            return True

        dano = monstro.atacar()
        aventureiro.defender(dano)
        print(f"Monstro causa {dano} de dano! Vida de {aventureiro.nome}: {aventureiro.vida}")
        if not aventureiro.esta_vivo():
            print(f"{aventureiro['nome']} foi derrotado!")
            return False

def movimentar(aventureiro, direcao):
    """
    Realiza a ação de movimento e analisa as consequências.

    Chama a função aventureiro.andar e analisa o seu resultado. Se for False,
    ou seja, se o aventureiro não tiver andado nada, retorna True.

    Em seguida, analisa o efeito do movimento. Há 60% de chance de nada
    acontecer, e 40% de chance de um monstro aparecer (pesquise sobre a função
    random.choices).

    Se um monstro aparecer, inicia um novo monstro e retorna e resultado da
    função iniciar_combate.

    Caso não seja um monstro, retorna True.
    """
    if not aventureiro.andar(direcao):
        return True

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = Monstro()
        return iniciar_combate(aventureiro, monstro)

    return True

def jogo():
    """
    Fluxo principal do jogo, possui as seguintes etapas:
    - Inicia um aventureiro
    - Inicia um tesouro
    - Desenha o mapa pela primeira vez
    - Em um loop infinito:
        - Lê o comando inserido pelo usuário
        - Se for o comando "Q", encerra o programa
        - Se for o comando "T", exibe os atributos do aventureiro
        - Se o comando for "W", "A", "S" ou "D":
            - Realiza o movimento e verifica o resultado da função movimentar
            - Se o resultado for True, desenha novamente o mapa
            - Se for False, imprime "Game over" na tela e encerra o programa
        - Se o usuário inserir algum comando diferente, diz que não reconheceu
        - Se a posição do aventureiro for igual à posição do tesouro, dispara
        uma mensagem que o aventureiro ganhou o jogo
    """
    aventureiro = Aventureiro()
    tesouro = Tesouro()

    print(f"Saudações, {aventureiro.nome}! Boa sorte!")

    mapa.desenhar(aventureiro, tesouro)

    while True:
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break
        elif op == "T":
            print(aventureiro)
        elif op in ["W", "A", "S", "D"]:
            if movimentar(aventureiro, op):
                mapa.desenhar(aventureiro, tesouro)
            else:
                print("Game Over...")
                break
        else:
            print(f"{aventureiro.nome}, não conheço essa opção! Tente novamente!")

        if aventureiro.posicao == tesouro.posicao:
            print(f"Parabéns, {aventureiro.nome}! Você encontrou o tesouro!")
            break
