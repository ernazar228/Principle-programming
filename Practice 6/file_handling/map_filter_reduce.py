numbers = [1, 2, 3, 4]

# map
result = map(lambda x: x * 2, numbers)
print(list(result))

# filter
result = filter(lambda x: x > 2, numbers)
print(list(result))
