"""Import de la clase Searcher"""
from models.searcher import Searcher

route = input('Ingrese la ruta de su archivo CSV: ')

searcher = Searcher(route)
searcher.find_file()
