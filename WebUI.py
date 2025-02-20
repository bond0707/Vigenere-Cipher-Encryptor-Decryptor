import streamlit as st
from VigenereCipher import VigenereCipher
from streamlit_option_menu import option_menu

def encryptUI():
    st.markdown("<h1 style='text-align: center;'>Vigenère Cipher Encryptor</h1>",
                unsafe_allow_html=True)

    with st.form("Encoder_Form"):
        cipher_key = st.text_input("Cipher Key")
        encrypt_key = st.text_input("Encryption Key")
        text = st.text_input("Plaintext")
        submit_btn = st.form_submit_button("Encrypt", use_container_width=True)

        if submit_btn:
            cipher_key = cipher_key.strip().upper()
            encrypt_key = encrypt_key.strip().upper()
            text = text.strip().upper()

            if not cipher_key.isalpha():
                st.error("Please Enter A Valid Cipher Key! (A-Z, a-z)", icon="❌")
            elif not encrypt_key.isalpha():
                st.error(
                    "Please Enter A Valid Encryption Key! (A-Z, a-z)", icon="❌")
            elif text == "" or not all(char.isupper() or char.isspace() for char in text):
                st.error(
                    "Please Enter valid text to Encrypt! (A-Z, a-z, whitespace)", icon="❌")
            else:
                on_encrypt_submit(cipher_key, encrypt_key, text)


def decryptUI():
    st.markdown("<h1 style='text-align: center;'>Vigenère Cipher Decryptor</h1>",
                unsafe_allow_html=True)

    with st.form("Decoder_Form"):
        cipher_key = st.text_input("Cipher Key")
        encrypt_key = st.text_input("Encryption Key")
        cipher = st.text_input("Ciphertext")
        submit_btn = st.form_submit_button("Decrypt", use_container_width=True)

        if submit_btn:
            cipher_key = cipher_key.strip().upper()
            encrypt_key = encrypt_key.strip().upper()
            cipher = cipher.strip().upper()

            if not cipher_key.isalpha():
                st.error("Please Enter A Valid Cipher Key! (A-Z, a-z)", icon="❌")
            elif not encrypt_key.isalpha():
                st.error(
                    "Please Enter A Valid Encryption Key! (A-Z, a-z)", icon="❌")
            elif cipher == "" or not all(char.isupper() or char.isspace() for char in cipher):
                st.error(
                    "Please Enter valid ciphertext to Decrypt! (A-Z, a-z, whitespace)", icon="❌")
            else:
                on_decrypt_submit(cipher_key, encrypt_key, cipher)


def aboutUI():
    with open("README.md", "r") as f:
        about = "".join(f.readlines()).replace("VigenÃ¨re", "Vigenère")
        st.markdown(about)


def on_encrypt_submit(cipher_key, encrypt_key, text):
    encryptor = VigenereCipher(cipher_key)

    cipher_text_list = []
    for text_part in text.split():
        cipher_text_list.append(encryptor.encrypt(encrypt_key, text_part))

    cipher_text = " ".join(cipher_text_list).strip()

    st.markdown("<h3 style='text-align: center; vertical-align: middle;'>Plaintext encrypted successfully!</h3>",
                unsafe_allow_html=True)

    st.code(cipher_text)


def on_decrypt_submit(cipher_key, encrypt_key, cipher):
    decryptor = VigenereCipher(cipher_key)

    plain_text_list = []
    for cipher_part in cipher.split():
        plain_text_list.append(decryptor.decrypt(encrypt_key, cipher_part))

    plain_text = " ".join(plain_text_list).strip()

    st.markdown("<h3 style='text-align: center; vertical-align: middle;'>Ciphertext decrypted successfully!</h3>",
                unsafe_allow_html=True)

    st.code(plain_text)


if __name__ == "__main__":
    st.set_page_config(
        page_icon="🔐",
        layout="wide",
        page_title="Vigenère Cipher",
    )

    with st.sidebar:
        options = option_menu(
            menu_title="Main Menu",
            menu_icon="cast",
            options=["Encrypt", "Decrypt", "About"],
            icons=["lock", "unlock", "question"],
            default_index=0
        )

    if options == "Encrypt":
        encryptUI()
    elif options == "Decrypt":
        decryptUI()
    else:
        aboutUI()
