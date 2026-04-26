import streamlit as st
from fpdf import FPDF

# Configuração da página
st.set_page_config(page_title="Certificado - Trilha de Automação", layout="centered")

def gerar_certificado_pdf(nome):
    # Criar PDF em formato paisagem (Landscape)
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    
    # Borda decorativa - Alterada para o VERDE Produttivo (34, 197, 94)
    pdf.set_line_width(5)
    pdf.set_draw_color(34, 197, 94) 
    pdf.rect(10, 10, 277, 190)
    
    # Título
    pdf.set_font("Arial", "B", 45)
    pdf.set_text_color(30, 41, 59)
    pdf.ln(30)
    pdf.cell(0, 20, "CERTIFICADO", ln=True, align="C")
    
    # Subtítulo baseado na trilha
    pdf.set_font("Arial", "", 20)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 15, "MESTRE DA AUTOMAÇÃO", ln=True, align="C")
    
    pdf.ln(15)
    pdf.set_font("Arial", "I", 15)
    pdf.cell(0, 10, "Concedido a:", ln=True, align="C")
    
    # Nome do Aluno - Alterado para o VERDE Produttivo (34, 197, 94)
    pdf.set_font("Arial", "B", 35)
    pdf.set_text_color(34, 197, 94)
    pdf.cell(0, 30, nome.upper(), ln=True, align="C")
    
    # Descrição das competências
    pdf.ln(5)
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(71, 85, 105)
    texto = (
        "Pela excelência na trilha de automação, demonstrando domínio em conectividade via APIs e Webhooks, "
        "estruturação de dados em JSON e criação de fluxos inteligentes entre Intercom e Zapier."
    )
    pdf.multi_cell(0, 10, texto, align="C")
    
    # Regra de Ouro
    pdf.ln(20)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 10, '"Se você fez algo manual mais de 3 vezes, pode automatizar."', ln=True, align="C")
    
    return pdf.output()

# Interface do Streamlit
st.title("🏆 Parabéns pela Conclusão!")
st.write("Você chegou ao final da nossa jornada. Agora, vamos oficializar sua entrega das chaves no mundo da automação.")

nome_usuario = st.text_input("Digite seu nome completo como deseja no certificado:")

if st.button("Gerar meu Certificado"):
    if nome_usuario:
        try:
            pdf_output = gerar_certificado_pdf(nome_usuario)
            st.success(f"Excelente trabalho, {nome_usuario}! Seu certificado está pronto.")
            
            st.download_button(
                label="Baixar Certificado em PDF",
                data=bytes(pdf_output),
                file_name=f"Certificado_Automacao_{nome_usuario.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
        except Exception:
            st.error("Houve um erro ao gerar o arquivo. Tente novamente.")
    else:
        st.warning("Por favor, preencha seu nome antes de gerar o documento.")
