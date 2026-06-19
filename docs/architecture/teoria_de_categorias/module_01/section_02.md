# Funtores, Applicativos y Mónadas



Estos temas son particulares de lenguajes funcionales. Aunque no son exactamente de python podemos hacer simulaciones usando clases y tipos genéricos.

Estos conceptos provienen de la **Teoría de Categorías** y son fundamentales en programación funcional para manejar **efectos** (como `None`, errores, IO, listas, etc.) de forma **composable** y **segura**.

## Functor ("Mapeable")

Un **Functor** es un tipo que puede **mapear una función sobre sus valores internos**, preservando la estructura.

> En palabras simples: `fmap(f, Container(x)) = Container(f(x))`

### Ejemplo en Python: `Maybe` (equivalente a `Optional` o `None`)

```python
from typing import Generic, TypeVar, Callable, Optional
from abc import ABC, abstractmethod

A = TypeVar('A')
B = TypeVar('B')

classFunctor(Generic[A], ABC):
    @abstractmethod
defmap(self, f: Callable[[A], B]) -> 'Functor[B]':
        pass

classMaybe(Functor[A]):
    def__init__(self, value: Optional[A]):
        self.value = value

    defmap(self, f: Callable[[A], B]) -> 'Maybe[B]':
        ifself.value isNone:
            returnMaybe(None)
        returnMaybe(f(self.value))

    def__repr__(self):
        returnf"Maybe({self.value})"
```

### Uso:

```python
# Función que puede fallar
defsafe_div(x: float, y: float) -> Maybe[float]:
    returnMaybe(None) if y == 0 elseMaybe(x /-equally y)

# Ejemplo con map
result = (
    Maybe(10)
    .map(lambda x: x * 2)        # → Maybe(20)
    .map(lambda x: safe_div(x, 4))  # → aplica safe_div → Maybe(5.0)
    .map(lambda x: x + 1)        # → Maybe(6.0)
)

print(result)  # Maybe(6.0)
```

> Si en algún punto hay `None`, **todo el pipeline se "corta"** y devuelve `Maybe(None)`.

---

## 2. **Applicative Functor** – "Aplica funciones dentro del contexto"

Un **Applicative** permite **aplicar funciones que están dentro del contexto** a valores también en contexto.

> Es como `map`, pero la **función también puede estar "envuelta"**.

### Extensión de `Maybe` a Applicative

```python
classApplicative(Functor[A], ABC):
    @abstractmethod
defap(self, fab: 'Applicative[Callable[[A], B]]') -> 'Applicative[B]':
        pass

    @classmethod
    @abstractmethod
    defpure(cls, value: A) -> 'Applicative[A]':
        pass

classMaybe(Applicative[A]):
    def__init__(self, value: Optional[A]):
        self.value = value

    defmap(self, f: Callable[[A], B]) -> 'Maybe[B]':
        ifself.value isNone:
            returnMaybe(None)
        returnMaybe(f(self.value))

    defap(self, fab: 'Maybe[Callable[[A], B]]') -> 'Maybe[B]':
        iffab.value isNone orself.value isNone:
            returnMaybe(None)
        returnMaybe(fab.value(self.value))

    @classmethod
    defpure(cls, value: A) -> 'Maybe[A]':
        returnMaybe(value)

    def__repr__(self):
        returnf"Maybe({self.value})"
```

### Uso con funciones envueltas:

```python
# Funciones que podrían fallar
add = lambda x: lambda y: x + y
mul = lambda x: lambda y: x * y

# Aplicamos funciones "curried" dentro de Maybe
result = (
    Maybe.pure(add)          # Maybe(<función add>)
    .ap(Maybe(5))            # → Maybe(<función parcial: add(5)>)
    .ap(Maybe(3))            # → Maybe(8)
)

print(result)  # Maybe(8)
```

> Esto es útil para combinar operaciones que pueden fallar **sin anidar `if`**.

---

## 3. **Monad** – "Encadenamiento plano"

