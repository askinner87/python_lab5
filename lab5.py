#PART 1
def is_valid_part(part):
    if part.isdigit():

        if len(part) > 1 and part[0] == '0':
            return False

        number = int(part)

        if 0 <= number <= 255:
            return True

    return False
print(is_valid_part("255"))  # True
print(is_valid_part("256"))  # False
print(is_valid_part("01"))   # False
print(is_valid_part("0"))    # True
print()

def is_valid_ip(ip):
    parts = ip.split('.')

    if len(parts) != 4:
        return False
    for p in parts:
        if not is_valid_part(p):
            return False
    return True
print(is_valid_ip("192.168.1.1"))      # True
print(is_valid_ip("192.168.256.1"))    # False
print(is_valid_ip("192.168.1"))        # False
print(is_valid_ip("192.168.01.1"))     # False
print()

#PART 2
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    return decimal_to_binary(n // 2) + str(n % 2)
print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))    # "1"
print()

def binary_to_decimal(b):
    if b == "":
        return 0
    return int(b[0]) * 2 ** (len(b) - 1) + binary_to_decimal(b[1:])
print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1
print()

#PART 3
def ip_to_binary(ip):
    if not is_valid_ip(ip):
       return "Invalid IP Adress"
    parts = ip.split('.')
    binary_parts = []

    for p in parts:
       binary_part = decimal_to_binary(int(p)).zfill(8)
       binary_parts.append(binary_part)

    return ".".join(binary_parts)
print(ip_to_binary("192.168.1.1"))
print(ip_to_binary("255.255.255.0"))
print(ip_to_binary("256.1.1.1"))



