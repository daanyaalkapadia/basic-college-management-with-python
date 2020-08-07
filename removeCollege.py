import csv
def remove():
	lines = list()
	flag = False
	rmCollegeId= input("Please enter a College Id to be deleted:")
	with open('colleges.csv', 'r') as readFile:
		reader = csv.reader(readFile)
		for row in reader:
			lines.append(row)
			for field in row:
				if field == rmCollegeId:
					lines.remove(row)
					flag = True
	with open('colleges.csv', 'w', newline='') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(lines)
	if(flag == True):
		print('College with {} removed succesfully'.format(rmCollegeId))
	else:
		print('No college exist with {} as a collegeId'.format(rmCollegeId))