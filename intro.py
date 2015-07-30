def rec_area (width, height):
	return width*height

def add (a,b):
	return a+b

def welcome_student(name,age):
	print "Morning " + name
	print "Your age is: "+str (age)
	
	if age<5: 
		print "Go Home"
	elif age<18:
		print "Go to School"
	else:
		print "Go to University"

def main():
	sum= add(3,2)
	print "sum 3+2=" +str(sum)
	area= rec_area(45,20)
	print "Area of a rectange with width 45 cm and height 20 cm is " +str(area) +" sq cms."
	print "Hi"

	for i in range(3):
		print "hi"+str(i)
	Students = ["Isaac", "Tom", "Peter", "Jack", "Harry", "Ron"]
	for Student in Students:
		print "hi " + Student

	i=1
	while i<20:
		print "odd "+ str(i)
		i = i+2

	welcome_student("Tom", 18)
	welcome_student("Isaac", 27)
	welcome_student("Jack", 7)
	welcome_student("Lily", 2)

	print "Hi "+Students[0]
	print "Hi "+Students[1]
	Students[0] = "Bob"
	print "Hi "+Students[0]
	Students.append("Moulshree")
	for i in range(len(Students)):
		print "Student "+str(i)+":" +Students[i]

	ages = {"Tom" : 18, "Isaac": 27 }
	print "Tom is " +str(ages["Tom"])
	ages["Tom"]=19
	print "Tom is " +str(ages["Tom"])
	ages["John"]=32
	for name,age in ages.iteritems():
		print name+ " is "+ str(age)


if __name__ == '__main__':
    main()
