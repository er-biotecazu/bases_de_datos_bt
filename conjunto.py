#Importamos el módulo que nos va a permitir trabajar sobre la base de datos.
import mysql.connector 
from mysql.connector import errorcode
#Importamos el resto de módulos que vayamos a necesitar.
import re
    #from os import system

#Creamos la conexión con la base de datos y la almacenamos en la variable "Base". Hacemos manejo de excepciones con la sentencia "try... except"
def Conexion():
    Base=mysql.connector.connect(host="localhost",
                                port=3306,
                                user="disnet_user",
                                passwd="disnet_pwd",
                                database="disnet_drugslayer")

    return Base

Base=Conexion()
Cursor=Base.cursor()

#Definimos una función que sirve para comprobar el menú que está metiendo el usuario. Analiza:
 # a) Que la cadena introducida no sea texto (manejado con el "try... except ValueError"). 
 # Esto se basa en el hecho de que la función "int" lanza una excepción con cadenas de texto que no pueden convertirse en enteros. 
 # b) Que el número introducido esté en el menú (números dentro del rango correspondiente).
def Seleccion(Opcion_mayor, Opcion_menor):
    #Iniciamos un bucle "while" del que no permitiremos salir hasta que se haya introducido una cadena correcta.
    Continuar=True
    while Continuar:
        Ir_a=input("Por favor, introduzca por teclado el menú al que quiera acceder: ")
        try:
            Ir_a=int(Ir_a)
            #Una vez sabemos que la cadena es numérica, comprobamos que el número introducido esté entre las opciones posibles.
            #Lógicamente, no puede estar por debajo de la opción (número) más pequeña, ni por encima de la más grande.
            if Ir_a>Opcion_mayor or Ir_a<Opcion_menor:
                print("No hay ningún menú que tenga asociado ese número. Por favor, revísalo.\n")
            else:
                #Si la cadena cumple todas las condiciones, salimos del bucle.
                Continuar=False
        #Este error sólo salta cuando el usuario mete texto (no se puede aplicar "int" a cadenas no numéricos).
        except ValueError:
            if Ir_a == "X" or Ir_a == "x":
                Continuar=False
            else:
                print("Necesitas meter un número para avanzar. Inténtalo de nuevo.\n")  
    #system("cls") ##PUEDE SER DE UTILIDAD, PERO LO COMENTO POR SI ACASO.
    #Devolvemos "Ir_a" (el menú seleccionado por el usuario) para alimentar otras funciones.
    return Ir_a

#Definimos los menús con funciones, pues tendremos que imprimirlos en varias ocasiones.
 #Estas funciones cuentan con cuatro partes:
 # 1) Texto del menú: Indica al usuario las distintas opciones dentro del menú y su número asociado.
 # 2) Características del menú: Simplemente, el número mayor y menor que tiene dicho menú.
 # 3) Petición al usuario: Usando la función "Seleccion()", se pide al usuario que seleccione un menú; esto se guarda en "Ir_a".
 # 4) Devolución del menú seleccionado: Sirve para alimentar otras funciones.

def Menu_principal():
    print("                     \033[1mMENÚ PRINCIPAL\033[0m     ")
    print("    [1]    Información general de la base de datos")
    print("    [2]    Información de los fármacos")
    print("    [3]    Información de las enfermedades")
    print("    [4]    Información de los efectos fenotípicos")
    print("    [5]    Información de los \033[3mtargets\033[0m")
    print("    [6]    Borrado de entradas")
    print("    [7]    Inserción de entradas")
    print("    [8]    Modificación de entradas")
    print("    [X]    Cerrar el programa\n")
    Opcion_menor=1
    Opcion_mayor=8
    Ir_a=Seleccion(Opcion_mayor, Opcion_menor)
    return Ir_a

def Menu_1():
    print("\n     \033[1m[1]    Información general de la base de datos\033[0m")
    print("           [0]    Volver al menú principal")
    print("           [1]    Número total de fármacos")
    print("           [2]    Número total de enfermedades")
    print("           [3]    Número total de efectos fenotípicos")
    print("           [4]    Número total de \033[3mtargets\033[0m")
    print("           [5]    Primeros 10 fármacos")
    print("           [6]    Primeras 10 enfermedades")
    print("           [7]    Primeros 10 efectos fenotípicos")
    print("           [8]    Primeros 10 \033[3mtargets\033[0m")
    print("           [X]    Cerrar el programa\n")
    Opcion_menor=0
    Opcion_mayor=8
    Ir_a=Seleccion(Opcion_mayor, Opcion_menor)
    return Ir_a

def Menu_2():
    print("\n     \033[1m[2]    Información de los fármacos\033[0m")
    print("           [0]    Volver al menú principal")
    print("           [1]    Información sobre un fármaco")
    print("           [2]    Sinónimos de un fármaco")
    print("           [3]    Código ATC de un fármaco")
    print("           [4]    Enfermedades tratadas por un fármaco")
    print("           [5]    Código ChEMBL de un fármaco")
    print("           [X]    Cerrar el programa\n")
    Opcion_menor=0
    Opcion_mayor=5
    Ir_a=Seleccion(Opcion_mayor, Opcion_menor)
    return Ir_a
    
def Menu_3():
    print("\n     \033[1m[3]    Información de las enfermedades\033[0m")
    print("           [0]    Volver al menú principal")
    print("           [1]    Fármacos para una enfermedad")
    print("           [2]    Fármaco y enfermedad con el mayor \033[3mscore\033[0m de asociación")
    print("           [3]    Enfermedades relacionadas con un término clave")
    print("           [X]    Cerrar el programa\n")
    Opcion_menor=0
    Opcion_mayor=3
    Ir_a=Seleccion(Opcion_mayor, Opcion_menor)
    return Ir_a

