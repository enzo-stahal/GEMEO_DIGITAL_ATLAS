import random
import time
from colorama import Fore, Style, init

# Inicializa o colorama para funcionar corretamente em todos os terminais (inclusive Windows)
init(autoreset=True)

nome_missao = "Atlas Odyssey"
nome_equipe = "Orbit Engineers"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# === NOVA ETAPA: CALIBRAÇÃO ESTATÍSTICA REAL (1957-2018) ===
ERAS_ESPACIAIS = {
    "1": {"nome": "Início da Corrida Espacial (1957-1969)", "falha_base": 0.35},
    "2": {"nome": "Maturação Orbital (1970-1999)", "falha_base": 0.15},
    "3": {"nome": "Era Moderna (2000-2018)", "falha_base": 0.05}
}

print(Fore.CYAN + "===============================================" + Style.RESET_ALL)
print(Fore.CYAN + "     SIMULADOR GEMEO DIGITAL - MISSION CONTROL " + Style.RESET_ALL)
print(Fore.CYAN + "===============================================" + Style.RESET_ALL)
print("Selecione a Era Historica Aeroespacial para calibrar o simulador:")
for k, v in ERAS_ESPACIAIS.items():
    print(f"{k} - {v['nome']} (Taxa Historica de Falhas: {v['falha_base']*100}%)")

escolha = input("\nEscolha a opção (1, 2 ou 3): ")
era_selecionada = ERAS_ESPACIAIS.get(escolha, ERAS_ESPACIAIS["3"])
taxa_falha = era_selecionada["falha_base"]

# Gerando 6 ciclos de telemetria baseados na probabilidade da Era escolhida
dados_missao = []
for _ in range(6):
    if random.random() < taxa_falha: # Injeção de estresse/anomalia histórica
        temp = random.randint(31, 42)     # Temperatura Elevada ou Crítica
        com = random.randint(10, 55)      # Comunicação Instável ou Crítica
        bat = random.randint(5, 45)       # Bateria Crítica ou Baixa
        oxigenio = random.randint(70, 85) # Oxigênio Crítico ou Baixo
        estab = random.randint(30, 65)    # Estabilidade Crítica ou Reduzida
    else: # Parâmetros 100% Nominais/Estáveis
        temp = random.randint(20, 28)
        com = random.randint(85, 100)
        bat = random.randint(80, 100)
        oxigenio = random.randint(92, 100)
        estab = random.randint(85, 100)
    
    dados_missao.append([temp, com, bat, oxigenio, estab])


def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação crítica"
    elif valor <= 59:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria crítica"
    elif valor <= 49:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio crítico"
    elif valor <= 89:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade crítica"
    elif valor <= 69:
        return "ATENÇÃO", 1, "Estabilidade reduzida"
    else:
        return "NORMAL", 0, "Estabilidade adequada"


def classificar_ciclo(pontos):
    if pontos <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontos <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def analisar_tendencia(primeiro, ultimo):
    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável."


def gerar_recomendacao(
    status_temperatura,
    status_comunicacao,
    status_bateria,
    status_oxigenio,
    status_estabilidade
):
    recomendacoes = []

    if status_temperatura == "CRÍTICO":
        recomendacoes.append("Verificar controle térmico da missão.")
    elif status_temperatura == "ATENÇÃO":
        recomendacoes.append("Monitorar aumento de temperatura.")

    if status_comunicacao == "CRÍTICO":
        recomendacoes.append("Tentar restabelecer contato com a base.")
    elif status_comunicacao == "ATENÇÃO":
        recomendacoes.append("Monitorar estabilidade da comunicação.")

    if status_bateria == "CRÍTICO":
        recomendacoes.append("Ativar modo de economia de energia.")
    elif status_bateria == "ATENÇÃO":
        recomendacoes.append("Reduzir consumo energético.")

    if status_oxigenio == "CRÍTICO":
        recomendacoes.append("Acionar protocolo de suporte à vida.")
    elif status_oxigenio == "ATENÇÃO":
        recomendacoes.append("Monitorar níveis de oxigênio.")

    if status_estabilidade == "CRÍTICO":
        recomendacoes.append("Reduzir operações não essenciais.")
    elif status_estabilidade == "ATENÇÃO":
        recomendacoes.append("Revisar estabilidade operacional.")

    if len(recomendacoes) == 0:
        return "Manter operação normal e continuar monitoramento."

    return " | ".join(recomendacoes)


print("\n" + "=" * 60)
print(Fore.CYAN + "MISSION CONTROL AI" + Style.RESET_ALL)
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos: {len(dados_missao)}")
print("=" * 60)

riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]

