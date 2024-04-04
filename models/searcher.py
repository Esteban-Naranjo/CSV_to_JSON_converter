"""Importación del objeto Path que contiene funciones útiles para una ruta, y json para 
hacer operaciones de conversión"""
from pathlib import Path
import json

class Searcher:
    """Clase Control que funciona como buscador de archivos y se encarga de convertir CSV a JSON"""
    def __init__(self, route: str) -> None:
        self.route = Path(route)

    def find_file(self) -> str:
        """Método que busca si una ruta existe, y si corresponde a un archivo con extensión CSV"""
        if self.route.exists():
            if self.route.suffix == '.csv' and self.route.is_file():
                self.convert_to_json()
                return 'Ok'
            print('Directorio o archivo no válido para la conversión')
            raise ValueError
        print("El archivo no existe.")
        raise FileNotFoundError

    def convert_to_json(self) -> bool:
        """Método que se ejecuta luego de find_file, y lo convierte 
        en un archivo JSON con la información contenida"""
        data = []
        json_route = self.route.with_suffix('.json')
        with self.route.open(encoding='utf-8') as text:
            content = text.read()
            if ',' in content:
                for line in content.splitlines():
                    student = line.strip().split(',')
                    data.append({"id": student[0], "nombre": student[1], "apellido": student[2]})
                with json_route.open(mode='w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, indent=4, ensure_ascii=False)
                return True
            print('Archivo sin delimitadores (,) en su interior')
            return False
