from src.planet import Planet
from src.buggy import Buggy


def get_user_input():
    """Bekéri és validálja a felhasználói inputot a kezdőállapothoz."""
    while True:
        try:
            x = int(input("Add meg a kezdő X koordinátát: "))
            y = int(input("Add meg a kezdő Y koordinátát: "))
            break
        except ValueError:
            print("Hibás formátum! Kérlek, számot adj meg.")

    while True:
        direction = input("Add meg a kezdő irányt (N, E, S, W): ").upper()
        if direction in ['N', 'E', 'S', 'W']:
            break
        else:
            print("Hibás irány! Kérlek, az 'N', 'E', 'S', 'W' értékek egyikét add meg.")

    return x, y, direction


def run_simulation():
    """Fő szimulációs ciklus."""
    print("--- Holdjáró Szimulátor ---")

    # 1. Hozzuk létre a környezetet
    # Statikus bolygó néhány akadállyal a példa kedvéért
    akadalyok = [(1, 4), (5, 8), (7, 2)]
    bolygo = Planet(latitudes=10, longitudes=10, obstacles=akadalyok)
    print(f"A bolygó mérete: 10x10. Akadályok itt: {akadalyok}")

    # 2. Kérjük be a felhasználótól a kezdőpozíciót
    start_x, start_y, start_dir = get_user_input()

    # 3. Hozzuk létre a járművet a megadott adatokkal
    holdjaro = Buggy(x=start_x, y=start_y, direction=start_dir, planet=bolygo)

    print("\nA szimuláció elindult. Parancsok: 'f' (előre), 'b' (hátra), 'l' (balra), 'r' (jobbra), 'exit' (kilépés)")

    # 4. Parancs-ciklus
    while True:
        print(f"\nJelenlegi pozíció: ({holdjaro.x}, {holdjaro.y}), Irány: {holdjaro.direction}")
        command = input("Parancs > ").lower()

        if command == 'exit':
            print("A szimuláció leállt.")
            break

        if command in ['f', 'b', 'l', 'r']:
            report = holdjaro.move(command)
            if report == "AKADÁLY":
                print(">>> Jelentés: AKADÁLY a következő pozíción!")
            else:
                print(">>> Jelentés: A manőver sikeres.")
        else:
            print(">>> Ismeretlen parancs.")


if __name__ == "__main__":
    run_simulation()