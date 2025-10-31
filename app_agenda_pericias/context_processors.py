from django.contrib.auth import get_user_model
from app_agenda_pericias.models import tbl_usuarios, tbl_unidades # Substitua pelo seu modelo de usuário, se necessário

def variaveis_globais(request):
    usuario = None
    nome = None
    unidade = None
    subsecao = None
    disable_pericias = False
    disable_informacoes = False    
    disable_atualizar = False
    disable_area_perito = False

    usuario_id = request.session.get('usuario_id')
    unidade_sessao = request.session.get('unidade')
    
    if usuario_id:
        try:
            usuario = tbl_usuarios.objects.get(pk=usuario_id)
            nome = usuario.nome

            # Verifica se é perito
            is_perito = bool(usuario.perito)
            
            # Define a unidade conforme o tipo de usuário
            if is_perito:
                unidade = unidade_sessao
            else:
                unidade = usuario.unidade

            # Obtém a subseção com base na unidade
            if unidade:
                subsecao = tbl_unidades.objects.get(pk=unidade)
            
            # Controle de visibilidade
            disable_pericias = is_perito
            disable_atualizar = is_perito
            disable_informacoes = is_perito
            disable_area_perito = not is_perito

        except tbl_usuarios.DoesNotExist:
            pass

    return {
        'usuario': usuario,
        'nome': nome,
        'unidade': unidade,
        'subsecao': subsecao,
        'disable_pericias': disable_pericias,
        'disable_informacoes': disable_informacoes,
        'disable_atualizar': disable_atualizar,
        'disable_area_perito': disable_area_perito,
    }
