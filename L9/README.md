# Zad1
## Stos w funkcji login zajmują kolejno:
- wskaźnik do tablicy code
- adres instrukcji po wywołaniu main
- wartość stack base pointera
- zmienna secret
- zmienna authenticated
- tablica pass[10]
jako że stos rośnie od największego adresu do najmniejszego, nadpisując "pass" zbyt długim stringiem, nadpisujemy też poprzednio zapisane wartości, czyli "authenticated". String nie może być zbyt długi, bo nadpiszemy też poprzednie zmienne.