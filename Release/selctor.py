from colorama import Fore
import time
from get_coordinates import get_coordinates
from filtercreators import *
from datetime import date
import re
from connectiondb import clear_screen

filters = {}

def select_name():
    global filters
    concerti = []
    while True:
        clear_screen()
        concerto = input("Digita il nome del concerto, anche parziale: ")
        concerti.append(concerto)
        scelta = input("Vuoi digitarne un altro? y/n \n")
        if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
            continue
        else:
            pass
        filtro = concert_name_checker(concert=concerti)
        filters["concerto"] = filtro
        print(f"{Fore.GREEN}Filtro aggiunto con successo!{Fore.RESET}")
        time.sleep(3)
        break
    
def select_artist():
    global filters
    artisti = []
    while True:
        clear_screen()
        artista = input("Digita il nome dell'artista, anche parziale: ")
        artisti.append(artista)
        scelta = input("Vuoi digitarne un altro/a? y/n \n")
        if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
            continue
        else:
            pass
        filtro = artist_checker(artist=artisti)
        filters["artista"] = filtro
        print(f"{Fore.GREEN}Filtro aggiunto con successo!{Fore.RESET}")
        time.sleep(3)
        break
    
def select_date():
    global filters
    date_pattern = r'^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$'
    clear_screen()
    scelta1 = input("Vorresti usare la data di oggi come inizio della ricerca? y/n \n")
    if scelta1.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
        today = date.today()
        start_date = today.strftime("%Y-%m-%d")
        print(f"Data di partenza settata come {today}!")
        scelta2 = input("Vuoi inserire una data massima? y/n \n")
        if scelta2.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
            while True:
                clear_screen()
                end_date = input("Il formato della data deve essere 'anno-mese-giorno': ")
                if re.match(date_pattern, end_date):
                    filtro = date_checker(start_date=start_date, end_date=end_date)
                    filters["date"] = filtro
                    print(f"{Fore.GREEN}Filtro aggiunto con successo!{Fore.RESET}")
                    time.sleep(3)
                    break
                else:
                    scelta3 = input("Formato di data sbagliato, deve essere 'anno-mese-giorno'! Vuoi riprovare? y/n \n")
                    if scelta3.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                        continue
                    else:
                        filtro = date_checker(start_date=start_date)
                        filters["date"] = filtro
                        print(f"{Fore.GREEN}Filtro sulla data di partenza aggiunto con successo!{Fore.RESET}")
                        time.sleep(3)
                        break
        else:
            filtro = date_checker(start_date=start_date)
            filters["date"] = filtro
            print(f"{Fore.GREEN}Filtro sulla data di partenza aggiunto con successo!{Fore.RESET}")
            time.sleep(3)
        
    else:
        scelta4 = input("D'accordo! Desideri settare un giorno di partenza? y/n \n")
        if scelta4.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
            while True:
                clear_screen()
                start_date = input("Il formato della data deve essere 'anno-mese-giorno': ")
                if re.match(date_pattern, start_date):
                    scelta5 = input("Data inserita con successo! Desideri aggiungere una data massima? y/n \n")
                    if scelta5.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                        while True:
                            clear_screen()
                            end_date = input("Il formato della data deve essere 'anno-mese-giorno': ")
                            if re.match(date_pattern, end_date):
                                filtro = date_checker(start_date=start_date, end_date=end_date)
                                filters["date"] = filtro
                                print(f"{Fore.GREEN}Filtro aggiunto con successo!{Fore.RESET}")
                                time.sleep(3)
                                break
                            else:
                                scelta6 = input("Formato di data sbagliato, deve essere 'anno-mese-giorno'! Vuoi riprovare? y/n \n")
                                if scelta6.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                                    continue
                                else:
                                    filtro = date_checker(start_date=start_date)
                                    filters["date"] = filtro
                                    print(f"{Fore.GREEN}Filtro sulla data di partenza aggiunto con successo!{Fore.RESET}")
                                    time.sleep(3)
                                    break
                    else:
                        filtro = date_checker(start_date=start_date)
                        filters["date"] = filtro
                        print(f"{Fore.GREEN}Filtro sulla data di partenza aggiunto con successo!{Fore.RESET}")
                        time.sleep(3)
                        break
                else:
                    scelta7 = input("Formato di data sbagliato, deve essere 'anno-mese-giorno'! Vuoi riprovare? y/n \n")
                    if scelta7.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                        continue
                    else:
                        print(f"{Fore.RED}Ritorno al menu principale...{Fore.RESET}")
                        time.sleep(2)
                        break
        else:
            scelta8 = input("Va bene, desideri aggiungere una data massima? y/n \n")
            if scelta8.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                while True:
                    clear_screen()
                    end_date = input("Il formato della data deve essere 'anno-mese-giorno': ")
                    if re.match(date_pattern, end_date):
                        filtro = date_checker(start_date=None, end_date=end_date)
                        filters["date"] = filtro
                        print(f"{Fore.GREEN}Filtro aggiunto con successo!{Fore.RESET}")
                        time.sleep(3)
                        break
                    else:
                        scelta9 = input("Formato di data sbagliato, deve essere 'anno-mese-giorno'! Vuoi riprovare? y/n \n")
                        if scelta9.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                            continue
                        else:
                            print(f"{Fore.RED}Ritorno al menu principale...{Fore.RESET}")
                            time.sleep(2)
                            break
                        
            else:
                print(f"{Fore.RED}Ritorno al menu principale...{Fore.RESET}")
                time.sleep(2)
                        
