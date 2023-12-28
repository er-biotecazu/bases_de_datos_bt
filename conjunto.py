#Importamos el módulo que nos va a permitir trabajar sobre la base de datos y manejar errores. 
import mysql.connector 
from mysql.connector import errorcode
#Importamos el resto el módulo para trabajar con expresiones regulares. 
import re

#Por medio de la función Conexion() nos conectamos a la base de datos y, con la variable Base (objeto MySQLConnection), obtenemos un cursor. 
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
 # a) Que la cadena introducida no sea texto (manejado con el "try... except ValueError"), con la excepción de "X", que sirve para terminar la ejecución del programa. 
 # Esto se basa en el hecho de que la función "int" lanza una excepción con cadenas de texto que no pueden convertirse en enteros. 
 # b) Que el número introducido esté en el menú (números dentro del rango correspondiente).
def Seleccion(Opcion_mayor, Opcion_menor):
    #Iniciamos un bucle "while" del que no permitiremos salir hasta que se haya introducido una cadena correcta.
    Continuar=True
    while Continuar:
        Ir_a=input("Por favor, introduzca por teclado el menú al que quiera acceder: ").replace("\t", "")
        try:
            Ir_a=int(Ir_a)
            #Una vez sabemos que la cadena es numérica, comprobamos que el número introducido esté entre las opciones posibles.
            #Lógicamente, no puede estar por debajo de la opción (número) más pequeña, ni por encima de la más grande.
            if Ir_a>Opcion_mayor or Ir_a<Opcion_menor:
                print("No hay ningún menú que tenga asociado ese número. Por favor, revíselo.\n")
            else:
                #Si la cadena cumple todas las condiciones, salimos del bucle.
                Continuar=False
        #Este error sólo salta cuando el usuario mete texto (no se puede aplicar "int" a cadenas no numéricos).
        except ValueError:
            #Si la cadena introducida es "X", se sale del bucle. 
            if re.search(r"[xX]", Ir_a):
                Continuar=False
            else:
                print("Necesita meter un número para avanzar. Inténtelo de nuevo.\n")  
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

#A continuación, se definen una serie de funciones que servirán para alimentar otras funciones en los distintos subapartados. 

#La función que se define a continuación comprueba que el identificador ChEMBL de un fármaco que se introduce por teclado es correcto. 
def Buscar_farmaco():
    Continuar=True
    while Continuar:
        Farmaco=input("Por favor, introduzca el identificador ChEMBL de su fármaco de interés (ejemplo: CHEMBL1000): ").replace("\t", "")
        Farmaco=Farmaco.upper()
        if re.search(r"^(CHEMBL)[0123456789]{1,}$", Farmaco):
            Continuar=False
        else:
            print("Lo sentimos, la cadena introducida no es un identificador válido. Inténtelo de nuevo.\n")
    
    return Farmaco

#La función que se define a continuación sirve para que el usuario tenga la opción de generar un archivo de texto 
#con los resultados de la consulta. Viene definido por una serie de argumentos: 
    #Numero_campos se refiere al total de campos que se devuelve en cada tupla o fila.  
    #Encabezado contiene el encabezado para una determinada consulta. 
    #Datos contiene las tuplas de la consulta tal y como se almacenan en una variable con fetchall o fetchone. 
    #Nombre_archivo será el nombre que le demos al archivo de texto. 
#Esta función se utiliza en aquellas consultas que devuelven más de una tupla (cuando el resultado es un listado).
#Cada vez que el usuario acepte generar un archivo para un subapartado concreto, el anterior archivo, si es que 
#existía, será reescrito totalmente. 
def Obtener_archivo_texto(Numero_campos, Encabezado, Datos, Nombre_archivo): 
    Respuesta_usuario=input("\n¿Quiere generar un archivo de texto con los resultados de la consulta? El archivo resultante se guardará en su directorio de trabajo\ny reemplazará la versión anterior en caso de que exista. [En caso afirmativo, escriba \"Sí\"]: ").replace("\t", "")
    if re.search("[Ss][IiÍí]", Respuesta_usuario):
        Archivo_salida=open(Nombre_archivo, "w")
        #Se crea una lista donde se incluye el encabezado y las distintas filas con resultados. Esta lista se va a convertir
        #a texto posteriormente con el método .writelines()
        Tuplas_consulta=[]
        Tuplas_consulta.append(Encabezado)
        Numero_orden = 1
        #Se van rellenando los distintos campos de cada fila por dos bucles for encadenados.  
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

