'''[Bài tập] Erstellen einer Wörterbuch-App

Ziel
Übung:
Arbeiten mit dem Dictionary-Objekt,
Schreiben und Verwenden von Funktionen in der Programmierung,
Verwendung von if…elif…else-Anweisungen,
Verwendung von for…in-Schleifen.

Beschreibung
Schreiben Sie ein Programm, das es dem Benutzer ermöglicht, englische Wörter ins Vietnamesische zu übersetzen, indem er das zu suchende Wort eingibt. Die Liste der Wörter wird in einem Dictionary gespeichert.

Anleitung
Schritt 1: Definieren Sie eine Funktion zum Suchen und Ausgeben des übersetzten Wortes
Die Funktion erhält zwei Parameter: das Wörterbuch und das zu übersetzende Wort.
Verwenden Sie eine for…in-Schleife, um das Wörterbuch zu durchlaufen, wobei der aktuelle Wert die Wörter sind.
Innerhalb der Schleife verwenden Sie eine if-Anweisung, um zu überprüfen, ob das aktuelle Wort mit dem zu übersetzenden Wort übereinstimmt:
Wenn ja, geben Sie den Wert des aktuellen Wortes aus.

Schritt 2: Definieren Sie die Variable input_word, die den vom Benutzer eingegebenen Begriff enthält
Verwenden Sie die input()-Funktion, um den vom Benutzer eingegebenen Wert zu erhalten, und weisen Sie ihn dann der Variablen input_word zu.

Schritt 3: Rufen Sie die Funktion zum Suchen des zu übersetzenden Wortes auf
Rufen Sie die Funktion zum Suchen des zu übersetzenden Wortes auf, indem Sie das Wörterbuch und das zu übersetzende Wort als Parameter übergeben, und weisen Sie den zurückgegebenen Wert der Variablen translated_word zu.

Schritt 4: Ergebnis ausgeben
Verwenden Sie eine if…else-Anweisung, um zu überprüfen, ob die Variable translated_word einen Wert enthält:
Wenn ja, geben Sie den Wert von translated_word aus.
Wenn nicht, geben Sie eine Meldung aus, dass das eingegebene Wort nicht im Wörterbuch enthalten ist.'''

def find_and_translate_word(dictionary, word_to_translate):
    for word in dictionary:
        if word == word_to_translate:
            return f"{word} means {dictionary[word]} in vietnamese"
    return "Your word is not in this dictionary"

dictionary = {
    "hello": "Xin chào",
    "goodbye": "Tạm biệt",
    "apple": "Quả táo",
    "book": "Sách",
    "computer": "Máy tính"
}

word_to_translate = input("")

translated_word = find_and_translate_word(dictionary, word_to_translate.lower())
print(translated_word)