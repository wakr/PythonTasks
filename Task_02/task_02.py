# 1. Tee funktio kerro_arvo() joka kysyy numeron kayttajalta ja palauttaa seuraavat merkkijonot väleiltä
#  1-10 => "jee"
#  11 => "jeejee"
#  Negatiivisille => "Kaapon vene"
#  Lopuille => "Maarittelematon"

def kerro_arvo():
    return ""


# 2. Legendaarinen FizzBuzz http://blog.codinghorror.com/why-cant-programmers-program/
# Tee ohjelma fizz_buzz(numero), joka palauttaa "Fizz" jos numero oli jaollinen kolmella, "Buzz" jos
# numero oli jaollinen 5 ja "FizzBuzz", jos luku oli jaollinen kolmella sekä viidellä.
#

def fizz_buzz(numero):
    return ""


# 3. Tee ohjelma suuret_alkuun, joka käy luvut läpi 1-10. Jos luku on jaollinen kahdella se laitetaan listan alkuun,
# muuten luku laitetaan listan loppuun.
# Palauta lopuksi valmis lista.
# Vinkki taululla löytyy funktiot .append ja .insert

def suuret_alkuun():
    taulu = []
    return taulu


# Tee funktio pisin_sana(sanat), joka palauttaa pisimman sanan sanat-taulukosta

def pisin_sana(sanat):
    return ""


# 4. Tee funktio pisimman_indeksi(sanat), joka palauttaa parin (a,b) (eli ns. tuplen), jossa a on pisin sana sanat-taulukosta ja
# b on pisimman sanan indeksi
def pisimman_indeksi(sanat):
    return "", 0


# 5. Tee funktio alusta_loppuun_listaan(alku, loppu), joka luo uuden listan valilta alku-loppu

def alusta_loppuun_listaan(alku, loppu):
    return []


# 6. Tee funktio erittele_parilliset(lista), joka muodostaa uuden listan ilman parittomia lukuja
# Vinkki: continue

def erittele_pariliset(lista):
    return []


# 7. Tutustu dictionary-rakenteeseen https://docs.python.org/2/tutorial/datastructures.html#dictionaries
# ja ota selvää mita **-operaattori tekee. Tee sen jälkeen henkilotieto_tulostin(henkilo), jota kutsut **henkilo-muuttujalla.
# Funktion pitaisi palauttaa muodossa "Pultun syntymavuosi on 1992 ja han tykkaa sukluusta"
# Mita tapahtui **-operaattorilla?

def henkilotieto_tulostin(nimi, syntymavuosi, tykkaa):
    return ""

# ala muokkaa tata dictionary-rakennetta
henkilo = {"nimi": "Pultu", "syntymavuosi": "1992", "tykkaa": "sukluusta"}

# 8. Parannellaan tulostajaa. Tee funktio paranneltu_henkilo_tulostin(henkilo), joka tulostaa henkilon tiedot
# kayttaen [] -operaattoria, jotta paaset tietoihin kasiksi.

def paranneltu_henkilo_tulostin(henkilo):
    return ""

    # Jos sait edellisen tehtavan tehtya ota selvaa http://fi.wikipedia.org/wiki/JSON
    # Kay ilmi, etta Pythonin kayttama dictionary-muoto on itseasiassa JSON-tyyppista dataa. Taman muodon kanssa
    # on hyvin helppoa kommunikoida jolloin esim. seuraava sivu on mahdollinen
    # https://glosbe.com/gapi/translate?from=eng&dest=fra&format=json&phrase=chocolate&pretty=true
    # Jos osoitteen parametreja lukee tarkasti, voi nahda, etta kyseinen kysely kaantaa sanan "chocolate" englannista
    # ranskaan


# 9. Tutustutaan viela hieman JSON-formaattiin ja dictionary-rakenteeseen. Tee funktio tulostus_natiksi(dict), joka
# palauttaa minkä tahansa dictionary-rakenteen seuraavassa muodossa (eli siis json-muodossa):
#   {
#       "nimi": "Pultu",
#       "syntymavuosi": "1992",
#       "tykkaa": "sukluusta"
#   }
#
# Vinkit: json, dumps()-funktio, indent, sort_keys (huomaa, että avaimet ovat aakkosjärjestyksessä). Saat
# paluuarvona json-objektin, jonka tulostaminen tuottaa ylhäällä mainitun muotoilun

def tulostus_natiksi(dc):
    return ""
