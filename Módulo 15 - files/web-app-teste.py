import streamlit as st

st.title('Bem vindo')
st.header('Bem vindo')
st.subheader('Bem vindo')

st.markdown("---")

st.markdown("# Isso é um texto com markdown e um[#]")
st.markdown("## Isso é um texto com markdown e um[##]")
st.markdown("### Isso é um texto com markdown e um[###]")

st.markdown("---")

st.markdown("Markdown")
st.markdown("_Markdown itálico_")
st.markdown("*Markdown itálico*")

st.markdown("__Markdown negrito__")
st.markdown("**Markdown negrito**")

st.markdown("__*Markdown itálico e negrito*__")

st.markdown("Isso é um link pro [google](https://google.com.br)")

st.markdown('''NOME |  SOBRENOME | IDADE
               ---  |    ---     | ---      
            ''')