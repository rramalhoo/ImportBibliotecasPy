import time

def relogio():
    while True:
        agora = time.strftime("%H:%M:%S") #formato = hora, mes, segundo
        print(f"Hora atual {agora}") #mostra na tela
        time.sleep(1) #atualiza em cada 1s

relogio()