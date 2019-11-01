
from BaseClasses import Door, DoorType, Direction, CrystalBarrier
from RoomData import PairedDoor

# constants
We = Direction.West
Ea = Direction.East
So = Direction.South
No = Direction.North
Up = Direction.Up
Dn = Direction.Down
# door offsets
Top = 0
Left = 0
Mid = 1
Bot = 2
Right = 2
# layer numbers
High = 0
Low = 1
# Quadrants - just been using this in my head - no reason to keep them labeled this way
A = 0
S = 1
Z = 2
X = 3
# Layer transitions
HTH = 0  # High to High 00
HTL = 1  # High to Low  01
LTH = 2  # Low to High  10
LTL = 3  # Low to Low   11
# Type Shortcuts
Nrml = DoorType.Normal
StrS = DoorType.StraightStairs
Hole = DoorType.Hole
Warp = DoorType.Warp
Sprl = DoorType.SpiralStairs
Lddr = DoorType.Ladder
Open = DoorType.Open
Lgcl = DoorType.Logical
Intr = DoorType.Interior


def create_doors(world, player):
    world.doors += [
        # hyrule castle
        create_door(player, 'Hyrule Castle Lobby W', Nrml).dir(We, 0x61, Mid, High).toggler().pos(0),
        create_door(player, 'Hyrule Castle Lobby E', Nrml).dir(Ea, 0x61, Mid, High).toggler().pos(2),
        create_door(player, 'Hyrule Castle Lobby WN', Nrml).dir(We, 0x61, Top, High).pos(1),
        create_door(player, 'Hyrule Castle Lobby North Stairs', StrS).dir(No, 0x61, Mid, High),
        create_door(player, 'Hyrule Castle West Lobby E', Nrml).dir(Ea, 0x60, Mid, Low).toggler().pos(1),
        create_door(player, 'Hyrule Castle West Lobby N', Nrml).dir(No, 0x60, Right, Low).pos(0),
        create_door(player, 'Hyrule Castle West Lobby EN', Nrml).dir(Ea, 0x60, Top, High).pos(3),
        create_door(player, 'Hyrule Castle East Lobby W', Nrml).dir(We, 0x62, Mid, Low).toggler().pos(0),
        create_door(player, 'Hyrule Castle East Lobby N', Nrml).dir(No, 0x62, Mid, High).pos(3),
        create_door(player, 'Hyrule Castle East Lobby NW', Nrml).dir(No, 0x62, Left, Low).pos(2),
        create_door(player, 'Hyrule Castle East Hall W', Nrml).dir(We, 0x52, Top, Low).pos(0),
        create_door(player, 'Hyrule Castle East Hall S', Nrml).dir(So, 0x52, Mid, High).pos(2),
        create_door(player, 'Hyrule Castle East Hall SW', Nrml).dir(So, 0x52, Left, Low).pos(1),
        create_door(player, 'Hyrule Castle West Hall E', Nrml).dir(Ea, 0x50, Top, Low).pos(0),
        create_door(player, 'Hyrule Castle West Hall S', Nrml).dir(So, 0x50, Right, Low).pos(1),
        create_door(player, 'Hyrule Castle Back Hall W', Nrml).dir(We, 0x01, Top, Low).pos(0),
        create_door(player, 'Hyrule Castle Back Hall E', Nrml).dir(Ea, 0x01, Top, Low).pos(1),
        create_door(player, 'Hyrule Castle Back Hall Down Stairs', Sprl).dir(Dn, 0x01, 0, HTL).ss(A, 0x2a, 0x00),
        create_door(player, 'Hyrule Castle Throne Room N', Nrml).dir(No, 0x51, Mid, High).pos(1),
        create_door(player, 'Hyrule Castle Throne Room South Stairs', StrS).dir(So, 0x51, Mid, Low),

        # hyrule dungeon level
        create_door(player, 'Hyrule Dungeon Map Room Up Stairs', Sprl).dir(Up, 0x72, 0, LTH).ss(A, 0x4b, 0xec),
        create_door(player, 'Hyrule Dungeon Map Room Key Door S', Intr).dir(So, 0x72, Mid, High).small_key().pos(0),
        create_door(player, 'Hyrule Dungeon North Abyss Key Door N', Intr).dir(No, 0x72, Mid, High).small_key().pos(0),
        create_door(player, 'Hyrule Dungeon North Abyss South Edge', Open).dir(So, 0x72, None, Low),
        create_door(player, 'Hyrule Dungeon North Abyss Catwalk Edge', Open).dir(So, 0x72, None, High),
        create_door(player, 'Hyrule Dungeon North Abyss Catwalk Dropdown', Lgcl),
        create_door(player, 'Hyrule Dungeon South Abyss North Edge', Open).dir(No, 0x82, None, Low),
        create_door(player, 'Hyrule Dungeon South Abyss West Edge', Open).dir(We, 0x82, None, Low),
        create_door(player, 'Hyrule Dungeon South Abyss Catwalk North Edge', Open).dir(No, 0x82, None, High),
        create_door(player, 'Hyrule Dungeon South Abyss Catwalk West Edge', Open).dir(We, 0x82, None, High),
        create_door(player, 'Hyrule Dungeon Guardroom Catwalk Edge', Open).dir(Ea, 0x81, None, High),
        create_door(player, 'Hyrule Dungeon Guardroom Abyss Edge', Open).dir(We, 0x81, None, High),
        create_door(player, 'Hyrule Dungeon Guardroom N', Nrml).dir(No, 0x81, Left, Low).pos(0),
        create_door(player, 'Hyrule Dungeon Armory S', Nrml).dir(So, 0x71, Left, Low).trap(0x2).pos(1),
        create_door(player, 'Hyrule Dungeon Armory ES', Intr).dir(Ea, 0x71, Left, Low).pos(2),
        create_door(player, 'Hyrule Dungeon Armory Boomerang WS', Intr).dir(We, 0x71, Left, Low).pos(2),
        create_door(player, 'Hyrule Dungeon Armory Interior Key Door N', Intr).dir(No, 0x71, Left, High).small_key().pos(0),
        create_door(player, 'Hyrule Dungeon Armory Interior Key Door S', Intr).dir(So, 0x71, Left, High).small_key().pos(0),
        create_door(player, 'Hyrule Dungeon Armory Down Stairs', Sprl).dir(Dn, 0x71, 0, HTL).ss(A, 0x11, 0xa8, True),
        create_door(player, 'Hyrule Dungeon Staircase Up Stairs', Sprl).dir(Up, 0x70, 2, LTH).ss(A, 0x32, 0x94, True),
        create_door(player, 'Hyrule Dungeon Staircase Down Stairs', Sprl).dir(Dn, 0x70, 1, HTH).ss(A, 0x11, 0x58),
        create_door(player, 'Hyrule Dungeon Cellblock Up Stairs', Sprl).dir(Up, 0x80, 0, HTH).ss(A, 0x1a, 0x44),

        # sewers
        create_door(player, 'Sewers Behind Tapestry S', Nrml).dir(So, 0x41, Mid, High).no_exit().trap(0x4).pos(0),
        create_door(player, 'Sewers Behind Tapestry Down Stairs', Sprl).dir(Dn, 0x41, 0, HTH).ss(S, 0x12, 0xb0),
        create_door(player, 'Sewers Rope Room Up Stairs', Sprl).dir(Up, 0x42, 0, HTH).ss(S, 0x1b, 0x9c),
        create_door(player, 'Sewers Rope Room North Stairs', StrS).dir(No, 0x42, Mid, High),
        create_door(player, 'Sewers Dark Cross South Stairs', StrS).dir(So, 0x32, Mid, High),
        create_door(player, 'Sewers Dark Cross Key Door N', Nrml).dir(No, 0x32, Mid, High).small_key().pos(0),
        create_door(player, 'Sewers Dark Cross Key Door S', Nrml).dir(So, 0x22, Mid, High).small_key().pos(0),
        create_door(player, 'Sewers Water W', Nrml).dir(We, 0x22, Bot, High).pos(1),
        create_door(player, 'Sewers Key Rat E', Nrml).dir(Ea, 0x21, Bot, High).pos(1),
        create_door(player, 'Sewers Key Rat Key Door N', Nrml).dir(No, 0x21, Right, High).small_key().pos(0),
        create_door(player, 'Sewers Secret Room Key Door S', Nrml).dir(So, 0x11, Right, High).small_key().pos(2),
        create_door(player, 'Sewers Rat Path WS', Intr).dir(We, 0x11, Bot, High).pos(1),
        create_door(player, 'Sewers Rat Path WN', Intr).dir(We, 0x11, Top, High).pos(0),
        create_door(player, 'Sewers Secret Room ES', Intr).dir(Ea, 0x11, Bot, High).pos(1),
        create_door(player, 'Sewers Secret Room EN', Intr).dir(Ea, 0x11, Top, High).pos(0),
        create_door(player, 'Sewers Secret Room Push Block', Lgcl),
        create_door(player, 'Sewers Secret Room Up Stairs', Sprl).dir(Up, 0x11, 0, LTH).ss(S, 0x33, 0x6c, True),
        create_door(player, 'Sewers Pull Switch Down Stairs', Sprl).dir(Dn, 0x02, 0, HTL).ss(S, 0x12, 0x80),
        create_door(player, 'Sewers Yet More Rats S', Intr).dir(So, 0x02, Mid, Low).pos(1),
        create_door(player, 'Sewers Pull Switch N', Intr).dir(No, 0x02, Mid, Low).pos(1),
        create_door(player, 'Sewers Pull Switch S', Nrml).dir(So, 0x02, Mid, Low).trap(0x4).toggler().pos(0),
        # logically one way the sanc, but should be linked - also toggle
        create_door(player, 'Sanctuary N', Nrml).dir(No, 0x12, Mid, High).no_exit().toggler().pos(0),

        # Eastern Palace
        create_door(player, 'Eastern Lobby N', Intr).dir(No, 0xc9, Mid, High).pos(0),
        create_door(player, 'Eastern Lobby Bridge S', Intr).dir(So, 0xc9, Mid, High).pos(0),
        create_door(player, 'Eastern Lobby NW', Intr).dir(No, 0xc9, Left, High).pos(2),
        create_door(player, 'Eastern Lobby Left Ledge SW', Intr).dir(So, 0xc9, Left, High).pos(2),
        create_door(player, 'Eastern Lobby NE', Intr).dir(No, 0xc9, Right, High).pos(3),
        create_door(player, 'Eastern Lobby Right Ledge SE', Intr).dir(So, 0xc9, Right, High).pos(3),
        create_door(player, 'Eastern Lobby Bridge N', Nrml).dir(No, 0xc9, Mid, High).pos(1),
        create_door(player, 'Eastern Cannonball S', Nrml).dir(So, 0xb9, Mid, High).pos(2),
        create_door(player, 'Eastern Cannonball N', Nrml).dir(No, 0xb9, Mid, High).pos(1),
        create_door(player, 'Eastern Cannonball Ledge WN', Nrml).dir(We, 0xb9, Top, High).pos(3),
        create_door(player, 'Eastern Cannonball Ledge Key Door EN', Nrml).dir(Ea, 0xb9, Top, High).small_key().pos(0),
        create_door(player, 'Eastern Courtyard Ledge S', Nrml).dir(So, 0xa9, Mid, High).pos(5),
        create_door(player, 'Eastern Courtyard Ledge W', Nrml).dir(We, 0xa9, Mid, High).trap(0x4).pos(0),
        create_door(player, 'Eastern Courtyard Ledge E', Nrml).dir(Ea, 0xa9, Mid, High).trap(0x2).pos(1),
        create_door(player, 'Eastern East Wing W', Nrml).dir(We, 0xaa, Mid, High).pos(4),
        create_door(player, 'Eastern East Wing EN', Intr).dir(Ea, 0xaa, Top, High).pos(2),
        create_door(player, 'Eastern Pot Switch WN', Intr).dir(We, 0xaa, Top, High).pos(2),
        create_door(player, 'Eastern East Wing ES', Intr).dir(Ea, 0xaa, Bot, High).pos(3),
        create_door(player, 'Eastern Map Balcony WS', Intr).dir(We, 0xaa, Bot, High).pos(3),
        create_door(player, 'Eastern Pot Switch SE', Intr).dir(So, 0xaa, Right, High).pos(0),
        create_door(player, 'Eastern Map Room NE', Intr).dir(No, 0xaa, Right, High).pos(0),
        create_door(player, 'Eastern Map Balcony Hook Path', Lgcl),
        create_door(player, 'Eastern Map Room Drop Down', Lgcl),
        create_door(player, 'Eastern West Wing E', Nrml).dir(Ea, 0xa8, Mid, High).pos(5),
        create_door(player, 'Eastern West Wing WS', Intr).dir(We, 0xa8, Bot, High).pos(0),
        create_door(player, 'Eastern Stalfos Spawn ES', Intr).dir(Ea, 0xa8, Bot, High).pos(0),
        create_door(player, 'Eastern Stalfos Spawn NW', Intr).dir(No, 0xa8, Left, High).pos(1),
        create_door(player, 'Eastern Compass Room SW', Intr).dir(So, 0xa8, Left, High).pos(1),
        create_door(player, 'Eastern Compass Room EN', Intr).dir(Ea, 0xa8, Top, High).pos(3),
        create_door(player, 'Eastern Hint Tile WN', Intr).dir(We, 0xa8, Top, High).pos(3),
        create_door(player, 'Eastern Hint Tile EN', Nrml).dir(Ea, 0xa8, Top, Low).pos(4),
        create_door(player, 'Eastern Hint Tile Blocked Path SE', Nrml).dir(So, 0xa8, Right, High).small_key().pos(2),
        create_door(player, 'Eastern Hint Tile Push Block', Lgcl),
        create_door(player, 'Eastern Courtyard WN', Nrml).dir(We, 0xa9, Top, Low).pos(3),
        create_door(player, 'Eastern Courtyard EN', Nrml).dir(Ea, 0xa9, Top, Low).pos(4),
        create_door(player, 'Eastern Courtyard N', Nrml).dir(No, 0xa9, Mid, High).big_key().pos(2),
        create_door(player, 'Eastern Courtyard Potholes', Hole),
        create_door(player, 'Eastern Fairies\' Warp', Warp),
        create_door(player, 'Eastern Map Valley WN', Nrml).dir(We, 0xaa, Top, Low).pos(1),
        create_door(player, 'Eastern Map Valley SW', Nrml).dir(So, 0xaa, Left, High).pos(5),
        create_door(player, 'Eastern Dark Square NW', Nrml).dir(No, 0xba, Left, High).trap(0x2).pos(1),
        create_door(player, 'Eastern Dark Square Key Door WN', Nrml).dir(We, 0xba, Top, High).small_key().pos(0),
        create_door(player, 'Eastern Dark Square EN', Intr).dir(Ea, 0xba, Top, High).pos(2),
        create_door(player, 'Eastern Dark Pots WN', Intr).dir(We, 0xba, Top, High).pos(2),
        create_door(player, 'Eastern Big Key EN', Nrml).dir(Ea, 0xb8, Top, High).pos(1),
        create_door(player, 'Eastern Big Key NE', Nrml).dir(No, 0xb8, Right, High).big_key().pos(0),
        create_door(player, 'Eastern Darkness S', Nrml).dir(So, 0x99, Mid, High).small_key().pos(1),
        create_door(player, 'Eastern Darkness NE', Intr).dir(No, 0x99, Right, High).pos(2),
        create_door(player, 'Eastern Rupees SE', Intr).dir(So, 0x99, Right, High).pos(2),
        # Up is a keydoor and down is not. Only the up stairs should be considered a key door for now.
        create_door(player, 'Eastern Darkness Up Stairs', Sprl).dir(Up, 0x99, 0, HTH).ss(Z, 0x1a, 0x6c, False, True).small_key().pos(0),
        create_door(player, 'Eastern Attic Start Down Stairs', Sprl).dir(Dn, 0xda, 0, HTH).ss(Z, 0x11, 0x80, True, True),
        create_door(player, 'Eastern Attic Start WS', Nrml).dir(We, 0xda, Bot, High).trap(0x4).pos(0),
        create_door(player, 'Eastern False Switches ES', Nrml).dir(Ea, 0xd9, Bot, High).trap(0x1).pos(2),
        create_door(player, 'Eastern False Switches WS', Intr).dir(We, 0xd9, Bot, High).pos(1),
        create_door(player, 'Eastern Cannonball Hell ES', Intr).dir(Ea, 0xd9, Bot, High).pos(1),
        create_door(player, 'Eastern Cannonball Hell WS', Nrml).dir(We, 0xd9, Bot, High).trap(0x4).pos(0),
        create_door(player, 'Eastern Single Eyegore ES', Nrml).dir(Ea, 0xd8, Bot, High).pos(2),
        create_door(player, 'Eastern Single Eyegore NE', Intr).dir(No, 0xd8, Right, High).pos(1),
        create_door(player, 'Eastern Duo Eyegores SE', Intr).dir(So, 0xd8, Right, High).pos(1),
        create_door(player, 'Eastern Duo Eyegores NE', Nrml).dir(No, 0xd8, Right, High).trap(0x4).pos(0),
        create_door(player, 'Eastern Boss SE', Nrml).dir(So, 0xc8, Right, High).no_exit().trap(0x4).pos(0),

        # Desert Palace
        create_door(player, 'Desert Main Lobby NW Edge', Open).dir(No, 0x84, None, High),
        create_door(player, 'Desert Main Lobby N Edge', Open).dir(No, 0x84, None, High),
        create_door(player, 'Desert Main Lobby NE Edge', Open).dir(No, 0x84, None, High),
        create_door(player, 'Desert Main Lobby E Edge', Open).dir(Ea, 0x84, None, High),
        create_door(player, 'Desert Dead End Edge', Open).dir(So, 0x74, None, High),
        create_door(player, 'Desert East Wing W Edge', Open).dir(We, 0x85, None, High),
        create_door(player, 'Desert East Wing N Edge', Open).dir(No, 0x85, None, High),
        create_door(player, 'Desert East Lobby WS', Intr).dir(We, 0x85, Bot, High).pos(3),
        create_door(player, 'Desert East Wing ES', Intr).dir(Ea, 0x85, Bot, High).pos(3),
        create_door(player, 'Desert East Wing Key Door EN', Intr).dir(Ea, 0x85, Top, High).small_key().pos(1),
        create_door(player, 'Desert Compass Key Door WN', Intr).dir(We, 0x85, Top, High).small_key().pos(1),
        create_door(player, 'Desert Compass NW', Nrml).dir(No, 0x85, Right, High).trap(0x4).pos(0),
        create_door(player, 'Desert Cannonball S', Nrml).dir(So, 0x75, Right, High).pos(1),
        create_door(player, 'Desert Arrow Pot Corner S Edge', Open).dir(So, 0x75, None, High),
        create_door(player, 'Desert Arrow Pot Corner W Edge', Open).dir(We, 0x75, None, High),
        create_door(player, 'Desert North Hall SE Edge', Open).dir(So, 0x74, None, High),
        create_door(player, 'Desert North Hall SW Edge', Open).dir(So, 0x74, None, High),
        create_door(player, 'Desert North Hall W Edge', Open).dir(We, 0x74, None, High),
        create_door(player, 'Desert North Hall E Edge', Open).dir(Ea, 0x74, None, High),
        create_door(player, 'Desert North Hall NW', Intr).dir(No, 0x74, Left, High).pos(1),
        create_door(player, 'Desert Map SW', Intr).dir(So, 0x74, Left, High).pos(1),
        create_door(player, 'Desert North Hall NE', Intr).dir(No, 0x74, Right, High).pos(0),
        create_door(player, 'Desert Map SE', Intr).dir(So, 0x74, Right, High).pos(0),
        create_door(player, 'Desert Sandworm Corner S Edge', Open).dir(So, 0x73, None, High),
        create_door(player, 'Desert Sandworm Corner E Edge', Open).dir(Ea, 0x73, None, High),
        create_door(player, 'Desert Sandworm Corner NE', Intr).dir(No, 0x73, Right, High).pos(2),
        create_door(player, 'Desert Bonk Torch SE', Intr).dir(So, 0x73, Right, High).pos(2),
        create_door(player, 'Desert Sandworm Corner WS', Intr).dir(We, 0x73, Bot, High).pos(1),
        # I don't know if I have to mark trap on interior doors yet - haven't mucked them up much
        create_door(player, 'Desert Circle of Pots ES', Intr).dir(Ea, 0x73, Bot, High).pos(1),
        create_door(player, 'Desert Circle of Pots NW', Intr).dir(No, 0x73, Left, High).pos(0),
        create_door(player, 'Desert Big Chest SW', Intr).dir(So, 0x73, Left, High).pos(0),
        create_door(player, 'Desert West Wing N Edge', Open).dir(No, 0x83, None, High),
        create_door(player, 'Desert West Wing WS', Intr).dir(We, 0x83, Bot, High).pos(2),
        create_door(player, 'Desert West Lobby ES', Intr).dir(Ea, 0x83, Bot, High).pos(2),
        # Desert Back
        create_door(player, 'Desert Back Lobby NW', Intr).dir(No, 0x63, Left, High).pos(1),
        create_door(player, 'Desert Tiles 1 SW', Intr).dir(So, 0x63, Left, High).pos(1),
        create_door(player, 'Desert Tiles 1 Up Stairs', Sprl).dir(Up, 0x63, 0, HTH).ss(A, 0x1b, 0x6c, True).small_key().pos(0),
        create_door(player, 'Desert Bridge Down Stairs', Sprl).dir(Dn, 0x53, 0, HTH).ss(A, 0x0f, 0x80, True),
        create_door(player, 'Desert Bridge SW', Intr).dir(So, 0x53, Left, High).pos(0),
        create_door(player, 'Desert Four Statues NW', Intr).dir(No, 0x53, Left, High).pos(0),
        create_door(player, 'Desert Four Statues ES', Intr).dir(Ea, 0x53, Bot, High).pos(1),
        create_door(player, 'Desert Beamos Hall WS', Intr).dir(We, 0x53, Bot, High).pos(1),
        create_door(player, 'Desert Beamos Hall NE', Nrml).dir(No, 0x53, Right, High).small_key().pos(2),
        create_door(player, 'Desert Tiles 2 SE', Nrml).dir(So, 0x43, Right, High).small_key().pos(2),
        create_door(player, 'Desert Tiles 2 NE', Intr).dir(No, 0x43, Right, High).small_key().pos(1),
        create_door(player, 'Desert Wall Slide SE', Intr).dir(So, 0x43, Right, High).small_key().pos(1),
        create_door(player, 'Desert Wall Slide NW', Nrml).dir(No, 0x43, Left, High).big_key().pos(0).no_entrance(),
        create_door(player, 'Desert Boss SW', Nrml).dir(So, 0x33, Left, High).no_exit().trap(0x4).pos(0),

        # Hera
        create_door(player, 'Hera Lobby Down Stairs', Sprl).dir(Dn, 0x77, 3, HTL).ss(Z, 0x21, 0x90, False, True),
        create_door(player, 'Hera Lobby Key Stairs', Sprl).dir(Dn, 0x77, 1, HTL).ss(A, 0x12, 0x80).small_key().pos(0),
        create_door(player, 'Hera Lobby Up Stairs', Sprl).dir(Up, 0x77, 2, HTL).ss(X, 0x2b, 0x5c, False, True),
        create_door(player, 'Hera Basement Cage Up Stairs', Sprl).dir(Up, 0x87, 3, LTH).ss(Z, 0x42, 0x7c, True, True),
        create_door(player, 'Hera Tile Room Up Stairs', Sprl).dir(Up, 0x87, 1, LTH).ss(A, 0x32, 0x6c, True, True),
        create_door(player, 'Hera Tile Room EN', Intr).dir(Ea, 0x87, Top, High).pos(0),
        create_door(player, 'Hera Tridorm WN', Intr).dir(We, 0x87, Top, High).pos(0),
        create_door(player, 'Hera Tridorm SE', Intr).dir(So, 0x87, Right, High).pos(1),
        create_door(player, 'Hera Torches NE', Intr).dir(No, 0x87, Right, High).pos(1),
        create_door(player, 'Hera Beetles Down Stairs', Sprl).dir(Dn, 0x31, 2, LTH).ss(X, 0x3a, 0x70, True, True),
        create_door(player, 'Hera Beetles WS', Intr).dir(We, 0x31, Bot, High).pos(1),
        create_door(player, 'Hera Beetles Holes', Hole),
        create_door(player, 'Hera Startile Corner ES', Intr).dir(Ea, 0x31, Bot, High).pos(1),
        create_door(player, 'Hera Startile Corner NW', Intr).dir(No, 0x31, Left, High).big_key().pos(0),
        create_door(player, 'Hera Startile Corner Holes', Hole),
        # technically ugly but causes lots of failures in basic
        create_door(player, 'Hera Startile Wide SW', Intr).dir(So, 0x31, Left, High).pos(0),
        create_door(player, 'Hera Startile Wide Up Stairs', Sprl).dir(Up, 0x31, 0, HTH).ss(S, 0x6b, 0xac, False, True),
        create_door(player, 'Hera Startile Wide Holes', Hole),
        create_door(player, 'Hera 4F Down Stairs', Sprl).dir(Dn, 0x27, 0, HTH).ss(S, 0x62, 0xc0),
        create_door(player, 'Hera 4F Up Stairs', Sprl).dir(Up, 0x27, 1, HTH).ss(A, 0x6b, 0x2c),
        create_door(player, 'Hera 4F Holes', Hole),
        create_door(player, 'Hera Big Chest Landing Exit', Lgcl),
        create_door(player, 'Hera Big Chest Landing Holes', Hole),
        create_door(player, 'Hera 5F Down Stairs', Sprl).dir(Dn, 0x17, 1, HTH).ss(A, 0x62, 0x40),
        create_door(player, 'Hera 5F Up Stairs', Sprl).dir(Up, 0x17, 0, HTH).ss(S, 0x6a, 0x9c),
        create_door(player, 'Hera 5F Star Hole', Hole),
        create_door(player, 'Hera 5F Pothole Chain', Hole),
        create_door(player, 'Hera 5F Normal Holes', Hole),
        create_door(player, 'Hera Fairies\' Warp', Warp),
        create_door(player, 'Hera Boss Down Stairs', Sprl).dir(Dn, 0x07, 0, HTH).ss(S, 0x61, 0xb0),
        create_door(player, 'Hera Boss Outer Hole', Hole),
        create_door(player, 'Hera Boss Inner Hole', Hole),

        # Castle Tower
        create_door(player, 'Tower Lobby NW', Intr).dir(No, 0xe0, Left, High).pos(1),
        create_door(player, 'Tower Gold Knights SW', Intr).dir(So, 0xe0, Left, High).pos(1),
        create_door(player, 'Tower Gold Knights EN', Intr).dir(Ea, 0xe0, Top, High).pos(0),
        create_door(player, 'Tower Room 03 WN', Intr).dir(We, 0xe0, Bot, High).pos(0),
        create_door(player, 'Tower Room 03 Up Stairs', Sprl).dir(Up, 0xe0, 0, HTH).ss(S, 0x1a, 0x6c, True, True).small_key().pos(2),
        create_door(player, 'Tower Lone Statue Down Stairs', Sprl).dir(Dn, 0xd0, 0, HTH).ss(S, 0x11, 0x80, True, True),
        create_door(player, 'Tower Lone Statue WN', Intr).dir(We, 0xd0, Top, High).pos(1),
        create_door(player, 'Tower Dark Maze EN', Intr).dir(Ea, 0xd0, Top, High).pos(1),
        create_door(player, 'Tower Dark Maze ES', Intr).dir(Ea, 0xd0, Bot, High).small_key().pos(0),
        create_door(player, 'Tower Dark Chargers WS', Intr).dir(We, 0xd0, Bot, High).small_key().pos(0),
        create_door(player, 'Tower Dark Chargers Up Stairs', Sprl).dir(Up, 0xd0, 2, HTH).ss(X, 0x1b, 0x8c, True, True),
        create_door(player, 'Tower Dual Statues Down Stairs', Sprl).dir(Dn, 0xc0, 2, HTH).ss(X, 0x12, 0xa0, True, True),
        create_door(player, 'Tower Dual Statues WS', Intr).dir(We, 0xc0, Bot, High).pos(1),
        create_door(player, 'Tower Dark Pits ES', Intr).dir(Ea, 0xc0, Bot, High).pos(1),
        create_door(player, 'Tower Dark Pits EN', Intr).dir(Ea, 0xc0, Top, High).pos(0),
        create_door(player, 'Tower Dark Archers WN', Intr).dir(We, 0xc0, Top, High).pos(0),
        create_door(player, 'Tower Dark Archers Up Stairs', Sprl).dir(Up, 0xc0, 0, HTH).ss(S, 0x1b, 0x6c, True, True).small_key().pos(2),
        create_door(player, 'Tower Red Spears Down Stairs', Sprl).dir(Dn, 0xb0, 0, HTH).ss(S, 0x12, 0x80, True, True),
        create_door(player, 'Tower Red Spears WN', Intr).dir(We, 0xb0, Top, High).pos(1),
        create_door(player, 'Tower Red Guards EN', Intr).dir(Ea, 0xb0, Top, High).pos(1),
        create_door(player, 'Tower Red Guards SW', Intr).dir(So, 0xb0, Left, High).pos(0),
        create_door(player, 'Tower Circle of Pots NW', Intr).dir(No, 0xb0, Left, High).pos(0),
        create_door(player, 'Tower Circle of Pots WS', Intr).dir(We, 0xb0, Bot, High).small_key().pos(2),
        create_door(player, 'Tower Pacifist Run ES', Intr).dir(Ea, 0xb0, Bot, High).small_key().pos(2),
        create_door(player, 'Tower Pacifist Run Up Stairs', Sprl).dir(Up, 0xb0, 2, LTH).ss(X, 0x33, 0x8c, True, True),
        create_door(player, 'Tower Push Statue Down Stairs', Sprl).dir(Dn, 0x40, 0, HTL).ss(X, 0x12, 0xa0, True, True),
        create_door(player, 'Tower Push Statue WS', Intr).dir(We, 0x40, Bot, Low).pos(0),
        create_door(player, 'Tower Catwalk ES', Intr).dir(Ea, 0x40, Bot, Low).pos(0),
        create_door(player, 'Tower Catwalk North Stairs', StrS).dir(No, 0x40, Left, High),
        create_door(player, 'Tower Antechamber South Stairs', StrS).dir(So, 0x30, Left, High),
        create_door(player, 'Tower Antechamber NW', Intr).dir(No, 0x30, Left, High).pos(1),
        create_door(player, 'Tower Altar SW', Intr).dir(So, 0x30, Left, High).pos(1),
        create_door(player, 'Tower Altar NW', Nrml).dir(No, 0x30, Left, High).pos(0),
        create_door(player, 'Tower Agahnim 1 SW', Nrml).dir(So, 0x20, Left, High).no_exit().trap(0x4).pos(0),

        # Palace of Darkness
        create_door(player, 'PoD Lobby N', Intr).dir(No, 0x4a, Mid, High).pos(2),
        create_door(player, 'PoD Lobby NW', Intr).dir(No, 0x4a, Left, High).pos(0),
        create_door(player, 'PoD Lobby NE', Intr).dir(No, 0x4a, Right, High).pos(1),
        create_door(player, 'PoD Left Cage SW', Intr).dir(No, 0x4a, Left, High).pos(0),
        create_door(player, 'PoD Middle Cage S', Intr).dir(No, 0x4a, Mid, High).pos(2),
        create_door(player, 'PoD Middle Cage SE', Intr).dir(No, 0x4a, Right, High).pos(1),
        create_door(player, 'PoD Left Cage Down Stairs', Sprl).dir(Dn, 0x4a, 1, HTH).ss(A, 0x12, 0x80, False, True),
        create_door(player, 'PoD Middle Cage Down Stairs', Sprl).dir(Dn, 0x4a, 0, HTH).ss(S, 0x12, 0x80, False, True),
        create_door(player, 'PoD Middle Cage N', Nrml).dir(No, 0x4a, Mid, High).small_key().pos(2),
        create_door(player, 'PoD Shooter Room Up Stairs', Sprl).dir(Up, 0x09, 1, HTH).ss(A, 0x1b, 0x6c, True, True),
        create_door(player, 'PoD Warp Room Up Stairs', Sprl).dir(Up, 0x09, 0, HTH).ss(S, 0x1a, 0x6c, True, True),
        create_door(player, 'PoD Warp Room Warp', Warp),
        create_door(player, 'PoD Pit Room S', Nrml).dir(So, 0x3a, Mid, High).small_key().pos(0),
        create_door(player, 'PoD Pit Room NW', Nrml).dir(No, 0x3a, Left, High).pos(1),
        create_door(player, 'PoD Pit Room NE', Nrml).dir(No, 0x3a, Right, High).pos(2),
        create_door(player, 'PoD Pit Room Freefall', Hole),
        create_door(player, 'PoD Pit Room Bomb Hole', Hole),
        create_door(player, 'PoD Big Key Landing Hole', Hole),
        create_door(player, 'PoD Big Key Landing Down Stairs', Sprl).dir(Dn, 0x3a, 0, HTH).ss(A, 0x11, 0x00),
        create_door(player, 'PoD Basement Ledge Up Stairs', Sprl).dir(Up, 0x0a, 0, HTH).ss(A, 0x1a, 0xec).small_key().pos(0),
        create_door(player, 'PoD Basement Ledge Drop Down', Lgcl),
        create_door(player, 'PoD Stalfos Basement Warp', Warp),
        create_door(player, 'PoD Arena Main SW', Nrml).dir(So, 0x2a, Left, High).pos(4),
        create_door(player, 'PoD Arena Bridge SE', Nrml).dir(So, 0x2a, Right, High).pos(5),
        create_door(player, 'PoD Arena Main NW', Nrml).dir(No, 0x2a, Left, High).small_key().pos(1),
        create_door(player, 'PoD Arena Main NE', Nrml).dir(No, 0x2a, Right, High).no_exit().trap(0x4).pos(0),
        create_door(player, 'PoD Arena Main Crystal Path', Lgcl),
        create_door(player, 'PoD Arena Main Orange Barrier', Lgcl),
        create_door(player, 'PoD Arena North Drop Down', Lgcl),
        create_door(player, 'PoD Arena Crystals E', Nrml).dir(Ea, 0x2a, Mid, High).pos(3),
        create_door(player, 'PoD Arena Crystal Path', Lgcl),
        create_door(player, 'PoD Arena Bridge Drop Down', Lgcl),
        create_door(player, 'PoD Arena Ledge ES', Nrml).dir(Ea, 0x2a, Bot, High).pos(2),
        create_door(player, 'PoD Sexy Statue W', Nrml).dir(We, 0x2b, Mid, High).pos(3),
        create_door(player, 'PoD Sexy Statue NW', Nrml).dir(No, 0x2b, Left, High).trap(0x1).pos(2),
        create_door(player, 'PoD Map Balcony Drop Down', Lgcl),
        create_door(player, 'PoD Map Balcony WS', Nrml).dir(We, 0x2b, Bot, High).pos(1),
        create_door(player, 'PoD Map Balcony South Stairs', StrS).dir(So, 0x2b, Left, High),
        create_door(player, 'PoD Conveyor North Stairs', StrS).dir(No, 0x3b, Left, High),
        create_door(player, 'PoD Conveyor SW', Nrml).dir(So, 0x3b, Left, High).pos(0),
        create_door(player, 'PoD Mimics 1 NW', Nrml).dir(No, 0x4b, Left, High).trap(0x4).pos(0),
        create_door(player, 'PoD Mimics 1 SW', Intr).dir(So, 0x4b, Left, High).pos(1),
        create_door(player, 'PoD Jelly Hall NW', Intr).dir(No, 0x4b, Left, High).pos(1),
        create_door(player, 'PoD Jelly Hall NE', Intr).dir(No, 0x4b, Right, High).pos(2),
        create_door(player, 'PoD Warp Hint SE', Intr).dir(So, 0x4b, Right, High).pos(2),
        create_door(player, 'PoD Warp Hint Warp', Warp),
        create_door(player, 'PoD Falling Bridge SW', Nrml).dir(So, 0x1a, Left, High).small_key().pos(3),
        create_door(player, 'PoD Falling Bridge WN', Nrml).dir(We, 0x1a, Top, High).small_key().pos(1),
        create_door(player, 'PoD Falling Bridge EN', Intr).dir(Ea, 0x1a, Top, High).pos(4),
        create_door(player, 'PoD Big Chest Balcony W', Nrml).dir(We, 0x1a, Mid, High).pos(2),
        create_door(player, 'PoD Dark Maze EN', Nrml).dir(Ea, 0x19, Top, High).small_key().pos(1),
        create_door(player, 'PoD Dark Maze E', Nrml).dir(Ea, 0x19, Mid, High).pos(0),
        create_door(player, 'PoD Compass Room WN', Intr).dir(We, 0x1a, Top, High).pos(4),
        create_door(player, 'PoD Compass Room SE', Intr).dir(No, 0x1a, Mid, High).small_key().pos(0),
        create_door(player, 'PoD Harmless Hellway NE', Intr).dir(No, 0x1a, Right, High).small_key().pos(0),
        create_door(player, 'PoD Harmless Hellway SE', Nrml).dir(So, 0x1a, Right, High).pos(5),
        create_door(player, 'PoD Compass Room W Down Stairs', Sprl).dir(Dn, 0x1a, 0, HTH).ss(S, 0x12, 0x50, True, True),
        create_door(player, 'PoD Compass Room E Down Stairs', Sprl).dir(Dn, 0x1a, 1, HTH).ss(S, 0x11, 0xb0, True, True),
        create_door(player, 'PoD Dark Basement W Up Stairs', Sprl).dir(Up, 0x6a, 0, HTH).ss(S, 0x1b, 0x3c, True),
        create_door(player, 'PoD Dark Basement E Up Stairs', Sprl).dir(Up, 0x6a, 1, HTH).ss(S, 0x1b, 0x9c, True),
        create_door(player, 'PoD Dark Alley NE', Nrml).dir(No, 0x6a, Right, High).big_key().pos(0),
        create_door(player, 'PoD Mimics 2 SW', Nrml).dir(So, 0x1b, Left, High).pos(1),
        create_door(player, 'PoD Mimics 2 NW', Intr).dir(No, 0x1b, Left, High).pos(0),
        create_door(player, 'PoD Bow Statue SW', Intr).dir(So, 0x1b, Left, High).pos(0),
        create_door(player, 'PoD Bow Statue Down Ladder', Lddr).no_entrance(),
        create_door(player, 'PoD Dark Pegs Up Ladder', Lddr),
        create_door(player, 'PoD Dark Pegs WN', Intr).dir(We, 0x0b, Mid, High).small_key().pos(2),
        create_door(player, 'PoD Lonely Turtle SW', Intr).dir(So, 0x0b, Mid, High).pos(0),
        create_door(player, 'PoD Lonely Turtle EN', Intr).dir(Ea, 0x0b, Mid, High).small_key().pos(2),
        create_door(player, 'PoD Turtle Party ES', Intr).dir(Ea, 0x0b, Mid, High).pos(1),
        create_door(player, 'PoD Turtle Party NW', Intr).dir(No, 0x0b, Mid, High).pos(0),
        create_door(player, 'PoD Callback WS', Intr).dir(We, 0x0b, Mid, High).pos(1),
        create_door(player, 'PoD Callback Warp', Warp),
        create_door(player, 'PoD Boss SE', Nrml).dir(So, 0x5a, Right, High).no_exit().trap(0x4).pos(0),

        create_door(player, 'Swamp Lobby Moat', Lgcl),
        create_door(player, 'Swamp Entrance Down Stairs', Sprl).dir(Dn, 0x28, 0, HTH).ss(A, 0x11, 0x80).small_key().pos(0),
        create_door(player, 'Swamp Entrance Moat', Lgcl),
        create_door(player, 'Swamp Pot Row Up Stairs', Sprl).dir(Up, 0x38, 0, HTH).ss(A, 0x1a, 0x6c, True),
        create_door(player, 'Swamp Pot Row WN', Nrml).dir(We, 0x38, Top, High).pos(0),
        create_door(player, 'Swamp Pot Row WS', Nrml).dir(We, 0x38, Bot, High).small_key().pos(1),
        create_door(player, 'Swamp Map Ledge EN', Nrml).dir(Ea, 0x37, Top, High).pos(1),
        create_door(player, 'Swamp Trench 1 Approach ES', Nrml).dir(Ea, 0x37, Bot, High).small_key().pos(3),
        create_door(player, 'Swamp Trench 1 Approach Dry', Lgcl),
        create_door(player, 'Swamp Trench 1 Approach Key', Lgcl),
        create_door(player, 'Swamp Trench 1 Approach Swim Depart', Lgcl),
        create_door(player, 'Swamp Trench 1 Nexus Approach', Lgcl),
        create_door(player, 'Swamp Trench 1 Nexus Key', Lgcl),
        create_door(player, 'Swamp Trench 1 Nexus N', Intr).dir(No, 0x37, Mid, Low).pos(5),
        create_door(player, 'Swamp Trench 1 Alcove S', Intr).dir(So, 0x37, Mid, Low).pos(5),
        create_door(player, 'Swamp Trench 1 Key Ledge Dry', Lgcl),
        create_door(player, 'Swamp Trench 1 Key Approach', Lgcl),
        create_door(player, 'Swamp Trench 1 Key Ledge Depart', Lgcl),
        create_door(player, 'Swamp Trench 1 Key Ledge NW', Intr).dir(No, 0x37, Left, High).small_key().pos(2),
        create_door(player, 'Swamp Trench 1 Departure Dry', Lgcl),
        create_door(player, 'Swamp Trench 1 Departure Approach', Lgcl),
        create_door(player, 'Swamp Trench 1 Departure Key', Lgcl),
        create_door(player, 'Swamp Trench 1 Departure WS', Nrml).dir(We, 0x37, Bot, High).pos(4),
        create_door(player, 'Swamp Hammer Switch SW', Intr).dir(So, 0x37, Left, High).small_key().pos(2),
        create_door(player, 'Swamp Hammer Switch WN', Nrml).dir(We, 0x37, Top, High).pos(0),
        create_door(player, 'Swamp Hub ES', Nrml).dir(Ea, 0x36, Bot, High).pos(4),
        create_door(player, 'Swamp Hub S', Nrml).dir(So, 0x36, Mid, High).pos(5),
        create_door(player, 'Swamp Hub WS', Nrml).dir(We, 0x36, Bot, High).pos(3),
        create_door(player, 'Swamp Hub WN', Nrml).dir(We, 0x36, Top, High).small_key().pos(2),
        create_door(player, 'Swamp Hub Hook Path', Lgcl),
        create_door(player, 'Swamp Hub Dead Ledge EN', Nrml).dir(Ea, 0x36, Top, High).pos(0),
        create_door(player, 'Swamp Hub North Ledge N', Nrml).dir(No, 0x36, Mid, High).small_key().pos(1),
        create_door(player, 'Swamp Hub North Ledge Drop Down', Lgcl),
        create_door(player, 'Swamp Donut Top N', Nrml).dir(No, 0x46, Mid, High).pos(0),
        create_door(player, 'Swamp Donut Top SE', Intr).dir(So, 0x46, Right, High).pos(2),
        create_door(player, 'Swamp Donut Bottom NE', Intr).dir(No, 0x46, Right, High).pos(2),
        create_door(player, 'Swamp Donut Bottom NW', Intr).dir(No, 0x46, Left, High).pos(1),
        create_door(player, 'Swamp Compass Donut SW', Intr).dir(So, 0x46, Left, High).pos(1),
        create_door(player, 'Swamp Compass Donut Push Block', Lgcl),
        create_door(player, 'Swamp Crystal Switch EN', Nrml).dir(Ea, 0x35, Top, High).small_key().pos(0),
        create_door(player, 'Swamp Crystal Switch SE', Intr).dir(So, 0x35, Right, High).pos(3),
        create_door(player, 'Swamp Shortcut NE', Intr).dir(No, 0x35, Right, High).pos(3),
        create_door(player, 'Swamp Shortcut Blue Barrier', Lgcl),
        create_door(player, 'Swamp Trench 2 Pots ES', Nrml).dir(Ea, 0x35, Bot, High).pos(4),
        create_door(player, 'Swamp Trench 2 Pots Blue Barrier', Lgcl),
        create_door(player, 'Swamp Trench 2 Pots Dry', Lgcl),
        create_door(player, 'Swamp Trench 2 Pots Wet', Lgcl),
        create_door(player, 'Swamp Trench 2 Blocks Pots', Lgcl),
        create_door(player, 'Swamp Trench 2 Blocks N', Intr).dir(No, 0x35, Mid, Low).pos(5),
        create_door(player, 'Swamp Trench 2 Alcove S', Intr).dir(So, 0x35, Mid, Low).pos(5),
        create_door(player, 'Swamp Trench 2 Departure Wet', Lgcl),
        create_door(player, 'Swamp Trench 2 Departure WS', Nrml).dir(We, 0x35, Bot, High).pos(2),
        create_door(player, 'Swamp Big Key Ledge WN', Nrml).dir(We, 0x35, Top, High).pos(1),
        create_door(player, 'Swamp West Shallows ES', Nrml).dir(Ea, 0x34, Bot, High).pos(1),
        create_door(player, 'Swamp West Shallows Push Blocks', Lgcl),
        create_door(player, 'Swamp West Block Path Up Stairs', Sprl).dir(Up, 0x34, 0, HTH).ss(Z, 0x1b, 0x6c, False, True),
        create_door(player, 'Swamp West Block Path Drop Down', Lgcl),
        create_door(player, 'Swamp West Ledge Drop Down', Lgcl),
        create_door(player, 'Swamp West Ledge Hook Path', Lgcl),
        create_door(player, 'Swamp Barrier Ledge Drop Down', Lgcl),
        create_door(player, 'Swamp Barrier Ledge - Orange', Lgcl),
        create_door(player, 'Swamp Barrier EN', Nrml).dir(Ea, 0x34, Top, High).pos(0),
        create_door(player, 'Swamp Barrier - Orange', Lgcl),
        create_door(player, 'Swamp Barrier Ledge Hook Path', Lgcl),
        create_door(player, 'Swamp Attic Down Stairs', Sprl).dir(Dn, 0x54, 0, HTH).ss(Z, 0x12, 0x80, False, True),
        create_door(player, 'Swamp Attic Left Pit', Hole),
        create_door(player, 'Swamp Attic Right Pit', Hole),
        create_door(player, 'Swamp Push Statue S', Nrml).dir(So, 0x26, Mid, High).small_key().pos(0),
        create_door(player, 'Swamp Push Statue NW', Intr).dir(No, 0x26, Left, High).pos(1),
        create_door(player, 'Swamp Push Statue NE', Intr).dir(No, 0x26, Right, High).pos(2),
        create_door(player, 'Swamp Push Statue Down Stairs', Sprl).dir(Dn, 0x26, 2, HTH).ss(X, 0x12, 0xc0, False, True),
        create_door(player, 'Swamp Shooters SW', Intr).dir(So, 0x26, Left, High).pos(1),
        create_door(player, 'Swamp Shooters EN', Intr).dir(Ea, 0x26, Top, High).pos(3),
        create_door(player, 'Swamp Left Elbow WN', Intr).dir(We, 0x26, Top, High).pos(3),
        create_door(player, 'Swamp Left Elbow Down Stairs', Sprl).dir(Dn, 0x26, 0, HTH).ss(S, 0x11, 0x40, True, True),
        create_door(player, 'Swamp Right Elbow SE', Intr).dir(So, 0x26, Right, High).pos(2),
        create_door(player, 'Swamp Right Elbow Down Stairs', Sprl).dir(Dn, 0x26, 1, HTH).ss(S, 0x12, 0xb0, True, True),
        create_door(player, 'Swamp Drain Left Up Stairs', Sprl).dir(Up, 0x76, 0, HTH).ss(S, 0x1b, 0x2c, True, True),
        create_door(player, 'Swamp Drain WN', Intr).dir(We, 0x76, Top, Low).pos(0),
        create_door(player, 'Swamp Drain Right Switch', Lgcl),
        create_door(player, 'Swamp Drain Right Up Stairs', Sprl).dir(Up, 0x76, 1, HTH).ss(S, 0x1b, 0x9c, True, True),
        create_door(player, 'Swamp Flooded Room Up Stairs', Sprl).dir(Up, 0x76, 2, HTH).ss(X, 0x1a, 0xac, True, True),
        create_door(player, 'Swamp Flooded Room WS', Intr).dir(We, 0x76, Bot, Low).pos(1),
        create_door(player, 'Swamp Flooded Spot Ladder', Lgcl),
        create_door(player, 'Swamp Flooded Room Ladder', Lgcl),
        create_door(player, 'Swamp Basement Shallows NW', Nrml).dir(No, 0x76, Left, High).toggler().pos(2),
        create_door(player, 'Swamp Basement Shallows EN', Intr).dir(We, 0x76, Top, High).pos(0),
        create_door(player, 'Swamp Basement Shallows ES', Intr).dir(Ea, 0x76, Bot, High).pos(1),
        create_door(player, 'Swamp Waterfall Room SW', Nrml).dir(So, 0x66, Left, Low).toggler().pos(1),
        create_door(player, 'Swamp Waterfall Room NW', Intr).dir(No, 0x66, Left, Low).pos(3),
        create_door(player, 'Swamp Waterfall Room NE', Intr).dir(No, 0x66, Right, Low).pos(0),
        create_door(player, 'Swamp Refill SW', Intr).dir(So, 0x66, Left, Low).pos(3),
        create_door(player, 'Swamp Behind Waterfall SE', Intr).dir(So, 0x66, Right, Low).pos(0),
        create_door(player, 'Swamp Behind Waterfall Up Stairs', Sprl).dir(Up, 0x66, 0, HTH).ss(S, 0x1a, 0x6c, True, True),
        create_door(player, 'Swamp C Down Stairs', Sprl).dir(Dn, 0x16, 0, HTH).ss(S, 0x11, 0x80, True, True),
        create_door(player, 'Swamp C SE', Intr).dir(So, 0x16, Right, High).pos(2),
        create_door(player, 'Swamp Waterway NE', Intr).dir(No, 0x16, Right, High).pos(2),
        create_door(player, 'Swamp Waterway N', Intr).dir(No, 0x16, Mid, High).pos(0),
        create_door(player, 'Swamp Waterway NW', Intr).dir(No, 0x16, Left, High).small_key().pos(1),
        create_door(player, 'Swamp I S', Intr).dir(So, 0x16, Mid, High).pos(0),
        create_door(player, 'Swamp T SW', Intr).dir(So, 0x16, Left, High).small_key().pos(1),
        create_door(player, 'Swamp T NW', Nrml).dir(No, 0x16, Left, High).pos(3),
        create_door(player, 'Swamp Boss SW', Nrml).dir(So, 0x06, Left, High).trap(0x4).pos(0),

        create_door(player, 'Skull 1 Lobby WS', Nrml).dir(We, 0x58, Bot, High).small_key().pos(1),
        create_door(player, 'Skull 1 Lobby ES', Intr).dir(Ea, 0x58, Bot, High).pos(5),
        create_door(player, 'Skull Map Room WS', Intr).dir(We, 0x58, Bot, High).pos(5),
        create_door(player, 'Skull Map Room SE', Nrml).dir(So, 0x58, Right, High).small_key().pos(2),
        create_door(player, 'Skull Pot Circle WN', Intr).dir(We, 0x58, Top, High).pos(3),
        create_door(player, 'Skull Pull Switch EN', Intr).dir(Ea, 0x58, Top, High).pos(3),
        create_door(player, 'Skull Pot Circle Star Path', Lgcl),
        create_door(player, 'Skull Pull Switch S', Intr).dir(So, 0x58, Left, High).pos(0),
        create_door(player, 'Skull Big Chest N', Intr).dir(No, 0x58, Left, High).no_exit().pos(0),
        create_door(player, 'Skull Big Chest Hookpath', Lgcl),
        create_door(player, 'Skull Pinball NE', Nrml).dir(No, 0x68, Right, High).small_key().pos(1),
        create_door(player, 'Skull Pinball WS', Nrml).dir(We, 0x68, Bot, High).no_exit().trap(0x4).pos(0),
        create_door(player, 'Skull Compass Room NE', Nrml).dir(No, 0x67, Right, High).pos(0),
        create_door(player, 'Skull Compass Room ES', Nrml).dir(Ea, 0x67, Bot, High).pos(2),
        create_door(player, 'Skull Left Drop ES', Intr).dir(Ea, 0x67, Bot, High).pos(1),
        create_door(player, 'Skull Compass Room WS', Intr).dir(We, 0x67, Bot, High).pos(1),
        create_door(player, 'Skull Pot Prison ES', Nrml).dir(Ea, 0x57, Bot, High).small_key().pos(2),
        create_door(player, 'Skull Pot Prison SE', Nrml).dir(So, 0x57, Right, High).pos(5),
        create_door(player, 'Skull 2 East Lobby WS', Nrml).dir(We, 0x57, Bot, High).pos(4),
        create_door(player, 'Skull 2 East Lobby NW', Intr).dir(No, 0x57, Left, High).pos(1),
        create_door(player, 'Skull Big Key SW', Intr).dir(So, 0x57, Left, High).pos(1),
        create_door(player, 'Skull Big Key WN', Intr).dir(We, 0x57, Top, High).pos(0),
        create_door(player, 'Skull Lone Pot EN', Intr).dir(Ea, 0x57, Top, High).pos(0),
        create_door(player, 'Skull Small Hall ES', Nrml).dir(Ea, 0x56, Bot, High).pos(3),
        create_door(player, 'Skull Small Hall WS', Intr).dir(We, 0x56, Bot, High).pos(2),
        create_door(player, 'Skull 2 West Lobby ES', Intr).dir(Ea, 0x56, Bot, High).pos(2),
        create_door(player, 'Skull 2 West Lobby NW', Intr).dir(No, 0x56, Left, High).small_key().pos(0),
        create_door(player, 'Skull X Room SW', Intr).dir(So, 0x56, Left, High).small_key().pos(0),
        create_door(player, 'Skull Back Drop Star Path', Lgcl),
        create_door(player, 'Skull 3 Lobby NW', Nrml).dir(No, 0x59, Left, High).small_key().pos(0),
        create_door(player, 'Skull 3 Lobby WN', Intr).dir(We, 0x59, Top, High).pos(2),
        create_door(player, 'Skull East Bridge EN', Intr).dir(Ea, 0x59, Top, High).pos(2),
        create_door(player, 'Skull East Bridge ES', Intr).dir(Ea, 0x59, Bot, High).pos(3),
        create_door(player, 'Skull West Bridge Nook WS', Intr).dir(We, 0x59, Bot, High).pos(3),
        create_door(player, 'Skull Star Pits SW', Nrml).dir(So, 0x49, Left, High).small_key().pos(2),
        create_door(player, 'Skull Star Pits WS', Intr).dir(We, 0x49, Bot, High).pos(3),
        create_door(player, 'Skull Torch Room ES', Intr).dir(Ea, 0x49, Bot, High).pos(3),
        create_door(player, 'Skull Torch Room EN', Intr).dir(Ea, 0x49, Top, High).pos(1),
        create_door(player, 'Skull Vines WN', Intr).dir(We, 0x49, Top, High).pos(1),
        create_door(player, 'Skull Vines NW', Nrml).dir(No, 0x49, Left, High).pos(0),
        create_door(player, 'Skull Spike Corner SW', Nrml).dir(So, 0x39, Left, High).no_exit().trap(0x4).pos(0),
        create_door(player, 'Skull Spike Corner WS', Intr).dir(We, 0x39, Bot, High).small_key().pos(1),
        create_door(player, 'Skull Final Drop ES', Intr).dir(Ea, 0x39, Bot, High).small_key().pos(1),
        create_door(player, 'Skull Final Drop Hole', Hole),

        create_door(player, 'Thieves Lobby N Edge', Open).dir(No, 0xdb, None, Low),
        create_door(player, 'Thieves Lobby NE Edge', Open).dir(No, 0xdb, None, Low),
        create_door(player, 'Thieves Lobby E', Nrml).dir(Ea, 0xdb, Mid, High).no_exit().trap(0x4).pos(0),
        create_door(player, 'Thieves Big Chest Nook WS Edge', Open).dir(We, 0xdb, None, Low),
        create_door(player, 'Thieves Ambush S Edge', Open).dir(So, 0xcb, None, Low),
        create_door(player, 'Thieves Ambush SE Edge', Open).dir(So, 0xcb, None, Low),
        create_door(player, 'Thieves Ambush ES Edge', Open).dir(Ea, 0xcb, None, Low),
        create_door(player, 'Thieves Ambush EN Edge', Open).dir(Ea, 0xcb, None, Low),
        create_door(player, 'Thieves Ambush E', Nrml).dir(Ea, 0xcb, Mid, High).pos(0),
        create_door(player, 'Thieves BK Corner WN Edge', Open).dir(We, 0xcc, None, Low),
        create_door(player, 'Thieves BK Corner WS Edge', Open).dir(We, 0xcc, None, Low),
        create_door(player, 'Thieves BK Corner S Edge', Open).dir(So, 0xcc, None, Low),
        create_door(player, 'Thieves BK Corner SW Edge', Open).dir(So, 0xcc, None, Low),
        create_door(player, 'Thieves BK Corner W', Nrml).dir(We, 0xcc, Mid, High).pos(2),
        create_door(player, 'Thieves BK Corner NW', Nrml).dir(No, 0xcc, Left, High).pos(1),
        create_door(player, 'Thieves BK Corner NE', Nrml).dir(No, 0xcc, Right, High).big_key().pos(0),
        create_door(player, 'Thieves Compass Room NW Edge', Open).dir(No, 0xdc, None, Low),
        create_door(player, 'Thieves Compass Room N Edge', Open).dir(No, 0xdc, None, Low),
        create_door(player, 'Thieves Compass Room WS Edge', Open).dir(We, 0xdc, None, Low),
        create_door(player, 'Thieves Compass Room W', Nrml).dir(We, 0xdc, Mid, High).pos(0),
        create_door(player, 'Thieves Hallway SE', Nrml).dir(So, 0xbc, Right, High).small_key().pos(1),
        create_door(player, 'Thieves Hallway NE', Nrml).dir(No, 0xbc, Right, High).pos(7),
        create_door(player, 'Thieves Pot Alcove Mid WS', Nrml).dir(We, 0xbc, Bot, High).pos(5),
        create_door(player, 'Thieves Pot Alcove Bottom SW', Nrml).dir(So, 0xbc, Left, High).pos(3),
        create_door(player, 'Thieves Conveyor Maze WN', Nrml).dir(We, 0xbc, Top, High).pos(4),
        create_door(player, 'Thieves Hallway WS', Intr).dir(We, 0xbc, Bot, High).small_key().pos(0),
        create_door(player, 'Thieves Pot Alcove Mid ES', Intr).dir(Ea, 0xbc, Bot, High).small_key().pos(0),
        create_door(player, 'Thieves Conveyor Maze SW', Intr).dir(So, 0xbc, Left, High).pos(6),
        create_door(player, 'Thieves Pot Alcove Top NW', Intr).dir(No, 0xbc, Left, High).pos(6),
        create_door(player, 'Thieves Conveyor Maze EN', Intr).dir(Ea, 0xbc, Top, High).pos(2),
        create_door(player, 'Thieves Hallway WN', Intr).dir(We, 0xbc, Top, High).no_exit().pos(2),
        create_door(player, 'Thieves Conveyor Maze Down Stairs', Sprl).dir(Dn, 0xbc, 0, HTH).ss(A, 0x11, 0x80, True, True),
        create_door(player, 'Thieves Boss SE', Nrml).dir(So, 0xac, Right, High).no_exit().trap(0x4).pos(0),
        create_door(player, 'Thieves Spike Track ES', Nrml).dir(Ea, 0xbb, Bot, High).pos(5),
        create_door(player, 'Thieves Hellway NW', Nrml).dir(No, 0xbb, Left, High).pos(0),
        create_door(player, 'Thieves Triple Bypass EN', Nrml).dir(Ea, 0xbb, Top, High).pos(4),
        create_door(player, 'Thieves Hellway Orange Barrier', Lgcl),
        create_door(player, 'Thieves Hellway Crystal Orange Barrier', Lgcl),
        create_door(player, 'Thieves Hellway Blue Barrier', Lgcl),
        create_door(player, 'Thieves Hellway Crystal Blue Barrier', Lgcl),
        create_door(player, 'Thieves Spike Track WS', Intr).dir(We, 0xbb, Bot, High).pos(2),
        create_door(player, 'Thieves Hellway Crystal ES', Intr).dir(Ea, 0xbb, Bot, High).pos(2),
        create_door(player, 'Thieves Spike Track NE', Intr).dir(No, 0xbb, Right, High).pos(3),
        create_door(player, 'Thieves Triple Bypass SE', Intr).dir(So, 0xbb, Right, High).pos(3),
        create_door(player, 'Thieves Hellway Crystal EN', Intr).dir(Ea, 0xbb, Top, High).pos(1),
        create_door(player, 'Thieves Triple Bypass WN', Intr).dir(We, 0xbb, Top, High).pos(1),
        create_door(player, 'Thieves Spike Switch SW', Nrml).dir(So, 0xab, Left, High).pos(1),
        create_door(player, 'Thieves Spike Switch Up Stairs', Sprl).dir(Up, 0xab, 0, HTH).ss(Z, 0x1a, 0x6c, True, True).small_key().pos(0),
        create_door(player, 'Thieves Attic Down Stairs', Sprl).dir(Dn, 0x64, 0, HTH).ss(Z, 0x11, 0x80, True, True),
        create_door(player, 'Thieves Attic ES', Intr).dir(Ea, 0x64, Bot, High).pos(0),
        create_door(player, 'Thieves Cricket Hall Left WS', Intr).dir(We, 0x64, Bot, High).pos(0),
        create_door(player, 'Thieves Cricket Hall Left Edge', Open).dir(Ea, 0x64, None, High),
        create_door(player, 'Thieves Cricket Hall Right Edge', Open).dir(We, 0x65, None, High),
        create_door(player, 'Thieves Cricket Hall Right ES', Intr).dir(Ea, 0x65, Bot, High).pos(0),
        create_door(player, 'Thieves Attic Window WS', Intr).dir(We, 0x65, Bot, High).pos(0),
        create_door(player, 'Thieves Basement Block Up Stairs', Sprl).dir(Up, 0x45, 0, HTH).ss(A, 0x1a, 0x6c, True, True),
        create_door(player, 'Thieves Basement Block WN', Nrml).dir(We, 0x45, Top, High).trap(0x4).pos(0),
        create_door(player, 'Thieves Basement Block Path', Lgcl),
        create_door(player, 'Thieves Blocked Entry Path', Lgcl),
        create_door(player, 'Thieves Lonely Zazak WS', Nrml).dir(We, 0x45, Bot, High).pos(2),
        create_door(player, 'Thieves Blocked Entry SW', Intr).dir(So, 0x45, Left, High).pos(1),
        create_door(player, 'Thieves Lonely Zazak NW', Intr).dir(No, 0x45, Left, High).pos(1),
        create_door(player, 'Thieves Lonely Zazak ES', Intr).dir(Ea, 0x45, Right, High).pos(3),
        create_door(player, 'Thieves Blind\'s Cell WS', Intr).dir(We, 0x45, Right, High).pos(3),
        create_door(player, 'Thieves Conveyor Bridge EN', Nrml).dir(Ea, 0x44, Top, High).pos(2),
        create_door(player, 'Thieves Conveyor Bridge ES', Nrml).dir(Ea, 0x44, Bot, High).pos(3),
        create_door(player, 'Thieves Conveyor Bridge Block Path', Lgcl),
        create_door(player, 'Thieves Conveyor Block Path', Lgcl),
        create_door(player, 'Thieves Conveyor Bridge WS', Intr).dir(We, 0x44, Bot, High).small_key().pos(1),
        create_door(player, 'Thieves Big Chest Room ES', Intr).dir(Ea, 0x44, Bot, High).small_key().pos(1),
        create_door(player, 'Thieves Conveyor Block WN', Intr).dir(We, 0x44, Top, High).pos(0),
        create_door(player, 'Thieves Trap EN', Intr).dir(Ea, 0x44, Left, Top).pos(0),

        create_door(player, 'Ice Lobby WS', Intr).dir(We, 0x0e, Bot, High).pos(1),
        create_door(player, 'Ice Jelly Key ES', Intr).dir(Ea, 0x0e, Bot, High).pos(1),
        create_door(player, 'Ice Jelly Key Down Stairs', Sprl).dir(Dn, 0x0e, 0, HTH).ss(X, 0x11, 0x80, True, True).small_key().pos(0),
        create_door(player, 'Ice Floor Switch Up Stairs', Sprl).dir(Up, 0x1e, 0, HTH).ss(X, 0x1a, 0x6c, True, True),
        create_door(player, 'Ice Floor Switch ES', Intr).dir(Ea, 0x1e, Bot, High).pos(1),
        create_door(player, 'Ice Cross Left WS', Intr).dir(We, 0x1e, Bot, High).pos(1),
        create_door(player, 'Ice Cross Top NE', Intr).dir(No, 0x1e, Right, High).pos(2),
        create_door(player, 'Ice Bomb Drop SE', Intr).dir(So, 0x1e, Right, High).pos(2),
        create_door(player, 'Ice Cross Left Push Block', Lgcl),  # dynamic
        create_door(player, 'Ice Cross Bottom Push Block Left', Lgcl),
        create_door(player, 'Ice Cross Bottom Push Block Right', Lgcl),  # dynamic
        create_door(player, 'Ice Cross Right Push Block Top', Lgcl),
        create_door(player, 'Ice Cross Right Push Block Bottom', Lgcl),  # dynamic
        create_door(player, 'Ice Cross Top Push Block Left', Lgcl),
        create_door(player, 'Ice Cross Top Push Block Right', Lgcl),  # dynamic
        create_door(player, 'Ice Cross Bottom SE', Nrml).dir(So, 0x1e, Right, High).pos(3),
        create_door(player, 'Ice Cross Right ES', Nrml).dir(Ea, 0x1e, Bot, High).pos(0),
        create_door(player, 'Ice Bomb Drop Hole', Hole),
        create_door(player, 'Ice Compass Room NE', Nrml).dir(No, 0x2e, Right, High).pos(0),
        create_door(player, 'Ice Pengator Switch WS', Nrml).dir(We, 0x1f, Bot, High).pos(0),
        create_door(player, 'Ice Pengator Switch ES', Intr).dir(Ea, 0x1f, Bot, High).pos(1),
        create_door(player, 'Ice Dead End WS', Intr).dir(We, 0x1f, Bot, High).pos(1),
        create_door(player, 'Ice Big Key Push Block', Lgcl),
        create_door(player, 'Ice Big Key Down Ladder', Lddr),
        create_door(player, 'Ice Stalfos Hint SE', Intr).dir(So, 0x3e, Right, High).pos(0),
        create_door(player, 'Ice Conveyor NE', Intr).dir(No, 0x3e, Right, High).no_exit().pos(0),
        create_door(player, 'Ice Conveyor SW', Nrml).dir(So, 0x3e, Left, High).small_key().pos(1),
        create_door(player, 'Ice Bomb Jump NW', Nrml).dir(No, 0x4e, Left, High).small_key().pos(1),
        create_door(player, 'Ice Bomb Jump Ledge Orange Barrier', Lgcl),
        create_door(player, 'Ice Bomb Jump Catwalk Orange Barrier', Lgcl),
        create_door(player, 'Ice Bomb Jump EN', Intr).dir(Ea, 0x4e, Top, High).pos(0),
        create_door(player, 'Ice Narrow Corridor WN', Intr).dir(We, 0x4e, Top, High).pos(0),
        create_door(player, 'Ice Narrow Corridor Down Stairs', Sprl).dir(Dn, 0x4e, 0, HTH).ss(S, 0x52, 0xc0, True, True),
        create_door(player, 'Ice Pengator Trap Up Stairs', Sprl).dir(Up, 0x6e, 0, HTH).ss(S, 0x5a, 0xac, True, True),
        create_door(player, 'Ice Pengator Trap NE', Nrml).dir(No, 0x6e, Right, High).pos(0),
        create_door(player, 'Ice Spike Cross SE', Nrml).dir(So, 0x5e, Right, High).pos(2),
        create_door(player, 'Ice Spike Cross ES', Nrml).dir(Ea, 0x5e, Bot, High).small_key().pos(0),
        create_door(player, 'Ice Spike Cross WS', Intr).dir(We, 0x5e, Bot, High).pos(3),
        create_door(player, 'Ice Firebar ES', Intr).dir(Ea, 0x5e, Bot, High).pos(3),
        create_door(player, 'Ice Firebar Down Ladder', Lddr),
        create_door(player, 'Ice Spike Cross NE', Intr).dir(No, 0x5e, Right, High).pos(1),
        create_door(player, 'Ice Falling Square SE', Intr).dir(So, 0x5e, Right, High).pos(1),
        create_door(player, 'Ice Falling Square Hole', Hole),
        create_door(player, 'Ice Spike Room WS', Nrml).dir(We, 0x5f, Bot, High).small_key().pos(0),
        create_door(player, 'Ice Spike Room Up Stairs', Sprl).dir(Up, 0x5f, 4, HTH).ss(Z, 0x11, 0x48, True, True),
        create_door(player, 'Ice Spike Room Down Stairs', Sprl).dir(Dn, 0x5f, 3, HTH).ss(Z, 0x1a, 0xa4, True, True),
        create_door(player, 'Ice Hammer Block Down Stairs', Sprl).dir(Dn, 0x3f, 0, HTH).ss(Z, 0x11, 0xb8, True, True),
        create_door(player, 'Ice Hammer Block ES', Intr).dir(Ea, 0x3f, Bot, High).pos(0),
        create_door(player, 'Ice Tongue Pull WS', Intr).dir(We, 0x3f, Bot, High).pos(0),
        create_door(player, 'Ice Tongue Pull Up Ladder', Lddr),
        create_door(player, 'Ice Freezors Up Ladder', Lddr),
        create_door(player, 'Ice Freezors Hole', Hole),
        create_door(player, 'Ice Freezors Bomb Hole', Hole), # combine these two? -- they have to lead to the same spot
        create_door(player, 'Ice Freezors Ledge Hole', Hole),
        create_door(player, 'Ice Freezors Ledge ES', Intr).dir(Ea, 0x7e, Bot, High).pos(2),
        create_door(player, 'Ice Tall Hint WS', Intr).dir(We, 0x7e, Bot, High).pos(1),
        create_door(player, 'Ice Tall Hint EN', Nrml).dir(Ea, 0x7e, Top, High).pos(1),
        create_door(player, 'Ice Tall Hint SE', Nrml).dir(So, 0x7e, Right, High).small_key().pos(0),
        create_door(player, 'Ice Hookshot Ledge WN', Nrml).dir(We, 0x7f, Top, High).pos(0),
        create_door(player, 'Ice Hookshot Ledge Path', Lgcl),
        create_door(player, 'Ice Hookshot Balcony Path', Lgcl),
        create_door(player, 'Ice Hookshot Balcony SW', Intr).dir(So, 0x7f, Left, High).pos(1),
        create_door(player, 'Ice Spikeball NW', Intr).dir(No, 0x7f, Left, High).pos(1),
        create_door(player, 'Ice Spikeball Up Stairs', Sprl).dir(Up, 0x7f, 0, HTH).ss(Z, 0x1a, 0x34, True, True),
        create_door(player, 'Ice Lonely Freezor NE', Nrml).dir(No, 0x8e, Right, High).small_key().pos(0),
        create_door(player, 'Ice Lonely Freezor Down Stairs', Sprl).dir(Up, 0x8e, 0, HTH).ss(S, 0x11, 0x50, True, True),
        create_door(player, 'Iced T EN', Nrml).dir(Ea, 0xae, Top, High).pos(0),
        create_door(player, 'Iced T Up Stairs', Sprl).dir(Up, 0xae, 0, HTH).ss(S, 0x1a, 0x3c, True, True),
        create_door(player, 'Ice Catwalk WN', Nrml).dir(We, 0xaf, Top, High).pos(1),
        create_door(player, 'Ice Catwalk NW', Nrml).dir(No, 0xaf, Left, High).pos(0),
        create_door(player, 'Ice Many Pots SW', Nrml).dir(So, 0x9f, Left, High).pos(1),
        create_door(player, 'Ice Many Pots WS', Nrml).dir(We, 0x9f, Bot, High).pos(0),
        create_door(player, 'Ice Crystal Right ES', Nrml).dir(Ea, 0x9e, Bot, High).pos(3),
        create_door(player, 'Ice Crystal Right Orange Barrier', Lgcl),
        create_door(player, 'Ice Crystal Right Blue Hole', Hole),  # combine holes again??
        create_door(player, 'Ice Crystal Left Orange Barrier', Lgcl),
        create_door(player, 'Ice Crystal Left Blue Barrier', Lgcl),
        create_door(player, 'Ice Crystal Block Exit', Lgcl),
        create_door(player, 'Ice Crystal Block Hole', Hole),
        create_door(player, 'Ice Crystal Left WS', Intr).dir(We, 0x9e, Bot, High).pos(2),
        create_door(player, 'Ice Big Chest View ES', Intr).dir(Ea, 0x9e, Bot, High).pos(2),
        create_door(player, 'Ice Big Chest Landing Push Blocks', Lgcl),
        create_door(player, 'Ice Crystal Right NE', Intr).dir(No, 0x9e, Right, High).big_key().pos(1),
        create_door(player, 'Ice Backwards Room SE', Intr).dir(So, 0x9e, Right, High).pos(1),
        create_door(player, 'Ice Backwards Room Down Stairs', Sprl).dir(Dn, 0x9e, 0, HTH).ss(S, 0x11, 0x80, True, True).small_key().pos(0),
        create_door(player, 'Ice Backwards Room Hole', Hole),
        create_door(player, 'Ice Anti-Fairy Up Stairs', Sprl).dir(Up, 0xbe, 0, HTH).ss(S, 0x1a, 0x6c, True, True),
        create_door(player, 'Ice Anti-Fairy SE', Intr).dir(So, 0xbe, Right, High).pos(2),
        create_door(player, 'Ice Switch Room NE', Intr).dir(No, 0xbe, Right, High).pos(2),
        create_door(player, 'Ice Switch Room ES', Nrml).dir(Ea, 0xbe, Bot, High).small_key().pos(1),
        create_door(player, 'Ice Switch Room SE', Nrml).dir(So, 0xbe, Right, High).pos(0),
        create_door(player, 'Ice Refill WS', Nrml).dir(We, 0xbf, Bot, High).small_key().pos(0),
        create_door(player, 'Ice Fairy Warp', Warp),
        create_door(player, 'Ice Antechamber NE', Nrml).dir(No, 0xce, Right, High).pos(0),
        create_door(player, 'Ice Antechamber Hole', Hole),

        # Door Templates
        # create_door(player, '', Nrml).dir(No, 0x00, Right, High).pos(),
        # create_door(player, '', Intr).dir(No, 0x00, Right, High).pos(),
        # create_door(player, '', Sprl).dir(Up, 0x00, 0, HTH).ss(Q, 0x0, 0x0),
        # create_door(player, '', Lgcl),
        # create_door(player, '', Hole),
        # create_door(player, '', Warp),
    ]
    create_paired_doors(world, player)

    # swamp events
    world.get_door('Swamp Trench 1 Approach Key', player).event('Trench 1 Switch')
    world.get_door('Swamp Trench 1 Approach Swim Depart', player).event('Trench 1 Switch')
    world.get_door('Swamp Trench 1 Key Approach', player).event('Trench 1 Switch')
    world.get_door('Swamp Trench 1 Key Ledge Depart', player).event('Trench 1 Switch')
    world.get_door('Swamp Trench 1 Departure Approach', player).event('Trench 1 Switch')
    world.get_door('Swamp Trench 1 Departure Key', player).event('Trench 1 Switch')
    world.get_door('Swamp Trench 2 Pots Wet', player).event('Trench 2 Switch')
    world.get_door('Swamp Trench 2 Departure Wet', player).event('Trench 2 Switch')
    world.get_door('Swamp Drain WN', player).event('Swamp Drain')
    world.get_door('Swamp Flooded Room WS', player).event('Swamp Drain')
    world.get_door('Swamp Drain Right Switch', player).event('Swamp Drain')
    world.get_door('Swamp Flooded Room Ladder', player).event('Swamp Drain')


    # crystal switches and barriers
    world.get_door('Hera Lobby Down Stairs', player).c_switch()
    world.get_door('Hera Lobby Key Stairs', player).c_switch()
    world.get_door('Hera Lobby Up Stairs', player).c_switch()
    world.get_door('Hera Basement Cage Up Stairs', player).c_switch()
    world.get_door('Hera Tile Room Up Stairs', player).c_switch()
    world.get_door('Hera Tile Room EN', player).c_switch()
    world.get_door('Hera Tridorm WN', player).c_switch()
    world.get_door('Hera Tridorm SE', player).c_switch()
    world.get_door('Hera Beetles Down Stairs', player).c_switch()
    world.get_door('Hera Beetles WS', player).c_switch()
    world.get_door('Hera Beetles Holes', player).c_switch()
    world.get_door('Hera Startile Wide SW', player).c_switch()
    world.get_door('Hera Startile Wide Up Stairs', player).c_switch()
    world.get_door('Hera Startile Wide Holes', player).c_switch()

    world.get_door('PoD Arena Main SW', player).c_switch()
    world.get_door('PoD Arena Bridge SE', player).c_switch()
    world.get_door('PoD Arena Main Orange Barrier', player).barrier(CrystalBarrier.Orange)
    # maybe you can cross this way with blue up??
    world.get_door('PoD Arena Main Crystal Path', player).barrier(CrystalBarrier.Blue)
    world.get_door('PoD Arena Crystals E', player).barrier(CrystalBarrier.Blue)
    world.get_door('PoD Arena Crystal Path', player).barrier(CrystalBarrier.Blue)
    world.get_door('PoD Sexy Statue W', player).c_switch()
    world.get_door('PoD Sexy Statue NW', player).c_switch()
    world.get_door('PoD Bow Statue SW', player).c_switch()
    world.get_door('PoD Bow Statue Down Ladder', player).c_switch()
    world.get_door('PoD Dark Pegs Up Ladder', player).c_switch()
    world.get_door('PoD Dark Pegs WN', player).c_switch()

    world.get_door('Swamp Crystal Switch EN', player).c_switch()
    world.get_door('Swamp Crystal Switch SE', player).c_switch()
    world.get_door('Swamp Shortcut Blue Barrier', player).barrier(CrystalBarrier.Blue)
    world.get_door('Swamp Trench 2 Pots Blue Barrier', player).barrier(CrystalBarrier.Blue)
    world.get_door('Swamp Barrier Ledge - Orange', player).barrier(CrystalBarrier.Orange)
    world.get_door('Swamp Barrier - Orange', player).barrier(CrystalBarrier.Orange)

    world.get_door('Thieves Spike Switch Up Stairs', player).c_switch()
    world.get_door('Thieves Spike Switch SW', player).c_switch()
    world.get_door('Thieves Attic ES', player).barrier(CrystalBarrier.Blue)
    world.get_door('Thieves Hellway Blue Barrier', player).barrier(CrystalBarrier.Blue)
    world.get_door('Thieves Hellway Crystal Blue Barrier', player).barrier(CrystalBarrier.Blue)
    world.get_door('Thieves Triple Bypass SE', player).barrier(CrystalBarrier.Blue)
    world.get_door('Thieves Triple Bypass WN', player).barrier(CrystalBarrier.Blue)
    world.get_door('Thieves Triple Bypass EN', player).barrier(CrystalBarrier.Blue)
    world.get_door('Thieves Hellway Orange Barrier', player).barrier(CrystalBarrier.Orange)
    world.get_door('Thieves Hellway Crystal Orange Barrier', player).barrier(CrystalBarrier.Orange)

    world.get_door('Ice Bomb Drop SE', player).c_switch()
    world.get_door('Ice Conveyor SW', player).c_switch()
    world.get_door('Ice Refill WS', player).c_switch()
    world.get_door('Ice Bomb Drop Hole', player).barrier(CrystalBarrier.Orange)  # not required to hit switch w/ bomb
    world.get_door('Ice Bomb Jump Ledge Orange Barrier', player).barrier(CrystalBarrier.Orange)
    world.get_door('Ice Bomb Jump Catwalk Orange Barrier', player).barrier(CrystalBarrier.Orange)
    world.get_door('Ice Crystal Right Orange Barrier', player).barrier(CrystalBarrier.Orange)
    world.get_door('Ice Crystal Right Blue Hole', player).barrier(CrystalBarrier.Blue)
    world.get_door('Ice Crystal Left Orange Barrier', player).barrier(CrystalBarrier.Orange)
    world.get_door('Ice Crystal Left Blue Barrier', player).barrier(CrystalBarrier.Blue)
    world.get_door('Ice Backwards Room Hole', player).barrier(CrystalBarrier.Blue)

    # nifty dynamic logical doors:
    south_controller = world.get_door('Ice Cross Bottom SE', player)
    east_controller = world.get_door('Ice Cross Right ES', player)
    controller_door(south_controller, world.get_door('Ice Cross Left Push Block', player))
    controller_door(south_controller, world.get_door('Ice Cross Right Push Block Bottom', player))
    controller_door(east_controller, world.get_door('Ice Cross Bottom Push Block Right', player))
    controller_door(east_controller, world.get_door('Ice Cross Top Push Block Right', player))


