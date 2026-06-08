# 🚀 Atlas Odyssey — Sistema Integrado de Gêmeo Digital & Monitoramento Aeroespacial
> **Global Solution 2026 — 1° Semestre** > **Curso:** Ciências da Computação | **Turma:** 1CCPX  
> **Instituição:** FIAP  
> **Core Team:** Orbit Engineers  

---

## 👥 Corpo Discente (Orbit Engineers)
* **Enzo Stahal Freitas** — RM: 569001
* **Matheus Bruno de Lima** — RM: 572944

---

## 🛰️ 1. Introdução e Conceito de Gêmeo Digital (Digital Twin)

Na engenharia aeroespacial contemporânea (adotada por agências como NASA e SpaceX), o conceito de **Gêmeo Digital (Digital Twin)** baseia-se na criação de uma réplica virtual de alta fidelidade de um ativo físico. Este modelo digital consome variáveis de estado para simular cenários de estresse, prever falhas catastróficas por fadiga de material ou erros sistêmicos e treinar controladores de voo sem expor tripulações ou hardwares reais a riscos.

O **Atlas Odyssey Mission Control** é um Gêmeo Digital que replica computacionalmente os sensores físicos da cápsula **OrbitalGuard** (desenvolvida em ambiente embarcado Arduino). O sistema processa fluxos contínuos de telemetria estruturada em matrizes e aplica algoritmos de tomada de decisão baseados nas equações booleanas do circuito lógico analógico do **Mission Control AI**.

---

## 📊 2. Modelagem Estatística Descritiva & Injeção de Falhas (1957–2018)

O motor de simulação de telemetria deste software não utiliza coeficientes aleatórios comuns (*pseudo-random* puros). Em vez disso, o gerador estocástico foi calibrado e parametrizado com base no comportamento histórico real extraído de **61 anos de lançamentos orbitais mundiais (1957–2018)**.

Ao iniciar a aplicação, o utilizador calibra as matrizes de sensores selecionando uma de três **Eras Aeroespaciais**. Cada uma possui uma distribuição probabilística de falha baseada no desvio padrão histórico da época:

### ⏳ Definição das Eras de Calibração:
1. **Era 1: Início da Corrida Espacial (1957–1969)**
   * **Probabilidade de Falha por Ciclo:** `35%` ($P(\text{Anomalia}) = 0.35$)
   * **Análise Técnica:** Período caracterizado por altíssima variabilidade tecnológica, ausência de redundâncias eletrônicas e tecnologia de circuitos integrados experimental. O simulador injeta desvios severos e flutuações críticas frequentes.
2. **Era 2: Maturação Orbital (1970–1999)**
   * **Probabilidade de Falha por Ciclo:** `15%` ($P(\text{Anomalia}) = 0.15$)
   * **Análise Técnica:** Época marcada pela estabilização da inserção de satélites em órbita baixa (LEO) e desenvolvimento de estações espaciais (Mir, Skylab). Redução significativa do coeficiente de variação de anomalias.
3. **Era 3: Era Moderna (2000–2018)**
   * **Probabilidade de Falha por Ciclo:** `5%` ($P(\text{Anomalia}) = 0.05$)
   * **Análise Técnica:** Sensores digitais de estado sólido de alta precisão, tolerância a falhas tripla e barramentos de comunicação redundantes. A atividade espacial opera dentro de um desvio padrão controlado, resultando em ciclos predominantemente estáveis.

---

## 📐 3. Arquitetura de Dados & Lógica de Matrizes (Data Structures)

O fluxo de dados do simulador baseia-se em uma estrutura de matriz bidimensional dinâmica (Lista de Listas em Python), onde cada linha representa um **Ciclo de Telemetria** discreto e cada coluna representa o canal de dados de um sensor específico:

$$\text{Ciclo} = [\text{Temperatura}, \text{Comunicação}, \text{Bateria}, \text{Oxigénio}, \text{Estabilidade}]$$

### 🛠️ Transposição da Lógica de Hardware para Software:
As funções de classificação de criticidade do script Python operam como uma emulação de software do circuito lógico implementado fisicamente no Tinkercad. 
O mapeamento de thresholds (limiares) de interrupção respeita estritamente as restrições de engenharia:

* **Temperatura Interna ($T$):** Crítica acima de $35^\circ\text{C}$ (Risco de superaquecimento dos aviônicos).
* **Comunicação com a Base ($C$):** Crítica abaixo de $30\%$ (Perda iminente de pacotes de telemetria).
* **Sistema de Energia/Bateria ($B$):** Crítico abaixo de $20\%$ (Subtensão nas barras de corrente contínua).
* **Suporte de Oxigênio ($O$):** Crítico abaixo de $80\%$ (Hipóxia na cabine tripulada).
* **Estabilidade Operacional ($E$):** Crítica abaixo de $40\%$ (Instabilidade estrutural ou oscilação aerodinâmica).

Cada sensor atribui uma pontuação de risco ponderada ($0$ para Normal, $1$ para Atenção, $2$ para Crítico). O risco acumulado determina a classificação do ciclo:
* $\Sigma \text{ Pontos} \le 2 \rightarrow$ **Missão Estável** (Interface Verde 🟢)
* $\Sigma \text{ Pontos} \le 5 \rightarrow$ **Missão em Atenção** (Interface Amarela 🟡)
* $\Sigma \text{ Pontos} > 5 \rightarrow$ **Missão Crítica** (Interface Vermelha 🔴)

---

## 🎨 4. Design de Interface de Linha de Comando (CLI)

O console foi projetado utilizando códigos de escape ANSI através da biblioteca `colorama` para prover feedback visual analítico imediato, simulando as telas de diagnóstico CRT dos antigos centros de controle da NASA.

* `Fore.GREEN`: Parâmetros Nominais e Operação Segura.
* `Fore.YELLOW`: Estados de Alerta que exigem monitoramento preventivo.
* `Fore.RED`: Falhas Críticas que demandam interrupção imediata ou atuação de protocolos de emergência.
* `Style.BRIGHT`: Utilizado para aumentar a luminância de labels cruciais de diagnóstico.

---

### 🔧 Pré-requisitos do Sistema
* Python 3.8 ou superior instalado.
* Git configurado na máquina local.