import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.parse import urlparse, unquote
import pandas as pd

#Lista de temporadas
temporadas = [
    '1992-1993', '1993-1994', '1994-1995', '1995-1996', '1996-1997',
    '1997-1998', '1998-1999', '1999-2000', '2000-2001', '2001-2002',
    '2002-2003', '2003-2004', '2004-2005', '2005-2006', '2006-2007',
    '2007-2008', '2008-2009', '2009-2010', '2010-2011', '2011-2012',
    '2012-2013', '2013-2014', '2014-2015', '2015-2016', '2016-2017']

#A partir del 16-17 la tabla cambia
'''    '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022',
    '2022-2023', '2023-2024'
]
'''

equipos = ['Real Madrid' 'Milan' 'Bayern München' 'Liverpool' 'Barcelona' 'Ajax'
 'Inter' 'Manchester United' 'Juventus' 'Benfica' 'Chelsea' 'Porto'
 'Nottingham Forest' 'Borussia Dortmund' 'Celtic' 'Manchester City'
 'Olympique de Marseille' 'FCSB' 'Hamburger' 'Crvena Zvezda' 'PSV'
 'Feyenoord' 'Aston Villa' 'Atlético de Madrid' 'Valencia'
 'Stade de Reims' 'Monaco' 'PSG' 'Panathinaikos' 'Leeds' 'Arsenal' 'Roma'
 'Tottenham' 'Borussia Mönchengladbach' 'Saint-Étienne' 'Partizan'
 'Bayer Leverkusen' 'Brugge' 'Fiorentina' 'Malmö' 'Eintracht Frankfurt'
 'Sampdoria' 'Dynamo Kyiv' 'Anderlecht' 'CSKA Sofia' 'Olympique Lyonnais'
 'Villarreal' 'Zürich' 'Rangers' 'Galatasaray' 'Rapid Wien' 'Dukla Praha'
 'Standard Liège' 'Göteborg' 'Schalke 04' 'Újpest' 'Spartak Moskva'
 'Spartak Trnava' 'Legia Warszawa' 'Girondins de Bordeaux'
 'Deportivo de La Coruña' 'Austria Wien' 'Vasas' 'Köln' 'Dinamo București'
 'Nantes' 'Young Boys' 'RB Leipzig' 'Real Sociedad' 'Győr' 'Derby County'
 'Widzew Łódź' 'Dundee United' 'Dundee' 'Hibernian' 'Sparta Praha'
 'Dynamo Dresden' 'Hajduk Split' 'Dynamo Berlin' 'Sevilla' 'Grasshopper'
 'Nice' 'Dnipro' 'Wiener SC' 'Olympiacos' 'Górnik Zabrze'
 'Sporting de Portugal' 'Fenerbahçe' 'Basel' 'Napoli' 'AGF'
 'Shakhtar Donetsk' 'Werder Bremen' 'Beşiktaş' 'AEK' 'Vorwärts Berlin'
 'Ferencváros' 'CSKA Moskva' 'Lazio' 'Baník Ostrava' 'Wismut Aue'
 'Linfield' 'Rosenborg' 'Ruch Chorzów' 'Athletic Club' 'MTK Budapest'
 'Aberdeen' 'Atalanta' 'Wolverhampton' 'APOEL' 'SSW Innsbruck' 'Kuusysi'
 'Brøndby' 'Djurgården' 'Universitatea Craiova' 'Vojvodina' 'Nürnberg'
 'Carl Zeiss Jena' 'Åtvidabergs' 'Everton' 'Wisła Kraków' 'Wolfsburg'
 'Auxerre' 'Kaiserslautern' 'Málaga' 'Leicester' 'Ararat Yerevan' 'DWS'
 'Dinamo Minsk' 'IFK Malmö' 'Strasbourg' 'Sparta Rotterdam' 'KV Mechelen'
 'Eintracht Braunschweig' 'Burnley' 'Hradec Králové' 'Omonia'
 'Budapest Honvéd' 'Servette' 'Zenit' 'Norrköping' 'Levski Sofia'
 "Jeunesse d'Esch" 'Helsinki' 'Glentoran' 'Tirana' 'Slovan Bratislava'
 'Lillestrøm' 'Vejle' 'Esbjerg' 'Stuttgart' 'Magdeburg' 'København'
 'Lille' 'Swarovski Tirol' 'Neuchâtel Xamax' 'Argeș Pitești'
 'Lokomotiv Sofia' 'Valur' 'Trabzonspor' 'Sliema Wanderers' 'Dundalk' 'ÍA'
 'Waterford' 'Haka' 'KB' 'Lyn' 'Lech Poznań' 'Vålerenga' 'Reipas' 'B1903'
 'Hvidovre' 'Fredrikstad' 'TPS' 'B1909' 'PAOK' 'Sarajevo' 'Bohemians'
 'Polonia Bytom' 'Beveren' 'Gwardia Warszawa' 'Derry City' 'UTA Arad'
 'Red Bull Salzburg' 'Dinamo Tbilisi' 'Lokomotiv Moskva'
 'Inter Bratislava' 'Gent' 'AZ Alkmaar' 'Celta de Vigo' 'Royal Antwerp'
 '1860 München' 'Ipswich Town' 'Lyngby' 'Zaria' 'Vítkovice'
 'Hellas Verona' 'Cagliari' 'Molenbeek' 'B 1913' 'Rapid București'
 'Zbrojovka Brno' 'La Chaux-de-Fonds' 'Kilmarnock' 'Torino' 'AB'
 'Spartak Plovdiv' 'Szombierki Byton' 'Saarbrücken' 'Rot-Weiss Essen'
 'Rapid JC' 'Cork Celtic' 'HPS' 'Shamrock Rovers' 'Partizani' 'Hibernians'
 'Floriana' 'Viking' 'Valletta' 'Östers' 'Avenir' 'Keflavík' 'KR'
 'Dinamo Tirana' 'Odense' 'Petrolul Ploiești' 'Ħamrun' 'Spora'
 'Drumcondra' 'Fram' 'KuPS' 'Olympiakos Nicosia' 'Aris Bonnevoie'
 'Dinamo Zagreb' 'Halmstad' 'Víkingur Reykjavík' 'Heart of Midlothian'
 'Crusaders' 'Trakia Plovdiv' 'Torpedo Moskva' 'Athlone Town' 'OPS'
 'Progrès' 'Union Luxembourg' 'Rabat Ajax' 'Stal Mielec' 'HIFK Helsinki'
 'Start' 'Limerick' 'Stade Dudelange' 'Anorthosis' 'Vardar' 'AEL'
 'Shelbourne' 'Željezničar' 'ŁKS' 'Vllaznia' 'ÍBV' 'LASK' 'Lierse'
 'Śląsk Wrocław' 'Bologna' 'Elbasani' 'KA' 'Larissa'
 'Red Boys Differdange' "St Patrick's" 'Portadown' 'Glenavon' 'VOËST Linz'
 'Distillery' 'Beroe' 'Csepel' 'Skeid' 'Admira Energie' 'Lausanne'
 'Strømsgodset' 'Sligo Rovers' 'Cork Hibernians' 'Køge' 'KPV'
 'EPA Larnaca' 'Karl-Marx-Stadt' 'Coleraine' 'Chemie Leipzig' 'Ilves'
 'Örgryte' 'Ards' 'Luzern' 'Pezoporikos' 'Moss' 'DOS' 'BATE Borisov'
 'Sheriff Tiraspol' 'Maribor' 'Ludogorets' 'Maccabi Haifa'
 'Viktoria Plzeň' 'Qarabağ' 'Cluj' 'Skonto' 'Maccabi Tel Aviv'
 'Sturm Graz' 'Slavia Praha' 'Astana' 'Newcastle' 'Braga' 'FBK Kaunas'
 'Debrecen' 'Molde' 'Dudelange' 'The New Saints' 'Pyunik' 'Žalgiris'
 'Žilina' "Hapoel Be'er Sheva" 'Litex Lovech' 'Levadia Tallinn' 'Boavista'
 'Midtjylland' 'Aalborg' 'Petržalka' 'Neftçi' 'Aktobe' 'AIK Solna'
 'Zimbru' 'Lens' 'Helsingborg' 'Lincoln Red Imps' 'Skënderbeu'
 'Beitar Jerusalem' 'Parma' 'Ventspils' 'Košice' 'Genk' 'Hafnarfjarðar'
 'Ekranas' 'Hapoel Tel Aviv' 'Torpedo Kutaisi' 'Grazer AK' 'Raków'
 'Tampere United' 'Gorica' 'Breiðablik' 'Rubin Kazan' 'Vidi' 'Flora' 'KÍ'
 'Udinese' 'Elfsborg' 'Krasnodar' 'Olimpija' 'Mallorca' 'Thun'
 'Barry Town' 'Bodø/Glimt' 'Shakhter Karagandy' 'Sion' 'Domžale'
 'Zrinjski' 'Rabotnički' 'HB' 'Alashkert' 'Hertha Berliner' 'Rostov'
 'Birkirkara' 'Betis' 'Shkëndija' 'Kairat' 'Široki Brijeg'
 'Olimpija Ljubljana' 'Drita' 'Twente' 'Santa Coloma' 'B36' 'Slavia-Mozyr'
 'Unirea Urziceni' 'Başakşehir' 'Budućnost' 'Rijeka' 'Slovan Liberec'
 'Bakı' 'Kiryat Shmona' 'Häcken' 'Cork City' 'Apollon Limassol'
 'Nõmme Kalju' 'Trenčín' 'Víkingur Gøta' 'Rudar Pljevlja' 'Astana 64'
 'Polonia Warszawa' 'Feronikeli' 'MYPA' 'Obilić' 'Drogheda' 'Mura'
 'Mogren' "Inter d'Escaldes" 'Milsami Orhei' 'Borac Banja Luka'
 'Prishtina' 'Jazz' 'Aris Limassol' 'Zalaegerszeg' 'Modriča' 'Urartu'
 'Dinamo Brest' 'Sloga Jugomagnat' 'Kukësi' 'Inter Baku' 'Shirak' 'Sūduva'
 'Zestafoni' 'Brann' 'Stabæk' 'Mladá Boleslav' 'Dunaferr' 'Heerenveen'
 'Blackburn Rovers' 'EB/Streymur' 'WIT Georgia' 'Liepājas Metalurgs'
 'Sileks' 'Ballkani' 'Tirol Innsbruck' 'Leotar' 'Tavriya' 'Aarau'
 'Belshina' 'Shkupi' 'Metalist' 'Tre Penne' 'Shamkir' 'Ružomberok' 'Kapaz'
 'Saburtalo' 'Zeta' 'Sioni' 'Zagłębie Lubin' 'Europa FC' 'Ararat-Armenia'
 'Lugano' 'Farul Constanța' 'NK Zagreb' 'Gomel' 'Sivasspor' 'Brotnjo'
 'Dynamo Moskva' 'RFS' 'Cwmbran Town' 'Celje' 'Llanelli Town' 'Viitorul'
 'St Gilloise' 'Hansa Rostock' 'Koper' 'Kalmar' 'Dacia Chișinău' 'NSÍ'
 'Universitatea Craiova FC' 'Sutjeska' 'Hoffenheim' 'Riga'
 'Politehnica Timișoara' 'Tre Fiori' 'Fola Esch' 'Montpellier'
 'Union Berlin' 'Willem II' 'Tobol' 'Hapoel Haifa' 'Pobeda' 'Sant Julià'
 'Spartaks Jūrmala' 'Olimpi Rustavi' 'Vaslui' 'AEK Larnaca' 'Osasuna'
 'Flamurtari' 'Nordsjælland' 'Shakhtyor Soligorsk' 'Bursaspor' 'Rennes'
 'La Fiorita' 'Cliftonville' 'Kareda' 'Norma Tallinn' 'Lusitans'
 "Connah's Quay" 'Etar' 'Silkeborg' 'Swift Hesperange'
 'Constructorul Chişinău' 'Vitória de Guimarães' 'St. Gallen'
 'Dinamo Batumi' 'Metz' 'Dnipro-1' 'Larne' 'VB Vágur' 'TVMK' 'SJK'
 'Hammarby' 'Khazar Lankaran' 'Irtysh' 'Astra' 'ChievoVerona'
 'Grevenmacher' 'Piast' 'Struga' 'Oțelul Galați' 'Murata' 'Rhyl'
 'Araks Ararat' 'Folgore' 'TSC Bačka Topola' 'Herfølge BK' 'Valmiera'
 "Rànger's" 'Toulouse' 'Dnepr' 'Lokomotiv Plovdiv' 'Teplice' 'Marsaxlokk'
 'Samtredia' 'Alania Vladikavkaz' 'Kilikija' 'Liepāja' 'Mladost Podgorica'
 'Dila' 'Stjarnan' 'Daugava Daugavpils' 'Zulte Waregem'
 'Paços de Ferreira' 'Ulisses' 'FC Yerevan' 'FCI Tallinn' 'Motherwell'
 'Renova' 'Makedonija' 'Teuta' 'B68' 'Vác' 'Inter Turku' 'Mariehamn' 'GÍ'
 'Lantana' 'Bangor City' "Trepça'89" 'Lokomotiva Zagreb'
 'Atlètic Escaldes']



