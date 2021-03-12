
for fizzbuzz in range(100):
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")
        continue
    if fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    if fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(fizzbuzz)
