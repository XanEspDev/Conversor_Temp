"""Conversor de Temperatura"""

temperatura = float(input("Ingrese temperatura:"))
escala = input("Es Farenheit(F), Kelvin(K) o Celcius(C)?:").lower()
# escala_deseada = input("A que escala desea convertir (F, K, C)?:").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5 / 9
    kelvin = (temperatura - 32) * 5 / 9 + 273.15
    print("La temperatura en Celcius es ", celsius, " Y en Kelvin es: ", kelvin),
elif escala == "c":
    farenheit = temperatura * 9 / 5 + 32
    kelvin1 = temperatura + 273.15
    print("La temperatura en Farenheit es: ", farenheit, " Y en Kelvin es: ", kelvin1),
elif escala == "k":
    celsius1 = temperatura - 273.15
    farenheit1 = (temperatura - 273.15) * 9 / 5 + 32
    print(
        "La temperatura en Celsius es: ", celsius1, " Y en Farenheit es: ", farenheit1
    )
else:
    print("Escala incorrecta")