#La función que se define a continuación sirve para buscar fármacos en caso de que la cadena introducida no corresponda
#con ninguno de los presentes en la base de datos. Esto es útil porque en muchas ocasiones, el usuario no sabe cómo 
#escribir de forma exacta el nombre de un fármaco tal cual aparece en la base de datos. Por tanto, si la cadena introducida
#(el nombre del fármaco) supera los tres caracteres, por medio de la cláusula LIKE, se buscan aquellos fármacos que se parezcan
#al patrón introducido. 
def Busqueda_laxa_farmacos (Farmaco):
    Sentencia_estricta = "SELECT drug_name, drug_id FROM drug WHERE drug_name = %s"
    Cursor.execute(Sentencia_estricta, (Farmaco, ))
    Datos=Cursor.fetchall()
    #Si no aparecen resultados para el fármaco introducido, pero tiene más de tres caracteres, buscar fármacos con el patrón introducido. 
    if len(Datos) == 0 and len(Farmaco) >= 3:
        Sentencia_laxa = "SELECT drug_name, drug_id FROM drug WHERE drug_name LIKE %s"
        Farmaco = f"%{Farmaco}%"
        Cursor.execute(Sentencia_laxa, (Farmaco,))
        Datos=Cursor.fetchall()
        if len(Datos)!=0:
            print("\nNo hemos encontrado el fármaco que busca. ¿Quizás se refería a alguno de los siguientes?:\n")
            Numero_inicial=1
            for Fila in Datos:
                print(f"{Numero_inicial}\t{Fila[0]}")
                Numero_inicial+=1
            #Se pregunta al usuario si se encuentra en la lista proporcionada su fármaco de interés. 
            Respuesta_usuario=input(f"\n¿Se encuentra su fármaco de interés en la lista? [En caso afirmativo, escriba \"Sí\"]: ").replace("\t", "")
            if re.search("[Ss][IiÍí]", Respuesta_usuario): 
                try:
                    Respuesta3_usuario=input("Por favor, seleccione el número de su fármaco de interés: ").replace("\t", "")
                    Farmaco=Datos[int(Respuesta3_usuario)-1][0]
                    print(f"Su elección ha sido: {Farmaco}.") 
                except (ValueError, IndexError): 
                    print("\nPor favor, introduzca una opción válida.")
                    Farmaco=None
            #Si el usuario no encuentra ningún fármaco de interés entre las opciones mostradas, no es posible continuar con la consulta. 
            else: 
                print("Sentimos las molestias. Por favor, inténtelo de nuevo")
                Farmaco=None
        #Si no se encuentra ningún fármaco que incluya el patrón introducido, no es posible continuar con la consulta.
        else: 
            print("\nEl nombre del fármaco introducido no se encuentra en la base de datos. Por favor, inténtelo de nuevo.")
            Farmaco=None
    #Si la cadena introducida tiene menos de tres caracteres, no es posible continuar con la consulta. 
    elif len(Datos) == 0 and len(Farmaco) < 3: 
        print("\nEl nombre del fármaco introducido no se encuentra en la base de datos. Por favor, inténtelo de nuevo.")
        Farmaco=None
    return Farmaco


#A continuación, definimos los comandos DML que se requieren en los distintos apartados de los submenús por medio de funciones. 

# Apartado 1: Información general de la base de datos 
#Para los subapartados 1.1 - 1.4, empleamos la función de agregación "count()" con la clave primaria de las respectivas tablas.

## Subapartado 1.1: Número total de fármacos diferentes 
def Obtener_total_farmacos (): 
    Numero_farmacos = "SELECT COUNT(drug_id) FROM drug"
    Cursor.execute(Numero_farmacos)
    Datos = Cursor.fetchone()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"         | Número de fármacos registrados: {Datos[0]} fármacos |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

## Subapartado 1.2: Número total de enfermedades diferentes 
def Obtener_total_enfermedades ():
    Numero_enfermedades = "SELECT COUNT(disease_id) FROM disease"
    Cursor.execute(Numero_enfermedades)
    Datos = Cursor.fetchone()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"      | Número de enfermedades registradas: {Datos[0]} enfermedades |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

## Subapartado 1.3: Número total de fenotipos diferentes
def Obtener_total_fenotipos ():
    Numero_fenotipos = "SELECT COUNT(phenotype_id) FROM phenotype_effect"
    Cursor.execute(Numero_fenotipos)
    Datos = Cursor.fetchone()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"   | Número de efectos fenotípicos registrados: {Datos[0]} efectos fenotípicos |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

## Subapartado 1.4: Número total de dianas diferentes 
def Obtener_total_dianas (): 
    Numero_dianas = "SELECT COUNT(target_id) FROM target"
    Cursor.execute(Numero_dianas)
    Datos = Cursor.fetchone()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"           | Número de dianas registradas: {Datos[0]} dianas |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#Para los subapartados 1.5-1.8, se seleccionan las diez primeras instancias de fármacos, enfermedades, fenotipos y dianas
#con la condición de que los campos seleccionados no sean nulos. 

## Subapartado 1.5: Mostrar las primeras diez instancias de fármacos
def Primeros_resultados_farmacos ():
    Instancias_farmacos = """ 
                          SELECT drug_id, drug_name, molecular_type, chemical_structure, inchi_key 
                          FROM drug
                          WHERE drug_id IS NOT NULL AND drug_name IS NOT NULL AND molecular_type IS NOT NULL AND chemical_structure IS NOT NULL AND inchi_key IS NOT NULL
                          LIMIT 10;
                          """
    Cursor.execute(Instancias_farmacos)
    Datos = Cursor.fetchall()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Encabezado="**\t\t\tDiez primeras instancias de fármacos\t\t\t**\n\nN.º\tIdentificador\tNombre\t\tTipo molecular\tEstructura química\tClave InChy\n"
    print(Encabezado)
    Numero_inicial=1
    for Fila in Datos:
        print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}\t{Fila[2]}\t{Fila[3]}\t{Fila[4]}")
        Numero_inicial+=1
    Obtener_archivo_texto(5, Encabezado, Datos, "Consulta_1.5.txt")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    

