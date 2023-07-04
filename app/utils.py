import streamlit as st

def setMassa(label, placeholder):
    massa = st.text_input(label=label , placeholder=f"{placeholder} Kg")
    if not massa: massa = placeholder
    else: massa = float(massa)
    if massa<0: massa=0
    return massa

def setAtrito(label, placeholder):
    atrito = st.text_input(label=label, placeholder=f"{placeholder} μ")
    if not atrito: atrito = placeholder
    else: atrito = float(atrito)
    if atrito<0 : atrito = 0
    return atrito

def setForca(label,placeholder):
    forca = st.text_input(label=label, placeholder=f"{placeholder} N")
    if not forca: forca = placeholder
    else: forca = float(forca)
    return forca

def setGravidade(label,placeholder):
    gravidade = st.text_input(label=label, placeholder=f"{placeholder} m/s²")
    if not gravidade: gravidade = placeholder
    else: gravidade = float(gravidade)
    return gravidade

def setAngulo(label,placeholder):
    angulo = st.text_input(label=label, placeholder=f"{placeholder}°")
    if not angulo: angulo = placeholder
    else: angulo = float(angulo)
    if angulo<0: angulo = 0
    return angulo

def setNumObjetos(label,placeholder):
    num_objetos = st.text_input(label=label, placeholder=f"{placeholder} (Número Inteiro, mínimo 1)")
    if not num_objetos: num_objetos = placeholder
    else: num_objetos = int(num_objetos)
    if num_objetos<=0: num_objetos = 1
    return num_objetos

def setRazaoProgressao(label,placeholder):
    razao_progressao = st.text_input(label=label ,placeholder=f"{placeholder} (Número Real, em Kg)")
    if not razao_progressao: razao_progressao = placeholder
    else: razao_progressao = float(razao_progressao)
    if razao_progressao<0: razao_progressao = 0
    return razao_progressao