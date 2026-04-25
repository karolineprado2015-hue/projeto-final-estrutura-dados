"""
main.py - Interface principal do Sistema de Cadastro de Lista de Espera Escolar.

Escola localizada em: Guarujá - SP
Cidade intermediária fixa (perfil assistente): Indaiatuba

Fluxo de uso:
    1. Secretário(a)  → usa Lista Encadeada Simples
    2. Diretor(a)     → usa Árvore Binária de Busca (gerada a partir da lista)
    3. Assistente     → usa Grafo + Dijkstra (lido do cidades_vizinhas.csv)
"""

from lista_encadeada import ListaEncadeada
from carrega_dados import carregar_grafo_e_cidades
import atribuicoes_secretario as sec
import atribuicoes_diretor as dire
import atribuicoes_assistente as ass

# Constantes do sistema
CIDADE_ESCOLA = "Guarujá"
CIDADE_INTERMEDIARIA = "Indaiatuba"
ARQUIVO_CSV = "cidades_vizinhas.csv"


# =============================================================================
# Utilitários de exibição
# =============================================================================

def linha(caractere="=", tamanho=60):
    print(caractere * tamanho)


def titulo(texto):
    linha()
    print(f"   {texto}")
    linha()


def opcao_invalida(minimo, maximo):
    print(f"\n  [ERRO] Opção inválida. Digite um número entre {minimo} e {maximo}.")


def ler_opcao():
    return input("\nDigite a opção: ").strip()


