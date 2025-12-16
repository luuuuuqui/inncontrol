from templates.mantertesteUI import ManterTesteUI
import streamlit as st

class IndexUI:
    @staticmethod
    def menu_admin():            
        ManterTesteUI.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()

    @staticmethod
    def main():
        IndexUI.sidebar()

if __name__ == "__main__":
    ManterTesteUI.main()