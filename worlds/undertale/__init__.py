from .Items import UndertaleItem, item_table, required_armor, required_weapons, non_key_items, key_items, \
    junk_weights_all, plot_items, junk_weights_neutral, junk_weights_pacifist, junk_weights_genocide, \
    junk_weights_cut_items
from .Locations import UndertaleAdvancement, advancement_table, exclusion_table
from .er_rules import set_er_location_rules
from .er_scripts import create_er_regions, create_er_regions_vanilla
from worlds.generic.Rules import exclusion_rules
from BaseClasses import Tutorial, Item
from .Options import UndertaleOptions
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components
from multiprocessing import Process
from typing import Dict
import Utils
import math


def run_client():
    print('running undertale client')
    from .UndertaleClient import main  # lazy import
    p = Process(target=main)
    p.start()


# components.append(Component("Undertale Client", "UndertaleClient"))
components.append(Component("Undertale Client", func=run_client))


def data_path(file_name: str):
    import pkgutil
    return pkgutil.get_data(__name__, "data/" + file_name)


class UndertaleWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago Undertale software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Mewlif"]
    )]


class UndertaleWorld(World):
    """
    Undertale is an RPG where every choice you make matters. You could choose to hurt all the enemies, eventually
    causing genocide of the monster species. Or you can spare all the enemies, befriending them and freeing them
    from their underground prison.
    """
    game = "Undertale"
    options_dataclass = UndertaleOptions
    options: UndertaleOptions
    web = UndertaleWeb()

    topology_present = True

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in advancement_table.items()}

    data_version = 7
    undertale_portal_pairs: Dict[str, str]
    er_portal_hints: Dict[int, str]

    def _get_undertale_data(self):
        return {
            "world_seed": self.multiworld.per_slot_randoms[self.player].getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
            "client_version": self.required_client_version,
            "race": self.multiworld.is_race,
            "route_required": self.options.route_required.current_key,
            "starting_area": self.options.starting_area.current_key,
            "temy_include": bool(self.options.temy_include.value),
            "only_flakes": bool(self.options.only_flakes.value),
            "no_equips": bool(self.options.no_equips.value),
            "key_hunt": bool(self.options.key_hunt.value),
            "key_pieces": self.options.key_pieces.value,
            "rando_love": bool(self.options.rando_love.value),
            "rando_stats": bool(self.options.rando_stats.value),
            "prog_armor": bool(self.options.prog_armor.value),
            "prog_weapons": bool(self.options.prog_weapons.value),
            "rando_item_button": bool(self.options.rando_item_button.value),
            "kill_sanity": bool(self.options.kill_sanity.value),
            "rando_jump": bool(self.options.rando_jump.value),
            "cut_items": bool(self.options.cut_items.value),
            "kill_sanity_pack_size": self.options.kill_sanity_pack_size.value,
            "ice_traps": self.options.ice_traps.value,
            "spare_sanity": bool(self.options.spare_sanity.value),
            "entrance_rando": bool(self.options.entrance_rando.value),
            "spare_sanity_max": self.options.spare_sanity_max.value,
            "spare_sanity_pack_size": self.options.spare_sanity_pack_size.value,
            "Entrance Rando": self.undertale_portal_pairs
        }

    def get_filler_item_name(self):
        if self.options.route_required == "all_routes":
            junk_pool = junk_weights_all.copy()
        elif self.options.route_required == "genocide":
            junk_pool = junk_weights_genocide.copy()
        elif self.options.route_required == "neutral":
            junk_pool = junk_weights_neutral.copy()
        elif self.options.route_required == "pacifist":
            junk_pool = junk_weights_pacifist.copy()
        else:
            junk_pool = junk_weights_all.copy()
        if self.options.cut_items:
            junk_pool = junk_pool | junk_weights_cut_items.copy()
        if not self.options.only_flakes:
            return self.multiworld.random.choices(list(junk_pool.keys()), weights=list(junk_pool.values()))[0]
        else:
            return "Temmie Flakes"

    def create_items(self):
        exclusion_pool = set()
        # Generate item pool
        itempool = []
        # Add all required progression items
        for name, num in key_items.items():
            itempool += [name] * num
        for name, num in required_armor.items():
            itempool += [name] * num
        for name, num in required_weapons.items():
            itempool += [name] * num
        for name, num in non_key_items.items():
            itempool += [name] * num
        if self.options.rando_item_button:
            itempool += ["ITEM"]
        else:
            self.multiworld.push_precollected(self.create_item("ITEM"))
        if not self.options.rando_jump:
            itempool.remove("Jump")
            self.multiworld.push_precollected(self.create_item("Jump"))
        self.multiworld.push_precollected(self.create_item("FIGHT"))
        self.multiworld.push_precollected(self.create_item("ACT"))
        self.multiworld.push_precollected(self.create_item("MERCY"))
        if self.options.route_required == "genocide":
            itempool = [item for item in itempool if item != "Popato Chisps" and item != "Stained Apron" and
                        item != "Nice Cream" and item != "Hot Cat" and item != "Hot Dog...?" and item != "Punch Card"]
        elif self.options.route_required == "neutral":
            itempool = [item for item in itempool if item != "Popato Chisps" and item != "Hot Cat" and
                        item != "Hot Dog...?"]
        if self.options.route_required == "pacifist" or \
                self.options.route_required == "all_routes":
            itempool += ["Undyne Letter EX"]
        else:
            itempool.remove("Complete Skeleton")
            itempool.remove("Fish")
            itempool.remove("DT Extractor")
            itempool.remove("Hush Puppy")
        if self.options.key_hunt:
            itempool += ["Key Piece"] * self.options.key_pieces.value
        else:
            itempool += ["Left Home Key"]
            itempool += ["Right Home Key"]
        if not self.options.rando_love or \
                (self.options.route_required != "genocide" and
                 self.options.route_required != "all_routes"):
            itempool = [item for item in itempool if not item == "LOVE"]
        if self.options.spare_sanity and self.options.route_required != "genocide":
            itempool += ["Ruins Spare"] * math.ceil(self.options.spare_sanity_max.value /
                                                    self.options.spare_sanity_pack_size.value)
            itempool += ["Snowdin Spare"] * math.ceil(self.options.spare_sanity_max.value /
                                                      self.options.spare_sanity_pack_size.value)
            itempool += ["Waterfall Spare"] * math.ceil(self.options.spare_sanity_max.value /
                                                        self.options.spare_sanity_pack_size.value)
            itempool += ["Hotland Spare"] * math.ceil(self.options.spare_sanity_max.value /
                                                      self.options.spare_sanity_pack_size.value)
        if not self.options.kill_sanity or \
                (self.options.route_required != "genocide" and
                 self.options.route_required != "all_routes"):
            self.multiworld.precollected_items[self.player] += [self.create_item("Ruins Population Pack")]
            self.multiworld.precollected_items[self.player] += [self.create_item("Snowdin Population Pack")]
            self.multiworld.precollected_items[self.player] += [self.create_item("Waterfall Population Pack")]
            self.multiworld.precollected_items[self.player] += [self.create_item("Hotland Population Pack")]
            exclusion_pool.update(exclusion_table["NoKills"])
        else:
            itempool += ["Ruins Population Pack"] * math.ceil(20/self.options.kill_sanity_pack_size.value)
            itempool += ["Snowdin Population Pack"] * math.ceil(16/self.options.kill_sanity_pack_size.value)
            itempool += ["Waterfall Population Pack"] * math.ceil(18/self.options.kill_sanity_pack_size.value)
            itempool += ["Hotland Population Pack"] * math.ceil(40/self.options.kill_sanity_pack_size.value)
        if self.options.ice_traps.value > 0:
            itempool += ["Ice Trap"] * self.options.ice_traps.value
        if not self.options.rando_stats or \
                (self.options.route_required != "genocide" and
                 self.options.route_required != "all_routes"):
            itempool = [item for item in itempool if not (item == "ATK Up" or item == "DEF Up" or item == "HP Up")]
        if self.options.temy_include:
            itempool += ["temy armor"]
        if self.options.no_equips:
            itempool = [item for item in itempool if item not in required_armor and item not in required_weapons]
        else:
            if self.options.prog_armor:
                itempool = [item if (item not in required_armor and not item == "temy armor") else
                            "Progressive Armor" for item in itempool]
            if self.options.prog_weapons:
                itempool = [item if item not in required_weapons else "Progressive Weapons" for item in itempool]
        if self.options.route_required == "genocide" or \
                self.options.route_required == "all_routes":
            if not self.options.only_flakes:
                itempool += ["Snowman Piece"] * 2
            if not self.options.no_equips:
                itempool = ["Real Knife" if item == "Worn Dagger" else "The Locket"
                            if item == "Heart Locket" else item for item in itempool]
        if self.options.only_flakes:
            itempool = [item for item in itempool if item not in non_key_items]

        if self.options.starting_area.current_key.title() == "All" or self.options.entrance_rando:
            all_keys = ["Ruins Key", "Snowdin Key", "Waterfall Key", "Hotland Key"]
            for item in all_keys:
                itempool.remove(item)
                self.multiworld.push_precollected(self.create_item(item))
        else:
            starting_key = self.options.starting_area.current_key.title() + " Key"
            itempool.remove(starting_key)
            self.multiworld.push_precollected(self.create_item(starting_key))
        # Choose locations to automatically exclude based on settings
        exclusion_pool.update(exclusion_table[self.options.route_required.current_key])
        if not self.options.rando_love or \
                (self.options.route_required != "genocide" and
                 self.options.route_required != "all_routes"):
            exclusion_pool.update(exclusion_table["NoLove"])
        if not self.options.rando_stats or \
                (self.options.route_required != "genocide" and
                 self.options.route_required != "all_routes"):
            exclusion_pool.update(exclusion_table["NoStats"])

        # Choose locations to automatically exclude based on settings
        exclusion_checks = set()
        exclusion_checks.update(["Nicecream Punch Card", "Hush Trade"])
        exclusion_rules(self.multiworld, self.player, exclusion_checks)

        # Convert itempool into real items
        itempool = [item for item in map(lambda itm_name: self.create_item(itm_name), itempool)]
        # Fill remaining items with randomly generated junk or Temmie Flakes
        while len(itempool) < len(self.multiworld.get_unfilled_locations(self.player)):
            itempool += [self.create_filler()]

        self.multiworld.itempool += itempool
    
    def set_rules(self) -> None:
        set_er_location_rules(self)

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        if self.options.entrance_rando:
            hint_data[self.player] = self.er_portal_hints

    def create_regions(self):
        self.undertale_portal_pairs = {}
        self.er_portal_hints = {}
        if self.options.entrance_rando:
            portal_pairs, portal_hints = create_er_regions(self)
            for portal1, portal2 in portal_pairs.items():
                self.undertale_portal_pairs[portal1.scene_destination()] = portal2.scene_destination()
            self.er_portal_hints = portal_hints
        else:
            portal_pairs = create_er_regions_vanilla(self)
            for portal1, portal2 in portal_pairs.items():
                self.undertale_portal_pairs[portal1.scene_destination()] = portal2.scene_destination()

    def fill_slot_data(self):
        slot_data = self._get_undertale_data()
        for option_name in self.options.as_dict():
            option = getattr(self.multiworld, option_name)[self.player]
            if (option_name == "rando_love" or option_name == "rando_stats" or option_name == "kill_sanity") and \
                    self.options.route_required != "genocide" and \
                    self.options.route_required != "all_routes":
                option.value = False
                slot_data[option_name] = int(option.value)
            elif (option_name == "spare_sanity") and \
                    self.options.route_required == "genocide":
                option.value = False
                slot_data[option_name] = int(option.value)
            elif (option_name == "kill_sanity_pack_size" and ((
                    self.options.route_required != "genocide" and
                    self.options.route_required != "all_routes") or not bool(self.options.kill_sanity.value))):
                option.value = 40
                slot_data[option_name] = int(option.value)
            elif slot_data.get(option_name, None) is None and type(option.value) in {str, int}:
                slot_data[option_name] = int(option.value)

        state = self.multiworld.get_all_state(False)
        state.update_reachable_regions(self.player)
        Utils.visualize_regions(self.multiworld.get_region("Menu", self.player), "undertale_check_player_" + 
                                str(self.multiworld.player_name[self.player])+".puml", show_entrance_names=True, 
                                highlight_regions=state.reachable_regions[self.player])
        return slot_data

    def create_item(self, name: str) -> Item:
        from .Items import item_table
        item_data = item_table[name]
        item = UndertaleItem(name, item_data.classification, item_data.code, self.player)
        return item
