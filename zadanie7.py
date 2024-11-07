import random

# Losowanie, czy pada, czy nie
pogoda = random.choice(["pada", "nie pada"])

# Pętla do momentu, gdy użytkownik zgadnie poprawnie
while True:
    # Pobieranie odpowiedzi od użytkownika
    odpowiedz = input("Czy pada deszcz? (pada/nie pada): ").strip().lower()
    
    # Sprawdzanie, czy odpowiedź użytkownika jest poprawna
    if odpowiedz == pogoda:
        print("Brawo! Zgadłeś(aś) poprawnie!")
        break  # Zakończenie pętli, jeśli odpowiedź jest poprawna
    else:
        print("Niestety, to nie jest poprawna odpowiedź. Spróbuj ponownie.")
