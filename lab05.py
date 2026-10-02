#PART1

def is_valid_part(part):
    try:
        code = int(part)
        if part[0] == '0' and not code == 0: return False
        return 0 <= code < 256
    except ValueError as ve:
        return False

def is_valid_ip(ip:str):
    parts = ip.split('.')
    if len(parts) != 4: return False
    for part in parts:
        if not is_valid_part(part): return False
    return True

print(is_valid_part('143'),is_valid_part('259'),is_valid_part('CAT'),is_valid_part('-28'),is_valid_part('01'),is_valid_part('0'))

print(
    is_valid_ip('255.255.255.255'),
    is_valid_ip("192.168.1.1"),
    is_valid_ip("192.168.256.1"),
    is_valid_ip("192.168.1"),
    is_valid_ip('192.168.01.1'),
        )

#PART2
def decimal_to_binary(n):
    if n == 0: return '0'
    if n == 1: return '1'
    return decimal_to_binary(n // 2) + str(n % 2)

def binary_to_decimal(b):
    if b == "":
        return 0
    last_bit = int(b[-1])
    return binary_to_decimal(b[:-1]) * 2 + last_bit


print(
    decimal_to_binary(10),
    decimal_to_binary(255),
    decimal_to_binary(1),
     )

print(
    binary_to_decimal("1010"),
    binary_to_decimal("11111111"),
    binary_to_decimal("1"),
      )