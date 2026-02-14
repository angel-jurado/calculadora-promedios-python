# calculadora de promedios escolares

def pedir_texto_no_vacio(msg):
    # para que no meta texto vacio
    while True:
        texto = input(msg).strip()
        if texto:
            return texto
        print("Error: el nombre no puede estar vacio.")


def pedir_nota(msg, minimo=0.0, maximo=10.0):
    while True:
        entrada = input(msg).strip().replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Error: introduce un numero.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"Error: tiene que estar entre {minimo} y {maximo}.")


def pedir_si_no(msg):
    while True:
        resp = input(msg).strip().lower()
        if resp in ("s", "si", "sí"):
            return True
        if resp in ("n", "no"):
            return False
        print("Responde con 's' o 'n'.")


def ingresar_calificaciones():
    materias = []
    notas = []

    print("\n--- Entrada de materias y calificaciones ---")

    while True:
        materia = pedir_texto_no_vacio("Nombre de la materia: ")
        nota = pedir_nota("Calificacion (0 a 10): ")

        materias.append(materia)
        notas.append(nota)

        if not pedir_si_no("Otra materia? (s/n): "):
            break

    return materias, notas


def calcular_promedio(notas):
    if len(notas) == 0:
        return None
    return sum(notas) / len(notas)


def determinar_estado(notas, umbral=5.0):
    aprobadas = []
    reprobadas = []
    for i in range(len(notas)):
        if notas[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    return aprobadas, reprobadas


def encontrar_mejor_y_peor(notas):
    if len(notas) == 0:
        return None, None
    pos_max = 0
    pos_min = 0
    for i in range(1, len(notas)):
        if notas[i] > notas[pos_max]:
            pos_max = i
        if notas[i] < notas[pos_min]:
            pos_min = i
    return pos_max, pos_min


def mostrar_resumen(materias, notas, umbral=5.0):
    print("\n--- Resumen ---")

    if len(materias) == 0:
        print("No se ingresaron materias.")
        return

    print("\nMaterias y calificaciones:")
    for i in range(len(materias)):
        print(f"  {materias[i]}: {notas[i]}")

    promedio = calcular_promedio(notas)
    print(f"\nPromedio general: {round(promedio, 2)}")

    aprobadas, reprobadas = determinar_estado(notas, umbral)

    print("\nAprobadas:")
    if len(aprobadas) > 0:
        for i in aprobadas:
            print(f"  {materias[i]} ({notas[i]})")
    else:
        print("  Ninguna")

    print("\nReprobadas:")
    if len(reprobadas) > 0:
        for i in reprobadas:
            print(f"  {materias[i]} ({notas[i]})")
    else:
        print("  Ninguna")

    mejor, peor = encontrar_mejor_y_peor(notas)
    print(f"\nMejor nota: {materias[mejor]} ({notas[mejor]})")
    print(f"Peor nota: {materias[peor]} ({notas[peor]})")


def main():
    print("Bienvenido a la calculadora de promedios")
    materias, notas = ingresar_calificaciones()
    mostrar_resumen(materias, notas)
    print("\nGracias por usar el programa.")


if __name__ == "__main__":
    main()

