from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2010.bin",                # FileName
        "r2010",                    # MapName
        "r2010",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2010", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x12,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 3, 0, 4],
    )

    BuildStringList((
        "r2010",                  # 0
        "Narses, the Crazy Wave", # 1
        "ロックラッタ",           # 2
        "ロックラッタ",           # 3
        "鉄鋼ドリュー",           # 4
        "鉄鋼ドリュー",           # 5
        "Cryptid",                # 6
        "2nd Lt. Mireille",       # 7
        "CGF Member",             # 8
        "CGF Member",             # 9
        "CGF Member",             # 10
        "CGF Member",             # 11
        "CGF Member",             # 12
        "CGF Member",             # 13
        "CGF Member",             # 14
        "CGF Member",             # 15
        "CGF Member",             # 16
        "CGF Member",             # 17
        "Wolf",                   # 18
        "Wolf",                   # 19
        "Wolf",                   # 20
        "Wolf",                   # 21
        "Wolf",                   # 22
        "Jaeger Sachs",           # 23
        "Jaeger",                 # 24
        "Jaeger",                 # 25
        "Jaeger",                 # 26
        "Jaeger",                 # 27
        "Jaeger",                 # 28
        "Jaeger",                 # 29
        "Jaeger",                 # 30
        "クーガー",               # 31
        "クーガー",               # 32
        "クーガー",               # 33
        "SE制御",                 # 34
        "br2000",                 # 35
        "br2000",                 # 36
        "br2000",                 # 37
        "br2000",                 # 38
        "br2000",                 # 39
        "br2000",                 # 40
        "br2000",                 # 41
        "br2000",                 # 42
        "To Crossbell City",      # 43
        "To Mining Town Mainz",   # 44
    ))

    ATBonus("ATBonus_6FC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_71C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_58B9", 6,   0,   0,   3,   2,   4,   0)
    Sepith("Sepith_58C1", 3,   0,   1,   5,   3,   2,   0)
    Sepith("Sepith_58D1", 6,   0,   8,   0,   1,   0,   6)
    Sepith("Sepith_58C9", 0,   7,   2,   0,   1,   0,   4)
    Sepith("Sepith_5901", 11,  3,   6,   4,   6,   10,  8)

    MonsterBattlePostion("MonsterBattlePostion_73C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_740", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_744", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_748", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_74C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_750", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_754", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_758", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7BC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_7C0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_7C4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_7C8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_7CC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_7D0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_7D4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_75C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_760", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_764", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_768", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_76C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_770", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_774", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_778", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7DC", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E0", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E4", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E8", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_7EC", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_7F0", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_7F4", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_7F8", 0, 0, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_7FC", 0x0000, 52, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_58B9", 40, 30, 20, 0,
        (
            ("ms62500.dat", "ms62500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms62500.dat", "ms65900.dat", "ms62500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms62500.dat", "ms62500.dat", "ms65500.dat", "ms62500.dat", 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_934", 0x0000, 52, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_58C1", 40, 30, 20, 0,
        (
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9D0", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_58D1", 40, 30, 20, 0,
        (
            ("ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms69400.dat", "ms69400.dat", "ms69400.dat", "ms69400.dat", 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_898", 0x0000, 52, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_58C9", 40, 30, 20, 0,
        (
            ("ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A6C", 0x0000, 82, 6, 45, 6, 1, 30, 0, "br2000", "Sepith_5901", 100, 30, 20, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_73C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7450", "ed7453", "ATBonus_6FC"),
            (),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_B08", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62500.dat", "ms62500.dat", "ms62500.dat", "ms62500.dat", "ms62500.dat", "ms62500.dat", 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7453", "ed7453", "ATBonus_6FC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B4C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, "MonsterBattlePostion_75C", "MonsterBattlePostion_7BC", "ed7453", "ed7453", "ATBonus_6FC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B90", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88702.dat", "ms88802.dat", "ms88802.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_7DC", "MonsterBattlePostion_7DC", "ed7454", "ed7453", "ATBonus_71C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch45900.itc",                   # 00
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
        "monster/ch62550.itc",               # 10
        "monster/ch62551.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch65550.itc",               # 14
        "monster/ch65551.itc",               # 15
        "monster/ch69450.itc",               # 16
        "monster/ch69450.itc",               # 17
        "monster/ch76050.itc",               # 18
        "monster/ch76051.itc",               # 19
    ))

    DeclNpc(4294955166, 5380,    58639,   315,  261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294909046, 0,       33119,   270,  484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(27629,   8000,    38669,   270,  484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294909046, 0,       33119,   270,  484,  0x0, 0,   24,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(27629,   8000,    38669,   270,  484,  0x0, 0,   24,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294935576, 15370,   0,       0x1010000,    "BattleInfo_7FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294903206, 36330,   0,       0x1010000,    "BattleInfo_934", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294925876, 86260,   8000,    0x1010000,    "BattleInfo_9D0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(8029,    99200,   18000,   0x1010000,    "BattleInfo_898", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(27930,   93470,   18000,   0x1010000,    "BattleInfo_7FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(30600,   53520,   8000,    0x1010000,    "BattleInfo_934", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(17410,   30550,   8000,    0x1010000,    "BattleInfo_898", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294914576, 42390,   0,       0x1010000,    "BattleInfo_A6C", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(19680,   94830,   18000,   0x1010000,    "BattleInfo_A6C", 0,   24,  0xFFFF, 8,  9)

    DeclEvent(0x0040, 0, 11,  -64.7300033569336,     40.720001220703125,    -1.25,                 16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   8.0912504196167,       -5.090000152587891,    0.3125,                1.0])

    DeclActor(4294880296, 0,       35750,   1200,    4294880296, 1000,    35750,   0x007C, 0,  5,  0x0000)
    DeclActor(4294956466, 5380,    59860,   1200,    4294953936, 380,     68320,   0x007C, 0,  12, 0x0000)
    DeclActor(4294909046, 0,       33120,   1200,    4294909046, 0,       33120,   0x007C, 0,  7,  0x0000)
    DeclActor(27630,   8000,    38670,   1200,    27630,   8000,    38670,   0x007C, 0,  8,  0x0000)

    PlaceName(26.0, 0.0, -28.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(61.0, 18.0, 112.0, 0x0000, 0x0000, "To Mining Town Mainz")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9

    ScpFunction((
        "Function_0_D9C",          # 00, 0
        "Function_1_E54",          # 01, 1
        "Function_2_E73",          # 02, 2
        "Function_3_E92",          # 03, 3
        "Function_4_F88",          # 04, 4
        "Function_5_16DA",         # 05, 5
        "Function_6_182C",         # 06, 6
        "Function_7_1830",         # 07, 7
        "Function_8_1B8E",         # 08, 8
        "Function_9_1EEC",         # 09, 9
        "Function_10_1F05",        # 0A, 10
        "Function_11_2BE8",        # 0B, 11
        "Function_12_2C64",        # 0C, 12
        "Function_13_2F0E",        # 0D, 13
        "Function_14_3AFF",        # 0E, 14
        "Function_15_3BAF",        # 0F, 15
        "Function_16_3BE3",        # 10, 16
        "Function_17_3C37",        # 11, 17
        "Function_18_3C8B",        # 12, 18
        "Function_19_3D55",        # 13, 19
        "Function_20_3D87",        # 14, 20
        "Function_21_3DB9",        # 15, 21
        "Function_22_3DF2",        # 16, 22
        "Function_23_3E17",        # 17, 23
        "Function_24_3E7A",        # 18, 24
        "Function_25_3EF1",        # 19, 25
        "Function_26_3F30",        # 1A, 26
        "Function_27_3FA7",        # 1B, 27
        "Function_28_4017",        # 1C, 28
        "Function_29_408E",        # 1D, 29
        "Function_30_40C7",        # 1E, 30
        "Function_31_413E",        # 1F, 31
        "Function_32_418B",        # 20, 32
        "Function_33_4202",        # 21, 33
        "Function_34_424F",        # 22, 34
        "Function_35_42C6",        # 23, 35
        "Function_36_430C",        # 24, 36
        "Function_37_4383",        # 25, 37
        "Function_38_43CF",        # 26, 38
        "Function_39_4446",        # 27, 39
        "Function_40_44A0",        # 28, 40
        "Function_41_4517",        # 29, 41
        "Function_42_4574",        # 2A, 42
        "Function_43_45EB",        # 2B, 43
        "Function_44_464B",        # 2C, 44
        "Function_45_46A7",        # 2D, 45
        "Function_46_46F4",        # 2E, 46
        "Function_47_475A",        # 2F, 47
        "Function_48_479D",        # 30, 48
        "Function_49_47F9",        # 31, 49
        "Function_50_486F",        # 32, 50
        "Function_51_48DF",        # 33, 51
        "Function_52_49A1",        # 34, 52
        "Function_53_4A17",        # 35, 53
        "Function_54_4A9E",        # 36, 54
        "Function_55_4AF9",        # 37, 55
        "Function_56_4C40",        # 38, 56
        "Function_57_4C75",        # 39, 57
        "Function_58_4CF1",        # 3A, 58
        "Function_59_4D26",        # 3B, 59
        "Function_60_4D5F",        # 3C, 60
        "Function_61_4D94",        # 3D, 61
        "Function_62_4DCD",        # 3E, 62
        "Function_63_4E02",        # 3F, 63
        "Function_64_4E3B",        # 40, 64
        "Function_65_4E96",        # 41, 65
        "Function_66_4F36",        # 42, 66
        "Function_67_4F91",        # 43, 67
        "Function_68_502B",        # 44, 68
        "Function_69_5086",        # 45, 69
        "Function_70_50B4",        # 46, 70
        "Function_71_5101",        # 47, 71
        "Function_72_52B0",        # 48, 72
        "Function_73_52FD",        # 49, 73
        "Function_74_532C",        # 4A, 74
        "Function_75_5379",        # 4B, 75
        "Function_76_53AF",        # 4C, 76
        "Function_77_53C9",        # 4D, 77
        "Function_78_53FA",        # 4E, 78
        "Function_79_5484",        # 4F, 79
        "Function_80_5682",        # 50, 80
        "Function_81_56E8",        # 51, 81
        "Function_82_5727",        # 52, 82
        "Function_83_577C",        # 53, 83
    ))


    def Function_0_D9C(): pass

    label("Function_0_D9C")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_DDC"),
        (1, "loc_DE8"),
        (2, "loc_DF4"),
        (3, "loc_E00"),
        (4, "loc_E0C"),
        (5, "loc_E18"),
        (6, "loc_E24"),
        (SWITCH_DEFAULT, "loc_E30"),
    )


    label("loc_DDC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_DE8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_DF4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E00")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E0C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E18")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E24")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E30")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E53")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E3C")

    label("loc_E53")

    Return()

    # Function_0_D9C end

    def Function_1_E54(): pass

    label("Function_1_E54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E72")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_E54")

    label("loc_E72")

    Return()

    # Function_1_E54 end

    def Function_2_E73(): pass

    label("Function_2_E73")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E91")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_E73")

    label("loc_E91")

    Return()

    # Function_2_E73 end

    def Function_3_E92(): pass

    label("Function_3_E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_EAC")
    SetChrPos(0x8, -13910, 5380, 56930, 295)

    label("loc_EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_EBF")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F5E")

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_EDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_ED6")
    SetChrFlags(0x8, 0x80)

    label("loc_ED6")

    Jump("loc_F5E")

    label("loc_EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_EEE")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F5E")

    label("loc_EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EFC")
    Jump("loc_F5E")

    label("loc_EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F0A")
    Jump("loc_F5E")

    label("loc_F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F18")
    Jump("loc_F5E")

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F26")
    Jump("loc_F5E")

    label("loc_F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F34")
    Jump("loc_F5E")

    label("loc_F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F42")
    Jump("loc_F5E")

    label("loc_F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F50")
    Jump("loc_F5E")

    label("loc_F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F5E")
    SetChrFlags(0x8, 0x80)

    label("loc_F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F75")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 7)
    Event(0, 13)
    Jump("loc_F84")

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F84")
    ClearScenarioFlags(0x22, 1)
    Event(0, 83)

    label("loc_F84")

    Call(0, 9)
    Return()

    # Function_3_E92 end

    def Function_4_F88(): pass

    label("Function_4_F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_F9A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_FAE")
    OP_24(0x7C)
    ClearScenarioFlags(0x0, 7)
    Jump("loc_FCA")

    label("loc_FAE")

    SoundDistance(0x7C, 0xFFFFCE6E, 0x1504, 0x1205C, 0x7530, 0x249F0, 0x64, 0x0)

    label("loc_FCA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FF1")
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0xD, 0x4)
    Jump("loc_105A")

    label("loc_FF1")

    OP_78(0xD, 0xD)
    ClearMapObjFlags(0xD, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x1)
    SetChrPos(0xD, -64730, 250, 40720, 0)
    OP_93(0xD, 0x0, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, -64730, -1250, 40720, 3000, 3000, 90000)

    label("loc_105A")

    OP_52(0x31, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x31, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x32, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13EE")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)

    label("loc_13EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_146C")
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    Jump("loc_14AE")

    label("loc_146C")

    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)

    label("loc_14AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1583")
    OP_11(0x87, 0xAA, 0xFF, 0xA, 0x73, 0x0)
    ClearMapObjFlags(0xE, 0x4)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x0, 0x258, 0x0, 0x20)
    OP_C3(0x0, 0x1, 0x3, 0x0, 0x0, 0x1, -13740, -500, 5790, 2000, 2000, 0)
    OP_C3(0x1, 0x1, 0x3, 0x0, 0x0, 0x1, -11950, -500, 7590, 2000, 2000, 0)
    OP_C3(0x2, 0x1, 0x3, 0x0, 0x0, 0x1, -10120, -500, 9350, 2000, 2000, 0)
    OP_C3(0x3, 0x1, 0x3, 0x0, 0x0, 0x1, -8140, -500, 11380, 2000, 2000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg2.eff")
    Jump("loc_1589")

    label("loc_1583")

    SetMapObjFlags(0xE, 0x4)

    label("loc_1589")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -13360, 380, 68320, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15ED")
    OP_66(0x1, 0x1)

    label("loc_15ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15FF")
    OP_65(0x1, 0x1)

    label("loc_15FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1612")
    OP_70(0x0, 0x0)
    Jump("loc_1616")

    label("loc_1612")

    OP_70(0x0, 0x1E)

    label("loc_1616")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1677")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -58250, 0, 33120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1677")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16C3")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 27630, 8000, 38670, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_16C3")

    OP_1C(0x0, 0xF, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x10, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    Return()

    # Function_4_F88 end

    def Function_5_16DA(): pass

    label("Function_5_16DA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D6")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3F, 1)"), scpexpr(EXPR_END)), "loc_175F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E6, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_17D1")

    label("loc_175F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F),
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

    label("loc_17D1")

    Jump("loc_1820")

    label("loc_17D6")

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

    label("loc_1820")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16DA end

    def Function_6_182C(): pass

    label("Function_6_182C")

    Call(1, 6)
    Return()

    # Function_6_182C end

    def Function_7_1830(): pass

    label("Function_7_1830")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19E8")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_19C9")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C4")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_19C1")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_18E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_18E6)
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
    Battle("BattleInfo_B08", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BC")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_19A3")
    Call(1, 5)
    Jump("loc_19BC")

    label("loc_19A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_19B9")
    Call(1, 4)
    Jump("loc_19BC")

    label("loc_19B9")

    Call(1, 3)

    label("loc_19BC")

    Jump("loc_19C4")

    label("loc_19C1")

    Call(1, 1)

    label("loc_19C4")

    Jump("loc_19DF")

    label("loc_19C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_19DF")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_19DF")

    TalkEnd(0xFF)
    Return()

    label("loc_19E8")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_1B73")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6E")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_1B6B")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1A90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1A90)
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
    Battle("BattleInfo_B4C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B66")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B4D")
    Call(1, 5)
    Jump("loc_1B66")

    label("loc_1B4D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B63")
    Call(1, 4)
    Jump("loc_1B66")

    label("loc_1B63")

    Call(1, 3)

    label("loc_1B66")

    Jump("loc_1B6E")

    label("loc_1B6B")

    Call(1, 1)

    label("loc_1B6E")

    Jump("loc_1B89")

    label("loc_1B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_1B89")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1B89")

    TalkEnd(0xFF)
    Return()

    # Function_7_1830 end

    def Function_8_1B8E(): pass

    label("Function_8_1B8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D46")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_1D27")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D22")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1D1F")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C44():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1C44)
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
    Battle("BattleInfo_B08", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D1A")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D01")
    Call(1, 5)
    Jump("loc_1D1A")

    label("loc_1D01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D17")
    Call(1, 4)
    Jump("loc_1D1A")

    label("loc_1D17")

    Call(1, 3)

    label("loc_1D1A")

    Jump("loc_1D22")

    label("loc_1D1F")

    Call(1, 1)

    label("loc_1D22")

    Jump("loc_1D3D")

    label("loc_1D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1D3D")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1D3D")

    TalkEnd(0xFF)
    Return()

    label("loc_1D46")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 2)), scpexpr(EXPR_END)), "loc_1ED1")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ECC")
    ClearScenarioFlags(0x3A, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1EC9")
    ClearScenarioFlags(0x38, 2)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1DEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1DEE)
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
    Battle("BattleInfo_B4C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC4")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EAB")
    Call(1, 5)
    Jump("loc_1EC4")

    label("loc_1EAB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EC1")
    Call(1, 4)
    Jump("loc_1EC4")

    label("loc_1EC1")

    Call(1, 3)

    label("loc_1EC4")

    Jump("loc_1ECC")

    label("loc_1EC9")

    Call(1, 1)

    label("loc_1ECC")

    Jump("loc_1EE7")

    label("loc_1ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 2)), scpexpr(EXPR_END)), "loc_1EE7")
    ClearScenarioFlags(0x38, 2)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1EE7")

    TalkEnd(0xFF)
    Return()

    # Function_8_1B8E end

    def Function_9_1EEC(): pass

    label("Function_9_1EEC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F04")
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)

    label("loc_1F04")

    Return()

    # Function_9_1EEC end

    def Function_10_1F05(): pass

    label("Function_10_1F05")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F1D")
    SetScenarioFlags(0x0, 6)

    label("loc_1F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_1F29")
    SetScenarioFlags(0x0, 6)

    label("loc_1F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_216E")
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Fumu, who are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FUhhm, I am Lloyd, of\x01",
            "the Fisherman's Guild.\x02\x03",
            "#00005FAre you...from the Fishing Emperor Club?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ofu koosu.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Indeed I am, Narses, the\x01",
            ""Crazy Wave", the ereganto &\x01",
            "sutairisshu gai of the Elite Four.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, it seems you're going\x01",
            "to charenji me, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, first, go fisshingu the\x01",
            "mosuto byurihoo fisshu of\x01",
            "this place, Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FEeehm, the most beautiful\x01",
            "fish in Crossbell, is it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hahhah, well, try shinkingu\x01",
            "well about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll stay here, \x01",
            "ueitingu for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 3)

    label("loc_216E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2178")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21CF")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                                 # 0
            "Challenge Him to an Angler Duel\x01",      # 1
            "Quit\x01",                                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_21D9")

    label("loc_21CF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28CE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B8")

    ChrTalk(
        0x8,
        (
            "Fumu, then, I'll chekku\x01",
            "your fisshingu nooto.\x02",
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
            "Right, the Noble Carp.\x01",
            "That's the very mosuto\x01",
            "piscine beauty in Crossbell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4SGureito & byurihoooo!#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012FT-Thanks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hahhah, you're welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, about the "Angler\x01",
            "Dyueru" with me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With a beauty dyueru...\x01",
            "It would be hard to choose.\x01",
            "And with saizu, the criteria differ...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So let's decide the uinaa with\x01",
            "an "Angler Puraisu Dyueru".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You'll have a wan taimu chansu...\x01\x07\x02",
            "The uinaa will be who has caught\x01",
            "the fish with the higher price\x07\x00",
            "!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 4)
    Jump("loc_2561")

    label("loc_24B8")


    ChrTalk(
        0x8,
        (
            "Do you want to charenji me\x01",
            "to an "Angler Puraisu Dyueru"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You'll have a wan taimu chansu...\x01",
            "The uinaa will be who has caught\x01",
            "the fish with the higher price\x07\x00",
            "!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2561")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Challenge Narses, the "Crazy Wave"\x01",
            "to an "Angler Price Duel"?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Challenge Him\x01",      # 0
            "Do Not\x01",             # 1
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
        (0, "loc_2601"),
        (1, "loc_2819"),
        (SWITCH_DEFAULT, "loc_283C"),
    )


    label("loc_2601")


    ChrTalk(
        0x8,
        (
            "Gureito!\x01",
            "Then, let's dyueringu at once!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    ClearMapFlags(0x1)
    OP_68(-15360, 4380, 58540, 0)
    MoveCamera(25, 37, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, -2570, 5380, 47750, 295)
    OP_31(0x1)
    SetChrPos(0x101, -13910, 5380, 56930, 315)
    OP_93(0x8, 0x13B, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE("apl/ch51004.itc")
    MiniGame(0x7, 0x2, 0x8, 0xFFFFC131, 0x140, 0xE5B0, 0xFFFFCCB6, 0x140, 0xFA50)
    SetChrPos(0x0, -2570, 5380, 47750, 295)
    OP_31(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2752")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_68(-9740, 4380, 61600, 0)
    MoveCamera(25, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x101, -11300, 5380, 56730, 340)
    OP_93(0xFE, 0xA0, 0x0)
    Sleep(500)
    Call(0, 79)
    Return()

    label("loc_2752")

    OP_68(-12100, 4380, 60440, 0)
    MoveCamera(25, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, -13910, 5380, 56930, 46)
    OP_93(0xFE, 0xE1, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B1")
    Call(0, 80)
    Jump("loc_27D8")

    label("loc_27B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C7")
    Call(0, 82)
    Jump("loc_27D8")

    label("loc_27C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D8")
    Call(0, 81)

    label("loc_27D8")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_93(0x8, 0x13B, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -13910, 5380, 56930, 46)
    OP_31(0x1)
    SetMapFlags(0x1)
    OP_69(0xFF, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_283C")

    label("loc_2819")


    ChrTalk(
        0x8,
        "Natto gureito...too bad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_283C")

    label("loc_283C")

    Jump("loc_28C9")

    label("loc_2841")


    ChrTalk(
        0x8,
        (
            "Fumu, then, I'll chekku\x01",
            "your fisshingu nooto.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "Noo guddo...\x01",
            "It's natto byurihoo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Shinkingu agein!\x02",
    )

    CloseMessageWindow()

    label("loc_28C9")

    Jump("loc_2BDF")

    label("loc_28CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_28FF")
    Jump("loc_2BDF")

    label("loc_28FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2945")

    ChrTalk(
        0x8,
        (
            "I, who kyacchi fisshu...\x01",
            "Nnn, veri veri byurihooo!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDF")

    label("loc_2945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2953")
    Jump("loc_2BDF")

    label("loc_2953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2999")

    ChrTalk(
        0x8,
        (
            "I, who is exposed to the rein...\x01",
            "Nnn, kooketisshu!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDF")

    label("loc_2999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_29F4")

    ChrTalk(
        0x8,
        "Muu, it's been somehow noiji since before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Nnn, natto byurihooooo!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BDF")

    label("loc_29F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A3C")

    ChrTalk(
        0x8,
        (
            "I, who sutea at the fisshu...\x01",
            "Nnn, sofisutikeiteddo!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDF")

    label("loc_2A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A83")

    ChrTalk(
        0x8,
        (
            "I, who setto the fishing bait...\x01",
            "Nnn, wandahouuuuu!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDF")

    label("loc_2A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AC1")

    ChrTalk(
        0x8,
        (
            "I, who suingu the roddo...\x01",
            "Nnn, maaverasu!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDF")

    label("loc_2AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B0E")

    ChrTalk(
        0x8,
        (
            "I, who sutando in the mother nature...\x01",
            "Nnn, ekuserentou!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDF")

    label("loc_2B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2BC8")

    ChrTalk(
        0x8,
        (
            "I, who is rifaindo on the water's surface...\x01",
            "Nnn, byurihooooo!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BC3")

    ChrTalk(
        0x101,
        (
            "#00003F(It seems I could fish here, but...\x01",
            "Since there's already someone, I won't.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC3")

    Jump("loc_2BDF")

    label("loc_2BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2BD6")
    Jump("loc_2BDF")

    label("loc_2BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2BDF")

    label("loc_2BDF")

    Jump("loc_2178")

    label("loc_2BE4")

    TalkEnd(0xFE)
    Return()

    # Function_10_1F05 end

    def Function_11_2BE8(): pass

    label("Function_11_2BE8")

    Battle("BattleInfo_B90", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2F")
    OP_90(0x0, -62530, 0, 33250, 180)
    EventEnd(0x5)
    SetChrFlags(0xD, 0x8000)
    Jump("loc_2C63")

    label("loc_2C2F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C42")
    Jump("loc_2C63")

    label("loc_2C42")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0xD, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x3C, 1)
    EventEnd(0x5)

    label("loc_2C63")

    Return()

    # Function_11_2BE8 end

    def Function_12_2C64(): pass

    label("Function_12_2C64")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
    )

    CloseMessageWindow()
    OP_68(-13230, 4370, 66180, 1500)
    MoveCamera(25, 49, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(26000, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F09")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D3B")
    MiniGame(0x6, 0x8, 0xFFFFD5B2, 0x1504, 0xE9D4, 0x14E, 0xFFFFCBD0, 0x17C, 0x10AE0)
    Jump("loc_2F09")

    label("loc_2D3B")

    MiniGame(0x6, 0x9, 0xFFFFD5B2, 0x1504, 0xE9D4, 0x14E, 0xFFFFCBD0, 0x17C, 0x10AE0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F09")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F09")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(-9450, 4370, 64390, 0)
    MoveCamera(20, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21120, 0)
    LoadChrToIndex("apl/ch50160.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, -10830, 5380, 59860, 334)
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
            "#00011FT-This is...\x01",
            "Another very pretty big game.\x02\x03",
            "#00003FIt resembles an Angel Fish, but...\x01",
            "Could it be a special type of fish?\x01\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, -10830, 5380, 59860, 334)
    SetChrPos(0x2, -10830, 5380, 59860, 334)
    SetChrPos(0x3, -10830, 5380, 59860, 334)
    SetChrPos(0x4, -10830, 5380, 59860, 334)
    SetChrPos(0x5, -10830, 5380, 59860, 334)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_37()
    SetScenarioFlags(0x18B, 3)

    label("loc_2F09")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_12_2C64 end

    def Function_13_2F0E(): pass

    label("Function_13_2F0E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_D7(0x0)
    OP_D7(0x10)
    OP_D7(0x11)
    OP_D7(0x12)
    OP_D7(0x13)
    OP_D7(0x14)
    OP_D7(0x15)
    OP_D7(0x16)
    OP_D7(0x17)
    OP_D7(0x18)
    OP_D7(0x19)
    LoadChrToIndex("monster/ch86150.itc", 0x1E)
    LoadChrToIndex("monster/ch86151.itc", 0x1F)
    LoadChrToIndex("monster/ch86152.itc", 0x20)
    LoadChrToIndex("monster/ch86153.itc", 0x21)
    LoadChrToIndex("chr/ch41950.itc", 0x23)
    LoadChrToIndex("chr/ch41951.itc", 0x24)
    LoadChrToIndex("chr/ch41952.itc", 0x25)
    LoadChrToIndex("chr/ch42050.itc", 0x28)
    LoadChrToIndex("chr/ch42051.itc", 0x29)
    LoadChrToIndex("chr/ch42052.itc", 0x2A)
    LoadChrToIndex("chr/ch42056.itc", 0x2B)
    LoadChrToIndex("chr/ch31250.itc", 0x2D)
    LoadChrToIndex("chr/ch31251.itc", 0x2E)
    LoadChrToIndex("chr/ch31252.itc", 0x2F)
    LoadChrToIndex("chr/ch31350.itc", 0x32)
    LoadChrToIndex("chr/ch31351.itc", 0x33)
    LoadChrToIndex("chr/ch31352.itc", 0x34)
    LoadChrToIndex("apl/ch50112.itc", 0x3C)
    LoadChrToIndex("apl/ch50118.itc", 0x3D)
    LoadChrToIndex("apl/ch50113.itc", 0x3E)
    LoadChrToIndex("chr/ch32650.itc", 0x37)
    LoadChrToIndex("chr/ch32651.itc", 0x38)
    LoadChrToIndex("chr/ch32654.itc", 0x39)
    LoadChrToIndex("chr/ch32654.itc", 0x3A)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "battle/sp003000.eff")
    SoundLoad(124)
    SoundLoad(860)
    SoundLoad(861)
    SoundLoad(974)
    SoundLoad(1001)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x1F)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x24)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x24)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x24)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x29)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x29)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x29)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x1E, 0x29)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0xF, 0x2E)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x2E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x2E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x2E)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x33)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x33)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x3D)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x3D)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x3D)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x3D)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x3D)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0xE, 0x38)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    OP_90(0xE, -8500, 20000, 88000, 270)
    OP_90(0x14, -6500, 20000, 89250, 270)
    OP_90(0x15, -7000, 20000, 88000, 270)
    OP_90(0x16, -5900, 20000, 86700, 270)
    OP_90(0x17, -4950, 20000, 88700, 270)
    OP_90(0x18, -4300, 20000, 87500, 270)
    OP_90(0xF, -4900, 20000, 90300, 270)
    OP_90(0x10, -3350, 20000, 89550, 270)
    OP_90(0x11, -4750, 20000, 85450, 270)
    OP_90(0x12, -3150, 20000, 86450, 270)
    OP_90(0x13, -2400, 20000, 88300, 270)
    SetChrPos(0x19, -47900, 10000, 95450, 135)
    SetChrPos(0x1A, -45250, 10000, 97850, 180)
    SetChrPos(0x1B, -41600, 10000, 98850, 180)
    SetChrPos(0x1C, -39350, 10000, 97850, 225)
    SetChrPos(0x1D, -38350, 10000, 98400, 225)
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-8500, 18300, 88000, 0)
    MoveCamera(55, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30000, 0)
    OP_68(-36500, 8600, 86000, 7000)
    MoveCamera(55, 25, 0, 7000)
    OP_6E(510, 7000)
    SetCameraDistance(25000, 7000)
    BeginChrThread(0xE, 1, 0, 23)
    BeginChrThread(0x14, 1, 0, 34)
    BeginChrThread(0x15, 1, 0, 36)
    BeginChrThread(0x16, 1, 0, 38)
    BeginChrThread(0x17, 1, 0, 40)
    BeginChrThread(0x18, 1, 0, 42)
    BeginChrThread(0xF, 1, 0, 24)
    BeginChrThread(0x10, 1, 0, 26)
    BeginChrThread(0x11, 1, 0, 28)
    BeginChrThread(0x12, 1, 0, 30)
    BeginChrThread(0x13, 1, 0, 32)
    Sound(124, 2, 60, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    OP_68(-44000, 8600, 74500, 6000)
    MoveCamera(50, 20, 0, 6000)
    SetCameraDistance(22000, 6000)
    Sleep(2000)
    BeginChrThread(0x29, 1, 0, 76)
    BeginChrThread(0x19, 1, 0, 44)
    Sleep(400)
    BeginChrThread(0x1A, 1, 0, 46)
    Sleep(400)
    BeginChrThread(0x1B, 1, 0, 48)
    Sleep(400)
    BeginChrThread(0x1C, 1, 0, 50)
    Sleep(400)
    BeginChrThread(0x1D, 1, 0, 52)
    WaitChrThread(0xE, 1)
    Sound(531, 0, 80, 0)
    WaitChrThread(0x14, 1)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)
    Sound(805, 0, 80, 0)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x13, 1)
    EndChrThread(0x29, 0x1)
    WaitChrThread(0x19, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1D, 1)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    ClearChrFlags(0x28, 0x4)
    ClearChrFlags(0x1F, 0x4)
    ClearChrFlags(0x20, 0x4)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    ClearChrFlags(0x1E, 0x4)
    OP_90(0x1E, -40550, 4000, 24100, 315)
    OP_90(0x26, -39100, 4000, 22600, 315)
    OP_90(0x27, -37000, 4000, 23300, 315)
    OP_90(0x28, -39500, 4000, 19900, 315)
    OP_90(0x23, -36850, 4000, 20350, 315)
    OP_90(0x24, -34650, 4000, 20100, 315)
    OP_90(0x25, -35800, 4000, 18000, 315)
    OP_90(0x1F, -32549, 4000, 19950, 315)
    OP_90(0x20, -32700, 4000, 17600, 315)
    OP_90(0x21, -34550, 4000, 16350, 315)
    OP_90(0x22, -36850, 4000, 16350, 315)
    BeginChrThread(0x1E, 1, 0, 54)
    BeginChrThread(0x29, 1, 0, 76)
    BeginChrThread(0x26, 1, 0, 70)
    BeginChrThread(0x27, 1, 0, 72)
    BeginChrThread(0x28, 1, 0, 74)
    BeginChrThread(0x23, 1, 0, 64)
    BeginChrThread(0x24, 1, 0, 66)
    BeginChrThread(0x25, 1, 0, 68)
    BeginChrThread(0x1F, 1, 0, 56)
    BeginChrThread(0x20, 1, 0, 58)
    BeginChrThread(0x21, 1, 0, 60)
    BeginChrThread(0x22, 1, 0, 60)
    OP_68(-38550, 1700, 22050, 0)
    MoveCamera(90, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    OP_68(-52550, 1700, 41050, 4500)
    MoveCamera(50, 10, 0, 4500)
    SetCameraDistance(24500, 4500)
    OP_0D()
    Sleep(2000)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sleep(1000)
    CancelBlur(2000)
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x20, 0x0)
    EndChrThread(0x21, 0x0)
    EndChrThread(0x22, 0x0)
    EndChrThread(0x23, 0x0)
    EndChrThread(0x24, 0x0)
    EndChrThread(0x25, 0x0)
    EndChrThread(0x1E, 0x0)
    ClearChrFlags(0x1F, 0x20)
    ClearChrFlags(0x20, 0x20)
    ClearChrFlags(0x21, 0x20)
    ClearChrFlags(0x22, 0x20)
    ClearChrFlags(0x23, 0x20)
    ClearChrFlags(0x24, 0x20)
    ClearChrFlags(0x25, 0x20)
    ClearChrFlags(0x1E, 0x20)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x1F, 0x3)
    EndChrThread(0x20, 0x0)
    EndChrThread(0x20, 0x3)
    EndChrThread(0x21, 0x0)
    EndChrThread(0x21, 0x3)
    EndChrThread(0x22, 0x0)
    EndChrThread(0x22, 0x3)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x29, 0x1)
    EndChrThread(0x26, 0x1)
    EndChrThread(0x27, 0x1)
    EndChrThread(0x28, 0x1)
    OP_68(-44000, 8600, 73000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    SetChrChipByIndex(0xE, 0x39)
    SetChrSubChip(0xE, 0x3)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#07903F──Commence operation.\x02\x03",
            "#07901FCrossbell CGF members, liberation\x01",
            "squad and Divine Wolves unit...\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7544", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    SetChrSubChip(0xE, 0x4)
    Sound(802, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xE,
        "#07907F#4SOpen combat!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(80, 0, -1, -1)
    SetChrName("CGF Members")

    AnonymousTalk(
        0xFF,
        "#5SYes ma'am!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    BeginChrThread(0x19, 0, 0, 22)
    Sleep(30)
    BeginChrThread(0x1A, 0, 0, 22)
    BeginChrThread(0x1B, 0, 0, 22)
    Sleep(30)
    BeginChrThread(0x1C, 0, 0, 22)
    BeginChrThread(0x1D, 0, 0, 22)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sound(1001, 0, 100, 0)
    SetMessageWindowPos(40, 30, -1, -1)
    SetChrName("Wolves")

    AnonymousTalk(
        0xFF,
        "#5SWoof!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopEffect(0x0, 0x2)
    BeginChrThread(0x29, 2, 0, 77)
    OP_82(0x32, 0x32, 0xBB8, 0x4E20)
    BeginChrThread(0x14, 1, 0, 35)
    BeginChrThread(0x15, 1, 0, 37)
    BeginChrThread(0x16, 1, 0, 39)
    BeginChrThread(0x17, 1, 0, 41)
    BeginChrThread(0x18, 1, 0, 43)
    BeginChrThread(0xF, 1, 0, 25)
    BeginChrThread(0x10, 1, 0, 27)
    BeginChrThread(0x11, 1, 0, 29)
    BeginChrThread(0x12, 1, 0, 31)
    BeginChrThread(0x13, 1, 0, 33)
    BeginChrThread(0x19, 1, 0, 45)
    BeginChrThread(0x1A, 1, 0, 47)
    BeginChrThread(0x1B, 1, 0, 49)
    BeginChrThread(0x1C, 1, 0, 51)
    BeginChrThread(0x1D, 1, 0, 53)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sleep(1000)
    Fade(500)
    SetChrPos(0x1E, -44150, 0, 55700, 0)
    SetChrPos(0x23, -43050, 0, 54250, 0)
    SetChrPos(0x24, -45150, 0, 53500, 0)
    SetChrPos(0x25, -44000, 0, 52250, 0)
    SetChrPos(0x26, -46350, 0, 54900, 0)
    SetChrPos(0x27, -41550, 0, 55700, 0)
    SetChrPos(0x28, -42100, 0, 51850, 0)
    SetChrFlags(0x27, 0x800)
    SetChrFlags(0x28, 0x800)
    SetChrPos(0x1F, -41050, 0, 51100, 0)
    SetChrPos(0x20, -42650, 0, 50050, 0)
    SetChrPos(0x21, -44850, 0, 50400, 0)
    SetChrPos(0x22, -46700, 0, 50600, 0)
    OP_68(-44230, 2430, 57830, 0)
    MoveCamera(124, 39, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(15000, 0)
    OP_68(-44360, 6230, 63300, 3000)
    MoveCamera(115, 42, 0, 3000)
    SetCameraDistance(18000, 3000)
    BeginChrThread(0x1E, 1, 0, 55)
    BeginChrThread(0x26, 1, 0, 71)
    BeginChrThread(0x27, 1, 0, 73)
    BeginChrThread(0x28, 1, 0, 75)
    BeginChrThread(0x23, 1, 0, 65)
    BeginChrThread(0x24, 1, 0, 67)
    BeginChrThread(0x25, 1, 0, 69)
    BeginChrThread(0x1F, 1, 0, 57)
    BeginChrThread(0x20, 1, 0, 59)
    BeginChrThread(0x21, 1, 0, 61)
    BeginChrThread(0x22, 1, 0, 61)
    OP_6F(0x79)
    Fade(500)
    OP_68(-44100, 5330, 63070, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(31500, 0)
    MoveCamera(55, 35, 0, 6000)
    SetCameraDistance(31500, 6000)
    Sleep(4000)
    StopSound(860, 1000, 50)
    StopSound(861, 1000, 40)
    BeginChrThread(0x29, 2, 0, 78)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    EndChrThread(0x29, 0x1)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0x22, 2)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2F0E end

    def Function_14_3AFF(): pass

    label("Function_14_3AFF")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3B37"),
        (1, "loc_3B43"),
        (2, "loc_3B4F"),
        (3, "loc_3B5B"),
        (4, "loc_3B67"),
        (5, "loc_3B73"),
        (6, "loc_3B7F"),
        (SWITCH_DEFAULT, "loc_3B8B"),
    )


    label("loc_3B37")

    OP_A0(0xFE, 1950, 0x0, 0xFB)
    Jump("loc_3B97")

    label("loc_3B43")

    OP_A0(0xFE, 2050, 0x0, 0xFB)
    Jump("loc_3B97")

    label("loc_3B4F")

    OP_A0(0xFE, 2100, 0x0, 0xFB)
    Jump("loc_3B97")

    label("loc_3B5B")

    OP_A0(0xFE, 1900, 0x0, 0xFB)
    Jump("loc_3B97")

    label("loc_3B67")

    OP_A0(0xFE, 2150, 0x0, 0xFB)
    Jump("loc_3B97")

    label("loc_3B73")

    OP_A0(0xFE, 1850, 0x0, 0xFB)
    Jump("loc_3B97")

    label("loc_3B7F")

    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("loc_3B97")

    label("loc_3B8B")

    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("loc_3B97")

    label("loc_3B97")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BAE")
    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("loc_3B97")

    label("loc_3BAE")

    Return()

    # Function_14_3AFF end

    def Function_15_3BAF(): pass

    label("Function_15_3BAF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BE2")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BD6")
    OP_4C(0xFE, 0x0)
    Jump("loc_3BDA")

    label("loc_3BD6")

    OP_4B(0xFE, 0x0)

    label("loc_3BDA")

    Sleep(500)
    Jump("Function_15_3BAF")

    label("loc_3BE2")

    Return()

    # Function_15_3BAF end

    def Function_16_3BE3(): pass

    label("Function_16_3BE3")

    SetChrChipByIndex(0xFE, 0x25)

    label("loc_3BE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C36")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 1050, 1700, 0, -20, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("loc_3BE7")

    label("loc_3C36")

    Return()

    # Function_16_3BE3 end

    def Function_17_3C37(): pass

    label("Function_17_3C37")

    SetChrChipByIndex(0xFE, 0x2F)

    label("loc_3C3B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C8A")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x3)
    Jump("loc_3C3B")

    label("loc_3C8A")

    Return()

    # Function_17_3C37 end

    def Function_18_3C8B(): pass

    label("Function_18_3C8B")

    SetChrChipByIndex(0xFE, 0x1F)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3CDD"),
        (1, "loc_3CE9"),
        (2, "loc_3CF5"),
        (3, "loc_3D01"),
        (4, "loc_3D0D"),
        (5, "loc_3D19"),
        (6, "loc_3D25"),
        (SWITCH_DEFAULT, "loc_3D31"),
    )


    label("loc_3CDD")

    OP_A0(0xFE, 1200, 0x0, 0x5)
    Jump("loc_3D3D")

    label("loc_3CE9")

    OP_A0(0xFE, 1300, 0x0, 0x5)
    Jump("loc_3D3D")

    label("loc_3CF5")

    OP_A0(0xFE, 1400, 0x0, 0x5)
    Jump("loc_3D3D")

    label("loc_3D01")

    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3D3D")

    label("loc_3D0D")

    OP_A0(0xFE, 1600, 0x0, 0x5)
    Jump("loc_3D3D")

    label("loc_3D19")

    OP_A0(0xFE, 1700, 0x0, 0x5)
    Jump("loc_3D3D")

    label("loc_3D25")

    OP_A0(0xFE, 1800, 0x0, 0x5)
    Jump("loc_3D3D")

    label("loc_3D31")

    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3D3D")

    label("loc_3D3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D54")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3D3D")

    label("loc_3D54")

    Return()

    # Function_18_3C8B end

    def Function_19_3D55(): pass

    label("Function_19_3D55")

    SetChrChipByIndex(0xFE, 0x1E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D6F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D86")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_3D6F")

    label("loc_3D86")

    Return()

    # Function_19_3D55 end

    def Function_20_3D87(): pass

    label("Function_20_3D87")

    SetChrChipByIndex(0xFE, 0x3D)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DA1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DB8")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    Jump("loc_3DA1")

    label("loc_3DB8")

    Return()

    # Function_20_3D87 end

    def Function_21_3DB9(): pass

    label("Function_21_3DB9")

    SetChrChipByIndex(0xFE, 0x3C)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DD3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DF1")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_3DD3")

    label("loc_3DF1")

    Return()

    # Function_21_3DB9 end

    def Function_22_3DF2(): pass

    label("Function_22_3DF2")

    SetChrChipByIndex(0xFE, 0x3E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Return()

    # Function_22_3DF2 end

    def Function_23_3E17(): pass

    label("Function_23_3E17")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF3, 0x1388, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF3, 0x1388, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF3, 0x1388, 0x1194, 0x0)
    OP_95(0xFE, -44000, 8000, 73000, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_3E17 end

    def Function_24_3E7A(): pass

    label("Function_24_3E7A")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1194, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1194, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_95(0xFE, -42550, 8000, 80000, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_3E7A end

    def Function_25_3EF1(): pass

    label("Function_25_3EF1")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -41350, 7990, 71150, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sound(531, 0, 100, 0)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_25_3EF1 end

    def Function_26_3F30(): pass

    label("Function_26_3F30")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x1004, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x1004, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1194, 0x1004, 0x0)
    OP_95(0xFE, -42050, 8000, 77650, 4500, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_3F30 end

    def Function_27_3FA7(): pass

    label("Function_27_3FA7")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -43900, 7700, 70250, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    PlayEffect(0x1, 0x0, 0xFF, 0x0, -44050, 2070, 58650, 0, -50, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_27_3FA7 end

    def Function_28_4017(): pass

    label("Function_28_4017")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0xFA0, 0xFA0, 0x0)
    OP_95(0xFE, -41350, 8000, 75050, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_4017 end

    def Function_29_408E(): pass

    label("Function_29_408E")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -42600, 8140, 71650, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_29_408E end

    def Function_30_40C7(): pass

    label("Function_30_40C7")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_95(0xFE, -42400, 8000, 76250, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_40C7 end

    def Function_31_413E(): pass

    label("Function_31_413E")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -46250, 8000, 72600, 4000, 0x0)
    OP_95(0xFE, -46700, 8050, 70350, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_31_413E end

    def Function_32_418B(): pass

    label("Function_32_418B")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0xFA0, 0x0)
    OP_95(0xFE, -40850, 8000, 79750, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_418B end

    def Function_33_4202(): pass

    label("Function_33_4202")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2E)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45100, 8000, 75150, 4000, 0x0)
    OP_95(0xFE, -45350, 8170, 70750, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 17)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_33_4202 end

    def Function_34_424F(): pass

    label("Function_34_424F")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1324, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1324, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1324, 0x0)
    OP_95(0xFE, -45200, 8000, 74250, 4100, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_424F end

    def Function_35_42C6(): pass

    label("Function_35_42C6")

    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45650, 8000, 72400, 4000, 0x0)
    OP_95(0xFE, -44000, 6110, 64450, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_42C6 end

    def Function_36_430C(): pass

    label("Function_36_430C")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x1194, 0x0)
    OP_95(0xFE, -43300, 8000, 74800, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_430C end

    def Function_37_4383(): pass

    label("Function_37_4383")

    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -42350, 8000, 72550, 4000, 0x0)
    OP_95(0xFE, -42500, 6280, 64849, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sound(844, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_4383 end

    def Function_38_43CF(): pass

    label("Function_38_43CF")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF9, 0x1770, 0x109A, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1004, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF3, 0x157C, 0x1004, 0x0)
    OP_95(0xFE, -44550, 8000, 75850, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_43CF end

    def Function_39_4446(): pass

    label("Function_39_4446")

    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45550, 8000, 74000, 4000, 0x0)
    OP_95(0xFE, -45550, 8000, 72400, 4000, 0x0)
    OP_95(0xFE, -45550, 6440, 65200, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_39_4446 end

    def Function_40_44A0(): pass

    label("Function_40_44A0")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5BCC, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1194, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0x1194, 0x0)
    OP_95(0xFE, -45800, 8000, 77000, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_44A0 end

    def Function_41_4517(): pass

    label("Function_41_4517")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45550, 8000, 74000, 4000, 0x0)
    OP_95(0xFE, -45550, 8000, 72400, 4000, 0x0)
    OP_95(0xFE, -44500, 6990, 67000, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_4517 end

    def Function_42_4574(): pass

    label("Function_42_4574")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x59D8, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0xFA0, 0x0)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x157C, 0xFA0, 0x0)
    OP_95(0xFE, -43750, 8000, 77750, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_4574 end

    def Function_43_45EB(): pass

    label("Function_43_45EB")

    SetChrChipByIndex(0xFE, 0x33)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -43450, 8000, 74700, 4000, 0x0)
    OP_95(0xFE, -42350, 8000, 72550, 4000, 0x0)
    OP_95(0xFE, -43100, 7030, 67600, 4000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sound(844, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_43_45EB end

    def Function_44_464B(): pass

    label("Function_44_464B")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF4A5C, 0x1F40, 0x15FF4, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 20)
    OP_95(0xFE, -47800, 8000, 74700, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_44_464B end

    def Function_45_46A7(): pass

    label("Function_45_46A7")

    BeginChrThread(0x29, 1, 0, 76)
    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -46300, 8000, 72350, 5000, 0x0)
    OP_95(0xFE, -46550, 6010, 64250, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x29, 0x1)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_45_46A7 end

    def Function_46_46F4(): pass

    label("Function_46_46F4")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF5420, 0x1F40, 0x1653A, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0x29, 1, 0, 76)
    BeginChrThread(0xFE, 0, 0, 20)
    OP_95(0xFE, -47050, 8000, 78600, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x29, 0x1)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_46_46F4 end

    def Function_47_475A(): pass

    label("Function_47_475A")

    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -46300, 8000, 72350, 5000, 0x0)
    OP_95(0xFE, -46300, 7050, 66650, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_47_475A end

    def Function_48_479D(): pass

    label("Function_48_479D")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF59FC, 0x1F40, 0x16666, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 20)
    OP_95(0xFE, -45000, 8000, 81250, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_48_479D end

    def Function_49_47F9(): pass

    label("Function_49_47F9")

    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -47350, 8000, 74250, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF42BE, 0x23BE, 0x11684, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_95(0xFE, -48100, 8100, 68250, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_49_47F9 end

    def Function_50_486F(): pass

    label("Function_50_486F")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF60D2, 0x1F40, 0x16602, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 20)
    OP_95(0xFE, -42400, 8000, 83750, 5000, 0x0)
    OP_95(0xFE, -43400, 8000, 80750, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_50_486F end

    def Function_51_48DF(): pass

    label("Function_51_48DF")

    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -40300, 8000, 76350, 5000, 0x0)
    OP_95(0xFE, -40300, 8000, 73900, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF6582, 0x23F0, 0x11684, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_95(0xFE, -40300, 6600, 64900, 5000, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF5E7A, 0x14C8, 0xF4BA, 0x1F4, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x3E8)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_51_48DF end

    def Function_52_49A1(): pass

    label("Function_52_49A1")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(844, 0, 30, 0)
    OP_9D(0xFE, 0xFFFF6906, 0x1F40, 0x16184, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 20)
    OP_95(0xFE, -39600, 8000, 85050, 5000, 0x0)
    OP_95(0xFE, -40600, 8000, 82050, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_52_49A1 end

    def Function_53_4A17(): pass

    label("Function_53_4A17")

    Sleep(1000)
    BeginChrThread(0xFE, 0, 0, 20)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -40300, 8000, 76350, 5000, 0x0)
    OP_95(0xFE, -40300, 8000, 73900, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0xFFFF6582, 0x23F0, 0x11684, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_95(0xFE, -40300, 6600, 64900, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 21)
    Return()

    # Function_53_4A17 end

    def Function_54_4A9E(): pass

    label("Function_54_4A9E")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x1450, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_54_4A9E end

    def Function_55_4AF9(): pass

    label("Function_55_4AF9")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -44100, 5070, 62200, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    label("loc_4B1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C3F")
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x34)
    SetChrSubChip(0x14, 0x2)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x4)
    OP_9D(0x14, 0xFFFF53BC, 0x11F8, 0xF582, 0x3E8, 0xFA0)
    SetChrFlags(0x14, 0x4)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(532, 0, 60, 0)

    def lambda_4B78():
        OP_A0(0xFE, 1500, 0x3, 0x4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4B78)
    Sound(540, 0, 60, 0)
    Sound(501, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4B99():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4B99)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x4)
    WaitChrThread(0xFE, 3)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Sound(538, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x2B)
    OP_A0(0xFE, 1500, 0x0, 0x1)

    def lambda_4BEB():
        OP_A0(0xFE, 1000, 0x2, 0x4)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_4BEB)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4BFD():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BFD)
    SetChrChipByIndex(0x14, 0x34)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x4)
    OP_9B(0x1, 0x14, 0x0, 0xFFFFFD12, 0x2710, 0x0)
    SetChrFlags(0x14, 0x4)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x4)
    Sleep(1000)
    Jump("loc_4B1F")

    label("loc_4C3F")

    Return()

    # Function_55_4AF9 end

    def Function_56_4C40(): pass

    label("Function_56_4C40")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_56_4C40 end

    def Function_57_4C75(): pass

    label("Function_57_4C75")

    SetChrChipByIndex(0xFE, 0x24)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -44300, 7250, 67800, 0, -30, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Sound(860, 2, 60, 0)
    Sound(861, 2, 50, 0)
    BeginChrThread(0xFE, 0, 0, 16)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_57_4C75 end

    def Function_58_4CF1(): pass

    label("Function_58_4CF1")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_58_4CF1 end

    def Function_59_4D26(): pass

    label("Function_59_4D26")

    SetChrChipByIndex(0xFE, 0x24)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 16)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_59_4D26 end

    def Function_60_4D5F(): pass

    label("Function_60_4D5F")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x6590, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_60_4D5F end

    def Function_61_4D94(): pass

    label("Function_61_4D94")

    SetChrChipByIndex(0xFE, 0x24)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 16)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_61_4D94 end

    def Function_62_4DCD(): pass

    label("Function_62_4DCD")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x6978, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_62_4DCD end

    def Function_63_4E02(): pass

    label("Function_63_4E02")

    SetChrChipByIndex(0xFE, 0x24)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 16)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_63_4E02 end

    def Function_64_4E3B(): pass

    label("Function_64_4E3B")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x5208, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x13EC, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x13EC, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x13EC, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_64_4E3B end

    def Function_65_4E96(): pass

    label("Function_65_4E96")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -42550, 4800, 63150, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x15, 0x34)

    def lambda_4EC5():
        OP_A0(0xFE, 1500, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4EC5)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4ED7():
        OP_96(0xFE, 0xFFFF59CA, 0x141E, 0xFB2C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4ED7)

    def lambda_4EF1():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_4EF1)
    Sound(538, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4F18():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4F18)
    WaitChrThread(0x15, 1)
    SetChrFlags(0x15, 0x4)
    Return()

    # Function_65_4E96 end

    def Function_66_4F36(): pass

    label("Function_66_4F36")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_66_4F36 end

    def Function_67_4F91(): pass

    label("Function_67_4F91")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45400, 5030, 63600, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x16, 0x34)

    def lambda_4FC0():
        OP_A0(0xFE, 1500, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_4FC0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4FD2():
        OP_96(0xFE, 0xFFFF4EA8, 0x14F0, 0xFCEE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4FD2)

    def lambda_4FEC():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_4FEC)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_500D():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_500D)
    WaitChrThread(0x16, 1)
    SetChrFlags(0x16, 0x4)
    Return()

    # Function_67_4F91 end

    def Function_68_502B(): pass

    label("Function_68_502B")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 14)
    OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x14B4, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xBB8, 0x14B4, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x14B4, 0x0)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_68_502B end

    def Function_69_5086(): pass

    label("Function_69_5086")

    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -45250, 3920, 59150, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x3E8)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_69_5086 end

    def Function_70_50B4(): pass

    label("Function_70_50B4")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4844, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x13EC, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x13EC, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x13EC, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_70_50B4 end

    def Function_71_5101(): pass

    label("Function_71_5101")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -46400, 4850, 61800, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 19)
    Sleep(1000)

    label("loc_5132")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52AF")
    EndChrThread(0x19, 0x0)
    SetChrChipByIndex(0x19, 0x3D)
    SetChrSubChip(0x19, 0x0)
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 60, 0)
    ClearChrFlags(0x19, 0x4)
    OP_9D(0x19, 0xFFFF4A8E, 0x1126, 0xF3F2, 0x3E8, 0xFA0)
    SetChrFlags(0x19, 0x4)
    Sound(657, 0, 50, 0)
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x19, 0, 0, 21)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(501, 0, 60, 0)

    def lambda_51D5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_51D5)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x4)
    WaitChrThread(0xFE, 0)
    BeginChrThread(0xFE, 0, 0, 19)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A0(0xFE, 1500, 0x0, 0x2)
    Sleep(500)
    ClearChrFlags(0xFE, 0x4)

    def lambda_5242():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5242)
    Sound(657, 0, 50, 0)

    def lambda_525D():
        OP_A0(0xFE, 1500, 0x3, 0x5)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_525D)

    def lambda_526A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_526A)
    ClearChrFlags(0x19, 0x4)
    OP_9B(0x1, 0x19, 0x0, 0xFFFFFC18, 0x2710, 0x0)
    SetChrFlags(0x19, 0x4)
    WaitChrThread(0xFE, 3)
    WaitChrThread(0xFE, 0)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 19)
    Jump("loc_5132")

    label("loc_52AF")

    Return()

    # Function_71_5101 end

    def Function_72_52B0(): pass

    label("Function_72_52B0")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4650, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x1388, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_72_52B0 end

    def Function_73_52FD(): pass

    label("Function_73_52FD")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -41750, 4270, 60750, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 19)
    Return()

    # Function_73_52FD end

    def Function_74_532C(): pass

    label("Function_74_532C")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xFA0, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0xBB8, 0x1450, 0x0)
    OP_9B(0x0, 0xFE, 0x19, 0x2710, 0x1450, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_74_532C end

    def Function_75_5379(): pass

    label("Function_75_5379")

    BeginChrThread(0xFE, 0, 0, 18)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -43200, 3150, 58750, 5000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 19)
    Return()

    # Function_75_5379 end

    def Function_76_53AF(): pass

    label("Function_76_53AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53C8")
    Sound(845, 0, 50, 0)
    Sleep(500)
    Jump("Function_76_53AF")

    label("loc_53C8")

    Return()

    # Function_76_53AF end

    def Function_77_53C9(): pass

    label("Function_77_53C9")

    Sound(974, 2, 40, 0)
    Sleep(200)
    OP_25(0x3CE, 0x32)
    Sleep(200)
    OP_25(0x3CE, 0x3C)
    Sleep(200)
    OP_25(0x3CE, 0x46)
    Sleep(200)
    OP_25(0x3CE, 0x50)
    Sleep(200)
    OP_25(0x3CE, 0x5A)
    Sleep(200)
    OP_25(0x3CE, 0x64)
    Return()

    # Function_77_53C9 end

    def Function_78_53FA(): pass

    label("Function_78_53FA")

    OP_25(0x3CE, 0x5F)
    Sleep(50)
    OP_25(0x3CE, 0x5A)
    Sleep(50)
    OP_25(0x3CE, 0x55)
    Sleep(50)
    OP_25(0x3CE, 0x50)
    Sleep(50)
    OP_25(0x3CE, 0x4B)
    Sleep(50)
    OP_25(0x3CE, 0x46)
    Sleep(50)
    OP_25(0x3CE, 0x41)
    Sleep(50)
    OP_25(0x3CE, 0x3C)
    Sleep(50)
    OP_25(0x3CE, 0x37)
    Sleep(50)
    OP_25(0x3CE, 0x32)
    Sleep(50)
    OP_25(0x3CE, 0x2D)
    Sleep(50)
    OP_25(0x3CE, 0x28)
    Sleep(50)
    OP_25(0x3CE, 0x23)
    Sleep(50)
    OP_25(0x3CE, 0x1E)
    Sleep(50)
    OP_25(0x3CE, 0x19)
    Sleep(50)
    OP_25(0x3CE, 0x14)
    Sleep(50)
    OP_25(0x3CE, 0xF)
    Sleep(50)
    OP_25(0x3CE, 0xA)
    Sleep(50)
    OP_25(0x3CE, 0x5)
    Sleep(50)
    OP_25(0x3CE, 0x0)
    Return()

    # Function_78_53FA end

    def Function_79_5484(): pass

    label("Function_79_5484")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Fumu, you're good...\x01",
            "You're quite byurihoo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, as proof you have won against\x01",
            "me, I'll puresento you disu medaru.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x29),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x29, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00012FT-Thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, then, from now on, you'll be\x01",
            "called the "Crazy Wave Hunter".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, at any rate you only won\x01",
            "wan taimu against me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't forget to porisshu\x01",
            "the byuutii from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C0, 5)
    SetChrPos(0x8, -13910, 5380, 56930, 295)
    OP_66(0x1, 0x1)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -11300, 5380, 56730, 250)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_79_5484 end

    def Function_80_5682(): pass

    label("Function_80_5682")


    ChrTalk(
        0x8,
        (
            "Uh uh, and so it's my vikutorii\x01",
            "in this dyueru.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, go uosshu your feisu\x01",
            "and come again.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_80_5682 end

    def Function_81_56E8(): pass

    label("Function_81_56E8")


    ChrTalk(
        0x8,
        (
            "Fumu, is it your\x01",
            "toiretto taimu?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Natto byurihoo.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_81_56E8 end

    def Function_82_5727(): pass

    label("Function_82_5727")


    ChrTalk(
        0x8,
        "Nnn, natto byurihoo result.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, we can dyueringu again\x01",
            "eburitaimu, no?\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_82_5727 end

    def Function_83_577C(): pass

    label("Function_83_577C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetChrPos(0x0, -1500, 0, 9000, 0)
    SetChrPos(0x1, -1500, 0, 9000, 0)
    SetChrPos(0x2, -1500, 0, 9000, 0)
    SetChrPos(0x3, -1500, 0, 9000, 0)
    SetMapObjFlags(0xE, 0x1000)
    OP_68(-11500, 3000, 8000, 0)
    MoveCamera(77, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25500, 0)
    OP_68(-11500, 2500, 8000, 8000)
    MoveCamera(87, 17, 0, 8000)
    SetCameraDistance(21500, 8000)
    OP_71(0xE, 0x208, 0x2BC, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(700)
    Sound(202, 0, 100, 0)
    Sleep(100)
    Sound(223, 0, 100, 0)
    Sleep(1200)
    FadeToDark(1000, 16777215, -1)
    Sound(181, 0, 100, 0)
    Sleep(1500)
    FadeToBright(1000, 16777215)
    OP_0D()
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_83_577C end

    SaveToFile()

Try(main)
