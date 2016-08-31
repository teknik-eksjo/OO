from math import gcd


class Circle():
    """Implementation av klassen `Circle`.

    Klassen ska ha attributen `radius` och `color`. Attributet `radius` ska
    vara obligatioriskt och attributet `color` ska ha ett standardvärdet `red`.

    Klassen ska ha metoderna `diameter()` och `area()` som returnerar
    lämpliga värden.
    """
    pass


class BankAccount():
    """Implementation av klassen `BankAccount`.

    Klassen ska ha attributet `balance` med standardvärdet 0.

    Klassen ska ha metoderna `deposit` och `withdraw` som används för att
    sätta in (`deposit`)och ta ut (`withdraw`) pengar från kontot. Båda dessa
    ska returnera aktuell kontobalans efter operationen.
    """
    pass


class MinimumBalanceAccount():
    """Implementation av klassen `MinimumBalanceAccount`.

    Klassen ska ärva av `BankAccount` och initieras med ett attribut
    `minimum_balance`. Denna lägsta balans ska sedan tvingas.

    När man försöker ta ut mer pengar än kontobalansen ska ett
    `ValueError`-exception kastas.
    """
    pass


class RationalNumber():
    """Implementation av klass för rationella tal ex: 4/7, 3/11, 9/2.

    Klassen initieras med täljare och nämnare och ska klara av operationerna
    addition, subtraktion, multiplikation, division och jämförelse.
    """
    def __init__(self, numerator, denominator):
        if not denominator:
            raise ValueError

        self.n = numerator
        self.d = denominator

    @staticmethod
    def _reduce(n, d):
        common = int(gcd(n, d))
        n = n // common
        d = d // common
        return RationalNumber(n, d)

    def __eq__(self, other):
        return self.n == other.n and self.d == other.d

    def __repr__(self):
        return '<RationalNumber: {}/{}>'.format(self.n, self.d)

    def __str__(self):
        return '{}/{}'.format(self.n, self.d)
