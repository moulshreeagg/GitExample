import random

def binary_search(x,ls):
	s=0
	e=len(ls)-1
	while s<=e:
		mid=int((s+e)/2)
		if ls[mid]==x:
			return True
		elif ls[mid]<x:
			s=mid+1
		else:
			e=mid-1
	return False


def linear_search(x,ls):
	for l in ls:
		if x==l:
			return True
		elif l>x:
			return False
	return False

def main():
	numbers = [ random.randrange(1,1000000) for i in range(10000000) ]
	# numbers = [1, 1, 1, 1, 1]
	numbers.sort()
	find= random.randrange(1,1000000)

	print "binary_search:"
	print binary_search(find,numbers)
	print "linear_search:"
	print linear_search(find,numbers)


if __name__ == '__main__':
    main()