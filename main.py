class KontoBankowe:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def wplata(self, kwota):
        self.saldo += kwota

    def wyplata(self, kwota):
        if kwota > self.saldo:
            print("Nie można wypłacić kwoty większej niż saldo konta!")
        else:
            self.saldo -= kwota

    def stan_konta(self):
        print(f"Saldo konta wynosi: {self.saldo} zł")


# przykładowe użycie klasy KontoBankowe
konto = KontoBankowe()
konto.stan_konta() # Saldo konta wynosi: 0 zł

konto.wplata(100)
konto.stan_konta() # Saldo konta wynosi: 100 zł

konto.wyplata(50)
konto.stan_konta() # Saldo konta wynosi: 50 zł

konto.wyplata(100)
konto.stan_konta() # Nie można wypłacić kwoty większej niż saldo konta!
