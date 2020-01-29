class Item:
    def __init__(self, item_name, item_desc):
        self.item_name = item_name
        self.item_desc = item_desc

    # def take_item(player, curr_rm):
    #     item_to_add = curr_rm.rm_items.remove(curr_rm.rm_items[0])
    #     player.items_found.append(item_to_add)
    #     return f'{curr_rm.rm_items}'
