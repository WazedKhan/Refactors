from typing import Iterable
from item import Item
from item_updater import DefaultItemUpdater, ITEM_UPDATERS


def update_quality(items: Iterable[Item]):
    for item in items:
        update_quality_single(item)


def update_quality_single(item: Item) -> None:
    item_updater = ITEM_UPDATERS.get(item.name, DefaultItemUpdater())

    item_updater.update_sell_in(item)
    item_updater.update_quality(item)
