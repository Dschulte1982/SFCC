# CYBR 410 Encyrption Lab 6 Part 1
# Created by Pranay Arora
# Modified by Dr. D.Vo 11/06/2022; 11/04/2024
#
# Modifyied By:    Dustin Schulte
# Modified On:     11/04/2024
#
# Python for RSA asymmetric cryptographic algorithm.
# For demonstration, values are relatively
#  small compared to practical application

import math

def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

# Defined RSA parameters as:
p = 3                # Step 2
q = 7                # Step 2

n = p*q                 # Step 3
print("n value = ", n)  # Step 3 Check

e = 2     # Step 4; ENTER smaller e the better HERE

phi = (p-1)*(q-1)          # Step 6
print("phi value = ", phi) # Step 6 check

while (e < phi):

    # e must be co-prime to phi and
    # smaller than phi.
    if(gcd(e, phi) == 1):
        break
    else:
        e = e + 1

# Private key (d stands for decrypt)
# choosing k such that it satisfies
# d*e = k * totient + 1

k = 2
d = ((k*phi)+ 1)/e      # Step 6
print("d value = ", d)  # Step 6 Check

# Message to be encrypted
msg = 14             # Step 8: ENTER numerical under 20 HERE
print("")
print("Message data = ", msg)

# Encryption c = (msg ^ e) % n Step 9
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)

# Decryption m = (c ^ d) % n Step 10
m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)
