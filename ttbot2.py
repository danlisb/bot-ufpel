import tweepy
import datetime

# Insira as chaves aqui
CONSUMER_KEY = '
CONSUMER_SECRET = ''
BEARER_TOKEN = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Acessa a API do Twitter
client_v2 = tweepy.Client(bearer_token=BEARER_TOKEN, 
                          consumer_key=CONSUMER_KEY, 
                          consumer_secret=CONSUMER_SECRET, 
                          access_token=ACCESS_TOKEN, 
                          access_token_secret=ACCESS_TOKEN_SECRET)

ferias = datetime.date(2023,9,22) # Colocar o dia das férias (ANO,MES,DIA)
agora = datetime.date.today() # Pega o dia de hoje
fdias_horas = ferias - agora # Diferença entre os dias colocados anteriormente (Tempo para as férias)
fdias = fdias_horas.days  # Agora pegamos somente os dias

if fdias > 1:
    client_v2.create_tweet(text="Faltam " + str(fdias) + " dias para as férias da UFPEL")
if fdias == 1:
    client_v2.create_tweet(text="Falta " + str(fdias) + " dia para as férias da UFPEL!!!")
if fdias == 0:
    client_v2.create_tweet(text="Hoje começam as férias na UFPEL!!!")
if fdias < 0:
    pass
