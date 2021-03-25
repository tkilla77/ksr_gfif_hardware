def binaer_zu_dezimal(b):
    d = 0
    n = len(b)
    for i in range(n):
        d += int(b[n-i-1])*2**i
    return d

print(binaer_zu_dezimal("1000011"))
print(binaer_zu_dezimal("100010001000"))
print(binaer_zu_dezimal("11111111"))

print(binaer_zu_dezimal("1010"))
print(binaer_zu_dezimal("110100"))
print(binaer_zu_dezimal("100111"))