## Subapartado 1.6: Mostrar las primeras diez instancias de enfermedades
def Primeros_resultados_enfermedades ():
    Instancias_enfermedades = """
                              SELECT disease_id, disease_name
                              FROM disease
                              WHERE disease_id IS NOT NULL AND disease_name IS NOT NULL
                              LIMIT 10; 
                              """
    Cursor.execute(Instancias_enfermedades)
    Datos = Cursor.fetchall()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Encabezado="**\tDiez primeras instancias de enfermedades\t**\n\nN.º\tIdentificador\tNombre\n"
    print(Encabezado)
    Numero_inicial=1
    for Fila in Datos:
        print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
        Numero_inicial+=1
    Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_1.6.txt")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
   
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
    Encabezado="**\tDiez primeras instancias de fenotipos\t**\n\nN.º\tIdentificador\tNombre\n"
    print(Encabezado)
    Numero_inicial=1
    for Fila in Datos:
        print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
        Numero_inicial+=1
    Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_1.7.txt")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

## Subapartado 1.8: Mostrar las primeras diez instancias de dianas 
def Primeros_resultados_dianas():
    Instancias_dianas = """
                        SELECT t.target_id, t.target_name_pref, t.target_type, o.taxonomy_name 
                        FROM target AS t, organism AS o
                        WHERE t.organism_id=o.taxonomy_id AND t.target_id IS NOT NULL AND t.target_name_pref IS NOT NULL AND t.target_type IS NOT NULL AND o.taxonomy_name IS NOT NULL
                        LIMIT 10;
                        """
    Cursor.execute(Instancias_dianas)
    Datos = Cursor.fetchall()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Encabezado="**\t\t\tDiez primeras instancias de dianas\t\t\t**\n\nN.º\tIdentificador\tNombre\t\t\tTipo\t\tOrganismo\n"
    print(Encabezado)
    Numero_inicial=1
    for Fila in Datos:
        print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}\t{Fila[2]}\t{Fila[3]}")
        Numero_inicial+=1
    Obtener_archivo_texto(4, Encabezado, Datos, "Consulta_1.8.txt")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Apartado 2: Información de los fármacos
## Subapartado 2.1: Información sobre un fármaco. 
def Coger_informacion_farmaco_especifico(Farmaco): 
    Consulta_SQL = """
                   SELECT drug_name, molecular_type, chemical_structure, inchi_key FROM drug
                   WHERE drug_id = %s;
                   """
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    Cursor.execute(Consulta_SQL, (Farmaco,))
    Datos=Cursor.fetchall()
    if len(Datos) != 0:
        Encabezado=f"**\tInformación sobre el fármaco {Farmaco.upper()}\t**\n\nNombre\tTipo molecular\tEstructura química\tClave InChi"
        print(Encabezado)
        print(f"{Datos[0][0]}\t{Datos[0][1]}\t{Datos[0][2]}\t{Datos[0][3]}")
    else:
        print("Este fármaco no está incluido en la base de datos.")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

## Subapartado 2.2: Sinónimos de un fármaco. 
def Coger_sinonimos_farmaco_especifico():
    Farmaco=input("Por favor, indique el nombre del fármaco del cual quiere obtener sus sinónimos (ejemplo: ASPIRIN): ").replace("\t", "")
    #Se comprueba que se haya introducido texto para continuar la consulta. 
    if len(Farmaco) != 0:
        Farmaco=Busqueda_laxa_farmacos(Farmaco)
        #Se comprueba que el nombre del fármaco existe en la base de datos.
        if Farmaco != None: 
            Consulta_SQL = """
                           SELECT s.synonymous_name FROM synonymous AS s, drug AS d
                           WHERE d.drug_name = %s AND s.drug_id = d.drug_id; 
                        """
            Cursor.execute(Consulta_SQL, (Farmaco, ))
            Datos=Cursor.fetchall()
            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            if len(Datos) != 0:
                Encabezado=f"Los sinónimos encontrados para el fármaco '{Farmaco.upper()}' son:\n"
                print(Encabezado)
                for Fila in Datos: 
                    print(Fila[0])
                Obtener_archivo_texto(1, Encabezado, Datos, "Consulta_2.2.txt")
            else: 
                print("No hay sinónimos para el fármaco proporcionado.")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    else:
        print("\nNo ha introducido texto. Por favor, inténtelo de nuevo.")

## Subapartado 2.3: Código ATC de un fármaco
def Coger_codigos_ATC_farmaco_especifico(Farmaco):
    Consulta_SQL = """
                   SELECT ATC_code_id FROM atc_code 
                   WHERE drug_id = %s
                   """
    Cursor.execute(Consulta_SQL, (Farmaco,))
    Datos=Cursor.fetchall()
    #Los resultados se presentarán de forma diferente en función de si existe o no código ATC para el fármaco en cuestión y, en caso que exista, si hay más de uno. 
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if len(Datos) != 0: 
        if len(Datos) == 1:
            Encabezado=f"Identificador ATC del fármaco seleccionado: {Datos[0][0]}"
            print(Encabezado)
        else: 
            Encabezado="Identificadores ATC del fármaco seleccionado:\n"
            print(Encabezado)
            Numero_inicial = 1
            for Fila in Datos: 
                print(f"{Numero_inicial}: {Fila[0]}")
                Numero_inicial+=1
            Obtener_archivo_texto(1, Encabezado, Datos, "Consulta_2.3.txt")
    else: 
        print("No se ha encontrado ningún identificador ATC para el fármaco solicitado.")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

