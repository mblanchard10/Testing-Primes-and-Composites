#!/usr/bin/env python3

__author__ = "Mike Blanchard"
__copyright__ = "Copyright 2020"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "0.0.0"
__maintainer__ = ""
__email__ = "mblancha@highpoint.edu"
__status__ = "Complete"

def main():
   num = int(input("Enter a positive integer: "))
   if num < 0:
      print("The input must be a positive integer!")
   elif num == float:
      print("The input must be an integer!")

   for i in range(2,num):
      answer = i % num
      if answer == 0:
         composite = True
      elif answer > 0:
         composite = False
   
   if composite == True:
      print("The number entered is composite.")
   elif composite == False:
      print("The number entered is prime.")

if __name__ == "__main__":
   main() 
