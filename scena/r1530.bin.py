﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1530.bin",                # FileName
        "r1530",                    # MapName
        "r1530",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r1530", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x0C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 4800, 0, 35500, 180, 0, 1, 96, 0, 3, 0, 4],
    )

    BuildStringList((
        "r1530",                  # 0
        "Lakelord III",           # 1
        "Peter",                  # 2
        "Coppen",                 # 3
        "バス",                   # 4
        "ケサラン",               # 5
        "ケサラン",               # 6
        "ゴーディ・オッサー",     # 7
        "ゴーディ・オッサー",     # 8
        "Cryptid",                # 9
        "ナデリア茸",             # 10
        "Branch Manager Celdan",  # 11
        "Leader Fisher",          # 12
        "Triton, the Silver Orca",# 13
        "Kaguya, the Dragon Queen",# 14
        "Narses, the Crazy Wave", # 15
        "Sharkman, the Sea Edge", # 16
        "br1500",                 # 17
        "br1520",                 # 18
        "br1500",                 # 19
        "br1520",                 # 20
        "br1500",                 # 21
        "br1500",                 # 22
        "br1520",                 # 23
        "br1500",                 # 24
        "br1500",                 # 25
        "br1500",                 # 26
        "To Crossbell City",      # 27
        "To St. Ursula Medical College",# 28
    ))

    ATBonus("ATBonus_6D8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_6F8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_5AE2", 3,   10,  0,   8,   3,   0,   0)
    Sepith("Sepith_5ABA", 0,   10,  0,   7,   4,   3,   0)
    Sepith("Sepith_5ADA", 6,   4,   9,   4,   0,   0,   0)
    Sepith("Sepith_5ACA", 0,   5,   0,   0,   6,   6,   6)
    Sepith("Sepith_5AD2", 0,   10,  0,   5,   2,   4,   2)
    Sepith("Sepith_5AAA", 5,   3,   0,   8,   0,   4,   3)

    MonsterBattlePostion("MonsterBattlePostion_738", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_73C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_740", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_744", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_748", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_74C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_750", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_754", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_798", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_79C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_7A4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_7A8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_7AC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_718", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_72C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_730", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_734", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D4", 0, 0, 180)

    # monster count: 15

    BattleInfo(
        "BattleInfo_AF8", 0x0000, 58, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_5AE2", 30, 40, 20, 10,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_968", 0x0010, 58, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_5ABA", 30, 40, 20, 10,
        (
            ("ms63600.dat", 0, 0, 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms63600.dat", "ms63600.dat", 0, 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_C88", 0x0000, 58, 6, 45, 10, 1, 50, 0, "br1520", "Sepith_5ADA", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_8A0", 0x0000, 58, 6, 45, 10, 1, 40, 0, "br1520", "Sepith_5ACA", 30, 40, 20, 10,
        (
            ("ms65200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_A30", 0x0000, 58, 6, 45, 10, 1, 30, 0, "br1520", "Sepith_5AD2", 30, 40, 20, 10,
        (
            ("ms61300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_7D8", 0x0000, 58, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_5AAA", 30, 40, 20, 10,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_718", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    BattleInfo(
        "BattleInfo_BC0", 0x0000, 58, 6, 45, 10, 1, 50, 0, "br1500", "Sepith_5ADA", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7450", "ed7453", "ATBonus_6D8"),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_D50", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7453", "ed7453", "ATBonus_6D8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D94", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "MonsterBattlePostion_738", "MonsterBattlePostion_798", "ed7453", "ed7453", "ATBonus_6D8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_DD8", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88901.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7B8", "MonsterBattlePostion_798", "ed7454", "ed7453", "ATBonus_6F8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch45600.itc",                   # 00
        "chr/ch45400.itc",                   # 01
        "apl/ch50165.itc",                   # 02
        "apl/ch50166.itc",                   # 03
        "apl/ch51017.itc",                   # 04
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
        "monster/ch62150.itc",               # 10
        "monster/ch62151.itc",               # 11
        "monster/ch65250.itc",               # 12
        "monster/ch65251.itc",               # 13
        "monster/ch63650.itc",               # 14
        "monster/ch63650.itc",               # 15
        "monster/ch61350.itc",               # 16
        "monster/ch61350.itc",               # 17
        "monster/ch69750.itc",               # 18
        "monster/ch69750.itc",               # 19
        "monster/ch65350.itc",               # 1A
        "monster/ch65351.itc",               # 1B
        "monster/ch70250.itc",               # 1C
        "monster/ch70251.itc",               # 1D
    ))

    DeclNpc(46709,   4294960996, 4294908537, 95,   389,  0x0, 0,   0,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(47180,   4294961007, 4294910127, 90,   405,  0x0, 0,   2,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(43380,   4294961016, 4294904826, 180,  405,  0x0, 0,   3,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(28200,   4294961697, 4294935037, 270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294950116, 4294961796, 4294864197, 270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(28200,   4294961697, 4294935037, 270,  484,  0x0, 0,   28,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(4294950116, 4294961796, 4294864197, 270,  484,  0x0, 0,   28,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4930,    10160,   0,       0x1010000,    "BattleInfo_AF8", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294934156, 4294962366, 0,       0x1010000,    "BattleInfo_968", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294928846, 4294935786, 4294964496, 0x1010000,    "BattleInfo_968", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294949756, 4294929126, 4294961696, 0x1010000,    "BattleInfo_C88", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294962236, 4294953966, 4294960996, 0x1010000,    "BattleInfo_8A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4200,    4294946746, 4294960996, 0x1010000,    "BattleInfo_A30", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(2370,    4294924786, 4294960996, 0x1010000,    "BattleInfo_8A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(19970,   4294917986, 4294960996, 0x1010000,    "BattleInfo_A30", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(33630,   4294943736, 4294961696, 0x1010000,    "BattleInfo_8A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(52410,   4294939066, 4294961696, 0x1010000,    "BattleInfo_A30", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294928486, 4294915236, 4294963096, 0x1010000,    "BattleInfo_7D8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294945706, 4294917386, 4294963096, 0x1010000,    "BattleInfo_7D8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294937246, 4294859096, 4294962396, 0x1010000,    "BattleInfo_AF8", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294951226, 4294858986, 4294961526, 0x1010000,    "BattleInfo_BC0", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(4294952296, 4294875116, 4294961526, 0x1010000,    "BattleInfo_BC0", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 24,  42.25,                 -21.75,                -5.599999904632568,    324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -14.083333969116211,   1.8125,                1.1200000047683716,    1.0])
    DeclEvent(0x0040, 0, 22,  -38.16999816894531,    -33.31999969482422,    -3.799999952316284,    16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   4.771249771118164,     4.164999961853027,     0.949999988079071,     1.0])

    DeclActor(4294942446, 0,       4294964376, 1200,    4294942446, 1000,    4294964376, 0x007C, 0,  21, 0x0000)
    DeclActor(36340,   4294961696, 4294927546, 1200,    36340,   4294962696, 4294927546, 0x007C, 0,  5,  0x0000)
    DeclActor(49800,   4294961696, 4294949846, 1200,    49800,   4294962696, 4294949846, 0x007C, 0,  6,  0x0000)
    DeclActor(4294952796, 4294961496, 4294878976, 1200,    4294952796, 4294962496, 4294878976, 0x007C, 0,  7,  0x0000)
    DeclActor(28200,   4294961696, 4294935037, 1200,    28200,   4294961696, 4294935037, 0x007C, 0,  8,  0x0000)
    DeclActor(4294950116, 4294961796, 4294864196, 1200,    4294950116, 4294961796, 4294864196, 0x007C, 0,  9,  0x0000)
    DeclActor(36400,   4294961006, 4294899866, 1200,    35830,   4294961496, 4294892336, 0x007C, 0,  23, 0x0000)
    DeclActor(4294948566, 0,       4294967286, 1200,    4294948566, 2000,    4294967286, 0x007C, 0,  20, 0x0000)

    PlaceName(7.0, 0.0, 52.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-89.0, 0.0, -115.0, 0x0000, 0x0000, "To St. Ursula Medical College")
    PlaceName(-24.700000762939453, 0.0, -2.950000047683716, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5, 6, 7])              # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 11

    ScpFunction((
        "Function_0_F24",          # 00, 0
        "Function_1_FDC",          # 01, 1
        "Function_2_FFB",          # 02, 2
        "Function_3_101A",         # 03, 3
        "Function_4_15D1",         # 04, 4
        "Function_5_1AF9",         # 05, 5
        "Function_6_1C4B",         # 06, 6
        "Function_7_1D9D",         # 07, 7
        "Function_8_1EEF",         # 08, 8
        "Function_9_224D",         # 09, 9
        "Function_10_25AB",        # 0A, 10
        "Function_11_25C4",        # 0B, 11
        "Function_12_25C8",        # 0C, 12
        "Function_13_2695",        # 0D, 13
        "Function_14_27C8",        # 0E, 14
        "Function_15_28FB",        # 0F, 15
        "Function_16_294C",        # 10, 16
        "Function_17_29E0",        # 11, 17
        "Function_18_2A78",        # 12, 18
        "Function_19_2D7B",        # 13, 19
        "Function_20_2DEA",        # 14, 20
        "Function_21_3123",        # 15, 21
        "Function_22_3177",        # 16, 22
        "Function_23_31F3",        # 17, 23
        "Function_24_3313",        # 18, 24
        "Function_25_38A9",        # 19, 25
        "Function_26_3CB0",        # 1A, 26
        "Function_27_3D12",        # 1B, 27
        "Function_28_3D76",        # 1C, 28
        "Function_29_44AE",        # 1D, 29
    ))


    def Function_0_F24(): pass

    label("Function_0_F24")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_F64"),
        (1, "loc_F70"),
        (2, "loc_F7C"),
        (3, "loc_F88"),
        (4, "loc_F94"),
        (5, "loc_FA0"),
        (6, "loc_FAC"),
        (SWITCH_DEFAULT, "loc_FB8"),
    )


    label("loc_F64")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_F70")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_F7C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_F88")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_F94")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_FA0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_FAC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_FB8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_FC4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FDB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_FC4")

    label("loc_FDB")

    Return()

    # Function_0_F24 end

    def Function_1_FDC(): pass

    label("Function_1_FDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FFA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_1_FDC")

    label("loc_FFA")

    Return()

    # Function_1_FDC end

    def Function_2_FFB(): pass

    label("Function_2_FFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1019")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_FFB")

    label("loc_1019")

    Return()

    # Function_2_FFB end

    def Function_3_101A(): pass

    label("Function_3_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1032")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_10E8")

    label("loc_1032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1040")
    Jump("loc_10E8")

    label("loc_1040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_105C")
    ClearChrFlags(0x8, 0x80)

    label("loc_105C")

    Jump("loc_10E8")

    label("loc_1061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_106F")
    Jump("loc_10E8")

    label("loc_106F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_107D")
    Jump("loc_10E8")

    label("loc_107D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_108B")
    Jump("loc_10E8")

    label("loc_108B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1099")
    Jump("loc_10E8")

    label("loc_1099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10A7")
    Jump("loc_10E8")

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10B5")
    Jump("loc_10E8")

    label("loc_10B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_10C3")
    Jump("loc_10E8")

    label("loc_10C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10D1")
    Jump("loc_10E8")

    label("loc_10D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_10DF")
    Jump("loc_10E8")

    label("loc_10DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_10E8")

    label("loc_10E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158C")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1175")
    SetScenarioFlags(0x38, 0)

    label("loc_1175")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118B")
    SetScenarioFlags(0x38, 1)

    label("loc_118B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A1")
    SetScenarioFlags(0x38, 2)

    label("loc_11A1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B7")
    SetScenarioFlags(0x38, 3)

    label("loc_11B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CD")
    SetScenarioFlags(0x38, 4)

    label("loc_11CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E3")
    SetScenarioFlags(0x38, 5)

    label("loc_11E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F9")
    SetScenarioFlags(0x38, 6)

    label("loc_11F9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120F")
    SetScenarioFlags(0x38, 7)

    label("loc_120F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1225")
    SetScenarioFlags(0x39, 0)

    label("loc_1225")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123B")
    SetScenarioFlags(0x39, 1)

    label("loc_123B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1251")
    SetScenarioFlags(0x39, 2)

    label("loc_1251")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1267")
    SetScenarioFlags(0x39, 3)

    label("loc_1267")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127D")
    SetScenarioFlags(0x39, 4)

    label("loc_127D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1293")
    SetScenarioFlags(0x39, 5)

    label("loc_1293")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A9")
    SetScenarioFlags(0x39, 6)

    label("loc_12A9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BF")
    SetScenarioFlags(0x39, 7)

    label("loc_12BF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D5")
    SetScenarioFlags(0x3A, 0)

    label("loc_12D5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EB")
    SetScenarioFlags(0x3A, 1)

    label("loc_12EB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1301")
    SetScenarioFlags(0x3A, 2)

    label("loc_1301")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1317")
    SetScenarioFlags(0x3A, 3)

    label("loc_1317")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132D")
    SetScenarioFlags(0x3A, 4)

    label("loc_132D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1343")
    SetScenarioFlags(0x3A, 5)

    label("loc_1343")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1359")
    SetScenarioFlags(0x3A, 6)

    label("loc_1359")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136F")
    SetScenarioFlags(0x3A, 7)

    label("loc_136F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1385")
    SetScenarioFlags(0x3B, 0)

    label("loc_1385")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139B")
    SetScenarioFlags(0x3B, 1)

    label("loc_139B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B1")
    SetScenarioFlags(0x3B, 2)

    label("loc_13B1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C7")
    SetScenarioFlags(0x3B, 3)

    label("loc_13C7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DD")
    SetScenarioFlags(0x3B, 4)

    label("loc_13DD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F3")
    SetScenarioFlags(0x3B, 5)

    label("loc_13F3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1409")
    SetScenarioFlags(0x3B, 6)

    label("loc_1409")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141F")
    SetScenarioFlags(0x3B, 7)

    label("loc_141F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1435")
    SetScenarioFlags(0x3D, 5)

    label("loc_1435")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144B")
    SetScenarioFlags(0x3D, 6)

    label("loc_144B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1461")
    SetScenarioFlags(0x3D, 7)

    label("loc_1461")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149C")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_158C")

    label("loc_149C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BF")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_158C")

    label("loc_14BF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E2")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_158C")

    label("loc_14E2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1505")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_158C")

    label("loc_1505")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1528")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_158C")

    label("loc_1528")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154B")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_158C")

    label("loc_154B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156E")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_158C")

    label("loc_156E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158C")
    SetScenarioFlags(0x3C, 7)

    label("loc_158C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15BE")
    SetChrPos(0x0, -18130, 0, -610, 135)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 16)

    label("loc_15BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_15CD")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 15)

    label("loc_15CD")

    Call(0, 10)
    Return()

    # Function_3_101A end

    def Function_4_15D1(): pass

    label("Function_4_15D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_15E3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15E3")

    Sound(136, 1, 50, 0)
    SoundDistance(0x7D, 0x8DF4, 0xFFFFEA20, 0xFA32, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E3(0x3F52, 0xFFFFE976, 0xFFFE520A)
    OP_E3(0xFFFFF10A, 0xFFFFECDC, 0xFFFDF6AC)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1637")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1637")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_165E")
    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16C7")

    label("loc_165E")

    OP_78(0xE, 0x10)
    ClearMapObjFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x1)
    SetChrPos(0x10, -38170, -2800, -33320, 90)
    OP_93(0x10, 0x5A, 0x0)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, -38170, -3800, -33320, 3000, 3000, 90000)

    label("loc_16C7")

    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18AB")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_18AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1902")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    Jump("loc_1932")

    label("loc_1902")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)

    label("loc_1932")

    MiniGame(0x2F, 0x7, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_END)), "loc_197E")
    SetMapObjFrame(0xFF, "stone_off", 0x0, 0x1)
    Jump("loc_199B")

    label("loc_197E")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 56600, -7000, -23650, 6200, 3000, 265000)

    label("loc_199B")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 35830, -5800, -74960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F8")
    OP_70(0x1, 0x0)
    Jump("loc_19FC")

    label("loc_19F8")

    OP_70(0x1, 0x1E)

    label("loc_19FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0F")
    OP_70(0x2, 0x0)
    Jump("loc_1A13")

    label("loc_1A0F")

    OP_70(0x2, 0x1E)

    label("loc_1A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A26")
    OP_70(0x3, 0x0)
    Jump("loc_1A2A")

    label("loc_1A26")

    OP_70(0x3, 0x1E)

    label("loc_1A2A")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A8B")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 28200, -5600, -32259, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1A8B")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AD7")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -17180, -5500, -103100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_1AD7")

    OP_1C(0x0, 0xF, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x10, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x11, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    Return()

    # Function_4_15D1 end

    def Function_5_1AF9(): pass

    label("Function_5_1AF9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF5")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1B7E")
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
    SetScenarioFlags(0x1EC, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1BF0")

    label("loc_1B7E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1BF0")

    Jump("loc_1C3F")

    label("loc_1BF5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1C3F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1AF9 end

    def Function_6_1C4B(): pass

    label("Function_6_1C4B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D47")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x97, 1)"), scpexpr(EXPR_END)), "loc_1CD0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x97),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1D42")

    label("loc_1CD0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x97),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D42")

    Jump("loc_1D91")

    label("loc_1D47")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1D91")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C4B end

    def Function_7_1D9D(): pass

    label("Function_7_1D9D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E99")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_1E22")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1E94")

    label("loc_1E22")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E94")

    Jump("loc_1EE3")

    label("loc_1E99")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1EE3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1D9D end

    def Function_8_1EEF(): pass

    label("Function_8_1EEF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20A7")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_2088")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2083")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2080")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1FA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1FA5)
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
    Battle("BattleInfo_D50", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_207B")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2062")
    Call(1, 5)
    Jump("loc_207B")

    label("loc_2062")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2078")
    Call(1, 4)
    Jump("loc_207B")

    label("loc_2078")

    Call(1, 3)

    label("loc_207B")

    Jump("loc_2083")

    label("loc_2080")

    Call(1, 1)

    label("loc_2083")

    Jump("loc_209E")

    label("loc_2088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_209E")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_209E")

    TalkEnd(0xFF)
    Return()

    label("loc_20A7")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_2232")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_222D")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_222A")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_214F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_214F)
    TurnDirection(0xE, 0x0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    PlayEffect(0x7, 0x1, 0xE, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_D94", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2225")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_220C")
    Call(1, 5)
    Jump("loc_2225")

    label("loc_220C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2222")
    Call(1, 4)
    Jump("loc_2225")

    label("loc_2222")

    Call(1, 3)

    label("loc_2225")

    Jump("loc_222D")

    label("loc_222A")

    Call(1, 1)

    label("loc_222D")

    Jump("loc_2248")

    label("loc_2232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2248")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2248")

    TalkEnd(0xFF)
    Return()

    # Function_8_1EEF end

    def Function_9_224D(): pass

    label("Function_9_224D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2405")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_23E6")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E1")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_23DE")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2303():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2303)
    TurnDirection(0xD, 0x0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    PlayEffect(0x7, 0x1, 0xD, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_D50", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23D9")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23C0")
    Call(1, 5)
    Jump("loc_23D9")

    label("loc_23C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23D6")
    Call(1, 4)
    Jump("loc_23D9")

    label("loc_23D6")

    Call(1, 3)

    label("loc_23D9")

    Jump("loc_23E1")

    label("loc_23DE")

    Call(1, 1)

    label("loc_23E1")

    Jump("loc_23FC")

    label("loc_23E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_23FC")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_23FC")

    TalkEnd(0xFF)
    Return()

    label("loc_2405")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 5)), scpexpr(EXPR_END)), "loc_2590")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_258B")
    ClearScenarioFlags(0x3A, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_2588")
    ClearScenarioFlags(0x38, 5)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_24AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_24AD)
    TurnDirection(0xF, 0x0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    PlayEffect(0x7, 0x1, 0xF, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_D94", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2583")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_256A")
    Call(1, 5)
    Jump("loc_2583")

    label("loc_256A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2580")
    Call(1, 4)
    Jump("loc_2583")

    label("loc_2580")

    Call(1, 3)

    label("loc_2583")

    Jump("loc_258B")

    label("loc_2588")

    Call(1, 1)

    label("loc_258B")

    Jump("loc_25A6")

    label("loc_2590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 5)), scpexpr(EXPR_END)), "loc_25A6")
    ClearScenarioFlags(0x38, 5)
    OP_65(0x5, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_25A6")

    TalkEnd(0xFF)
    Return()

    # Function_9_224D end

    def Function_10_25AB(): pass

    label("Function_10_25AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25BE")
    Jump("loc_25C3")

    label("loc_25BE")

    SetChrFlags(0x1A, 0x80)

    label("loc_25C3")

    Return()

    # Function_10_25AB end

    def Function_11_25C4(): pass

    label("Function_11_25C4")

    Call(1, 6)
    Return()

    # Function_11_25C4 end

    def Function_12_25C8(): pass

    label("Function_12_25C8")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City South Exit\x01",       # 0
            "St. Ursula Medical College\x01",      # 1
            "Quit\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266D")
    Call(0, 13)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_268D")

    label("loc_266D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268D")
    Call(0, 14)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()

    label("loc_268D")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_12_25C8 end

    def Function_13_2695(): pass

    label("Function_13_2695")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_27C4")
    Fade(500)
    OP_68(-20430, 600, -680, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -25190, 0, -1760, 180)
    SetChrPos(0x1, -24640, 0, -460, 180)
    SetChrPos(0x2, -23960, 0, 1080, 180)
    SetChrPos(0x3, -23400, 0, 2850, 180)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0xB)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xB, -27960, -10, -14410, 45)
    OP_D5(0xB, 0x0, 0xAFC8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_277B():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_277B)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xB, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_27C4")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_13_2695 end

    def Function_14_27C8(): pass

    label("Function_14_27C8")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_28F7")
    Fade(500)
    OP_68(-22010, 600, -2420, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -25190, 0, -1760, 180)
    SetChrPos(0x1, -24640, 0, -460, 180)
    SetChrPos(0x2, -23960, 0, 1080, 180)
    SetChrPos(0x3, -23400, 0, 2850, 180)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0xB)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xB, -9730, 0, 4220, 225)
    OP_D5(0xB, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_28AE():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_28AE)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xB, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_28F7")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_14_27C8 end

    def Function_15_28FB(): pass

    label("Function_15_28FB")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -25540, 0, -2260, 225)
    OP_31(0x1)
    OP_68(-25540, 600, -2260, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x5)
    Return()

    # Function_15_28FB end

    def Function_16_294C(): pass

    label("Function_16_294C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_29A7")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_299C")
    Sound(2502, 255, 100, 0)
    Jump("loc_29A2")

    label("loc_299C")

    Sound(2503, 255, 100, 0)

    label("loc_29A2")

    Jump("loc_29CB")

    label("loc_29A7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29C5")
    Sound(3347, 255, 100, 0)
    Jump("loc_29CB")

    label("loc_29C5")

    Sound(3348, 255, 100, 0)

    label("loc_29CB")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_294C end

    def Function_17_29E0(): pass

    label("Function_17_29E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F5")
    Call(0, 25)
    Jump("loc_2A74")

    label("loc_29F5")


    ChrTalk(
        0x8,
        (
            "Nevertheless, to think that a Giant Pirarucu\x01",
            "would appear here in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Just you watch! I'll get it for sure!\x02",
    )

    CloseMessageWindow()

    label("loc_2A74")

    TalkEnd(0xFE)
    Return()

    # Function_17_29E0 end

    def Function_18_2A78(): pass

    label("Function_18_2A78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C72")

    ChrTalk(
        0x9,
        (
            "That giant tree worries me but,\x01",
            "in any case, not dropping the\x01",
            "fishing line wouldn't calm me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In fishing like in every thing,\x01",
            "I think it's important to assume\x01",
            "an immovable attitude.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2BA7")

    ChrTalk(
        0x9,
        (
            "And that's why, Master Lloyd, please\x01",
            "use these to take a breather, if you want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BFC")

    label("loc_2BA7")


    ChrTalk(
        0x9,
        (
            "And that's why, Master Lloyd, please\x01",
            "use these to take a breather, if you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BFC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x18B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "x5 received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x18B, 5)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000FT-Thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 1)
    Jump("loc_2D77")

    label("loc_2C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2C")

    ChrTalk(
        0x9,
        (
            "Incidentally, Branch Manager\x01",
            "Celdan went to see how \x01",
            "that boat shed is doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh uh, it appears that the\x01",
            "branch manager liked that\x01",
            "place and can't forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D77")

    label("loc_2D2C")


    ChrTalk(
        0x9,
        (
            "Well then, today, I'll focus myself\x01",
            "on fishing to my heart's content.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D77")

    TalkEnd(0xFE)
    Return()

    # Function_18_2A78 end

    def Function_19_2D7B(): pass

    label("Function_19_2D7B")

    TalkBegin(0xFE)

    ChrTalk(
        0xA,
        (
            "Aah...finally, I can\x01",
            "fish outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Fishing amidst Mother Nature\x01",
            "is really the best!!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2D7B end

    def Function_20_2DEA(): pass

    label("Function_20_2DEA")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E1C")
    SetScenarioFlags(0x31, 2)

    label("loc_2E1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2E5C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E51")
    Sound(2499, 255, 100, 0)
    Jump("loc_2E57")

    label("loc_2E51")

    Sound(3537, 255, 100, 0)

    label("loc_2E57")

    Jump("loc_2E62")

    label("loc_2E5C")

    Sound(3344, 255, 100, 0)

    label("loc_2E62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2ED5")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EB5"),
        (SWITCH_DEFAULT, "loc_2EC6"),
    )


    label("loc_2EB5")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2ED0")

    label("loc_2EC6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2ED0")

    Jump("loc_3110")

    label("loc_2ED5")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2F07")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_2F07")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F39"),
        (1, "loc_303D"),
        (2, "loc_30CE"),
        (SWITCH_DEFAULT, "loc_3106"),
    )


    label("loc_2F39")

    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_74(0xC, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F6A")
    OP_70(0xC, 0x12C)
    OP_71(0xC, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2F7A")

    label("loc_2F6A")

    OP_70(0xC, 0xF0)
    OP_71(0xC, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2F7A")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FD0")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF3")
    Sound(461, 0, 100, 0)

    label("loc_2FF3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3013")
    OP_70(0xC, 0x14A)
    OP_71(0xC, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_3023")

    label("loc_3013")

    OP_70(0xC, 0x10E)
    OP_71(0xC, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_3023")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xC, "light", 0x1, 0x1)
    OP_70(0xC, 0x0)
    Jump("loc_2E62")

    label("loc_303D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_30AF")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_3072")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_308A")

    label("loc_3072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3085")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_308A")

    label("loc_3085")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_308A")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30C9")

    label("loc_30AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_30BF")
    OP_AF(0xFB)
    Jump("loc_30C9")

    label("loc_30BF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30C9")

    Jump("loc_3110")

    label("loc_30CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3101")

    label("loc_30E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_30F7")
    OP_AF(0xFB)
    Jump("loc_3101")

    label("loc_30F7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3101")

    Jump("loc_3110")

    label("loc_3106")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3110")

    Jump("loc_2E62")

    label("loc_3115")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_2DEA end

    def Function_21_3123(): pass

    label("Function_21_3123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3173")
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

    label("loc_3173")

    Call(0, 12)
    Return()

    # Function_21_3123 end

    def Function_22_3177(): pass

    label("Function_22_3177")

    Battle("BattleInfo_DD8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31BE")
    OP_90(0x0, -30320, -2800, -33510, 90)
    EventEnd(0x5)
    SetChrFlags(0x10, 0x8000)
    Jump("loc_31F2")

    label("loc_31BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31D1")
    Jump("loc_31F2")

    label("loc_31D1")

    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0xE, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 1)
    EventEnd(0x5)

    label("loc_31F2")

    Return()

    # Function_22_3177 end

    def Function_23_31F3(): pass

    label("Function_23_31F3")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
    )

    CloseMessageWindow()
    OP_68(35730, -5700, -72750, 1500)
    MoveCamera(45, 33, 0, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(18000, 1500)
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
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_330E")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32EC")
    MiniGame(0x6, 0xD, 0x8E30, 0xFFFFE76E, 0xFFFEF89A, 0xB4, 0x8BF6, 0xFFFFE958, 0xFFFEDB30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32E7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_END)), "loc_32E7")
    Call(0, 29)
    Return()

    label("loc_32E7")

    Jump("loc_330E")

    label("loc_32EC")

    MiniGame(0x6, 0xC, 0x8E30, 0xFFFFE76E, 0xFFFEF89A, 0xB4, 0x8BF6, 0xFFFFE958, 0xFFFEDB30)

    label("loc_330E")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_23_31F3 end

    def Function_24_3313(): pass

    label("Function_24_3313")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    OP_68(41000, -4700, -21900, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(43010, -4700, -22040, 1500)
    SetCameraDistance(18000, 1500)
    SetChrPos(0x101, 41600, -5600, -22000, 90)
    SetChrPos(0x102, 41250, -5600, -23250, 90)
    SetChrPos(0x103, 40800, -5600, -21000, 90)
    SetChrPos(0x104, 40150, -5600, -22600, 90)
    SetChrPos(0x109, 40500, -5600, -20200, 90)
    SetChrPos(0x105, 38750, -5600, -21900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)

    def lambda_3405():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3405)
    Sleep(0)

    def lambda_341D():
        OP_9B(0x0, 0x102, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_341D)
    Sleep(0)

    def lambda_3435():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3435)
    Sleep(0)

    def lambda_344D():
        OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_344D)
    Sleep(0)

    def lambda_3465():
        OP_9B(0x0, 0x109, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3465)
    Sleep(0)

    def lambda_347D():
        OP_9B(0x0, 0x105, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_347D)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#5PThat's...\x02",
    )

    CloseMessageWindow()
    OP_68(57750, -6200, -24100, 3000)
    MoveCamera(58, 30, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(22000, 3000)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 3)), scpexpr(EXPR_END)), "loc_35CB")

    ChrTalk(
        0x109,
        (
            "#10111FWhen did such a...\x02\x03",
            "#10101FWhen we came before it\x01",
            "wasn't opened, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3628")

    label("loc_35CB")


    ChrTalk(
        0x109,
        (
            "#10111FWhen did such a...\x02\x03",
            "#10108FWhen we patrolled before it\x01",
            "wasn't opened, and yet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3628")


    ChrTalk(
        0x104,
        (
            "#00301FIt could be that by chance, the buried\x01",
            "entrance has been opened up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(42800, -4700, -21900, 0)
    MoveCamera(42, 23, 0, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    TurnDirection(0x105, 0x103, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#6PSo, does it mean that the "Cryptid"\x01",
            "that ran away before is here?\x02\x03",
            "#10300FWhat about the presence of a "space anomaly"?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3739():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3739)

    def lambda_3746():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3746)
    Sleep(50)

    def lambda_3756():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3756)
    Sleep(50)

    def lambda_3766():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3766)
    Sleep(50)

    def lambda_3776():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3776)
    Sleep(50)

    def lambda_3786():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3786)
    Sleep(50)

    def lambda_3796():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3796)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x103,
        (
            "#00203F#5P...As of yet, I can't clearly say it.\x02\x03",
            "#00201FHowever, I sense a strange presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#11P...At any rate, we\x01",
            "can only go inside.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 43500, -5600, -22000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 2)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_24_3313 end

    def Function_25_38A9(): pass

    label("Function_25_38A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A7")

    ChrTalk(
        0x8,
        "You've come...let's start at once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First of all, are you qualified to\x01",
            "challenge me, the "Fishing Emperor"...?\x01",
            "I'm going to test that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Its name is "Hitting The Targets Angler Duel"...\x01",
            "Can you keep up with me till the end?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A1F")

    label("loc_39A7")


    ChrTalk(
        0x8,
        "Hmph, have you mentally prepared?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            ""Hitting The Targets Angler Duel"...\x01",
            "Show me your strong spirit and skills!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A1F")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Challenge Lakelord III to a\x01",
            ""Hitting The Targets Angler Duel"?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Challenge Him\x01",      # 0
            "Quit\x01",               # 1
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
        (0, "loc_3AC0"),
        (1, "loc_3C68"),
        (SWITCH_DEFAULT, "loc_3CAF"),
    )


    label("loc_3AC0")


    ChrTalk(
        0x8,
        "Nice preparedness...let's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E2(0x2)
    ClearMapFlags(0x1)
    OP_68(47160, -5700, -57300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x0, 31550, -5620, -50140, 315)
    OP_31(0x1)
    SetChrPos(0x101, 47200, -6300, -56050, 90)
    OP_93(0xFE, 0x5A, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    MiniGame(0x7, 0x5, 0x8, 0xCD8C, 0xFFFFE764, 0xFFFF24B4, 0xCD6E, 0xFFFFE764, 0xFFFF1352)
    SetChrPos(0x0, 56010, -5600, -3460, 89)
    OP_31(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA4")
    Call(0, 28)
    Return()

    label("loc_3BA4")

    OP_68(45050, -5700, -58570, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 44490, -6270, -58570, 90)
    OP_93(0xFE, 0x10E, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C03")
    Call(0, 26)
    Jump("loc_3C27")

    label("loc_3C03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C16")
    Jump("loc_3C27")

    label("loc_3C16")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C27")
    Call(0, 27)

    label("loc_3C27")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 41770, -5950, -58520, 270)
    OP_31(0x1)
    SetMapFlags(0x1)
    OP_69(0xFF, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_3CAF")

    label("loc_3C68")


    ChrTalk(
        0x8,
        "Hmph, having cold feet now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Whatever, suit yourself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CAF")

    label("loc_3CAF")

    Return()

    # Function_25_38A9 end

    def Function_26_3CB0(): pass

    label("Function_26_3CB0")


    ChrTalk(
        0x8,
        (
            "Bwah ha ha, have you\x01",
            "realized our different league?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's truly what\x01",
            ""foolish" means.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_26_3CB0 end

    def Function_27_3D12(): pass

    label("Function_27_3D12")


    ChrTalk(
        0x8,
        (
            "Hmph, to think you'd run\x01",
            "away in the middle of the duel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Worthless, really worthless.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_27_3D12 end

    def Function_28_3D76(): pass

    label("Function_28_3D76")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadEffect(0x0, "eff\\mgm03_02.eff")
    LoadEffect(0x1, "eff\\mgm03_01.eff")
    LoadEffect(0x2, "eff\\step04.eff")
    OP_68(49440, -6400, -56150, 0)
    MoveCamera(65, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(24610, 0)
    SetChrPos(0x101, 46750, -6300, -56900, 180)
    TurnDirection(0x8, 0x101, 0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x102, 42000, -5600, -54570, 90)
    SetChrPos(0x104, 41350, -5610, -56000, 90)
    SetChrPos(0x103, 41570, -5600, -53840, 90)
    SetChrPos(0x109, 40430, -5600, -55560, 90)
    SetChrPos(0x105, 40020, -5600, -54360, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "Uhuhu...bwah ha ha ha hah!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Interesting, very interesting...\x01",
            "You did good in keeping up with me until now\x01",
            "in the "Hitting The Targets Angler Duel".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Very well, I\x01",
            "approve of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, the problem is how to settle this...\x01",
            "Well then, what could an appropriate duel be\x01",
            "for the finale...?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(11, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 60110, -6300, -61610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(11, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, 60110, -6300, -61610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 60110, -6300, -61610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 60110, -6300, -61610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(12, 0, 100, 0)
    Sleep(150)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_40EF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40EF)
    Sleep(50)

    def lambda_40FF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_40FF)
    Sleep(300)
    StopEffect(0x1, 0x2)

    ChrTalk(
        0x101,
        "#00005FW-What was that...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwah ha ha, it appears that an\x01",
            "amazing big game wandered in\x01",
            "affected by our heat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure that one was a Pirarucu, but...\x01",
            "It boasted a giant body on the 4 arge class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right, that's surely the super\x01",
            "rare species, the Giant Pirarucu!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwah ha hah, I would've never thought\x01",
            "I could encounter it in Crossbell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FA G-Giant Pirarucu...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "In any case, our final duel\x01",
            "will be settled with this!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x8,
        (
            "The one who can fish\x01",
            "tha Giant Pirarucu first...\x01",
            "Will be the winner of this contest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...No objections, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FN-No.\x01",
            "I don't mind, but...\x02\x03",
            "#00001F(Such a super big game...\x01",
            "It would be indeed amazing if I could fish it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, it's decided.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, from now on, time\x01",
            "and turns won't count.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Who will be able to fish\x01",
            "up that thing first...?\x01",
            "The match begins right now!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x191, 0)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 46320, -6300, -56810, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_3D76 end

    def Function_29_44AE(): pass

    label("Function_29_44AE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch32200.itc", 0x1E)
    LoadChrToIndex("chr/ch46100.itc", 0x1F)
    LoadChrToIndex("chr/ch45700.itc", 0x20)
    LoadChrToIndex("chr/ch45800.itc", 0x21)
    LoadChrToIndex("chr/ch45900.itc", 0x22)
    LoadChrToIndex("chr/ch46000.itc", 0x23)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Giant Pirarucu spat out something else.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEF, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4562")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xEF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    AddItemNumber(0xEF, 1)
    Jump("loc_457B")

    label("loc_4562")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    AddItemNumber(0x6F, 1)

    label("loc_457B")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(40790, -6600, -57830, 0)
    MoveCamera(41, 18, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23320, 0)
    SetChrPos(0x101, 37690, -6090, -62260, 0)
    SetChrPos(0x8, 37660, -5910, -60080, 180)
    SetChrPos(0x102, 40850, -5600, -55900, 225)
    SetChrPos(0x103, 39410, -5600, -55320, 225)
    SetChrPos(0x104, 42210, -5640, -55120, 225)
    SetChrPos(0x109, 40880, -5610, -54220, 225)
    SetChrPos(0x105, 39030, -5610, -53880, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "I-I don't believe it.\x01",
            "Someone like me, getting forestalled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Hm, however, a loss is a loss.\x01",
            "It seems I have to accept it in honesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'll give...no, I will award you this.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "Also, you, who gained this proof, have been\x01",
            "given the title of "Fishing Emperor Slayer",\x01",
            "as per the Fishing Emperor Club code.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's the title that acknowledges an angler superiority\x01",
            "throughout the continent. Be honored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "As for the rest, about what was agreed for the matches...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 30650, -5880, -57210, 135)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 31220, -5790, -55880, 135)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 34190, -5610, -52480, 225)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 33770, -5600, -52140, 225)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 33620, -5600, -51290, 225)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 32560, -5600, -52360, 225)

    ChrTalk(
        0x15,
        "S-Sir Lakelord!\x02",
    )

    CloseMessageWindow()

    def lambda_497A():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_497A)
    Sleep(50)

    def lambda_498A():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_498A)
    OP_68(37270, -5200, -59200, 4000)
    MoveCamera(331, 19, 0, 4000)
    OP_6E(530, 4000)
    SetCameraDistance(19090, 4000)

    def lambda_49C5():
        OP_95(0xFE, 34400, -6070, -60340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_49C5)
    Sleep(50)

    def lambda_49E2():
        OP_95(0xFE, 36920, -5650, -57140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_49E2)
    Sleep(50)

    def lambda_49FF():
        OP_95(0xFE, 34950, -5770, -58800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_49FF)
    Sleep(50)

    def lambda_4A1C():
        OP_95(0xFE, 37600, -5610, -55680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4A1C)
    Sleep(50)

    def lambda_4A39():
        OP_95(0xFE, 35900, -5610, -55640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4A39)
    Sleep(50)

    def lambda_4A56():
        OP_95(0xFE, 35440, -5610, -56920, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4A56)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)

    ChrTalk(
        0x12,
        (
            "*pant pant*...\x01",
            "Member Lloyd, you have...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "???",
        (
            "#5PHm, it appears it has\x01",
            "already been settled.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 500)

    ChrTalk(
        0x8,
        "Y-You are Harvard...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Harvard Fisher!!\x02",
    )

    CloseMessageWindow()

    def lambda_4B14():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4B14)
    Sleep(50)

    def lambda_4B24():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4B24)
    Sleep(50)

    def lambda_4B34():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4B34)
    Sleep(50)

    def lambda_4B44():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4B44)
    Sleep(50)

    def lambda_4B54():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4B54)

    ChrTalk(
        0x13,
        (
            "#5PAnd you are William's kid...\x01",
            "You have grown up in the time I didn't see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5POh, should I have called\x01",
            "you Lakelord III now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, you traitor!\x01",
            "Don't call my name friendly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You...why did you abandon the Fishing Emperor Club!?\x01",
            "Why did you oppose dad and returned evil for good!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#5PHm...that's a misunderstanding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5PIt is indeed true that between the\x01",
            "Fishing Emperor Club and I there\x01",
            "was a considerable discord...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5PBut even your father, Lakelord II, knew very\x01",
            "well of my retirement from the Fishing Emperor\x01",
            "Club and that I found the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5PThat's why even now I use the\x01",
            "title of "Avid Angler" that I had at\x01",
            "the time of the Fishing Emperor Club...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmh, shut up. Don't say what you\x01",
            "like with an important-looking air!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At any rate, I was thinking to give you\x01",
            "what you deserve when I met you, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly, now I've had enough.\x01",
            "I'll do it at the next opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Until then, be prepared\x01",
            "and just wait and see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#5PHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, Celdan. \x01",
            "Like I promised, I return the office to you, but\x01",
            "I'll take some time to sort out the luggages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When we're over with that,\x01",
            "the Fishing Emperor Club will\x01",
            "fully withdraw from Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...Yes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "As for what remains...\x01",
            "You would have complied to one order\x01",
            "from us, whatever it was, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmph, do you have already decided about it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Yes, I did.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x101, 500)

    ChrTalk(
        0x12,
        "Member Lloyd, do you mind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FNo, of course not.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 500)

    ChrTalk(
        0x12,
        (
            "*cough*...\x01",
            "Then, I'll give you my order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            ""I want you to cancel the \x01",
            "Fishing Emperor Club \x01",
            "withdrawal from Crossbell".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_52EF():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_52EF)
    Sleep(50)

    def lambda_52FF():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_52FF)
    Sleep(50)

    def lambda_530F():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_530F)
    Sleep(50)

    def lambda_531F():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_531F)
    Sleep(50)

    def lambda_532F():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_532F)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#5POoh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Y-You...\x01",
            "Are you mocking us!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "No...rather, it's the opposite.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "By fighting you all we came\x01",
            "to know how much narrow\x01",
            "our world was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If the opportunity arises,\x01",
            "I want to fish with you again...\x01",
            "I simply thought that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FBranch Manager Celdan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5PHm, nothing less to be expected\x01",
            "from the man I put my trust upon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Fishing together...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As if we could ever get\x01",
            "along well with y――\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I don't mind that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "In the first place, we greatly\x01",
            "welcome anyone, provided they\x01",
            "don't get in our way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If you can abide to that,\x01",
            "I don't even mind you\x01",
            "using our boat shed.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "W-Who would ever use\x01",
            "such a miserable shed!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, we accept\x01",
            "rules as rules, so...\x01",
            "There won't be any change later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That's fine with you, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Yes, no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph...\x01",
            "Both Harvard and you, how much\x01",
            "simple souls can you be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, also, about the\x01",
            "receptionist, Sylum...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Originally, she wasn't a member of\x01",
            "the Fishing Emperor Club and she\x01",
            "wanted to join the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Look after her, understood?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Yes, that's a simple request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmph, I'm finished talking.\x02",
    )

    CloseMessageWindow()
    OP_68(37650, -5000, -59390, 3000)
    MoveCamera(4, 23, 0, 3000)
    OP_6E(530, 3000)
    SetCameraDistance(18950, 3000)

    def lambda_5827():
        OP_95(0xFE, 36110, -5730, -58120, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5827)
    Sleep(500)

    def lambda_5844():

        label("loc_5844")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5844")

    QueueWorkItem2(0x101, 1, lambda_5844)
    Sleep(50)

    def lambda_5859():

        label("loc_5859")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5859")

    QueueWorkItem2(0x13, 1, lambda_5859)
    Sleep(50)

    def lambda_586E():

        label("loc_586E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_586E")

    QueueWorkItem2(0x12, 1, lambda_586E)
    Sleep(50)

    def lambda_5883():

        label("loc_5883")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5883")

    QueueWorkItem2(0x102, 1, lambda_5883)
    Sleep(50)

    def lambda_5898():

        label("loc_5898")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5898")

    QueueWorkItem2(0x103, 1, lambda_5898)
    Sleep(50)

    def lambda_58AD():

        label("loc_58AD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_58AD")

    QueueWorkItem2(0x104, 1, lambda_58AD)
    Sleep(50)

    def lambda_58C2():

        label("loc_58C2")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_58C2")

    QueueWorkItem2(0x109, 1, lambda_58C2)
    Sleep(50)

    def lambda_58D7():

        label("loc_58D7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_58D7")

    QueueWorkItem2(0x105, 1, lambda_58D7)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "Come on, everybody. Let's pack things\x01",
            "at once and go back to our country.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(185, 20, -1, -1)
    SetChrName("Elite Fours")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...Yes, boss!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_95(0x8, 34490, -5660, -57880, 2000, 0x0)

    def lambda_5989():
        OP_95(0xFE, 31090, -5670, -51170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5989)
    Sleep(50)

    def lambda_59A6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_59A6)
    Sleep(50)

    def lambda_59B6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_59B6)
    Sleep(50)

    def lambda_59C6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_59C6)
    Sleep(50)

    def lambda_59D6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_59D6)
    WaitChrThread(0x15, 1)
    Sleep(1000)

    def lambda_59EA():
        OP_95(0xFE, 33250, -5600, -50050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_59EA)
    Sleep(50)

    def lambda_5A07():
        OP_95(0xFE, 34190, -5610, -52480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5A07)
    Sleep(50)

    def lambda_5A24():
        OP_95(0xFE, 32560, -5600, -52360, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5A24)
    Sleep(50)

    def lambda_5A41():
        OP_95(0xFE, 33770, -5600, -52140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5A41)
    OP_68(37650, -3000, -59390, 3000)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("r0200", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_44AE end

    SaveToFile()

Try(main)
