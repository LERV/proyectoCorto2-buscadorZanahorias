<h1>Proyecto Corto#2-3 - Buscador de Zanahorias</h1>
<h2>IC-6200 Inteligencia Artificial</h2>
<h2>Integrantes:</h2>
<ul>
<li>Brayan Fajardo Alvarado - 201157035
<li>David Gómez Vargas - 2015028430
<li>Luis Edward Rodríguez Varela - 2014082498
</ul>


<h3>I Semestre 2018</h3>

<h1></h1>

---

<h2>1. Introducción </h2>

<h2>2. Descripción del Problema</h2>

<p>En particular, se pide a los estudiantes procesar tableros rectangulares representados como archivos de texto que contendrán un conejo y múltiples zanahorias.</p>

<p> El objetivo primario de cada corrida de programa será que el conejo encuentre una cierta cantidad de zanahorias.</p>

<p> Tanto para el algoritmo A* como para el algoritmo genético, se definen ciertos requerimientos que se verán ampliamente en cada sección de los algoritmos</p>

<h2>3. Algoritmo A*</h2>

<p> Este algoritmo es una modificación del algoritmo Dijkstra, el cual posee la variante de tener una función heurítica de costo que permite la distancia más corta para llegar a un punto. </p>

<p> Algunos puntos clave acerca del funcionamiento del algoritmo son: </p>

<ul>
<li> Se debe mover el conejo un paso a la vez.
<li> El conejo se puede mover hacia arriba, abajo, izquierda o derecha únicamente.
<li> El conejo posee una distancia de visión según se establezca en el programa.
<li> Se posee un acumulado de pasos o distancia recorrida.
<li> El conejo recolecta una cantidad predefinida de zanahorias, no necesariamente todas las que hayan en el campo.
</ul>

<p>  </p>

<h3>3.1. Diseño del algoritmo</h3>
El diseño del algoritmo posee los siguientes componentes:
<ul>
<li> **Función heurística _(hx)_ **: Es una función que define un valor heurístico óptimo, el cual define un costo real para alcanzar el objetivo.
<li> **Función de costo _g(x)_**: Es el costo o peso que hay para llegar a un cierto nodo o posición. Para este algoritmo, el costo es
<li> **Función de valor _f(x)_**: Es la suma de _g(x)_ con _h(x)_, que permite escoger a cual nodo acceder para obtener la ruta más corta para llegar a un punto.
</ul>

<h4>3.1.1. Diseño de función heurística _(hx)_ </h4>
<p> La función heurística es un valor que se signa a cada elemento o nodo en una matriz, es decir, la estructura que define la ubicación de las zanahorias y del conejo en el campo.</p>

<p> </p>


<h4> </h4>


<h4> </h4>
<h4> </h4>
<h4> </h4>

<h3>3.2. Pruebas y análisis del algoritmo  </h3>

<h2>4. Algoritmo Genético</h2>

<h3>4.1. Diseño del algoritmo  </h3>

<h3>4.2. Pruebas y análisis del algoritmo  </h3>


<h2>5. Conclusiones  </h2>


<h2>6. Apéndice  </h2>


<h2>7. Referencias Bibliográficas  </h2>
