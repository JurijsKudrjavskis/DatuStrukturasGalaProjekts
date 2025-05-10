<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>Title</title>
</head>
<body>
    <div>
    <h1>Dzīvokļu Meklētājs</h1>
<p>&nbsp;</p>
<h2># Projekta uzdevums</h2>
<p>&Scaron;ī projekta mērķis ir programmatūra, kas automatizē dzīvokļu meklē&scaron;anu un datu apstrādi no sludinājumu portāla <strong>ss.lv</strong>. Programma ļauj lietotājam:</p>
<p>- Norādīt reģionu/pislētu/rajonu un lapu skaitu, no kurām iegūt datus.</p>
<p>- Saglabāt iegūtos datus CSV failā.</p>
<p>- Meklēt dzīvokļus pēc dažādiem kritērijiem, piemēram, istabu skaita,cenas, laukuma un citiem parametriem.</p>
<p>- Apskatīt visus iegūtos datus lietotāja interfeisā, kas sakartoti lietotājam saprotama veidā.</p>
<p>Programma nodro&scaron;ina lietotājam ērtu grafisko interfeisu, kas ļauj veikt visas darbības bez nepiecie&scaron;amības rakstīt kodu. Padarot programmu vieglāku izmanto&scaron;ana</p>
<p>&nbsp;</p>
<h2># Izmantotās Python bibliotēkas un to pielietojums</h2>
<p>Projekta izstrādes laikā tiek izmantotas &scaron;ādas Python bibliotēkas:</p>
<p>Tkinter</p>
<p>requests</p>
<p>BeautifulSoup</p>
<p>threading</p>
<p>time</p>
<p>&nbsp;</p>
<h3>1. tkinter:</h3>
<p>- Tiek izmantota lai izveidot grafisko lietotāja interfeisu (GUI). Ar viņas palīdzību tika izveidots logs, ievades lauki, pogas, izvēlnes un citi interfeisa elementi.</p>
<h3>2. requests:</h3>
<p>- Tiek izmantota, lai veiktu HTTP pieprasījumus un iegūtu tīmekļa lapu saturu no <strong>ss.lv</strong>.</p>
<h3>3. BeautifulSoup (bs4):</h3>
<p>- Bibliotēka, kas paredzēta HTML un XML dokumentu parsē&scaron;anai un informācijas iegū&scaron;anai no tīmekļa lapām</p>
<p>- Tiek izmantota, lai analizētu un iegūtu nepiecie&scaron;amos datus.</p>
<h3>4. threading:</h3>
<p>- Tiek izmantota, lai nodro&scaron;inātu paralēlu datu iegū&scaron;anu, neapturot lietotāja interfeisa darbību.</p>
<h3>5. io un sys:</h3>
<p>- Tiek izmantotas, lai pārtvertu un apstrādātu konsoles izvadi, kas tiek parādīta lietotāja interfeisā.</p>
<h3>6. time</h3>
<p>- Bibliotēka time tiek izmantota, lai ieviestu pauzi starp tīmekļa lapu pieprasījumiem. Tas tiek darīts, lai izvairītos no servera pārslodzes vai bloķē&scaron;anas, kas var rasties pārāk biežu pieprasījumu dēļ.</p>
<p>&nbsp;</p>
<h2># Izmantotās datu struktūras</h2>
<p>Projekta izstrādes laikā tiek izmantotas:</p>
<h3>LinkedList</h3>
<p>- Vienkār&scaron;ota saistītā saraksta implementācija, kas ļauj darboties ar datiem piem: (saglabāt un apstrādāt dzīvokļu objektus).</p>
<p>Tā tiek realizēta izmantojot:</p>
<h3>1. Dzivoklis klase:</h3>
<p>- Atspoguļo dzīvokļa objektu ar tādiem atribūtiem kā saite, adrese, istabu skaits, laukums, stāvs, sērija, cena/m&sup2; un kopējā cena. Nodro&scaron;ina metodes datu iegū&scaron;anai un izdrukā&scaron;anai.</p>
<h3>2. Node klase:</h3>
<p>- Reprezentē vienu saistītā saraksta elementu, kas satur vērtību (dzīvokļa objektu) un norādi uz nākamo elementu.</p>
<h3>3. LinkedList klase:</h3>
<p>- Satur metodes elementu pievieno&scaron;anai, dzē&scaron;anai un saraksta izdrukā&scaron;anai.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2># Programmatūras izmanto&scaron;anas metodes</h2>
<h3>1. Programmas palai&scaron;ana:</h3>
<p>- Programma tiek palaista, izpildot gui.py failu. Tas atver grafisko lietotāja interfeisu.</p>
<h3>2. Datu iegū&scaron;ana:</h3>
<p>- Lietotājs ievada reģiona URL daļu un norāda, cik lapas jāapstrādā, kā arī vai vēlas sagalbat iegutos datus CSV failā.</p>
<p>- Nospiežot pogu "Start Scraping", programma iegūst datus no norādītā reģiona un saglabā tos saistītajā sarakstā.</p>
<h3>3. Datu meklē&scaron;ana:</h3>
<p>- Lietotājs izvēlas meklē&scaron;anas metodi (`findAnythingInt`, `findIela`, `findSerija`) un ievada meklē&scaron;anas kritērijus.</p>
<p>- Nospiežot pogu "Search", programma parāda rezultātus, kas atbilst mekle&scaron;anas kritērījiem.</p>
<p>- Nospiežot pogu "Show All", lietotājs var apskatīt visus iepriek&scaron; iegūtos datus bez meklē&scaron;anas kritērijiem, interfeisa logā.</p>
<h3>4. Paralēla datu apstrāde:</h3>
<p>- Datu iegū&scaron;ana notiek atsevi&scaron;ķā pavedienā, lai lietotāja interfeiss paliktu atsaucīgs.</p>
    </div>
</body>
</html>