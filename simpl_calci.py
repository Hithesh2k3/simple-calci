# -*- coding: utf-8 -*-
"""simpl calci.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f2Vj3_gJgPavftxwzNOXsUmh1jSox2Os
"""

def main():
  a=int(input("enter the num:"));
  b=int(input("enter the num:"));
  op= input("enter the first 3 letters of the operation:");
  operation(a,b,op)

def operation(a,b,op):
  if (op=="add"):
    print(a+b);
  elif (op=="sub"):
    print(a-b);
  elif (op=="mul"):
    print(a*b);
  elif (op=="rem"):
    print(a%b);
  elif (op=="div"):
    print(a/b);

main()

