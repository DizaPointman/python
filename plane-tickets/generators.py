"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_letters = ['A', 'B', 'C', 'D']
    for i in range(number):
        yield seat_letters[i % len(seat_letters)]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    seat_letters = ['A', 'B', 'C', 'D']
    counter = number
    
    for i in range(number):
        if i + 1 == 13:
            continue
        for j in range(4):
            if counter > 0:
                yield f"{i + 1}{seat_letters[j % len(seat_letters)]}"
                counter -= 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_letters = ['A', 'B', 'C', 'D']
    number = len(passengers)
    counter = 0
    result = {}
    
    for i in range(number):
        if i + 1 == 13:
            continue
        for j in range(4):
            if counter < number:
                result[passengers[counter]] = f"{i + 1}{seat_letters[j % len(seat_letters)]}"
                counter += 1
    return result

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for num in seat_numbers:
        yield (num + flight_id).ljust(12, '0')
