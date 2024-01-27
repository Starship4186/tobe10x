from base64 import b64encode
import codecs

def hex_to_b64(hex_string:str):
    return b64encode(bytes.fromhex(hex_string)).decode()


def fixed_xor(hex_string1:str, hex_string2:str):
    # Converted from string to hex -> bytes.fromhex
    # xored -> i ^ j
    # converted back to hex
    return codecs.encode("".join(chr(i ^ j) for i, j in zip(bytes.fromhex(hex_string1), bytes.fromhex(hex_string2))).encode(), "hex").decode() if len(hex_string1) == len(hex_string2) else "Need strings of same length"



def single_bytes_xor_cipher(hex_string:str):
    # check with each single byte from  0 to 255
    # with every xor bruteforce, check the frequency of the occuring alphabets
    # alphabets like E, T, A, O, I, N , S, H more frequently
    # Add the number of occurence of such alphabets
    # The solution with most number of occurence of such alphabets might be the single byte with which the cipher was xored
    pass

str1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
