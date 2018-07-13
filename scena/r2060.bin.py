from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Miner Gantz",            # 1
        "ロッズ",                 # 2
        "ロッズ",                 # 3
        "鉄鋼ドリュー",           # 4
        "鉄鋼ドリュー",           # 5
        "CGF Member",             # 6
        "CGF Member",             # 7
        "CGF Member",             # 8
        "CGF Member",             # 9
        "CGF Member",             # 10
        "CGF Member",             # 11
        "CGF Member",             # 12
        "CGF Member",             # 13
        "Jaeger",                 # 14
        "Jaeger",                 # 15
        "Jaeger",                 # 16
        "Jaeger",                 # 17
        "Jaeger",                 # 18
        "Jaeger",                 # 19
        "Jaeger",                 # 20
        "Randy",                  # 21
        "Shirley",                # 22
        "2nd Lt. Mireille",       # 23
        "Grace",                  # 24
        "Jaeger Gareth",          # 25
        "クーガー",               # 26
        "クーガー",               # 27
        "クーガー",               # 28
        "クーガー",               # 29
        "クーガー",               # 30
        "クーガー",               # 31
        "Wolf",                   # 32
        "Wolf",                   # 33
        "Wolf",                   # 34
        "Wolf",                   # 35
        "Wolf",                   # 36
        "車",                     # 37
        "Armored Vehicle",        # 38
        "Armored Vehicle",        # 39
        "新型装甲車",             # 40
        "武器",                   # 41
        "武器",                   # 42
        "SE制御",                 # 43
        "br2060",                 # 44
        "br2060",                 # 45
        "br2060",                 # 46
        "br2060",                 # 47
        "br2060",                 # 48
        "br2060",                 # 49
        "br2060",                 # 50
        "br2061",                 # 51
        "To Crossbell City",      # 52
        "To Mining Town Mainz",   # 53
    ))

    ATBonus("ATBonus_A34", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A54", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_13943", 0,   6,   2,   1,   3,   3,   0)
    Sepith("Sepith_1396B", 0,   0,   0,   5,   5,   5,   3)
    Sepith("Sepith_1392B", 0,   7,   2,   0,   1,   0,   4)
    Sepith("Sepith_13963", 11,  3,   6,   4,   6,   10,  8)

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
        "BattleInfo_CE4", 0x0000, 53, 6, 45, 10, 1, 50, 0, "br2060", "Sepith_13943", 30, 40, 20, 10,
        (
            ("ms64400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
        )
    )

    BattleInfo(
        "BattleInfo_B54", 0x0000, 53, 6, 45, 10, 1, 30, 0, "br2060", "Sepith_1396B", 30, 40, 20, 10,
        (
            ("ms71700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms71700.dat", "ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
        )
    )

    BattleInfo(
        "BattleInfo_C1C", 0x0000, 53, 6, 45, 10, 1, 25, 0, "br2060", "Sepith_1392B", 30, 40, 20, 10,
        (
            ("ms65900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A94", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_A74", "MonsterBattlePostion_AF4", "ed7450", "ed7453", "ATBonus_A34"),
        )
    )

    BattleInfo(
        "BattleInfo_DAC", 0x0000, 81, 6, 45, 6, 1, 30, 0, "br2060", "Sepith_13963", 40, 35, 25, 0,
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

    PlaceName(-3.0, 0.0, -15.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(87.0, 6.0, 122.0, 0x0000, 0x0000, "To Mining Town Mainz")

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
        "Function_6_2273",         # 06, 6
        "Function_7_23C5",         # 07, 7
        "Function_8_2517",         # 08, 8
        "Function_9_2875",         # 09, 9
        "Function_10_2BD3",        # 0A, 10
        "Function_11_2BF6",        # 0B, 11
        "Function_12_2DAC",        # 0C, 12
        "Function_13_34C4",        # 0D, 13
        "Function_14_34EC",        # 0E, 14
        "Function_15_3826",        # 0F, 15
        "Function_16_383D",        # 10, 16
        "Function_17_3AAB",        # 11, 17
        "Function_18_3B11",        # 12, 18
        "Function_19_3B1C",        # 13, 19
        "Function_20_3B7A",        # 14, 20
        "Function_21_3C08",        # 15, 21
        "Function_22_3D1C",        # 16, 22
        "Function_23_3D8C",        # 17, 23
        "Function_24_3F09",        # 18, 24
        "Function_25_3F7C",        # 19, 25
        "Function_26_3F91",        # 1A, 26
        "Function_27_40AE",        # 1B, 27
        "Function_28_4110",        # 1C, 28
        "Function_29_5561",        # 1D, 29
        "Function_30_5677",        # 1E, 30
        "Function_31_5794",        # 1F, 31
        "Function_32_57E0",        # 20, 32
        "Function_33_583A",        # 21, 33
        "Function_34_5880",        # 22, 34
        "Function_35_58CC",        # 23, 35
        "Function_36_591F",        # 24, 36
        "Function_37_596C",        # 25, 37
        "Function_38_59B9",        # 26, 38
        "Function_39_5A0C",        # 27, 39
        "Function_40_5A4B",        # 28, 40
        "Function_41_972A",        # 29, 41
        "Function_42_9752",        # 2A, 42
        "Function_43_977A",        # 2B, 43
        "Function_44_97A2",        # 2C, 44
        "Function_45_97CA",        # 2D, 45
        "Function_46_97F2",        # 2E, 46
        "Function_47_982E",        # 2F, 47
        "Function_48_986A",        # 30, 48
        "Function_49_9892",        # 31, 49
        "Function_50_98C6",        # 32, 50
        "Function_51_9916",        # 33, 51
        "Function_52_9966",        # 34, 52
        "Function_53_99B6",        # 35, 53
        "Function_54_9A11",        # 36, 54
        "Function_55_9A5C",        # 37, 55
        "Function_56_9AB8",        # 38, 56
        "Function_57_9AEA",        # 39, 57
        "Function_58_9B1C",        # 3A, 58
        "Function_59_9B81",        # 3B, 59
        "Function_60_9BE3",        # 3C, 60
        "Function_61_9C30",        # 3D, 61
        "Function_62_9C81",        # 3E, 62
        "Function_63_9D1F",        # 3F, 63
        "Function_64_9D38",        # 40, 64
        "Function_65_9D51",        # 41, 65
        "Function_66_9D6A",        # 42, 66
        "Function_67_9D82",        # 43, 67
        "Function_68_9DED",        # 44, 68
        "Function_69_9E96",        # 45, 69
        "Function_70_9EA6",        # 46, 70
        "Function_71_9EBC",        # 47, 71
        "Function_72_9ED6",        # 48, 72
        "Function_73_D4FC",        # 49, 73
        "Function_74_D52A",        # 4A, 74
        "Function_75_D55E",        # 4B, 75
        "Function_76_D654",        # 4C, 76
        "Function_77_D688",        # 4D, 77
        "Function_78_D70D",        # 4E, 78
        "Function_79_D763",        # 4F, 79
        "Function_80_D824",        # 50, 80
        "Function_81_D87A",        # 51, 81
        "Function_82_D901",        # 52, 82
        "Function_83_D96B",        # 53, 83
        "Function_84_DA47",        # 54, 84
        "Function_85_DAB1",        # 55, 85
        "Function_86_DB53",        # 56, 86
        "Function_87_DBD1",        # 57, 87
        "Function_88_DC55",        # 58, 88
        "Function_89_DCA5",        # 59, 89
        "Function_90_DD6A",        # 5A, 90
        "Function_91_DDED",        # 5B, 91
        "Function_92_DE6A",        # 5C, 92
        "Function_93_DED3",        # 5D, 93
        "Function_94_DF3C",        # 5E, 94
        "Function_95_DF91",        # 5F, 95
        "Function_96_DFEC",        # 60, 96
        "Function_97_E011",        # 61, 97
        "Function_98_E036",        # 62, 98
        "Function_99_E451",        # 63, 99
        "Function_100_E60C",       # 64, 100
        "Function_101_F4F9",       # 65, 101
        "Function_102_F572",       # 66, 102
        "Function_103_F5EB",       # 67, 103
        "Function_104_12065",      # 68, 104
        "Function_105_12081",      # 69, 105
        "Function_106_1209D",      # 6A, 106
        "Function_107_120B9",      # 6B, 107
        "Function_108_120D5",      # 6C, 108
        "Function_109_120F5",      # 6D, 109
        "Function_110_121FA",      # 6E, 110
        "Function_111_1226F",      # 6F, 111
        "Function_112_1234A",      # 70, 112
        "Function_113_123DA",      # 71, 113
        "Function_114_124DF",      # 72, 114
        "Function_115_12575",      # 73, 115
        "Function_116_1262A",      # 74, 116
        "Function_117_1269F",      # 75, 117
        "Function_118_12742",      # 76, 118
        "Function_119_127B7",      # 77, 119
        "Function_120_12860",      # 78, 120
        "Function_121_128D5",      # 79, 121
        "Function_122_12999",      # 7A, 122
        "Function_123_12A59",      # 7B, 123
        "Function_124_12AD7",      # 7C, 124
        "Function_125_12B85",      # 7D, 125
        "Function_126_12BE7",      # 7E, 126
        "Function_127_12C37",      # 7F, 127
        "Function_128_12CD6",      # 80, 128
        "Function_129_12D75",      # 81, 129
        "Function_130_12DE5",      # 82, 130
        "Function_131_12F2C",      # 83, 131
        "Function_132_12FC9",      # 84, 132
        "Function_133_130F1",      # 85, 133
        "Function_134_13123",      # 86, 134
        "Function_135_1315C",      # 87, 135
        "Function_136_1320F",      # 88, 136
        "Function_137_132C9",      # 89, 137
        "Function_138_13383",      # 8A, 138
        "Function_139_1344D",      # 8B, 139
        "Function_140_134B7",      # 8C, 140
        "Function_141_13516",      # 8D, 141
        "Function_142_13547",      # 8E, 142
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221D")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x38E, 1)"), scpexpr(EXPR_END)), "loc_21A6")
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
    SetScenarioFlags(0x1E7, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_2218")

    label("loc_21A6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2218")

    Jump("loc_2267")

    label("loc_221D")

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

    label("loc_2267")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_2121 end

    def Function_6_2273(): pass

    label("Function_6_2273")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236F")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5B, 1)"), scpexpr(EXPR_END)), "loc_22F8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_236A")

    label("loc_22F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5B),
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

    label("loc_236A")

    Jump("loc_23B9")

    label("loc_236F")

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

    label("loc_23B9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_2273 end

    def Function_7_23C5(): pass

    label("Function_7_23C5")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C1")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_244A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_24BC")

    label("loc_244A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
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

    label("loc_24BC")

    Jump("loc_250B")

    label("loc_24C1")

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

    label("loc_250B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_23C5 end

    def Function_8_2517(): pass

    label("Function_8_2517")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26CF")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_26B0")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26AB")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_26A8")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_25CD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_25CD)
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
    Battle("BattleInfo_E48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A3")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_268A")
    Call(1, 5)
    Jump("loc_26A3")

    label("loc_268A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_26A0")
    Call(1, 4)
    Jump("loc_26A3")

    label("loc_26A0")

    Call(1, 3)

    label("loc_26A3")

    Jump("loc_26AB")

    label("loc_26A8")

    Call(1, 1)

    label("loc_26AB")

    Jump("loc_26C6")

    label("loc_26B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_26C6")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_26C6")

    TalkEnd(0xFF)
    Return()

    label("loc_26CF")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_285A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2855")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_2852")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2777():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2777)
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
    Battle("BattleInfo_E8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_284D")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2834")
    Call(1, 5)
    Jump("loc_284D")

    label("loc_2834")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_284A")
    Call(1, 4)
    Jump("loc_284D")

    label("loc_284A")

    Call(1, 3)

    label("loc_284D")

    Jump("loc_2855")

    label("loc_2852")

    Call(1, 1)

    label("loc_2855")

    Jump("loc_2870")

    label("loc_285A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_2870")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2870")

    TalkEnd(0xFF)
    Return()

    # Function_8_2517 end

    def Function_9_2875(): pass

    label("Function_9_2875")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A2D")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_2A0E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A09")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2A06")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_292B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_292B)
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
    Battle("BattleInfo_E48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A01")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_29E8")
    Call(1, 5)
    Jump("loc_2A01")

    label("loc_29E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_29FE")
    Call(1, 4)
    Jump("loc_2A01")

    label("loc_29FE")

    Call(1, 3)

    label("loc_2A01")

    Jump("loc_2A09")

    label("loc_2A06")

    Call(1, 1)

    label("loc_2A09")

    Jump("loc_2A24")

    label("loc_2A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2A24")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2A24")

    TalkEnd(0xFF)
    Return()

    label("loc_2A2D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_2BB8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB3")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2BB0")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2AD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2AD5)
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
    Battle("BattleInfo_E8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BAB")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B92")
    Call(1, 5)
    Jump("loc_2BAB")

    label("loc_2B92")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2BA8")
    Call(1, 4)
    Jump("loc_2BAB")

    label("loc_2BA8")

    Call(1, 3)

    label("loc_2BAB")

    Jump("loc_2BB3")

    label("loc_2BB0")

    Call(1, 1)

    label("loc_2BB3")

    Jump("loc_2BCE")

    label("loc_2BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_2BCE")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2BCE")

    TalkEnd(0xFF)
    Return()

    # Function_9_2875 end

    def Function_10_2BD3(): pass

    label("Function_10_2BD3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BF5")
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x40, 0x80)

    label("loc_2BF5")

    Return()

    # Function_10_2BD3 end

    def Function_11_2BF6(): pass

    label("Function_11_2BF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D49")

    ChrTalk(
        0xFE,
        (
            "This is the old abandoned mine entrance.\x01",
            "When you're ready, please do your investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...At any rate, for such a\x01",
            "solid lock to have been broken...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a feat that even us, who're\x01",
            "tempered daily, could never do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know who ever could've broken it...\x01",
            "If you're going in, be careful, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DA8")

    label("loc_2D49")


    ChrTalk(
        0xFE,
        (
            "This is the old abandoned mine entrance.\x01",
            "When you're ready, please do your investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA8")

    TalkEnd(0xFE)
    Return()

    # Function_11_2BF6 end

    def Function_12_2DAC(): pass

    label("Function_12_2DAC")

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

    def lambda_2E61():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E61)
    Sleep(50)

    def lambda_2E79():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E79)
    Sleep(50)

    def lambda_2E91():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2E91)
    Sleep(50)
    FadeToBright(1000, 0)

    def lambda_2EB2():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2EB2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#11PHey there, you've come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes. So it's here.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_68(-27470, 9000, 194940, 1500)
    MoveCamera(6, 20, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(16800, 1500)
    Sleep(200)

    def lambda_2F50():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F50)
    Sleep(100)

    def lambda_2F60():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F60)
    Sleep(100)

    def lambda_2F70():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2F70)
    Sleep(100)

    def lambda_2F80():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2F80)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00001F#6P#NThis is the gate that was broken...?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#12P#N...It really seems it was \x01",
            "cut off with something.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11PYeah, honestly, I can't really think it\x01",
            "can be done with a human's strength...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PSo, this is the old mine entrance.\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x9, 0x0, 0xFF, 0x0, -16500, 10100, 203350, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x32, 1, 0, 13)
    Sleep(200)

    def lambda_30D3():
        OP_93(0xFE, 0x2C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_30D3)
    Sleep(300)
    OP_68(-25180, 9700, 194680, 2000)
    MoveCamera(45, 4, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(14520, 2000)

    def lambda_3111():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3111)
    Sleep(100)

    def lambda_3121():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3121)
    Sleep(150)

    def lambda_3131():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3131)
    Sleep(100)

    def lambda_3141():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3141)
    Sleep(600)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x109,
        "#10105F#6P#NT-This light...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10304F#12P#NUh uh, quite the suspicious\x01",
            "atmosphere, eh?\x02\x03",
            "#10300FIt also seem that dangerous-looking\x01",
            "monsters are wandering about too.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00003F#6P#NYeah...\x02",
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

    def lambda_325C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_325C)
    Sleep(100)

    def lambda_326C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_326C)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00108F#11P...What do we do, Lloyd?\x02\x03",
            "#00101FDepending on the situation, I think we can\x01",
            "contact the CGF personnel too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PYou're right... That would increase\x01",
            "the investigation options too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_334A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_334A)
    Sleep(50)

    def lambda_335A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_335A)
    Sleep(50)

    def lambda_336A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_336A)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00003F#5P...No, first, we'll check\x01",
            "the situation inside.\x02\x03",
            "#00001FIn case it becomes impossible to do,\x01",
            "we'll request the CGF backup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#11PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PWell, in that case it would be\x01",
            "better to be fully prepared.\x02",
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

    # Function_12_2DAC end

    def Function_13_34C4(): pass

    label("Function_13_34C4")

    Sleep(2300)
    Sound(929, 0, 30, 0)
    Sound(828, 2, 50, 0)
    Sleep(2200)
    Sound(831, 0, 40, 0)
    Sleep(1500)
    Sound(948, 0, 30, 0)
    Sound(830, 0, 30, 0)
    Return()

    # Function_13_34C4 end

    def Function_14_34EC(): pass

    label("Function_14_34EC")

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
            "#00008F#5P(Perhaps, if we begin searching this place, we\x01",
            "won't be free to go to other places anymore.)\x02\x03",
            "#00001F(...What to do?)\x02",
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
            "[There's Still Other Things to Do]\x01",      # 0
            "[Step Inside the Old Mine]\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3669"),
        (1, "loc_3681"),
        (SWITCH_DEFAULT, "loc_3825"),
    )


    label("loc_3669")

    SetChrPos(0x0, -27820, 8000, 192000, 225)
    EventEnd(0x5)
    Jump("loc_3825")

    label("loc_3681")

    OP_4B(0x8, 0xFF)
    Sleep(100)

    def lambda_368D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_368D)
    Sleep(50)

    def lambda_369D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_369D)
    Sleep(50)

    def lambda_36AD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_36AD)
    Sleep(50)

    def lambda_36BD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_36BD)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#6PThen, Mr. Gantz.\x02\x03",
            "We'll go have a brief look inside,\x01",
            "so please, wait here for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYeah, be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you think it's dangerous,\x01",
            "come back immediately, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-23660, 8600, 196120, 2500)
    MoveCamera(44, 15, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(21380, 2500)

    def lambda_37B8():

        label("loc_37B8")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_37B8")

    QueueWorkItem2(0x8, 2, lambda_37B8)
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
    Jump("loc_3825")

    label("loc_3825")

    Return()

    # Function_14_34EC end

    def Function_15_3826(): pass

    label("Function_15_3826")

    OP_93(0xFE, 0x2D, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    Return()

    # Function_15_3826 end

    def Function_16_383D(): pass

    label("Function_16_383D")

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
        "#5PW-Whaaaaaaaaat!?\x02",
    )

    WaitChrThread(0x8, 3)
    CloseMessageWindow()
    OP_64(0x8)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 19)
    WaitChrThread(0x8, 3)

    ChrTalk(
        0x8,
        "#5PW-What the heck has...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#4S#5PHeeey!\x01",
            "You ok, guys!?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        "#4S#5PAnswer me if you hear me!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PI-It's no use...\x01",
            "It doesn't seem my voice reaches them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PA-Anyway, I must inform the others!\x02",
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

    # Function_16_383D end

    def Function_17_3AAB(): pass

    label("Function_17_3AAB")

    OP_9B(0x0, 0xFE, 0xF, 0x7D0, 0x1388, 0x1)
    BeginChrThread(0xFE, 2, 0, 18)
    OP_9B(0x1, 0xFE, 0x1E, 0x7D0, 0x1388, 0x1)
    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0x0, 0xFA, 0x3E8)
    OP_9C(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x32, 0x3E8)
    WaitChrThread(0xFE, 2)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    Return()

    # Function_17_3AAB end

    def Function_18_3B11(): pass

    label("Function_18_3B11")

    Sleep(50)
    OP_93(0xFE, 0x5A, 0x3E8)
    Return()

    # Function_18_3B11 end

    def Function_19_3B1C(): pass

    label("Function_19_3B1C")

    OP_9B(0x0, 0xFE, 0x159, 0x7D0, 0xFA0, 0x1)
    OP_68(-21150, 8600, 198420, 1000)
    MoveCamera(45, 8, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(24670, 1000)
    OP_9B(0x0, 0xFE, 0xF, 0xBB8, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x1F4, 0x7D0, 0x0)
    OP_6F(0x1)
    Return()

    # Function_19_3B1C end

    def Function_20_3B7A(): pass

    label("Function_20_3B7A")

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

    # Function_20_3B7A end

    def Function_21_3C08(): pass

    label("Function_21_3C08")

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

    # Function_21_3C08 end

    def Function_22_3D1C(): pass

    label("Function_22_3D1C")

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

    # Function_22_3D1C end

    def Function_23_3D8C(): pass

    label("Function_23_3D8C")

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

    # Function_23_3D8C end

    def Function_24_3F09(): pass

    label("Function_24_3F09")

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

    # Function_24_3F09 end

    def Function_25_3F7C(): pass

    label("Function_25_3F7C")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Return()

    # Function_25_3F7C end

    def Function_26_3F91(): pass

    label("Function_26_3F91")

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

    # Function_26_3F91 end

    def Function_27_40AE(): pass

    label("Function_27_40AE")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -13140, 200, 38660)
    OP_9F(0x1, -6650, 200, 32140)
    OP_9F(0x1, -1380, 200, 24520)
    OP_9F(0x1, -390, 200, 17010)
    OP_9F(0x1, -500, 200, -6130)
    OP_9F(0x1, -550, 400, -19760)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_27_40AE end

    def Function_28_4110(): pass

    label("Function_28_4110")

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
            "#1K1 hour before──",
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
    SetChrName("Voice from Communicator")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This is Headquarters──\x01",
            "A message to the 3rd Company.\x05\x02",
        )
    )

    Sleep(6500)
    Sound(471, 0, 100, 0)
    SetChrName("Voice from Communicator")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The armed group goal is unknown.\x05\x02",
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
    SetChrName("Voice from Communicator")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's highly possible it's the "Red Constellation"\x01",
            "jaeger corps that were hiding in the city.\x05\x02",
        )
    )

    Sleep(6750)
    SetChrName("Voice from Communicator")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Make your top priority that no damage\x01",
            "befall on the Mainz citizens.\x07\x00\x05\x02",
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
    SetChrName("Voice from Communicator")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "3rd Company, roger that.\x05\x02",
        )
    )

    Sleep(7000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As for the armed group, we'll──\x07\x00\x05\x02",
        )
    )

    WaitChrThread(0x2D, 3)
    OP_71(0xC, 0x79, 0x79, 0x0, 0x0)
    EndChrThread(0x2E, 0x3)

    def lambda_47AC():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_47AC)

    def lambda_47C1():
        OP_D5(0xFE, 0x0, 0x1ADB0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_47C1)
    OP_74(0xD, 0xF)
    OP_71(0xD, 0x5B, 0x78, 0x0, 0x8)
    EndChrThread(0x2F, 0x3)

    def lambda_47EE():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_47EE)
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
    SetChrName("Voice from Communicator")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An orbal mine...!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("Voice from Communicator")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3ADamn, all personnel, battle stations──\x07\x00\x02",
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
        "Girl's Voice",
        (
            "#35A#3953V#30WAhaha...\x01",
            "Not a bad reaction at all.\x02",
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
            "Uh uh...\x01",
            "Has it been three months\x01",
            "since the last time?\x02\x03",
            "It seems I'll finally be able\x01",
            "to satisfy my "Testa-Rossa"♪\x02",
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
        "Kh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "W-Who the heck are they!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04602F#11P──Starting cleanup operation.\x01",
            "First, let's push them up to the tunnel.\x02\x03",
            "#04612FYou can slaughter all those who strike back㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(290, 30, -1, -1)
    SetChrName("Jaegers")
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    AnonymousTalk(
        0xFF,
        "#4SJaー!\x02",
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

    # Function_28_4110 end

    def Function_29_5561(): pass

    label("Function_29_5561")

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

    # Function_29_5561 end

    def Function_30_5677(): pass

    label("Function_30_5677")

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

    # Function_30_5677 end

    def Function_31_5794(): pass

    label("Function_31_5794")


    def lambda_5799():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5799)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0xD, 1)
    OP_95(0xD, -8350, 0, 134700, 4000, 0x0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_31_5794 end

    def Function_32_57E0(): pass

    label("Function_32_57E0")


    def lambda_57E5():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_57E5)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0xE, 1)
    OP_95(0xE, -14150, 0, 135000, 4000, 0x0)
    OP_95(0xE, -15650, 0, 137600, 4000, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x2)
    Return()

    # Function_32_57E0 end

    def Function_33_583A(): pass

    label("Function_33_583A")


    def lambda_583F():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_583F)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0xF, 1)
    OP_95(0xF, -8000, 0, 133000, 4000, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x2)
    Return()

    # Function_33_583A end

    def Function_34_5880(): pass

    label("Function_34_5880")


    def lambda_5885():
        OP_95(0xFE, -11800, 0, 134700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5885)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x10, 1)
    OP_95(0x10, -15400, 0, 134000, 4000, 0x0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x2)
    Return()

    # Function_34_5880 end

    def Function_35_58CC(): pass

    label("Function_35_58CC")


    def lambda_58D1():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_58D1)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x11, 1)
    OP_95(0x11, -20920, 0, 132340, 4000, 0x0)
    OP_93(0x11, 0x46, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x2)
    Return()

    # Function_35_58CC end

    def Function_36_591F(): pass

    label("Function_36_591F")


    def lambda_5924():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5924)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x12, 1)
    OP_95(0x12, -25270, 0, 136260, 4000, 0x0)
    OP_93(0x12, 0x46, 0x1F4)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x2)
    Return()

    # Function_36_591F end

    def Function_37_596C(): pass

    label("Function_37_596C")


    def lambda_5971():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5971)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x13, 1)
    OP_95(0x13, -24450, 0, 131530, 4000, 0x0)
    OP_93(0x13, 0x46, 0x1F4)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x2)
    Return()

    # Function_37_596C end

    def Function_38_59B9(): pass

    label("Function_38_59B9")


    def lambda_59BE():
        OP_95(0xFE, -25200, 0, 132750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_59BE)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    WaitChrThread(0x14, 1)
    OP_95(0x14, -26170, 0, 133270, 4000, 0x0)
    OP_93(0x14, 0x46, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x2)
    Return()

    # Function_38_59B9 end

    def Function_39_5A0C(): pass

    label("Function_39_5A0C")

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

    # Function_39_5A0C end

    def Function_40_5A4B(): pass

    label("Function_40_5A4B")

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

    def lambda_5CA0():
        OP_95(0x1C, -10150, 4000, 151000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5CA0)
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

    def lambda_5E14():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5E14)

    def lambda_5E29():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5E29)

    def lambda_5E3E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5E3E)

    def lambda_5E53():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5E53)

    def lambda_5E68():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5E68)

    def lambda_5E7D():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5E7D)

    def lambda_5E92():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5E92)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    PlayEffect(0x1, 0x0, 0x1A, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(861, 2, 80, 0)
    WaitChrThread(0x1A, 1)
    SetChrChipByIndex(0x1A, 0x35)
    BeginChrThread(0x1A, 3, 0, 62)

    ChrTalk(
        0x1A,
        "#10A#5PArgh...!\x02",
    )

    WaitChrThread(0x1B, 1)
    SetChrChipByIndex(0x1B, 0x35)
    BeginChrThread(0x1B, 3, 0, 62)

    ChrTalk(
        0x1B,
        "#10A#6PUwooh...!?\x02",
    )

    StopEffect(0x0, 0x2)
    OP_24(0x35D)
    StopSound(291, 500, 80)
    StopSound(580, 500, 50)
    WaitChrThread(0x15, 1)

    def lambda_5F51():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5F51)
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

    def lambda_5FA6():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5FA6)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5FCE():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_5FCE)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5FF3():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_5FF3)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_601B():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_601B)
    Sleep(50)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6043():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_6043)
    Sleep(1000)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 2)
    WaitChrThread(0x17, 2)
    WaitChrThread(0x18, 2)
    WaitChrThread(0x19, 2)

    ChrTalk(
        0x16,
        "#11PWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#4P...No way!\x01",
            "Captain Randolph!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    ChrTalk(
        0x15,
        (
            "#2PDeploy!\x01",
            "Don't stay still on the same place!\x02",
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
        "#00314F#2761V#5P#8A#30WSlooow──\x02",
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

    def lambda_652C():
        OP_96(0xFE, 0xFFFFFF06, 0x0, 0x2049A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_652C)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    SetChrFlags(0x16, 0x20)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x1)

    def lambda_655B():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0x21F8E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_655B)
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

    def lambda_65BA():
        OP_96(0xFE, 0xFFFFE638, 0x0, 0x2130E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_65BA)
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
        "#10A#6PUwoooh!?\x02",
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
        "#6PNothing less to be expected from the Captain...!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    TurnDirection(0x15, 0x19, 500)

    ChrTalk(
        0x15,
        (
            "Hmph!\x01",
            "Send the Cougars!\x02",
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

    def lambda_681E():

        label("loc_681E")

        TurnDirection(0xFE, 0x21, 1000)
        Yield()
        Jump("loc_681E")

    QueueWorkItem2(0x1C, 2, lambda_681E)
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

    def lambda_6891():

        label("loc_6891")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_6891")

    QueueWorkItem2(0x21, 2, lambda_6891)
    BeginChrThread(0x21, 0, 0, 57)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)

    def lambda_68B5():

        label("loc_68B5")

        TurnDirection(0xFE, 0x22, 1000)
        Yield()
        Jump("loc_68B5")

    QueueWorkItem2(0x1C, 2, lambda_68B5)
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

    def lambda_6928():

        label("loc_6928")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_6928")

    QueueWorkItem2(0x22, 2, lambda_6928)
    BeginChrThread(0x22, 0, 0, 57)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)

    def lambda_694C():

        label("loc_694C")

        TurnDirection(0xFE, 0x23, 1000)
        Yield()
        Jump("loc_694C")

    QueueWorkItem2(0x1C, 2, lambda_694C)
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

    def lambda_69BF():

        label("loc_69BF")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_69BF")

    QueueWorkItem2(0x23, 2, lambda_69BF)
    BeginChrThread(0x23, 0, 0, 57)
    EndChrThread(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x48)
    SetChrSubChip(0x1C, 0x0)

    def lambda_69E3():

        label("loc_69E3")

        TurnDirection(0xFE, 0x24, 1000)
        Yield()
        Jump("loc_69E3")

    QueueWorkItem2(0x1C, 2, lambda_69E3)
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

    def lambda_6A56():

        label("loc_6A56")

        TurnDirection(0xFE, 0x1C, 1000)
        Yield()
        Jump("loc_6A56")

    QueueWorkItem2(0x24, 2, lambda_6A56)
    BeginChrThread(0x24, 0, 0, 57)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1C,
        "#00312F#2762V#12P#16A#30WHah...as if this worked.\x02",
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

    def lambda_6AE9():
        OP_96(0xFE, 0x3746, 0x1770, 0x236FE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6AE9)
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

    def lambda_6EBD():
        OP_96(0xFE, 0x14B4, 0x1770, 0x24252, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6EBD)
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

    def lambda_7042():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_7042)

    def lambda_7053():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 3, lambda_7053)

    def lambda_7064():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_7064)

    def lambda_7075():
        OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_7075)
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
        "#11POoh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#5PT-The Crimson Reaper...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x19, 500)

    ChrTalk(
        0x15,
        (
            "Don't cower!\x01",
            "Attack him in waves!\x02",
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

    def lambda_719E():
        OP_95(0xFE, -14850, 0, 140200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_719E)
    Sleep(100)
    SetChrChipByIndex(0x17, 0x33)

    def lambda_71BF():
        OP_95(0xFE, -14850, 10, 139000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_71BF)
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
        "#00011F#5PA-Amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5PO-Overwhelming...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#5PImpressive...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#5PThose're senior's Randy\x01",
            "true fighting abilities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5POh boy, I guess that he\x01",
            "didn't need assistance...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10301F#5P──No. Things seem\x01",
            "a bit dangerous now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#5PWhat...!?\x02",
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
        "Girl's Voice",
        (
            "#3954V#6P#25A#30WAhaha!\x01",
            "You're in top form, Randy bro!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1C, 0x1D, 500)

    ChrTalk(
        0x1C,
        "#00311F#2763V#6P#15A#30W...Shirley!?\x02",
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
            "#04612F#5PYes, yes, Randy bro\x01",
            "has to be like that!\x02\x03",
            "#04602FYou're different from my favorite\x01",
            "types, but you're cool!\x02",
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
            "#00311F#12PShut it...you damn little girl.\x02\x03",
            "I'll never want a man-eating\x01",
            "tiger like you...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04612F#6PUh uh, how cold!\x02\x03",
            "#04602FBut since we're here, let\x01",
            "Shirley have a little more fun!\x02",
        )
    )

    CloseMessageWindow()
    Sound(291, 2, 100, 0)
    Sound(580, 2, 70, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    SetChrChipByIndex(0x1C, 0x47)
    BeginChrThread(0x1C, 3, 0, 52)

    def lambda_7B6C():

        label("loc_7B6C")

        TurnDirection(0xFE, 0x1D, 300)
        Yield()
        Jump("loc_7B6C")

    QueueWorkItem2(0x1C, 2, lambda_7B6C)
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

    def lambda_7DC3():

        label("loc_7DC3")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_7DC3")

    QueueWorkItem2(0x1C, 3, lambda_7DC3)
    Sleep(50)

    def lambda_7DE4():

        label("loc_7DE4")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_7DE4")

    QueueWorkItem2(0x1D, 3, lambda_7DE4)
    OP_0D()

    ChrTalk(
        0x1C,
        "#00310F#6PGh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04604F#11PUh uh... But as I thought, this is the\x01",
            "result for the time you spent inactive.\x02\x03",
            "#04611FYou're almost at your limit, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#00307F#6P"Testa-Rossa"...\x01",
            "Did you fully master it...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04609F#11P*cluckle*, I'm not the Shirley\x01",
            "of when you were teaching me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x1D,
        "#04602F#11P#10A#4SCan't you get that, jeez!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1D, 0x20)
    OP_68(-19300, 1190, 137780, 1500)

    def lambda_7F8A():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7F8A)

    def lambda_7F9F():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7F9F)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1D, 1)
    Sleep(500)
    OP_68(-19700, 1190, 137860, 1500)

    def lambda_7FD0():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7FD0)

    def lambda_7FE5():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7FE5)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1D, 1)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    Sound(3920, 255, 90, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x1D,
        (
            "#04612F#5S#11P#18AAhaha!\x01",
            "Gooooooo!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1D, 0x3)
    SetChrFlags(0x1C, 0x800)
    SetChrFlags(0x1D, 0x800)
    Sound(874, 0, 100, 0)

    def lambda_8062():
        OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_8062)
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

    def lambda_80FE():
        OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_80FE)
    EndChrThread(0x1D, 0x3)
    SetChrFlags(0x1D, 0x2)
    SetChrChipByIndex(0x1D, 0x2D)
    Sound(815, 0, 100, 0)
    OP_A1(0x1D, 0xDAC, 0x2, 0x0, 0x1)
    Sound(2764, 255, 100, 1)

    ChrTalk(
        0x1C,
        "#00313F#6P#10A#NGwarh...!\x02",
    )


    def lambda_8152():
        OP_A0(0xFE, 2000, 0x3, 0x4)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_8152)

    def lambda_815F():
        OP_9D(0xFE, 0xFFFFA740, 0x0, 0x214BC, 0x2EE, 0x2710)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_815F)

    def lambda_817C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_817C)
    Sound(880, 0, 80, 0)
    Sound(566, 0, 50, 0)
    ClearChrFlags(0x31, 0x80)

    def lambda_81A6():
        OP_9D(0xFE, 0xFFFFA7B8, 0xFFFFFF38, 0x20E5E, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_81A6)
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
            "#04606F#11PUhhm, with the way you're now, Randy bro,\x01",
            "I can't be satisfied, as I feared...\x02\x03",
            "#04611FOh, well.\x01",
            "I'll find myself a pricey\x01",
            "proper playmate㈱\x02",
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
        "#00311F#6P#NY-You...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1D,
        (
            "#04604F#11PUh uh, Randy bro, you\x01",
            "should rehabilitate at\x01",
            "papa's place for a while.\x02\x03",
            "#04602FWhen you get back your "sense", you'll\x01",
            "inherit the "War God" position at once.\x02\x03",
            "#04609FBut still, should Shirley get at least\x01",
            "one arm for herself this time?\x02",
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
        "#00310F#6P#NGh...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#3320V#4S#10ARandyyyyyyyyyyyyyy!!\x02",
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
        "#04605F#12PWhoops.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#00305F#12P#N...!?\x02",
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

    def lambda_8666():
        OP_9B(0x1, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8666)
    Sleep(50)

    def lambda_867E():
        OP_9B(0x1, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_867E)
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
            "#04612F#11PAhaha, nice one!\x02\x03",
            "#04602FThen, I'll refresh my\x01",
            "palate pronto and──\x02",
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

    def lambda_89CC():
        OP_95(0xFE, -16000, 0, 138600, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_89CC)
    OP_0D()
    Sound(2014, 255, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x101,
        "#00007F#4S#10A#5PUwooooooooooooo!\x02",
    )

    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x39)
    SetChrSubChip(0x101, 0x4)
    Sound(251, 0, 100, 0)

    def lambda_8A36():
        OP_9D(0xFE, 0xFFFFCE96, 0x0, 0x21214, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A36)
    WaitChrThread(0x101, 1)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x1D, 0x2C)
    SetChrSubChip(0x1D, 0x0)
    PlayEffect(0x9, 0xFF, 0x101, 0x3, -300, 800, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(566, 0, 70, 0)
    Sound(815, 0, 100, 0)
    Sound(862, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    def lambda_8ABD():

        label("loc_8ABD")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_8ABD")

    QueueWorkItem2(0x101, 3, lambda_8ABD)
    Sleep(50)

    def lambda_8ADE():

        label("loc_8ADE")

        OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_8ADE")

    QueueWorkItem2(0x1D, 3, lambda_8ADE)
    Sleep(500)
    Sleep(1000)

    ChrTalk(
        0x1C,
        "#00307F#5PLloyd...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04604F#11PKh...Ahaha!\x02\x03",
            "#04602FMister, despite appearances,\x01",
            "you're quick in decision making, eh?\x02\x03",
            "To think you did a nasty combo\x01",
            "to a little girl like Shirley is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#6PIt's because just by looking at you I could tell\x01",
            "you're an opponent I can't go easy with...\x02\x03",
            "#00007FYou give me a vibe like when we deal\x01",
            "with S-danger Wanted Monsters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#04609F#11PAhaha, correct!\x02",
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
            "#00310F#5P...No, get away!\x02\x03",
            "There's no way you could defend\x01",
            "yourself fully with those tonfas──\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x105,
        "Voice",
        "#11P#NWell, that seems for sure.\x02",
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

    def lambda_8E65():
        OP_96(0xFE, 0xFFFFD21A, 0xFFFFFE70, 0x20F8A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8E65)
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

    def lambda_8EF1():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_8EF1)
    ClearChrFlags(0x1D, 0x20)
    OP_6F(0x79)
    StopEffect(0x0, 0x2)
    SetChrChip(0x1, 0x105, 0x0, 0x0)

    ChrTalk(
        0x1D,
        "#04605F#11P#6AWaoh!?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x105, 0x55)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x1000)
    SetChrPos(0x105, -11750, 0, 135050, 295)

    def lambda_8F63():

        label("loc_8F63")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_8F63")

    QueueWorkItem2(0x105, 3, lambda_8F63)
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
            "#10306F#6P...Oh boy. I couldn't make\x01",
            "her trip with that attack, eh?\x02",
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
        "Lady Shirley!\x02",
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

    def lambda_91A9():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_91A9)
    Sleep(50)

    def lambda_91C1():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_91C1)
    Sleep(50)

    def lambda_91D9():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_91D9)
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

    def lambda_92B5():
        OP_95(0xFE, -15250, 0, 138150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_92B5)

    def lambda_92CF():
        OP_95(0xFE, -15200, 0, 135450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_92CF)

    def lambda_92E9():
        OP_95(0xFE, -16800, 0, 136150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92E9)

    def lambda_9303():
        OP_95(0xFE, -16700, 0, 137700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9303)
    WaitChrThread(0x105, 1)

    def lambda_9321():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9321)
    WaitChrThread(0x109, 1)
    Sound(531, 0, 100, 0)

    def lambda_9338():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9338)
    WaitChrThread(0x102, 1)

    def lambda_9349():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9349)
    WaitChrThread(0x103, 1)
    Sound(805, 0, 100, 0)

    def lambda_9360():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9360)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x1C,
        "#00306F#6P#NYou...\x02",
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
            "#04604F#3955V#11P#40WUh uh, okkay, okkay...\x02\x03",
            "#3956VIf you want to play with Shirley that badly,\x01",
            "then I'll make you company just for a little...\x02",
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
            "#3933V#40WAH HA HA HA HAH, you'll make Shirley\x01",
            "#4S#30Whave a little fun, eh!?\x02",
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
        "#00007FHere she comes──!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 150, -1, -1)

    AnonymousTalk(
        0x109,
        "#10107FLet's deal with her with full force!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    def lambda_95BB():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_95BB)

    def lambda_95D0():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_95D0)

    def lambda_95E5():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_95E5)

    def lambda_95FA():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_95FA)

    def lambda_960F():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_960F)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrChipByIndex(0x15, 0x33)
    SetChrChipByIndex(0x16, 0x33)
    SetChrChipByIndex(0x21, 0x1F)

    def lambda_9634():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9634)

    def lambda_9649():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9649)

    def lambda_965E():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_965E)

    def lambda_9673():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_9673)
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

    # Function_40_5A4B end

    def Function_41_972A(): pass

    label("Function_41_972A")

    SetChrChipByIndex(0x15, 0x33)
    OP_95(0x15, -50, 0, 133650, 6000, 0x0)
    OP_93(0x15, 0x0, 0x1F4)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x1)
    Return()

    # Function_41_972A end

    def Function_42_9752(): pass

    label("Function_42_9752")

    SetChrChipByIndex(0x15, 0x33)
    OP_95(0x15, -18850, 0, 137000, 6000, 0x0)
    OP_93(0x15, 0x0, 0x1F4)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x1)
    Return()

    # Function_42_9752 end

    def Function_43_977A(): pass

    label("Function_43_977A")

    SetChrChipByIndex(0x16, 0x33)
    OP_95(0x16, -2050, 0, 137900, 6000, 0x0)
    OP_93(0x16, 0x0, 0x1F4)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x1)
    Return()

    # Function_43_977A end

    def Function_44_97A2(): pass

    label("Function_44_97A2")

    SetChrChipByIndex(0x17, 0x33)
    OP_95(0x17, -4500, 0, 131150, 6000, 0x0)
    OP_93(0x17, 0x0, 0x1F4)
    SetChrChipByIndex(0x17, 0x34)
    SetChrSubChip(0x17, 0x1)
    Return()

    # Function_44_97A2 end

    def Function_45_97CA(): pass

    label("Function_45_97CA")

    SetChrChipByIndex(0x17, 0x33)
    OP_95(0x17, -17500, 0, 139450, 6000, 0x0)
    OP_93(0x17, 0x0, 0x1F4)
    SetChrChipByIndex(0x17, 0x34)
    SetChrSubChip(0x17, 0x1)
    Return()

    # Function_45_97CA end

    def Function_46_97F2(): pass

    label("Function_46_97F2")

    SetChrChipByIndex(0x18, 0x33)
    OP_95(0x18, -3950, 0, 136900, 6000, 0x0)
    OP_95(0x18, -5300, 0, 137700, 6000, 0x0)
    OP_93(0x18, 0x0, 0x1F4)
    SetChrChipByIndex(0x18, 0x34)
    SetChrSubChip(0x18, 0x1)
    Return()

    # Function_46_97F2 end

    def Function_47_982E(): pass

    label("Function_47_982E")

    SetChrChipByIndex(0x19, 0x33)
    OP_95(0x19, -4500, 0, 131150, 6000, 0x0)
    OP_95(0x19, -7550, 0, 133100, 6000, 0x0)
    OP_93(0x19, 0x0, 0x1F4)
    SetChrChipByIndex(0x19, 0x34)
    SetChrSubChip(0x19, 0x1)
    Return()

    # Function_47_982E end

    def Function_48_986A(): pass

    label("Function_48_986A")

    SetChrChipByIndex(0x19, 0x33)
    OP_95(0x19, -20150, 0, 140400, 6000, 0x0)
    OP_93(0x19, 0x0, 0x1F4)
    SetChrChipByIndex(0x19, 0x34)
    SetChrSubChip(0x19, 0x1)
    Return()

    # Function_48_986A end

    def Function_49_9892(): pass

    label("Function_49_9892")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98C5")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_98B9")
    OP_4C(0xFE, 0x3)
    Jump("loc_98BD")

    label("loc_98B9")

    OP_4B(0xFE, 0x3)

    label("loc_98BD")

    Sleep(500)
    Jump("Function_49_9892")

    label("loc_98C5")

    Return()

    # Function_49_9892 end

    def Function_50_98C6(): pass

    label("Function_50_98C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9915")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_50_98C6")

    label("loc_9915")

    Return()

    # Function_50_98C6 end

    def Function_51_9916(): pass

    label("Function_51_9916")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9965")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_51_9916")

    label("loc_9965")

    Return()

    # Function_51_9916 end

    def Function_52_9966(): pass

    label("Function_52_9966")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99B5")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, -150, 1250, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_52_9966")

    label("loc_99B5")

    Return()

    # Function_52_9966 end

    def Function_53_99B6(): pass

    label("Function_53_99B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A10")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 0, 1100, 2600, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x14, 0x32, 0xBB8)
    Jump("Function_53_99B6")

    label("loc_9A10")

    Return()

    # Function_53_99B6 end

    def Function_54_9A11(): pass

    label("Function_54_9A11")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A5B")
    PlayEffect(0x9, 0xFF, 0xFE, 0x3, -200, 1550, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_54_9A11")

    label("loc_9A5B")

    Return()

    # Function_54_9A11 end

    def Function_55_9A5C(): pass

    label("Function_55_9A5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9AB7")
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x9, 0xFF, 0xFE, 0x3, -300, 800, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_55_9A5C")

    label("loc_9AB7")

    Return()

    # Function_55_9A5C end

    def Function_56_9AB8(): pass

    label("Function_56_9AB8")

    SetChrChipByIndex(0xFE, 0x1F)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9AD2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9AE9")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_9AD2")

    label("loc_9AE9")

    Return()

    # Function_56_9AB8 end

    def Function_57_9AEA(): pass

    label("Function_57_9AEA")

    SetChrChipByIndex(0xFE, 0x1E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9B04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B1B")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_9B04")

    label("loc_9B1B")

    Return()

    # Function_57_9AEA end

    def Function_58_9B1C(): pass

    label("Function_58_9B1C")

    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x5)
    Sound(809, 0, 100, 0)
    OP_9D(0x21, 0x3B60, 0x1770, 0x23410, 0x3E8, 0x1770)
    BeginChrThread(0x21, 0, 0, 56)
    OP_95(0x21, 12700, 6000, 144400, 6000, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrSubChip(0x21, 0x5)

    def lambda_9B68():
        OP_9D(0xFE, 0x265C, 0x1770, 0x233DE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_9B68)
    Return()

    # Function_58_9B1C end

    def Function_59_9B81(): pass

    label("Function_59_9B81")

    Sleep(100)
    SetChrChipByIndex(0x22, 0x1F)
    BeginChrThread(0x22, 0, 0, 56)
    OP_95(0x22, -320, 4000, 149170, 6000, 0x0)
    OP_95(0x22, 5060, 6000, 148610, 6000, 0x0)
    EndChrThread(0x22, 0x0)
    TurnDirection(0x22, 0x1C, 500)
    SetChrSubChip(0x22, 0x5)

    def lambda_9BCA():
        OP_9D(0xFE, 0x21FC, 0x1770, 0x23F32, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9BCA)
    Return()

    # Function_59_9B81 end

    def Function_60_9BE3(): pass

    label("Function_60_9BE3")

    Sleep(1600)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x5)
    Sound(809, 0, 100, 0)
    OP_9D(0x23, 0x238C, 0x1770, 0x24784, 0x3E8, 0x1770)
    TurnDirection(0x23, 0x1C, 500)

    def lambda_9C17():
        OP_9D(0xFE, 0x2D82, 0x186A, 0x241F8, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9C17)
    Return()

    # Function_60_9BE3 end

    def Function_61_9C30(): pass

    label("Function_61_9C30")

    Sleep(2000)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x5)
    Sound(809, 0, 100, 0)
    OP_9D(0x24, 0x285A, 0x1770, 0x24572, 0x3E8, 0x1770)
    TurnDirection(0x24, 0x1C, 500)
    SetChrSubChip(0x24, 0x5)

    def lambda_9C68():
        OP_9D(0xFE, 0x30A2, 0x1770, 0x23988, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9C68)
    Return()

    # Function_61_9C30 end

    def Function_62_9C81(): pass

    label("Function_62_9C81")

    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 60, 0)

    def lambda_9CCC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9CCC)

    def lambda_9CE5():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CE5)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE70, 0x7D0, 0x0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sound(514, 0, 75, 0)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_62_9C81 end

    def Function_63_9D1F(): pass

    label("Function_63_9D1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D37")
    OP_A1(0xFE, 0xDAC, 0x2, 0x1, 0x2)
    Jump("Function_63_9D1F")

    label("loc_9D37")

    Return()

    # Function_63_9D1F end

    def Function_64_9D38(): pass

    label("Function_64_9D38")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D50")
    OP_A1(0xFE, 0xDAC, 0x2, 0x4, 0x5)
    Jump("Function_64_9D38")

    label("loc_9D50")

    Return()

    # Function_64_9D38 end

    def Function_65_9D51(): pass

    label("Function_65_9D51")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D69")
    OP_A1(0xFE, 0xDAC, 0x2, 0x0, 0x1)
    Jump("Function_65_9D51")

    label("loc_9D69")

    Return()

    # Function_65_9D51 end

    def Function_66_9D6A(): pass

    label("Function_66_9D6A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D81")
    OP_A0(0xFE, 5000, 0x1, 0x6)
    Jump("Function_66_9D6A")

    label("loc_9D81")

    Return()

    # Function_66_9D6A end

    def Function_67_9D82(): pass

    label("Function_67_9D82")

    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_9D8A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9DEC")
    SetChrSubChip(0xFE, 0x2)
    Sleep(850)
    SetChrSubChip(0xFE, 0x3)
    Sound(530, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x5, 0, 1200, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(80)
    SetChrSubChip(0xFE, 0x4)
    Sleep(80)
    Jump("loc_9D8A")

    label("loc_9DEC")

    Return()

    # Function_67_9D82 end

    def Function_68_9DED(): pass

    label("Function_68_9DED")

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

    # Function_68_9DED end

    def Function_69_9E96(): pass

    label("Function_69_9E96")

    Sound(872, 0, 100, 0)
    Sleep(400)
    Sound(870, 2, 100, 0)
    Return()

    # Function_69_9E96 end

    def Function_70_9EA6(): pass

    label("Function_70_9EA6")

    Sound(872, 0, 100, 0)
    Sleep(400)
    Sound(870, 2, 100, 0)
    Sound(875, 2, 100, 0)
    Return()

    # Function_70_9EA6 end

    def Function_71_9EBC(): pass

    label("Function_71_9EBC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9ED5")
    Sound(845, 0, 100, 0)
    Sleep(400)
    Jump("Function_71_9EBC")

    label("loc_9ED5")

    Return()

    # Function_71_9EBC end

    def Function_72_9ED6(): pass

    label("Function_72_9ED6")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A187")
    OP_2C(0xAA, 0x1)

    label("loc_A187")

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
        "#00010F#5PKh, *pant pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10310F#5PThis is the real strength of the\x01",
            "strongest class jaegers...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PKh...\x01",
            "I can't lose in experience!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#04606F#12PUhhm, it's not bad but,\x01",
            "is it this all you have?\x02\x03",
            "#04611FYou're nothing more than desserts\x01",
            "before the main valuable banquet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PWhat...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x131, 0x1F4)

    ChrTalk(
        0x103,
        "#00202F#11PAh...!\x02",
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
        "#00002F#6P#N2nd Lt. Mireille...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10109F#12P#NY-You have come for us...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#07904F#5PYes, there was a call from your Section\x01",
            "Chief addressed to the Commander.\x02\x03",
            "#07907F──Confirmed enemy forces!\x01",
            "Starting sweep operation now!\x02\x03",
            "However, maintain the recapture of Mainz\x01",
            "and security the maximum priority!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("CGF Members")

    AnonymousTalk(
        0xFF,
        "#4SYes ma'am!\x02",
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

    def lambda_A90C():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A90C)
    Sleep(50)
    SetChrChipByIndex(0xF, 0x23)

    def lambda_A928():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A928)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x23)

    def lambda_A944():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A944)
    Sleep(300)
    SetChrChipByIndex(0x12, 0x23)

    def lambda_A960():
        OP_9B(0x0, 0xFE, 0xA, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A960)
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

    def lambda_AB65():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_AB65)
    StopSound(865, 300, 50)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    Sleep(300)
    SetChrChipByIndex(0x16, 0x32)
    OP_93(0x16, 0xE1, 0x2EE)

    def lambda_AB96():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_AB96)

    ChrTalk(
        0x1D,
        (
            "#04612F#6PUh uh, then, see ya!\x02\x03",
            "#04602FShirley has a hunch we'll be\x01",
            "meeting again soon enough!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1D, 0x29)
    OP_93(0x1D, 0xE1, 0x2EE)

    def lambda_AC1A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_AC1A)
    OP_68(-29200, 1000, 127750, 5000)

    def lambda_AC40():
        OP_9B(0x0, 0xFE, 0xFFFD, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_AC40)
    Sleep(50)

    def lambda_AC58():
        OP_9B(0x0, 0xFE, 0x3, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_AC58)
    Sleep(300)

    def lambda_AC70():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_AC70)
    Sleep(50)

    def lambda_AC88():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AC88)
    Sleep(300)

    def lambda_ACA0():
        OP_9B(0x0, 0xFE, 0xFFFA, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_ACA0)
    Sleep(50)

    def lambda_ACB8():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_ACB8)
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

    def lambda_B019():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B019)

    def lambda_B02E():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B02E)
    SetChrChipByIndex(0x1E, 0x1F)

    def lambda_B047():
        OP_95(0xFE, -22150, 0, 139350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_B047)
    OP_68(-20950, 1200, 137200, 0)
    MoveCamera(13, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(20000, 2000)
    WaitChrThread(0x1E, 1)

    def lambda_B09C():

        label("loc_B09C")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B09C")

    QueueWorkItem2(0x101, 2, lambda_B09C)

    def lambda_B0AE():

        label("loc_B0AE")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B0AE")

    QueueWorkItem2(0x104, 2, lambda_B0AE)

    def lambda_B0C0():
        TurnDirection(0x1E, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_B0C0)
    Sleep(50)

    def lambda_B0D0():

        label("loc_B0D0")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B0D0")

    QueueWorkItem2(0x102, 2, lambda_B0D0)

    def lambda_B0E2():

        label("loc_B0E2")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B0E2")

    QueueWorkItem2(0x103, 2, lambda_B0E2)
    Sleep(50)

    def lambda_B0F7():

        label("loc_B0F7")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B0F7")

    QueueWorkItem2(0x109, 2, lambda_B0F7)

    def lambda_B109():

        label("loc_B109")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B109")

    QueueWorkItem2(0x105, 2, lambda_B109)
    WaitChrThread(0x1E, 2)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#00308F#12PMireille...\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    ChrTalk(
        0x1E,
        (
            "#07906F#5PHonestly, when it comes to you,\x01",
            "it's always some reckless stunt...\x02\x03",
            "#07902FLeave those\x01",
            "guys to us.\x02\x03",
            "...You all.\x01",
            "Please, don't let Randy do\x01",
            "anything more reckless than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#12PLeave it us.\x02",
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
        "#00006F#5P*sigh*, oh man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PAt any rate... It seems that things\x01",
            "have been settled for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00314F#5P#40W............\x02",
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

    def lambda_B40C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B40C)
    Sleep(50)

    def lambda_B41C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B41C)

    def lambda_B429():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B429)
    Sleep(50)

    def lambda_B439():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B439)

    def lambda_B446():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B446)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#12PRandy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#12PA-Are you all right?\x01",
            "Are you hurt anywhere...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00303F#30W#5P...Lloyd.\x01",
            "I'm gonna ask you...\x02\x03",
            "#00312FWhat the hell do you wanted to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12PHuh...\x02",
    )

    CloseMessageWindow()

    def lambda_B540():

        label("loc_B540")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_B540")

    QueueWorkItem2(0x102, 2, lambda_B540)

    def lambda_B552():

        label("loc_B552")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_B552")

    QueueWorkItem2(0x103, 2, lambda_B552)

    def lambda_B564():

        label("loc_B564")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_B564")

    QueueWorkItem2(0x109, 2, lambda_B564)

    def lambda_B576():

        label("loc_B576")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_B576")

    QueueWorkItem2(0x105, 2, lambda_B576)
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

    def lambda_B5E9():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5E9)
    OP_0D()
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011F#12P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PRandy!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11PMr. Randy...!?\x02",
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
            "#00311F#30W#5PDo you get it...?\x01",
            "You all stepped into a\x01",
            ""battlefield", you know...?\x02\x03",
            "#30WYou're no soldiers, no\x01",
            "jaegers, not even\x01",
            "killing pros...\x02\x03",
            "#30WDon't you really get it how much of\x01",
            "a dangerous thing did you do...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#12P...Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#30W#5P...I also want to say something\x01",
            "to milady and peTiote...\x02\x03",
            "...Also, to Noｱl and Wazy. You\x01",
            "should've known it was dangerous,\x01",
            "but why didn't you stop...?\x02\x03",
            "#00311FBut most of all, you Lloyd──\x01",
            "You're supposed to be the leader...\x02\x03",
            "What's with you actin' impulsively and exposin'\x01",
            "your comrades to danger in such a time...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P#30W...Don't joke with me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetCameraDistance(20000, 100)

    def lambda_B910():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B910)
    Sound(811, 0, 60, 0)

    def lambda_B92B():
        OP_A0(0xFE, 2000, 0x29, 0x2B)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B92B)

    def lambda_B938():
        OP_A0(0xFE, 2000, 0x2, 0x4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_B938)

    def lambda_B945():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B945)

    def lambda_B95A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B95A)
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

    def lambda_B9F2():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B9F2)
    OP_0D()

    ChrTalk(
        0x104,
        "#00305F#5PGh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12PLloyd...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12PMr. Lloyd...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00010F#12PDidn't I come here because I can't let\x01",
            "my comrade be exposed to danger!?\x02\x03",
            "#00006FAnd that "see ya"...\x02\x03",
            "#00007F...Do you really think that...\x01",
            "We could've been persuaded\x01",
            "by such a scrap of paper!?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0x104, 1000, 0x20, 0x21)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00313F#5P#30WKh...\x02\x03",
            "...I knew it...\x02\x03",
            "#40WI...I should've never been together\x01",
            "with you all in the first place...\x02",
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
            "#00313F#30W#5P...My hands are smeared with blood...\x02\x03",
            "I didn't only kill soldiers on the battlefields...\x02\x03",
            "In order to ensnare a strong enemy force,\x01",
            "once I used a village that had nothing to do...\x02\x03",
            "And so, I even sacrificed...\x02\x03",
            "...An innocent guy, a youngster\x01",
            "who had eyes like yours...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P...!\x02",
    )

    CloseMessageWindow()
    OP_68(-20000, 1000, 137750, 500)
    SetChrSubChip(0x101, 0x2D)

    def lambda_BDD8():
        OP_9B(0x1, 0xFE, 0xFFF6, 0xFFFFFDA8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDD8)

    def lambda_BDED():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BDED)
    Sound(811, 0, 60, 0)

    def lambda_BE0C():
        OP_A0(0xFE, 1500, 0x6, 0x7)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_BE0C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    Sleep(500)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#00307F#5PWho is in front of you all is such\x01",
            "an irredeemable piece of shit!\x02\x03",
            "#00306FIt's gonna be troublesome...any more than this!\x02\x03",
            "Relyin' on an older brother-like someone to\x01",
            "whom you look at with puppy eyes and snuggle to...!\x02\x03",
            "#00308FIf you keep doin' such a thing...I...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x104,
        (
            "#00313F#4S#5P#40W...I...I could...\x01",
            "End up forgivin' myself!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#30W...Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#11P#30WMr. Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#12P#30W...Senior Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F#11P#30W...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P#30W...........\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_A0(0x101, 1000, 0x2D, 0x30)

    ChrTalk(
        0x101,
        (
            "#00004F#12P#30W...Ha ha...\x02\x03",
            "Thank goodness... I'm relieved.\x02",
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
        "#00305F#40W#5P......Huh......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PL-Loyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11PMr. Lloyd...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0x101, 1000, 0x2F, 0x2D)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W...I was thinking what would I've\x01",
            "done if you had replied jokingly\x01",
            "with a calm face like always...\x02\x03",
            "#00002FBut you finally...\x01",
            "Spit it out to us, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x104, 0x7D0, 0x4, 0x1D, 0x1E, 0x1D, 0xA)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x104,
        "#00305F#5P!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12P#30W...Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#12P#30W...Mr. Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30WThinking about it, Randy too \x01",
            "is a youngster like us...\x02\x03",
            "#00008F...Since everyone knows that you carry\x01",
            "something heavy within you, just out of \x01",
            "consideration no one touched that subject...\x02\x03",
            "We just kept getting helped by you,\x01",
            "without being able to help you, Randy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#11P#30W...Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#12P#30W...You're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5P#30W...Hey...Hey now...\x02\x03",
            "#00301FLike I said, I have no\x01",
            "right to be said such...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W──Randy's past too, and also the\x01",
            "feelings of guilt are part of yourself.\x02\x03",
            "#00003FI think that maybe you should come\x01",
            "to terms with those, Randy.\x02\x03",
            "#00001FAnd indeed, the result could also be\x01",
            "that you won't be able to forgive yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#5P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30WHowever, even if others\x01",
            "don't forgive you, Randy...\x02\x03",
            "Even if you yourself\x01",
            "don't forgive you, Randy...\x02\x03",
            "#00002F...We'll all\x01",
            "forgive you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x104,
        "#00305F#5P#4S!!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12P#30W...That's right.\x02\x03",
            "#00102FForgiving and accepting each other\x01",
            "is what you call "comrades"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11P#30WLike everyone accepted\x01",
            "my past before...\x02\x03",
            "#00202FI too will forgive Mr. Randy's\x01",
            "past, flirty personality, and\x01",
            "slovenly aspects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#12P#30W...I'll forgive you too.\x02\x03",
            "#10100FAs a fellow soldier...\x01",
            "It's a problem we have to face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11P#30WOh boy, this is not in\x01",
            "my character, but...\x02\x03",
            "#10304F...First of all, a man is a creature that\x01",
            "bears many kinds of sins just by living.\x02\x03",
            "#10300FWhat I'm trying to say is...\x01",
            "Aren't we virtually all the same before the Goddess?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0x104, 1500, 0xA, 0xD)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00314F#40W#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30WWe can't live neither in the past,\x01",
            "nor in the unforeseeable future...\x02\x03",
            "We can only live intently in\x01",
            "the "today" and the "now".\x02\x03",
            "#00008FAnd in this moment...\x01",
            "We're in the same time and same place.\x02\x03",
            "Randy, if you can be happy\x01",
            "even for a moment with that...\x02\x03",
            "#00000FPlease── I want you to accept us\x01",
            "like we are, us who forgive you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_CA52():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CA52)
    WaitChrThread(0x104, 2)
    Sleep(500)

    def lambda_CA72():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CA72)
    WaitChrThread(0x104, 2)
    Sleep(500)
    OP_A0(0x104, 1500, 0xE, 0x10)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00313F#40W#5P............\x02\x03",
            "...Jeez...you guys...\x02\x03",
            "#40WWhy do I have...to receive\x01",
            "such affected words...\x02\x03",
            "#40W...What kind of a bashful play is this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PWell, it is a path I too\x01",
            "walked through once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12P*giggle*, like you said before...\x02\x03",
            "#00102FWe're probably all victims of a\x01",
            "certain someone who ended up\x01",
            "choosing the Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#11PNo, like I told you, why do I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#12PUh uh... But he seems to \x01",
            "posses a persuasive power, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#11PAhaha, even I am no\x01",
            "match for our natural gigolo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00314F#40W#5P............\x02",
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
            "#00306F#5P#30W...*haah*.\x02\x03",
            "#00303FI'm a murderer and a...\x01",
            "Good-for-nothing irresponsible guy.\x02\x03",
            "I tried to appear smart but\x01",
            "I ended up being beaten by\x01",
            "a monster-like little girl.\x02\x03",
            "#00308FDue to such a temper I\x01",
            "could be causin' troubles\x01",
            "in the future too...\x02",
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
        "#5P#30W──Even so, you don't mind?\x02",
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
        "#00014F#12PNo, I don't...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#12PNo, of course not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00214F#11PDo your worst.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#12PNice to be working with\x01",
            "you from now on too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHu hu...\x01",
            "Adversity builds character, I guess?\x02",
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

    def lambda_D029():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D029)
    Sleep(500)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#00310F#5PWazy, you...\x02\x03",
            "You promised you'd be silent,\x01",
            "but you spilled all to them, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11POh come on, it's a misunderstanding.\x02\x03",
            "#10306FI kept properly silent, but\x01",
            "Lloyd and the others began\x01",
            "to look for you on their own...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D130():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D130)
    Sleep(50)

    def lambda_D140():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D140)

    def lambda_D14D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D14D)
    Sleep(50)

    def lambda_D15D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D15D)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x109,
        (
            "#10105F#6PH-Hey, Wazy...?\x02\x03",
            "#10101FYou knew that senior\x01",
            "Randy had left!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PWazy, listen here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12PMr. Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12P*sigh*, I don't know what\x01",
            "to think about you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PWell, even I didn't hear\x01",
            "where he was headed...\x02\x03",
            "#10306FOh boy... Does it mean that\x01",
            "in the end I'm the bad guy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#6PHonestly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PI think that sometimes Mr. Wazy\x01",
            "too should reflect on his actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PHa ha...\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x9B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00304F#5P──Alright.\x01",
            "It seems I can move too somehow.\x02\x03",
            "#00300FAlthough it's rather too late, let's go see\x01",
            "how Mireille and the others are doin'.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D3EF():
        OP_93(0xFE, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D3EF)
    Sleep(50)

    def lambda_D3FF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D3FF)

    def lambda_D40C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D40C)
    Sleep(50)

    def lambda_D41C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D41C)

    def lambda_D429():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D429)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        "#00000F#12PYou're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PThe "Red Constellation"...\x01",
            "It would be nice if they had\x01",
            "withdrawn somehow.\x02",
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

    # Function_72_9ED6 end

    def Function_73_D4FC(): pass

    label("Function_73_D4FC")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -20000, 4000, 152450, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_73_D4FC end

    def Function_74_D52A(): pass

    label("Function_74_D52A")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -20000, 4000, 155150, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_74_D52A end

    def Function_75_D55E(): pass

    label("Function_75_D55E")

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

    # Function_75_D55E end

    def Function_76_D654(): pass

    label("Function_76_D654")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -18750, 4000, 155600, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_76_D654 end

    def Function_77_D688(): pass

    label("Function_77_D688")

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

    # Function_77_D688 end

    def Function_78_D70D(): pass

    label("Function_78_D70D")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -21500, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -21500, 4000, 152550, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_78_D70D end

    def Function_79_D763(): pass

    label("Function_79_D763")

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

    # Function_79_D763 end

    def Function_80_D824(): pass

    label("Function_80_D824")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -23200, 8000, 177100, 5000, 0x0)
    OP_95(0xFE, -18800, 8000, 172750, 5000, 0x0)
    OP_95(0xFE, -18800, 4000, 152400, 6000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_80_D824 end

    def Function_81_D87A(): pass

    label("Function_81_D87A")

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

    # Function_81_D87A end

    def Function_82_D901(): pass

    label("Function_82_D901")

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

    # Function_82_D901 end

    def Function_83_D96B(): pass

    label("Function_83_D96B")

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

    # Function_83_D96B end

    def Function_84_DA47(): pass

    label("Function_84_DA47")

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

    # Function_84_DA47 end

    def Function_85_DAB1(): pass

    label("Function_85_DAB1")

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

    # Function_85_DAB1 end

    def Function_86_DB53(): pass

    label("Function_86_DB53")

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

    # Function_86_DB53 end

    def Function_87_DBD1(): pass

    label("Function_87_DBD1")

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

    # Function_87_DBD1 end

    def Function_88_DC55(): pass

    label("Function_88_DC55")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DCA4")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 950, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x3, 0x2)
    Jump("Function_88_DC55")

    label("loc_DCA4")

    Return()

    # Function_88_DC55 end

    def Function_89_DCA5(): pass

    label("Function_89_DCA5")

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

    # Function_89_DCA5 end

    def Function_90_DD6A(): pass

    label("Function_90_DD6A")

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

    # Function_90_DD6A end

    def Function_91_DDED(): pass

    label("Function_91_DDED")

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

    # Function_91_DDED end

    def Function_92_DE6A(): pass

    label("Function_92_DE6A")

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

    # Function_92_DE6A end

    def Function_93_DED3(): pass

    label("Function_93_DED3")

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

    # Function_93_DED3 end

    def Function_94_DF3C(): pass

    label("Function_94_DF3C")

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

    # Function_94_DF3C end

    def Function_95_DF91(): pass

    label("Function_95_DF91")

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

    # Function_95_DF91 end

    def Function_96_DFEC(): pass

    label("Function_96_DFEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E010")
    OP_82(0xA, 0xA, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_96_DFEC")

    label("loc_E010")

    Return()

    # Function_96_DFEC end

    def Function_97_E011(): pass

    label("Function_97_E011")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E035")
    OP_82(0x28, 0x28, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_97_E011")

    label("loc_E035")

    Return()

    # Function_97_E011 end

    def Function_98_E036(): pass

    label("Function_98_E036")

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

    def lambda_E114():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E114)
    Sleep(0)

    def lambda_E12C():
        OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E12C)
    Sleep(0)

    def lambda_E144():
        OP_9B(0x0, 0x106, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_E144)
    Sleep(0)

    def lambda_E15C():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E15C)
    Sleep(0)

    def lambda_E174():
        OP_9B(0x0, 0x107, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_E174)
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
        "#00007F#11PThe sounds of a battle...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PNorth west, about 10 selge!\x02\x03",
            "There is probably a battle in the mountain\x01",
            "zone far from the mountain path...!\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7586", 0)
    ReplaceBGM("ed7251", "ed7586")

    ChrTalk(
        0x101,
        "#00010F#11PKh...a mountain zone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#12PIt won't be easy to\x01",
            "reach by foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10707F#11PNo...\x01",
            "Let's try going!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01201F#12P#3CIf push come to shove, I'll\x01",
            "jump over the cliff and intervene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#11PUnderstood! If there'll be a\x01",
            "need for that, I'll count on you!\x02",
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

    # Function_98_E036 end

    def Function_99_E451(): pass

    label("Function_99_E451")

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
        "#00010F#11PKh, what's this!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10408F#12PBarbed wire to seal off\x01",
            "a battlefield area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PIt appears that the battle\x01",
            "is going on further in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#11PIt can't be helped...\x01",
            "Let's look for a place we can go around from!\x02",
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

    # Function_99_E451 end

    def Function_100_E60C(): pass

    label("Function_100_E60C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 0)), scpexpr(EXPR_END)), "loc_E72A")
    SetScenarioFlags(0x0, 4)

    label("loc_E72A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 1)), scpexpr(EXPR_END)), "loc_E736")
    SetScenarioFlags(0x0, 4)

    label("loc_E736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 2)), scpexpr(EXPR_END)), "loc_E742")
    SetScenarioFlags(0x0, 4)

    label("loc_E742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 3)), scpexpr(EXPR_END)), "loc_E74E")
    SetScenarioFlags(0x0, 4)

    label("loc_E74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 4)), scpexpr(EXPR_END)), "loc_E75A")
    SetScenarioFlags(0x0, 4)

    label("loc_E75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 5)), scpexpr(EXPR_END)), "loc_E766")
    SetScenarioFlags(0x0, 4)

    label("loc_E766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 6)), scpexpr(EXPR_END)), "loc_E772")
    SetScenarioFlags(0x0, 4)

    label("loc_E772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 7)), scpexpr(EXPR_END)), "loc_E77E")
    SetScenarioFlags(0x0, 4)

    label("loc_E77E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 0)), scpexpr(EXPR_END)), "loc_E78A")
    SetScenarioFlags(0x0, 4)

    label("loc_E78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 1)), scpexpr(EXPR_END)), "loc_E796")
    SetScenarioFlags(0x0, 4)

    label("loc_E796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 2)), scpexpr(EXPR_END)), "loc_E7A2")
    SetScenarioFlags(0x0, 4)

    label("loc_E7A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 3)), scpexpr(EXPR_END)), "loc_E7AE")
    SetScenarioFlags(0x0, 4)

    label("loc_E7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7BD")
    OP_2C(0xAF, 0x1)

    label("loc_E7BD")

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

    def lambda_E91E():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E91E)
    Sleep(10)

    def lambda_E936():
        OP_9B(0x0, 0x106, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_E936)
    Sleep(10)

    def lambda_E94E():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E94E)
    Sleep(10)

    def lambda_E966():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E966)
    Sleep(10)

    def lambda_E97E():
        OP_9B(0x0, 0x107, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_E97E)
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
        "#00005F#5P...?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x106,
        "#10707F#6P#4SMr. Lloyd!\x02",
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

    def lambda_EA73():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EA73)
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

    def lambda_EB52():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EB52)
    Sleep(50)

    def lambda_EB62():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_EB62)
    Sleep(50)

    def lambda_EB72():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_EB72)
    Sleep(50)

    def lambda_EB82():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_EB82)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    ChrTalk(
        0x105,
        "#10410F#6PA sniper...!?\x02",
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
            "#5PAs expected from "Yin".\x01",
            "You did well in noticing me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#11PKh...\x01",
            "Were you waiting in ambush!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PAfter all, I could sense there had been\x01",
            "some movements in the tunnel path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PStill, to think you could appear here and there\x01",
            "like this in a Crossbell under martial law...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PAre you using the Merkabah of that\x01",
            "Knight over there like I suspect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#11P...Eeh.\x01",
            "Did you pin me down too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PPerhaps, you may have come to join\x01",
            "hands with the Resistance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PYou're slightly late. The cleanup\x01",
            "operation has already begun.\x02",
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
            "#5PIt's somewhat of a bother, but the\x01",
            "cleanup will soon be completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PI'm sorry but, could you not rise\x01",
            "a finger and stay there to look?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#11PKh...as if we'd do that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10707F#11PMr. Zeit and I will\x01",
            "break through here...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PI won't let you.\x02",
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

    def lambda_F0E5():
        OP_95(0xFE, 1300, 0, 131450, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_F0E5)
    Sleep(100)
    BeginChrThread(0x24, 3, 0, 56)

    def lambda_F108():
        OP_95(0xFE, 1750, 0, 136900, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_F108)
    Sleep(100)
    BeginChrThread(0x25, 3, 0, 56)

    def lambda_F12B():
        OP_95(0xFE, 8390, 0, 129310, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_F12B)
    Sleep(100)
    BeginChrThread(0x26, 3, 0, 56)

    def lambda_F14E():
        OP_95(0xFE, 11450, 0, 133150, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_F14E)
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
        "#10701F#11P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01201F#11P#3CHm, surrounded, are we.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10408F#12PThis is a little bad...\x02",
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
            "#5PLloyd Bannings\x01",
            "and party...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PRegimental commander of the "Red Constellation",\x01",
            ""Lightning Attack" Gareth, will be your opponent.\x02",
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
            "#00007F#5PKh...\x01",
            "Everyone, prepare for battle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#5PPlease be careful of sniping\x01",
            "from above the cliff!\x02",
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

    def lambda_F3F7():
        OP_9D(0xFE, 0x1C52, 0x0, 0x20ADA, 0x1F4, 0x88B8)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_F3F7)

    def lambda_F414():
        OP_9D(0xFE, 0x1482, 0x0, 0x20ADA, 0x1F4, 0x88B8)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_F414)

    def lambda_F431():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_F431)

    def lambda_F44E():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_F44E)

    def lambda_F46B():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_F46B)

    def lambda_F488():
        OP_9D(0xFE, 0x186A, 0x0, 0x20ADA, 0x1F4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_F488)
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

    # Function_100_E60C end

    def Function_101_F4F9(): pass

    label("Function_101_F4F9")

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

    # Function_101_F4F9 end

    def Function_102_F572(): pass

    label("Function_102_F572")

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

    # Function_102_F572 end

    def Function_103_F5EB(): pass

    label("Function_103_F5EB")

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
            "#00010F#5P...Kh...nothing to be less expected\x01",
            "from the "Red Constellation"...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10410F#12PTo think that sniping from high\x01",
            "altitudes could be such a pain...!\x02",
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
            "#5PSince you're the Young Master's \x01",
            "colleagues, it wasn't a bad fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PHowever, when a high place\x01",
            "has been taken by a sniper,\x01",
            "a strategic defeat is inevitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PSurrender quietly and──\x02",
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
        "#11PWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PWhat was that...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PP-Perhaps...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#11P#3CHm, they made it in time.\x02",
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
        "#11PKh...wolves!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00214F#11PZeit's subordinates...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PAlso...\x01",
            "Isn't that Miss Mireille and her men!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#11PKh... \x01",
            "You're nothing more than beasts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#11PVery well!\x01",
            "We'll make a pincer movement and──\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x104,
        "Youth's Voice",
        "#2768V#15A#30WAs if I'd let you, Gareth!\x02",
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
        "#5PUwoh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01200F#11P#3COoh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PR-Randy!?\x02",
    )

    CloseMessageWindow()
    MoveCamera(27, 26, 0, 20000)
    OP_A1(0x104, 0x5DC, 0x2, 0x4, 0x5)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x104,
        (
            "#00304F#2769V#11PYo, long time no see.\x02\x03",
            "#00302F#2770VWe've got a great deal to talk about,\x01",
            "but let's postpone that for now.\x02",
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
        "#5PYoung Master...well done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PTo think a sniper like myself\x01",
            "would've been ambushed from behind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PWell, without the wolves' assistance,\x01",
            "that would've gone bad.\x02\x03",
            "#00301FAlso, it's your mistake having got your\x01",
            "attention caught by Lloyd and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PIt is as you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5P...Still, Young Master, isn't\x01",
            "that your usual halberd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PWithout your blade rifle...do you\x01",
            "think you can win against me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#11PSo? That doesn't\x01",
            "mean I won't use it.\x02",
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
            "#00300F#11PI got ol' man Guillaume\x01",
            "to repair it for me.\x02\x03",
            "#00306FAlso, no matter how powerful,\x01",
            "if the engine mechanism gets\x01",
            "busted, the usability decreases.\x02\x03",
            "#00302FI only use it in critical moments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5P...I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5PIndeed, with that single strike,\x01",
            "my rifle precision went out of order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PThe situation is very unfavorable, hm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PYeah, just retreat.\x02\x03",
            "#00307FAnd tell this to my uncle...\x01",
            ""I'm gonna beat you to a pulp!"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5P──Young Master.\x01",
            "It seems you've matured, hm?\x02",
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
            "#11P#4SOperation suspended!\x01",
            "Retreat up to point D!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Jaegers")

    AnonymousTalk(
        0xFF,
        "#4SJ-Jaー!\x02",
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

    def lambda_11135():
        OP_95(0xFE, -20250, 0, 142650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11135)
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
        "#00014F#12PRandy...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00214F#11P...Mr. Randy!\x02",
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
            "Yo! Nice job there.\x02\x03",
            "I'd never thought\x01",
            "you'd come here...\x02\x03",
            "Lloyd, peTiote.\x01",
            "I'm really glad you're\x01",
            "all in one piece.\x02",
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
        "#00002F#12PYeah, you too Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PDid you...escape?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#5PYeah, after I somehow managed to escape by myself, \x01",
            "I was able to join with Mireille and the others.\x02\x03",
            "#00301FI've been helpin' the Resistance\x01",
            "around this area until now, but...\x02\x03",
            "#00306FI really thought that this\x01",
            "time could've been the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PI see...\x01",
            "I'm really glad you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PThanks to Zeit's\x01",
            "subordinates.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x107, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00304F#6PYeah, in a dangerous time like that\x01",
            "they suddenly assisted us.\x02\x03",
            "#00302FDid you perhaps\x01",
            "call them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3CHm, just in case.\x02\x03",
            "#01200FI also instructed them to pay attention\x01",
            "to those jaegers or whatever actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PEeh, I see...\x02",
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
            "#00307F#6P#4SWait, what!?\x02\x03",
            "#4SWhy're you talkin'!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#12PHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PWell, that is shocking.\x02",
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
            "#00305F#5P...And now that I see it,\x01",
            "Wazy is dressed like that and...\x02\x03",
            "#00307FAnd also...dear Rixia!?\x01",
            "Why're you with Lloyd and the others!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#6POh boy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10709F#12P*chuckle chuckle*...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1E, 0x80)

    NpcTalk(
        0x1E,
        "Woman's Voice",
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

    def lambda_117DA():
        OP_96(0x1E, 0xFFFFA84E, 0x0, 0x22024, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_117DA)

    def lambda_117F4():
        OP_92(0x101, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_117F4)
    Sleep(0)

    def lambda_1180A():
        OP_92(0x103, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1180A)
    Sleep(0)

    def lambda_11820():
        OP_92(0x104, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11820)
    Sleep(0)

    def lambda_11836():
        OP_92(0x105, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11836)
    Sleep(0)

    def lambda_1184C():
        OP_92(0x106, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1184C)
    Sleep(0)

    def lambda_11862():
        OP_92(0x107, 0xFFFFA84E, 0x22024, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_11862)
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
            "The enemy forces have been \x01",
            "confirmed to have retreated!\x02\x03",
            "With this, we can probably\x01",
            "hold out for a little while.\x02",
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
        "#00302F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PMiss Mireille, long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#11PI am glad you are all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#07904F#6PYou too... I'm happy to see\x01",
            "you all in one piece.\x02\x03",
            "#07902F...Somehow you seem to be together\x01",
            "with some eccentric people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PWell, there are many reasons.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#5PFor now let's take a breather\x01",
            "and exchange information.\x02",
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
        "Woman's Voice",
        "#4PYes── I strongly agree!\x02",
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

    def lambda_11BEC():
        OP_95(0xFE, -19850, 450, 144900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_11BEC)

    def lambda_11C06():
        OP_92(0x101, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11C06)
    Sleep(50)

    def lambda_11C1C():
        OP_92(0x103, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11C1C)
    Sleep(50)

    def lambda_11C32():
        OP_92(0x104, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11C32)
    Sleep(50)

    def lambda_11C48():
        OP_92(0x105, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11C48)
    Sleep(50)

    def lambda_11C5E():
        OP_92(0x106, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_11C5E)
    Sleep(50)

    def lambda_11C74():
        OP_92(0x107, 0xFFFFB276, 0x23604, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_11C74)
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
        "#00011F#12PM-Miss Grace!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12PWhy are you here...\x02",
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
            "Weeell, there was a little\x01",
            "problem and it became hard\x01",
            "to stay in Crossbell City.\x02\x03",
            "And so, I imposed at Randy and\x01",
            "the others' place as a war\x01",
            "correspondent and cameraman too.\x02",
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
            "#07906F#6P#N*haah*...I didn't really want\x01",
            "to welcome her, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00309F#5PHa ha, well, that's what happened.\x02\x03",
            "#00300FIt seems we all need to explain to each\x01",
            "other what we've been up to 'til now.\x02",
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

    # Function_103_F5EB end

    def Function_104_12065(): pass

    label("Function_104_12065")

    OP_95(0xFE, -20250, 0, 141150, 5000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_104_12065 end

    def Function_105_12081(): pass

    label("Function_105_12081")

    OP_95(0xFE, -18900, 0, 141140, 5000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_105_12081 end

    def Function_106_1209D(): pass

    label("Function_106_1209D")

    OP_95(0xFE, -22600, 0, 140700, 3000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_106_1209D end

    def Function_107_120B9(): pass

    label("Function_107_120B9")

    OP_95(0xFE, -20400, 0, 139200, 3000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_107_120B9 end

    def Function_108_120D5(): pass

    label("Function_108_120D5")

    OP_95(0xFE, -17750, 0, 142700, 3000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_108_120D5 end

    def Function_109_120F5(): pass

    label("Function_109_120F5")

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

    # Function_109_120F5 end

    def Function_110_121FA(): pass

    label("Function_110_121FA")

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

    # Function_110_121FA end

    def Function_111_1226F(): pass

    label("Function_111_1226F")

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

    # Function_111_1226F end

    def Function_112_1234A(): pass

    label("Function_112_1234A")

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

    # Function_112_1234A end

    def Function_113_123DA(): pass

    label("Function_113_123DA")

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

    # Function_113_123DA end

    def Function_114_124DF(): pass

    label("Function_114_124DF")

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

    # Function_114_124DF end

    def Function_115_12575(): pass

    label("Function_115_12575")

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

    # Function_115_12575 end

    def Function_116_1262A(): pass

    label("Function_116_1262A")

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

    # Function_116_1262A end

    def Function_117_1269F(): pass

    label("Function_117_1269F")

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

    # Function_117_1269F end

    def Function_118_12742(): pass

    label("Function_118_12742")

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

    # Function_118_12742 end

    def Function_119_127B7(): pass

    label("Function_119_127B7")

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

    # Function_119_127B7 end

    def Function_120_12860(): pass

    label("Function_120_12860")

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

    # Function_120_12860 end

    def Function_121_128D5(): pass

    label("Function_121_128D5")

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

    # Function_121_128D5 end

    def Function_122_12999(): pass

    label("Function_122_12999")

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

    # Function_122_12999 end

    def Function_123_12A59(): pass

    label("Function_123_12A59")

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

    # Function_123_12A59 end

    def Function_124_12AD7(): pass

    label("Function_124_12AD7")

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

    # Function_124_12AD7 end

    def Function_125_12B85(): pass

    label("Function_125_12B85")

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

    # Function_125_12B85 end

    def Function_126_12BE7(): pass

    label("Function_126_12BE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12C36")
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x3)
    Jump("Function_126_12BE7")

    label("loc_12C36")

    Return()

    # Function_126_12BE7 end

    def Function_127_12C37(): pass

    label("Function_127_12C37")

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

    # Function_127_12C37 end

    def Function_128_12CD6(): pass

    label("Function_128_12CD6")

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

    # Function_128_12CD6 end

    def Function_129_12D75(): pass

    label("Function_129_12D75")

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

    # Function_129_12D75 end

    def Function_130_12DE5(): pass

    label("Function_130_12DE5")

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

    label("loc_12EAD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12F2B")

    def lambda_12EBD():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_12EBD)
    SetChrChipByIndex(0x18, 0x5D)

    def lambda_12ED6():
        OP_A0(0xFE, 2000, 0x0, 0x3)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_12ED6)
    OP_9A(0x18, 0xFE, 0x3E8, 0x2710, 0x0)
    Sleep(1000)

    def lambda_12EF4():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_12EF4)
    SetChrChipByIndex(0xFE, 0x61)

    def lambda_12F0D():
        OP_A0(0xFE, 2000, 0x0, 0x4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_12F0D)
    OP_9A(0xFE, 0x18, 0x3E8, 0x2710, 0x0)
    Sleep(1000)
    Jump("loc_12EAD")

    label("loc_12F2B")

    Return()

    # Function_130_12DE5 end

    def Function_131_12F2C(): pass

    label("Function_131_12F2C")

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

    # Function_131_12F2C end

    def Function_132_12FC9(): pass

    label("Function_132_12FC9")

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

    def lambda_13090():
        OP_A0(0xFE, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_13090)
    SetChrFlags(0xFE, 0x20)
    OP_9A(0xFE, 0x19, 0x3E8, 0x2710, 0x0)
    Sound(566, 0, 20, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x19, 0x5C)
    SetChrSubChip(0x19, 0x0)

    def lambda_130C3():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_130C3)

    def lambda_130DC():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_130DC)
    Return()

    # Function_132_12FC9 end

    def Function_133_130F1(): pass

    label("Function_133_130F1")

    SetChrChipByIndex(0xFE, 0x65)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1310B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13122")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    Jump("loc_1310B")

    label("loc_13122")

    Return()

    # Function_133_130F1 end

    def Function_134_13123(): pass

    label("Function_134_13123")

    SetChrChipByIndex(0xFE, 0x64)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1313D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1315B")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_1313D")

    label("loc_1315B")

    Return()

    # Function_134_13123 end

    def Function_135_1315C(): pass

    label("Function_135_1315C")

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

    # Function_135_1315C end

    def Function_136_1320F(): pass

    label("Function_136_1320F")

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

    # Function_136_1320F end

    def Function_137_132C9(): pass

    label("Function_137_132C9")

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

    # Function_137_132C9 end

    def Function_138_13383(): pass

    label("Function_138_13383")

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

    # Function_138_13383 end

    def Function_139_1344D(): pass

    label("Function_139_1344D")

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

    # Function_139_1344D end

    def Function_140_134B7(): pass

    label("Function_140_134B7")

    BeginChrThread(0xFE, 0, 0, 134)

    label("loc_134BD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13515")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1350D")
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x66)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3)
    Return()

    label("loc_1350D")

    Sleep(1000)
    Jump("loc_134BD")

    label("loc_13515")

    Return()

    # Function_140_134B7 end

    def Function_141_13516(): pass

    label("Function_141_13516")

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

    # Function_141_13516 end

    def Function_142_13547(): pass

    label("Function_142_13547")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x323, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_13740")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1366E")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The old abandoned mine gate is tightly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FThere was a request saying that a Wanted Monster \x01",
            "had appeared in the old abandoned mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FMaybe it would be better to consult\x01",
            "with the Town Mayor before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1373B")

    label("loc_1366E")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The old abandoned mine gate is tightly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FThere was a request saying that a\x01",
            "Wanted Monster had appeared...\x01",
            "We don't have a spare key.\x02\x03",
            "Let's consult with the Town Mayor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1373B")

    Jump("loc_137D0")

    label("loc_13740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1378F")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The old abandoned mine gate is tightly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_137D0")

    label("loc_1378F")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The old abandoned mine gate is tightly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_137D0")

    Jump("loc_138EF")

    label("loc_137D5")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The old abandoned mine gate is tightly shut.\x02\x03",
            "It appears it can be opened with the spare\x01",
            "key you borrowed from the Town Mayor.\x07\x00\x02",
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
            "Use The Key\x01",      # 0
            "Do Not Use\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_138EF")
    Sound(806, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate was unlocked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x14F, 4)
    SetMapObjFlags(0x5, 0x10)
    OP_65(0x6, 0x1)
    Jump("loc_138EF")

    label("loc_138EF")

    TalkEnd(0xFF)
    Return()

    # Function_142_13547 end

    SaveToFile()

Try(main)
