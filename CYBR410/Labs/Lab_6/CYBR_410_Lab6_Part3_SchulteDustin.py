# CYBR 410 Encyrption Lab 6 Part 3
# Created by Souvik Nandi
# Modified by Dr. D.Vo 11/07/2022, 11/04/20224
#
# Modified By:     Student Name
# Modified On:     Enter Date here

from random import randint

if __name__ == '__main__':

    # Both the persons will be agreed upon the
    # public keys G and P
    # A prime number P is taken
    P = 23
    
    # A primitive root for P, G is taken
    G = 9
    
    
    print('The Value of P is: %d'%(P))
    print('The Value of G is: %d'%(G))
    
    # Alice will choose the private key a
    a = 4
    print('The Private Key a for Alice is: %d'%(a))
    
    # Bob will choose the private key b
    b = 3
    print('The Private Key b for Bob is: %d'%(b))
    
    # gets the generated key
    x = int(pow(G,a,P))
    print('Alice computed public value is: %d'%(x))
    
    # gets the generated key
    y = int(pow(G,b,P))
    print('Bob computed public value is: %d'%(y))
    
    # Secret key for Alice
    ka = int(pow(y,a,P))
    
    # Secret key for Bob
    kb = int(pow(x,b,P))
    
    print('Symmetric key for the Alice is: %d'%(ka))
    print('Symmetric Key for the Bob is: %d'%(kb))
    print('Thus, the common shared secret for both is: %d'%(kb))
