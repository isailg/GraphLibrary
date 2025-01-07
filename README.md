# GraphLibrary - Algoritmo de Dijkstra

### Isaí López García  
---

## Descripción

Este repositorio contiene el código del Proyecto 3 para aplicar el algoeritmo de Dijkstra a los grafos generados aleatoriamente con los algoritmos de proyectos anteriores.

### Contenido del Repositorio

1. **Código:** Incluye los algoritmos y clases del proyecto anterior junto con el nuevo método de la clase Grafo llamados `Dijkstra`, que únicamente tiene de entrada el nodo origen del cual serán calculados los caminos de mínimo peso para cada uno de los nodos.

  - **Main.py** Ejecuta todos los modelos de generación aleatoria de grafos para pocos nodos (30) y muchos nodos (100), y luego aplica Dijkstra que exporta un archivo (.gv) usado para visualizar el grafo y el peso del camino mínimo de cada uno de los nodos al nodo origen.

2. **Archivos Generados:**
   
  - **GeneratedGraphs(gv)/**: Carpeta que contiene los archivos `.gv` generados por los algoritmos de generación aleatoria para 30 y 100 nodos.
  - **CalculatedGraphs(gv)/**: Carpeta que contiene los archivos `.gv` generados por el algoritmo de Dijkstra aplicado a cada grafo de la carpeta mencionada anteriormente.

3. **Capturas de Pantalla:**
   
- **GeneratedGraphs(img)/**: Carpeta que contiene las imágenes generadas con Gephi a partir de los grafos de la carpeta GeneratedGraphs(gv)/.
- **CalculatedGraphs(img)/**: Carpeta que contiene las imágenes generadas con Gephi a partir de los grafos inducidos por Dijkstra. Se puede visualizar el peso total del camino de mínimo peso de cada uno de los nodos hacia el nodo origen, además de los pesos de cada arista.
