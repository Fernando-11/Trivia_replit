BLACK = "\033[30m"
RESET = "\033[39m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RED = "\033[31m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"
print(
    GREEN +
    "Bienvenidos a mi trivia sobre una serie de preguntas de computación e informática."
    + RESET)
print("Pondremos a prueba tus conocimientos sobre el tema.")

nombre = input("Ingresa tu nombre:")
carrera = input("Ingresa tu carrera:")
ciclo = input("Ingresa tu ciclo:")
print(
    "\n Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativas que se encontrará y presionando'Enter'para enviar tu respuesta:\n"
)

jugadas = 1
while True:
    puntaje = random.randint(0, 10)

    print(YELLOW + "Comenzarás con:", puntaje, "puntos" + RESET)

    for numero_carga in range(5, 0, -1):
        print(numero_carga)
    import time
    time.sleep(1)

    print(GREEN + "1) ¿Quién es el dueño de Microsoft?" + RESET)
    print("a) Bill Gates")
    print("b) Mark Zuckerberg")
    print("c) Elon Musk")
    print("d) Albert Einstein")
    respuesta_1 = input("\nTu respuesta:")
    while respuesta_1 not in ("a", "b", "c", "d", "x"):
        respuesta_1 = input(
            "Debes responder a, b, c o d. \nIngresa nuevamente tu respuesta:")
    if respuesta_1 == "x":
        puntaje -= 2
        print("Este es un mensaje secreto")
    if respuesta_1 == "b":
        puntaje -= 2
        print("Incorrecto!", nombre, "No es el dueño")
        puntaje = puntaje / 2
    elif respuesta_1 == "c":
        puntaje -= 2
        print("Incorrecto!", nombre, "No es el dueño")
        puntaje = puntaje + 5
    elif respuesta_1 == "d":
        puntaje -= 2
        print("Incorrecto", nombre, "No es el dueño")
        puntaje = puntaje - 5
    else:
        puntaje += 10
        print("Muy bien", nombre, "!")
        puntaje = puntaje * 2
    import time

    time.sleep(2)

    print(RED + "2) ¿Qué es el hardware?" + RESET)
    print("a) Parte que no se puede describir")
    print(
        "b) Conjunto de elementos físicos o materiales que contituyen una computadora"
    )
    print("c) Son elementos materiales")
    print("d) Computador informático")
    respuesta_2 = input("\nTu respuesta:")
    while respuesta_2 not in ("a", "b", "c", "d", "x"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. \nIngresa nuevamente tu respuesta:")
        if respuesta_2 == "x":
            print("Este es un mensaje secreto")
    if respuesta_2 == "a":
        puntaje -= 2
        print("Incorrecto!", nombre, "si puede describir")
        puntaje = puntaje / 2
    elif respuesta_2 == "c":
        puntaje -= 2
        print("Incorrecto!", nombre, "no necesariamente se define así")
        puntaje = puntaje + 5
    elif respuesta_2 == "d":
        puntaje -= 2
        print("Incorrecto", nombre, "no necesariamente se define así")
    else:
        puntaje += 4
        print("Muy bien", nombre, "!")
        puntaje = puntaje * 2
    time.sleep(2)

    print(BLUE + "3) ¿Cuál de las siguientes alternativas no es un hardware?" +
          RESET)
    print("a) Impressa")
    print("b) Monitor")
    print("c) Mouse")
    print("d) Sistema operativo")
    respuesta_3 = input("\nTu respuesta:")
    while respuesta_3 not in ("a", "b", "c", "d", "x"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. \nIngresa nuevamente tu respuesta:")
        if respuesta_3 == "x":
            print("Este es un mensaje secreto")
    if respuesta_3 == "a":
        puntaje -= 2
        print("Incorrecto!", nombre, "si es un hardware")
        puntaje = puntaje / 2
    elif respuesta_3 == "b":
        puntaje -= 2
        print("Incorrecto!", nombre, "si es un hardware")
        puntaje = puntaje + 5
    elif respuesta_3 == "c":
        puntaje -= 2
        print("Incorrecto", nombre, "si es un hardware")
        puntaje = puntaje - 5
    else:
        puntaje += 8
        print("Muy bien", nombre, "!")
        puntaje = puntaje * 2
    time.sleep(2)

    print(YELLOW + "4) ¿Cuál es un sistema operativo?" + RESET)
    print("a) Windows 10")
    print("b) Monitor")
    print("c) Microsoft Word")
    print("d) Outlook")
    respuesta_4 = input("\nTu respuesta:")
    while respuesta_4 not in ("a", "b", "c", "d", "x"):
        respuesta_4 = input(
            "Debes responder a, b, c o d. \nIngresa nuevamente tu respuesta:")
    if respuesta_4 == "x":
        print("Este es un mensaje secreto")
    if respuesta_4 == "b":
        puntaje -= 2
        print("Incorrecto!", nombre, "no es un sistema operativo")
        puntaje = puntaje / 2
    elif respuesta_4 == "c":
        puntaje -= 2
        print("Incorrecto!", nombre, "no es un sistema operativo")
        puntaje = puntaje + 5
    elif respuesta_4 == "d":
        puntaje -= 2
        print("Incorrecto", nombre, "no es un sistema operativo")
        puntaje = puntaje - 5
    else:
        puntaje += 6
        print("Muy bien", nombre, "!")
        puntaje = puntaje * 2
    time.sleep(2)

    print(MAGENTA + "5) El antivirus protege al computador de:" + RESET)
    print("a) Fallas eléctricas")
    print("b) Fallas del registro principal")
    print("c) Virus-malware-spyware")
    respuesta_5 = input("\nTu respuesta:")
    while respuesta_5 not in ("a", "b", "c", "x"):
        respuesta_5 = input(
            "Debes responder a, b o c. \nIngresa nuevamente tu respuesta:")
        if respuesta_5 == "x":
            print("Este es un mensaje secreto")
    if respuesta_5 == "a":
        puntaje -= 2
        print("Incorrecto!", nombre, "el antivirus no lo protege")
        puntaje = puntaje / 2
    elif respuesta_5 == "b":
        puntaje -= 2
        print("Incorrecto!", nombre, "el antivirus no lo protege")
        puntaje = puntaje + 5
    else:
        puntaje += 16
        print("Muy bien", nombre, "!")
        puntaje = puntaje * 2
    time.sleep(2)

    print(RED + "6) TIC quiere decir:" + RESET)
    print("a) Técnico informático y comunicador")
    print("b) Tecnología e informática")
    print("c) Tecnología de la información y la comunicación")
    print("d) Tratado de Libre Comercio")
    respuesta_6 = input("\nTu respuesta:")
    while respuesta_6 not in ("a", "b", "c", "d", "x"):
        respuesta_6 = input(
            "Debes responder a, b, c o d. \nIngresa nuevamente tu respuesta:")
    if respuesta_6 == "x":
        print("Este es un mensaje secreto")
    if respuesta_6 == "a":
        puntaje -= 2
        print("Incorrecto!", nombre, "tiene otro significado")
        puntaje = puntaje / 2
    elif respuesta_6 == "b":
        puntaje -= 2
        print("Incorrecto!", nombre, "tiene otro significado")
        puntaje = puntaje + 5
    elif respuesta_6 == "d":
        puntaje -= 2
        print("Incorrecto", nombre, "tiene otro significado")
        puntaje = puntaje - 5
    else:
        puntaje += 18
        print("Muy bien", nombre, "!")
        puntaje = puntaje * 2
    time.sleep(2)

    print(BLUE + "7) ¿Cuántos bits tiene un Kilobyte?" + RESET)
    print("a) 1O24")
    print("b) 1O455464")
    print("c) O.OOO5")
    print("d) 564")
    respuesta_7 = input("\nTu respuesta:")
    while respuesta_7 not in ("a", "b", "c", "d", "x"):
        respuesta_7 = input(
            "Debes responder a, b, c o d. \nIngresa nuevamente tu respuesta:")
    if respuesta_7 == "x":
        print("Este es un mensaje secreto")
    if respuesta_7 == "b":
        puntaje -= 2
        print("Incorrecto!", nombre, "se tiene que hacer la conversión")
        puntaje = puntaje / 2
    elif respuesta_7 == "c":
        puntaje -= 2
        print("Incorrecto!", nombre, "se tiene que hacer la conversión")
        puntaje = puntaje + 5
    elif respuesta_7 == "d":
        puntaje -= 2
        print("Incorrecto", nombre, "se tiene que hacer la conversión")
        puntaje = puntaje - 5
    else:
        puntaje += 20
        print("Muy bien", nombre, "!")
        puntaje = puntaje * 2
    time.sleep(2)

    print(MAGENTA + "8) No es un dispositivo de salida:" + RESET)
    print("a) Teclado")
    print("b) Monitor")
    print("c) Parlantes")
    respuesta_8 = input("\nTu respuesta:")
    while respuesta_8 not in ("a", "b", "c", "d", "x"):
        respuesta_8 = input(
            "Debes responder a, b, o c. \nIngresa nuevamente tu respuesta:")
    if respuesta_8 == "x":
        print("Este es un mensaje secreto")
    if respuesta_8 == "c":
        puntaje -= 2
        print("Incorrecto!", nombre, "si es un dispositivo de salida")
        puntaje = puntaje / 2
    elif respuesta_8 == "b":
        puntaje -= 2
        print("Incorrecto!", nombre, "si es un dispositivo de salida")
        puntaje = puntaje + 5
    else:
        puntaje += 22
        print("Muy bien", nombre, "!")
        puntaje = puntaje * 2
    time.sleep(2)

    print(RED + "9) La memoria RAM es:" + RESET)
    print("a) Es permanente")
    print("b) Es volátil")
    print("c) Puede ser permanente o volátil")
    print("d) Tiene una parte permanente")
    respuesta_9 = input("\nTu respuesta:")
    while respuesta_9 not in ("a", "b", "c", "d", "x"):
        respuesta_9 = input(
            "Debes responder a, b, c o d. \nIngresa nuevamente tu respuesta:")
    if respuesta_9 == "x":
        print("Este es un mensaje secreto")
    if respuesta_2 == "a":
        puntaje -= 2
        print("Incorrecto!", nombre, "no lo es")
        puntaje = puntaje / 2
    elif respuesta_2 == "c":
        puntaje -= 2
        print("Incorrecto!", nombre, "no")
        puntaje = puntaje + 5
    elif respuesta_2 == "d":
        puntaje -= 2
        print("Incorrecto", nombre, "no lo es")
        puntaje = puntaje - 5
    else:
        puntaje += 24
        print("Muy bien", nombre, "!")
        puntaje = puntaje * 2
        time.sleep(2)

    print(
        BLUE +
        "1O) Una aplicación que aporta una solución informática para automatizar la tarea de contabilidad se considera como:"
        + RESET)
    print("a) Software de aplicación")
    print("b) Software de sistema")
    print("c) Software de compilación")
    print("d) Software de programación")
    respuesta_1O = input("\nTu respuesta:")
    while respuesta_1O not in ("a", "b", "c", "d", "x"):
        respuesta_1O = input(
            "Debes responder a, b, c o d. \nIngresa nuevamente tu respuesta:")
    if respuesta_1O == "x":
        print("Este es un mensaje secreto")
    if respuesta_1O == "b":
        puntaje -= 2
        print("Incorrecto!", nombre, "aporta mediante diferente manera")
        puntaje = puntaje / 2
    elif respuesta_1O == "c":
        puntaje -= 2
        print("Incorrecto!", nombre, "aporta mediante diferente manera")
        puntaje = puntaje + 5
    elif respuesta_1O == "d":
        puntaje -= 2
        print("Incorrecto", nombre, "aporta mediante diferente manera")
        puntaje = puntaje - 5
    else:
        puntaje += 26
        print("Muy bien", nombre, "!")
        puntaje = puntaje * 2

    numero_random = random.randint(0, 10)
    puntaje = puntaje + numero_random

    print(RED + "Gracias", nombre, "por jugar mi trivia,alcanzaste", puntaje,
          "puntos" + RESET)

    repeat = input("¿Quiere volver a jugar? Y/N: ")

    if repeat == "N":
        break
    else:
        jugadas += 1

print(RED + "Gracias", nombre, "por jugar mi trivia,jugaste un total de",
      jugadas, "veces" + RESET)