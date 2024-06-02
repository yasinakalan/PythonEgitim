# Bool cebirine (0-False, 1-True) göre işlem yapılacak.

# and(ve), or(veya), not(değil) mantık operatörleridir.

a = 3
b = 2
c = 3

islem_or = a == b or a == c
islem_and = a == b and a == c
islem_not = not(a == b)

islem_coklu_or = (a == b or a == c) or (a == b and a == c)
islem_coklu_and = (a == b or a == c) or (a == b and a == c)
islem_coklu_not_or = not(a == b or a == c)
islem_coklu_not_and = not(a == b and a == c)

print("or: ", islem_or)
print("and: ", islem_and)
print("not: ", islem_not)

print("islem_coklu_or: ", islem_coklu_or)
print("islem_coklu_and: ", islem_coklu_and)
print("islem_coklu_not_or: ", islem_coklu_not_or)
print("islem_coklu_not_and: ", islem_coklu_not_and)