"""
Project Euler Problem 59
========================

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key. The
advantage with the XOR function is that using the same encryption key on
the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using cipher1.txt, a file containing the encrypted
ASCII codes, and the knowledge that the plain text must contain common
English words, decrypt the message and find the sum of the ASCII values
in the original text.
"""

import csv

def string_sum(s):
    return sum(bytearray(s))

def simple_decrypt(cipher, key):

    msg = [None] * (len(cipher) - 1)
    for c in range( 0, len(cipher)-3, 3):
        msg[c]    =    chr(cipher[c]    ^   key[0])
        msg[c+1]  =    chr(cipher[c+1]  ^   key[1])
        msg[c+2]  =    chr(cipher[c+2]  ^   key[2])

    return msg



cipher = []
with open('./resources/cipher1.txt', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        cipher.extend( row )


#print(cipher)
cipher = list(map(int, cipher))
#print(cipher)
#cipher = list(map(unichr, cipher))
#print(cipher)

#characters = [chr(n) for n in cipher]
#print(characters)

#result = 97 ^ 100
#print(bool('a'))
#print (result)

# lower case chars 97 to 122
f = open("msgs.txt","w")

for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            key = [i,j,k]

            str1 = map(str, key)
            str1 = ''.join(str1)
            f.write( str1 )
            f.write( "\n" )
            #print(int(str1))

            msg = simple_decrypt(cipher, key)

            str2 = map(str, msg)
            str2 = ''.join(str2)

            if int(str1) == 103111100:
                ans_sum = string_sum(str2)
                print(ans_sum)

            #str2 = [chr(n) for n in str2]

            f.write( str2 )
            f.write( "\n" )


f.close()




#key 103 111 100

#msg
'''(The Gospel of John, chapter 1) 1 In the beginning the Word already existed.
He was with God, and he was God. 2 He was in the beginning with God. 3 He
created everything there is. Nothing exists that he didn't make. 4 Life
itself was in him, and this life gives light to everyone. 5 The light shines
through the darkness, and the darkness can never extinguish it. 6 God sent John
the Baptist 7 to tell everyone about the light so that everyone might believe
because of his testimony. 8 John himself was not the light; he was only a
witness to the light. 9 The one who is the true light, who gives light to
everyone, was going to come into the world. 10 But although the world was made
through him, the world didn't recognize him when he came. 11 Even in his own
land and among his own people, he was not accepted. 12 But to all who
believed him and accepted him, he gave the right to become children of God.
13 They are reborn! This is not a physical birth resulting from human passion
or plan, this rebirth comes from God.14 So the Word became human and lived here
on earth among us. He was full of unfailing love and faithfulness. And we have
seen his glory, the glory of the only Son of the Father
'''
