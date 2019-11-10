import random
import string
from collections import defaultdict

n = 100
val_str = ''.join([random.choice(string.ascii_lowercase) for i in range(n)])
# print(val_str)
d = defaultdict(int)
print(d)
for key in val_str:
    d[key] += 1
print(d)