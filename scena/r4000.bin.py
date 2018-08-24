from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Randy",                  # 1
        "Warrant Officer Mireille",# 2
        "CGF Member's Voice",     # 3
        "State Guard Soldier",    # 4
        "State Guard Soldier",    # 5
        "State Guard Soldier",    # 6
        "State Guard Soldier",    # 7
        "State Guard Soldier",    # 8
        "State Guard Soldier",    # 9
        "State Guard Soldier",    # 10
        "State Guard Soldier",    # 11
        "State Guard Soldier",    # 12
        "State Guard Soldier",    # 13
        "State Guard Soldier",    # 14
        "State Guard Soldier",    # 15
        "ハバネリアン",           # 16
        "ハバネリアン",           # 17
        "ガンテ",                 # 18
        "ガンテ",                 # 19
        "車",                     # 20
        "Armored Vehicle",        # 21
        "Cryptid",                # 22
        "SE制御",                 # 23
        "br4000",                 # 24
        "br4000",                 # 25
        "br4000",                 # 26
        "br4000",                 # 27
        "br4000",                 # 28
        "br4000",                 # 29
        "br4000",                 # 30
        "br4000",                 # 31
        "To Crossbell City/Bellguard Gate",# 32
        "To Police Academy",      # 33
    ))

    ATBonus("ATBonus_800", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_820", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_5DA2", 2,   2,   0,   4,   3,   0,   3)
    Sepith("Sepith_5DAA", 4,   2,   3,   2,   1,   1,   1)
    Sepith("Sepith_5DBA", 5,   0,   0,   3,   3,   3,   0)
    Sepith("Sepith_5DB2", 2,   2,   0,   2,   2,   2,   4)

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
        "BattleInfo_900", 0x0000, 51, 6, 60, 8, 1, 25, 0, "br4000", "Sepith_5DA2", 20, 40, 30, 10,
        (
            ("ms78900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms78900.dat", "ms78900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms78900.dat", "ms78900.dat", "ms78900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms78900.dat", "ms78900.dat", "ms78900.dat", "ms78900.dat", 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
        )
    )

    BattleInfo(
        "BattleInfo_9C8", 0x0000, 51, 6, 60, 8, 1, 35, 0, "br4000", "Sepith_5DAA", 20, 40, 30, 10,
        (
            ("ms84700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms84700.dat", "ms84700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms84700.dat", "ms84700.dat", "ms84700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms84700.dat", "ms84700.dat", "ms84700.dat", "ms84700.dat", 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
        )
    )

    BattleInfo(
        "BattleInfo_B58", 0x0000, 51, 6, 60, 8, 1, 40, 0, "br4000", "Sepith_5DBA", 20, 40, 30, 10,
        (
            ("ms81600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms81600.dat", "ms81600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms81600.dat", "ms81600.dat", "ms81600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_860", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
            ("ms81600.dat", "ms81600.dat", "ms81600.dat", "ms81600.dat", 0, 0, 0, 0, "MonsterBattlePostion_840", "MonsterBattlePostion_8C0", "ed7450", "ed7453", "ATBonus_800"),
        )
    )

    BattleInfo(
        "BattleInfo_A90", 0x0000, 51, 6, 60, 8, 1, 30, 0, "br4000", "Sepith_5DB2", 20, 30, 30, 20,
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

    PlaceName(0.0, 0.0, 150.0, 0x0000, 0x0000, "To Crossbell City/Bellguard Gate")
    PlaceName(-20.0, 0.0, -130.0, 0x0000, 0x0000, "To Police Academy")

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
        "Function_7_1B61",         # 07, 7
        "Function_8_1EBD",         # 08, 8
        "Function_9_1F59",         # 09, 9
        "Function_10_21C5",        # 0A, 10
        "Function_11_2241",        # 0B, 11
        "Function_12_2727",        # 0C, 12
        "Function_13_3001",        # 0D, 13
        "Function_14_3DB2",        # 0E, 14
        "Function_15_3E23",        # 0F, 15
        "Function_16_3EAA",        # 10, 16
        "Function_17_48B5",        # 11, 17
        "Function_18_4BAC",        # 12, 18
        "Function_19_5699",        # 13, 19
        "Function_20_56E8",        # 14, 20
        "Function_21_577B",        # 15, 21
        "Function_22_57A9",        # 16, 22
        "Function_23_57D7",        # 17, 23
        "Function_24_5805",        # 18, 24
        "Function_25_5842",        # 19, 25
        "Function_26_587F",        # 1A, 26
        "Function_27_58BC",        # 1B, 27
        "Function_28_58DB",        # 1C, 28
        "Function_29_5990",        # 1D, 29
        "Function_30_5A45",        # 1E, 30
        "Function_31_5AE3",        # 1F, 31
        "Function_32_5BF2",        # 20, 32
        "Function_33_5C08",        # 21, 33
        "Function_34_5C18",        # 22, 34
        "Function_35_5C50",        # 23, 35
        "Function_36_5C88",        # 24, 36
        "Function_37_5CEC",        # 25, 37
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165F")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x78, 1)"), scpexpr(EXPR_END)), "loc_15E8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x78),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E4, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_165A")

    label("loc_15E8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x78),
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

    label("loc_165A")

    Jump("loc_16A8")

    label("loc_165F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B0")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1739")
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
    SetScenarioFlags(0x1E4, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_17AB")

    label("loc_1739")

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

    label("loc_17AB")

    Jump("loc_17F9")

    label("loc_17B0")

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

    label("loc_17F9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16B4 end

    def Function_6_1805(): pass

    label("Function_6_1805")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19BC")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_END)), "loc_199D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1998")
    ClearScenarioFlags(0x3B, 2)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_1995")
    ClearScenarioFlags(0x39, 2)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_18BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_18BA)
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
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_C20", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x17, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1990")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1977")
    Call(1, 5)
    Jump("loc_1990")

    label("loc_1977")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_198D")
    Call(1, 4)
    Jump("loc_1990")

    label("loc_198D")

    Call(1, 3)

    label("loc_1990")

    Jump("loc_1998")

    label("loc_1995")

    Call(1, 1)

    label("loc_1998")

    Jump("loc_19B3")

    label("loc_199D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_19B3")
    ClearScenarioFlags(0x39, 2)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_19B3")

    TalkEnd(0xFF)
    Return()

    label("loc_19BC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_END)), "loc_1B46")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B41")
    ClearScenarioFlags(0x3B, 2)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_1B3E")
    ClearScenarioFlags(0x39, 2)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1A63():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_1A63)
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
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_C64", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B39")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B20")
    Call(1, 5)
    Jump("loc_1B39")

    label("loc_1B20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B36")
    Call(1, 4)
    Jump("loc_1B39")

    label("loc_1B36")

    Call(1, 3)

    label("loc_1B39")

    Jump("loc_1B41")

    label("loc_1B3E")

    Call(1, 1)

    label("loc_1B41")

    Jump("loc_1B5C")

    label("loc_1B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_1B5C")
    ClearScenarioFlags(0x39, 2)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1B5C")

    TalkEnd(0xFF)
    Return()

    # Function_6_1805 end

    def Function_7_1B61(): pass

    label("Function_7_1B61")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D18")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_1CF9")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF4")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1CF1")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1C16)
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
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_C20", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEC")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CD3")
    Call(1, 5)
    Jump("loc_1CEC")

    label("loc_1CD3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CE9")
    Call(1, 4)
    Jump("loc_1CEC")

    label("loc_1CE9")

    Call(1, 3)

    label("loc_1CEC")

    Jump("loc_1CF4")

    label("loc_1CF1")

    Call(1, 1)

    label("loc_1CF4")

    Jump("loc_1D0F")

    label("loc_1CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1D0F")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1D0F")

    TalkEnd(0xFF)
    Return()

    label("loc_1D18")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 3)), scpexpr(EXPR_END)), "loc_1EA2")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E9D")
    ClearScenarioFlags(0x3B, 3)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1E9A")
    ClearScenarioFlags(0x39, 3)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1DBF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1DBF)
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
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_C64", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E95")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E7C")
    Call(1, 5)
    Jump("loc_1E95")

    label("loc_1E7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E92")
    Call(1, 4)
    Jump("loc_1E95")

    label("loc_1E92")

    Call(1, 3)

    label("loc_1E95")

    Jump("loc_1E9D")

    label("loc_1E9A")

    Call(1, 1)

    label("loc_1E9D")

    Jump("loc_1EB8")

    label("loc_1EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 3)), scpexpr(EXPR_END)), "loc_1EB8")
    ClearScenarioFlags(0x39, 3)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1EB8")

    TalkEnd(0xFF)
    Return()

    # Function_7_1B61 end

    def Function_8_1EBD(): pass

    label("Function_8_1EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECB")
    Call(0, 17)
    Return()

    label("loc_1ECB")

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
            "Descend with the rope\x01",      # 0
            "Step away\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F2C"),
        (1, "loc_1F4C"),
        (SWITCH_DEFAULT, "loc_1F58"),
    )


    label("loc_1F2C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    NewScene("r4050", 102, 0, 0)
    IdleLoop()
    Jump("loc_1F58")

    label("loc_1F4C")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_1F58")

    label("loc_1F58")

    Return()

    # Function_8_1EBD end

    def Function_9_1F59(): pass

    label("Function_9_1F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 0)), scpexpr(EXPR_END)), "loc_1F63")
    Return()

    label("loc_1F63")

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
        (1, "loc_2041"),
        (SWITCH_DEFAULT, "loc_205A"),
    )


    label("loc_2041")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 75460, 1500, 44120, 270)
    EventEnd(0x5)
    Return()

    label("loc_205A")

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
        (2, "loc_211C"),
        (1, "loc_2121"),
        (SWITCH_DEFAULT, "loc_2124"),
    )


    label("loc_211C")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_2121")

    OP_B9(0x0)
    Return()

    label("loc_2124")

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
            scpstr(SCPSTR_CODE_ITEM, 0xC0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xC0, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21D, 0)
    OP_29(0x92, 0x4, 0x2)
    OP_29(0x92, 0x4, 0x10)
    OP_29(0x92, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 3, 0x80)
    EventEnd(0x5)
    Return()

    # Function_9_1F59 end

    def Function_10_21C5(): pass

    label("Function_10_21C5")

    Battle("BattleInfo_CEC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_220C")
    OP_90(0x0, 44490, 0, 47190, 270)
    EventEnd(0x5)
    SetChrFlags(0x1D, 0x8000)
    Jump("loc_2240")

    label("loc_220C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221F")
    Jump("loc_2240")

    label("loc_221F")

    ModifyEventFlags(0, 4, 0x80)
    SetMapObjFlags(0x1D, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 3)
    EventEnd(0x5)

    label("loc_2240")

    Return()

    # Function_10_21C5 end

    def Function_11_2241(): pass

    label("Function_11_2241")

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
            "#00105F#5PSo this is Knox\x01",
            "Woodlands...\x02\x03",
            "#00108FI've heard about this\x01",
            "place, but we're in\x01",
            "pretty deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5POh brother. Do we really\x01",
            "have go on foot through\x01",
            "a place like this?\x02\x03",
            "#10301FThat's not smart at all.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24BB():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_24BB)
    Sleep(100)

    def lambda_24CB():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_24CB)
    Sleep(100)

    def lambda_24DB():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_24DB)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#00004F#12PWell, this is the style of the\x01",
            "Support Section too, so I'll have\x01",
            "to ask you grin and bear it.\x02\x03",
            "#00000FBut Wazy, even though you\x01",
            "complain you don't seem tired,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6PHmm, and I thought a city\x01",
            "boy like you would've\x01",
            "given up already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PI'm just holding it in.\x01",
            "My feet have been killing\x01",
            "me for a while now.\x02\x03",
            "#10302FHehe, maybe it's time for\x01",
            "that piggyback ride from\x01",
            "our leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PYou seem totally fine to\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PHaha. Shall we proceed?\x02",
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

    # Function_11_2241 end

    def Function_12_2727(): pass

    label("Function_12_2727")

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

    def lambda_27D2():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27D2)

    def lambda_27E7():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27E7)

    def lambda_27FC():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_27FC)

    def lambda_2811():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2811)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Sleep(100)

    def lambda_284E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_284E)
    Sleep(100)

    def lambda_285E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_285E)
    Sleep(100)

    def lambda_286E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_286E)
    WaitChrThread(0x102, 1)
    Sleep(350)

    def lambda_2882():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2882)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x102,
        "#00105F#11PHuh?\x02",
    )

    CloseMessageWindow()
    OP_68(14000, -3300, 7450, 4000)
    MoveCamera(48, 21, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(26000, 4000)

    def lambda_28E2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28E2)
    Sleep(100)

    def lambda_28F2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_28F2)
    Sleep(100)

    def lambda_2902():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2902)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00100F#6PWhat could that be?\x02\x03",
            "A climbing rope to the\x01",
            "bottom of the cliff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12POh, that's how you get\x01",
            "the the survival\x01",
            "training grounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PSurvival training...\x02",
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

    def lambda_2A90():
        OP_95(0xFE, 16720, -4000, 7260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A90)

    def lambda_2AAA():
        OP_95(0xFE, 16950, -4000, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2AAA)

    def lambda_2AC4():
        OP_95(0xFE, 15030, -4000, 5650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2AC4)

    def lambda_2ADE():
        OP_95(0xFE, 15690, -4000, 4050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2ADE)
    WaitChrThread(0x109, 1)

    def lambda_2AFC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2AFC)
    WaitChrThread(0x105, 1)

    def lambda_2B0D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B0D)
    WaitChrThread(0x101, 1)

    def lambda_2B1E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B1E)
    WaitChrThread(0x102, 1)

    def lambda_2B2F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B2F)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10103F#11PBelow, there's only a dense\x01",
            "forest with poor visibility and\x01",
            "nothing but animal trails.\x02\x03",
            "#10100FYou have to spend several days\x01",
            "in that environment with\x01",
            "limited equipment and supplies.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00106F#11PI-I could never do\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#11PYeah, I'll pass as well.\x02\x03",
            "#10302FWell, I'd think about it if\x01",
            "you throw in a vintage wine\x01",
            "and some hors d'oeuvres.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, there are dehydrated\x01",
            "cheese-flavored rations at\x01",
            "least.\x02\x03",
            "#00008FI took the survival\x01",
            "training for the detective\x01",
            "exam, but...\x02\x03",
            "#00001FHonestly speaking, it was\x01",
            "quite intense.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DA6():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DA6)
    Sleep(100)

    def lambda_2DB6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2DB6)
    Sleep(100)

    def lambda_2DC6():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2DC6)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#10112F#6PAhaha...\x02\x03",
            "#10105FThat reminds me, is\x01",
            "Randy training here?\x02",
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
            "#00005F#5POh right. That's\x01",
            "possible.\x02\x03",
            "#00000FIt's also possible he's\x01",
            "doing it at a different\x01",
            "training ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#12PHe's helping the CGF\x01",
            "members who were controlled\x01",
            "with their rehab, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x102,
        (
            "#00104F#11PYes, due to the new CGF\x01",
            "commander's request.\x02\x03",
            "#00102FI hope the training\x01",
            "concludes quickly so he\x01",
            "can come back to us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PYeah, me too.\x02",
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

    # Function_12_2727 end

    def Function_13_3001(): pass

    label("Function_13_3001")

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
        "Youth's Voice",
        (
            "#2750V#2P#30WWhoo! That's one cool\x01",
            "car.\x02",
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
            "Randy, you're unbelievable...\x02\x03",
            "It's the start of your 5th full day\x01",
            "of survival training. How can you\x01",
            "be so unfazed?\x02",
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
            "Haha, well I really am exhausted.\x02\x03",
            "So tired that I'd like to shower\x01",
            "together and sleep in the same bed.\x02",
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
            "#07906F#6PJ-Jeez... You say the\x01",
            "dumbest things\x01",
            "sometimes.\x02\x03",
            "#07900FEven so... I've never\x01",
            "seen a car like that\x01",
            "before.\x02\x03",
            "Did the police introduce\x01",
            "a new Verne Co. model?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11004F#11PNo, it looked like a ZCF\x01",
            "make.\x02\x03",
            "#11002FI can't believe the\x01",
            "support section was\x01",
            "issued such a pricey car.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0xC8, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#07905F#6PZCF you say... I didn't\x01",
            "think they made orbal\x01",
            "cars.\x02\x03",
            "#07900FAnd how do you know it\x01",
            "belongs to your section,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11005F#11PWell, Lloyd and milady\x01",
            "were in the car, you\x01",
            "see.\x02\x03",
            "#11004FChief and the new guys\x01",
            "were there too, so it's\x01",
            "probably ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#07906F#6PH-How could you see\x01",
            "inside from so far\x01",
            "away...?\x02\x03",
            "#07902FWas ZCF branding on it\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11000F#11PYeah, their emblem was\x01",
            "on the side.\x02\x03",
            "#11009FMaaan, now I really\x01",
            "can't wait to go back!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0xC8, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#07908F#6P...Say, Randy.\x02\x03",
            "#07900FDon't you really want to\x01",
            "come back to the CGF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11005F#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#07906F#6PYou see, your abilities\x01",
            "are clearly suited for\x01",
            "the army...\x02\x03",
            "#07908FAlso, you're properly\x01",
            "training with the rifle\x01",
            "too, this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11004F#11PHaha... It's just a\x01",
            "practice rifle that uses\x01",
            "blanks.\x02\x03",
            "#11000FYou know that this can't\x01",
            "be used in a real\x01",
            "battle, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#07906F#6PB-But...\x02",
    )

    CloseMessageWindow()
    OP_68(15350, -2700, 4200, 1000)

    def lambda_399B():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_399B)
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
        "#07911F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11004F#11PWell, if you're ever in\x01",
            "a pinch, I'll rush to\x01",
            "your aid.\x02\x03",
            "#11002FLet's finish up the\x01",
            "rehabilitation training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#07911F#6PI-I know!\x02",
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
            "#07907F#11P#4S─Too slow! How long are you\x01",
            "gonna dawdle!?\x02\x03",
            "#4SIf you all aren't up here in\x01",
            "10 minutes, we'll practice\x01",
            "for another half day!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 3000, -8000, 0, 0)

    ChrTalk(
        0xA,
        "#5P#2SEeeek!!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrPos(0xA, 0, -8000, 0, 0)

    ChrTalk(
        0xA,
        "#5P#2SY-Yes ma'am!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrPos(0xA, 2000, -8000, 0, 0)

    ChrTalk(
        0xA,
        (
            "#5P#2SI've had enough snakes\x01",
            "already!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrPos(0xA, 1000, -8000, 0, 0)

    ChrTalk(
        0xA,
        (
            "#5P#2SDon't laze around! Climb\x01",
            "quickly and safely!\x02",
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
        (
            "#11006F#11PWow, you're a demon\x01",
            "commander.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#07907F#6P#4SShut up. Stupid Randy!\x02",
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

    # Function_13_3001 end

    def Function_14_3DB2(): pass

    label("Function_14_3DB2")

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

    # Function_14_3DB2 end

    def Function_15_3E23(): pass

    label("Function_15_3E23")

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

    # Function_15_3E23 end

    def Function_16_3EAA(): pass

    label("Function_16_3EAA")

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

    def lambda_3F8B():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F8B)
    Sleep(0)

    def lambda_3FA3():
        OP_9B(0x0, 0x102, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3FA3)
    Sleep(0)

    def lambda_3FBB():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3FBB)
    Sleep(0)

    def lambda_3FD3():
        OP_9B(0x0, 0x104, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3FD3)
    Sleep(0)

    def lambda_3FEB():
        OP_9B(0x0, 0x109, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3FEB)
    Sleep(0)

    def lambda_4003():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4003)
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

    def lambda_414F():
        OP_9B(0x0, 0x101, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_414F)
    Sleep(100)

    def lambda_4167():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4167)
    Sleep(100)

    def lambda_417F():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_417F)
    Sleep(100)

    def lambda_4197():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4197)
    Sleep(100)

    def lambda_41AF():
        OP_9B(0x0, 0x109, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_41AF)
    Sleep(100)

    def lambda_41C7():
        OP_9B(0x0, 0x105, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_41C7)
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
            "#00013F#12PAs I thought, it looks\x01",
            "like this place is\x01",
            "trashed too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PAnd that means...\x02",
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

    def lambda_430D():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_430D)
    Sleep(20)

    def lambda_4325():
        OP_9B(0x0, 0x102, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4325)
    Sleep(20)

    def lambda_433D():
        OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_433D)
    Sleep(20)

    def lambda_4355():
        OP_9B(0x0, 0x104, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4355)
    Sleep(20)

    def lambda_436D():
        OP_9B(0x0, 0x109, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_436D)
    Sleep(20)

    def lambda_4385():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4385)
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
            "#00101F#11PIt went below here, I\x01",
            "suppose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PThere's no mistake. I\x01",
            "sense its presence\x01",
            "below.\x02\x03",
            "#00208F...And... I feel a\x01",
            "strange presence as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PA strange presence?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#5PThe survival training\x01",
            "area is below.\x02\x03",
            "#10101FIt's a dense woodland,\x01",
            "hardly touched by human\x01",
            "hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#11PIf we're going to give\x01",
            "chase, it seems we need\x01",
            "to be prepared.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah... I went down there once for\x01",
            "training at the police academy and it\x01",
            "was a tough place with poor visibility.\x02\x03",
            "#00001FIt's going to be really hard... Elie,\x01",
            "Tio, Wazy─\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4601():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4601)
    Sleep(50)

    def lambda_4611():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4611)
    Sleep(50)

    def lambda_4621():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4621)
    Sleep(50)

    def lambda_4631():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4631)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        (
            "#00106F#11P*sigh*, what are you\x01",
            "saying now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#12PI'd be more worried if\x01",
            "you all went without me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#11PI can at least support\x01",
            "you with arts. It's our\x01",
            "specialty, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#12PWell, it'll be tough,\x01",
            "but we'll get through it\x01",
            "if we work together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#11PYes, let's all go down\x01",
            "together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P─Understood.\x02\x03",
            "#00001FWe don't know what kind of enemies\x01",
            "are waiting for us. Let's descend\x01",
            "after we're fully prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PRoger.\x02",
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

    # Function_16_3EAA end

    def Function_17_48B5(): pass

    label("Function_17_48B5")

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
            "Descend into the woodland\x01",      # 0
            "Step away\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_49D0"),
        (1, "loc_4B7D"),
        (SWITCH_DEFAULT, "loc_4BAB"),
    )


    label("loc_49D0")


    ChrTalk(
        0x101,
        (
            "#00003F#5P─Alright, Randy and I\x01",
            "will descend first.\x02\x03",
            "#00001FAfterwards, Elie, Tio\x01",
            "and Wazy will come down,\x01",
            "and finally Noｱl.\x02",
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
        "#10101F#11PRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#12POh yeah, should we\x01",
            "contact the Commander\x01",
            "before headin' down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PYeah, good idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#11PDepending on the repair\x01",
            "situation, they might be\x01",
            "able to come help us.\x02",
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
    Jump("loc_4BAB")

    label("loc_4B7D")

    SetChrPos(0x0, 16100, -4000, 5850, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_4BAB")

    label("loc_4BAB")

    Return()

    # Function_17_48B5 end

    def Function_18_4BAC(): pass

    label("Function_18_4BAC")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4E3C")
    FadeToBright(0, 0)
    Jump("loc_52A4")

    label("loc_4E3C")

    OP_68(36950, 900, -7950, 0)
    MoveCamera(15, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23150, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(18150, 2500)

    def lambda_4E81():
        OP_95(0xFE, 38000, 0, -9000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E81)
    WaitChrThread(0x101, 1)
    StopBGM(0x7D0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(2093, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00011F#11P#10ADamn!\x02",
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
            "#00010F#11PUgh. I've got to hide\x01",
            "somehow and hold out!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1E, 1, 0, 33)
    SetChrPos(0x11, 38000, 0, -37000, 0)

    NpcTalk(
        0x11,
        "Man's Voice",
        "#2S─Target sighted!\x02",
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
        (
            "#11PEngage in a pincer\x01",
            "attack!\x02",
        )
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
            "#00007F#5PUgh... If that's how it\x01",
            "is, then...!\x02",
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

    label("loc_52A4")

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

    # Function_18_4BAC end

    def Function_19_5699(): pass

    label("Function_19_5699")

    Sound(471, 0, 100, 0)
    SetChrPos(0xFE, -3350, 0, 88050, 180)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -750, 0, 78200)
    OP_9F(0x1, 4700, 0, 71000)
    OP_9F(0x1, 19600, 0, 67750)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    Return()

    # Function_19_5699 end

    def Function_20_56E8(): pass

    label("Function_20_56E8")

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

    # Function_20_56E8 end

    def Function_21_577B(): pass

    label("Function_21_577B")

    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    Return()

    # Function_21_577B end

    def Function_22_57A9(): pass

    label("Function_22_57A9")

    OP_9B(0x0, 0xFE, 0x0, 0x32C8, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    Return()

    # Function_22_57A9 end

    def Function_23_57D7(): pass

    label("Function_23_57D7")

    OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2710, 0xFA0, 0x1)
    Return()

    # Function_23_57D7 end

    def Function_24_5805(): pass

    label("Function_24_5805")

    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x2EE0, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x1F40, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x145, 0x4E20, 0x1770, 0x1)
    Return()

    # Function_24_5805 end

    def Function_25_5842(): pass

    label("Function_25_5842")

    OP_9B(0x0, 0xFE, 0x163, 0x2134, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x30D4, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2134, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x145, 0x5014, 0x1770, 0x1)
    Return()

    # Function_25_5842 end

    def Function_26_587F(): pass

    label("Function_26_587F")

    OP_9B(0x0, 0xFE, 0x163, 0x2328, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x32C8, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x14F, 0x2328, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x145, 0x5208, 0x1770, 0x1)
    Return()

    # Function_26_587F end

    def Function_27_58BC(): pass

    label("Function_27_58BC")

    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4650, 0xFA0, 0x1)
    Return()

    # Function_27_58BC end

    def Function_28_58DB(): pass

    label("Function_28_58DB")

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

    # Function_28_58DB end

    def Function_29_5990(): pass

    label("Function_29_5990")

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

    # Function_29_5990 end

    def Function_30_5A45(): pass

    label("Function_30_5A45")

    SetChrPos(0xFE, 33430, 0, -7320, 225)
    OP_95(0xFE, 29580, 0, -7910, 6000, 0x1)
    OP_95(0xFE, 28040, -70, -13230, 6000, 0x1)
    OP_95(0xFE, 33910, -2000, -16410, 6000, 0x1)
    OP_95(0xFE, 35650, -2050, -21630, 6000, 0x1)
    OP_95(0xFE, 33250, -3090, -27780, 6000, 0x1)
    OP_95(0xFE, 29550, -4000, -28490, 6000, 0x1)
    OP_95(0xFE, 24450, -4000, -21310, 6000, 0x0)
    Return()

    # Function_30_5A45 end

    def Function_31_5AE3(): pass

    label("Function_31_5AE3")

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

    # Function_31_5AE3 end

    def Function_32_5BF2(): pass

    label("Function_32_5BF2")

    Sound(465, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(3000)
    Sound(487, 0, 100, 0)
    Return()

    # Function_32_5BF2 end

    def Function_33_5C08(): pass

    label("Function_33_5C08")

    Sound(910, 0, 30, 0)
    Sleep(800)
    Sound(909, 0, 30, 0)
    Return()

    # Function_33_5C08 end

    def Function_34_5C18(): pass

    label("Function_34_5C18")

    Sleep(2300)

    label("loc_5C1B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C4F")
    Sound(909, 0, 40, 0)
    Sleep(1200)
    Sound(909, 0, 40, 0)
    Sleep(900)
    Sound(909, 0, 40, 0)
    Sleep(1600)
    Sound(909, 0, 40, 0)
    Sleep(950)
    Jump("loc_5C1B")

    label("loc_5C4F")

    Return()

    # Function_34_5C18 end

    def Function_35_5C50(): pass

    label("Function_35_5C50")

    Sleep(3000)

    label("loc_5C53")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C87")
    Sound(910, 0, 40, 0)
    Sleep(700)
    Sound(910, 0, 40, 0)
    Sleep(1600)
    Sound(910, 0, 40, 0)
    Sleep(1400)
    Sound(910, 0, 40, 0)
    Sleep(1800)
    Jump("loc_5C53")

    label("loc_5C87")

    Return()

    # Function_35_5C50 end

    def Function_36_5C88(): pass

    label("Function_36_5C88")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Survival Training Area Ahead\x01",
            "   Crossbell Police Academy \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_5C88 end

    def Function_37_5CEC(): pass

    label("Function_37_5CEC")

    EventBegin(0x1)
    OP_E2(0x3)

    ChrTalk(
        0x101,
        (
            "#00001FThe monster in question isn't this\x01",
            "way... Let's head to the survival\x01",
            "training grounds below the cliff.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 37840, 0, -8070, 319)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_37_5CEC end

    SaveToFile()

Try(main)
