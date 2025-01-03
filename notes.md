# Notes from freeCodeCamp

## Self
Argumento self torna um metodo instanciavel
```{python}
class Board:
	def spam(self):
		pass
		
obj = Board()
obj.spam() # apenas porque spam tem self.
```
## `__init__`

O método `__ini__` é um método especial que permite instanciar o objeto para um estado customizado.
Quando uma classe é implementada o método `__init__` é automaticamente executado antes da instancialização da classe.
```{python}
class Board:
	def __init__(self):
        pass

```

## Walrus operator `:=`

The `:=` operator gives you the ability to assign variables in the middle of an expression. The syntax is: `name := val`, where `name` is the variable name and `val` is the variable value.

This construct is formally named assignment expressions, while the `:=`operator is commonly referred to as the walrus operator.

```{python}
def solver(self):
        if(next_empty := self.find_empty_cell()) is None:
                return True
        for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                        return True
                self.board[row][col] = 0
        return False
            
```
## `__str__`
The `__str__` method is a special method that is called under the hood when the object is printed using the `print()` function, or converted into a string using the `str()` function.
