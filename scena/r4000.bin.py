﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r4000.bin",                # FileName
        "r4000",                    # MapName
        "r4000",                    # Location
        0x00A3,                     # MapIndex
        "ed7250",
        0x00000000,                 # Flags
        ("r4000", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x24,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 1000, 119000, 0, 0, 1, 163, 0, 2, 0, 3],
    )

    BuildStringList((
        "r4000",                  # 0
        "Randy",               # 1
        "Warrant Mireille",           # 2
        "Voice of a crew member",               # 3
        "Defense Forces soldier",             # 4
        "Defense Forces soldier",             # 5
        "Defense Forces soldier",             # 6
        "Defense Forces soldier",             # 7
        "Defense Forces soldier",             # 8
        "Defense Forces soldier",             # 9
        "Defense Forces soldier",             # 10
        "Defense Forces soldier",             # 11
        "Defense Forces soldier",             # 12
        "Defense Forces soldier",             # 13
        "Defense Forces soldier",             # 14
        "Defense Forces soldier",             # 15
        "Havanellian",           # 16
        "Havanellian",           # 17
        "Gante",                 # 18
        "Gante",                 # 19
        "car",                     # 20
        "Armored car",                 # 21
        "Eidolon",                   # 22
        "SE control",                 # 23
        "br4000",                 # 24
        "br4000",                 # 25
        "br4000",                 # 26
        "br4000",                 # 27
        "br4000",                 # 28
        "br4000",                 # 29
        "br4000",                 # 30
        "br4000",                 # 31
        "Crossbell City · Belgard gate towards the gate",# 32
        "To the police school",           # 33
    ))

    ATBonus("ATBonus_800", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_820", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_5B70", 2,   2,   0,   4,   3,   0,   3)
    Sepith("Sepith_5B78", 4,   2,   3,   2,   1,   1,   1)
    Sepith("Sepith_5B88", 5,   0,   0,   3,   3,   3,   0)
    Sepith("Sepith_5B80", 2,   2,   0,   2,   2,   2,   4)

    MonsterBattlePostion("MonsterBattlePostion_860", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_864", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_868", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_86C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_870", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_874", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_878", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_87C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_8C4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_8C8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_8CC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_8D0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_8D4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_8D8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8DC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_840", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_844", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_848", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_84C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_850", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_854", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_858", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_85C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8FC", 0, 0, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_900", 0x0000, 51, 6, 60, 8, 1, 25, 0, "br4000", "Sepith_5B70", 20, 40, 30, 10,
        (
            ("ms78900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms78900.dat", "ms78900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms78900.dat", "ms78900.dat", "ms78900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms78900.dat", "ms78900.dat", "ms78900.dat", "ms78900.dat", 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
        )
    )

    BattleInfo(
        "BattleInfo_9C8", 0x0000, 51, 6, 60, 8, 1, 35, 0, "br4000", "Sepith_5B78", 20, 40, 30, 10,
        (
            ("ms84700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms84700.dat", "ms84700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms84700.dat", "ms84700.dat", "ms84700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms84700.dat", "ms84700.dat", "ms84700.dat", "ms84700.dat", 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
        )
    )

    BattleInfo(
        "BattleInfo_B58", 0x0000, 51, 6, 60, 8, 1, 40, 0, "br4000", "Sepith_5B88", 20, 40, 30, 10,
        (
            ("ms81600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms81600.dat", "ms81600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms81600.dat", "ms81600.dat", "ms81600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms81600.dat", "ms81600.dat", "ms81600.dat", "ms81600.dat", 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
        )
    )

    BattleInfo(
        "BattleInfo_A90", 0x0000, 51, 6, 60, 8, 1, 30, 0, "br4000", "Sepith_5B80", 20, 30, 30, 20,
        (
            ("ms78600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms78600.dat", "ms78600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms78600.dat", "ms78600.dat", "ms78600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms78600.dat", "ms78600.dat", "ms83000.dat", "ms78600.dat", 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
        )
    )

    BattleInfo(
        "BattleInfo_CA8", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br4000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms81101.dat", "ms81101.dat", "ms81101.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7451", "ed7453", "ATBonus_820"),
            (),
            (),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_C20", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br4000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms78700.dat", "ms78700.dat", "ms78700.dat", "ms78700.dat", "ms78700.dat", "ms78700.dat", "ms78700.dat", "ms78700.dat", "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7453", "ed7453", "ATBonus_800"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C64", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br4000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7453", "ed7453", "ATBonus_800"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_CEC", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br4000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88901.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8E0", "MonsterBattlePostion_8C0", "ed7454", "ed7453", "ATBonus_820"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
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
        "monster/ch78950.itc",               # 10
        "monster/ch78951.itc",               # 11
        "monster/ch84750.itc",               # 12
        "monster/ch84751.itc",               # 13
        "monster/ch78650.itc",               # 14
        "monster/ch78651.itc",               # 15
        "monster/ch81650.itc",               # 16
        "monster/ch81651.itc",               # 17
        "monster/ch78750.itc",               # 18
        "monster/ch78751.itc",               # 19
        "monster/ch60750.itc",               # 1A
        "monster/ch60750.itc",               # 1B
        "monster/ch81150.itc",               # 1C
        "monster/ch81151.itc",               # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(56250,   4294967287, 46669,   270,  485,  0x0, 0,   24,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294947006, 4294967287, 4294920067, 270,  485,  0x0, 0,   24,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(56250,   4294967287, 46669,   270,  485,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294947006, 4294967287, 4294920067, 270,  485,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4040,    71340,   0,       0x101013B,    "BattleInfo_900", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(54290,   59400,   0,       0x101010E,    "BattleInfo_9C8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(45430,   35760,   0,       0x101007C,    "BattleInfo_B58", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(78720,   46080,   2000,    0x10100FA,    "BattleInfo_A90", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(47580,   4294935526, 0,       0x101015E,    "BattleInfo_900", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(5940,    4294916316, 0,       0x101014E,    "BattleInfo_9C8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294961316, 4294926066, 0,       0x10100AA,    "BattleInfo_B58", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294947976, 4294900426, 0,       0x101015E,    "BattleInfo_900", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(81820,   47520,   2000,    0x18500E1,    "BattleInfo_CA8", 0,   28,  0xFFFF, 8,  9)

    DeclEvent(0x0000, 0, 12,  32.0,                  14.0,                  -1.0,                  2500.0,                [0.05000000074505806,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.600000023841858,    -2.799999952316284,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 16,  32.0,                  14.0,                  -1.0,                  2500.0,                [0.05000000074505806,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.600000023841858,    -2.799999952316284,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 18,  38.0,                  -9.0,                  -1.0,                  900.0,                 [0.047140561044216156, -0.17677630484104156,  0.0,                   0.0,                   0.047140348702669144,  0.17677709460258484,   -0.0,                  0.0,                   -0.0,                  -0.0,                  0.20000000298023224,   0.0,                   -1.367078185081482,    8.308493614196777,     0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 9,   81.81999969482422,     47.52000045776367,     1.0,                   16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -10.227499961853027,   -5.940000057220459,    -0.25,                 1.0])
    DeclEvent(0x0040, 0, 10,  52.369998931884766,    46.08000183105469,     0.0,                   16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -6.546249866485596,    -5.760000228881836,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 37,  40.619998931884766,    -11.300000190734863,   -1.0,                  225.0,                 [-0.07071074843406677, 0.2357020378112793,    0.0,                   0.0,                   -0.07071061432361603,  -0.2357024997472763,   0.0,                   0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   2.0732405185699463,    -12.237654685974121,   0.20000001788139343,   1.0])

    DeclActor(84000,   2000,    42500,   1200,    84000,   3000,    42500,   0x007C, 0,  4,  0x0000)
    DeclActor(30020,   4294963296, 4294945296, 1200,    30020,   4294964296, 4294945296, 0x007C, 0,  5,  0x0000)
    DeclActor(56250,   4294967286, 46670,   1200,    56250,   4294967286, 46670,   0x007C, 0,  6,  0x0000)
    DeclActor(4294947006, 4294967286, 4294920066, 1200,    4294947006, 4294967286, 4294920066, 0x007C, 0,  7,  0x0000)
    DeclActor(14470,   4294963296, 7090,    1200,    14470,   4294963796, 7090,    0x007C, 0,  8,  0x0000)
    DeclActor(16890,   4294963306, 9960,    1200,    16890,   4294965306, 9960,    0x007C, 0,  36, 0x0000)

    PlaceName(0.0, 0.0, 150.0, 0x0000, 0x0000, "Crossbell City · Belgard gate towards the gate")
    PlaceName(-20.0, 0.0, -130.0, 0x0000, 0x0000, "To the police school")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 2
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9

    ScpFunction((
        "Function_0_E40",          # 00, 0
        "Function_1_E5C",          # 01, 1
        "Function_2_E7B",          # 02, 2
        "Function_3_EA1",          # 03, 3
        "Function_4_1563",         # 04, 4
        "Function_5_16B4",         # 05, 5
        "Function_6_1805",         # 06, 6
        "Function_7_1B63",         # 07, 7
        "Function_8_1EC1",         # 08, 8
        "Function_9_1F61",         # 09, 9
        "Function_10_21CD",        # 0A, 10
        "Function_11_2249",        # 0B, 11
        "Function_12_26D2",        # 0C, 12
        "Function_13_2F46",        # 0D, 13
        "Function_14_3C66",        # 0E, 14
        "Function_15_3CD7",        # 0F, 15
        "Function_16_3D5E",        # 10, 16
        "Function_17_46C7",        # 11, 17
        "Function_18_49BB",        # 12, 18
        "Function_19_5494",        # 13, 19
        "Function_20_54E3",        # 14, 20
        "Function_21_5576",        # 15, 21
        "Function_22_55A4",        # 16, 22
        "Function_23_55D2",        # 17, 23
        "Function_24_5600",        # 18, 24
        "Function_25_563D",        # 19, 25
        "Function_26_567A",        # 1A, 26
        "Function_27_56B7",        # 1B, 27
        "Function_28_56D6",        # 1C, 28
        "Function_29_578B",        # 1D, 29
        "Function_30_5840",        # 1E, 30
        "Function_31_58DE",        # 1F, 31
        "Function_32_59ED",        # 20, 32
        "Function_33_5A03",        # 21, 33
        "Function_34_5A13",        # 22, 34
        "Function_35_5A4B",        # 23, 35
        "Function_36_5A83",        # 24, 36
        "Function_37_5ADF",        # 25, 37
    ))


    def Function_0_E40(): pass

    label("Function_0_E40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E5B")
    OP_A1(0xFE, 0x320, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_E40")

    label("loc_E5B")

    Return()

    # Function_0_E40 end

    def Function_1_E5C(): pass

    label("Function_1_E5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E7A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_E5C")

    label("loc_E7A")

    Return()

    # Function_1_E5C end

    def Function_2_E7B(): pass

    label("Function_2_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E8A")
    ClearScenarioFlags(0x22, 0)
    Event(0, 13)

    label("loc_E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EA0")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_EA0")

    Return()

    # Function_2_E7B end

    def Function_3_EA1(): pass

    label("Function_3_EA1")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF2D100C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_EBC")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EBC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EE3")
    ModifyEventFlags(0, 4, 0x80)
    SetMapObjFlags(0x1D, 0x4)
    Jump("loc_F4C")

    label("loc_EE3")

    OP_78(0x1D, 0x1D)
    ClearMapObjFlags(0x1D, 0x4)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x8)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x1)
    SetChrPos(0x1D, 52370, 0, 46080, 270)
    OP_93(0x1D, 0x10E, 0x0)
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, 52370, 0, 46080, 3000, 3000, 90000)

    label("loc_F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F73")
    ClearChrFlags(0x27, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    SetChrFlags(0x27, 0x8000)

    label("loc_F73")

    Jump("loc_F82")

    label("loc_F78")

    SetChrFlags(0x27, 0x80)
    ModifyEventFlags(0, 3, 0x80)

    label("loc_F82")

    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_122C")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_122C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_12D1")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xC8, 0x0)
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
    Jump("loc_134F")

    label("loc_12D1")

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

    label("loc_134F")

    SoundDistance(0x7A, 0x1C55C, 0x7D0, 0xADE8, 0xC350, 0x186A0, 0x64, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1383")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1383")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_139B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_139B")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B3")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_13B3")

    ModifyEventFlags(0, 5, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13CB")
    ModifyEventFlags(1, 5, 0x80)

    label("loc_13CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13EE")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_70(0x5, 0x0)
    Jump("loc_1411")

    label("loc_13EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1407")
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_1411")

    label("loc_1407")

    SetMapObjFlags(0x6, 0x4)
    OP_70(0x5, 0x32)

    label("loc_1411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_144C")
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0xFF, "miropost00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kusari00", 0x0, 0x1)
    Jump("loc_1464")

    label("loc_144C")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFrame(0xFF, "miropost01", 0x0, 0x1)

    label("loc_1464")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 6)), scpexpr(EXPR_END)), "loc_1475")
    OP_66(0x4, 0x1)

    label("loc_1475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1487")
    OP_65(0x5, 0x1)

    label("loc_1487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149A")
    OP_70(0x0, 0x0)
    Jump("loc_149E")

    label("loc_149A")

    OP_70(0x0, 0x1E)

    label("loc_149E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B1")
    OP_70(0x1, 0x0)
    Jump("loc_14B5")

    label("loc_14B1")

    OP_70(0x1, 0x1E)

    label("loc_14B5")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1516")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 56250, -10, 46670, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1516")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1562")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -20290, -10, -47230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1562")

    Return()

    # Function_3_EA1 end

    def Function_4_1563(): pass

    label("Function_4_1563")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1663")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('魔防１', 1)"), scpexpr(EXPR_END)), "loc_15EC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E4, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_165E")

    label("loc_15EC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '魔防１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '魔防１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_165E")

    Jump("loc_16A8")

    label("loc_1663")

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

    label("loc_16A8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1563 end

    def Function_5_16B4(): pass

    label("Function_5_16B4")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B4")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_173D")
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
    SetScenarioFlags(0x1E4, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_17AF")

    label("loc_173D")

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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17AF")

    Jump("loc_17F9")

    label("loc_17B4")

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

    label("loc_17F9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16B4 end

    def Function_6_1805(): pass

    label("Function_6_1805")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19BD")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_END)), "loc_199E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1999")
    ClearScenarioFlags(0x3B, 2)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_1996")
    ClearScenarioFlags(0x39, 2)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_18BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_18BF)
    TurnDirection(0x17, 0x0, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    PlayEffect(0x7, 0x1, 0x17, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_C20", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x17, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1991")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1978")
    Call(1, 5)
    Jump("loc_1991")

    label("loc_1978")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_198E")
    Call(1, 4)
    Jump("loc_1991")

    label("loc_198E")

    Call(1, 3)

    label("loc_1991")

    Jump("loc_1999")

    label("loc_1996")

    Call(1, 1)

    label("loc_1999")

    Jump("loc_19B4")

    label("loc_199E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_19B4")
    ClearScenarioFlags(0x39, 2)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_19B4")

    TalkEnd(0xFF)
    Return()

    label("loc_19BD")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_END)), "loc_1B48")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B43")
    ClearScenarioFlags(0x3B, 2)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_1B40")
    ClearScenarioFlags(0x39, 2)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1A69():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_1A69)
    TurnDirection(0x19, 0x0, 0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    PlayEffect(0x7, 0x1, 0x19, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_C64", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3B")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B22")
    Call(1, 5)
    Jump("loc_1B3B")

    label("loc_1B22")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B38")
    Call(1, 4)
    Jump("loc_1B3B")

    label("loc_1B38")

    Call(1, 3)

    label("loc_1B3B")

    Jump("loc_1B43")

    label("loc_1B40")

    Call(1, 1)

    label("loc_1B43")

    Jump("loc_1B5E")

    label("loc_1B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_1B5E")
    ClearScenarioFlags(0x39, 2)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1B5E")

    TalkEnd(0xFF)
    Return()

    # Function_6_1805 end

    def Function_7_1B63(): pass

    label("Function_7_1B63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D1B")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_1CFC")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF7")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1CF4")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C1D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1C1D)
    TurnDirection(0x18, 0x0, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    PlayEffect(0x7, 0x1, 0x18, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_C20", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEF")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CD6")
    Call(1, 5)
    Jump("loc_1CEF")

    label("loc_1CD6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CEC")
    Call(1, 4)
    Jump("loc_1CEF")

    label("loc_1CEC")

    Call(1, 3)

    label("loc_1CEF")

    Jump("loc_1CF7")

    label("loc_1CF4")

    Call(1, 1)

    label("loc_1CF7")

    Jump("loc_1D12")

    label("loc_1CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1D12")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1D12")

    TalkEnd(0xFF)
    Return()

    label("loc_1D1B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_1EA6")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA1")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1E9E")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1DC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1DC7)
    TurnDirection(0x1A, 0x0, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    PlayEffect(0x7, 0x1, 0x1A, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_C64", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E99")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E80")
    Call(1, 5)
    Jump("loc_1E99")

    label("loc_1E80")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E96")
    Call(1, 4)
    Jump("loc_1E99")

    label("loc_1E96")

    Call(1, 3)

    label("loc_1E99")

    Jump("loc_1EA1")

    label("loc_1E9E")

    Call(1, 1)

    label("loc_1EA1")

    Jump("loc_1EBC")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1EBC")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1EBC")

    TalkEnd(0xFF)
    Return()

    # Function_7_1B63 end

    def Function_8_1EC1(): pass

    label("Function_8_1EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECF")
    Call(0, 17)
    Return()

    label("loc_1ECF")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Pass down along Zile and get off\x01",      # 0
            "Leave the spot\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F34"),
        (1, "loc_1F54"),
        (SWITCH_DEFAULT, "loc_1F60"),
    )


    label("loc_1F34")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    NewScene("r4050", 102, 0, 0)
    IdleLoop()
    Jump("loc_1F60")

    label("loc_1F54")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_1F60")

    label("loc_1F60")

    Return()

    # Function_8_1EC1 end

    def Function_9_1F61(): pass

    label("Function_9_1F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 0)), scpexpr(EXPR_END)), "loc_1F6B")
    Return()

    label("loc_1F6B")

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
        (1, "loc_204D"),
        (SWITCH_DEFAULT, "loc_2066"),
    )


    label("loc_204D")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 75460, 1500, 44120, 270)
    EventEnd(0x5)
    Return()

    label("loc_2066")

    Battle("BattleInfo_CA8", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(75460, 2500, 44120, 0)
    OP_90(0x0, 75460, 1500, 44120, 270)
    OP_90(0x1, 75460, 1500, 44120, 270)
    OP_90(0x2, 75460, 1500, 44120, 270)
    OP_90(0x3, 75460, 1500, 44120, 270)
    OP_90(0x4, 75460, 1500, 44120, 270)
    OP_90(0x5, 75460, 1500, 44120, 270)
    OP_90(0x6, 75460, 1500, 44120, 270)
    OP_90(0x7, 75460, 1500, 44120, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_2128"),
        (1, "loc_212D"),
        (SWITCH_DEFAULT, "loc_2130"),
    )


    label("loc_2128")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_212D")

    OP_B9(0x0)
    Return()

    label("loc_2130")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x27, 0x80)
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
            scpstr(SCPSTR_CODE_ITEM, '封魔之刃２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber('封魔之刃２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21D, 0)
    OP_29(0x92, 0x4, 0x2)
    OP_29(0x92, 0x4, 0x10)
    OP_29(0x92, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 3, 0x80)
    EventEnd(0x5)
    Return()

    # Function_9_1F61 end

    def Function_10_21CD(): pass

    label("Function_10_21CD")

    Battle("BattleInfo_CEC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2214")
    OP_90(0x0, 44490, 0, 47190, 270)
    EventEnd(0x5)
    SetChrFlags(0x1D, 0x8000)
    Jump("loc_2248")

    label("loc_2214")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2227")
    Jump("loc_2248")

    label("loc_2227")

    ModifyEventFlags(0, 4, 0x80)
    SetMapObjFlags(0x1D, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 3)
    EventEnd(0x5)

    label("loc_2248")

    Return()

    # Function_10_21CD end

    def Function_11_2249(): pass

    label("Function_11_2249")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    OP_11(0xB4, 0xA7, 0xB8, 0x32, 0x1F4, 0x0)
    SetChrPos(0x101, 0, 2000, 118650, 180)
    SetChrPos(0x102, 1000, 2000, 120350, 180)
    SetChrPos(0x109, -1000, 2000, 119650, 180)
    SetChrPos(0x105, 0, 2000, 121350, 180)
    FadeToBright(1000, 0)
    OP_68(-9240, 8350, 102390, 0)
    MoveCamera(96, 12, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(46020, 0)
    OP_68(-10550, 8350, 89910, 7000)
    Sleep(6000)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_11(0xB4, 0xA7, 0xB8, 0x32, 0x15E, 0x0)
    OP_68(97850, 1760, 36130, 0)
    MoveCamera(85, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(66950, 0)
    SetCameraDistance(62450, 6000)
    Sleep(5000)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_68(23320, -2600, -8460, 0)
    MoveCamera(48, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(78020, 0)
    OP_68(28640, -2600, -14370, 6000)
    Sleep(5000)
    PlaceName2(340, 200, "c_plac36", 0x0, 0)
    OP_6F(0x79)
    OP_0D()
    Sleep(4500)
    Fade(1000)
    OP_68(0, 1150, 120000, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19650, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#00105F#5PThis is the Knox Forest Zone ……\x02\x03",
            "#00108FI was listening to the story\x01",
            "You are in a quite deep place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWhew, this place\x01",
            "Do I have to walk by walking?\x02\x03",
            "#10301FIt's not really smart.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24B2():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_24B2)
    Sleep(100)

    def lambda_24C2():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_24C2)
    Sleep(100)

    def lambda_24D2():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_24D2)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#00004F#12PWell, this is also the style of the support department\x01",
            "I have no choice but to give up.\x02\x03",
            "#00000FBut Wadi, complaining about it\x01",
            "Are not you feeling awkward?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6PWell, it seems like a city urban,\x01",
            "I thought he would raise the sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PJust being thinned.\x01",
            "My feet are shaky from a little while ago.\x02\x03",
            "#10302FHugh, it is about time for the leader\x01",
            "Should I have a negative impact?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PIt seems all right …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PHehuu, shall we go ahead?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_11(0xB4, 0xA7, 0xB8, 0x32, 0xC8, 0x0)
    SetChrPos(0x0, 0, 0, 119000, 180)
    SetScenarioFlags(0x127, 1)
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0xA1, 0x1, 0x6)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_2249 end

    def Function_12_26D2(): pass

    label("Function_12_26D2")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    OP_68(29000, 800, 9000, 0)
    MoveCamera(48, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 29000, 0, 12650, 180)
    SetChrPos(0x102, 27850, 0, 13150, 180)
    SetChrPos(0x109, 30000, 0, 14350, 180)
    SetChrPos(0x105, 29000, 0, 15350, 180)
    FadeToBright(1000, 0)
    SetCameraDistance(19500, 2250)

    def lambda_277D():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_277D)

    def lambda_2792():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2792)

    def lambda_27A7():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_27A7)

    def lambda_27BC():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_27BC)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Sleep(100)

    def lambda_27F9():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27F9)
    Sleep(100)

    def lambda_2809():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2809)
    Sleep(100)

    def lambda_2819():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2819)
    WaitChrThread(0x102, 1)
    Sleep(350)

    def lambda_282D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_282D)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x102,
        "#00105F#11POh……?\x02",
    )

    CloseMessageWindow()
    OP_68(14000, -3300, 7450, 4000)
    MoveCamera(48, 21, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(26000, 4000)

    def lambda_2893():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2893)
    Sleep(100)

    def lambda_28A3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_28A3)
    Sleep(100)

    def lambda_28B3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_28B3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00100F#6PSomething, that?\x02\x03",
            "Zile is under the cliff\x01",
            "It seems they are extending ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12POh, that one\x01",
            "For survival training\x01",
            "I am about to get off at the training ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PSurvival training ……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 3000)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_68(15960, -2800, 4550, 0)
    MoveCamera(48, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    OP_68(14000, -2800, 7450, 3000)
    MoveCamera(56, 21, 0, 3000)
    SetChrPos(0x101, 17990, -4000, 3720, 270)
    SetChrPos(0x102, 18540, -4000, 1940, 270)
    SetChrPos(0x109, 16810, -4000, 2970, 270)
    SetChrPos(0x105, 17800, -4000, 1230, 270)

    def lambda_2A3B():
        OP_95(0xFE, 16720, -4000, 7260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A3B)

    def lambda_2A55():
        OP_95(0xFE, 16950, -4000, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A55)

    def lambda_2A6F():
        OP_95(0xFE, 15030, -4000, 5650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A6F)

    def lambda_2A89():
        OP_95(0xFE, 15690, -4000, 4050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2A89)
    WaitChrThread(0x109, 1)

    def lambda_2AA7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2AA7)
    WaitChrThread(0x105, 1)

    def lambda_2AB8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2AB8)
    WaitChrThread(0x101, 1)

    def lambda_2AC9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AC9)
    WaitChrThread(0x102, 1)

    def lambda_2ADA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2ADA)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10103F#11PUnder this is the forest sea\x01",
            "The visibility is bad and there is only a martial arts.\x02\x03",
            "#10100FIn such an environment,\x01",
            "With limited equipment and food only\x01",
            "I spend a few days.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00106F#11PI guess it is impossible for me …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#11PWell, I am truly amazed.\x02\x03",
            "#10302FVintage wines and\x01",
            "If a fancy hors d'oeuvres out\x01",
            "I do not mind thinking.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, at most it has cheese taste\x01",
            "It's about dry condition.\x02\x03",
            "#00008FI also worked for the investigator exam\x01",
            "I have survival training ….\x02\x03",
            "#00001FTo be honest, it was quite hard training.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D02():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D02)
    Sleep(100)

    def lambda_2D12():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D12)
    Sleep(100)

    def lambda_2D22():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2D22)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#10112F#6PHaha ……\x02\x03",
            "#10105FBy the way, Randy - senpai,\x01",
            "Are they doing the training here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#5PReally……\x01",
            "There is a possibility.\x02\x03",
            "#00000FAt another training site\x01",
            "There is also possibility of doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#12PCertainly he, the guards manipulated\x01",
            "Are you going out for rehab?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x102,
        (
            "#00104F#11PYes, at the request of the new Guard Command.\x02\x03",
            "#00102FTraining is over soon\x01",
            "I hope returning ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5POh … That's right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 16250, -4000, 5400, 270)
    SetScenarioFlags(0x127, 2)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_12_26D2 end

    def Function_13_2F46(): pass

    label("Function_13_2F46")

    EventBegin(0x0)
    OP_E2(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    LoadChrToIndex("chr/ch12300.itc", 0x1E)
    LoadChrToIndex("chr/ch32600.itc", 0x1F)
    LoadChrToIndex("apl/ch51105.itc", 0x20)
    LoadChrToIndex("apl/ch51106.itc", 0x21)
    SoundLoad(468)
    SoundLoad(2750)
    SoundLoad(2746)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11000.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07900.itp")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 17500, -4000, 4500, 45)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 16000, -4000, 5000, 90)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0x1B, 0x80)
    OP_78(0x4, 0x1B)
    OP_49()
    SetChrPos(0x1B, -7660, 0, -47850, 90)
    OP_D5(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0xB5, 0xF0, 0x1, 0x20)
    FadeToBright(1000, 0)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    BeginChrThread(0x1B, 3, 0, 14)
    OP_68(41840, -1250, -23020, 0)
    MoveCamera(60, 9, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(68590, 0)
    OP_68(41840, -3250, -23020, 6000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    EndChrThread(0x1B, 0x3)
    BeginChrThread(0x1B, 3, 0, 15)
    OP_68(37650, 1750, -4210, 0)
    MoveCamera(32, 12, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25880, 0)
    StopSound(468, 1000, 60)
    OP_68(27860, 1750, 1910, 7500)
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x8,
        "Voice of a young man",
        (
            "#2750V#2P#30WHu!\x01",
            "It's a fucking power car.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xABE)
    OP_C9(0x1, 0x80000000)
    Fade(1000)
    OP_68(15900, -1800, 4200, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19650, 0)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    OP_68(15900, -2700, 4200, 3000)
    OP_6F(0x79)
    OP_0D()
    Fade(350)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x9, 0x1)
    OP_0D()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "Randy, you …\x02\x03",
            "Even though the survival training on the 5th day is on end\x01",
            "Why is that so fine ……\x02",
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
    TurnDirection(0x8, 0x9, 500)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x8,
        (
            "Haha, I'm honest.\x02\x03",
            "Take a shower together\x01",
            "I'd rather sleep in the same bed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_63(0x9, 0xC8, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#07906F#6PEven ….\x01",
            "Just say stupid things.\x02\x03",
            "#07900FEven so ……\x01",
            "It was a car I had never seen before.\x02\x03",
            "It was introduced to the police\x01",
            "Is it a new model per Verne?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11004F#11PNo, it looks like ZCF made.\x02\x03",
            "#11002FNo wonder that such a car seems to be high\x01",
            "I wish you to be paid to the support section.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0xC8, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#07905F#6PWhat is ZCF …?\x01",
            "I should not have made a guided car.\x02\x03",
            "#07900FAnd why to your department\x01",
            "Do you understand that it was paid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11005F#11PNo, Lloyd and Miss\x01",
            "I was sitting in the car.\x02\x03",
            "#11004FThe section chief and the rookie were also on board\x01",
            "Perhaps, it was paid to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#07906F#6POkay, so far away\x01",
            "You can check in the car …\x02\x03",
            "#07902FI mean ZCF made\x01",
            "Because it was written on the car body?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11000F#11POh, beside the body\x01",
            "The emblem was engraved.\x02\x03",
            "#11009FNo, thanks\x01",
            "I am looking forward to go home!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0xC8, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#07908F#6P…… Hey, Randy.\x02\x03",
            "#07900FAs it is this way\x01",
            "Would you like to come back to the guard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11005F#11PWhat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#07906F#6PBecause, your ability\x01",
            "Even if you think about it, it's for military ……\x02\x03",
            "#07908FAnd rifle\x01",
            "With this exercise properly ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11004F#11PHahaha ….\x01",
            "It is an exercise using simulated bullets.\x02\x03",
            "#11000FIt is not a usable thing in the actual war\x01",
            "You know too, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#07906F#6PBut,\x02",
    )

    CloseMessageWindow()
    OP_68(15350, -2700, 4200, 1000)

    def lambda_3872():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3872)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    Fade(250)
    Sound(898, 0, 100, 0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrChipByIndex(0x8, 0x21)
    OP_A1(0x8, 0x1F4, 0x5, 0x1, 0x0, 0x1, 0x0, 0x1)
    OP_0D()

    ChrTalk(
        0x9,
        "#07911F#6P……Ah……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11004F#11PWell, when you become a pinch\x01",
            "Because I'll rush you at any time.\x02\x03",
            "#11002FLet's go with the finish of rehabilitation training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#07911F#6PI know!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0xC8, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)
    Fade(250)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x800)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_68(12000, -2800, 4200, 3000)
    SetCameraDistance(21650, 3000)
    OP_9D(0x9, 0x3A98, 0xFFFFF060, 0x1388, 0x12C, 0xDAC)
    Sound(38, 0, 100, 0)
    Sleep(250)
    OP_93(0x9, 0x10E, 0x2EE)
    OP_9B(0x0, 0x9, 0x0, 0x7D0, 0xBB8, 0x0)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#07907F#11P#4S── It's late!\x01",
            "How long will it go!\x02\x03",
            "#4SIn ten minutes we all have to climb\x01",
            "I will extend it for another half day!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 3000, -8000, 0, 0)

    ChrTalk(
        0xA,
        "#5P#2SHime yeah … …!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrPos(0xA, 0, -8000, 0, 0)

    ChrTalk(
        0xA,
        "#5P#2SYes, Yes Mam!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrPos(0xA, 2000, -8000, 0, 0)

    ChrTalk(
        0xA,
        "#5P#2SI do not want snakes anymore!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrPos(0xA, 1000, -8000, 0, 0)

    ChrTalk(
        0xA,
        (
            "#5P#2SDo not be dull!\x01",
            "Climb quickly and safely!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(14500, -2800, 4200, 2000)
    MoveCamera(55, 22, 0, 2000)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    Sound(2366, 255, 100, 0)
    Sleep(800)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#11006F#11PHello, it is a demon superior.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#07907F#6P#4SNoisy, idiot RANDY!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(22000, 1500)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 1)
    NewScene("r1020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2F46 end

    def Function_14_3C66(): pass

    label("Function_14_3C66")

    SetChrPos(0xFE, -7660, 0, -47850, 0)
    Sound(468, 2, 60, 0)
    Sound(457, 0, 80, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 17500, 0, -45440)
    OP_9F(0x1, 39450, 0, -36110)
    OP_9F(0x1, 46840, 0, -22020)
    OP_9F(0x1, 32759, 0, -4480)
    OP_9F(0x1, 29580, 0, 13540)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    Return()

    # Function_14_3C66 end

    def Function_15_3CD7(): pass

    label("Function_15_3CD7")

    SetChrPos(0xFE, 47350, 0, -20530, 0)
    Sound(458, 0, 90, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 36220, 0, -8050)
    OP_9F(0x1, 30910, 0, 370)
    OP_9F(0x1, 30550, 0, 17420)
    OP_9F(0x1, 46710, 0, 33130)
    OP_9F(0x1, 49060, 0, 52000)
    OP_9F(0x1, 35830, 0, 65400)
    OP_9F(0x1, 23510, 0, 67300)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    Return()

    # Function_15_3CD7 end

    def Function_16_3D5E(): pass

    label("Function_16_3D5E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    OP_68(30050, 1050, 16250, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 32229, 0, 18430, 225)
    SetChrPos(0x102, 32189, 0, 19730, 225)
    SetChrPos(0x103, 33730, 0, 18580, 225)
    SetChrPos(0x104, 34930, 0, 20580, 225)
    SetChrPos(0x109, 33580, 0, 20330, 225)
    SetChrPos(0x105, 34580, 0, 22030, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(19000, 2500)

    def lambda_3E3F():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E3F)
    Sleep(0)

    def lambda_3E57():
        OP_9B(0x0, 0x102, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E57)
    Sleep(0)

    def lambda_3E6F():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3E6F)
    Sleep(0)

    def lambda_3E87():
        OP_9B(0x0, 0x104, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3E87)
    Sleep(0)

    def lambda_3E9F():
        OP_9B(0x0, 0x109, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E9F)
    Sleep(0)

    def lambda_3EB7():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3EB7)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(18510, -2700, 8680, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21350, 0)
    SetChrPos(0x101, 18550, -4000, -9250, 0)
    SetChrPos(0x102, 19600, -4000, -9500, 0)
    SetChrPos(0x103, 18250, -4000, -10400, 0)
    SetChrPos(0x104, 19100, -4000, -11250, 0)
    SetChrPos(0x109, 18150, -4000, -11700, 0)
    SetChrPos(0x105, 20100, -4000, -11200, 0)
    OP_68(18000, -2700, 200, 10000)
    Sleep(6000)

    def lambda_4003():
        OP_9B(0x0, 0x101, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4003)
    Sleep(100)

    def lambda_401B():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_401B)
    Sleep(100)

    def lambda_4033():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4033)
    Sleep(100)

    def lambda_404B():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_404B)
    Sleep(100)

    def lambda_4063():
        OP_9B(0x0, 0x109, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4063)
    Sleep(100)

    def lambda_407B():
        OP_9B(0x0, 0x105, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_407B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00013F#12P…… After all this also\x01",
            "She seems to have just been destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PI mean …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(13350, -2900, 7950, 0)
    MoveCamera(90, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    SetChrPos(0x101, 17370, -4000, 5880, 315)
    SetChrPos(0x102, 17370, -4000, 3780, 315)
    SetChrPos(0x103, 15720, -4000, 4180, 315)
    SetChrPos(0x104, 15520, -4000, 3030, 315)
    SetChrPos(0x109, 18220, -4000, 4830, 315)
    SetChrPos(0x105, 17020, -4000, 2280, 315)
    OP_68(14450, -2900, 6600, 3000)

    def lambda_41B5():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_41B5)
    Sleep(20)

    def lambda_41CD():
        OP_9B(0x0, 0x102, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_41CD)
    Sleep(20)

    def lambda_41E5():
        OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_41E5)
    Sleep(20)

    def lambda_41FD():
        OP_9B(0x0, 0x104, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_41FD)
    Sleep(20)

    def lambda_4215():
        OP_9B(0x0, 0x109, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4215)
    Sleep(20)

    def lambda_422D():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_422D)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#00101F#11P… … down this down\x01",
            "I wonder if I went there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PThere is no mistake.\x01",
            "I feel a sign from the lower side.\x02\x03",
            "#00208F……in addition……\x01",
            "I feel something strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PStrange sign?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#5PBelow this is a survival training ground.\x02\x03",
            "#10101FThere is almost no human hands in it\x01",
            "The trees are spreading … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#11P…… If you chase after you prepare\x01",
            "It seems necessary to decide.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PAh……\x01",
            "I got off once at the police school training\x01",
            "It was a difficult place with poor visibility.\x02\x03",
            "#00001FIt will be difficult indeed,\x01",
            "Eli, Tio, Wadi ─\x02",
        )
    )

    CloseMessageWindow()

    def lambda_446D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_446D)
    Sleep(50)

    def lambda_447D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_447D)
    Sleep(50)

    def lambda_448D():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_448D)
    Sleep(50)

    def lambda_449D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_449D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        "#00106F#11PFuu, what are you now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#12POnly Lloyds\x01",
            "I am worried about letting go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#11PAt least with regard to Arts\x01",
            "We are good at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PWow ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#12PWell, it's definitely a tough place\x01",
            "If you cooperate it will do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#11PYes, let's get together!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P─ ─ It turned out.\x02\x03",
            "#00001FI do not know what enemies are.\x01",
            "Let's get down after preparing everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PIt is okay.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(20650, 1000)
    OP_6F(0x79)
    OP_0D()
    SetChrPos(0x0, 16100, -4000, 5850, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x163, 6)
    OP_29(0xA8, 0x1, 0x9)
    ModifyEventFlags(0, 1, 0x80)
    OP_66(0x4, 0x1)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_3D5E end

    def Function_17_46C7(): pass

    label("Function_17_46C7")

    EventBegin(0x0)
    OP_E2(0x3)
    Fade(1000)
    OP_68(14450, -2900, 6600, 0)
    MoveCamera(90, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20750, 0)
    SetChrPos(0x101, 15250, -4000, 8000, 225)
    SetChrPos(0x102, 15250, -4000, 5900, 0)
    SetChrPos(0x103, 13600, -4000, 6300, 45)
    SetChrPos(0x104, 13400, -4000, 5150, 45)
    SetChrPos(0x109, 16100, -4000, 6950, 315)
    SetChrPos(0x105, 14900, -4000, 4400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(20150, 1500)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Take the zile and get off the trees\x01",      # 0
            "Leave the spot\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_47E8"),
        (1, "loc_498C"),
        (SWITCH_DEFAULT, "loc_49BA"),
    )


    label("loc_47E8")


    ChrTalk(
        0x101,
        (
            "#00003F#5P── Alright, first of all\x01",
            "Randy will come down with me.\x02\x03",
            "#00001FThen, in order of Eli, Tio, Wadi\x01",
            "Finally Noel comes down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#11PI knew it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#11POK!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#12PYes, before you get off you command\x01",
            "Is not it better to contact you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5POh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#11PAs the target for recovery comes along,\x01",
            "It seems better to have you come.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(19900, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("r4050", 0, 0, 0)
    IdleLoop()
    Jump("loc_49BA")

    label("loc_498C")

    SetChrPos(0x0, 16100, -4000, 5850, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_49BA")

    label("loc_49BA")

    Return()

    # Function_17_46C7 end

    def Function_18_49BB(): pass

    label("Function_18_49BB")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x1)
    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch00056.itc", 0x22)
    LoadChrToIndex("chr/ch41550.itc", 0x23)
    LoadChrToIndex("chr/ch41551.itc", 0x24)
    SoundLoad(2093)
    SetChrPos(0x101, 43350, 0, -15550, 315)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -4200, 0, 94000, 180)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -2800, 0, 94000, 180)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -4200, 0, 97000, 180)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -2800, 0, 97000, 180)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -4200, 0, 100000, 180)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2800, 0, 100000, 180)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -10000, 0, -50000, 45)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -11000, 0, -51000, 45)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -12000, 0, -52000, 45)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -11200, 0, -48800, 45)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -12200, 0, -49800, 45)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -13200, 0, -50800, 45)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x7, 0x1C)
    OP_49()
    SetChrPos(0x1C, -3350, 0, 88050, 165)
    OP_D5(0x1C, 0x0, 0x28488, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "mark00", 0x0, 0x1)
    SetMapObjFrame(0x7, "mark01", 0x1, 0x1)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x1, 0x20)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4C4B")
    FadeToBright(0, 0)
    Jump("loc_509F")

    label("loc_4C4B")

    OP_68(36950, 900, -7950, 0)
    MoveCamera(15, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23150, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(18150, 2500)

    def lambda_4C90():
        OP_95(0xFE, 38000, 0, -9000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C90)
    WaitChrThread(0x101, 1)
    StopBGM(0x7D0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(2093, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00011F#11P#10ACrap\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7453", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1C5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    OP_68(-600, 300, 86750, 0)
    MoveCamera(27, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(25000, 5000)
    BeginChrThread(0x1C, 3, 0, 19)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0xC, 3, 0, 21)
    BeginChrThread(0xD, 3, 0, 22)
    BeginChrThread(0xE, 3, 0, 22)
    BeginChrThread(0xF, 3, 0, 23)
    BeginChrThread(0x10, 3, 0, 23)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(38000, 900, -9000, 0)
    MoveCamera(15, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18250, 0)
    EndChrThread(0x1C, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x3)
    OP_0D()
    OP_9B(0x1, 0x101, 0xB4, 0x12C, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#00010F#11PCut, somehow hidden\x01",
            "I have to go through … …!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1E, 1, 0, 33)
    SetChrPos(0x11, 38000, 0, -37000, 0)

    NpcTalk(
        0x11,
        "Voice of a man",
        "#2STarget spotted!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(-6600, 1500, -44000, 0)
    MoveCamera(75, 12, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(19500, 0)
    OP_68(-9600, 1500, -47000, 1500)
    OP_93(0x101, 0x10E, 0x0)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x11, -10000, 0, -50000, 45)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x11,
        "#11PIt's Lloyd Bannings!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11PGet him!\x02",
    )

    CloseMessageWindow()
    OP_68(-9600, 3500, -47000, 5000)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    BeginChrThread(0x11, 3, 0, 27)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    BeginChrThread(0x12, 3, 0, 27)
    Sleep(50)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 3, 0, 27)
    Sleep(50)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    BeginChrThread(0x14, 3, 0, 27)
    Sleep(50)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 3, 0, 27)
    Sleep(50)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    BeginChrThread(0x16, 3, 0, 27)
    Sleep(2500)
    Fade(500)
    OP_68(38000, 900, -9000, 0)
    MoveCamera(15, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18250, 0)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x3)
    OP_93(0x101, 0x87, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00007F#5PDamn\x01",
            "When it comes to this!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_5A()
    Fade(500)
    OP_68(27750, 3000, -13450, 0)
    MoveCamera(36, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12250, 0)
    OP_68(27750, 1800, -28450, 6000)
    MoveCamera(8, 19, 0, 6000)
    OP_6E(650, 6000)
    SetCameraDistance(18250, 6000)
    BeginChrThread(0x101, 3, 0, 30)
    OP_0D()
    Sleep(4500)

    label("loc_509F")

    Fade(1000)
    OP_68(27650, 4900, 9000, 0)
    MoveCamera(36, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12250, 0)
    OP_68(27650, 2900, 2000, 6500)
    MoveCamera(24, 15, 0, 6500)
    SetCameraDistance(16250, 6500)
    EndChrThread(0x101, 0x3)
    SetChrFlags(0x101, 0x8)
    SetChrPos(0xB, 45000, 0, 35000, 225)
    SetChrPos(0xC, 46000, 0, 34000, 225)
    SetChrPos(0xD, 45750, 0, 36500, 225)
    SetChrPos(0xE, 46750, 0, 35500, 225)
    SetChrPos(0xF, 46500, 0, 38000, 225)
    SetChrPos(0x10, 47500, 0, 37000, 225)
    BeginChrThread(0x1C, 3, 0, 20)
    BeginChrThread(0x1E, 1, 0, 32)
    BeginChrThread(0x1E, 2, 0, 34)
    BeginChrThread(0x1E, 3, 0, 35)
    BeginChrThread(0xB, 3, 0, 24)
    Sleep(50)
    BeginChrThread(0xC, 3, 0, 24)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 26)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(29300, 1700, -8500, 0)
    MoveCamera(36, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    OP_68(27750, -2000, -24450, 7000)
    MoveCamera(36, 21, 0, 7000)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x3)
    SetChrPos(0xB, 28950, 0, -4670, 225)
    SetChrPos(0xC, 30130, 0, -3800, 225)
    SetChrPos(0xD, 28780, 0, -3000, 225)
    SetChrPos(0xE, 30120, 0, -2240, 225)
    SetChrPos(0xF, 28760, 0, -1500, 225)
    SetChrPos(0x10, 30130, 0, -670, 225)
    BeginChrThread(0xB, 3, 0, 29)
    BeginChrThread(0xC, 3, 0, 28)
    BeginChrThread(0xD, 3, 0, 29)
    BeginChrThread(0xE, 3, 0, 28)
    BeginChrThread(0xF, 3, 0, 29)
    BeginChrThread(0x10, 3, 0, 28)
    SetChrPos(0x11, 40660, 0, -10310, 225)
    SetChrPos(0x12, 41100, 0, -13330, 225)
    SetChrPos(0x13, 41770, 0, -11520, 225)
    SetChrPos(0x14, 39940, 0, -12050, 225)
    SetChrPos(0x15, 42940, 0, -12800, 225)
    SetChrPos(0x16, 42250, 0, -14440, 225)
    BeginChrThread(0x11, 3, 0, 29)
    BeginChrThread(0x12, 3, 0, 28)
    BeginChrThread(0x13, 3, 0, 29)
    BeginChrThread(0x14, 3, 0, 28)
    BeginChrThread(0x15, 3, 0, 29)
    BeginChrThread(0x16, 3, 0, 28)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(14500, -2800, 7000, 0)
    MoveCamera(112, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(19000, 0)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x3)
    SetChrPos(0xB, 18800, -4000, -12200, 0)
    SetChrPos(0xC, 18800, -4000, -12200, 0)
    SetChrPos(0xD, 18800, -4000, -12200, 0)
    SetChrPos(0xE, 18800, -4000, -12200, 0)
    SetChrPos(0xF, 18800, -4000, -12200, 0)
    SetChrPos(0x10, 18800, -4000, -12200, 0)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x3)
    SetChrPos(0x11, 18800, -4000, -12200, 0)
    SetChrPos(0x12, 18800, -4000, -12200, 0)
    SetChrPos(0x13, 18800, -4000, -12200, 0)
    SetChrPos(0x14, 18800, -4000, -12200, 0)
    SetChrPos(0x15, 18800, -4000, -12200, 0)
    SetChrPos(0x16, 18800, -4000, -12200, 0)
    ClearChrFlags(0x101, 0x8)
    BeginChrThread(0x101, 3, 0, 31)
    OP_0D()
    WaitChrThread(0x101, 3)
    EndChrThread(0x1E, 0x2)
    EndChrThread(0x1E, 0x3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("r4050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_49BB end

    def Function_19_5494(): pass

    label("Function_19_5494")

    Sound(471, 0, 100, 0)
    SetChrPos(0xFE, -3350, 0, 88050, 180)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -750, 0, 78200)
    OP_9F(0x1, 4700, 0, 71000)
    OP_9F(0x1, 19600, 0, 67750)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    Return()

    # Function_19_5494 end

    def Function_20_54E3(): pass

    label("Function_20_54E3")

    OP_71(0x7, 0xB5, 0xF0, 0x1, 0x20)
    SetChrPos(0xFE, 41710, 0, 28360, 225)
    OP_D5(0x1C, 0x0, 0x36EE8, 0x0, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 32409, 0, 19900)
    OP_9F(0x1, 32299, 0, 10000)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xBB8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x64, 0x3E8, 0x1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x8)
    Return()

    # Function_20_54E3 end

    def Function_21_5576(): pass

    label("Function_21_5576")

    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    Return()

    # Function_21_5576 end

    def Function_22_55A4(): pass

    label("Function_22_55A4")

    OP_9B(0x0, 0xFE, 0x0, 0x32C8, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    Return()

    # Function_22_55A4 end

    def Function_23_55D2(): pass

    label("Function_23_55D2")

    OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    Return()

    # Function_23_55D2 end

    def Function_24_5600(): pass

    label("Function_24_5600")

    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x2EE0, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x1F40, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x145, 0x4E20, 0x1770, 0x1)
    Return()

    # Function_24_5600 end

    def Function_25_563D(): pass

    label("Function_25_563D")

    OP_9B(0x0, 0xFE, 0x163, 0x2134, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x30D4, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2134, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x145, 0x5014, 0x1770, 0x1)
    Return()

    # Function_25_563D end

    def Function_26_567A(): pass

    label("Function_26_567A")

    OP_9B(0x0, 0xFE, 0x163, 0x2328, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x32C8, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2328, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x145, 0x5208, 0x1770, 0x1)
    Return()

    # Function_26_567A end

    def Function_27_56B7(): pass

    label("Function_27_56B7")

    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4650, 0xFA0, 0x1)
    Return()

    # Function_27_56B7 end

    def Function_28_56D6(): pass

    label("Function_28_56D6")

    OP_95(0xFE, 29190, 0, -8880, 5000, 0x0)
    OP_95(0xFE, 29980, -400, -12740, 5000, 0x0)
    OP_95(0xFE, 34550, -2000, -15540, 5000, 0x0)
    OP_95(0xFE, 36610, -2000, -20820, 5000, 0x0)
    OP_95(0xFE, 33770, -3020, -28020, 5000, 0x0)
    OP_95(0xFE, 28400, -4000, -26990, 5000, 0x0)
    OP_95(0xFE, 24370, -4000, -23110, 5000, 0x0)
    OP_95(0xFE, 19300, -4000, -14810, 5000, 0x0)
    OP_95(0xFE, 17760, -4000, -1770, 5000, 0x0)
    Return()

    # Function_28_56D6 end

    def Function_29_578B(): pass

    label("Function_29_578B")

    OP_95(0xFE, 27950, 0, -8490, 5000, 0x0)
    OP_95(0xFE, 27390, 0, -12920, 5000, 0x0)
    OP_95(0xFE, 33190, -1870, -16850, 5000, 0x0)
    OP_95(0xFE, 34620, -2000, -21300, 5000, 0x0)
    OP_95(0xFE, 32950, -3040, -26590, 5000, 0x0)
    OP_95(0xFE, 28760, -4000, -25820, 5000, 0x0)
    OP_95(0xFE, 25100, -4000, -20970, 5000, 0x0)
    OP_95(0xFE, 20880, -4000, -13050, 5000, 0x0)
    OP_95(0xFE, 19300, -4000, -860, 5000, 0x0)
    Return()

    # Function_29_578B end

    def Function_30_5840(): pass

    label("Function_30_5840")

    SetChrPos(0xFE, 33430, 0, -7320, 225)
    OP_95(0xFE, 29580, 0, -7910, 6000, 0x1)
    OP_95(0xFE, 28040, -70, -13230, 6000, 0x1)
    OP_95(0xFE, 33910, -2000, -16410, 6000, 0x1)
    OP_95(0xFE, 35650, -2050, -21630, 6000, 0x1)
    OP_95(0xFE, 33250, -3090, -27780, 6000, 0x1)
    OP_95(0xFE, 29550, -4000, -28490, 6000, 0x1)
    OP_95(0xFE, 24450, -4000, -21310, 6000, 0x0)
    Return()

    # Function_30_5840 end

    def Function_31_58DE(): pass

    label("Function_31_58DE")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, 20950, -4000, -6150, 225)
    OP_95(0xFE, 18350, -4000, 650, 6000, 0x1)
    OP_95(0xFE, 14850, -4000, 8050, 6000, 0x0)
    Sleep(50)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)
    Fade(350)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 13000, -4500, 8400, 225)
    OP_93(0xFE, 0x87, 0x0)
    SetChrSubChip(0xFE, 0x2)
    OP_0D()
    Sleep(200)
    OP_98(0xFE, 0x0, 0xFFFFFD12, 0x0, 0x7D0, 0x0)
    Sleep(350)
    OP_98(0xFE, 0x0, 0xFFFFFD12, 0x0, 0x7D0, 0x0)
    Sleep(350)
    OP_98(0xFE, 0x0, 0xFFFFFD12, 0x0, 0x7D0, 0x0)
    Sleep(350)
    OP_98(0xFE, 0x0, 0xFFFFFD12, 0x0, 0x7D0, 0x0)
    Sleep(350)
    OP_98(0xFE, 0x0, 0xFFFFFD12, 0x0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_31_58DE end

    def Function_32_59ED(): pass

    label("Function_32_59ED")

    Sound(465, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(3000)
    Sound(487, 0, 100, 0)
    Return()

    # Function_32_59ED end

    def Function_33_5A03(): pass

    label("Function_33_5A03")

    Sound(910, 0, 30, 0)
    Sleep(800)
    Sound(909, 0, 30, 0)
    Return()

    # Function_33_5A03 end

    def Function_34_5A13(): pass

    label("Function_34_5A13")

    Sleep(2300)

    label("loc_5A16")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A4A")
    Sound(909, 0, 40, 0)
    Sleep(1200)
    Sound(909, 0, 40, 0)
    Sleep(900)
    Sound(909, 0, 40, 0)
    Sleep(1600)
    Sound(909, 0, 40, 0)
    Sleep(950)
    Jump("loc_5A16")

    label("loc_5A4A")

    Return()

    # Function_34_5A13 end

    def Function_35_5A4B(): pass

    label("Function_35_5A4B")

    Sleep(3000)

    label("loc_5A4E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A82")
    Sound(910, 0, 40, 0)
    Sleep(700)
    Sound(910, 0, 40, 0)
    Sleep(1600)
    Sound(910, 0, 40, 0)
    Sleep(1400)
    Sound(910, 0, 40, 0)
    Sleep(1800)
    Jump("loc_5A4E")

    label("loc_5A82")

    Return()

    # Function_35_5A4B end

    def Function_36_5A83(): pass

    label("Function_36_5A83")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Before this, survival training grounds\x01",
            "Crossbell Police School\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_5A83 end

    def Function_37_5ADF(): pass

    label("Function_37_5ADF")

    EventBegin(0x1)
    OP_E2(0x3)

    ChrTalk(
        0x101,
        (
            "#00001FThe demon in question is not this -\x01",
            "Let's head to the survival training ground under the cliff.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 37840, 0, -8070, 319)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_37_5ADF end

    SaveToFile()

Try(main)
