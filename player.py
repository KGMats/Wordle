from utils import load_words, language
from math import log2


PALAVRAS_POSSIVEIS = [x for x in load_words() if len(x) == 5] # Palavras com comprimento diferente de 5 não são possibilidades


# Openers pre calculados para melhorar o desempenho do programa.
# Para listas de palavras diferentes essas podem não ser necessariamente
# as melhores paravras de abertura.

OPENERS = {
        'pt': 'SERIA',
        'en': 'TEARS',
        'sp': 'NORIA',
        'it': 'SERIO',
        'fr': 'LAINE'
        } 

def simulate_feedback(word: str, guess: str) -> list[str]:
    feedback = ["RED"] * 5
    word_chars = list(word)
    guess_chars = list(guess)
    letter_counts = {}

    for char in word_chars:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    for i in range(5):
        if guess_chars[i] == word_chars[i]:
            feedback[i] = "GREEN"
            letter_counts[guess_chars[i]] -= 1

    for i in range(5):
        letra = guess_chars[i]
        if feedback[i] == "RED" and letra in letter_counts and letter_counts[letra] > 0:
            feedback[i] = "YELLOW"
            letter_counts[letra] -= 1

    return feedback



def filter_words(guess: list, feedback: list) -> list[str]:
    global PALAVRAS_POSSIVEIS
    nova_lista = []

    for palavra_possivel in PALAVRAS_POSSIVEIS:
        fb = simulate_feedback(palavra_possivel, guess)
        if fb == feedback:
            nova_lista.append(palavra_possivel)

    PALAVRAS_POSSIVEIS = nova_lista
    return PALAVRAS_POSSIVEIS

def escolha_com_entropia() -> str:
    melhor_palavra = None
    melhor_entropia = -1
    numero_possibilidades = len(PALAVRAS_POSSIVEIS)
    for chute in PALAVRAS_POSSIVEIS:
        entropia_media = 0
        padroes = {}

        for palavra_possivel in PALAVRAS_POSSIVEIS:
            feedback = tuple(simulate_feedback(palavra_possivel, chute))

            if feedback not in padroes:
                padroes[feedback] = 1
            else:
                padroes[feedback] += 1

        items = padroes.items()
        for feedback, qtde in items:
            prob = qtde / numero_possibilidades
            entropia = -prob * log2(prob)
            entropia_media += entropia

        if entropia_media > melhor_entropia:
            melhor_palavra = chute
            melhor_entropia = entropia_media

    
    return melhor_palavra


def player(guess_hist: list, res_hist: list) -> str:
    global PALAVRAS_POSSIVEIS
    if len(res_hist) == 0: # Primeiro chute
        return OPENERS[language]


    PALAVRAS_POSSIVEIS = filter_words(guess_hist[-1], res_hist[-1])
    palavra_possivel = escolha_com_entropia()
    return palavra_possivel
