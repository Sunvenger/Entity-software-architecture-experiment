# Entity class
# -Entita može byť zároveň prepojením entít ktorá na ne priamo odkazuje
# -Entita má operatívny paralelný priestor (Task) ktorý načíta vstupné dáta ktoré sprostredkováva Prepojenie.
# V tomto momente sú dáta prenesené do paralelného priestoru entity
#
#
# Prepojenia samotné môžu mať definované ľubovolné operácie ktoré môžu manipulovať s obomi prepojenými entitami
#


class Entity:
    count = 0

    def __init__(self):
        Entity.count += 1
        self.data = None

    def __del__(self):
        Entity.count -= 1
