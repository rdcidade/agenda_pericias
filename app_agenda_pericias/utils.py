# app_agenda_pericias/utils.py
from django.core.mail import send_mail
from django.utils import timezone
from app_agenda_pericias.models import tbl_pericias_agendadas, tbl_usuarios
from datetime import datetime
from django.utils.html import strip_tags

def montar_corpo_perito(pericias, perito_nome, mes_ano_str):
    """
    Monta corpo do e-mail em HTML com tabela (Data, Hora, Periciado, Processo, Local).
    Recebe:
      - pericias: iterable de objetos (cada objeto tem data_marcada, hora_marcada, periciado, processo, jurisdicao)
      - perito_nome: string com o nome do perito
      - mes_ano_str: string para o header do e-mail (ex: '10/2025')
    Retorna: tupla (plain_text, html_body)
    """
    # Texto simples (fallback)
    linhas_texto = [f"Pauta de Perícias - {mes_ano_str}", f"Perito: {perito_nome}", ""]
    for p in pericias:
        data_str = p.data_marcada.strftime('%d/%m/%Y') if getattr(p, 'data_marcada', None) else ''
        hora_str = p.hora_marcada.strftime('%H:%M:%S') if getattr(p, 'hora_marcada', None) else ''
        linhas_texto.append(f"{data_str} {hora_str} | {p.periciado} | {p.processo} | {p.jurisdicao or ''}")

    plain_text = "\n".join(linhas_texto)

    # HTML
    html = f"""
    <html>
    <head>
      <meta charset="UTF-8">
      <style>
        table {{
          border-collapse: collapse;
          width: 100%;
          font-family: Arial, sans-serif;
          font-size: 12px;
        }}
        th {{
          background-color: #0d6efd;
          color: #ffffff;
          padding: 8px;
          text-align: center;
          border: 1px solid #ddd;
        }}
        td {{
          padding: 8px;
          border: 1px solid #ddd;
          text-align: left;
        }}
        tr:nth-child(even) {{
          background-color: #f8f9fa;
        }}
        tr:hover {{
          background-color: #e9ecef;
        }}
        h2 {{
          color: #0d6efd;
          text-align: center;
          font-family: Arial, sans-serif;
        }}
        .footer {{
          margin-top: 20px;
          font-size: 13px;
          color: #6c757d;
          text-align: center;
        }}
      </style>
    </head>
    <body style="font-family: Arial, sans-serif; font-size: 13px; color: #333;">
      <p>Prezado(a) Dr(a) <strong>{perito_nome}</strong>,</p>
      <p>Segue abaixo a pauta de perícias para o mês <strong>{mes_ano_str}</strong>:</p>

      <table class="table table-bordered table-striped" style="font-size: 15px; white-space: nowrap">
        <thead>
          <tr style="text-align:center; vertical-align: middle;">
            <th style="border: 1px solid #ddd; padding: 6px;">Data</th>
            <th style="border: 1px solid #ddd; padding: 6px;">Hora</th>
            <th style="border: 1px solid #ddd; padding: 6px;">Periciado</th>
            <th style="border: 1px solid #ddd; padding: 6px;">Processo</th>
            <th style="border: 1px solid #ddd; padding: 6px;">Local</th>
          </tr>
        </thead>
        <tbody>
    """

    # linhas da tabela
    for p in pericias:
        data_html = p.data_marcada.strftime('%d/%m/%Y') if getattr(p, 'data_marcada', None) else ''
        hora_html = p.hora_marcada.strftime('%H:%M:%S') if getattr(p, 'hora_marcada', None) else ''
        periciado_html = p.periciado or ''
        processo_html = p.processo or ''
        local_html = p.jurisdicao or ''
        html += f"""
          <tr style="text-align:center;">
            <td style="border:1px solid #ddd; padding:6px;">{data_html}</td>
            <td style="border:1px solid #ddd; padding:6px;">{hora_html}</td>
            <td style="border:1px solid #ddd; padding:6px; text-align:left;">{periciado_html}</td>
            <td style="border:1px solid #ddd; padding:6px; text-align:left;">{processo_html}</td>
            <td style="border:1px solid #ddd; padding:6px; text-align:left;">{local_html}</td>
          </tr>
        """

    html += """
        </tbody>
      </table>

      <p style="margin-top:20px;">Atenciosamente,<br/><strong>Seção de Perícias</strong></p>
    </body>
    </html>
    """

    return plain_text, html


def enviar_pauta_peritos(mes=None, ano=None, fail_silently=False):
    resumo = {'enviados': [], 'sem_email': [], 'sem_pericias': [], 'erros': []}

    hoje = timezone.now()
    mes = mes or hoje.month
    ano = ano or hoje.year
    mes_ano_str = f"{mes:02d}/{ano}"

    peritos = tbl_usuarios.objects.filter(perito=True).order_by('nome')

    for perito in peritos:
        try:
            if not perito.email:
                resumo['sem_email'].append({'nome': perito.nome})
                continue

            pericias = tbl_pericias_agendadas.objects.filter(
                perito=perito.nome,
                data_marcada__year=ano,
                data_marcada__month=mes,
                situacao_pericia='Designada'
            ).order_by('data_marcada')

            if not pericias.exists():
                resumo['sem_pericias'].append({'nome': perito.nome, 'email': perito.email})
                continue

            # monta corpo (texto e html)
            plain_text, html_body = montar_corpo_perito(pericias, perito.nome, mes_ano_str)

            assunto = f"Pauta de Perícias - {mes_ano_str}"

            # envia com html_message (plaintext fallback)
            send_mail(
                subject=assunto,
                message=plain_text,
                from_email=None,                 # usa DEFAULT_FROM_EMAIL do settings
                recipient_list=[perito.email],
                fail_silently=fail_silently,
                html_message=html_body
            )

            resumo['enviados'].append({'nome': perito.nome, 'email': perito.email, 'count': pericias.count()})

        except Exception as e:
            resumo['erros'].append({'nome': getattr(perito, 'nome', '??'), 'error': str(e)})

    return resumo
