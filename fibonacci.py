import time

fibonacci = [0,1]
print(f"{fibonacci[0]}\n{fibonacci[1]}")

while True:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    time.sleep(0.1)
    print(number)
