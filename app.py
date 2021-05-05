import math;
import os;
import sys;
import time;
import tkinter
from tkinter import *;
from datetime import datetime;

clear= lambda: os.system ('cls');

def horas_calc ():

    global current_time;

    now = datetime.now();

    current_time = now.strftime("%H:%M:%S");

    return current_time;

clear ();

print('Olá eu sou um Alarme'
'\n ' );

time.sleep (0.5);

pedido = '';

alarme = '';

temporizador = '';

def validação ():

    global pedido;

    print(' Podes:'
    '\n Perguntar-me as horas  (horas)'
    '\n Criar um alarme        (alarme)'
    '\n Criar um temporizador  (temporizador)'
    '\n ');

    time.sleep (0.5);

    pedido = str(input('Então o que deseja?'
    '\n '
    '\n'));

    if pedido != ('horas') and pedido != ('temporizador') and pedido != ('alarme'):

        clear();

        print('Comando Inválido'
        '\n ');

        validação ();
            
validação ();

if pedido == str('horas'):
    clear();

    horas_calc();

    print('\n'
        '\nHoras:', current_time,
        '\n '
        '\nPressione Qualquer Tecla para Fechar'
        '\n');
    input();
    

if pedido == str('temporizador'):

    clear();
    def val_temporizador ():

        global temporizador;

        temporizador = str(input('Daqui a quanto tempo quer que o temporizador toque? (hh:mm) '
        '\n'
        '\n'));

        clear();

        if len(temporizador) != 5 or not temporizador.replace(':','').isdigit():

            clear();

            print('Hora Inválida'
            '\n');

            val_temporizador();

    val_temporizador();

    dezenas_horas =  temporizador [0];

    unidades_horas =  temporizador [1];

    dezenas_minuto = temporizador [3];

    unidades_minuto = temporizador [4];

    horas = int(dezenas_horas) * 10 + int(unidades_horas);

    minutos = int(dezenas_minuto) * 10 + int(unidades_minuto);

    tempo_temporizador = int(horas * 3600 + minutos * 60);

    horas_str = str(horas);

    minutos_str = str(minutos);

    aviso = str(input('Escolhe um nome para o teu temporizador '
    '\n'
    '\n'));

    clear();

    def val_musica ():

        global musica;

        musica = str(input('Escolhe uma musica para o teu alarme'
        '\n'
        '\n Alarme Samsung    (musica1)'
        '\n Alarme Iphone     (musica2)'
        '\n Acordaaaa         (musica3)'
        '\n Alarme Guerra     (musica4)'
        '\n'
        '\n'));

        clear();
    
        if musica !=('musica1') and musica !=('musica2') and musica !=('musica3') and musica !=('musica4'):

            clear();

            print('Musica Inválida'
            '\n');

            val_musica();

    val_musica();

    print(str(aviso + ' definido para daqui a ' + horas_str + ' hora(s) e ' + minutos_str + ' minuto(s)'))
    
    time.sleep(int(tempo_temporizador));

    if musica ==('musica1'):
        
        os.system('cmd /c "start D:/Alarme/alarme1.mp3"');

    elif musica == ('musica2'):

        os.system('cmd /c "start D:/Alarme/alarme2.mp3"');

    elif musica == ('musica3'):

        os.system('cmd /c "start D:/Alarme/alarme3.mp3"');

    elif musica == ('musica4'):

        os.system('cmd /c "start D:/Alarme/alarme4.mp3"');

    os.system("exit");

    clear();

    print('**' + aviso.upper() + '**');

    print('Pressiona qualquer tecla para desligar');

    input();

    os.system('cmd /c "Taskkill /IM "Music.UI.exe" /F"');

    os.system("exit");

    clear();

if pedido == ('alarme'):

    clear();

    

    def val_alarme():

        global alarme;

        alarme = str(input('Escolhe a hora a que queres que o teu alarme toque (hh:mm) '
        '\n'
        '\n'));

        if len(alarme) != 5 or not alarme.replace(':','').isdigit():

            clear();

            print ('Hora Inválida'
            '\n');

            val_alarme();

    val_alarme();

    clear();

    dezenas_horas =  alarme [0];

    unidades_horas =  alarme [1];

    dezenas_minuto = alarme [3];

    unidades_minuto = alarme [4];

    horas = int(dezenas_horas) * 10 + int(unidades_horas);

    minutos = int(dezenas_minuto) * 10 + int(unidades_minuto);

    tempo_alarme = int(horas * 3600 + minutos * 60);

    horas_str = str(horas);

    minutos_str = str(minutos);

    horas_calc();

    dezenas_horas_atuais = current_time [0];

    unidades_horas_atuais =  current_time [1];

    dezenas_minuto_atuais = current_time [3];

    unidades_minuto_atuais = current_time [4];

    horas = int(dezenas_horas_atuais) * 10 + int(unidades_horas_atuais);

    minutos = int(dezenas_minuto_atuais) * 10 + int(unidades_minuto_atuais);
    
    tempo_atual = int(horas * 3600 + minutos * 60);

    aviso = str(input('Escolhe um nome para o teu alarme '
    '\n'
    '\n'));

    clear();

    def val_musica ():

        global musica;

        musica = str(input('Escolhe uma musica para o teu alarme'
        '\n'
        '\n Alarme Samsung    (musica1)'
        '\n Alarme Iphone     (musica2)'
        '\n Acordaaaa         (musica3)'
        '\n Alarme Guerra     (musica4)'
        '\n'
        '\n'));

        clear();
    
        if musica !=('musica1') and musica !=('musica2') and musica !=('musica3') and musica !=('musica4'):

            clear();

            print('Musica Inválida'
            '\n');

            val_musica();

    val_musica();

    print(str(aviso + ' definido para as ' + horas_str + ' hora(s) e ' + minutos_str + ' minuto(s)'));

    if tempo_alarme > tempo_atual:
        tempo_espera = (tempo_alarme - tempo_atual);

    elif tempo_alarme < tempo_atual:
        tempo_espera = (43200 - tempo_atual + 43200 + tempo_alarme);

    time.sleep(int(tempo_espera));

    if musica ==('musica1'):
        
        os.system('cmd /c "start D:/Alarme/alarme1.mp3"');

    elif musica == ('musica2'):

        os.system('cmd /c "start D:/Alarme/alarme2.mp3"');

    elif musica == ('musica3'):

        os.system('cmd /c "start D:/Alarme/alarme3.mp3"');

    elif musica == ('musica4'):

        os.system('cmd /c "start D:/Alarme/alarme4.mp3"');
        
    os.system("exit");

    clear();

    print('**' + aviso.upper() + '**');

    print('Pressiona ENTER para desligar');

    input();

    os.system('cmd /c "Taskkill /IM "Music.UI.exe" /F"');

    os.system("exit");

    clear();