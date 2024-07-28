from gilded_rose import Item, update_quality

AGED_BRIE = "Aged Brie"


def test_item_does_nt_change_name():
    item = Item("foo", 0, 0)
    update_quality([item])
    assert "foo" == item.name


def test_item_sell_in_decreases():
    item = Item(name="foo", sell_in=1, quality=0)
    update_quality([item])
    assert item.sell_in == 0


def test_item_quality_decreases():
    item = Item(name="foo", sell_in=1, quality=1)
    update_quality([item])
    assert item.quality == 0


def test_item_quality_degrades_twice_as_fast_after_sell_in():
    item = Item(name="foo", sell_in=0, quality=5)
    update_quality([item])
    assert item.quality == 3


def test_quality_never_negative():
    item = Item(name="foo", sell_in=0, quality=0)
    update_quality([item])
    assert item.quality == 0


def test_quality_never_more_then_50():
    item = Item(name=AGED_BRIE, sell_in=0, quality=50)
    update_quality([item])
    assert item.quality == 50
