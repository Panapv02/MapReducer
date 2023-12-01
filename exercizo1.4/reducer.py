#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

dicc = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    # Escribe un par key:value ante un cambio na key
    
    if thisKey in dicc:
	oldSale =  dicc[thisKey]
	if thisSale > oldSale
		dicc.update({thisKey,thisSale})
    else
	dicc.update({thisKey,thisSale})

# recorremos el diccionario comparando que elemento es más grande y eliminamos los pequeños
for i in dicc:
	for j in dicc:
		if dicc[i] > dicc[j]
			dicc.pop(j)
print(dicc)