for i, ciclo in enumerate(dados_missao):

    print(f"\nCICLO {i + 1}")
    print("-" * 50)

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    analises = [
        analisar_temperatura(temperatura),
        analisar_comunicacao(comunicacao),
        analisar_bateria(bateria),
        analisar_oxigenio(oxigenio),
        analisar_estabilidade(estabilidade)
    ]

    nomes = [
        "Temperatura",
        "Comunicação",
        "Bateria",
        "Oxigênio",
        "Estabilidade"
    ]

    valores = [temperatura, comunicacao, bateria, oxigenio, estabilidade]
    unidades = ["°C", "%", "%", "%", "%"]

    risco_total = 0

    # COLORIR CADA SENSOR INDIVIDUALMENTE
    for j in range(5):
        status, pontos, mensagem = analises[j]
        risco_total += pontos
        pontuacao_areas[j] += pontos

        # Escolhe a cor baseada no status do sensor
        if status == "CRÍTICO":
            cor_status = Fore.RED + Style.BRIGHT
        elif status == "ATENÇÃO":
            cor_status = Fore.YELLOW + Style.BRIGHT
        else:
            cor_status = Fore.GREEN

        print(f"{nomes[j]}: {valores[j]}{unidades[j]} | {cor_status}{status}{Style.RESET_ALL} | {mensagem}")

    classificacao = classificar_ciclo(risco_total)

    # COLORIR A CLASSIFICAÇÃO GERAL DO CICLO
    if "CRÍTICA" in classificacao:
        cor_ciclo = Fore.RED + Style.BRIGHT
    elif "ATENÇÃO" in classificacao:
        cor_ciclo = Fore.YELLOW + Style.BRIGHT
    else:
        cor_ciclo = Fore.GREEN + Style.BRIGHT

    recomendacao = gerar_recomendacao(
        analises[0][0], analises[1][0], analises[2][0], analises[3][0], analises[4][0]
    )

    print(f"\nPontuação de risco: {risco_total}")
    print(f"Classificação: {cor_ciclo}{classificacao}{Style.RESET_ALL}")
    
    # Destaca as recomendações em vermelho claro se o risco for crítico
    if risco_total > 5:
        print(Fore.LIGHTRED_EX + f"Recomendação: {recomendacao}" + Style.RESET_ALL)
    else:
        print(f"Recomendação: {recomendacao}")

    riscos_ciclos.append(risco_total)


# === RELATÓRIO FINAL COM DESTAQUES E CORES ===
print("\n" + "=" * 60)
print(Fore.CYAN + "RELATÓRIO FINAL" + Style.RESET_ALL)
print("=" * 60)

media_temperatura = sum([c[0] for c in dados_missao]) / len(dados_missao)
media_comunicacao = sum([c[1] for c in dados_missao]) / len(dados_missao)
media_bateria = sum([c[2] for c in dados_missao]) / len(dados_missao)
media_oxigenio = sum([c[3] for c in dados_missao]) / len(dados_missao)
media_estabilidade = sum([c[4] for c in dados_missao]) / len(dados_missao)

print(f"Média temperatura: {media_temperatura:.2f} °C")
print(f"Média comunicação: {media_comunicacao:.2f}%")
print(f"Média bateria: {media_bateria:.2f}%")
print(f"Média oxigênio: {media_oxigenio:.2f}%")
print(f"Média estabilidade: {media_estabilidade:.2f}%")

maior_risco = max(riscos_ciclos)
ciclo_critico = riscos_ciclos.index(maior_risco) + 1

print(f"\nCiclo mais crítico: {Fore.RED}Ciclo {ciclo_critico}{Style.RESET_ALL}")
print(f"Maior risco cadastrado: {Fore.RED}{maior_risco}{Style.RESET_ALL} pontos")

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)
print(f"Risco médio geral: {risco_medio:.2f}")

ciclos_criticos = sum(1 for risco in riscos_ciclos if risco >= 6)
if ciclos_criticos > 0:
    print(f"Quantidade de ciclos críticos: {Fore.RED}{ciclos_criticos}{Style.RESET_ALL}")
else:
    print(f"Quantidade de ciclos críticos: {Fore.GREEN}{ciclos_criticos}{Style.RESET_ALL}")

print("\nTendência da missão:")
tendencia_msg = analisar_tendencia(riscos_ciclos[0], riscos_ciclos[-1])
if "piora" in tendencia_msg:
    print(Fore.RED + tendencia_msg + Style.RESET_ALL)
elif "melhora" in tendencia_msg:
    print(Fore.GREEN + tendencia_msg + Style.RESET_ALL)
else:
    print(tendencia_msg)

print("\nPontuação total acumulada por área:")
for i in range(len(areas_monitoradas)):
    print(f"- {areas_monitoradas[i]}: {pontuacao_areas[i]} pontos")

maior_area = max(pontuacao_areas)
indice_area = pontuacao_areas.index(maior_area)

print(f"\nÁrea mais severamente afetada: {Fore.RED}{Style.BRIGHT}{areas_monitoradas[indice_area]}{Style.RESET_ALL}")

classificacao_final = classificar_ciclo(int(risco_medio))

# Cor para a conclusão final da simulação
if "CRÍTICA" in classificacao_final:
    cor_final = Fore.RED + Style.BRIGHT
    conclusao_txt = "A missão apresentou risco operacional elevado."
elif "ATENÇÃO" in classificacao_final:
    cor_final = Fore.YELLOW + Style.BRIGHT
    conclusao_txt = "A missão apresentou instabilidades moderadas."
else:
    cor_final = Fore.GREEN + Style.BRIGHT
    conclusao_txt = "A missão operou dentro dos parâmetros esperados."

print(f"Classificação final do Gêmeo Digital: {cor_final}{classificacao_final}{Style.RESET_ALL}")
print(f"\nConclusão Diagnóstica: {cor_final}{conclusao_txt}{Style.RESET_ALL}")