# GraphLibrary
A simple Python3 library to generate graphs

Main.py Ejecuta todos los modelos de generación aleatoria de grafos para 30, 100 y 500 nodos.


Algorithms.py Contiene todos los modelos usados para la generación aleatoria de grafos.


Graph.py Es la clase grafo, guarda los objetos nodos y objetos aristas en listas. Cuenta con una lista auxiliar llamada "str_edges" que guarda los mismos aristas de la lista "edges" pero en formato string (se usa porque facilita la búsqueda de aristas existentes en algunos algoritmos). Contiene métodos para agregar nodos, aristas, obtener el grado de un nodo y para exportar el grafo a un archivo GraphViz.



Edge.py Es la clase de arista. Contiene los atributos "start" y "end" que se refieren a los dos nodos que la componen.


Node.py Es la clase nodo. Tiene como atributo el id y coordenadas "x" y "y" que son ocupadas en el método geográfico simple.


Carpeta GraphViz Muestra los archivos .gv que se exporta de cada método en cada configuración (30,100,500).

Carpeta Graph Images Contiene las imágenes obtenidas en gephi de los grafos generados por main.py.
