a= 5
b= 2

try:
    print("Resource open")
    print(a/b)
except Exception as e:
    print("Dividing number by 0 not allowed", e)

finally:
    print("Resource Closed")

print("Bye")