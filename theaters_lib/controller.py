def read_theaters(theaters_data: list) -> None:
    for theater in theaters_data:
        print(
            f"{theater['name']} | "
            f"{theater['location']} | "
            f"spektakle: {theater['performances']}"
        )


def add_theater(theaters_data: list) -> None:
    name = input('Podaj nazwę teatru: ')
    location = input('Podaj miasto: ')

    theaters_data.append(
        {
            'name': name,
            'location': location,
            'performances': [],
            'clients': [],
            'employees': []
        }
    )


def remove_theater(theaters_data: list) -> None:
    name = input('Podaj nazwę teatru do usunięcia: ')

    for theater in theaters_data:
        if theater['name'] == name:
            theaters_data.remove(theater)
            break


def update_theater(theaters_data: list) -> None:
    name = input('Podaj nazwę teatru do zmiany: ')

    for theater in theaters_data:
        if theater['name'] == name:
            theater['name'] = input('Nowa nazwa: ')
            theater['location'] = input('Nowe miasto: ')
            break