resultados = []
headers = ['idEntrenador', 'Temporada', 'Equipo', 'Nun', 'Non', 'División', 'Edad', 'PJ', 'PG', 'PE', 'PP', 'Non']

for idx, url in enumerate(url):
    # Realizar la solicitud GET y crear el objeto BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar la tabla que corresponde a la clase "wikitable" y estilo "text-align:enter"
    tabla = soup.find('div', {'id': 'traj', 'class': 'scrtraj mt-2'})

    # Verificar si se encontró la tabla
    if tabla:
        # Obtener todas las filas y celdas de la tabla
        rows = tabla.find_all('tr')

        # Crear una lista para almacenar las filas de datos
        tabla_data = []

        # Recorrer cada fila y extraer el texto de las celdas
        for i, row in enumerate(rows[:-1]):
            if i == 0:
                continue
            cells = row.find_all(['td', 'th'])
            row_data = [lista_ids_entrenador[idx]] + [cell.get_text(strip=True).replace('⬤', '') for cell in cells]
            tabla_data.append(row_data)

        # Agregar los resultados a la lista general
        resultados.extend(tabla_data)
        #print(tabulate(tabla_data,  tablefmt='grid'))

    else:
        print('No se encontró la tabla')
        
if len(resultados) > 0:
    resultados.insert(0, headers)
    # Especificar el nombre del archivo CSV donde guardar la tabla
    file_name = './data/Trayectoria_entrenador.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(resultados)
    print(f'Se guardó la tabla en {file_name}')
else:
    print('La tabla no contiene datos.')
