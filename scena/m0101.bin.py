from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0101.bin",                # FileName
        "m0101",                    # MapName
        "m0101",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0101",                  # 0
        "Boy",                    # 1
        "Tio",                    # 2
        "Yin",                    # 3
        "符術",                   # 4
        "ブラッドモナド",         # 5
        "トルゾーＢ",             # 6
        "SE制御",                 # 7
        "bm0101",                 # 8
        "bm0101",                 # 9
        "bm0101",                 # 10
        "bm0101",                 # 11
        "bm0100",                 # 12
        "bm0100",                 # 13
        "bm0100",                 # 14
        "bm0100",                 # 15
        "bm0100",                 # 16
        "bm0100",                 # 17
    ))

    ATBonus("ATBonus_434", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_7EBA", 11,  1,   8,   0,   3,   7,   0)
    Sepith("Sepith_7EAA", 0,   10,  5,   0,   6,   2,   4)
    Sepith("Sepith_7EC2", 0,   0,   0,   8,   6,   6,   6)
    Sepith("Sepith_7EB2", 6,   0,   11,  0,   0,   4,   6)

    MonsterBattlePostion("MonsterBattlePostion_4D4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4EC", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F0", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_514", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_518", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_51C", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_520", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_524", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_528", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_52C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4CC", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_49C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_500", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_504", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_508", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_50C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_510", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_474", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_47C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 2, 13, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_6C4", 0x0000, 62, 6, 60, 6, 1, 25, 0, "bm0101", "Sepith_7EBA", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_534", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_7EAA", 30, 45, 20, 5,
        (
            ("ms63800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms63800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_AAC", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_7EC2", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_78C", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_7EC2", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_5FC", 0x0000, 62, 6, 60, 6, 1, 30, 0, "bm0101", "Sepith_7EB2", 30, 45, 20, 5,
        (
            ("ms68700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms68700.dat", "ms68700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms68700.dat", "ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_B74", 0x0000, 62, 6, 60, 0, 1, 0, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68700.dat", "ms68700.dat", "ms68700.dat", "ms68700.dat", "ms68700.dat", "ms68700.dat", "ms68700.dat", "ms68700.dat", "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7451", "ed7453", "ATBonus_434"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BB8", 0x0000, 62, 6, 60, 0, 1, 0, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7451", "ed7453", "ATBonus_434"),
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
        "monster/ch63850.itc",               # 10
        "monster/ch63851.itc",               # 11
        "monster/ch68750.itc",               # 12
        "monster/ch68750.itc",               # 13
        "monster/ch75850.itc",               # 14
        "monster/ch75851.itc",               # 15
        "monster/ch60550.itc",               # 16
        "monster/ch60550.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(109959,  4294961796, 19,      0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(92000,   4294958796, 90500,   0,    484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(99960,   100050,  4294957296, 0x1010000,    "BattleInfo_6C4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(100360,  200740,  0,       0x1010000,    "BattleInfo_534", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294967006, 199690,  0,       0x1010000,    "BattleInfo_AAC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(109910,  99810,   4294960296, 0x1010000,    "BattleInfo_78C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(200810,  94840,   0,       0x1010000,    "BattleInfo_6C4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(199760,  195940,  4294957296, 0x1010000,    "BattleInfo_5FC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(202350,  204410,  4294957296, 0x1010000,    "BattleInfo_534", 0,   16,  0xFFFF, 0,  1)

    DeclActor(500000,  150,     208500,  1200,    500000,  1150,    208500,  0x007C, 0,  8,  0x0000)
    DeclActor(109960,  4294961296, 20,      1200,    109960,  4294962296, 20,      0x007C, 0,  4,  0x0000)
    DeclActor(109970,  4294964296, 113430,  1200,    109970,  4294965296, 113430,  0x007C, 0,  5,  0x0000)
    DeclActor(190010,  4294963296, 200010,  1200,    190010,  4294964296, 200010,  0x007C, 0,  6,  0x0000)
    DeclActor(92000,   4294958296, 90500,   1200,    92000,   4294959296, 90500,   0x007C, 0,  7,  0x0000)
    DeclActor(2000,    0,       0,       1200,    2500,    1000,    0,       0x007C, 0,  14, 0x0000)
    DeclActor(108000,  4294961296, 2500,    2000,    108000,  4294962296, 2500,    0x007C, 0,  10, 0x0000)
    DeclActor(85500,   4294961296, 103000,  2000,    85500,   4294962296, 103000,  0x007C, 0,  11, 0x0000)
    DeclActor(203430,  4294961296, 184020,  2000,    203430,  4294962296, 184020,  0x007C, 0,  12, 0x0000)
    DeclActor(320000,  4294966296, 302800,  1200,    320000,  500,     302800,  0x007C, 0,  9,  0x0000)
    DeclActor(503490,  0,       199590,  1200,    503490,  1500,    199590,  0x007C, 0,  48, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7

    ScpFunction((
        "Function_0_D20",          # 00, 0
        "Function_1_D3F",          # 01, 1
        "Function_2_D5E",          # 02, 2
        "Function_3_DEF",          # 03, 3
        "Function_4_148E",         # 04, 4
        "Function_5_16A9",         # 05, 5
        "Function_6_1812",         # 06, 6
        "Function_7_1963",         # 07, 7
        "Function_8_1B7E",         # 08, 8
        "Function_9_1C06",         # 09, 9
        "Function_10_1CFA",        # 0A, 10
        "Function_11_1D16",        # 0B, 11
        "Function_12_1D32",        # 0C, 12
        "Function_13_1D4E",        # 0D, 13
        "Function_14_224D",        # 0E, 14
        "Function_15_23D4",        # 0F, 15
        "Function_16_251B",        # 10, 16
        "Function_17_282E",        # 11, 17
        "Function_18_284D",        # 12, 18
        "Function_19_2AA1",        # 13, 19
        "Function_20_2E6F",        # 14, 20
        "Function_21_334F",        # 15, 21
        "Function_22_75F7",        # 16, 22
        "Function_23_7648",        # 17, 23
        "Function_24_76B1",        # 18, 24
        "Function_25_7713",        # 19, 25
        "Function_26_7775",        # 1A, 26
        "Function_27_77CA",        # 1B, 27
        "Function_28_781F",        # 1C, 28
        "Function_29_7874",        # 1D, 29
        "Function_30_78E7",        # 1E, 30
        "Function_31_7921",        # 1F, 31
        "Function_32_795B",        # 20, 32
        "Function_33_79B3",        # 21, 33
        "Function_34_7A0B",        # 22, 34
        "Function_35_7A45",        # 23, 35
        "Function_36_7A64",        # 24, 36
        "Function_37_7AA4",        # 25, 37
        "Function_38_7AE4",        # 26, 38
        "Function_39_7B60",        # 27, 39
        "Function_40_7BA7",        # 28, 40
        "Function_41_7C2A",        # 29, 41
        "Function_42_7C4C",        # 2A, 42
        "Function_43_7C90",        # 2B, 43
        "Function_44_7CD4",        # 2C, 44
        "Function_45_7CF7",        # 2D, 45
        "Function_46_7D1A",        # 2E, 46
        "Function_47_7DD0",        # 2F, 47
        "Function_48_7E31",        # 30, 48
    ))


    def Function_0_D20(): pass

    label("Function_0_D20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D3E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_D20")

    label("loc_D3E")

    Return()

    # Function_0_D20 end

    def Function_1_D3F(): pass

    label("Function_1_D3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D5D")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_D3F")

    label("loc_D5D")

    Return()

    # Function_1_D3F end

    def Function_2_D5E(): pass

    label("Function_2_D5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D86")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D86")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D9D")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 16)
    Jump("loc_DD4")

    label("loc_D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_DB1")
    ClearScenarioFlags(0x22, 1)
    Event(0, 19)
    Jump("loc_DD4")

    label("loc_DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_DC5")
    ClearScenarioFlags(0x22, 2)
    Event(0, 18)
    Jump("loc_DD4")

    label("loc_DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_DD4")
    ClearScenarioFlags(0x22, 3)
    Event(0, 46)

    label("loc_DD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DEE")
    Event(0, 20)

    label("loc_DEE")

    Return()

    # Function_2_D5E end

    def Function_3_DEF(): pass

    label("Function_3_DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E04")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E68")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E4B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x241), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x32, 0xC8)
    SetMapFlags(0x2)
    Jump("loc_E68")

    label("loc_E4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E68")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x241), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x64, 0xC8)

    label("loc_E68")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E84")
    ClearMapObjFlags(0x13, 0x10)
    OP_66(0x0, 0x1)

    label("loc_E84")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EB9")
    SetMapFlags(0x2000)
    OP_E2(0x0)
    Jump("loc_EBE")

    label("loc_EB9")

    ClearMapFlags(0x2000)

    label("loc_EBE")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 106000, -6000, 0, 6000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 98000, -6000, 0, 6000, 2000, 90000)
    SetBarrier(0x0, 0x2, 0x1, 0x0, 100000, -7380, 89000, 4000, 2000, 0)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 100000, -7800, 110000, 4000, 2000, 0)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 96000, -7000, 100000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 104000, -7000, 100000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, 92000, -8000, 96000, 4000, 2000, 0)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 0, -7000, 100000, 4000, 2000, 0)
    SetBarrier(0x0, 0x8, 0x1, 0x0, 0, -7000, 92000, 4000, 2000, 0)
    SetBarrier(0x0, 0x9, 0x1, 0x0, 200000, -8000, 190000, 8000, 2000, 0)
    SetBarrier(0x0, 0xA, 0x1, 0x0, 200000, -8000, 210000, 8000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 0)), scpexpr(EXPR_END)), "loc_107A")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    SetBarrier(0x3, 0xA, 0x1)
    SetMapObjFrame(0xE, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "Null", 0x2, "high")
    Jump("loc_10EB")

    label("loc_107A")

    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    SetBarrier(0x2, 0xA, 0x1)
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "Null", 0x2, "low")

    label("loc_10EB")

    SetMapObjFrame(0x11, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x3, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x3, "light01", 0x0, 0x1)
    SetMapObjFrame(0x4, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x4, "light01", 0x0, 0x1)
    SetMapObjFrame(0x5, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x5, "light01", 0x0, 0x1)
    SetMapObjFrame(0x6, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x6, "light01", 0x0, 0x1)
    SetMapObjFrame(0x7, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x7, "light01", 0x0, 0x1)
    SetMapObjFrame(0x8, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x8, "light01", 0x0, 0x1)
    SetMapObjFrame(0x9, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x9, "light01", 0x0, 0x1)
    SetMapObjFrame(0xA, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xA, "light01", 0x0, 0x1)
    SetMapObjFrame(0xB, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xB, "light01", 0x0, 0x1)
    SetMapObjFrame(0xC, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xC, "light01", 0x0, 0x1)
    SetMapObjFrame(0xD, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xD, "light01", 0x0, 0x1)
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
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1408")
    OP_70(0x14, 0x0)
    Jump("loc_140C")

    label("loc_1408")

    OP_70(0x14, 0x1E)

    label("loc_140C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141F")
    OP_70(0x15, 0x0)
    Jump("loc_1423")

    label("loc_141F")

    OP_70(0x15, 0x1E)

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1436")
    OP_70(0x16, 0x0)
    Jump("loc_143A")

    label("loc_1436")

    OP_70(0x16, 0x1E)

    label("loc_143A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144D")
    OP_70(0x17, 0x0)
    Jump("loc_1451")

    label("loc_144D")

    OP_70(0x17, 0x1E)

    label("loc_1451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1473")
    ClearMapObjFlags(0x1F, 0x4)
    SetMapObjFrame(0xFF, "koge00", 0x1, 0x1)
    Jump("loc_1487")

    label("loc_1473")

    SetMapObjFlags(0x1F, 0x4)
    SetMapObjFrame(0xFF, "koge00", 0x0, 0x1)

    label("loc_1487")

    ClearMapObjFlags(0x18, 0x10)
    Return()

    # Function_3_DEF end

    def Function_4_148E(): pass

    label("Function_4_148E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165F")
    Sound(14, 0, 100, 0)
    OP_74(0x14, 0x1E)
    OP_71(0x14, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1591")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_14EB():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_14EB)

    def lambda_1505():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1505)
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
    Battle("BattleInfo_B74", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1572"),
        (2, "loc_1581"),
        (1, "loc_158E"),
        (SWITCH_DEFAULT, "loc_1591"),
    )


    label("loc_1572")

    SetScenarioFlags(0x216, 7)
    OP_70(0x14, 0x1E)
    Sleep(500)
    Jump("loc_1591")

    label("loc_1581")

    OP_70(0x14, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_158E")

    OP_B9(0x0)
    Return()

    label("loc_1591")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x50, 1)"), scpexpr(EXPR_END)), "loc_15EA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EF, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_165A")

    label("loc_15EA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x50),
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
    OP_71(0x14, 0x1E, 0x0, 0x0, 0x0)

    label("loc_165A")

    Jump("loc_169D")

    label("loc_165F")

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

    label("loc_169D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_148E end

    def Function_5_16A9(): pass

    label("Function_5_16A9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E2")
    Sound(14, 0, 100, 0)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x15, 0x1E)
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
    SetScenarioFlags(0x1EF, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1800")

    label("loc_17E2")


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

    label("loc_1800")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16A9 end

    def Function_6_1812(): pass

    label("Function_6_1812")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190E")
    Sound(14, 0, 100, 0)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x334, 1)"), scpexpr(EXPR_END)), "loc_1897")
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
    SetScenarioFlags(0x1EF, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1909")

    label("loc_1897")

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
    OP_71(0x16, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1909")

    Jump("loc_1957")

    label("loc_190E")

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

    label("loc_1957")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1812 end

    def Function_7_1963(): pass

    label("Function_7_1963")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B34")
    Sound(14, 0, 100, 0)
    OP_74(0x17, 0x1E)
    OP_71(0x17, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A66")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_19C0():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19C0)

    def lambda_19DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_19DA)
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
    Battle("BattleInfo_BB8", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1A47"),
        (2, "loc_1A56"),
        (1, "loc_1A63"),
        (SWITCH_DEFAULT, "loc_1A66"),
    )


    label("loc_1A47")

    SetScenarioFlags(0x217, 0)
    OP_70(0x17, 0x1E)
    Sleep(500)
    Jump("loc_1A66")

    label("loc_1A56")

    OP_70(0x17, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1A63")

    OP_B9(0x0)
    Return()

    label("loc_1A66")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xAF, 1)"), scpexpr(EXPR_END)), "loc_1ABF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EF, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1B2F")

    label("loc_1ABF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
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
    OP_71(0x17, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1B2F")

    Jump("loc_1B72")

    label("loc_1B34")

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

    label("loc_1B72")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1963 end

    def Function_8_1B7E(): pass

    label("Function_8_1B7E")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Step Inside\x01",      # 0
            "Step away\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BD0"),
        (1, "loc_1BED"),
        (SWITCH_DEFAULT, "loc_1BF2"),
    )


    label("loc_1BD0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x13, 0x10)
    OP_65(0x0, 0x1)
    Call(0, 21)
    Jump("loc_1BF2")

    label("loc_1BED")

    Jump("loc_1BF2")

    label("loc_1BF2")

    SetChrPos(0x0, 500000, 0, 205800, 180)
    EventEnd(0x5)
    Return()

    # Function_8_1B7E end

    def Function_9_1C06(): pass

    label("Function_9_1C06")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEB")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x12, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x12, 0x0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x12)
    OP_71(0x12, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x12, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1CEB")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_9_1C06 end

    def Function_10_1CFA(): pass

    label("Function_10_1CFA")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1CFA end

    def Function_11_1D16(): pass

    label("Function_11_1D16")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1D16 end

    def Function_12_1D32(): pass

    label("Function_12_1D32")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_1D32 end

    def Function_13_1D4E(): pass

    label("Function_13_1D4E")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a control unit for\x01",
            "adjusting the water\x01",
            "level. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_224C")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E43")
    SetChrPos(0x0, 107620, -6000, 200, 0)
    SetChrPos(0x1, 108620, -6000, -600, 0)
    SetChrPos(0x2, 106620, -6000, -600, 0)
    SetChrPos(0x3, 107620, -6000, -1900, 0)
    OP_68(107660, -5000, 850, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    Jump("loc_1F4A")

    label("loc_1E43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC9")
    SetChrPos(0x0, 85000, -6000, 101000, 0)
    SetChrPos(0x1, 83800, -6000, 101000, 0)
    SetChrPos(0x2, 83800, -6000, 99800, 0)
    SetChrPos(0x3, 85000, -6000, 99800, 0)
    OP_68(84580, -5000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27000, 0)
    Jump("loc_1F4A")

    label("loc_1EC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F4A")
    SetChrPos(0x0, 201500, -6000, 184000, 90)
    SetChrPos(0x1, 200000, -6000, 185000, 90)
    SetChrPos(0x2, 200000, -6000, 183000, 90)
    SetChrPos(0x3, 198500, -6000, 184000, 90)
    OP_68(201500, -5000, 184020, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33500, 0)

    label("loc_1F4A")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 0)), scpexpr(EXPR_END)), "loc_20D5")
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FEE")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_206D")

    label("loc_1FEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2030")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_206D")

    label("loc_2030")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206D")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_206D")

    OP_0D()
    Sound(157, 2, 100, 0)
    SetMapObjFrame(0xFF, "null", 0x2, "down")
    Sleep(4000)
    OP_24(0x9D)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    SetBarrier(0x2, 0xA, 0x1)
    ClearScenarioFlags(0x150, 0)
    Jump("loc_224C")

    label("loc_20D5")

    SetMapObjFrame(0xE, "m01gim01", 0x2, "on")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216C")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_21EB")

    label("loc_216C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21AE")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_21EB")

    label("loc_21AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21EB")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_21EB")

    OP_0D()
    Sound(157, 2, 100, 0)
    SetMapObjFrame(0xFF, "null", 0x2, "up")
    Sleep(4000)
    OP_24(0x9D)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    SetBarrier(0x3, 0xA, 0x1)
    SetScenarioFlags(0x150, 0)

    label("loc_224C")

    Return()

    # Function_13_1D4E end

    def Function_14_224D(): pass

    label("Function_14_224D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(144)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elevator control\x01",
            "panel. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23CC")
    Fade(500)
    SetChrPos(0x0, 600, 0, 600, 90)
    SetChrPos(0x1, 600, 0, -600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_232C")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_234B")

    label("loc_232C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_234B")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_234B")

    OP_68(600, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600, 6000, 0, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0100", 0, 0, 0)
    IdleLoop()

    label("loc_23CC")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_224D end

    def Function_15_23D4(): pass

    label("Function_15_23D4")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, 600, 90)
    OP_90(0x1, 600, 30000, -600, 90)
    OP_90(0x2, -600, 30000, -600, 90)
    OP_90(0x3, -600, 30000, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A7")
    OP_90(0x4, -1800, 0, -600, 90)
    OP_90(0x5, -1800, 0, 600, 90)
    Jump("loc_24C6")

    label("loc_24A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C6")
    OP_90(0x4, -1800, 0, 0, 90)

    label("loc_24C6")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 0, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x11)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_23D4 end

    def Function_16_251B(): pass

    label("Function_16_251B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51207.itc", 0x1E)
    SoundLoad(938)
    SoundLoad(3706)
    SoundLoad(3707)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04800.itp")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 250, 302000, 0)
    BeginChrThread(0x8, 3, 0, 17)
    SetMapObjFlags(0x20, 0x1000)
    OP_70(0x20, 0x0)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    Sound(836, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3706V#30W─Uhuhu. I see.\x02\x03",
            "#3707VIt's quite the easy to\x01",
            "use terminal.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE7B)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    PlayBGM("ed7580", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x244), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(499510, 1050, 296140, 0)
    MoveCamera(26, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    Sound(938, 2, 60, 0)
    OP_68(499320, 1050, 303000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(499320, 1050, 303000, 0)
    MoveCamera(26, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16640, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Jona Sacred, the foundation's most\x01",
            "gifted system engineer, huh.\x02\x03",
            "Though it's an old-style network,\x01",
            "to think he created such an\x01",
            "environment.\x02\x03",
            "It wasn't necessarily a fluke that\x01",
            "he he was able to catch Renne.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    StopSound(938, 2000, 60)
    SetCameraDistance(16140, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x3AA)
    SetScenarioFlags(0x22, 0)
    NewScene("e4810", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_251B end

    def Function_17_282E(): pass

    label("Function_17_282E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_284C")
    SetChrSubChip(0x8, 0x0)
    Sleep(200)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)
    Jump("Function_17_282E")

    label("loc_284C")

    Return()

    # Function_17_282E end

    def Function_18_284D(): pass

    label("Function_18_284D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51207.itc", 0x1E)
    SoundLoad(938)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 250, 302000, 0)
    SetMapObjFlags(0x20, 0x1000)
    OP_70(0x20, 0xB)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    OP_68(498250, 1050, 304800, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16250, 0)
    SetCameraDistance(17250, 2000)
    FadeToBright(2000, 0)
    Sleep(1500)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#6P#04805FWhoops... Did I make a\x01",
            "mistake?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 17)
    Sound(938, 2, 60, 0)
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#6P#04802FUhuhu... You're good,\x01",
            "freckles.\x02\x03",
            "But, I guess you won't\x01",
            "discover this trap until\x01",
            "around tomorrow?\x02\x03",
            "#04809FSince I'm here, I think\x01",
            "I'll have a little more\x01",
            "fun㈱\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17750, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    StopSound(938, 2000, 60)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    ReplaceBGM(-1, -1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3AA)
    SetScenarioFlags(0x22, 4)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_284D end

    def Function_19_2AA1(): pass

    label("Function_19_2AA1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51207.itc", 0x1E)
    SoundLoad(938)
    SoundLoad(3708)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis339.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis340.itp")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 250, 302000, 0)
    SetMapObjFlags(0x20, 0x1000)
    OP_70(0x20, 0x15)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    OP_68(498200, 1900, 303600, 0)
    MoveCamera(29, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    FadeToBright(0, 0)
    Sleep(500)
    SetMessageWindowPos(15, 130, -1, -1)
    OP_C9(0x0, 0x80000000)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3708V#40WAnd thusly, the tower of fate appears.\x01",
            "Whilst a multitude of destinies\x01",
            "intertwine, a spiral is formed...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE7C)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x8, 3, 0, 17)
    Sound(938, 2, 60, 0)
    OP_68(498200, 1400, 302600, 3000)
    MoveCamera(29, 14, 0, 3000)
    SetCameraDistance(16000, 3000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#12P#04804FHaha. Bleublanc would\x01",
            "really love that scene.\x02\x03",
            "#04800FWell, for an event like\x01",
            "this, maybe he came to\x01",
            "see it on his own.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    StopSound(938, 500, 60)
    Sound(839, 0, 100, 0)
    Sleep(400)
    Sound(839, 0, 100, 0)
    Sleep(400)
    EndChrThread(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#12P#04805FOh, it's here, it's\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#04802FUhuhu... All that's left\x01",
            "is to give it to "him",\x01",
            "huh.\x02\x03",
            "#04809FWell, I think I'll set up\x01",
            "something fun for him as\x01",
            "well, while I'm at it㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(0, 0, -1)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x3AA)
    SetScenarioFlags(0x22, 2)
    NewScene("c0180", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_2AA1 end

    def Function_20_2E6F(): pass

    label("Function_20_2E6F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(489500, 1150, 200000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    OP_90(0x101, 491000, 0, 200600, 90)
    OP_90(0x102, 491000, 0, 199400, 90)
    OP_90(0x104, 490000, 0, 201100, 90)
    OP_90(0x109, 490000, 0, 198900, 90)
    OP_90(0x105, 489000, 0, 199400, 90)
    OP_90(0x10A, 489000, 0, 200600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(500000, 1300, 208000, 0)
    MoveCamera(23, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(35, 21, 0, 6000)
    OP_6E(500, 0)
    SetCameraDistance(20000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(492600, 1100, 200090, 3000)
    MoveCamera(33, 16, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(19000, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011F#6P(T-this song is...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_2FD8():
        OP_97(0x101, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FD8)
    Sleep(100)

    def lambda_2FF5():
        OP_97(0x102, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2FF5)
    Sleep(100)

    def lambda_3012():
        OP_97(0x104, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3012)
    Sleep(100)

    def lambda_302F():
        OP_97(0x109, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_302F)
    Sleep(100)

    def lambda_304C():
        OP_97(0x10A, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_304C)
    Sleep(100)

    def lambda_3069():
        OP_97(0x105, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3069)
    Sleep(2000)
    Fade(500)
    OP_68(500000, 1100, 204000, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    WaitChrThread(0x101, 0)

    def lambda_30BD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30BD)
    WaitChrThread(0x102, 0)

    def lambda_30CE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_30CE)
    WaitChrThread(0x104, 0)

    def lambda_30DF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_30DF)
    WaitChrThread(0x109, 0)

    def lambda_30F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_30F0)
    WaitChrThread(0x10A, 0)

    def lambda_3101():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3101)
    WaitChrThread(0x105, 0)

    def lambda_3112():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3112)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#00108F(Is it from the orbal\x01",
            "stereo in Jona's room?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F(What...? It might be\x01",
            "broken.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)

    ChrTalk(
        0x10A,
        (
            "#6P#00603F(It might be a trap...\x01",
            "Let's enter cautiously,\x01",
            "just in case.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x10A,
        (
            "#6P#00601F(Bannings, Orlando. We\x01",
            "three are going in\x01",
            "first.)\x02\x03",
            "(The rest of you, follow\x01",
            "in behind us.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3264():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3264)
    Sleep(50)

    def lambda_3274():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3274)
    Sleep(50)

    def lambda_3284():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3284)
    Sleep(50)

    def lambda_3294():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3294)
    Sleep(50)

    def lambda_32A4():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_32A4)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00013F#11P(Roger.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#11P(Aye sir.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101F(Acknowledged!)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 499600, 0, 202400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x141, 4)
    ClearMapObjFlags(0x13, 0x10)
    OP_66(0x0, 0x1)
    EventEnd(0x5)
    Return()

    # Function_20_2E6F end

    def Function_21_334F(): pass

    label("Function_21_334F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00200.itc", 0x1E)
    LoadChrToIndex("chr/ch00500.itc", 0x1F)
    LoadChrToIndex("chr/ch00959.itc", 0x20)
    LoadChrToIndex("chr/ch00002.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00051.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00950.itc", 0x26)
    LoadChrToIndex("chr/ch00951.itc", 0x27)
    LoadChrToIndex("apl/ch51216.itc", 0x28)
    LoadChrToIndex("apl/ch51217.itc", 0x29)
    LoadChrToIndex("apl/ch51219.itc", 0x2A)
    LoadChrToIndex("apl/ch51220.itc", 0x2B)
    LoadChrToIndex("apl/ch51221.itc", 0x2C)
    LoadChrToIndex("apl/ch51223.itc", 0x2D)
    LoadChrToIndex("apl/ch50221.itc", 0x2E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis340.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00700.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis341.itp")
    LoadEffect(0x0, "event\\ev202_00.eff")
    LoadEffect(0x1, "event\\ev15020.eff")
    LoadEffect(0x2, "event\\ev12006.eff")
    LoadEffect(0x4, "event/ev15102.eff")
    SoundLoad(868)
    SoundLoad(825)
    SoundLoad(3709)
    SoundLoad(3710)
    SoundLoad(3711)
    SoundLoad(3712)
    SoundLoad(3713)
    SoundLoad(3714)
    SoundLoad(3715)
    SoundLoad(3453)
    SoundLoad(2669)
    SoundLoad(2670)
    SoundLoad(2671)
    SoundLoad(2672)
    SoundLoad(2673)
    OP_90(0x101, 499300, 0, 205000, 0)
    OP_90(0x104, 500600, 0, 204700, 0)
    OP_90(0x10A, 500000, 150, 206400, 0)
    OP_90(0x102, 500810, 0, 200440, 0)
    OP_90(0x109, 499230, 0, 200150, 0)
    OP_90(0x105, 497790, 0, 200360, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_68(500000, 1000, 207200, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_35BD():
        OP_95(0xFE, 500000, 150, 207400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_35BD)
    WaitChrThread(0x10A, 1)
    SetChrChipByIndex(0x10A, 0x26)
    SetChrSubChip(0x10A, 0x0)
    Sleep(300)
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10A)
    OP_93(0x10A, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0x10A, 0x0, 0x3E8)
    Sound(121, 0, 100, 0)
    Sound(103, 0, 100, 0)
    OP_71(0x13, 0x0, 0xA, 0x0, 0x0)

    def lambda_3627():
        OP_95(0xFE, 500000, 150, 210400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3627)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 22)
    Sleep(200)

    def lambda_364D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_364D)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 22)
    WaitChrThread(0x10A, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x10A, 0xFF)
    SetChrPos(0x101, 499700, 150, 287400, 0)
    SetChrPos(0x102, 499700, 150, 287400, 0)
    SetChrPos(0x104, 499700, 150, 287400, 0)
    SetChrPos(0x109, 499700, 150, 287400, 0)
    SetChrPos(0x105, 499700, 150, 287400, 0)
    SetChrPos(0x10A, 499700, 150, 287400, 0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x20, 0x1000)
    OP_70(0x20, 0x1F)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    OP_71(0x1E, 0x0, 0x14, 0x0, 0x20)
    VolumeBGM(0x64, 0x3E8)
    OP_68(499700, 1000, 295500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_68(499200, 1000, 297000, 3000)
    MoveCamera(55, 20, 0, 3000)
    SetCameraDistance(24000, 3000)
    BeginChrThread(0x10A, 3, 0, 23)
    Sleep(400)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 25)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00008FNo one's here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PI don't sense anyone's\x01",
            "hiding either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00606F#11P...So he ran away.\x02\x03",
            "#00600FBut we didn't pass\x01",
            "anyone on our way\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(500700, 1300, 293900, 0)
    MoveCamera(47, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 28)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x102,
        "#12P#00108FD-Did they get away?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)

    def lambda_3910():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3910)
    Sleep(50)

    def lambda_3920():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3920)
    Sleep(50)

    def lambda_3930():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3930)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x10A, 0)

    ChrTalk(
        0x101,
        "#00006F#5PYeah, it appears so.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001F#6PThe music... Looks like\x01",
            "it's coming from this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39B8():
        OP_92(0x101, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39B8)
    Sleep(50)

    def lambda_39CE():
        OP_92(0x102, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_39CE)
    Sleep(50)

    def lambda_39E4():
        OP_92(0x105, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_39E4)
    Sleep(50)

    def lambda_39FA():
        OP_92(0x10A, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_39FA)
    Sleep(50)

    def lambda_3A10():
        OP_92(0x109, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3A10)
    Sleep(50)

    def lambda_3A26():
        OP_92(0x104, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3A26)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x10A,
        (
            "#6P#00601FIt's really annoying...\x01",
            "Can you make it stop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PYeah... This is the\x01",
            "switch.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3AB9():
        OP_96(0xFE, 0x7AF94, 0x0, 0x4824C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AB9)
    WaitChrThread(0x104, 1)
    Sleep(150)
    Sound(853, 0, 100, 0)
    SetMapObjFlags(0x1E, 0x4)
    StopBGM(0x1F4)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#12P#10108FSomehow it's eerie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FR-Right... It's\x01",
            "unnatural that music was\x01",
            "playing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10308FHmm, I feel malice for\x01",
            "some reason, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#12P#10305FAt any rate, what's that\x01",
            "on the monitor in the\x01",
            "back?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(498200, 1300, 303700, 2500)
    MoveCamera(33, 20, 0, 2500)

    def lambda_3C60():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C60)
    Sleep(50)

    def lambda_3C70():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3C70)
    Sleep(50)

    def lambda_3C80():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3C80)
    Sleep(50)

    def lambda_3C90():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C90)
    Sleep(50)

    def lambda_3CA0():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3CA0)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#N#12PBlueprints...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(498200, 1300, 302600, 3000)
    SetCameraDistance(21000, 3000)
    BeginChrThread(0x101, 3, 0, 29)
    BeginChrThread(0x10A, 3, 0, 30)
    BeginChrThread(0x104, 3, 0, 31)
    BeginChrThread(0x102, 3, 0, 32)
    BeginChrThread(0x105, 3, 0, 33)
    BeginChrThread(0x109, 3, 0, 34)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00011FT-These are...!\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x102,
        (
            "#00105FT-These are... No way,\x01",
            "they're Orchis Tower's!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10101FIt looks like a map of\x01",
            "the tower's internal\x01",
            "structure.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x10A,
        (
            "#00610FTch, why is something\x01",
            "like that in a place\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_7D(0xFF, 0x64, 0x64, 0x0, 0x1F4)
    BeginChrThread(0xE, 1, 0, 44)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    PlayBGM("ed7561", 0)

    ChrTalk(
        0x101,
        "#11P#00011F!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10310FDamn!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(504300, 900, 399700, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 498800, 200, 397200, 270)
    SetChrPos(0x102, 500400, 0, 397200, 270)
    SetChrPos(0x104, 499400, 0, 400300, 225)
    SetChrPos(0x109, 501100, 0, 399700, 270)
    SetChrPos(0x105, 501100, 0, 398700, 270)
    SetChrPos(0x10A, 499600, 0, 399200, 270)
    ClearMapObjFlags(0x19, 0x10)
    OP_70(0x19, 0xA)
    Sleep(500)
    Sound(104, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_71(0x19, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x19)
    OP_82(0x32, 0x0, 0xBB8, 0x12C)

    def lambda_4027():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4027)
    Sleep(30)

    def lambda_4037():
        OP_93(0x10A, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_4037)
    Sleep(30)

    def lambda_4047():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4047)
    Sleep(30)

    def lambda_4057():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4057)
    Sleep(30)

    def lambda_4067():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4067)
    Sleep(30)

    def lambda_4077():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4077)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        "#00101F#6P#N!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        "#00610F#6PTch, a trap!?\x02",
    )

    CloseMessageWindow()
    OP_68(505950, 900, 400300, 1500)
    MoveCamera(50, 17, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(21500, 1500)

    def lambda_40FE():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_40FE)
    Sleep(300)

    def lambda_411B():
        OP_95(0xFE, 502700, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_411B)
    WaitChrThread(0x105, 1)

    def lambda_4139():
        OP_95(0xFE, 508400, 0, 400700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4139)
    WaitChrThread(0x109, 1)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x2B)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x87, 0x1F4)
    OP_6F(0x79)
    Sleep(800)

    ChrTalk(
        0x109,
        (
            "#10110F#6PI-It's no use! It won't\x01",
            "open!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308F#5PLooks like it's locked\x01",
            "with an orbal mechanism.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(4113, 255, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(500300, 1600, 297000, 0)
    MoveCamera(37, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 497200, 200, 301200, 180)
    SetChrPos(0x102, 497100, 0, 299900, 180)
    SetChrPos(0x104, 500200, 0, 300600, 180)
    SetChrPos(0x109, 499700, 0, 290400, 180)
    SetChrPos(0x105, 501100, 0, 291200, 225)
    SetChrPos(0x10A, 498600, 200, 300600, 180)
    OP_0D()
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)

    def lambda_4331():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4331)

    def lambda_433E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_433E)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#00010FWhat was that just now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00307FHey, who are...!?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3709V#30WUhuhu... How do you do,\x01",
            "ladies and gentlemen of the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(160, 100, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3710V#30WAs expected, it seems\x01",
            "you've come to visit.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(30, 50, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3711V#30WI've left for you a little\x01",
            "something to remember me by.\x01",
            "I do hope you enjoy it.㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE7F)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        "#5P#00011FWhat...\x02",
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x10A,
        (
            "#00607F#11PTch, it's from the\x01",
            "terminal?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(498200, 1300, 302300, 2000)
    MoveCamera(33, 17, 0, 2000)
    SetCameraDistance(20500, 2000)

    def lambda_4560():
        OP_95(0xFE, 499500, 0, 298400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4560)

    def lambda_457A():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_457A)
    Sleep(30)

    def lambda_458A():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_458A)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    def lambda_45A2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_45A2)
    Sleep(30)

    def lambda_45B2():
        OP_95(0xFE, 499200, 0, 299300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_45B2)
    WaitChrThread(0x105, 1)

    def lambda_45D0():
        OP_95(0xFE, 498100, 0, 299300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_45D0)
    WaitChrThread(0x105, 1)

    def lambda_45EE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_45EE)
    WaitChrThread(0x109, 1)

    def lambda_45FF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_45FF)
    OP_6F(0x79)
    EndChrThread(0xE, 0x1)
    Fade(250)
    OP_70(0x20, 0x29)
    Sleep(500)
    Sound(72, 0, 100, 0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x109,
        "#10105FT-This is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00101FIt's the puzzle battle\x01",
            "game Chief Roberts gave\x01",
            "us!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 60, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "If you win 2 out of 3,\x01",
            "I'll let you guys go.\x02\x03",
            "However, in case you\x01",
            "lose, I guess you'll be\x01",
            "burnt to a crisp?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00010FWhat!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(499300, 1300, 297300, 3000)
    MoveCamera(53, 20, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(20000, 3000)
    BeginChrThread(0xE, 1, 0, 45)
    Sound(614, 0, 100, 0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 496500, 500, 292600, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 502300, 2000, 292100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 493200, 2000, 299500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 504000, 1500, 298100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 502000, 2500, 301100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_48C1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48C1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_48E9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_48E9)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_490E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_490E)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4936():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4936)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_495B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_495B)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4983():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_4983)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#6P#10111FWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00307FNo way! There wasn't any\x01",
            "sign of a trap!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(498200, 1300, 302300, 0)
    MoveCamera(33, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_0D()
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Uhuhu. Then, shall we\x01",
            "begin?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "There isn't much time...\x01",
            "You'll die if you don't\x01",
            "hurry, you know?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0x10A, 0x0, 0x1F4)

    ChrTalk(
        0x10A,
        "#00610FYou bastard!\x02",
    )

    CloseMessageWindow()

    def lambda_4AC6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4AC6)

    def lambda_4AD3():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4AD3)
    Sleep(30)

    def lambda_4AE3():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4AE3)
    Sleep(30)

    def lambda_4AF3():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4AF3)
    Sleep(30)

    def lambda_4B03():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4B03)
    Sleep(30)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x105,
        (
            "#12P#10307FLloyd! We have no\x01",
            "choice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00010FShit... Got it!\x02",
    )

    CloseMessageWindow()
    StopSound(868, 1000, 40)
    StopSound(825, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0x20, 0x33)
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BE0")
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BD6")
    OP_2C(0xA3, 0x1)
    Jump("loc_4BDB")

    label("loc_4BD6")

    OP_2C(0xA3, 0x2)

    label("loc_4BDB")

    Jump("loc_4BE3")

    label("loc_4BE0")

    ClearScenarioFlags(0x0, 1)

    label("loc_4BE3")

    FadeToBright(0, -1)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 498200, 250, 302000, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 496500, 500, 292600, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 502300, 2000, 292100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 493200, 2000, 299500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 504000, 1500, 298100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 502000, 2500, 301100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 498500, 2000, 401200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 501700, 1500, 404100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 507700, 1000, 402700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 507200, 500, 396600, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    Sound(868, 2, 40, 0)
    Sound(825, 2, 40, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(20500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4EF9")

    ChrTalk(
        0x101,
        "#11P#00000FAll right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FYou're amazing, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FYou're good!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Hmm. Maybe I went too\x01",
            "easy on you?\x02\x03",
            "Then for our next match,\x01",
            "I'll get serious...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4FB5")

    label("loc_4EF9")


    ChrTalk(
        0x101,
        "#11P#00010F...Damn...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#12PAah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10306FHmm. Too bad, but...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Ahaha! All that's left\x01",
            "is for you to die.\x02\x03",
            "Now then, for the\x01",
            "finishing─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4FB5")

    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("Young Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2669V#30W─Quit horsing around.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA6D)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7524", 0)

    ChrTalk(
        0x102,
        "#12P#00105FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FThis voice is...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("Young Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2670V#30WI will be your opponent.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2671V#30W─Prepare yourself.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA6F)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    StopSound(868, 1000, 40)
    StopSound(825, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToDark(0, -1, 0)
    Sleep(500)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_08a.pmf", 0x20C, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    Sound(868, 2, 60, 0)
    Sound(825, 2, 60, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5384")
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 496500, 500, 292600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502300, 2000, 292100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 493200, 2000, 299500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 504000, 1500, 298100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502000, 2500, 301100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 498500, 2000, 401200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 501700, 1500, 404100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507700, 1000, 402700, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507200, 500, 396600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)

    label("loc_5384")

    FadeToBright(0, -1)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D3")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3712V#30WWhaaat!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE80)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("Young Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2672V#30WAnd now for the next\x01",
            "one.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA70)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    StopSound(868, 1000, 60)
    StopSound(825, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToDark(0, -1, 0)
    Sleep(500)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_08b.pmf", 0x20C, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    Sound(868, 2, 60, 0)
    Sound(825, 2, 60, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 496500, 500, 292600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502300, 2000, 292100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 493200, 2000, 299500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 504000, 1500, 298100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502000, 2500, 301100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 498500, 2000, 401200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 501700, 1500, 404100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507700, 1000, 402700, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507200, 500, 396600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    FadeToBright(0, -1)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    label("loc_56D3")

    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        "#11P#00002FS-She did it!\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x2D, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00310F#5PTch... It's this bad\x01",
            "already!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3713V#30WUhuhu, nicely done.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3714V#30WIt looks like she's one\x01",
            "of you, so I'll let you\x01",
            "go as promised.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3715V#30W─Well then, later㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE83)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Fade(250)
    OP_68(504300, 900, 399700, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 498300, 250, 398300, 270)
    SetChrPos(0x102, 500400, 0, 397200, 270)
    SetChrPos(0x104, 499400, 0, 400300, 225)
    SetChrPos(0x109, 501100, 0, 399700, 270)
    SetChrPos(0x105, 501100, 0, 398700, 270)
    SetChrPos(0x10A, 499600, 0, 399200, 270)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_71(0x19, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x19)
    OP_82(0x32, 0x0, 0xBB8, 0x12C)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_58FE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_58FE)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5923():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5923)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_594B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_594B)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5970():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5970)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5998():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_5998)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10107F#5PIt opened!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00610F#5PQuick, it's gonna blow!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(100)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 498800, 200, 397200, 270)
    OP_0D()
    OP_93(0x101, 0x59, 0x1F4)

    ChrTalk(
        0x101,
        "#6P#00007F#NRight!\x02",
    )

    CloseMessageWindow()
    OP_68(509000, 900, 399700, 4000)
    MoveCamera(57, 17, 0, 4000)
    SetCameraDistance(20500, 4000)
    BeginChrThread(0x109, 3, 0, 35)
    BeginChrThread(0x105, 3, 0, 36)
    BeginChrThread(0x104, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x10A, 3, 0, 39)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x105, 0xFF)
    EndChrThread(0x109, 0xFF)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, 500000, 150, 210400, 180)
    SetChrPos(0x102, 500000, 150, 207400, 180)
    SetChrPos(0x104, 500000, 0, 205000, 180)
    SetChrPos(0x109, 502000, 0, 200700, 315)
    SetChrPos(0x105, 502000, 0, 199600, 315)
    SetChrPos(0x10A, 498700, 0, 199200, 0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 489200, 0, 198100, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x1A, 0x1000)
    SetMapObjFlags(0x1B, 0x1000)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x13, 0x4)
    OP_68(500000, 1000, 209400, 0)
    MoveCamera(27, 21, 5, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(500000, 1300, 204000, 2000)
    MoveCamera(45, 17, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(19500, 2000)
    BeginChrThread(0x104, 3, 0, 43)
    BeginChrThread(0x102, 3, 0, 42)
    BeginChrThread(0x101, 3, 0, 41)
    OP_25(0x364, 0x1E)
    OP_25(0x339, 0x1E)
    FadeToBright(500, 0)
    OP_0D()
    OP_82(0xC8, 0x0, 0xBB8, 0x258)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x10A,
        "#12A#00607F#3453V#12P#N#4SGet down!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x101, 3)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x104, 0x2A)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x109, 0x2B)
    SetChrSubChip(0x105, 0x1)
    SetChrChipByIndex(0x105, 0x2C)
    SetChrSubChip(0x10A, 0x1)
    SetChrChipByIndex(0x10A, 0x2D)
    Sound(2030, 255, 100, 0)
    Sound(2128, 255, 100, 1)
    Sound(2317, 255, 100, 2)
    Sound(2463, 255, 100, 3)
    Sound(2402, 255, 100, 4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 500000, 400, 208000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(2500)
    SetMapObjFrame(0xFF, "koge00", 0x1, 0x1)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x7D0)
    Sound(200, 0, 100, 0)
    Sound(833, 0, 100, 0)
    StopSound(868, 2000, 30)
    StopSound(825, 2000, 30)
    Sleep(2500)

    def lambda_5D4D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D4D)
    WaitChrThread(0x101, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#00006F#40W*pant, pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#40W#11PUgh, that was too close!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#40W#11PI-I thought I was gonna\x01",
            "die...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00610F#40W#11PTch... Who's there!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x9, 0x80)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x9,
        "Young Girl's Voice",
        (
            "#2673V#30W─Thank goodness. It\x01",
            "seems you're all ok.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA71)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    Fade(500)
    OP_68(501600, 1100, 506500, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(501900, 1100, 499900, 3000)
    MoveCamera(35, 23, 0, 3000)
    SetCameraDistance(17500, 3000)
    SetMapObjFrame(0x1C, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1C, "light01", 0x0, 0x1)
    ClearMapObjFlags(0x1C, 0x10)
    OP_70(0x1C, 0xA)
    SetChrPos(0x101, 502600, 0, 499800, 270)
    SetChrPos(0x102, 500400, 0, 500300, 90)
    SetChrPos(0x104, 500400, 0, 499000, 90)
    SetChrPos(0x109, 498900, 0, 498300, 45)
    SetChrPos(0x105, 499900, 0, 497600, 45)
    SetChrPos(0x10A, 498900, 0, 500000, 90)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x1)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x9, 501600, 0, 507500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 500000, 150, 512000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 500000, 0, 504000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_608B():
        OP_96(0xFE, 0x7AA1C, 0x0, 0x7A508, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_608B)
    OP_0D()
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x104, 500)

    ChrTalk(
        0x101,
        "#12P#00002FTio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FI-I knew it was you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FHey now! What the heck's\x01",
            "goin' on?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2276, 255, 80, 0)
    Sleep(800)

    def lambda_6125():
        OP_95(0xFE, 502500, 0, 500400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6125)
    WaitChrThread(0x9, 1)

    def lambda_6143():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6143)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    def lambda_6173():
        OP_96(0xFE, 0x7AA1C, 0x0, 0x7A508, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6173)
    TurnDirection(0x101, 0x9, 500)
    WaitChrThread(0x9, 1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "─Actually, I boarded an\x01",
            "international flight to Crossbell\x01",
            "this afternoon.\x02\x03",
            "Things seemed tough here, so I\x01",
            "hastened my return somehow.\x02",
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
        0x101,
        "#12P#00000FI see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    TurnDirection(0x102, 0x9, 0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    TurnDirection(0x104, 0x9, 0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    TurnDirection(0x109, 0x9, 0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    TurnDirection(0x105, 0x9, 0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    TurnDirection(0x10A, 0x9, 0)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha... You can't beat\x01",
            "that timing, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#12P#N#10302FSo, you heard from chief\x01",
            "and came here?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x9, 0x104, 500)

    ChrTalk(
        0x9,
        (
            "#00204FYes. I contacted him via\x01",
            "ENIGMA, and he told me\x01",
            "you were headed here.\x02\x03",
            "#00202FSo I came here directly\x01",
            "from the airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F*giggle*... You really\x01",
            "saved us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#N#10109FThank you, Tio!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#00204F#5PWell, I'm just glad I\x01",
            "made it in time.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#00201F#5P...Even so, he was a\x01",
            "troublesome opponent.\x02\x03",
            "Somehow I was able to\x01",
            "repel him by cutting in,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FCutting in...? Ah, that.\x02",
    )

    CloseMessageWindow()
    OP_68(502700, 500, 508900, 2000)
    OP_93(0x9, 0x0, 0x190)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#12P#N#00202FYes. I knew you guys were\x01",
            "locked inside, so I came\x01",
            "in through a backup line.\x02\x03",
            "#00206FIt seems he was quite the\x01",
            "skilled hacker.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00006F#12P#NYeah, seems so.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(501000, 1100, 500100, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    ChrTalk(
        0x10A,
        (
            "#6P#00601FHmph, it seems he\x01",
            "withdrew a long time\x01",
            "ago, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x10A,
        (
            "#6P#00605FBy the way, Plato.\x02\x03",
            "Did you come all the way\x01",
            "here by yourself?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10A, 500)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#11P#00205FAh, no.\x02\x03",
            "#00203FThere was someone\x01",
            "around, so I came here\x01",
            "together with him.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        "#12P#00005FHuh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2629, 255, 100, 0)
    Sleep(800)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(
        0xA,
        "Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#N─I find all of you in\x01",
            "the most unlikely of\x01",
            "places.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    OP_68(500140, 1100, 501660, 3000)
    MoveCamera(47, 15, 0, 3000)
    OP_6E(550, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_6896():
        OP_96(0xFE, 0x7A120, 0x0, 0x7B0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6896)

    def lambda_68B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_68B0)

    def lambda_68C1():

        label("loc_68C1")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_68C1")

    QueueWorkItem2(0x101, 2, lambda_68C1)

    def lambda_68D3():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_68D3)

    def lambda_68E0():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_68E0)

    def lambda_68ED():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_68ED)

    def lambda_68FA():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_68FA)

    def lambda_6907():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_6907)

    def lambda_6914():

        label("loc_6914")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_6914")

    QueueWorkItem2(0x9, 2, lambda_6914)
    WaitChrThread(0xA, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00007FYou're...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10107FF-From back then!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FYin!\x02",
    )

    CloseMessageWindow()
    Sound(2627, 255, 100, 0)
    Sleep(800)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "So you let him get away.\x02\x03",
            "I don't know where that rat came\x01",
            "from, but he was quite\x01",
            "shrewd.\x07\x00\x02",
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
        0x101,
        (
            "#00006FW-Wait!\x02\x03",
            "#00013FThe hacker... Were they\x01",
            "affiliated with Heiyue!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00700FNo, he's unrelated.\x02\x03",
            "Most likely, the hacker is\x01",
            "not affiliated with Red\x01",
            "Constellation, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FHow do you know that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702FHaha, Heiyue and Red\x01",
            "Constellation both have\x01",
            "their own intelligence.\x02\x03",
            "That hacker or whatever\x01",
            "shouldn't belong to\x01",
            "either of them.\x02\x03",
            "#00700F─It seems he was\x01",
            "planning something for\x01",
            "the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F...!\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    ChrTalk(
        0x102,
        (
            "#12P#00108FThe Orchis Tower\x01",
            "blueprints on the\x01",
            "terminal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FI see... Surely\x01",
            "tomorrow's conference is\x01",
            "the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#12P#00608F#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_6D1F():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6D1F)
    WaitChrThread(0x10A, 1)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#12P#00603F─I believe this is the\x01",
            "first time we've met.\x02\x03",
            "#00600FAlex Dudley, Crossbell\x01",
            "Police Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702FHaha... Your reputation\x01",
            "precedes you.\x02\x03",
            "Having trouble with\x01",
            "trade conference\x01",
            "security, right?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00604FHmph, it seems a certain\x01",
            "organization is infested\x01",
            "with suspicious people.\x02\x03",
            "It appears you know many\x01",
            "things that we do not...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0x10A, 0x26)
    SetChrSubChip(0x10A, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#12P#00601FCan I ask you to come to\x01",
            "HQ and ask you about\x01",
            "them?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F07():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6F07)
    Sleep(50)

    def lambda_6F17():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6F17)
    Sleep(50)

    def lambda_6F27():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6F27)
    Sleep(50)

    def lambda_6F37():
        TurnDirection(0x9, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6F37)
    Sleep(50)

    def lambda_6F47():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6F47)
    Sleep(50)

    def lambda_6F57():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6F57)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_6F7C():

        label("loc_6F7C")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6F7C")

    QueueWorkItem2(0x101, 2, lambda_6F7C)

    def lambda_6F8E():

        label("loc_6F8E")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6F8E")

    QueueWorkItem2(0x102, 2, lambda_6F8E)

    def lambda_6FA0():

        label("loc_6FA0")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6FA0")

    QueueWorkItem2(0x9, 2, lambda_6FA0)

    def lambda_6FB2():

        label("loc_6FB2")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6FB2")

    QueueWorkItem2(0x109, 2, lambda_6FB2)

    def lambda_6FC4():

        label("loc_6FC4")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6FC4")

    QueueWorkItem2(0x105, 2, lambda_6FC4)

    def lambda_6FD6():

        label("loc_6FD6")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6FD6")

    QueueWorkItem2(0x104, 2, lambda_6FD6)

    ChrTalk(
        0x101,
        "#00011FMr. Dudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FWhoa... You serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702FHaha, under what charge?\x02\x03",
            "I don't remember\x01",
            "violating any criminal\x01",
            "law.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00602FIt would just be a\x01",
            "voluntary interview.\x02\x03",
            "#00607FIf you're not guilty of\x01",
            "anything, then you should\x01",
            "have nothing to hide!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(341, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xA, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7145():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7145)
    ClearChrFlags(0xB, 0x80)

    def lambda_715B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_715B)
    Sleep(200)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    OP_68(500500, 1100, 504600, 1000)
    MoveCamera(59, 23, 0, 1000)
    SetCameraDistance(16500, 1000)
    SetChrFlags(0x10A, 0x20)
    SetChrFlags(0x10A, 0x1000)
    SetChrChipByIndex(0x10A, 0x20)
    SetChrSubChip(0x10A, 0x0)
    SetChrChip(0x0, 0x10A, 0x1E, 0x64)
    Sound(250, 0, 80, 0)

    def lambda_71C0():
        OP_96(0xFE, 0x7A4A4, 0x0, 0x7B700, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_71C0)
    WaitChrThread(0x10A, 1)
    CancelBlur(0)
    SetChrChipByIndex(0x10A, 0x2D)
    SetChrSubChip(0x10A, 0x1)
    Sleep(1000)
    SetChrChip(0x1, 0x10A, 0x0, 0x0)
    ClearChrFlags(0x10A, 0x20)
    ClearChrFlags(0x10A, 0x1000)
    SetChrChipByIndex(0x10A, 0x26)
    SetChrSubChip(0x10A, 0x0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)
    Sleep(500)
    Sound(2555, 255, 100, 0)

    ChrTalk(
        0x10A,
        "#11P#00603FHmph...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x9,
        "#00205F...When did he.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12P#NWow, a clone using\x01",
            "talisman arts, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(2628, 255, 100, 0)
    Sleep(800)
    SetMessageWindowPos(15, 10, -1, -1)
    SetChrName("Yin's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#40W...Farewell for tonight.\x02\x03",
            "#30WHowever, I feel we will\x01",
            "meet again soon.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0xA, 0x80)
    OP_68(500000, 1500, 501500, 3000)
    MoveCamera(47, 15, 0, 3000)
    SetCameraDistance(17500, 3000)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x10A)
    OP_64(0x9)
    OP_6F(0x79)
    Sleep(300)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#5P#00201FLloyd, should we search\x01",
            "the area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FNo... There's no need for\x01",
            "that.\x02\x03",
            "#00001FFor now, it appears we need to\x01",
            "return to the Support Section\x01",
            "and discuss this matter.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    TurnDirection(0x10A, 0x101, 500)

    ChrTalk(
        0x10A,
        (
            "#5P#00606FYeah... I guess we have\x01",
            "no choice.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(500000, 2000, 501500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0x9, 0x80)
    RemoveParty(0x9, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    OP_32(0x2, 0x0, 0x3F)
    OP_32(0x2, 0x5, 0x64)
    OP_42(0x2, 0x413, 0xFF)
    OP_42(0x2, 0x5E1, 0xFF)
    OP_42(0x2, 0x645, 0xFF)
    RemoveCraft(0x2, 0xFFFF)
    OP_38(0x2, 0x80, 0x2)
    OP_38(0x2, 0x81, 0x1)
    OP_38(0x2, 0x82, 0x1)
    OP_38(0x2, 0x83, 0x1)
    OP_38(0x2, 0x85, 0x1)
    OP_38(0x2, 0x86, 0x1)
    OP_42(0x2, 0xE3, 0x0)
    OP_42(0x2, 0x88, 0x1)
    OP_42(0x2, 0x78, 0x2)
    OP_42(0x2, 0x8F, 0x3)
    OP_42(0x2, 0x68, 0x5)
    OP_42(0x2, 0x74, 0x6)
    SetScenarioFlags(0x20, 3)
    AddCraft(0x2, 0xAA)
    AddCraft(0x2, 0xAC)
    AddCraft(0x2, 0xAD)
    AddCraft(0x2, 0xAE)
    AddCraft(0x2, 0xB0)
    AddCraft(0x2, 0x122)
    AddCraft(0x2, 0x123)
    SetChrChipPat(0x2, 0x6, 0x123)
    SetChrChipPat(0x2, 0x6, 0x125)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75B2")
    AddCraft(0x2, 0x1AF)
    AddCraft(0x0, 0x1AF)
    Jump("loc_75D0")

    label("loc_75B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_75C8")
    AddCraft(0x2, 0x19B)
    AddCraft(0x0, 0x19B)
    Jump("loc_75D0")

    label("loc_75C8")

    AddCraft(0x2, 0x187)
    AddCraft(0x0, 0x187)

    label("loc_75D0")

    AddCraft(0x2, 0x164)
    AddCraft(0x2, 0x189)
    AddCraft(0x1, 0x189)
    AddCraft(0x2, 0x18B)
    AddCraft(0x3, 0x18B)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 5)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_334F end

    def Function_22_75F7(): pass

    label("Function_22_75F7")


    def lambda_75FC():
        OP_96(0xFE, 0x7A120, 0x96, 0x32A28, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75FC)
    WaitChrThread(0xFE, 1)

    def lambda_761A():
        OP_96(0xFE, 0x7A120, 0x96, 0x335E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_761A)
    Sleep(300)

    def lambda_7637():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7637)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_75F7 end

    def Function_23_7648(): pass

    label("Function_23_7648")


    def lambda_764D():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_764D)

    def lambda_7667():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7667)
    WaitChrThread(0xFE, 1)

    def lambda_767C():
        OP_95(0xFE, 501000, 0, 296900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_767C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x3C, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_23_7648 end

    def Function_24_76B1(): pass

    label("Function_24_76B1")


    def lambda_76B6():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76B6)

    def lambda_76D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_76D0)
    WaitChrThread(0xFE, 1)

    def lambda_76E5():
        OP_95(0xFE, 499700, 0, 295200, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76E5)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_24_76B1 end

    def Function_25_7713(): pass

    label("Function_25_7713")


    def lambda_7718():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7718)

    def lambda_7732():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7732)
    WaitChrThread(0xFE, 1)

    def lambda_7747():
        OP_95(0xFE, 501700, 0, 294900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7747)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x3C, 0x1F4)
    Return()

    # Function_25_7713 end

    def Function_26_7775(): pass

    label("Function_26_7775")


    def lambda_777A():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_777A)

    def lambda_7794():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7794)
    WaitChrThread(0xFE, 1)

    def lambda_77A9():
        OP_95(0xFE, 499300, 0, 293200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77A9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_26_7775 end

    def Function_27_77CA(): pass

    label("Function_27_77CA")


    def lambda_77CF():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77CF)

    def lambda_77E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_77E9)
    WaitChrThread(0xFE, 1)

    def lambda_77FE():
        OP_95(0xFE, 501800, 0, 293000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77FE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_27_77CA end

    def Function_28_781F(): pass

    label("Function_28_781F")


    def lambda_7824():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7824)

    def lambda_783E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_783E)
    WaitChrThread(0xFE, 1)

    def lambda_7853():
        OP_95(0xFE, 500300, 0, 292400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7853)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_781F end

    def Function_29_7874(): pass

    label("Function_29_7874")

    SetChrPos(0x101, 500300, 0, 296300, 0)

    def lambda_788A():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_788A)
    WaitChrThread(0xFE, 1)

    def lambda_78A8():
        OP_95(0xFE, 497200, 0, 299700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78A8)
    WaitChrThread(0xFE, 1)

    def lambda_78C6():
        OP_95(0xFE, 497200, 200, 301200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78C6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_29_7874 end

    def Function_30_78E7(): pass

    label("Function_30_78E7")

    SetChrPos(0x10A, 501300, 200, 295600, 0)
    Sleep(700)

    def lambda_7900():
        OP_95(0xFE, 498600, 200, 300600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7900)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_30_78E7 end

    def Function_31_7921(): pass

    label("Function_31_7921")

    SetChrPos(0x10A, 501300, 200, 294600, 0)
    Sleep(1800)

    def lambda_793A():
        OP_95(0xFE, 500200, 0, 300600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_793A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_7921 end

    def Function_32_795B(): pass

    label("Function_32_795B")

    SetChrPos(0x102, 500300, 0, 295300, 0)
    Sleep(1300)

    def lambda_7974():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7974)
    WaitChrThread(0xFE, 1)

    def lambda_7992():
        OP_95(0xFE, 497100, 0, 299900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7992)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_32_795B end

    def Function_33_79B3(): pass

    label("Function_33_79B3")

    SetChrPos(0x105, 500300, 0, 294300, 0)
    Sleep(1900)

    def lambda_79CC():
        OP_95(0xFE, 499500, 0, 298400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79CC)
    WaitChrThread(0xFE, 1)

    def lambda_79EA():
        OP_95(0xFE, 498100, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79EA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_33_79B3 end

    def Function_34_7A0B(): pass

    label("Function_34_7A0B")

    SetChrPos(0x109, 500300, 0, 294300, 0)
    Sleep(2500)

    def lambda_7A24():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A24)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_34_7A0B end

    def Function_35_7A45(): pass

    label("Function_35_7A45")


    def lambda_7A4A():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7A4A)
    WaitChrThread(0x109, 1)
    Return()

    # Function_35_7A45 end

    def Function_36_7A64(): pass

    label("Function_36_7A64")

    Sleep(300)

    def lambda_7A6C():
        OP_95(0xFE, 502700, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7A6C)
    WaitChrThread(0x105, 1)

    def lambda_7A8A():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7A8A)
    WaitChrThread(0x105, 1)
    Return()

    # Function_36_7A64 end

    def Function_37_7AA4(): pass

    label("Function_37_7AA4")

    Sleep(550)

    def lambda_7AAC():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7AAC)
    WaitChrThread(0x104, 1)

    def lambda_7ACA():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7ACA)
    WaitChrThread(0x104, 1)
    Return()

    # Function_37_7AA4 end

    def Function_38_7AE4(): pass

    label("Function_38_7AE4")

    Sleep(200)

    def lambda_7AEC():
        OP_95(0xFE, 502500, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AEC)
    WaitChrThread(0xFE, 1)

    def lambda_7B0A():
        OP_95(0xFE, 505900, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B0A)
    WaitChrThread(0xFE, 1)

    def lambda_7B28():
        OP_95(0xFE, 509000, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B28)
    WaitChrThread(0xFE, 1)

    def lambda_7B46():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B46)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_7AE4 end

    def Function_39_7B60(): pass

    label("Function_39_7B60")

    OP_93(0x10A, 0x5A, 0x1F4)
    Sleep(900)

    def lambda_7B6F():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7B6F)
    WaitChrThread(0x10A, 1)

    def lambda_7B8D():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7B8D)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_39_7B60 end

    def Function_40_7BA7(): pass

    label("Function_40_7BA7")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(850)

    def lambda_7BB6():
        OP_95(0xFE, 502500, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BB6)
    WaitChrThread(0xFE, 1)

    def lambda_7BD4():
        OP_95(0xFE, 505900, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BD4)
    WaitChrThread(0xFE, 1)

    def lambda_7BF2():
        OP_95(0xFE, 509000, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BF2)
    WaitChrThread(0xFE, 1)

    def lambda_7C10():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C10)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_40_7BA7 end

    def Function_41_7C2A(): pass

    label("Function_41_7C2A")

    Sleep(300)

    def lambda_7C32():
        OP_95(0xFE, 500000, 0, 202400, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C32)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_41_7C2A end

    def Function_42_7C4C(): pass

    label("Function_42_7C4C")


    def lambda_7C51():
        OP_95(0xFE, 500000, 0, 203700, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C51)
    WaitChrThread(0xFE, 1)

    def lambda_7C6F():
        OP_95(0xFE, 499400, 0, 200700, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C6F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_42_7C4C end

    def Function_43_7C90(): pass

    label("Function_43_7C90")


    def lambda_7C95():
        OP_95(0xFE, 500000, 0, 204000, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C95)
    WaitChrThread(0xFE, 1)

    def lambda_7CB3():
        OP_95(0xFE, 500400, 0, 200000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7CB3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_43_7C90 end

    def Function_44_7CD4(): pass

    label("Function_44_7CD4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7CF6")
    Sound(840, 0, 100, 0)
    Sleep(1500)
    Sound(840, 0, 100, 0)
    Sleep(2000)
    Jump("Function_44_7CD4")

    label("loc_7CF6")

    Return()

    # Function_44_7CD4 end

    def Function_45_7CF7(): pass

    label("Function_45_7CF7")

    Sound(868, 2, 20, 0)
    Sound(825, 2, 20, 0)
    Sleep(200)
    OP_25(0x364, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(300)
    OP_25(0x364, 0x28)
    OP_25(0x339, 0x28)
    Return()

    # Function_45_7CF7 end

    def Function_46_7D1A(): pass

    label("Function_46_7D1A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(931)
    SoundLoad(825)
    OP_68(295000, 1500, 300000, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25000, 0)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x1E)
    ClearMapObjFlags(0x1D, 0x4)
    OP_75(0x1D, 0x2, 0x1B58)
    OP_7D(0x7D, 0x9B, 0xFF, 0x0, 0x2328)
    Sound(930, 0, 100, 0)
    OP_68(315000, 1500, 300000, 9000)
    MoveCamera(57, 10, -10, 9000)
    SetCameraDistance(27000, 9000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0xE, 1, 0, 47)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m0301", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_7D1A end

    def Function_47_7DD0(): pass

    label("Function_47_7DD0")

    Sound(931, 2, 30, 0)
    Sound(825, 2, 30, 0)
    Sleep(400)
    OP_25(0x3A3, 0x28)
    OP_25(0x339, 0x28)
    Sleep(400)
    OP_25(0x3A3, 0x32)
    OP_25(0x339, 0x32)
    Sleep(400)
    OP_25(0x3A3, 0x3C)
    OP_25(0x339, 0x3C)
    Sleep(400)
    OP_25(0x3A3, 0x46)
    OP_25(0x339, 0x46)
    Sleep(400)
    OP_25(0x3A3, 0x50)
    OP_25(0x339, 0x50)
    Sleep(400)
    OP_25(0x339, 0x5A)
    Sleep(400)
    OP_25(0x339, 0x64)
    Sleep(4200)
    StopSound(931, 1000, 80)
    StopSound(825, 1000, 100)
    Return()

    # Function_47_7DD0 end

    def Function_48_7E31(): pass

    label("Function_48_7E31")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The duct entrance is\x01",
            "locked with a sturdy\x01",
            "padlock.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_48_7E31 end

    SaveToFile()

Try(main)
