# Lis‰‰ t‰nne omat funktiot, mutta lue ensin materiaali. Korjaa siis kaikki virheet!
# Materiaali: https://docs.python.org/3.4/tutorial/introduction.html#using-python-as-a-calculator

# 1. Tee muuttuja 'nimi' johon laitat oman nimesi

# 2. T‰ydenn‰ muuttujaa 'lempielokuva' johon talletat lempielokuvasi niin, ett‰ sen ymp‰rill‰ on ""

lempielokuva = None

# 3. T‰ydenn‰ seuraava funktio niin, ett‰ se palauttaa parametrein‰ saadut merkkijonot katenoituina
# Esim. Kaapon lempielokuva on "Nallen puisto"

def lempi_elokuva(kuka, mika):
    return ''


# 4. Tee funktio, joka palauttaa sanan pituuden vinkki: len()

def sanan_pituus(sana):
    return -1


# 5. Tee funktio, joka ottaa sanan ensimm‰isen ja viimeisen kirjaimen ja yhdist‰‰ ne uudeksi sanaksi
# Esim. eka_vika("Kaapo") => "Ko"

def eka_vika(sana):
    return ''


# 6. Tee funktio, joka k‰‰nt‰‰ sanan. Huom ‰l‰ k‰yt‰ .reverse()-funktiota, vaan [n] merkint‰‰, jossa n on kirjaimen
# indeksi

def kaantaen(sana):
    return ''


# 7. Tee funktio, joka palauttaa True, jos annettu sana oli palindromi ja False muuten. Kayta edellisen teht‰v‰n
# kaanaten(sana) -funktiota

def onko_palindromi(sana):
    return False


# 8. Tee funktio listaan, joka muodostaa listan annetuista parametreista
# Esim. listaan(1,2,3,4) => [1,2,3,4]

def listaan(a, b, c, d):
    return None


# 9. Tee funktio indeksiin_asti, joka palauttaa luvut tiettyyn indeksiin asti
# Esim. indeksiin_asti([1,2,3],2) palauttaa [1,2]

def indeksiin_asti(luvut, asti):
    return []


# 10. Tee funktio vaihda_luku, joka vaihtaa luvun halutusta indeksista

def vaihda_luku(luvut, indeksi, uusi_luku):
    return []


# 11. Tee funktio yhdista_taulut(a,b), joka yhdistaa taulukot a ja b toisiinsa
# Esim. yhdista_taulut([1,2], [3,4]) palauttaa [1,2,3,4]

def yhdista_taulut(a, b):
    return []

# 12. Tee funktio capslockkaa(kirjaimet), joka muuttaa muuttujan 'kirjaimet' kirjaimet isoiksi Vinkki: upper()

kirjaimet = [['a'], ['b'], ['c']]


def capslockkaa(kirjaimet):
    return []


# 13. Tee funktio fibonacci(n), joka palauttaa fibonaccin luvun n:nteen lukuun asti
# http://fi.wikipedia.org/wiki/Fibonaccin_lukujono
# Esim fibonacci(5) palauttaa luvun 5, mutta fibonacci(6) palauttaa 8

def fibonacci(n):
    return 0;


# 14. Tee funktio eka_rekursio(sana), joka tyhjentaa rekursiivisesti listan
# http://www.helsinki.fi/~huhmarni/cog131/luento1_k08.pdf
# https://noppa.aalto.fi/noppa/kurssi/t-106.1210/luennot/T-106_1210_luento_20.pdf
# Siis esimerkiksi: eka_rekursio("Pultsi") k‰y l‰pi j‰rjestyksess‰
# Pultsi => ultsi => ltsi => tsi => si => i ja lopulta tyhj‰n
# palautusarvo pit‰isi siis aina olla tyhj‰ taulukko eli ""
# Vinkki: kannattaa piirt‰‰ paperille kuvia miten ohjelma toimisi graafisesti

def eka_rekursio(sana):
    # muista lopettaa ohjelmasi
    # kutsu uudelleen samaa funktiota eka_rekursio
    # muista muokata parametria jotenkin
    return sana
