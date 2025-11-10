import json
from pathlib import Path
import menu, os

class Libro:
    def __init__(self, titulo, autor, isbn,disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}) - {estado}"

def afegir():
    print('------------Introducción de un nuevo libro------------------\n\n')
    titol = input('Introduce el título del libro:                   ')
    autor = input('Introduce el autor del libro:                    ')
    ISBN = input('Introduce el ISBN del libro:                   ')
    Disponible = input('¿Está disponible ya el libro? Si/No:                ').lower()

    if Disponible == 'si':
        Disponible = True
    else:
        Disponible = False

     
    nou_registre ={"Titulo" : titol, "Autor" : autor, "ISBN" : ISBN, "Disponible" : Disponible}      
        
    #print(nou_registre)
    ruta = Path(__file__).parent / 'catalogo.json'
    with ruta.open('r', encoding="utf-8") as f:
        diccionario = json.load(f)
    #print(f'Imprimiendo diccionario {diccionario}')
    diccionario.append(nou_registre)
        #print(diccionario)
    print('Libro añadido al catálogo:')
    with ruta.open('w', encoding="utf-8") as f:
         json.dump(diccionario, f, ensure_ascii=False, indent=2)

def buscar():
    trobat = False
    ruta = Path(__file__).parent / 'catalogo.json' 
    with ruta.open('r', encoding="utf-8") as f:
        diccionario = json.load(f) #bajo el contenido del json
    
    autor = input('Introduce el autor por el que desea buscar:           ')
    for dic in diccionario:
        if dic["Autor"] == autor:
            print(f'Esto es lo que se ha encontrado en la biblioteca:\n') if not trobat else None
            llibretrobat = Libro(dic["Titulo"], dic["Autor"], dic["ISBN"], dic["Disponible"])
            print(llibretrobat) # si los encuentra los imprime
            trobat = True
    if not trobat:
        print('No tenemos libros de este autor en la biblioteca') #Si no lo encuentra muestra este mensaje       
    input('Pulse cualquier tecla para continuar....')

def prestar():
    ruta = Path(__file__).parent / 'catalogo.json' 
    with ruta.open('r', encoding="utf-8") as f:
        diccionario = json.load(f) #bajo el contenido del json al diccionario
    titulo = input('Introduce el título del libro que desea prestar:           ')
    for dic in diccionario:
        if dic["Titulo"] == titulo:
            if dic["Disponible"]:
                libroaprestar = Libro(dic["Titulo"], dic["Autor"], dic["ISBN"], dic["Disponible"])
                libroaprestar.prestar()
                print(f'El libro "{titulo}" ha sido prestado correctamente.')
                dic["Disponible"] = libroaprestar.disponible
                with ruta.open('w', encoding="utf-8") as f:
                    json.dump(diccionario, f, ensure_ascii=False, indent=2)
            else:
                print(f'El libro "{titulo}" no está disponible para préstamo.')
            break

def devolver():
    ruta = Path(__file__).parent / 'catalogo.json' 
    with ruta.open('r', encoding="utf-8") as f:
        diccionario = json.load(f) #bajo el contenido del json al diccionario
    titulo = input('Introduce el título del libro que desea devolver:           ')
    for dic in diccionario:
        if dic["Titulo"] == titulo:
            if not dic["Disponible"]:
                libroadevolver = Libro(dic["Titulo"], dic["Autor"], dic["ISBN"], dic["Disponible"])
                libroadevolver.devolver()
                print(f'El libro "{titulo}" ha sido devuelto correctamente.')
                dic["Disponible"] = libroadevolver.disponible
                with ruta.open('w', encoding="utf-8") as f:
                    json.dump(diccionario, f, ensure_ascii=False, indent=2)
            else:
                print(f'El libro "{titulo}" está disponible para préstamo no para devolver.')
            break

def main():
    catalogo = []

    Libros = [
        Libro('Carrie', 'Stephen King', '0-7645-2641-1', True),
        Libro('El resplandor', 'Stephen King', '0-7645-2642-2', True),
        Libro('Rabia', 'Stephen King', '0-7645-2643-3', True),
        Libro('La danza de la muerte', 'Stephen King', '0-7645-2644-4', True),
        Libro('La larga marcha', 'Stephen King', '0-7645-2645-5', True),
        Libro('La zona muerta', 'Stephen King', '0-7645-2646-6', True),
        Libro('It', 'Stephen King', '0-7645-2647-7', True),
        Libro('Misery', 'Stephen King', '0-7645-2648-8', True),
        Libro('El misterio de Salem\'s Lot', 'Stephen King', '0-7645-2650-0', True),
        Libro('Christine', 'Stephen King', '0-7645-2651-1', True),
        Libro('El fugitivo', 'Stephen King', '0-7645-2652-2', True),
        Libro('Apocalipsis', 'Stephen King', '0-7645-2653-3', True),
        Libro('La torre oscura I: El pistolero', 'Stephen King', '0-7645-2654-4', True),
        Libro('La torre oscura II: La llegada de los tres', 'Stephen King', '0-7645-2655-5', True),
        Libro('La torre oscura III: Las tierras baldías', 'Stephen King', '0-7645-2656-6', True),
        Libro('La torre oscura IV: Mago y cristal', 'Stephen King', '0-7645-2657-7', True),
        Libro('La torre oscura V: Lobos del Calla', 'Stephen King', '0-7645-2658-8', True),
        Libro('La torre oscura VI: Canción de Susannah', 'Stephen King', '0-7645-2659-9', True),
        Libro('La torre oscura VII: La torre oscura', 'Stephen King', '0-7645-2660-0', True),
        Libro('Doctor Sueño', 'Stephen King', '0-7645-2661-1', True),
        Libro('11/22/63', 'Stephen King', '0-7645-2662-2', True),
        Libro('El Instituto', 'Stephen King', '0-7645-2663-3', True)
            ]
    
    for libro in Libros:
        mi_libro = {
            "Titulo": libro.titulo,
            "Autor": libro.autor,
            "ISBN": libro.isbn,
            "Disponible": libro.disponible
        }
        catalogo.append(mi_libro)
   
    os.system('cls' if os.name == 'nt' else 'clear')
    ruta= Path(__file__).parent / 'catalogo.json'
    if not ruta.exists():
        with ruta.open('w', encoding="utf-8") as f:
            json.dump(catalogo, f, ensure_ascii=False, indent=2)
    
    while True:
        menu.mostrarmenu()
        try:
            opcion = int(input('Elige una opción: '))
        except ValueError:
            print('Introduce una opción válida')
            continue

        match opcion:
            case 1:
                #afegir()
                pass
            case 2:
                #prestar()
                pass
            case 3:
                #devolver()
                pass
            case 4:
                #buscar()
                pass
            case 5:
                print('¡Gracias por usar el gestor de Biblioteca!')
                break
            case _:
                print('Opción no válida!')

        input('Pulse cualquier tecla para continuar....')
        os.system('cls' if os.name == 'nt' else 'clear')

# Llamada a la main
if __name__ == '__main__':
    main()
