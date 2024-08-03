from typing import Iterable
from item import Item
from constants import AGED_BRIE, SULFURAS, BACKSTAGE_PASSES


def update_quality(items: Iterable[Item]):
    for item in items:
        update_quality_single(item)


def decrease_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(0, item.quality - amount)


def increase_item_quality(item: Item, amount: int = 1, max_quality: int = 50) -> None:
    item.quality = min(max_quality, item.quality + amount)


def update_quality_single(item: Item) -> None:

    if item.name == SULFURAS:
        pass
    else:
        item.sell_in = item.sell_in - 1

    if item.name == AGED_BRIE:
        increase_item_quality(item)

        if item.sell_in < 0:
            increase_item_quality(item)

    elif item.name == BACKSTAGE_PASSES:
        increase_item_quality(item)
        if item.sell_in < 10:
            increase_item_quality(item)
        if item.sell_in < 5:
            increase_item_quality(item)

        if item.sell_in < 0:
            item.quality = 0

    elif item.name == SULFURAS:
        pass
    else:
        decrease_item_quality(item)
        if item.sell_in < 0:
            decrease_item_quality(item)