## Subapartado 2.4: Enfermedades que puede tratar un fármaco determinado
def Farmaco_trata_enfermedades():
    Farmaco=input("Introduce el nombre de tu fármaco de interés (por ejemplo, ASPIRIN): ").replace("\t", "")
    if len(Farmaco) != 0:
        Farmaco=Busqueda_laxa_farmacos(Farmaco)
        if Farmaco != None:
            Consulta_SQL="""
                    SELECT d.disease_id, d.disease_name FROM disease AS d, disease_has_code AS dhc, drug_disease AS dd
                    WHERE dd.drug_id IN (SELECT drug_ID FROM drug WHERE drug_name=%s) AND dhc.code_id = dd.code_id AND d.disease_id = dhc.disease_id;
                    """
            Cursor.execute(Consulta_SQL, (Farmaco,))
            Datos=Cursor.fetchall()
            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            if len(Datos)!=0:
                Encabezado=f"**\tEnfermedades tratadas por el fármaco {Farmaco.upper()}\t\t**\n\nN.º\tIdentificador\tNombre\n"
                print(Encabezado)
                Numero_inicial = 1
                for Fila in Datos:
                    print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
                    Numero_inicial+=1
                Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_2.4.txt")
            else:
                print("Este fármaco no tiene asociada ninguna enfermedad tratada en la base de datos.")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    else:
        print("\nNo ha introducido texto. Por favor, inténtelo de nuevo.")

## Subapartado 2.5: Obtener identificadores del fármaco 
def Obtener_identificadores_farmaco():
    Farmaco=input("Introduce el nombre de tu fármaco de interés (por ejemplo, ASPIRIN): ").replace("\t", "")
    if len(Farmaco) != 0:
        Farmaco=Busqueda_laxa_farmacos(Farmaco)
        if Farmaco != None:
            Sentencia="SELECT drug_name, drug_id FROM drug WHERE drug_name = %s"
            Cursor.execute(Sentencia, (Farmaco,))
            Codigo_CHEMBL=Cursor.fetchall()
            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            if len(Codigo_CHEMBL)!=0:
                print(f"\t\t\t{Codigo_CHEMBL[0][0]}:  {Codigo_CHEMBL[0][1]}")
            else:
                print("    |    Este fármaco no se encuentra presente en la base de datos.    |    ")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    else:
        print("\nNo ha introducido texto. Por favor, inténtelo de nuevo.")

# Apartado 3. Información de las enfermedades 
## Subapartado 3.1: Fármacos para una enfermedad: 
def Coger_farmacos_para_enfermedad(): 
    Respuesta_usuario = input("Por favor, indique el nombre de la enfermedad de la que quiere consultar los fármacos involucrados en su tratamiento: ").replace("\t", "")
    if len(Respuesta_usuario) != 0:
        Consulta_SQL = """
                       SELECT d.drug_id, d.drug_name FROM drug_disease as dd, drug as d, disease_code AS dc
                       WHERE dc.name = %s AND dd.code_id = dc.code_id AND d.drug_id = dd.drug_id;
                       """
        Cursor.execute(Consulta_SQL, (Respuesta_usuario,))
        Datos=Cursor.fetchall()
        print("\n##############################################################################################")
        if len(Datos) != 0:
            Encabezado=f"**\tFármacos para el tratamiento de la enfermedad '{Respuesta_usuario}'\t**\nN.º\tIdentificador\tNombre\n"
            print(Encabezado)
            Numero_inicial=1
            for Fila in Datos:
                print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
                Numero_inicial+=1
            Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_3.1.txt")
        else:
            print("Esta enfermedad no está incluida en la base de datos.")
        print("##############################################################################################\n")
    else:
        print("\nNo ha introducido texto. Por favor, inténtelo de nuevo.\n")

## Subapartado 3.2: Enfermedad y fármaco con el mayor "score" de asociación.
def Mayor_asociacion():
    Sentencia="""
              SELECT d.drug_name, dc.name, dd.inferred_score FROM drug_disease AS dd, drug AS d, disease_code AS dc
              WHERE dd.inferred_score = (SELECT max(inferred_score) FROM drug_disease) AND d.drug_id = dd.drug_id AND dc.code_id = dd.code_id;
              """
    Cursor.execute(Sentencia)
    Resultado=Cursor.fetchone()   
    print("\n##################################################################################################################################")
    print(f"La mayor asociación la presentan la enfermedad '{Resultado[1]}' y el fármaco '{Resultado[0]}' (la puntuación es de {Resultado[2]}).")
    print("##################################################################################################################################\n")

## Subapartado 3.3: Buscar enfermedades asociadas a un término clave.
def Buscar_termino_clave():
    Termino_clave=input("Por favor, introduce una palabra o término clave y te devolveremos enfermedades en cuyo nombre se incluya (ejemplo: NEURO): ").replace("\t", "")
    #Con esta condición, nos aseguramos de que el usuario no ha introducido un "Enter".
    if len(Termino_clave) != 0:
        Termino_clave_patron=f"%{Termino_clave}%"
        Sentencia="SELECT name, code_id, vocabulary FROM disease_code WHERE name LIKE %s"
        Cursor.execute(Sentencia, (Termino_clave_patron,))
        Datos=Cursor.fetchall()
        print("\n##############################################################################################################")
        if len(Datos)!=0:
            Encabezado=f"Enfermedades encontradas para el patrón '{Termino_clave}'. Se proporciona el nombre de la enfermedad y su código en cierto vocabulario:\n"
            print(Encabezado)
            for Fila in Datos:
                print(f"  -  {Fila[0]} ({Fila[1]}; {Fila[2]})")
            Obtener_archivo_texto(3, Encabezado, Datos, "Consulta_3.3.txt")
        else:
            print("Lo sentimos, no se ha encontrado ninguna enfermedad que incluya ese término.")
        print("##############################################################################################################\n")
    else:
        print("\nNo ha introducido texto. Por favor, inténtelo de nuevo.\n")

