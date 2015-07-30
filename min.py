import sys


def main():
	print "HI "+str(len(sys.argv))
	print sys.argv
	min=int(sys.argv[1])
	for i in range(2,len(sys.argv)):
		x=int(sys.argv[i])
		if x <=min:
			min=x
	print "Minimum value is " +str(min) 


















if __name__ == '__main__':
    main()