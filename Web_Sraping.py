#Importando bibliotecas
from bs4 import BeautifulSoup
import requests as rq
import streamlit as st

#Realizando a solicitação
pagina = rq.get("https://www.pensador.com/autor/richard_feynman/")

# Extraindo o codigo html da página
extrato = BeautifulSoup(pagina.text,'html.parser')

# Filtrando as tags correspondetes
filtro = extrato.find_all('p', class_= "frase fr",)


# Criando uma lista com as frases
lista_de_frases = []

for frase in filtro:
    lista_de_frases.append(frase.get_text())

for i in lista_de_frases:
    print(i)

# Streamlit 

st.set_page_config(page_title="Frases Richard Feyman", page_icon="feyman_page_icon.jpg")

col1, col2 = st.columns([3,1])

with col1:

    st.markdown("### Frases - Richard Feyman")

    st.write("Este é um mini site streamlit sobre as frases mais famosas do físico estadunidense richard feyman."
    " Este site foi feito com o objetivo de exibir as informações obtidas com o web scraping (BeautifulSoup4).")

    st.write("As informações foram extraídas do site \"O pensador\", disponível no link abaixo:")

    st.write("https://www.pensador.com/autor/richard_feynman/")

with col2:

    st.image("Richard_Feynman.png")

botao1 = st.button("Ver frases", icon="🧠", use_container_width=True)

if botao1 :

    lista_imagens = ["chato.png", "religiao.jpg","estrela.png","ciencia.png","atomo.png","quantum_mechanicis.jpg","nao_deve.png",
                     "estudar.jpg","liberdade.png","incerteza.png","descoberta.png","idiota.png","mentira.png","pergunta.png",
                     "analisar.png"
                    ]

    #imprimido as frases + imagens correspondentes

    for frase_na_lista in range (len((lista_de_frases))) :

        col1, col2 = st.columns([8,1])
        
        with col1:

            st.write(lista_de_frases[frase_na_lista])

        with col2:

            st.image(lista_imagens[frase_na_lista])


for item in lista_de_frases:
    print(item)

