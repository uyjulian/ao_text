from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1540.bin",                # FileName
        "r1540",                    # MapName
        "r1540",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r1540", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x0D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 96, 0, 4, 0, 5],
    )

    BuildStringList((
        "r1540",                  # 0
        "Sharkman, the Sea Edge", # 1
        "ファイヤービートル",     # 2
        "ファイヤービートル",     # 3
        "ゴーディ・オッサー",     # 4
        "ゴーディ・オッサー",     # 5
        "クリドゥヴァー",         # 6
        "Cryptid",                # 7
        "br1530",                 # 8
        "br1530",                 # 9
        "br1530",                 # 10
        "br1530",                 # 11
        "br1530",                 # 12
        "br1530",                 # 13
        "br1530",                 # 14
        "br1530",                 # 15
        "br1530",                 # 16
        "br1530",                 # 17
        "To Crossbell City",      # 18
        "To St. Ursula Medical College",# 19
    ))

    ATBonus("ATBonus_564", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_584", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_4C16", 0,   0,   18,  2,   2,   0,   2)
    Sepith("Sepith_4C26", 0,   9,   3,   0,   4,   4,   4)
    Sepith("Sepith_4C0E", 3,   10,  0,   8,   3,   0,   0)
    Sepith("Sepith_4C1E", 9,   5,   0,   3,   0,   3,   4)
    Sepith("Sepith_4C56", 23,  23,  23,  23,  23,  23,  23)
    Sepith("Sepith_4C5E", 9,   7,   18,  6,   7,   6,   3)

    MonsterBattlePostion("MonsterBattlePostion_5C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_624", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_628", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_62C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_630", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_634", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_638", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_63C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_640", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_644", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_64C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_650", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_654", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_658", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_660", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_700", 0x0000, 58, 6, 45, 10, 1, 40, 0, "br1530", "Sepith_4C16", 30, 40, 20, 10,
        (
            ("ms65700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms65700.dat", "ms65700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms65700.dat", "ms65700.dat", "ms65700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms65700.dat", "ms65700.dat", "ms62100.dat", "ms65700.dat", 0, 0, 0, 0, "MonsterBattlePostion_5A4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_958", 0x0000, 58, 6, 45, 10, 1, 65, 0, "br1530", "Sepith_4C26", 45, 20, 20, 15,
        (
            ("ms70800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms70800.dat", "ms70800.dat", "ms70800.dat", "ms61400.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms70800.dat", "ms70700.dat", "ms70800.dat", "ms70800.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms70800.dat", "ms70700.dat", "ms70800.dat", "ms61400.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_890", 0x0000, 58, 6, 45, 10, 1, 25, 0, "br1530", "Sepith_4C0E", 30, 40, 20, 10,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_7C8", 0x0000, 58, 6, 45, 10, 1, 40, 0, "br1530", "Sepith_4C1E", 30, 40, 20, 10,
        (
            ("ms61100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms61100.dat", "ms61100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_A20", 0x0000, 58, 6, 90, 8, 1, 50, 0, "br1530", "Sepith_4C56", 30, 40, 20, 10,
        (
            ("ms66401.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms66401.dat", "ms66401.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms66401.dat", "ms66401.dat", "ms66401.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms66401.dat", "ms66401.dat", "ms66401.dat", "ms66401.dat", 0, 0, 0, 0, "MonsterBattlePostion_5A4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_664", 0x0000, 81, 6, 45, 6, 1, 40, 0, "br1530", "Sepith_4C5E", 40, 35, 25, 0,
        (
            ("ms70201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_B70", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7451", "ed7453", "ATBonus_564"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AE8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7453", "ed7453", "ATBonus_564"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B2C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7453", "ed7453", "ATBonus_564"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BB4", 0x0040, 255, 6, 45, 3, 3, 30, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88901.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_624", "ed7454", "ed7453", "ATBonus_584"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch46000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
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
        "monster/ch70250.itc",               # 10
        "monster/ch70251.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "monster/ch65750.itc",               # 14
        "monster/ch65751.itc",               # 15
        "monster/ch61150.itc",               # 16
        "monster/ch61150.itc",               # 17
        "monster/ch69750.itc",               # 18
        "monster/ch69750.itc",               # 19
        "monster/ch70850.itc",               # 1A
        "monster/ch70851.itc",               # 1B
        "monster/ch66450.itc",               # 1C
        "monster/ch66450.itc",               # 1D
    ))

    DeclNpc(4294930026, 4294966847, 4294886807, 270,  277,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294955876, 0,       4294952916, 270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294902027, 6300,    17739,   270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294955876, 0,       4294952916, 270,  484,  0x0, 0,   16,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(4294902027, 6300,    17739,   270,  484,  0x0, 0,   16,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(4294904227, 6849,    15500,   0,    484,  0x0, 0,   22,  0,   0,   3,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294951147, 4294952246, 0,       0x1010000,    "BattleInfo_700", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(4294937996, 4294939936, 0,       0x1010000,    "BattleInfo_958", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(4294939336, 4294917476, 0,       0x1010000,    "BattleInfo_890", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(4294917196, 4294925916, 0,       0x1010000,    "BattleInfo_7C8", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(4294905896, 7360,    6300,    0x1010000,    "BattleInfo_700", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(4294896486, 4294914886, 4294965196, 0x1010000,    "BattleInfo_7C8", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(4294883526, 4294912056, 4294965196, 0x1010000,    "BattleInfo_7C8", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(4294911796, 4294886016, 4294966426, 0x1010000,    "BattleInfo_958", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(4294927896, 4294901977, 4294966596, 0x1010000,    "BattleInfo_700", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(4294947266, 4294882856, 4294966596, 0x1010000,    "BattleInfo_890", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(4294897026, 4294930966, 0,       0x1010000,    "BattleInfo_A20", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(4294939116, 4294953856, 0,       0x1010000,    "BattleInfo_664", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294890246, 4294901856, 4294965196, 0x1010000,    "BattleInfo_664", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 16,  -74.0,                 -45.0,                 -2.5,                  441.0,                 [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   5.285714626312256,     15.0,                  0.5,                   1.0])
    DeclEvent(0x0000, 0, 18,  2.9100000858306885,    -95.0,                 -1.7000000476837158,   324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.9700000286102295,   7.9166669845581055,    0.3400000035762787,    1.0])

    DeclActor(4294940166, 0,       4294914546, 1200,    4294940166, 1000,    4294914546, 0x007C, 0,  6,  0x0000)
    DeclActor(4294904226, 6350,    15500,   1200,    4294904226, 7350,    15500,   0x007C, 0,  7,  0x0000)
    DeclActor(4294930956, 4294966596, 4294902176, 1200,    4294930956, 300,     4294902176, 0x007C, 0,  8,  0x0000)
    DeclActor(4294955876, 0,       4294952916, 1200,    4294955876, 0,       4294952916, 0x007C, 0,  9,  0x0000)
    DeclActor(4294902027, 6300,    17740,   1200,    4294902027, 6300,    17740,   0x007C, 0,  10, 0x0000)
    DeclActor(4294930056, 4294966886, 4294887626, 1200,    4294924406, 4294964496, 4294888626, 0x007C, 0,  15, 0x0000)
    DeclActor(4294964846, 4294966596, 4294875286, 1500,    4294964846, 1000,    4294875286, 0x007C, 0,  24, 0x0000)

    PlaceName(27.450000762939453, 0.0, 1.25, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(26.0, 0.0, -92.0, 0x0000, 0x0000, "To St. Ursula Medical College")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_CEC",          # 00, 0
        "Function_1_DA4",          # 01, 1
        "Function_2_DC3",          # 02, 2
        "Function_3_DE2",          # 03, 3
        "Function_4_E01",          # 04, 4
        "Function_5_1388",         # 05, 5
        "Function_6_19B3",         # 06, 6
        "Function_7_1B1C",         # 07, 7
        "Function_8_1D37",         # 08, 8
        "Function_9_1E88",         # 09, 9
        "Function_10_21E4",        # 0A, 10
        "Function_11_2540",        # 0B, 11
        "Function_12_256F",        # 0C, 12
        "Function_13_2573",        # 0D, 13
        "Function_14_32CC",        # 0E, 14
        "Function_15_3379",        # 0F, 15
        "Function_16_3617",        # 10, 16
        "Function_17_39F2",        # 11, 17
        "Function_18_3F8A",        # 12, 18
        "Function_19_40CC",        # 13, 19
        "Function_20_4769",        # 14, 20
        "Function_21_47F8",        # 15, 21
        "Function_22_4A4C",        # 16, 22
        "Function_23_4ADA",        # 17, 23
        "Function_24_4B36",        # 18, 24
    ))


    def Function_0_CEC(): pass

    label("Function_0_CEC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_D2C"),
        (1, "loc_D38"),
        (2, "loc_D44"),
        (3, "loc_D50"),
        (4, "loc_D5C"),
        (5, "loc_D68"),
        (6, "loc_D74"),
        (SWITCH_DEFAULT, "loc_D80"),
    )


    label("loc_D2C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D38")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D44")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D50")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D5C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D68")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D74")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D80")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_DA3")

    Return()

    # Function_0_CEC end

    def Function_1_DA4(): pass

    label("Function_1_DA4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DC2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_DA4")

    label("loc_DC2")

    Return()

    # Function_1_DA4 end

    def Function_2_DC3(): pass

    label("Function_2_DC3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DE1")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_DC3")

    label("loc_DE1")

    Return()

    # Function_2_DC3 end

    def Function_3_DE2(): pass

    label("Function_3_DE2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E00")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_3_DE2")

    label("loc_E00")

    Return()

    # Function_3_DE2 end

    def Function_4_E01(): pass

    label("Function_4_E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_E1B")
    SetChrPos(0x8, -37300, -440, -76070, 270)

    label("loc_E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E2E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_EC8")

    label("loc_E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_E45")
    SetChrFlags(0x8, 0x80)

    label("loc_E45")

    Jump("loc_EC8")

    label("loc_E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E58")
    Jump("loc_EC8")

    label("loc_E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E66")
    Jump("loc_EC8")

    label("loc_E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E74")
    Jump("loc_EC8")

    label("loc_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E82")
    Jump("loc_EC8")

    label("loc_E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E90")
    Jump("loc_EC8")

    label("loc_E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E9E")
    Jump("loc_EC8")

    label("loc_E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EAC")
    Jump("loc_EC8")

    label("loc_EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EBA")
    Jump("loc_EC8")

    label("loc_EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_EC8")
    SetChrFlags(0x8, 0x80)

    label("loc_EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_ED7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)

    label("loc_ED7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1384")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6D")
    SetScenarioFlags(0x38, 0)

    label("loc_F6D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F83")
    SetScenarioFlags(0x38, 1)

    label("loc_F83")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F99")
    SetScenarioFlags(0x38, 2)

    label("loc_F99")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAF")
    SetScenarioFlags(0x38, 3)

    label("loc_FAF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC5")
    SetScenarioFlags(0x38, 4)

    label("loc_FC5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDB")
    SetScenarioFlags(0x38, 5)

    label("loc_FDB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF1")
    SetScenarioFlags(0x38, 6)

    label("loc_FF1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1007")
    SetScenarioFlags(0x38, 7)

    label("loc_1007")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101D")
    SetScenarioFlags(0x39, 0)

    label("loc_101D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1033")
    SetScenarioFlags(0x39, 1)

    label("loc_1033")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1049")
    SetScenarioFlags(0x39, 2)

    label("loc_1049")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105F")
    SetScenarioFlags(0x39, 3)

    label("loc_105F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1075")
    SetScenarioFlags(0x39, 4)

    label("loc_1075")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108B")
    SetScenarioFlags(0x39, 5)

    label("loc_108B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A1")
    SetScenarioFlags(0x39, 6)

    label("loc_10A1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B7")
    SetScenarioFlags(0x39, 7)

    label("loc_10B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CD")
    SetScenarioFlags(0x3A, 0)

    label("loc_10CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E3")
    SetScenarioFlags(0x3A, 1)

    label("loc_10E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F9")
    SetScenarioFlags(0x3A, 2)

    label("loc_10F9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110F")
    SetScenarioFlags(0x3A, 3)

    label("loc_110F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1125")
    SetScenarioFlags(0x3A, 4)

    label("loc_1125")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113B")
    SetScenarioFlags(0x3A, 5)

    label("loc_113B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1151")
    SetScenarioFlags(0x3A, 6)

    label("loc_1151")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1167")
    SetScenarioFlags(0x3A, 7)

    label("loc_1167")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117D")
    SetScenarioFlags(0x3B, 0)

    label("loc_117D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1193")
    SetScenarioFlags(0x3B, 1)

    label("loc_1193")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A9")
    SetScenarioFlags(0x3B, 2)

    label("loc_11A9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BF")
    SetScenarioFlags(0x3B, 3)

    label("loc_11BF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D5")
    SetScenarioFlags(0x3B, 4)

    label("loc_11D5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EB")
    SetScenarioFlags(0x3B, 5)

    label("loc_11EB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1201")
    SetScenarioFlags(0x3B, 6)

    label("loc_1201")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1217")
    SetScenarioFlags(0x3B, 7)

    label("loc_1217")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122D")
    SetScenarioFlags(0x3D, 5)

    label("loc_122D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1243")
    SetScenarioFlags(0x3D, 6)

    label("loc_1243")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1259")
    SetScenarioFlags(0x3D, 7)

    label("loc_1259")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1294")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1384")

    label("loc_1294")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B7")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1384")

    label("loc_12B7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DA")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1384")

    label("loc_12DA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FD")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1384")

    label("loc_12FD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1320")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1384")

    label("loc_1320")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1343")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1384")

    label("loc_1343")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1366")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1384")

    label("loc_1366")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1384")
    SetScenarioFlags(0x3C, 7)

    label("loc_1384")

    Call(0, 11)
    Return()

    # Function_4_E01 end

    def Function_5_1388(): pass

    label("Function_5_1388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_139A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_139A")

    SoundDistance(0x7B, 0xFFFF4174, 0xFFFFFACE, 0xFFFEFDA4, 0x1770, 0xC350, 0x64, 0x0)
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_173C")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xBE, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_173C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_17A3")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xBE, 0x0)
    SetMapObjFrame(0xFF, "allback", 0x2, "gray")
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    Jump("loc_17D3")

    label("loc_17A3")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)

    label("loc_17D3")

    SetMapObjFlags(0x10, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17ED")
    ClearMapObjFlags(0x10, 0x4)

    label("loc_17ED")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -42890, -2800, -78670, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1851")
    OP_66(0x5, 0x1)

    label("loc_1851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1864")
    OP_70(0x0, 0x0)
    Jump("loc_1868")

    label("loc_1864")

    OP_70(0x0, 0x1E)

    label("loc_1868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187B")
    OP_70(0x1, 0x0)
    Jump("loc_187F")

    label("loc_187B")

    OP_70(0x1, 0x1E)

    label("loc_187F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1892")
    OP_70(0x2, 0x0)
    Jump("loc_1896")

    label("loc_1892")

    OP_70(0x2, 0x1E)

    label("loc_1896")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18F7")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -11420, 0, -14380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_18F7")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1943")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -65269, 6300, 17740, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1943")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_195B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_195B")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1973")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1986")
    OP_1B(0x1, 0x0, 0x14)

    label("loc_1986")

    OP_1C(0x0, 0xB, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0xC, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0xD, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0xE, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    Return()

    # Function_5_1388 end

    def Function_6_19B3(): pass

    label("Function_6_19B3")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AEC")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 60)
    AddSepith(0x1, 60)
    AddSepith(0x2, 60)
    AddSepith(0x3, 60)
    AddSepith(0x4, 60)
    AddSepith(0x5, 60)
    AddSepith(0x6, 60)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I Earth Sepith  x60\x01\x07\x02",
            "#57I Water Sepith  x60\x01\x07\x02",
            "#58I Fire Sepith   x60\x01\x07\x02",
            "#59I Wind Sepith   x60\x01\x07\x02",
            "#60I Time Sepith   x60\x01\x07\x02",
            "#61I Space Sepith  x60\x01\x07\x02",
            "#62I Mirage Sepith x60\x01\x07\x00",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1EC, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1B0A")

    label("loc_1AEC")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest is empty.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1B0A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_19B3 end

    def Function_7_1B1C(): pass

    label("Function_7_1B1C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CED")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1F")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1B79():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B79)

    def lambda_1B93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1B93)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xD, 1)
    Battle("BattleInfo_B70", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1C00"),
        (2, "loc_1C0F"),
        (1, "loc_1C1C"),
        (SWITCH_DEFAULT, "loc_1C1F"),
    )


    label("loc_1C00")

    SetScenarioFlags(0x216, 6)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1C1F")

    label("loc_1C0F")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1C1C")

    OP_B9(0x0)
    Return()

    label("loc_1C1F")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xB6, 1)"), scpexpr(EXPR_END)), "loc_1C78")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1CE8")

    label("loc_1C78")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB6),
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

    label("loc_1CE8")

    Jump("loc_1D2B")

    label("loc_1CED")

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

    label("loc_1D2B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1B1C end

    def Function_8_1D37(): pass

    label("Function_8_1D37")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E33")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1DBC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1E2E")

    label("loc_1DBC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
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

    label("loc_1E2E")

    Jump("loc_1E7C")

    label("loc_1E33")

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

    label("loc_1E7C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1D37 end

    def Function_9_1E88(): pass

    label("Function_9_1E88")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_203F")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_2020")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_201B")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2018")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1F3D)
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
    Battle("BattleInfo_AE8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2013")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FFA")
    Call(1, 5)
    Jump("loc_2013")

    label("loc_1FFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2010")
    Call(1, 4)
    Jump("loc_2013")

    label("loc_2010")

    Call(1, 3)

    label("loc_2013")

    Jump("loc_201B")

    label("loc_2018")

    Call(1, 1)

    label("loc_201B")

    Jump("loc_2036")

    label("loc_2020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2036")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2036")

    TalkEnd(0xFF)
    Return()

    label("loc_203F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_21C9")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21C4")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_21C1")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_20E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_20E6)
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
    Battle("BattleInfo_B2C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21BC")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21A3")
    Call(1, 5)
    Jump("loc_21BC")

    label("loc_21A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21B9")
    Call(1, 4)
    Jump("loc_21BC")

    label("loc_21B9")

    Call(1, 3)

    label("loc_21BC")

    Jump("loc_21C4")

    label("loc_21C1")

    Call(1, 1)

    label("loc_21C4")

    Jump("loc_21DF")

    label("loc_21C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_21DF")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_21DF")

    TalkEnd(0xFF)
    Return()

    # Function_9_1E88 end

    def Function_10_21E4(): pass

    label("Function_10_21E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_239B")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_237C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2377")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_2374")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2299():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2299)
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
    Battle("BattleInfo_AE8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_236F")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2356")
    Call(1, 5)
    Jump("loc_236F")

    label("loc_2356")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_236C")
    Call(1, 4)
    Jump("loc_236F")

    label("loc_236C")

    Call(1, 3)

    label("loc_236F")

    Jump("loc_2377")

    label("loc_2374")

    Call(1, 1)

    label("loc_2377")

    Jump("loc_2392")

    label("loc_237C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_2392")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2392")

    TalkEnd(0xFF)
    Return()

    label("loc_239B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_2525")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2520")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_251D")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2442():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2442)
    TurnDirection(0xC, 0x0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    PlayEffect(0x7, 0x1, 0xC, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_B2C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2518")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24FF")
    Call(1, 5)
    Jump("loc_2518")

    label("loc_24FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2515")
    Call(1, 4)
    Jump("loc_2518")

    label("loc_2515")

    Call(1, 3)

    label("loc_2518")

    Jump("loc_2520")

    label("loc_251D")

    Call(1, 1)

    label("loc_2520")

    Jump("loc_253B")

    label("loc_2525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_253B")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_253B")

    TalkEnd(0xFF)
    Return()

    # Function_10_21E4 end

    def Function_11_2540(): pass

    label("Function_11_2540")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2558")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    label("loc_2558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 0)), scpexpr(EXPR_END)), "loc_2569")
    ClearScenarioFlags(0x3C, 0)
    Jump("loc_256E")

    label("loc_2569")

    SetChrFlags(0x19, 0x80)

    label("loc_256E")

    Return()

    # Function_11_2540 end

    def Function_12_256F(): pass

    label("Function_12_256F")

    Call(1, 6)
    Return()

    # Function_12_256F end

    def Function_13_2573(): pass

    label("Function_13_2573")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_258B")
    SetScenarioFlags(0x0, 1)

    label("loc_258B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_2597")
    SetScenarioFlags(0x0, 1)

    label("loc_2597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2848")
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Gwah ha ha, you're from\x01",
            "the Fisherman's Guild,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm Sharkman. Sharkman,\x01",
            "the Sea Edge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FSea... what?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "It's Sea Edge. Sea Edge\x01",
            "as in the edge of the\x01",
            "sea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, you're gonna have a\x01",
            ""Sudden Death Angler\x01",
            "Duel" with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Whoops, no, that's not\x01",
            "it. There was a\x01",
            "condition before that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Despite appearances, they\x01",
            "call me the best technician\x01",
            "of the Elite Four.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To fight me, you'll have\x01",
            "to catch of the fish\x01",
            "called "game fish".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you want to know\x01",
            "the species in detail, go\x01",
            "ask Sylum in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FU-Understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 5)
    OP_93(0x8, 0x10E, 0x0)

    label("loc_2848")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2852")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28AB")

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
    Jump("loc_28B5")

    label("loc_28AB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC2")
    TurnDirection(0x8, 0x0, 0)
    Call(0, 14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A63")

    ChrTalk(
        0x8,
        (
            "Hey, show me your\x01",
            "fishing notebook then!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Gwah ha ha, good! You've\x01",
            "filled the condition\x01",
            "splendidly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright, then, let's\x01",
            "have our duel at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I told you before too,\x01",
            "mine is a "Sudden Death\x01",
            "Angler Duel"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We simply swing the rod\x01",
            "alternately and the \x07\x02",
            "first who\x01",
            "fails to catch a fish, loses.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 6)
    Jump("loc_2B02")

    label("loc_2A63")


    ChrTalk(
        0x8,
        (
            "Gwah ha ha, wanna have a\x01",
            ""Sudden Death Angler\x01",
            "Duel" with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We simply swing the rod\x01",
            "alternately and the \x07\x02",
            "first who\x01",
            "fails to catch a fish, loses.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B02")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Challenge Sharkman, the\x01",
            ""Sea Edge", to a "Sudden\x01",
            "Death Angler Duel"?\x07\x00\x02",
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
        (0, "loc_2BAB"),
        (1, "loc_2DC0"),
        (SWITCH_DEFAULT, "loc_2E1D"),
    )


    label("loc_2BAB")


    ChrTalk(
        0x8,
        (
            "Gwah ha ha, let's begin\x01",
            "at once then!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E2(0x2)
    ClearMapFlags(0x1)
    OP_68(-40100, -1120, -77350, 0)
    MoveCamera(29, 40, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, -38000, -700, -95000, 182)
    OP_31(0x1)
    SetChrPos(0x101, -37300, -440, -76070, 270)
    OP_93(0x8, 0x10E, 0x1F4)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE("apl/ch51003.itc")
    MiniGame(0x7, 0x1, 0x8, 0xFFFF5F92, 0xFFFFF510, 0xFFFED0EA, 0xFFFF5EFC, 0xFFFFF510, 0xFFFEC370)
    SetChrPos(0x0, -53410, 0, 15290, 226)
    OP_31(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CFC")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_68(-34670, -440, -78930, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -35530, -450, -80410, 270)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(500)
    Call(0, 21)
    Return()

    label("loc_2CFC")

    OP_68(-36530, -1120, -76470, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -37300, -440, -76070, 180)
    OP_93(0xFE, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5B")
    Call(0, 22)
    Jump("loc_2D7F")

    label("loc_2D5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6E")
    Jump("loc_2D7F")

    label("loc_2D6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7F")
    Call(0, 23)

    label("loc_2D7F")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_93(0x8, 0x10E, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -37300, -440, -76070, 180)
    OP_31(0x1)
    SetMapFlags(0x1)
    OP_69(0xFF, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_2E1D")

    label("loc_2DC0")


    ChrTalk(
        0x8,
        "Huh? I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you don't wanna\x01",
            "do it, it can't be\x01",
            "helped, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)
    Jump("loc_2E1D")

    label("loc_2E1D")

    Jump("loc_2FBD")

    label("loc_2E22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2EFE")

    ChrTalk(
        0x8,
        (
            "Hey, show me your\x01",
            "fishing notebook then!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "Well, you get an A for\x01",
            "effort. You're still\x01",
            "missing a few, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Go collect all the game\x01",
            "fish I love greatly!!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)
    Jump("loc_2FBD")

    label("loc_2EFE")


    ChrTalk(
        0x8,
        (
            "Hey, show me your\x01",
            "fishing notebook then!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "The heck is this? You've\x01",
            "got still a long way to\x01",
            "go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Go catch all the game\x01",
            "fish I greatly love at\x01",
            "once!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)

    label("loc_2FBD")

    Jump("loc_32C3")

    label("loc_2FC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FF3")
    Jump("loc_32C3")

    label("loc_2FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3043")

    ChrTalk(
        0x8,
        (
            "I aaam Shaarkmaaan. The\x01",
            "technician loooved by\x01",
            "the oooceaaan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C3")

    label("loc_3043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_308E")

    ChrTalk(
        0x8,
        (
            "Getting hit by the\x01",
            "raaain... A maan becomes\x01",
            "stroongeer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C3")

    label("loc_308E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_30E1")

    ChrTalk(
        0x8,
        (
            "Huumaaans, eeverythiing,\x01",
            "are brooothers boorn\x01",
            "frooom thee seea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C3")

    label("loc_30E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_313B")

    ChrTalk(
        0x8,
        (
            "A maaan of the seeea, can\x01",
            "staay siilent aand\x01",
            "speeeak with hiis baaack.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C3")

    label("loc_313B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31A4")

    ChrTalk(
        0x8,
        (
            "Hard-a-pooort, hard-a-\x01",
            "dreeeams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm a maaan, who sold\x01",
            "his liiife for a\x01",
            "dreeaam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C3")

    label("loc_31A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_320B")

    ChrTalk(
        0x8,
        (
            "I'm Shaarkmaaan. I puuut\x01",
            "out my boooat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the stormy seeea,\x01",
            "called wooorld.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C3")

    label("loc_320B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32AC")

    ChrTalk(
        0x8,
        (
            "I'm Shaarkmaaan. A maan\x01",
            "of the seeea.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32A7")

    ChrTalk(
        0x101,
        (
            "#00003F(It seems I could fish\x01",
            "here, but... Since there's\x01",
            "already someone, I won't.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32A7")

    Jump("loc_32C3")

    label("loc_32AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32BA")
    Jump("loc_32C3")

    label("loc_32BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_32C3")

    label("loc_32C3")

    Jump("loc_2852")

    label("loc_32C8")

    TalkEnd(0xFE)
    Return()

    # Function_13_2573 end

    def Function_14_32CC(): pass

    label("Function_14_32CC")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32F1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_330C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_330C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3327")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3327")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3342")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3342")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_335D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_335D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3378")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3378")

    Return()

    # Function_14_32CC end

    def Function_15_3379(): pass

    label("Function_15_3379")

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
    OP_68(-42270, 170, -79360, 1500)
    MoveCamera(45, 28, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(19500, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3612")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3452")
    MiniGame(0x6, 0xF, 0xFFFF6E88, 0xFFFFFE66, 0xFFFEC8CA, 0x10E, 0xFFFF5876, 0xFFFFF510, 0xFFFECCB2)
    Jump("loc_3612")

    label("loc_3452")

    MiniGame(0x6, 0x10, 0xFFFF6E88, 0xFFFFFE66, 0xFFFEC8CA, 0x10E, 0xFFFF5876, 0xFFFFF510, 0xFFFECCB2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3612")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3612")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(-36950, 170, -79060, 0)
    MoveCamera(29, 26, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16720, 0)
    LoadChrToIndex("apl/ch50163.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, -37240, -410, -79670, 270)
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
            "#00011FW-Whoa... What a\x01",
            "ferocious-looking fish.\x02\x03",
            "#00003FIt resembles a piranha,\x01",
            "but... Could it be a\x01",
            "peculiar fish?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, -37240, -410, -79670, 270)
    SetChrPos(0x2, -37240, -410, -79670, 270)
    SetChrPos(0x3, -37240, -410, -79670, 270)
    SetChrPos(0x4, -37240, -410, -79670, 270)
    SetChrPos(0x5, -37240, -410, -79670, 270)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_37()
    SetScenarioFlags(0x18B, 2)

    label("loc_3612")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_15_3379 end

    def Function_16_3617(): pass

    label("Function_16_3617")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch03150.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadEffect(0x0, "battle\\cr036301.eff")
    ClearChrFlags(0xE, 0x80)
    OP_78(0xF, 0xE)
    OP_49()
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_71(0xF, 0xA, 0x32, 0x1, 0x20)
    OP_75(0xF, 0x1, 0x0)
    SetMapObjFrame(0xFF, "tree", 0x0, 0x1)
    SetMapObjFrame(0xFF, "wood01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E1")
    SetChrPos(0x101, -77200, -2100, -46800, 180)
    SetChrPos(0x105, -75950, -2100, -46300, 180)
    SetChrPos(0x107, -77650, -2100, -45600, 180)
    SetChrPos(0xE, -76750, -2100, -56600, 0)
    OP_68(-77200, -1500, -51000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30500, 0)
    OP_68(-77200, -1500, -52150, 3000)
    MoveCamera(45, 30, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(28000, 3000)

    def lambda_3763():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3763)
    Sleep(50)

    def lambda_377B():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_377B)
    Sleep(50)

    def lambda_3793():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3793)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    Sound(919, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0xE, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 1000)
    Sleep(100)
    SetChrSubChip(0x107, 0x5)
    Sleep(900)
    OP_75(0xF, 0x2, 0x3E8)
    CancelBlur(1000)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x1F)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x20)
    SetChrSubChip(0x107, 0x0)
    OP_0D()
    OP_71(0xF, 0x48, 0x5B, 0x1, 0x8)
    OP_79(0xF)

    def lambda_3899():
        OP_9B(0x1, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3899)
    OP_74(0xF, 0xA)
    Sound(842, 0, 100, 0)
    OP_71(0xF, 0x5B, 0x5F, 0x1, 0x8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    SetCameraDistance(23500, 200)
    Sleep(200)
    Jump("loc_397C")

    label("loc_38E1")

    SetChrPos(0x101, -77200, -2100, -49800, 180)
    SetChrPos(0x105, -75950, -2100, -49300, 180)
    SetChrPos(0x107, -77650, -2100, -48600, 180)
    SetChrPos(0xE, -76750, -2100, -56600, 0)
    OP_75(0xF, 0x2, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x1F)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x20)
    SetChrSubChip(0x107, 0x0)
    OP_68(-77200, -1500, -52150, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(28000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_397C")

    Battle("BattleInfo_BB4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    SetMapObjFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39EE")
    SetScenarioFlags(0x1A9, 7)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    OP_49()
    OP_37()
    SetChrPos(0x0, -73500, -600, -40000, 0)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_39F1")

    label("loc_39EE")

    Call(0, 17)

    label("loc_39F1")

    Return()

    # Function_16_3617 end

    def Function_17_39F2(): pass

    label("Function_17_39F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch03150.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x1F)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x20)
    SetChrSubChip(0x107, 0x0)
    SetChrPos(0x101, -76500, -2100, -55450, 180)
    SetChrPos(0x105, -75050, -2100, -53150, 180)
    SetChrPos(0x107, -77050, -2100, -52500, 180)
    OP_68(-76500, -1100, -56000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    OP_68(-76450, -1100, -54000, 3000)
    SetCameraDistance(19500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x5)
    OP_0D()

    def lambda_3ADA():
        OP_92(0x101, 0xFFFED55E, 0xFFFF2D10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3ADA)
    Sleep(50)

    def lambda_3AF0():
        OP_92(0x105, 0xFFFED55E, 0xFFFF2D10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3AF0)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    SetChrSubChip(0x107, 0x5)

    ChrTalk(
        0x101,
        (
            "#00006F#12P*sigh*... That was out of the\x01",
            "blue.\x02\x03",
            "#00013FBut with things like that\x01",
            "around, can buses really make it\x01",
            "from the city to the hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PThat might be difficult.\x02\x03",
            "#10408FThose State Guard armored\x01",
            "cars seem like they could\x01",
            "make it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PIn that case, it's\x01",
            "possible citizen health\x01",
            "is suffering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CHmm. It's simple cause\x01",
            "and effect.\x02\x03",
            "If Ursula saw this, I'm\x01",
            "sure she'd grieve.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3CF3():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3CF3)
    Sleep(0)

    def lambda_3D03():
        TurnDirection(0x105, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D03)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00005F#12PUrsula you say... The\x01",
            "one from "The Saint and\x01",
            "the White Wolf"?\x02\x03",
            "#00011FWait, so the white wolf\x01",
            "was really you, Zeit!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11PThe healer girl who\x01",
            "punished a middle age\x01",
            "feudal lord, eh?\x02\x03",
            "#10400FIn the church, she's\x01",
            "basically a saint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CYes, she was a compassionate\x01",
            "young girl.\x02\x03",
            "#01200FBy the way, in the story she\x01",
            "dies, but in truth she escaped\x01",
            "death...\x02\x03",
            "Later, she married the knight\x01",
            "for life and their descendants\x01",
            "still live in these lands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#12PI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10409F#11PAhaha. Truth is stranger\x01",
            "than fiction.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_37()
    SetChrPos(0x0, -76500, -2100, -55450, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A0, 3)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_39F2 end

    def Function_18_3F8A(): pass

    label("Function_18_3F8A")

    EventBegin(0x0)
    OP_E2(0x3)
    OP_68(3370, -100, -96510, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0x101, -840, -700, -98050, 90)
    SetChrPos(0x105, -1380, -700, -96700, 90)
    SetChrPos(0x107, -3500, -700, -97500, 90)
    Fade(500)

    def lambda_3FF9():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3FF9)
    Sleep(50)

    def lambda_4011():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4011)
    Sleep(50)

    def lambda_4029():
        OP_9B(0x0, 0x107, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_4029)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#5P(That's...)\x02",
    )

    CloseMessageWindow()
    OP_68(9880, -100, -96020, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_3F8A end

    def Function_19_40CC(): pass

    label("Function_19_40CC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_68(3370, -100, -96510, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0x101, 2590, -700, -94990, 90)
    SetChrPos(0x105, 1520, -700, -94950, 90)
    SetChrPos(0x107, 880, -700, -93770, 90)
    SetChrSubChip(0x107, 0x5)
    OP_68(3140, -500, -93460, 0)
    MoveCamera(56, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(20000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#5P...As you might expect,\x01",
            "we can't let the State\x01",
            "Guard find us here, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#6PWell, it would be safer\x01",
            "to avoid them if we\x01",
            "could.\x02\x03",
            "#10408FAlthough we don't know\x01",
            "when they'll leave the\x01",
            "area.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0x1C2, 2100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x107)
    Sleep(500)

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3C...Hmm.\x02\x03",
            "#01200FIt seems Tio is in the\x01",
            "hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_42F0():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42F0)
    Sleep(50)

    def lambda_4300():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4300)

    ChrTalk(
        0x101,
        "#00007F#11PWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10401F#12PSeriously...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CYes, I faintly sense her\x01",
            "smell.\x02\x03",
            "#01201FAlthough, the other\x01",
            "Support Section members\x01",
            "don't appear to be here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PNo way... Tio...?\x02\x03",
            "#00010FWas she was hurt and\x01",
            "hospitalized?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#5P#3CHmm. Even my nose can't\x01",
            "tell you that much,\x01",
            "but...\x02\x03",
            "#01203FEven so, it is a little\x01",
            "worrying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PUgh, what should we\x01",
            "do...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x105)
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#10403F#6P...I have a little trick up\x01",
            "my sleeve.\x02\x03",
            "#10400FWe may be able to engage the\x01",
            "soldiers here without them\x01",
            "calling for reinforcements.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x1B8, 2100, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4588():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4588)
    Sleep(50)
    SetChrFlags(0x107, 0x20)
    OP_93(0x107, 0xB4, 0x1F4)
    ClearChrFlags(0x107, 0x20)

    ChrTalk(
        0x101,
        "#00005F#11PR-Really...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#5P#3CHmm. It seems you have\x01",
            "some way of dealing with\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PHehe, more or less.\x02\x03",
            "#10402FSo what's the plan,\x01",
            "Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P...You don't even have\x01",
            "to ask. We're going in.\x02\x03",
            "#00013FWe have to see what's\x01",
            "going on with Tio, no\x01",
            "matter what!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01201F#5P#3CYes, let's do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PThen let's settle this\x01",
            "at lightning speed.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 960, -700, -97990, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A0, 4)
    ModifyEventFlags(0, 1, 0x80)
    OP_1B(0x1, 0x0, 0x14)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_19_40CC end

    def Function_20_4769(): pass

    label("Function_20_4769")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Charge!\x01",              # 0
            "Prepare for now\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_47BD"),
        (1, "loc_47DF"),
        (SWITCH_DEFAULT, "loc_47F7"),
    )


    label("loc_47BD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_47F7")

    label("loc_47DF")

    SetChrPos(0x0, 2500, -700, -97500, 270)
    EventEnd(0x5)
    Jump("loc_47F7")

    label("loc_47F7")

    Return()

    # Function_20_4769 end

    def Function_21_47F8(): pass

    label("Function_21_47F8")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "I'd never thought I'd\x01",
            "lose to some cake-eater\x01",
            "like you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Here, take this. It's\x01",
            "proof you won against\x01",
            "me.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x28),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x28, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00012FT-Thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well then, with this,\x01",
            "you're the "Sea Edge\x01",
            "Buster" from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Still... Don't get too\x01",
            "carried away, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm Sharkman, the "Sea\x01",
            "Edge". In other words, a\x01",
            "man of the sea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If this had been sea\x01",
            "fishing, I'd never lose\x01",
            "to someone like you!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, -37300, -440, -76070, 270)
    OP_66(0x5, 0x1)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x1C0, 6)
    SetChrPos(0x0, -35530, -450, -80410, 315)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_21_47F8 end

    def Function_22_4A4C(): pass

    label("Function_22_4A4C")


    ChrTalk(
        0x8,
        (
            "Gwah ha ha, and with that,\x01",
            "I win the match, but no\x01",
            "need to fret about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's just because I'm\x01",
            "way too strong! Gwah ha\x01",
            "ha ha hah!\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_22_4A4C end

    def Function_23_4ADA(): pass

    label("Function_23_4ADA")


    ChrTalk(
        0x8,
        (
            "Hey there, you're giving\x01",
            "up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tch, oh, whatever. Next\x01",
            "time it won't go like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_23_4ADA end

    def Function_24_4B36(): pass

    label("Function_24_4B36")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "East - St. Ursula Medical College\x01",
            "North - Crossbell City  153 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_4B36 end

    SaveToFile()

Try(main)
