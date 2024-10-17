import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor de e-mail
smtp_server = 'smtp.gmail.com'  # Servidor SMTP para Gmail
smtp_port = 587  # Porta para TLS

# Credenciais de autenticação
username = 'seu_email@gmail.com'  # Utilize seu endereço de e-mail do Gmail
password = ''  # Utilize uma senha de aplicativo gerada. [Saiba mais sobre como gerar senhas de aplicativo](https://myaccount.google.com/apppasswords)

# Informações do e-mail
from_email = 'seu_email@gmail.com'  # E-mail remetente
to_email = 'destinatario@gmail.com'  # E-mail destinatário
subject = 'E-mail enviado pelo Python'  # Assunto do e-mail
body = '''
Olá,

Este é um e-mail de teste enviado automaticamente pelo seu script Python.

Se você receber este e-mail, significa que a configuração está funcionando corretamente!

Atenciosamente,
Seu Script de Envio de E-mails
'''

# Criação do e-mail
msg = MIMEMultipart()
msg['From'] = from_email  # Adiciona o e-mail remetente
msg['To'] = to_email  # Adiciona o e-mail destinatário
msg['Subject'] = subject  # Adiciona o assunto do e-mail
msg.attach(MIMEText(body, 'plain'))  # Anexa o corpo do e-mail

try:
    # Conexão ao servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)  # Cria uma instância do servidor SMTP
    server.starttls()  # Ativa a criptografia TLS
    server.login(username, password)  # Realiza o login com as credenciais fornecidas
    server.send_message(msg)  # Envia a mensagem
    print('E-mail enviado com sucesso!')  # Mensagem de sucesso
except Exception as e:
    print(f'Falha ao enviar e-mail: {e}')  # Mensagem de erro
finally:
    server.quit()  # Fecha a conexão com o servidor
