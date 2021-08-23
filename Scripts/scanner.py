#!/bin/python

#Scanner de portas com python

#Modo de usar: python3 scanner.py <ip alvo>
import sys
import socket
from datetime import datetime

#Definir o alvo

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Traduz o hostname para IPv4
else:
    print("Argumentos inválidos")

#Adicionando um Banner
print("-"*50)
print("Scaneando o alvo" + target)
print("Time started: "+str(datetime.now()))
print("-"*50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result =s.connect_ex((target, port))
        if result == 0:
            print(f"Porta {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nSaindo do programa")
    sys.exit()

except socket.gaierror:
    print("O hostname não pôde ser resolvido")
    sys.exit()

except socket.error:
    print("Sem conexão com o servidor")
    sys.exit()