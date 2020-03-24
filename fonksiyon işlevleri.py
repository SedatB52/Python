list=["a",9,4,6,8]

dir(list)#içindeki eleman ile neler yapılabilecegi (  list.fonksiyon  ) 
list=list+[11]
list
del list#listeyi sil
del list[0]# index li elemanı sil
list.append(12)# direk ekleme

list.remove("a")# elemana göre çıkarma

list.insert(0,"bbbb") #indexe göre ekle

list.pop(2)  #indexe göre çıkar

   uzunluk =len(list) #uzunluk bul
   
list.insert(uzunluk,"sedat") 

listeyedek=list.copy()#liste kopyala

list.index("sedat") # eleman indexini ver

list.reverse()#elemanları terse çevir

list.pop(0)

list.sort()# elemanları sıralar

list.clear()# liste için boşalt



ad="sedat"
ad.upper()#string içindeki harfleri büyültür

ad.lower()#string içindeki harfleri küçültür

ad.islower()#küçük mü diye bakar hepsi küçükse true 1 verir

ad.isupper()#buyuk mü diye bakar hepsi büyükse true 1 verir
    
ad.replace("e","a") #harflere yeni deger atar

ad.strip("s") #kesme yapar hiçbişi tanımlanmazsa bas ve sondaki boşlukları keser





#   ^^^^  tuple  ^^^^  (listeler ile aynı tek farkı değiştirelemez)

t= ("a",3,1.4,[1,2,3])

tupnot=("sedat")# bu str olur

tupis=("sedat",) # bu tuple olur (sona virgül gerek)

t[1]
t[1:3]# erişmeler liste ile aynı

t[2]=99 # hata verir atama yapılmaz





#             Dictionary (Sözlük)


 #                  ----------------------> dic = {keyword : item }


sozluk={"s":"sedat"  ,  "v":[10,20,"vedat"]  ,  "f": 20  ,  21 :"asd"} #sözlük oluşturma
len(sozluk)

sozluk[21]="dsssss"
q= sozluk[21]

sozluk


sozlukic={"a":{"h":10,"j":20,"k":30}, #iç içe sözlükler 
          
          "b":{"h":10,"j":20,"k":30},
          
          "c":{"h":10,"j":20,"k":30}}


sozlukic["a"]["k"]

sozluk["ist"]="istanbul" # eleman ekleme

sozluk["s"]="SEDAT B"  # eleman değiştirme veya atama






