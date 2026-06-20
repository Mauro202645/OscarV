# -*- coding: utf-8 -*-
import random
import string
import os
import time

# Colores (si no funcionan en QPython, se pueden quitar)
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

NOMBRES_LATINOS = [
    "Jose", "Armando", "Mario", "Carlos", "Luis", "Juan", "Pedro", "Pablo",
    "Andres", "Felipe", "Santiago", "Mateo", "Sebastian", "Diego", "Martin",
    "Alejandro", "Javier", "Rafael", "Gabriel", "Emilio", "Ernesto", "Julian",
    "Antonio", "Manuel", "Ricardo", "Fernando", "Alberto", "Roberto", "Hector"
]

APELLIDOS_LATINOS = [
    "Torres", "Gonzales", "Perez", "Rodriguez", "Lopez", "Martinez", "Sanchez",
    "Ramirez", "Flores", "Morales", "Vargas", "Rojas", "Diaz", "Castro", "Ortega"
]

def mostrar_banner():
    # Eliminamos os.system('clear') porque puede fallar en QPython
    print(GREEN + """
    ╔═══════════════════════════════════════╗
    ║          👻  P H A N T O M  👻        ║
    ║     Generador de combos user:pass     ║
    ╚═══════════════════════════════════════╝
    """ + RESET)
    print(CYAN + "🔮 ¡Bienvenido, alma errante! 🔮\n" + RESET)

def barra_progreso(actual, total, longitud=40):
    porcentaje = actual / total
    bloque = int(round(longitud * porcentaje))
    barra = "█" * bloque + "░" * (longitud - bloque)
    print(f"\r{GREEN}Progreso: |{barra}| {actual}/{total} combos generados{RESET}", end="")
    if actual == total:
        print()

def opcion_1(cantidad):
    combos = []
    for _ in range(cantidad):
        nombre = random.choice(NOMBRES_LATINOS)
        apellido = random.choice(APELLIDOS_LATINOS)
        user = nombre + apellido
        combos.append(f"{user}:{user}")
    return combos

def opcion_2(cantidad):
    combos = []
    for _ in range(cantidad):
        nombre = random.choice(NOMBRES_LATINOS)
        user = nombre + "12345"
        combos.append(f"{user}:{user}")
    return combos

def opcion_3(cantidad):
    combos = []
    for _ in range(cantidad):
        numero = ''.join(random.choices(string.digits, k=8))
        combos.append(f"{numero}:{numero}")
    return combos

def opcion_4(cantidad):
    combos = []
    for _ in range(cantidad):
        nombre = random.choice(NOMBRES_LATINOS)
        anio = random.randint(1990, 2026)
        user = f"{nombre}{anio}"
        combos.append(f"{user}:{user}")
    return combos

def guardar_combos(combos, nombre_archivo):
    # Intentamos guardar en la carpeta de descargas o en la raíz
    # Probamos varias rutas
    rutas_posibles = [
        f"/storage/emulated/0/{nombre_archivo}.txt",
        f"/sdcard/{nombre_archivo}.txt",
        f"/mnt/sdcard/{nombre_archivo}.txt",
        f"./{nombre_archivo}.txt"  # directorio actual
    ]
    for ruta in rutas_posibles:
        try:
            with open(ruta, "w") as f:
                for combo in combos:
                    f.write(combo + "\n")
            return ruta
        except:
            continue
    return None

def main():
    try:
        mostrar_banner()

        print(YELLOW + "👻 Elige una opción fantasmagórica:" + RESET)
        print("1️⃣  - Nombres + Apellidos (Ej: JoseTorres:JoseTorres)")
        print("2️⃣  - Nombres + 12345 (Ej: Jose12345:Jose12345)")
        print("3️⃣  - Números aleatorios de 8 dígitos")
        print("4️⃣  - Nombres + Años (1990-2026)")

        opcion = int(input(BLUE + "\n➡️  Opción (1-4): " + RESET))
        if opcion not in [1, 2, 3, 4]:
            print(RED + "❌ Opción no válida. Fantasma enfadado 👻" + RESET)
            return

        cantidad = int(input(BLUE + "🔢 ¿Cuántos combos generar? " + RESET))
        if cantidad <= 0:
            print(RED + "❌ La cantidad debe ser mayor a 0." + RESET)
            return

        nombre_archivo = input(BLUE + "📄 Nombre del archivo .txt (sin extensión): " + RESET)
        if not nombre_archivo.strip():
            print(RED + "❌ Nombre inválido." + RESET)
            return

        print(CYAN + "\n🔄 Generando combos... ¡Ten paciencia, alma en pena! 👻\n" + RESET)

        combos = []
        if opcion == 1:
            combos = opcion_1(cantidad)
        elif opcion == 2:
            combos = opcion_2(cantidad)
        elif opcion == 3:
            combos = opcion_3(cantidad)
        elif opcion == 4:
            combos = opcion_4(cantidad)

        for i in range(cantidad):
            barra_progreso(i + 1, cantidad)
            time.sleep(0.001)

        print("\n")
        ruta = guardar_combos(combos, nombre_archivo)

        if ruta:
            print(GREEN + f"✅ ¡Éxito! Se generaron {cantidad} combos." + RESET)
            print(GREEN + f"📁 Archivo guardado en: {ruta}" + RESET)
            print(CYAN + "👻 ¡Phantom se despide, vuelve pronto!" + RESET)
        else:
            print(RED + "❌ Error al guardar el archivo. ¿Permisos de escritura?" + RESET)

    except ValueError:
        print(RED + "❌ Error: Ingresa solo números válidos. 👻" + RESET)
    except Exception as e:
        print(RED + f"❌ Error inesperado: {e}" + RESET)
        # Esperamos para que el usuario vea el error antes de salir
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()