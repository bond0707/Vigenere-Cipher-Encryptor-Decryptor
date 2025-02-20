import streamlit as st
from VigenereCypher import VigenereCypher
from streamlit_option_menu import option_menu

def encryptUI():
    st.markdown("<h1 style='text-align: center;'>Vigenère Cypher Encryptor</h1>", unsafe_allow_html=True)

    with st.form("Encoder_Form"):
        cypher_key = st.text_input("Cypher Key")
        encrypt_key = st.text_input("Encryption Key")
        text = st.text_input("Plain Text")
        submit_btn = st.form_submit_button("Encrypt", use_container_width=True)

        if submit_btn:
            cypher_key = cypher_key.strip().upper()
            encrypt_key = encrypt_key.strip().upper()
            text = text.strip().upper()

            if not cypher_key.isalpha():
                st.error("Please Enter A Valid Cypher Key! (A-Z, a-z)", icon="❌")
            elif not encrypt_key.isalpha():
                st.error("Please Enter A Valid Encryption Key! (A-Z, a-z)", icon="❌")
            elif text == "" or not all(char.isupper() or char.isspace() for char in text):
                st.error("Please Enter valid text to Encrypt! (A-Z, a-z, whitespace)", icon="❌")
            else:
                on_encrypt_submit(cypher_key, encrypt_key, text)


def decryptUI():
    st.markdown("<h1 style='text-align: center;'>Vigenère Cypher Decryptor</h1>", unsafe_allow_html=True)

    with st.form("Decoder_Form"):
        cypher_key = st.text_input("Cypher Key")
        encrypt_key = st.text_input("Encryption Key")
        cypher = st.text_input("Cypher Text")
        submit_btn = st.form_submit_button("Decrypt", use_container_width=True)

        if submit_btn:
            cypher_key = cypher_key.strip().upper()
            encrypt_key = encrypt_key.strip().upper()
            cypher = cypher.strip().upper()

            if not cypher_key.isalpha():
                st.error("Please Enter A Valid Cypher Key! (A-Z, a-z)", icon="❌")
            elif not encrypt_key.isalpha():
                st.error("Please Enter A Valid Encryption Key! (A-Z, a-z)", icon="❌")
            elif cypher == "" or not all(char.isupper() or char.isspace() for char in cypher):
                st.error("Please Enter valid cyphertext to Decrypt! (A-Z, a-z, whitespace)", icon="❌")
            else:
                on_decrypt_submit(cypher_key, encrypt_key, cypher)

def aboutUI():
    with open("README.md", "r") as f:
        about = "".join(f.readlines()).replace("VigenÃ¨re", "Vigenère")
        st.markdown(about)

def on_encrypt_submit(cypher_key, encrypt_key, text):
    encryptor = VigenereCypher(cypher_key)
    
    cypher_text_list = []
    for text_part in text.split(): 
        cypher_text_list.append(encryptor.encrypt(encrypt_key, text_part))

    cypher_text = " ".join(cypher_text_list).strip()
    st.success("Encrypted Cypher : " + cypher_text, icon="✔️")


def on_decrypt_submit(cypher_key, encrypt_key, cypher):
    decryptor = VigenereCypher(cypher_key)

    plain_text_list = []
    for cypher_part in cypher.split():
        plain_text_list.append(decryptor.decrypt(encrypt_key, cypher_part))

    plain_text = " ".join(plain_text_list).strip()
    st.success("Decrypted Text : " + plain_text, icon="✔️")


if __name__ == "__main__":
    st.set_page_config(
        page_icon="🔐",
        layout="wide",
        page_title="Vigenère Cypher",
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