# Różnica pomiędzy pętlą 'for' a pętlą 'while':

# Pętla 'for' jest używana, gdy z góry znamy liczbę iteracji lub chcemy iterować po jakiejś kolekcji (np. liście, ciągu znaków, zakresie).
# W pętli 'for' iterujemy po elementach w określonym zakresie lub po elementach kolekcji. Zwykle jest to bardziej zwięzłe i czytelne.
# Przykład:
for i in range(5):  # Pętla 'for' iteruje po liczbach od 0 do 4
    print(i)

# Pętla 'while' jest używana, gdy warunek kontynuacji pętli jest bardziej dynamiczny lub nie znamy liczby iteracji z góry.
# Pętla 'while' wykonuje się, dopóki warunek określony w jej nagłówku jest spełniony.
# Używamy jej, gdy chcemy kontrolować zakończenie pętli na podstawie zmiennej lub warunku, który zmienia się w czasie działania pętli.
# Przykład:
i = 0
while i < 5:  # Pętla 'while' wykonuje się dopóki i jest mniejsze niż 5
    print(i)
    i += 1

# W skrócie:
# - 'for' jest bardziej odpowiednia, gdy iterujemy po znanym zbiorze elementów (np. liczbach w zakresie, elementach listy).
# - 'while' jest bardziej elastyczna, gdy warunek kontynuacji pętli zależy od zmieniających się danych, które nie są znane z góry.
