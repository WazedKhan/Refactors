# item_updater

from typing import Protocol
from constants import AGED_BRIE, BACKSTAGE_PASSES, SULFURAS
from utils import decrease_item_quality, increase_item_quality, Item


class ItemUpdater(Protocol):
    def update_quality(self, item: Item): ...

    def update_sell_in(self, item: Item): ...


class DefaultItemUpdater(ItemUpdater):
    def update_quality(self, item: Item) -> None:
        decrease_item_quality(item)
        if item.sell_in < 0:
            decrease_item_quality(item)

    def update_sell_in(self, item: Item) -> None:
        item.sell_in = item.sell_in - 1


class AgedBrieUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 0:
            increase_item_quality(item)


class BackStagePassesUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 10:
            increase_item_quality(item)
        if item.sell_in < 5:
            increase_item_quality(item)

        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        pass

    def update_sell_in(self, item: Item) -> None:
        pass


ITEM_UPDATERS = {
    AGED_BRIE: AgedBrieUpdater(),
    BACKSTAGE_PASSES: BackStagePassesUpdater(),
    SULFURAS: SulfurasUpdater(),
}
