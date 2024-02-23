fizzbuzz = {"Fizz": 3, "Buzz": 5, "Whiz": 7, "Bang": 11}

for i in range(1, 101):
  output = ""
  for key, value in fizzbuzz.items():
    if i % value == 0:
      output += key
  print(output or i)
