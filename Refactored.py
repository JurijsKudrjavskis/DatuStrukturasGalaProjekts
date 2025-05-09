import requests
from bs4 import BeautifulSoup
import time
import LinkedListImplementation as ll
import Dzivoklis as dz

def LinkedList_print_listALLVALUES(linkedListObj):
    temp = linkedListObj.head
    while temp is not None:
        temp.value.DZIVprint()
        temp = temp.next

def LinkedList_writeALLVALUESInFile(linkedListObj, FileName):
    temp = linkedListObj.head
    f = open(FileName, "a", encoding="utf-8")
    while temp is not None:
        f.write(",".join(temp.value.DzivAllDataGetter()) + "\n")
        temp = temp.next
    f.close()

def GetPageSaturs(adrese):
    lapa = requests.get(adrese)
    if lapa.status_code == 200:
        return BeautifulSoup(lapa.content, "html.parser") #  lapas_saturs
    else:
        return None
        
def FromLapasSatrursfillLinkedListWithDzivoklisObjects(lapas_saturs, linkedListObj):
    trs = lapas_saturs.find_all("tr")
    for tr in trs:
        id_attr = tr.get("id")
        if id_attr and id_attr.startswith("tr_") and len(id_attr) == 11:
            a_tag = tr.find("a", class_="am")  
            if a_tag:
                link = "https://www.ss.lv" + a_tag.get("href") +" "
                tds = tr.find_all("td", class_="msga2-o pp6")
                if len(tds) >= 6:
                    dzivoklis_obj = dz.Dzivoklis(
                        link,
                        tds[0].get_text(strip=True),
                        tds[1].get_text(strip=True),
                        tds[2].get_text(strip=True),
                        tds[3].get_text(strip=True),
                        tds[4].get_text(strip=True),
                        tds[5].get_text(strip=True).replace(" ", "").replace(",", "").replace(".", "").replace("€", "").strip(),
                        tds[6].get_text(strip=True).replace(" ", "").replace(",", "").replace(".", "").replace("€", "").strip()
                    )
                    if dzivoklis_obj.get_cena().isdigit(): # ignore / men / diena  dzīvokļu izīrēšana
                        linkedListObj.append(dzivoklis_obj)
        
def howManyPagesToWorkWith(n,adrese,linkedListObj):
    for i in range(1, n+1):
        time.sleep(2)
        FromLapasSatrursfillLinkedListWithDzivoklisObjects(GetPageSaturs(adrese+"page"+str(i)+".html"), linkedListObj)
        print(f"Done page {i}")
        
def FromLinkedListOfObjectsWriteInCSVfile(fileName, linkedListObj):
    f = open(fileName, "w", encoding="utf-8")
    f.write("link,iela,istabuSkaits,laukumsM2,stavs,serija,cenaM2,cena\n")
    f.close()
    LinkedList_writeALLVALUESInFile(linkedListObj, fileName)

def findAnythingInt(category, search, howToCompare, linkedListObj):
    temp = linkedListObj.head

    match howToCompare:
        case "=":
            while temp is not None:
                match category:
                    case "istabu_skaits":
                        value = temp.value.get_istabu_skaits()
                    case "laukums_m2":
                        value = temp.value.get_laukums_m2()
                    case "stavs":
                        value = temp.value.get_stavs()
                    case "cena_m2":
                        value = temp.value.get_cena_m2()
                    case "cena":
                        value = temp.value.get_cena()
                    case _:
                        value = None

                if value is not None and int(search) == int(value):
                    temp.value.DZIVprint()

                temp = temp.next

        case "<":
            while temp is not None:
                match category:
                    case "istabu_skaits":
                        value = temp.value.get_istabu_skaits()
                    case "laukums_m2":
                        value = temp.value.get_laukums_m2()
                    case "stavs":
                        value = temp.value.get_stavs()
                    case "cena_m2":
                        value = temp.value.get_cena_m2()
                    case "cena":
                        value = temp.value.get_cena()
                    case _:
                        value = None

                if value is not None and int(search) > int(value):
                    temp.value.DZIVprint()

                temp = temp.next
        case ">":
            while temp is not None:
                match category:
                    case "istabu_skaits":
                        value = temp.value.get_istabu_skaits()
                    case "laukums_m2":
                        value = temp.value.get_laukums_m2()
                    case "stavs":
                        value = temp.value.get_stavs()
                    case "cena_m2":
                        value = temp.value.get_cena_m2()
                    case "cena":
                        value = temp.value.get_cena()
                    case _:
                        value = None

                if value is not None and int(search) < int(value):
                    temp.value.DZIVprint()

                temp = temp.next
        case _:
            print("Invalid comparison operator.")

def findIela(search, linkedListObj):
    temp = linkedListObj.head
    while temp is not None: 
        if search in temp.value.get_iela():
            temp.value.DZIVprint()
        temp = temp.next

def findSerija(search, linkedListObj):
    temp = linkedListObj.head
    while temp is not None: 
        if search in temp.value.get_serija():
            temp.value.DZIVprint()
        temp = temp.next


MyLinkedList = ll.LinkedList(None)
MyLinkedList.pop()
howManyPagesToWorkWith(5,"https://www.ss.lv/lv/real-estate/flats/riga/purvciems/", MyLinkedList)
# FromLinkedListOfObjectsWriteInCSVfile("data.csv", MyLinkedList)
# findAnythingInt("istabu_skaits", "2", ">", MyLinkedList)
# findIela("Staiceles", MyLinkedList)
findSerija("Jaun.", MyLinkedList)
