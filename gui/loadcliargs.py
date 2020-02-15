from classes.SpriteSelector import SpriteSelector as spriteSelector
from gui.randomize.gameoptions import set_sprite
from Rom import Sprite


def loadcliargs(gui, args, settings=None):
    if args is not None:
        for k, v in vars(args).items():
            if type(v) is dict:
                setattr(args, k, v[1])  # only get values for player 1 for now
        # load values from commandline args

        # set up options to get
        # Page::Subpage::GUI-id::param-id
        options = {
          "randomizer": {
            "item": {
              "retro": "retro",
              "worldstate": "mode",
              "logiclevel": "logic",
              "goal": "goal",
              "crystals_gt": "crystals_gt",
              "crystals_ganon": "crystals_ganon",
              "weapons": "swords",
              "itempool": "difficulty",
              "itemfunction": "item_functionality",
              "timer": "timer",
              "progressives": "progressive",
              "accessibility": "accessibility",
              "sortingalgo": "algorithm"
            },
            "entrance": {
              "openpyramid": "openpyramid",
              "shuffleganon": "shuffleganon",
              "entranceshuffle": "shuffle"
            },
            "enemizer": {
              "potshuffle": "shufflepots",
              "enemyshuffle": "shuffleenemies",
              "bossshuffle": "shufflebosses",
              "enemydamage": "enemy_damage",
              "enemyhealth": "enemy_health"
            },
            "dungeon": {
              "mapshuffle": "mapshuffle",
              "compassshuffle": "compassshuffle",
              "smallkeyshuffle": "keyshuffle",
              "bigkeyshuffle": "bigkeyshuffle",
              "dungeondoorshuffle": "door_shuffle",
              "experimental": "experimental"
            },
            "gameoptions": {
              "hints": "hints",
              "nobgm": "disablemusic",
              "quickswap": "quickswap",
              "heartcolor": "heartcolor",
              "heartbeep": "heartbeep",
              "menuspeed": "fastmenu",
              "owpalettes": "ow_palettes",
              "uwpalettes": "uw_palettes"
            },
            "generation": {
              "spoiler": "create_spoiler",
              "suppressrom": "suppress_rom"
            } 
          }
        }
        for mainpage in options:
            for subpage in options[mainpage]:
                for widget in options[mainpage][subpage]:
                    arg = options[mainpage][subpage][widget]
                    gui.pages[mainpage].pages[subpage].widgets[widget].storageVar.set(getattr(args, arg))
                    if subpage == "gameoptions" and not widget == "hints":
                        hasSettings = settings is not None
                        hasWidget = ("adjust." + widget) in settings if hasSettings else None
                        if hasWidget is None:
                            gui.pages["adjust"].content.widgets[widget].storageVar.set(getattr(args, arg))

        gui.pages["randomizer"].pages["enemizer"].enemizerCLIpathVar.set(args.enemizercli)
        gui.pages["randomizer"].pages["generation"].romVar.set(args.rom)

        if args.multi:
            gui.pages["randomizer"].pages["multiworld"].widgets["worlds"].storageVar.set(str(args.multi))
        if args.seed:
            gui.frames["bottom"].seedVar.set(str(args.seed))
        if args.count:
            gui.frames["bottom"].widgets["generationcount"].storageVar.set(str(args.count))
        gui.outputPath.set(args.outputpath)

        def sprite_setter(spriteObject):
            gui.pages["randomizer"].pages["gameoptions"].widgets["sprite"]["spriteObject"] = spriteObject
        if args.sprite is not None:
            sprite_obj = args.sprite if isinstance(args.sprite, Sprite) else Sprite(args.sprite)
            r_sprite_flag = args.randomSprite if hasattr(args, 'randomSprite') else False
            set_sprite(sprite_obj, r_sprite_flag, spriteSetter=sprite_setter,
                       spriteNameVar=gui.pages["randomizer"].pages["gameoptions"].widgets["sprite"]["spriteNameVar"],
                       randomSpriteVar=gui.randomSprite)

        def sprite_setter_adj(spriteObject):
            gui.pages["adjust"].content.sprite = spriteObject
        if args.sprite is not None:
            sprite_obj = args.sprite if isinstance(args.sprite, Sprite) else Sprite(args.sprite)
            r_sprite_flag = args.randomSprite if hasattr(args, 'randomSprite') else False
            set_sprite(sprite_obj, r_sprite_flag, spriteSetter=sprite_setter_adj,
                       spriteNameVar=gui.pages["adjust"].content.spriteNameVar2,
                       randomSpriteVar=gui.randomSprite)

def loadadjustargs(gui, settings):
    options = {
        "adjust": {
            "content": {
                "nobgm": "adjust.nobgm",
                "quickswap": "adjust.quickswap",
                "heartcolor": "adjust.heartcolor",
                "heartbeep": "adjust.heartbeep",
                "menuspeed": "adjust.menuspeed",
                "owpalettes": "adjust.owpalettes",
                "uwpalettes": "adjust.uwpalettes"
            }
        }
    }
    for mainpage in options:
        for subpage in options[mainpage]:
            for widget in options[mainpage][subpage]:
                key = options[mainpage][subpage][widget]
                if key in settings:
                    gui.pages[mainpage].content.widgets[widget].storageVar.set(settings[key])
