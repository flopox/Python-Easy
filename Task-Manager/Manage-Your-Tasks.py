import os

# Clase para representar una tarea
class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = False

# Obtener la ubicación del script actual
script_directory = os.path.dirname(os.path.abspath(__file__))
archivo_tareas_path = os.path.join(script_directory, "lista_tareas.txt")

# Función para leer la lista de tareas del archivo
def leer_lista_tareas():
    lista_tareas = []
    archivo_tareas = None

    try:
        archivo_tareas = open(archivo_tareas_path, "r")
        for linea in archivo_tareas:
            nombre, descripcion = linea.strip().split(",")
            lista_tareas.append(Tarea(nombre, descripcion))
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        pass
    finally:
        if archivo_tareas:
            archivo_tareas.close()

    return lista_tareas

# Función para escribir la lista de tareas en el archivo
def escribir_lista_tareas(lista_tareas):
    archivo_tareas = open(archivo_tareas_path, "w")
    for tarea in lista_tareas:
        archivo_tareas.write(tarea.nombre + "," + tarea.descripcion + "\n")
    archivo_tareas.close()

# Función para mostrar la lista de tareas
def mostrar_lista_tareas(lista_tareas):
    print("Aqui las tareas que tienes:")
    for tarea in lista_tareas:
        if tarea.completada:
            estado = "Completada"
        else:
            estado = "Pendiente"
        print("* Nombre:", tarea.nombre, "Descripción:", tarea.descripcion, "Estado:", estado)
    print("___________________________________________")

# Función para agregar una nueva tarea
def agregar_tarea(lista_tareas):
    nombre = input("Ingrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    tarea = Tarea(nombre, descripcion)
    lista_tareas.append(tarea)
    escribir_lista_tareas(lista_tareas)

def eliminar_tarea(lista_tareas):
    nombre = input("Ingrese el nombre de la tarea que desea eliminar: ")
    for tarea in lista_tareas:
        if tarea.nombre == nombre:
            lista_tareas.remove(tarea)
            escribir_lista_tareas(lista_tareas)
            return
    print("No se encontró la tarea con el nombre especificado.")

def marcar_tarea_como_completada(lista_tareas):
    nombre = input("Ingrese el nombre de la tarea que desea marcar como completada: ")
    for tarea in lista_tareas:
        if tarea.nombre == nombre:
            tarea.completada = True
            escribir_lista_tareas(lista_tareas)
            return
    print("No se encontró la tarea con el nombre especificado.")

def main():
    lista_tareas = []
    lista_tareas = leer_lista_tareas()

    while True:
        print("___________________________________________")
        print("* Menú de opciones")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Marcar tarea como completada")
        print("4. Mostrar lista de tareas")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        print("___________________________________________")

        # Procesar la opción seleccionada.
        if opcion == "1":
            # Agregar una nueva tarea.
            agregar_tarea(lista_tareas)
        elif opcion == "2":
            # Eliminar una tarea.
            eliminar_tarea(lista_tareas)
        elif opcion == "3":
            # Marcar una tarea como completada.
            marcar_tarea_como_completada(lista_tareas)
        elif opcion == "4":
            # Mostrar la lista de tareas.
            mostrar_lista_tareas(lista_tareas)
        elif opcion == "5":
            # Salir del programa.
            break

if __name__ == "__main__":
    main()
