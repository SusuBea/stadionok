from datetime import datetime

stadion_nev = []
varos = []
csapat_szam = []
elso = []
utolso = []

def fajl_beolvas():
    fajlom = open("stadionok.txt", "r", encoding="utf-8")
    fejlec = fajlom.readline()
    print(fejlec)
    fajl_tartalom = fajlom.readlines()
    # a readlines ömlesztve egy listába beleteszi a fájl szövegét, a fájl egyes sorai lesznek a lista egyes elemei
    print(fajl_tartalom)
    fajlom.close()
    feldolgoz(fajl_tartalom)



def feldolgoz(fajl_tartalom):
    i = 0
    while (i < len(fajl_tartalom)):
        #soronként történik a feldolgozás
        #létrehozom az aktuális sorokat, amik a lista egyes elemei
        #végigmegyek a lista minden elemén
        sor = fajl_tartalom[i].strip().split(";")
        # a strippel leszedem ezzel a /n-t, vagyis az üres sorokat az egyes tényleges szöveges sorok  között
        # split-tel pedig az egyes sorokat beleteszem egy listába, amelynek minden eleme egy szöveg
        # a nagy listát kisebb listákra darabolom
        # meg kell adni, hogy mivel splittelem ";" vagy "," ...stb
        stadion_nev.append(sor[0])
        varos.append(sor[1])
        csapat_szam.append(int(sor[2]))
        elso.append(sor[3])
        utolso.append(sor[4])
        i+=1


    print(stadion_nev)
    print(varos)
    print(csapat_szam)
    print(elso)
    print(utolso)
    print(f"A stadionok darabszáma: {len(csapat_szam)}")
    print("A new Yorki stadionok listája:")
    newYorki_csapatok()


def newYorki_csapatok():
    i = 0
    while (i < len(varos)):
        if (varos[i] == "New York"):
            print(f"{stadion_nev[i]:>40}: {csapat_szam[i]:5} db")
        i += 1


def elso_szamma_alakit():
    i = 0
    elso_szam = []
    while i < len(elso):
        elso_szam.append(int(elso[i][0:4]))
        i += 1
    print("")
    print("1900 előtt:")
    elso_merkozes_1900_elott(elso_szam)

def elso_merkozes_1900_elott(elso_szam):
    i = 0
    while i < len(elso_szam):
        if elso_szam[i] < 1900:
            print(f"{elso_szam[i]}:  {stadion_nev[i]:<40} stadion")
        i += 1



def utolso_szamma_alakit():
    i = 0
    utolso_szam = []
    while i < len(utolso):
        utolso_szam.append(int(utolso[i][0:4]))
        i += 1
    print("")
    print("2000 óta nem volt mérkőzés:")
    utolso_merkozes_2000_ota(utolso_szam)

def utolso_merkozes_2000_ota(utolso_szam):
    i = 0
    nem_volt_2000_ota = []
    sorszam = 0
    while i < len(utolso_szam):
        if utolso_szam[i] < 2000:
            nem_volt_2000_ota.append(utolso_szam[i])
            sorszam += 1
            print(f"{sorszam}. {utolso_szam[i]}: {stadion_nev[i]}")
        i += 1

    print(f"{len(nem_volt_2000_ota)} db stadionban")

def csapatok_buffaloban():
    buffaloban_jatszott = 0
    i = 0
    while i < len(varos):
        if varos[i] == "Buffalo":
            buffaloban_jatszott += 1
        i += 1

    print("")
    print(f"A Buffalo játszott csapatok száma: {buffaloban_jatszott} db")


