def create_paired_doors(world, player):
    world.paired_doors[player] = [
        PairedDoor('Sewers Secret Room Key Door S', 'Sewers Key Rat Key Door N'),
        # PairedDoor('', ''),  # TR Pokey Key
        # PairedDoor('', ''),  # TR Big key door by pipes
        PairedDoor('PoD Falling Bridge WN', 'PoD Dark Maze EN'),  # Pod Dark maze door
        PairedDoor('PoD Dark Maze E', 'PoD Big Chest Balcony W'),  # PoD Bombable by Big Chest
        PairedDoor('PoD Arena Main NW', 'PoD Falling Bridge SW'),  # Pod key door by bridge
        PairedDoor('Sewers Dark Cross Key Door N', 'Sewers Dark Cross Key Door S'),
        PairedDoor('Swamp Hub WN', 'Swamp Crystal Switch EN'),  # Swamp key door crystal switch
        PairedDoor('Swamp Hub North Ledge N', 'Swamp Push Statue S'),  # Swamp key door above big chest
        PairedDoor('PoD Map Balcony WS', 'PoD Arena Ledge ES'),  # Pod bombable by arena
        PairedDoor('Swamp Hub Dead Ledge EN', 'Swamp Hammer Switch WN'),  # Swamp bombable to random pots
        PairedDoor('Swamp Pot Row WN', 'Swamp Map Ledge EN'),  # Swamp bombable to map chest
        PairedDoor('Swamp Pot Row WS', 'Swamp Trench 1 Approach ES'),  # Swamp key door early room $38
        PairedDoor('PoD Middle Cage N', 'PoD Pit Room S'),
        # PairedDoor('', ''),  # GT moldorm key door
        PairedDoor('Ice Conveyor SW', 'Ice Bomb Jump NW'),  # Ice BJ key door
        PairedDoor('Desert Tiles 2 SE', 'Desert Beamos Hall NE'),
        PairedDoor('Skull 3 Lobby NW', 'Skull Star Pits SW'),  # Skull 3 key door
        PairedDoor('Skull 1 Lobby WS', 'Skull Pot Prison ES'),  # Skull 1 key door - pot prison to big chest
        PairedDoor('Skull Map Room SE', 'Skull Pinball NE'),  # Skull 1 - pinball key door
        # PairedDoor('', ''),  # gt main big key door
        PairedDoor('Ice Spike Cross ES', 'Ice Spike Room WS'),  # ice door to spike chest
        # PairedDoor('', ''),  # gt right side key door to cape bridge
        # PairedDoor('', ''),  # gt bombable to rando room
        PairedDoor('Ice Tall Hint SE', 'Ice Lonely Freezor NE'),  # ice's big icy room key door to lonely freezor
        PairedDoor('Eastern Courtyard N', 'Eastern Darkness S'),
        # PairedDoor('', ''),  # mire fishbone key door
        # PairedDoor('', ''),  # mire big key door to bridges
        PairedDoor('Eastern Big Key NE', 'Eastern Hint Tile Blocked Path SE'),
        # PairedDoor('', ''),  # TR somaria hub to pokey
        PairedDoor('Eastern Dark Square Key Door WN', 'Eastern Cannonball Ledge Key Door EN'),
        PairedDoor('Thieves BK Corner NW', 'Thieves Pot Alcove Bottom SW'),  # TT random bomb to pots
        PairedDoor('Thieves BK Corner NW', 'Thieves Hallway SE'),  # TT big key door
        PairedDoor('Ice Switch Room ES', 'Ice Refill WS'),  # Ice last key door to crystal switch
        # PairedDoor('', ''),  # mire hub key door to attic
        # PairedDoor('', ''),  # mire hub key door to map
        # PairedDoor('', ''),  # tr last key door to switch maze
        PairedDoor('Thieves Ambush E', 'Thieves BK Corner W')  # TT dashable above
    ]


def controller_door(controller, dependent):
    dependent.controller = controller
    controller.dependents.append(dependent)


def create_door(player, name, door_type):
    return Door(player, name, door_type)


def ugly_door(door):
    door.ugly = True
    return door
