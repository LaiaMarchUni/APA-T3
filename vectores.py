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