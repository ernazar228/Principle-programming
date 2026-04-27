import re

a = "hello world"
pattern = re.compile("hello")

print(bool(pattern.search(a)))
