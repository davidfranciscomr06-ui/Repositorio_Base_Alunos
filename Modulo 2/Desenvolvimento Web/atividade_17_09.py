import streamlit as st
import app2_imc as nt

nome = st.title('Boletim escolar 🏫')
bimestre = st.caption('veja seu boletim do bimestre')
st.write('****')

with st.form('formulario_boletim'):
    nota1= st.number_input('nota1 :',min_value=0.0, max_value=10.0)
    nota2= st.number_input('nota2 :',min_value=0.0, max_value=10.0)
    nota3= st.number_input('nota3 :',min_value=0.0, max_value=10.0)
    nota4= st.number_input('nota4 :',min_value=0.0, max_value=10.0)

    calcular =  st.form_submit_button('Calcular a media')
   
if calcular:
    valor_nota = nt.calcula_media(nota1,nota2,nota3,nota4)
    status = nt.tabela_nota(valor_nota)


    if status == "aprovado":
        st.success(f"{valor_nota:.2f}")
        st.write("aprovado")

    elif status == "recuperaçao":
        st.warning(f"{valor_nota:.2f}")
        st.write("recuperaçao")
    else:
        st.error(f"{valor_nota:.2f}")
        st.write("reprovado")

with st.sidebar:
    st.subheader('Programas')
