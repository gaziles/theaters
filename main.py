from theaters_lib.model import theaters
from theaters_lib.controller import (
    read_theaters,
    add_theater,
    remove_theater,
    update_theater
)

while True:
    print('0 - zakończ program')
    print('1 - wyświetl teatry')
    print('2 - dodaj teatr')
    print('3 - usuń teatr')
    print('4 - aktualizuj teatr')

    choice = input('Wybierz opcję: ')

    if choice == '0':
        break

    if choice == '1':
        read_theaters(theaters)

    if choice == '2':
        add_theater(theaters)

    if choice == '3':
        remove_theater(theaters)

    if choice == '4':
        update_theater(theaters)