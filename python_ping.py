#!/usr/bin/python3

# python_ping.py
#
# Una sencilla herramienta para verificar algunos elementos
# de una red usando python y fping.
# ---------------------------------------------------------
# Este programa es software libre. Puede redistribuirlo y/o
# modificarlo bajo los términos de la Licencia Pública General
# de GNU según es publicada por la Free Software Foundation,
# bien de la versión 2 de dicha Licencia o bien (según su
# elección) de cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea
# útil, pero SIN NINGUNA GARANTÍA, incluso sin la garantía
# MERCANTIL implícita o sin garantizar la CONVENIENCIA PARA UN
# PROPÓSITO PARTICULAR. Para más detalles, véase la Licencia
# Pública General de GNU.
#
# Autor: LinuxmanR4
# https://linuxmanr4.com
#

import os
import csv
from colorama import Fore
import time
import datetime

# Configuración.
# ----------------------------
archivo_csv = 'servidores.csv'
tiempo_entre_pruebas = 600


# Funciones.
# ----------------------------


def check_ping(hostname):
    response = os.system("fping -r 5 -q " + hostname + " >/dev/null")
    if response == 0:
        return "[OK]"
    else:
        return "[Error]"


def revisar_red():
    for i in range(len(datos_servidores)):
        servidorTexto = datos_servidores[i][0]
        servidorIP = datos_servidores[i][1]
        resultado = check_ping(datos_servidores[i][1])

        if resultado == "[OK]":
            print("{0:30} {1:17} {2:7}".format(Fore.WHITE +
                                               servidorTexto, servidorIP,
                                               Fore.GREEN + resultado))
        else:
            print("{0:30} {1:17} {2:7}".format(Fore.WHITE +
                                               servidorTexto, servidorIP,
                                               Fore.RED + resultado))


archivo = open(archivo_csv)
servidores = csv.reader(archivo)
datos_servidores = list(servidores)
contador = 0

while True:
    revisar_red()
    contador += 1
    print(Fore.BLUE)
    print('{0} {1:%H:%M:%S} {2}'.format(contador, datetime.datetime.now(),
                                        "________________________________________"))
    print()
    time.sleep(tiempo_entre_pruebas)
