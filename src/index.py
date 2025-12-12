import streamlit as st

class IndexUI:
    @staticmethod
    def main():
        st.title("Hello, Streamlit!")

if __name__ == "__main__":
    IndexUI.main()
else: 
    exit('Esse arquivo deve ser executado diretamente pelo Streamlit.')