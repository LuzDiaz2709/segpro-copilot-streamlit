import streamlit as st

# Configuración básica de la página
st.set_page_config(
    page_title="Asistente PostVenta SEGPRO",
    page_icon="🛠️",
    layout="wide"
)

# Título principal
st.title("🤖 Asistente PostVenta SEGPRO")

st.markdown(
    """
    Bienvenido al asistente de postventa de **SEGPRO** 🧤🦺  
    Aquí puedes hacer consultas sobre pedidos, garantías, cambios, devoluciones y soporte de EPP.
    """
)

# ✅ AQUÍ SOLO VA LA URL DEL SRC, NADA MÁS
iframe_code = """
<iframe
    src="https://copilotstudio.microsoft.com/environments/Default-3209b50b-b79b-43dc-9fc4-8d42c406dd61/bots/cr0ac_asistentePostVentaSegpro/webchat?__version__=2"
    style="width: 100%; height: 750px; border: none;"
    allow="microphone; camera"
    sandbox="allow-scripts allow-same-origin allow-forms allow-popups"
></iframe>
"""

# Render del iframe en Streamlit
st.components.v1.html(iframe_code, height=800)

