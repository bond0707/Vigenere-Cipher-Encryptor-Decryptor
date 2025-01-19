# The pre-processing for the arguements happens in the "WebUI.py" file.
# so if you happen to run this file directly then follow the instrutions given below.

# Pass only UPPERCASE LETTERS in the constructor for "cypher_key" arguement.
# Pass only UPPERCASE LETTERS in encrypt and decrypt methods for the "key" agruement.
# Pass only UPPERCASE LETTERS and WHITESPACE(" ") in the encrypt and decrypt methods
# for the "message" and "cypher" arguements respectively.

from string import ascii_uppercase

class VigenereCypher():
    def __init__(self, cypher_key: str) -> None:
        key_alphabets = list(cypher_key) + [i for i in ascii_uppercase if i not in cypher_key]
        self.vignere_table = [list(key_alphabets)[i:] + (list(key_alphabets)[0:i]) for i in range(len(key_alphabets))]

    def make_keystream(self, key: str, msg_len: int) -> str:
        keystream, i = '', 0
        while len(keystream) < msg_len:
            keystream += key[i]
            if i == len(key) - 1:
                i = 0
            else:
                i+=1
        return keystream

    def encrypt(self, key: str, message: str) -> str:
        keystream, cypher = self.make_keystream(key, len(message)), ''
        for i in range(len(message)):
            row_i = self.vignere_table[0].index(message[i])
            col_i = self.vignere_table[0].index(keystream[i])
            cypher += self.vignere_table[row_i][col_i]
        return cypher

    def decrypt(self, key: str, cypher: str) -> str:
        keystream, plaintext = self.make_keystream(key, len(cypher)), ''
        for i in range(len(cypher)):
            row_i = self.vignere_table[0].index(keystream[i])
            col_i = self.vignere_table[row_i].index(cypher[i])
            plaintext += self.vignere_table[0][col_i]
        return plaintext


if __name__ == "__main__":    
    obj = VigenereCypher("KRYPTOS")
    print("Encrypted :", obj.encrypt("HIDDEN", "LEET FORCE"))
    print("Decrypted :", obj.decrypt("HIDDEN", "OKUH KQENV"))
