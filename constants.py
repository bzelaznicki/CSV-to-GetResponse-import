TAGS_COLUMN = "tags"

FIELD_MAPPINGS = {
    # Email fields
    "email": "email",
    "e-mail": "email",
    "e_mail": "email",
    "email address": "email",
    "email_address": "email",
    "e-mail address": "email",
    "e-mail_address": "email",
    "e_mail_address": "email",
    "adres email": "email",  # Polish
    "Adres e-mail": "email",  # Polish
    "correo electronico": "email",  # Spanish
    "correo": "email",  # Spanish
    "indirizzo email": "email",  # Italian
    "posta elettronica": "email",  # Italian

    # Name fields
    "first name": "first_name",
    "last name": "last_name",
    "imie": "first_name",  # Polish
    "nazwisko": "last_name",  # Polish
    "vorname": "first_name",  # German
    "nachname": "last_name",  # German
    "prenom": "first_name",  # French
    "nom": "last_name",  # French
    "nombre": "first_name",  # Spanish
    "apellido": "last_name",  # Spanish
    "nome": "first_name",  # Italian
    "cognome": "last_name",  # Italian

    # Full name fields
    "full name": "name",
    "fullname": "name",
    "name": "name",
    "nombre completo": "name",  # Spanish
    "nom complet": "name",  # French
    "vollständiger name": "name",  # German
    "nome completo": "name",  # Italian

    # Address fields
    "street": "street",
    "street address": "street",
    "ulica": "street",  # Polish
    "strasse": "street",  # German
    "rue": "street",  # French
    "calle": "street",  # Spanish
    "miasto": "city",  # Polish
    "city": "city",
    "kraj": "country",  # Polish
    "country": "country",
    "via": "street",  # Italian
    "indirizzo": "street",  # Italian
    "città": "city",  # Italian
    "citta": "city",  # Italian
    "paese": "country",  # Italian
    "stato": "country",  # Italian

    # Postal code
    "postal code": "postal_code",
    "zip code": "postal_code",
    "zip": "postal_code",
    "kod pocztowy": "postal_code",  # Polish
    "kod": "postal_code",  # Polish
    "postleitzahl": "postal_code",  # German
    "code postal": "postal_code",  # French
    "codigo postal": "postal_code",  # Spanish
    "codice postale": "postal_code",  # Italian
    "cap": "postal_code",  # Italian

    # Phone numbers
    "phone": "phone",
    "phone number": "phone",
    "telefon": "phone",  # Polish
    "telephone": "phone",  # French
    "mobile": "mobile_phone",
    "cell": "mobile_phone",
    "telefon komorkowy": "mobile_phone",  # Polish
    "telefon_komorkowy": "mobile_phone",  # Polish
    "komórka": "mobile_phone",  # Polish
    "mobile phone": "mobile_phone",
    "cellphone": "mobile_phone",
    "handy": "mobile_phone",  # German
    "portable": "mobile_phone",  # French
    "movil": "mobile_phone",  # Spanish
    "telefono": "phone",  # Italian
    "numero di telefono": "phone",  # Italian
    "cellulare": "mobile_phone",  # Italian
    "tel": "phone",  # Italian
    "tel. casa": "home_phone",  # Italian
    "tel. ufficio": "work_phone",  # Italian

    # Other phone types
    "telefon stacjonarny": "home_phone",  # Polish
    "telefon sluzbowy": "work_phone",  # Polish
    "home phone": "home_phone",
    "work phone": "work_phone",
    "faks": "fax",  # Polish
    "fax": "fax",

    # Company/Organization
    "firma": "company",  # Polish
    "company": "company",
    "entreprise": "company",  # French
    "empresa": "company",  # Spanish
    "unternehmen": "company",  # German
    "azienda": "company",  # Italian
    "società": "company",  # Italian
    "societa": "company",  # Italian

    # Tags
    "tags": TAGS_COLUMN,
    "tag": TAGS_COLUMN,
    "tagi": TAGS_COLUMN,  # Polish
    "etykiety": TAGS_COLUMN,  # Polish
    "labels": TAGS_COLUMN,
    "categories": TAGS_COLUMN,
    "etichette": TAGS_COLUMN,  # Italian
    "categorie": TAGS_COLUMN,  # Italian

    # Other fields
    "komentarz": "comment",  # Polish
    "comment": "comment",
    "data urodzenia": "birthdate",  # Polish
    "data urodzin": "birthdate",  # Polish
    "birth date": "birthdate",
    "fecha de nacimiento": "birthdate",  # Spanish
    "date de naissance": "birthdate",  # French
    "geburtsdatum": "birthdate",  # German
    "commento": "comment",  # Italian
    "data di nascita": "birthdate",  # Italian
    "data nascita": "birthdate",  # Italian
    "nascita": "birthdate"  # Italian
}

