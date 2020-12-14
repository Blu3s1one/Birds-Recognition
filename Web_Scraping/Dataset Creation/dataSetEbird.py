import os
import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
import numpy as np
import selenium
import urllib.request

# instruction:
#preparation:
# 0. installer firefox
# 1.installer selenium (pip install selenium)
# 2. installer le driver firefox dans un fichier : lien https://github.com/mozilla/geckodriver/releases
# 3. installer urllib
# 4. copier le chemin du driverfirefox (même format que dans le python)
#

#lancement de l'algorithme:
#1.indiquer le chemin ou doit aller les données (on doit le créé manuelement)
#2. regler la recherche et le nombre d'image, puis lancer l'algorithme



###lancement du navigateur et recherche

cheminDriver="C:/Users/lavra/Documents/webdriver/bin"
cheminDonnee="C:/Users/lavra/Documents/tensorflow/workspace/training_demo/dataset_antoine"

nombreImage=30


# headers = {}
# headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"



os.chdir(cheminDriver)
driver = Firefox()
driver.maximize_window()

number_of_scrolls = (nombreImage-1)// 30 + 1
os.chdir(cheminDonnee)



# tableauRecherche=['becasseau sanderling' , 'courlis cendre' , 'bernache cravant' , 'canard siffleur' , 'canard colvert' , 'goeland argenté' , 'grand gravelot' , 'mouette rieuse' , 'pluvier argente', 'vanneau huppe' , 'tadorne de belon']
#
#
# anglais=['Sanderling','Eurasian curlew','brant','Eurasian wigeon','Mallard','European herring gull',"Common ringed plover",'Black-headed gull','Grey plover','Northern lapwing','Common shelduck']


url_ebird='https://ebird.org/media/catalog?taxonCode=sander&regionCode=&mediaType=p'

labelImage='sander'+'-'


url="https://www.google.co.in/search?q=recherche&source=lnms&tbm=isch"
driver.get(url_ebird)

###choix des images
from pynput import keyboard
global indiceRow


#sander: année récupéré entre 2001 et 2005

tableau=[]
ligne=[]
indiceRow=0

def on_press(key):

    global indiceRow
    global row
    res=key
    if key==keyboard.Key.down:
        row=driver.find_elements_by_xpath('//div[contains(@class,"ResultsGallery-row")]')
        indiceRow+=1
        actualisation(indiceRow)
        print(indiceRow)
    else:
        try:

            dic={'&':0,'é':1,'"':2,"'":3,'(':4,'-':5,'è':6}
            candidat=key.char
            if not(dic[candidat] in ligne):
                ligne.append(dic[candidat])

        except:
            print(key)

    print(ligne)

def actualisation(indiceRow):
    global ligne

    row[indiceRow].location_once_scrolled_into_view
    tableau.append(ligne)
    ligne=[]
    #actualise les objets présents sur la pagesaaa&&
    pass


listener = keyboard.Listener(
    on_press=on_press,
    )
listener.start()


###download
listener.stop()



def download():

    row=driver.find_elements_by_xpath('//div[contains(@class,"ResultsGallery-row")]')
    num=122
    for i in range(len(tableau)):
        elements=row[i].find_elements_by_xpath('.//img[contains(@class,"ResultsGallery-image")]')

        ligne=tableau[i]
        for numero in ligne:

            #download
            try:
                img_url=elements[numero].get_attribute('srcset').split(",")[-2][0:-5]
                #full res : img_url=elements[numero].get_attribute('srcset').split(",")[-1][0:-6]
                req = urllib.request.Request(img_url)
                ouverte=urllib.request.urlopen(req)
                type=ouverte.info().get_params()[0][0][6:]
                raw_img = ouverte.read()
                f = open(cheminDonnee+"/"+'sander_2'+"/"+labelImage+str(num)+"."+type, "wb")
                f.write(raw_img)
                f.close()
                num+=1
            except:
                print("image pas téléchargé")
                print('row n° ',i)
                print('photo numero ',numero)







download()

