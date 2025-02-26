# 📌 TPC3 - Conversor de MarkDown para HTML

## 📅 Data
2025-02-26

## 👤 Autor
- **Nome:** Pedro Figueiredo Pereira
- **Número de Aluno:** A104082
<img src="../guardapedropereira.jpg" alt="Pedro Pereira" width="200" />

## 📖 Resumo
Para resolver o problema de converter MarkDown para HTML, utilizei expressões regulares em Python para identificar e processar os elementos descritos na "Basic Syntax". Segue a descrição da resolução para cada tipo de elemento:

- **Cabeçalhos (Alínea 1):** Utilizei uma expressão regular para identificar linhas começando com `#`, `##` ou `###`. O número de símbolos `#` determina o nível do cabeçalho (`<h1>`, `<h2>`, `<h3>`). Cada linha correspondente é processada para gerar a tag HTML adequada.

- **Texto em Negrito e Itálico (Alínea 2):** Implementei substituições regulares para converter `**texto**` em `<b>texto</b>` e `*texto*` em `<i>texto</i>`. Estas operações são realizadas no processamento inline do texto.

- **Listas Numeradas (Alínea 3):** Detectei itens de lista começando com números seguidos de `.` (ex: `1.`). Os itens são coletados num buffer e, ao sair da lista, gerado o HTML correspondente (`<ol>...</ol>` com `<li>...</li>`).

- **Links (Alínea 4):** Utilizei regex para identificar padrões `[texto](url)` e converter em `<a href="url">texto</a>`.

- **Imagens (Alínea 5):** Implementei regex para processar `![alt](url)` em `<img src="url" alt="alt"/>`. Importante processar imagens **antes** dos links para evitar conflitos de padrões.

## 📂 Resultados
Segue a localização dos ficheiros produzidos:
- [`MDToHTML.py`](MDToHTML.py) - [Ficheiro com código fonte]
- [`output.html`](output.html) - [Ficheiro de saída]

---