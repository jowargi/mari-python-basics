# def say_hi():
#     print("Hello!")


# say_hi()
# say_hi()
# say_hi()


# def say_hi(from_name, to_name):
#     print(f"{from_name} передает привет {to_name}!")


# say_hi("Витя", "Толе")
# say_hi(to_name="Саше", from_name="Аня")
# say_hi("Саша", to_name="Марго")


# def get_max(a, b):
#     if a > b:
#         return a

#     return b


# result = get_max(1, 2)

# print(result)
# print(get_max(b=7, a=9))
# print(get_max(10, b=10))


# def func():
#     pass

#     # return None


# result = func()

# print(result)


# def func():
#     return  # return None


# result = func()

# print(result)


# def say_phrase(phrase, count=1):
#     print(phrase * count)


# say_phrase("Hello")
# say_phrase("Goodbye", 5)


# def func(a, b, *c, **d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)


# func(1, 2, 3, 4, 5, alex=27, bob=29)


def get_sum(*numbers):
    total = 0

    for num in numbers:  # (1, 2, 3, 4, 5)
        total += num  # total = total + num

    return total


print(get_sum())
print(get_sum(5))
print(get_sum(1, 2, 3, 4, 5))