def Menu_4():
    print("\n     \033[1m[4]    Información de los efectos fenotípicos\033[0m")
    print("           [0]    Volver al menú principal")
    print("           [1]    Indicaciones de un fármaco")
    print("           [2]    Efectos secundarios de un fármaco")
    print("           [3]    Fármacos que causan un efecto secundario concreto")
    print("           [X]    Cerrar el programa\n")
    Opcion_menor=0
    Opcion_mayor=3
    Ir_a=Seleccion(Opcion_mayor, Opcion_menor)
    return Ir_a

def Menu_5():
    print("\n     \033[1m[5]    Información de los \033[3mtargets\033[0m\033[0m")
    print("           [0]    Volver al menú principal")
    print("           [1]    Dianas de un tipo")
    print("           [2]    Organismo al que se asocian un mayor número de dianas")
    print("           [3]    Dianas asociadas a un organismo")
    print("           [4]    Obtener los tipos de dianas")
    print("           [X]    Cerrar el programa\n")
    Opcion_menor=0
    Opcion_mayor=4
    Ir_a=Seleccion(Opcion_mayor, Opcion_menor)
    return Ir_a

def Menu_6():
    print("\n     \033[1m[6]    Borrado de entradas\033[0m")
    print("           [0]    Volver al menú principal")
    print("           [1]    Borrar una asociación fármaco-enfermedad de bajo \033[3mscore\033[0m")
    print("           [X]    Cerrar el programa\n")
    Opcion_menor=0
    Opcion_mayor=1
    Ir_a=Seleccion(Opcion_mayor, Opcion_menor)
    return Ir_a

def Menu_7():
    print("\n     \033[1m[7]    Inserción de entradas\033[0m")
    print("           [0]    Volver al menú principal")
    print("           [1]    Introducir una nueva codificación para un fármaco")
    print("           [X]    Cerrar el programa\n")
    Opcion_menor=0
    Opcion_mayor=1
    Ir_a=Seleccion(Opcion_mayor, Opcion_menor)
    return Ir_a

def Menu_8():
    print("\n     \033[1m[8]    Modificación de entradas\033[0m")
    print("           [0]    Volver al menú principal")
    print("           [1]    Cambiar a 0 los \033[3mscores\033[0m bajos")
    print("           [X]    Cerrar el programa\n")
    Opcion_menor=0
    Opcion_mayor=1
    Ir_a=Seleccion(Opcion_mayor, Opcion_menor)
    return Ir_a

#A continuación, definimos los comandos DML que se requieren en los distintos apartados de los submenús por medio de funciones. 

# Apartado 1: Información general de la base de datos 
## Subapartado 1.1: Número total de fármacos diferentes 

#Para los subapartados 1.1 - 1.4, empleamos la función "count()" con la clave primaria de las respectivas tablas, para asegurarnos que no haya campos vacíos. 
def Obtener_total_farmacos (): 
    Numero_farmacos = 'SELECT COUNT(drug_id) FROM drug'
    Cursor.execute(Numero_farmacos)
    Datos = Cursor.fetchone()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"         | Número de fármacos registrados: {Datos[0]} fármacos |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    return 

## Subapartado 1.2: Número total de enfermedades diferentes 
def Obtener_total_enfermedades ():
    Numero_enfermedades = 'SELECT COUNT(disease_id)s FROM disease'
    Cursor.execute(Numero_enfermedades)
    Datos = Cursor.fetchone()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"      | Número de enfermedades registradas: {Datos[0]} enfermedades |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    return 

## Subapartado 1.3: Número total de fenotipos diferentes
def Obtener_total_fenotipos ():
    Numero_fenotipos = 'SELECT COUNT(phenotype_id) FROM phenotype_effect'
    Cursor.execute(Numero_fenotipos)
    Datos = Cursor.fetchone()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"   | Número de efectos fenotípicos registrados: {Datos[0]} efectos fenotípicos |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    return 

## Subapartado 1.4: Número total de dianas diferentes 
def Obtener_total_dianas (): 
    Numero_dianas = 'SELECT COUNT(target_id) FROM target'
    Cursor.execute(Numero_dianas)
    Datos = Cursor.fetchone()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"           | Número de dianas registradas: {Datos[0]} dianas |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    return 

## Subapartado 1.5: Mostrar las primeras diez instancias de fármacos
def Primeros_resultados_farmacos ():
    Instancias_farmacos = """ 
        SELECT drug_id, 
	           drug_name, 
               molecular_type, 
               chemical_structure,
               inchi_key 
        FROM drug
        WHERE drug_id IS NOT NULL AND drug_name IS NOT NULL AND molecular_type IS NOT NULL AND chemical_structure IS NOT NULL AND inchi_key IS NOT NULL
        LIMIT 10;
        """
    Cursor.execute(Instancias_farmacos)
    Datos = Cursor.fetchall()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Encabezado="N.º\tIdentificador\tNombre\t\tTipo molecular\tEstructura química\tClave InChy\n"
    print(Encabezado)
    Numero_inicial=1
    for Fila in Datos:
        print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}\t{Fila[2]}\t{Fila[3]}\t{Fila[4]}")
        Numero_inicial+=1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    Obtener_archivo_texto(5, Encabezado, Datos, "Consulta_1.5.txt")
    return 

## Subapartado 1.6: Mostrar las primeras diez instancias de enfermedades
def Primeros_resultados_enfermedades ():
    Instancias_enfermedades = """
        SELECT disease_id, 
	           disease_name
        FROM disease
        WHERE disease_id IS NOT NULL AND disease_name IS NOT NULL
        LIMIT 10; 
    """
    Cursor.execute(Instancias_enfermedades)
    Datos = Cursor.fetchall()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Encabezado="N.º\tIdentificador\tNombre\n"
    Numero_inicial=1
    for Fila in Datos:
        print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
        Numero_inicial+=1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_1.6.txt")
    return 

## Subapartado 1.7: Mostrar las primeras diez instancias de fenotipos
def Primeros_resultados_fenotipos():
    Instancias_fenotipos = """
        SELECT * FROM phenotype_effect 
        WHERE phenotype_id IS NOT NULL AND phenotype_name IS NOT NULL
        LIMIT 10; 
        """
    Cursor.execute(Instancias_fenotipos)
    Datos = Cursor.fetchall()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Encabezado="N.º\tIdentificador\tNombre\n"
    Numero_inicial=1
    for Fila in Datos:
        print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
        Numero_inicial+=1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_1.7.txt")
    return 

