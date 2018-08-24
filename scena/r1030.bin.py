from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1030.bin",                # FileName
        "r1030",                    # MapName
        "r1030",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1030", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x07,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 4, 0, 5],
    )

    BuildStringList((
        "r1030",                  # 0
        "CGF Member",             # 1
        "CGF Member",             # 2
        "Triton, the Silver Orca",# 3
        "バス",                   # 4
        "Special Support Vehicle",# 5
        "暴走車",                 # 6
        "メルカバ",               # 7
        "メルカバ",               # 8
        "カエンギーヌー",         # 9
        "カエンギーヌー",         # 10
        "ガンテ",                 # 11
        "ガンテ",                 # 12
        "br1000",                 # 13
        "br1000",                 # 14
        "br1000",                 # 15
        "br1000",                 # 16
        "br1000",                 # 17
        "br1000",                 # 18
        "br1000",                 # 19
        "br1000",                 # 20
        "br1000",                 # 21
        "To Crossbell City",      # 22
        "To Bellguard Gate",      # 23
        "To Police Academy",      # 24
    ))

    ATBonus("ATBonus_868", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_888", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_8B15", 0,   0,   7,   0,   2,   2,   2)
    Sepith("Sepith_8B1D", 2,   2,   0,   0,   3,   3,   3)
    Sepith("Sepith_8AF5", 2,   1,   5,   0,   0,   3,   2)
    Sepith("Sepith_8AFD", 0,   3,   0,   5,   2,   3,   0)
    Sepith("Sepith_8B2D", 2,   1,   4,   1,   0,   2,   2)
    Sepith("Sepith_8B3D", 11,  7,   4,   3,   6,   12,  7)

    MonsterBattlePostion("MonsterBattlePostion_8C8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_8CC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8DC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_928", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_92C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_930", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_934", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_938", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_93C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_940", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_944", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_8A8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_8AC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8BC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C4", 2, 13, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_A10", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_8B15", 30, 40, 20, 10,
        (
            ("ms71300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71300.dat", "ms71300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71300.dat", "ms70400.dat", "ms71300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71300.dat", "ms71300.dat", "ms70400.dat", "ms66900.dat", 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
        )
    )

    BattleInfo(
        "BattleInfo_BA0", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_8B1D", 30, 30, 20, 20,
        (
            ("ms64200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms64200.dat", "ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms64200.dat", "ms66900.dat", "ms64200.dat", "ms66900.dat", 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
        )
    )

    BattleInfo(
        "BattleInfo_C68", 0x0000, 50, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_8AF5", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
        )
    )

    BattleInfo(
        "BattleInfo_948", 0x0000, 50, 6, 60, 8, 1, 40, 0, "br1000", "Sepith_8AFD", 30, 40, 20, 10,
        (
            ("ms70300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms70300.dat", "ms70300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms70300.dat", "ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
        )
    )

    BattleInfo(
        "BattleInfo_AD8", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_8B2D", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms71900.dat", "ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
        )
    )

    BattleInfo(
        "BattleInfo_D30", 0x0000, 84, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_8B3D", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8C8", "MonsterBattlePostion_928", "ed7450", "ed7453", "ATBonus_868"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E54", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72400.dat", "ms72400.dat", "ms72400.dat", "ms72400.dat", "ms72400.dat", "ms72400.dat", 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7451", "ed7453", "ATBonus_888"),
            (),
            (),
            (),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_DCC", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7453", "ed7453", "ATBonus_868"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E10", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, "MonsterBattlePostion_8A8", "MonsterBattlePostion_928", "ed7453", "ed7453", "ATBonus_868"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch45700.itc",                   # 00
        "chr/ch31200.itc",                   # 01
        "chr/ch31300.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch70350.itc",               # 10
        "monster/ch70351.itc",               # 11
        "monster/ch71350.itc",               # 12
        "monster/ch71351.itc",               # 13
        "monster/ch71950.itc",               # 14
        "monster/ch71950.itc",               # 15
        "monster/ch64250.itc",               # 16
        "monster/ch64251.itc",               # 17
        "monster/ch63250.itc",               # 18
        "monster/ch63251.itc",               # 19
        "monster/ch60750.itc",               # 1A
        "monster/ch60750.itc",               # 1B
        "monster/ch72450.itc",               # 1C
        "monster/ch72450.itc",               # 1D
    ))

    DeclNpc(4294911736, 4294961296, 4294889066, 135,  389,  0x0, 0,   1,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294912596, 4294961296, 4294888087, 315,  389,  0x0, 0,   2,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294907646, 0,       34909,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294927966, 0,       46720,   270,  485,  0x0, 0,   18,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294885066, 4294965296, 4294940217, 270,  485,  0x0, 0,   18,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294927966, 0,       46720,   270,  485,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(4294885066, 4294965296, 4294940217, 270,  485,  0x0, 0,   26,  0,   0,   2,   255, 255, 255,  0)

    DeclMonster(4294949416, 910,     0,       0x1010000,    "BattleInfo_A10", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294922886, 4294959546, 0,       0x1010000,    "BattleInfo_BA0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294950856, 44520,   0,       0x1010000,    "BattleInfo_C68", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294928146, 60950,   0,       0x1010000,    "BattleInfo_948", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294893006, 4294941556, 4294965296, 0x1010000,    "BattleInfo_C68", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294932586, 4294924706, 4294963296, 0x1010000,    "BattleInfo_A10", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294904536, 4294904796, 4294961296, 0x1010000,    "BattleInfo_AD8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294948166, 6440,    0,       0x1010000,    "BattleInfo_D30", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294907726, 4294958016, 0,       0x1010000,    "BattleInfo_D30", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294910926, 4294891156, 4294961296, 0x1010000,    "BattleInfo_D30", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294939806, 31330,   0,       0x1010000,    "BattleInfo_D30", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294943476, 53310,   0,       0x18500B4,    "BattleInfo_E54", 0,   28,  0xFFFF, 12, 13)

    DeclEvent(0x0000, 0, 28,  -56.0,                 -87.0,                 -7.0,                  2500.0,                [0.05000000074505806,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.799999952316284,     17.399999618530273,    1.399999976158142,     1.0])
    DeclEvent(0x0000, 0, 29,  -32.5,                 1.5,                   -1.0,                  2025.0,                [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666667014360428,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   5.4166669845581055,    -0.10000000894069672,  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 30,  -56.0,                 -80.0,                 -7.0,                  2500.0,                [0.05000000074505806,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.799999952316284,     16.0,                  1.399999976158142,     1.0])
    DeclEvent(0x0040, 0, 22,  -23.81999969482422,    53.310001373291016,    0.0,                   16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   2.9774999618530273,    -6.663750171661377,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 26,  -56.4900016784668,     -86.98999786376953,    -6.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.766000270843506,     28.996665954589844,    1.2000000476837158,    1.0])
    DeclEvent(0x0000, 0, 54,  -34.95000076293945,    23.649999618530273,    0.0,                   900.0,                 [0.035355325788259506, 0.23570235073566437,   -0.0,                  0.0,                   -0.035355351865291595, 0.23570218682289124,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.0718226432800293,    2.663440704345703,     -0.0,                  1.0])
    DeclEvent(0x0000, 0, 55,  -57.27000045776367,    20.360000610351562,    0.0,                   225.0,                 [0.23570218682289124,  0.07071070373058319,   -0.0,                  0.0,                   -0.23570235073566437,  0.07071065157651901,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   18.297563552856445,    2.6099331378936768,    -0.0,                  1.0])

    DeclActor(4294929596, 0,       8150,    1200,    4294929596, 1000,    8150,    0x007C, 0,  25, 0x0000)
    DeclActor(4294955156, 0,       44860,   1200,    4294955156, 1000,    44860,   0x007C, 0,  6,  0x0000)
    DeclActor(4294926086, 0,       4294959257, 1200,    4294926086, 1000,    4294959257, 0x007C, 0,  7,  0x0000)
    DeclActor(4294940086, 4294963396, 4294923266, 1200,    4294940086, 4294964396, 4294923266, 0x007C, 0,  8,  0x0000)
    DeclActor(4294927966, 0,       46720,   1200,    4294927966, 0,       46720,   0x007C, 0,  9,  0x0000)
    DeclActor(4294885066, 4294965296, 4294940216, 1200,    4294885066, 4294965296, 4294940216, 0x007C, 0,  10, 0x0000)
    DeclActor(4294909466, 0,       35060,   1200,    4294908966, 4294966296, 41020,   0x007C, 0,  23, 0x0000)
    DeclActor(4294931106, 0,       16430,   1200,    4294931106, 2000,    16430,   0x007C, 0,  24, 0x0000)
    DeclActor(4294907296, 0,       32650,   1200,    4294907296, 2000,    32650,   0x007C, 0,  24, 0x0000)
    DeclActor(4294917846, 4294961296, 4294891036, 1200,    4294917936, 4294964296, 4294890656, 0x007C, 0,  57, 0x0000)
    DeclActor(4294929506, 0,       10900,   1500,    4294929506, 1700,    10900,   0x007C, 0,  58, 0x0000)

    PlaceName(29.0, 0.0, 19.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-95.0, 0.0, 84.0, 0x0000, 0x0000, "To Bellguard Gate")
    PlaceName(-55.0, 0.0, -114.0, 0x0000, 0x0000, "To Police Academy")
    PlaceName(-37.5, 0.0, 8.449999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 12
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 13

    ScpFunction((
        "Function_0_102C",         # 00, 0
        "Function_1_10E4",         # 01, 1
        "Function_2_1103",         # 02, 2
        "Function_3_1122",         # 03, 3
        "Function_4_118E",         # 04, 4
        "Function_5_17C0",         # 05, 5
        "Function_6_290B",         # 06, 6
        "Function_7_2A5C",         # 07, 7
        "Function_8_2BAD",         # 08, 8
        "Function_9_2CFE",         # 09, 9
        "Function_10_305A",        # 0A, 10
        "Function_11_33B6",        # 0B, 11
        "Function_12_33D9",        # 0C, 12
        "Function_13_33DD",        # 0D, 13
        "Function_14_34A0",        # 0E, 14
        "Function_15_35D3",        # 0F, 15
        "Function_16_3706",        # 10, 16
        "Function_17_3757",        # 11, 17
        "Function_18_37EB",        # 12, 18
        "Function_19_387B",        # 13, 19
        "Function_20_38F5",        # 14, 20
        "Function_21_4591",        # 15, 21
        "Function_22_48E1",        # 16, 22
        "Function_23_4B4D",        # 17, 23
        "Function_24_4DF2",        # 18, 24
        "Function_25_512F",        # 19, 25
        "Function_26_5481",        # 1A, 26
        "Function_27_5A97",        # 1B, 27
        "Function_28_5CAA",        # 1C, 28
        "Function_29_674D",        # 1D, 29
        "Function_30_6B0D",        # 1E, 30
        "Function_31_7176",        # 1F, 31
        "Function_32_77A9",        # 20, 32
        "Function_33_77C8",        # 21, 33
        "Function_34_7828",        # 22, 34
        "Function_35_785F",        # 23, 35
        "Function_36_78DF",        # 24, 36
        "Function_37_7904",        # 25, 37
        "Function_38_7969",        # 26, 38
        "Function_39_7984",        # 27, 39
        "Function_40_79DF",        # 28, 40
        "Function_41_8134",        # 29, 41
        "Function_42_81A6",        # 2A, 42
        "Function_43_8208",        # 2B, 43
        "Function_44_826A",        # 2C, 44
        "Function_45_82DA",        # 2D, 45
        "Function_46_8374",        # 2E, 46
        "Function_47_83AC",        # 2F, 47
        "Function_48_83F2",        # 30, 48
        "Function_49_842A",        # 31, 49
        "Function_50_84A4",        # 32, 50
        "Function_51_8692",        # 33, 51
        "Function_52_870E",        # 34, 52
        "Function_53_8755",        # 35, 53
        "Function_54_87CA",        # 36, 54
        "Function_55_88C2",        # 37, 55
        "Function_56_8934",        # 38, 56
        "Function_57_89CA",        # 39, 57
        "Function_58_8A2A",        # 3A, 58
    ))


    def Function_0_102C(): pass

    label("Function_0_102C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_106C"),
        (1, "loc_1078"),
        (2, "loc_1084"),
        (3, "loc_1090"),
        (4, "loc_109C"),
        (5, "loc_10A8"),
        (6, "loc_10B4"),
        (SWITCH_DEFAULT, "loc_10C0"),
    )


    label("loc_106C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_1078")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_1084")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_1090")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_109C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_10A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_10B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_10C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_10CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10CC")

    label("loc_10E3")

    Return()

    # Function_0_102C end

    def Function_1_10E4(): pass

    label("Function_1_10E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1102")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_10E4")

    label("loc_1102")

    Return()

    # Function_1_10E4 end

    def Function_2_1103(): pass

    label("Function_2_1103")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1121")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_1103")

    label("loc_1121")

    Return()

    # Function_2_1103 end

    def Function_3_1122(): pass

    label("Function_3_1122")

    SetMapObjFlags(0x29, 0x2000000)
    SetMapObjFlags(0x2A, 0x2000000)
    SetMapObjFlags(0x28, 0x2000000)
    SetMapObjFlags(0x24, 0x2000000)
    SetMapObjFlags(0x4, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_114F")
    ClearMapObjFlags(0x28, 0x2000000)

    label("loc_114F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1169")
    ClearMapObjFlags(0x29, 0x2000000)
    ClearMapObjFlags(0x2A, 0x2000000)

    label("loc_1169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_117D")
    ClearMapObjFlags(0x24, 0x2000000)

    label("loc_117D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118D")
    ClearMapObjFlags(0x4, 0x2000000)

    label("loc_118D")

    Return()

    # Function_3_1122 end

    def Function_4_118E(): pass

    label("Function_4_118E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_11A8")
    SetChrPos(0xA, -57240, 0, 32830, 95)

    label("loc_11A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11BB")
    SetChrFlags(0xA, 0x80)
    Jump("loc_126E")

    label("loc_11BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_11D2")
    SetChrFlags(0xA, 0x80)

    label("loc_11D2")

    Jump("loc_126E")

    label("loc_11D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11E5")
    Jump("loc_126E")

    label("loc_11E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1207")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    Jump("loc_126E")

    label("loc_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_1215")
    Jump("loc_126E")

    label("loc_1215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1223")
    Jump("loc_126E")

    label("loc_1223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1231")
    Jump("loc_126E")

    label("loc_1231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_123F")
    Jump("loc_126E")

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1252")
    SetChrFlags(0xA, 0x10)
    Jump("loc_126E")

    label("loc_1252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1260")
    Jump("loc_126E")

    label("loc_1260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_126E")
    SetChrFlags(0xA, 0x80)

    label("loc_126E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_127D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 40)

    label("loc_127D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_128E")
    Event(0, 31)

    label("loc_128E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1732")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131B")
    SetScenarioFlags(0x38, 0)

    label("loc_131B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1331")
    SetScenarioFlags(0x38, 1)

    label("loc_1331")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1347")
    SetScenarioFlags(0x38, 2)

    label("loc_1347")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
    SetScenarioFlags(0x38, 3)

    label("loc_135D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    SetScenarioFlags(0x38, 4)

    label("loc_1373")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1389")
    SetScenarioFlags(0x38, 5)

    label("loc_1389")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139F")
    SetScenarioFlags(0x38, 6)

    label("loc_139F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B5")
    SetScenarioFlags(0x38, 7)

    label("loc_13B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CB")
    SetScenarioFlags(0x39, 0)

    label("loc_13CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E1")
    SetScenarioFlags(0x39, 1)

    label("loc_13E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F7")
    SetScenarioFlags(0x39, 2)

    label("loc_13F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140D")
    SetScenarioFlags(0x39, 3)

    label("loc_140D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1423")
    SetScenarioFlags(0x39, 4)

    label("loc_1423")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1439")
    SetScenarioFlags(0x39, 5)

    label("loc_1439")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144F")
    SetScenarioFlags(0x39, 6)

    label("loc_144F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1465")
    SetScenarioFlags(0x39, 7)

    label("loc_1465")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147B")
    SetScenarioFlags(0x3A, 0)

    label("loc_147B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1491")
    SetScenarioFlags(0x3A, 1)

    label("loc_1491")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A7")
    SetScenarioFlags(0x3A, 2)

    label("loc_14A7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BD")
    SetScenarioFlags(0x3A, 3)

    label("loc_14BD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D3")
    SetScenarioFlags(0x3A, 4)

    label("loc_14D3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E9")
    SetScenarioFlags(0x3A, 5)

    label("loc_14E9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FF")
    SetScenarioFlags(0x3A, 6)

    label("loc_14FF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1515")
    SetScenarioFlags(0x3A, 7)

    label("loc_1515")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152B")
    SetScenarioFlags(0x3B, 0)

    label("loc_152B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1541")
    SetScenarioFlags(0x3B, 1)

    label("loc_1541")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1557")
    SetScenarioFlags(0x3B, 2)

    label("loc_1557")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156D")
    SetScenarioFlags(0x3B, 3)

    label("loc_156D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1583")
    SetScenarioFlags(0x3B, 4)

    label("loc_1583")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1599")
    SetScenarioFlags(0x3B, 5)

    label("loc_1599")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AF")
    SetScenarioFlags(0x3B, 6)

    label("loc_15AF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C5")
    SetScenarioFlags(0x3B, 7)

    label("loc_15C5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DB")
    SetScenarioFlags(0x3D, 5)

    label("loc_15DB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F1")
    SetScenarioFlags(0x3D, 6)

    label("loc_15F1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1607")
    SetScenarioFlags(0x3D, 7)

    label("loc_1607")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1642")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1732")

    label("loc_1642")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1665")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1732")

    label("loc_1665")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1688")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1732")

    label("loc_1688")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16AB")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1732")

    label("loc_16AB")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CE")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1732")

    label("loc_16CE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F1")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1732")

    label("loc_16F1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1714")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1732")

    label("loc_1714")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1732")
    SetScenarioFlags(0x3C, 7)

    label("loc_1732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1748")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_177A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177A")
    SetChrPos(0x0, -36420, 0, 17340, 315)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 17)

    label("loc_177A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_17AD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AD")
    SetChrPos(0x0, -60000, 0, 32650, 315)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_17AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_17BC")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 16)

    label("loc_17BC")

    Call(0, 11)
    Return()

    # Function_4_118E end

    def Function_5_17C0(): pass

    label("Function_5_17C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_17D2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17D2")

    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17EA")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_17EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17FD")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_17FD")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1815")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1815")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_182D")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_182D")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1845")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1845")

    ModifyEventFlags(0, 5, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_185D")
    ModifyEventFlags(1, 5, 0x80)

    label("loc_185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1870")
    ModifyEventFlags(1, 5, 0x80)

    label("loc_1870")

    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1888")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_1888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_189B")
    OP_1B(0x1, 0x0, 0x38)

    label("loc_189B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18C1")
    SetMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    OP_70(0x3, 0x0)
    OP_10(0x2, 0x0)
    Jump("loc_18E4")

    label("loc_18C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18DA")
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_18E4")

    label("loc_18DA")

    SetMapObjFlags(0x7, 0x4)
    OP_70(0x3, 0x28)

    label("loc_18E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1995")
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    ClearMapObjFlags(0x1E, 0x4)
    ClearMapObjFlags(0x1F, 0x4)
    ClearMapObjFlags(0x20, 0x4)
    ClearMapObjFlags(0x21, 0x4)
    ClearMapObjFlags(0x22, 0x4)
    ClearMapObjFlags(0x23, 0x4)

    label("loc_1995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19A3")
    Jump("loc_1A3D")

    label("loc_19A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19D2")
    ClearMapObjFlags(0x24, 0x4)
    SetMapObjFrame(0x24, "light", 0x0, 0x1)
    SetMapObjFrame(0x24, "mark01", 0x0, 0x1)
    Jump("loc_1A3D")

    label("loc_19D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_19E0")
    Jump("loc_1A3D")

    label("loc_19E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_19EE")
    Jump("loc_1A3D")

    label("loc_19EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_19FC")
    Jump("loc_1A3D")

    label("loc_19FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1A0A")
    Jump("loc_1A3D")

    label("loc_1A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A18")
    Jump("loc_1A3D")

    label("loc_1A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A26")
    Jump("loc_1A3D")

    label("loc_1A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_1A34")
    Jump("loc_1A3D")

    label("loc_1A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1A3D")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1A64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5F")
    ClearChrFlags(0x1F, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    SetChrFlags(0x1F, 0x8000)

    label("loc_1A5F")

    Jump("loc_1A6E")

    label("loc_1A64")

    SetChrFlags(0x1F, 0x80)
    ModifyEventFlags(0, 3, 0x80)

    label("loc_1A6E")

    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2597")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_2597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_2679")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    ClearMapObjFlags(0x1E, 0x4)
    ClearMapObjFlags(0x1F, 0x4)
    ClearMapObjFlags(0x20, 0x4)
    ClearMapObjFlags(0x21, 0x4)
    ClearMapObjFlags(0x22, 0x4)
    ClearMapObjFlags(0x23, 0x4)
    Jump("loc_2721")

    label("loc_2679")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x22, 0x4)
    SetMapObjFlags(0x23, 0x4)

    label("loc_2721")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -58330, -1000, 41020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2785")
    OP_66(0x6, 0x1)

    label("loc_2785")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27CA")
    OP_65(0x6, 0x1)

    label("loc_27CA")

    MiniGame(0x2F, 0x7, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0x4, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_280A")
    OP_70(0x0, 0x0)
    Jump("loc_280E")

    label("loc_280A")

    OP_70(0x0, 0x1E)

    label("loc_280E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2821")
    OP_70(0x1, 0x0)
    Jump("loc_2825")

    label("loc_2821")

    OP_70(0x1, 0x1E)

    label("loc_2825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2838")
    OP_70(0x2, 0x0)
    Jump("loc_283C")

    label("loc_2838")

    OP_70(0x2, 0x1E)

    label("loc_283C")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_289D")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -39330, 0, 46720, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_289D")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28E9")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -82230, -2000, -27080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_28E9")

    OP_1C(0x0, 0x25, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0x26, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0x27, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    Return()

    # Function_5_17C0 end

    def Function_6_290B(): pass

    label("Function_6_290B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A07")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x9D, 1)"), scpexpr(EXPR_END)), "loc_2990")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E3, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_2A02")

    label("loc_2990")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2A02")

    Jump("loc_2A50")

    label("loc_2A07")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_2A50")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_290B end

    def Function_7_2A5C(): pass

    label("Function_7_2A5C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B58")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_2AE1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E3, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_2B53")

    label("loc_2AE1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2B53")

    Jump("loc_2BA1")

    label("loc_2B58")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_2BA1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_2A5C end

    def Function_8_2BAD(): pass

    label("Function_8_2BAD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA9")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x38E, 1)"), scpexpr(EXPR_END)), "loc_2C32")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E3, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_2CA4")

    label("loc_2C32")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2CA4")

    Jump("loc_2CF2")

    label("loc_2CA9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_2CF2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_2BAD end

    def Function_9_2CFE(): pass

    label("Function_9_2CFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EB5")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_2E96")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like\x01",
            "something's buried. Dig\x01",
            "it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E91")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2E8E")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2DB3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2DB3)
    TurnDirection(0x10, 0x0, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    PlayEffect(0x7, 0x1, 0x10, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_DCC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E89")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E70")
    Call(1, 5)
    Jump("loc_2E89")

    label("loc_2E70")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E86")
    Call(1, 4)
    Jump("loc_2E89")

    label("loc_2E86")

    Call(1, 3)

    label("loc_2E89")

    Jump("loc_2E91")

    label("loc_2E8E")

    Call(1, 1)

    label("loc_2E91")

    Jump("loc_2EAC")

    label("loc_2E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2EAC")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2EAC")

    TalkEnd(0xFF)
    Return()

    label("loc_2EB5")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_303F")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like\x01",
            "something's buried. Dig\x01",
            "it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303A")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_3037")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2F5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2F5C)
    TurnDirection(0x12, 0x0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    PlayEffect(0x7, 0x1, 0x12, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_E10", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3032")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3019")
    Call(1, 5)
    Jump("loc_3032")

    label("loc_3019")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_302F")
    Call(1, 4)
    Jump("loc_3032")

    label("loc_302F")

    Call(1, 3)

    label("loc_3032")

    Jump("loc_303A")

    label("loc_3037")

    Call(1, 1)

    label("loc_303A")

    Jump("loc_3055")

    label("loc_303F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_3055")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_3055")

    TalkEnd(0xFF)
    Return()

    # Function_9_2CFE end

    def Function_10_305A(): pass

    label("Function_10_305A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3211")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_31F2")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like\x01",
            "something's buried. Dig\x01",
            "it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31ED")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_31EA")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_310F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_310F)
    TurnDirection(0x11, 0x0, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    PlayEffect(0x7, 0x1, 0x11, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_DCC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E5")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_31CC")
    Call(1, 5)
    Jump("loc_31E5")

    label("loc_31CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_31E2")
    Call(1, 4)
    Jump("loc_31E5")

    label("loc_31E2")

    Call(1, 3)

    label("loc_31E5")

    Jump("loc_31ED")

    label("loc_31EA")

    Call(1, 1)

    label("loc_31ED")

    Jump("loc_3208")

    label("loc_31F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_3208")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_3208")

    TalkEnd(0xFF)
    Return()

    label("loc_3211")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_339B")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like\x01",
            "something's buried. Dig\x01",
            "it out?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3396")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_3393")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_32B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_32B8)
    TurnDirection(0x13, 0x0, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    PlayEffect(0x7, 0x1, 0x13, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_E10", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_338E")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3375")
    Call(1, 5)
    Jump("loc_338E")

    label("loc_3375")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_338B")
    Call(1, 4)
    Jump("loc_338E")

    label("loc_338B")

    Call(1, 3)

    label("loc_338E")

    Jump("loc_3396")

    label("loc_3393")

    Call(1, 1)

    label("loc_3396")

    Jump("loc_33B1")

    label("loc_339B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_33B1")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_33B1")

    TalkEnd(0xFF)
    Return()

    # Function_10_305A end

    def Function_11_33B6(): pass

    label("Function_11_33B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33D8")
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)

    label("loc_33D8")

    Return()

    # Function_11_33B6 end

    def Function_12_33D9(): pass

    label("Function_12_33D9")

    Call(1, 6)
    Return()

    # Function_12_33D9 end

    def Function_13_33DD(): pass

    label("Function_13_33DD")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KIt's a bus stop. Ride the bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City West Entrance\x01",      # 0
            "Bellguard Gate\x01",                    # 1
            "Cancel\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3478")
    Call(0, 14)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_3498")

    label("loc_3478")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3498")
    Call(0, 15)
    ClearMapFlags(0x8000000)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()

    label("loc_3498")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_13_33DD end

    def Function_14_34A0(): pass

    label("Function_14_34A0")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_35CF")
    Fade(500)
    OP_68(-40030, 600, 12630, 0)
    MoveCamera(38, 23, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(24000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -39500, 0, 7300, 270)
    SetChrPos(0x1, -39500, 0, 8500, 270)
    SetChrPos(0x2, -39500, 0, 9700, 270)
    SetChrPos(0x3, -39500, 0, 10900, 270)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    OP_78(0x4, 0xB)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xB, -34810, 0, 22700, 225)
    OP_D5(0xB, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_3586():
        OP_95(0xFE, -43990, 0, 13530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3586)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xB, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_35CF")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_14_34A0 end

    def Function_15_35D3(): pass

    label("Function_15_35D3")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_3702")
    Fade(500)
    OP_68(-38160, 600, 3480, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -39500, 0, 7300, 180)
    SetChrPos(0x1, -39500, 0, 8500, 180)
    SetChrPos(0x2, -39500, 0, 9700, 180)
    SetChrPos(0x3, -39500, 0, 10900, 180)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    OP_78(0x4, 0xB)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xB, -27200, 0, 1290, 270)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_36B9():
        OP_95(0xFE, -39660, 0, 1670, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_36B9)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xB, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_3702")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_15_35D3 end

    def Function_16_3706(): pass

    label("Function_16_3706")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -36870, 0, 7430, 225)
    OP_31(0x1)
    OP_68(-36870, 600, 7430, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x5)
    Return()

    # Function_16_3706 end

    def Function_17_3757(): pass

    label("Function_17_3757")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_37B2")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37A7")
    Sound(2502, 255, 100, 0)
    Jump("loc_37AD")

    label("loc_37A7")

    Sound(2503, 255, 100, 0)

    label("loc_37AD")

    Jump("loc_37D6")

    label("loc_37B2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37D0")
    Sound(3347, 255, 100, 0)
    Jump("loc_37D6")

    label("loc_37D0")

    Sound(3348, 255, 100, 0)

    label("loc_37D6")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_3757 end

    def Function_18_37EB(): pass

    label("Function_18_37EB")

    TalkBegin(0xFE)

    ChrTalk(
        0x8,
        (
            "*sigh*, working in this\x01",
            "rain... Today just isn't\x01",
            "my day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm just about finished\x01",
            "here, so I think I'll be\x01",
            "leaving pretty soon.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_37EB end

    def Function_19_387B(): pass

    label("Function_19_387B")

    TalkBegin(0xFE)

    ChrTalk(
        0x9,
        (
            "We finally finished\x01",
            "cleaning up that trashed\x01",
            "gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What could have done\x01",
            "something like that, and\x01",
            "how...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_387B end

    def Function_20_38F5(): pass

    label("Function_20_38F5")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_390D")
    SetScenarioFlags(0x0, 1)

    label("loc_390D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_3919")
    SetScenarioFlags(0x0, 1)

    label("loc_3919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AF3")
    TurnDirection(0xA, 0x101, 0)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Oh, could you be from\x01",
            "the Fisherman's Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I'm Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Haha, I knew it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm Triton. They call me\x01",
            "the Silver Orca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well to be honest, I\x01",
            "wonder about that name\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems anglers have to\x01",
            "have one. Club rules say\x01",
            "so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, whenever you want\x01",
            "to challenge me, just\x01",
            "say the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, I'll have to\x01",
            "make sure you're\x01",
            "qualified.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AF3")
    OP_93(0xA, 0x0, 0x0)

    label("loc_3AF3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_458D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B56")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                                 # 0
            "Challenge Him to an Angler Duel\x01",      # 1
            "Cancel\x01",                               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_3B60")

    label("loc_3B56")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_427E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B8E")
    TurnDirection(0xA, 0x0, 0)

    label("loc_3B8E")

    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_409C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D28")

    ChrTalk(
        0xA,
        (
            "Alright then, let me\x01",
            "have a look at your\x01",
            "fishing notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Wow, that's amazing. You\x01",
            "did well in catching so\x01",
            "many different types.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha, then, want to have\x01",
            "an Angler Duel against\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mine is a "5-Catch Angler Duel"...\x01\x07\x02",
            "It means the first to catch 5\x01",
            "different types of fish, wins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Doesn't that sound fun?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 0)
    Jump("loc_3DB7")

    label("loc_3D28")


    ChrTalk(
        0xA,
        (
            "Hmm? Want to have a\x01",
            "match with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mine is a "5-Catch Angler Duel"...\x01\x07\x02",
            "It means the first to catch 5\x01",
            "different types of fish, wins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DB7")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Challenge Triton, the\x01",
            "Silver Orca, to a\x01",
            ""5-Catch Angler Duel"?\x07\x00",
            ".\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Challenge Him\x01",      # 0
            "Refuse\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E5B"),
        (1, "loc_4065"),
        (SWITCH_DEFAULT, "loc_4097"),
    )


    label("loc_3E5B")


    ChrTalk(
        0xA,
        "Haha, that's the spirit♪\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    ClearMapFlags(0x1)
    OP_68(-58450, 1000, 33710, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, -53410, 0, 15290, 226)
    OP_31(0x1)
    SetChrPos(0x101, -57240, 0, 32830, 95)
    OP_93(0xA, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE("apl/ch51012.itc")
    MiniGame(0x7, 0x3, 0xA, 0xFFFF2CDE, 0x0, 0x821E, 0xFFFF1C26, 0xFFFFFC18, 0xA03C)
    SetChrPos(0x0, -53410, 0, 15290, 226)
    OP_31(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9E")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_68(-60090, 1000, 33250, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -59650, 0, 32659, 0)
    OP_93(0xA, 0xB4, 0x0)
    Sleep(500)
    Call(0, 50)
    Return()

    label("loc_3F9E")

    OP_68(-58660, 1000, 33990, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -57240, 0, 32830, 315)
    TurnDirection(0xA, 0x101, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FFD")
    Call(0, 51)
    Jump("loc_4024")

    label("loc_3FFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4013")
    Call(0, 53)
    Jump("loc_4024")

    label("loc_4013")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4024")
    Call(0, 52)

    label("loc_4024")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, -57240, 0, 32830, 315)
    OP_31(0x1)
    SetMapFlags(0x1)
    OP_69(0xFF, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_4097")

    label("loc_4065")


    ChrTalk(
        0xA,
        "Hmm, too bad then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4092")
    OP_93(0xA, 0x0, 0x0)

    label("loc_4092")

    Jump("loc_4097")

    label("loc_4097")

    Jump("loc_4279")

    label("loc_409C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_41A1")

    ChrTalk(
        0xA,
        (
            "Let's see then, I'll\x01",
            "check your fishing\x01",
            "notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "Hmm, close. You're\x01",
            "missing one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, you've come this\x01",
            "far, so I'm sure you'll\x01",
            "make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Just a little more. Do\x01",
            "your best, ok?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_419C")
    OP_93(0xA, 0x0, 0x0)

    label("loc_419C")

    Jump("loc_4279")

    label("loc_41A1")


    ChrTalk(
        0xA,
        (
            "Alright then, let me\x01",
            "have a look at your\x01",
            "fishing notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "Hmm, you still lack\x01",
            "effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyhow, I can't accept a\x01",
            "challenge from you with\x01",
            "just these catches.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4279")
    OP_93(0xA, 0x0, 0x0)

    label("loc_4279")

    Jump("loc_4588")

    label("loc_427E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_42A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_42AF")
    Jump("loc_4588")

    label("loc_42AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4315")

    ChrTalk(
        0xA,
        (
            "Hmm, it's become\x01",
            "dangerous lately\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Could this be no time\x01",
            "for fishing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4588")

    label("loc_4315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_436C")

    ChrTalk(
        0xA,
        (
            "Maaan, it's raining\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm gonna get soaked.\x01",
            "Ahhahahaha.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4588")

    label("loc_436C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_43DA")

    ChrTalk(
        0xA,
        (
            "*yaaawn*, anyway, I'm\x01",
            "sleepy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even though I slept more\x01",
            "than twelve hours\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4588")

    label("loc_43DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4424")

    ChrTalk(
        0xA,
        "*ooooooh, aaaaaah*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, today's air is\x01",
            "clean too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4588")

    label("loc_4424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4483")

    ChrTalk(
        0xA,
        (
            "*yaaawn*, they're not\x01",
            "biting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I guess it's time to\x01",
            "test the next bait?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4588")

    label("loc_4483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_44BE")

    ChrTalk(
        0xA,
        "*staaaaaaaaaare*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hmm, so quiet...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4588")

    label("loc_44BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4571")

    ChrTalk(
        0xA,
        "*yaa...aaawaaaawn*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "............ ...hmm,\x01",
            "sleepy...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_456C")

    ChrTalk(
        0x101,
        (
            "#00003F(It seems I could fish\x01",
            "here, but... Since there's\x01",
            "already someone, I won't.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_456C")

    Jump("loc_4588")

    label("loc_4571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_457F")
    Jump("loc_4588")

    label("loc_457F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4588")

    label("loc_4588")

    Jump("loc_3AFD")

    label("loc_458D")

    TalkEnd(0xFE)
    Return()

    # Function_20_38F5 end

    def Function_21_4591(): pass

    label("Function_21_4591")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45B6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45D1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45EC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4607")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4607")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4622")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4622")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_463D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_463D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4658")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4658")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4673")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4673")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_468E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_468E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46A9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46C4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46DF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46FA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4715")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4715")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4730")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4730")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_474B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_474B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4766")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4781")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4781")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_479C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_479C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47B7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47D2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47ED")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4808")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4808")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4823")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4823")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_483E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_483E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4859")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4859")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4874")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4874")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_488F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_488F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48AA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_48AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48C5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_48C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48E0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_48E0")

    Return()

    # Function_21_4591 end

    def Function_22_48E1(): pass

    label("Function_22_48E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 3)), scpexpr(EXPR_END)), "loc_48EB")
    Return()

    label("loc_48EB")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is\x01",
            "wandering about.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Cancel]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_49C9"),
        (SWITCH_DEFAULT, "loc_49E2"),
    )


    label("loc_49C9")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -24310, 0, 47440, 180)
    EventEnd(0x5)
    Return()

    label("loc_49E2")

    Battle("BattleInfo_E54", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-24310, 1000, 47440, 0)
    OP_90(0x0, -24310, 0, 47440, 180)
    OP_90(0x1, -24310, 0, 47440, 180)
    OP_90(0x2, -24310, 0, 47440, 180)
    OP_90(0x3, -24310, 0, 47440, 180)
    OP_90(0x4, -24310, 0, 47440, 180)
    OP_90(0x5, -24310, 0, 47440, 180)
    OP_90(0x6, -24310, 0, 47440, 180)
    OP_90(0x7, -24310, 0, 47440, 180)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_4AA4"),
        (1, "loc_4AA9"),
        (SWITCH_DEFAULT, "loc_4AAC"),
    )


    label("loc_4AA4")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_4AA9")

    OP_B9(0x0)
    Return()

    label("loc_4AAC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x1F, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wanted monster\x01",
            "exterminated!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x73),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0x73, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21D, 3)
    OP_29(0x99, 0x4, 0x2)
    OP_29(0x99, 0x4, 0x10)
    OP_29(0x99, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 3, 0x80)
    EventEnd(0x5)
    Return()

    # Function_22_48E1 end

    def Function_23_4B4D(): pass

    label("Function_23_4B4D")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-58890, 1000, 38460, 1500)
    MoveCamera(45, 38, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(21000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DED")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C26")
    MiniGame(0x6, 0x13, 0xFFFF1E1A, 0x0, 0x88F4, 0x0, 0xFFFF1C26, 0xFFFFFC18, 0xA03C)
    Jump("loc_4DED")

    label("loc_4C26")

    MiniGame(0x6, 0x14, 0xFFFF1E1A, 0x0, 0x88F4, 0x0, 0xFFFF1C26, 0xFFFFFC18, 0xA03C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DED")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(-57530, 1000, 35490, 0)
    MoveCamera(42, 31, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17270, 0)
    LoadChrToIndex("apl/ch50160.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, -57830, 0, 35060, 0)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x0,
        "Lloyd",
        (
            "#00011FW-Whoa... The thickness\x01",
            "and weight are\x01",
            "incredible.\x02\x03",
            "#00003FAnd also, it's very\x01",
            "pretty... Could this be\x01",
            "a rare fish?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, -57830, 0, 35060, 0)
    SetChrPos(0x2, -57830, 0, 35060, 0)
    SetChrPos(0x3, -57830, 0, 35060, 0)
    SetChrPos(0x4, -57830, 0, 35060, 0)
    SetChrPos(0x5, -57830, 0, 35060, 0)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_37()
    SetScenarioFlags(0x18B, 5)

    label("loc_4DED")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_23_4B4D end

    def Function_24_4DF2(): pass

    label("Function_24_4DF2")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E24")
    SetScenarioFlags(0x31, 2)

    label("loc_4E24")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_4E64")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E59")
    Sound(2499, 255, 100, 0)
    Jump("loc_4E5F")

    label("loc_4E59")

    Sound(3537, 255, 100, 0)

    label("loc_4E5F")

    Jump("loc_4E6A")

    label("loc_4E64")

    Sound(3344, 255, 100, 0)

    label("loc_4E6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5121")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4EDF")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4EBF"),
        (SWITCH_DEFAULT, "loc_4ED0"),
    )


    label("loc_4EBF")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4EDA")

    label("loc_4ED0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EDA")

    Jump("loc_511C")

    label("loc_4EDF")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4F11")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_4F11")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F45"),
        (1, "loc_5049"),
        (2, "loc_50DA"),
        (SWITCH_DEFAULT, "loc_5112"),
    )


    label("loc_4F45")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4F76")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4F86")

    label("loc_4F76")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4F86")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FDC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FDC")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FFF")
    Sound(461, 0, 100, 0)

    label("loc_4FFF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_501F")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_502F")

    label("loc_501F")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_502F")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_4E6A")

    label("loc_5049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_50BB")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_507E")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_5096")

    label("loc_507E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5091")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_5096")

    label("loc_5091")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_5096")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50D5")

    label("loc_50BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_50CB")
    OP_AF(0xFB)
    Jump("loc_50D5")

    label("loc_50CB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50D5")

    Jump("loc_511C")

    label("loc_50DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_510D")

    label("loc_50F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5103")
    OP_AF(0xFB)
    Jump("loc_510D")

    label("loc_5103")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_510D")

    Jump("loc_511C")

    label("loc_5112")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_511C")

    Jump("loc_4E6A")

    label("loc_5121")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_24_4DF2 end

    def Function_25_512F(): pass

    label("Function_25_512F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53AF")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5334")

    ChrTalk(
        0x105,
        (
            "#10309FWell then, shall we ride\x01",
            "the bus and return to\x01",
            "Crossbell City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWe've come this far, so\x01",
            "that's a no.\x02\x03",
            "#00000FWe're halfway there, I\x01",
            "guess? Let's do our best\x01",
            "the rest of the way.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_532C")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When the story advances,\x01",
            "you will be able to take\x01",
            "the bus at all bus stops.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They are convenient for traveling\x01",
            "on the highways, so please use\x01",
            "them when the time comes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 5)

    label("loc_532C")

    SetScenarioFlags(0x0, 2)
    Jump("loc_53AC")

    label("loc_5334")


    ChrTalk(
        0x101,
        (
            "#00000FWe've come this far... I guess we're\x01",
            "halfway there? Let's do our best and\x01",
            "walk the rest of the way as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53AC")

    EventEnd(0x3)
    Return()

    label("loc_53AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_542D")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001FWith the accident, we\x01",
            "don't have time to wait\x01",
            "for the bus.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x3)
    Return()

    label("loc_542D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_547D")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems the orbal bus service is not running.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_547D")

    Call(0, 13)
    Return()

    # Function_25_512F end

    def Function_26_5481(): pass

    label("Function_26_5481")

    SetMapObjFlags(0x3, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_556A")
    EventBegin(0x1)
    OP_E2(0x3)
    Fade(500)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00001FThe police academy is this way...\x02\x03",
            "Of course, the State Guard soldiers\x01",
            "are here as well. Let's retrace our\x01",
            "steps before we get noticed.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -56320, -6000, -83050, 0)
    OP_E2(0x2)
    EventEnd(0x4)
    Jump("loc_5A90")

    label("loc_556A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59C2")
    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -55720, -6000, -85510, 180)
    SetChrPos(0x103, -54770, -6000, -85100, 180)
    SetChrPos(0x104, -56880, -6000, -85190, 180)
    SetChrPos(0x105, -55010, -6000, -83820, 180)
    SetChrPos(0x106, -56250, -6000, -83870, 180)
    SetChrPos(0x107, -55490, -6000, -82560, 180)
    SetChrSubChip(0x107, 0x5)
    OP_68(-57100, -1680, -84150, 0)
    MoveCamera(135, 18, 0, 0)
    OP_6E(490, 0)
    SetCameraDistance(17500, 0)
    OP_68(-57100, -4080, -84150, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003F#5PThe police academy area\x01",
            "is this way...\x02\x03",
            "#0001FThe gate is completely\x01",
            "shut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6P... I sensed a small\x01",
            "quantity of orbal waves\x01",
            "near the gate.\x02\x03",
            "#00200FIt seems some new\x01",
            "sensors have been\x01",
            "installed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah, they may have\x01",
            "heightened security\x01",
            "after my jailbreak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400F#6PWell, it's best not to\x01",
            "get too close.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00308F#12PYou said that ol' man\x01",
            "Garcｵa helped you escape\x01",
            "from prison?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3C#6PWhen I arrived, though,\x01",
            "you were alone, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PYeah. To allow me to\x01",
            "escape, he distracted\x01",
            "the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10712F#6PThat Killing Bear did\x01",
            "that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PA lot of stuff happened\x01",
            "to that ol' man too, I\x01",
            "bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P... I'm honestly a little\x01",
            "worried about what\x01",
            "happened after that...\x02\x03",
            "#00001FAt any rate, let's think\x01",
            "about how to proceed.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 27)
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -56320, -6000, -83050, 0)
    SetScenarioFlags(0x1BC, 6)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_5A90")

    label("loc_59C2")

    EventBegin(0x1)
    OP_E2(0x3)
    Fade(500)
    MoveCamera(45, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#00200FIt seems some sensors\x01",
            "have been newly\x01",
            "installed near the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI'm worried about\x01",
            "Garcｵa, but... Let's not\x01",
            "get too close.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -56320, -6000, -83050, 0)
    OP_E2(0x2)
    EventEnd(0x4)

    label("loc_5A90")

    ClearMapObjFlags(0x3, 0x1000)
    Return()

    # Function_26_5481 end

    def Function_27_5A97(): pass

    label("Function_27_5A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CA9")
    OP_29(0xAF, 0x1, 0xF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008F#5PAnd so, we've checked\x01",
            "everywhere we could, but it's\x01",
            "blocked from every direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12POf course we can't go to Crossbell City, but\x01",
            "it doesn't look like we can go to Bellguard\x01",
            "Gate or the police academy either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10706F#6PThat's a problem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400F#6PHmm, isn't there\x01",
            "anywhere else we can go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3C#6PMaybe it's best to look\x01",
            "for someplace a ways\x01",
            "away from the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#5PYou're right... Let's\x01",
            "search a little more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA9")

    Return()

    # Function_27_5A97 end

    def Function_28_5CAA(): pass

    label("Function_28_5CAA")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-56090, -3600, -86800, 0)
    OP_6E(510, 0)
    MoveCamera(359, 24, 0, 0)
    SetCameraDistance(28520, 0)
    SetChrPos(0x101, -56000, -6000, -78000, 180)
    SetChrPos(0x102, -55200, -6000, -76800, 180)
    SetChrPos(0x109, -56850, -6000, -76650, 180)
    SetChrPos(0x105, -56100, -6000, -75650, 180)
    FadeToBright(1000, 0)
    OP_68(-56030, -3600, -90500, 3000)

    def lambda_5D8F():
        OP_9B(0x0, 0x101, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5D8F)
    Sleep(0)

    def lambda_5DA7():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5DA7)
    Sleep(0)

    def lambda_5DBF():
        OP_9B(0x0, 0x109, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5DBF)
    Sleep(0)

    def lambda_5DD7():
        OP_9B(0x0, 0x105, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5DD7)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F#5PYeah, they left it open\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306F#5PMan, we're finally here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PThe police academy is\x01",
            "further ahead, right?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-56250, -4550, -87530, 0)
    MoveCamera(135, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19650, 0)
    SetChrPos(0x101, -56450, -6000, -88250, 180)
    SetChrPos(0x102, -55350, -6000, -87250, 180)
    SetChrPos(0x109, -57000, -6000, -86650, 180)
    SetChrPos(0x105, -56000, -6000, -86000, 180)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah. A paved woodland\x01",
            "path starts here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6PIf we follow it, we'll\x01",
            "end up at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, no one's here to\x01",
            "welcome us. Shall we\x01",
            "head on in?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)
    TurnDirection(0x101, 0x105, 500)
    Sleep(50)

    def lambda_608D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_608D)
    Sleep(100)

    def lambda_609D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_609D)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        (
            "#00006F#11P...No. I'm worried about\x01",
            "that guy we met earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PYeah... He looked way\x01",
            "too strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PBut we can't ignore that\x01",
            "request from chief.\x02\x03",
            "#00101FShould we split into two\x01",
            "teams?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6POne team to continue to the\x01",
            "academy and the other to\x01",
            "return to the city, huh.\x02\x03",
            "#10300FThat's not a bad idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#11PNo. With these members,\x01",
            "it's too early to split\x01",
            "up.\x02\x03",
            "#00001FBut, just to be safe,\x01",
            "I'll contact Section\x01",
            "One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#5PI see. That's a good\x01",
            "idea.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(823, 0, 100, 0)
    Sleep(2700)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Emma's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─Crossbell Police,\x01",
            "Section One.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FDetective Emma. Thanks\x01",
            "for your help earlier.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Emma's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Detective Bannings.\x02\x03",
            "What's wrong? Is about\x01",
            "that earlier case?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003FNo, this is different.\x02\x03",
            "#00001FYou see...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd told Emma about the\x01",
            "one-eyed giant man they\x01",
            "encountered on the highway.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Emma's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...A big, red headed,\x01",
            "one-eyed man about 40\x01",
            "years old?\x02\x03",
            "Not using a car, train\x01",
            "or airship, but on foot\x01",
            "on the highway...\x02\x03",
            "─Understood. We'll keep\x01",
            "an eye out for him.\x02\x03",
            "You should do as Chief\x01",
            "Sergei asks.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FYes ma'am. And thank\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(250)
    Sound(813, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302F#6PHaha, you got in touch\x01",
            "with that lady from\x01",
            "Section One, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah. I feel a little\x01",
            "better now.\x02\x03",
            "#00000FThen, shall we pass\x01",
            "through the gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#5PRight. Let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#6PRoger that.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(19400, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, -56000, -6000, -86000, 180)
    SetScenarioFlags(0x127, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_28_5CAA end

    def Function_29_674D(): pass

    label("Function_29_674D")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    OP_68(-35500, 1000, 1000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -31450, 0, 1050, 270)
    SetChrPos(0x102, -30850, 0, 100, 270)
    SetChrPos(0x103, -29950, 0, 1850, 270)
    SetChrPos(0x104, -28850, 0, 1550, 270)
    SetChrPos(0x109, -29650, 0, 0, 270)
    SetChrPos(0x105, -28050, 0, 750, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(19500, 2500)

    def lambda_682E():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_682E)
    Sleep(20)

    def lambda_6846():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6846)
    Sleep(20)

    def lambda_685E():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_685E)
    Sleep(20)

    def lambda_6876():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6876)
    Sleep(20)

    def lambda_688E():
        OP_9B(0x0, 0x109, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_688E)
    Sleep(20)

    def lambda_68A6():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_68A6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    Sound(288, 0, 70, 0)
    Sound(876, 0, 50, 0)
    Sleep(200)
    Sound(880, 0, 70, 0)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6998():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6998)
    Sleep(50)

    def lambda_69A8():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_69A8)
    Sleep(50)

    def lambda_69B8():
        OP_93(0x103, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_69B8)
    Sleep(50)

    def lambda_69C8():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_69C8)
    Sleep(50)

    def lambda_69D8():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_69D8)
    Sleep(50)

    def lambda_69E8():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_69E8)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00007F#5PWhat was that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#11PThat was... an\x01",
            "explosion!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11PWasn't that an\x01",
            "explosion!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#5PFrom the south! Let's\x01",
            "head there!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(20500, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrPos(0x0, -35500, 0, 1000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetScenarioFlags(0x163, 4)
    OP_29(0xA8, 0x1, 0x7)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_29_674D end

    def Function_30_6B0D(): pass

    label("Function_30_6B0D")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    OP_68(-56000, -5200, -84500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, -56000, -6000, -77000, 180)
    SetChrPos(0x102, -56800, -6000, -75800, 180)
    SetChrPos(0x103, -55250, -6000, -76300, 180)
    SetChrPos(0x104, -55950, -6000, -75050, 180)
    SetChrPos(0x109, -55000, -6000, -74450, 180)
    SetChrPos(0x105, -56500, -6000, -73700, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_6BDC():
        OP_95(0xFE, -56000, -6000, -83000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BDC)

    def lambda_6BF6():
        OP_95(0xFE, -56800, -6000, -81800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BF6)

    def lambda_6C10():
        OP_95(0xFE, -55250, -6000, -82300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C10)

    def lambda_6C2A():
        OP_95(0xFE, -55950, -6000, -81050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C2A)

    def lambda_6C44():
        OP_95(0xFE, -55000, -6000, -80450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C44)

    def lambda_6C5E():
        OP_95(0xFE, -56500, -6000, -79700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C5E)
    FadeToBright(1000, 0)
    OP_68(-56000, -5200, -82500, 3000)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    SetChrPos(0x101, -56000, -6000, -79000, 180)
    SetChrPos(0x102, -56800, -6000, -77800, 180)
    SetChrPos(0x103, -55250, -6000, -78300, 180)
    SetChrPos(0x104, -55950, -6000, -77050, 180)
    SetChrPos(0x109, -55000, -6000, -76450, 180)
    SetChrPos(0x105, -56500, -6000, -75700, 180)

    def lambda_6D9D():
        OP_95(0xFE, -56000, -6000, -91000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D9D)

    def lambda_6DB7():
        OP_95(0xFE, -56800, -6000, -89800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6DB7)

    def lambda_6DD1():
        OP_95(0xFE, -55250, -6000, -90300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6DD1)

    def lambda_6DEB():
        OP_95(0xFE, -55950, -6000, -89050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6DEB)

    def lambda_6E05():
        OP_95(0xFE, -55000, -6000, -88450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6E05)

    def lambda_6E1F():
        OP_95(0xFE, -56500, -6000, -87700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E1F)
    OP_68(-56740, 500, -88290, 0)
    MoveCamera(163, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18760, 0)
    OP_68(-57070, -800, -87550, 4000)
    MoveCamera(163, 32, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(17690, 4000)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x102,
        "#00107F#12P#NT-This is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00010F#6P#NThis gate was made of a\x01",
            "special alloy...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10106F#6P#NU-Unbelievable... To think\x01",
            "a simple monster could do\x01",
            "something like this...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00311F#6P#NConsiderin' it derailed\x01",
            "a train... It's quite\x01",
            "the monster, isn't it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-58390, -800, -83470, 0)
    MoveCamera(162, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(11800, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10303F#6P#N...Anyway, let's follow\x01",
            "it. It couldn't have\x01",
            "gone far.\x02\x03",
            "#10301FIt'd be pain if it\x01",
            "escaped into the forest,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7083():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7083)
    Sleep(50)

    def lambda_7093():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7093)
    Sleep(50)

    def lambda_70A3():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_70A3)
    Sleep(50)

    def lambda_70B3():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_70B3)
    Sleep(50)

    def lambda_70C3():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_70C3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#00001F#11PY-Yeah... (Hasn't he\x01",
            "been acting strange for\x01",
            "quite a while now?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -56000, -6000, -84500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x163, 5)
    OP_29(0xA8, 0x1, 0x8)
    ModifyEventFlags(0, 2, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_30_6B0D end

    def Function_31_7176(): pass

    label("Function_31_7176")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch03154.itc", 0x1E)
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(950)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -61160, 0, 28890, 10)
    SetChrPos(0x106, -59710, 0, 27350, 10)
    SetChrPos(0x103, -60010, 0, 28310, 10)
    SetChrPos(0x104, -60900, 0, 27820, 10)
    SetChrPos(0x107, -62090, 0, 27860, 10)
    SetChrPos(0x105, -60370, 0, 30240, 10)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrChipByIndex(0x105, 0x1E)
    SetChrSubChip(0x105, 0x0)
    BeginChrThread(0x105, 0, 0, 38)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x29, 0xE)
    OP_49()
    SetChrPos(0xE, -60450, 18000, 28100, 0)
    OP_D5(0xE, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x29, 0x4)
    OP_74(0x29, 0x1E)
    OP_71(0x29, 0x1, 0x78, 0x0, 0x20)
    OP_75(0x29, 0x1, 0x0)
    ClearChrFlags(0xF, 0x80)
    OP_78(0x2A, 0xF)
    OP_49()
    SetChrPos(0xF, -60450, 18000, 28100, 0)
    OP_D5(0xF, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x2A, 0x4)
    OP_74(0x2A, 0x1E)
    OP_71(0x2A, 0x65, 0xA0, 0x0, 0x20)
    SetMapObjFlags(0x6, 0x4)
    OP_68(-60450, 15000, 28100, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(36500, 0)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_68(-60450, 0, 28100, 10000)
    MoveCamera(15, 20, 0, 10000)
    BeginChrThread(0xE, 3, 0, 32)
    BeginChrThread(0xF, 3, 0, 33)
    OP_0D()
    StopSound(132, 1000, 100)
    Sleep(4500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xE, 0x3)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0xF, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x105, 0x8)
    OP_68(-60250, 5000, 30900, 0)
    MoveCamera(60, 40, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(27000, 0)
    FadeToBright(1000, 0)
    OP_68(-60250, 1000, 30900, 6000)
    MoveCamera(45, 36, 0, 6000)
    SetCameraDistance(20000, 6000)
    BeginChrThread(0x105, 3, 0, 39)
    BeginChrThread(0xE, 3, 0, 34)
    BeginChrThread(0xF, 3, 0, 35)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x105, 3)
    SetMapObjFlags(0x29, 0x4)
    SetChrFlags(0xE, 0x80)
    SetMapObjFlags(0x2A, 0x4)
    SetChrFlags(0xF, 0x80)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x101, -52550, 0, 19530, 135)
    SetChrPos(0x106, -53540, 0, 20610, 135)
    SetChrPos(0x103, -54530, 0, 19160, 135)
    SetChrPos(0x104, -55090, 0, 20060, 135)
    SetChrPos(0x107, -55500, 0, 21740, 135)
    SetChrPos(0x105, -56410, 0, 20640, 135)
    OP_68(-50660, 1000, 16690, 0)
    MoveCamera(90, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13500, 3000)

    def lambda_74CE():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_74CE)
    Sleep(50)

    def lambda_74E6():
        OP_9B(0x0, 0x106, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_74E6)
    Sleep(50)

    def lambda_74FE():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_74FE)
    Sleep(50)

    def lambda_7516():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7516)
    Sleep(50)

    def lambda_752E():
        OP_9B(0x0, 0x107, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_752E)
    Sleep(50)

    def lambda_7546():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7546)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00301F#6PIf we go west, we'd reach Bellguard\x01",
            "Gate immediately, but...\x02\x03",
            "#00306FIf Commander Sonya is there, you can\x01",
            "imagine that I wouldn't have the\x01",
            "nerve to come face to face with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#6P...Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#6PAnyhow, all we can do is\x01",
            "search where we can.\x02\x03",
            "#10401FThough if a State Guard\x01",
            "armored car comes, we'll\x01",
            "need to take cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10703F#6PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6P(Commander Sonya,\x01",
            "huh...?)\x02\x03",
            "#00001F(...I'd like to contact\x01",
            "her somehow, but...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x2B, 0x4)
    SetMapObjFlags(0x2C, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, -48700, 0, 15700, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 0)
    OP_29(0xAF, 0x1, 0xE)
    OP_24(0x84)
    OP_24(0x1F1)
    OP_24(0x3B6)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_31_7176 end

    def Function_32_77A9(): pass

    label("Function_32_77A9")

    BeginChrThread(0xFE, 0, 0, 36)
    OP_96(0xFE, 0xFFFF13DE, 0xBB8, 0x6DC4, 0x7D0, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_32_77A9 end

    def Function_33_77C8(): pass

    label("Function_33_77C8")


    def lambda_77CD():
        OP_96(0xFE, 0xFFFF13DE, 0xBB8, 0x6DC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77CD)
    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_74(0x2A, 0x1E)
    OP_71(0x2A, 0x0, 0x32, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 1000, 40)
    Sleep(1000)
    OP_75(0x29, 0x2, 0x0)
    OP_79(0x2A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_77C8 end

    def Function_34_7828(): pass

    label("Function_34_7828")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_75(0x29, 0x2, 0x0)
    SetChrPos(0xFE, -60450, 6000, 28100, 0)
    OP_96(0xFE, 0xFFFF13DE, 0x4650, 0x6DC4, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_34_7828 end

    def Function_35_785F(): pass

    label("Function_35_785F")

    SetChrPos(0xFE, -60450, 6000, 28100, 0)

    def lambda_7875():
        OP_96(0xFE, 0xFFFF13DE, 0x4650, 0x6DC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7875)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_74(0x2A, 0x1E)
    OP_71(0x2A, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 1000, 40)
    OP_75(0x29, 0x1, 0x0)
    OP_79(0x2A)
    OP_71(0x2A, 0x65, 0xA0, 0x0, 0x20)
    StopSound(497, 4000, 90)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_35_785F end

    def Function_36_78DF(): pass

    label("Function_36_78DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7903")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_36_78DF")

    label("loc_7903")

    Return()

    # Function_36_78DF end

    def Function_37_7904(): pass

    label("Function_37_7904")

    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x28, 0x28, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x1E, 0x1E, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x14, 0x14, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0xA, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_37_7904 end

    def Function_38_7969(): pass

    label("Function_38_7969")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7983")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_38_7969")

    label("loc_7983")

    Return()

    # Function_38_7969 end

    def Function_39_7984(): pass

    label("Function_39_7984")

    Sleep(1500)
    ClearMapObjFlags(0x2B, 0x4)
    SetMapObjFrame(0x2B, "Null_fream", 0x2, "start")
    Sleep(1500)
    EndChrThread(0x105, 0x0)
    Sound(935, 0, 60, 0)
    SetChrSubChip(0x105, 0x3)
    Sleep(100)
    SetChrSubChip(0x105, 0x4)
    ClearMapObjFlags(0x2C, 0x4)
    SetMapObjFrame(0x2C, "Null_fream", 0x2, "start")
    Sleep(2000)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Return()

    # Function_39_7984 end

    def Function_40_79DF(): pass

    label("Function_40_79DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x5, 0xC)
    OP_49()
    SetChrPos(0xC, -85890, 2000, 73990, 90)
    OP_D5(0xC, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0xD, 0x80)
    ClearMapObjFlags(0x28, 0x4)
    OP_78(0x28, 0xD)
    SetMapObjFrame(0x28, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xD, -85890, 2000, 73990, 90)
    OP_D5(0xD, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x28, 0x1000)
    OP_74(0x28, 0x1E)
    OP_71(0x28, 0xB5, 0xF0, 0x1, 0x20)
    LoadEffect(0x6, "event\\eva04_00.eff")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x103, 0x80)
    OP_E2(0x3)
    OP_68(-68470, 2600, 62700, 0)
    MoveCamera(82, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(28350, 0)
    OP_68(-66340, 2600, 57390, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(457, 0, 100, 0)
    Sound(493, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 43)
    Sleep(2000)
    BeginChrThread(0xC, 1, 0, 42)
    Sleep(1000)
    Sound(494, 0, 100, 0)
    Sleep(2000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    OP_68(-29120, 2100, 39710, 0)
    MoveCamera(32, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(33680, 0)
    SetChrPos(0xC, -43110, 0, 54200, 90)
    SetChrPos(0xD, -43110, 0, 54200, 0)
    SetCameraDistance(35680, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(486, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 45)
    Sleep(1500)
    BeginChrThread(0xC, 1, 0, 44)
    Sound(493, 0, 100, 0)

    NpcTalk(
        0xD,
        "Sykes",
        (
            "#6A#40WThe heck are these\x01",
            "guys!?\x02",
        )
    )

    Sleep(1000)
    OP_68(-48380, 2100, 2970, 4000)
    MoveCamera(32, 26, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(30590, 4000)
    Sound(458, 0, 100, 0)

    NpcTalk(
        0xD,
        "Yuri",
        "#6A#40WHaha, let's scare 'em!\x02",
    )

    Sleep(1500)
    Sound(486, 0, 100, 0)
    Sleep(2500)
    Sound(487, 0, 100, 0)
    WaitChrThread(0xD, 1)
    BeginChrThread(0xD, 3, 0, 41)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(500)
    WaitChrThread(0xC, 1)
    OP_71(0x5, 0xB5, 0xB5, 0x0, 0x0)
    OP_71(0x28, 0xB5, 0xB5, 0x0, 0x0)
    FadeToDark(300, 0, 100)

    NpcTalk(
        0xC,
        "Lloyd",
        (
            "#00010F(They're trying to bump\x01",
            "us!!)\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KEmergency Navigation\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Hit the emergency brakes\x01",      # 0
            "Go off-course and dodge\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F37")
    OP_2C(0x8B, 0x1)
    SetScenarioFlags(0x178, 2)

    NpcTalk(
        0xC,
        "Lloyd",
        (
            "#00007FNoｱl, the emergency\x01",
            "brakes!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Noｱl",
        "#10107FRight!\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_0D()
    Sound(487, 0, 100, 0)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    OP_71(0x28, 0xB5, 0xF0, 0x1, 0x20)
    OP_68(-41710, 600, 4300, 2000)
    BeginChrThread(0xC, 1, 0, 46)
    WaitChrThread(0xC, 1)
    Sound(494, 0, 100, 0)
    Sound(493, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 48)
    OP_0D()
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)

    NpcTalk(
        0xD,
        "Reggie",
        "#8A#30WKiiidding!\x02",
    )

    Sleep(1200)

    NpcTalk(
        0xC,
        "Elie",
        "#00105FEeh...!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Randy",
        (
            "#00303FTch... What reckless\x01",
            "guys.\x02\x03",
            "#00300FStill, at this rate\x01",
            "we'll be able to catch\x01",
            "'em soon, right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Lloyd",
        (
            "#00000FYeah! Noｱl, keep at it\x01",
            "and pursue them!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Noｱl",
        "#10101FRoger!\x02",
    )

    CloseMessageWindow()
    Sound(494, 0, 100, 0)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    BeginChrThread(0xC, 1, 0, 48)
    OP_29(0x8B, 0x1, 0x2)
    Sleep(3000)
    Jump("loc_8127")

    label("loc_7F37")


    NpcTalk(
        0xC,
        "Lloyd",
        (
            "#00007FLet's go off course for\x01",
            "now!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Noｱl",
        "#10105FR-Right!\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_0D()
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    OP_68(-53830, 2100, -2640, 2000)
    Sound(494, 0, 100, 0)
    Sound(493, 0, 100, 0)
    BeginChrThread(0xC, 1, 0, 47)
    OP_71(0x28, 0xB5, 0xF0, 0x1, 0x20)
    BeginChrThread(0xD, 1, 0, 48)

    NpcTalk(
        0xD,
        "Sykes",
        "#8A#30WKiiidding!\x02",
    )

    Sleep(1200)
    Sound(492, 0, 100, 0)
    WaitChrThread(0xC, 1)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)

    NpcTalk(
        0xC,
        "Elie",
        "#00105FEeh...!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Randy",
        (
            "#00303FTch... What reckless\x01",
            "guys.\x02\x03",
            "#00308FWe could've avoided em\x01",
            "just usin' the breaks,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Lloyd",
        (
            "#00006F(Getting off course was\x01",
            "a mistake...)\x02\x03",
            "#00001F─Sorry, Noｱl! Let's\x01",
            "chase them once more!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Noｱl",
        "#10101FRoger!\x02",
    )

    CloseMessageWindow()
    OP_68(-48380, 2100, 2970, 2000)
    BeginChrThread(0xC, 1, 0, 49)
    OP_29(0x8B, 0x1, 0x3)
    Sleep(4000)

    label("loc_8127")

    SetScenarioFlags(0x22, 2)
    NewScene("r1020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_79DF end

    def Function_41_8134(): pass

    label("Function_41_8134")

    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -45630, 0, 13920, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -47650, 0, 1320, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_41_8134 end

    def Function_42_81A6(): pass

    label("Function_42_81A6")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -85890, 2000, 73990)
    OP_9F(0x1, -65760, 2000, 55290)
    OP_9F(0x1, -54460, 2000, 54530)
    OP_9F(0x1, -45720, 0, 54180)
    OP_9F(0x1, -34680, 0, 52700)
    OP_9F(0x1, -28120, 0, 46140)
    OP_9F(0x2, 0xC, 12000, 0x6)
    Return()

    # Function_42_81A6 end

    def Function_43_8208(): pass

    label("Function_43_8208")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, -85890, 2000, 73990)
    OP_9F(0x1, -65760, 2000, 55290)
    OP_9F(0x1, -54460, 2000, 54530)
    OP_9F(0x1, -45720, 0, 54180)
    OP_9F(0x1, -34680, 0, 52700)
    OP_9F(0x1, -28120, 0, 46140)
    OP_9F(0x2, 0xD, 11000, 0x6)
    Return()

    # Function_43_8208 end

    def Function_44_826A(): pass

    label("Function_44_826A")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -43110, 0, 54200)
    OP_9F(0x1, -32830, 0, 51030)
    OP_9F(0x1, -24400, 0, 40770)
    OP_9F(0x1, -27180, 0, 30110)
    OP_9F(0x1, -37110, 0, 22440)
    OP_9F(0x1, -45630, 0, 13920)
    OP_9F(0x1, -46520, 0, 9080)
    OP_9F(0x2, 0xC, 12000, 0x6)
    Return()

    # Function_44_826A end

    def Function_45_82DA(): pass

    label("Function_45_82DA")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, -43110, 0, 54200)
    OP_9F(0x1, -32830, 0, 51030)
    OP_9F(0x1, -24400, 0, 40770)
    OP_9F(0x1, -27180, 0, 30110)
    OP_9F(0x1, -37110, 0, 22440)
    OP_9F(0x1, -45630, 0, 13920)
    OP_9F(0x2, 0xD, 11000, 0x6)
    OP_9F(0x0, 0xD)
    OP_9F(0x1, -47650, 0, 1320)
    OP_9F(0x1, -46440, 0, 1320)
    OP_9F(0x2, 0xD, 15000, 0x6)
    OP_9B(0x1, 0xD, 0x5A, 0x3E8, 0x2710, 0x0)
    Return()

    # Function_45_82DA end

    def Function_46_8374(): pass

    label("Function_46_8374")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -46520, 0, 9080)
    OP_9F(0x1, -46890, 0, 7430)
    OP_9F(0x1, -46230, 0, 5680)
    OP_9F(0x2, 0xC, 12000, 0x6)
    Return()

    # Function_46_8374 end

    def Function_47_83AC(): pass

    label("Function_47_83AC")

    OP_9F(0x0, 0xC)
    OP_9F(0x1, -46520, 0, 9080)
    OP_9F(0x1, -49690, 0, 3690)
    OP_9F(0x1, -52720, 0, 250)
    OP_9F(0x1, -56430, 0, -3730)
    OP_9F(0x2, 0xC, 15000, 0x6)
    Return()

    # Function_47_83AC end

    def Function_48_83F2(): pass

    label("Function_48_83F2")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -41760, 0, 1800)
    OP_9F(0x1, -26570, 0, 2310)
    OP_9F(0x1, -20250, 0, 7670)
    OP_9F(0x2, 0xFE, 12000, 0x6)
    Return()

    # Function_48_83F2 end

    def Function_49_842A(): pass

    label("Function_49_842A")

    Sound(493, 0, 100, 0)
    OP_9B(0x1, 0xC, 0xB4, 0x2710, 0x2710, 0x0)
    OP_9E(0xFE, 0xFFFF277A, 0x1856, 0xFFFFC568, 0x2710, 0x4)
    OP_9B(0x1, 0xC, 0xB4, 0x7D0, 0x2710, 0x0)
    Sleep(300)
    Sound(494, 0, 100, 0)
    OP_9F(0x0, 0xC)
    OP_9F(0x1, -41760, 0, 1800)
    OP_9F(0x1, -26570, 0, 2310)
    OP_9F(0x1, -20250, 0, 7670)
    OP_9F(0x2, 0xC, 12000, 0x6)
    Return()

    # Function_49_842A end

    def Function_50_84A4(): pass

    label("Function_50_84A4")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "To think that I'd\x01",
            "lose... You're good,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Then, I'll present proof\x01",
            "that you've defeated I,\x01",
            "the Silver Orca.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00012FT-Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Then, with this, the club\x01",
            "will acknowledge you as\x01",
            "the "Silver Orca Eater".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To put it bluntly, it's\x01",
            "a lame title, but, well,\x01",
            "forgive us for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FD-Don't worry about it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C0, 3)
    SetChrPos(0xA, -57240, 0, 32830, 90)
    OP_66(0x6, 0x1)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, -59650, 0, 32659, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_50_84A4 end

    def Function_51_8692(): pass

    label("Function_51_8692")


    ChrTalk(
        0xA,
        (
            "I see, it ends here\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, maybe you were just\x01",
            "unlucky this time. Feel free to\x01",
            "challenge me again whenever.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_51_8692 end

    def Function_52_870E(): pass

    label("Function_52_870E")


    ChrTalk(
        0xA,
        (
            "Giving up, huh...? Well,\x01",
            "whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Then, see you next time.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_52_870E end

    def Function_53_8755(): pass

    label("Function_53_8755")


    ChrTalk(
        0xA,
        (
            "Haha. You're pretty good\x01",
            "if you drew with me,\x01",
            "y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, well. We'll settle\x01",
            "the score in our next\x01",
            "match.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_53_8755 end

    def Function_54_87CA(): pass

    label("Function_54_87CA")

    EventBegin(0x1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8854")

    ChrTalk(
        0x101,
        (
            "#00000FBellguard Gate is this way,\x01",
            "right?\x02\x03",
            "Let's avoid any unnecessary\x01",
            "detours until we get to the\x01",
            "police academy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88AB")

    ChrTalk(
        0x101,
        (
            "#00001FThe voice didn't come\x01",
            "from this direction.\x01",
            "Let's head south.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88AB")

    OP_5A()
    SetChrPos(0x0, -37940, 0, 20690, 225)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_54_87CA end

    def Function_55_88C2(): pass

    label("Function_55_88C2")

    EventBegin(0x1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_891D")

    ChrTalk(
        0x101,
        (
            "#00001FThe voice didn't come\x01",
            "from this direction.\x01",
            "Let's head south.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_891D")

    OP_5A()
    SetChrPos(0x0, -53410, 0, 18420, 143)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_55_88C2 end

    def Function_56_8934(): pass

    label("Function_56_8934")

    EventBegin(0x1)
    OP_E2(0x3)

    ChrTalk(
        0x101,
        (
            "#00001FThe Bellguard Gate area\x01",
            "is this way, huh...?\x02\x03",
            "It'll be dangerous if we\x01",
            "get any closer. Let's\x01",
            "quietly withdraw.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -70920, 2000, 59620, 135)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_56_8934 end

    def Function_57_89CA(): pass

    label("Function_57_89CA")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "C.  P.  A.  Crossbell\x01",
            "Police Academy\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_57_89CA end

    def Function_58_8A2A(): pass

    label("Function_58_8A2A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "East - Crossbell City   137 selge\x01",
            "North - Bellguard Gate   61 selge\x01",
            "South - C. P. A.  31 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_58_8A2A end

    SaveToFile()

Try(main)
