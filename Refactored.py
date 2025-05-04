import requests
from bs4 import BeautifulSoup
import time
import LinkedListImplementation as ll
import Dzivoklis as dz


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
                        tds[5].get_text(strip=True),
                        tds[6].get_text(strip=True)
                    )
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
    linkedListObj.writeALLVALUESInFile(fileName)

# def findIela(search, linkedListObj):

MyLinkedList = ll.LinkedList(None)
MyLinkedList.pop()
howManyPagesToWorkWith(3,"https://www.ss.lv/lv/real-estate/flats/riga/purvciems/", MyLinkedList)
FromLinkedListOfObjectsWriteInCSVfile("data.csv", MyLinkedList)
MyLinkedList.print_listALLVALUES()

