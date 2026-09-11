# 💡 Sistema de Gestão de Ideias

Aplicação web desenvolvida em **Python** com **Streamlit** para
registrar, priorizar, consultar e acompanhar ideias de inovação e
melhoria.

O sistema utiliza **SQLite** para persistência dos dados e apresenta um
painel de gestão com indicadores e gráficos.

## 🚀 Funcionalidades

-   Cadastro de novas ideias
-   Registro de título, descrição, responsável e área solicitante
-   Avaliação por impacto, urgência e esforço
-   Cálculo automático de prioridade
-   Armazenamento em SQLite
-   Consulta e ordenação por prioridade
-   Pesquisa de ideias
-   Filtros por área e status
-   Visualização da descrição e justificativa
-   Edição de título e responsável
-   Alteração de status
-   Exclusão de ideias
-   Painel com indicadores gerais
-   Distribuição por área e status
-   Taxa de aceitação
-   Gráficos com Altair
-   Teste automatizado com pytest e SQLite em memória

## 🧮 Lógica de Prioridade

A prioridade considera **impacto**, **urgência** e **esforço**:

``` text
Prioridade = (Impacto × 2) + (Urgência × 2) - Esforço
```

Impacto e urgência aumentam a pontuação, enquanto um esforço maior reduz
a prioridade.

## 🛠️ Tecnologias Utilizadas

-   Python
-   Streamlit
-   SQLite3
-   Pandas
-   Altair
-   Pytest

## 📁 Estrutura do Projeto

``` text
projeto_ideias/
│
├── main.py
├── grafico_geral.py
├── banco.db
│
├── pages/
│   ├── app.py
│   └── ideias_cadastradas.py
│
└── test/
    └── test_prioridade.py
```

### Principais arquivos

**`main.py`** --- navegação entre as páginas do sistema.

**`pages/app.py`** --- registro de novas ideias e estrutura do banco de
dados.

**`pages/ideias_cadastradas.py`** --- gestão das ideias, com pesquisa,
filtros, detalhes, edição, status e exclusão.

**`grafico_geral.py`** --- painel com indicadores, taxa de aceitação e
gráficos.

**`banco.db`** --- banco de dados SQLite da aplicação.

**`test/test_prioridade.py`** --- teste automatizado utilizando SQLite
temporário em memória.

## ▶️ Como Executar

### 1. Instale as dependências

No terminal, dentro da pasta do projeto:

``` bash
pip install streamlit pandas altair pytest
```

O `sqlite3` já faz parte da biblioteca padrão do Python.

### 2. Inicie a aplicação

``` bash
streamlit run main.py
```

O Streamlit abrirá a aplicação no navegador.

## 🧪 Como Executar o Teste

``` bash
pytest
```

O teste utiliza um banco SQLite criado em memória e não altera os dados
do `banco.db`.

## 📊 Fluxo do Sistema

1.  O usuário registra uma nova ideia.
2.  A ideia recebe valores de impacto, urgência e esforço.
3.  O sistema calcula a prioridade.
4.  A ideia é armazenada no SQLite com status inicial **Recebida**.
5.  Na Gestão de Ideias, é possível pesquisar, filtrar, consultar
    detalhes, editar, alterar status e excluir registros.
6.  O Painel de Gestão consolida os dados em indicadores e gráficos.

## 📌 Status Utilizados

-   Recebida
-   Em análise
-   Aprovada
-   Reprovada

## 🎯 Objetivo

Organizar o processo de recebimento e acompanhamento de propostas de
inovação, permitindo que as ideias sejam registradas, avaliadas,
priorizadas e gerenciadas de forma simples e visual.
