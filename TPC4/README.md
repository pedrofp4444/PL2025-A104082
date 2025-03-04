# 📌 TPC4 - Analisador Léxico para Linguagem de Query

## 📅 Data
2025-03-04

## 👤 Autor
- **Nome:** Pedro Figueiredo Pereira
- **Número de Aluno:** A104082
<img src="../guardapedropereira.jpg" alt="Pedro Pereira" width="200" />

## 📖 Resumo
Para resolver o problema de construir um analisador léxico para uma linguagem de query, utilizei o módulo `ply.lex` em Python. O objetivo era criar um tokenizer capaz de processar consultas semelhantes às utilizadas em certas linguagens de query, reconhecendo palavras reservadas, identificadores, strings, símbolos e números. Segue a descrição da resolução:

- **Palavras Reservadas:** Utilizei um dicionário para mapear palavras reservadas como `SELECT`, `WHERE`, `LIMIT` e outras. Durante o processamento de identificadores, verifico se o valor está no dicionário para atribuir o tipo correto.

- **Identificadores:** Aceitam caracteres alfanuméricos e colons (`:`), adequados para IRIs (ex: `dbo:MusicalArtist`).

- **Strings:** A regex `r'"[^"]*"(?:@[a-zA-Z]+)?'` captura strings entre aspas duplas, permitindo tags de idioma opcionais (ex: `@en`).

- **Números:** Capturados como sequências de dígitos e convertidos para inteiros.

- **Símbolos:** Definidos por regex simples, como `.` (ponto), `?` (interrogação), `=` (igual), `{`, `}`.

- **Comentários:** Linhas começando com `#` são ignoradas.

- **Rastreamento de Linhas:** A regra `t_newline` atualiza o contador de linhas (`lineno`) para facilitar depuração.

## 📂 Resultados
Segue a localização dos ficheiros produzidos:
- [`lexical_analyzer.py`](lexical_analyzer.py) - [Ficheiro com código fonte]

---
