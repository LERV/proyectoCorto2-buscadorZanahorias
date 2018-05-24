# Proyecto Corto#2-3 - Buscador de Zanahorias
## IC-6200 Inteligencia Artificial
## Integrantes:

* Brayan Fajardo Alvarado - 201157035
* David Gómez Vargas - 2015028430
* Luis Edward Rodríguez Varela - 2014082498



### I Semestre 2018</h3>


## 1. Introducción

## 2. Descripción del Problema

En particular, se pide a los estudiantes procesar tableros rectangulares representados como archivos de texto que contendrán un conejo y múltiples zanahorias.

El objetivo primario de cada corrida de programa será que el conejo encuentre una cierta cantidad de zanahorias.

Tanto para el algoritmo A* como para el algoritmo genético, se definen ciertos requerimientos que se verán ampliamente en cada sección de los algoritmos.

## 3. Algoritmo A*

Este algoritmo es una modificación del algoritmo Dijkstra, el cual posee la variante de tener una función heurítica de costo que permite la distancia más corta para llegar a un punto.

Algunos puntos clave acerca del funcionamiento del algoritmo son:


* Se debe mover el conejo un paso a la vez.
* El conejo se puede mover hacia arriba, abajo, izquierda o derecha únicamente.
* El conejo posee una distancia de visión según se establezca en el programa.
* Se posee un acumulado de pasos o distancia recorrida.
* El conejo recolecta una cantidad predefinida de zanahorias, no necesariamente todas las que hayan en el campo.



#### 3.1. Diseño del algoritmo
El diseño del algoritmo posee los siguientes componentes:

* **Función heurística _(hx)_**: Es una función que define un valor heurístico óptimo, el cual define un costo real para alcanzar el objetivo.
* **Función de costo _g(x)_**: Es el costo o peso que hay para llegar a un cierto nodo o posición. Para este algoritmo, el costo es
* **Función de valor _f(x)_**: Es la suma de _g(x)_ con _h(x)_, que permite escoger a cual nodo acceder para obtener la ruta más corta para llegar a un punto.


#### 3.1.1. Diseño de función heurística _(hx)_
La función heurística es un valor que se signa a cada elemento o nodo en una matriz, es decir, la estructura que define la ubicación de las zanahorias y del conejo en el campo.




### 3.2. Pruebas y análisis del algoritmo


## 4. Algoritmo Genético

### 4.1. Diseño del algoritmo

### 4.2. Pruebas y análisis del algoritmo

## 5. Conclusiones


## 6. Apéndice


## 7. Referencias Bibliográficas

1. A* Search - YouTube. (s. f.). Recuperado 23 de mayo de 2018, a partir de https://www.youtube.com/watch?v=6TsL96NAZCo
2. A* search algorithm. (2018, mayo 17). En Wikipedia. Recuperado a partir de https://en.wikipedia.org/w/index.php?title=A*_search_algorithm&oldid=841756385
3. Algoritmo de búsqueda A*. (2018, abril 12). En Wikipedia, la enciclopedia libre. Recuperado a partir de https://es.wikipedia.org/w/index.php?title=Algoritmo_de_b%C3%BAsqueda_A*&oldid=106980195
4. Algoritmo de búsqueda A* (A estrella) - Inteligencia Artificial UD. (s. f.). Recuperado 23 de mayo de 2018, a partir de http://20151578079ia.blogspot.es/1508616746/algoritmo-de-busqueda-a-a-estrella-/
5. A-star Shortest Path Algorithm « Python recipes « ActiveState Code. (s. f.). Recuperado 23 de mayo de 2018, a partir de http://code.activestate.com/recipes/577519-a-star-shortest-path-algorithm/
6. Implementation of A*. (s. f.). Recuperado 23 de mayo de 2018, a partir de https://www.redblobgames.com/pathfinding/a-star/implementation.html
