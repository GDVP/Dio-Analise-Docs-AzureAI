import streamlit as st
from services.blob_services import upload_blob
from services.credit_card_service import analize_credit_card


def configure_interface():
    st.title('Upload de Arquivo - Desafio 1 - Azure - Fake Docs')
    uploaded_file = st.file_uploader('Escolha um arquivo', type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        #Envia para o blob storage
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f'Arquivo {fileName} enviado com sucesso para o Azure Blob Storage.')
            credit_card_info = analize_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f'Erro ao enviar o arquivo {fileName} para o Azure Blob Storage')

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption='Imagem enviada', use_column_width=True)
    st.write('Resultado da validação:')
    if credit_card_info and credit_card_info['card_name']:
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f'Nome do Titular: {credit_card_info['card_name']}')
        st.write(f'Banco Emissor: {credit_card_info['bank_name']}')
        st.write(f'Data de Validade: {credit_card_info['expiration_date']}')
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=False)
        st.write(f'Este não é um cartão de crédito válido.')


if __name__ == '__main__':
    configure_interface()


#02/11/2025: Para executar este app usando streamlit:
# 1. Navegue via CMD com o ambiente virtual (python) ativo, até o diretório 'src/' onde está esta aplicação 'app.py'.
# 2. Em seguida, execute o comando:
    # streamlit run .\app.py
# Obs.: Note que usamos variáveis de ambiente 'load_dotenv', as variaveis necessárias (tal como endpoint, key, entre outras) devem estar na pasta '.env' no diretório acima de 'src/', caso contrário a aplicação não funcionará.
