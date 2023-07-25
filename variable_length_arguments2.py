def sum(init_sum, *elements):
    res = init_sum
    for x in elements:
        res = res + x

    return res

print(sum(0,10,20))
print(sum(5,10,15))
