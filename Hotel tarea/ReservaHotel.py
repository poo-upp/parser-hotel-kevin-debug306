#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Sistema de Reservaciones para un Hotel

from datetime import date


# Clase base Habitacion que representa cualquier tipo de habitación en el hotel
class Habitacion:
    def __init__(self, numero, capacidad, precio, disponible=True):
        # Inicializa los atributos básicos de la habitación
        self.numero = numero
        self.capacidad = capacidad
        self.precio = precio
        self._disponible = disponible  # atributo privado para manejar disponibilidad

    @property
    def disponible(self):
        # Devuelve el estado de disponibilidad de la habitación
        return self._disponible

    @disponible.setter
    def disponible(self, estado):
        # Permite modificar la disponibilidad de la habitación
        self._disponible = estado

    def __eq__(self, otra):
        # Compara dos habitaciones en función de su número, capacidad y precio
        return (self.numero == otra.numero and
                self.capacidad == otra.capacidad and
                self.precio == otra.precio)

    def __add__(self, otra):
        # Calcula el costo total al sumar el precio de dos habitaciones
        return self.precio + otra.precio


# Clase HabitacionSimple con características específicas
# Habitación simple: capacidad para 1 persona y precio fijo
class HabitacionSimple(Habitacion):
    def __init__(self, numero):
        super().__init__(numero, capacidad=1, precio=500)


# Clase HabitacionDoble con características específicas
# Habitación doble: capacidad para 2 personas y precio fijo
class HabitacionDoble(Habitacion):
    def __init__(self, numero, balcon=False):
        super().__init__(numero, capacidad=2, precio=900)
        self.balcon = balcon  # Nuevo atributo


# Clase Suite con opción adicional de jacuzzi
# Suite: capacidad para 4 personas y precio base más alto
class Suite(Habitacion):
    def __init__(self, numero, jacuzzi=False):
        super().__init__(numero, capacidad=4, precio=2000)
        self.jacuzzi = jacuzzi  # Nuevo atributo


# Clase Cliente que gestiona la información del cliente y sus reservas
class Cliente:
    def __init__(self, nombre, correo):
        self.nom = nombre
        self.correo = correo
        # Lista para almacenar todas las reservas del cliente
        self.reservas = []

    # Clase Reserva que crea una relación entre cliente, habitación y fechas


class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        # Se agrega la reserva al historial del cliente
        self.cliente.reservas.append(self)
        # La habitación se marca como no disponible
        self.habitacion.disponible = False  # cambia


def parser(documento):#quita espacios en blanco 
    flag=0
    with open(documento, 'r') as file:
        for line in file:
            line=line.strip() #quita espacios en blanco
            lin=line.split()
            ## line es la linea tal cual
            ## lin es la linea separada por palabras en una lista
            if len(lin) > 0:
                #print(lin)  #print para verificar que se estan leyendo las lineas
                if flag == 1:
                    name=line.strip("-")
                    clientx = Cliente(name, '-')
                    flag=0
                if "Nombre del cliente" in line: flag=1
                if "correo" in line:
                    print(lin)
                    mail=lin[1]
                    clientx.correo=mail
                    return  clientx

#      para el cliente con el total de su reserva.
doc=str("input.txt")
cliente=parser(doc)
print(cliente.nom)
print(cliente.correo)