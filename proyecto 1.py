import xml.etree.ElementTree as ET


# Clase Vuelo
class Vuelo:
    def __init__(self, codigo, origen, destino, duracion, aerolinea):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.duracion = duracion
        self.aerolinea = aerolinea



# Cargar archivo XML
def cargar_archivo_xml(ruta):
    vuelos = []
    codigos = set()

    try:
        tree = ET.parse(ruta)
        raiz = tree.getroot()

        for v in raiz.findall("vuelo"):
            codigo = v.find("codigo").text

            if codigo in codigos:
                print(f" Vuelo duplicado ignorado: {codigo}")
                continue

            codigos.add(codigo)

            vuelo = Vuelo(
                codigo,
                v.find("origen").text,
                v.find("destino").text,
                int(v.find("duracion").text),
                v.find("aerolinea").text
            )

            vuelos.append(vuelo)

        print("✔ Archivo cargado correctamente")

    except FileNotFoundError:
        print(" Error: Archivo no encontrado")
    except ET.ParseError:
        print(" Error: Formato XML inválido")

    return vuelos



# Detalle de vuelo específico
def detalle_vuelo(vuelos, codigo):
    for vuelo in vuelos:
        if vuelo.codigo == codigo:
            print("\nDetalle del vuelo")
            print(f"Código     : {vuelo.codigo}")
            print(f"Origen     : {vuelo.origen}")
            print(f"Destino    : {vuelo.destino}")
            print(f"Duración   : {vuelo.duracion}")
            print(f"Aerolínea  : {vuelo.aerolinea}")
            return

    print(" Vuelo no encontrado")



# Agrupar vuelos por aerolíneaD
def agrupar_por_aerolinea(vuelos):
    grupos = {}

    for vuelo in vuelos:
        if vuelo.aerolinea not in grupos:
            grupos[vuelo.aerolinea] = []
        grupos[vuelo.aerolinea].append(vuelo.codigo)

    for aerolinea, codigos in grupos.items():
        print(f"\nAerolínea: {aerolinea}")
        for codigo in codigos:
            print(codigo)



# Ordenar por duración
def ordenar_por_duracion(vuelos):
    ordenados = sorted(vuelos, key=lambda v: v.duracion, reverse=True)

    print("\nVuelos ordenados por duración (mayor a menor):")
    for vuelo in ordenados:
        print(vuelo.codigo)



# Menú principal
def menu():
    vuelos = []

    while True:
        print("\n----- MENÚ AEROLÍNEA -----")
        print("1. Cargar Archivo")
        print("2. Detalle de vuelo específico")
        print("3. Agrupar vuelos por aerolínea")
        print("4. Ordenar más duración a menor duración")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ruta = input("Ingrese la ruta del archivo XML: ")
            vuelos = cargar_archivo_xml(ruta)

        elif opcion == "2":
            if vuelos:
                codigo = input("Ingrese el código del vuelo: ")
                detalle_vuelo(vuelos, codigo)
            else:
                print(" Primero cargue el archivo")

        elif opcion == "3":
            if vuelos:
                agrupar_por_aerolinea(vuelos)
            else:
                print("primero cargue el archivo")

        elif opcion == "4":
            if vuelos:
                ordenar_por_duracion(vuelos)
            else:
                print("Primero cargue el archivo")

        elif opcion == "5":
            print(" Programa finalizado")
            break

        else:
            print(" Opción inválida")



# Punto de entrada
if __name__ == "__main__":
    menu()