Una **Mónada** permite **encadenar operaciones** que devuelven valores envueltos, **aplanando** el resultado.

> `bind(m, f) = f(x)` si `m = Just(x)`, y `f` devuelve otra mónada.

### Firma clave:
```python
bind :: m a → (a → m b) → m b
```

En Python: `flat_map` o `>>=`

### `Maybe` como Mónada

```python
classMonad(Maybe[A]):
    defbind(self, f: Callable[[A], 'Monad[B]']) -> 'Monad[B]':
        ifself.value isNone:
            returnMaybe(None)
        returnf(self.value)

# Alias para claridad
defbind(m: Maybe[A], f: Callable[[A], Maybe[B]]) -> Maybe[B]:
    return m.bind(f)
```

### Uso con `bind` (encadenamiento plano)

```python
defsafe_sqrt(x: float) -> Maybe[float]:
    returnMaybe(None) if x < 0 elseMaybe(x ** 0.5)

defsafe_reciprocal(x: float) -> Maybe[float]:
    returnMaybe(None) if x == 0 elseMaybe(1 / x)

# Encadenamiento con bind (sin anidar)
result = (
    Maybe(16)
    .bind(safe_sqrt)        # → Maybe(4.0)
    .bind(lambda x: Maybe(x + 1))  # → Maybe(5.0)
    .bind(safe_reciprocal)  # → Maybe(0.2)
)

print(result)  # Maybe(0.2)
```

> ¡No hay anidamiento! Cada paso devuelve un `Maybe`, y `bind` lo "aplana".

---

## Ejemplo completo: Pipeline con Mónadas

```python
defparse_int(s: str) -> Maybe[int]:
    try:
        returnMaybe(int(s))
    exceptValueError:
        returnMaybe(None)

pipeline = (
    Maybe("10")
    .bind(parse_int)           # → Maybe(10)
    .bind(lambda x: Maybe(x * 2))     # → Maybe(20)
    .bind(lambda x: safe_div(x, 5))   # → Maybe(4.0)
    .bind(lambda x: Maybe(round(x)))  # → Maybe(4)
)

print(pipeline)  # Maybe(4)
```

---

## Resumen: Diferencias clave

| Concepto       | Qué permite                              | Ejemplo en `Maybe` |
|----------------|------------------------------------------|--------------------|
| **Functor**    | `map(f)` → aplica `f` al valor interno   | `m.map(double)` |
| **Applicative**| `ap(f)` → aplica función envuelta        | `f.ap(m1).ap(m2)` |
| **Monad**      | `bind(f)` → encadena funciones que devuelven contexto | `m.bind(f).bind(g)` |

---

## Otros ejemplos de Mónadas en Python

| Mónada       | Tipo en Python         | `bind` (flat_map) |
|--------------|------------------------|-------------------|
| `list`       | `[a]`                  | `itertools.chain` |
| `Optional`   | `Optional[a]`          | `.and_then()` |
| `IO`         | función → valor        | composición |
| `Either`     | `Left\|Right`          | manejo de errores |

### Ejemplo con `list` como Mónada:

```python
from typing import List

defbind_list(xs: List[A], f: Callable[[A], List[B]]) -> List[B]:
    return [y for x in xs for y in f(x)]

# Duplicar y luego generar pares
result = bind_list([1, 2, 3], lambda x: [x, x*10])
print(result)  # [1, 10, 2, 20, 3, 30]
```

---

## Conclusión

- **Functors**: `map`
- **Applicatives**: `map` + `pure` + `ap` → combinan efectos
- **Monads**: `bind` → encadenan efectos **sin anidamiento**

En Python, aunque no hay soporte nativo, puedes **implementarlos con clases** y usarlos para:
- Manejo seguro de `None`
- Pipelines de validación
- Procesamiento de datos con errores
- Programación funcional limpia

¿Quieres que hagamos una implementación de `Either` (para errores) o `IO` como mónada?