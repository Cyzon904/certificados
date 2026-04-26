import streamlit as st
from fpdf import FPDF

# Configuração da página para ficar com um visual limpo
st.set_page_config(page_title="Certificado – Mestre da Automação", layout="centered")

def gerar_pdf(nome):
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    
    # Borda decorativa azul
    pdf.set_line_width(5)
    pdf.set_draw_color(37, 99, 235) 
    pdf.rect(10, 10, 277, 190)
    
    # Título principal
    pdf.set_font("Arial", "B", 45)
    pdf.set_text_color(30, 41, 59)
    pdf.ln(30)
    pdf.cell(0, 20, "CERTIFICADO", ln=True, align="C")
    
    # Subtítulo da trilha
    pdf.set_font("Arial", "", 20)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 15, "MESTRE DA AUTOMAÇÃO", ln=True, align="C")
    
    pdf.ln(15)
    pdf.set_font("Arial", "I", 15)
    pdf.cell(0, 10, "Concedido a:", ln=True, align="C")
    
    # Nome do Aluno em destaque
    pdf.set_font("Arial", "B", 35)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 30, nome.upper(), ln=True, align="C")
    
    # Descrição das competências
    pdf.ln(5)
    pdf.set_font("Arial", "", 14)
    pdf.set_text_color(71, 85, 105)
    texto = (
        "Pela conclusão da trilha de conhecimento em tecnologia e automação de processos, "
        "demonstrando domínio nas ferramentas Intercom, Zapier, Jira e lógica em Python."
    )
    pdf.multi_cell(0, 10, texto, align="C")
    
    # Frase final – O mantra da trilha
    pdf.ln(20)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, '"Se fez mais de 3 vezes, pode automatizar."', ln=True, align="C")
    
    return pdf.output()

# Interface do Aplicativo
st.title("🏆 Parabéns pela Conclusão!")
st.write("Você chegou ao final da nossa jornada. Agora, vamos oficializar sua entrega das chaves no mundo da automação.")

# Campo para o nome
nome_usuario = st.text_input("Digite seu nome completo como deseja no certificado:")

if st.button("Gerar meu Certificado"):
    if nome_usuario:
        try:
            pdf_bytes = gerar_pdf(nome_usuario)
            st.success(f"Excelente trabalho, {nome_usuario}! Seu certificado está pronto.")
            
            st.download_button(
                label="Clique aqui para baixar seu PDF",
                data=pdf_bytes,
                file_name=f"Certificado_Automacao_{nome_usuario.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error("Houve um erro ao gerar o arquivo. Tente novamente.")
    else:
        st.warning("Por favor, preencha seu nome antes de gerar o documento.")
