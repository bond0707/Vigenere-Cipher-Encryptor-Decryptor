import streamlit as st
from VigenereCypher import VigenereCypher
from streamlit_option_menu import option_menu

def encryptUI():
    st.markdown("<h1 style='text-align: center;'>Vigènere Cypher Encoder</h1>", unsafe_allow_html=True)
    
    with st.form("Encoder_Form"):
        cypher_key = st.text_input("Cypher Key")
        encrypt_key = st.text_input("Encryption Key")
        text = st.text_input("Text")
        submit_btn = st.form_submit_button("Encrypt", use_container_width=True)
        
        if submit_btn:
            if cypher_key == "":
                st.error("Please Enter A Valid Cypher Key!", icon="❌")
            elif encrypt_key == "":
                st.error("Please Enter A Valid Encryption Key!", icon="❌")
            elif text == "":
                st.error("Please Enter Something to Encrypt!", icon="❌")
            else:
                on_encrypt_submit(cypher_key, encrypt_key, text)


def decryptUI():
    st.markdown("<h1 style='text-align: center;'>Vigènere Cypher Decoder</h1>", unsafe_allow_html=True)

    with st.form("Decoder_Form"):
        cypher_key = st.text_input("Cypher Key")
        encrypt_key = st.text_input("Encryption Key")
        cypher = st.text_input("Cypher")
        submit_btn = st.form_submit_button("Decrypt", use_container_width=True)

        if submit_btn:
            if cypher_key == "":
                st.error("Please Enter A Valid Cypher Key!", icon="❌")
            elif encrypt_key == "":
                st.error("Please Enter A Valid Encryption Key!", icon="❌")
            elif cypher == "":
                st.error("Please Enter Something to Decrypt!", icon="❌")
            else:
                on_decrypt_submit(cypher_key, encrypt_key, cypher)

def aboutUI():
    with open("README.md", "r") as f:
        about = "".join(f.readlines()).replace("VigÃ¨nere", "Vigènere")
        st.markdown(about)


def on_encrypt_submit(cypher_key, encrypt_key, text):
    encryptor = VigenereCypher(cypher_key)
    st.success("Encrypted Cypher : " + encryptor.encrypt(encrypt_key, text), icon="✔️")


def on_decrypt_submit(cypher_key, encrypt_key, cypher):
    decryptor = VigenereCypher(cypher_key)
    st.success("Decrypted Text : " + decryptor.decrypt(encrypt_key, cypher), icon="✔️")


if __name__ == "__main__":
    st.set_page_config(
        page_icon="🔐",
        page_title="Vigènere Cypher",
        layout="wide"
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