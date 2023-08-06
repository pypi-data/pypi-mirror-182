import sys
from decimal import Decimal


class MahlzeitException(Exception):
    pass


class MahlzeitBase():
    """
    The base class for Einkauf and Bezahlung, providing convenience methods for accessing the
    weighed length (number of elements of attributes) via len() and iterating the elements of
    attributes via iterate()
    """

    def len(self, attribute):
        """
        Return the length including gewichtung of attribute (e.g. bezahler, bezahlter, or
        esser)
        """
        return sum([ e.gewichtung for e in getattr(self, attribute) ])

    def iterate(self, attribute):
        """
        Return an iterator for the requested attribute with name and amount (by taking
        gewichtung and weighed Esser into account.
        """
        for p in getattr(self, attribute):
            yield p.name, self.betrag * p.gewichtung / self.len(attribute)


class Esser():
    """
    The class which represents bezahler, bezahlter, and esser. All user provided strings are
    converted into Esser with gewichtung 1.
    """

    def __init__(self, name, gewichtung=1):
        self.gewichtung = Decimal(gewichtung)
        if self.gewichtung < 0:
            # allow gewichtung 0 for placeholding
            raise MahlzeitException('gewichtung muss >= 0 sein')
        if '  ' in name:
            raise MahlzeitException(f'account names cannot have more than two adjacent spaces "{name}"')
        self.name = name

    def __str__(self):
        return f"Esser: {self.name} ({self.gewichtung:.2f})"


class Einkauf(MahlzeitBase):
    def __init__(self, betrag, esser, bezahler, datum=None, description=None, comment=None):
        """
        betrag may be negative to indicate income e.g. voucher or thelike
        """
        if type(esser) not in (str, list, tuple, Esser):
            raise MahlzeitException('esser must be str, list, tuple or Esser')
        if type(bezahler) not in (str, list, tuple, Esser):
            raise MahlzeitException('bezahler must be str, list, tuple or Esser')
        self.betrag = Decimal(betrag)
        self.comment = comment
        self.datum = datum
        self.description = description
        if type(esser) is str:
            self.esser = (Esser(esser),)
        elif type(esser) is Esser:
            self.esser = (esser,)
        else:
            for e in esser:
                if type(e) not in (str, Esser):
                    raise MahlzeitException(f'Element {type(e)} is not of type str or Esser')
            self.esser = [ e if type(e) is Esser else Esser(e) for e in esser ]
        if type(bezahler) is str:
            self.bezahler = (Esser(bezahler),)
        elif type(bezahler) is Esser:
            self.bezahler = (bezahler,)
        else:
            for e in bezahler:
                if type(e) not in (str, Esser):
                    raise MahlzeitException(f'Element {type(e)} is not of type str or Esser')
            self.bezahler = [ e if type(e) is Esser else Esser(e) for e in bezahler ]
        if self.len('bezahler') < 1:
            raise MahlzeitException(f'Einkauf {str(self)}: The length of bezahler (sum of all weights) must be >= 1')

    def __str__(self):
        return "Einkauf {}; {}; {}".format(self.betrag, ','.join([ str(e) for e in self.esser ]), ','.join([ str(b) for b in self.bezahler]))

    def toJournal(self, file=sys.stdout, places=3):
        if not self.datum and not self.description:
            raise MahlzeitException(f"Datum and description not set for {self}. Cannot output journal")
        if self.comment:
            print(";", self.comment, file=file)
        print(self.datum, self.description, file=file)
        for name, betrag in self.iterate('bezahler'):
            print(f"\t{name}:einkauf:bezahler\t\t{-betrag:.{places}f}", file=file)
        for name, betrag in self.iterate('esser'):
            print(f"\t{name}:einkauf:esser\t\t{betrag:.{places}f}", file=file)
        print("\trounding\n", file=file)


