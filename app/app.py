import streamlit as st
from phys_utils import *
import numpy as np
import math

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
        
        Retorno: (Aceleração, Tração 1, Tração 2, Tração 3)
        """
    )

    st.write("### Exercício 2")
    st.image(image="images/ex2.png", width=400)
    st.markdown(
        """
        Variáveis: (Massa 1, Massa 2, Atrito, Gravidade)
        
        Retorno: (Aceleração, Tração)
        """
    )

    st.write("### Exercício 3")
    st.image(image="images/ex3.png")
    st.markdown(
        """
        Variáveis: (Massa 1, Massa 2, Gravidade)

        Retorno: (Aceleração, Tração)
        """
    )

    st.write("### Exercício 4")
    st.image(image="images/ex4.png")
    st.markdown(
        """
        Variáveis: (Massa 1, Massa 2, Ângulo, Gravidade)

        Retorno: (Aceleração, Tração)
        """
    )

    st.write("### Exercício 5")
    st.image(image="images/ex5.png")
    st.markdown(
        """
        Variáveis: (Número de Objetos, Razão da Progressão Aritmética, Massas definidas pela progressão, Força, Atrito)

        Retorno: (Aceleração, Tração N)
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
    
    #Força de atrito 1
    forca_atrito_1 = calcula_atrito(massa1,atrito,10)
    
    #Normal e força de atrito 2
    forca_atrito_2 = calcula_atrito(massa2,atrito,10)

    #Normal e força de atrito 3
    forca_atrito_3 = calcula_atrito(massa3,atrito,10)

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
        st.write(f"## Aceleração: {round(aceleracao,2)} m/s²")
        #Tração 1
        tension1 = massa_total + forca_atrito_total
        st.write(f"## Tração 1: {round(tension1,2)} N")
        #Tração 2
        tension2 = ((massa2+massa3)*aceleracao) + (forca_atrito_2+forca_atrito_3)
        st.write(f"## Tração 2: {round(tension2,2)} N")
        #Tração 3
        tension3 = (massa3*aceleracao) + (forca_atrito_3)
        st.write(f"## Tração 3: {round(tension3,2)} N")

    
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

    #Variáveis
    tensao = massa2*gravidade
    forca_atrito = calcula_atrito(massa1, atrito, gravidade)
    if forca_atrito>= tensao:
        aceleracao=0
    else:
        aceleracao = (tensao-forca_atrito)/massa1+massa2
    #Output
    # Aceleração, Tração
    st.write(f"## Tração: {round(tensao,2)} N")
    st.write(f"## Aceleração: {round(aceleracao,2)} m/s²")

    st.sidebar.success("Valores não especificados usarão os valores placeholder.")

def exercicio3():
    st.write("# Exercício 3")
    st.image(image="images/ex3.png")

    #Inputs
    with st.sidebar:
        massa1 = setMassa("Massa 1", 10)
        massa2 = setMassa("Massa 2", 10)
        gravidade = setGravidade("Gravidade", 10)


    #Output
    #Aceleração, Tração
    peso1 = massa1*gravidade
    peso2 = massa2*gravidade

    maior_peso = peso1 if peso1>peso2 else peso2
    menor_peso = peso1 if peso1<peso2 else peso2

    if massa1+massa2 == 0:
        st.write("## Massa total é zero, impossível de continuar o cálculo")
    else:
        aceleracao = (maior_peso-menor_peso)/(massa1+massa2)
        st.write(f"## Aceleração: {round(aceleracao,2)} m/s²")
        peso_total = peso1+peso2
        massa_total = massa1+massa2

        tensao = peso_total + massa_total*aceleracao
        st.write(f"## Tração: {round(tensao,2)} N")
        

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

    #Output
    #Retorno: (Aceleração, Tração)
    peso1 = massa1*gravidade
    peso1x = peso1*np.sin(math.radians(angulo))
    peso2 = massa2*gravidade

    aceleracao = (peso2-peso1x)/(massa1+massa2)
    tensao = peso1x + massa1 * aceleracao
    if tensao<0: tensao=tensao*-1
    st.write(f"## Tração: {round(tensao,2)} N")
    if aceleracao<0: aceleracao = aceleracao*-1
    if peso1x!=peso2:
        direcao = "em direção a M1" if peso1x>peso2 else "em direção a M2"
    else: direcao=""
    st.write(f"## Aceleração: {round(aceleracao,2)} m/s² {direcao}")

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
        numero_n = st.number_input(label="Número N que deseja ver", min_value=1, max_value=num_objetos)

        #Cálculo da massa N
        massaN = lambda N,razao,massa1: massa1+(N*razao)

        massa_final = massaN(num_objetos,razao_progressao,massa1)
        massa_total = (num_objetos*(massa1*massa_final))/2
        peso_total = massa_total*10
        atrito_total = atrito*(peso_total)
        
        if atrito_total>= forca:
            aceleracao=0
            tensaoN = forca
        else:
            aceleracao = (forca-atrito_total)/massa_total
            #Tração N é a soma das massas até N vezes a aceleração
            tensaoN = massaN(numero_n,razao_progressao,massa1)*aceleracao

    st.write(f"## Aceleração: {aceleracao} m/s²")
    st.write(f"## Tração N: {tensaoN} N")

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

    #Output
    #Retorno: (Aceleração, ForçaAB, ForçaBC)

    massa_total = massaA+massaB+massaC
    if(massa_total==0):
        st.write("Massa total é zero, impossível continuar os cálculos")
    else:
        peso1 = massaA*10
        peso2 = massaB*10
        peso3 = massaC*10
        forca_atrito_total = (atrito*peso1)+(atrito*peso2)+(atrito*peso3)

        aceleracao = (forca-forca_atrito_total)/massa_total
        if forca-forca_atrito_total<0: aceleracao=0
    
        forcaAB = forca-(massaA*aceleracao)
        forcaBC = forca-((massaA+massaB)*aceleracao)

        st.write(f"## Aceleração: {aceleracao} m/s²")
        st.write(f"## Força AB: {forcaAB} N")
        st.write(f"## Força BC: {forcaBC} N")
        

    st.sidebar.success("Valores não especificados usarão os valores placeholder.")
    st.sidebar.success("Para esse exercício, utilizamos gravidade = 10 m/s²")


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