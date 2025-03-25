# **Simulador de Jornada Pokémon**  

## **Descrição**  
Este projeto consiste na implementação de um **simulador de jornada Pokémon** utilizando **Python** e a biblioteca **NetworkX** para a construção e visualização de **grafos**. O objetivo é otimizar a movimentação do treinador entre cidades, capturar Pokémon e gerenciar recursos até alcançar o destino final.  

O trabalho foi desenvolvido para a disciplina de **Algoritmos e Estruturas de Dados II**, explorando conceitos de **grafos, algoritmos de caminho mínimo e simulação baseada em regras**.  

---

## **Tecnologias Utilizadas**  
- **Python 3.8+**  
- **NetworkX** (Para representação e manipulação de grafos)  
- **Matplotlib** (Para visualização dos grafos)  
- **Requests** (Para obter dados da PokéAPI)  

---

## **Funcionalidades**  
### ✅ **Leitura do Arquivo de Configuração**  
- O sistema lê um **arquivo de configuração** contendo o **mapa do jogo**, conexões entre cidades e informações sobre Pokémon iniciais e finais.  
- O mapa é representado como um **grafo não direcionado ponderado**, onde os pesos representam a distância entre as cidades.  

### ✅ **Exibição do Mapa (Grafo)**  
- O grafo é desenhado utilizando **NetworkX e Matplotlib**, mostrando as conexões entre cidades e suas respectivas distâncias.  

### ✅ **Planejamento de Rotas**  
- O algoritmo de **Dijkstra** é usado para encontrar o caminho mais curto entre a cidade inicial e o destino final.  
- Opcionalmente, um algoritmo baseado no **Caixeiro Viajante (TSP)** pode ser utilizado para visitar todas as cidades antes de chegar ao destino final.  

### ✅ **Captura de Pokémon**  
- O sistema obtém dados da **PokéAPI** para determinar a **chance de captura** de cada Pokémon.  
- A captura é simulada com base em uma **probabilidade aleatória**, considerando o número de **Pokébolas disponíveis**.  

### ✅ **Gerenciamento de Recursos**  
- O jogador começa com um **número limitado de Pokébolas e poções**.  
- O sistema permite o uso de **itens para melhorar a jornada**.  

### ✅ **Interface Simples (Texto)**  
- O jogo possui um **menu interativo** onde o jogador pode:  
  - **Mover-se** entre cidades.  
  - **Capturar Pokémon**.  
  - **Visualizar status e itens**.  
  - **Sair do jogo**.  

---

## **Como Executar o Projeto**  
### **1️⃣ Instalar Dependências**  
Antes de executar o projeto, instale os pacotes necessários:  
```sh
pip install networkx matplotlib requests
```  

### **2️⃣ Executar o Programa**  
```sh
python main.py
```  

---

## **Estrutura do Código**  
```plaintext
📂 simulador_pokemon
│── 📄 main.py             # Arquivo principal do jogo
│── 📄 configuracao.py      # Leitura do arquivo de configuração
│── 📄 grafo.py             # Implementação do grafo e exibição
│── 📄 captura.py           # Simulação de captura de Pokémon
│── 📄 treinador.py         # Classe para gerenciar o treinador
│── 📄 algoritmos.py        # Implementação dos algoritmos de caminho mínimo
│── 📄 README.md            # Documentação do projeto
│── 📄 config.txt           # Arquivo de configuração do mapa
```  

---

## **Exemplo do Arquivo de Configuração (`config.txt`)**  
```ini
[kanto]
pikachu

[alola] 7 [kanto]
[kanto] 12 [johto]
[johto] 9 [hoenn]

[paldea]
Sprigatito
```  

---

## **Autores**  
- **João Pedro Valente**  
- **Thales Rodrigues**  
- Disciplina: **Algoritmos e Estruturas de Dados II**    
