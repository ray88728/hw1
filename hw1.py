# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061147.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
#target_data={'C0A880':'PRESS','C0F9A0':'PRESS','C0G640':'PRESS','C0R190':'PRESS','C0X260':'PRESS'}
Press = 0
time = 0
#for i in range(len(data)):
#   print(i)
#   if data[i]['PRESS']=='-99.000' or data[i]['PRESS']=='-999.000':
#      del data[i] 

res = [i for i in data if not ((i['PRES'] == '-99.000')|(i['PRES'] == '-999.000'))] 
#print(res)
#for i in range(len(data)):
#   print(data[i]['station_id'])
#print(data[11])

#for i in range(len(data)):
##   if data[i]['station_id']=='C0A880':
#      time_C0A880 = 1
#      Press = Press + float(data[i]['PRESS'])
#target_data['C0A880']=Press     
#=======================================
target_data =[]
target_C0A880 = list(filter(lambda item: item['station_id'] == 'C0A880', res))
target_C0F9A0 = list(filter(lambda item: item['station_id'] == 'C0F9A0', res))
target_C0G640 = list(filter(lambda item: item['station_id'] == 'C0G640', res))
target_C0R190 = list(filter(lambda item: item['station_id'] == 'C0R190', res))   
target_C0X260 = list(filter(lambda item: item['station_id'] == 'C0X260', res))

for i in range(len(target_C0A880)):
   Press = Press + float(target_C0A880[i]['PRES'])
   time = 1
target_data.append('C0A880')
if time == 1:
   target_data.append(Press/len(target_C0A880))
else:
   target_data.append('\'None\'')

time = 0
Press = 0

for i in range(len(target_C0F9A0)):
   Press = Press + float(target_C0F9A0[i]['PRES'])
   time = 1
target_data.append('C0F9A0')
if time == 1:
   target_data.append(Press/len(target_C0F9A0))
else:
   target_data.append('\'None\'')

time = 0
Press = 0

for i in range(len(target_C0G640)):
   Press = Press + float(target_C0G640[i]['PRES'])
   time = 1
target_data.append('C0G640')
if time == 1:
   target_data.append(Press/len(target_C0G640))
else:
   target_data.append('\'None\'')

time = 0
Press = 0

for i in range(len(target_C0R190)):
   Press = Press + float(target_C0R190[i]['PRES'])
   time = 1
target_data.append('C0R190')
if time == 1:
   target_data.append(Press/len(target_C0R190))
else:
   target_data.append('\'None\'')

time = 0
Press = 0

for i in range(len(target_C0X260)):
   Press = Press + float(target_C0X260[i]['PRES'])
   time = 1
target_data.append('C0X260')
if time == 1:
   target_data.append(Press/len(target_C0X260))
else:
   target_data.append('\'None\'')

# Part. 4
#=======================================
# Print result
#print(target_C0A880[1])
#print(target_C0F9A0)
#print(target_C0G640)
#print(target_C0R190)
#print(target_C0X260)
#print(target_data[1])
#print('[')
#for i in range(len(target_data)):
#   print('[')
#   print(target_data[i])
#   print(']')
print('[', end='')
for i in range(len(target_data)):
   if i % 2 == 0: 
      print('[',end='')
      print('\'',end='')
      print(target_data[i],end='')
      print('\'',end='')
      print(',',end='')
   else:
      print(target_data[i],end='')
      print(']',end='')
      if i != len(target_data)-1:
         print(',',end='')
print(']')
#print(']')
#========================================