NON_NFKD_MAP = {
    u'\u0181': u'B', u'\u1d81': u'd', u'\u1d85': u'l', u'\u1d89': u'r', u'\u028b': u'v', u'\u1d8d': u'x', 
    u'\u1d83': u'g', u'\u0191': u'F', u'\u0199': u'k', u'\u019d': u'N', u'\u0220': u'N', u'\u01a5': u'p', 
    u'\u0224': u'Z', u'\u0126': u'H', u'\u01ad': u't', u'\u01b5': u'Z', u'\u0234': u'l', u'\u023c': u'c', 
    u'\u0240': u'z', u'\u0142': u'l', u'\u0244': u'U', u'\u2c60': u'L', u'\u0248': u'J', u'\ua74a': u'O', 
    u'\u024c': u'R', u'\ua752': u'P', u'\ua756': u'Q', u'\ua75a': u'R', u'\ua75e': u'V', u'\u0260': u'g', 
    u'\u01e5': u'g', u'\u2c64': u'R', u'\u0166': u'T', u'\u0268': u'i', u'\u2c66': u't', u'\u026c': u'l', 
    u'\u1d6e': u'f', u'\u1d87': u'n', u'\u1d72': u'r', u'\u2c74': u'v', u'\u1d76': u'z', u'\u2c78': u'e', 
    u'\u027c': u'r', u'\u1eff': u'y', u'\ua741': u'k', u'\u0182': u'B', u'\u1d86': u'm', u'\u0288': u't', 
    u'\u018a': u'D', u'\u1d8e': u'z', u'\u0111': u'd', u'\u0290': u'z', u'\u0192': u'f', u'\u1d96': u'i', 
    u'\u019a': u'l', u'\u019e': u'n', u'\u1d88': u'p', u'\u02a0': u'q', u'\u01ae': u'T', u'\u01b2': u'V', 
    u'\u01b6': u'z', u'\u023b': u'C', u'\u023f': u's', u'\u0141': u'L', u'\u0243': u'B', u'\ua745': u'k', 
    u'\u0247': u'e', u'\ua749': u'l', u'\u024b': u'q', u'\ua74d': u'o', u'\u024f': u'y', u'\ua751': u'p', 
    u'\u0253': u'b', u'\ua755': u'p', u'\u0257': u'd', u'\ua759': u'q', u'\xd8': u'O', u'\u2c63': u'P', 
    u'\u2c67': u'H', u'\u026b': u'l', u'\u1d6d': u'd', u'\u1d71': u'p', u'\u0273': u'n', u'\u1d75': u't', 
    u'\u1d91': u'd', u'\xf8': u'o', u'\u2c7e': u'S', u'\u1d7d': u'p', u'\u2c7f': u'Z', u'\u0183': u'b', 
    u'\u0187': u'C', u'\u1d80': u'b', u'\u0289': u'u', u'\u018b': u'D', u'\u1d8f': u'a', u'\u0291': u'z', 
    u'\u0110': u'D', u'\u0193': u'G', u'\u1d82': u'f', u'\u0197': u'I', u'\u029d': u'j', u'\u019f': u'O', 
    u'\u2c6c': u'z', u'\u01ab': u't', u'\u01b3': u'Y', u'\u0236': u't', u'\u023a': u'A', u'\u023e': u'T', 
    u'\ua740': u'K', u'\u1d8a': u's', u'\ua744': u'K', u'\u0246': u'E', u'\ua748': u'L', u'\ua74c': u'O', 
    u'\u024e': u'Y', u'\ua750': u'P', u'\ua754': u'P', u'\u0256': u'd', u'\ua758': u'Q', u'\u2c68': u'h', 
    u'\ua75b': u'r', u'\ua75f': u'v', u'\u2c61': u'l', u'\u2c65': u'a', u'\u01e4': u'G', u'\u0167': u't', 
    u'\u2c69': u'K', u'\u026d': u'l', u'\u1d6f': u'm', u'\u0271': u'm', u'\u1d73': u'r', u'\u027d': u'r', 
    u'\u1efe': u'Y'
}