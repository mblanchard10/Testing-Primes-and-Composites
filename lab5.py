#!/usr/bin/env python3

__author__ = "Mike Blanchard"
__copyright__ = "Copyright 2020"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "0.0.0"
__maintainer__ = ""
__email__ = "mblancha@highpoint.edu"
__status__ = "Lab 5 Complete"

def main():
   num = int(input("Enter a positive integer: "))

   if num <= 0:
      print("The input must be a positive integer!")
   elif num == 1:
      print(num, "is neither prime or composite!")
   elif num == 2:
      print(num, "is prime.")
   else:
      for i in range(2,num):
         answer = num % i
         if answer == 0:
            composite = True
            break
         elif answer > 0:
            composite = False     
      if composite == False:
         print("The number entered is prime.")
      elif composite == True:
         print("The number entered is composite.")
      

if __name__ == "__main__":
   main() 
