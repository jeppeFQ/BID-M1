#%%writefile census_modul.py

import json
import glob
import os
from datetime import datetime

class Person:
    def __init__(self, navn, alder, køn, adresse):
        self.__navn = navn
        self.__alder = alder
        self.__køn = køn
        self.__adresse = adresse
        self.__husstand = None
        self.__uddannelsesinstitution = None
        self.__arbejdsplads = None

    # Getter og setter for navn
    def get_navn(self):
        return self.__navn

    def set_navn(self, navn):
        self.__navn = navn

    # Getter og setter for alder
    def get_alder(self):
        return self.__alder

    def set_alder(self, alder):
        if alder < 0:
            raise ValueError("Alder kan ikke være negativ")
        self.__alder = alder

    # Getter og setter for køn
    def get_køn(self):
        return self.__køn

    def set_køn(self, køn):
        self.__køn = køn

    # Getter og setter for adresse
    def get_adresse(self):
        return self.__adresse

    def set_adresse(self, adresse):
        self.__adresse = adresse

    # Getter og setter for husstand
    def get_husstand(self):
        return self.__husstand

    def set_husstand(self, husstand):
        self.__husstand = husstand

    # Getter og setter for uddannelsesinstitution
    def get_uddannelsesinstitution(self):
        return self.__uddannelsesinstitution

    def set_uddannelsesinstitution(self, institution):
        self.__uddannelsesinstitution = institution

    # Getter og setter for arbejdsplads
    def get_arbejdsplads(self):
        return self.__arbejdsplads

    def set_arbejdsplads(self, arbejdsplads):
        self.__arbejdsplads = arbejdsplads

    def __str__(self):
        husstand_info = f"Husstand: {self.__husstand.get_adresse()}" if self.__husstand else "Ingen husstand"
        uddannelse_info = f"Uddannelsesinstitution: {self.__uddannelsesinstitution.get_navn()}" if self.__uddannelsesinstitution else "Ingen uddannelsesinstitution"
        arbejdsplads_info = f"Arbejdsplads: {self.__arbejdsplads.get_navn()}" if self.__arbejdsplads else "Ingen arbejdsplads"
        return f"{self.__navn}, {self.__alder} år, {self.__køn}, {self.__adresse}, {husstand_info}, {uddannelse_info}, {arbejdsplads_info}"

class Student(Person):
    def __init__(self, navn, alder, køn, adresse, studie):
        super().__init__(navn, alder, køn, adresse)
        self.__studie = studie

    # Getter og setter for studie
    def get_studie(self):
        return self.__studie

    def set_studie(self, studie):
        self.__studie = studie

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Studie: {self.__studie}"

class Arbejder(Person):
    def __init__(self, navn, alder, køn, adresse, jobtitel):
        super().__init__(navn, alder, køn, adresse)
        self.__jobtitel = jobtitel

    # Getter og setter for jobtitel
    def get_jobtitel(self):
        return self.__jobtitel

    def set_jobtitel(self, jobtitel):
        self.__jobtitel = jobtitel

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Jobtitel: {self.__jobtitel}"

class Pensionist(Person):
    def __init__(self, navn, alder, køn, adresse, tidligere_erhverv):
        super().__init__(navn, alder, køn, adresse)
        self.__tidligere_erhverv = tidligere_erhverv

    # Getter og setter for tidligere erhverv
    def get_tidl_erhverv(self):
        return self.__tidligere_erhverv

    def set_tidl_erhverv(self, tidligere_erhverv):
        self.__tidligere_erhverv = tidligere_erhverv

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Tidligere erhverv: {self.__tidligere_erhverv}"


