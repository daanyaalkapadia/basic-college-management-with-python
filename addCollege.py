import csv
def add(collegeId, collegeName, courseType, city, fees, pinCode):
	with open("colleges.csv","a",newline='') as f:
			w=csv.writer(f)
			w.writerow([collegeId, collegeName, courseType, city, fees, pinCode])
			print(collegeName,'is added to the .csv file')