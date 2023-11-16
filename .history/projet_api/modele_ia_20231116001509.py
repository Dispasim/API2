from projet.models import Order
from collections import Counter
import random
from datetime import date
def transform(text):
    mots = text.split()
    mots_frequent = Counter(mots).most_common(5)
    transformation = Order(text= text, isin = mots_frequent[0],trade_date=date.today(),settlement_date=date.today(),primary_brocker=mots_frequent[1], sens = mots_frequent[2], trader = mots_frequent[3], price = random.randint(1, 100), size = random.randint(1, 100), price_type = mots_frequent[4], currency = mots_frequent[5], clean_dirty = mots_frequent[6] )
    return transformation