class Husstand:
    def __init__(self, adresse):
        self.__adresse = adresse
        self.__personer = []

    # Getter og setter for adresse
    def get_adresse(self):
        return self.__adresse

    def set_adresse(self, adresse):
        self.__adresse = adresse

    # Getter og setter for personer
    def get_personer(self):
        return self.__personer

    def set_personer(self, personer):
        self.__personer = personer

    # Tilføj personer til en liste af personer, der tilhører klassen.
    # `self` henviser til den klasse metode tilhører. `person` er et objekt fra
    # en klasse (Person, Student, Arbejder), der tilføjes husstands-klassen.
    def tilføj_person(self, person):      # self.personer er en privat liste, der indeholder alle personer i en husstand.
        if person not in self.__personer: # Kontrollerer at person ikke allerede er tilstede i listen self.__personer
            self.__personer.append(person)# Hvis personen ikke er i self.personer, tilføjes de hertil.
            person.set_husstand(self)     # Når personen tilføjes, opdateres personens husstands attribut,
                                          # da `set_husstand` er en metode i personens klasse (Person, Student, Arbejder).
                                          # Hermed er husstands-referencen altid synkroniseret mellem de to klasser.

    def __str__(self):
        return f"Husstand på {self.__adresse} med {len(self.__personer)} personer."

class Uddannelsesinstitution:
    def __init__(self, navn):
        self.__navn = navn
        self.__personer = []

    # Getter og setter for navn
    def get_navn(self):
        return self.__navn

    def set_navn(self, navn):
        self.__navn = navn

    # Getter og setter for personer
    def get_personer(self):
        return self.__personer

    def set_personer(self, personer):
        self.__personer = personer

    def tilføj_person(self, person):
        if person not in self.__personer:
            self.__personer.append(person)
            person.set_uddannelsesinstitution(self)

    def __str__(self):
        return f"{self.__navn} med {len(self.__personer)} personer."

class Arbejdsplads:
    def __init__(self, navn):
        self.__navn = navn
        self.__personer = []

    # Getter og setter for navn
    def get_navn(self):
        return self.__navn

    def set_navn(self, navn):
        self.__navn = navn

    # Getter og setter for personer
    def get_personer(self):
        return self.__personer

    def set_personer(self, personer):
        self.__personer = personer

    def tilføj_person(self, person):
        if person not in self.__personer:
            self.__personer.append(person)
            person.set_arbejdsplads(self)

    def __str__(self):
        return f"{self.__navn} med {len(self.__personer)} ansatte."

def print_personer_af_klasse(personer, klasse):
    print(f"Personer af klasse {klasse.__name__}:")
    for person in personer:
        if isinstance(person, klasse):
            print(person)
    print()

def tilføj_person_interaktivt(personer, husstande, institutioner, arbejdspladser):
    print("Opret en ny person:")

    # Navn-validering
    while True:
        navn = input("Navn: ").strip()
        if navn:
            break
        else:
            print("Navn kan ikke være tomt. Prøv igen.")

    # Alder-validering
    while True:
        alder_input = input("Alder: ").strip()
        if alder_input.isdigit() and 0 <= int(alder_input) <= 120:
            alder = int(alder_input)
            break
        else:
            print("Ugyldig alder. Indtast et tal mellem 0 og 120.")

    # Køn-validering
    while True:
        køn = input("Køn (Mand/Kvinde): ").strip().capitalize()
        if køn in ["Mand", "Kvinde"]:
            break
        else:
            print("Ugyldigt køn. Indtast enten 'Mand' eller 'Kvinde'.")

    # Adresse-validering
    while True:
        adresse = input("Adresse: ").strip()
        if adresse:
            break
        else:
            print("Adresse kan ikke være tom. Prøv igen.")

        # Validering af om personen er student, arbejder eller pensionist
    while True:
        type_person = input("Er personen en Student, Arbejder eller Pensionist? (S/A/P): ").strip().upper()
        if type_person in ["S", "A", "P"]:
            break
        else:
            print("Ugyldigt valg. Indtast 'S' for Student, 'A' for Arbejder eller 'P' for Pensionist.")

    # Hvis personen er en student, valider studie
    if type_person == "S":
        while True:
            studie = input("Studie: ").strip()
            if studie:
                ny_person = Student(navn, alder, køn, adresse, studie)
                break
            else:
                print("Studie kan ikke være tomt. Prøv igen.")

    # Hvis personen er en arbejder, valider jobtitel
    elif type_person == "A":
        while True:
            jobtitel = input("Jobtitel: ").strip()
            if jobtitel:
                ny_person = Arbejder(navn, alder, køn, adresse, jobtitel)
                break
            else:
                print("Jobtitel kan ikke være tom. Prøv igen.")

    # Hvis personen er en pensionist, valider tidligere erhverv
    elif type_person == "P":
        while True:
            tidligere_erhverv = input("Tidligere erhverv: ").strip()
            if tidligere_erhverv:
                ny_person = Pensionist(navn, alder, køn, adresse, tidligere_erhverv)
                break
            else:
                print("Tidligere erhverv kan ikke være tomt. Prøv igen.")


    # Tilføj den nye person til listen over personer
    personer.append(ny_person)
    print(f"{ny_person.get_navn()} er nu tilføjet til systemet.") # Use the getter method to access the name


    # Tilknyt husstand
    husstand_adresse = input("Tilknyt til husstand (ID): ")
    husstand = next((h for h in husstande if h.get_adresse() == husstand_adresse), None)
    if not husstand:
        husstand = Husstand(husstand_adresse)
        husstande.append(husstand)
    husstand.tilføj_person(ny_person)

    # Tilknyt uddannelsesinstitution
    institution_navn = input("Tilknyt til uddannelsesinstitution (AAU/AU, eller Ingen): ")
    if institution_navn != "Ingen":
        institution = next((i for i in institutioner if i.get_navn() == institution_navn), None)
        if not institution:
            institution = Uddannelsesinstitution(institution_navn)
            institutioner.append(institution)
        ny_person.set_uddannelsesinstitution(institution)

    # Tilknyt arbejdsplads
    arbejdsplads_navn = input("Tilknyt til arbejdsplads (X/Y/Z, eller Ingen): ")
    if arbejdsplads_navn != "Ingen":
        arbejdsplads = next((a for a in arbejdspladser if a.get_navn() == arbejdsplads_navn), None)
        if not arbejdsplads:
            arbejdsplads = Arbejdsplads(arbejdsplads_navn)
            arbejdspladser.append(arbejdsplads)
        ny_person.set_arbejdsplads(arbejdsplads)

    print("Personen er blevet tilføjet.")

