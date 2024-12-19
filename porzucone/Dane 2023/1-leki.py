#-----------------------------------METODYKA--------------------------------------------------------------------------------------------------
"""Liczba sprzedanych opakowań leków stosowanych w leczeniu nietrzymania moczu oraz ich koszty w podziale na refundację i dopłatę pacjenta. 
Wyodrębniono refundację dla pacjentów z uprawnieniami dodatkowymi: inwalida wojenny, żołnierz zasadniczej służby wojskowej, senior, weteran z uszczerbkiem zdrowia powyżej 30%y"""

class Rob:
    def __init__(self):
        self.solifenacyna = {'liczba_opakowan_tys': 0, 'koszt_refundacji_tys_zl': 0, 'w_tym_refundacja-uprawnienia_dodatkowe_tys_zl': 0, 
                             'doplata_pacjenta_tys_zl': 0, 'koszty_calkowite_tys_zl': 0}
        self.tolterodyna = {'liczba_opakowan_tys': 0, 'koszt_refundacji_tys_zl': 0, 'w_tym_refundacja-uprawnienia_dodatkowe_tys_zl': 0, 
                        'doplata_pacjenta_tys_zl': 0, 'koszty_calkowite_tys_zl': 0}