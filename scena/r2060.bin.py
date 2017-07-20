﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r2060.bin",                # FileName
        "r2060",                    # MapName
        "r2060",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r0020", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x16,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 3, 0, 4],
    )

    BuildStringList((
        "r2060",                  # 0
        "Miner Gantz",             # 1
        "Rods",                 # 2
        "Rods",                 # 3
        "Steel Drew",           # 4
        "Steel Drew",           # 5
        "A security guard",               # 6
        "A security guard",               # 7
        "A security guard",               # 8
        "A security guard",               # 9
        "A security guard",               # 10
        "A security guard",               # 11
        "A security guard",               # 12
        "A security guard",               # 13
        "A hunter",                   # 14
        "A hunter",                   # 15
        "A hunter",                   # 16
        "A hunter",                   # 17
        "A hunter",                   # 18
        "A hunter",                   # 19
        "A hunter",                   # 20
        "Randy",               # 21
        "Charlie",             # 22
        "Lieutenant Mireille",           # 23
        "Grace",               # 24
        "Hunting soldier Gareth",             # 25
        "Cougar",               # 26
        "Cougar",               # 27
        "Cougar",               # 28
        "Cougar",               # 29
        "Cougar",               # 30
        "Cougar",               # 31
        "wolf",                     # 32
        "wolf",                     # 33
        "wolf",                     # 34
        "wolf",                     # 35
        "wolf",                     # 36
        "car",                     # 37
        "Armored car",                 # 38
        "Armored car",                 # 39
        "New armored car",             # 40
        "weapon",                   # 41
        "weapon",                   # 42
        "SE control",                 # 43
        "br2060",                 # 44
        "br2060",                 # 45
        "br2060",                 # 46
        "br2060",                 # 47
        "br2060",                 # 48
        "br2060",                 # 49
        "br2060",                 # 50
        "br2061",                 # 51
        "Cross Bell City",       # 52
        "Mine town mining to Mainz",     # 53
    ))

    ATBonus("ATBonus_A34", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A54", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_12FC5", 0,   6,   2,   1,   3,   3,   0)
    Sepith("Sepith_12FED", 0,   0,   0,   5,   5,   5,   3)
    Sepith("Sepith_12FAD", 0,   7,   2,   0,   1,   0,   4)
    Sepith("Sepith_12FE5", 11,  3,   6,   4,   6,   10,  8)

    MonsterBattlePostion("MonsterBattlePostion_A94", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_A98", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A9C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AA0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_AA4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_AA8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_AAC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_AB0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_AF4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_AF8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_AFC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_B00", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_B04", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_B08", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_B0C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B10", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_A74", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A78", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A7C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_A80", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_A84", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_A88", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_A90", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B14", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B18", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B1C", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B20", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B24", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B28", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B2C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B30", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B34", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B38", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_B3C", 9, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_B40", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B44", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B48", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4C", 7, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B50", 9, 10, 180)

    # monster count: 14

    BattleInfo(
        "BattleInfo_CE4", 0x0000, 53, 6, 45, 10, 1, 50, 0, "br2060", "Sepith_12FC5", 30, 40, 20, 10,
        (
            ("ms64400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
        )
    )

    BattleInfo(
        "BattleInfo_B54", 0x0000, 53, 6, 45, 10, 1, 30, 0, "br2060", "Sepith_12FED", 30, 40, 20, 10,
        (
            ("ms71700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms71700.dat", "ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
        )
    )

    BattleInfo(
        "BattleInfo_C1C", 0x0000, 53, 6, 45, 10, 1, 25, 0, "br2060", "Sepith_12FAD", 30, 40, 20, 10,
        (
            ("ms65900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
        )
    )

    BattleInfo(
        "BattleInfo_DAC", 0x0000, 81, 6, 45, 6, 1, 30, 0, "br2060", "Sepith_12FE5", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_E48", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7453", "ed7453", "ATBonus_A34"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E8C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7453", "ed7453", "ATBonus_A34"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_ED0", 0x00DA, 3, 6, 45, 3, 3, 30, 0, "br2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03400.dat", "ms41900.dat", "ms41900.dat", "ms82000.dat", 0, 0, "ms81800.dat", 0, "MonsterBattlePostion_B14", "MonsterBattlePostion_A94", "ed7455", "ed7453", "ATBonus_A54"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_F14", 0x0042, 0, 6, 0, 0, 3, 0, 0, "br2061", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42100.dat", "ms82001.dat", "ms82001.dat", "ms82001.dat", "ms82001.dat", "ms82001.dat", "ms82001.dat", 0, "MonsterBattlePostion_B34", "MonsterBattlePostion_B34", "ed7455", "ed7453", "ATBonus_A54"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch30700.itc",                   # 00
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
        "monster/ch71750.itc",               # 10
        "monster/ch71751.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch64450.itc",               # 14
        "monster/ch64450.itc",               # 15
        "monster/ch76050.itc",               # 16
        "monster/ch76051.itc",               # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(3630,    0,       25250,   270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(14050,   10000,   160259,  270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(3630,    0,       25250,   270,  484,  0x0, 0,   22,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(14050,   10000,   160259,  270,  484,  0x0, 0,   22,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(690,     27940,   0,       0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294927386, 61380,   0,       0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294925126, 79460,   0,       0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(350,     141340,  0,       0x1010000,    "BattleInfo_B54", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(5600,    124460,  0,       0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(23790,   135160,  0,       0x1010000,    "BattleInfo_C1C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294959646, 149400,  4000,    0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(15210,   144180,  6000,    0x1010000,    "BattleInfo_CE4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(12090,   156500,  10000,   0x1010000,    "BattleInfo_B54", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(6050,    159680,  10000,   0x1010000,    "BattleInfo_B54", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294953586, 39330,   0,       0x1010000,    "BattleInfo_DAC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294934826, 88800,   0,       0x1010000,    "BattleInfo_DAC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294946656, 138730,  0,       0x1010000,    "BattleInfo_DAC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(14120,   125230,  0,       0x1010000,    "BattleInfo_DAC", 0,   22,  0xFFFF, 6,  7)

    DeclEvent(0x0040, 0, 12,  -24.0,                 196.0,                 7.0,                   42.25,                 [0.07692307978868484,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.07692307978868484,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.846153974533081,     -15.076923370361328,   -1.399999976158142,    1.0])
    DeclEvent(0x0000, 0, 99,  -20.0,                 152.0,                 2.0,                   900.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.6666667461395264,    -30.399999618530273,   -0.4000000059604645,   1.0])
    DeclEvent(0x0000, 0, 100, -8.0,                  135.5,                 -1.0,                  2500.0,                [0.18793852627277374,  0.017101014032959938,  -0.0,                  0.0,                   -0.06840405613183975,  0.046984631568193436,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   10.772257804870605,    -6.229609489440918,    0.20000001788139343,   1.0])
    DeclEvent(0x0000, 0, 14,  -25.84000015258789,    198.6999969482422,     7.0,                   441.0,                 [0.05050760880112648,  0.23570233583450317,   -0.0,                  0.0,                   -0.050507642328739166, 0.23570218682289124,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   11.340985298156738,    -40.74347686767578,    -1.3999998569488525,   1.0])

    DeclActor(18120,   10000,   151900,  1200,    18120,   11000,   151900,  0x007C, 0,  5,  0x0000)
    DeclActor(4294924956, 8000,    197150,  1200,    4294924956, 9000,    197150,  0x007C, 0,  6,  0x0000)
    DeclActor(21780,   6050,    139350,  1200,    21780,   7050,    139350,  0x007C, 0,  7,  0x0000)
    DeclActor(3630,    0,       25250,   1200,    3630,    0,       25250,   0x007C, 0,  8,  0x0000)
    DeclActor(14050,   10000,   160260,  1200,    14050,   10000,   160260,  0x007C, 0,  9,  0x0000)
    DeclActor(4294947256, 8000,    199730,  1200,    4294947256, 9500,    199730,  0x007C, 0,  142, 0x0000)
    DeclActor(4294944636, 8000,    197420,  1200,    4294944636, 9500,    197420,  0x007C, 0,  142, 0x0000)

    PlaceName(-3.0, 0.0, -15.0, 0x0000, 0x0000, "Cross Bell City")
    PlaceName(87.0, 6.0, 122.0, 0x0000, 0x0000, "Mine town mining to Mainz")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_11F4",         # 00, 0
        "Function_1_12A4",         # 01, 1
        "Function_2_12C3",         # 02, 2
        "Function_3_12E2",         # 03, 3
        "Function_4_188B",         # 04, 4
        "Function_5_2121",         # 05, 5
        "Function_6_2272",         # 06, 6
        "Function_7_23C3",         # 07, 7
        "Function_8_2514",         # 08, 8
        "Function_9_2872",         # 09, 9
        "Function_10_2BD0",        # 0A, 10
        "Function_11_2BF3",        # 0B, 11
        "Function_12_2D3B",        # 0C, 12
        "Function_13_33B3",        # 0D, 13
        "Function_14_33DB",        # 0E, 14
        "Function_15_36D9",        # 0F, 15
        "Function_16_36F0",        # 10, 16
        "Function_17_3952",        # 11, 17
        "Function_18_39B8",        # 12, 18
        "Function_19_39C3",        # 13, 19
        "Function_20_3A21",        # 14, 20
        "Function_21_3AAF",        # 15, 21
        "Function_22_3BC3",        # 16, 22
        "Function_23_3C33",        # 17, 23
        "Function_24_3DB0",        # 18, 24
        "Function_25_3E23",        # 19, 25
        "Function_26_3E38",        # 1A, 26
        "Function_27_3F55",        # 1B, 27
        "Function_28_3FB7",        # 1C, 28
        "Function_29_52F7",        # 1D, 29
        "Function_30_540D",        # 1E, 30
        "Function_31_552A",        # 1F, 31
        "Function_32_5576",        # 20, 32
        "Function_33_55D0",        # 21, 33
        "Function_34_5616",        # 22, 34
        "Function_35_5662",        # 23, 35
        "Function_36_56B5",        # 24, 36
        "Function_37_5702",        # 25, 37
        "Function_38_574F",        # 26, 38
        "Function_39_57A2",        # 27, 39
        "Function_40_57E1",        # 28, 40
        "Function_41_93C6",        # 29, 41
        "Function_42_93EE",        # 2A, 42
        "Function_43_9416",        # 2B, 43
        "Function_44_943E",        # 2C, 44
        "Function_45_9466",        # 2D, 45
        "Function_46_948E",        # 2E, 46
        "Function_47_94CA",        # 2F, 47
        "Function_48_9506",        # 30, 48
        "Function_49_952E",        # 31, 49
        "Function_50_9562",        # 32, 50
        "Function_51_95B2",        # 33, 51
        "Function_52_9602",        # 34, 52
        "Function_53_9652",        # 35, 53
        "Function_54_96AD",        # 36, 54
        "Function_55_96F8",        # 37, 55
        "Function_56_9754",        # 38, 56
        "Function_57_9786",        # 39, 57
        "Function_58_97B8",        # 3A, 58
        "Function_59_981D",        # 3B, 59
        "Function_60_987F",        # 3C, 60
        "Function_61_98CC",        # 3D, 61
        "Function_62_991D",        # 3E, 62
        "Function_63_99BB",        # 3F, 63
        "Function_64_99D4",        # 40, 64
        "Function_65_99ED",        # 41, 65
        "Function_66_9A06",        # 42, 66
        "Function_67_9A1E",        # 43, 67
        "Function_68_9A89",        # 44, 68
        "Function_69_9B32",        # 45, 69
        "Function_70_9B42",        # 46, 70
        "Function_71_9B58",        # 47, 71
        "Function_72_9B72",        # 48, 72
        "Function_73_CF90",        # 49, 73
        "Function_74_CFBE",        # 4A, 74
        "Function_75_CFF2",        # 4B, 75
        "Function_76_D0E8",        # 4C, 76
        "Function_77_D11C",        # 4D, 77
        "Function_78_D1A1",        # 4E, 78
        "Function_79_D1F7",        # 4F, 79
        "Function_80_D2B8",        # 50, 80
        "Function_81_D30E",        # 51, 81
        "Function_82_D395",        # 52, 82
        "Function_83_D3FF",        # 53, 83
        "Function_84_D4DB",        # 54, 84
        "Function_85_D545",        # 55, 85
        "Function_86_D5E7",        # 56, 86
        "Function_87_D665",        # 57, 87
        "Function_88_D6E9",        # 58, 88
        "Function_89_D739",        # 59, 89
        "Function_90_D7FE",        # 5A, 90
        "Function_91_D881",        # 5B, 91
        "Function_92_D8FE",        # 5C, 92
        "Function_93_D967",        # 5D, 93
        "Function_94_D9D0",        # 5E, 94
        "Function_95_DA25",        # 5F, 95
        "Function_96_DA80",        # 60, 96
        "Function_97_DAA5",        # 61, 97
        "Function_98_DACA",        # 62, 98
        "Function_99_DEA4",        # 63, 99
        "Function_100_E03D",       # 64, 100
        "Function_101_EE5F",       # 65, 101
        "Function_102_EED8",       # 66, 102
        "Function_103_EF51",       # 67, 103
        "Function_104_117AC",      # 68, 104
        "Function_105_117C8",      # 69, 105
        "Function_106_117E4",      # 6A, 106
        "Function_107_11800",      # 6B, 107
        "Function_108_1181C",      # 6C, 108
        "Function_109_1183C",      # 6D, 109
        "Function_110_11941",      # 6E, 110
        "Function_111_119B6",      # 6F, 111
        "Function_112_11A91",      # 70, 112
        "Function_113_11B21",      # 71, 113
        "Function_114_11C26",      # 72, 114
        "Function_115_11CBC",      # 73, 115
        "Function_116_11D71",      # 74, 116
        "Function_117_11DE6",      # 75, 117
        "Function_118_11E89",      # 76, 118
        "Function_119_11EFE",      # 77, 119
        "Function_120_11FA7",      # 78, 120
        "Function_121_1201C",      # 79, 121
        "Function_122_120E0",      # 7A, 122
        "Function_123_121A0",      # 7B, 123
        "Function_124_1221E",      # 7C, 124
        "Function_125_122CC",      # 7D, 125
        "Function_126_1232E",      # 7E, 126
        "Function_127_1237E",      # 7F, 127
        "Function_128_1241D",      # 80, 128
        "Function_129_124BC",      # 81, 129
        "Function_130_1252C",      # 82, 130
        "Function_131_12673",      # 83, 131
        "Function_132_12710",      # 84, 132
        "Function_133_12838",      # 85, 133
        "Function_134_1286A",      # 86, 134
        "Function_135_128A3",      # 87, 135
        "Function_136_12956",      # 88, 136
        "Function_137_12A10",      # 89, 137
        "Function_138_12ACA",      # 8A, 138
        "Function_139_12B94",      # 8B, 139
        "Function_140_12BFE",      # 8C, 140
        "Function_141_12C5D",      # 8D, 141
        "Function_142_12C8E",      # 8E, 142
    ))


    def Function_0_11F4(): pass

    label("Function_0_11F4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_122C"),
        (1, "loc_1238"),
        (2, "loc_1244"),
        (3, "loc_1250"),
        (4, "loc_125C"),
        (5, "loc_1268"),
        (6, "loc_1274"),
        (SWITCH_DEFAULT, "loc_1280"),
    )


    label("loc_122C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1238")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1244")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1250")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_125C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1268")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1274")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_1280")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_128C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_128C")

    label("loc_12A3")

    Return()

    # Function_0_11F4 end

    def Function_1_12A4(): pass

    label("Function_1_12A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12C2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_12A4")

    label("loc_12C2")

    Return()

    # Function_1_12A4 end

    def Function_2_12C3(): pass

    label("Function_2_12C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E1")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_12C3")

    label("loc_12E1")

    Return()

    # Function_2_12C3 end

    def Function_3_12E2(): pass

    label("Function_3_12E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1306")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -24500, 8000, 193000, 270)

    label("loc_1306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1321")
    SetMapFlags(0x10000000)
    Event(0, 40)
    Jump("loc_1337")

    label("loc_1321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1337")
    SetMapFlags(0x10000000)
    Event(0, 98)

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_134E")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 16)
    Jump("loc_13CA")

    label("loc_134E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1362")
    ClearScenarioFlags(0x22, 1)
    Event(0, 21)
    Jump("loc_13CA")

    label("loc_1362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1376")
    ClearScenarioFlags(0x22, 2)
    Event(0, 23)
    Jump("loc_13CA")

    label("loc_1376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_138A")
    ClearScenarioFlags(0x22, 3)
    Event(0, 26)
    Jump("loc_13CA")

    label("loc_138A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_13A1")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x0, 0)
    Event(0, 28)
    Jump("loc_13CA")

    label("loc_13A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_13B5")
    ClearScenarioFlags(0x22, 5)
    Event(0, 72)
    Jump("loc_13CA")

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_13CA")
    ClearScenarioFlags(0x22, 6)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 103)

    label("loc_13CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1877")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1460")
    SetScenarioFlags(0x38, 0)

    label("loc_1460")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1476")
    SetScenarioFlags(0x38, 1)

    label("loc_1476")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148C")
    SetScenarioFlags(0x38, 2)

    label("loc_148C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A2")
    SetScenarioFlags(0x38, 3)

    label("loc_14A2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B8")
    SetScenarioFlags(0x38, 4)

    label("loc_14B8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14CE")
    SetScenarioFlags(0x38, 5)

    label("loc_14CE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E4")
    SetScenarioFlags(0x38, 6)

    label("loc_14E4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FA")
    SetScenarioFlags(0x38, 7)

    label("loc_14FA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1510")
    SetScenarioFlags(0x39, 0)

    label("loc_1510")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1526")
    SetScenarioFlags(0x39, 1)

    label("loc_1526")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153C")
    SetScenarioFlags(0x39, 2)

    label("loc_153C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1552")
    SetScenarioFlags(0x39, 3)

    label("loc_1552")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1568")
    SetScenarioFlags(0x39, 4)

    label("loc_1568")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157E")
    SetScenarioFlags(0x39, 5)

    label("loc_157E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1594")
    SetScenarioFlags(0x39, 6)

    label("loc_1594")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AA")
    SetScenarioFlags(0x39, 7)

    label("loc_15AA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C0")
    SetScenarioFlags(0x3A, 0)

    label("loc_15C0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D6")
    SetScenarioFlags(0x3A, 1)

    label("loc_15D6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EC")
    SetScenarioFlags(0x3A, 2)

    label("loc_15EC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1602")
    SetScenarioFlags(0x3A, 3)

    label("loc_1602")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1618")
    SetScenarioFlags(0x3A, 4)

    label("loc_1618")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162E")
    SetScenarioFlags(0x3A, 5)

    label("loc_162E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1644")
    SetScenarioFlags(0x3A, 6)

    label("loc_1644")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165A")
    SetScenarioFlags(0x3A, 7)

    label("loc_165A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1670")
    SetScenarioFlags(0x3B, 0)

    label("loc_1670")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1686")
    SetScenarioFlags(0x3B, 1)

    label("loc_1686")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169C")
    SetScenarioFlags(0x3B, 2)

    label("loc_169C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B2")
    SetScenarioFlags(0x3B, 3)

    label("loc_16B2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C8")
    SetScenarioFlags(0x3B, 4)

    label("loc_16C8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16DE")
    SetScenarioFlags(0x3B, 5)

    label("loc_16DE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F4")
    SetScenarioFlags(0x3B, 6)

    label("loc_16F4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170A")
    SetScenarioFlags(0x3B, 7)

    label("loc_170A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1720")
    SetScenarioFlags(0x3D, 5)

    label("loc_1720")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1736")
    SetScenarioFlags(0x3D, 6)

    label("loc_1736")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174C")
    SetScenarioFlags(0x3D, 7)

    label("loc_174C")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1787")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1877")

    label("loc_1787")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AA")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1877")

    label("loc_17AA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CD")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1877")

    label("loc_17CD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F0")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1877")

    label("loc_17F0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1813")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1877")

    label("loc_1813")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1836")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1877")

    label("loc_1836")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1859")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1877")

    label("loc_1859")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1877")
    SetScenarioFlags(0x3C, 7)

    label("loc_1877")

    Call(0, 10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_188A")
    OP_E2(0x1)

    label("loc_188A")

    Return()

    # Function_3_12E2 end

    def Function_4_188B(): pass

    label("Function_4_188B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18A5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_18B7")

    label("loc_18A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_18B7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18B7")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18CF")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_18CF")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E7")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_18E7")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1904")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1904")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_191C")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_191C")

    OP_52(0x3D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E0B")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1E32")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_1E32")

    label("loc_1E32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E94")
    LoadEffect(0x9, "event/ev11006.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 1)), scpexpr(EXPR_END)), "loc_1E94")
    PlayEffect(0x9, 0x0, 0xFF, 0x0, -16500, 10100, 203350, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_1E94")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EEE")
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -23440, 8000, 175460, 10000, 5000, 150000)
    Jump("loc_1F0E")

    label("loc_1EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F0E")
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)

    label("loc_1F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1E")
    SetMapObjFlags(0x5, 0x4)

    label("loc_1F1E")

    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F79")
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetBarrier(0x0, 0x0, 0x1, 0x0, -19610, 3500, 152140, 8000, 5000, 0)

    label("loc_1F79")

    SetMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F92")
    OP_70(0x0, 0x0)
    Jump("loc_1F96")

    label("loc_1F92")

    OP_70(0x0, 0x1E)

    label("loc_1F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA9")
    OP_70(0x1, 0x0)
    Jump("loc_1FAD")

    label("loc_1FA9")

    OP_70(0x1, 0x1E)

    label("loc_1FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC0")
    OP_70(0x2, 0x0)
    Jump("loc_1FC4")

    label("loc_1FC0")

    OP_70(0x2, 0x1E)

    label("loc_1FC4")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2025")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 3630, 0, 25250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_2025")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2071")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 14050, 10000, 160260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_2071")

    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_209D")
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x10)
    Jump("loc_20D5")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B0")
    OP_66(0x5, 0x1)
    Jump("loc_20D5")

    label("loc_20B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BF")
    Jump("loc_20D5")

    label("loc_20BF")

    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x10)
    OP_66(0x6, 0x1)

    label("loc_20D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_20E9")
    OP_24(0x6E)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_2120")

    label("loc_20E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2120")
    SoundDistance(0x6E, 0xFFFFE976, 0x1F40, 0x2F472, 0x186A0, 0x186A0, 0x5A, 0x0)
    OP_E3(0xAFC8, 0x0, 0xDEEE)

    label("loc_2120")

    Return()

    # Function_4_188B end

    def Function_5_2121(): pass

    label("Function_5_2121")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2221")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('Ｕ材料', 1)"), scpexpr(EXPR_END)), "loc_21AA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_221C")

    label("loc_21AA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_221C")

    Jump("loc_2266")

    label("loc_2221")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_2266")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_2121 end

    def Function_6_2272(): pass

    label("Function_6_2272")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2372")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('安全头盔', 1)"), scpexpr(EXPR_END)), "loc_22FB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '安全头盔'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_236D")

    label("loc_22FB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '安全头盔'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '安全头盔'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_236D")

    Jump("loc_23B7")

    label("loc_2372")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_23B7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_2272 end

    def Function_7_23C3(): pass

    label("Function_7_23C3")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C3")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅰ', 1)"), scpexpr(EXPR_END)), "loc_244C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅰ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_24BE")

    label("loc_244C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅰ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅰ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_24BE")

    Jump("loc_2508")

    label("loc_24C3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_2508")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_23C3 end

    def Function_8_2514(): pass

    label("Function_8_2514")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26CC")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_26AD")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A8")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_26A5")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_25CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_25CE)
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
    Battle("BattleInfo_E48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A0")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2687")
    Call(1, 5)
    Jump("loc_26A0")

    label("loc_2687")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_269D")
    Call(1, 4)
    Jump("loc_26A0")

    label("loc_269D")

    Call(1, 3)

    label("loc_26A0")

    Jump("loc_26A8")

    label("loc_26A5")

    Call(1, 1)

    label("loc_26A8")

    Jump("loc_26C3")

    label("loc_26AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_26C3")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_26C3")

    TalkEnd(0xFF)
    Return()

    label("loc_26CC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_2857")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2852")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_284F")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2778():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2778)
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
    Battle("BattleInfo_E8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_284A")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2831")
    Call(1, 5)
    Jump("loc_284A")

    label("loc_2831")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2847")
    Call(1, 4)
    Jump("loc_284A")

    label("loc_2847")

    Call(1, 3)

    label("loc_284A")

    Jump("loc_2852")

    label("loc_284F")

    Call(1, 1)

    label("loc_2852")

    Jump("loc_286D")

    label("loc_2857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_286D")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_286D")

    TalkEnd(0xFF)
    Return()

    # Function_8_2514 end

    def Function_9_2872(): pass

    label("Function_9_2872")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A2A")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_2A0B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A06")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2A03")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_292C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_292C)
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
    Battle("BattleInfo_E48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29FE")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_29E5")
    Call(1, 5)
    Jump("loc_29FE")

    label("loc_29E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_29FB")
    Call(1, 4)
    Jump("loc_29FE")

    label("loc_29FB")

    Call(1, 3)

    label("loc_29FE")

    Jump("loc_2A06")

    label("loc_2A03")

    Call(1, 1)

    label("loc_2A06")

    Jump("loc_2A21")

    label("loc_2A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2A21")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2A21")

    TalkEnd(0xFF)
    Return()

    label("loc_2A2A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_2BB5")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB0")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2BAD")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2AD6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2AD6)
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
            "A monster appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_E8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA8")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B8F")
    Call(1, 5)
    Jump("loc_2BA8")

    label("loc_2B8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2BA5")
    Call(1, 4)
    Jump("loc_2BA8")

    label("loc_2BA5")

    Call(1, 3)

    label("loc_2BA8")

    Jump("loc_2BB0")

    label("loc_2BAD")

    Call(1, 1)

    label("loc_2BB0")

    Jump("loc_2BCB")

    label("loc_2BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2BCB")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2BCB")

    TalkEnd(0xFF)
    Return()

    # Function_9_2872 end

    def Function_10_2BD0(): pass

    label("Function_10_2BD0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BF2")
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x40, 0x80)

    label("loc_2BF2")

    Return()

    # Function_10_2BD0 end

    def Function_11_2BF3(): pass

    label("Function_11_2BF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFE")

    ChrTalk(
        0xFE,
        (
            "This is the entrance of the former mine.\x01",
            "If you are ready, ask me for a survey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Shut up, this\x01",
            "Cutting out a strong key …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even we who are trained from usual\x01",
            "It is a trick that can not be imitated at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know who broke down … …\x01",
            "Be careful if you go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D37")

    label("loc_2CFE")


    ChrTalk(
        0xFE,
        (
            "This is the entrance of the former mine.\x01",
            "If you are ready, ask me for a survey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D37")

    TalkEnd(0xFE)
    Return()

    # Function_11_2BF3 end

    def Function_12_2D3B(): pass

    label("Function_12_2D3B")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -24500, 8000, 193000, 225)
    OP_68(-26610, 8600, 194070, 0)
    MoveCamera(18, 12, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22780, 0)
    SetChrPos(0x101, -30700, 8000, 190200, 45)
    SetChrPos(0x102, -29700, 8000, 189200, 45)
    SetChrPos(0x109, -31700, 8000, 189200, 45)
    SetChrPos(0x105, -30700, 8000, 188200, 45)
    SetCameraDistance(21780, 2000)

    def lambda_2DF0():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DF0)
    Sleep(50)

    def lambda_2E08():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E08)
    Sleep(50)

    def lambda_2E20():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2E20)
    Sleep(50)
    FadeToBright(1000, 0)

    def lambda_2E41():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2E41)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#11PYou came.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, here it is.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_68(-27470, 9000, 194940, 1500)
    MoveCamera(6, 20, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(16800, 1500)
    Sleep(200)

    def lambda_2ED8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2ED8)
    Sleep(100)

    def lambda_2EE8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2EE8)
    Sleep(100)

    def lambda_2EF8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2EF8)
    Sleep(100)

    def lambda_2F08():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2F08)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00001F#6P#NIs this the door that was destroyed …?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#12P#N…… Surely something\x01",
            "It has been cut off.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11POh, honestly by the power of human beings\x01",
            "I do not think I can do it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PSo this is the entrance to the old mine.\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x9, 0x0, 0xFF, 0x0, -16500, 10100, 203350, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x32, 1, 0, 13)
    Sleep(200)

    def lambda_301F():
        OP_93(0xFE, 0x2C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_301F)
    Sleep(300)
    OP_68(-25180, 9700, 194680, 2000)
    MoveCamera(45, 4, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(14520, 2000)

    def lambda_305D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_305D)
    Sleep(100)

    def lambda_306D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_306D)
    Sleep(150)

    def lambda_307D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_307D)
    Sleep(100)

    def lambda_308D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_308D)
    Sleep(600)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x109,
        "#10105F#6P#NHere, this light …\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10304F#12P#NHuh, anything\x01",
            "It is a magical atmosphere.\x02\x03",
            "#10300FThere are also devil demons\x01",
            "It sounds like you are wandering around.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00003F#6P#NAh……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopSound(828, 1000, 40)
    Sleep(500)
    Sleep(100)
    OP_68(-27900, 9400, 191850, 1500)
    MoveCamera(45, 20, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(17520, 1500)
    Sleep(1000)

    def lambda_318C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_318C)
    Sleep(100)

    def lambda_319C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_319C)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00108F#11P…… What will you do, Lloyd?\x02\x03",
            "#00101FIn some cases to the guard\x01",
            "I think I can contact you, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PI agree……\x01",
            "I can also increase the search hand.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3249():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3249)
    Sleep(50)

    def lambda_3259():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3259)
    Sleep(50)

    def lambda_3269():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3269)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00003F#5P…… No, first of all we\x01",
            "Let's examine the inside.\x02\x03",
            "#00001FIf I did not seem to get it\x01",
            "Ask the guard for cheering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#11PI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6POK!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PWell, then, when preparing\x01",
            "It seems better to do it all.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, -24500, 8000, 193000, 270)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -28770, 8000, 190930, 45)
    SetScenarioFlags(0x12A, 1)
    OP_29(0xA2, 0x1, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    EventEnd(0x5)
    Return()

    # Function_12_2D3B end

    def Function_13_33B3(): pass

    label("Function_13_33B3")

    Sleep(2300)
    Sound(929, 0, 30, 0)
    Sound(828, 2, 50, 0)
    Sleep(2200)
    Sound(831, 0, 40, 0)
    Sleep(1500)
    Sound(948, 0, 30, 0)
    Sound(830, 0, 30, 0)
    Return()

    # Function_13_33B3 end

    def Function_14_33DB(): pass

    label("Function_14_33DB")

    EventBegin(0x0)
    Fade(500)
    OP_68(-25500, 8600, 194000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -26580, 8000, 194320, 45)
    SetChrPos(0x102, -25580, 8000, 193320, 45)
    SetChrPos(0x109, -27580, 8000, 193320, 45)
    SetChrPos(0x105, -26580, 8000, 192320, 45)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00008F#5P(Probably, if you are looking into this place\x01",
            "There is no room to spare others. )\x02\x03",
            "#00001F(……what will you do?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【There are still other things to do】\x01",          # 0
            "【Step into the former mine】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_352F"),
        (1, "loc_3547"),
        (SWITCH_DEFAULT, "loc_36D8"),
    )


    label("loc_352F")

    SetChrPos(0x0, -27820, 8000, 192000, 225)
    EventEnd(0x5)
    Jump("loc_36D8")

    label("loc_3547")

    OP_4B(0x8, 0xFF)
    Sleep(100)

    def lambda_3553():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3553)
    Sleep(50)

    def lambda_3563():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3563)
    Sleep(50)

    def lambda_3573():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3573)
    Sleep(50)

    def lambda_3583():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3583)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWell then, Mr. Gantz.\x02\x03",
            "I will investigate a bit\x01",
            "Please wait here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POh, be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you think it is dangerous\x01",
            "You will be back soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-23660, 8600, 196120, 2500)
    MoveCamera(44, 15, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(21380, 2500)

    def lambda_366B():

        label("loc_366B")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_366B")

    QueueWorkItem2(0x8, 2, lambda_366B)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 15)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 15)
    Sleep(200)
    BeginChrThread(0x105, 3, 0, 15)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    Sleep(500)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    OP_4C(0x8, 0xFF)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("m4100", 0, 0, 0)
    IdleLoop()
    Jump("loc_36D8")

    label("loc_36D8")

    Return()

    # Function_14_33DB end

    def Function_15_36D9(): pass

    label("Function_15_36D9")

    OP_93(0xFE, 0x2D, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    Return()

    # Function_15_36D9 end

    def Function_16_36F0(): pass

    label("Function_16_36F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    StopEffect(0x0, 0x0)
    LoadEffect(0x1, "event/ev11008.eff")
    ClearMapObjFlags(0x6, 0x4)
    SoundLoad(996)
    OP_68(-26540, 9100, 195770, 0)
    MoveCamera(30, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x8, -25500, 8000, 194000, 225)
    OP_93(0x8, 0xE1, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(996, 2, 30, 0)
    FadeToBright(1000, 0)
    Sound(833, 0, 40, 0)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, -22000, 8500, 197270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    StopSound(996, 4000, 20)
    BeginChrThread(0x8, 3, 0, 17)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5PWhat, what ah ah! Is it?\x02",
    )

    WaitChrThread(0x8, 3)
    CloseMessageWindow()
    OP_64(0x8)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 19)
    WaitChrThread(0x8, 3)

    ChrTalk(
        0x8,
        "#5PWell, what the heck ….\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#4S#5PHey!\x01",
            "Are you all right! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        "#4S#5PPlease reply me if you hear me!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PIt is useless\x01",
            "It seems that the voice is reaching …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAnd just tell everyone!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x8, 3, 0, 20)
    WaitChrThread(0x8, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x8)
    SetScenarioFlags(0x22, 1)
    NewScene("m4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_36F0 end

    def Function_17_3952(): pass

    label("Function_17_3952")

    OP_9B(0x0, 0xFE, 0xF, 0x7D0, 0x1388, 0x1)
    BeginChrThread(0xFE, 2, 0, 18)
    OP_9B(0x1, 0xFE, 0x1E, 0x7D0, 0x1388, 0x1)
    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0x0, 0xFA, 0x3E8)
    OP_9C(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x32, 0x3E8)
    WaitChrThread(0xFE, 2)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    Return()

    # Function_17_3952 end

    def Function_18_39B8(): pass

    label("Function_18_39B8")

    Sleep(50)
    OP_93(0xFE, 0x5A, 0x3E8)
    Return()

    # Function_18_39B8 end

    def Function_19_39C3(): pass

    label("Function_19_39C3")

    OP_9B(0x0, 0xFE, 0x159, 0x7D0, 0xFA0, 0x1)
    OP_68(-21150, 8600, 198420, 1000)
    MoveCamera(45, 8, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(24670, 1000)
    OP_9B(0x0, 0xFE, 0xF, 0xBB8, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x1F4, 0x7D0, 0x0)
    OP_6F(0x1)
    Return()

    # Function_19_39C3 end

    def Function_20_3A21(): pass

    label("Function_20_3A21")

    OP_9B(0x0, 0xFE, 0x87, 0x7D0, 0x1388, 0x1)
    OP_9C(0xFE, 0x1F4, 0x0, 0xFFFFFC18, 0xC8, 0x514)
    OP_9F(0x0, 0xFE)
    OP_68(-17810, 8600, 176550, 1800)
    MoveCamera(103, 14, 0, 1800)
    OP_6E(570, 1800)
    SetCameraDistance(24170, 1800)
    OP_9F(0x1, -24060, 8000, 179360)
    OP_9F(0x1, -18830, 8000, 172310)
    OP_9F(0x1, -19580, 6190, 164770)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    OP_6F(0x1)
    Return()

    # Function_20_3A21 end

    def Function_21_3AAF(): pass

    label("Function_21_3AAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    Call(0, 25)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(71000, 6600, 117380, 0)
    MoveCamera(43, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(44310, 0)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0xB, 0x2C)
    OP_49()
    SetChrPos(0x2C, 96000, 6100, 116000, 270)
    OP_D5(0x2C, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_93(0x2C, 0x10E, 0x0)
    BeginChrThread(0x2C, 3, 0, 22)
    OP_68(54840, 6400, 109190, 6000)
    MoveCamera(12, 10, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(34290, 6000)
    Sound(458, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3AAF end

    def Function_22_3BC3(): pass

    label("Function_22_3BC3")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 68060, 6100, 116000)
    OP_9F(0x1, 63850, 5100, 116200)
    OP_9F(0x1, 59920, 3400, 116450)
    OP_9F(0x1, 57920, 2800, 116670)
    OP_9F(0x1, 54050, 2300, 116670)
    OP_9F(0x1, 42060, 1800, 116840)
    OP_9F(0x1, 37880, 900, 117530)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_22_3BC3 end

    def Function_23_3C33(): pass

    label("Function_23_3C33")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    Call(0, 25)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(-26280, 9500, 189200, 0)
    MoveCamera(12, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(32439, 0)
    OP_68(-24060, 9100, 174650, 3000)
    MoveCamera(4, 10, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(32439, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(-24020, 3700, 131610, 0)
    MoveCamera(34, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(28620, 0)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0xB, 0x2C)
    OP_49()
    SetChrPos(0x2C, 2100, 100, 132550, 295)
    OP_D5(0x2C, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x1, 0x20)
    OP_93(0x2C, 0x127, 0x0)
    BeginChrThread(0x2C, 3, 0, 24)
    Fade(500)
    OP_0D()
    OP_6F(0x79)
    OP_68(-28890, 5300, 118180, 5500)
    MoveCamera(41, 22, 0, 5500)
    OP_6E(510, 5500)
    SetCameraDistance(45260, 5500)
    Sleep(1000)
    Sound(458, 0, 100, 0)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3C33 end

    def Function_24_3DB0(): pass

    label("Function_24_3DB0")

    Sleep(1500)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -7160, 100, 136270)
    OP_9F(0x1, -17940, 100, 135920)
    OP_9F(0x1, -24640, 100, 131910)
    OP_9F(0x1, -31160, 100, 124060)
    OP_9F(0x1, -32000, -200, 115650)
    OP_9F(0x1, -32000, -800, 112000)
    OP_9F(0x1, -32000, -800, 100000)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_24_3DB0 end

    def Function_25_3E23(): pass

    label("Function_25_3E23")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Return()

    # Function_25_3E23 end

    def Function_26_3E38(): pass

    label("Function_26_3E38")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    Call(0, 25)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(480, 600, 7510, 0)
    MoveCamera(19, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(34550, 0)
    OP_68(1970, 600, -2920, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(33700, 5000)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0xB, 0x2C)
    OP_49()
    SetChrPos(0x2C, -13140, 200, 38660, 135)
    OP_D5(0x2C, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x1, 0x20)
    OP_93(0x2C, 0x87, 0x0)
    BeginChrThread(0x2C, 3, 0, 27)
    Sound(458, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    MoveCamera(60, 24, 0, 4000)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_3E38 end

    def Function_27_3F55(): pass

    label("Function_27_3F55")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13140, 200, 38660)
    OP_9F(0x1, -6650, 200, 32140)
    OP_9F(0x1, -1380, 200, 24520)
    OP_9F(0x1, -390, 200, 17010)
    OP_9F(0x1, -500, 200, -6130)
    OP_9F(0x1, -550, 400, -19760)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_27_3F55 end

    def Function_28_3FB7(): pass

    label("Function_28_3FB7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    LoadChrToIndex("chr/ch31251.itc", 0x23)
    LoadChrToIndex("chr/ch31252.itc", 0x24)
    LoadChrToIndex("chr/ch31253.itc", 0x25)
    LoadChrToIndex("apl/ch50515.itc", 0x26)
    LoadChrToIndex("chr/ch41950.itc", 0x32)
    LoadChrToIndex("chr/ch42057.itc", 0x33)
    LoadChrToIndex("chr/ch03450.itc", 0x28)
    LoadEffect(0x0, "battle\\sc008002.eff")
    LoadEffect(0x1, "event\\ev14014.eff")
    LoadEffect(0x2, "battle\\sp003000.eff")
    LoadEffect(0x3, "battle\\sc008100.eff")
    LoadEffect(0x4, "battle/cr414000.eff")
    LoadEffect(0x5, "event/ev14001.eff")
    LoadEffect(0x6, "event/ev14002.eff")
    SoundLoad(469)
    SoundLoad(868)
    SoundLoad(577)
    SoundLoad(586)
    SoundLoad(861)
    SoundLoad(865)
    SoundLoad(866)
    SoundLoad(869)
    SoundLoad(3953)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x32)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x1)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x33)
    SetChrSubChip(0x19, 0x1)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0xC, 0x2D)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFrame(0xC, "mark01", 0x0, 0x1)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0xD, 0x2E)
    OP_49()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "mark01", 0x0, 0x1)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0x2F, 0x80)
    OP_78(0xE, 0x2F)
    OP_49()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    SetMapObjFrame(0xE, "mark01", 0x0, 0x1)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x79, 0xB4, 0x0, 0x20)
    OP_F3(100000)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x18, 2350, 5250, 147800, 225)
    SetChrPos(0x19, 10550, 6000, 145050, 225)
    SetChrPos(0x2D, 0, 250, -10000, 0)
    SetChrPos(0x2E, 0, 250, -20000, 0)
    SetChrPos(0x2F, 0, 250, -30000, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K1 hour ago ──",
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(500)
    OP_68(-410, 1500, -5380, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(28000, 0)
    OP_68(-10670, 1500, 35200, 16000)
    MoveCamera(5, 14, 0, 16000)
    SetCameraDistance(36000, 16000)
    BeginChrThread(0x2D, 3, 0, 29)
    BeginChrThread(0x2E, 3, 0, 29)
    BeginChrThread(0x2F, 3, 0, 29)
    PlayBGM("ed7566", 0)
    Sound(465, 0, 100, 0)
    BeginChrThread(0x32, 1, 0, 39)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(867, 0, 100, 0)
    SetMessageWindowPos(270, 140, -1, -1)
    SetChrName("Communication voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Here the headquarters ──\x01",
            "Tell the third company.\x05\x02",
        )
    )

    Sleep(6500)
    Sound(471, 0, 100, 0)
    SetChrName("Communication voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The size of the armed group is unknown.\x05\x02",
        )
    )

    Sleep(6000)
    OP_57(0x0)
    OP_5A()
    Sound(457, 0, 100, 0)
    Fade(500)
    OP_68(-22250, 1500, 48650, 0)
    MoveCamera(95, 15, 0, 0)
    SetCameraDistance(34000, 0)
    OP_68(-36150, 1500, 70550, 10000)
    MoveCamera(35, 15, 0, 15500)
    SetCameraDistance(35000, 15500)
    OP_0D()
    SetChrName("Communication voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The hunting soldiers hiding in the city\x01",
            "Possibility of \"red constellation\".\x05\x02",
        )
    )

    Sleep(6750)
    SetChrName("Communication voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Damage to the residents of Mainz\x01",
            "Take the utmost care so as not to exceed.\x07\x00\x05\x02",
        )
    )

    Sleep(6750)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(471, 0, 100, 0)
    Fade(500)
    OP_68(-32700, 400, 104650, 0)
    MoveCamera(30, 22, 0, 0)
    SetCameraDistance(22000, 0)
    OP_6B(0x2D)
    MoveCamera(45, 26, 0, 12000)
    SetCameraDistance(30000, 12000)
    OP_0D()
    Sleep(1500)
    SetMessageWindowPos(30, 30, -1, -1)
    SetChrName("Communication voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Third Squadron, OK.\x05\x02",
        )
    )

    Sleep(7000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From this it is an armed group ─\x07\x00\x05\x02",
        )
    )

    WaitChrThread(0x2D, 3)
    OP_71(0xC, 0x79, 0x79, 0x0, 0x0)
    EndChrThread(0x2E, 0x3)

    def lambda_459A():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_459A)

    def lambda_45AF():
        OP_D5(0xFE, 0x0, 0x1ADB0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_45AF)
    OP_74(0xD, 0xF)
    OP_71(0xD, 0x5B, 0x78, 0x0, 0x8)
    EndChrThread(0x2F, 0x3)

    def lambda_45DC():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_45DC)
    OP_74(0xE, 0xF)
    OP_71(0xE, 0x5B, 0x78, 0x0, 0x8)
    OP_6B(0xFF)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    StopSound(469, 500, 100)
    OP_78(0xF, 0x2D)
    OP_49()
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_74(0xF, 0x1E)
    StopBGM(0x0)
    Sound(200, 0, 70, 0)
    Sound(196, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0x2D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x3E8, 0x0, 0xBB8, 0x3E8)
    OP_71(0xF, 0x1, 0x3C, 0x0, 0x8)
    OP_79(0xF)
    Sound(868, 2, 100, 0)
    OP_71(0xF, 0x3D, 0x78, 0x0, 0x20)
    Sleep(1000)
    OP_0D()
    PlayBGM("ed7586", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x24A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(-11650, 1100, 136550, 0)
    MoveCamera(45, 29, 0, 0)
    SetCameraDistance(30000, 0)
    SetCameraDistance(25000, 500)
    OP_0D()
    OP_74(0xD, 0x1E)
    OP_74(0xE, 0x1E)
    SetMessageWindowPos(40, 20, -1, -1)
    SetChrName("Communication voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Conducting mine#8ROvalmain#……! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Communication voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3AWell, all battle placement ──\x07\x00\x02",
        )
    )

    BeginChrThread(0x2E, 3, 0, 30)
    Sleep(1000)
    Fade(250)
    OP_78(0x10, 0x2E)
    OP_49()
    OP_D5(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    OP_74(0x10, 0x1E)
    OP_71(0x10, 0x1, 0x3C, 0x0, 0x8)
    OP_79(0x10)
    OP_71(0x10, 0x3D, 0x78, 0x0, 0x20)
    WaitChrThread(0x2E, 3)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    MoveCamera(45, 32, 0, 3000)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xD, -11800, 600, 135700, 180)
    SetChrPos(0xE, -11800, 600, 135700, 180)
    SetChrPos(0xF, -11800, 600, 135700, 180)
    SetChrPos(0x10, -11800, 600, 135700, 180)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0xD, 3, 0, 31)
    Sleep(300)
    BeginChrThread(0xE, 3, 0, 32)
    Sleep(300)
    BeginChrThread(0xF, 3, 0, 33)
    Sleep(300)
    BeginChrThread(0x10, 3, 0, 34)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    Sound(865, 2, 90, 0)
    Sound(861, 2, 90, 0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, -12000, 0, 134900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x1, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x3, 0xF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x3E8, 0x0, 0xBB8, 0x5DC)
    Sleep(200)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    Sleep(1300)
    Sound(871, 0, 80, 0)
    StopSound(865, 500, 90)
    StopSound(861, 500, 90)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    Sleep(500)
    Fade(250)
    Sound(514, 0, 100, 0)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x26)
    SetChrSubChip(0x10, 0x0)
    OP_0D()
    Sleep(500)
    Fade(500)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x11, -23450, 750, 134000, 250)
    SetChrPos(0x12, -23450, 750, 134000, 250)
    SetChrPos(0x13, -23450, 750, 134000, 250)
    SetChrPos(0x14, -23450, 750, 134000, 250)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, 4720, 6000, 147900, 225)
    SetChrPos(0x16, 6820, 6000, 145170, 225)
    SetChrPos(0x17, 8210, 6000, 144440, 225)
    SetChrPos(0x1D, 5120, 6000, 144550, 225)
    OP_68(-21010, 1700, 135220, 0)
    MoveCamera(25, 25, -2, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetCameraDistance(25000, 1500)
    Sound(586, 2, 70, 0)
    Sound(577, 2, 80, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1388)
    PlayEffect(0x2, 0x1, 0xFF, 0x0, -23450, 0, 134000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_87(0x3, 0x0, 0xE, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sound(464, 0, 100, 0)
    OP_71(0xE, 0x0, 0x14, 0x0, 0x0)
    OP_79(0xE)
    BeginChrThread(0x11, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x12, 3, 0, 36)
    Sleep(300)
    StopEffect(0x1, 0x2)
    BeginChrThread(0x13, 3, 0, 37)
    Sleep(300)
    BeginChrThread(0x14, 3, 0, 38)
    Sleep(500)
    Sound(463, 0, 100, 0)
    OP_71(0xE, 0x1E, 0x32, 0x0, 0x0)
    OP_79(0xE)
    OP_74(0xE, 0x2)
    OP_71(0xE, 0x12C, 0x12A, 0x0, 0x0)
    OP_79(0xE)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    StopEffect(0x0, 0x2)
    StopSound(586, 500, 70)
    StopSound(577, 500, 80)
    Sound(866, 0, 100, 0)
    Sleep(500)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x1D,
        "Daughter's voice",
        (
            "#35A#3953V#30WAhaha …\x01",
            "It's quite a bad response.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_68(5200, 6900, 144650, 2000)
    MoveCamera(20, 12, 0, 2000)
    SetCameraDistance(18500, 2000)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1D,
        (
            "Hehu ……\x01",
            "Is it the first time in three months for a real battle?\x02\x03",
            "Finally \"Tester = Rossa\"\x01",
            "It seems I can satisfy you ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0xD,
        "Damn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "What, who are you! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04602F#11P── Starting a sweeping game.\x01",
            "Let's hold down to the tunnel first.\x02\x03",
            "#04612FYou can kill everyone who faces you\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(290, 30, -1, -1)
    SetChrName("R-right!")
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    AnonymousTalk(
        0xFF,
        "#4Sroger that#4RYa#It is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_25(0x364, 0x5A)
    Sleep(200)
    OP_25(0x364, 0x50)
    Sleep(200)
    OP_25(0x364, 0x46)
    Sleep(200)
    OP_25(0x364, 0x3C)
    Sleep(200)
    Sleep(200)
    Sleep(1500)
    OP_71(0xF, 0x79, 0xF0, 0x0, 0x20)
    OP_71(0x10, 0x79, 0xF0, 0x0, 0x20)
    OP_78(0x11, 0x2F)
    OP_49()
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0x79, 0xF0, 0x0, 0x20)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    PlayEffect(0x5, 0x0, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x10, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x2, 0x14, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-21010, 1000, 135220, 0)
    MoveCamera(40, 23, -5, 0)
    SetCameraDistance(24000, 0)
    OP_6E(500, 0)
    MoveCamera(45, 25, -5, 3000)
    SetCameraDistance(29000, 3000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x96, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrPos(0x2D, -35750, 0, 65550, 315)
    SetChrPos(0xD, -36550, 0, 70200, 0)
    SetChrPos(0xE, -35400, 0, 59650, 135)
    PlayEffect(0x5, 0x0, 0xD, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-36760, 1000, 70070, 0)
    MoveCamera(50, 14, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(15200, 0)
    OP_68(-36450, 1300, 65180, 6000)
    MoveCamera(58, 19, -5, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(18000, 6000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x2F, 250, 0, 2000, 70)
    SetChrPos(0xD, -1750, 0, 5650, 0)
    SetChrPos(0xE, 1500, 0, -2550, 315)
    PlayEffect(0x5, 0x0, 0xD, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-600, 1750, 8400, 0)
    MoveCamera(40, 7, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(16600, 0)
    OP_68(-500, 1750, -5000, 6000)
    MoveCamera(50, 25, -5, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(18100, 6000)
    Sleep(5000)
    StopSound(868, 1000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D5)
    OP_24(0x364)
    OP_24(0x241)
    OP_24(0x24A)
    OP_24(0x35D)
    OP_24(0x361)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_3FB7 end

    def Function_29_52F7(): pass

    label("Function_29_52F7")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -330, 0, 18450)
    OP_9F(0x1, -1340, 0, 24860)
    OP_9F(0x1, -10950, 0, 37180)
    OP_9F(0x1, -23380, 0, 49190)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -27790, 0, 53200)
    OP_9F(0x1, -34120, 0, 61210)
    OP_9F(0x1, -34850, 0, 65540)
    OP_9F(0x1, -36260, 0, 80660)
    OP_9F(0x1, -32229, 0, 91050)
    OP_9F(0x1, -32229, -1000, 105220)
    OP_9F(0x1, -32229, -1000, 108220)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -32229, -1000, 110120)
    OP_9F(0x1, -32229, 0, 120970)
    OP_9F(0x1, -29470, 0, 127710)
    OP_9F(0x1, -20460, 0, 135510)
    OP_9F(0x1, -10260, 0, 136910)
    OP_9F(0x1, -1960, 0, 134520)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_29_52F7 end

    def Function_30_540D(): pass

    label("Function_30_540D")

    Sound(869, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2E, 0x0, -500, 0, -20000, 30, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2E, 0x0, 1000, 0, -19000, 30, 40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    OP_82(0x3E8, 0x0, 0xBB8, 0x1F4)
    Sound(200, 0, 70, 0)
    Sound(196, 0, 80, 0)
    PlayEffect(0x6, 0xFF, 0x2E, 0x0, -500, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x3E8, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x6, 0xFF, 0x2E, 0x0, 1000, 0, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Return()

    # Function_30_540D end

    def Function_31_552A(): pass

    label("Function_31_552A")


    def lambda_552F():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_552F)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0xD, 1)
    OP_95(0xD, -8350, 0, 134700, 4000, 0x0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_31_552A end

    def Function_32_5576(): pass

    label("Function_32_5576")


    def lambda_557B():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_557B)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0xE, 1)
    OP_95(0xE, -14150, 0, 135000, 4000, 0x0)
    OP_95(0xE, -15650, 0, 137600, 4000, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x2)
    Return()

    # Function_32_5576 end

    def Function_33_55D0(): pass

    label("Function_33_55D0")


    def lambda_55D5():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_55D5)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0xF, 1)
    OP_95(0xF, -8000, 0, 133000, 4000, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x2)
    Return()

    # Function_33_55D0 end

    def Function_34_5616(): pass

    label("Function_34_5616")


    def lambda_561B():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_561B)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x10, 1)
    OP_95(0x10, -15400, 0, 134000, 4000, 0x0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x2)
    Return()

    # Function_34_5616 end

    def Function_35_5662(): pass

    label("Function_35_5662")


    def lambda_5667():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5667)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x11, 1)
    OP_95(0x11, -20920, 0, 132340, 4000, 0x0)
    OP_93(0x11, 0x46, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x2)
    Return()

    # Function_35_5662 end

    def Function_36_56B5(): pass

    label("Function_36_56B5")


    def lambda_56BA():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_56BA)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x12, 1)
    OP_95(0x12, -25270, 0, 136260, 4000, 0x0)
    OP_93(0x12, 0x46, 0x1F4)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x2)
    Return()

    # Function_36_56B5 end

    def Function_37_5702(): pass

    label("Function_37_5702")


    def lambda_5707():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5707)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x13, 1)
    OP_95(0x13, -24450, 0, 131530, 4000, 0x0)
    OP_93(0x13, 0x46, 0x1F4)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x2)
    Return()

    # Function_37_5702 end

    def Function_38_574F(): pass

    label("Function_38_574F")


    def lambda_5754():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5754)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x14, 1)
    OP_95(0x14, -26170, 0, 133270, 4000, 0x0)
    OP_93(0x14, 0x46, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x2)
    Return()

    # Function_38_574F end

    def Function_39_57A2(): pass

    label("Function_39_57A2")

    Sound(469, 2, 20, 0)
    Sleep(100)
    OP_25(0x1D5, 0x1E)
    Sleep(100)
    OP_25(0x1D5, 0x28)
    Sleep(100)
    OP_25(0x1D5, 0x32)
    Sleep(100)
    OP_25(0x1D5, 0x3C)
    Sleep(100)
    OP_25(0x1D5, 0x46)
    Sleep(100)
    OP_25(0x1D5, 0x50)
    Sleep(100)
    OP_25(0x1D5, 0x5A)
    Sleep(100)
    OP_25(0x1D5, 0x64)
    Return()

    # Function_39_57A2 end

    def Function_40_57E1(): pass

    label("Function_40_57E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("monster/ch82053.itc", 0x20)
    LoadChrToIndex("apl/ch51428.itc", 0x46)
    LoadChrToIndex("apl/ch51429.itc", 0x47)
    LoadChrToIndex("chr/ch0035E.itc", 0x48)
    LoadChrToIndex("apl/ch51430.itc", 0x49)
    LoadChrToIndex("chr/ch41950.itc", 0x32)
    LoadChrToIndex("chr/ch41951.itc", 0x33)
    LoadChrToIndex("chr/ch41952.itc", 0x34)
    LoadChrToIndex("chr/ch41953.itc", 0x35)
    LoadChrToIndex("chr/ch41954.itc", 0x36)
    LoadEffect(0x0, "event/ev14020.eff")
    LoadEffect(0x1, "battle/sp003000.eff")
    LoadEffect(0x2, "battle/ms00000.eff")
    LoadEffect(0x3, "battle/btgun00.eff")
    LoadEffect(0x4, "event/ev14021.eff")
    SoundLoad(3320)
    SoundLoad(2761)
    SoundLoad(2762)
    SoundLoad(2763)
    SoundLoad(2764)
    SoundLoad(3954)
    SoundLoad(3955)
    SoundLoad(3956)
    SoundLoad(3933)
    SoundLoad(580)
    SoundLoad(291)
    SoundLoad(861)
    SoundLoad(865)
    OP_32(0xFF, 0xFF, 0x0)
    SetChrPos(0x101, -27840, 8000, 191100, 180)
    SetChrPos(0x102, -26070, 8000, 191780, 180)
    SetChrPos(0x103, -28370, 8000, 192020, 180)
    SetChrPos(0x109, -29440, 8000, 192310, 180)
    SetChrPos(0x105, -26390, 8000, 193520, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x1C, 0x46)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x15, 0x33)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x33)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x33)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x33)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x33)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x21, 0x20)
    SetChrChipByIndex(0x22, 0x1F)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x22, 0x20)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x23, 0x20)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x20)
    OP_F3(100000)
    SetChrPos(0x1C, -20150, 5250, 161000, 135)
    ClearChrFlags(0x1C, 0x4)

    def lambda_5A36():
        OP_95(0x1C, -10150, 4000, 151000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5A36)
    BeginChrThread(0x1C, 3, 0, 53)
    OP_68(-20150, 5850, 161000, 0)
    MoveCamera(15, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_6B(0x1C)
    MoveCamera(10, 25, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(16000, 2000)
    OP_82(0x64, 0x0, 0xBB8, 0x7D0)
    Sound(291, 2, 80, 0)
    Sound(580, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x1C, 1)
    EndChrThread(0x1C, 0x3)
    SetChrFlags(0x1C, 0x4)
    Fade(500)
    OP_6B(0xFF)
    OP_68(-3950, 600, 134100, 0)
    MoveCamera(40, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    OP_68(-1000, 600, 134250, 1500)
    MoveCamera(45, 22, 0, 1500)
    SetCameraDistance(19750, 500)
    SetChrPos(0x15, -850, 0, 134500, 90)
    SetChrPos(0x16, -2850, 0, 134750, 90)
    SetChrPos(0x17, -2850, 0, 133250, 90)
    SetChrPos(0x18, -4850, 0, 134750, 90)
    SetChrPos(0x19, -4850, 0, 133250, 90)
    SetChrPos(0x1A, -6850, 0, 134750, 90)
    SetChrPos(0x1B, -6850, 0, 133250, 90)

    def lambda_5BAA():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5BAA)

    def lambda_5BBF():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5BBF)

    def lambda_5BD4():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5BD4)

    def lambda_5BE9():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5BE9)

    def lambda_5BFE():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5BFE)

    def lambda_5C13():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5C13)

    def lambda_5C28():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5C28)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x1, 0x0, 0x1A, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(861, 2, 80, 0)
    WaitChrThread(0x1A, 1)
    SetChrChipByIndex(0x1A, 0x35)
    BeginChrThread(0x1A, 3, 0, 62)

    ChrTalk(
        0x1A,
        "#10A#5PHang on!\x02",
    )

    WaitChrThread(0x1B, 1)
    SetChrChipByIndex(0x1B, 0x35)
    BeginChrThread(0x1B, 3, 0, 62)

    ChrTalk(
        0x1B,
        "#10A#6PWow …! Is it?\x02",
    )

    StopEffect(0x0, 0x2)
    OP_24(0x35D)
    StopSound(291, 500, 80)
    StopSound(580, 500, 50)
    WaitChrThread(0x15, 1)

    def lambda_5CED():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5CED)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x0)
    WaitChrThread(0x18, 1)
    SetChrChipByIndex(0x18, 0x32)
    SetChrSubChip(0x18, 0x0)
    WaitChrThread(0x19, 1)
    SetChrChipByIndex(0x19, 0x32)
    SetChrSubChip(0x19, 0x0)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5D42():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5D42)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5D6A():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_5D6A)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5D8F():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_5D8F)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5DB7():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_5DB7)
    Sleep(50)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5DDF():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_5DDF)
    Sleep(1000)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 2)
    WaitChrThread(0x17, 2)
    WaitChrThread(0x18, 2)
    WaitChrThread(0x19, 2)

    ChrTalk(
        0x16,
        "#11PI mean …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#4P…… No way!\x01",
            "Captain Randolph! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    ChrTalk(
        0x15,
        (
            "#2PDrop out!\x01",
            "Do not stay in one place!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-3700, 600, 134450, 1500)
    MoveCamera(45, 25, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(22000, 1500)
    BeginChrThread(0x18, 3, 0, 46)
    Sleep(50)
    BeginChrThread(0x19, 3, 0, 47)
    Sleep(50)
    BeginChrThread(0x16, 3, 0, 43)
    Sleep(50)
    BeginChrThread(0x17, 3, 0, 44)
    Sleep(50)
    BeginChrThread(0x15, 3, 0, 41)
    WaitChrThread(0x15, 3)
    Sound(865, 2, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    BeginChrThread(0x15, 0, 0, 49)
    BeginChrThread(0x15, 3, 0, 50)
    WaitChrThread(0x16, 3)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x16, 3, 0, 50)
    WaitChrThread(0x18, 3)
    BeginChrThread(0x18, 0, 0, 49)
    BeginChrThread(0x18, 3, 0, 50)
    WaitChrThread(0x17, 3)
    BeginChrThread(0x17, 0, 0, 49)
    BeginChrThread(0x17, 3, 0, 50)
    WaitChrThread(0x19, 3)
    BeginChrThread(0x19, 0, 0, 49)
    BeginChrThread(0x19, 3, 0, 50)
    OP_6F(0x79)
    Sleep(1000)
    OP_25(0x361, 0x28)
    Sound(861, 2, 60, 0)
    Fade(500)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x19, 0x3)
    OP_68(-10150, 4600, 151000, 0)
    MoveCamera(45, 30, 5, 0)
    SetCameraDistance(22000, 0)
    OP_6B(0x1C)
    MoveCamera(90, 30, 0, 3000)
    SetCameraDistance(18000, 3000)
    PlayEffect(0x0, 0x0, 0x1C, 0x5, 3000, 3000, -8000, 90, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    SetChrFlags(0x1C, 0x800)
    ClearChrFlags(0x1C, 0x4)
    OP_95(0x1C, -430, 4000, 148540, 7000, 0x0)
    OP_95(0x1C, 5180, 6000, 148550, 7000, 0x0)
    StopEffect(0x0, 0x2)
    StopSound(865, 1000, 30)
    StopSound(861, 1000, 50)
    OP_95(0x1C, 9820, 6000, 144350, 7000, 0x0)
    OP_93(0x1C, 0xE1, 0x1F4)
    SetChrFlags(0x1C, 0x4)
    Sound(358, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1C,
        "#00314F#2761V#5P#8A#30WSlow\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Fade(250)
    SetChrChipByIndex(0x1C, 0x47)
    SetChrFlags(0x1C, 0x2)
    SetChrSubChip(0x1C, 0x0)
    OP_0D()
    Sound(318, 0, 100, 0)
    Sound(859, 0, 50, 0)
    OP_A1(0x1C, 0x5DC, 0x2, 0x0, 0x6)
    Sleep(100)
    OP_A0(0x1C, 1500, 0x1, 0x2)
    SetChrSubChip(0x1C, 0x3)
    PlayEffect(0x4, 0x1, 0x1C, 0x3, 0, -6500, 10500, 5, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x4, 0x2, 0x1C, 0x3, 0, -6500, 10500, -5, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    Sleep(500)
    OP_A0(0x1C, 1500, 0x4, 0x5)
    Fade(250)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x2)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    BeginChrThread(0x1C, 3, 0, 51)
    Sound(291, 2, 80, 0)
    Sound(580, 2, 50, 0)
    Sleep(1000)
    EndChrThread(0x1C, 0x3)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    Fade(500)
    ClearChrFlags(0x1C, 0x800)
    OP_6B(0xFF)
    OP_68(-3700, 600, 134450, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    TurnDirection(0x15, 0x1C, 0)
    TurnDirection(0x16, 0x1C, 0)
    TurnDirection(0x17, 0x1C, 0)
    TurnDirection(0x18, 0x1C, 0)
    TurnDirection(0x19, 0x1C, 0)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 50, 0)
    BeginChrThread(0x15, 0, 0, 49)
    BeginChrThread(0x15, 3, 0, 50)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x16, 3, 0, 50)
    BeginChrThread(0x17, 0, 0, 49)
    BeginChrThread(0x17, 3, 0, 50)
    BeginChrThread(0x18, 0, 0, 49)
    BeginChrThread(0x18, 3, 0, 50)
    BeginChrThread(0x19, 0, 0, 49)
    BeginChrThread(0x19, 3, 0, 50)
    PlayEffect(0x4, 0x0, 0xFF, 0x0, -1000, 0, 135500, 225, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 700)
    PlayEffect(0x4, 0x1, 0xFF, 0x0, -4400, 0, 138500, 225, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 400)
    OP_0D()
    OP_25(0x123, 0x14)
    OP_25(0x244, 0x14)
    OP_4B(0x15, 0x0)
    OP_4B(0x15, 0x3)
    SetChrFlags(0x15, 0x20)

    def lambda_62BE():
        OP_96(0xFE, 0xFFFFFF06, 0x0, 0x2049A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_62BE)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    SetChrFlags(0x16, 0x20)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x1)

    def lambda_62ED():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0x21F8E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_62ED)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Sound(200, 0, 100, 0)
    Sound(833, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0x16, 0x34)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x16, 3, 0, 50)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x18, 0x3)
    SetChrFlags(0x18, 0x20)
    SetChrChipByIndex(0x18, 0x35)
    SetChrSubChip(0x18, 0x0)

    def lambda_634C():
        OP_96(0xFE, 0xFFFFE638, 0x0, 0x2130E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_634C)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Sound(196, 0, 100, 0)
    Sleep(500)
    SetChrChipByIndex(0x18, 0x34)
    BeginChrThread(0x18, 0, 0, 49)
    BeginChrThread(0x18, 3, 0, 50)
    ClearChrFlags(0x15, 0x20)
    OP_4C(0x15, 0x0)
    OP_4C(0x15, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x1, 0x2, 0xFF, 0x0, -3750, 0, 137850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    SetChrChipByIndex(0x16, 0x35)
    BeginChrThread(0x16, 3, 0, 62)

    ChrTalk(
        0x16,
        "#10A#6PWow! Is it?\x02",
    )

    Sleep(1500)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x18, 0x3)
    SetChrChipByIndex(0x18, 0x35)
    BeginChrThread(0x18, 3, 0, 62)
    WaitChrThread(0x18, 3)
    OP_25(0x361, 0x32)
    OP_25(0x35D, 0x28)

    ChrTalk(
        0x18,
        "#6PAs expected it is a captain …!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    TurnDirection(0x15, 0x19, 500)

    ChrTalk(
        0x15,
        (
            "Well!\x01",
            "Hit Cougar!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x19, 0x0)
    EndChrThread(0x19, 0x3)
    Sleep(300)
    OP_93(0x19, 0x5A, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x19, 0x36)
    SetChrSubChip(0x19, 0x0)
    OP_0D()
    Sound(947, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    StopEffect(0x2, 0x0)
    StopSound(865, 490, 40)
    StopSound(861, 490, 40)
    OP_24(0x123)
    OP_24(0x244)
    Sound(948, 0, 100, 0)
    Fade(500)
    OP_68(9820, 6600, 144350, 0)
    MoveCamera(80, 15, 5, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x21, 21700, 10000, 144400, 270)
    SetChrPos(0x22, -3450, 4000, 149200, 90)
    SetChrPos(0x23, 5640, 10000, 153370, 134)
    SetChrPos(0x24, 9200, 10000, 153110, 180)
    BeginChrThread(0x21, 3, 0, 58)
    BeginChrThread(0x22, 3, 0, 59)
    BeginChrThread(0x23, 3, 0, 60)
    BeginChrThread(0x24, 3, 0, 61)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    BeginChrThread(0x1C, 3, 0, 51)
    Sound(291, 2, 80, 0)
    Sound(580, 2, 50, 0)
    Sleep(500)
    StopSound(291, 500, 80)
    StopSound(580, 500, 50)
    EndChrThread(0x1C, 0x3)

    def lambda_659C():

        label("loc_659C")

        TurnDirection(0xFE, 0x21, 1000)
        Yield()
        Jump("loc_659C")

    QueueWorkItem2(0x1C, 2, lambda_659C)
    WaitChrThread(0x21, 3)
    OP_68(8450, 6600, 145850, 500)
    MoveCamera(60, 30, -5, 500)
    OP_6E(500, 500)
    SetCameraDistance(20000, 500)
    Sound(844, 0, 50, 0)
    SetChrChipByIndex(0x1C, 0x49)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0x21FC, 0x1770, 0x23F32, 0x3E8, 0x1770)
    SetChrSubChip(0x1C, 0x0)
    Sound(62, 0, 100, 0)

    def lambda_660F():

        label("loc_660F")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_660F")

    QueueWorkItem2(0x21, 2, lambda_660F)
    BeginChrThread(0x21, 0, 0, 57)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)

    def lambda_6633():

        label("loc_6633")

        TurnDirection(0xFE, 0x22, 1000)
        Yield()
        Jump("loc_6633")

    QueueWorkItem2(0x1C, 2, lambda_6633)
    WaitChrThread(0x22, 3)
    OP_68(11050, 6600, 145550, 500)
    MoveCamera(355, 28, -5, 500)
    OP_6E(500, 500)
    SetCameraDistance(20000, 500)
    Sound(844, 0, 70, 0)
    SetChrChipByIndex(0x1C, 0x49)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0x2D82, 0x186A, 0x241F8, 0x3E8, 0x1770)
    SetChrSubChip(0x1C, 0x0)
    Sound(63, 0, 100, 0)

    def lambda_66A6():

        label("loc_66A6")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_66A6")

    QueueWorkItem2(0x22, 2, lambda_66A6)
    BeginChrThread(0x22, 0, 0, 57)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)

    def lambda_66CA():

        label("loc_66CA")

        TurnDirection(0xFE, 0x23, 1000)
        Yield()
        Jump("loc_66CA")

    QueueWorkItem2(0x1C, 2, lambda_66CA)
    WaitChrThread(0x23, 3)
    OP_68(10400, 7500, 146150, 500)
    MoveCamera(60, 28, 10, 500)
    OP_6E(500, 500)
    SetCameraDistance(20000, 500)
    Sound(844, 0, 70, 0)
    SetChrChipByIndex(0x1C, 0x49)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0x30A2, 0x1770, 0x23988, 0x3E8, 0x1770)
    SetChrSubChip(0x1C, 0x0)
    Sound(62, 0, 100, 0)

    def lambda_673D():

        label("loc_673D")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_673D")

    QueueWorkItem2(0x23, 2, lambda_673D)
    BeginChrThread(0x23, 0, 0, 57)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)

    def lambda_6761():

        label("loc_6761")

        TurnDirection(0xFE, 0x24, 1000)
        Yield()
        Jump("loc_6761")

    QueueWorkItem2(0x1C, 2, lambda_6761)
    WaitChrThread(0x24, 3)
    OP_68(14150, 6600, 145450, 500)
    MoveCamera(335, 21, -5, 500)
    OP_6E(500, 500)
    SetCameraDistance(19000, 500)
    Sound(844, 0, 70, 0)
    SetChrChipByIndex(0x1C, 0x49)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0x413C, 0x1770, 0x233DE, 0x3E8, 0x1770)
    SetChrSubChip(0x1C, 0x0)
    Sound(63, 0, 100, 0)

    def lambda_67D4():

        label("loc_67D4")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_67D4")

    QueueWorkItem2(0x24, 2, lambda_67D4)
    BeginChrThread(0x24, 0, 0, 57)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1C,
        "#00312F#2762V#12P#16A#30WHappy … I do not understand.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    EndChrThread(0x1C, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    SetCameraDistance(16000, 100)
    Sound(358, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrFlags(0x1C, 0x20)
    SetChrSubChip(0x1C, 0x1)

    def lambda_6867():
        OP_96(0xFE, 0x3746, 0x1770, 0x236FE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6867)
    Sleep(100)
    EndChrThread(0x1C, 0x1)
    ClearChrFlags(0x1C, 0x20)
    EndChrThread(0x21, 0x0)
    EndChrThread(0x22, 0x0)
    EndChrThread(0x23, 0x0)
    EndChrThread(0x24, 0x0)
    OP_24(0x244)
    OP_24(0x123)
    OP_24(0x35D)
    OP_24(0x361)
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xFFFFFFFF, 0x30200020, "", 0x30000300, 0x0, 0x0, 0x0, 0x30082000, 0x30082000, 0x30082000, 0x30082000, 0x0, 0x0, 0x0, 0x0, 0x24A, 0x8)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04602.itp")
    OP_D7(0x0)
    OP_D7(0x10)
    OP_D7(0x11)
    OP_D7(0x12)
    OP_D7(0x13)
    OP_D7(0x14)
    OP_D7(0x15)
    OP_D7(0x16)
    OP_D7(0x17)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("monster/ch82053.itc", 0x20)
    LoadChrToIndex("apl/ch51428.itc", 0x46)
    LoadChrToIndex("chr/ch0035E.itc", 0x47)
    LoadChrToIndex("chr/ch0035C.itc", 0x48)
    LoadChrToIndex("apl/ch51431.itc", 0x49)
    LoadChrToIndex("apl/ch51437.itc", 0x4A)
    LoadChrToIndex("apl/ch51430.itc", 0x4B)
    LoadChrToIndex("apl/ch51432.itc", 0x4C)
    LoadChrToIndex("chr/ch03450.itc", 0x28)
    LoadChrToIndex("chr/ch03451.itc", 0x29)
    LoadChrToIndex("chr/ch03452.itc", 0x2A)
    LoadChrToIndex("chr/ch0345F.itc", 0x2B)
    LoadChrToIndex("apl/ch51442.itc", 0x2C)
    LoadChrToIndex("apl/ch51433.itc", 0x2D)
    LoadChrToIndex("chr/ch41950.itc", 0x32)
    LoadChrToIndex("chr/ch41951.itc", 0x33)
    LoadChrToIndex("chr/ch41952.itc", 0x34)
    LoadChrToIndex("chr/ch41953.itc", 0x35)
    LoadChrToIndex("chr/ch00050.itc", 0x37)
    LoadChrToIndex("chr/ch00051.itc", 0x38)
    LoadChrToIndex("chr/ch00052.itc", 0x39)
    LoadChrToIndex("chr/ch00150.itc", 0x3C)
    LoadChrToIndex("chr/ch00151.itc", 0x3D)
    LoadChrToIndex("chr/ch00152.itc", 0x3E)
    LoadChrToIndex("chr/ch00250.itc", 0x41)
    LoadChrToIndex("chr/ch00251.itc", 0x42)
    LoadChrToIndex("chr/ch00254.itc", 0x43)
    LoadChrToIndex("chr/ch02950.itc", 0x50)
    LoadChrToIndex("chr/ch02951.itc", 0x51)
    LoadChrToIndex("chr/ch02952.itc", 0x52)
    LoadChrToIndex("chr/ch03050.itc", 0x55)
    LoadChrToIndex("chr/ch03051.itc", 0x56)
    LoadChrToIndex("apl/ch51436.itc", 0x57)
    LoadEffect(0x0, "battle/mg040_00.eff")
    LoadEffect(0x1, "battle/sp003000.eff")
    LoadEffect(0x2, "battle/ms00000.eff")
    LoadEffect(0x3, "battle/btgun00.eff")
    LoadEffect(0x4, "event/ev14021.eff")
    LoadEffect(0x5, "event/ev14020.eff")
    LoadEffect(0x6, "battle/mgaria0.eff")
    LoadEffect(0x7, "battle/mgaria1.eff")
    LoadEffect(0x8, "battle/sc003200.eff")
    LoadEffect(0x9, "event/eva01_01.eff")
    LoadEffect(0xA, "event/ev606_00.eff")
    LoadEffect(0xF, "battle/sc003203.eff")
    SoundLoad(580)
    SoundLoad(291)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(870)
    SoundLoad(875)
    SoundLoad(863)
    SoundLoad(196)
    SoundLoad(566)
    SetMapObjFlags(0x5, 0x1000)
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x30)
    SetChrChipByIndex(0x15, 0x32)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x35)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x32)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x35)
    SetChrSubChip(0x1A, 0x3)
    SetChrChipByIndex(0x1B, 0x35)
    SetChrSubChip(0x1B, 0x3)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrSubChip(0x1D, 0x1)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x21, 0x20)
    SetChrSubChip(0x21, 0x1)
    SetChrChipByIndex(0x22, 0x20)
    SetChrSubChip(0x22, 0x1)
    SetChrChipByIndex(0x23, 0x20)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0x0)
    SetChrChipByIndex(0x30, 0x4C)
    SetChrSubChip(0x30, 0x0)
    SetChrFlags(0x30, 0x20)
    SetChrFlags(0x30, 0x2)
    SetChrFlags(0x30, 0x8000)
    ClearChrFlags(0x30, 0x1)
    SetChrPos(0x30, -21250, -200, 135950, 0)
    SetChrChipByIndex(0x31, 0x4C)
    SetChrSubChip(0x31, 0x0)
    SetChrFlags(0x31, 0x20)
    SetChrFlags(0x31, 0x2)
    SetChrFlags(0x31, 0x8000)
    ClearChrFlags(0x31, 0x1)
    SetChrPos(0x31, -20000, 1000, 137600, 0)
    OP_52(0x31, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F3(100000)
    SetChrPos(0x1C, 8100, 6000, 147450, 300)

    def lambda_6C3B():
        OP_96(0xFE, 0x14B4, 0x1770, 0x24252, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6C3B)
    OP_68(9000, 6600, 147400, 0)
    MoveCamera(55, 15, 5, 0)
    OP_6E(600, 0)
    SetCameraDistance(14300, 0)
    SetCameraDistance(16300, 500)
    Sound(251, 0, 100, 0)
    FadeToBright(500, 16777215)
    OP_0D()
    WaitChrThread(0x1C, 1)
    Sound(358, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_A0(0x1C, 2000, 0x31, 0x37)
    Sleep(300)
    Sound(288, 0, 100, 0)
    Sound(540, 0, 80, 0)
    OP_A0(0x1C, 6000, 0x38, 0x3C)
    Sound(948, 0, 100, 0)
    PlayEffect(0x8, 0x0, 0x21, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x1, 0x22, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x2, 0x23, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x3, 0x24, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(289, 0, 100, 0)
    Sound(514, 0, 100, 0)
    Sound(833, 0, 70, 0)
    Sleep(500)

    def lambda_6DC0():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_6DC0)

    def lambda_6DD1():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 3, lambda_6DD1)

    def lambda_6DE2():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_6DE2)

    def lambda_6DF3():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_6DF3)
    WaitChrThread(0x21, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x23, 3)
    WaitChrThread(0x24, 3)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    Sleep(1000)
    Fade(500)
    TurnDirection(0x15, 0x1C, 0)
    TurnDirection(0x17, 0x1C, 0)
    TurnDirection(0x19, 0x1C, 0)
    OP_68(-3700, 600, 134450, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    ChrTalk(
        0x17,
        "#11POh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#5POh, the red death god … …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x19, 500)

    ChrTalk(
        0x15,
        (
            "Do not get swallowed!\x01",
            "Get it down with a wavy attack!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x0, 0x1F4)
    SetChrChipByIndex(0x15, 0x34)
    BeginChrThread(0x15, 3, 0, 50)
    Sound(865, 2, 60, 0)
    OP_68(-7750, 600, 136150, 2000)
    MoveCamera(45, 25, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(20000, 2000)
    SetChrChipByIndex(0x19, 0x33)

    def lambda_6F18():
        OP_95(0xFE, -14850, 0, 140200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6F18)
    Sleep(100)
    SetChrChipByIndex(0x17, 0x33)

    def lambda_6F39():
        OP_95(0xFE, -14850, 10, 139000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6F39)
    OP_6F(0x79)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x19, 0x1)
    Fade(500)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    StopSound(865, 500, 60)
    SetChrPos(0x17, -11400, 0, 137850, 275)
    SetChrPos(0x19, -13600, 0, 137850, 275)
    SetChrPos(0x15, -10600, 0, 135600, 275)
    OP_68(-20000, 5000, 152050, 0)
    MoveCamera(55, 30, -5, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(-19450, 2000, 145100, 4000)
    MoveCamera(60, 30, -10, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(20750, 4000)
    ClearChrFlags(0x1C, 0x20)
    ClearChrFlags(0x1C, 0x2)
    SetChrPos(0x1C, -15900, 4040, 156150, 230)
    SetChrChipByIndex(0x1C, 0x46)
    OP_95(0x1C, -20000, 4000, 152050, 7000, 0x0)
    OP_93(0x1C, 0xB4, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x1388)
    SetChrChipByIndex(0x1C, 0x47)
    BeginChrThread(0x1C, 3, 0, 51)
    Sound(291, 2, 80, 0)
    Sound(580, 2, 50, 0)
    Sound(861, 2, 50, 0)
    PlayEffect(0x1, 0x0, 0x17, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x19, 3, 0, 48)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 45)
    Sleep(500)
    BeginChrThread(0x15, 3, 0, 42)
    WaitChrThread(0x19, 3)
    SetChrChipByIndex(0x19, 0x34)
    BeginChrThread(0x19, 0, 0, 49)
    BeginChrThread(0x19, 3, 0, 50)
    WaitChrThread(0x17, 3)
    SetChrChipByIndex(0x17, 0x34)
    BeginChrThread(0x17, 0, 0, 49)
    BeginChrThread(0x17, 3, 0, 50)
    WaitChrThread(0x15, 3)
    SetChrChipByIndex(0x15, 0x34)
    BeginChrThread(0x15, 0, 0, 49)
    BeginChrThread(0x15, 3, 0, 50)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x19, 0x3)
    SetChrChipByIndex(0x19, 0x35)
    BeginChrThread(0x19, 3, 0, 62)
    Sleep(500)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    SetChrChipByIndex(0x17, 0x35)
    BeginChrThread(0x17, 3, 0, 62)
    OP_6F(0x79)
    Sleep(1000)
    OP_82(0x0, 0x0, 0xBB8, 0x0)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    SetChrChipByIndex(0x15, 0x35)
    SetChrSubChip(0x15, 0x3)
    StopSound(291, 300, 80)
    StopSound(580, 300, 50)
    OP_24(0x35D)
    EndChrThread(0x1C, 0x3)
    StopEffect(0x0, 0x0)
    Fade(500)
    SetChrPos(0x101, -28250, 8000, 190850, 180)
    SetChrPos(0x102, -29000, 8000, 191650, 180)
    SetChrPos(0x103, -26500, 8000, 191250, 180)
    SetChrPos(0x109, -26600, 8000, 192950, 180)
    SetChrPos(0x105, -27900, 8000, 193650, 180)
    OP_68(-27850, 8600, 188350, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_68(-27000, 8600, 192650, 3000)
    MoveCamera(50, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(19500, 3000)
    OP_0D()
    Sound(863, 2, 80, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011F#5PThat's amazing …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5POh, overwhelming …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#5PThat's unexpected …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#5PThat is Randy's senior\x01",
            "Real fighting ability ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWhew, thanks for your support\x01",
            "I wonder if it was not necessary …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10301F#5P─ ─ No.\x01",
            "Sounds a little unwise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#5PWhat!?\x02",
    )

    CloseMessageWindow()
    StopSound(863, 1000, 80)
    Fade(500)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    OP_68(-20000, 4600, 152050, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(-20000, 4600, 152050, 1000)
    MoveCamera(50, 30, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(14750, 1000)
    SetChrPos(0x1D, 4540, 10000, 165890, 225)
    Sound(291, 2, 100, 0)
    Sound(580, 2, 50, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    SetChrChipByIndex(0x1C, 0x47)
    BeginChrThread(0x1C, 3, 0, 51)
    OP_0D()
    OP_6F(0x79)
    StopSound(291, 700, 100)
    StopSound(580, 700, 50)
    EndChrThread(0x1C, 0x3)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x1D,
        "Daughter's voice",
        (
            "#3954V#6P#25A#30WAhaha!\x01",
            "You're great, Randy Brother!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1C, 0x1D, 500)

    ChrTalk(
        0x1C,
        "#00311F#2763V#6P#15A#30W…… Charlie?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_6B(0x1C)
    MoveCamera(40, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15750, 3000)
    ClearChrFlags(0x1C, 0x4)
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x4, 0x0, 0xFF, 0x0, -18400, 4000, 154350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1100)
    Sleep(100)
    Sound(200, 0, 80, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    SetChrChipByIndex(0x1C, 0x4B)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0xFFFFAAA6, 0x9A6, 0x245C2, 0x3E8, 0x1B58)
    SetChrSubChip(0x1C, 0x0)
    PlayEffect(0x4, 0x1, 0xFF, 0x0, -21750, 3000, 149950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1100)
    Sleep(100)
    Sound(196, 0, 80, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    OP_93(0x1C, 0x13B, 0x3E8)
    SetChrSubChip(0x1C, 0x2)
    OP_9D(0x1C, 0xFFFFB758, 0x5D2, 0x23EB0, 0x3E8, 0x1B58)
    SetChrSubChip(0x1C, 0x0)
    Sound(580, 2, 70, 0)
    Sound(291, 2, 70, 0)
    Sound(861, 2, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    PlayEffect(0x1, 0x2, 0x1C, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x1C, 0x46)
    OP_95(0x1C, -19500, 0, 137600, 7000, 0x0)
    WaitChrThread(0x1C, 1)
    SetChrFlags(0x1C, 0x4)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopSound(580, 700, 80)
    StopSound(291, 700, 60)
    OP_24(0x35D)
    OP_82(0x0, 0x0, 0xBB8, 0x0)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x1C, 0x47)
    TurnDirection(0x1C, 0x1D, 500)
    OP_6B(0xFF)
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(-16100, 7300, 151850, 0)
    MoveCamera(30, 20, -5, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(15500, 1000)
    OP_93(0x1C, 0xA, 0x0)
    SetChrPos(0x1D, -16100, 10700, 151850, 210)
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1D, 0x2B)
    SetChrSubChip(0x1D, 0x1)
    Sound(844, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFC11C, 0x1A2C, 0x2512A, 0x3E8, 0x2710)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    Sound(326, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x1D,
        (
            "#04612F#5PYes, of course\x01",
            "Randy brother needs to do so!\x02\x03",
            "#04602FIt is different from Shirley's preference\x01",
            "Cool!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-19500, 1000, 137600, 1500)
    MoveCamera(65, 20, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(16000, 1500)
    OP_6F(0x79)

    ChrTalk(
        0x1C,
        (
            "#00311F#12PStray … … little girl.\x02\x03",
            "A man eating a tiger like a temple,\x01",
            "It is my refusal … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04612F#6PHuh, you can not tie!\x02\x03",
            "#04602FBut do not worry\x01",
            "I will have some more fun!\x02",
        )
    )

    CloseMessageWindow()
    Sound(291, 2, 100, 0)
    Sound(580, 2, 70, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    SetChrChipByIndex(0x1C, 0x47)
    BeginChrThread(0x1C, 3, 0, 52)

    def lambda_78C3():

        label("loc_78C3")

        TurnDirection(0xFE, 0x1D, 300)
        Yield()
        Jump("loc_78C3")

    QueueWorkItem2(0x1C, 2, lambda_78C3)
    Sleep(1000)
    Fade(500)
    EndChrThread(0x1C, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    OP_68(-16100, 7300, 151850, 0)
    MoveCamera(60, 30, -5, 0)
    OP_6E(500, 0)
    SetCameraDistance(15700, 0)
    OP_6B(0x1D)
    MoveCamera(70, 30, -5, 3000)
    SetChrFlags(0x1D, 0x800)
    PlayEffect(0x5, 0x0, 0x1D, 0x5, 3000, 3000, -8000, 90, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x1D, 0x29)
    OP_95(0x1D, -15400, 6700, 148050, 10000, 0x0)
    OP_95(0x1D, -14000, 6700, 145400, 10000, 0x0)
    OP_82(0x0, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0x1D, 0x2B)
    SetChrSubChip(0x1D, 0x1)
    Sound(844, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFD954, 0xFA0, 0x230BE, 0x3E8, 0x2710)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    StopSound(291, 700, 80)
    StopSound(580, 700, 40)
    StopEffect(0x0, 0x2)
    OP_6B(0xFF)
    OP_68(-16980, 1100, 137980, 750)
    MoveCamera(25, 26, 0, 750)
    SetCameraDistance(18000, 750)
    SetChrFlags(0x1D, 0x2)
    SetChrSubChip(0x1D, 0xE)
    Sound(844, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFC68A, 0x0, 0x21BCE, 0x3E8, 0x1388)
    SetChrSubChip(0x1D, 0x6)
    Sleep(100)
    ClearChrFlags(0x1D, 0x2)
    Sound(326, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    TurnDirection(0x1D, 0x1C, 0)
    ClearChrFlags(0x1D, 0x800)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x1C, 0x2)
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x2A)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x32, 1, 0, 69)
    BeginChrThread(0x1D, 3, 0, 63)
    Sleep(100)
    EndChrThread(0x1D, 0x3)
    SetChrSubChip(0x1D, 0x3)
    OP_68(-18900, 1190, 137700, 500)
    SetCameraDistance(14670, 500)
    Sound(250, 0, 100, 0)
    SetChrFlags(0x1D, 0x20)
    OP_9A(0x1D, 0x1C, 0x6A4, 0x4E20, 0x0)
    ClearChrFlags(0x1D, 0x20)
    Sound(875, 2, 90, 0)
    OP_25(0x366, 0x50)
    SetChrChipByIndex(0x1D, 0x2C)
    BeginChrThread(0x1D, 2, 0, 65)
    Fade(250)
    Sound(566, 0, 80, 0)
    Sound(372, 0, 80, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0xFA)
    SetChrChipByIndex(0x1C, 0x49)
    SetChrFlags(0x1C, 0x2)
    OP_A0(0x1C, 2000, 0x0, 0x1)
    BeginChrThread(0x1C, 2, 0, 54)

    def lambda_7B1A():

        label("loc_7B1A")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_7B1A")

    QueueWorkItem2(0x1C, 3, lambda_7B1A)
    Sleep(50)

    def lambda_7B3B():

        label("loc_7B3B")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_7B3B")

    QueueWorkItem2(0x1D, 3, lambda_7B3B)
    OP_0D()

    ChrTalk(
        0x1C,
        "#00310F#6PDamn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04604F#11PHehu ……\x01",
            "But I guess it's blank, right?\x02\x03",
            "#04611FIs not it the limit soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#00307F#6P\"Tester = Rossa\" ……\x01",
            "Have you completely managed to use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04609F#11PKusu, when I was taught by Randy brother\x01",
            "It's not Charlie, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x1D,
        "#04602F#11P#10A#4SWonder if I do not care, Somewhere!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1D, 0x20)
    OP_68(-19300, 1190, 137780, 1500)

    def lambda_7CCF():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7CCF)

    def lambda_7CE4():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7CE4)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1D, 1)
    Sleep(500)
    OP_68(-19700, 1190, 137860, 1500)

    def lambda_7D15():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7D15)

    def lambda_7D2A():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7D2A)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1D, 1)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    Sound(3920, 255, 90, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x1D,
        (
            "#04612F#5S#11P#18AHaha!\x01",
            "Ichae yeah yeah yeah! It is!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1D, 0x3)
    SetChrFlags(0x1C, 0x800)
    SetChrFlags(0x1D, 0x800)
    Sound(874, 0, 100, 0)

    def lambda_7DB8():
        OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7DB8)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1D, 0x2A)
    OP_A0(0x1D, 3000, 0x0, 0x3)
    BeginChrThread(0x1D, 3, 0, 64)
    StopSound(870, 500, 80)
    StopSound(875, 500, 90)
    Sound(873, 0, 100, 0)
    OP_68(-19830, 1190, 136740, 300)
    SetCameraDistance(16000, 300)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    OP_68(-21240, 1200, 136720, 500)
    MoveCamera(63, 24, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(14000, 500)
    Sleep(100)

    def lambda_7E54():
        OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7E54)
    EndChrThread(0x1D, 0x3)
    SetChrFlags(0x1D, 0x2)
    SetChrChipByIndex(0x1D, 0x2D)
    Sound(815, 0, 100, 0)
    OP_A1(0x1D, 0xDAC, 0x2, 0x0, 0x1)
    Sound(2764, 255, 100, 1)

    ChrTalk(
        0x1C,
        "#00313F#6P#10A#NIguchi …!\x02",
    )


    def lambda_7EAB():
        OP_A0(0xFE, 2000, 0x3, 0x4)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_7EAB)

    def lambda_7EB8():
        OP_9D(0xFE, 0xFFFFA740, 0x0, 0x214BC, 0x2EE, 0x2710)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7EB8)

    def lambda_7ED5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_7ED5)
    Sound(880, 0, 80, 0)
    Sound(566, 0, 50, 0)
    ClearChrFlags(0x31, 0x80)

    def lambda_7EFF():
        OP_9D(0xFE, 0xFFFFA7B8, 0xFFFFFF38, 0x20E5E, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_7EFF)
    BeginChrThread(0x31, 3, 0, 66)
    WaitChrThread(0x1C, 1)
    Sound(811, 0, 100, 0)
    Sound(862, 0, 100, 0)
    SetChrChipByIndex(0x1C, 0x4A)
    SetChrSubChip(0x1C, 0x2)
    ClearChrFlags(0x30, 0x80)
    WaitChrThread(0x1D, 1)
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0x31, 1)
    EndChrThread(0x31, 0x3)
    SetChrSubChip(0x31, 0x1)
    Sound(288, 0, 70, 0)
    OP_6F(0x79)
    ClearChrFlags(0x1D, 0x20)
    ClearChrFlags(0x1C, 0x20)
    Sleep(1000)
    Fade(250)
    SetCameraDistance(13500, 2000)
    OP_A1(0x1D, 0xDAC, 0x2, 0x2, 0x3)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x1D,
        (
            "#04606F#11PWell, it's about Randy's older brother right now.\x01",
            "I still can not be satisfied.\x02\x03",
            "#04611FWell someday.\x01",
            "Your best playing partner\x01",
            "I have found it properly and sprayed\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x1C, 0x3)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x1C,
        "#00311F#6P#NTake care …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1D,
        (
            "#04604F#11PHehe, Randy elder brother\x01",
            "For a while at the dad\x01",
            "You should rehabilitate.\x02\x03",
            "#04602FAs soon as you regain the can\x01",
            "Because I will take over the seat of \"fighting spirit\".\x02\x03",
            "#04609FBut well this time\x01",
            "Let's get a single arm?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x2)
    SetChrChipByIndex(0x1D, 0x2A)
    SetChrSubChip(0x1D, 0x0)
    Sound(358, 0, 100, 0)
    Sleep(50)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x1D, 3, 0, 63)
    BeginChrThread(0x32, 1, 0, 69)
    Sleep(500)

    ChrTalk(
        0x1C,
        "#00310F#6P#NDamn\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        "#3320V#4S#10ARandy ─ ─ ─ ─! It is!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    StopSound(870, 500, 100)
    Sound(873, 0, 100, 0)
    EndChrThread(0x1D, 0x3)
    Sound(530, 0, 100, 0)
    PlayEffect(0xA, 0xFF, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1D, 0x2B)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFBB40, 0x0, 0x21B10, 0x1F4, 0xFA0)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    OP_93(0x1D, 0x168, 0x0)
    Sound(530, 0, 100, 0)
    PlayEffect(0xA, 0xFF, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFBDCA, 0x0, 0x2146C, 0x1F4, 0xFA0)
    SetChrSubChip(0x1D, 0x0)
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0x1D, 0x28)

    ChrTalk(
        0x1D,
        "#04605F#12POops.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#00305F#12P#N……! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    ClearChrFlags(0x1C, 0x800)
    ClearChrFlags(0x1D, 0x800)
    OP_68(-21250, 8600, 172900, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(18000, 3000)
    SetChrChipByIndex(0x101, 0x37)
    SetChrChipByIndex(0x102, 0x3E)
    SetChrChipByIndex(0x103, 0x43)
    SetChrChipByIndex(0x109, 0x50)
    SetChrPos(0x101, -21400, 7650, 170850, 180)
    SetChrPos(0x102, -22000, 8000, 172800, 180)
    SetChrPos(0x103, -20300, 8000, 173230, 180)
    SetChrPos(0x109, -20850, 7850, 171700, 180)
    BeginChrThread(0x102, 3, 0, 67)
    BeginChrThread(0x103, 3, 0, 68)
    Sleep(100)

    def lambda_838E():
        OP_9B(0x1, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_838E)
    Sleep(50)

    def lambda_83A6():
        OP_9B(0x1, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_83A6)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x103, 3)
    EndChrThread(0x102, 0x3)
    Fade(500)
    OP_68(-16950, 600, 136300, 0)
    MoveCamera(30, 28, 0, 0)
    SetCameraDistance(17000, 0)
    OP_6B(0x1D)
    SetCameraDistance(16000, 2000)
    MoveCamera(70, 30, 0, 2000)
    OP_0D()
    OP_93(0x1D, 0x13B, 0x320)
    Sound(530, 0, 100, 0)
    PlayEffect(0xA, 0xFF, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x1D, 0x2B)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFC3D8, 0x0, 0x20DC8, 0x1F4, 0x1770)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x2D, 0x320)
    Sound(530, 0, 100, 0)
    PlayEffect(0xA, 0xFF, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x1D, 0x1)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFCA4A, 0x0, 0x212AA, 0x1F4, 0x1770)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x13B, 0x320)
    Sound(530, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFD21A, 0x0, 0x20F8A, 0x1F4, 0x1770)
    OP_93(0x1D, 0x12C, 0x320)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x1D, 0x28)
    OP_6F(0x79)

    ChrTalk(
        0x1D,
        (
            "#04612F#11PHaha, I will do it!\x02\x03",
            "#04602FWell then\x01",
            "Even cranking up - ─\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x1, 0x0, 0x1D, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(865, 2, 30, 0)
    Sound(861, 2, 60, 0)
    Sound(539, 0, 100, 0)
    Sleep(420)
    Sound(539, 0, 100, 0)
    Sleep(420)
    Sound(539, 0, 100, 0)
    Sleep(160)
    StopEffect(0x0, 0x2)
    StopSound(861, 500, 60)
    StopSound(865, 500, 40)
    Fade(500)
    SetChrPos(0x101, -19400, 0, 142000, 120)
    SetChrPos(0x109, -17400, 0, 141450, 135)
    SetChrPos(0x105, -8700, 0, 133000, 295)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x109, 0x52)
    SetChrSubChip(0x109, 0x4)
    OP_6B(0xFF)
    OP_68(-19400, 1600, 142000, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(-12200, 1000, 135050, 1500)
    MoveCamera(70, 30, -5, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(15000, 1500)

    def lambda_86EC():
        OP_95(0xFE, -16000, 0, 138600, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86EC)
    OP_0D()
    Sound(2014, 255, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x101,
        "#00007F#4S#10A#5POoooooooooooooooooooo!\x02",
    )

    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x39)
    SetChrSubChip(0x101, 0x4)
    Sound(251, 0, 100, 0)

    def lambda_875C():
        OP_9D(0xFE, 0xFFFFCE96, 0x0, 0x21214, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_875C)
    WaitChrThread(0x101, 1)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x1D, 0x2C)
    SetChrSubChip(0x1D, 0x0)
    PlayEffect(0x9, 0xFF, 0x101, 0x3, -300, 800, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(566, 0, 70, 0)
    Sound(815, 0, 100, 0)
    Sound(862, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    def lambda_87E3():

        label("loc_87E3")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_87E3")

    QueueWorkItem2(0x101, 3, lambda_87E3)
    Sleep(50)

    def lambda_8804():

        label("loc_8804")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_8804")

    QueueWorkItem2(0x1D, 3, lambda_8804)
    Sleep(500)
    Sleep(1000)

    ChrTalk(
        0x1C,
        "#00307F#5PLloyd …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04604F#11PCut …… Haha!\x02\x03",
            "#04602FOlder brother, regardless of appearance\x01",
            "Are you going to have a bad start?\x02\x03",
            "To a girl like Charlie\x01",
            "It's an enormous collaboration attack!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#6PIt is not an opponent you can count on\x01",
            "I saw it by seeing it … …\x02\x03",
            "#00007FTo you, to the ordering monster of danger S\x01",
            "Have them hit by dealing with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#04609F#11PHaha, that's correct!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 2, 0, 55)
    BeginChrThread(0x1D, 2, 0, 65)
    BeginChrThread(0x32, 1, 0, 70)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)

    ChrTalk(
        0x1C,
        (
            "#00310F#5PWell … not useless, get away!\x02\x03",
            "No matter how much your toffee is\x01",
            "There is a reason to be defended - ─\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x105,
        "voice",
        "#11P#NWell, that's right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    OP_68(-8700, 600, 133000, 400)
    MoveCamera(85, 30, -10, 400)
    SetCameraDistance(15000, 400)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x1D, 0x3)
    EndChrThread(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x37)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_6F(0x79)
    SetChrChip(0x0, 0x105, 0x1E, 0xC8)
    OP_99(0x105, 0x1D, 0x5DC, 0x4E20, 0x0)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x105, 0x1000)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x57)
    SetChrSubChip(0x105, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(500)
    PlayEffect(0xF, 0x0, 0x105, 0x3, 0, 500, -400, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(253, 0, 100, 0)

    def lambda_8B37():
        OP_96(0xFE, 0xFFFFD21A, 0xFFFFFE70, 0x20F8A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8B37)
    Sound(3091, 255, 100, 0)
    OP_68(-11000, 900, 135050, 500)
    MoveCamera(68, 25, 5, 500)
    OP_6E(500, 500)
    SetCameraDistance(18250, 500)
    Sound(873, 0, 100, 0)
    StopSound(870, 500, 100)
    StopSound(875, 500, 100)
    EndChrThread(0x1D, 0x2)
    SetChrFlags(0x1D, 0x20)
    SetChrChipByIndex(0x1D, 0x2B)
    SetChrSubChip(0x1D, 0x0)
    OP_93(0x1D, 0x13B, 0x0)
    OP_96(0x1D, 0xFFFFDDA0, 0x0, 0x20D96, 0x2710, 0x0)

    def lambda_8BC3():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_8BC3)
    ClearChrFlags(0x1D, 0x20)
    OP_6F(0x79)
    StopEffect(0x0, 0x2)
    SetChrChip(0x1, 0x105, 0x0, 0x0)

    ChrTalk(
        0x1D,
        "#04605F#11P#6AWow! Is it?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x1000)
    SetChrPos(0x105, -11750, 0, 135050, 295)

    def lambda_8C39():

        label("loc_8C39")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_8C39")

    QueueWorkItem2(0x105, 3, lambda_8C39)
    OP_68(-8600, 1000, 135100, 1000)
    MoveCamera(50, 25, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(18700, 1000)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFE34A, 0x0, 0x20882, 0x1F4, 0x1B58)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    SetChrSubChip(0x1D, 0x2)
    Sound(250, 0, 100, 0)
    OP_9D(0x1D, 0xFFFFEB24, 0x0, 0x20CCE, 0x1F4, 0x1B58)
    SetChrSubChip(0x1D, 0x0)
    TurnDirection(0x1D, 0x101, 1000)
    SetChrChipByIndex(0x1D, 0x28)
    EndChrThread(0x105, 0x3)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10306F#6P… …. Good luck.\x01",
            "Can not you move down now?\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x15, 0x33)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x20)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x20)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x15, 10600, 0, 135200, 275)
    SetChrPos(0x16, 10100, 0, 132750, 275)
    SetChrPos(0x21, 13100, 0, 133700, 275)

    ChrTalk(
        0x15,
        "Captain!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Mr. Charlie!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, -7850, 0, 136800, 270)
    SetChrPos(0x15, 4350, 0, 137800, 270)
    SetChrPos(0x16, 3850, 0, 135800, 270)
    SetChrPos(0x21, 6350, 0, 136800, 270)
    SetChrPos(0x101, -14350, 0, 136800, 90)
    SetChrPos(0x105, -13050, 0, 138200, 270)
    OP_68(0, 600, 136800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(-6950, 600, 136800, 2000)
    MoveCamera(45, 30, 5, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(16000, 2000)

    def lambda_8E6E():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8E6E)
    Sleep(50)

    def lambda_8E86():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8E86)
    Sleep(50)

    def lambda_8E9E():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8E9E)
    BeginChrThread(0x21, 3, 0, 56)
    BeginChrThread(0x32, 1, 0, 71)
    OP_0D()
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x1)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x1)
    WaitChrThread(0x21, 1)
    EndChrThread(0x21, 0x3)
    EndChrThread(0x32, 0x1)
    SetChrChipByIndex(0x21, 0x1E)
    SetChrSubChip(0x21, 0x0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-19050, 600, 137050, 0)
    MoveCamera(90, 22, -5, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(17000, 1500)
    SetChrChipByIndex(0x101, 0x37)
    SetChrChipByIndex(0x102, 0x3C)
    SetChrChipByIndex(0x103, 0x41)
    SetChrChipByIndex(0x109, 0x50)
    SetChrChipByIndex(0x105, 0x55)
    SetChrPos(0x102, -17850, 0, 141950, 180)
    SetChrPos(0x103, -18750, 0, 143300, 178)
    SetChrPos(0x109, -17000, 0, 140850, 180)

    def lambda_8F7A():
        OP_95(0xFE, -15250, 0, 138150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8F7A)

    def lambda_8F94():
        OP_95(0xFE, -15200, 0, 135450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8F94)

    def lambda_8FAE():
        OP_95(0xFE, -16800, 0, 136150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8FAE)

    def lambda_8FC8():
        OP_95(0xFE, -16700, 0, 137700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8FC8)
    WaitChrThread(0x105, 1)

    def lambda_8FE6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8FE6)
    WaitChrThread(0x109, 1)
    Sound(531, 0, 100, 0)

    def lambda_8FFD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8FFD)
    WaitChrThread(0x102, 1)

    def lambda_900E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_900E)
    WaitChrThread(0x103, 1)
    Sound(805, 0, 100, 0)

    def lambda_9025():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9025)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x1C,
        "#00306F#6P#NYou guys……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_68(-12400, 1150, 136830, 2000)
    MoveCamera(87, 10, -5, 2000)
    OP_6E(450, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1D,
        (
            "#04604F#3955V#11P#40WHuh, you okay.\x02\x03",
            "#3956VIf you want to play with Charlie so much\x01",
            "I will give you some opportunities … …\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF74)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7455", 0)

    AnonymousTalk(
        0x1D,
        (
            "#3933V#40WAhahahaha-ha#1200W,#40WA little#1000WIs\x01",
            "#4S#30WI am entertaining! Is it?\x02",
        )
    )

    Sleep(2800)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    OP_24(0xF5D)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(10, 50, -1, -1)

    AnonymousTalk(
        0x101,
        "#00007FI will come!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 150, -1, -1)

    AnonymousTalk(
        0x109,
        "#10107FI will intercept with full power!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    def lambda_9257():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9257)

    def lambda_926C():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_926C)

    def lambda_9281():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9281)

    def lambda_9296():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9296)

    def lambda_92AB():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_92AB)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrChipByIndex(0x15, 0x33)
    SetChrChipByIndex(0x16, 0x33)
    SetChrChipByIndex(0x21, 0x1F)

    def lambda_92D0():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_92D0)

    def lambda_92E5():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_92E5)

    def lambda_92FA():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_92FA)

    def lambda_930F():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_930F)
    BeginChrThread(0x21, 3, 0, 56)
    OP_24(0x244)
    OP_24(0x123)
    OP_24(0x361)
    OP_24(0x35D)
    OP_24(0x366)
    OP_24(0x36B)
    OP_24(0x35F)
    SetCameraDistance(17000, 150)
    Sleep(150)
    Battle("BattleInfo_ED0", 0x0, 0x0, 0x100, 0x3D, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x21, 0x3)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    AddParty(0x3, 0xFF, 0xFF)
    ClearMapFlags(0x10000000)
    Call(0, 72)
    Return()

    # Function_40_57E1 end

    def Function_41_93C6(): pass

    label("Function_41_93C6")

    SetChrChipByIndex(0x15, 0x33)
    OP_95(0x15, -50, 0, 133650, 6000, 0x0)
    OP_93(0x15, 0x0, 0x1F4)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x1)
    Return()

    # Function_41_93C6 end

    def Function_42_93EE(): pass

    label("Function_42_93EE")

    SetChrChipByIndex(0x15, 0x33)
    OP_95(0x15, -18850, 0, 137000, 6000, 0x0)
    OP_93(0x15, 0x0, 0x1F4)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x1)
    Return()

    # Function_42_93EE end

    def Function_43_9416(): pass

    label("Function_43_9416")

    SetChrChipByIndex(0x16, 0x33)
    OP_95(0x16, -2050, 0, 137900, 6000, 0x0)
    OP_93(0x16, 0x0, 0x1F4)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x1)
    Return()

    # Function_43_9416 end

    def Function_44_943E(): pass

    label("Function_44_943E")

    SetChrChipByIndex(0x17, 0x33)
    OP_95(0x17, -4500, 0, 131150, 6000, 0x0)
    OP_93(0x17, 0x0, 0x1F4)
    SetChrChipByIndex(0x17, 0x34)
    SetChrSubChip(0x17, 0x1)
    Return()

    # Function_44_943E end

    def Function_45_9466(): pass

    label("Function_45_9466")

    SetChrChipByIndex(0x17, 0x33)
    OP_95(0x17, -17500, 0, 139450, 6000, 0x0)
    OP_93(0x17, 0x0, 0x1F4)
    SetChrChipByIndex(0x17, 0x34)
    SetChrSubChip(0x17, 0x1)
    Return()

    # Function_45_9466 end

    def Function_46_948E(): pass

    label("Function_46_948E")

    SetChrChipByIndex(0x18, 0x33)
    OP_95(0x18, -3950, 0, 136900, 6000, 0x0)
    OP_95(0x18, -5300, 0, 137700, 6000, 0x0)
    OP_93(0x18, 0x0, 0x1F4)
    SetChrChipByIndex(0x18, 0x34)
    SetChrSubChip(0x18, 0x1)
    Return()

    # Function_46_948E end

    def Function_47_94CA(): pass

    label("Function_47_94CA")

    SetChrChipByIndex(0x19, 0x33)
    OP_95(0x19, -4500, 0, 131150, 6000, 0x0)
    OP_95(0x19, -7550, 0, 133100, 6000, 0x0)
    OP_93(0x19, 0x0, 0x1F4)
    SetChrChipByIndex(0x19, 0x34)
    SetChrSubChip(0x19, 0x1)
    Return()

    # Function_47_94CA end

    def Function_48_9506(): pass

    label("Function_48_9506")

    SetChrChipByIndex(0x19, 0x33)
    OP_95(0x19, -20150, 0, 140400, 6000, 0x0)
    OP_93(0x19, 0x0, 0x1F4)
    SetChrChipByIndex(0x19, 0x34)
    SetChrSubChip(0x19, 0x1)
    Return()

    # Function_48_9506 end

    def Function_49_952E(): pass

    label("Function_49_952E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9561")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9555")
    OP_4C(0xFE, 0x3)
    Jump("loc_9559")

    label("loc_9555")

    OP_4B(0xFE, 0x3)

    label("loc_9559")

    Sleep(500)
    Jump("Function_49_952E")

    label("loc_9561")

    Return()

    # Function_49_952E end

    def Function_50_9562(): pass

    label("Function_50_9562")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_95B1")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_50_9562")

    label("loc_95B1")

    Return()

    # Function_50_9562 end

    def Function_51_95B2(): pass

    label("Function_51_95B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9601")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_51_95B2")

    label("loc_9601")

    Return()

    # Function_51_95B2 end

    def Function_52_9602(): pass

    label("Function_52_9602")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9651")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, -150, 1250, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_52_9602")

    label("loc_9651")

    Return()

    # Function_52_9602 end

    def Function_53_9652(): pass

    label("Function_53_9652")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96AC")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 0, 1100, 2600, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x14, 0x32, 0xBB8)
    Jump("Function_53_9652")

    label("loc_96AC")

    Return()

    # Function_53_9652 end

    def Function_54_96AD(): pass

    label("Function_54_96AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96F7")
    PlayEffect(0x9, 0xFF, 0xFE, 0x3, -200, 1550, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_54_96AD")

    label("loc_96F7")

    Return()

    # Function_54_96AD end

    def Function_55_96F8(): pass

    label("Function_55_96F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9753")
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x9, 0xFF, 0xFE, 0x3, -300, 800, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_55_96F8")

    label("loc_9753")

    Return()

    # Function_55_96F8 end

    def Function_56_9754(): pass

    label("Function_56_9754")

    SetChrChipByIndex(0xFE, 0x1F)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_976E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9785")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_976E")

    label("loc_9785")

    Return()

    # Function_56_9754 end

    def Function_57_9786(): pass

    label("Function_57_9786")

    SetChrChipByIndex(0xFE, 0x1E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_97B7")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_97A0")

    label("loc_97B7")

    Return()

    # Function_57_9786 end

    def Function_58_97B8(): pass

    label("Function_58_97B8")

    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x5)
    Sound(809, 0, 100, 0)
    OP_9D(0x21, 0x3B60, 0x1770, 0x23410, 0x3E8, 0x1770)
    BeginChrThread(0x21, 0, 0, 56)
    OP_95(0x21, 12700, 6000, 144400, 6000, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrSubChip(0x21, 0x5)

    def lambda_9804():
        OP_9D(0xFE, 0x265C, 0x1770, 0x233DE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_9804)
    Return()

    # Function_58_97B8 end

    def Function_59_981D(): pass

    label("Function_59_981D")

    Sleep(100)
    SetChrChipByIndex(0x22, 0x1F)
    BeginChrThread(0x22, 0, 0, 56)
    OP_95(0x22, -320, 4000, 149170, 6000, 0x0)
    OP_95(0x22, 5060, 6000, 148610, 6000, 0x0)
    EndChrThread(0x22, 0x0)
    TurnDirection(0x22, 0x1C, 500)
    SetChrSubChip(0x22, 0x5)

    def lambda_9866():
        OP_9D(0xFE, 0x21FC, 0x1770, 0x23F32, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9866)
    Return()

    # Function_59_981D end

    def Function_60_987F(): pass

    label("Function_60_987F")

    Sleep(1600)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x5)
    Sound(809, 0, 100, 0)
    OP_9D(0x23, 0x238C, 0x1770, 0x24784, 0x3E8, 0x1770)
    TurnDirection(0x23, 0x1C, 500)

    def lambda_98B3():
        OP_9D(0xFE, 0x2D82, 0x186A, 0x241F8, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_98B3)
    Return()

    # Function_60_987F end

    def Function_61_98CC(): pass

    label("Function_61_98CC")

    Sleep(2000)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x5)
    Sound(809, 0, 100, 0)
    OP_9D(0x24, 0x285A, 0x1770, 0x24572, 0x3E8, 0x1770)
    TurnDirection(0x24, 0x1C, 500)
    SetChrSubChip(0x24, 0x5)

    def lambda_9904():
        OP_9D(0xFE, 0x30A2, 0x1770, 0x23988, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9904)
    Return()

    # Function_61_98CC end

    def Function_62_991D(): pass

    label("Function_62_991D")

    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 60, 0)

    def lambda_9968():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9968)

    def lambda_9981():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9981)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE70, 0x7D0, 0x0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sound(514, 0, 75, 0)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_62_991D end

    def Function_63_99BB(): pass

    label("Function_63_99BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99D3")
    OP_A1(0xFE, 0xDAC, 0x2, 0x1, 0x2)
    Jump("Function_63_99BB")

    label("loc_99D3")

    Return()

    # Function_63_99BB end

    def Function_64_99D4(): pass

    label("Function_64_99D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99EC")
    OP_A1(0xFE, 0xDAC, 0x2, 0x4, 0x5)
    Jump("Function_64_99D4")

    label("loc_99EC")

    Return()

    # Function_64_99D4 end

    def Function_65_99ED(): pass

    label("Function_65_99ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A05")
    OP_A1(0xFE, 0xDAC, 0x2, 0x0, 0x1)
    Jump("Function_65_99ED")

    label("loc_9A05")

    Return()

    # Function_65_99ED end

    def Function_66_9A06(): pass

    label("Function_66_9A06")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A1D")
    OP_A0(0xFE, 5000, 0x1, 0x6)
    Jump("Function_66_9A06")

    label("loc_9A1D")

    Return()

    # Function_66_9A06 end

    def Function_67_9A1E(): pass

    label("Function_67_9A1E")

    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_9A26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A88")
    SetChrSubChip(0xFE, 0x2)
    Sleep(850)
    SetChrSubChip(0xFE, 0x3)
    Sound(530, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x5, 0, 1200, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(80)
    SetChrSubChip(0xFE, 0x4)
    Sleep(80)
    Jump("loc_9A26")

    label("loc_9A88")

    Return()

    # Function_67_9A1E end

    def Function_68_9A89(): pass

    label("Function_68_9A89")

    SetChrSubChip(0xFE, 0x0)
    Sound(357, 0, 100, 0)
    PlayEffect(0x6, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    Sound(280, 0, 80, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_68_9A89 end

    def Function_69_9B32(): pass

    label("Function_69_9B32")

    Sound(872, 0, 100, 0)
    Sleep(400)
    Sound(870, 2, 100, 0)
    Return()

    # Function_69_9B32 end

    def Function_70_9B42(): pass

    label("Function_70_9B42")

    Sound(872, 0, 100, 0)
    Sleep(400)
    Sound(870, 2, 100, 0)
    Sound(875, 2, 100, 0)
    Return()

    # Function_70_9B42 end

    def Function_71_9B58(): pass

    label("Function_71_9B58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B71")
    Sound(845, 0, 100, 0)
    Sleep(400)
    Jump("Function_71_9B58")

    label("loc_9B71")

    Return()

    # Function_71_9B58 end

    def Function_72_9B72(): pass

    label("Function_72_9B72")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x37)
    LoadChrToIndex("chr/ch00150.itc", 0x3C)
    LoadChrToIndex("chr/ch00250.itc", 0x41)
    LoadChrToIndex("apl/ch51439.itc", 0x47)
    LoadChrToIndex("chr/ch02950.itc", 0x50)
    LoadChrToIndex("chr/ch03050.itc", 0x55)
    LoadChrToIndex("chr/ch32650.itc", 0x1E)
    LoadChrToIndex("chr/ch32651.itc", 0x1F)
    LoadChrToIndex("chr/ch32654.itc", 0x21)
    LoadChrToIndex("chr/ch31251.itc", 0x23)
    LoadChrToIndex("chr/ch31252.itc", 0x24)
    LoadChrToIndex("chr/ch03450.itc", 0x28)
    LoadChrToIndex("chr/ch03451.itc", 0x29)
    LoadChrToIndex("chr/ch0345F.itc", 0x2A)
    LoadChrToIndex("chr/ch41951.itc", 0x32)
    LoadChrToIndex("chr/ch41952.itc", 0x33)
    LoadChrToIndex("chr/ch41953.itc", 0x34)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis266.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis267.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis268.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    LoadEffect(0x0, "battle/sp003000.eff")
    LoadEffect(0x1, "event/ev12002.eff")
    LoadEffect(0x3, "battle/btgun00.eff")
    SoundLoad(860)
    SoundLoad(861)
    SoundLoad(865)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x2)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x2)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x3)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x20)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x3)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x33)
    SetChrSubChip(0x17, 0x2)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x2)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x33)
    SetChrSubChip(0x19, 0x2)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x33)
    SetChrSubChip(0x1A, 0x2)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x101, 0x37)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x3C)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x41)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x47)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x50)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0x28)
    SetMapObjFlags(0x5, 0x1000)
    OP_F3(100000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E23")
    OP_2C(0xAA, 0x1)

    label("loc_9E23")

    SetChrPos(0x101, -25100, 0, 133850, 215)
    SetChrPos(0x102, -23800, 0, 136100, 215)
    SetChrPos(0x103, -22350, 0, 135550, 215)
    SetChrPos(0x109, -23050, 0, 134100, 215)
    SetChrPos(0x105, -25200, 0, 135200, 215)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x104, -20800, 0, 138300, 215)
    SetChrPos(0x1D, -27600, 0, 129250, 45)
    SetChrPos(0x15, -29400, 0, 127550, 45)
    SetChrPos(0x16, -27750, 0, 127050, 45)
    OP_68(-26000, 1200, 132500, 0)
    MoveCamera(75, 20, 3, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00010F#5PCut, Haha … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10310F#5PThis is the strongest class\x01",
            "Whether the skill of hunting corps … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PDamn\x01",
            "To be defeated by the skill!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04606F#12PWell, not bad, but\x01",
            "Is it such a place?\x02\x03",
            "#04611FBefore a special treat\x01",
            "What are the most desserts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PHuh……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x131, 0x1F4)

    ChrTalk(
        0x103,
        "#00202F#11PAh……!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0x1F4)
    Sound(860, 2, 80, 0)
    Sound(861, 2, 50, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    StopSound(860, 1000, 70)
    StopSound(861, 1000, 40)
    Sleep(500)
    Fade(500)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x1E, -26100, 8000, 175800, 180)
    SetChrPos(0xD, -27300, 8000, 176550, 180)
    SetChrPos(0xE, -25250, 8000, 174750, 180)
    SetChrPos(0xF, -25240, 8000, 180620, 182)
    SetChrPos(0x10, -27270, 8000, 183470, 137)
    SetChrPos(0x11, -27530, 8000, 187170, 182)
    SetChrPos(0x12, -27170, 8000, 190850, 225)
    SetChrPos(0x13, -25790, 8000, 194970, 225)
    SetChrPos(0x14, -22670, 8000, 198030, 225)
    OP_68(-28100, 10150, 182100, 0)
    MoveCamera(30, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21450, 0)
    OP_68(-26100, 8600, 175800, 7000)
    MoveCamera(45, 25, 0, 7000)
    SetCameraDistance(20000, 7000)
    PlayEffect(0x1, 0x0, 0xD, 0x3, 100, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xE, 0x3, 100, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xF, 1, 0, 78)
    BeginChrThread(0x10, 1, 0, 80)
    BeginChrThread(0x11, 1, 0, 82)
    BeginChrThread(0x12, 1, 0, 84)
    BeginChrThread(0x13, 1, 0, 86)
    BeginChrThread(0x14, 1, 0, 87)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0x1E, -17250, 6300, 165100, 180)
    SetChrPos(0xD, -18000, 6650, 166580, 180)
    SetChrPos(0xE, -16050, 6880, 167530, 180)
    OP_68(-18150, 6000, 161050, 0)
    MoveCamera(15, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_68(-20000, 4900, 152450, 3000)
    MoveCamera(15, 25, -5, 3000)
    SetCameraDistance(20000, 3000)
    BeginChrThread(0x1E, 1, 0, 73)
    BeginChrThread(0xD, 1, 0, 74)
    BeginChrThread(0xE, 1, 0, 76)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x1E, 1)

    ChrTalk(
        0x101,
        "#00002F#6P#NThree Lieutenant Mireille … …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10109F#12P#NYou came, …?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#07904F#5PYeah, from your manager\x01",
            "There is a message to the commander.\x02\x03",
            "#07907F── Confirm enemy troops!\x01",
            "Begin sweeping fight from this!\x02\x03",
            "However, with Mainz recapture\x01",
            "Make it the top priority for ensuring safety!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("Security guards")

    AnonymousTalk(
        0xFF,
        "#4SJesus Mum!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_82(0x0, 0x64, 0xBB8, 0x2710)
    Sound(860, 2, 80, 0)
    Sound(861, 2, 50, 0)
    BeginChrThread(0xD, 0, 0, 49)
    BeginChrThread(0xD, 3, 0, 88)
    BeginChrThread(0xE, 0, 0, 49)
    BeginChrThread(0xE, 3, 0, 88)
    BeginChrThread(0x13, 0, 0, 49)
    BeginChrThread(0x13, 3, 0, 88)
    BeginChrThread(0x14, 0, 0, 49)
    BeginChrThread(0x14, 3, 0, 88)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x10, 0x23)

    def lambda_A53E():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A53E)
    Sleep(50)
    SetChrChipByIndex(0xF, 0x23)

    def lambda_A55A():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A55A)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x23)

    def lambda_A576():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A576)
    Sleep(300)
    SetChrChipByIndex(0x12, 0x23)

    def lambda_A592():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A592)
    Sleep(1000)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    OP_25(0x35C, 0x32)
    OP_25(0x35D, 0x3C)
    Fade(500)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x3)
    SetChrChipByIndex(0xD, 0x23)
    SetChrChipByIndex(0xE, 0x23)
    SetChrPos(0x101, -23100, 0, 133850, 215)
    SetChrPos(0x102, -21800, 0, 136100, 215)
    SetChrPos(0x103, -20250, 0, 135550, 215)
    SetChrPos(0x109, -21050, 0, 134100, 215)
    SetChrPos(0x105, -23200, 0, 135200, 215)
    SetChrSubChip(0x104, 0x26)
    SetChrPos(0x15, -29350, 0, 128850, 45)
    SetChrPos(0x16, -27650, 0, 127400, 45)
    SetChrPos(0xD, -18850, 0, 142850, 225)
    SetChrPos(0xE, -18850, 0, 142850, 225)
    SetChrPos(0xF, -18850, 0, 142850, 225)
    SetChrPos(0x10, -14750, 0, 138850, 225)
    SetChrPos(0x11, -13750, 0, 139150, 225)
    SetChrPos(0x12, -14750, 0, 138850, 225)
    SetChrChipByIndex(0x15, 0x33)
    SetChrChipByIndex(0x16, 0x33)
    Sound(865, 2, 60, 0)
    BeginChrThread(0x15, 0, 0, 49)
    BeginChrThread(0x15, 3, 0, 50)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x16, 3, 0, 50)
    OP_68(-26250, 1000, 130699, 0)
    MoveCamera(45, 30, -2, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(21500, 1000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -29900, 0, 126800, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 1, 0, 96)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    Sleep(300)
    SetChrChipByIndex(0x15, 0x32)
    OP_93(0x15, 0xE1, 0x2EE)

    def lambda_A797():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A797)
    StopSound(865, 300, 50)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    Sleep(300)
    SetChrChipByIndex(0x16, 0x32)
    OP_93(0x16, 0xE1, 0x2EE)

    def lambda_A7C8():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A7C8)

    ChrTalk(
        0x1D,
        (
            "#04612F#6PHuh, and see you then!\x02\x03",
            "#04602FAlso soon\x01",
            "I feel like I can meet you!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1D, 0x29)
    OP_93(0x1D, 0xE1, 0x2EE)

    def lambda_A844():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A844)
    OP_68(-29200, 1000, 127750, 5000)

    def lambda_A86A():
        OP_9B(0x0, 0xFE, 0xFFFD, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A86A)
    Sleep(50)

    def lambda_A882():
        OP_9B(0x0, 0xFE, 0x3, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A882)
    Sleep(300)

    def lambda_A89A():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A89A)
    Sleep(50)

    def lambda_A8B2():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A8B2)
    Sleep(300)

    def lambda_A8CA():
        OP_9B(0x0, 0xFE, 0xFFFA, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A8CA)
    Sleep(50)

    def lambda_A8E2():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A8E2)
    Sleep(1000)
    WaitChrThread(0x1D, 1)
    Fade(500)
    BeginChrThread(0x101, 1, 0, 97)
    StopEffect(0x0, 0x0)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1D, -32049, -1000, 105900, 180)
    SetChrPos(0x15, -33400, -1000, 103250, 0)
    SetChrPos(0x16, -30900, -1000, 103850, 0)
    SetChrPos(0x17, -32500, -1000, 100400, 0)
    SetChrPos(0x18, -31150, -770, 98800, 0)
    SetChrPos(0x19, -30900, 0, 90450, 0)
    SetChrPos(0x1A, -34100, 0, 91050, 0)
    SetChrPos(0xD, -32750, -870, 112700, 180)
    SetChrPos(0xE, -31350, -980, 112150, 180)
    SetChrPos(0xF, -30000, -560, 114350, 180)
    SetChrPos(0x10, -33850, -600, 114150, 180)
    SetChrPos(0x11, -33050, -310, 115700, 180)
    SetChrPos(0x12, -30500, -290, 115800, 180)
    BeginChrThread(0xD, 1, 0, 75)
    BeginChrThread(0xE, 1, 0, 77)
    BeginChrThread(0xF, 1, 0, 79)
    BeginChrThread(0x10, 1, 0, 81)
    BeginChrThread(0x11, 1, 0, 83)
    BeginChrThread(0x12, 1, 0, 85)
    BeginChrThread(0x1D, 1, 0, 89)
    BeginChrThread(0x15, 1, 0, 90)
    BeginChrThread(0x16, 1, 0, 91)
    BeginChrThread(0x17, 1, 0, 92)
    BeginChrThread(0x18, 1, 0, 93)
    BeginChrThread(0x19, 1, 0, 94)
    BeginChrThread(0x1A, 1, 0, 95)
    OP_68(-32159, -400, 105000, 0)
    MoveCamera(35, 25, 5, 0)
    OP_6E(500, 0)
    SetCameraDistance(25600, 0)
    OP_68(-35290, 600, 84430, 7000)
    MoveCamera(45, 25, 10, 7000)
    OP_6F(0x79)
    WaitChrThread(0x1D, 1)
    Sleep(1500)
    StopSound(860, 1000, 40)
    StopSound(861, 1000, 50)
    Fade(500)
    EndChrThread(0x101, 0x1)
    OP_82(0xA, 0xA, 0xBB8, 0x0)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x10, 0x3)
    EndChrThread(0x11, 0x0)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x12, 0x3)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1A, 0x1)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x104, 0x2)
    SetChrPos(0x101, -19900, 0, 137400, 270)
    SetChrPos(0x102, -18800, 0, 135450, 335)
    SetChrPos(0x103, -17850, 0, 136550, 270)
    SetChrPos(0x109, -19750, 0, 135350, 270)
    SetChrPos(0x105, -18200, 0, 138000, 270)
    SetChrPos(0x1E, -20000, 0, 143700, 225)
    SetChrPos(0xD, -22200, 0, 141350, 225)
    SetChrPos(0xE, -21750, 0, 139600, 225)
    SetChrChipByIndex(0xD, 0x23)
    SetChrChipByIndex(0xE, 0x23)

    def lambda_AC43():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_AC43)

    def lambda_AC58():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_AC58)
    SetChrChipByIndex(0x1E, 0x1F)

    def lambda_AC71():
        OP_95(0xFE, -22150, 0, 139350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_AC71)
    OP_68(-20950, 1200, 137200, 0)
    MoveCamera(13, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(20000, 2000)
    WaitChrThread(0x1E, 1)

    def lambda_ACC6():

        label("loc_ACC6")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_ACC6")

    QueueWorkItem2(0x101, 2, lambda_ACC6)

    def lambda_ACD8():

        label("loc_ACD8")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_ACD8")

    QueueWorkItem2(0x104, 2, lambda_ACD8)

    def lambda_ACEA():
        TurnDirection(0x1E, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_ACEA)
    Sleep(50)

    def lambda_ACFA():

        label("loc_ACFA")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_ACFA")

    QueueWorkItem2(0x102, 2, lambda_ACFA)

    def lambda_AD0C():

        label("loc_AD0C")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_AD0C")

    QueueWorkItem2(0x103, 2, lambda_AD0C)
    Sleep(50)

    def lambda_AD21():

        label("loc_AD21")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_AD21")

    QueueWorkItem2(0x109, 2, lambda_AD21)

    def lambda_AD33():

        label("loc_AD33")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_AD33")

    QueueWorkItem2(0x105, 2, lambda_AD33)
    WaitChrThread(0x1E, 2)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#00308F#12PMireille ……\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    ChrTalk(
        0x1E,
        (
            "#07906F#5PIf you come with you at all\x01",
            "Do nothing wrong ……\x02\x03",
            "#07902FThe other party's\x01",
            "Leave it to us.\x02\x03",
            "……You guys.\x01",
            "No more Randy\x01",
            "You asked me not to be unreasonable?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12PYes……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#12PI was left to do.\x02",
    )

    CloseMessageWindow()
    OP_68(-23820, 1000, 133320, 2000)
    MoveCamera(25, 25, 0, 2000)
    SetCameraDistance(18500, 2000)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x1E, 0x1F)
    OP_95(0x1E, -28500, 0, 128750, 5000, 0x0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x1E, 0x80)
    Sleep(500)
    Fade(500)
    OP_93(0x101, 0xC8, 0x0)
    OP_93(0x102, 0xC8, 0x0)
    OP_93(0x103, 0xC8, 0x0)
    OP_93(0x109, 0xC8, 0x0)
    OP_93(0x105, 0xC8, 0x0)
    OP_68(-19800, 1000, 137300, 0)
    MoveCamera(20, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00006F#5PWhew … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PTentatively …\x01",
            "It seems that the first paragraph appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00314F#5P#40W…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(-20300, 1000, 137800, 1500)

    def lambda_B00E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B00E)
    Sleep(50)

    def lambda_B01E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B01E)

    def lambda_B02B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B02B)
    Sleep(50)

    def lambda_B03B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B03B)

    def lambda_B048():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B048)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#12PRandy … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#12PIs that okay?\x01",
            "I guessed somewhere ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00303F#30W#5P…… Lloyd.\x01",
            "I will ask again …\x02\x03",
            "#00312FWhat on earth is he doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12PHuh……\x02",
    )

    CloseMessageWindow()

    def lambda_B141():

        label("loc_B141")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_B141")

    QueueWorkItem2(0x102, 2, lambda_B141)

    def lambda_B153():

        label("loc_B153")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_B153")

    QueueWorkItem2(0x103, 2, lambda_B153)

    def lambda_B165():

        label("loc_B165")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_B165")

    QueueWorkItem2(0x109, 2, lambda_B165)

    def lambda_B177():

        label("loc_B177")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_B177")

    QueueWorkItem2(0x105, 2, lambda_B177)
    OP_68(-20000, 1000, 137800, 1000)
    OP_9A(0x104, 0x101, 0x190, 0x3E8, 0x0)
    Fade(250)
    SetCameraDistance(20000, 250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x47)
    SetChrSubChip(0x101, 0x29)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x47)
    SetChrSubChip(0x104, 0x2)

    def lambda_B1EA():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B1EA)
    OP_0D()
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011F#12PHuh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PRandy! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11PRandy's …! Is it?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    SetCameraDistance(18000, 50000)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00311F#30W#5PDo you understand ……\x01",
            "You are \"battlefield\"\x01",
            "You entered a step … ….?\x02\x03",
            "#30WIt is not a soldier or a hunter,\x01",
            "It is not a professional killing professional\x01",
            "You guys ……\x02\x03",
            "#30WDid you do anything dangerous?\x01",
            "Do not you really understand …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#12P… … Randy ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#30W#5P…… Lady and Tio\x01",
            "There is something I want to say ……\x02\x03",
            "…… Noel and Wadi also\x01",
            "I do not know the danger\x01",
            "Why did not you stop ……\x02\x03",
            "#00311FBut, above all, Lloyd ─ ─\x01",
            "I guess the leader is … ….?\x02\x03",
            "At such a time, moving in a straightforward way\x01",
            "What to do with exposing their companions to danger …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P#30W…………Do not be silly.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetCameraDistance(20000, 100)

    def lambda_B4CF():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B4CF)
    Sound(811, 0, 60, 0)

    def lambda_B4EA():
        OP_A0(0xFE, 2000, 0x29, 0x2B)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B4EA)

    def lambda_B4F7():
        OP_A0(0xFE, 2000, 0x2, 0x4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_B4F7)

    def lambda_B504():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B504)

    def lambda_B519():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B519)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x104, 1)
    Sleep(500)
    OP_68(-20350, 1000, 137900, 500)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_99(0x101, 0x104, 0x190, 0x3E8, 0x0)
    OP_6F(0x79)
    SetCameraDistance(18000, 120000)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x47)
    SetChrSubChip(0x101, 0x2C)
    SetChrSubChip(0x104, 0x5)

    def lambda_B5B1():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B5B1)
    OP_0D()

    ChrTalk(
        0x104,
        "#00305F#5PDamn it …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12PLloyd …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12PMr. Lloyd …!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00010F#12PBecause I can not put my companions in danger#24R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#\x01",
            "I wonder if it has come so far! Is it?\x02\x03",
            "#00006F\"Well then,\" …\x02\x03",
            "#00007F…… With such a piece of paper\x01",
            "We can be convinced ……\x01",
            "Did you really think that! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0x104, 1000, 0x20, 0x21)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00313F#5P#30WDamn\x02\x03",
            "After all … I …\x02\x03",
            "#40WI … … In the first place with you guys\x01",
            "I should not have stayed together …\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_CB(0x2, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00313F#30W#5P…… My hands are bloody … …\x02\x03",
            "It was not just a killing soldier on the battlefield ……\x02\x03",
            "To fit a tough enemy unit\x01",
            "Sometimes I used a village hey ….\x02\x03",
            "So do not sin either … ….\x02\x03",
            "…… Young woman with eyes like you\x01",
            "There are things I sacrificed …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P…!\x02",
    )

    CloseMessageWindow()
    OP_68(-20000, 1000, 137750, 500)
    SetChrSubChip(0x101, 0x2D)

    def lambda_B987():
        OP_9B(0x1, 0xFE, 0xFFF6, 0xFFFFFDA8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B987)

    def lambda_B99C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B99C)
    Sound(811, 0, 60, 0)

    def lambda_B9BB():
        OP_A0(0xFE, 1500, 0x6, 0x7)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_B9BB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    Sleep(500)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#00307F#5PYou are in front of you\x01",
            "I guess I'm such a salvation fucker!\x02\x03",
            "#00306FIt's annoying … … More than that!\x02\x03",
            "Squeezed away with eyes like a puppy\x01",
            "I was relying on my brother like that I could …!\x02\x03",
            "#00308FIf you continue to do that … … I am ha!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x104,
        (
            "#00313F#4S#5P#40W…… I am myself ……\x01",
            "I'm going to forgive you! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#30W… …. Randy …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#11P#30WRandy san ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#12P#30W………Senior……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F#11P#30W……… that sort of thing …………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P#30W…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_A0(0x101, 1000, 0x2D, 0x30)

    ChrTalk(
        0x101,
        (
            "#00004F#12P#30W………my mother……………\x02\x03",
            "I'm glad … I was relieved.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x12C, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_A0(0x104, 1500, 0x7, 0xA)
    Sleep(150)

    ChrTalk(
        0x104,
        "#00305F#40W#5P……… Eh ……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PB, Lloyd …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11PMr. Lloyd … ….?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0x101, 1000, 0x2F, 0x2D)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W…… With the face we can afford as usual\x01",
            "If you are joking and returning\x01",
            "I thought what to do ……\x02\x03",
            "#00002FFinally …\x01",
            "You spit it out to us?\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x104, 0x7D0, 0x4, 0x1D, 0x1E, 0x1D, 0xA)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x104,
        "#00305F#5PIt is! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12P#30W……Ah………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#12P#30WMr. Lloyd … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30WIf you think about it, Randy will also\x01",
            "It is the same young man as us … …\x02\x03",
            "#00008F…… I have a heavy thing\x01",
            "Everyone knows\x01",
            "I just cared about not to touch ……\x02\x03",
            "I just get to become a force,\x01",
            "I could not be the power of Randy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#11P#30W……Yes……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#12P#30W……… well … … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5P#30W…… Okay … Hey … … …\x02\x03",
            "#00301FSo that way\x01",
            "I can not qualify …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W── In the past of Randy,\x01",
            "The feeling of guilt is also Randy's own.\x02\x03",
            "#00003FPerhaps it is, Randy is in himself\x01",
            "I think that should be solved.\x02\x03",
            "#00001FAs a result, it is true that you\x01",
            "There may be things that can not be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#5P#30W…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30WBut someone else\x01",
            "Even if I do not allow Randy ……\x02\x03",
            "Even if Randy himself\x01",
            "Even if I can not forgive myself ……\x02\x03",
            "#00002F…… only us\x01",
            "I will forgive Randy.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x104,
        "#00305F#5P#4SIt is! It is! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12P#30W… That's right.\x02\x03",
            "#00102FAllowing each other and admitting each other\x01",
            "Because it is called \"fellow\" ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11P#30WEveryone before, my past\x01",
            "As I accepted … ….\x02\x03",
            "#00202FRandy's past, too,\x01",
            "Nanpa's personality and,\x01",
            "I will forgive sluggish place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#12P#30W…… I will forgive.\x02\x03",
            "#10100FAs the same soldier ……\x01",
            "It is a problem that can not be avoided if I avoid it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11P#30WWhew, this is\x01",
            "It is not my character.\x02\x03",
            "#10304F…… In the first place people are alive\x01",
            "It is the existence which carries something of sin.\x02\x03",
            "#10300FWhy do not you say this … ….\x01",
            "Is not there a big difference before the goddess?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0x104, 1500, 0xA, 0xD)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00314F#40W#5P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30WWe can not live in the past,\x01",
            "I can not live tomorrow I have not seen yet …\x02\x03",
            "The day of today, the moment of now,\x01",
            "I think that there is no other choice but to live alone.\x02\x03",
            "#00008FAnd now this moment ……\x01",
            "We are in the same place at the same time.\x02\x03",
            "If Randy does it even a little\x01",
            "If you are glad you …\x02\x03",
            "#00000FPlease forgive us who forgive Randy\x01",
            "I want you to accept it as it is.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_C597():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C597)
    WaitChrThread(0x104, 2)
    Sleep(500)

    def lambda_C5B7():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C5B7)
    WaitChrThread(0x104, 2)
    Sleep(500)
    OP_A0(0x104, 1500, 0xE, 0x10)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00313F#40W#5P…………………………………….\x02\x03",
            "…… っ ぱ く …… When you come with you … …\x02\x03",
            "#40WWhy am I … … such a wonderful word\x01",
            "You have to be exposed … …\x02\x03",
            "#40W…… What shame play is it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PWell, once again I\x01",
            "It is a way passed through … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PHehe, as you mentioned before … …\x02\x03",
            "#00102FWhen I chose the support department\x01",
            "Everyone's someone's\x01",
            "It will be a victim.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#11PNo, so why am I … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#12PHehu ……\x01",
            "But it seems to be convincing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#11PHaha, as I expected\x01",
            "Natural gigolo does not enemy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00314F#40W#5P…………………………………….\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    Sleep(150)
    OP_A0(0x104, 1200, 0x10, 0x13)
    Sleep(500)
    Sound(2374, 255, 80, 0)
    OP_A0(0x104, 1200, 0x13, 0x16)
    Sleep(800)

    ChrTalk(
        0x104,
        (
            "#00306F#5P#30W…… Huh.\x02\x03",
            "#00303FI am a murderer ……\x01",
            "It is a huge bastard of Rokudenashi.\x02\x03",
            "Where I got it\x01",
            "As a girl you like goddess\x01",
            "It is enough to take a lag.\x02\x03",
            "#00308FTempered like this\x01",
            "Even bothering me\x01",
            "It may be there in the future …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    OP_A0(0x104, 1300, 0x16, 0x19)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7569", 0)

    AnonymousTalk(
        0x104,
        "#5P#30W── Still, is it OK?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00014F#12PAh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#12PYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00214F#11PHow come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#12PFrom now on\x01",
            "Thank you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHehu ……\x01",
            "What does it take after it rains?\x02",
        )
    )

    CloseMessageWindow()
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x32, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sleep(500)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    OP_68(-19000, 1000, 137650, 1000)

    def lambda_CB31():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CB31)
    Sleep(500)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#00310F#5PWas this review helpful?\x02\x03",
            "I was promised to be silent\x01",
            "I was stupid! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PYou are misunderstood.\x02\x03",
            "#10306FI was silent properly\x01",
            "Lloyd's without permission\x01",
            "I'm starting to find out where you are.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CC10():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CC10)
    Sleep(50)

    def lambda_CC20():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CC20)

    def lambda_CC2D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CC2D)
    Sleep(50)

    def lambda_CC3D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CC3D)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x109,
        (
            "#10105F#6PWait a minute, are not you …?\x02\x03",
            "#10101FYou, Randy-senpai\x01",
            "I knew that I went out! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PWadi, you're …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12PMr. Wasi …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PHa, indeed\x01",
            "I think something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PNo, even I am a destination\x01",
            "I did not hear that ….\x02\x03",
            "#10306FWhew ……\x01",
            "Is this the bad guy I am?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#6PAltogether ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PSometimes Wasy\x01",
            "I should refrain from it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5Pmy mother……\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x9B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00304F#5P── Okay.\x01",
            "It seems that I managed to move.\x02\x03",
            "#00300FSlowly, Mireille's\x01",
            "Let's go see the state.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CE9A():
        OP_93(0xFE, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CE9A)
    Sleep(50)

    def lambda_CEAA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CEAA)

    def lambda_CEB7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CEB7)
    Sleep(50)

    def lambda_CEC7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CEC7)

    def lambda_CED4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_CED4)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        "#00000F#12PThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12P\"Red constellation\" ……\x01",
            "Withdrawing somehow\x01",
            "I do not mind.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    ReplaceBGM(-1, -1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 3)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_72_9B72 end

    def Function_73_CF90(): pass

    label("Function_73_CF90")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -20000, 4000, 152450, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_73_CF90 end

    def Function_74_CFBE(): pass

    label("Function_74_CFBE")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -20000, 4000, 155150, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_74_CFBE end

    def Function_75_CFF2(): pass

    label("Function_75_CFF2")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -32000, -1000, 102300, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    StopEffect(0x0, 0x2)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -34000, -1000, 107960, 4000, 0x0)
    OP_95(0xFE, -34000, 0, 89150, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -37350, 0, 76050, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_75_CFF2 end

    def Function_76_D0E8(): pass

    label("Function_76_D0E8")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -18750, 4000, 155600, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_76_D0E8 end

    def Function_77_D11C(): pass

    label("Function_77_D11C")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    Sleep(1500)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -29680, -1000, 108290, 4000, 0x0)
    OP_95(0xFE, -32800, 0, 88200, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    Return()

    # Function_77_D11C end

    def Function_78_D1A1(): pass

    label("Function_78_D1A1")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -21500, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -21500, 4000, 152550, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_78_D1A1 end

    def Function_79_D1F7(): pass

    label("Function_79_D1F7")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -30450, -1000, 108500, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, -32100, 0, 93750, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    StopEffect(0x1, 0x2)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -31360, 0, 87960, 4000, 0x0)
    OP_95(0xFE, -33960, 0, 81120, 4000, 0x0)
    OP_95(0xFE, -34760, 0, 71820, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_79_D1F7 end

    def Function_80_D2B8(): pass

    label("Function_80_D2B8")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -18800, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -18800, 4000, 152400, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_80_D2B8 end

    def Function_81_D30E(): pass

    label("Function_81_D30E")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -33250, -1000, 107600, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    Sleep(2000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -34390, 0, 90290, 4000, 0x0)
    OP_95(0xFE, -39800, 0, 82050, 4000, 0x0)
    OP_95(0xFE, -38250, 0, 70760, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_81_D30E end

    def Function_82_D395(): pass

    label("Function_82_D395")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -27250, 8000, 183450, 5000, 0x0)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -18150, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -18150, 4000, 154150, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_82_D395 end

    def Function_83_D3FF(): pass

    label("Function_83_D3FF")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -34000, -1000, 107960, 4000, 0x0)
    OP_95(0xFE, -32500, -1000, 103650, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, -32750, 0, 90700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(2500)
    StopEffect(0x2, 0x2)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -34390, 0, 90290, 4000, 0x0)
    OP_95(0xFE, -39800, 0, 82050, 4000, 0x0)
    OP_95(0xFE, -38250, 0, 70760, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_83_D3FF end

    def Function_84_D4DB(): pass

    label("Function_84_D4DB")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -27250, 8000, 183450, 5000, 0x0)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -20900, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -20900, 4000, 154150, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_84_D4DB end

    def Function_85_D545(): pass

    label("Function_85_D545")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -29800, -1000, 107850, 4000, 0x0)
    OP_95(0xFE, -31150, -1000, 101100, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 88)
    Sleep(2500)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    OP_95(0xFE, -31360, 0, 87960, 4000, 0x0)
    OP_95(0xFE, -33960, 0, 81120, 4000, 0x0)
    OP_95(0xFE, -34760, 0, 71820, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_85_D545 end

    def Function_86_D5E7(): pass

    label("Function_86_D5E7")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -27170, 8000, 190850, 5000, 0x0)
    OP_95(0xFE, -27250, 8000, 183450, 5000, 0x0)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -15550, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -17550, 4000, 152900, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_86_D5E7 end

    def Function_87_D665(): pass

    label("Function_87_D665")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -27170, 8000, 190850, 5000, 0x0)
    OP_95(0xFE, -27250, 8000, 183450, 5000, 0x0)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -22250, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -22250, 4000, 153950, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_87_D665 end

    def Function_88_D6E9(): pass

    label("Function_88_D6E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D738")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 950, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x3, 0x2)
    Jump("Function_88_D6E9")

    label("loc_D738")

    Return()

    # Function_88_D6E9 end

    def Function_89_D739(): pass

    label("Function_89_D739")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -32650, 0, 89540, 6000, 0x0)
    OP_95(0xFE, -37240, 0, 83770, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xFE, 0x10E, 0x3E8)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF6276, 0xA28, 0x14776, 0xBB8, 0x1770)
    Sound(326, 0, 100, 0)
    OP_95(0xFE, -43910, 2600, 80620, 6000, 0x0)
    OP_93(0xFE, 0x87, 0x3E8)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF5FD8, 0x14B4, 0x130B0, 0xBB8, 0x1770)
    Sound(326, 0, 100, 0)
    OP_95(0xFE, -38420, 5300, 70130, 6000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_89_D739 end

    def Function_90_D7FE(): pass

    label("Function_90_D7FE")

    Sound(865, 2, 60, 0)
    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(1000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -33500, -1000, 100150, 5000, 0x0)
    OP_95(0xFE, -32900, 0, 91150, 5000, 0x0)
    OP_95(0xFE, -36550, 0, 84250, 5000, 0x0)
    OP_95(0xFE, -36950, 0, 67700, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_90_D7FE end

    def Function_91_D881(): pass

    label("Function_91_D881")

    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(1300)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -30050, -810, 99000, 5000, 0x0)
    OP_95(0xFE, -32049, 0, 90500, 5000, 0x0)
    OP_95(0xFE, -35650, 0, 79100, 5000, 0x0)
    OP_95(0xFE, -34860, 0, 68450, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_91_D881 end

    def Function_92_D8FE(): pass

    label("Function_92_D8FE")

    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(2500)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -32900, 0, 91150, 5000, 0x0)
    OP_95(0xFE, -36550, 0, 84250, 5000, 0x0)
    OP_95(0xFE, -36950, 0, 67700, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_92_D8FE end

    def Function_93_D967(): pass

    label("Function_93_D967")

    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(2800)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -32049, 0, 90500, 5000, 0x0)
    OP_95(0xFE, -35650, 0, 79100, 5000, 0x0)
    OP_95(0xFE, -34860, 0, 68450, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_93_D967 end

    def Function_94_D9D0(): pass

    label("Function_94_D9D0")

    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(5000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -35650, 0, 79100, 5000, 0x0)
    OP_95(0xFE, -34860, 0, 68450, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_94_D9D0 end

    def Function_95_DA25(): pass

    label("Function_95_DA25")

    SetChrChipByIndex(0xFE, 0x33)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(5000)
    StopSound(865, 500, 50)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    Sleep(300)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    OP_95(0xFE, -36550, 0, 84250, 5000, 0x0)
    OP_95(0xFE, -36950, 0, 67700, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_95_DA25 end

    def Function_96_DA80(): pass

    label("Function_96_DA80")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DAA4")
    OP_82(0xA, 0xA, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_96_DA80")

    label("loc_DAA4")

    Return()

    # Function_96_DA80 end

    def Function_97_DAA5(): pass

    label("Function_97_DAA5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DAC9")
    OP_82(0x28, 0x28, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_97_DAA5")

    label("loc_DAC9")

    Return()

    # Function_97_DAA5 end

    def Function_98_DACA(): pass

    label("Function_98_DACA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_E2(0x1)
    SetChrPos(0x101, -250, 0, -750, 0)
    SetChrPos(0x106, 750, 0, -1500, 0)
    SetChrPos(0x103, -1250, 0, -2500, 0)
    SetChrPos(0x107, -2250, 0, -2750, 0)
    SetChrPos(0x105, -250, 0, -3500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(0, 600, -2000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    OP_68(140, 600, 1460, 2000)
    MoveCamera(45, 25, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(20500, 2000)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)

    def lambda_DBA8():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DBA8)
    Sleep(0)

    def lambda_DBC0():
        OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DBC0)
    Sleep(0)

    def lambda_DBD8():
        OP_9B(0x0, 0x106, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_DBD8)
    Sleep(0)

    def lambda_DBF0():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DBF0)
    Sleep(0)

    def lambda_DC08():
        OP_9B(0x0, 0x107, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_DC08)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    OP_0D()
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#11PTio\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PAbout 10 Selge from here!\x02\x03",
            "Probably deviated from the mountain path\x01",
            "Or battle in mountainous areas … …!\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7586", 0)
    ReplaceBGM("ed7251", "ed7586")

    ChrTalk(
        0x101,
        "#00010F#11PUgh. Mountainland\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#12PWith our feet, easy\x01",
            "You may not be able to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10707F#11PHouse……\x01",
            "Let's go anyway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01201F#12P#3CWhen it comes to our emergency\x01",
            "Let's jump over the cliff and intervene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#11PI understood!\x01",
            "If it seems necessary, I will ask!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 1500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x1A2, 5)
    OP_29(0xAF, 0x1, 0xC)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetBarrier(0x0, 0x0, 0x1, 0x0, -19610, 3500, 152140, 8000, 5000, 0)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    Return()

    # Function_98_DACA end

    def Function_99_DEA4(): pass

    label("Function_99_DEA4")

    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    OP_68(-19600, 4400, 152850, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25650, 0)
    SetChrPos(0x101, -19600, 3800, 151650, 0)
    SetChrPos(0x106, -19000, 3350, 150700, 0)
    SetChrPos(0x103, -21000, 3550, 151100, 0)
    SetChrPos(0x107, -21900, 3350, 150700, 0)
    SetChrPos(0x105, -20450, 3100, 150150, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x107, 0x5)
    OP_0D()

    ChrTalk(
        0x101,
        "#00010F#11PWhat the hell is this! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10408F#12PTo block the theater\x01",
            "Where is barbed wire ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PBattle is above this\x01",
            "It seems to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#11Pit can not be helped……\x01",
            "Let's find a place to wrap around!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -19790, 3280, 150550, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x1A2, 6)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_99_DEA4 end

    def Function_100_E03D(): pass

    label("Function_100_E03D")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x1)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("apl/ch51708.itc", 0x32)
    LoadChrToIndex("apl/ch51709.itc", 0x33)
    LoadChrToIndex("apl/ch51775.itc", 0x34)
    LoadChrToIndex("chr/ch00050.itc", 0x37)
    LoadChrToIndex("chr/ch00250.itc", 0x41)
    LoadChrToIndex("chr/ch03150.itc", 0x55)
    LoadChrToIndex("chr/ch02750.itc", 0x50)
    LoadChrToIndex("chr/ch03250.itc", 0x3C)
    LoadChrToIndex("chr/ch0325A.itc", 0x3D)
    LoadChrToIndex("chr/ch03257.itc", 0x3E)
    LoadEffect(0x0, "event/ev17048.eff")
    LoadEffect(0x1, "event/eva01_01.eff")
    SoundLoad(863)
    SoundLoad(864)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 0x32)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x1F)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    StopEffect(0x9, 0x0)
    StopEffect(0xA, 0x0)
    OP_F3(100000)
    ClearScenarioFlags(0x0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 0)), scpexpr(EXPR_END)), "loc_E15B")
    SetScenarioFlags(0x0, 4)

    label("loc_E15B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 1)), scpexpr(EXPR_END)), "loc_E167")
    SetScenarioFlags(0x0, 4)

    label("loc_E167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 2)), scpexpr(EXPR_END)), "loc_E173")
    SetScenarioFlags(0x0, 4)

    label("loc_E173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 3)), scpexpr(EXPR_END)), "loc_E17F")
    SetScenarioFlags(0x0, 4)

    label("loc_E17F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 4)), scpexpr(EXPR_END)), "loc_E18B")
    SetScenarioFlags(0x0, 4)

    label("loc_E18B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 5)), scpexpr(EXPR_END)), "loc_E197")
    SetScenarioFlags(0x0, 4)

    label("loc_E197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 6)), scpexpr(EXPR_END)), "loc_E1A3")
    SetScenarioFlags(0x0, 4)

    label("loc_E1A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 7)), scpexpr(EXPR_END)), "loc_E1AF")
    SetScenarioFlags(0x0, 4)

    label("loc_E1AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 0)), scpexpr(EXPR_END)), "loc_E1BB")
    SetScenarioFlags(0x0, 4)

    label("loc_E1BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 1)), scpexpr(EXPR_END)), "loc_E1C7")
    SetScenarioFlags(0x0, 4)

    label("loc_E1C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 2)), scpexpr(EXPR_END)), "loc_E1D3")
    SetScenarioFlags(0x0, 4)

    label("loc_E1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 3)), scpexpr(EXPR_END)), "loc_E1DF")
    SetScenarioFlags(0x0, 4)

    label("loc_E1DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1EE")
    OP_2C(0xAF, 0x1)

    label("loc_E1EE")

    SetChrPos(0x101, 3800, 0, 134250, 95)
    SetChrPos(0x106, 2800, 0, 135300, 95)
    SetChrPos(0x103, 1650, 0, 133250, 95)
    SetChrPos(0x107, 900, 0, 131850, 95)
    SetChrPos(0x105, 750, 0, 134500, 95)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_52(0x107, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x20, 10700, 10000, 152000, 180)
    SetChrPos(0x21, 22750, 14000, 155150, 225)
    SetChrPos(0x22, 7000, 15000, 165350, 180)
    SetChrPos(0x23, -6000, 0, 129500, 95)
    SetChrPos(0x24, -5350, 0, 142650, 140)
    SetChrPos(0x25, 15250, 0, 123500, 320)
    SetChrPos(0x26, 18500, 0, 131500, 275)
    OP_68(3000, 1000, 134200, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(6250, 1000, 133850, 2500)
    MoveCamera(50, 25, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(22000, 2500)
    FadeToBright(1000, 0)

    def lambda_E34F():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E34F)
    Sleep(10)

    def lambda_E367():
        OP_9B(0x0, 0x106, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_E367)
    Sleep(10)

    def lambda_E37F():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E37F)
    Sleep(10)

    def lambda_E397():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E397)
    Sleep(10)

    def lambda_E3AF():
        OP_9B(0x0, 0x107, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_E3AF)
    Sleep(10)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5P…\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x106,
        "#10707F#6P#4SLLOYD!\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    ReplaceBGM(-1, -1)
    Sound(567, 0, 100, 0)
    OP_68(7950, 1000, 135000, 300)
    MoveCamera(50, 20, 0, 300)
    OP_6E(510, 300)
    SetCameraDistance(24000, 300)
    SetChrFlags(0x106, 0x20)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x106, 0x3D)
    SetChrSubChip(0x106, 0x1)
    Sound(251, 0, 100, 0)
    OP_96(0x106, 0x1F40, 0x0, 0x20F26, 0x2710, 0x0)

    def lambda_E4A8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E4A8)
    SetChrChipByIndex(0x106, 0x3C)
    SetChrSubChip(0x106, 0x0)
    OP_93(0x106, 0x5, 0x3E8)
    SetChrChipByIndex(0x106, 0x3E)
    SetChrSubChip(0x106, 0x0)
    PlayEffect(0x0, 0xFF, 0x106, 0x5, 0, 800, -1200, 180, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x106, 0x5, 0, 1200, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetCameraDistance(20530, 500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(361, 0, 100, 0)
    Sound(566, 0, 60, 0)
    OP_A6(0x106, 0x0, 0x14, 0x1F4, 0xBB8)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sleep(300)
    CancelBlur(0)

    def lambda_E587():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E587)
    Sleep(50)

    def lambda_E597():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E597)
    Sleep(50)

    def lambda_E5A7():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E5A7)
    Sleep(50)

    def lambda_E5B7():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_E5B7)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    ChrTalk(
        0x105,
        "#10410F#6PAmbush?!\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5, 0x1F4)

    ChrTalk(
        0x103,
        "#00207F#12PUp there!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    Fade(500)
    OP_68(9000, 4400, 147650, 0)
    MoveCamera(35, -8, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_68(9860, 10000, 150940, 4000)
    MoveCamera(40, 4, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(18000, 4000)
    SetChrFlags(0x20, 0x800)
    OP_6F(0x79)

    ChrTalk(
        0x20,
        (
            "#5PAs expected, \"silver#2RIn#\".\x01",
            "It is something you noticed often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#11PDamn\x01",
            "Were you in an ambush! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PThere was movement in the tunnel road\x01",
            "I knew it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PBut to the crossbell under the martial law\x01",
            "It is said that this also goes out here and there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PAs I thought, the knights\x01",
            "Strategic boat#6RMel kava#Do you use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#11PWow ….\x01",
            "Have you identified my status as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5POkita, resistance and\x01",
            "I wonder if she came even to combine hands ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PI was late for a while.\x01",
            "The sweeping operation has already begun.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(11210, 11800, 153420, 2000)
    MoveCamera(23, 4, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(20580, 2000)
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x20, 0x33)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x2)
    OP_0D()
    OP_6F(0x79)
    Sound(863, 2, 100, 0)
    Sound(864, 2, 80, 0)

    ChrTalk(
        0x20,
        (
            "#5PSomewhat strange, though\x01",
            "Soon suppression will be completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PIt's bad, but holding a finger there\x01",
            "Let's have a view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#11PTch. You think we'll let you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10707F#11PThis is me and Mr. Zeit\x01",
            "Breakthrough ……!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PI won't let you!\x02",
    )

    CloseMessageWindow()
    StopSound(864, 1000, 100)
    StopSound(863, 1000, 80)
    Fade(250)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 0x34)
    OP_A0(0x20, 1500, 0x0, 0x1)
    Sound(947, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0x101, 0x37)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x5F, 0x0)
    SetChrChipByIndex(0x103, 0x41)
    SetChrSubChip(0x103, 0x0)
    OP_93(0x103, 0x8C, 0x0)
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    OP_93(0x105, 0x140, 0x0)
    SetChrChipByIndex(0x107, 0x50)
    SetChrSubChip(0x107, 0x0)
    OP_93(0x107, 0x113, 0x0)
    SetChrChipByIndex(0x106, 0x3C)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x106, 6780, 0, 134950, 5)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    OP_68(6250, 1000, 133850, 5000)
    MoveCamera(50, 30, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(23000, 5000)
    BeginChrThread(0x21, 1, 0, 101)
    BeginChrThread(0x22, 1, 0, 102)
    StopBGM(0xFA0)
    Sleep(3000)
    BeginChrThread(0x32, 1, 0, 71)
    BeginChrThread(0x23, 3, 0, 56)

    def lambda_EA8B():
        OP_95(0xFE, 1300, 0, 131450, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_EA8B)
    Sleep(100)
    BeginChrThread(0x24, 3, 0, 56)

    def lambda_EAAE():
        OP_95(0xFE, 1750, 0, 136900, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_EAAE)
    Sleep(100)
    BeginChrThread(0x25, 3, 0, 56)

    def lambda_EAD1():
        OP_95(0xFE, 8390, 0, 129310, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_EAD1)
    Sleep(100)
    BeginChrThread(0x26, 3, 0, 56)

    def lambda_EAF4():
        OP_95(0xFE, 11450, 0, 133150, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_EAF4)
    WaitChrThread(0x23, 1)
    BeginChrThread(0x23, 3, 0, 57)
    WaitChrThread(0x24, 1)
    BeginChrThread(0x24, 3, 0, 57)
    WaitChrThread(0x25, 1)
    BeginChrThread(0x25, 3, 0, 57)
    WaitChrThread(0x26, 1)
    EndChrThread(0x32, 0x1)
    BeginChrThread(0x26, 3, 0, 57)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x22, 1)
    OP_6F(0x79)

    ChrTalk(
        0x106,
        "#10701F#11P…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01201F#11P#3CHmm. So we're surrounded\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10408F#12PThis looks a bit bad\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7455", 0)
    Fade(500)
    SetChrChipByIndex(0x20, 0x33)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x2)
    OP_68(10700, 10600, 152000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18000, 800)
    OP_0D()
    OP_6F(0x79)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 100, 0)
    OP_A1(0x20, 0x5DC, 0x2, 0x1, 0x2)
    Sleep(300)

    ChrTalk(
        0x20,
        (
            "#5PLloyd Bannings.\x01",
            "And that one party …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5P\"Red constellation\" is the regiment head,\x01",
            "Gales of 'Sudden' is the opponent.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(6250, 1000, 133850, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00007F#5PDamn\x01",
            "Everyone is in an intercept!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#5PTo a sniper from the cliff\x01",
            "be careful!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    EndChrThread(0x21, 0x3)
    EndChrThread(0x22, 0x3)
    EndChrThread(0x23, 0x3)
    EndChrThread(0x24, 0x3)
    EndChrThread(0x25, 0x3)
    EndChrThread(0x26, 0x3)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x6)
    SetChrChipByIndex(0x22, 0x1F)
    SetChrSubChip(0x22, 0x6)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x6)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x6)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x6)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x6)

    def lambda_ED5D():
        OP_9D(0xFE, 0x1C52, 0x0, 0x20ADA, 0x1F4, 0x88B8)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_ED5D)

    def lambda_ED7A():
        OP_9D(0xFE, 0x1482, 0x0, 0x20ADA, 0x1F4, 0x88B8)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_ED7A)

    def lambda_ED97():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_ED97)

    def lambda_EDB4():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_EDB4)

    def lambda_EDD1():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_EDD1)

    def lambda_EDEE():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_EDEE)
    OP_24(0x35F)
    OP_24(0x360)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(20000, 200)
    Sleep(200)
    CancelBlur(200)
    Battle("BattleInfo_F14", 0x30200011, 0x0, 0x100, 0x17, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    EndChrThread(0x26, 0x1)
    Call(0, 103)
    Return()

    # Function_100_E03D end

    def Function_101_EE5F(): pass

    label("Function_101_EE5F")

    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    SetChrSubChip(0xFE, 0x6)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x4812, 0x2710, 0x24E3C, 0x3E8, 0x1770)
    BeginChrThread(0xFE, 3, 0, 56)
    OP_96(0xFE, 0x4268, 0x2710, 0x248C4, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x3C28, 0x1770, 0x22E66, 0x3E8, 0x1770)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 3, 0, 57)
    Return()

    # Function_101_EE5F end

    def Function_102_EED8(): pass

    label("Function_102_EED8")

    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    SetChrSubChip(0xFE, 0x6)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x1C52, 0x2710, 0x273BC, 0x3E8, 0x1770)
    BeginChrThread(0xFE, 3, 0, 56)
    OP_96(0xFE, 0x1FD6, 0x2710, 0x2576A, 0x1770, 0x0)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x1E14, 0x1770, 0x23668, 0x3E8, 0x1770)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 3, 0, 57)
    Return()

    # Function_102_EED8 end

    def Function_103_EF51(): pass

    label("Function_103_EF51")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    SoundLoad(2768)
    SoundLoad(2769)
    SoundLoad(2770)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07900.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02100.itp")
    AddParty(0x3, 0xFF, 0xFF)
    OP_32(0x3, 0x0, 0x54)
    OP_32(0x3, 0x5, 0x64)
    OP_42(0x3, 0x42D, 0xFF)
    OP_42(0x3, 0x5ED, 0xFF)
    OP_42(0x3, 0x651, 0xFF)
    OP_38(0x3, 0x81, 0x2)
    OP_38(0x3, 0x83, 0x2)
    OP_38(0x3, 0x84, 0x2)
    OP_38(0x3, 0x85, 0x2)
    OP_42(0x3, 0x8D, 0x1)
    OP_42(0x3, 0x9F, 0x3)
    OP_42(0x3, 0x6E, 0x4)
    OP_42(0x3, 0x7E, 0x5)
    AddCraft(0x3, 0xB9)
    AddCraft(0x3, 0xBA)
    AddCraft(0x3, 0x12A)
    OP_D7(0x0)
    OP_D7(0x10)
    OP_D7(0x11)
    OP_D7(0x12)
    OP_D7(0x13)
    OP_D7(0x14)
    OP_D7(0x15)
    OP_D7(0x16)
    OP_D7(0x17)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("apl/ch51709.itc", 0x32)
    LoadChrToIndex("apl/ch51710.itc", 0x33)
    LoadChrToIndex("chr/ch41951.itc", 0x34)
    LoadChrToIndex("chr/ch41952.itc", 0x35)
    LoadChrToIndex("chr/ch42051.itc", 0x5A)
    LoadChrToIndex("chr/ch42050.itc", 0x5B)
    LoadChrToIndex("chr/ch42052.itc", 0x5C)
    LoadChrToIndex("chr/ch42056.itc", 0x5D)
    LoadChrToIndex("chr/ch31251.itc", 0x23)
    LoadChrToIndex("chr/ch31252.itc", 0x24)
    LoadChrToIndex("chr/ch31351.itc", 0x5F)
    LoadChrToIndex("chr/ch31350.itc", 0x60)
    LoadChrToIndex("chr/ch31352.itc", 0x61)
    LoadChrToIndex("apl/ch50112.itc", 0x64)
    LoadChrToIndex("apl/ch50118.itc", 0x65)
    LoadChrToIndex("apl/ch50113.itc", 0x66)
    LoadChrToIndex("chr/ch00050.itc", 0x37)
    LoadChrToIndex("chr/ch00250.itc", 0x41)
    LoadChrToIndex("chr/ch03150.itc", 0x55)
    LoadChrToIndex("chr/ch02750.itc", 0x50)
    LoadChrToIndex("chr/ch03250.itc", 0x3C)
    LoadChrToIndex("chr/ch00352.itc", 0x46)
    LoadChrToIndex("chr/ch0035E.itc", 0x47)
    LoadChrToIndex("chr/ch32650.itc", 0x25)
    LoadChrToIndex("chr/ch32651.itc", 0x26)
    LoadChrToIndex("chr/ch32654.itc", 0x27)
    LoadChrToIndex("chr/ch06000.itc", 0x21)
    LoadChrToIndex("apl/ch50010.itc", 0x22)
    LoadEffect(0x0, "event/ev14020.eff")
    LoadEffect(0x1, "battle/sp003000.eff")
    LoadEffect(0x2, "battle/ms00000.eff")
    LoadEffect(0x3, "battle/btgun00.eff")
    LoadEffect(0x4, "event/eva01_01.eff")
    LoadEffect(0x8, "event/eva02_00.eff")
    SoundLoad(110)
    SoundLoad(974)
    SoundLoad(865)
    SoundLoad(863)
    SoundLoad(861)
    SetChrChipByIndex(0x101, 0x37)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x41)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x50)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x106, 0x3C)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0x20, 0x32)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x1E)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    SetChrChipByIndex(0x22, 0x1E)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    ClearChrFlags(0x25, 0x80)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    ClearChrFlags(0x26, 0x80)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x34)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x5A)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x5A)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x5A)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x11, 0x5F)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x5F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x5F)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x27, 0x65)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x65)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    SetChrChipByIndex(0x29, 0x65)
    SetChrSubChip(0x29, 0x0)
    SetChrFlags(0x29, 0x8000)
    SetChrChipByIndex(0x2A, 0x65)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2B, 0x65)
    SetChrSubChip(0x2B, 0x0)
    SetChrFlags(0x2B, 0x8000)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    StopEffect(0x9, 0x0)
    StopEffect(0xA, 0x0)
    OP_52(0x107, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 7780, 0, 133900, 95)
    SetChrPos(0x106, 6780, 0, 134950, 5)
    SetChrPos(0x103, 5630, 0, 132900, 140)
    SetChrPos(0x107, 4880, 0, 131500, 275)
    SetChrPos(0x105, 4730, 0, 134150, 320)
    SetChrPos(0x104, 21900, 14000, 153900, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x20, 10700, 10000, 152000, 180)
    SetChrPos(0x21, 9800, 0, 137600, 220)
    SetChrPos(0x22, 5200, 0, 138500, 180)
    SetChrPos(0x23, 1300, 0, 131450, 75)
    SetChrPos(0x24, 1750, 0, 136900, 130)
    SetChrPos(0x25, 8390, 0, 129310, 310)
    SetChrPos(0x26, 11450, 0, 133150, 280)
    BeginChrThread(0x21, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x22, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x23, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x24, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x25, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x26, 3, 0, 57)
    OP_68(6250, 1000, 133850, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2000)
    PlayBGM("ed7582", 0)
    Sound(110, 2, 30, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00010F#5P…… Ku … …\x01",
            "Truly \"Red constellation\" … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10410F#12PA sniper from a high place\x01",
            "That's awkward so far …!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    EndChrThread(0x21, 0x3)
    EndChrThread(0x22, 0x3)
    EndChrThread(0x23, 0x3)
    EndChrThread(0x24, 0x3)
    EndChrThread(0x25, 0x3)
    EndChrThread(0x26, 0x3)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    OP_68(10700, 10600, 152000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x20,
        (
            "#5PJust a young colleague\x01",
            "It's not a bad stroll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PBut as a sniper\x01",
            "At the time of high altitude being taken\x01",
            "Tactical defeat is inevitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PStand down quietly\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    StopSound(110, 4000, 20)
    Sound(973, 0, 100, 0)
    Sleep(800)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x20, 0x13B, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x20,
        "#11PWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PThat was…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PC-could it be\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#11P#3CHmm. They made it in time\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_68(8700, 10600, 153000, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x15, 15600, 21000, 37950, 195)
    SetChrPos(0x16, 13450, 21000, 42250, 195)
    SetChrPos(0x17, 10650, 21000, 43650, 195)
    SetChrPos(0x18, 15600, 21000, 37950, 195)
    SetChrPos(0x19, 13450, 21000, 42250, 195)
    SetChrPos(0x1A, 10650, 21000, 43650, 195)
    SetChrPos(0x23, 16900, 21000, 40050, 235)
    SetChrPos(0x24, 5550, 21000, 43750, 145)
    SetChrPos(0x27, 17200, 21000, 40500, 180)
    SetChrPos(0x28, 11150, 21000, 43950, 180)
    SetChrPos(0x29, 14600, 21000, 42050, 180)
    SetChrPos(0x2A, 15450, 21000, 40850, 180)
    SetChrPos(0x2B, 14150, 21000, 42150, 180)
    SetChrPos(0xD, 18850, 21000, 37900, 225)
    SetChrPos(0xE, 10000, 21000, 43900, 180)
    SetChrPos(0xF, 16350, 21000, 40850, 180)
    SetChrPos(0x11, 18850, 21000, 37400, 180)
    SetChrPos(0x12, 15600, 21000, 37950, 180)
    SetChrPos(0x13, 18600, 21000, 39500, 180)
    SetChrPos(0x1E, 12200, 21000, 42800, 180)
    OP_68(14320, 15500, 34850, 0)
    MoveCamera(55, 5, -5, 0)
    SetCameraDistance(21000, 0)
    OP_68(12250, 15900, 33850, 8000)
    MoveCamera(65, 25, -5, 8000)
    SetCameraDistance(23500, 8000)
    OP_11(0xFF, 0xFF, 0xFF, 0x1E, 0x1F4, 0x0)
    BeginChrThread(0x32, 1, 0, 141)
    FadeToBright(1000, 0)
    BeginChrThread(0x24, 1, 0, 122)
    BeginChrThread(0x23, 1, 0, 121)
    BeginChrThread(0x17, 1, 0, 113)
    BeginChrThread(0x1A, 1, 0, 119)
    BeginChrThread(0x16, 1, 0, 111)
    BeginChrThread(0x18, 1, 0, 115)
    BeginChrThread(0x15, 1, 0, 109)
    BeginChrThread(0x19, 1, 0, 117)
    BeginChrThread(0x27, 1, 0, 135)
    BeginChrThread(0x28, 1, 0, 136)
    BeginChrThread(0x29, 1, 0, 137)
    BeginChrThread(0x1E, 1, 0, 125)
    BeginChrThread(0xD, 1, 0, 127)
    BeginChrThread(0xE, 1, 0, 128)
    BeginChrThread(0xF, 1, 0, 129)
    BeginChrThread(0x11, 1, 0, 130)
    BeginChrThread(0x12, 1, 0, 131)
    BeginChrThread(0x13, 1, 0, 132)
    BeginChrThread(0x2A, 1, 0, 138)
    BeginChrThread(0x2B, 1, 0, 139)
    Sleep(8000)
    Fade(500)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x19, 0x1)
    Sound(865, 2, 50, 0)
    Sound(861, 2, 50, 0)
    SetChrChipByIndex(0x15, 0x35)
    BeginChrThread(0x15, 0, 0, 49)
    BeginChrThread(0x15, 3, 0, 50)
    SetChrChipByIndex(0x16, 0x35)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x16, 3, 0, 50)
    SetChrChipByIndex(0x17, 0x35)
    BeginChrThread(0x17, 0, 0, 49)
    BeginChrThread(0x17, 3, 0, 50)
    SetChrChipByIndex(0x18, 0x5B)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x5B)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x5B)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x23, 0x1E)
    BeginChrThread(0x23, 3, 0, 57)
    SetChrChipByIndex(0x24, 0x1E)
    BeginChrThread(0x24, 3, 0, 57)
    SetChrPos(0x15, 11300, 8000, 21350, 0)
    SetChrPos(0x16, 22150, 12000, 20940, 315)
    SetChrPos(0x17, 19200, 12000, 19100, 0)
    SetChrPos(0x18, 15050, 8000, 23450, 0)
    SetChrPos(0x19, 16850, 8000, 23000, 0)
    SetChrPos(0x1A, 8300, 8000, 19300, 45)
    SetChrPos(0x23, 13500, 8000, 25150, 0)
    SetChrPos(0x24, 14450, 12000, 18100, 0)
    OP_68(17990, 13000, 30170, 0)
    MoveCamera(125, 35, -10, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(30000, 4000)
    OP_82(0x0, 0x64, 0xBB8, 0xFA0)
    Sleep(4000)
    Fade(500)
    OP_68(14600, 12800, 29330, 0)
    MoveCamera(62, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(33000, 0)
    SetCameraDistance(37000, 4000)
    OP_82(0x0, 0x64, 0xBB8, 0xFA0)
    Sleep(2000)
    StopSound(865, 900, 40)
    StopSound(861, 900, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x64, 0xBB8, 0x0)
    StopSound(974, 1000, 50)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x11, 0x1)
    ClearChrFlags(0x18, 0x20)
    ClearChrFlags(0x11, 0x20)
    EndChrThread(0x23, 0x3)
    EndChrThread(0x24, 0x3)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    OP_11(0xFF, 0xFF, 0xFF, 0x1E, 0x96, 0x0)
    SetChrPos(0x20, 11400, 10000, 153550, 315)
    OP_68(9400, 10600, 154550, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(11400, 10600, 153550, 2000)
    Sound(863, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x20,
        "#11PCut … … as a wolf! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00214F#11PTch. Wolves?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11Pin addition……\x01",
            "That is Mireille! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#11PDamn\x01",
            "Taka like a beast!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#11PAll right!\x01",
            "Hang it from here ──\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x104,
        "Voice of a young man",
        "#2768V#15A#30WVery well then I'll engage them from here!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x20, 0x5A, 0x1F4)
    Fade(500)
    OP_68(21900, 15000, 153900, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(14500, 0)
    SetChrChipByIndex(0x104, 0x46)
    SetChrSubChip(0x104, 0x5)
    OP_0D()
    OP_68(10700, 11200, 153480, 1000)
    MoveCamera(37, 26, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(17100, 1000)
    SetChrSubChip(0x104, 0x1)
    Sound(2293, 255, 100, 0)
    Sound(844, 0, 100, 0)
    OP_9D(0x104, 0x31CE, 0x2710, 0x25706, 0x3E8, 0x1388)
    Fade(100)
    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0x20, 0x33)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x2)
    SetChrSubChip(0x104, 0x2)
    OP_0D()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    PlayEffect(0x4, 0xFF, 0x20, 0x5, 0, 1200, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(372, 0, 60, 0)
    Sound(566, 0, 70, 0)
    SetChrSubChip(0x104, 0x3)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x1000)
    OP_9B(0x1, 0x20, 0x0, 0xFFFFF63C, 0x2710, 0x0)
    ClearChrFlags(0x20, 0x20)
    ClearChrFlags(0x20, 0x1000)

    ChrTalk(
        0x20,
        "#5PYou think I'll let you, Gares?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01200F#11P#3CAh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11POh\x02",
    )

    CloseMessageWindow()
    MoveCamera(27, 26, 0, 20000)
    OP_A1(0x104, 0x5DC, 0x2, 0x4, 0x5)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x104,
        (
            "#00304F#2769V#11PR-randy!\x02\x03",
            "#00302F#2770VThere will be stories to be piled up\x01",
            "For the time being, I will postpone it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xAD2)
    OP_C9(0x1, 0x80000000)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x20, 0x32)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x20,
        "#5PLots to say, but let's clean up the trash first\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PNo doubt a sniper\x01",
            "It is not to take behind me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PWell, if there are no activists from the wolves\x01",
            "Although it was bad place.\x02\x03",
            "#00301FFor those and Lloyd's\x01",
            "You made a mistake that was distracting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PAnd it was your bad for engaging Lloyd's team\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5P…… But young,\x01",
            "As usual that product#4RHalberd#Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PWithout blade rifle\x01",
            "Do you think that I can win this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#11PSeparately?\x01",
            "Why not use it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x47)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(300)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00300F#11PTo Guillaume's Osan\x01",
            "I was repaired.\x02\x03",
            "#00306FBesides, no matter how powerful it is\x01",
            "Once you are engaged in the engineering department\x01",
            "Usability drops.\x02\x03",
            "#00302FAnd even if it is strong some engines are stronger than others\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PSo I got it all set for a time like this\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PCertainly now with a blow\x01",
            "Gifts#4Rrifle#The accuracy of this was also mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PI might be at a disadvantage\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PYeah. Get the hell out of here\x02\x03",
            "#00307FThen tell your uncle … …\x01",
            "I definitely want to knock it down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PUnderstood\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5P── Young.\x01",
            "It seems that it was peeled off.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(8380, 11000, 154390, 1000)
    OP_93(0x20, 0x13B, 0x1F4)
    OP_6F(0x1)
    Sound(947, 0, 100, 0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x20,
        (
            "#11P#4SStop operation!\x01",
            "Withdraw to point D!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("R-right!")

    AnonymousTalk(
        0xFF,
        "#4SYa, okay#4RYa#It is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x32, 1, 0, 141)
    StopSound(863, 1000, 40)
    Fade(500)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x2)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x2)
    SetChrChipByIndex(0x11, 0x60)
    SetChrSubChip(0x11, 0x1)
    SetChrChipByIndex(0x12, 0x60)
    SetChrSubChip(0x12, 0x1)
    SetChrChipByIndex(0x13, 0x60)
    SetChrSubChip(0x13, 0x1)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x15, 11300, 8000, 21350, 0)
    SetChrPos(0x16, 22150, 12000, 20940, 315)
    SetChrPos(0x17, 19200, 12000, 19100, 0)
    SetChrPos(0x18, 13500, 8000, 23700, 315)
    SetChrPos(0x19, 16850, 8000, 23000, 315)
    SetChrPos(0x1A, 8300, 8000, 19300, 45)
    SetChrPos(0x25, 13500, 8000, 25150, 315)
    SetChrPos(0x26, 14450, 12000, 18100, 0)
    SetChrPos(0x27, 17600, 12000, 30300, 180)
    SetChrPos(0x28, 13900, 12000, 33350, 225)
    SetChrPos(0x29, 8950, 12000, 36650, 180)
    SetChrPos(0x2A, 13650, 8000, 28530, 180)
    SetChrPos(0x2B, 14150, 16000, 38400, 180)
    SetChrPos(0xD, 14050, 12000, 31950, 225)
    SetChrPos(0xE, 11100, 12000, 35250, 180)
    SetChrPos(0xF, 17700, 16000, 36750, 225)
    SetChrPos(0x11, 15950, 8000, 26850, 225)
    SetChrPos(0x12, 16050, 12000, 30400, 180)
    SetChrPos(0x13, 18250, 8000, 24600, 270)
    SetChrPos(0x1E, 12100, 16000, 39450, 180)
    OP_11(0xFF, 0xFF, 0xFF, 0x1E, 0x1F4, 0x0)
    OP_68(13500, 16950, 33900, 0)
    MoveCamera(66, 20, 5, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    OP_68(13500, 14950, 33900, 5000)
    SetCameraDistance(22000, 5000)
    OP_0D()
    Sound(973, 0, 70, 0)
    BeginChrThread(0x27, 1, 0, 140)
    BeginChrThread(0x28, 1, 0, 140)
    BeginChrThread(0x29, 1, 0, 140)
    BeginChrThread(0x2A, 1, 0, 140)
    BeginChrThread(0x2B, 1, 0, 140)
    Sleep(4000)
    Fade(500)
    BeginChrThread(0x25, 1, 0, 123)
    BeginChrThread(0x18, 1, 0, 116)
    BeginChrThread(0x15, 1, 0, 110)
    BeginChrThread(0x19, 1, 0, 118)
    BeginChrThread(0x1A, 1, 0, 120)
    BeginChrThread(0x16, 1, 0, 112)
    BeginChrThread(0x17, 1, 0, 114)
    BeginChrThread(0x26, 1, 0, 124)
    OP_68(12380, 9100, 24480, 0)
    MoveCamera(75, 15, 0, 0)
    SetCameraDistance(20000, 0)
    OP_68(15030, 8500, 24830, 8000)
    MoveCamera(65, 20, 5, 8000)
    SetCameraDistance(35000, 8000)
    Sound(973, 0, 60, 0)
    Sleep(6000)
    StopSound(974, 2000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x25, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x26, 0x1)
    EndChrThread(0x27, 0x1)
    EndChrThread(0x28, 0x1)
    EndChrThread(0x29, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x2B, 0x1)
    OP_11(0xFF, 0xFF, 0xFF, 0x1E, 0x96, 0x0)
    StopBGM(0x1770)
    WaitBGM()
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrPos(0x101, -13100, 0, 138500, 270)
    SetChrPos(0x103, -12250, 0, 137300, 270)
    SetChrPos(0x104, -19350, 4000, 152500, 180)
    SetChrPos(0x105, -13100, 0, 138500, 270)
    SetChrPos(0x106, -12250, 0, 137300, 270)
    SetChrPos(0x107, -11100, 0, 138500, 270)
    SetChrPos(0x1E, -26650, 0, 131150, 45)
    SetChrPos(0x1F, -19350, 4000, 152500, 180)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7569", 0)
    OP_68(-19350, 5000, 152500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_68(-20250, 1000, 142000, 5000)
    MoveCamera(45, 25, 0, 5000)
    SetCameraDistance(19000, 5000)

    def lambda_10959():
        OP_95(0xFE, -20250, 0, 142650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10959)
    FadeToBright(1000, 0)
    Sleep(3000)
    BeginChrThread(0x101, 1, 0, 104)
    Sleep(200)
    BeginChrThread(0x103, 1, 0, 105)
    Sleep(500)
    BeginChrThread(0x105, 1, 0, 106)
    Sleep(300)
    BeginChrThread(0x106, 1, 0, 107)
    Sleep(300)
    BeginChrThread(0x107, 1, 0, 108)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x101,
        "#00014F#12PRandy …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00214F#11P…… Randy!\x02",
    )

    WaitChrThread(0x106, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)
    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    Sound(2364, 255, 100, 0)

    AnonymousTalk(
        0x104,
        (
            "Good morning.\x02\x03",
            "No way, you\x01",
            "I do not think you will come here …\x02\x03",
            "Lloyd, Tio Sukei.\x01",
            "It was really safe and nice.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        "#00002F#12POh, Randy ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PEscape … were you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#5POh, after somehow escaping with self,\x01",
            "You can join with Mireille.\x02\x03",
            "#00301FUntil now, in this part of the area\x01",
            "I was doing a resistance … ….\x02\x03",
            "#00306FAs expected, this time\x01",
            "I thought it was the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PI see……\x01",
            "It was really safe and good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PMr. Zeit's men\x01",
            "Thanks.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x107, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00304F#6POh, when I get on with this thing\x01",
            "He suddenly helped me.\x02\x03",
            "#00302FPossibly\x01",
            "Did you call it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3CWell, just in case.\x02\x03",
            "#01200FAnd the movements of the soldiers and the hunters\x01",
            "I was telling you to be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PWell, I see. ….\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        (
            "#00307F#6P#4SWell, yeah! Is it?\x02\x03",
            "#4SWhy are you talking! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#12Pmy mother……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PWell, you are surprised.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0x104, 0x105, 500)
    Sleep(500)
    TurnDirection(0x104, 0x106, 500)

    ChrTalk(
        0x104,
        (
            "#00305F#5PIf you look closely\x01",
            "Wadi is also dressed like that … …\x02\x03",
            "#00307FAnd Lisa-chan! Is it?\x01",
            "Why are you with the Lloyds! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#6PWhew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10709F#12PCouscous……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1E, 0x80)

    NpcTalk(
        0x1E,
        "Female voice",
        "#5PRandy!\x02",
    )

    OP_64(0x104)
    CloseMessageWindow()
    Fade(500)
    OP_68(-26650, 1000, 131150, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(-21000, 1000, 141150, 2000)
    MoveCamera(40, 20, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(21000, 2000)
    SetChrPos(0x107, -18250, 0, 142700, 0)
    SetChrChipByIndex(0x1E, 0x26)

    def lambda_10FB8():
        OP_96(0x1E, 0xFFFFA84E, 0x0, 0x22024, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_10FB8)

    def lambda_10FD2():
        OP_92(0x101, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10FD2)
    Sleep(0)

    def lambda_10FE8():
        OP_92(0x103, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10FE8)
    Sleep(0)

    def lambda_10FFE():
        OP_92(0x104, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10FFE)
    Sleep(0)

    def lambda_11014():
        OP_92(0x105, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11014)
    Sleep(0)

    def lambda_1102A():
        OP_92(0x106, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1102A)
    Sleep(0)

    def lambda_11040():
        OP_92(0x107, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_11040)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    WaitChrThread(0x1E, 1)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1E,
        (
            "I confirmed the withdrawal of enemy troops safely.\x02\x03",
            "With this,\x01",
            "It will endure for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x104,
        "#00302F#5PReally……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PMireilleu, it's been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#11PIt was safe and the best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#07904F#6PYou also ….\x01",
            "It was nice to be safe.\x02\x03",
            "#07902F… … somewhat with individual persons\x01",
            "It looks like it's together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PWell, there is circumstance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#5PTake a breath for the time being\x01",
            "I want to exchange information.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x80)
    FadeToDark(0, 16777215, -1)
    Sound(810, 0, 100, 0)
    OP_0D()
    Sleep(100)
    FadeToBright(650, 16777215)
    OP_0D()

    NpcTalk(
        0x1F,
        "Female voice",
        "#4PYes, I agree!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-21250, 1800, 140800, 3000)
    MoveCamera(35, 20, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(22000, 3000)

    def lambda_11372():
        OP_95(0xFE, -19850, 450, 144900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_11372)

    def lambda_1138C():
        OP_92(0x101, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1138C)
    Sleep(50)

    def lambda_113A2():
        OP_92(0x103, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_113A2)
    Sleep(50)

    def lambda_113B8():
        OP_92(0x104, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_113B8)
    Sleep(50)

    def lambda_113CE():
        OP_92(0x105, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_113CE)
    Sleep(50)

    def lambda_113E4():
        OP_92(0x106, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_113E4)
    Sleep(50)

    def lambda_113FA():
        OP_92(0x107, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_113FA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    WaitChrThread(0x1F, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011F#12PGood, Grace! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12PWhy are you here …?\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 4000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    OP_96(0x1F, 0xFFFFB65E, 0x1C2, 0x23604, 0x7D0, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    Sleep(50)
    Sound(810, 0, 100, 0)
    PlayEffect(0x8, 0xFF, 0x1F, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    OP_96(0x1F, 0xFFFFAE8E, 0x1C2, 0x23604, 0x7D0, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    Sleep(50)
    Sound(810, 0, 100, 0)
    PlayEffect(0x8, 0xFF, 0x1F, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    OP_96(0x1F, 0xFFFFB276, 0x1C2, 0x23604, 0x7D0, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    Sleep(50)
    Sound(810, 0, 100, 0)
    PlayEffect(0x8, 0xFF, 0x1F, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x1F,
        (
            "Yea ~, I got a problem a little\x01",
            "I got hot in the crossbell city.\x02\x03",
            "So as a serving reporter and a photographer\x01",
            "Randy pushed you guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x1E,
        (
            "#07906F#6P#NHaa … … I would like to welcome you less\x01",
            "I do not have it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00309F#5PHa ha, that kind of stuff.\x02\x03",
            "#00300FApparently each other, until now\x01",
            "It seems necessary to explain.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19370, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x6E)
    OP_24(0x3CE)
    OP_24(0x361)
    OP_24(0x35F)
    OP_24(0x35D)
    SetScenarioFlags(0x22, 4)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_103_EF51 end

    def Function_104_117AC(): pass

    label("Function_104_117AC")

    OP_95(0xFE, -20250, 0, 141150, 5000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_104_117AC end

    def Function_105_117C8(): pass

    label("Function_105_117C8")

    OP_95(0xFE, -18900, 0, 141140, 5000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_105_117C8 end

    def Function_106_117E4(): pass

    label("Function_106_117E4")

    OP_95(0xFE, -22600, 0, 140700, 3000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_106_117E4 end

    def Function_107_11800(): pass

    label("Function_107_11800")

    OP_95(0xFE, -20400, 0, 139200, 3000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_107_11800 end

    def Function_108_1181C(): pass

    label("Function_108_1181C")

    OP_95(0xFE, -17750, 0, 142700, 3000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_108_1181C end

    def Function_109_1183C(): pass

    label("Function_109_1183C")

    Sleep(3000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x3CF0, 0x3E80, 0x943E, 0x1F4, 0x1388)
    Sound(326, 0, 50, 0)
    OP_95(0xFE, 17500, 16000, 35950, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x4556, 0x2EE0, 0x7D31, 0x1F4, 0x1388)
    Sound(326, 0, 50, 0)
    OP_95(0xFE, 18350, 12000, 28550, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_82(0x0, 0x64, 0xBB8, 0x3E8)
    SetChrChipByIndex(0xFE, 0x35)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(1000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    StopSound(865, 500, 40)
    StopSound(861, 500, 40)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 50, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_109_1183C end

    def Function_110_11941(): pass

    label("Function_110_11941")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sleep(2000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    OP_95(0xFE, 11800, 8000, 25000, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 50, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_110_11941 end

    def Function_111_119B6(): pass

    label("Function_111_119B6")

    Sleep(2000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x348A, 0x3E80, 0xA50A, 0x1F4, 0x1388)
    OP_95(0xFE, 14000, 16000, 38300, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x3BF6, 0x2EE0, 0x83D6, 0x1F4, 0x1388)
    OP_95(0xFE, 16250, 12000, 30050, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_82(0x0, 0x64, 0xBB8, 0x7D0)
    SetChrChipByIndex(0xFE, 0x35)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(2000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_111_119B6 end

    def Function_112_11A91(): pass

    label("Function_112_11A91")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sleep(6000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x4BFA, 0x1F40, 0x59D8, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 12400, 8000, 26250, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_112_11A91 end

    def Function_113_11B21(): pass

    label("Function_113_11B21")

    Sleep(1000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x299A, 0x3E80, 0xAA82, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 10950, 16000, 40000, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x3070, 0x2EE0, 0x8CA0, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 13850, 12000, 32100, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sound(865, 2, 50, 0)
    Sound(861, 2, 50, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x7D0)
    SetChrChipByIndex(0xFE, 0x35)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 50)
    Sleep(2000)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_113_11B21 end

    def Function_114_11C26(): pass

    label("Function_114_11C26")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sleep(7000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x474A, 0x1F40, 0x574E, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 11800, 8000, 25000, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_114_11C26 end

    def Function_115_11CBC(): pass

    label("Function_115_11CBC")

    Sleep(2500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x3CF0, 0x3E80, 0x943E, 0x1F4, 0x1388)
    OP_95(0xFE, 17500, 16000, 35950, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x4556, 0x2EE0, 0x7D31, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 17350, 12000, 29450, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_115_11CBC end

    def Function_116_11D71(): pass

    label("Function_116_11D71")

    SetChrChipByIndex(0xFE, 0x5B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    OP_95(0xFE, 11800, 8000, 25000, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_116_11D71 end

    def Function_117_11DE6(): pass

    label("Function_117_11DE6")

    Sleep(3500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x348A, 0x3E80, 0xA50A, 0x1F4, 0x1388)
    OP_95(0xFE, 12850, 16000, 39150, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x3BF6, 0x2EE0, 0x83D6, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 17350, 12000, 29450, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_117_11DE6 end

    def Function_118_11E89(): pass

    label("Function_118_11E89")

    SetChrChipByIndex(0xFE, 0x5B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(3000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    OP_95(0xFE, 12400, 8000, 26250, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_118_11E89 end

    def Function_119_11EFE(): pass

    label("Function_119_11EFE")

    Sleep(1500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x299A, 0x3E80, 0xAA82, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 9000, 16000, 40400, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x3070, 0x2EE0, 0x8CA0, 0x1F4, 0x1388)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 17350, 12000, 29450, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_119_11EFE end

    def Function_120_11FA7(): pass

    label("Function_120_11FA7")

    SetChrChipByIndex(0xFE, 0x5B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(4000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5A)
    OP_95(0xFE, 11800, 8000, 25000, 4000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 100, 0)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    Sound(326, 0, 30, 0)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_120_11FA7 end

    def Function_121_1201C(): pass

    label("Function_121_1201C")

    Sleep(500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x6)
    OP_9D(0xFE, 0x4204, 0x3E80, 0x9C72, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 14650, 16000, 38300, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrSubChip(0xFE, 0x6)
    OP_9D(0xFE, 0x4556, 0x2EE0, 0x7D31, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 17350, 12000, 29450, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_121_1201C end

    def Function_122_120E0(): pass

    label("Function_122_120E0")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x6)
    OP_9D(0xFE, 0x15AE, 0x3E80, 0xAAE6, 0x1F4, 0x1388)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 7700, 16000, 40750, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 70, 0)
    OP_9D(0xFE, 0x27A6, 0x2EE0, 0x8D68, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 12250, 12000, 33250, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(809, 0, 60, 0)
    OP_9D(0xFE, 0x34EE, 0x1F40, 0x7116, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_122_120E0 end

    def Function_123_121A0(): pass

    label("Function_123_121A0")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1F)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 12400, 8000, 26250, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 60, 0)
    OP_9D(0xFE, 0x2486, 0xFA0, 0x70E4, 0x1F4, 0xFA0)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 3350, 4000, 34900, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_123_121A0 end

    def Function_124_1221E(): pass

    label("Function_124_1221E")

    Sleep(5000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1F)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 14450, 12000, 19000, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x6)
    OP_9D(0xFE, 0x37AA, 0x1F40, 0x587A, 0x1F4, 0xFA0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 11800, 8000, 25000, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x6)
    OP_9D(0xFE, 0x238C, 0xFA0, 0x6B08, 0x1F4, 0xFA0)
    BeginChrThread(0xFE, 0, 0, 56)
    OP_95(0xFE, 2950, 4000, 33550, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_124_1221E end

    def Function_125_122CC(): pass

    label("Function_125_122CC")

    Sleep(6500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x2FA8, 0x3E80, 0xA730, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 12100, 16000, 39450, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    SetChrSubChip(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_125_122CC end

    def Function_126_1232E(): pass

    label("Function_126_1232E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1237D")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x3)
    Jump("Function_126_1232E")

    label("loc_1237D")

    Return()

    # Function_126_1232E end

    def Function_127_1237E(): pass

    label("Function_127_1237E")

    Sleep(7000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x4)
    Sound(809, 0, 40, 0)
    OP_9D(0xFE, 0x49A2, 0x3E80, 0x940C, 0x1F4, 0x1388)
    OP_95(0xFE, 17250, 16000, 36300, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x3B92, 0x2EE0, 0x8340, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 14050, 12000, 31950, 5000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 126)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_127_1237E end

    def Function_128_1241D(): pass

    label("Function_128_1241D")

    Sleep(7500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 40, 0)
    OP_9D(0xFE, 0x2710, 0x3E80, 0xAB7C, 0x1F4, 0x1388)
    OP_95(0xFE, 10450, 16000, 39900, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x2A94, 0x2EE0, 0x90BA, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 11100, 12000, 35250, 5000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 126)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_128_1241D end

    def Function_129_124BC(): pass

    label("Function_129_124BC")

    Sleep(8500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 40, 0)
    OP_9D(0xFE, 0x3FDE, 0x3E80, 0x9F92, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 17700, 16000, 36750, 5000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    BeginChrThread(0xFE, 0, 0, 49)
    BeginChrThread(0xFE, 3, 0, 126)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_129_124BC end

    def Function_130_1252C(): pass

    label("Function_130_1252C")

    Sleep(9000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5F)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x49A2, 0x4E20, 0x9218, 0x1F4, 0x1388)
    Sound(326, 0, 10, 0)
    OP_95(0xFE, 18850, 16000, 36250, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x44C0, 0x2EE0, 0x82DC, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 16600, 12000, 29850, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x410A, 0x1F40, 0x65C2, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    TurnDirection(0xFE, 0x18, 500)
    SetChrChipByIndex(0xFE, 0x60)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x18, 0xFE, 500)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0xFE, 0x20)

    label("loc_125F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12672")

    def lambda_12604():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_12604)
    SetChrChipByIndex(0x18, 0x5D)

    def lambda_1261D():
        OP_A0(0xFE, 2000, 0x0, 0x3)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_1261D)
    OP_9A(0x18, 0xFE, 0x3E8, 0x2710, 0x0)
    Sleep(1000)

    def lambda_1263B():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_1263B)
    SetChrChipByIndex(0xFE, 0x61)

    def lambda_12654():
        OP_A0(0xFE, 2000, 0x0, 0x4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_12654)
    OP_9A(0xFE, 0x18, 0x3E8, 0x2710, 0x0)
    Sleep(1000)
    Jump("loc_125F4")

    label("loc_12672")

    Return()

    # Function_130_1252C end

    def Function_131_12673(): pass

    label("Function_131_12673")

    Sleep(9500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5F)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x3CF0, 0x3E80, 0x943E, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 17500, 16000, 35950, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x4556, 0x2EE0, 0x7D31, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 16050, 12000, 30400, 5000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x60)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_131_12673 end

    def Function_132_12710(): pass

    label("Function_132_12710")

    Sleep(10000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x5F)
    SetChrSubChip(0xFE, 0x4)
    OP_9D(0xFE, 0x48A8, 0x3E80, 0x9A4C, 0x1F4, 0x1388)
    OP_95(0xFE, 18850, 16000, 36250, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x44C0, 0x2EE0, 0x82DC, 0x1F4, 0x1388)
    Sound(326, 0, 40, 0)
    OP_95(0xFE, 18750, 12000, 28900, 5000, 0x0)
    SetChrSubChip(0xFE, 0x4)
    Sound(541, 0, 50, 0)
    OP_9D(0xFE, 0x474A, 0x1F40, 0x6018, 0x1F4, 0x1388)
    TurnDirection(0xFE, 0x19, 500)
    SetChrChipByIndex(0xFE, 0x60)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x19, 0xFE, 500)
    SetChrChipByIndex(0xFE, 0x61)

    def lambda_127D7():
        OP_A0(0xFE, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_127D7)
    SetChrFlags(0xFE, 0x20)
    OP_9A(0xFE, 0x19, 0x3E8, 0x2710, 0x0)
    Sound(566, 0, 20, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x19, 0x5C)
    SetChrSubChip(0x19, 0x0)

    def lambda_1280A():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1280A)

    def lambda_12823():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_12823)
    Return()

    # Function_132_12710 end

    def Function_133_12838(): pass

    label("Function_133_12838")

    SetChrChipByIndex(0xFE, 0x65)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12852")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12869")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    Jump("loc_12852")

    label("loc_12869")

    Return()

    # Function_133_12838 end

    def Function_134_1286A(): pass

    label("Function_134_1286A")

    SetChrChipByIndex(0xFE, 0x64)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12884")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_128A2")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_12884")

    label("loc_128A2")

    Return()

    # Function_134_1286A end

    def Function_135_128A3(): pass

    label("Function_135_128A3")

    Sleep(4500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x4330, 0x3E80, 0x9E34, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 17050, 16000, 36600, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 134)
    Sleep(1000)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x4556, 0x2EE0, 0x7D31, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 17600, 12000, 30300, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 134)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_135_128A3 end

    def Function_136_12956(): pass

    label("Function_136_12956")

    Sleep(5000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x2B8E, 0x3E80, 0xABAE, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 11400, 16000, 39700, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 134)
    Sleep(1000)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x3BF6, 0x2EE0, 0x83D6, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 13900, 12000, 33350, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 134)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_136_12956 end

    def Function_137_12A10(): pass

    label("Function_137_12A10")

    Sleep(5500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 40, 0)
    OP_9D(0xFE, 0x3908, 0x3E80, 0xA442, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 14500, 16000, 38100, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 134)
    Sleep(1000)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x3070, 0x2EE0, 0x8CA0, 0x1F4, 0x1388)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 8950, 12000, 36650, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 134)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_137_12A10 end

    def Function_138_12ACA(): pass

    label("Function_138_12ACA")

    Sleep(6000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 40, 0)
    OP_9D(0xFE, 0x3C5A, 0x3E80, 0x9F92, 0x1F4, 0x1388)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 15750, 16000, 36400, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x3E3A, 0x2EE0, 0x7EC2, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 15100, 12000, 31250, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x3552, 0x1F40, 0x6F72, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    OP_93(0xFE, 0xB4, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 134)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_138_12ACA end

    def Function_139_12B94(): pass

    label("Function_139_12B94")

    Sleep(6500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x65)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x3746, 0x3E80, 0xA4A6, 0x1F4, 0x1388)
    Sound(845, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 133)
    OP_95(0xFE, 14150, 16000, 38400, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 134)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_139_12B94 end

    def Function_140_12BFE(): pass

    label("Function_140_12BFE")

    BeginChrThread(0xFE, 0, 0, 134)

    label("loc_12C04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12C5C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12C54")
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x66)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3)
    Return()

    label("loc_12C54")

    Sleep(1000)
    Jump("loc_12C04")

    label("loc_12C5C")

    Return()

    # Function_140_12BFE end

    def Function_141_12C5D(): pass

    label("Function_141_12C5D")

    Sound(974, 2, 20, 0)
    Sleep(200)
    OP_25(0x3CE, 0x1E)
    Sleep(200)
    OP_25(0x3CE, 0x28)
    Sleep(200)
    OP_25(0x3CE, 0x32)
    Sleep(200)
    OP_25(0x3CE, 0x3C)
    Sleep(200)
    OP_25(0x3CE, 0x46)
    Sleep(200)
    OP_25(0x3CE, 0x46)
    Return()

    # Function_141_12C5D end

    def Function_142_12C8E(): pass

    label("Function_142_12C8E")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('旧矿山的钥匙', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E89")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_12E0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D71")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door of the old mine is closed tightly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FIt is said that a magical beast was arranged at the former mine\x01",
            "I had a request … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt is better to consult with the mayor first\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_12E07")

    label("loc_12D71")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door of the old mine is closed tightly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FI ordered devils to appear\x01",
            "I had a request but …\x01",
            "I do not have a key.\x02\x03",
            "Let's consult with the Mayor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E07")

    Jump("loc_12E84")

    label("loc_12E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12E4F")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door of the old mine is closed tightly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_12E84")

    label("loc_12E4F")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door of the old mine is closed tightly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_12E84")

    Jump("loc_12F71")

    label("loc_12E89")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door of the old mine is closed tightly.\x02\x03",
            "With the spare key I borrowed from the town mayor\x01",
            "I can seem to be able to open it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Use keys\x01",      # 0
            "do not use\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F71")
    Sound(806, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The key of the door has come off.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x14F, 4)
    SetMapObjFlags(0x5, 0x10)
    OP_65(0x6, 0x1)
    Jump("loc_12F71")

    label("loc_12F71")

    TalkEnd(0xFF)
    Return()

    # Function_142_12C8E end

    SaveToFile()

Try(main)
