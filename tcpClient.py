import socket
import sys


HOST = '127.0.0.1'  # endereço IP
PORT = 20000        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados


def main(argv):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Servidor executando!")
            while(True):
                texto = input("Digite o texto a ser enviado ao servidor:\n")
                # texto.encode - converte a string para bytes
                s.send(texto.encode())
                # recv - recebe o texto em forma de bites
                data = s.recv(BUFFER_SIZE)
                # decode recebe o texto em bytes e converte para string no formato 'utf-8'
                texto_recebido = data.decode('utf-8')
                print('Recebido do servidor: \'{}\''.format(texto_recebido))
                # receber a opção do cliente
                txt = input(
                    '1 - Saber a quantidade de vogais;\n2 - Saber a quantidade de consoantes;\n3 - Saber a palavra invertida;\n4 - Todas as funções;\n5 - Finalizar programa;\n')
                s.send(txt.encode())
                # converte txt para um inteiro
                txt = int(txt)
                # método se para testar os números 1,2,3,4 e imprimir o que o cliente deseja
                if txt in (1, 2, 3, 4):
                    dataTxt = s.recv(BUFFER_SIZE)
                    txt_recebido = dataTxt.decode('utf-8')
                    print('Recebido do servidor:\n{}'.format(txt_recebido))
                # else utilizado para encerrar o programa
                else:
                    print('Vai encerrar o socket cliente!')
                    s.close()
                    break
    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return


if __name__ == "__main__":
    main(sys.argv[1:])
