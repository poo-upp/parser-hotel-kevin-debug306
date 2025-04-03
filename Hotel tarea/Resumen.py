from ReservaHotel import Cliente, HabitacionDoble, Suite  
from datetime import datetime, timedelta  

def parser(documento):
    clientx, num_noches, fecha_inicio = None, 0, ""
    habitaciones = []
    habitaciones_disponibles = {"habitacion doble": HabitacionDoble, "suite": Suite}

    with open(documento, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip().lower()

            if "nombre del cliente" in line:
                clientx = Cliente(next(file).strip(), "-")

            elif "correo" in line and clientx:
                clientx.correo = line.split()[-1]

            elif "numero de noches" in line:
                num_noches = int(line.split()[-1])

            elif "fecha inicio" in line:
                fecha_inicio = line.split()[-1]

            elif line in habitaciones_disponibles:
                habitaciones.append(habitaciones_disponibles[line](len(habitaciones) + 1))

    return clientx, num_noches, fecha_inicio, habitaciones


def generar_resumen(cliente, noches, fecha, habitaciones):
    fecha_checkout = (datetime.strptime(fecha, "%d-%m-%Y") + timedelta(days=noches)).strftime("%d-%m-%Y")

    habitacion_contador = {"Habitacion doble": 0, "Suite": 0}
    for hab in habitaciones:
        nombre_hab = "Habitacion doble" if isinstance(hab, HabitacionDoble) else "Suite"
        habitacion_contador[nombre_hab] += 1

    precios = {"Habitacion doble": 900, "Suite": 2000}

    total_precio = sum(habitacion_contador[nombre] * precios[nombre] for nombre in precios) * noches

    with open("output.txt", "w", encoding="utf-8") as out:
        out.write(f"¡Hola {cliente.nom}! Aquí tienes los detalles de tu reserva:\n\n")
        out.write(f"Check-in:\t{fecha}\nCheck-out:\t{fecha_checkout}\n\n")
        out.write(f"Reservaste\t{noches} noches, {len(habitaciones)} habitaciones, {sum(h.capacidad for h in habitaciones)} personas\n\n")

        out.write("Detalles de reserva\n")
        for nombre, cantidad in habitacion_contador.items():
            if cantidad:
                out.write(f"[{cantidad}]\t{nombre}\n")

        out.write(f"\nE-mail de contacto\t[{cliente.correo}]\n\nDetalles del precio:\n")
        for nombre, cantidad in habitacion_contador.items():
            if cantidad:
                precio_total = cantidad * precios[nombre] * noches
                out.write(f"[{cantidad}]\t{nombre}\t\t {precio_total:.2f}$\n")

        out.write("----------------------------------------------\n")
        out.write(f"Total:\t\t\t\t\t{total_precio:.2f}$\n")



doc = "input.txt"
cliente, noches, fecha, habitaciones = parser(doc)

if cliente:
    generar_resumen(cliente, noches, fecha, habitaciones)
    print("Resumen generado en 'output.txt'.")
else:
    print("No se encontró información del cliente.")

