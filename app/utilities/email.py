from flask import current_app
import os
import resend

def envia_Email(name, subject, sender, msg):
    remetente = os.environ.get('MAIL_DEFAULT_SENDER')
    destinatario = os.environ.get('MAIL_RECIPIENT')
    api_key = os.environ.get('RESEND_API_KEY')

    html_content = f"""
        <h3>Nova mensagem de contato recebida</h3>
        <p><strong>De:</strong> {name} <{sender}></p>
        <p><strong>Assunto:</strong> {subject}</p>
        <hr>
        <p>{msg.replace('\n', '<br>')}</p>
    """

    try:
        params = {
            "from": remetente,
            "to": destinatario,
            "subject": subject,
            "html": html_content,
            "reply_to": remetente,
        }

        resend.Emails.send(params)

        return True, 'Mensagem enviada com sucesso!'
    except Exception as e:
        print(f'LOG - Erro: {e}')

        return False, f'Ocorreu um erro ao enviar a mensagem: {e}'