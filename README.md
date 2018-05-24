# Proyecto Corto#2-3 - Buscador de Zanahorias
## IC-6200 Inteligencia Artificial
## Integrantes:

* Brayan Fajardo Alvarado - 201157035
* David Gómez Vargas - 2015028430
* Luis Edward Rodríguez Varela - 2014082498



### I Semestre 2018</h3>


## 1. Introducción

## 2. Descripción del Problema

Se procesarán tableros rectangulares representados como archivos de texto que contendrán un conejo y múltiples zanahorias.

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
La función heurística es un valor que se asigna a cada elemento o nodo en una matriz, es decir, la estructura que define la ubicación de las zanahorias y del conejo en el campo.




### 3.2. Pruebas y análisis del algoritmo


## 4. Algoritmo Genético

Este tipo de algorimos se encargan de realizar búsquedas por medio de mecanismos de selección natural y génetica. En general estos algorimos funcionan creando un conjunto de individuos que representan las posibles soluciones y se involucran en un proceso semi-aleatorio de cruce para obtener nuevas posibles soluciónes al problema, el resultado del cruce de todos los individuos se denomina generación.

Para dar variabilidad a los individuos se les puede realizar un cambio en la estructura denominado mutación, esto sucede para intentar obtener una nueva posible solución al problema. Todos los individuos de una generación son validados con una prueba de aptitud para verificar si son una solución al problema o están cerca de serlo.

Las características principales de estos algorimos son:

* En cada ejecución se encontraran soluciones distintas, se consideran estocásticos.
* Se optienen multiples soluciones a un problema y se verifica cúal es la mejor.
* Son algoritmos que exploran una gran cantidad de soluciones en poco tiempo.
* La convergencia del algoritmo es poco sensible al punto inicial.
* Resultan menos afectados por los máximos locales que las técnicas tradicionales.
* Pueden tardar mucho en converger o no converger en absoluto, también es posible que converge rápido.


### 4.1. Diseño del algoritmo
El algoritmo empieza con un poco de trabajo de preparación para la parte genética, primero se cuentan los elementos que hay inicialmente en el tablero y se busca la posición inicial del conejo, con estos datos se crea la población inicial que son copias del tablero leído en la entrada.

El ciclo de vida del algoritmo en sí, consiste en lo siguiente:

* Se ordenan los individuos de menor a mayor con respecto a la función de validación (Entre menor sea la el resultado de la función mejor solución es el individuo).
* Se cruzan los individuos partiendo las columnas a la mitad y con las siguientes políticas de cruce (Según el parámetro dado):
  - Política de cruce "**best**": Se seleccionan la mitad de los individuos que contienen los mejores resultados de la función de validación y se agregan a la nueva generación, además, se cruzan esos mismos individuos ordenados con respecto a la función de validación. Por ejemplo:
    -  El mejor individuo se cruza con el segundo mejor, el tercer mejor individuo con el cuarto mejor...
  - Política de cruce "**inverted**": Se seleccionan la mitad de los individuos que contienen los mejores resultados de la función de validación y se agregan a la nueva generación, además, se cruzan esos mismos individuos, pero en este caso los que obtuvieron mejores resultados con respecto a la función de validación se cruzan con los que tuvieron peores resultados. Por ejemplo:
    -  El mejor individuo se cruza con el peor, el segundo mejor individuo con el segundo peor...
- Por lo tanto la nueva generación contiene los mejores individuos de la generación anterior y los cruces de ellos mismos para intentar converger con resultados parecidos a los obtenidos.
-  Luego cada individuo tienen la posibilidad de ser mutado, dependiendo de la taza de mutación dada como parámetro, esa taza se divide en tres opciones:
  - Agregar direccionador.
  - Modificar direccionador.
  - Eliminar direccionador.
- Por último se calcula la función de validación para cada nuevo individuo con la función que corresponde a la siguiente fórmula:
<blockquote>
<p><strong>h(zanahorias, pasos, direccionadores)</strong> = direccionadores + 10 * (total_zanahorias - zanahorias) + pasos / 4
</blockquote>
* Se verifica si el resultado de la función de validación es el mejor y en el caso que si sea entonces se guarda el resultado.

### 4.2. Pruebas y análisis del algoritmo
Se analizará el resultado para el algoritmo para el siguiente tablero:

Columna 1 | Columna 2 | Columna 3 | Columna 4 | Columna 5 | Columna 6 | Columna 7
-- | --  | --  | --  | --  | -- | --
| | |Z| | |
| | | |Z| |
| |Z| | | |
| | |C| | |
|Z| | | | |

Se empieza con dirección hacia la derecha y se obtienen los siguientes resultados:
* Se ejecutó el algoritmo con 2 tazas de mutación (0.1 y 0.3) y se observa en el gráfico que se obtienen mejores resultados con la taza de de 0.3. El gráfico muestra la cantidad de veces que el algoritmo convergio a un máximo global. Un algoritmo genético debe tener una taza de mutación baja para poder mantener una zona de convergencia fija y no alejarse mutando la mayoria de los individuos. Se concluye que la taza de 0.3 obtiene mejores resultados.
![alt text](images/genetico1.PNG "Resultados del algoritmo genético con diferentes tazas de mutación")

* El algoritmo fue ejecutado con las 2 políticas de cruce explicadas anteriormente (best e inverted) y se observa en el gráfico que se obtienen mejores resultados con la política que cruza los mejores entre sí porque converge en más ocasiones a un máximo global. Para la política de cruce inverted se consiguió la misma cantidad de máximos globales y de máximos locales. Se concluye que la política de cruce best obtiene mejores resultados.
![alt text](images/genetico2.PNG "Resultados del algoritmo genético con diferentes políticas de cruce")


* El último gráfico muestra la frecuencia de convergencia en las generaciónes. Se observa como en la generación 76 converge en 3 ocasiones mientras en generaciones cercanas se logra una frecuencia convergencia de 2 y en el resto 1. Se visualiza una semi-campana de Gauss en el histograma que puede hacerse más notable con más ejecuciones, ya que solo se ejecutarón 40 para este análisis.
![alt text](images/genetico3.PNG "Resultados del algoritmo genético con frecuencias de convergencia por generación")


## 5. Conclusiones


## 6. Apéndice


## 7. Referencias Bibliográficas

1. A* Search - YouTube. (s. f.). Recuperado 23 de mayo de 2018, a partir de https://www.youtube.com/watch?v=6TsL96NAZCo
2. A* search algorithm. (2018, mayo 17). En Wikipedia. Recuperado a partir de https://en.wikipedia.org/w/index.php?title=A*_search_algorithm&oldid=841756385
3. Algoritmo de búsqueda A*. (2018, abril 12). En Wikipedia, la enciclopedia libre. Recuperado a partir de https://es.wikipedia.org/w/index.php?title=Algoritmo_de_b%C3%BAsqueda_A*&oldid=106980195
4. Algoritmo de búsqueda A* (A estrella) - Inteligencia Artificial UD. (s. f.). Recuperado 23 de mayo de 2018, a partir de http://20151578079ia.blogspot.es/1508616746/algoritmo-de-busqueda-a-a-estrella-/
5. A-star Shortest Path Algorithm « Python recipes « ActiveState Code. (s. f.). Recuperado 23 de mayo de 2018, a partir de http://code.activestate.com/recipes/577519-a-star-shortest-path-algorithm/
6. Implementation of A*. (s. f.). Recuperado 23 de mayo de 2018, a partir de https://www.redblobgames.com/pathfinding/a-star/implementation.html
