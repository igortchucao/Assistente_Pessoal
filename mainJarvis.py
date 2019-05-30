import os
from Jarvis.comandos import *
import speech_recognition as sr
from gtts import gTTS
from pygame import *
import mutagen.mp3
'''
Função que faz a criação das falas do Assitente 
- esta função precisa de internet para fazer sua tradução
- os arquivos sao temporarios 
'''

def cria_audio(audio, var):
	tts = gTTS(audio, lang='pt-br')
	tts.save('Audios/'+var+'.mp3')

	mp3 = mutagen.mp3.MP3('Audios/'+var+'.mp3')
	mixer.init(frequency=mp3.info.sample_rate)

	mixer.music.load('Audios/'+var+'.mp3')
	mixer.music.play()
	while mixer.music.get_busy():
		time.Clock().tick(10)
	if var != 'oi':
		mixer.music.load('Audios/end.mp3')
		mixer.music.play()
		os.remove('Audios/'+var+'.mp3')


def chamado():
	microfone = sr.Recognizer()
	with sr.Microphone() as source:
		microfone.adjust_for_ambient_noise(source)
		return microfone.recognize_google(microfone.listen(source), language='pt-BR')

def ouvir_microfone():

	microfone = sr.Recognizer()

	with sr.Microphone() as source:
		microfone.adjust_for_ambient_noise(source)
		audio = microfone.listen(source)
	try:
		frase = microfone.recognize_google(audio,language='pt-BR')
		print("Você disse: " + frase)

	except sr.UnkownValueError:
		print("Não entendi")

def tradutor_de_comando(comando):
	executor = ""
	cont = 0
	for aux in comando:
		if(aux.isdigit()):
			executor = executor + aux
			cont = 1;
		else:
			try:
				arquivo = open('Jarvis/vocabulario/'+aux+'.txt', 'r')
				executor = executor + arquivo.readline()
				arquivo.close()

			except FileNotFoundError:
				arquivo = open('Jarvis/vocabulario/'+aux+'.txt', 'w+')
				significado = input("O que é " + aux + "?")
				arquivo.write(significado)
				arquivo.close()

				arquivo = open('Jarvis/vocabulario/' + aux + '.txt', 'r')
				executor = executor + arquivo.readline()
				arquivo.close()
	if cont == 1:
		executor = executor + ' , "é o valor da conta' + '"' + "), 'temp')"
		cont = 0

	try:
		print(executor)
		exec(executor)
	except SyntaxError or PermissionError:
		print("Comando Invalido")



if __name__ == "__main__":
	while True:
		#é nescesssario ativar o assistente
		#if(input("...") == 'jarvis'):
			cria_audio("Boa tarde Aladjáh", 'oi')
			while True:
				comando = input("digite um comando")
				if(comando == 'sair'):
					break
				else:
					tradutor_de_comando(comando.split())
			break

'''
while True:
	frase = chamado()
	if re.search('jarvis', frase, re.IGNORECASE):
		cria_audio("Bom dia Igor", 'oi')
		while True:
			if(ouvir_microfone() == 'dormir'):
				cria_audio("valeu falou", 'xau')
				break
		break

'''
