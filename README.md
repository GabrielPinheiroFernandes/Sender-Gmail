# Envio de E-mails em Python

Este projeto é um script simples em Python para enviar e-mails utilizando o servidor SMTP do Gmail. Ele utiliza as bibliotecas padrão `smtplib`, `email.mime.text` e `email.mime.multipart` para compor e enviar a mensagem.

## Pré-requisitos

- Python 3.x
- Biblioteca `smtplib` (inclusa no Python padrão)
- Conta de e-mail do Gmail

## Configuração

1. **Habilite a autenticação em duas etapas** na sua conta do Google. Isso é necessário para gerar uma senha de aplicativo.
2. **Gere uma senha de aplicativo**:
   - Acesse [Gerenciamento de Conta Google](https://myaccount.google.com/apppasswords).
   - Selecione "Aplicativo" e escolha "Outro" (nomeie como desejar).
   - Copie a senha gerada.

3. **Configuração do script**:
   - Substitua `seu_email@gmail.com` pelo seu e-mail no campo `username`.
   - Cole a senha de aplicativo no campo `password`.
   - Altere `from_email` e `to_email` para o remetente e destinatário desejados.

## Execução

Para executar o script, use o seguinte comando no terminal:

```bash
python nome_do_seu_script.py
```

## Exemplo de Saída

Se a configuração estiver correta, você verá a seguinte mensagem no console:

```
E-mail enviado com sucesso!
```

## Notas

- Certifique-se de que o seu firewall ou software de segurança permite conexões SMTP.
- Este script é um exemplo básico e pode ser aprimorado para incluir recursos como envio de anexos, HTML, entre outros.

## Licença

Este projeto está licenciado sob a MIT License.
