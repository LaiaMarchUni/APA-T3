# Tercera tarea de APA: Multiplicación de vectores y ortogonalidad

## Nom i cognoms

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Laia March Cervantes

## Aviso Importante

> [!Caution]
>
> 
> El objetivo de esta tarea es programar en Python usando el pardigma de la programación
> orientada a objeto. Es el alumno quien debe realizar esta programación. Existen bibliotecas
> que, si lugar a dudas, lo harán mejor que él, pero su uso está prohibido.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Fecha de entrega: 6 de abril a medianoche

## Clase Vector e implementación de la multiplicación de vectores

El fichero `algebra/vectores.py` incluye la definición de la clase `Vector` con los
métodos desarrollados en clase, que incluyen la construcción, representación y
adición de vectores, entre otros.

Añada a este fichero los métodos siguientes, junto con sus correspondientes
tests unitarios.

### Multiplicación de los elementos de dos vectores (Hadamard) o de un vector por un escalar

- Sobrecargue el operador asterisco (`*`, correspondiente a los métodos `__mul__()`,
  `__rmul__()`, etc.) para implementar el producto de Hadamard (vector formado por
  la multiplicación elemento a elemento de dos vectores) o la multiplicación de un
  vector por un escalar.

  - La prueba unitaria consistirá en comprobar que, dados `v1 = Vector([1, 2, 3])` y
    `v2 = Vector([4, 5, 6])`, la multiplicación de `v1` por `2` es `Vector([2, 4, 6])`,
    y el producto de Hadamard de `v1` por `v2` es `Vector([4, 10, 18])`.

- Sobrecargue el operador arroba (`@`, multiplicación matricial, correspondiente a los
  métodos `__matmul__()`, `__rmatmul__()`, etc.) para implementar el producto escalar
  de dos vectores.

  - La prueba unitaria consistirá en comprobar que el producto escalar de los dos
    vectores `v1` y `v2` del apartado anterior es igual a `32`.

### Obtención de las componentes normal y paralela de un vector respecto a otro

Dados dos vectores $v_1$ y $v_2$, es posible descomponer $v_1$ en dos componentes,
$v_1 = v_1^\parallel + v_1^\perp$ tales que $v_1^\parallel$ es tangencial (paralela) a
$v_2$, y $v_1^\perp$ es normal (perpendicular) a $v_2$.

> Se puede demostrar:
>
> - $v_1^\parallel = \frac{v_1\cdot v_2}{\left|v_2\right|^2} v_2$
> - $v_1^\perp = v_1 - v_1^\parallel$

- Sobrecargue el operador doble barra inclinada (`//`, métodos `__floordiv__()`,
  `__rfloordiv__()`, etc.) para que devuelva la componente tangencial $v_1^\parallel$.

- Sobrecargue el operador tanto por ciento (`%`, métodos `__mod__()`, `__rmod__()`, etc.)
  para que devuelva la componente normal $v_1^\perp$.

> Es discutible esta elección de las sobrecargas, dado que extraer la componente
> tangencial no es equivalente a ningún tipo de división. Sin embargo, está
> justificado en el hecho de que su representación matemática es dos barras
> paralelas ($\parallel$), similares a las usadas para la división entera (`//`).
>
> Por otro lado, y de manera *parecida* (aunque no idéntica) al caso de la división
> entera, las dos componentes cumplen: `v1 = v1 // v2 + v1 % v2`, lo cual justifica
> el empleo del tanto por ciento para la componente normal.

- En este caso, las pruebas unitarias consistirán en comprobar que, dados los vectores
  `v1 = Vector([2, 1, 2])` y `v2 = Vector([0.5, 1, 0.5])`, la componente de `v1` paralela
  a `v2` es `Vector([1.0, 2.0, 1.0])`, y la componente perpendicular es `Vector([1.0, -1.0, 1.0])`.

### Entrega

#### Fichero `algebra/vectores.py`

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno
  y los tests unitarios de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido
  de la función, los argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el
  uso de los estándares marcados por PEP-ocho.

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el
fichero `algebra/vectores.py` con la opción *verbosa*, de manera que se muestre el
resultado de la ejecución de los tests unitarios.

<img src="./Test1.png" width="45%"> <img src="./Test2.png" width="45%">

#### Código desarrollado

Inserte a continuación el código de los métodos desarrollados en esta tarea, usando los
comandos necesarios para que se realice el realce sintáctico en Python del mismo (no
vale insertar una imagen o una captura de pantalla, debe hacerse en formato *markdown*).

