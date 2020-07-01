import streamlit as st
import pandas as pd

def main():
    #comandos básicos
    st.title("Hello World")
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.text("Isto é um texto")
    st.image("logo.png")

    #comando para criar um botão
    st.markdown("Botao")
    botao = st.button("Botao")

    if botao:
        st.markdown("Clicado")
    
    #comando para criar uma checkbox
    check = st.checkbox("Checkbox")

    if check:
        st.markdown("Clicado")

    #comando para criar uma lista de opções
    st.markdown("Radio")
    radio = st.radio("Escolhas as opcoes", ("Opt 1", "Opt 2"))

    if radio == "Opt 1":
        st.markdown("Escolhido a opção 1")
    if radio == "Opt 2":
        st.markdown("Escolhido a opção 2")
    
    #comando para criar uma caixa de seleção
    st.markdown("SelectBox")
    select = st.selectbox("Choose opt", ("Opt 1", "Opt 2"))

    if select == "Opt 1":
        st.markdown("Escolhido a opção 1")
    if select == "Opt 2":
        st.markdown("Escolhido a opção 2")

    #comando para criar varias seleções
    st.markdown("Multi")
    multi = st.multiselect("Choose", ("Opt 1", "Opt 2"))

    if multi == "Opt 1":
        st.markdown("Escolhido a opção 1")
    if multi == "Opt 2":
        st.markdown("Escolhido a opção 2")

    #comando para ler um arquivo
    st.markdown("File uploader")
    #st.file_uploader("Chosse your file", type = 'cvs')

    #if file is not None:
        #st.markdown("Não esta vazio")

    #usando pandas para ler um arquivo
    df = pd.read_csv('IRIS.csv')
    st.dataframe(df.head())

    #usando pandas para ler um arquivo imputado
    file = st.file_uploader("Upload your file", type = 'csv')

    if file is not None:
        slider = st.slider('Valores', 1,100)
        df =  pd.read_csv(file)
        st.dataframe(df.head(slider))
        st.markdown("Markdown")
        st.table(df.head(slider))

        st.write(df.columns)
        st.table(df.groupby("species")['petal_width'].mean())


if __name__ == '__main__':
    main()