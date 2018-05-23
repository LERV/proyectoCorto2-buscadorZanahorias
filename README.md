# Proyecto Corto#2-3 - Buscador de Zanahorias
## IC-6200 Inteligencia Artificial
## Integrantes:

* Brayan Fajardo Alvarado - 201157035
* David Gómez Vargas - 2015028430
* Luis Edward Rodríguez Varela - 2014082498



### I Semestre 2018</h3>

<h1></h1>

---

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



#### 3.1. Diseño del algoritmo</h3>
El diseño del algoritmo posee los siguientes componentes:

* **Función heurística _(hx)_ **: Es una función que define un valor heurístico óptimo, el cual define un costo real para alcanzar el objetivo.
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
