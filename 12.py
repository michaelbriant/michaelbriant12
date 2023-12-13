# elkom 1
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@\n')

list=[]
minta=int(input('berapa rangenya? '))
for i in range(minta):
    i+=1
    list.append(int(input(f'masukan angka ke {i}:')))
print(sorted(list))

# elkom 2
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@\n')

def Binary_search(num,nilai_dicari,kiri,kanan):
    while kiri <= kanan:
        mid = (kiri + kanan)//2
        if nilai_dicari == num[mid]:
            return mid
        elif nilai_dicari > num[mid]:
            kiri = mid + 1
        else:
            kanan = mid - 1
    return -1
num =[]
minta=int(input('berapa rangenya? '))
for i in range(minta):
    i+=1
    num.append(int(input(f'masukan angka ke {i}:')))
print(num)
nilai_dicari = int(input('angka berapa?'))
hasil = Binary_search(num,nilai_dicari,0,len(num)-1)
if hasil != -1:
    print("Angka ditemukan pada index ke " + str(hasil))
else:
    print("Angka tidak ditemukan")

# elkom 3
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@\n')

def bubble_sorted():
    list=[]
    minta=int(input('berapa rangenya? '))
    for i in range(minta):
        i+=1
        list.append(int(input(f'masukan angka ke {i}:')))
    print('list normalnya:',list)
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    print(f'Hasil Bubble Sort = {list}')
bubble_sorted()

# elkom 4
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@\n')

def selection():
    list=[]
    minta=int(input('Berapa kali maunya? '))
    for i in range(minta):
        i+=1
        list.append(int(input(f'Masukan angka ke {i}: ')))
    print (f'list: {list}')
    for i in range(0,len(list)-1):
        p=0
        mini=list[-1]
        for j in range(i,len(list)):
            if list[j]<=mini:
                mini=list[j]
                p=j
        list[i],list[p]=list[p],list[i]
    print(f'list dengan selection: {list}')
selection()