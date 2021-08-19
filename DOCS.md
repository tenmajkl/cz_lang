# Jazyk Č - Dokumentace
Jazyk Č je ezoterický jazyk se syntaxemi podobnými jazyku C, akorát v češtině. K překladu jazyk Č využívá překladač napsaný v pythonu.

# Instalace
Pro instalaci překladače, naklonujte repozitář `git clone https://github.com/TENMAJKL/cz_lang.git` a ve složce cz_lang instalujte pomocí `make install`

# Kompilace
Pro kopilaci překaldače, napište `bin/pyinstaller src/cz.py`

# Základní informace
Každý soubor s kódem jazyka Č musí mít koncovku `.cz`\
Pokud chceme náš kód přeložit do jazyka c, stačí napsat `dist/cz/cz -t <soubor>`\
Pro přímou kompilaci stačí napsat `dist/cz/cz -c <soubor>`\

Zde jsou všechny značky které překladač podporuje:
- `-h` Help-Seznam všech příkazů
- `-t` Translate-Přeloží kód do jazyka c
- `-c` Compile-Přeloží kód do jazyka c a následně vykompiluje pomocí **gcc**
 
# Syntaxe
Překladač vpodstatě pouze přepisuje kód jazyka Č do jazyka c. Klíčová slova z jazyka c jsou tak pouze doslovně přeložena do češtiny.

Zde je kompletní seznam všech klíčových slov:
| C | Č |
|---|---|
| int | celé_číslo |
| float | desetinné_číslo |
| long | dlouhé_číslo |
| const | konstanta |
| double | dvojitý |
| char | znak |
| void | prázdno |
| printf | tiskni |
| main | hlavní |
| #include | #zahrň |
| struct | struktura |
| do | vykonávej |
| while | dokud |
| for | pro |
| if | pokud |
| else | jinak |
| return | vrať |
| static | statický/statické |
| switch | přepínač |
| case | případ |
| = | přiřaď |
| == | rovno |
| + | plus |
| - | minus |
| * | krát |
| / | děleno |
| ; | . | Tečka se v Č používá pro ukončení statementu, takže jiné tečky nebudou nahrazeny. Snad.

# Příklad
```
#zahrň<stdio.h>

celé_číslo hlavní()
{
    tiskni("Dobrý den přeji.").
    vrať 0.
}
```

# Poděkování
- @CoolFido který díky Matrix08 přišel na tento geniální nápad
- Komukoliv kdo udělal tutorial na tvorbu vlastního jazyka a to i přes fakt, že reálně celý jazyk stojí na regexu.
