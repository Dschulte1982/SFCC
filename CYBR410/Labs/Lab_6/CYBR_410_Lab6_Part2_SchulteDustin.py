# CYBR 410 Encyrption Lab 6 Part 2
# Created by Pranay Arora
# Modified by Dr. D.Vo 11/07/2022, 11/04/2024
#
# Modified By:     Dustin Schulte
# Modified On:     11/04/2024

# Function to find the gcd of two integers using Euclidean algorithm
def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

# Function to find the lcm of two integers
def lcm(p, q):
    return p * q // gcd(p, q)  # Kudos to Kenneth S. on the //

# Function implementing extended euclidean algorithm
def egcd(e, phi):
    if e == 0:
        return (phi, 0, 1)
    else:
        g, y, x = egcd(phi % e, e)
        return (g, x - (phi // e) * y, y)

# Function to compute the modular inverse
def modinv(e, phi):
    g, x, y = egcd(e, phi)
    return x % phi


# Implementation of the Chinese Remainder Theorem
def chineseremaindertheorem(dq, dp, p, q, c):
    # Message part 1
    m1 = pow(c, dp, p)
    # Message part 2
    m2 = pow(c, dq, q)

    qinv = modinv(q, p)
    h = (qinv * (m1 - m2)) % p
    m = m2 + h * q
    return m

# ENTER your Driver Code HERE:
P = 953
Q = 2063
E = 42
C = 275382
D = modinv(E, lcm(P-1,Q-1))
print("private key d =", D)

# pow(a, b, c) calculates "a" raised to power "b"
# modulus "c", at a much faster rate than pow(a, b) % c
# Furthermore, we use Chinese Remainder Theorem as it
# splits the equation such that we have to calculate two
# values whose equations have smaller moduli and exponent
# value, thereby reducing computing time.

DQ = pow(D, 1, Q-1)
DP = pow(D, 1, P-1)
print("chinese remainder theorem = ", chineseremaindertheorem(DQ, DP, P, Q, C))
