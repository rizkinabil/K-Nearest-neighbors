import pandas
import math

dataset = pandas.read_excel('Dataset Tugas 3.xls')

#fungsi normalisasi untuk data training
def normalisasi():
  data = []
  for i in range(0, len(dataset)):
    data.append([
      list_namaMobil[i], (list_ukuran[i] - list_ukuran.min()) / (list_ukuran.max() - list_ukuran.min()),
      (list_kenyamanan[i] - list_kenyamanan.min()) / (list_kenyamanan.max() - list_kenyamanan.min()),
      (list_irit[i] - list_irit.min()) / (list_irit.max() - list_irit.min()),
      (list_kecepatan[i] - list_kecepatan.min()) / (list_kecepatan.max() - list_kecepatan.min()),
      (list_harga[i] - list_harga.min()) / (list_harga.max() - list_harga.min())
    ])

  return data
  

#euclidean distance
def euclidean(data, data_in) :
  result = []
  i = 0
  while(i<len(data)):
    euclidean = (math.pow(data[i][1] - data_in[0],2) + math.pow(data[i][2] - data_in[1],2) + math.pow(data[i][3] - data_in[2],2) + math.pow(data[i][4] - data_in[3],2) + math.pow(data[i][5] - data_in[4],2))
    euclidean = math.pow(euclidean, 0.5)
    result.append(euclidean)
    i = i + 1

  return result

#manhattan distance
def manhattan(data, data_in):

  result = []
  i = 0
  while(i<len(data)):
    man = abs((data[i][1] - data_in[0]) + (data[i][2] - data_in[1]) + (data[i][3] - data_in[2]) + (data[i][4] - data_in[3]) + (data[i][5] - data_in[4]) )
    result.append(man)
    i += 1

  return result

#minkowski distance
def minkowski(data,data_in):
  h = 3
  result = []
  i = 0
  while(i<len(data)):
    min = abs(math.pow(data[i][1] - data_in[0],h) + math.pow(data[i][2] - data_in[1],h) + math.pow(data[i][3] - data_in[2],h) + math.pow(data[i][4] - data_in[3],h) + math.pow(data[i][5] - data_in[4],h))
    min = math.pow(min,0.3)
    min = float(min)
    result.append(min)
    i += 1

  return result

#supremum distance
def supremum(data, data_in):
  result = []
  i = 0
  while(i<len(data)):
    sup = abs((data[i][1] - data_in[0]) + (data[i][2] - data_in[1]) + (data[i][3] - data_in[2]) + (data[i][4] - data_in[3]) + (data[i][5] - data_in[4]))
    sup = int(sup)
    result.append(sup)
    i += 1
    
  return result

def col_result(dataset, result):
  for i in range(0, len(dataset)):
    dataset[i].append(result[i])
  return dataset

def col_result1(dataset1, result):
  for i in range(0, len(dataset1)):
    dataset1[i].append(result[i])
  return dataset1

def col_result2(dataset2, result):
  for i in range(0, len(dataset2)):
    dataset2[i].append(result[i])
  return dataset2

def col_result3(dataset3, result):
  for i in range(0, len(dataset3)):
    dataset3[i].append(result[i])
  return dataset3  

def sorting(dataset):
  list_sorting = []
  sort = sorted(dataset, key=lambda x:x[6])
  for i in range(3):
    list_sorting.append(sort[i])
  
  return list_sorting

def sorting1(dataset1):
  list_sorting1 = []
  sort = sorted(dataset1, key=lambda x:x[7])
  for i in range(3):
    list_sorting1.append(sort[i])
  
  return list_sorting1

def sorting2(dataset2):
  list_sorting2 = []
  sort = sorted(dataset2, key=lambda x:x[8])
  for i in range(3):
    list_sorting2.append(sort[i])
  
  return list_sorting2

def sorting3(dataset3):
  list_sorting3 = []
  sort = sorted(dataset3, key=lambda x:x[9])
  for i in range(3):
    list_sorting3.append(sort[i])
  
  return list_sorting3

