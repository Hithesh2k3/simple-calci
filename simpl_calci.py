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
  elif (op=="div"):
    print(a/b);

main()

a= input("Enter your Name:");
b= input("Enter the time_24hr format:");
h, m = map(int, b.split(':'))
if (h<12 and m!=0):
    print("Good Morning");
elif (h==12 and m==0):
    print("Good Afternoon");
else:
    print("Good Evening");

def greet(name, hour, minute):
    if hour < 12 or (hour == 12 and minute == 0):
        print(f"Good morning, {name}!")
    else:
        print(f"Good evening, {name}!")

def main():
    name = input("Enter your name: ")
    time_input = input("Enter the time in HH:MM format (24-hour clock): ")
    hour, minute = map(int, time_input.split(':'))
    greet(name, hour, minute)

if __name__ == "__main__":
    main()