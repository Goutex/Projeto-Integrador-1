import importar
import mysql.connector
from connector import host, user, password, database

conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()

def menu():

    while True:
        print("\n  --- Goutex Store ---\n")
        print("M. Mostrar jogos da Loja")
        print("J. Mostrar meus jogos")
        print("S. Sair")

        opcao = input("\nDigite a opção desejada: ").upper()

        if opcao == "S":
            importar.Acessando.acessando()

        elif opcao == "M":
            importar.menujogos.mostrarjogos.mostrar_jogos()

        elif opcao == "J":
            importar.jogosusuario.jogos_usuario()

        else:
            print("\nOpção inválida. Digite novamente.")

# menu()
