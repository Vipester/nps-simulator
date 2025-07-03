import streamlit as st

st.set_page_config(page_title="Simulador de NPS", layout="centered")
st.title("📊 Simulador de NPS")

st.markdown("""
Ajuste os números de **Promotores**, **Neutros** e **Detratores** para simular o resultado do NPS em diferentes cenários. Ideal para planejamentos estratégicos e análises de satisfação.
""")

# Inputs
col1, col2, col3 = st.columns(3)
with col1:
    promotores = st.number_input("Promotores", min_value=0, value=99)
with col2:
    neutros = st.number_input("Neutros", min_value=0, value=73)
with col3:
    detratores = st.number_input("Detratores", min_value=0, value=45)

# Cálculos
total = promotores + neutros + detratores
if total == 0:
    nps = 0
else:
    nps = ((promotores - detratores) / total) * 100

# Resultados
st.markdown("---")
st.subheader("Resultado")
st.metric("Total de Respondentes", total)
st.metric("NPS Calculado", f"{nps:.2f}")

# Distribuição
st.markdown("### Distribuição Percentual")
if total > 0:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"**Promotores:** {promotores} ({promotores/total:.0%})")
    with col2:
        st.write(f"**Neutros:** {neutros} ({neutros/total:.0%})")
    with col3:
        st.write(f"**Detratores:** {detratores} ({detratores/total:.0%})")

# Observação
st.markdown("""
<small>NPS varia de -100 a +100. Uma boa meta é atingir 70 ou mais, o que indica uma alta satisfação e lealdade dos clientes.</small>
""", unsafe_allow_html=True)
