import random


def gen_ran_chr():
    chr_ran = chr(random.randint(0, 127))
    return chr_ran


print(gen_ran_chr())
print(gen_ran_chr())
print(gen_ran_chr())
print(gen_ran_chr())
print(gen_ran_chr())