def ler_inteiro(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("  [ERRO] Por favor, informe um número inteiro válido.")


# =============================================================================
# Perfil: Secretário(a)
# =============================================================================

def menu_secretario(lista, cidades):
    titulo("BEM-VINDO(A), SECRETÁRIO(A)!")

    while True:
        print("\n--- MENU SECRETÁRIO(A) ---")
        print("1. Cadastrar nova pessoa na lista de espera")
        print("2. Consultar pessoa cadastrada")
        print("3. Verificar quantidade de pessoas na lista")
        print("4. Encerrar atendimento")

        opcao = ler_opcao()

        if opcao == "1":
            print("\n--- CADASTRAR NOVA PESSOA ---")
            nome = input("Nome: ").strip()
            idade = ler_inteiro("Idade: ")
            telefone = input("Telefone: ").strip()

            pessoa = sec.adicionar_pessoa(lista, nome, idade, telefone, cidades)
            print(f"\n  Pessoa cadastrada com sucesso!")
            print(f"  Cidade atribuída aleatoriamente: {pessoa.cidade}")

            print("\n--- LISTA DE ESPERA ATUAL ---")
            sec.exibir_lista(lista)

        elif opcao == "2":
            print("\n--- CONSULTAR PESSOA ---")
            nome = input("Nome da pessoa: ").strip()
            pessoa = sec.buscar_pessoa(lista, nome)
            if pessoa:
                print("\n  Pessoa encontrada:")
                print(pessoa)
            else:
                print(f"\n  [INFO] Pessoa '{nome}' não encontrada na lista de espera.")

        elif opcao == "3":
            qtd = sec.contar_pessoas(lista)
            print(f"\n  Total de pessoas na lista de espera: {qtd}")

        elif opcao == "4":
            print("\n  Secretário(a) finalizou as operações.")
            break

        else:
            opcao_invalida(1, 4)


# =============================================================================
# Perfil: Diretor(a)
# =============================================================================

def menu_diretor(arvore):
    titulo("BEM-VINDO(A), DIRETOR(A)!")

    while True:
        print("\n--- MENU DIRETOR(A) ---")
        print("1. Editar informações de uma pessoa")
        print("2. Descadastrar pessoa da lista de espera")
        print("3. Exibir pessoa com nome primeiro em ordem alfabética")
        print("4. Exibir pessoa com nome último em ordem alfabética")
        print("5. Encerrar atendimento")

        opcao = ler_opcao()

        # ---- Opção 1: Editar ----
        if opcao == "1":
            print("\n--- EDITAR PESSOA ---")
            nome = input("Nome da pessoa a editar: ").strip()
            pessoa = dire.buscar_pessoa(arvore, nome)

            if not pessoa:
                print(f"\n  [INFO] Pessoa '{nome}' não encontrada na lista de espera.")
                continue

            print("\n  Dados atuais:")
            print(pessoa)
            print("\n  O que deseja alterar?")
            print("  1. Nome")
            print("  2. Idade")
            print("  3. Telefone")

            while True:
                sub = input("\n  Opção: ").strip()

                if sub == "1":
                    novo_nome = input("  Novo nome: ").strip()
                    dire.editar_nome(arvore, nome, novo_nome)
                    print(f"\n  [OK] Nome alterado de '{nome}' para '{novo_nome}'.")
                    break

                elif sub == "2":
                    nova_idade = ler_inteiro("  Nova idade: ")
                    dire.editar_idade(arvore, nome, nova_idade)
                    print(f"\n  [OK] Idade alterada para {nova_idade}.")
                    break

                elif sub == "3":
                    novo_tel = input("  Novo telefone: ").strip()
                    dire.editar_telefone(arvore, nome, novo_tel)
                    print(f"\n  [OK] Telefone alterado para '{novo_tel}'.")
                    break

                else:
                    print("  [ERRO] Opção inválida. Digite 1, 2 ou 3.")

        # ---- Opção 2: Descadastrar ----
        elif opcao == "2":
            print("\n--- DESCADASTRAR PESSOA ---")
            nome = input("Nome da pessoa a descadastrar: ").strip()
            pessoa = dire.buscar_pessoa(arvore, nome)

            if not pessoa:
                print(f"\n  [INFO] Pessoa '{nome}' não encontrada na lista de espera.")
                continue

            print("\n  Dados da pessoa a ser descadastrada:")
            print(pessoa)

            while True:
                confirmacao = input("\n  Confirma o descadastramento? (S/N): ").strip().upper()
                if confirmacao == "S":
                    dire.descadastrar_pessoa(arvore, nome)
                    print(f"\n  [OK] Pessoa '{nome}' descadastrada com sucesso.")
                    break
                elif confirmacao == "N":
                    print("  [INFO] Operação cancelada.")
                    break
                else:
                    print("  [ERRO] Digite S para confirmar ou N para cancelar.")

        # ---- Opção 3: Primeiro alfabético ----
        elif opcao == "3":
            pessoa = dire.primeiro_alfabetico(arvore)
            if pessoa:
                print("\n  Primeira pessoa em ordem alfabética:")
                print(pessoa)
            else:
                print("\n  [INFO] A lista de espera está vazia.")

        # ---- Opção 4: Último alfabético ----
        elif opcao == "4":
            pessoa = dire.ultimo_alfabetico(arvore)
            if pessoa:
                print("\n  Última pessoa em ordem alfabética:")
                print(pessoa)
            else:
                print("\n  [INFO] A lista de espera está vazia.")

        # ---- Opção 5: Sair ----
        elif opcao == "5":
            print("\n  Diretor(a) finalizou as operações.")
            break

        else:
            opcao_invalida(1, 5)


# =============================================================================
# Perfil: Assistente
# =============================================================================

def menu_assistente(grafo, arvore):
    titulo("BEM-VINDO(A), ASSISTENTE!")

    while True:
        print("\n--- MENU ASSISTENTE ---")
        print("1. Menor distância: escola → cidade de uma pessoa")
        print(f"2. Menor distância passando por {CIDADE_INTERMEDIARIA}")
        print("3. Cidade mais próxima da escola com moradores cadastrados")
        print("4. Encerrar atendimento")

        opcao = ler_opcao()

        # ---- Opção 1: Menor distância direta ----
        if opcao == "1":
            print(f"\n--- MENOR DISTÂNCIA: {CIDADE_ESCOLA.upper()} → CIDADE DA PESSOA ---")
            nome = input("Nome da pessoa: ").strip()
            pessoa = ass.buscar_pessoa(arvore, nome)

            if not pessoa:
                print(f"\n  [INFO] Pessoa '{nome}' não encontrada na lista de espera.")
                continue

            print("\n  Dados da pessoa:")
            print(pessoa)

            caminho, distancia = ass.menor_distancia(grafo, CIDADE_ESCOLA, pessoa.cidade)

            if caminho:
                print(f"\n  Menor caminho:")
                print(f"  {' → '.join(caminho)}")
                print(f"  Distância total: {distancia} km")
            else:
                print(f"\n  [INFO] Não foi possível calcular o caminho até '{pessoa.cidade}'.")

        # ---- Opção 2: Caminho passando por Indaiatuba ----
        elif opcao == "2":
            print(f"\n--- MENOR DISTÂNCIA PASSANDO POR {CIDADE_INTERMEDIARIA.upper()} ---")
            nome = input("Nome da pessoa: ").strip()
            pessoa = ass.buscar_pessoa(arvore, nome)

            if not pessoa:
                print(f"\n  [INFO] Pessoa '{nome}' não encontrada na lista de espera.")
                continue

            print("\n  Dados da pessoa:")
            print(pessoa)

            caminho, distancia = ass.menor_distancia_com_intermediario(
                grafo, CIDADE_ESCOLA, CIDADE_INTERMEDIARIA, pessoa.cidade
            )

            if caminho:
                print(f"\n  Menor caminho passando por {CIDADE_INTERMEDIARIA}:")
                print(f"  {' → '.join(caminho)}")
                print(f"  Distância total: {distancia} km")
            else:
                print(f"\n  [INFO] Não foi possível calcular o caminho passando por '{CIDADE_INTERMEDIARIA}'.")

        # ---- Opção 3: Cidade mais próxima com moradores ----
        elif opcao == "3":
            print("\n--- CIDADE MAIS PRÓXIMA DA ESCOLA COM MORADORES CADASTRADOS ---")

            cidade, distancia, moradores = ass.cidade_mais_proxima_com_moradores(
                grafo, arvore, CIDADE_ESCOLA
            )

            if cidade:
                print(f"\n  Cidade mais próxima: {cidade}")
                print(f"  Distância até a escola: {distancia} km")
                print(f"\n  Moradores cadastrados em {cidade}:")
                for morador in moradores:
                    print(morador)
                    print()
            else:
                print("\n  [INFO] Não há pessoas cadastradas na lista de espera.")

        # ---- Opção 4: Sair ----
        elif opcao == "4":
            print("\n  Assistente finalizou as operações.")
            print("\n  Sistema encerrado. Até logo!")
            break

        else:
            opcao_invalida(1, 4)


# =============================================================================
# Ponto de entrada
# =============================================================================

def main():
    titulo("SISTEMA DE CADASTRO DE LISTA DE ESPERA ESCOLAR")
    print(f"  Escola localizada em: {CIDADE_ESCOLA} - SP\n")

    # Carrega o grafo e as cidades do CSV
    try:
        grafo, cidades = carregar_grafo_e_cidades(ARQUIVO_CSV)
        print(f"  [OK] Arquivo '{ARQUIVO_CSV}' carregado: {len(cidades)} cidades disponíveis.")
    except FileNotFoundError:
        print(f"\n  [ERRO] Arquivo '{ARQUIVO_CSV}' não encontrado.")
        print("  Certifique-se de que o arquivo está na mesma pasta do programa.")
        return

    # Inicializa a lista encadeada
    lista = ListaEncadeada()

    # ----- Fase 1: Secretário(a) -----
    menu_secretario(lista, cidades)

    if lista.contar() == 0:
        print("\n  [INFO] Nenhuma pessoa foi cadastrada pelo secretário. Encerrando sistema.")
        return

    # ----- Transição: gera a Árvore BST a partir da lista encadeada -----
    arvore = dire.gerar_arvore(lista)
    print(f"\n  [OK] Árvore binária de busca gerada com {lista.contar()} pessoa(s).")

    # ----- Fase 2: Diretor(a) -----
    menu_diretor(arvore)

    # ----- Fase 3: Assistente -----
    menu_assistente(grafo, arvore)


if __name__ == "__main__":
    main()
