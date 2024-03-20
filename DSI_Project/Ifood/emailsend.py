# Seu código Python (por exemplo, em views.py)
from django.core.mail import send_mail

def enviar_email():
    assunto = 'teste'
    mensagem = 'código teste.'

    send_mail(
        assunto,
        mensagem,
        'andrefelippecarvalho@gmail.com',  # E-mail do remetente
        ['andrefacarvalho@gmail.com'],  # Lista de destinatários
        fail_silently=False,
    )