def find_seneste_fil(filnavn_mønster):
    """Finder den seneste fil baseret på et filnavn-mønster."""
    filer = glob.glob(filnavn_mønster)
    if not filer:
        return None
    seneste_fil = max(filer, key=os.path.getctime)
    return seneste_fil

def gem_data(alle_personer, husstande, institutioner, arbejdspladser):
    data = {
        "personer": [
            {
                "type": p.__class__.__name__,
                "navn": p.get_navn(),
                "alder": p.get_alder(),
                "køn": p.get_køn(),
                "adresse": p.get_adresse(),
                "husstand": p.get_husstand().get_adresse() if p.get_husstand() else None,
                "uddannelsesinstitution": p.get_uddannelsesinstitution().get_navn() if p.get_uddannelsesinstitution() else None,
                "arbejdsplads": p.get_arbejdsplads().get_navn() if p.get_arbejdsplads() else None,
                # Tilføj evt. specifikke attributter for Student/Arbejder
                "studie": p.get_studie() if isinstance(p, Student) else None,
                "jobtitel": p.get_jobtitel() if isinstance(p, Arbejder) else None,
                "tidligere_erhverv": p.get_tidl_erhverv() if isinstance(p, Pensionist) else None,

            }
            for p in alle_personer
        ],
        "husstande": [{"adresse": h.get_adresse()} for h in husstande],
        "institutioner": [{"navn": i.get_navn()} for i in institutioner],
        "arbejdspladser": [{"navn": a.get_navn()} for a in arbejdspladser],

    }

    # Tilføj dato og tid til filnavnet
    tidsstempel = datetime.now().strftime("%Y%m%d_%H%M%S")
    filnavn = f"census_register_{tidsstempel}.json"

    with open(filnavn, 'w') as f:
        json.dump(data, f, indent=4, default=str)

