
Tekst = 'atcaatgatcaacgtaagcttctaagcATGATCAAGgtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagATGATCAAGagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaATGATCAAGctgctgctcttgatcatcgtttc'

k = int(input('Prosze o podanie dlugosci meru: '))
assert k > 0, 'Dlugosc meru musi byc wieksza niz zero!'

def FrequentPatterns(Tekst, k):
    Tekst = Tekst.upper()  # Zmieniam wszystkie litery w Tekst na duze litery
    Count = []
    FrequentPatterns = []

    for i in range(0, len(Tekst) - k):  # Pętla iterujaca od 0 do konca Tekstu
        Pattern = Tekst[i:i + k]  # Wyciecie czesci tekstu od aktualnej iteracji do iteracji + dlugosc meru.
        Ilosc = 0
        for j in range(0, len(Tekst)):  # Petla iterujaca od 0 do konca tekstu - dlugosc meru by nie wyjsc
            #  poza tekst
            if Tekst[j:j + len(Pattern)] == Pattern:  # Jesli fragment tekstu == aktualnemu merowi.
                Ilosc += 1  # Zwiekszana jest zmienna ilosc.
        Count.append(Ilosc)  # Zmienna ilosc jest zapiswyana do wektora Count dla kazdego meru.

    assert len(Count) != 0, 'Mer jest dluzszy niz zmienna Tekst!'

    MaxCount = max(Count)  # Zapisana zostaje najwyzsza wartosc z wektora Count

    for i in range(0, len(Tekst) - k):  # Petla iterujaca od 0 do konca tekstu - dlugosc meru
        if Count[i] == MaxCount:  # Kazdy mer ktorego Count byl najwyzszy
            FrequentPatterns.append(Tekst[i:i+k])  # Zostaje zapisany do wektora FrequentPatterns

    assert len(Count) >= len(FrequentPatterns), 'Zle dziala przepisanie z Count do FrequentPatterns!'

    FrequentPatterns = list(set(FrequentPatterns))  # Wykorzystuje brak duplikatow w set by usunac powtarzajce sie mery z
    #  wektora Frequent words
    return FrequentPatterns


assert FrequentPatterns('TATAGCGCTA', 2) == ['TA'], 'FrequentAssert zle wyszukuje mery!'

Wynik = FrequentPatterns(Tekst, k)

with open('plik.txt', 'w') as plik:
    print(Wynik, file=plik)  # Wynik pracy programu zostaje zapisany do pliku tekstowego
