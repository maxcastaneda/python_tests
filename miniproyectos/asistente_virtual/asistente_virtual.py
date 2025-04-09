import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# escuchar microfono y devolver el audio como texto
def  audio_en_texto():

    # alamcenar recognizer en una variable
    r = sr.Recognizer()

    # configuirar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_theshold = 0.8

        # informar que comenzo la grabacion
        print("ya puedes hablar...")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google 
            pedido = r.recognize_google(audio, language="es-mx")

            # prueba de que se interpreto el audio
            print("Dijiste: " + pedido)

            return pedido

        except sr.UnknownValueError:
            print ("ups, no entendi")
            return "sigo esperando"

        except sr.RequestError:
            print ("ups, no se puede conectar con google")
            return "sigo esperando"
        
        except:
            print ("ups, error inesperado")
            return "sigo esperando"

# emitir voz del asisente
def hablar(mensaje):

    # encender el motor pyttsx3
    engine = pyttsx3.init()
    id1= r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
    engine.setProperty('voice',id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# pedir dia
def pedir_dia():
    
    dia = datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()    
    calendario = {0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Viernes", 5:"Sabado",6:"Domingo"}
    print(calendario[dia_semana])

    #decir el dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")
                   
# pedir hora
def pedir_hora():

    orita = datetime.datetime.now()
    print(orita)

    # decir hora
    orita_chida = f"en este momento son las {orita.hour} horas con {orita.minute} minutos y {orita.second} segundos"
    hablar(orita_chida)

# saludar
def saludo_inicial():

    orita = datetime.datetime.now()
    if orita.hour < 6 or orita.hour > 18:
        momento = "Buenas noches!"
    elif orita.hour >= 6 or orita.hour < 13:
        momento = "Buenos dias!"
    else:
        momento = "Buenas tardes!"

    hablar(f"Hola {momento}, soy Sabina, por favor dime en que te puedo ayudar")

# funcion central del asistente
def pedir_cosas():
    
    saludo_inicial()

    comenzar = True
    while comenzar:

        pedido = audio_en_texto().lower();
        if "abrir youtube" in pedido:
            hablar("En seguida, abriendo youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "abrir navegador" in pedido:
            hablar("En seguida, abriendo tu navegador predeterminado")
            webbrowser.open("https://www.google.com")
            continue
        elif "qué día es" in pedido:
            pedir_dia()
            continue
        elif "qué hora" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("OK, buscando en wikipedia")
            pedido = pedido.replace("busca en wikipedia","")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice lo siguiente:")
            hablar(resultado)
        elif "busca en internet" in pedido:
            hablar("Claro, buscando en internet")
            pedido = pedido.replace("busca en internet","")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
        elif "reproducir" in pedido:
            pedido = pedido.replace("reproducir","")
            pywhatkit.playonyt(pedido)
            continue
        elif "chiste" in pedido:
            hablar(pyjokes.get_joke('es'))
            continue            
        elif "adios" in pedido:
            hablar("ok, me voy a descansar, cualquier cosa me avisas")
            break

pedir_cosas()

# sumar a y b


