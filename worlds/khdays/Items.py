import struct

from BaseClasses import ItemClassification, Item, IntFlag
import typing
from typing import Dict

progression = ItemClassification.progression
filler = ItemClassification.filler
useful = ItemClassification.useful
trap = ItemClassification.trap


class KHDaysItem(Item):
    game = 'Kingdom Hearts Days'


class ItemData(typing.NamedTuple):
    classification: ItemClassification
    khdaysamount: int
    khdaysaddress: int
    code: int = 0
    event: bool = False


item_table: Dict[str, ItemData] = {
    "Potion": ItemData(filler, 95, 0x194DCA),
    "Panel Slot": ItemData(useful, 105,0x194DC9),
    "Hi-Potion": ItemData(filler, 54,0x194DCB),
    "Mega-Potion": ItemData(filler, 15,0x194DCC),
    "Ether": ItemData(filler, 56,0x194DCD),
    "Hi-Ether": ItemData(filler, 30,0x194DCE),
    "Mega-Ether": ItemData(filler, 15,0x194DCF),
    "Elixir": ItemData(filler, 20, 0x194DD0),
    "Megalixir": ItemData(filler, 6, 0x194DD1),
    "Panacea": ItemData(filler, 31, 0x194DD2),
    "Limit Recharge": ItemData(useful, 10,0x194DD3),
    "Level Up": ItemData(progression, 39,0x194E07),
    "LV Doubler 5": ItemData(useful, 1, 0x194E08),
    "LV Doubler 6": ItemData(useful, 1, 0x194E09),
    "LV Doubler 6B": ItemData(useful, 1, 0x194F8D),
    "LV Doubler 6C": ItemData(useful, 1, 0x194F8E),
    "LV Doubler 6D": ItemData(useful, 1, 0x194F8F),
    "LV Tripler 4": ItemData(useful, 1, 0x194E0A),
    "LV Tripler 4B": ItemData(useful, 1, 0x194E0B),
    "LV Tripler 4C": ItemData(useful, 1, 0x194E0C),
    "LV Quadrupler 3": ItemData(useful, 1, 0x194E0D),
    "LV Quadrupler 3B": ItemData(useful, 1, 0x194E0E),
    "LV Quadrupler 3C": ItemData(useful, 1, 0x194E0F),
    "Backpack": ItemData(useful,  3, 0x194E23),
    "Pack Extender": ItemData(useful, 1, 0x194E24),
    "Fire": ItemData(progression, 24, 0x194E25),
    "Fira": ItemData(progression, 10, 0x194E26),
    "Firaga": ItemData(useful, 3, 0x194E27),
    "Blizzard": ItemData(progression,22, 0x194E28),
    "Blizzara": ItemData(progression,13,0x194E29),
    "Blizzaga": ItemData(useful,5,0x194E2A),
    "Thunder": ItemData(progression,23,0x194E2B),
    "Thundara": ItemData(progression,9,0x194E2C),
    "Thundaga": ItemData(useful,5,0x194E2D),
    "Aero": ItemData(progression,19,0x194E2E),
    "Aerora": ItemData(progression,9,0x194E2F),
    "Aeroga": ItemData(useful,4,0x194E30),
    "Cure": ItemData(progression,22,0x194E31),
    "Cura": ItemData(progression,12,0x194E32),
    "Curaga": ItemData(useful,5,0x194E33),
    "Magic LV2 4": ItemData(useful, 1, 0x194E34),
    "Magic LV2 4B": ItemData(useful, 1, 0x194E35),
    "Magic LV2 4C": ItemData(useful, 1, 0x194E36),
    "Magic LV3 4": ItemData(useful, 1, 0x194E37),
    "Magic LV3 4B": ItemData(useful, 1, 0x194E38),
    "Magic LV4 4": ItemData(useful, 1, 0x194E39),
    "Doublecast 4": ItemData(useful, 1, 0x194E3A),
    "Triplecast 3": ItemData(useful, 1, 0x194E3B),
    "Quadcast 3": ItemData(useful, 1, 0x194E3C),
    "Dodge Roll": ItemData(useful, 1, 0x194E3D),
    "Dodge Roll 3": ItemData(useful, 1, 0x194E3E),
    "Dodge Roll LV+": ItemData(useful,1,0x194E3F),
    "Dodge Rush": ItemData(useful, 1, 0x194E40),
    "Dodging Deflect": ItemData(useful, 1, 0x194F88),
    "Dodge Combo": ItemData(useful, 1, 0x194E41),
    "Auto-Dodge": ItemData(useful, 1, 0x194E42),
    "Block 2": ItemData(useful, 1, 0x194E43),
    "Block 4": ItemData(useful, 1, 0x194E44),
    "Block LV+": ItemData(useful,3,0x194E45),
    "Perfect Block": ItemData(useful, 1, 0x194E46),
    "Block-Counter": ItemData(useful, 1, 0x194E47),
    "Block-Retreat": ItemData(useful, 1, 0x194E48),
    "Sliding Block": ItemData(useful, 1, 0x194E49),
    "Block-Jump": ItemData(useful, 1, 0x194E4A),
    "Fire Block": ItemData(useful, 1, 0x194E4B),
    "Blizzard Block": ItemData(useful, 1, 0x194E4C),
    "Thunder Block": ItemData(useful, 1, 0x194E4D),
    "Aero Block": ItemData(useful, 1, 0x194E4E),
    "Block Bonus": ItemData(useful, 1, 0x194E4F),
    "Round Block": ItemData(useful, 1, 0x194E50),
    "Auto-Block": ItemData(useful, 1, 0x194E51),
    "Aerial Recovery": ItemData(useful, 1, 0x194E5C),
    "Aerial Recovery 3": ItemData(useful, 1, 0x194E5D),
    "A. Recovery LV+": ItemData(useful,2,0x194E5E),
    "Quick Recovery": ItemData(useful, 1, 0x194E5F),
    "Aerial Payback": ItemData(useful, 1, 0x194E60),
    "Smash Recovery": ItemData(useful, 1, 0x194E61),
    "Air Slide 2": ItemData(progression, 1, 0x194E58),
    "Air Slide 5": ItemData(progression, 1, 0x194E59),
    "Air Slide LV+": ItemData(progression,4,0x194E5A),
    "Air Rush": ItemData(useful, 1, 0x194E5B),
    "Sliding Dash": ItemData(progression, 1, 0x194E62),
    "Sliding Dash 3": ItemData(progression, 1, 0x194E63),
    "Sliding Dash LV+": ItemData(progression,2,0x194E64),
    "Glide 3": ItemData(progression, 1, 0x194E52),
    "Glide 5": ItemData(progression, 1, 0x194E53),
    "Glide LV+": ItemData(progression,4,0x194E54),
    "Homing Glide": ItemData(useful, 1, 0x194E56),
    "Rocket Glide": ItemData(useful, 1, 0x194E57),
    "Haste": ItemData(useful, 1, 0x194E65),
    "Haste 3": ItemData(useful, 1, 0x194E66),
    "Haste LV+": ItemData(useful,2,0x194E67),
    "High Jump": ItemData(progression, 1, 0x194E68),
    "High Jump 3": ItemData(progression, 1, 0x194E69),
    "High Jump LV+": ItemData(progression,2,0x194E6A),
    "Float": ItemData(useful, 1, 0x194E6B),
    "Treasure Magnet": ItemData(useful, 1, 0x194E7C),
    "Treasure Magnet 3": ItemData(useful, 1, 0x194E7D),
    "Treasure Magnet LV+": ItemData(useful,2,0x194E7E),
    "Auto-Life 3": ItemData(useful, 1, 0x194E6C),
    "Auto-Life LV+": ItemData(useful,2,0x194E6D),
    "Limit Boost": ItemData(useful, 1, 0x194E85),
    "Final Limit": ItemData(useful, 1, 0x194F89),
    "Scan": ItemData(useful, 1, 0x194E84),
    "Range Extender": ItemData(useful, 1, 0x194E83),
    "Auto-Lock": ItemData(useful, 1, 0x194E86),
    "Ultima Weapon": ItemData(useful, 1, 0x194F87),
    "Skill Gear": ItemData(useful, 1, 0x194E88),
    "Skill Gear+ 2": ItemData(useful, 1, 0x194E89),
    "Technical Gear 3": ItemData(useful, 1, 0x194E8F),
    "Technical Gear+ 3": ItemData(useful, 1, 0x194E90),
    "Duel Gear 4": ItemData(useful, 1, 0x194E9B),
    "Duel Gear+ 4": ItemData(useful, 1, 0x194E9A),
    "Duel Gear++ 5": ItemData(useful, 1, 0x194EA4),
    "Loaded Gear": ItemData(useful, 1, 0x194E8A),
    "Loaded Gear+ 2": ItemData(useful, 1, 0x194E8B),
    "Chrono Gear 3": ItemData(useful, 1, 0x194E91),
    "Chrono Gear+ 3": ItemData(useful, 1, 0x194E92),
    "Phantom Gear 4": ItemData(useful, 1, 0x194E9C),
    "Phantom Gear+ 4": ItemData(useful, 1, 0x194E9D),
    "Phantom Gear++ 5": ItemData(useful, 1, 0x194EA5),
    "Lift Gear 3": ItemData(useful, 1, 0x194E95),
    "Lift Gear+ 3": ItemData(useful, 1, 0x194E96),
    "Nimble Gear 4": ItemData(useful, 1, 0x194EA1),
    "Nimble Gear+ 4": ItemData(useful, 1, 0x194EA0),
    "Wild Gear 3": ItemData(useful, 1, 0x194E97),
    "Wild Gear+ 3": ItemData(useful, 1, 0x194E98),
    "Ominous Gear 4": ItemData(useful, 1, 0x194EA3),
    "Ominous Gear+ 4": ItemData(useful, 1, 0x194EA2),
    "Valor Gear 2": ItemData(useful, 1, 0x194E8C),
    "Valor Gear+ 2": ItemData(useful, 1, 0x194E8D),
    "Fearless Gear 3": ItemData(useful, 1, 0x194E93),
    "Fearless Gear+ 3": ItemData(useful, 1, 0x194E94),
    "Prestige Gear 4": ItemData(useful, 1, 0x194E9F),
    "Prestige Gear+ 4": ItemData(useful, 1, 0x194E9E),
    "Crisis Gear 5": ItemData(useful, 1, 0x194EA8),
    "Crisis Gear+ 5": ItemData(useful, 1, 0x194EA9),
    "Omega Gear 6": ItemData(useful, 1, 0x194EB2),
    "Omega Gear+ 6": ItemData(useful, 1, 0x194EB1),
    "Hazard Gear 5": ItemData(useful, 1, 0x194EA6),
    "Hazard Gear+ 5": ItemData(useful, 1, 0x194EA7),
    "Rage Gear 5": ItemData(useful, 1, 0x194EAD),
    "Rage Gear+ 5": ItemData(useful, 1, 0x194EAC),
    "Champion Gear 5": ItemData(useful, 1, 0x194EAA),
    "Champion Gear+ 5": ItemData(useful, 1, 0x194EAB),
    "Ultimate Gear 6": ItemData(useful, 1, 0x194EB4),
    "Ultimate Gear+ 6": ItemData(useful, 1, 0x194EB3),
    "Pandora's Gear 5": ItemData(useful, 1, 0x194EB0),
    "Pandora's Gear+ 5": ItemData(useful, 1, 0x194EAF),
    "Zero Gear 5": ItemData(useful, 1, 0x194EAE),
    "Casual Gear 2": ItemData(useful, 1, 0x194E8E),
    "Mystery Gear 3": ItemData(useful, 1, 0x194E99),
    "Ability Unit": ItemData(useful,3,0x194EB9),
    "Power Unit": ItemData(useful,5,0x194EBF),
    "Magic Unit": ItemData(useful,5,0x194EC1),
    "Guard Unit": ItemData(useful,5,0x194EC0),
    "Sight Unit": ItemData(useful,5,0x194EC2),
    "Sign of Resolve": ItemData(useful, 1, 0x194F92),
    "Brawl Ring": ItemData(useful, 1, 0x194F93),
    "Magic Ring": ItemData(useful, 1, 0x194F94),
    "Soldier Ring": ItemData(useful, 1, 0x194F95),
    "Fencer's Ring": ItemData(useful, 1, 0x194F96),
    "Fire Charm": ItemData(useful, 1, 0x194F97),
    "Flower Charm": ItemData(useful, 1, 0x194F98),
    "Strike Ring": ItemData(useful, 1, 0x194F99),
    "Lucky Ring": ItemData(progression, 1, 0x194F9A),
    "Blizzard Charm": ItemData(useful, 1, 0x194F9B),
    "White Ring": ItemData(useful, 1, 0x194F9C),
    "Knight's Defense": ItemData(useful, 1, 0x194F9D),
    "Raider's Ring": ItemData(useful, 1, 0x194F9E),
    "Thunder Charm": ItemData(useful, 1, 0x194F9F),
    "Recovery Ring": ItemData(useful, 1, 0x194FA0),
    "Vitality Ring": ItemData(useful, 1, 0x194FA1),
    "Rainforce Ring": ItemData(useful, 1, 0x194FA2),
    "Double Up": ItemData(useful, 1, 0x194FA3),
    "Storm's Eye": ItemData(useful, 1, 0x194FA4),
    "Critical Ring": ItemData(useful, 1, 0x194FA5),
    "Fairy Circle": ItemData(useful, 1, 0x194FA6),
    "Full Circle": ItemData(useful, 1, 0x194FA7),
    "Lucky Star": ItemData(useful, 1, 0x194FA8),
    "Charge Ring": ItemData(useful, 1, 0x194FA9),
    "Eternal Ring": ItemData(useful, 1, 0x194FAA),
    "Carmine Blight": ItemData(useful, 1, 0x194FAB),
    "Frozen Blight": ItemData(useful, 1, 0x194FAC),
    "Safety Ring": ItemData(useful, 1, 0x194FAD),
    "Princess's Crown": ItemData(useful, 1, 0x194FAE),
    "Lunar Strike": ItemData(useful, 1, 0x194FAF),
    "Crimson Blood": ItemData(useful, 1, 0x194FB0),
    "Deep Sky": ItemData(useful, 1, 0x194FB1),
    "Protect Ring": ItemData(useful, 1, 0x194FB2),
    "Might Crown": ItemData(useful, 1, 0x194FB3),
    "Critical Sun": ItemData(useful, 1, 0x194FB4),
    "Three Stars": ItemData(useful, 1, 0x194FB5),
    "Imperial Crown": ItemData(useful, 1, 0x194FB6),
    "Witch's Chaos": ItemData(useful, 1, 0x194FB7),
    "Rune Ring": ItemData(useful, 1, 0x194FB8),
    "Extreme": ItemData(useful, 1, 0x194FB9),
    "Master's Circle": ItemData(useful, 1, 0x194FBA),
    "Nothing to Fear": ItemData(useful, 1, 0x194FC7),
    "Space in Its Place": ItemData(useful, 1, 0x194FBB),
    "Flagging Winds": ItemData(useful, 1, 0x194FBC),
    "Ice Breaker": ItemData(useful, 1, 0x194FBD),
    "Down to Earth": ItemData(useful, 1, 0x194FBE),
    "Lose Your Illusion": ItemData(useful, 1, 0x194FBF),
    "Sighing of the Moon": ItemData(useful, 1, 0x194FC0),
    "Tears of Flame": ItemData(useful, 1, 0x194FC1),
    "Parting of Waters": ItemData(useful, 1, 0x194FC2),
    "Test of Time": ItemData(useful, 1, 0x194FC3),
    "Flowers Athirst": ItemData(useful, 1, 0x194FC4),
    "Stolen Thunder": ItemData(useful, 1, 0x194FC5),
    "Dying of the Light": ItemData(useful, 1, 0x194FC6),
}	

