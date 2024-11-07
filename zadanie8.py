# Inicjalizacja licznika odpowiedzi "nie"
nie_liczba = 0

# Pętla, która będzie działała, dopóki użytkownik nie odpowie "tak"
while True:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").strip().lower()
    
    if odpowiedz == "nie":
        nie_liczba += 1  # Zwiększamy licznik, jeśli odpowiedź to "nie"
    elif odpowiedz == "tak":
        print(f"Liczba odpowiedzi 'nie': {nie_liczba}")
        break  # Kończymy program, gdy użytkownik odpowie "tak"
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")
