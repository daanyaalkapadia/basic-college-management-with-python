import csv
def display():
	with open("colleges.csv","r") as f: 
		r=csv.reader(f)
		data=list(r)
		flag = False
		count=0
		for line in data:
			for field in line:
				if field.strip().lower() == 'Engineering'.lower():
					count=count+1
				if field.strip().lower() == 'Mumbai'.lower():
					count=count+1
			if(count == 2):
				for word in line:
					print(word,"\t",end='')
					flag = True
				print()
			count = 0
		if flag == False:
			print('Nothing to display')