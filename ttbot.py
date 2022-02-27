import tweepy
import datetime 

key =  ''  #Acess
secret = '' #Chave secreta

consumer_key = '' #API
consumer_secret = '' #Chave secreta

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


ferias = datetime.date() #Colocar o dia das férias
agora = datetime.date.today() #Computa o dia de hoje

fdias_horas = ferias - agora #Diferença entre os dias colocados anteriormente (Tempo para as férias)
fdias = fdias_horas.days  #Agora pegamos somente os dias 

if fdias != 1 and fdias != 0:
    api.update_status("Faltam " + str(fdias) + " dias para as férias da UFPEL")
if fdias == 1:
    api.update_status("Falta " + str(fdias) + " dia para as férias da UFPEL!!!")
if fdias == 0:
    api.update_status("Hoje começam as férias na UFPEL!!!")