def select_position():
    global filtersf
    filtro_trovato = False
    while filtro_trovato==False:
        clear_screen()
        indirizzo = input("Inserisci l'indirizzo di tuo interesse, senza virgole: ")
        while True:
            raggio = input("Ora inserisci la distanza di kilometri massima dall'indirizzo: ")
            try:
                raggio = int(raggio) * 1000
                lat, lon = get_coordinates(indirizzo, max_attempts=3)
            # lat, lon = 45,32
                if not (lat == 0 and lon == 0):
                    filtro = geo_checker(lon=lon, lat=lat, maxdistance=raggio)
                    filters["distanza"] = filtro
                    print(f"{Fore.GREEN}Indirizzo trovato e filtro aggiunto con successo!{Fore.RESET}")
                    time.sleep(3)
                    filtro_trovato = True
                    break
                if (lat==0 and lon==0):
                    scelta = input("Indirizzo non trovato, vuoi riprovare? y/n \n")
                    if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                        break
                    else:
                        print(f"{Fore.RED}Ritorno al menu principale...{Fore.RESET}")
                        time.sleep(2)
                        break
                else:
                    scelta = input("Non puoi sfruttare la ricerca se non sei connesso/a a internet, vuoi riprovare? y/n \n")
                    if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                        continue
                    else:
                        print(f"{Fore.RED}Ritorno al menu principale...{Fore.RESET}")
                        time.sleep(2)
                        break
            except ValueError:
                print("Devi inserire un numero!")
                continue
            
def select_soldout():
    global filters
    clear_screen()
    scelta = input("Vuoi oscurare automaticamente dai risultati i concerti sold out? y/n \n")
    if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
        filtro = available_tickets_checker()
        filters["soldout"] = filtro
        print(f"{Fore.GREEN}Filtro aggiunto con successo!{Fore.RESET}")
        time.sleep(3)
    else:
        print(f"{Fore.RED}Filtro non aggiunto!{Fore.RESET}")
        time.sleep(2)
       
def select_price():
    global filters
    while True:
        clear_screen()
        max_price = input("Qual è il massimo che vuoi spendere per un biglietto? Inserisci il numero senza '€' \n")
        try:
            max_price = int(max_price)
        except ValueError:
            scelta = input("Il valore deve essere numerico! Vuoi riprovare? y/n \n")
            if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                continue
            else:
                print(f"{Fore.RED}Ritorno al menu principale...{Fore.RESET}")
                time.sleep(2)
                break
        filtro = price_checker(max_price=max_price)
        filters["max_price"] = filtro
        print(f"{Fore.GREEN}Filtro aggiunto con successo!{Fore.RESET}")
        time.sleep(3)
        break 
    

def select_genre():
    generi = []
    while True:
        clear_screen()
        genere = input("Digita il genere musicale, anche parziale: ")
        generi.append(genere)
        scelta = input("Vuoi digitarne un altro? y/n \n")
        if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
            continue
        else:
            pass
        filtro = genre_checker(genre=generi)
        filters["generi_musicali"] = filtro
        print(f"{Fore.GREEN}Filtro aggiunto con successo!{Fore.RESET}")
        time.sleep(3)
        break

