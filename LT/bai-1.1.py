# Viet chuong trinh so tu 2000 3200 chia het cho 7 khong la boi cua nam in tong va list so
s = 0
f= []
for i in range(2000,3201):
    if (i%7 == 0 and i% 5 !=0):
        f.append(str(i))
        s = s +i
print(','.join(f))
print(s)
