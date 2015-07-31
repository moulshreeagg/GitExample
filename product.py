import sys

def main():
	print "HI"
	print sys.argv
	product=1 
	for i in range(1,len(sys.argv)):
		try:	
			product*=float(sys.argv[i])
		except ValueError:
			print "y is not an integer"
			sys.exit(-1)
	print "Product is " +str(product) 


if __name__ == '__main__':
    main()