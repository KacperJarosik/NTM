#-----------------------------------METODYKA--------------------------------------------------------------------------------------------------
"""Liczba sprzedanych opakowań leków stosowanych w leczeniu nietrzymania moczu oraz ich koszty w podziale na refundację i dopłatę pacjenta. 
Wyodrębniono refundację dla pacjentów z uprawnieniami dodatkowymi: inwalida wojenny"""
class Leki2019:
    def __init__(self):
        self.solifenacyna = {'liczba_opakowan_tys': 687, 'koszt_refundacji_tys_zl': 24545, 'w_tym_refundacja-uprawnienia_dodatkowe_tys_zl': 1048, 
                             'doplata_pacjenta_tys_zl': 32291, 'koszty_calkowite_tys_zl': 56837}
        self.tolterodyna = {'liczba_opakowan_tys': 303, 'koszt_refundacji_tys_zl': 4654, 'w_tym_refundacja-uprawnienia_dodatkowe_tys_zl': 158, 
                        'doplata_pacjenta_tys_zl': 3569, 'koszty_calkowite_tys_zl': 8224}
        
class Leki2020:
    def __init__(self):
        self.solifenacyna = {'liczba_opakowan_tys': 663, 'koszt_refundacji_tys_zl': 14968, 'w_tym_refundacja-uprawnienia_dodatkowe_tys_zl': 553, 
                                'doplata_pacjenta_tys_zl': 13221, 'koszty_calkowite_tys_zl': 28189}
        self.tolterodyna = {'liczba_opakowan_tys': 165, 'koszt_refundacji_tys_zl': 1631, 'w_tym_refundacja-uprawnienia_dodatkowe_tys_zl': 88, 
                        'doplata_pacjenta_tys_zl': 2420, 'koszty_calkowite_tys_zl': 4051}