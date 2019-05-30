from Jarvis.comandos import *

def tradutor_de_comando(comando):
    executor = ""
    for aux in comando:
        try:
            arquivo = open('vocabulario/'+aux+'.txt', 'r')
            executor = executor + arquivo.readline()
            arquivo.close()

        except FileNotFoundError:
            arquivo = open('vocabulario/'+aux+'.txt', 'w+')
            significado = input("O que é " + aux + "?")
            arquivo.write(significado)
            arquivo.close()

            arquivo = open('vocabulario/' + aux + '.txt', 'r')
            executor = executor + arquivo.readline()
            arquivo.close()

    try:
        exec(executor)
    except SyntaxError:
        print("Comando Invalido")



if __name__ == "__main__":
    while True:
        #é nescesssario ativar o assistente
        if(input("...") == 'jarvis'):
            while True:
                comando = input("digite um comando")
                if(comando == 'sair'):
                    break
                else:
                    tradutor_de_comando(comando.split())
