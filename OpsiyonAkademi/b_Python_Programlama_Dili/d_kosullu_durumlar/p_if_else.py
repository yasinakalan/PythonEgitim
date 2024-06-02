a = [1,2,3,4,5,6,7,8,9]
b = 6

if not(b in a):
    b *= 2
    print("b_yeni: ", b)

else:
    b *= 0.5
    print("b_yeni: ", b)

print("a_son: ", a)
print("b_son: ", b)



c = 9
d = 5
e = 7

if c > d:
    c += 10
    print("c_yeni: ", c)

else:
    d -= 2
    print("d_yeni: ", d)

print("c_son: ", c)
print("d_son: ", d)

if c > e:
    e += b
    print("e_yeni: ", e)

print("e_son: ", e)



if c > d:
    c += 2
elif c < d:
    d += 2
else:
    e += 2

print("c_en son: ", c)
print("d_en son: ", d)
print("e_en son: ", e)