#Apartado 4. 
##Subapartado 4.1: Indicaciones de un fármaco
def Coger_indicaciones_fenotipo(Farmaco): 
    Consulta_SQL = """
                   SELECT pe.phenotype_id, pe.phenotype_name FROM drug_phenotype_effect AS dpe, phenotype_effect AS pe
                   WHERE dpe.drug_id = %s AND dpe.phenotype_type="INDICATION" AND pe.phenotype_id = dpe.phenotype_id;
                   """
    Cursor.execute(Consulta_SQL, (Farmaco,))
    Datos=Cursor.fetchall()
    if len(Datos) != 0: 
        Encabezado=f"**\tIndicaciones del fármaco {Farmaco}\t**\nN.º\tID del fenotipo\tIndicado para\n"
        print(Encabezado)
        Numero_inicial=1
        for Fila in Datos: 
            print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
            Numero_inicial+=1
        Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_4.1.txt")
    else: 
        print("No hay efectos secundarios registrados para este fármaco.")

##Subapartado 4.2: Efectos secundarios de un fármaco
def Coger_efectos_secundarios_fenotipo(Farmaco): 
    Consulta_SQL = """
                   SELECT pe.phenotype_id, pe.phenotype_name FROM drug_phenotype_effect AS dpe, phenotype_effect AS pe
                   WHERE dpe.drug_id = %s AND dpe.phenotype_type="SIDE EFFECT" AND pe.phenotype_id = dpe.phenotype_id
                   ORDER BY score DESC;
                   """
    Cursor.execute(Consulta_SQL, (Farmaco,))
    Datos=Cursor.fetchall()
    if len(Datos) != 0: 
        Encabezado=f"**\tEfectos secundarios del fármaco {Farmaco}\t**\nN.º\tID del fenotipo\t\tEfecto secundario\n"
        print(Encabezado)
        Numero_inicial=1
        for Fila in Datos: 
            print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
            Numero_inicial+=1
        Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_4.2.txt")
    else: 
        print("No hay efectos secundarios registrados para este fármaco.")

