# Entity class
# Dizajn 1:
# -(Entita) može byť zároveň prepojením entít ktorá na ne priamo odkazuje
# -(Entita) má operatívny paralelný priestor (Task) ktorý načíta vstupné dáta ktoré sprostredkováva
#  (komunikačný kanál.)
#
# -(Entita) može s ostatnými entitami mat otvorený lubovolný počet komunikačných kanálov
# -(Komunikačný kanál) definuje sposob komunikácie entít napríklad založený na posielaní správ ostatným entitám
#  alebo na zdielanie nejakého stavu medzi entitami.
#  Pričom zdielanie stavu funguje tak, že pri každej zmene zdielaneho atribútu je poslaná správa všetkým entitám
#  ktorým je atribút zdielaný
#
# -alebo -> entity A B majú povolené obojstranne komunikovať.
#  entita A pošle entite B správu o stave jedného jej atribútu Teplota = 99°.
#  entita B nevedela o tom, že entita B má atribút Teplota a do záznamu o entite A založí nový atribút a priradí
#  mu hodnotu 99°


#
#


class Entity:
    count = 0

    def __init__(self):
        Entity.count += 1
        self.data = None

    def __del__(self):
        Entity.count -= 1
