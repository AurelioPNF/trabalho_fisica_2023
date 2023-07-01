import streamlit as st

def introducao():
    st.write("## Trabalho de Física 1 - 2023 - Semestre 1")
    st.sidebar.success("Selecione uma das simulações acima.")

    st.markdown(
        """
            ## Integrantes do grupo:
            
            Aurélio Pajuaba Nehme Filho
            
            Bruno Ribeiro Borges Gomes
            
            Henri Celso Fukuyama Mogami

        """
    )

    st.write("## Documentação")

    st.write("### Exercício 1")
    st.image(image="images/ex1.png")
    st.markdown(
        """
        Variáveis: (Massa 1, Massa 2, Massa 3, Atrito, Força)
        
        Retorno: (Aceleração, Tensão 1, Tensão 2, Tensão 3)
        """
    )

    st.write("### Exercício 2")
    st.image(image="images/ex2.png")
    st.markdown(
        """
        Variáveis: (Massa 1, Massa 2, Atrito, Gravidade)
        
        Retorno: (Aceleração, Tensão)
        """
    )

def exercicio1():
    st.write("Exercício 1")

def exercicio2():
    st.write("Exercício 2")

def exercicio3():
    st.write("Exercício 3")

def exercicio4():
    st.write("Exercício 4")

def exercicio5():
    st.write("Exercício 5")

def exercicio6():
    st.write("Exercício 6")

page_names_to_funcs = {
    "Intro": introducao,
    "Exercício 1": exercicio1,
    "Exercício 2": exercicio2,
    "Exercício 3": exercicio3,
    "Exercício 4": exercicio4,
    "Exercício 5": exercicio5,
    "Exercício 6": exercicio6,
}


demo_name = st.sidebar.selectbox("Selecione uma simulação", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()