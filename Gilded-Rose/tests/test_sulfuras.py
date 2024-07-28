from gilded_rose import Item, update_quality

SULFURAS = "Sulfuras, Hand of Ragnaros"


def test_sulfuras_sell_in_dose_not_decrease():
    __sell_in = 1
    item = Item(SULFURAS, __sell_in, 1)
    update_quality([item])
    assert __sell_in == item.sell_in


def test_sulfuras_quality_dose_not_decrease():
    __quality = 1
    item = Item(SULFURAS, 1, __quality)
    update_quality([item])
    assert __quality == item.quality


def test_sulfuras_quality_80_dose_not_alters():
    __quality = 80
    item = Item(SULFURAS, 1, __quality)
    update_quality([item])
    assert __quality == item.quality
