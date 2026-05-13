def juft_sonlar_generator():
    son = 0
    while True:
        yield son
        son += 2

generator = juft_sonlar_generator()
for _ in range(10):
    print(next(generator))
```

```python
def juft_sonlar_generator():
    son = 0
    while True:
        yield son
        son += 2

generator = juft_sonlar_generator()
for i in range(10):
    print(next(generator))
