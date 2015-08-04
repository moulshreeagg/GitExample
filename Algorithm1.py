def bubblesort(ls):
	n = len(ls)
	swapped = True
	while swapped: 
		swapped = False
		for i in range(n-1):
			if ls[i] > ls[i+1]:
				temp = ls[i]
				ls[i] = ls [i+1]
				ls[i+1] = temp
				swapped = True
	return ls

def main():
	print bubblesort([0,8,10,7,6,5,2,1, -9 ,10, -78])


if __name__ == '__main__':
    main()