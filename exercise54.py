# This is where Exercise 5.4 goes
# Name: Christopher Van Schyndel


def is_triangle(a, b, c):
	if a > b + c or b > a + c or c > a + b:
		print "No"
		return False
	else:
		print "Yes"
		return True

def stickinput():
	print "This program will compare three side lengths of a triangle and respond with"
	print "whether or not such a triangle is possible."
	a = raw_input("Enter the first triangle side length: ")
	print "1) " + str(a)
	b = raw_input("Now the second side length, please: ")
	print "1) " + str(a) + "  2) " + str(b)
	c = raw_input("The third and last side length, please: ")
	print "1) " + str(a) + "  2) " + str(b) + "  3) " + str(c)
	if a.isdigit() == False or b.isdigit() == False or c.isdigit() == False:
		print "Please input integers only!"
	else:
		a = int(a)
		b = int(b)
		c = int(c)
		print "Is the triangle possible with the lengths given?"
		is_triangle(a, b, c)


stickinput()


