from database import conectar, criar_tabelas
from datetime import datetime

criar_tabelas()


def cadastrar_animal():
    conn = conectar()
    cursor = conn.cursor()

    nome = input("Nome do animal: ")
    brinco = input("Número do brinco: ")
    raca = input("Raça: ")
    idade = int(input("Idade: "))

    try:
        cursor.execute("""
        INSERT INTO animais(nome, brinco, raca, idade)
        VALUES (?, ?, ?, ?)
        """, (nome, brinco, raca, idade))

        conn.commit()
        print("\nAnimal cadastrado com sucesso!")

    except Exception as erro:
        print("\nErro:", erro)

    conn.close()


def listar_animais():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, nome, brinco, raca, idade
    FROM animais
    """)

    animais = cursor.fetchall()

    print("\n===== ANIMAIS CADASTRADOS =====")

    if not animais:
        print("Nenhum animal cadastrado.")

    for animal in animais:
        print(
            f"ID: {animal[0]} | "
            f"Nome: {animal[1]} | "
            f"Brinco: {animal[2]} | "
            f"Raça: {animal[3]} | "
            f"Idade: {animal[4]}"
        )

    conn.close()


def registrar_pesagem():
    conn = conectar()
    cursor = conn.cursor()

    animal_id = int(input("ID do animal: "))
    peso = float(input("Peso (kg): "))

    data = datetime.now().strftime("%d/%m/%Y")

    cursor.execute("""
    INSERT INTO pesagens(animal_id, peso, data_pesagem)
    VALUES (?, ?, ?)
    """, (animal_id, peso, data))

    conn.commit()
    conn.close()

    print("\nPesagem registrada!")


def historico_pesagens():
    conn = conectar()
    cursor = conn.cursor()

    animal_id = int(input("ID do animal: "))

    cursor.execute("""
    SELECT peso, data_pesagem
    FROM pesagens
    WHERE animal_id = ?
    """, (animal_id,))

    dados = cursor.fetchall()

    print("\n===== HISTÓRICO =====")

    if not dados:
        print("Nenhuma pesagem encontrada.")

    for peso, data in dados:
        print(f"{data} - {peso} kg")

    conn.close()


def atualizar_animal():
    conn = conectar()
    cursor = conn.cursor()

    id_animal = int(input("ID do animal: "))
    novo_nome = input("Novo nome: ")

    cursor.execute("""
    UPDATE animais
    SET nome = ?
    WHERE id = ?
    """, (novo_nome, id_animal))

    conn.commit()
    conn.close()

    print("\nAnimal atualizado!")


def excluir_animal():
    conn = conectar()
    cursor = conn.cursor()

    id_animal = int(input("ID do animal: "))

    cursor.execute(
        "DELETE FROM animais WHERE id = ?",
        (id_animal,)
    )

    conn.commit()
    conn.close()

    print("\nAnimal removido!")


while True:

    print("""
=========================
 SISTEMA DE FAZENDA
=========================

1 - Cadastrar Animal
2 - Listar Animais
3 - Registrar Pesagem
4 - Histórico de Pesagens
5 - Atualizar Animal
6 - Excluir Animal
0 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_animal()

    elif opcao == "2":
        listar_animais()

    elif opcao == "3":
        registrar_pesagem()

    elif opcao == "4":
        historico_pesagens()

    elif opcao == "5":
        atualizar_animal()

    elif opcao == "6":
        excluir_animal()

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")