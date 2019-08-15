import random

def text2number(msg):
    f = open("MessageInNumbers.txt", "w+")
    for letter in msg:
        ascii_val = ord(letter)
        f.write(""+ str(ascii_val) + "\n")
    f.close()

def cipher():
    f = open("PublicKey.txt", "r")
    content = f.read()
    f.close()

    # Reading PublicKey file contents
    parts = content.split(",")
    n = int(parts[0])
    e = int(parts[1])

    f = open("MessageInNumbers.txt", "r")
    lines_array = f.readlines()
    f.close()
    f = open("CipherMessage.txt", "w+")

    for line in lines_array:
        c = int(line)**e % n
        f.write("" + str(c) + "\n")

    print("Cifrado con éxito! Su mensaje cifrado se encuentra en el archivo CipherMessage.txt.")

def decipher():
    f = open("PrivateKey.txt", "r")
    content = f.read()
    f.close()
    # Reading PublicKey file contents
    parts = content.split(",")
    n = int(parts[0])
    d = int(parts[1])

    f = open("CipherMessage.txt", "r")
    lines_array = f.readlines()
    f.close()

    f = open("DecipherMessage.txt", "w+")
    for line in lines_array:
        m = int(line)**d % n
        f.write("" + str(m) + "\n")


def generateKey():
    p = int(input("Ingrese el primer número primo: "))
    q = int(input("Ingrese el segundo número primo: "))
    n = p * q
    m = (p - 1) * (q - 1)
    x = 0

    x = random.randint(2, m)
    while x % m == 0:
        x = random.randint(2, m)

    #for i in range(2, m):
    #    if i % m != 0:
    #        x = i
    #        break

    #d = 0
    #while (d * x) % m != 1:
    #   print(d)
    #    d = d + 1

    d = modulo_multiplicative_inverse(x, m)

    f = open("PrivateKey.txt", "w+")
    f.write(str(n) + "," + str(d))
    f.close()
    f = open("PublicKey.txt", "w+")
    f.write(str(n) + "," + str(x))
    f.close()


def modulo_multiplicative_inverse(A, M):
    """
    Assumes that A and M are co-prime
    Returns multiplicative modulo inverse of A under M
    """
    # Find gcd using Extended Euclid's Algorithm
    gcd, x, y = extended_euclid_gcd(A, M)

    # In case x is negative, we handle it by adding extra M
    # Because we know that multiplicative inverse of A in range M lies
    # in the range [0, M-1]
    if x < 0:
        x += M

    return x


def extended_euclid_gcd(a, b):
    """
    Returns a list `result` of size 3 where:
    Referring to the equation ax + by = gcd(a, b)
        result[0] is gcd(a, b)
        result[1] is x
        result[2] is y
    """
    s = 0;
    old_s = 1
    t = 1;
    old_t = 0
    r = b;
    old_r = a

    while r != 0:
        quotient = old_r // r  # In Python, // operator performs integer or floored division
        # This is a pythonic way to swap numbers
        # See the same part in C++ implementation below to know more
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return [old_r, old_s, old_t]


def main():
    print("Bienvenido al programa RSA.\nListado de opciones:\n1. Cifrar\n2. Descifrar\n3. Generar llave.\n4. Parsear mensaje")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        cipher()
    elif op == 2:
        decipher()
    elif op == 3:
        generateKey()
    elif op == 4:
        text2number(msg = input("Ingrese el mensaje a parsear: "))


main()