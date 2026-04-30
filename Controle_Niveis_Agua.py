import colorama
from colorama import Fore, Style

#Iniciar o colorama para Windows
colorama.init()

def controle_nivel(nivel_alerta):

#List de SITUAÇÕES conforme a progressão de risco
    situacoes = [
        "Muito baixo (crítico)", # Nível 1
        "Baixo",                 # Nível 2
        "Médio",                 # Nível 3
        "Alto",                  # Nível 4
        "Muito alto (alerta)"    # Nível 5
    ]

#Lista de CORES conforme cada nível
    cores = [
        Fore.RED,     # Nível 1
        Fore.YELLOW,  # Nível 2
        Fore.GREEN,   # Nível 3
        Fore.CYAN,    # Nível 4
        Fore.BLUE     # Nível 5
    ]

#DICA: Como a lista começa no índice 0, subtrair 1 do nível informado
    indice = nivel_alerta - 1
    
    cor_escolhida = cores[indice]
    mensagem = situacoes[indice]

#Saída do monitoramento
    print(f" Nível {nivel_alerta} -> {cor_escolhida}{mensagem}{Style.RESET_ALL}")

#Relatorio 
print("="*35)
print("    CONTROLE DE NÍVEIS DE ÁGUA    ")
print("="*35)

print("Início do monitoramento:\n ")

#Simulação com valores definidos no código
niveis_para_testar = [1, 2, 3, 4, 5]
for n in niveis_para_testar:
    controle_nivel(n)

print("\nFim do monitoramento ")
print("="*35)