```python
class Vector:
    """
    Clase que representa un vector matemático y sus operaciones algebraicas.
    Laia March Cervantes

    Tests unitarios:

    >>> v1 = Vector([1, 2, 3])
    >>> v2 = Vector([4, 5, 6])
    >>> v1 * 2
    Vector([2, 4, 6])

    >>> v1 * v2
    Vector([4, 10, 18])
        
    >>> v1 @ v2
    32

    >>> v1 = Vector([2, 1, 2])
    >>> v2 = Vector([0.5, 1, 0.5])
    >>> v1 // v2
    Vector([1.0, 2.0, 1.0])
        
    >>> v1 % v2
    Vector([1.0, -1.0, 1.0])
    """   

    def __init__(self, iterable):
        """
        Constructor de la clase Vector.
        Argumentos:
            iterable: Un objeto iterable (lista, tupla, etc.).
        Salida:
            Instancia de la clase Vector.
        """
        self.vector = [elemento for elemento in iterable]

    def __repr__(self):
        """
        Representación oficial del vector.
        Salida:
            Cadena de texto con formato Vector([...]).
        """
        return "Vector(" + repr(self.vector) + ")"

    def __str__(self):
        """
        Representación visual (bonita) del vector.
        Salida:
            Cadena de texto con los elementos del vector.
        """
        return str(self.vector)

    def __sub__(self, other):
        """
        Resta dos vectores elemento a elemento.
        Argumentos:
            other (Vector): El vector que se resta del actual.
        Salida:
            Vector: Un nuevo vector con el resultado de la resta.
        """
        if isinstance(other, Vector):
            return Vector([a - b for a, b in zip(self.vector, other.vector)])
        return NotImplemented

    def __rsub__(self, other):
        """Resta por la izquierda: other - self"""
        if isinstance(other, Vector):
            return other.__sub__(self)
        return NotImplemented

    def __mul__(self, other):
        """
        Multiplica el vector por un escalar o realiza el producto de Hadamard.
        Argumentos:
            other (int, float, Vector): Escalar o vector por el cual multiplicar.
        Salida:
            Vector: Resultado de la multiplicación.
        """
        if isinstance(other, (int, float)):
            return Vector([a * other for a in self.vector])
        
        elif isinstance(other, Vector):
            return Vector([a * b for a, b in zip(self.vector, other.vector)])

        return NotImplemented
        
    def __rmul__(self, other):
        """Multiplicación por la izquierda (escalar * vector)."""
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        Calcula el producto escalar de dos vectores usando el operador @.
        Argumentos:
            other (Vector): El segundo vector para el producto punto.
        Salida:
            float/int: El valor escalar resultante.
        """
        if isinstance(other, Vector):
            # Usamos a * b porque son elementos numéricos individuales
            return sum(a * b for a, b in zip(self.vector, other.vector))
        
        return NotImplemented

    def __rmatmul__(self, other):
        """Multiplicación matricial por la izquierda."""
        return self.__matmul__(other)

    def __floordiv__(self, other):
        """
        Componente tangencial de self respecto a other (v1 // v2).
        Argumentos:
            other (Vector): Vector sobre el cual se proyecta.
        Salida:
            Vector: Componente paralela.
        """
        if isinstance(other, Vector):
            escalar = (self @ other) / (other @ other)
            return escalar * other
        
        return NotImplemented

    def __rfloordiv__(self, other):
        """Componente tangencial por la izquierda."""
        if isinstance(other, Vector):
            return other.__floordiv__(self)
        return NotImplemented

    def __mod__(self, other):
        """
        Componente normal de self respecto a other (v1 % v2).
        Argumentos:
            other (Vector): Vector de referencia.
        Salida:
            Vector: Componente perpendicular.
        """
        if isinstance(other, Vector):
            return self - (self // other)
        
        return NotImplemented
        
    def __rmod__(self, other):
        """Componente normal por la izquierda."""
        if isinstance(other, Vector):
            return other.__mod__(self)
       
        return NotImplemented

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
````



#### Subida del resultado al repositorio GitHub y *pull-request*

La entrega se formalizará mediante *pull request* al repositorio de la tarea.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y
visualizarse correctamente en el repositorio, incluyendo la imagen con la ejecución de
los tests unitarios y el realce sintáctico del código fuente insertado.
