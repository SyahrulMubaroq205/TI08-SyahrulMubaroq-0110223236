a=[1,2,3,4,5]
b=["12345","arul",19,172,5]
b.append("laki-laki")
b.insert(2,"Depok")
b.pop(1)
print(a[1:4])
print(b)

c= a + b
print(c)
print(b)

nilai1 = input ("masukan nilai pertama")
nilai2 = input ("masukan nilai kedua")
jumlah = nilai1 + nilai2

print(jumlah)


cuaca= input ("apakah cuaca pada hari ini")
match cuaca:
    case "Hujan":
        print("berangkat kuliah memakai jas ujan")
    case "badai":
        print("tidak berangkat kuliah")
    case "panas":
        print("berangkat kuliah pakai mobil")
    case _:
        print("tetap berangkat kuliah")
        