import removeCollege as rm
import addCollege as add
import displayCollege as disp
class College:
	def __init__(self, collegeId, collegeName, courseType, city, fees, pinCode):
		self.collegeId = collegeId
		self.collegeName = collegeName
		self.courseType = courseType
		self.city = city
		self.fees = fees
		self.pinCode = pinCode
		self.addCollege()
	def addCollege(self):
		add.add(self.collegeId, self.collegeName, self.courseType, self.city, self.fees, self.pinCode)
	@staticmethod
	def display():
		disp.display()
	@staticmethod
	def remove():
		rm.remove()
print('Welcome to College Management System')
while True:
	choice = int(input('What you want to do: 1.Add College \t 2.Display College \t 3. Remove College \t 4.Exit\n'))
	if(choice == 1):
		collegeId=input("Enter College Id:")
		collegeName=input("Enter College Name:")
		courseType=input("Enter Course Type:")
		city=input("Enter City Name:")
		fees=input("Enter Fees:")
		pinCode=input("Enter Pincode:")
		c=College(collegeId, collegeName, courseType, city, fees, pinCode)
	elif(choice == 2):
		College.display()
	elif(choice == 3):
		College.remove()
	elif(choice == 4):
		break
	else:
		print('Wrong Input')