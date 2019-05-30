#!/usr/bin/env python
import datetime

def data(dia):
    hoje = datetime.date.today()
    aniversario = datetime.date(1995,6,14)
    return (hoje + datetime.timedelta(days=dia)).strftime('%d/%m/%Y')

def dia_semana(dia):
    Diasemana = ('segunda feira', 'terceira feira', 'quarta feira',
                 'quinta feira', 'sexta feira', 'sabado', 'domingo')
    hoje = datetime.date.today()
    hoje = (hoje + datetime.timedelta(days=dia))
    diadasemana = datetime.date.weekday(hoje)
    if dia == -1: return "Ontem foi " +Diasemana[diadasemana]
    if dia == 0: return "hoje é " + Diasemana[diadasemana]
    if dia == 1: return "amanhã é " + Diasemana[diadasemana]
    return Diasemana[diadasemana]
def mes(mes):
    Meses=('Janeiro','Fevereiro','Março','Abril','Maio','Junho',
    'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
    hoje = datetime.date.today()
    hoje = (hoje + datetime.timedelta(days=mes))
    mes = (hoje.month - 1)
    return Meses[mes]

def dias_faltam(data):
    agora = datetime.date.today()
    return agora.strftime("%j")

