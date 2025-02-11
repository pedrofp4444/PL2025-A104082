# 📌 TPC1 - Configuração do Repositório e somador on/off

## 📅 Data
11/02/2025

## 👤 Autor
- **Nome:** Pedro Figueiredo Pereira
- **Número de Aluno:** A104082
- ![Pedro Pereira](../guardapedropereira.jpg)

## 📖 Resumo
Este trabalho consistiu em:
- Criar o respositório para disponibilizar a resolução dos trabalhos práticos;
- Definir a estruturação dos conteúdos do repositório;
- Resolver o problema proposto, para tal, segui o seguinte raciocínio:
  - Criação de duas variáveis: acc(acumular o valor total da soma dos números) e summing(booleano para verificar a possibilidade de acumular o valor);
  - Leitura do ficheiro do stdin linha a linha;
  - Iteração pelos caracteres de cada linha e verificação se é um digito:
    - Se sim, guarda a posição do digito e procura o próximo caracter enquanto for um digito e menor que o tamanho da linha;
    - Se não, converte para inteiro o número preservado entre a posição inicial e atual da iteração;
    - Se summing for verdadeiro, acumula o valor do número na variável acc;
  - Se a posição da linha não for um digito, verifica é:
    - Se for um on (após colocar todas as letras em minúsculas), ativa o summing;
    - Se for um off (após colocar todas as letras em minúsculas), desativa o summing;
    - Se for um igual imprime o valor acumulado;

## 📂 Resultados
O resultado deste trabalho é, numa primeira instância, a criação do presente repositório, disponível em https://github.com/pedrofp4444/PL2025-A104082.

Segue a localização dos ficheiros produzidos:
- [`tpc1.py`](tpc1.py) - [Ficheiro com código fonte] 
- [`test.txt`](test.txt) - [Ficheiro com exemplo de teste]

---