def output(final):
  hasil = sorting(final)
  namamobil = [x[0] for x in hasil]
  jarak = [x[6] for x in hasil]

  rekomendasi = {'Nama Mobil': namamobil, 'Nilai Jarak' : jarak}
  rek = pandas.DataFrame(rekomendasi, columns=['Nama Mobil','Nilai Jarak'])
  
  return rek
 

def output1(final1):
  hasil = sorting1(final1)
  namamobil = [x[0] for x in hasil]
  jarak = [x[7] for x in hasil]

  rekomendasi = {'Nama Mobil': namamobil, 'Nilai Jarak' : jarak}
  rek1 = pandas.DataFrame(rekomendasi, columns=['Nama Mobil','Nilai Jarak'])

  return rek1
  
def output2(final2):
  hasil = sorting1(final2)
  namamobil = [x[0] for x in hasil]
  jarak = [x[8] for x in hasil]

  rekomendasi = {'Nama Mobil': namamobil, 'Nilai Jarak' : jarak}
  rek2 = pandas.DataFrame(rekomendasi, columns=['Nama Mobil','Nilai Jarak'])

  return rek2

def output3(final3):
  hasil = sorting1(final3)
  namamobil = [x[0] for x in hasil]
  jarak = [x[9] for x in hasil]

  rekomendasi = {'Nama Mobil': namamobil, 'Nilai Jarak' : jarak}
  rek3 = pandas.DataFrame(rekomendasi, columns=['Nama Mobil','Nilai Jarak'])

  return rek3

list_namaMobil = dataset['Nama Mobil']
list_ukuran = dataset['Ukuran']
list_kenyamanan = dataset['Kenyamanan']
list_irit = dataset['Irit']
list_kecepatan = dataset['Kecepatan']
list_harga = dataset['Harga (Ratus Juta)']

data_in = [] #list untuk data uji


in_ukuran = int(input("masukkan skala ukuran : "))
in_kenyamanan = int(input("masukkan skala kenyamanan : "))
in_irit = int(input("masukkan skala irit : "))
in_kecepatan = int(input("masukkan skala kecepatan : "))
in_harga = int(input("masukkan skala harga : "))

#proses normalisai min max scaler untuk data uji
n_ukuran = (in_ukuran - list_ukuran.min()) / (list_ukuran.max() - list_ukuran.min())
n_kenyamanan = (in_kenyamanan - list_kenyamanan.min()) / (list_kenyamanan.max() - list_kenyamanan.min())
n_irit = (in_irit - list_irit.min()) / (list_irit.max() - list_irit.min())
n_kecepatan = (in_kecepatan - list_kecepatan.min()) / (list_kecepatan.max() - list_kecepatan.min())
n_harga = (in_harga - list_harga.min()) / (list_harga.max() - list_harga.min())

data_in.append(n_ukuran)
data_in.append(n_kenyamanan)
data_in.append(n_irit)
data_in.append(n_kecepatan)
data_in.append(n_harga)

dataLatih = normalisasi()
euc = euclidean(dataLatih, data_in)
man = manhattan(dataLatih, data_in)
min = minkowski(dataLatih, data_in)
sup = supremum(dataLatih, data_in)

hasil_euc = col_result(dataLatih, euc)
final_euc = sorting(hasil_euc)
h1 = output(final_euc)
print("Daftar mobil terbaik Euclidean Distance :\n",h1)
h1.to_excel('Mobil-Euc.xls')

hasil_man = col_result1(dataLatih, man)
final_man = sorting1(hasil_man)
h2 = output1(final_man)
print("Daftar mobil terbaik Manhattan Distance :\n",h2)
h2.to_excel('Mobil-Man.xls')

hasil_min = col_result2(dataLatih, min)
final_min = sorting2(hasil_min)
h3 = output2(final_min)
print("Daftar mobil terbaik Minkowski Distance :\n",h3)
h3.to_excel('Mobil-Min.xls')

hasil_sup = col_result3(dataLatih, sup)
final_sup = sorting3(hasil_sup)
h4 = output3(final_sup)
print("Daftar mobil terbaik Supremum Distance :\n",h4)
h4.to_excel('Mobil-Sup.xls')





