# **1. Überprüfung des Barcodes**
#
# * Auf Waren befindet sich oft eine Zahlenreihe mit 13 Ziffern, die als Barcode bezeichnet wird. 
#   Diese Zahlenreihe wird nach folgender Regel erstellt: Ein Barcode ist eine Zeichenfolge mit genau 13 Ziffern, 
#   wobei die letzte Ziffer als Prüfziffer `C` bezeichnet wird. 
#   Bezeichnen wir `A` als die Summe der Ziffern an ungeraden Positionen (außer der Prüfziffer `C`). 
#   Bezeichnen wir `B` als die Summe der Ziffern an geraden Positionen. 
#   Setzen wir `D = A + 3B`. Wenn der Rest von `D` bei der Division durch 10 nicht null ist, 
#   dann ist `F=10-Rest`, andernfalls ist `F = 0`. 
#   Ein Barcode gilt als korrekt, wenn `F=C` ist. 
#   Definieren Sie eine Funktion, die überprüft, ob eine 13-stellige Zahl ein Barcode ist oder nicht. 
#   Zum Beispiel: `4902778120972` ist ein korrekter Barcode, `4902778120973` ist kein Barcode.
# 
# * Eine Datei `barcode.txt` enthält eine Liste von Zahlen, wobei jede Zahl in einer eigenen Zeile steht. 
#   Definieren Sie eine Funktion, um die angegebene Datei zu lesen, jede Zahl in der Datei zu überprüfen, 
#   ob sie ein Barcode ist oder nicht, und die Ergebnisse in einem Wörterbuch mit der Struktur 
#   `{'Zahl': 'ja/nein'}` zu speichern (`ja` - wenn die Zahl ein Barcode ist, `nein` - wenn die Zahl kein Barcode ist). 
#   Speichern Sie die Überprüfungsergebnisse in der Datei `barcode_validation.txt`, 
#   wobei jede Zeile eine Zahl und das Überprüfungsergebnis enthält. 
#   Zum Beispiel `4902778120972 - ja` oder `4902778120973 - nein`.


def check_barcode(barcode):
    a = 0
    for i in range(0, 11, 2):
        a += int(barcode[i])

    b = 0
    for i in range(1, 12, 2):
        b += int(barcode[i])

    d = a + 3 * b

    if d % 10 != 0:
        f = 10 - d % 10
    else:
        f = 0

    return f == int(barcode[12])  


def rw_barcode():
    results = {}
    
    with open("barcode.txt", "r") as rfile:
        for line in rfile:
            barcode = line.strip()  
            if len(barcode) == 13 and barcode.isdigit():  
                is_valid = check_barcode(barcode)
                results[barcode] = 'yes' if is_valid else 'no'
            else:
                results[barcode] = 'no'  

    with open("barcode_validation.txt", "w") as wfile:
        for barcode, result in results.items():
            wfile.write(f"{barcode} - {result}\n")

rw_barcode()


