
import os
import sys
import time
import platform
import random
from datetime import datetime

# Cores ANSI
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def carregar():
    print(f"\n{CYAN}Inicializando NEXUS...{RESET}")
    for i in range(101):
        barra = "█" * (i // 5) + "░" * (20 - i // 5)
        print(f"\r[{barra}] {i}%", end="", flush=True)
        time.sleep(0.02)
    print(f"\n{GREEN}Sistema inicializado!{RESET}")

def mostrar_sistema():
    limpar()

    print(f"""{CYAN}{BOLD}
╔══════════════════════════════════════╗
║             NEXUS SYSTEM             ║
║          PYTHON ENVIRONMENT          ║
╚══════════════════════════════════════╝
{RESET}""")

    print(f"{GREEN}[+] Sistema operacional:{RESET} {platform.system()}")
    print(f"{GREEN}[+] Versão:{RESET} {platform.version()}")
    print(f"{GREEN}[+] Arquitetura:{RESET} {platform.machine()}")
    print(f"{GREEN}[+] Processador:{RESET} {platform.processor()}")
    print(f"{GREEN}[+] Python:{RESET} {sys.version.split()[0]}")
    print(f"{GREEN}[+] Data:{RESET} {datetime.now():%d/%m/%Y %H:%M:%S}")

def teste_calculo():
    print(f"\n{YELLOW}Executando teste matemático...{RESET}")
    inicio = time.perf_counter()

    resultado = sum(i * i for i in range(1_000_000))

    fim = time.perf_counter()

    print(f"{GREEN}Resultado:{RESET} {resultado:,}")
    print(f"{GREEN}Tempo:{RESET} {fim - inicio:.4f} segundos")

def monitor():
    print(f"\n{CYAN}Monitor de atividade (simulação){RESET}")
    print("Pressione CTRL+C para sair.\n")

    try:
        while True:
            cpu = random.randint(5, 95)
            ram = random.randint(20, 90)

            print(
                f"\rCPU: {cpu:3}% | RAM: {ram:3}% ",
                end="",
                flush=True
            )

            time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Monitor encerrado.{RESET}")

def menu():
    carregar()

    while True:
        print(f"""
{CYAN}========== MENU PRINCIPAL =========={RESET}

1 - Informações do computador
2 - Teste de processamento
3 - Monitor de atividade (simulado)
4 - Sair
""")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            mostrar_sistema()
        elif opcao == "2":
            teste_calculo()
        elif opcao == "3":
            monitor()
        elif opcao == "4":
            print(f"\n{GREEN}NEXUS encerrado. Até logo!{RESET}")
            break
        else:
            print(f"{RED}Opção inválida!{RESET}")

if __name__ == "__main__":
    menu()
