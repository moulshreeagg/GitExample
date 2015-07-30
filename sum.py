import sys


def main():
	print "HI"
	print sys.argv
	sum=0
	for i in range(1,len(sys.argv)):
		sum+=int(sys.argv[i])
	print "sum is " +str(sum) 


















if __name__ == '__main__':
    main()