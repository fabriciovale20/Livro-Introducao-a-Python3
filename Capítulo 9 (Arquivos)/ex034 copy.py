import time

agora = time.localtime()
hora_inicio = agora.tm_sec

for c in range(0, 100):
    agora = time.localtime()
    time.sleep(1)
    print(agora.tm_sec)