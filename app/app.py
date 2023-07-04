import streamlit as st
from utils import *


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
    st.image(image="images/ex1.png", width=500)
    st.markdown(
        """
        Variáveis: (Massa 1, Massa 2, Massa 3, Atrito, Força)
        
        Retorno: (Aceleração, Tensão 1, Tensão 2, Tensão 3)
        """
    )

    st.write("### Exercício 2")
    st.image(image="images/ex2.png", width=400)
    st.markdown(
        """
        Variáveis: (Massa 1, Massa 2, Atrito, Gravidade)
        
        Retorno: (Aceleração, Tensão)
        """
    )

    st.write("### Exercício 3")
    st.image(image="images/ex3.png")
    st.markdown(
        """
        Variáveis: (Massa 1, Massa 2, Gravidade)

        Retorno: (Aceleração, Tensão)
        """
    )

    st.write("### Exercício 4")
    st.image(image="images/ex4.png")
    st.markdown(
        """
        Variáveis: (Massa 1, Massa 2, Ângulo, Gravidade)

        Retorno: (Aceleração, Tensão)
        """
    )

    st.write("### Exercício 5")
    st.image(image="images/ex5.png")
    st.markdown(
        """
        Variáveis: (Número de Objetos, Razão da Progressão Aritmética, Massas definidas pela progressão, Força, Atrito)

        Retorno: (Aceleração, Tensão N)
        """
    )

    st.write("### Exercício 6")
    st.image(image="images/ex6.png")
    st.markdown(
        """
        Variáveis: (Massa A, Massa B, Massa C, Atrito, Força)

        Retorno: (Aceleração, ForçaAB, ForçaBC)
        """
    )

def exercicio1():
    st.write("# Exercício 1")
    st.image(image="images/ex1.png")

    #Inputs
    with st.sidebar:
        massa1 = setMassa("Massa 1", 10)
        massa2 = setMassa("Massa 2", 10)
        massa3 = setMassa("Massa 3", 10)
        atrito = setAtrito("Atrito",0.1)
        forca = setForca("Força", 10)
        
    #Variáveis
    massa_total = massa1+massa2+massa3
    
    #Normal e força de atrito 1
    normal1 = massa1*10
    forca_atrito_1 = (atrito*normal1)
    
    #Normal e força de atrito 2
    normal2 = massa2*10
    forca_atrito_2 = (atrito*normal2)

    #Normal e força de atrito 3
    normal3 = massa3*10
    forca_atrito_3 = (atrito*normal3)

    #Força de atrito total
    forca_atrito_total = forca_atrito_1+forca_atrito_2+forca_atrito_3

    #Outputs

    #Aceleração
    if massa_total == 0:
        st.write("Massa total é 0. Não se pode continuar os cálculos")
    else:
        if forca_atrito_total<forca:
            aceleracao = (forca - forca_atrito_total)/ (massa_total)
        else:
            aceleracao = 0
        
        #Aceleração
        st.write(f"## Aceleração: {aceleracao} m/s²")
        #Tensão 1
        tension1 = massa_total + forca_atrito_total
        st.write(f"## Tensão 1: {tension1} N")
        #Tensão 2
        tension2 = ((massa2+massa3)*aceleracao) + (forca_atrito_2+forca_atrito_3)
        st.write(f"## Tensão 2: {tension2} N")
        #Tensão 3
        tension3 = (massa3*aceleracao) + (forca_atrito_3)
        st.write(f"## Tensão 3: {tension3} N")

    
    st.sidebar.success("Valores não especificados usarão os valores placeholder.")
    st.sidebar.success("Para esse exercício, assumimos gravidade = 10 m/s²")

def exercicio2():
    st.write("# Exercício 2")
    st.image(image="images/ex2.png")

    #Inputs
    with st.sidebar:
        massa1 = setMassa("Massa 1", 10)
        massa2 = setMassa("Massa 2", 10)
        atrito = setAtrito("Atrito",0.1)
        gravidade = setGravidade("Gravidade", 10)

    st.sidebar.success("Valores não especificados usarão os valores placeholder.")

def exercicio3():
    st.write("# Exercício 3")
    st.image(image="images/ex3.png")

    #Inputs
    with st.sidebar:
        massa1 = setMassa("Massa 1", 10)
        massa2 = setMassa("Massa 2", 10)
        gravidade = setGravidade("Gravidade", 10)

    st.sidebar.success("Valores não especificados usarão os valores placeholder.")


def exercicio4():
    st.write("# Exercício 4")
    st.image(image="images/ex4.png")

    #Inputs
    with st.sidebar:
        massa1 = setMassa("Massa 1", 10)
        massa2 = setMassa("Massa 2", 10)
        angulo = setAngulo("Angulo", 30)
        gravidade = setGravidade("Gravidade", 10)

    st.sidebar.success("Valores não especificados usarão os valores placeholder.")

def exercicio5():
    st.write("# Exercício 5")
    st.image(image="images/ex5.png")

    #Inputs
    with st.sidebar:
        massa1 = setMassa("Massa 1", 10)
        num_objetos = setNumObjetos("Número de Objetos",5)
        razao_progressao = setRazaoProgressao("Razão da progressão",10)
        atrito = setAtrito("Atrito",0.1)
        forca = setForca("Forca",10)

        massas_definidas = [massa1 + i * razao_progressao for i in range(num_objetos)]

    st.sidebar.success("Valores não especificados usarão os valores placeholder.")

def exercicio6():
    st.write("# Exercício 6")
    st.image(image="images/ex6.png")

    with st.sidebar:
        massaA = setMassa("Massa A",10)
        massaB = setMassa("Massa B",10)
        massaC = setMassa("Massa C",10)
        atrito = setAtrito("Atrito",0.1)
        forca = setForca("Forca",10)


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