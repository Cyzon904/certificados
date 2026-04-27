import streamlit as st
from fpdf import FPDF

# Configuracao da pagina
st.set_page_config(page_title="Certificado - Trilha de Automação", layout="centered")

def gerar_certificado_pdf(nome):
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    
    try:
        pdf.add_font('Comfortaa', '', 'Comfortaa-Regular.ttf')
        pdf.add_font('Comfortaa', 'B', 'Comfortaa-Bold.ttf')
        fonte_principal = 'Comfortaa'
    except:
        fonte_principal = 'Arial'

    pdf.add_page()
    
    # Borda em verde Produttivo
    pdf.set_line_width(5)
    pdf.set_draw_color(34, 197, 94) 
    pdf.rect(10, 10, 277, 190)
    
    # Titulo
    pdf.set_font(fonte_principal, 'B', 45)
    pdf.set_text_color(30, 41, 59)
    pdf.ln(30)
    pdf.cell(0, 20, "CERTIFICADO", ln=True, align="C")
    
    # Subtitulo
    pdf.set_font(fonte_principal, '', 20)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 15, "MESTRE DA AUTOMAÇÃO", ln=True, align="C")
    
    pdf.ln(15)
    pdf.set_font(fonte_principal, '', 15)
    pdf.cell(0, 10, "Concedido a:", ln=True, align="C")
    
    # Nome do Aluno
    pdf.set_font(fonte_principal, 'B', 35)
    pdf.set_text_color(34, 197, 94)
    pdf.cell(0, 30, nome.upper(), ln=True, align="C")
    
    # Descricao
    pdf.ln(5)
    pdf.set_font(fonte_principal, '', 12)
    pdf.set_text_color(71, 85, 105)
    texto = (
        "Pela excelência na trilha de automação, demonstrando domínio em conectividade via APIs e Webhooks, "
        "estruturação de dados em JSON e criação de fluxos inteligentes entre Intercom e Zapier."
    )
    pdf.multi_cell(0, 10, texto, align="C")
    
    # Regra de Ouro
    pdf.ln(20)
    pdf.set_font(fonte_principal, 'B', 11)
    pdf.cell(0, 10, '"Se você fez algo manual mais de 3 vezes, pode automatizar."', ln=True, align="C")
    
    return pdf.output()

# Interface do Streamlit
st.title("Parabéns pela Conclusão!")
st.write("Você chegou ao final da nossa jornada. Para liberar seu certificado, resolva o desafio final.")

# Secao do Desafio Final com 3 perguntas
st.markdown("### Teste seus Conhecimentos")

resposta_1 = st.radio(
    "1. Qual ferramenta funciona como o nosso Mestre de Obras, conectando sistemas que não se falam naturalmente?",
    ("Intercom", "Jira", "Zapier", "Pipefy"),
    index=None
)

resposta_2 = st.radio(
    "2. Na nossa analogia do restaurante, o que é uma API?",
    (
        "Um banco de dados de senhas.",
        "O garçom que leva o pedido de um sistema para o outro e traz o prato pronto.",
        "Um robô de atendimento do WhatsApp.",
        "Uma tela de configuração do sistema."
    ),
    index=None
)

resposta_3 = st.radio(
    "3. O que é um Workflow no Intercom?",
    (
        "Um mapa de decisões lógicas que o robô segue para organizar a fila e tomar ações.",
        "O histórico de mensagens apagadas do cliente.",
        "A central de ajuda com artigos em texto.",
        "Uma planilha externa do Google Sheets."
    ),
    index=None
)

st.markdown("---")

nome_usuario = st.text_input("Digite seu nome completo como deseja no certificado:")

if st.button("Gerar meu Certificado"):
    
    # Respostas corretas definidas aqui para facilitar
    resp_1_correta = "Zapier"
    resp_2_correta = "O garçom que leva o pedido de um sistema para o outro e traz o prato pronto."
    resp_3_correta = "Um mapa de decisões lógicas que o robô segue para organizar a fila e tomar ações."

    # Validacao 1: Nome preenchido
    if not nome_usuario:
        st.warning("Por favor, preencha seu nome primeiro.")
        
    # Validacao 2: Respostas corretas
    elif resposta_1 != resp_1_correta or resposta_2 != resp_2_correta or resposta_3 != resp_3_correta:
        st.error("Ops! Parece que alguma resposta está incorreta. Revise o material da trilha e tente novamente, você consegue!")
        
    # Sucesso: Tudo certo
    else:
        st.balloons()
        try:
            pdf_output = gerar_certificado_pdf(nome_usuario)
            st.success(f"Excelente trabalho, {nome_usuario}! Seu certificado está pronto.")
            
            st.download_button(
                label="Baixar PDF",
                data=bytes(pdf_output),
                file_name=f"Certificado_{nome_usuario.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error("Erro ao gerar. Verifique se os ficheiros da fonte estao na pasta.")
