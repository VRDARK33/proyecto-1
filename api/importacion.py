import pandas as pd # Se importa la biblioteca pandas para manejar los datos
from sodapy import Socrata # Se importa la biblioteca Socrata para interactuar con la API de datos abiertos

client = Socrata("www.datos.gov.co", None) # Se crea un objeto 'client' para interactuar con la API de datos abiertos

def base_de_datos(departamentoName,limite): # Se define la función 'base_de_datos' con dos argumentos: el nombre del departamento y el límite de resultados que se desean obtener
    results = client.get("gt2j-8ykr", limit=limite,departamento_nom = departamentoName) # Se utiliza el objeto 'client' para realizar una solicitud a la API de datos abiertos y obtener los datos correspondientes al departamento y límite especificados

    results_df = pd.DataFrame.from_records(results) # Se convierte la respuesta en formato JSON en un marco de datos de pandas
    return(results_df) # Se devuelve el marco de datos con los resultados de la consulta

    