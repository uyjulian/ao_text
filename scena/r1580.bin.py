from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1580.bin",                # FileName
        "r1580",                    # MapName
        "r1580",                    # Location
        0x0060,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r1580", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x0B,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 96, 0, 5, 0, 6],
    )

    BuildStringList((
        "r1580",                  # 0
        "スタービートル",         # 1
        "スタービートル",         # 2
        "ゴーディ・オッサー",     # 3
        "ゴーディ・オッサー",     # 4
        "ゴーディ・オッサー",     # 5
        "Cryptid",                # 6
        "Driver",                 # 7
        "送迎用リムジン",         # 8
        "ゴーディアン",           # 9
        "ゴーディアン",           # 10
        "バブーンモンチ",         # 11
        "アーミーパイナポゥ",     # 12
        "偽きのこ１",             # 13
        "偽きのこ２",             # 14
        "偽きのこ３",             # 15
        "偽きのこ４",             # 16
        "偽きのこ５",             # 17
        "アルマ茸",               # 18
        "SE制御",                 # 19
        "br1510",                 # 20
        "br1510",                 # 21
        "br1510",                 # 22
        "br1510",                 # 23
        "br1510",                 # 24
        "br1510",                 # 25
        "br1510",                 # 26
        "br1510",                 # 27
        "br1510",                 # 28
        "br1510",                 # 29
        "br1510",                 # 30
        "br1510",                 # 31
        "To St. Ursula Byroad",   # 32
        "To Tower of Stargaze",   # 33
    ))

    ATBonus("ATBonus_828", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_848", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_5240", 0,   1,   1,   9,   5,   3,   4)
    Sepith("Sepith_5248", 0,   0,   6,   10,  1,   2,   5)
    Sepith("Sepith_5258", 6,   6,   0,   9,   0,   2,   1)
    Sepith("Sepith_5250", 0,   8,   2,   3,   3,   7,   1)
    Sepith("Sepith_5260", 8,   0,   12,  0,   4,   2,   4)
    Sepith("Sepith_5270", 9,   7,   18,  6,   7,   6,   3)

    MonsterBattlePostion("MonsterBattlePostion_888", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_88C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_890", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_894", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_898", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_89C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_8EC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_8F0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_8F4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_8F8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_8FC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_900", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_904", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_868", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_86C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_870", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_874", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_878", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_87C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_880", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_884", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_928", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_92C", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_930", 3, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_934", 13, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_938", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_93C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_940", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_944", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_908", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_90C", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_910", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_914", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_918", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_91C", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_920", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_924", 0, 0, 180)

    # monster count: 16

    BattleInfo(
        "BattleInfo_98C", 0x0000, 58, 6, 60, 8, 1, 45, 0, "br1510", "Sepith_5240", 30, 40, 20, 10,
        (
            ("ms65600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms65600.dat", "ms65600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms65600.dat", "ms72700.dat", "ms65600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms65600.dat", "ms65600.dat", "ms72700.dat", "ms65600.dat", 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
        )
    )

    BattleInfo(
        "BattleInfo_A54", 0x0000, 58, 6, 60, 8, 1, 40, 0, "br1510", "Sepith_5248", 30, 40, 20, 10,
        (
            ("ms72300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72300.dat", "ms72300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72300.dat", "ms72700.dat", "ms72300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72300.dat", "ms72300.dat", "ms72700.dat", "ms72300.dat", 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
        )
    )

    BattleInfo(
        "BattleInfo_B1C", 0x0000, 58, 6, 60, 8, 1, 25, 0, "br1510", "Sepith_5258", 30, 40, 20, 10,
        (
            ("ms72700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72700.dat", "ms72700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72700.dat", "ms62400.dat", "ms72700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72700.dat", "ms72700.dat", "ms62400.dat", "ms72700.dat", 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
        )
    )

    BattleInfo(
        "BattleInfo_BE4", 0x0000, 58, 6, 60, 8, 1, 40, 0, "br1510", "Sepith_5250", 30, 40, 20, 10,
        (
            ("ms62400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms62400.dat", "ms62400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms62400.dat", "ms62400.dat", "ms62400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms62400.dat", "ms62400.dat", "ms62400.dat", "ms62400.dat", 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
        )
    )

    BattleInfo(
        "BattleInfo_948", 0x0000, 58, 6, 60, 8, 1, 30, 0, "br1510", "Sepith_5260", 100, 0, 0, 0,
        (
            ("ms68500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_CAC", 0x0000, 81, 6, 45, 6, 1, 40, 0, "br1510", "Sepith_5270", 40, 35, 25, 0,
        (
            ("ms70201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E14", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62300.dat", "ms62300.dat", "ms62300.dat", "ms62300.dat", "ms62300.dat", "ms62300.dat", 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7451", "ed7453", "ATBonus_848"),
            (),
            (),
            (),
        )
    )

    # event battle count: 8

    BattleInfo(
        "BattleInfo_DD0", 0x0000, 25, 6, 0, 0, 1, 0, 0, "br1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70200.dat", "ms70200.dat", "ms70200.dat", "ms70200.dat", 0, 0, 0, 0, "MonsterBattlePostion_928", "MonsterBattlePostion_8E8", "ed7451", "ed7453", "ATBonus_848"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D48", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72300.dat", "ms72300.dat", "ms72300.dat", "ms72300.dat", "ms72300.dat", "ms72300.dat", "ms72300.dat", "ms72300.dat", "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7453", "ed7453", "ATBonus_828"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D8C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7453", "ed7453", "ATBonus_828"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E9C", 0x0002, 255, 6, 45, 3, 3, 30, 0, "br1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68500.dat", "ms68500.dat", "ms68500.dat", "ms65600.dat", "ms65600.dat", "ms65600.dat", "ms72700.dat", "ms72700.dat", "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7451", "ed7453", "ATBonus_848"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E58", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88702.dat", "ms88802.dat", "ms88802.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_908", "MonsterBattlePostion_908", "ed7454", "ed7453", "ATBonus_848"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "apl/ch51090.itc",                   # 01
        "chr/ch00000.itc",                   # 02
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
        "monster/ch68550.itc",               # 10
        "monster/ch68551.itc",               # 11
        "monster/ch65650.itc",               # 12
        "monster/ch65651.itc",               # 13
        "monster/ch72350.itc",               # 14
        "monster/ch72351.itc",               # 15
        "monster/ch72750.itc",               # 16
        "monster/ch72750.itc",               # 17
        "monster/ch62450.itc",               # 18
        "monster/ch62450.itc",               # 19
        "monster/ch70250.itc",               # 1A
        "monster/ch70251.itc",               # 1B
        "monster/ch62350.itc",               # 1C
        "monster/ch62350.itc",               # 1D
    ))

    DeclNpc(4294910986, 4294964296, 4294963967, 270,  484,  0x0, 0,   20,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(4294826886, 4294958296, 4294901576, 270,  484,  0x0, 0,   20,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(4294910986, 4294964296, 4294963967, 270,  484,  0x0, 0,   26,  0,   0,   3,   255, 255, 255,  0)
    DeclNpc(4294826886, 4294958296, 4294901576, 270,  484,  0x0, 0,   26,  0,   0,   3,   255, 255, 255,  0)
    DeclNpc(10020,   4294962546, 4294954347, 180,  484,  0x0, 0,   26,  0,   0,   4,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294962427, 4294964296, 9930,    180,  389,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294881366, 4294964296, 8229,    0,    389,  0x0, 8,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294916017, 4294961296, 4294931686, 0,    389,  0x0, 8,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294966907, 4294961296, 4294953137, 0,    389,  0x0, 8,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4860,    4294961296, 4294908206, 0,    389,  0x0, 8,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294884106, 4294961296, 4294904056, 0,    389,  0x0, 8,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294827386, 4294958296, 4294909677, 0,    389,  0x0, 8,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294943406, 14070,   4294964296, 0x1010000,    "BattleInfo_98C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294890516, 7060,    4294964296, 0x1010000,    "BattleInfo_A54", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294877596, 4294958916, 4294964296, 0x1010000,    "BattleInfo_B1C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294905756, 4294960426, 4294964296, 0x1010000,    "BattleInfo_BE4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294903616, 4294924376, 4294961296, 0x1010000,    "BattleInfo_948", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294902616, 4294925376, 4294961296, 0x1010000,    "BattleInfo_98C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294940856, 4294926506, 4294961306, 0x1010000,    "BattleInfo_A54", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294952116, 4294948216, 4294961296, 0x1010000,    "BattleInfo_948", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(5510,    4294951266, 4294961306, 0x1010000,    "BattleInfo_B1C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294959926, 4294910406, 4294961306, 0x1010000,    "BattleInfo_BE4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294908956, 4294900226, 4294961306, 0x1010000,    "BattleInfo_98C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294873956, 4294903676, 4294961296, 0x1010000,    "BattleInfo_948", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294825916, 4294903946, 4294958296, 0x1010000,    "BattleInfo_B1C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294934537, 3490,    4294964296, 0x1010000,    "BattleInfo_CAC", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294934256, 4294903326, 4294961296, 0x1010000,    "BattleInfo_CAC", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294885776, 4294962836, 4294964296, 0x185010E,    "BattleInfo_E14", 0,   28,  0xFFFF, 12, 13)

    DeclEvent(0x0040, 0, 16,  -81.5199966430664,     -4.460000038146973,    -4.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   10.1899995803833,      0.5575000047683716,    1.0,                   1.0])
    DeclEvent(0x0040, 0, 47,  -22.260000228881836,   14.40999984741211,     -4.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   2.7825000286102295,    -1.8012499809265137,   1.0,                   1.0])
    DeclEvent(0x0000, 0, 48,  -132.42999267578125,   -40.720001220703125,   -9.970000267028809,    324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   11.035833358764648,    13.573333740234375,    1.9940000772476196,    1.0])

    DeclActor(10020,   4294961296, 4294954346, 1200,    10020,   4294962296, 4294954346, 0x007C, 0,  7,  0x0000)
    DeclActor(4294963277, 4294961296, 4294904556, 1200,    4294963277, 4294962296, 4294904556, 0x007C, 0,  8,  0x0000)
    DeclActor(4294904066, 4294961296, 4294921466, 1200,    4294904066, 4294962296, 4294921466, 0x007C, 0,  9,  0x0000)
    DeclActor(4294876146, 4294964296, 4294957526, 1200,    4294876146, 4294965296, 4294957526, 0x007C, 0,  10, 0x0000)
    DeclActor(4294910986, 4294964296, 4294963966, 1200,    4294910986, 4294964296, 4294963966, 0x007C, 0,  11, 0x0000)
    DeclActor(4294826886, 4294958296, 4294901576, 1200,    4294826886, 4294958296, 4294901576, 0x007C, 0,  12, 0x0000)
    DeclActor(4294881366, 4294964296, 8230,    1200,    4294881366, 4294965296, 8230,    0x007C, 0,  40, 0x0000)
    DeclActor(4294916016, 4294961296, 4294931686, 1200,    4294916016, 4294962296, 4294931686, 0x007C, 0,  41, 0x0000)
    DeclActor(4294966906, 4294961296, 4294953136, 1200,    4294966906, 4294962296, 4294953136, 0x007C, 0,  42, 0x0000)
    DeclActor(4860,    4294961296, 4294908206, 1200,    4860,    4294962296, 4294908206, 0x007C, 0,  43, 0x0000)
    DeclActor(4294884106, 4294961296, 4294904056, 1200,    4294884106, 4294962296, 4294904056, 0x007C, 0,  44, 0x0000)
    DeclActor(4294827386, 4294958296, 4294909676, 1200,    4294827386, 4294959296, 4294909676, 0x007C, 0,  27, 0x0000)

    PlaceName(35.220001220703125, 0.0, 7.400000095367432, 0x0000, 0x0000, "To St. Ursula Byroad")
    PlaceName(-128.0, 0.0, -20.0, 0x0000, 0x0000, "To Tower of Stargaze")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 11
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 12
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 13

    ScpFunction((
        "Function_0_104C",         # 00, 0
        "Function_1_1104",         # 01, 1
        "Function_2_11BC",         # 02, 2
        "Function_3_11DB",         # 03, 3
        "Function_4_11FA",         # 04, 4
        "Function_5_1219",         # 05, 5
        "Function_6_124D",         # 06, 6
        "Function_7_1DEB",         # 07, 7
        "Function_8_20AC",         # 08, 8
        "Function_9_21FD",         # 09, 9
        "Function_10_234E",        # 0A, 10
        "Function_11_249F",        # 0B, 11
        "Function_12_27FB",        # 0C, 12
        "Function_13_2B57",        # 0D, 13
        "Function_14_2B7A",        # 0E, 14
        "Function_15_2B7E",        # 0F, 15
        "Function_16_2D1A",        # 10, 16
        "Function_17_31B1",        # 11, 17
        "Function_18_37D2",        # 12, 18
        "Function_19_38A7",        # 13, 19
        "Function_20_38F2",        # 14, 20
        "Function_21_393D",        # 15, 21
        "Function_22_3988",        # 16, 22
        "Function_23_39D3",        # 17, 23
        "Function_24_3A1E",        # 18, 24
        "Function_25_3A58",        # 19, 25
        "Function_26_3AA3",        # 1A, 26
        "Function_27_3ABC",        # 1B, 27
        "Function_28_3B0C",        # 1C, 28
        "Function_29_4252",        # 1D, 29
        "Function_30_4271",        # 1E, 30
        "Function_31_4290",        # 1F, 31
        "Function_32_42AF",        # 20, 32
        "Function_33_42CE",        # 21, 33
        "Function_34_42ED",        # 22, 34
        "Function_35_430C",        # 23, 35
        "Function_36_4353",        # 24, 36
        "Function_37_439A",        # 25, 37
        "Function_38_43CB",        # 26, 38
        "Function_39_43FC",        # 27, 39
        "Function_40_4872",        # 28, 40
        "Function_41_499C",        # 29, 41
        "Function_42_4AB2",        # 2A, 42
        "Function_43_4BEB",        # 2B, 43
        "Function_44_4D17",        # 2C, 44
        "Function_45_4E58",        # 2D, 45
        "Function_46_4F09",        # 2E, 46
        "Function_47_4FD1",        # 2F, 47
        "Function_48_504D",        # 30, 48
    ))


    def Function_0_104C(): pass

    label("Function_0_104C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_108C"),
        (1, "loc_1098"),
        (2, "loc_10A4"),
        (3, "loc_10B0"),
        (4, "loc_10BC"),
        (5, "loc_10C8"),
        (6, "loc_10D4"),
        (SWITCH_DEFAULT, "loc_10E0"),
    )


    label("loc_108C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_10EC")

    label("loc_1098")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_10EC")

    label("loc_10A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_10EC")

    label("loc_10B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_10EC")

    label("loc_10BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_10EC")

    label("loc_10C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_10EC")

    label("loc_10D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10EC")

    label("loc_10E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10EC")

    label("loc_10EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1103")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_10EC")

    label("loc_1103")

    Return()

    # Function_0_104C end

    def Function_1_1104(): pass

    label("Function_1_1104")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1144"),
        (1, "loc_1150"),
        (2, "loc_115C"),
        (3, "loc_1168"),
        (4, "loc_1174"),
        (5, "loc_1180"),
        (6, "loc_118C"),
        (SWITCH_DEFAULT, "loc_1198"),
    )


    label("loc_1144")

    OP_A0(0xFE, 450, 0x0, 0xFB)
    Jump("loc_11A4")

    label("loc_1150")

    OP_A0(0xFE, 550, 0x0, 0xFB)
    Jump("loc_11A4")

    label("loc_115C")

    OP_A0(0xFE, 600, 0x0, 0xFB)
    Jump("loc_11A4")

    label("loc_1168")

    OP_A0(0xFE, 400, 0x0, 0xFB)
    Jump("loc_11A4")

    label("loc_1174")

    OP_A0(0xFE, 650, 0x0, 0xFB)
    Jump("loc_11A4")

    label("loc_1180")

    OP_A0(0xFE, 350, 0x0, 0xFB)
    Jump("loc_11A4")

    label("loc_118C")

    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_11A4")

    label("loc_1198")

    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_11A4")

    label("loc_11A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11BB")
    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_11A4")

    label("loc_11BB")

    Return()

    # Function_1_1104 end

    def Function_2_11BC(): pass

    label("Function_2_11BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11DA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_11BC")

    label("loc_11DA")

    Return()

    # Function_2_11BC end

    def Function_3_11DB(): pass

    label("Function_3_11DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11F9")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_3_11DB")

    label("loc_11F9")

    Return()

    # Function_3_11DB end

    def Function_4_11FA(): pass

    label("Function_4_11FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1218")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_4_11FA")

    label("loc_1218")

    Return()

    # Function_4_11FA end

    def Function_5_1219(): pass

    label("Function_5_1219")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_123A")
    ClearChrFlags(0xE, 0x80)

    label("loc_123A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1249")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)

    label("loc_1249")

    Call(0, 13)
    Return()

    # Function_5_1219 end

    def Function_6_124D(): pass

    label("Function_6_124D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_125F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_125F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1286")
    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_12EF")

    label("loc_1286")

    OP_78(0x4, 0xD)
    ClearMapObjFlags(0x4, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x1)
    SetChrPos(0xD, -22260, -3000, 14410, 180)
    OP_93(0xD, 0x0, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, -22260, -4000, 14410, 3000, 3000, 90000)

    label("loc_12EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1316")
    ClearChrFlags(0x2A, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x2A, 0x8000)

    label("loc_1316")

    Jump("loc_1325")

    label("loc_131B")

    SetChrFlags(0x2A, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_1325")

    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x2A, 0x100)
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B54")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1B7B")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_1B7B")

    label("loc_1B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BA1")
    OP_1B(0x0, 0x0, 0x2D)
    OP_1B(0x1, 0x0, 0x2E)

    label("loc_1BA1")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BB9")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1BB9")

    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CB5")
    OP_66(0xB, 0x1)
    OP_66(0x6, 0x1)
    OP_66(0x7, 0x1)
    OP_66(0x8, 0x1)
    OP_66(0x9, 0x1)
    OP_66(0xA, 0x1)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrFlags(0x17, 0x2)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x19, 0x2)
    ClearMapObjFlags(0x9, 0x2000000)
    OP_78(0x9, 0xF)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3710, -3000, 12490, 270)
    OP_D5(0xF, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_1CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC8")
    OP_70(0x0, 0x0)
    Jump("loc_1CCC")

    label("loc_1CC8")

    OP_70(0x0, 0x1E)

    label("loc_1CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CDF")
    OP_70(0x1, 0x0)
    Jump("loc_1CE3")

    label("loc_1CDF")

    OP_70(0x1, 0x1E)

    label("loc_1CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF6")
    OP_70(0x2, 0x0)
    Jump("loc_1CFA")

    label("loc_1CF6")

    OP_70(0x2, 0x1E)

    label("loc_1CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0D")
    OP_70(0x3, 0x0)
    Jump("loc_1D11")

    label("loc_1D0D")

    OP_70(0x3, 0x1E)

    label("loc_1D11")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D72")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -56310, -3000, -3330, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1D72")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DBE")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -140410, -9000, -65720, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_1DBE")

    OP_1C(0x0, 0x5, 0x0, 0x32, 0x0, 0xE, 0x0, 0x0)
    OP_1C(0x0, 0x6, 0x0, 0x32, 0x0, 0xE, 0x0, 0x0)
    OP_1C(0x0, 0x7, 0x0, 0x32, 0x0, 0xE, 0x0, 0x0)
    OP_1C(0x0, 0x8, 0x0, 0x32, 0x0, 0xE, 0x0, 0x0)
    Return()

    # Function_6_124D end

    def Function_7_1DEB(): pass

    label("Function_7_1DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E91")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You sense the presence of powerful monsters.\x01",
            "[Estimated Monster Level: 82]\x01",
            "Open the chest?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E91")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_1E91")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2062")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F94")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1EEE():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1EEE)

    def lambda_1F08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1F08)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_DD0", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1F75"),
        (2, "loc_1F84"),
        (1, "loc_1F91"),
        (SWITCH_DEFAULT, "loc_1F94"),
    )


    label("loc_1F75")

    SetScenarioFlags(0x214, 2)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_1F94")

    label("loc_1F84")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1F91")

    OP_B9(0x0)
    Return()

    label("loc_1F94")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA7, 1)"), scpexpr(EXPR_END)), "loc_1FED")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_205D")

    label("loc_1FED")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
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

    label("loc_205D")

    Jump("loc_20A0")

    label("loc_2062")

    FadeToDark(300, 0, 100)

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

    label("loc_20A0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1DEB end

    def Function_8_20AC(): pass

    label("Function_8_20AC")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A8")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x334, 1)"), scpexpr(EXPR_END)), "loc_2131")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_21A3")

    label("loc_2131")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
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

    label("loc_21A3")

    Jump("loc_21F1")

    label("loc_21A8")

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

    label("loc_21F1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_20AC end

    def Function_9_21FD(): pass

    label("Function_9_21FD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F9")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_2282")
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
    SetScenarioFlags(0x1ED, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_22F4")

    label("loc_2282")

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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_22F4")

    Jump("loc_2342")

    label("loc_22F9")

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

    label("loc_2342")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_21FD end

    def Function_10_234E(): pass

    label("Function_10_234E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244A")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1AD, 1)"), scpexpr(EXPR_END)), "loc_23D3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_2445")

    label("loc_23D3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AD),
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
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2445")

    Jump("loc_2493")

    label("loc_244A")

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

    label("loc_2493")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_234E end

    def Function_11_249F(): pass

    label("Function_11_249F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2656")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 0)), scpexpr(EXPR_END)), "loc_2637")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2632")
    ClearScenarioFlags(0x3B, 0)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_262F")
    ClearScenarioFlags(0x39, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2554():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2554)
    TurnDirection(0x8, 0x0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    PlayEffect(0x7, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_D48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262A")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2611")
    Call(1, 5)
    Jump("loc_262A")

    label("loc_2611")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2627")
    Call(1, 4)
    Jump("loc_262A")

    label("loc_2627")

    Call(1, 3)

    label("loc_262A")

    Jump("loc_2632")

    label("loc_262F")

    Call(1, 1)

    label("loc_2632")

    Jump("loc_264D")

    label("loc_2637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_264D")
    ClearScenarioFlags(0x39, 0)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_264D")

    TalkEnd(0xFF)
    Return()

    label("loc_2656")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 0)), scpexpr(EXPR_END)), "loc_27E0")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27DB")
    ClearScenarioFlags(0x3B, 0)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_27D8")
    ClearScenarioFlags(0x39, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_26FD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_26FD)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_D8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D3")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27BA")
    Call(1, 5)
    Jump("loc_27D3")

    label("loc_27BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27D0")
    Call(1, 4)
    Jump("loc_27D3")

    label("loc_27D0")

    Call(1, 3)

    label("loc_27D3")

    Jump("loc_27DB")

    label("loc_27D8")

    Call(1, 1)

    label("loc_27DB")

    Jump("loc_27F6")

    label("loc_27E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_27F6")
    ClearScenarioFlags(0x39, 0)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_27F6")

    TalkEnd(0xFF)
    Return()

    # Function_11_249F end

    def Function_12_27FB(): pass

    label("Function_12_27FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29B2")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_END)), "loc_2993")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298E")
    ClearScenarioFlags(0x3B, 1)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_298B")
    ClearScenarioFlags(0x39, 1)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_28B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_28B0)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_D48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2986")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_296D")
    Call(1, 5)
    Jump("loc_2986")

    label("loc_296D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2983")
    Call(1, 4)
    Jump("loc_2986")

    label("loc_2983")

    Call(1, 3)

    label("loc_2986")

    Jump("loc_298E")

    label("loc_298B")

    Call(1, 1)

    label("loc_298E")

    Jump("loc_29A9")

    label("loc_2993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_29A9")
    ClearScenarioFlags(0x39, 1)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_29A9")

    TalkEnd(0xFF)
    Return()

    label("loc_29B2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_END)), "loc_2B3C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B37")
    ClearScenarioFlags(0x3B, 1)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_2B34")
    ClearScenarioFlags(0x39, 1)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2A59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A59)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_D8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2F")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B16")
    Call(1, 5)
    Jump("loc_2B2F")

    label("loc_2B16")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B2C")
    Call(1, 4)
    Jump("loc_2B2F")

    label("loc_2B2C")

    Call(1, 3)

    label("loc_2B2F")

    Jump("loc_2B37")

    label("loc_2B34")

    Call(1, 1)

    label("loc_2B37")

    Jump("loc_2B52")

    label("loc_2B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_2B52")
    ClearScenarioFlags(0x39, 1)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2B52")

    TalkEnd(0xFF)
    Return()

    # Function_12_27FB end

    def Function_13_2B57(): pass

    label("Function_13_2B57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B74")
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    Jump("loc_2B79")

    label("loc_2B74")

    SetChrFlags(0x1B, 0x80)

    label("loc_2B79")

    Return()

    # Function_13_2B57 end

    def Function_14_2B7A(): pass

    label("Function_14_2B7A")

    Call(1, 6)
    Return()

    # Function_14_2B7A end

    def Function_15_2B7E(): pass

    label("Function_15_2B7E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D16")

    ChrTalk(
        0xE,
        (
            "There is also first aid\x01",
            "treatment inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Do you want to rest\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Rest\x01",        # 0
            "Cancel\x01",      # 1
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
        (0, "loc_2C47"),
        (1, "loc_2CC9"),
        (SWITCH_DEFAULT, "loc_2D16"),
    )


    label("loc_2C47")

    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_0D()
    OP_57(0x0)

    ChrTalk(
        0xE,
        (
            "Please, do be careful. I\x01",
            "leave His Excellency the\x01",
            "Archduke to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D16")

    label("loc_2CC9")


    ChrTalk(
        0xE,
        (
            "...Understood. If you\x01",
            "ever want to rest, please\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D16")

    label("loc_2D16")

    TalkEnd(0xFE)
    Return()

    # Function_15_2B7E end

    def Function_16_2D1A(): pass

    label("Function_16_2D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 4)), scpexpr(EXPR_END)), "loc_2D24")
    Return()

    label("loc_2D24")

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
        (1, "loc_2E02"),
        (SWITCH_DEFAULT, "loc_2E1B"),
    )


    label("loc_2E02")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -87190, -3000, -2850, 270)
    EventEnd(0x5)
    Return()

    label("loc_2E1B")

    Battle("BattleInfo_E14", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-87190, -2000, -2850, 0)
    OP_90(0x0, -87190, -3000, -2850, 270)
    OP_90(0x1, -87190, -3000, -2850, 270)
    OP_90(0x2, -87190, -3000, -2850, 270)
    OP_90(0x3, -87190, -3000, -2850, 270)
    OP_90(0x4, -87190, -3000, -2850, 270)
    OP_90(0x5, -87190, -3000, -2850, 270)
    OP_90(0x6, -87190, -3000, -2850, 270)
    OP_90(0x7, -87190, -3000, -2850, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_2EDD"),
        (1, "loc_2EE2"),
        (SWITCH_DEFAULT, "loc_2EE5"),
    )


    label("loc_2EDD")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_2EE2")

    OP_B9(0x0)
    Return()

    label("loc_2EE5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-84150, -2400, -3630, 0)
    MoveCamera(49, 34, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x2A, 0x80)
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
            scpstr(SCPSTR_CODE_ITEM, 0xE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xE, 1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -81820, -3000, -6090, 313)
    SetChrPos(0x102, -85560, -3000, -2620, 133)
    SetChrPos(0x103, -81370, -3000, -3860, 268)
    SetChrPos(0x104, -86540, -3000, -4560, 43)
    SetChrPos(0x109, -83290, -3000, -1880, 178)
    SetChrPos(0x105, -84580, -3000, -6420, 43)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x103,
        (
            "#00203FThis is... One of those\x01",
            "craft books.\x02\x03",
            "#00202FIt might be perfect for\x01",
            "Elie and Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWazy, do you want to try\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHehe, of course.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x1, 0x18F)
    AddCraft(0x4, 0x18F)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie and Wazy learned\x01",
            "the \x07\x02",
            ""Akashic Star"\x07\x05",
            " combi\x01",
            "craft.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By each expending 100 CP,\x01",
            "a powerful combination\x01",
            "attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x21C, 4)
    OP_29(0x7B, 0x4, 0x10)
    OP_29(0x7B, 0x4, 0x2)
    OP_29(0x7B, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_16_2D1A end

    def Function_17_31B1(): pass

    label("Function_17_31B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(11240, 2100, 6500, 0)
    MoveCamera(61, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(37120, 0)
    AddParty(0x76, 0xFF, 0xFF)
    ClearChrFlags(0x177, 0x80)
    OP_4B(0xE, 0xFF)
    SetChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0xE, 0x0)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -3740, -3000, 11760, 180)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x177, -3740, -3000, 11760, 180)
    OP_A7(0x177, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -3740, -3000, 11760, 180)
    SetChrPos(0x102, -3740, -3000, 11760, 180)
    SetChrPos(0x109, -3740, -3000, 11760, 180)
    SetChrPos(0x105, -3740, -3000, 11760, 180)
    SetChrPos(0x104, -3740, -3000, 11760, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearMapObjFlags(0x9, 0x2000000)
    OP_78(0x9, 0xF)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    OP_49()
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 34010, 0, 6210, 270)
    OP_D5(0xF, 0x0, 0x41EB0, 0x0, 0x0)
    OP_71(0x9, 0x79, 0xB4, 0x1, 0x20)
    OP_68(11240, 0, 6500, 5000)
    BeginChrThread(0xF, 3, 0, 18)
    BeginChrThread(0x1A, 1, 0, 26)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(-3480, 0, 6730, 0)
    MoveCamera(358, 29, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17780, 0)
    OP_0D()
    WaitChrThread(0xF, 3)
    OP_71(0x9, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x9)
    Sleep(1500)
    Sound(462, 0, 100, 0)
    OP_71(0x9, 0xF1, 0x10E, 0x1, 0x0)
    Sleep(500)
    OP_79(0x9)
    Sleep(1000)
    BeginChrThread(0xE, 3, 0, 25)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 20)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 21)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 22)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 23)
    WaitChrThread(0x104, 3)
    BeginChrThread(0x177, 3, 0, 24)
    WaitChrThread(0x177, 3)

    ChrTalk(
        0x177,
        (
            "We'll go on foot from\x01",
            "here, so wait for us\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Sir, please be careful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FStill, I knew there'd be\x01",
            "a lot of monsters here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FYou're right...\x02\x03",
            "#10101FWe must properly guard\x01",
            "His Excellency the\x01",
            "Archduke!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x177, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x177,
        "Haha, how dependable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "As I said before, there are\x01",
            "many mushrooms similar to the\x01",
            "Almashroom that grows here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "I'll identify it for you,\x01",
            "so let's first look for\x01",
            "any mushroom we can find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAlright. We're counting\x01",
            "on you to identify them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FShall we be going, then?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "There is also first aid\x01",
            "treatment inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please return here if\x01",
            "things get dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAlright, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FLet's proceed carefully.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x9, 0x10F, 0x12C, 0x1, 0x0)
    OP_79(0x9)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Archduke Albert has joined\x01",
            "as an escort. If his HP\x01",
            "reaches 0, it's game over.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x78, 0x1, 0x0)
    OP_69(0xFF, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrFlags(0x17, 0x2)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x19, 0x2)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0xE, 0x40)
    OP_4C(0xE, 0xFF)
    OP_37()
    OP_1B(0x0, 0x0, 0x2D)
    OP_1B(0x1, 0x0, 0x2E)
    SetChrPos(0x0, -8220, -3000, 8610, 270)
    EventEnd(0x5)
    Return()

    # Function_17_31B1 end

    def Function_18_37D2(): pass

    label("Function_18_37D2")

    OP_9F(0x0, 0xF)
    OP_9F(0x1, 34010, 0, 6210)
    OP_9F(0x1, 25150, 0, 5210)
    OP_9F(0x1, 16219, 0, 5500)
    OP_9F(0x1, 12320, -580, 5860)
    OP_9F(0x1, 7920, -1800, 5790)
    OP_9F(0x2, 0xF, 7000, 0x6)
    OP_9F(0x0, 0xF)
    OP_9F(0x1, 5380, -2500, 6070)
    OP_9F(0x1, 250, -3000, 9730)
    OP_9F(0x1, -4890, -3000, 12350)
    OP_9F(0x1, -7710, -3000, 12490)
    OP_9F(0x2, 0xF, 7000, 0x6)
    OP_71(0x9, 0x5B, 0x78, 0x1, 0x0)
    Sleep(1500)
    Sound(493, 0, 100, 0)
    Sleep(500)
    OP_71(0x9, 0x79, 0xB4, 0x1, 0x20)
    Sleep(500)
    OP_9B(0x1, 0xF, 0xB4, 0xFA0, 0xFA0, 0x0)
    Sound(492, 0, 60, 0)
    Return()

    # Function_18_37D2 end

    def Function_19_38A7(): pass

    label("Function_19_38A7")


    def lambda_38AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38AC)

    def lambda_38BD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38BD)
    WaitChrThread(0x101, 1)
    OP_95(0xFE, -3870, -3000, 6450, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_19_38A7 end

    def Function_20_38F2(): pass

    label("Function_20_38F2")


    def lambda_38F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_38F7)

    def lambda_3908():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3908)
    WaitChrThread(0x102, 1)
    OP_95(0xFE, -5300, -3000, 7650, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_20_38F2 end

    def Function_21_393D(): pass

    label("Function_21_393D")


    def lambda_3942():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3942)

    def lambda_3953():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3953)
    WaitChrThread(0x109, 1)
    OP_95(0xFE, -2210, -3000, 7240, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_21_393D end

    def Function_22_3988(): pass

    label("Function_22_3988")


    def lambda_398D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_398D)

    def lambda_399E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_399E)
    WaitChrThread(0x105, 1)
    OP_95(0xFE, -1590, -3000, 8360, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_22_3988 end

    def Function_23_39D3(): pass

    label("Function_23_39D3")


    def lambda_39D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_39D8)

    def lambda_39E9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39E9)
    WaitChrThread(0x104, 1)
    OP_95(0xFE, -1780, -3000, 10000, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_23_39D3 end

    def Function_24_3A1E(): pass

    label("Function_24_3A1E")


    def lambda_3A23():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x177, 2, lambda_3A23)

    def lambda_3A34():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF8F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x177, 1, lambda_3A34)
    WaitChrThread(0x177, 1)
    Sleep(300)
    TurnDirection(0xFE, 0xE, 500)
    Return()

    # Function_24_3A1E end

    def Function_25_3A58(): pass

    label("Function_25_3A58")


    def lambda_3A5D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3A5D)

    def lambda_3A6E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3A6E)
    WaitChrThread(0xE, 1)
    OP_95(0xFE, -4870, -3000, 9930, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_25_3A58 end

    def Function_26_3AA3(): pass

    label("Function_26_3AA3")

    Sound(458, 0, 80, 0)
    Sleep(4000)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    Sound(492, 0, 100, 0)
    Return()

    # Function_26_3AA3 end

    def Function_27_3ABC(): pass

    label("Function_27_3ABC")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00050.itc", 0x28)
    LoadChrToIndex("chr/ch00150.itc", 0x29)
    LoadChrToIndex("chr/ch00350.itc", 0x2A)
    LoadChrToIndex("chr/ch02950.itc", 0x2B)
    LoadChrToIndex("chr/ch03050.itc", 0x2C)
    Call(0, 28)
    LoadChrToIndex("chr/ch00050.itc", 0x28)
    LoadChrToIndex("chr/ch00150.itc", 0x29)
    LoadChrToIndex("chr/ch00350.itc", 0x2A)
    LoadChrToIndex("chr/ch02950.itc", 0x2B)
    LoadChrToIndex("chr/ch03050.itc", 0x2C)
    Call(0, 39)
    Return()

    # Function_27_3ABC end

    def Function_28_3B0C(): pass

    label("Function_28_3B0C")

    EventBegin(0x0)
    OP_E2(0x1)
    OP_68(-143150, -4400, -61520, 0)
    MoveCamera(40, 37, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(11320, 0)
    SetChrPos(0x177, -141180, -9000, -57770, 90)
    SetChrPos(0x19, -139910, -9000, -57620, 90)
    SetChrFlags(0x19, 0x2)
    SetChrPos(0x101, -138860, -9000, -57500, 270)
    SetChrPos(0x102, -140370, -9000, -59530, 0)
    SetChrPos(0x109, -136860, -9000, -57520, 270)
    SetChrPos(0x105, -137250, -9000, -59110, 270)
    SetChrPos(0x104, -139150, -9000, -60560, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found a mushroom!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FYour Excellency, is this\x01",
            "mushroom...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x177, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x177)

    ChrTalk(
        0x177,
        "...Yes, this is it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "This is undoubtedly an\x01",
            "Almashroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FR-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh man, we finally found\x01",
            "it, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FLet's harvest it\x01",
            "immediately!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(200)
    SetChrFlags(0x19, 0x80)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16IAlmashroom\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x156, 4)

    ChrTalk(
        0x101,
        (
            "#00000FAlright, now we can save\x01",
            "that patient─\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(830, 0, 80, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x177, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x11)
    SetChrChipByIndex(0x11, 0x11)
    SetChrChipByIndex(0x12, 0x13)
    SetChrChipByIndex(0x13, 0x17)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrPos(0x10, -126790, -9000, -55860, 225)
    SetChrPos(0x11, -133580, -9000, -67970, 315)
    SetChrPos(0x12, -126380, -9000, -61330, 315)
    SetChrPos(0x13, -130199, -9000, -50710, 225)
    OP_68(-142700, -4400, -63000, 3000)
    MoveCamera(57, 28, 0, 3000)
    OP_6E(560, 3000)
    SetCameraDistance(11590, 3000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    BeginChrThread(0x10, 3, 0, 35)
    BeginChrThread(0x11, 3, 0, 36)
    BeginChrThread(0x12, 3, 0, 37)
    BeginChrThread(0x13, 3, 0, 38)

    def lambda_4112():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4112)
    Sleep(50)

    def lambda_4122():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4122)
    Sleep(50)

    def lambda_4132():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4132)
    Sleep(50)

    def lambda_4142():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4142)
    Sleep(50)

    def lambda_4152():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4152)
    OP_6F(0x79)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x102, 0x29)
    SetChrChipByIndex(0x104, 0x2A)
    SetChrChipByIndex(0x109, 0x2B)
    SetChrChipByIndex(0x105, 0x2C)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00301FIs this... the territory\x01",
            "of those monsters!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        "My god!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYour Excellency, please\x01",
            "stay back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FHere they come!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x10, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    Battle("BattleInfo_E9C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_28_3B0C end

    def Function_29_4252(): pass

    label("Function_29_4252")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4270")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_29_4252")

    label("loc_4270")

    Return()

    # Function_29_4252 end

    def Function_30_4271(): pass

    label("Function_30_4271")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_428F")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_30_4271")

    label("loc_428F")

    Return()

    # Function_30_4271 end

    def Function_31_4290(): pass

    label("Function_31_4290")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42AE")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_31_4290")

    label("loc_42AE")

    Return()

    # Function_31_4290 end

    def Function_32_42AF(): pass

    label("Function_32_42AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42CD")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_32_42AF")

    label("loc_42CD")

    Return()

    # Function_32_42AF end

    def Function_33_42CE(): pass

    label("Function_33_42CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42EC")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_33_42CE")

    label("loc_42EC")

    Return()

    # Function_33_42CE end

    def Function_34_42ED(): pass

    label("Function_34_42ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_430B")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_34_42ED")

    label("loc_430B")

    Return()

    # Function_34_42ED end

    def Function_35_430C(): pass

    label("Function_35_430C")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 32)
    OP_95(0xFE, -132300, -9000, -57260, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 1, 0, 29)
    Return()

    # Function_35_430C end

    def Function_36_4353(): pass

    label("Function_36_4353")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 32)
    OP_95(0xFE, -135400, -9000, -63520, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 1, 0, 29)
    Return()

    # Function_36_4353 end

    def Function_37_439A(): pass

    label("Function_37_439A")

    BeginChrThread(0xFE, 2, 0, 33)
    OP_95(0xFE, -132410, -9000, -60610, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x12)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 30)
    Return()

    # Function_37_439A end

    def Function_38_43CB(): pass

    label("Function_38_43CB")

    BeginChrThread(0xFE, 2, 0, 34)
    OP_95(0xFE, -135470, -9000, -54720, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 31)
    Return()

    # Function_38_43CB end

    def Function_39_43FC(): pass

    label("Function_39_43FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_68(-143030, -4400, -63970, 0)
    MoveCamera(50, 29, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(6640, 0)
    SetChrPos(0x177, -140500, -9000, -59810, 135)
    SetChrPos(0x101, -136160, -9000, -60610, 135)
    SetChrPos(0x102, -136120, -9000, -58860, 135)
    SetChrPos(0x109, -138110, -9000, -58340, 135)
    SetChrPos(0x105, -138360, -9000, -60330, 90)
    SetChrPos(0x104, -137650, -9000, -62200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(4720, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FPhew! We did it,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x177, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FYour Excellency, are you\x01",
            "hurt?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4569():
        TurnDirection(0xFE, 0x177, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4569)
    Sleep(50)

    def lambda_4579():
        TurnDirection(0xFE, 0x177, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4579)
    Sleep(50)

    def lambda_4589():
        TurnDirection(0xFE, 0x177, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4589)
    Sleep(50)

    def lambda_4599():
        TurnDirection(0xFE, 0x177, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4599)
    Sleep(50)

    def lambda_45A9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x177, 1, lambda_45A9)
    Sleep(300)

    ChrTalk(
        0x177,
        (
            "No. Thanks to you, I'm\x01",
            "safe, as you can see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FPhew, thank goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FBut, why were there so\x01",
            "many all at once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "They feed on mushrooms\x01",
            "such as this Almashroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "They likely attacked us\x01",
            "thinking their feeding\x01",
            "ground was invaded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAnyway, it looks like we\x01",
            "can save that patient\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "Yes. Arios should be\x01",
            "getting back any minute\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "Let's hurry back to the\x01",
            "hospital.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And so, Lloyd and the others\x01",
            "returned to the hospital\x01",
            "with Archduke Albert...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Ante Grass that Arios picked and\x01",
            "the Almashroom were given to Professor\x01",
            "Seiland and she prepared the antidote.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)
    OP_E2(0x0)
    SetScenarioFlags(0x22, 3)
    NewScene("t1530", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_39_43FC end

    def Function_40_4872(): pass

    label("Function_40_4872")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4950")
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found a mushroom!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x109,
        (
            "#10100FYour Excellency, is this\x01",
            "mushroom...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "...No, this doesn't seem\x01",
            "to be an Almashroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...It seems we should\x01",
            "look elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4998")

    label("loc_4950")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems that this isn't\x01",
            "an Almashroom.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4998")

    TalkEnd(0xFF)
    Return()

    # Function_40_4872 end

    def Function_41_499C(): pass

    label("Function_41_499C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A66")
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found a mushroom!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x104,
        (
            "#00300FArchduke, what about\x01",
            "this one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "...That's not it. This\x01",
            "isn't an Almashroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...Let's search\x01",
            "elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AAE")

    label("loc_4A66")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems that this isn't\x01",
            "an Almashroom.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4AAE")

    TalkEnd(0xFF)
    Return()

    # Function_41_499C end

    def Function_42_4AB2(): pass

    label("Function_42_4AB2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B9F")
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found a mushroom!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FYour Grace, could this\x01",
            "one be an Almashroom...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "No... It looks like it,\x01",
            "but it's not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh man. Let's try\x01",
            "looking in somewhere\x01",
            "else, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4BE7")

    label("loc_4B9F")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems that this isn't\x01",
            "an Almashroom.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4BE7")

    TalkEnd(0xFF)
    Return()

    # Function_42_4AB2 end

    def Function_43_4BEB(): pass

    label("Function_43_4BEB")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CCB")
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found a mushroom!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        (
            "#00100FYour Grace, is this\x01",
            "mushroom any good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "Hm... Unfortunately, it\x01",
            "doesn't look like an\x01",
            "Almashroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWe can only keep\x01",
            "searching.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D13")

    label("loc_4CCB")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems that this isn't\x01",
            "an Almashroom.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4D13")

    TalkEnd(0xFF)
    Return()

    # Function_43_4BEB end

    def Function_44_4D17(): pass

    label("Function_44_4D17")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E0C")
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found a mushroom!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10300FYour Grace, what about\x01",
            "this mushroom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "Hmmm... No. This isn't\x01",
            "an Almashroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh man. I guess we can\x01",
            "only keep lookin' 'til\x01",
            "we find the right one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4E54")

    label("loc_4E0C")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems that this isn't\x01",
            "an Almashroom.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4E54")

    TalkEnd(0xFF)
    Return()

    # Function_44_4D17 end

    def Function_45_4E58(): pass

    label("Function_45_4E58")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00005FIf we go through here,\x01",
            "we'll exit the forest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "The Almashroom should be somewhere\x01",
            "in these woodlands. Let's pay\x01",
            "attention and look for it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 20500, 0, 6000, 270)
    EventEnd(0x4)
    Return()

    # Function_45_4E58 end

    def Function_46_4F09(): pass

    label("Function_46_4F09")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00005FIf we go through here,\x01",
            "we'll come out in the\x01",
            "Tower of Stargaze area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "The Almashroom should be somewhere\x01",
            "in these woodlands. Let's pay\x01",
            "attention and look for it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -132000, -9920, -35000, 180)
    EventEnd(0x4)
    Return()

    # Function_46_4F09 end

    def Function_47_4FD1(): pass

    label("Function_47_4FD1")

    Battle("BattleInfo_E58", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5018")
    OP_90(0x0, -22480, -3000, 9140, 180)
    EventEnd(0x5)
    SetChrFlags(0xD, 0x8000)
    Jump("loc_504C")

    label("loc_5018")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_502B")
    Jump("loc_504C")

    label("loc_502B")

    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0x4, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 2)
    EventEnd(0x5)

    label("loc_504C")

    Return()

    # Function_47_4FD1 end

    def Function_48_504D(): pass

    label("Function_48_504D")

    EventBegin(0x1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_515B")

    ChrTalk(
        0x101,
        (
            "#00001FThe tower is further\x01",
            "ahead...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FThe Steel Maiden is\x01",
            "there as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe can't avoid her, but let's\x01",
            "leave this place for later,\x01",
            "like Meister Jｶrg suggested.\x02\x03",
            "#00001FFirst, let's head to the\x01",
            "temple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201FRoger.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_51A9")

    label("loc_515B")


    ChrTalk(
        0x101,
        (
            "#00001FLet's leave the tower\x01",
            "for later. First, let's\x01",
            "head to the temple.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51A9")

    OP_5A()
    OP_E2(0x2)
    SetChrPos(0x0, -132430, -9000, -45250, 180)
    EventEnd(0x4)
    Return()

    # Function_48_504D end

    SaveToFile()

Try(main)
