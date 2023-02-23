import random

from DataReceived.models import DataBet
def logistic():
    variaveis=list(DataBet.objects.all().values_list('digit',flat=True))
    varia = [int(i) for i in variaveis]
    return sum(varia)+ random.random()*10