#-----------------------------------METODYKA--------------------------------------------------------------------------------------------------
"""Koszty refundacji hospitalizacji w ramach zabiegowych jednorodnych grup pacjentów ze sprawozdanym rozpoznaniem nietrzymania moczu. 
Koszty JGP z wybranymi procedurami wg klasyfikacji ICD 9 dotyczą łącznych kosztów hospitalizacji, w ramach których sprawozdano wyodrębnione procedury. 
Załączona lista dotyczy świadczeniodawców, którzy w 2020 r. sprawozdali co najmniej 5 hospitalizacji jako L91 IMPLANTACJA LUB 
WYMIANA HYDRAULICZNEGO ZWIERACZA CEWKI MOCZOWEJ (AUS)."""
class Zabiegi2019:
    def __init__(self):
        self.zabiegi_operacyjne_ogolem_mezczyzni = {'liczba_zabiegow': 334,  'koszt_JGP_tys_zl': 4286}
        self.zabiegi_operacyjne_ogolem_kobiety = {'liczba_zabiegow': 7928,  'koszt_JGP_tys_zl': 22967}