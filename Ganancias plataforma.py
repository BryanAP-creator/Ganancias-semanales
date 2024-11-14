# BryanAnguloPortuguez

ganancias_semanales = {
    "lunes": float(input("Ingrese las ganancias del lunes: ")),
    "martes": float(input("Ingrese las ganancias del martes: ")),
    "miércoles": float(input("Ingrese las ganancias del miércoles: ")),
    "jueves": float(input("Ingrese las ganancias del jueves: ")),
    "viernes": float(input("Ingrese las ganancias del viernes: ")),
    "sábado": float(input("Ingrese las ganancias del sábado: ")),
    "domingo": float(input("Ingrese las ganancias del domingo: "))
}

total_ganancias_semanales = sum(ganancias_semanales.values())

dia_maximo = max(ganancias_semanales, key=ganancias_semanales.get)
ganancia_maxima = ganancias_semanales[dia_maximo]

print("El total de ganancias semanales es:", total_ganancias_semanales)
print("El día con la ganancia más alta es:", dia_maximo, "con una ganancia de:", ganancia_maxima)