"""
URL configuration for agenda_pericias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app_agenda_pericias import views

urlpatterns = [
    path('', views.index, name='index,'),
    path('home/', views.home, name='home'),
    path('verificar_cpf/', views.verificar_cpf, name='verificar_cpf'),
    path('verificar_perito/', views.verificar_perito, name='verificar_perito'),    
    path('agenda_pericias/', views.agendar_pericias , name='agendar_pericias'),
    path('listagem/', views.listagem_pericias , name='listagem_pericias'),
    path('listagem_pericias/', views.listagem_completa_pericias , name='listagem_completa_pericias'),
    path('editar_pericia/<int:id>', views.editar_pericia, name='editar_pericia'),
    path('editar_listagem_pericia/<int:id>', views.editar_listagem_pericia, name='editar_listagem_pericia'),
    path('confirmacao/',views.confirmacao, name='confirmacao'),
    path("atualizar_comparecimento/", views.atualizar_comparecimento, name="atualizar_comparecimento"),
    path("atualizar_comparecimento_1/", views.atualizar_comparecimento_1, name="atualizar_comparecimento_1"),
    path('atualizar/<int:id>/', views.atualizar_saida_pericia, name='atualizar_saida_pericia'),
    path('login/', views.login, name='login'),
    path('import_excel/', views.import_excel , name='import_excel'),
    path('logout/', views.user_logout , name='logout'),
    path('pericias-por-especialidade/', views.pericias_por_especialidade, name='pericias_por_especialidade'),
    path('pericias-nao-realizadas/', views.pericias_nao_realizadas, name='pericias_nao_realizadas'),    
    path('pericias-por-perito/', views.pericias_por_perito, name='pericias_por_perito'),
    path('agendamento-por-tipo/', views.agendamentos_por_tipo , name='agendamento_por_tipo'),
    path('peritos/', views.listar_peritos, name='listar_peritos'),
    path('relatorio/', views.relatorio_pericias, name='relatorio_pericias'),
    path('relatorio_perito/', views.listagem_pericias_por_perito_mes, name='listagem_pericias_por_perito_mes'),
    path('gerar_pdf/', views.gerar_pdf, name='gerar_pdf'),    
    path('gerar_pdf_perito/', views.gerar_pdf_perito, name='gerar_pdf_perito'),    
    path('listagem_por_perito/', views.listagem_pericias_por_perito, name='listagem_pericias_por_perito'),    
    path('atualiza/', views.atualizar_registros_pericias, name='atualizar_registros_pericias'),
    path('enviar_pauta/', views.enviar_pauta_view, name='enviar_pauta'),    
]