## Subapartado 4.3: Fármacos que provocan un efecto secundario determinado
def Farmacos_provocan_efecto_secundario():
    Efecto=input("Por favor, indique el efecto secundario que le interesa: ").replace("\t", "")
    if len(Efecto) != 0:
        #Primero, se hace una comprobación de que el efecto fenotípico introducido aparece realmente como efecto secundario. 
        Consulta_SQL = """
                       SELECT * FROM drug_phenotype_effect
                       WHERE phenotype_id IN (SELECT phenotype_id FROM phenotype_effect WHERE phenotype_name = %s) AND phenotype_type = 'SIDE EFFECT';
                       """
        Cursor.execute(Consulta_SQL, (Efecto,))
        Datos=Cursor.fetchall()
        print("\n♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
        if len(Datos) != 0: 
            Consulta2_SQL="""
                  SELECT drug_id, drug_name FROM drug 
                  WHERE drug_id IN (SELECT drug_id FROM drug_phenotype_effect WHERE phenotype_id IN (SELECT phenotype_id FROM phenotype_effect WHERE phenotype_name = %s));
                """
            Cursor.execute(Consulta2_SQL, (Efecto,))
            Datos=Cursor.fetchall()
            Encabezado=f"**\tFármacos asociados con el efecto secundario '{Efecto}'\t**\nN.º\tIdentificador\tFármaco\n"
            print(Encabezado)
            Numero_inicial=1
            for Fila in Datos:
                print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
                Numero_inicial+=1
            Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_4.3.txt")
        else: 
            print("El efecto fenotípico introducido no aparece como efecto secundario de ningún fármaco. Por favor, inténtelo de nuevo.")
        print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n")
    else:
        print("\nNo ha introducido texto. Por favor, inténtelo de nuevo.\n")

# Apartado 5. 
## Subapartado 5.1: Dianas de un tipo
def Coger_primeras_dianas(): 
    Diana=input("\nPor favor, introduzca el tipo de diana de la que quiere obtener sus 20 primeras instancias: ").replace("\t", "")
    if len(Diana) != 0:
        Consulta_SQL = """
                       SELECT target_id, target_name_pref FROM target 
                       WHERE target_type = %s
                       ORDER BY target_name_pref ASC
                       LIMIT 20;
                    """
        Cursor.execute(Consulta_SQL, (Diana,))
        Datos=Cursor.fetchall()
        print("\n*******************************************************************************************")
        if len(Datos) != 0: 
            Encabezado=f"**\t20 primeras instancias de la diana '{Diana.upper()}'\t**\nN.º\tIdentificador\tDiana\n"
            print(Encabezado)
            Numero_inicial=1
            for Fila in Datos: 
                print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
                Numero_inicial+=1
            Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_5.1.txt")
        else: 
            print("\nNo se ha encontrado ningún fármaco para la diana proporcionada.")
        print("*******************************************************************************************\n")
    else:
        print("\nNo ha introducido texto. Por favor, inténtelo de nuevo.\n")

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
    Respuesta_usuario=input("\n¿Quiere consultar el total de las dianas para el organismo seleccionado? [En caso afirmativo, escriba \"Sí\"]: ").replace("\t", "")
    if re.search("[Ss][IiÍí]", Respuesta_usuario):    
        Consulta2_SQL="SELECT target_id, target_name_pref FROM target WHERE organism_id = %s;"
        Cursor.execute(Consulta2_SQL, (Datos[1],))
        Dianas=Cursor.fetchall()
        Encabezado=f"**\tDianas asociadas al organismo '{(Datos[0]).upper()}'\t**\n"
        Numero_inicial=1
        for Diana in Dianas:
            print(f"  ·  {Numero_inicial}: {Diana[1]} ({Diana[0]})")
            Numero_inicial+=1
        Obtener_archivo_texto(2, Encabezado, Dianas, "Consulta_5.2.txt")
    print("*******************************************************************************************\n")

## Subapartado 5.3: Dianas que hay asociadas a un organismo en concreto
def Dianas_organismo_concreto():
    Organismo=input("Por favor, indique el nombre de su organismo de interés (por ejemplo: Homo sapiens): ").replace("\t", "")
    if len(Organismo) != 0:
        Sentencia="""
                  SELECT target_id, target_name_pref 
                  FROM target 
                  WHERE organism_id=(SELECT taxonomy_id FROM organism WHERE taxonomy_name = %s);
                """
        Cursor.execute(Sentencia, (Organismo,))
        Datos=Cursor.fetchall()
        print("\n*******************************************************************************************")
        if len(Datos)!=0:
            Encabezado=f"**\tDianas asociadas a '{Organismo.upper()}'\t**\nN.º\tIdentificador\tDiana"
            print(Encabezado)
            Numero_inicial=1
            for Fila in Datos:
                print(f"{Numero_inicial}\t{Fila[0]}\t{Fila[1]}")
                Numero_inicial+=1
            Obtener_archivo_texto(2, Encabezado, Datos, "Consulta_5.3.txt")
        else:
            print("Este organismo no tiene dianas incluidas en la base de datos.")
        print("*******************************************************************************************\n")
    else:
        print("\nNo ha introducido texto. Por favor, inténtelo de nuevo.\n")

## Subapartado 5.4: Tipos de dianas que hay en la base de datos
def Obtener_tipos_diana():
    print("A continuación, se le van a proporcionar los distintos tipos de dianas que aparecen en la base de datos:")
    Consulta_SQL="SELECT target_type FROM target GROUP BY target_type;"
    Cursor.execute(Consulta_SQL)
    Datos=Cursor.fetchall()
    print("\n*****************************************************************************************************")
    for Fila in Datos:
        print(Fila[0])
    print("*****************************************************************************************************\n")

#Apartado 6: Borrado
def Borrado():
    print("Por medio de esta funcionalidad, se le van a mostrar las diez asociaciones entre fármaco y enfermedad con un score inferido más bajo.")
    print("Usted dispone de la oportunidad de borrar alguna de esas asociaciones.")
    sql_query = """ 
                SELECT dd.inferred_score, d.drug_name, dc.name FROM drug_disease AS dd, drug AS d, disease_code AS dc
                WHERE d.drug_id = dd.drug_id AND dc.code_id = dd.code_id AND inferred_score IS NOT NULL
                ORDER BY inferred_score ASC
                LIMIT 10;
                """
    Cursor.execute(sql_query)
    Datos=Cursor.fetchall()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("N.º\tScore inferido\tNombre del fármaco\tNombre de la enfermedad\n")
    Numero_inicial=1
    for Fila in Datos: 
        print(f"{Numero_inicial}\t{Fila[0]}\t\t{Fila[1]}\t{Fila[2]}")
        Numero_inicial+=1
    Respuesta_usuario=input("\n¿Desea borrar alguna asociación de entre las mostradas? [En caso afirmativo, escriba \"Sí\"]: ").replace("\t", "")
    if re.search("[Ss][IiÍí]", Respuesta_usuario):
        Respuesta_usuario2 = input("Indique el número de la asociación que quiere borrar: ").replace("\t", "")
        try:
            Seleccion_usuario = Datos[int(Respuesta_usuario2)-1]
            print(f"Esta ha sido su elección:\t{Seleccion_usuario[0]}\t{Seleccion_usuario[1]}\t{Seleccion_usuario[2]}")
            Respuesta_usuario3 = input("\n¿Está seguro de que quiere borrar esta relación? [En caso afirmativo, escriba \"Sí\"]: ").replace("\t", "")
            #Nótese que para buscar el fármaco que tiene el valor de inferred_score seleccionado para su borrado, utilizamos la función 'LIKE'. Esto se debe a que los valores de esta columna 
            #son de tipo 'float'. El sistema, internamente, representa los valores con mayor precisión añadiendo un número mayor de decimales que los que se devuelven en la consulta, por lo 
            #que no se puede utilizar un igual en este caso. 
            if  re.search("[Ss][IiÍí]", Respuesta_usuario3):
                Borrado_SQL = """
                              DELETE FROM drug_disease 
                              WHERE inferred_score LIKE %s AND drug_id IN (SELECT drug_id FROM drug WHERE drug_name = %s) 
                              AND code_id IN (SELECT code_id FROM disease_code WHERE name = %s)
                              """
                Cursor.execute(Borrado_SQL, (Seleccion_usuario[0], Seleccion_usuario[1], Seleccion_usuario[2],))
                Base.commit()
                print("\nEl borrado se ha realizado con éxito.")
            else: 
                print("Usted ha abandonado la opción de borrado")
        except (ValueError, IndexError):
                print("\nLo sentimos, necesita introducir una opción válida para proceder con el borrado.")
    else: 
        print("Usted ha abandonado la opción de borrado")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Apartado 7: Inserciones 

###Por medio de la siguiente función, se comprueba que el nombre de fármaco introducido está asociado a un identificador de la tabla drug.
def Comprobar_farmaco_nombre():
    Farmaco=input("\nPor favor, introduzca el nombre de su fármaco de interés (ejemplo: ASPIRIN): ").replace("\t", "")
    if len(Farmaco) != 0:
        #Primero, se hace una comprobación de que el nombre del fármaco existe. En realidad, no es necesaria (se podría comenzar por la Consulta2_SQL),
        #pero se incluye en cumplimiento de la consideración general sobre realizar comprobaciones cuando sea posible.
        Consulta_SQL = "SELECT drug_name FROM drug WHERE drug_name = %s;" 
        Cursor.execute(Consulta_SQL, (Farmaco,))
        Datos=Cursor.fetchall()
        if len(Datos) != 0:
            Consulta2_SQL = "SELECT drug_id FROM drug WHERE drug_name = %s;"
            Cursor.execute(Consulta2_SQL, (Farmaco,))
            Datos = Cursor.fetchall()
            #Si para un nombre de fármaco aparece más de un identificador ChEMBL, se le da al usuario la opción de elegir cuál quiere incluir.
            if len(Datos) > 1: 
                print("Se han encontrado varios identificadores para el nombre de fármaco introducido:")
                Numero_inicial=1
                for Fila in Datos: 
                    print(f"{Numero_inicial}\t{Fila[0]}")
                    Numero_inicial+=1
                Respuesta_usuario=input("Por favor, seleccione el número de uno de los identificadores mostrados: ").replace("\t", "")
                #Se hace manejo de errores si el usuario no proporciona un número válido o introduce una cadena de texto.
                try: 
                    Farmaco=Datos[int(Respuesta_usuario)-1][0]
                except (ValueError, IndexError): 
                    print("Lo sentimos, necesita introducir una opción válida.")
            else:
                Farmaco = Datos[0][0]
        #Si el nombre del fármaco no aparece en la base de datos, pero se han introducido por lo menos tres caracteres, el programa va a dar una
        #segunda oportunidad al usuario, escogiendo nombres de fármacos que sean similares. Esto es especialmente útil en aquellos fármacos, como
        #'penicillin', con varios nombres similares. Nuevamente, se hace manejo de errores en caso de que las respuestas introducidas por el usuario
        #sean incorrectas. 
        elif len(Farmaco) >= 3: 
            Consulta3_SQL = "SELECT drug_name FROM drug WHERE drug_name LIKE %s;"
            Farmaco = f"%{Farmaco}%"
            Cursor.execute(Consulta3_SQL, (Farmaco,))
            Datos=Cursor.fetchall()
            if len(Datos) != 0:
                print("\nLo sentimos, no hemos encontrado el fármaco que busca. ¿Quizás se refería a alguno de los siguientes?: ")
                Numero_inicial = 1
                for Fila in Datos:
                    print(f"{Numero_inicial}: {Fila[0]}")
                    Numero_inicial+=1
                Respuesta2_usuario=input(f"\n¿Se encuentra su fármaco de interés en la lista? [En caso afirmativo, escriba \"Sí\"]: ").replace("\t", "")
                if re.search("[Ss][IiÍí]", Respuesta2_usuario): 
                    try:
                        Respuesta3_usuario=input("\nPor favor, seleccione el número de su fármaco de interés: ").replace("\t", "")
                        Farmaco=Datos[int(Respuesta3_usuario)-1][0]
                        print(f"Su elección ha sido: {Farmaco}.")
                        Consulta2_SQL = "SELECT drug_id FROM drug WHERE drug_name = %s;"
                        Cursor.execute(Consulta2_SQL, (Farmaco,))
                        Datos = Cursor.fetchone()
                        Farmaco = Datos[0]
                    except (ValueError, IndexError):
                        print("Tiene que introducir una opción válida.")
            #Si el nombre del fármaco que introduce el usuario excede los tres caracteres, pero no se encuentra ninguno en la base de datos con un patrón 
            #similar, se hace saber al usuario que debe intentarlo de nuevo. 
            else:
                print(f"Lo sentimos, este fármaco no está dentro de la base de datos. Por favor, vuelva a intentarlo de nuevo.")
        #Si lo que introduce el usuario es una cadena de menos de tres caracteres, se hace saber al usuario que debe intentarlo de nuevo. 
        else:
            print(f"Lo sentimos, este fármaco no está dentro de la base de datos. Por favor, vuelva a intentarlo de nuevo.")
    else: 
        print("No ha introducido texto. Por favor, inténtelo de nuevo.")
    return Farmaco

###Por medio de la siguiente función, se comprueba que no existe la tupla id de fármaco - código del fármaco - vocabulario.
def Comprobar_codigo_farmaco(ID_Farmaco, Vocabulario_farmaco): 
    Codigo_farmaco=input("Por favor, introduzca el código identificador del fármaco. El dato introducido ha de ser un número: ").replace("\t", "")
    try: 
        int(Codigo_farmaco)
        Consulta_SQL = "SELECT code_id FROM drug_has_code WHERE drug_id = %s AND code_id = %s AND vocabulary = %s;"
        Cursor.execute(Consulta_SQL, (ID_Farmaco, Codigo_farmaco, Vocabulario_farmaco,))
        Datos=Cursor.fetchall()
        if len(Datos) != 0: 
            Codigo_farmaco="fail"
            print(f"\nLo sentimos, el código introducido ya está asociado a este fármaco para el vocabulario introducido.")
    except ValueError:
        Codigo_farmaco="fail" 
        print("\nNecesita meter un número para avanzar. Inténtelo de nuevo.\n")  
    return Codigo_farmaco

def Inserciones():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Por medio de esta funcionalidad, usted puede ampliar las codificaciones de un fármaco ya existente en la base de datos.")
    print("Usted debe introducir el nombre del fármaco, el nuevo código y el vocabulario del que proviene. El nombre del fármaco ha de existir ya en la base de datos.")
    print("El código introducido no puede estar ya asociado a ese fármaco para el vocabulario elegido.") 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ID_farmaco=Comprobar_farmaco_nombre()
    if re.search(r"^(CHEMBL)[0123456789]{1,}$", ID_farmaco):
        Vocabulario_farmaco=input("Por favor, introduzca el nombre del vocabulario para el que pertenece el código: ").replace("\t", "")
        Codigo_farmaco=Comprobar_codigo_farmaco(ID_farmaco, Vocabulario_farmaco)
        if Codigo_farmaco != "fail":
            Insercion_SQL="INSERT INTO drug_has_code(drug_id, code_id, vocabulary) VALUES (%s, %s, %s);" 
            try: 
                Cursor.execute(Insercion_SQL, (ID_farmaco, Codigo_farmaco, Vocabulario_farmaco,))
                Base.commit()
                print("\nLa inserción se ha realizado con éxito.")
            except:
                print("\nLo sentimos, no ha podido ejecutarse esta inserción")

#Apartado 8. Modificaciones 
def Modificaciones(): 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Por medio de esta funcionalidad, usted puede considerar despreciables aquellas asociaciones entre fármacos y efectos secundarios\ncuyo valor de asociación sea menor a cierto valor")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Respuesta_usuario=input("Por favor, indique el valor umbral de asociación entre fármaco y efecto secundario: ").replace("\t", "")
    try: 
        Respuesta_usuario=float(Respuesta_usuario)
        Consulta_SQL="""
                     SELECT score FROM drug_phenotype_effect
                     WHERE phenotype_type = "SIDE EFFECT" AND score < %s AND score != 0;
                     """
        Cursor.execute(Consulta_SQL, (Respuesta_usuario,))
        Datos=Cursor.fetchall()
        if len(Datos) != 0: 
            Respuesta2_usuario=input(f"\nSe ha encontrado un total de {len(Datos)} de asociaciones con un valor menor al especificado.\n¿Está seguro que quiere hacer la modificación? [En]caso afirmativo, escriba \"Sí\": ").replace("\t", "")
            if re.search("[Ss][IiÍí]", Respuesta2_usuario):
                Modificacion_SQL="""UPDATE drug_phenotype_effect 
                                SET score = 0 
                                WHERE phenotype_type = "SIDE EFFECT" AND score < %s;"""
                try:
                    Cursor.execute(Modificacion_SQL, (Respuesta_usuario,))
                    Base.commit()
                    print("\nLa modificación se ha realizado con éxito.")
                except:
                    print("\nLo sentimos, no ha podido ejecutarse la modificación.")
        else: 
            print("\nNo hay asocaciones fármaco-efecto secundario con un score menor al introducido.")
    except:
                print("Necesitas meter un número para avanzar. Inténtalo de nuevo.\n")

## Aquí definimos los menús con las funcionalidades
def Funcionalidades_1(Ir_a):
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
    if Ir_a==1:
       Coger_farmacos_para_enfermedad()
    elif Ir_a==2:
        Mayor_asociacion()
    elif Ir_a==3:
        Buscar_termino_clave()
    Ir_a=3
    Opciones(Ir_a)

def Funcionalidades_4(Ir_a):
    if Ir_a==1:
        Farmaco=Buscar_farmaco()
        Cursor.execute("SELECT * FROM  drug WHERE drug_id = %s", (Farmaco,))
        print("\n♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
        if len(Cursor.fetchall())!=0:
            Coger_indicaciones_fenotipo(Farmaco)
        else:
            print("Este fármaco no está incluido en la base de datos.")
        print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n")
    elif Ir_a==2:
        Farmaco=Buscar_farmaco()
        Cursor.execute("SELECT * FROM drug WHERE drug_id = %s", (Farmaco,))
        print("\n♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
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
    if Ir_a==1:
        Borrado()
    Ir_a=6
    Opciones(Ir_a)

def Funcionalidades_7(Ir_a):
    if Ir_a==1:
        Inserciones()
    Ir_a=7
    Opciones(Ir_a)

def Funcionalidades_8(Ir_a):
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