## Subapartado 1.8: Mostrar las primeras diez instancias de dianas 
def Primeros_resultados_dianas():
    Instancias_dianas = """
        SELECT t.target_id, 
               t.target_name_pref, 
               t.target_type, 
               o.taxonomy_name 
        FROM target AS t, organism AS o
        WHERE t.organism_id=o.taxonomy_id AND t.target_id IS NOT NULL AND t.target_name_pref IS NOT NULL AND t.target_type IS NOT NULL AND o.taxonomy_name IS NOT NULL
        LIMIT 10;
        """
    Cursor.execute(Instancias_dianas)
    Datos = Cursor.fetchall()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Encabezado="N.º\tIdentificador\tNombre\t\t\tTipo\t\t\tOrganismo\n"
    print(Encabezado)
    Numero_inicial=1
    for Fila in Datos:
        print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}\t{Fila[2]}\t{Fila[3]}")
        Numero_inicial+=1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    Obtener_archivo_texto(4, Encabezado, Datos, "Consulta_1.8.txt")
    return 

def Buscar_farmaco():
    Continuar=True
    while Continuar:
        Farmaco=input("Por favor, introduzca el identificador ChEMBL de su fármaco de interés (ejemplo: CHEMBL1000): ")
        Farmaco=Farmaco.upper()
        if re.search(r"^(CHEMBL)[0123456789]{1,}$", Farmaco):
            Continuar=False
        else:
            print("Lo sentimos, la cadena introducida no es un identificador válido. Inténtelo de nuevo.\n")
    
    return Farmaco

def Comprobar_farmaco_nombre():
    Farmaco=input("\nPor favor, introduzca el nombre de su fármaco de interés (ejemplo: ASPIRIN): ")
    Consulta_SQL = "SELECT drug_name FROM drug WHERE drug_name = %s"
    Cursor.execute(Consulta_SQL, (Farmaco,))
    Datos=Cursor.fetchall()
    if len(Datos) != 0:
        Consulta2_SQL = "SELECT drug_id FROM drug WHERE drug_name = %s"
        Cursor.execute(Consulta2_SQL, (Farmaco,))
        Datos = Cursor.fetchone()
        Farmaco = Datos[0]
    elif len(Farmaco) >= 3: 
        Consulta3_SQL = "SELECT drug_name FROM drug WHERE drug_name LIKE %s"
        Farmaco = f"%{Farmaco}%"
        Cursor.execute(Consulta3_SQL, (Farmaco,))
        Datos=Cursor.fetchall()
        if len(Datos) != 0:
            print("\nLo sentimos, no hemos encontrado el fármaco que busca. ¿Quizás se refería a alguno de los siguientes?: \n")
            Numero_inicial = 1
            for Fila in Datos:
                print(f"{Numero_inicial}: {Fila[0]}")
                Numero_inicial+=1
            Respuesta_usuario=input(f"\n¿Se encuentra su fármaco de interés en la lista? [sí|no]: ")
            if re.search("[Ss][IiÍí]", Respuesta_usuario): 
                Respuesta2_usario=input("\nPor favor, seleccione el número de su fármaco de interés: ")
                Farmaco=Datos[int(Respuesta2_usario)-1][0]
                print(f"Su elección ha sido: {Farmaco}.")
                Consulta2_SQL = "SELECT drug_id FROM drug WHERE drug_name = %s"
                Cursor.execute(Consulta2_SQL, (Farmaco,))
                Datos = Cursor.fetchone()
                Farmaco = Datos[0]
        else:
            print(f"Lo sentimos, este fármaco no está dentro de la base. Vuelva a intentarlo de nuevo.")
    else:
            print(f"Lo sentimos, este fármaco no está dentro de la base. Vuelva a intentarlo de nuevo.")
    return Farmaco

def Comprobar_codigo_farmaco(ID_Farmaco): 
    Codigo_farmaco=input("\nPor favor, introduzca el código identificador del fármaco: ")
    Consulta_SQL = "SELECT code_id FROM drug_has_code WHERE drug_id = %s AND code_id = %s"
    Cursor.execute(Consulta_SQL, (ID_Farmaco, Codigo_farmaco,))
    Datos=Cursor.fetchall()
    if len(Datos) == 0:
        print(f"\nEl código introducido está libre para su uso.")
    else: 
        Codigo_farmaco="fail"
        print(f"\nLo sentimos, el código introducido ya está asociado a este fármaco.")
    return Codigo_farmaco

#Esta función se define para que el usuario tenga la opción de generar un archivo de texto con los resultados de la consulta. Viene definido por una serie de argumentos: 
    #Numero_campos se refiere al conjunto de elementos de cada tupla resultante de la consulta que se presentan en la salida. 
    #Encabezado contiene el encabezado de los distintos atributos para una determinada consulta. 
    #Datos contiene el resultado de las tuplas de la consulta tal y como se almacenan en una variable con fetchall o fetchone. 
    #Consulta contiene la consulta introducida por el usuario (input)
    #Nombre_archivo será el nombre que le demos al archivo de texto. 
def Obtener_archivo_texto(Numero_campos, Encabezado, Datos, Nombre_archivo): 
    Respuesta_usuario=input("¿Quiere generar un archivo de texto con los resultados de la consulta que se guardará en su directorio de trabajo? [sí|no]: ")
    if re.search("[Ss][IiÍí]", Respuesta_usuario):
        Archivo_salida=open(Nombre_archivo, "w")
        #Archivo_salida.write(f"El usuario introdujo como dato a su consulta '{Consulta}'.")
        Tuplas_consulta=[]
        Tuplas_consulta.append(Encabezado)
        Numero_orden = 1
        for Fila in Datos:
            Texto_salida = ""
            for Numero in range(0,(Numero_campos)): 
                if Numero == (Numero_campos-1):
                     Texto_salida = Texto_salida + str(Numero_orden) + "\t" + Fila[Numero]  + "\n"
                else: 
                    Texto_salida = Texto_salida + str(Numero_orden) + "\t" + Fila[Numero] 
            Tuplas_consulta.append(Texto_salida)
            Numero_orden+=1
        Archivo_salida.writelines(Tuplas_consulta)
        Archivo_salida.close()
    return 

