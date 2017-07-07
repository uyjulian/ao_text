from ScenarioHelper import *

def main():
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
        "Star beetle",         # 1
        "Star beetle",         # 2
        "Goddy Osser",     # 3
        "Goddy Osser",     # 4
        "Goddy Osser",     # 5
        "Eidolon",                   # 6
        "A driver",                 # 7
        "Shuttle limousine",         # 8
        "Gordian",           # 9
        "Gordian",           # 10
        "Baboon Monch",         # 11
        "Army Pineapp",     # 12
        "Fake mushrooms 1",             # 13
        "Fake mushroom 2",             # 14
        "Fake mushroom 3",             # 15
        "Fake mushroom 4",             # 16
        "Fake mushroom 5",             # 17
        "Alma mushrooms",               # 18
        "SE control",                 # 19
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
        "Ursula intermittent way",       # 32
        "Direction of Tower of Hoshi",           # 33
    ))

    ATBonus("ATBonus_828", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_848", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_51A0", 0,   1,   1,   9,   5,   3,   4)
    Sepith("Sepith_51A8", 0,   0,   6,   10,  1,   2,   5)
    Sepith("Sepith_51B8", 6,   6,   0,   9,   0,   2,   1)
    Sepith("Sepith_51B0", 0,   8,   2,   3,   3,   7,   1)
    Sepith("Sepith_51C0", 8,   0,   12,  0,   4,   2,   4)
    Sepith("Sepith_51D0", 9,   7,   18,  6,   7,   6,   3)

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
        "BattleInfo_98C", 0x0000, 58, 6, 60, 8, 1, 45, 0, "br1510", "Sepith_51A0", 30, 40, 20, 10,
        (
            ("ms65600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms65600.dat", "ms65600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms65600.dat", "ms72700.dat", "ms65600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms65600.dat", "ms65600.dat", "ms72700.dat", "ms65600.dat", 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
        )
    )

    BattleInfo(
        "BattleInfo_A54", 0x0000, 58, 6, 60, 8, 1, 40, 0, "br1510", "Sepith_51A8", 30, 40, 20, 10,
        (
            ("ms72300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72300.dat", "ms72300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72300.dat", "ms72700.dat", "ms72300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72300.dat", "ms72300.dat", "ms72700.dat", "ms72300.dat", 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
        )
    )

    BattleInfo(
        "BattleInfo_B1C", 0x0000, 58, 6, 60, 8, 1, 25, 0, "br1510", "Sepith_51B8", 30, 40, 20, 10,
        (
            ("ms72700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72700.dat", "ms72700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72700.dat", "ms62400.dat", "ms72700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms72700.dat", "ms72700.dat", "ms62400.dat", "ms72700.dat", 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
        )
    )

    BattleInfo(
        "BattleInfo_BE4", 0x0000, 58, 6, 60, 8, 1, 40, 0, "br1510", "Sepith_51B0", 30, 40, 20, 10,
        (
            ("ms62400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms62400.dat", "ms62400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms62400.dat", "ms62400.dat", "ms62400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            ("ms62400.dat", "ms62400.dat", "ms62400.dat", "ms62400.dat", 0, 0, 0, 0, "MonsterBattlePostion_888", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
        )
    )

    BattleInfo(
        "BattleInfo_948", 0x0000, 58, 6, 60, 8, 1, 30, 0, "br1510", "Sepith_51C0", 100, 0, 0, 0,
        (
            ("ms68500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_868", "MonsterBattlePostion_8E8", "ed7450", "ed7453", "ATBonus_828"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_CAC", 0x0000, 81, 6, 45, 6, 1, 40, 0, "br1510", "Sepith_51D0", 40, 35, 25, 0,
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

    PlaceName(35.220001220703125, 0.0, 7.400000095367432, 0x0000, 0x0000, "Ursula intermittent way")
    PlaceName(-128.0, 0.0, -20.0, 0x0000, 0x0000, "Direction of Tower of Hoshi")

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
        "Function_8_20A5",         # 08, 8
        "Function_9_21F6",         # 09, 9
        "Function_10_2347",        # 0A, 10
        "Function_11_2498",        # 0B, 11
        "Function_12_27F6",        # 0C, 12
        "Function_13_2B54",        # 0D, 13
        "Function_14_2B77",        # 0E, 14
        "Function_15_2B7B",        # 0F, 15
        "Function_16_2D02",        # 10, 16
        "Function_17_31A7",        # 11, 17
        "Function_18_37CD",        # 12, 18
        "Function_19_38A2",        # 13, 19
        "Function_20_38ED",        # 14, 20
        "Function_21_3938",        # 15, 21
        "Function_22_3983",        # 16, 22
        "Function_23_39CE",        # 17, 23
        "Function_24_3A19",        # 18, 24
        "Function_25_3A53",        # 19, 25
        "Function_26_3A9E",        # 1A, 26
        "Function_27_3AB7",        # 1B, 27
        "Function_28_3B07",        # 1C, 28
        "Function_29_4249",        # 1D, 29
        "Function_30_4268",        # 1E, 30
        "Function_31_4287",        # 1F, 31
        "Function_32_42A6",        # 20, 32
        "Function_33_42C5",        # 21, 33
        "Function_34_42E4",        # 22, 34
        "Function_35_4303",        # 23, 35
        "Function_36_434A",        # 24, 36
        "Function_37_4391",        # 25, 37
        "Function_38_43C2",        # 26, 38
        "Function_39_43F3",        # 27, 39
        "Function_40_484A",        # 28, 40
        "Function_41_4966",        # 29, 41
        "Function_42_4A7C",        # 2A, 42
        "Function_43_4BA3",        # 2B, 43
        "Function_44_4CCF",        # 2C, 44
        "Function_45_4DFE",        # 2D, 45
        "Function_46_4E9B",        # 2E, 46
        "Function_47_4F43",        # 2F, 47
        "Function_48_4FBF",        # 30, 48
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8E")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I feel the signature of powerful demons from the treasure box.\x01",
            "【Estimated Demonic Level 82】\x01",
            "Would you like to open a treasure box?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E8E")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_1E8E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205F")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8D")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1EEB():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1EEB)

    def lambda_1F05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1F05)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A monster appeared!\x07\x00\x02",
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
        (0, "loc_1F6E"),
        (2, "loc_1F7D"),
        (1, "loc_1F8A"),
        (SWITCH_DEFAULT, "loc_1F8D"),
    )


    label("loc_1F6E")

    SetScenarioFlags(0x214, 2)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_1F8D")

    label("loc_1F7D")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1F8A")

    OP_B9(0x0)
    Return()

    label("loc_1F8D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('焰星铃', 1)"), scpexpr(EXPR_END)), "loc_1FEA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '焰星铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_205A")

    label("loc_1FEA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '焰星铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '焰星铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_205A")

    Jump("loc_2099")

    label("loc_205F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_2099")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1DEB end

    def Function_8_20A5(): pass

    label("Function_8_20A5")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A5")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('结晶碎片', 1)"), scpexpr(EXPR_END)), "loc_212E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '结晶碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_21A0")

    label("loc_212E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '结晶碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '结晶碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_21A0")

    Jump("loc_21EA")

    label("loc_21A5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_21EA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_20A5 end

    def Function_9_21F6(): pass

    label("Function_9_21F6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F6")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_227F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_22F1")

    label("loc_227F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_22F1")

    Jump("loc_233B")

    label("loc_22F6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_233B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_21F6 end

    def Function_10_2347(): pass

    label("Function_10_2347")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2447")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('细针面', 1)"), scpexpr(EXPR_END)), "loc_23D0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '细针面'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_2442")

    label("loc_23D0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '细针面'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '细针面'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2442")

    Jump("loc_248C")

    label("loc_2447")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_248C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_2347 end

    def Function_11_2498(): pass

    label("Function_11_2498")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2650")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 0)), scpexpr(EXPR_END)), "loc_2631")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "Something seems to be buried.\x01",
            "Do you dig it?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262C")
    ClearScenarioFlags(0x3B, 0)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_2629")
    ClearScenarioFlags(0x39, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2552():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2552)
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
            "A monster appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_D48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2624")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_260B")
    Call(1, 5)
    Jump("loc_2624")

    label("loc_260B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2621")
    Call(1, 4)
    Jump("loc_2624")

    label("loc_2621")

    Call(1, 3)

    label("loc_2624")

    Jump("loc_262C")

    label("loc_2629")

    Call(1, 1)

    label("loc_262C")

    Jump("loc_2647")

    label("loc_2631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_2647")
    ClearScenarioFlags(0x39, 0)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2647")

    TalkEnd(0xFF)
    Return()

    label("loc_2650")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 0)), scpexpr(EXPR_END)), "loc_27DB")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "Something seems to be buried.\x01",
            "Do you dig it?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D6")
    ClearScenarioFlags(0x3B, 0)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_27D3")
    ClearScenarioFlags(0x39, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_26FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_26FC)
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
            "A monster appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_D8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27CE")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27B5")
    Call(1, 5)
    Jump("loc_27CE")

    label("loc_27B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27CB")
    Call(1, 4)
    Jump("loc_27CE")

    label("loc_27CB")

    Call(1, 3)

    label("loc_27CE")

    Jump("loc_27D6")

    label("loc_27D3")

    Call(1, 1)

    label("loc_27D6")

    Jump("loc_27F1")

    label("loc_27DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 0)), scpexpr(EXPR_END)), "loc_27F1")
    ClearScenarioFlags(0x39, 0)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_27F1")

    TalkEnd(0xFF)
    Return()

    # Function_11_2498 end

    def Function_12_27F6(): pass

    label("Function_12_27F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29AE")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_END)), "loc_298F")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "Something seems to be buried.\x01",
            "Do you dig it?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298A")
    ClearScenarioFlags(0x3B, 1)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_2987")
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
            "A monster appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_D48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2982")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2969")
    Call(1, 5)
    Jump("loc_2982")

    label("loc_2969")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_297F")
    Call(1, 4)
    Jump("loc_2982")

    label("loc_297F")

    Call(1, 3)

    label("loc_2982")

    Jump("loc_298A")

    label("loc_2987")

    Call(1, 1)

    label("loc_298A")

    Jump("loc_29A5")

    label("loc_298F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_29A5")
    ClearScenarioFlags(0x39, 1)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_29A5")

    TalkEnd(0xFF)
    Return()

    label("loc_29AE")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_END)), "loc_2B39")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "Something seems to be buried.\x01",
            "Do you dig it?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B34")
    ClearScenarioFlags(0x3B, 1)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_2B31")
    ClearScenarioFlags(0x39, 1)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2A5A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A5A)
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
            "A monster appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_D8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2C")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B13")
    Call(1, 5)
    Jump("loc_2B2C")

    label("loc_2B13")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B29")
    Call(1, 4)
    Jump("loc_2B2C")

    label("loc_2B29")

    Call(1, 3)

    label("loc_2B2C")

    Jump("loc_2B34")

    label("loc_2B31")

    Call(1, 1)

    label("loc_2B34")

    Jump("loc_2B4F")

    label("loc_2B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_2B4F")
    ClearScenarioFlags(0x39, 1)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2B4F")

    TalkEnd(0xFF)
    Return()

    # Function_12_27F6 end

    def Function_13_2B54(): pass

    label("Function_13_2B54")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B71")
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    Jump("loc_2B76")

    label("loc_2B71")

    SetChrFlags(0x1B, 0x80)

    label("loc_2B76")

    Return()

    # Function_13_2B54 end

    def Function_14_2B77(): pass

    label("Function_14_2B77")

    Call(1, 6)
    Return()

    # Function_14_2B77 end

    def Function_15_2B7B(): pass

    label("Function_15_2B7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CFE")

    ChrTalk(
        0xE,
        "There is preparation for first aid in the car.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Would you like to take a rest here?\x02",
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
            "Rest\x01",      # 0
            "quit\x01",        # 1
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
        (0, "loc_2C40"),
        (1, "loc_2CB5"),
        (SWITCH_DEFAULT, "loc_2CFE"),
    )


    label("loc_2C40")

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
            "Please take care.\x01",
            "Honorable Dear Grand Prateree thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFE")

    label("loc_2CB5")


    ChrTalk(
        0xE,
        (
            "……I understand.\x01",
            "Whenever you want to take a break\x01",
            "Please tell us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFE")

    label("loc_2CFE")

    TalkEnd(0xFE)
    Return()

    # Function_15_2B7B end

    def Function_16_2D02(): pass

    label("Function_16_2D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 4)), scpexpr(EXPR_END)), "loc_2D0C")
    Return()

    label("loc_2D0C")

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
            "Large monsters wandering around#4RIt is alright#doing.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Exterminate】\x01",      # 0
            "【quit】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2DEE"),
        (SWITCH_DEFAULT, "loc_2E07"),
    )


    label("loc_2DEE")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -87190, -3000, -2850, 270)
    EventEnd(0x5)
    Return()

    label("loc_2E07")

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
        (2, "loc_2EC9"),
        (1, "loc_2ECE"),
        (SWITCH_DEFAULT, "loc_2ED1"),
    )


    label("loc_2EC9")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_2ECE")

    OP_B9(0x0)
    Return()

    label("loc_2ED1")

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
            "Arranged arrangements devils!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '战术书·虚'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber('战术书·虚', 1)
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
            "#00203Fthis is--\x01",
            "It is a tactical book.\x02\x03",
            "#00202FEly and Mr. Wazy\x01",
            "It might be perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FWaj, can you try it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHuh, of course.\x02",
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
            "Eli and Wazi combi craft\x01\x07\x02",
            "\"Akashic Star\"\x07\x05",
            "I have learned.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By consuming CP by 100\x01",
            "A powerful combination attack can be launched.\x07\x00\x02",
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

    # Function_16_2D02 end

    def Function_17_31A7(): pass

    label("Function_17_31A7")

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
            "I will go on foot from here,\x01",
            "You are waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Ha ha, be careful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FAfter all, here is\x01",
            "It seems there are quite a few demons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FI agree……\x02\x03",
            "#10101FDear Grand Prince\x01",
            "I have to keep a talent!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x177, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x177,
        "Huh, I'm relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "As I said, here is\x01",
            "『Alma mushrooms』に形が似たキノコが\x01",
            "It should live in mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "Since I will distinguish it,\x01",
            "First of all at random\x01",
            "Let's look for mushrooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, the judgment is\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FLet's suppose to go now.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        "There is preparation for first aid in the car.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When it comes to danger,\x01",
            "Please return to here once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FLet's take care and proceed.\x02",
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
            "The Grand Duke of Albert joined the escort subject.\x01",
            "Game over when HP becomes 0.\x07\x00\x02",
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

    # Function_17_31A7 end

    def Function_18_37CD(): pass

    label("Function_18_37CD")

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

    # Function_18_37CD end

    def Function_19_38A2(): pass

    label("Function_19_38A2")


    def lambda_38A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38A7)

    def lambda_38B8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38B8)
    WaitChrThread(0x101, 1)
    OP_95(0xFE, -3870, -3000, 6450, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_19_38A2 end

    def Function_20_38ED(): pass

    label("Function_20_38ED")


    def lambda_38F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_38F2)

    def lambda_3903():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3903)
    WaitChrThread(0x102, 1)
    OP_95(0xFE, -5300, -3000, 7650, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_20_38ED end

    def Function_21_3938(): pass

    label("Function_21_3938")


    def lambda_393D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_393D)

    def lambda_394E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_394E)
    WaitChrThread(0x109, 1)
    OP_95(0xFE, -2210, -3000, 7240, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_21_3938 end

    def Function_22_3983(): pass

    label("Function_22_3983")


    def lambda_3988():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3988)

    def lambda_3999():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3999)
    WaitChrThread(0x105, 1)
    OP_95(0xFE, -1590, -3000, 8360, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_22_3983 end

    def Function_23_39CE(): pass

    label("Function_23_39CE")


    def lambda_39D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_39D3)

    def lambda_39E4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39E4)
    WaitChrThread(0x104, 1)
    OP_95(0xFE, -1780, -3000, 10000, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_23_39CE end

    def Function_24_3A19(): pass

    label("Function_24_3A19")


    def lambda_3A1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x177, 2, lambda_3A1E)

    def lambda_3A2F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF8F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x177, 1, lambda_3A2F)
    WaitChrThread(0x177, 1)
    Sleep(300)
    TurnDirection(0xFE, 0xE, 500)
    Return()

    # Function_24_3A19 end

    def Function_25_3A53(): pass

    label("Function_25_3A53")


    def lambda_3A58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3A58)

    def lambda_3A69():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3A69)
    WaitChrThread(0xE, 1)
    OP_95(0xFE, -4870, -3000, 9930, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_25_3A53 end

    def Function_26_3A9E(): pass

    label("Function_26_3A9E")

    Sound(458, 0, 80, 0)
    Sleep(4000)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    Sound(492, 0, 100, 0)
    Return()

    # Function_26_3A9E end

    def Function_27_3AB7(): pass

    label("Function_27_3AB7")

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

    # Function_27_3AB7 end

    def Function_28_3B07(): pass

    label("Function_28_3B07")

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
            "I found mushrooms!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000FDear Grand Prince, this mushroom ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x177, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x177)

    ChrTalk(
        0x177,
        "…… Well, this is it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "これが『Alma mushrooms』に\x01",
            "There is no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIs it true? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306FWow, finally found it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FLet's collect immediately!\x02",
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
            "#16IAlma mushrooms\x07\x00",
            "I got it.\x02",
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
            "#00000FOK, in this\x01",
            "Helping that patient ──\x02",
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

    def lambda_4109():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4109)
    Sleep(50)

    def lambda_4119():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4119)
    Sleep(50)

    def lambda_4129():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4129)
    Sleep(50)

    def lambda_4139():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4139)
    Sleep(50)

    def lambda_4149():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4149)
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
            "#00301FThis guy……\x01",
            "I'm on a territory around here\x01",
            "Demon Beast! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        "Muu …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYour Excellency, please go down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F……come!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x10, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    Battle("BattleInfo_E9C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_28_3B07 end

    def Function_29_4249(): pass

    label("Function_29_4249")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4267")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_29_4249")

    label("loc_4267")

    Return()

    # Function_29_4249 end

    def Function_30_4268(): pass

    label("Function_30_4268")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4286")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_30_4268")

    label("loc_4286")

    Return()

    # Function_30_4268 end

    def Function_31_4287(): pass

    label("Function_31_4287")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42A5")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_31_4287")

    label("loc_42A5")

    Return()

    # Function_31_4287 end

    def Function_32_42A6(): pass

    label("Function_32_42A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42C4")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_32_42A6")

    label("loc_42C4")

    Return()

    # Function_32_42A6 end

    def Function_33_42C5(): pass

    label("Function_33_42C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42E3")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_33_42C5")

    label("loc_42E3")

    Return()

    # Function_33_42C5 end

    def Function_34_42E4(): pass

    label("Function_34_42E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4302")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_34_42E4")

    label("loc_4302")

    Return()

    # Function_34_42E4 end

    def Function_35_4303(): pass

    label("Function_35_4303")

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

    # Function_35_4303 end

    def Function_36_434A(): pass

    label("Function_36_434A")

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

    # Function_36_434A end

    def Function_37_4391(): pass

    label("Function_37_4391")

    BeginChrThread(0xFE, 2, 0, 33)
    OP_95(0xFE, -132410, -9000, -60610, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x12)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 30)
    Return()

    # Function_37_4391 end

    def Function_38_43C2(): pass

    label("Function_38_43C2")

    BeginChrThread(0xFE, 2, 0, 34)
    OP_95(0xFE, -135470, -9000, -54720, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 31)
    Return()

    # Function_38_43C2 end

    def Function_39_43F3(): pass

    label("Function_39_43F3")

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
        "#00003FWhew … … did something happen.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x177, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00100FYour Excellency, are you injured?\x02",
    )

    CloseMessageWindow()

    def lambda_455D():
        TurnDirection(0xFE, 0x177, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_455D)
    Sleep(50)

    def lambda_456D():
        TurnDirection(0xFE, 0x177, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_456D)
    Sleep(50)

    def lambda_457D():
        TurnDirection(0xFE, 0x177, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_457D)
    Sleep(50)

    def lambda_458D():
        TurnDirection(0xFE, 0x177, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_458D)
    Sleep(50)

    def lambda_459D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x177, 1, lambda_459D)
    Sleep(300)

    ChrTalk(
        0x177,
        (
            "Well, thanks to you guys.\x01",
            "This street is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWell, it was good …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FHurry up, why so suddenly\x01",
            "That number has gathered?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "この『Alma mushrooms』などは、\x01",
            "They are mushrooms that become food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "I thought that the feed place was destroyed\x01",
            "I guess it hit me.\x02",
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
            "#00000FAnyway, that patient with this\x01",
            "You seem to be able to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "Well, Arios, too\x01",
            "It will be around time to come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        "Shall I return to the hospital in a hurry?\x02",
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
            "Thus, Lloyd's\x01",
            "Returning to the hospital with Prince Albert ……\x07\x00\x02",
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
            "Arios' s \"Ante Grass\" and\x01",
            "『Alma mushrooms』がセイランド教授に渡され、\x01",
            "An antidote was formulated.\x07\x00\x02",
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

    # Function_39_43F3 end

    def Function_40_484A(): pass

    label("Function_40_484A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_491F")
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I found mushrooms!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x109,
        "#10100FDear Grand Prince, this mushroom ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "… Well, this is\x01",
            "『Alma mushrooms』ではないようだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F…… It seems better to find another place.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4962")

    label("loc_491F")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "これは『Alma mushrooms』ではないようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4962")

    TalkEnd(0xFF)
    Return()

    # Function_40_484A end

    def Function_41_4966(): pass

    label("Function_41_4966")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A35")
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I found mushrooms!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x104,
        "#00300FDaimo Sun, how is this mushroom?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "… It is not.\x01",
            "これは『Alma mushrooms』ではない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F… … Let's find another place.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A78")

    label("loc_4A35")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "これは『Alma mushrooms』ではないようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4A78")

    TalkEnd(0xFF)
    Return()

    # Function_41_4966 end

    def Function_42_4A7C(): pass

    label("Function_42_4A7C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B5C")
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I found mushrooms!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FPrince Hiroko, this mushroom\x01",
            "『Alma mushrooms』でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        "No, it seems to be different but similar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWhew, another place\x01",
            "Let's look for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B9F")

    label("loc_4B5C")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "これは『Alma mushrooms』ではないようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4B9F")

    TalkEnd(0xFF)
    Return()

    # Function_42_4A7C end

    def Function_43_4BA3(): pass

    label("Function_43_4BA3")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C88")
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I found mushrooms!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        (
            "#00100FYour Excellency, this mushroom\x01",
            "How do you like it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "Well … unfortunately\x01",
            "『Alma mushrooms』ではないようだね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI only need to find more\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4CCB")

    label("loc_4C88")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "これは『Alma mushrooms』ではないようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4CCB")

    TalkEnd(0xFF)
    Return()

    # Function_43_4BA3 end

    def Function_44_4CCF(): pass

    label("Function_44_4CCF")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DB7")
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I found mushrooms!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10300FHow old is this mushroom?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "ううむ… It is not.\x01",
            "これは『Alma mushrooms』ではない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, until Atari comes out\x01",
            "I only have to find it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4DFA")

    label("loc_4DB7")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "これは『Alma mushrooms』ではないようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4DFA")

    TalkEnd(0xFF)
    Return()

    # Function_44_4CCF end

    def Function_45_4DFE(): pass

    label("Function_45_4DFE")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        "#00005FDo not leave the forest when you come out here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "『Alma mushrooms』は\x01",
            "It should be somewhere in this forest zone.\x01",
            "Let's try to find it carefully.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 20500, 0, 6000, 270)
    EventEnd(0x4)
    Return()

    # Function_45_4DFE end

    def Function_46_4E9B(): pass

    label("Function_46_4E9B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00005FWhen you go this way\x01",
            "Do not go out to the Tower of Hoshi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x177,
        (
            "『Alma mushrooms』は\x01",
            "It should be somewhere in this forest zone.\x01",
            "Let's try to find it carefully.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -132000, -9920, -35000, 180)
    EventEnd(0x4)
    Return()

    # Function_46_4E9B end

    def Function_47_4F43(): pass

    label("Function_47_4F43")

    Battle("BattleInfo_E58", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F8A")
    OP_90(0x0, -22480, -3000, 9140, 180)
    EventEnd(0x5)
    SetChrFlags(0xD, 0x8000)
    Jump("loc_4FBE")

    label("loc_4F8A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F9D")
    Jump("loc_4FBE")

    label("loc_4F9D")

    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0x4, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 2)
    EventEnd(0x5)

    label("loc_4FBE")

    Return()

    # Function_47_4F43 end

    def Function_48_4FBF(): pass

    label("Function_48_4FBF")

    EventBegin(0x1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50C7")

    ChrTalk(
        0x101,
        "#00001FThe future is the \"tower\" … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FHere …\x01",
            "There is a \"steel saint\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAlthough I can not get through,\x01",
            "According to Jorg Meister's advice\x01",
            "Let's postpone it.\x02\x03",
            "#00001FFirst we will head for the \"monastery\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F- OK.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5109")

    label("loc_50C7")


    ChrTalk(
        0x101,
        (
            "#00001F…… \"Tower\" is a postponement.\x01",
            "Let's first head towards the \"monastery\".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5109")

    OP_5A()
    OP_E2(0x2)
    SetChrPos(0x0, -132430, -9000, -45250, 180)
    EventEnd(0x4)
    Return()

    # Function_48_4FBF end

    SaveToFile()

Try(main)
