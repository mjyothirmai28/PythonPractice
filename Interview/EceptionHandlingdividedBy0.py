n = int(input("Enter numerator"))
d = int(input("Enter Denominator"))
try:
    print(n/d)

except Exception as err:
    print("Exception occured with error",err)
finally:
    print("value of n and d are",n,d)

# try:
#     a = 10
#     b = 0
#     print(a/b)
# except Exception as e:
#     print("Error: Cannot divide by zero")