import sys # Command line arguments
import re # regex

def binary_to_decimal(binary):
       decimal=0
       for i in range(len(str(binary))):
           power=len(str(binary))-(i+1)
           decimal+=int(str(binary)[i])*(2**power)
       return decimal

def main(number):
    result = binary_to_decimal(00010101)
    return result

    
if __name__ == '__main__':
      main()