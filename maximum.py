import sys
import re 

def usage():
	print "Usage %s <decimal_number>" % (sys.argv[0])
	print "  Print a number "
	sys.exit(-1)

def main():
	if len(sys.argv) < 2 or not re.search('^-?\d+$', sys.argv[1]):
		usage()	

	print "HI "
	print sys.argv
	max=int(sys.argv[1])
	for i in range(2,len(sys.argv)):
		if not re.search('^-?\d+$', sys.argv[i]):
			usage()
		x=int(sys.argv[i])
		if x >=max:
			max=x
	print "Maximum value is " +str(max)


if __name__ == '__main__':
	main()