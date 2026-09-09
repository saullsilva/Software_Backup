# 💾 Software Backup

Um software de backup desenvolvido em **Python** com o objetivo de facilitar a seleção e preservação de arquivos pessoais antes de uma formatação ou reinstalação do sistema.

> 🚧 **Projeto em desenvolvimento (Beta)**

## 📌 Sobre o projeto

O **Software Backup** analisa os arquivos do diretório pessoal do usuário, organiza-os por tipo e permite selecionar quais arquivos devem ser preservados.

A proposta é tornar o processo de backup mais simples, permitindo que o usuário escolha exatamente o que deseja salvar em um arquivo `.backup`.

Atualmente, o projeto já possui:

* 🔎 Varredura de arquivos do diretório pessoal
* 📂 Classificação de arquivos por categoria
* 🗂️ Organização por extensão
* ☑️ Seleção de tipos inteiros ou arquivos individuais
* 📜 Visualização de nome, tamanho e última modificação
* 📦 Criação de arquivos `.backup`
* 🚫 Exclusão de diretórios que não são relevantes para o backup pessoal

## 🖥️ Funcionamento

O fluxo atual do programa é:

```text
Scanner
   ↓
Análise dos arquivos
   ↓
Classificação
   ↓
Organização por tipo
   ↓
Seleção dos arquivos
   ↓
Criação do arquivo .backup
```

A interface permite selecionar um tipo inteiro:

```text
☐ .pdf (15 arquivos)
☐ .jpg (32 arquivos)
```

ou expandir o tipo para selecionar arquivos individualmente:

```text
▼ .pdf (15 arquivos)

    ☐ trabalho.pdf   | 2.4 MB | 08/09/2026 18:20
    ☐ projeto.pdf    | 1.1 MB | 05/09/2026 14:10
    ☐ documento.pdf  | 800 KB | 28/08/2026 10:30
```

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **Tkinter** — interface gráfica
* **pathlib** — manipulação de caminhos e arquivos
* **zipfile** — criação do arquivo de backup
* **Git / GitHub** — controle de versão

## 📁 Estrutura do projeto

```text
Software_Backup/
│
├── analise/
├── backup/
├── database/
├── interface/
│   └── interface.py
├── models/
├── scanner/
│   └── Scanner.py
├── main.py
├── .gitignore
└── README.md
```

## 📦 Backup

Os arquivos selecionados pelo usuário são armazenados em:

```text
backup/backup.backup
```

Atualmente, o `.backup` utiliza internamente o formato ZIP para armazenar os arquivos selecionados.

## 🔮 Próximos passos

O projeto ainda está em desenvolvimento. Entre as próximas funcionalidades planejadas estão:

* 🔄 Restauração dos arquivos através do próprio programa
* 📍 Preservação do caminho original dos arquivos
* 💾 Escolha do local para salvar o backup
* 🕒 Histórico de backups
* 🗃️ Melhor organização entre arquivos pessoais, configurações e arquivos ignorados
* ☁️ Possibilidade de armazenamento externo ou em nuvem
* ⚙️ Mais opções de configuração para o usuário

## 🎯 Objetivo

Este projeto está sendo desenvolvido como um projeto acadêmico e de aprendizado, com foco em **Python, programação orientada a objetos, manipulação de arquivos, interfaces gráficas e controle de versão com Git**.

---

⭐ Projeto em desenvolvimento — novas funcionalidades serão adicionadas conforme o desenvolvimento avançar.
