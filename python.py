from datetime import datetime
from decimal import Decimal

DELIMITER = ";"


def zpracovani_dat(radek):
    data = radek.strip().split(DELIMITER)
    jmeno = data[0].strip()
    vek = data[1].strip()
    zvire = data[2].strip().lower() == "ano"
    pohlavi = data[3].strip()
    datum = datetime.strptime(data[4].strip(), "%Y-%m-%d")
    hodnoceni = Decimal(data[5].strip())

    if hodnoceni > Decimal("2.0"):
        zvire_text = "ano" if zvire else "ne"
        datum_text = datum.strftime("%Y-%m-%d")
        print(f"Jméno:{jmeno},\n Věk:{vek},\n Zvíře:{zvire_text},\n Pohlaví:{pohlavi},\n Datum:{datum_text}.\n Hodnocení:{hodnoceni}")
        
        return (
            "\t".join(
                [
                    jmeno,
                    vek,
                    zvire_text,
                    pohlavi,
                    datum_text,
                    str(hodnoceni),
                ]
            )
            + "\n"
        )
    return None
vystup = []

with open("data.txt", "r", encoding="utf-8") as soubor:
    for radek in soubor:
        vysledek = zpracovani_dat(radek)
        if vysledek is not None:
            vystup.append(vysledek)

with open("vypis.txt", "w", encoding="utf-8") as vystupni_soubor:
    vystupni_soubor.writelines(vystup)