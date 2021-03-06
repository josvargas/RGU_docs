#!/usr/bin/env python

import re
import math

roots_1 = []
entries_1 = []
errors_1 = []

with open("tb_1.log") as f:
        content_1 = f.readlines()

for x in content_1:
    roots_1.append(re.search(r'square=x\s*([^\n]+)', x))

for x in content_1:
    entries_1.append(re.search(r'Entrada=x\s*([^\n]+),', x))

for idx,valx in enumerate(roots_1):
	for idy,valy in enumerate(entries_1):		
		if idx==idy:
			if valy!=0:	
			#print('Roots',int(valx.group(1))," Entries",int(valy.group(1))," \n")	
				print('Raices iteradas',float(valx.group(1))/131072,"Calculo con entradas",1/math.sqrt(float(valy.group(1))/131072))
				print('Errores',((float(valx.group(1))/131072 - 1/math.sqrt(float(valy.group(1))/131072))/(float(valx.group(1))/131072))*100)
				errors_1.append(((float(valx.group(1))/131072 - 1/math.sqrt(float(valy.group(1))/131072))/(float(valx.group(1))/131072))*100)		
	
cont_1 = len(errors_1)
accumulator_1 = sum(int(i) for i in errors_1)
total_error_1 = float(accumulator_1)/float(cont_1)
print("Error promedio ",total_error_1) 

roots_2 = []
entries_2 = []
errors_2 = []

with open("tb_2.log") as f:
        content_2 = f.readlines()

for x in content_2:
    roots_2.append(re.search(r'square=x\s*([^\n]+)', x))

for x in content_2:
    entries_2.append(re.search(r'Entrada=x\s*([^\n]+),', x))

for idx,valx in enumerate(roots_2):
	for idy,valy in enumerate(entries_2):		
		if idx==idy:	
			if valy!=0:
				print('Raices iteradas',float(valx.group(1))/131072,"Calculo con entradas",1/math.sqrt(float(valy.group(1))/131072))
				print('Errores',((float(valx.group(1))/131072 - 1/math.sqrt(float(valy.group(1))/131072))/(float(valx.group(1))/131072))*100)
				errors_2.append(((float(valx.group(1))/131072 - 1/math.sqrt(float(valy.group(1))/131072))/(float(valx.group(1))/131072))*100)		
	
cont_2 = len(errors_2)
accumulator_2 = sum(int(i) for i in errors_2)
total_error_2 = float(accumulator_2)/float(cont_2)
print("Error promedio ",total_error_2) 

roots_3 = []
entries_3 = []
errors_3 = []

with open("tb_3.log") as f:
        content_3 = f.readlines()

for x in content_3:
    roots_3.append(re.search(r'square=x\s*([^\n]+)', x))

for x in content_3:
    entries_3.append(re.search(r'Entrada=x\s*([^\n]+),', x))

for idx,valx in enumerate(roots_3):
	for idy,valy in enumerate(entries_3):		
		if idx==idy:	
			if valy!=0:
				print('Raices iteradas',float(valx.group(1))/131072,"Calculo con entradas",1/math.sqrt(float(valy.group(1))/131072))
				print('Errores',((float(valx.group(1))/131072 - 1/math.sqrt(float(valy.group(1))/131072))/(float(valx.group(1))/131072))*100)
				errors_3.append(((float(valx.group(1))/131072 - 1/math.sqrt(float(valy.group(1))/131072))/(float(valx.group(1))/131072))*100)		
	
cont_3 = len(errors_3)
accumulator_3 = sum(int(i) for i in errors_3)
total_error_3 = float(accumulator_3)/float(cont_3)
print("Error promedio ",total_error_3) 

roots_4 = []
entries_4 = []
errors_4 = []

with open("tb_4.log") as f:
        content_4 = f.readlines()

for x in content_4:
    roots_4.append(re.search(r'square=x\s*([^\n]+)', x))

for x in content_4:
    entries_4.append(re.search(r'Entrada=x\s*([^\n]+),', x))

for idx,valx in enumerate(roots_4):
	for idy,valy in enumerate(entries_4):		
		if idx==idy:	
			if valy!=0:	
				print('Raices iteradas',float(valx.group(1))/131072,"Calculo con entradas",1/math.sqrt(float(valy.group(1))/131072))
				print('Errores',((float(valx.group(1))/131072 - 1/math.sqrt(float(valy.group(1))/131072))/(float(valx.group(1))/131072))*100)
				errors_4.append(((float(valx.group(1))/131072 - 1/math.sqrt(float(valy.group(1))/131072))/(float(valx.group(1))/131072))*100)		
	
cont_4 = len(errors_4)
accumulator_4 = sum(int(i) for i in errors_4)
total_error_4 = float(accumulator_4)/float(cont_4)
print("Error promedio ",total_error_4) 
