number = int(input("Enter a decimal number: "))

binary = bin(number)[2:]
hexadecimal = hex(number)[2:].upper()

print("Binary:", binary)
print("Hexadecimal:", hexadecimal)
