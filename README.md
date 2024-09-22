# Vigènere Cypher Encryptor/Decryptor

This is a simple project that implements a Vigènere Cypher for encrypting plaintext and decrypting cyphertext. It is deployed on streamlit cloud [here.](https://vigenerecypher.streamlit.app/ "Vigenere Cypher Encryptor Decryptor")

## About Vigènere Cyphers

A **Vigenère Cipher** is a polyalphabetic substitution cipher where each plaintext letter is encrypted with a different substitution alphabet based on a keyword. This makes it more secure than a simple substitution cipher. To encrypt/decrypt data using this method, a **Vigènere Table** is used.

A **Vigenère Table** makes it easier to find the corresponding encrypted letter. It's a grid where the rows and columns are labeled with the alphabet.

**This project uses a larger Vigènere Table which contains `uppercase letters`, `lowercase letters`, `digits`, `punctuation` and `whitespace`.**

## Important Note

Whenever you encrypt/decrypt some data, a `Cypher Key` and an `Encryption Key` will be required.

The `Cypher Key` is used to create the Vigènere Table and the `Encryption Key` is used to create the keystream.

So choose your Cypher Key and Encryption Key wisely and keep them safe.

**If any one of them is altered/lost, your data won't be recovered.**

## Installation Guide

Clone this repository and install the requirements in the `requirements.txt` file using the following command.

```powershell
pip install -r requirements.txt
```

After the installation, you can use the standard streamlit commands to run it.

```powershell
python -m streamlit run WebUI.py --theme.base=dark
```
