# Vigenère Cipher Encryptor/Decryptor

This is a simple project that implements a **Vigenère Cipher** for encrypting plaintext and decrypting ciphertext. It is deployed on Streamlit cloud [here.](https://vigenerecipher.streamlit.app/ "Vigenere Cipher Encryptor Decryptor")

## About Vigenère Ciphers

A **Vigenère Cipher** is a polyalphabetic substitution cipher where each plaintext letter is encrypted with a different substitution alphabet based on a keyword. This makes it more secure than a simple substitution cipher. To encrypt/decrypt data using this method, a **Vigenère** **Table** is used.

A **Vigenère Table** makes it easier to find the corresponding encrypted letter. It's a grid where the rows and columns are labeled with the alphabet.

**This project uses a Vigenère Table which contains `uppercase letters`. (like all basic Vigenère Tables)**

## Important Note

Whenever you encrypt/decrypt some data, a `Cipher Key` and an `Encryption Key` will be required.

The `Cipher Key` is used to create the Vigenère Table and the `Encryption Key` is used to create the keystream.

So choose your `Cipher Key` and `Encryption Key` wisely and keep them safe.

**If any one of them is altered/lost, your data won't be recovered.**

## Installation Guide

Clone this repository and install the requirements in the `requirements.txt` file using the following command.

```powershell
pip install -r requirements.txt
```

After the installation, you can use the standard Streamlit commands to run it.

```powershell
python -m streamlit run WebUI.py --theme.base=dark
```
