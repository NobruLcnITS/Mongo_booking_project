from colorama import Fore
import time
from filtercreators import *
from connectiondb import connection_collection, clear_screen
from selctor import *
import random

collection = connection_collection('Concerti')
collection.create_index([("luogo.posizione", "2dsphere")])
users_collection = connection_collection('utenti')


def generate_ticket_id(users_collection, concert, classe , data):
    prefix = concert[:2]
    while True:
        ticket_id = f"{prefix}cl{classe}{data}{random.randint(10000, 99999)}"
        
        if not users_collection.find_one({"tickets": ticket_id}):
            return ticket_id

def add_ticket_to_user(users_collection, username, ticket_id):
    users_collection.update_one(
        {"username": username},
        {"$push": {"tickets": ticket_id}}
    )
    return

def show_tickets(user):
    user_doc = users_collection.find_one({"username": user})
    tickets = user_doc["tickets"]
    if tickets:
        print(f"Tickets di {user}:")
        for ticket in tickets:
            print(f"- {ticket}")
    else:
        print(f"{Fore.RED}{user}, non hai ancora nessun ticket.{Fore.RESET}")
    stop = input("\nUsa un tasto qualsiasi per uscire dalla visualizzazione dei documenti: ")
    return 

def visualization_buy(user):
    global filters
    
    clear_screen() 
    if not filters:
        print(f"{Fore.YELLOW}Nessun filtro applicato. Verranno mostrati tutti i concerti.{Fore.RESET}")
        time.sleep(2)
        query = {}
    else:
        query = {}
        for key, value in filters.items():
            query.update(value)

    results = collection.find(query)
    results = list(results)
    count = len(results)
    
    if count == 0:
        print(f"{Fore.RED}Nessun concerto trovato con i filtri applicati.{Fore.RESET}")
    else:
        print(f"{Fore.GREEN}Trovati {count} concerti:{Fore.RESET}")
        
        concerti = list(results)
        
        while True:
            clear_screen()
            for i, concert in enumerate(concerti, 1):
                print(f"\n{i}. {concert['nome']}")

            scelta = input("\nInserisci il numero del concerto per vedere i dettagli (o 'exit' per tornare al menu principale): ")
            
            if scelta.lower() == 'exit':
                clear_screen()
                filters.clear()
                return False
            
            try:
                clear_screen()
                indice = int(scelta) - 1
                if 0 <= indice < len(concerti):
                    concerto = concerti[indice]
                    print(f"{Fore.YELLOW}\nDettagli del concerto:{Fore.RESET}\n")
                    print(f"Nome: {concerto['nome']}")
                    
                    if isinstance(concerto["artista"], list):
                        print(f"Artisti: {', '.join(concerto['artista'])}")
                    else:
                        print(f"Artista: {concerto['artista']}")
                    
                    print(f"Data: {concerto['data'].strftime('%Y-%m-%d')}")
                    print(f"Luogo: {concerto['luogo']['indirizzo']}")
                    
                    if isinstance(concerto["genere"], list):
                        print(f"Generi: {', '.join(concerto['genere'])}")
                    else:
                        print(f"Genere: {concerto['genere']}")
                    
                    biglietti_disponibili_tot = sum(concerto["biglietti_disponibili"])
                    
                    print(f"Prezzo: da €{min(concerto['prezzo_biglietti'])} a €{max(concerto['prezzo_biglietti'])}")
                    print(f"Biglietti disponibili: {biglietti_disponibili_tot}")
                    
                    if biglietti_disponibili_tot > 0:
                        scelta = input(f"\n{Fore.YELLOW}Vuoi vedere il prezzo biglietti? y/n {Fore.RESET}\n\n")
                        if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                            clear_screen()
                            print(f"{Fore.LIGHTYELLOW_EX}Ecco i prezzi per classe: \n {Fore.RESET}")
                            for i in range(len(concerto["biglietti_disponibili"])):
                                print(f"Classe {i+1}: Prezzo: {Fore.YELLOW}{concerto['prezzo_biglietti'][i]}€, Disponibilità: {concerto['biglietti_disponibili'][i]}pz{Fore.RESET}")
                            scelta = input(f"{Fore.YELLOW}\nVuoi acquistare dei biglietti? y/n \n{Fore.RESET}")
                            transazione_completata = False
                            transazione_annullata = False
                            if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                                while (transazione_completata ==False and transazione_annullata == False):
                                    quantità = input("\nQuanti ne vorresti acquistare? \n")
                                    try:
                                        quantità = int(quantità)
                                        while True:
                                            classe = input("Bene! Digita il numero della classe \n")
                                            try:
                                                classe = int(classe) - 1
                                                biglietti_tot_classe = int(concerto["biglietti_disponibili"][classe])
                                                if biglietti_tot_classe < quantità:
                                                    print(f"{Fore.RED}Non ci sono abbastanza biglietti in questa classe, dato che ne abbiamo solo {concerto['biglietti_disponibili'][classe]}, ci dispiace! {Fore.RESET}")
                                                    transazione_annullata = True
                                                    time.sleep(4)
                                                    break
                                                costo = float(concerto["prezzo_biglietti"][classe]) * quantità
                                                clear_screen()
                                                scelta = input(f"Il costo totale è di {costo}€, vuoi procedere al pagamento? y/n \n")
                                                if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                                                    print(f"{Fore.GREEN}Grazie per averci scelto! Transazione andata a buon fine{Fore.RESET}")
                                                    for i in range(quantità):
                                                        ticket_id = generate_ticket_id(users_collection=users_collection, concert=concerto["nome"], classe=classe+1, data=concerto["data"].strftime('%Y-%m-%d'))
                                                        add_ticket_to_user(ticket_id=ticket_id, users_collection=users_collection, username=user)
                                                    concerto["biglietti_disponibili"][classe] -= quantità
                                                    collection.update_one(
                                                    {"_id": concerto["_id"]},
                                                    {"$set": {f"biglietti_disponibili.{classe}": concerto['biglietti_disponibili'][classe]}}
                                                    )
                                                    transazione_completata = True
                                                    time.sleep(3)
                                                    break
                                                else:
                                                    print(f"\n{Fore.RED}Transazione non andata a buon fine. {Fore.RESET}")
                                                    transazione_annullata = True
                                                    time.sleep(3)
                                                    break
                                                
                                            except IndexError:
                                                print("\nLa classe da te digitata non esiste, riprova")
                                                continue
                                            except ValueError:
                                                print("\nDigita il numero della classe!")
                                                continue
                                            
                                    except ValueError:
                                        scelta = input("Devi digitare un numero, vuoi davvero acquistari? y/n \n")
                                        if scelta.lower() in ["y", "sì", "si", "yes", "ok", "1"]:
                                            continue
                                        else:
                                            filters.clear()
                                            return False
                    else:
                        print(f"{Fore.LIGHTRED_EX}\nQuesto concerto è sold out, ma non preoccuparti, hai l'imbarazzo della scelta!{Fore.RESET}")
                        time.sleep(3)
                        continue
                else:
                    print(f"{Fore.RED}Numero non valido. Riprova.{Fore.RESET}")
                    time.sleep(1.5)
            except ValueError:
                print(f"{Fore.RED}Input non valido. Inserisci un numero o 'exit' per uscire.{Fore.RESET}")
            scelta = input("Vuoi visualizzare di nuovo gli eventi? y/n \n")
            if scelta.lower() not in ["s", "si", "sì", "yes", "y", "1"]:
                print(f"{Fore.RED}Torno al menu principale...{Fore.RESET}")
                time.sleep(1)
                clear_screen()
                break
            else:
                filters.clear()

