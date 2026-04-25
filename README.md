# 📚 Sistema de Cadastro de Lista de Espera Escolar

Projeto Final da disciplina de Estruturas de Dados — implementação de um sistema de gerenciamento de lista de espera para uma escola localizada em **Guarujá - SP**, utilizando três estruturas de dados distintas com perfis de acesso diferenciados.

---

## ▶️ Como executar

```bash
python main.py
```

> **Requisito:** Python 3.x instalado. Certifique-se de que o arquivo `cidades_vizinhas.csv` está na mesma pasta que `main.py`.

---

## 👥 Perfis de acesso

O sistema possui três perfis, utilizados em sequência:

### 🗂️ Secretário(a) — Lista Encadeada Simples
- Cadastrar nova pessoa na lista de espera
- Consultar pessoa cadastrada
- Verificar quantidade de pessoas na lista

### 🏫 Diretor(a) — Árvore Binária de Busca (BST)
- Editar informações de uma pessoa (nome, idade, telefone)
- Descadastrar pessoa da lista
- Exibir primeiro/último nome em ordem alfabética

### 🗺️ Assistente — Grafo + Algoritmo de Dijkstra
- Menor distância entre a escola e a cidade de uma pessoa
- Menor distância passando pela cidade intermediária (Indaiatuba)
- Cidade mais próxima da escola com moradores cadastrados

---

## 🏗️ Estruturas de dados implementadas

| Estrutura | Arquivo | Uso |
|---|---|---|
| Lista Encadeada Simples | `lista_encadeada.py` | Perfil Secretário(a) |
| Árvore Binária de Busca | `arvore_bst.py` | Perfil Diretor(a) |
| Grafo ponderado não-direcionado | `grafo.py` | Perfil Assistente |

---

## 📁 Estrutura dos arquivos

```
├── main.py                     # Ponto de entrada — interface principal
├── pessoa.py                   # Classe Pessoa (nome, idade, telefone, cidade)
├── lista_encadeada.py          # Lista Encadeada Simples
├── arvore_bst.py               # Árvore Binária de Busca (BST)
├── grafo.py                    # Grafo + Dijkstra
├── carrega_dados.py            # Leitura do CSV e construção do grafo
├── atribuicoes_secretario.py   # Interface do perfil Secretário(a)
├── atribuicoes_diretor.py      # Interface do perfil Diretor(a)
├── atribuicoes_assistente.py   # Interface do perfil Assistente
└── cidades_vizinhas.csv        # Base de dados: 433 cidades do estado de SP
```

---

## 🗺️ Dados geográficos

- **Cidade da escola:** Guarujá - SP
- **Cidade intermediária fixa:** Indaiatuba - SP
- **Base de cidades:** 433 cidades do estado de São Paulo com distâncias reais (km)
- **Formato do CSV:** `cidade1;cidade2;distancia`

---

## 📐 Arquitetura do projeto

O `main.py` **nunca se comunica diretamente** com as estruturas de dados. Toda comunicação passa pelos módulos `atribuicoes_*.py`, que funcionam como camada de interface entre a lógica de apresentação e as estruturas de dados.

```
main.py
  ├── atribuicoes_secretario.py → lista_encadeada.py
  ├── atribuicoes_diretor.py    → arvore_bst.py
  └── atribuicoes_assistente.py → grafo.py
```
