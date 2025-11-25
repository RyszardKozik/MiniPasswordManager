# Mini Password Manager

Mini Password Manager to prosty program do bezpiecznego przechowywania i generowania haseł, napisany w Pythonie.  
Używa szyfrowania przy pomocy biblioteki **cryptography**, aby chronić Twoje dane.

---

## Funkcje

- Dodawanie nowych haseł z możliwością regenerowania losowego hasła  
- Usuwanie zapisanych haseł  
- Szyfrowanie i odszyfrowanie haseł przy użyciu klucza `key.key`  
- Prosta i intuicyjna obsługa  
- Przenośność: program można uruchomić jako `.exe` bez instalowania Pythona  

---

## Wymagania

- Python 3.10+ (jeśli uruchamiasz w wersji .py)  
- Biblioteki Python:

```bash
pip install -r requirements.txt
Instalacja i uruchomienie

Sklonuj repozytorium:

git clone https://github.com/RyszardKozik/MiniPasswordManager.git
cd MiniPasswordManager


Utwórz i aktywuj środowisko wirtualne:

python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows PowerShell
# lub
source .venv/bin/activate    # Mac/Linux


Zainstaluj wymagania:

pip install -r requirements.txt


Uruchom program:

python main.py

Użycie wersji .exe

Wygeneruj .exe przy pomocy PyInstaller:

pyinstaller --onefile --windowed main.py


Skopiuj dist/main.exe oraz key.key na inny komputer.

Uruchom main.exe i dodawaj nowe hasła – baza (passwords.db) powstanie automatycznie.

Bezpieczeństwo

Nie udostępniaj key.key innym osobom, bo to jest klucz do odszyfrowania Twojej bazy haseł.

passwords.db przechowuje zaszyfrowane hasła i można go tworzyć lokalnie.

Licencja

Projekt open-source – możesz korzystać, modyfikować i rozpowszechniać zgodnie z potrzebą.