def utente_session(user):
    while True:
        clear_screen()
        scelta = input( f"\n{Fore.YELLOW}Per quali criteri vuoi visualizzare i concerti?{Fore.RESET}\n\n"
                        f"- 1. Per nome del concerto \n"
                        f"- 2. Per artista presente \n"
                        f"- 3. Per data \n"
                        f"- 4. Per posizione \n"
                        f"- 5. Non sold out \n"
                        f"- 6. Prezzo dei biglietti \n"
                        f"- 7. Per genere musicale \n"
                        f"- 8. Esegui la ricerca \n"
                        f"- 9. Visualizza i tuoi biglietti \n"
                        f"- 10. Esci da TicketMania \n"
                        "\nNOTA: Scegliendo due volte lo stesso criterio, sovrascriverai quello settato precedentemente! \n\n"
                        )
        match scelta:
            case "1" | "nome" | "concerto":
                select_name()
            case "2" | "artista" | "aritsti":
                select_artist()

            case "3" | "data" | "quando":
                select_date()
            case "4" | "qua" | "dove" | "luogo":
                select_position()
                        
            case "5" | "soldout" | "sold out":
                select_soldout()
                    
            case "6" | "prezzo" | "soldi" | "prezzi":
                select_price()
                
            case "7" | "genere" | "musica":
                select_genre()
                
            case "8" | "vai" | "esegui" | "ok":
                check = visualization_buy(user) 
                if check is False:
                    continue
            
            case "9" | "biglietti" | "visualizza":
                clear_screen()
                show_tickets(user)
            
            case "10" | "esci":
                clear_screen()
                print(f"{Fore.RED}Uscendo da TicketMania...{Fore.RESET}")
                time.sleep(2)
                break
             

            
              

    