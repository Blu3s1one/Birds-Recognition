import os
import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
import numpy as np

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

###
cheminDriver="C:/Users/lavra/Documents/webdriver/bin"
cheminDonnee="C:/Users/lavra/Documents/imt atlantique 2A/commande entreprise/donnee"


nombreImage=200


# headers = {}
# headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"



os.chdir(cheminDriver)
driver = Firefox()


number_of_scrolls = (nombreImage)// 400 + 1
os.chdir(cheminDonnee)



tableauRecherche=['becasseau sanderling' , 'courlis cendre' , 'bernache cravant' , 'canard siffleur' , 'canard colvert' , 'goeland argenté' , 'grand gravelot' , 'mouette rieuse' , 'pluvier argente', 'vanneau huppe' , 'tadorne de belon']



#'becasseau variable'
for recherche in tableauRecherche:

    print(recherche)
    os.makedirs(recherche)
    labelImage=recherche+"-"
    url = "https://www.google.co.in/search?q="+recherche+"&source=lnms&tbm=isch"
    driver.get(url)
    for _ in range(number_of_scrolls):
        for __ in range(10):
            # Multiple scrolls needed to show all 400 images
            driver.execute_script("window.scrollBy(0, 1000000)")
            time.sleep(0.2)
        # to load next 400 images
        time.sleep(2.5)
        try:
            driver.find_element_by_xpath("//input[@value='Afficher plus de résultats']").click()
            time.sleep(2.5)
        except Exception as e:
            print("Less images found:"+ str(e))
            break

    # Process (download) images
    images = driver.find_elements_by_xpath('//div[contains(@class,"isv-r")]')




    for num in range(nombreImage):
        print(num)


        img_url=images[num].get_attribute('innerHTML').split("src=")[1].split('"')[1]

        req = urllib.request.Request(img_url)
        ouverte=urllib.request.urlopen(req)

        type=ouverte.info().get_params()[0][0][6:]
        raw_img = ouverte.read()
        f = open(cheminDonnee+"/"+recherche+"/"+labelImage+str(num)+"."+type, "wb")
        f.write(raw_img)
        f.close()
