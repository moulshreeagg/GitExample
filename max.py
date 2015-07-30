import sys


def main():
	print "HI "
	print sys.argv
	max=int(sys.argv[1])
	for i in range(2,len(sys.argv)):
		x=int(sys.argv[i])
		if x >=max:
			max=x
	print "Maximum value is " +str(max) 

if __name__ == '__main__':
    main()