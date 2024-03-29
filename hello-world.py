
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga
 #kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar
 #ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda 
 #bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []


for n in range(5):

    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


for mahsulot in savat:

    if mahsulot in mahsulotlar:

        print(f"Do'konimizda {mahsulot} bor")

    else:

        print(f"Do'konimizda {mahsulot} yo'q")