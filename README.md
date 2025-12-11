# Jednoduchý Python program který zjišťuje skutečný typ souboru podle prvních bajtů.

## Funkce
- Načte soubor z CMD
- Zjistí magic number: prvních N (nastaveno na 4) bajtů souboru
- Podle magic number rozpozná typ souboru (jpeg, png, gif, pdf, zip, exe)
- Porovná hlavičku s příponou souboru
- Varuje, pokud hlavička nedpovídá s příponou souboru

##Použití
- Ve složce testfiles se nachází soubory, které se dají využít jako testovací soubory.

### Příklad použití v CMD
```bash
python checkfile.py testfiles/fake_program.jpg
```

```bash
Program vypíše:

Soubor: testfiles/fake_program.jpg
Magic number: 4D5A9000
Zjisteny typ: exe
Pripona: jpg

POZOR! Pripona neodpovida typu souboru!
>>muze se jednat o prejmenovany malware
```