class Bezahlung(MahlzeitBase):
    def __init__(self, bezahler, bezahlter, betrag, datum=None, description=None, comment=None):
        if betrag <= 0:
            raise MahlzeitException('betrag <= 0')
        if type(bezahler) not in (str, tuple, list, Esser):
            raise MahlzeitException('bezahler must be str, tuple, or list')
        if type(bezahlter) not in (str, tuple, list, Esser):
            raise MahlzeitException('bezahlter must be str, tuple, or list')
        self.betrag = Decimal(betrag)
        self.comment = comment
        self.datum = datum
        self.description = description
        if type(bezahler) is str:
            self.bezahler = (Esser(bezahler),)
        elif type(bezahler) is Esser:
            self.bezahler = (bezahler,)
        else:
            for e in bezahler:
                if type(e) not in (str, Esser):
                    raise MahlzeitException(f'Element {type(e)} is not of type str or Esser')
            self.bezahler = [ e if type(e) is Esser else Esser(e) for e in bezahler ]
        if self.len('bezahler') < 1:
            raise MahlzeitException(f'Bezahlung {str(self)}: The length of bezahler (sum of all weights) must be >= 1')
        if type(bezahlter) is str:
            self.bezahlter = (Esser(bezahlter),)
        elif type(bezahlter) is Esser:
            self.bezahlter = (bezahlter,)
        else:
            for e in bezahlter:
                if type(e) not in (str, Esser):
                    raise MahlzeitException(f'Element {type(e)} is not of type str or Esser')
            self.bezahlter = [ e if type(e) is Esser else Esser(e) for e in bezahlter ]
        if self.len('bezahlter') < 1:
            raise MahlzeitException(f'Bezahlung {str(self)}: The length of bezahlter (sum of all weights) must be >= 1')


    def toJournal(self, file=sys.stdout, places=3):
        if not self.datum and not self.description:
            raise MahlzeitException(f"Datum and description not set for {self}. Cannot output journal")
        if self.comment:
            print(";", self.comment, file=file)
        print(self.datum, self.description, file=file)
        for name, betrag in self.iterate('bezahler'):
            print(f"\t{name}:bezahlung:bezahler\t\t{-betrag:.{places}f}", file=file)
        for name, betrag in self.iterate('bezahlter'):
            print(f"\t{name}:bezahlung:bezahlter\t\t{betrag:.{places}f}", file=file)
        print("\trounding\n", file=file)


class Mahlzeit():
    def __init__(self):
        self.einkaeufe = list()
        self.bezahlungen = list()

        # for usage in context
        self.datum = None
        self.description = None
        self.comment = None

    def __call__(self, datum=None, description=None, comment=None):
        self.datum = datum
        self.description = description
        self.comment = comment
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.datum = None
        self.description = None
        self.comment = None

    def einkauf(self, betrag, esser, bezahler, datum=None, description=None, comment=None):
        self.einkaeufe.append(Einkauf(betrag, esser, bezahler,
            datum=datum if datum else self.datum,
            description=description if description else self.description,
            comment=comment if comment else self.comment,
        ))

    def bezahlung(self, bezahler, bezahlter, betrag, datum=None, description='Bezahlung', comment=None):
        self.bezahlungen.append(Bezahlung(bezahler, bezahlter, betrag,
            datum=datum if datum else self.datum,
            description=description if description else self.description,
            comment=comment if comment else self.comment,
        ))

    def calc(self):
        ausgleich = dict()
        for e in self.einkaeufe:
            for name, betrag in e.iterate('bezahler'):
                ausgleich[name] = ausgleich.get(name, Decimal(0)) - betrag
            for name, betrag in e.iterate('esser'):
                ausgleich[name] = ausgleich.get(name, Decimal(0)) + betrag
        for b in self.bezahlungen:
            for name, betrag in b.iterate('bezahler'):
                ausgleich[name] = ausgleich.get(name, Decimal(0)) - betrag
            for name, betrag in b.iterate('bezahlter'):
                ausgleich[name] = ausgleich.get(name, Decimal(0)) + betrag
        return ausgleich

    def pretty(self, file=sys.stdout, places=2):
        self.pprint(file=file, places=places)

    def pprint(self, file=sys.stdout, places=2):
        for name, betrag in sorted(self.calc().items(), key=lambda x: -x[1]):
            print(f"{name:10s} {betrag:.{places}f}", file=file)

    def reset(self):
        self.einkaeufe = list()
        self.bezahlungen = list()

    def journal(self, file=sys.stdout, places=3):
        for eink in self.einkaeufe:
            eink.toJournal(file=file, places=places)

        for bez in self.bezahlungen:
            bez.toJournal(file=file, places=places)
