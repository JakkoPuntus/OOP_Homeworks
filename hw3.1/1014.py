def find_divisors(number):
    divisors = []
    for i in range(9, 1, -1):
        while number % i == 0:
            divisors.append(str(i))
            number //= i
    return divisors if number == 1 else None

number = int(input())


if number == 0:
    print(10)
elif number == 1:
    print(1)
else:
    divisors = find_divisors(number)
    if divisors is not None:
        print("".join(divisors[::-1]))
    else:
        print(-1)
