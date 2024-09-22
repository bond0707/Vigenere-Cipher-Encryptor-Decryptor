from string import ascii_letters, digits, punctuation, whitespace

class VigenereCypher():
    def __init__(self, cypher_key: str) -> None:
        key_alphabets = list(cypher_key) + [i for i in ascii_letters+digits+punctuation+whitespace if i not in cypher_key]
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
    obj = VigenereCypher("Kryptos")
    print("Encrypted :", obj.encrypt("Hidden", "Leet Force"))
    print("Decrypted :", obj.decrypt("Hidden", "*zqho0Njmq"))
