'''RECETARIO'''
import os
from pathlib import Path
from shutil import rmtree

rootPath = Path(os.getcwd(), 'Recetas')

#Mostrar ruta actual y cantidad de recetas en ruta
def get_total_recipes(path):
    recipes = 0
    for txt in Path(path).glob('**/*.txt'):
        recipes += 1
    return recipes

#Obtener Categorias
def get_categories():
    subfolders = [f.name for f in os.scandir(rootPath) if f.is_dir()]
    return subfolders

#Dar opciones de categoria/file y retornar seleccionada
def select_option(list):
    counter = 1
    valid_option = False
    selected_option = ''

    for item in list:
        print(f'    {counter}. {item}')
        counter += 1

    while valid_option == False:
        selected_option = input('\n    Selecciona una de las opciones: ')
        if selected_option.isnumeric() and (int(selected_option) in range(1,counter)):
            valid_option = True
        else:
            print('Opcion invalida, por favor intenta de nuevo.\n')

    return list[int(selected_option)-1]


#Obtener Recetas
def get_recipes_in_folder(path):
    recipes = []
    for txt in Path(path).glob('*.txt'):
        recipes.append(Path(txt).name)
    return recipes

#Pedir nombre de archivo o categoria
def input_new_name():
    new_name = ''
    is_file = False
    while is_file == False:
        count = 0
        new_name = input('\n    Ingresa el nombre: ')

        for letra in new_name:
            if letra in '/\\:*?\"\'<>|':
                count += 1

        if count == 0:
            is_file = True
        else:
            print(f'\'{new_name}\' no es un nombre valido, revisa e intenta con uno diferente.')

    return new_name

#Validar existencia de categoria
def validate_category(category):
    categories = get_categories()
    if category in categories:
        return True
    else:
        return False

#Validar existencia de receta
def validate_recipes(path, recipe):
    recipes = get_recipes_in_folder(path)
    if recipe in recipes:
        return True
    else:
        return False

#Eliminar categoria
def delete_category(path):
    rmtree(path)

#Crear Categoria
def create_category(path):
    os.mkdir(path)

#Eliminar receta
def delete_recipe(path):
    os.remove(path)

#Mostrar receta
def show_recipe(path):
    doc = open(path)
    print(doc.read())
    doc.close()

#Crear receta
def write_recipe(path, content):
    doc = open(path, 'w')
    for line in content:
        doc.write(line)
    doc.close()

def ask_recipe_content():
    content = []
    print('Escribe o pega el texto de tu receta. Presiona Ctrl+Z (Windows) cuando termines.')
    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line+'\n')
    return content

#While limpiar pantalla y Bienvenida
option = ''
while option != '6':
    os.system('cls')
    print(f'''--#--------------- Bienvenido a tu recetario ---------------#--
    Los archivos de tus recetas estan ubicados en: {rootPath}
    Actualmente tienes {get_total_recipes(rootPath)} recetas de diferentes categorias.
    
    Acciones:
    1. Consultar una receta
    2. Crear una receta
    3. Crear una categoria
    4. Elminar una receta
    5. Eliminar una categoria
    6. Salir del programa''')

    option = input('\n    ¿Qué acción te gustaria hacer? (ingresa el número): ')

    match option:
        case "1":
            categories = get_categories()
            if len(categories) > 0:
                print("\n    ¿De que categoria es tu receta?")
                cetegory = select_option(get_categories())
                recipe_list = get_recipes_in_folder(Path(rootPath,cetegory))
                if len(recipe_list)>0:
                    print("\n    ¿Qué receta quieres ver?")
                    recipe = select_option(recipe_list)
                    print(f'\n----------------{recipe}----------------')
                    show_recipe(Path(rootPath,cetegory,recipe))
                else:
                    print('\n----No hay recetas que mostrar en esta categoria.')
            else:
                print('\n----No existen categorias, ni recetas que mostrar')
        case "2":
            categories = get_categories()
            if len(categories)>0:
                print("\n    ¿De que categoria es tu receta?")
                cetegory = select_option(categories)
                print("\n    ¿Que platillo prepararás?")
                recipe = input_new_name() + '.txt'
                if validate_recipes(Path(rootPath,cetegory), recipe) == False:
                    print(f'\n----------------{recipe}----------------')
                    content = ask_recipe_content()
                    write_recipe(Path(rootPath,cetegory,recipe), content)
                    print('\n    Receta guardada con éxito.')
                else:
                    print(f'\n    La receta de {recipe} ya existe en el sistema')
                    if input('\n    ¿Deseas sobreescribirla? S = si, N = No ---------> ').upper() == 'S':
                        print(f'\n----------------{recipe}----------------')
                        content = ask_recipe_content()
                        write_recipe(Path(rootPath, cetegory, recipe), content)
                        print('\n    Receta guardada con éxito.')
                    else:
                        print('\n    Confirmación no recibida, volviendo al menú principal')
            else:
                print('''----No existen categorias en donde se pueda guardar tu receta----
----Por favor crea una categoria y vuelve a intentar         ----''')
        case "3":
            print("\n    ¿Que categoria te gustaría agregar a la lista?")
            category = input_new_name()
            category = category.capitalize()
            if validate_category(category) == False:
                create_category(Path(rootPath,category))
                print('\n    Categoria creada con éxito.')
            else:
                print(f'\n    La categoria {category} ya existe en el sistema, consulta y verifica por favor')
                print('    Volviendo al menú principal...')
        case "4":
            categories = get_categories()
            if len(categories) > 0:
                print("\n    ¿De que categoria es la receta que deseas eliminar?")
                cetegory = select_option(categories)
                recipe_list = get_recipes_in_folder(Path(rootPath, cetegory))
                if len(recipe_list) > 0:
                    print("\n    ¿Qué receta quieres eliminar?")
                    recipe = select_option(recipe_list)
                    confirmation = input(f'\n    ADVERTENCIA!!! Estas a punto de eliminar {recipe} \n    ¿Estas seguro? S = Si, N = No -------> ')
                    if confirmation.upper() == 'S':
                        delete_recipe(Path(rootPath,cetegory,recipe))
                        print(f'\n    La receta {recipe} fue eliminada con éxito.')
                    else:
                        print('\n    Confirmación no recibida, volviendo al menú principal')
                else:
                    print('\n----No hay recetas que eliminar en esta categoria.')
            else:
                print('\n----No existen categorias en esta ruta')
        case "5":
            categories = get_categories()
            if len(categories) > 0:
                print("\n    ¿Que categoria te gustaria eliminar?")
                cetegory = select_option(categories)
                confirmation = input('\n    ADVERTENCIA!!! Al eliminar una categoria también eliminaras las recetas que esta contiene \n    ¿Estas seguro? S = Si, N = No -------> ')
                if confirmation.upper() == 'S':
                    delete_category(Path(rootPath, cetegory))
                    print('\n    Categoria eliminada con éxito.')
                else:
                    print('\n    Confirmación no recibida, volviendo al menú principal')
            else:
                print('\n----No existen categorias en esta ruta')
        case "6":
            print("\n    Saliendo del programa....")
        case _:
            print("Parece que ingresaste una opción invalida, intenta de nuevo.")
            print('    Volviendo al menú principal...')

    input('\n    Presiona enter para continuar.')