# Apartado 2: Información de los fármacos
## Subapartado 2.1: Información sobre un fármaco
def Coger_informacion_farmaco_especifico(Farmaco): 
    Consulta_SQL = """SELECT drug_name, molecular_type, chemical_structure, inchi_key FROM drug
                WHERE drug_id = %s"""
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    try:
        Cursor.execute(Consulta_SQL, (Farmaco,))
        Datos=Cursor.fetchone()
        if len(Datos) != 0:
            print("Nombre\tTipo molecular\tEstructura química\tClave InChi\n")
            print(f"{Datos[0]}\t{Datos[1]}\t{Datos[2]}\t{Datos[3]}")
        else:
            print("Este fármaco no está incluido en la base de datos.")
    except TypeError:
        print("Este fármaco no está incluido en la base de datos.")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    return 


## Subapartado 2.2: Sinónimos de un fármaco 
def Coger_sinonimos_farmaco_especifico():
    Respuesta_usuario=input("\nPor favor, indique el nombre del fármaco del cual quiere obtener sus sinónimos (ejemplo: ASPIRIN): ")
    Consulta_SQL = """
            SELECT synonymous_name FROM synonymous 
            WHERE d.drug_id IN (SELECT drug_id FROM drug WHERE drug_name = %s); """
    #Obsérvese que para la subconsulta utilizamos un IN en lugar de un = porque en algunos casos, para un mismo nombre de fármaco, devuelve distintos drug_id (y daría un error)
    try:
        Cursor.execute(Consulta_SQL, (Respuesta_usuario, ))
        Datos=Cursor.fetchall()
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if len(Datos) != 0:
            print(f"Los sinónimos encontrados para el fármaco {Respuesta_usuario.capitalize()} son: ")
            for Fila in Datos: 
                print(Fila[0])
        else: 
            print("No hay sinónimos para el fármaco proporcionado.")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    except TypeError: 
        print("· Este fármaco no está incluido en la base de datos.")
    return 