i = 0
for (name) in item_table:
    item_table[name] = ItemData(item_table[name].classification, item_table[name].khdaysamount, item_table[name].khdaysaddress, i+25000)
    i += 1

character_list = ["Roxas", "Axel", "Xigbar", "Saix", "Xaldin", "Sora", "Demyx", "Larxene", "Lexaeus", "Luxord", "Marluxia", "Riku", "Vexen", "Xemnas", "Xion", "Zexion", "Mickey", "Donald", "Goofy", "Dual-Wield_Roxas"]

i = 0
for name in character_list:
    item_table[name] = ItemData(useful, 1, 0, 25000-i-1)
    i += 1

days = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 22, 23, 24, 25, 26, 51, 52, 53, 54, 71, 72, 73, 74, 75, 76, 77, 78, 79,
        94, 95, 96, 97, 98, 99, 100, 117, 118,
        119, 120, 121, 122, 149, 150, 151, 152, 153, 154, 155, 156, 171, 172, 173, 174, 175, 176, 193, 194, 195, 196,
        197, 224, 225, 226, 227, 255, 256, 257, 258, 277, 278, 279, 280, 296, 297, 298, 299, 300, 301, 302, 303, 304,
        321, 322, 323, 324, 325, 326, 352, 353, 354, 355, 357, 358]