def indlæs_data():
    filnavn_mønster = "census_register_*.json"
    filnavn = find_seneste_fil(filnavn_mønster)

    if not filnavn:
        raise FileNotFoundError("Ingen filer fundet.")

    with open(filnavn, 'r') as f:
        data = json.load(f)

    husstande = [Husstand(h.get('adresse', None)) for h in data.get("husstande", [])]
    institutioner = [Uddannelsesinstitution(i.get('navn', None)) for i in data.get("institutioner", [])]
    arbejdspladser = [Arbejdsplads(a.get('navn', None)) for a in data.get("arbejdspladser", [])]
    alle_personer = []

    for p in data.get("personer", []):
        if p["type"] == "Student":
            person = Student(p.get("navn"), p.get("alder"), p.get("køn"), p.get("adresse"), p.get("studie"))
        elif p["type"] == "Arbejder":
            person = Arbejder(p.get("navn"), p.get("alder"), p.get("køn"), p.get("adresse"), p.get("jobtitel"))
        elif p["type"] == "Pensionist":
            person = Pensionist(p.get("navn"), p.get("alder"), p.get("køn"), p.get("adresse"), p.get("tidligere_erhverv"))
        else:
            person = Person(p.get("navn"), p.get("alder"), p.get("køn"), p.get("adresse"))


        # Genopret tilknytninger
        husstand = next((h for h in husstande if h.get_adresse() == p.get("husstand")), None)
        if husstand:
            person.set_husstand(husstand)

        uddannelsesinstitution = next((i for i in institutioner if i.get_navn() == p.get("uddannelsesinstitution")), None)
        if uddannelsesinstitution:
            person.set_uddannelsesinstitution(uddannelsesinstitution)

        arbejdsplads = next((a for a in arbejdspladser if a.get_navn() == p.get("arbejdsplads")), None)
        if arbejdsplads:
            person.set_arbejdsplads(arbejdsplads)

        alle_personer.append(person)

    return alle_personer, husstande, institutioner, arbejdspladser


def main():
    try:
        alle_personer, husstande, institutioner, arbejdspladser = indlæs_data()
    except FileNotFoundError:
        # Opret husstande, institutioner og arbejdspladser hvis fil ikke findes
        husstand1 = Husstand("Nørregade 12")
        husstand2 = Husstand("Hovedgade 3")
        aau = Uddannelsesinstitution("AAU")
        au = Uddannelsesinstitution("AU")
        arbejdsplads_x = Arbejdsplads("X")
        arbejdsplads_y = Arbejdsplads("Y")
        husstande = [husstand1, husstand2]
        institutioner = [aau, au]
        arbejdspladser = [arbejdsplads_x, arbejdsplads_y]
        alle_personer = []

    # Tilføj nogle initiale personer hvis der ikke er nogen
    if not alle_personer:
        p1 = Student("Anna Jensen", 30, "Kvinde", "Nørregade 12", "Kultur")
        p2 = Student("Peter Hansen", 35, "Mand", "Nørregade 12", "Teknik")
        p3 = Arbejder("Laura Smith", 25, "Kvinde", "Hovedgade 3", "Ingeniør")
        p4 = Arbejder("Jens Nielsen", 40, "Mand", "Hovedgade 3", "Chef")
        alle_personer.extend([p1, p2, p3, p4])
        p1.set_husstand(husstand1)
        p2.set_husstand(husstand1)
        p3.set_husstand(husstand2)
        p4.set_husstand(husstand2)
        p1.set_uddannelsesinstitution(aau)
        p3.set_arbejdsplads(arbejdsplads_x)
        p4.set_arbejdsplads(arbejdsplads_y)

    # Menu for interaktiv brug
    while True:
        print("\nMenu:")
        print("1. Tilføj person")
        print("2. Print alle personer")
        print("3. Print personer af en given klasse")
        print("4. Gem data")
        print("5. Afslut")

        valg = input("Vælg en option: ")

        if valg == "1":
            tilføj_person_interaktivt(alle_personer, husstande, institutioner, arbejdspladser)
        elif valg == "2":
            print("Alle personer:")
            for person in alle_personer:
                print(person)
        elif valg == "3":
            klasse_str = input("Skriv klasse (Student/Arbejder/Pensionist): ")
            if klasse_str == "Student":
                print_personer_af_klasse(alle_personer, Student)
            elif klasse_str == "Arbejder":
                print_personer_af_klasse(alle_personer, Arbejder)
            elif klasse_str == "Pensionist":
                print_personer_af_klasse(alle_personer, Pensionist)
            else:
                print("Ugyldig klasse.")
        elif valg == "4":
            gem_data(alle_personer, husstande, institutioner, arbejdspladser)
            print("Data er gemt.")
        elif valg == "5":
            break
        else:
            print("Ugyldigt valg. Prøv igen.")

if __name__ == "__main__":
    main()