## Subapartado 2.3: Código ATC de un fármaco
def Coger_codigos_ATC_farmaco_especifico(Farmaco):
    Consulta_SQL = """
            SELECT ATC_code_id FROM atc_code 
            WHERE drug_id = %s
        """
    try: 
        Cursor.execute(Consulta_SQL, (Farmaco,))
        Datos=Cursor.fetchall()
        #Los resultados se presentarán de forma diferente en función de si existe o no código ATC para el fármaco en cuestión y, en caso que exista, si hay más de uno. 
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if len(Datos) != 0: 
            if len(Datos) == 1:
                print(f"Identificador ATC del fármaco seleccionado: {Datos[0][0]}")
            else: 
                print("Identificadores ATC del fármaco seleccionado: ")
                Numero_inicial = 1
                for Fila in Datos: 
                    print(f"{Numero_inicial}: {Fila[0][0]}")
                    Numero_inicial+=1
        else: 
            print("   No se ha encontrado ningún identificador ATC para el fármaco solicitado.   ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    except TypeError:
        print("· Este fármaco no está incluido en la base de datos.")
    return 

## Subapartado 2.4: Enfermedades que puede tratar un fármaco determinado
def Farmaco_trata_enfermedades():
    Farmaco=input("Introduce el nombre de tu fármaco de interés (por ejemplo, ASPIRIN): ")
    Sentencia="""SELECT d.disease_id, d.disease_name FROM disease AS d, disease_has_code AS dhc, drug_disease AS dd
                WHERE dd.drug_id IN (SELECT drug_ID FROM drug WHERE drug_name=%s) AND dhc.code_id = dd.code_id AND d.disease_id = dhc.disease_id;"""
    #Sentencia="SELECT * FROM disease WHERE disease_id IN (SELECT disease_id FROM disease_has_code WHERE code_id IN (SELECT code_id FROM drug_disease WHERE drug_id IN (SELECT drug_id FROM drug WHERE drug_name = %s)))"
    try:
        Cursor.execute(Sentencia, (Farmaco,))
        Enfermedades_tratables=Cursor.fetchall()
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if len(Enfermedades_tratables)!=0:
            print("N.º\tIdentificador\tNombre\n")
            Numero_inicial=1
            for Enfermedad in Enfermedades_tratables:
                print(f"{Numero_inicial}\t{Enfermedad[0]}\t{Enfermedad[1]}")
                Numero_inicial+=1
        else:
            print("Esta enfermedad no cuenta con fármacos contra ella introducidos en la base de datos.")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    except TypeError:
        print("· Esta enfermedad no cuenta con fármacos contra ella introducidos en la base de datos.")

## Subapartado 2.5: Obtener identificadores del fármaco 
def Obtener_identificadores_farmaco():
    Farmaco=input("Introduce el nombre de tu fármaco de interés (por ejemplo, ASPIRIN): ")
    Sentencia="SELECT drug_name, drug_id FROM drug WHERE drug_name = %s"
    try:
        Cursor.execute(Sentencia, (Farmaco,))
        Codigo_CHEMBL=Cursor.fetchall()
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if len(Codigo_CHEMBL)!=0:
            print(f"\t\t\t{Codigo_CHEMBL[0][0]}:  {Codigo_CHEMBL[0][1]}")
        elif len(Farmaco) >= 3:
            Sentencia_laxa = "SELECT drug_name, drug_id FROM drug WHERE drug_name LIKE %s"
            Farmaco = f"%{Farmaco}%"
            Cursor.execute(Sentencia_laxa, (Farmaco,))
            Codigo_CHEMBL=Cursor.fetchall()
            if len(Codigo_CHEMBL)!=0:
                print("\nNo hemos encontrado el fármaco que busca. ¿Quizás se refería a alguno de los siguientes?:\n")
                Numero_inicial=1
                for Fila in Codigo_CHEMBL:
                    print(f"{Numero_inicial}\t{Fila[0]}: {Fila[1]}")
                    Numero_inicial+=1
            else:
                print("\n    |    Esta enfermedad no cuenta con fármacos contra ella introducidos en la base de datos.    |    ")
        else:
            print("\n    |    Esta enfermedad no cuenta con fármacos contra ella introducidos en la base de datos.    |    ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    except TypeError:
        print("· Esta enfermedad no cuenta con fármacos contra ella introducidos en la base de datos.")

# Apartado 3. Información de las enfermedades 
## Subapartado 3.1: Fármacos para una enfermedad: 
def Coger_farmacos_para_enfermedad(): 
    Respuesta_usuario = input("\nPor favor, indique el nombre de la enfermedad de la que quiere consultar los fármacos involucrados en su tratamiento: ")
    Consulta_SQL = """
        SELECT d.drug_id, d.drug_name FROM drug_disease as dd, drug as d
        WHERE dd.code_id IN (SELECT code_id FROM disease_code WHERE name = %s) AND dd.drug_id = d.drug_id;
        """
    try:
        Cursor.execute(Consulta_SQL, (Respuesta_usuario,))
        Datos=Cursor.fetchall()
        print("\n##############################################################################################")
        if len(Datos) != 0:
            print("N.º\tIdentificador\tNombre\n")
            Numero_inicial=1
            for Fila in Datos:
                print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
                Numero_inicial+=1
        else:
            print("Esta enfermedad no está incluida en la base de datos.")
        print("##############################################################################################\n")
    except TypeError:
        print("· Esta enfermedad no está incluida en la base de datos.")
    return 

## Subapartado 3.2: Enfermedad y fármaco con el mayor "score" de asociación.
def Mayor_asociacion():
    Sentencia="""SELECT d.drug_name, dc.name, dd.inferred_score FROM drug_disease AS dd, drug AS d, disease_code AS dc
                 WHERE d.drug_id = (SELECT drug_id FROM drug_disease
					                ORDER BY inferred_score DESC
					                LIMIT 1) 
                 AND dc.code_id = (SELECT code_id FROM drug_disease
				                    ORDER BY inferred_score DESC
				                    LIMIT 1)
                 AND dd.code_id = dc.code_id AND dd.drug_id = d.drug_id;
        """
    Cursor.execute(Sentencia)
    Resultado=Cursor.fetchone()   
    print("\n##############################################################################################################")
    print(f"La mayor asociación la presentan la enfermedad '{Resultado[1]}' y el fármaco '{Resultado[0]}' (la puntuación es de {Resultado[2]}).")
    print("##############################################################################################################\n")

## Subapartado 3.3: Buscar enfermedades asociadas a un término clave.
def Buscar_termino_clave():
    Termino_clave=input("Por favor, introduce una palabra o término clave y te devolveremos enfermedades en cuyo nombre se incluya (ejemplo: NEURO): ")
    Termino_clave=f"%{Termino_clave}%"
    Sentencia="SELECT code_id, name FROM disease_code WHERE name LIKE %s"
    Cursor.execute(Sentencia, (Termino_clave,))
    Enfermedades=Cursor.fetchall()
    print("\n##############################################################################################################")
    if len(Enfermedades)!=0:
        for Enfermedad in Enfermedades:
            print(f"  -  {Enfermedad[1]} ({Enfermedad[0]})")
    else:
        print("Lo sentimos, no se ha encontrado ninguna enfermedad que incluya ese término.")
    print("##############################################################################################################\n")

#Apartado 4. 
##Subapartado 4.1: Indicaciones de un fármaco
def Coger_indicaciones_fenotipo(Farmaco): 
    Consulta_SQL = """
    SELECT pe.phenotype_id, pe.phenotype_name FROM drug_phenotype_effect AS dpe, phenotype_effect AS pe
    WHERE dpe.drug_id = %s AND dpe.phenotype_type="INDICATION" AND pe.phenotype_id = dpe.phenotype_id;
    """
    try:
        Cursor.execute(Consulta_SQL, (Farmaco,))
        Datos=Cursor.fetchall()
        if len(Datos) != 0: 
            print("N.º\tID del fenotipo\tIndicado para\n")
            Numero_inicial=1
            for Fila in Datos: 
                print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
                Numero_inicial+=1
        else: 
            print("\nNo hay efectos secundarios registrados para este fármaco.")
    except TypeError:
        print("· Este fármaco no está incluido en la base de datos.")
    return 

##Subapartado 4.2: Efectos secundarios de un fármaco
def Coger_efectos_secundarios_fenotipo(Farmaco): 
    Consulta_SQL = """
    SELECT pe.phenotype_id, pe.phenotype_name FROM drug_phenotype_effect AS dpe, phenotype_effect AS pe
    WHERE dpe.drug_id = %s AND dpe.phenotype_type="SIDE EFFECT" AND pe.phenotype_id = dpe.phenotype_id
    ORDER BY score DESC;
    """
    try:
        Cursor.execute(Consulta_SQL, (Farmaco,))
        Datos=Cursor.fetchall()
        if len(Datos) != 0: 
            print("\nID del fenotipo\t\tEfecto secundario\n")
            Numero_inicial=1
            for Fila in Datos: 
                print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
                Numero_inicial+=1
        else: 
            print("\nNo hay efectos secundarios registrados para este fármaco.")
    except TypeError:
        print("· No hay efectos secundarios registrados para este fármaco.")
    return 

## Subapartado 4.3: Fármacos que provocan un efecto secundario determinado
def Farmacos_provocan_efecto_secundario():
    Efecto=input("Por favor, indique el efecto secundario que le interesa: ")
    Sentencia="SELECT drug_id, drug_name FROM drug WHERE drug_id IN (SELECT drug_id FROM drug_phenotype_effect WHERE phenotype_id=(SELECT phenotype_id FROM phenotype_effect WHERE phenotype_name = %s))"
    Cursor.execute(Sentencia, (Efecto,))
    Farmacos=Cursor.fetchall()
    print("\n♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
    if len(Farmacos)!=0:
        print("N.º\tIdentificador\tFármaco")
        Numero_inicial=1
        for Farmaco in Farmacos:
            print(f"{Numero_inicial}\t{Farmaco[0]}\t{Farmaco[1]}")
            Numero_inicial+=1
    else:
        print("Este efecto fenotípico no está incluido en la base de datos.")
    print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n")

# Apartado 5. 
## Subapartado 5.1: Dianas de un tipo
def Coger_primeras_dianas(): 
    Respuesta_usuario=input("\nPor favor, introduzca el tipo de diana de la que quiere obtener sus 20 primeras instancias: ")
    Consulta_SQL = """
    SELECT target_id, target_name_pref FROM target 
    WHERE target_type = %s
    ORDER BY target_name_pref ASC
    LIMIT 20;
    """
    Cursor.execute(Consulta_SQL, (Respuesta_usuario,))
    Datos=Cursor.fetchall()
    if len(Datos) != 0: 
        print("\n*******************************************************************************************")
        print("\nN.º\tIdentificador\tDiana\n")
        Numero_inicial=1
        for Fila in Datos: 
            print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
            Numero_inicial+=1
        print("*******************************************************************************************\n")
    else: 
        print("\nNo se ha encontrado ningún fármaco para la diana proporcionada.")
    return 

## Subapartado 5.2: Organismo al que se asocian un mayor número de dianas
def Coger_organismo_mas_dianas(): 
    Consulta_SQL = """
    SELECT o.taxonomy_name, taxonomy_id, count(organism_id) FROM target, organism AS o
    WHERE o.taxonomy_id = organism_id
    GROUP BY organism_id
    ORDER BY count(organism_id) DESC
    LIMIT 1;
    """
    Cursor.execute(Consulta_SQL)
    Datos=Cursor.fetchone()
    print("\n*******************************************************************************************")
    print(f"El organismo con más dianas es: {Datos[0]} (identificador: {Datos[1]}), con un total de {Datos[2]} dianas.")
    Respuesta_usuario=input("\n¿Quiere consultar el total de las dianas para el organismo seleccionado? [sí|no]: ")
    if re.search("[Ss][IiÍí]", Respuesta_usuario):    
        Sentencia2="SELECT target_id, target_name_pref FROM target WHERE organism_id = %s"
        Cursor.execute(Sentencia2, (Datos[1],))
        Dianas=Cursor.fetchall()
        Numero_inicial=1
        for Diana in Dianas:
            print(f"  ·  {Numero_inicial}: {Diana[1]} ({Diana[0]})")
            Numero_inicial+=1
    print("****************************************************************************\n")
    return 

## Subapartado 5.3: Dianas que hay asociadas a un organismo en concreto
def Dianas_organismo_concreto():
    Organismo=input("Por favor, indique el nombre de su organismo de interés (por ejemplo: Homo sapiens): ")
    Sentencia="""SELECT target_id, target_name_pref 
                 FROM target 
                 WHERE organism_id=(SELECT taxonomy_id FROM organism WHERE taxonomy_name = %s)"""
    Cursor.execute(Sentencia, (Organismo,))
    Dianas=Cursor.fetchall()
    print("\n*******************************************************************************************")
    if len(Dianas)!=0:
        print("N.º\tIdentificador\tDiana")
        Numero_inicial=1
        for Diana in Dianas:
            print(f"{Numero_inicial}\t{Diana[0]}\t{Diana[1]}")
            Numero_inicial+=1
    else:
        print("Este organismo no tiene dianas incluidas en la base de datos.")
    print("****************************************************************************\n")

## Subapartado 5.4: Tipos de dianas que hay en la base de datos
def Obtener_tipos_diana():
    Consulta_SQL="SELECT target_type FROM target GROUP BY target_type;"
    Cursor.execute(Consulta_SQL)
    Datos=Cursor.fetchall()
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    for Fila in Datos:
        print(Fila[0])
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    return 

#Apartado 6: Borrado
def Borrado():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Por medio de esta funcionalidad, se le van a mostrar las diez asociaciones entre fármaco y enfermedad con un score inferido más bajo.")
    print("Usted dispone de la oportunidad de borrar alguna de esas asociaciones.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sql_query = """ 
    SELECT dd.inferred_score, d.drug_name, dc.name FROM drug_disease AS dd, drug AS d, disease_code AS dc
    WHERE d.drug_id = dd.drug_id AND dc.code_id = dd.code_id AND inferred_score IS NOT NULL
    ORDER BY inferred_score ASC
    LIMIT 10;
    """
    Cursor.execute(sql_query)
    Datos=Cursor.fetchall()
    print("\nN.º\tScore inferido\tNombre del fármaco\tNombre de la enfermedad")
    Numero_inicial=1
    for Fila in Datos: 
        print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}\t{Fila[2]}")
        Numero_inicial+=1
    Respuesta_usuario=input("\n¿Desea borrar alguna asociación de entre las mostradas? [sí|no]: ")
    if re.search("[Ss][IiÍí]", Respuesta_usuario):
        Respuesta_usuario2 = input("Indique el número de la asociación que quiere borrar: ")
        Seleccion_usuario = Datos[int(Respuesta_usuario2)-1]
        print("Esta ha sido su selección:")
        print(f"{Seleccion_usuario[0]}\t{Seleccion_usuario[1]}\t{Seleccion_usuario[2]}")
        Respuesta_usuario3 = input("\n¿Está seguro de que quiere borrar esta relación? [sí|no]: ")
        #Nótese que para buscar el fármaco que tiene el valor de inferred_score seleccionado para su borrado, utilizamos la función 'LIKE'. Esto se debe a que los valores de esta columna 
        #son de tipo 'float'. El sistema, internamente, representa los valores con mayor precisión añadiendo un número mayor de decimales que los que se devuelven en la consulta, por lo 
        #que no se puede utilizar un igual en este caso. 
        if  re.search("[Ss][IiÍí]", Respuesta_usuario3):
            Borrado_SQL = """DELETE FROM drug_disease 
                        WHERE inferred_score LIKE %s AND drug_id = (SELECT drug_id FROM drug WHERE drug_name = %s) AND code_id = (SELECT code_id FROM disease_code WHERE name = %s)
                        """
            try: 
                Cursor.execute(Borrado_SQL, (Seleccion_usuario[0], Seleccion_usuario[1], Seleccion_usuario[2],))
                print("\nEl borrado se ha realizado con éxito.")
            except mysql.connector.Error:
                print("\nLo sentimos, no ha podido ejecutarse este borrado.")
    return 

#Apartado 7: Inserciones 
def Inserciones():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Por medio de esta funcionalidad, usted puede ampliar las codificaciones de un fármaco ya existente en la base de datos.")
    print("Usted debe introducir el nombre del fármaco, el nuevo código y el vocabulario del que proviene.")
    print("El código introducido no puede estar ya asociado a ese fármaco.") 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ID_farmaco=Comprobar_farmaco_nombre()
    if re.search(r"^(CHEMBL)[0123456789]{1,}$", ID_farmaco):
        Codigo_farmaco=Comprobar_codigo_farmaco(ID_farmaco)
        if Codigo_farmaco != "fail":
            Vocabulario_farmaco=input("Por favor, introduzca el nombre del vocabulario para el que pertenece el código: ")
            Insercion_SQL="INSERT INTO drug_has_code(drug_id, code_id, vocabulary) VALUES (%s, %s, %s)" 
            try: 
                Cursor.execute(Insercion_SQL, (ID_farmaco, Codigo_farmaco, Vocabulario_farmaco,))
                print("\nLa inserción se ha realizaco con éxito.")
            except mysql.connector.Error:
                print("\nLo sentimos, no ha podido ejecutarse esta inserción")
    return

#Apartado 8. Modificaciones 
def Modificaciones(): 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Por medio de esta funcionalidad, usted puede considerar despreciables aquellas asociaciones entre fármacos y efectos secundarios\ncuyo valor de asociación sea menor a cierto valor")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Respuesta_usuario=input("Por favor, indique el valor umbral de asociación entre fármaco y efecto secundario: ")
    try: 
        Respuesta_usuario=float(Respuesta_usuario)
        Consulta_SQL="""SELECT score FROM drug_phenotype_effect
                        WHERE phenotype_type = "SIDE EFFECT" AND score < %s AND score != 0;"""
        Cursor.execute(Consulta_SQL, (Respuesta_usuario,))
        Datos=Cursor.fetchall()
        if len(Datos) != 0: 
            Respuesta2_usuario=input(f"\nSe ha encontrado un total de {len(Datos)} de asociaciones con un valor menor al especificado.\n¿Está seguro que quiere hacer la modificación? [sí|no]: ")
            if re.search("[Ss][IiÍí]", Respuesta2_usuario):
                Modificacion_SQL="""UPDATE drug_phenotype_effect 
                                SET score = 0 
                                WHERE phenotype_type = "SIDE EFFECT" AND score < %s;"""
                Cursor.execute(Modificacion_SQL, (Respuesta_usuario,))
                print("\nLa modificación se ha realizado con éxito.")
        else: 
            print("\nNo hay asocaciones fármaco-efecto secundario con un score menor al introducido.")
    except ValueError:
                print("Necesitas meter un número para avanzar. Inténtalo de nuevo.\n")  
    return

## Aquí definimos los menús con las funcionalidades
def Funcionalidades_1(Ir_a):
    #Cursor=Base.cursor()
    if Ir_a==1:
        Obtener_total_farmacos()
    elif Ir_a==2:
        Obtener_total_enfermedades()
    elif Ir_a==3:
        Obtener_total_fenotipos()
    elif Ir_a==4:
        Obtener_total_dianas()
    elif Ir_a==5:
        Primeros_resultados_farmacos()
    elif Ir_a==6:
        Primeros_resultados_enfermedades()
    elif Ir_a==7:
        Primeros_resultados_fenotipos()
    elif Ir_a==8:
        Primeros_resultados_dianas()
    Ir_a=1
    Opciones(Ir_a)

def Funcionalidades_2(Ir_a):
    Cursor=Base.cursor()
    if Ir_a==1:
        Coger_informacion_farmaco_especifico(Buscar_farmaco())
    elif Ir_a==2:
        Coger_sinonimos_farmaco_especifico()
    elif Ir_a==3:
        Coger_codigos_ATC_farmaco_especifico(Buscar_farmaco())
    elif Ir_a==4:
        Farmaco_trata_enfermedades()
    elif Ir_a==5:
        Obtener_identificadores_farmaco()
    Ir_a=2
    Opciones(Ir_a)

def Funcionalidades_3(Ir_a):
    Cursor=Base.cursor()
    if Ir_a==1:
       Coger_farmacos_para_enfermedad()
    elif Ir_a==2:
        Mayor_asociacion()
    elif Ir_a==3:
        Buscar_termino_clave()
    Ir_a=3
    Opciones(Ir_a)

def Funcionalidades_4(Ir_a):
    Cursor=Base.cursor()
    if Ir_a==1:
        print("\n♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
        Farmaco=Buscar_farmaco()
        Cursor.execute("SELECT * FROM  drug WHERE drug_id = %s", (Farmaco,))
        if len(Cursor.fetchall())!=0:
            Coger_indicaciones_fenotipo(Farmaco)
        else:
            print("Este fármaco no está incluido en la base de datos.")
        print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n")
    elif Ir_a==2:
        print("\n♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
        Farmaco=Buscar_farmaco()
        Cursor.execute("SELECT * FROM drug WHERE drug_id = %s", (Farmaco,))
        if len(Cursor.fetchall())!=0:
            Coger_efectos_secundarios_fenotipo(Farmaco)
        else:
            print("Este fármaco no está incluido en la base de datos.")
        print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n")
    elif Ir_a==3:
        Farmacos_provocan_efecto_secundario()
    Ir_a=4
    Opciones(Ir_a)

def Funcionalidades_5(Ir_a):
    Cursor=Base.cursor()
    if Ir_a==1:
        Coger_primeras_dianas()
    elif Ir_a==2:
        Coger_organismo_mas_dianas()
    elif Ir_a==3:
        Dianas_organismo_concreto()
    elif Ir_a==4:
        Obtener_tipos_diana()
    Ir_a=5
    Opciones(Ir_a)

def Funcionalidades_6(Ir_a):
    Cursor=Base.cursor()
    if Ir_a==1:
        Borrado()
    Ir_a=6
    Opciones(Ir_a)

def Funcionalidades_7(Ir_a):
    Cursor=Base.cursor()
    if Ir_a==1:
        Inserciones()
    Ir_a=7
    Opciones(Ir_a)

def Funcionalidades_8(Ir_a):
    Cursor=Base.cursor()
    if Ir_a==1:
        Modificaciones()
    Ir_a=8
    Opciones(Ir_a)

#Definimos esta función para volver al menú principal cada vez que el usuario elige el 0 en un submenú.

#NOTA: La función "Opciones()" se explicará más adelante.
def Vuelta_al_principal():
    print("\n")
    Ir_a=Menu_principal()
    Opciones(Ir_a)

# Esta celda hace que el usuario, al realizar una acción en un menú, se quede en dicho menú.
print("\n¡Hola, bienvenido!")
print("  Este programa ha sido diseñado para ayudarle a navegar cómodamente por la base de datos \"disnet_drugslayer\".")
print("  Para desplazarse entre los diferentes menús, teclee el número que desee y presione la tecla \"Enter\".\n")

#Llamos a la función que imprime el menú principal, y guardamos la elección del usuario en "Ir_a". Hay que recordar que las funciones
 #de los diferentes menú, además de imprimir el menú en cuestión, piden al usuario el menú al que quiere dirigirse (apoyándose en la
 #función "Seleccion()".
Ir_a=Menu_principal()

#Esta función es la que permite que los menús aparezcan de forma recurrente. Su fuerza radica en la autorreferencialidad. Consta de
 #tantos condicionales como opciones disponibles hay en el menú principal. Una vez se pulsa y se ha metido en uno de los condiciona-
 #les, despliega el (llama a la función del) submenú correspondiente, haciendo que se imprima el texto correspondiente y dejando que
 #el usuario ejecute la opción deseada. Ahora, si la elección es 0, llama a la función "Vuelta_al_principal()" lo que, en esencia,
 #implica la llamada de "Opciones()" (autorreferencia) y la vuelta al menú principal (principal uso que damos a la autorreferencia);
 #en el caso de que se haya seleccionado una opción diferente de 0, llamamos a la función que contiene las funcionalidades (valga la
 #redundancia) del submenú (pasando la elección del usuario, almacenada en "Ir_a", a la función para que ejecute dicha opción).
def Mensaje_despedida(): 
    print("\n=============================================================================================")
    print("Gracias por confiar en nosotros, esperamos haberle sido de utilidad. ¡Hasta pronto!")
    print("=============================================================================================")
    return 

def Opciones(Ir_a):
    if Ir_a==1:
        Ir_a=Menu_1()
        if Ir_a==0:
            Vuelta_al_principal()
        elif Ir_a=="x" or Ir_a=="X":
            Mensaje_despedida()
        else:
            Funcionalidades_1(Ir_a)

    elif Ir_a==2:
        Ir_a=Menu_2()
        if Ir_a==0:
            Vuelta_al_principal()
        elif Ir_a=="x" or Ir_a=="X":
            Mensaje_despedida()
        else:
            Funcionalidades_2(Ir_a)

    elif Ir_a==3:
        Ir_a=Menu_3()
        if Ir_a==0:
            Vuelta_al_principal()
        elif Ir_a=="x" or Ir_a=="X":
            Mensaje_despedida()
        else:
            Funcionalidades_3(Ir_a)

    elif Ir_a==4:
        Ir_a=Menu_4()
        if Ir_a==0:
            Vuelta_al_principal()
        elif Ir_a=="x" or Ir_a=="X":
            Mensaje_despedida()
        else:
            Funcionalidades_4(Ir_a)

    elif Ir_a==5:
        Ir_a=Menu_5()
        if Ir_a==0:
            Vuelta_al_principal()
        elif Ir_a=="x" or Ir_a=="X":
            Mensaje_despedida()
        else:
            Funcionalidades_5(Ir_a)

    elif Ir_a==6:
        Ir_a=Menu_6()
        if Ir_a==0:
            Vuelta_al_principal()
        elif Ir_a=="x" or Ir_a=="X":
            Mensaje_despedida()
        else:
            Funcionalidades_6(Ir_a)

    elif Ir_a==7:
        Ir_a=Menu_7()
        if Ir_a==0:
            Vuelta_al_principal()
        elif Ir_a=="x" or Ir_a=="X":
            Mensaje_despedida()
        else:
            Funcionalidades_7(Ir_a)

    elif Ir_a==8:
        Ir_a=Menu_8()
        if Ir_a==0:
            Vuelta_al_principal()
        elif Ir_a=="x" or Ir_a=="X":
            Mensaje_despedida()
        else:
            Funcionalidades_8(Ir_a)

    #Si es 9, salimos del programa (gracias a "return").
    elif Ir_a=="x" or Ir_a=="X":
       Mensaje_despedida()
    return 

#Llamamos a la función para que se ejecute.
Opciones(Ir_a)

#NOTA: Esta función se podría haber sustituido por bucles "while", pero creemos que esta segunda opción era más aparatosa.

Base.close()
Cursor.close()