"""Importación del controlador y la clase unittest para efectuar las pruebas sobre sus funciones"""
import unittest
from models.searcher import Searcher

class TestSearcher(unittest.TestCase):
    """Clase que testea las funcionalidades de la clase Searcher"""
    def test_correct_route_file(self):
        """Test que comprueba si la ruta dada existe"""
        searcher = Searcher('./example_files/estudiantes.csv')
        msj = searcher.find_file()
        self.assertEqual (msj, 'Ok')

    def test_incorrect_route_file(self):
        """Test que verifica el correcto manejo cuando una ruta no existe"""
        searcher = Searcher('./example_files/xyz.csv')
        with self.assertRaises(FileNotFoundError):
            file = searcher.find_file()

    def test_file_separated_by_comas(self):
        """Test que verifica si en el archivo CSV existen comas"""
        searcher = Searcher('./example_files/estudiantes.csv')
        result = searcher.convert_to_json()
        self.assertTrue(result)

    def test_file_not_separated_by_comas(self):
        """Test que verifica la no acción cuando en el archivo CSV no existen comas"""
        searcher = Searcher('./example_files/estudiantes_without_comas.csv')
        result = searcher.convert_to_json()
        self.assertFalse(result)

    def test_file_requirements(self):
        """Test que verifica cuando un archivo no tiene la extensión requerida (CSV)"""
        searcher = Searcher('./example_files/estudiantes.txt')
        with self.assertRaises(ValueError):
            result = searcher.find_file()

    def test_if_route_is_not_dir(self):
        """Test que verifica si la ruta dada es un directorio"""
        searcher = Searcher('./example_files')
        with self.assertRaises(ValueError):
            result = searcher.find_file()
