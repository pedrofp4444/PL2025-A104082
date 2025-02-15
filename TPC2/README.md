# 📌 TPC2 - Análise de um dataset de obras musicais

## 📅 Data
15/02/2025

## 👤 Autor
- **Nome:** Pedro Figueiredo Pereira
- **Número de Aluno:** A104082
<img src="../guardapedropereira.jpg" alt="Pedro Pereira" width="200" />

## 📖 Resumo
Para resolver o problema proposto, priorizei a leitura linha a linha do stdin, para tal desenvolvi um script para cada alínea do enunciado. Segue a descrição da resolução de cada alínea:
  - **Alínea 1:** Na alínea 1 pretende-se que sejam ordenados por ordem alfabética os compositores de cada obra do csv fornecido. Comecei por definir uma expressão regular que os identificasse e isolei o nome dos mesmos num grupo da expressão. De seguida, a cada linha do stdin aplico a expressão regular e guardo o nome do compositor numa lista. No final, ordeno a estrutura e imprimo o resultado.
  - **Alínea 2:** Na alínea 2 pretende-se que seja determinado o número de obras por cada período. Na mesma linha de racíocinio da alínea anterior, defini uma expressão regular que identificasse o período de cada obra e isolei o mesmo num grupo da expressão. A cada linha do stdin aplico a expressão regular e, para cada período, verifico se já existe no meu dicionário de períodos essa entrada, se não, crio uma nova entrada com o valor 1 (primeira ocorrência), se sim, incremento o valor da entrada. No final, imprimo o resultado.
  - **Alínea 3:** Na alínea 3 pretende-se que seja associada uma lista dos títulos das obras de cada época (ordenada alfabeticamente) ao período correspondente. Comecei por definir uma expressão regular que identificasse o titulo e periodo da obra em grupos, respetivamente. No entanto, ao fazer a leitura linha a linha do stdin deparei-me com a falha da identificação de padrões na medida em que as descrições continham quebras de linha e, por isso, não consegui implementar a solução. Em alternativa, criei um script de normalização do ficheiro obras.csv, que consiste em substituir as quebras de linha por espaços e, assim, permitir a identificação dos padrões pois uma entrada do csv fica associada a uma e apenas uma linha. Finalmente, apliquei a expressão regular inicialmente definida e, para cada linha, guardei o periodo no dicionário e adicionei o titulo da obra à lista de títulos associada ao periodo. No final, ordenei a lista de títulos de cada periodo e imprimi o resultado.
  
## 📂 Resultados
Segue a localização dos ficheiros produzidos:
- [`ordenarCompositores.py`](ordenarCompositores.py) - [Ficheiro com código fonte]
- [`obrasPorPeriodo.py`](obrasPorPeriodo.py) - [Ficheiro com código fonte]
- [`fomatarCSV.py`](fomatarCSV.py) - [Ficheiro com código fonte]
- [`titulosPorPeriodo.py`](titulosPorPeriodo.py) - [Ficheiro com código fonte]
- [`obras.csv`](obras.csv) - [Ficheiro com exemplo de teste]
- [`obras_normalizado.csv`](obras_normalizado.csv) - [Ficheiro com exemplo de teste]

---
