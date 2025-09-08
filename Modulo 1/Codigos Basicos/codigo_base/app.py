import streamlit as st
import app2_imc as imc
st.title("meu app incrivel😁")
st.caption("feito com streamlit.")
st.write("texto,*italico, **negrito**")


with st.form("formulario_imc"):
        peso = st.number_input("peso em kg:",min_value=0.0,max_value=300.0)
        altura = st.number_input("altura em metros:",min_value=0.1,max_value =2.11 )

        calcular =st.form_submit_button("calcular imc")

if calcular:
    valor_imc = imc.calcula_imc(peso=peso,altura=altura)
    categoria,status = imc.tabela_imc(valor_imc)


    st.progress(min(valor_imc/40,1.0))
    
    if status == "success":
        st.success(f"{valor_imc:.2f}")
    elif status == "info":
        st.info(f"{valor_imc:.2f}")
    elif status == "warning":
        st.warning(f"{valor_imc:.2f}")
    else:
        st.error(f"{valor_imc:.2f}")

    

with st.sidebar:
    st.subheader("programas")
    
