from gilded_rose import Item, update_quality
from constants import AGED_BRIE


def test_aged_brie_increases_quality():
    item = Item(AGED_BRIE, 0, 5)
    update_quality([item])
    # as sell in is 0 that's means it already passed sell in one day
    assert 7 == item.quality
