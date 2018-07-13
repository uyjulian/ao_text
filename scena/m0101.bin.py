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

    Sepith("Sepith_809E", 11,  1,   8,   0,   3,   7,   0)
    Sepith("Sepith_808E", 0,   10,  5,   0,   6,   2,   4)
    Sepith("Sepith_80A6", 0,   0,   0,   8,   6,   6,   6)
    Sepith("Sepith_8096", 6,   0,   11,  0,   0,   4,   6)

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
        "BattleInfo_6C4", 0x0000, 62, 6, 60, 6, 1, 25, 0, "bm0101", "Sepith_809E", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_534", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_808E", 30, 45, 20, 5,
        (
            ("ms63800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms63800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_AAC", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_80A6", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_78C", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_80A6", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_5FC", 0x0000, 62, 6, 60, 6, 1, 30, 0, "bm0101", "Sepith_8096", 30, 45, 20, 5,
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
        "Function_5_16AA",         # 05, 5
        "Function_6_1804",         # 06, 6
        "Function_7_1956",         # 07, 7
        "Function_8_1B72",         # 08, 8
        "Function_9_1BFA",         # 09, 9
        "Function_10_1CF0",        # 0A, 10
        "Function_11_1D0C",        # 0B, 11
        "Function_12_1D28",        # 0C, 12
        "Function_13_1D44",        # 0D, 13
        "Function_14_2247",        # 0E, 14
        "Function_15_23D2",        # 0F, 15
        "Function_16_2519",        # 10, 16
        "Function_17_283A",        # 11, 17
        "Function_18_2859",        # 12, 18
        "Function_19_2AB3",        # 13, 19
        "Function_20_2E6B",        # 14, 20
        "Function_21_3350",        # 15, 21
        "Function_22_77DE",        # 16, 22
        "Function_23_782F",        # 17, 23
        "Function_24_7898",        # 18, 24
        "Function_25_78FA",        # 19, 25
        "Function_26_795C",        # 1A, 26
        "Function_27_79B1",        # 1B, 27
        "Function_28_7A06",        # 1C, 28
        "Function_29_7A5B",        # 1D, 29
        "Function_30_7ACE",        # 1E, 30
        "Function_31_7B08",        # 1F, 31
        "Function_32_7B42",        # 20, 32
        "Function_33_7B9A",        # 21, 33
        "Function_34_7BF2",        # 22, 34
        "Function_35_7C2C",        # 23, 35
        "Function_36_7C4B",        # 24, 36
        "Function_37_7C8B",        # 25, 37
        "Function_38_7CCB",        # 26, 38
        "Function_39_7D47",        # 27, 39
        "Function_40_7D8E",        # 28, 40
        "Function_41_7E11",        # 29, 41
        "Function_42_7E33",        # 2A, 42
        "Function_43_7E77",        # 2B, 43
        "Function_44_7EBB",        # 2C, 44
        "Function_45_7EDE",        # 2D, 45
        "Function_46_7F01",        # 2E, 46
        "Function_47_7FB7",        # 2F, 47
        "Function_48_8018",        # 30, 48
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x14, 0x1E, 0x0, 0x0, 0x0)

    label("loc_165A")

    Jump("loc_169E")

    label("loc_165F")

    FadeToDark(300, 0, 100)

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

    label("loc_169E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_148E end

    def Function_5_16AA(): pass

    label("Function_5_16AA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D4")
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
            "#56IEarth Sepith x60\x01\x07\x02",
            "#57IWater Sepith x60\x01\x07\x02",
            "#58IFire Sepith x60\x01\x07\x02",
            "#59IWind Sepith x60\x01\x07\x02",
            "#60ITime Sepith x60\x01\x07\x02",
            "#61ISpace Sepith x60\x01\x07\x02",
            "#62IMirage Sepith x60\x01\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1EF, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_17F2")

    label("loc_17D4")


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

    label("loc_17F2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16AA end

    def Function_6_1804(): pass

    label("Function_6_1804")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1900")
    Sound(14, 0, 100, 0)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x334, 1)"), scpexpr(EXPR_END)), "loc_1889")
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
    Jump("loc_18FB")

    label("loc_1889")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x16, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18FB")

    Jump("loc_194A")

    label("loc_1900")

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

    label("loc_194A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1804 end

    def Function_7_1956(): pass

    label("Function_7_1956")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B27")
    Sound(14, 0, 100, 0)
    OP_74(0x17, 0x1E)
    OP_71(0x17, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A59")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_19B3():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19B3)

    def lambda_19CD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_19CD)
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
        (0, "loc_1A3A"),
        (2, "loc_1A49"),
        (1, "loc_1A56"),
        (SWITCH_DEFAULT, "loc_1A59"),
    )


    label("loc_1A3A")

    SetScenarioFlags(0x217, 0)
    OP_70(0x17, 0x1E)
    Sleep(500)
    Jump("loc_1A59")

    label("loc_1A49")

    OP_70(0x17, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1A56")

    OP_B9(0x0)
    Return()

    label("loc_1A59")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xAF, 1)"), scpexpr(EXPR_END)), "loc_1AB2")
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
    Jump("loc_1B22")

    label("loc_1AB2")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x17, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1B22")

    Jump("loc_1B66")

    label("loc_1B27")

    FadeToDark(300, 0, 100)

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

    label("loc_1B66")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1956 end

    def Function_8_1B72(): pass

    label("Function_8_1B72")

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
            "Walk Away\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BC4"),
        (1, "loc_1BE1"),
        (SWITCH_DEFAULT, "loc_1BE6"),
    )


    label("loc_1BC4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x13, 0x10)
    OP_65(0x0, 0x1)
    Call(0, 21)
    Jump("loc_1BE6")

    label("loc_1BE1")

    Jump("loc_1BE6")

    label("loc_1BE6")

    SetChrPos(0x0, 500000, 0, 205800, 180)
    EventEnd(0x5)
    Return()

    # Function_8_1B72 end

    def Function_9_1BFA(): pass

    label("Function_9_1BFA")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE1")
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

    label("loc_1CE1")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_9_1BFA end

    def Function_10_1CF0(): pass

    label("Function_10_1CF0")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1CF0 end

    def Function_11_1D0C(): pass

    label("Function_11_1D0C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1D0C end

    def Function_12_1D28(): pass

    label("Function_12_1D28")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_1D28 end

    def Function_13_1D44(): pass

    label("Function_13_1D44")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a control unit for adjusting the water level.\x01",
            "Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2246")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3D")
    SetChrPos(0x0, 107620, -6000, 200, 0)
    SetChrPos(0x1, 108620, -6000, -600, 0)
    SetChrPos(0x2, 106620, -6000, -600, 0)
    SetChrPos(0x3, 107620, -6000, -1900, 0)
    OP_68(107660, -5000, 850, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    Jump("loc_1F44")

    label("loc_1E3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC3")
    SetChrPos(0x0, 85000, -6000, 101000, 0)
    SetChrPos(0x1, 83800, -6000, 101000, 0)
    SetChrPos(0x2, 83800, -6000, 99800, 0)
    SetChrPos(0x3, 85000, -6000, 99800, 0)
    OP_68(84580, -5000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27000, 0)
    Jump("loc_1F44")

    label("loc_1EC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F44")
    SetChrPos(0x0, 201500, -6000, 184000, 90)
    SetChrPos(0x1, 200000, -6000, 185000, 90)
    SetChrPos(0x2, 200000, -6000, 183000, 90)
    SetChrPos(0x3, 198500, -6000, 184000, 90)
    OP_68(201500, -5000, 184020, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33500, 0)

    label("loc_1F44")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 0)), scpexpr(EXPR_END)), "loc_20CF")
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE8")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_2067")

    label("loc_1FE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202A")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_2067")

    label("loc_202A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2067")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_2067")

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
    Jump("loc_2246")

    label("loc_20CF")

    SetMapObjFrame(0xE, "m01gim01", 0x2, "on")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2166")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_21E5")

    label("loc_2166")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21A8")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_21E5")

    label("loc_21A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E5")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_21E5")

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

    label("loc_2246")

    Return()

    # Function_13_1D44 end

    def Function_14_2247(): pass

    label("Function_14_2247")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(144)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an elevator control panel.\x01",
            "Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23CA")
    Fade(500)
    SetChrPos(0x0, 600, 0, 600, 90)
    SetChrPos(0x1, 600, 0, -600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_232A")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_2349")

    label("loc_232A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2349")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_2349")

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

    label("loc_23CA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2247 end

    def Function_15_23D2(): pass

    label("Function_15_23D2")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A5")
    OP_90(0x4, -1800, 0, -600, 90)
    OP_90(0x5, -1800, 0, 600, 90)
    Jump("loc_24C4")

    label("loc_24A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C4")
    OP_90(0x4, -1800, 0, 0, 90)

    label("loc_24C4")

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

    # Function_15_23D2 end

    def Function_16_2519(): pass

    label("Function_16_2519")

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
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3706V#30W──Uhuhu, I see.\x02\x03",
            "#3707VQuite the easy\x01",
            "to use terminal.\x02",
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
            "The most gifted system engineer \x01",
            "of the Foundation, Jona Sacred, eh?\x02\x03",
            "To think he constructed such\x01",
            "an environment although this\x01",
            "is an old style network...\x02\x03",
            "It appears it wasn't\x01",
            "necessarily a fluke that he\x01",
            "was able to catch Renne.\x02",
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

    # Function_16_2519 end

    def Function_17_283A(): pass

    label("Function_17_283A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2858")
    SetChrSubChip(0x8, 0x0)
    Sleep(200)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)
    Jump("Function_17_283A")

    label("loc_2858")

    Return()

    # Function_17_283A end

    def Function_18_2859(): pass

    label("Function_18_2859")

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
            "#6P#04805FWhoops...\x01",
            "Did I make a mistake?\x02",
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
            "#6P#04802FUhuhu...\x01",
            "You're good, freckles.\x02\x03",
            "But I wonder, won't he discover\x01",
            "this trick until morning?\x02\x03",
            "#04809FSince I'm here, I guess I'll enjoy\x01",
            "myself in many different ways㈱\x02",
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

    # Function_18_2859 end

    def Function_19_2AB3(): pass

    label("Function_19_2AB3")

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
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3708V#40WThus, the fated tower appears.\x01",
            "Since it involves many destinies,\x01",
            "it describes a spiral──\x02",
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
            "#12P#04804FUh uh, it's a scene that Bleublanc\x01",
            "would love indeed.\x02\x03",
            "#04800FWell, it appears that he went on\x01",
            "his own accord to watch this event.\x02",
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
        "#12P#04805FOh, here they are.\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#04802FUhuhu...\x01",
            "Now I just have to hand these over to "them".\x02\x03",
            "#04809FWell then, since I'm here I guess\x01",
            "I'll do some funny preparations㈱\x02",
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

    # Function_19_2AB3 end

    def Function_20_2E6B(): pass

    label("Function_20_2E6B")

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
        "#00011F#6P(This melody...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_2FD1():
        OP_97(0x101, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FD1)
    Sleep(100)

    def lambda_2FEE():
        OP_97(0x102, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2FEE)
    Sleep(100)

    def lambda_300B():
        OP_97(0x104, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_300B)
    Sleep(100)

    def lambda_3028():
        OP_97(0x109, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3028)
    Sleep(100)

    def lambda_3045():
        OP_97(0x10A, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3045)
    Sleep(100)

    def lambda_3062():
        OP_97(0x105, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3062)
    Sleep(2000)
    Fade(500)
    OP_68(500000, 1100, 204000, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    WaitChrThread(0x101, 0)

    def lambda_30B6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30B6)
    WaitChrThread(0x102, 0)

    def lambda_30C7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_30C7)
    WaitChrThread(0x104, 0)

    def lambda_30D8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_30D8)
    WaitChrThread(0x109, 0)

    def lambda_30E9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_30E9)
    WaitChrThread(0x10A, 0)

    def lambda_30FA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_30FA)
    WaitChrThread(0x105, 0)

    def lambda_310B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_310B)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#00108F(Is it coming from the orbal\x01",
            "stereo Jona has in there...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F(What the...?\x01",
            "Could it be broken?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)

    ChrTalk(
        0x10A,
        (
            "#6P#00603F(Maybe it's a trap...\x01",
            "Let's step in cautiously, just in case.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x10A,
        (
            "#6P#00601F(Bannings, Orlando.\x01",
            "Let's charge in first.)\x02\x03",
            "(You other three, \x01",
            "enter after us.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3265():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3265)
    Sleep(50)

    def lambda_3275():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3275)
    Sleep(50)

    def lambda_3285():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3285)
    Sleep(50)

    def lambda_3295():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3295)
    Sleep(50)

    def lambda_32A5():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_32A5)
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

    # Function_20_2E6B end

    def Function_21_3350(): pass

    label("Function_21_3350")

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

    def lambda_35BE():
        OP_95(0xFE, 500000, 150, 207400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_35BE)
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

    def lambda_3628():
        OP_95(0xFE, 500000, 150, 210400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3628)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 22)
    Sleep(200)

    def lambda_364E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_364E)
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
        "#00301F#5PAnd no presence in hidin' too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5P#00606F#11P...Did he run away?\x02\x03",
            "#00600FStill, while coming here we\x01",
            "didn't pass anyone...\x02",
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
        "#12P#00108FD-Did he run away?\x02",
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
            "#00001F#6PThis music...\x01",
            "It seems it's from there.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39B1():
        OP_92(0x101, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39B1)
    Sleep(50)

    def lambda_39C7():
        OP_92(0x102, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_39C7)
    Sleep(50)

    def lambda_39DD():
        OP_92(0x105, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_39DD)
    Sleep(50)

    def lambda_39F3():
        OP_92(0x10A, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_39F3)
    Sleep(50)

    def lambda_3A09():
        OP_92(0x109, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3A09)
    Sleep(50)

    def lambda_3A1F():
        OP_92(0x104, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3A1F)
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
            "Could you make it stop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PYeah...\x01",
            "This is the switch.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3AB4():
        OP_96(0xFE, 0x7AF94, 0x0, 0x4824C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AB4)
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
            "#6P#00106FR-Right...\x01",
            "It's unnatural that\x01",
            "music was playing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10308FHm, somehow I\x01",
            "feel malice, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#12P#10305FAt any rate, what's that showing\x01",
            "on the monitors in the back?\x02",
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

    def lambda_3C5B():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C5B)
    Sleep(50)

    def lambda_3C6B():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3C6B)
    Sleep(50)

    def lambda_3C7B():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3C7B)
    Sleep(50)

    def lambda_3C8B():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C8B)
    Sleep(50)

    def lambda_3C9B():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3C9B)
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
            "#00105FT-These are...\x01",
            "No way, the Orchis Tower...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10101FIt looks like recorded data of the\x01",
            "structure charts of the tower interior...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x10A,
        (
            "#00610FKh, why are such things\x01",
            "in a place like this──\x02",
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
        "#12P#10310FDamn...!\x02",
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

    def lambda_4033():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4033)
    Sleep(30)

    def lambda_4043():
        OP_93(0x10A, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_4043)
    Sleep(30)

    def lambda_4053():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4053)
    Sleep(30)

    def lambda_4063():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4063)
    Sleep(30)

    def lambda_4073():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4073)
    Sleep(30)

    def lambda_4083():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4083)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        "#00101F#6P#N! \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        "#00610F#6PTsk, a trap!?\x02",
    )

    CloseMessageWindow()
    OP_68(505950, 900, 400300, 1500)
    MoveCamera(50, 17, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(21500, 1500)

    def lambda_410A():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_410A)
    Sleep(300)

    def lambda_4127():
        OP_95(0xFE, 502700, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4127)
    WaitChrThread(0x105, 1)

    def lambda_4145():
        OP_95(0xFE, 508400, 0, 400700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4145)
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
            "#10110F#6PI-It's no use!\x01",
            "It doesn't open at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308F#5PIt looks like it was locked\x01",
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

    def lambda_434B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_434B)

    def lambda_4358():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4358)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#00010FWhat was that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00307FHey, who's there...?\x02",
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
            "#3709V#30WUhuhu...\x01",
            "Pleased to meet you, ladies and \x01",
            "gentlemen of the Support Section.\x02",
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
            "#3710V#30WIt looks like you came to visit\x01",
            "as I had expected.\x02",
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
            "#3711V#30WIt would make me glad if you'd got \x01",
            "some fun from the parting gift I left\x01",
            "as a symbol of our acquaintanceship㈱\x07\x00\x02",
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
        "#00607F#11PKh, he's talking from the terminal?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(498200, 1300, 302300, 2000)
    MoveCamera(33, 17, 0, 2000)
    SetCameraDistance(20500, 2000)

    def lambda_45A1():
        OP_95(0xFE, 499500, 0, 298400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_45A1)

    def lambda_45BB():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_45BB)
    Sleep(30)

    def lambda_45CB():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_45CB)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    def lambda_45E3():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_45E3)
    Sleep(30)

    def lambda_45F3():
        OP_95(0xFE, 499200, 0, 299300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_45F3)
    WaitChrThread(0x105, 1)

    def lambda_4611():
        OP_95(0xFE, 498100, 0, 299300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4611)
    WaitChrThread(0x105, 1)

    def lambda_462F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_462F)
    WaitChrThread(0x109, 1)

    def lambda_4640():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4640)
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
            "#00101FThe competition puzzle game\x01",
            "Chief Roberts gave us...!?\x02",
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
            "If you manage to win 2 matches\x01",
            "out of 3, I'll set you free.\x02\x03",
            "However, in case you lose,\x01",
            "I guess you'll be burnt to a crisp?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#00010FWhat...!?\x02",
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

    def lambda_4917():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4917)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_493F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_493F)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4964():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4964)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_498C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_498C)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_49B1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_49B1)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_49D9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_49D9)
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
            "#5P#00307FNo way...!\x01",
            "I didn't sense any trap!?\x02",
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
            "Uhuhu, shall\x01",
            "we begin then?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "There isn't much time...\x01",
            "You must hurry up, or you'll die, you know?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0x10A, 0x0, 0x1F4)

    ChrTalk(
        0x10A,
        "#00610FBastard...!\x02",
    )

    CloseMessageWindow()

    def lambda_4B19():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4B19)

    def lambda_4B26():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4B26)
    Sleep(30)

    def lambda_4B36():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4B36)
    Sleep(30)

    def lambda_4B46():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4B46)
    Sleep(30)

    def lambda_4B56():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4B56)
    Sleep(30)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x105,
        (
            "#12P#10307FLloyd!\x01",
            "We have no choice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00010FShit──got it!\x02",
    )

    CloseMessageWindow()
    StopSound(868, 1000, 40)
    StopSound(825, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0x20, 0x33)
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C33")
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C29")
    OP_2C(0xA3, 0x1)
    Jump("loc_4C2E")

    label("loc_4C29")

    OP_2C(0xA3, 0x2)

    label("loc_4C2E")

    Jump("loc_4C36")

    label("loc_4C33")

    ClearScenarioFlags(0x0, 1)

    label("loc_4C36")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4F51")

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
        "#00309FYou're good, huh?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Hmmm.\x01",
            "Could I have let my guard down?\x02\x03",
            "Then, I'll do the next one in earnest──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_500D")

    label("loc_4F51")


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
        (
            "#12P#10306FUhhm.\x01",
            "Close, but...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Ahaha!\x01",
            "There's no way out for you.\x02\x03",
            "Then, I'll give you the finishing──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_500D")

    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2669V#30W──Please shape up already.\x07\x00\x02",
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
        "#12P#00105FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FThis voice...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2670V#30WFrom now on, I will\x01",
            "be your opponent.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2671V#30W──Please prepare yourself.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_53EC")
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 496500, 500, 292600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502300, 2000, 292100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 493200, 2000, 299500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 504000, 1500, 298100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502000, 2500, 301100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 498500, 2000, 401200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 501700, 1500, 404100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507700, 1000, 402700, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507200, 500, 396600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)

    label("loc_53EC")

    FadeToBright(0, -1)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5733")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3712V#30WEeeh...!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE80)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2672V#30WAnd now, the next one.\x07\x00\x02",
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

    label("loc_5733")

    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        "#11P#00002FY-Yes...!\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x2D, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00310F#5PKh...\x01",
            "Things are gettin' bad here, you know!?\x02",
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
            "#3714V#30WIt seems you're one of their comrades,\x01",
            "so like I promised, I'll let them out.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3715V#30W──Well then, see you㈱\x07\x00\x02",
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

    def lambda_597B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_597B)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_59A0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_59A0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_59C8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_59C8)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_59ED():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_59ED)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5A15():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_5A15)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10107F#5PIt opened...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00610F#5PQuick, it's going to explode!\x02",
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
        "#6P#00007F#NYes!\x02",
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

    def lambda_5DD1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DD1)
    WaitChrThread(0x101, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#00006F#40W*pant pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#40W#11PMan, by a hair's breath...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#40W#11PI-I thought I was going to die...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00610F#40W#11PKh...\x01",
            "Who's there...!?\x02",
        )
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
            "#2673V#30W──I am glad.\x01",
            "You look to be all in one piece.\x02",
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

    def lambda_611B():
        OP_96(0xFE, 0x7AA1C, 0x0, 0x7A508, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_611B)
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
        (
            "#00102FA-As I thought,\x01",
            "it was you, Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FHey now!\x01",
            "The heck's goin' on!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2276, 255, 80, 0)
    Sleep(800)

    def lambda_61BD():
        OP_95(0xFE, 502500, 0, 500400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_61BD)
    WaitChrThread(0x9, 1)

    def lambda_61DB():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_61DB)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    def lambda_620B():
        OP_96(0xFE, 0x7AA1C, 0x0, 0x7A508, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_620B)
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
            "──Actually, this afternoon\x01",
            "I boarded an international\x01",
            "airliner bound for Crossbell.\x02\x03",
            "Since it appeared you were\x01",
            "having many problems,\x01",
            "I kind of came back earlier.\x02",
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
        "#12P#00000FIs that so...\x02",
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
            "#6P#00309FHa ha...\x01",
            "You were really right on.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#12P#N#10302FSo, you heard the story from\x01",
            "Chief and came here?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x9, 0x104, 500)

    ChrTalk(
        0x9,
        (
            "#00204FYes. When I contacted him via ENIGMA,\x01",
            "I heard you had headed over here.\x02\x03",
            "#00202FSo, I came straightly here from the airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F*giggle*...\x01",
            "You really saved us.\x02",
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
        "#00204F#5PNo, I'm glad I made it in time.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#00201F#5P...Even so, it seems he\x01",
            "was a pain of an opponent.\x02\x03",
            "Somehow I was able to repel him\x01",
            "by cutting myself in, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FCutting in── ah, that.\x02",
    )

    CloseMessageWindow()
    OP_68(502700, 500, 508900, 2000)
    OP_93(0x9, 0x0, 0x190)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#12P#N#00202FYes. Since I understood that\x01",
            "you all were locked inside, I\x01",
            "intervened from a backup line.\x02\x03",
            "#00206FIt appears he is quite\x01",
            "the skilled hacker.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00006F#12P#NYeah, you're right.\x02",
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
            "#6P#00601FHmph, it appears he had\x01",
            "retreated a long time ago...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x10A,
        (
            "#6P#00605FBy the way, Plato.\x02\x03",
            "Did you come here through\x01",
            "the Geofront alone?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10A, 500)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#11P#00205FOh, no.\x02\x03",
            "#00203F...Since he happened to be around by chance,\x01",
            "I had myself accompanied by him.\x02",
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
            "#5P#N──It appears we met in\x01",
            "serious circumstances.\x07\x00\x02",
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

    def lambda_6986():
        OP_96(0xFE, 0x7A120, 0x0, 0x7B0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6986)

    def lambda_69A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_69A0)

    def lambda_69B1():

        label("loc_69B1")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_69B1")

    QueueWorkItem2(0x101, 2, lambda_69B1)

    def lambda_69C3():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_69C3)

    def lambda_69D0():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_69D0)

    def lambda_69DD():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_69DD)

    def lambda_69EA():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_69EA)

    def lambda_69F7():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_69F7)

    def lambda_6A04():

        label("loc_6A04")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_6A04")

    QueueWorkItem2(0x9, 2, lambda_6A04)
    WaitChrThread(0xA, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00007FYou...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10107FThe one f-from back then...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101F"Yin"...!\x02",
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
            "...You did fail to catch him?\x02\x03",
            "I don't know who that rat was, but\x01",
            "he seems considerably shrewd.\x07\x00\x02",
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
            "#00006FP-Please wait!\x02\x03",
            "#00013FIs the hacker that was here\x01",
            "related to the "Heiyue"!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00700FNo, he's a total stranger.\x02\x03",
            "And possibly he's not even connected\x01",
            "to the "Red Constellation".\x07\x00\x02",
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
        (
            "#12P#00301FHow'd you know\x01",
            "about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702FUh uh, the "Heiyue" and the "Red Constellation"\x01",
            "have both their monitoring systems.\x02\x03",
            "At least that hacker or whatever\x01",
            "shouldn't belong to either of them.\x02\x03",
            "#00700F──It appears he's a person with some ulterior\x01",
            "motive for the Trade Conference.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F......!\x02",
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
            "#12P#00108FThe Orchis Tower blueprints that\x01",
            "were showing on the terminals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FI see...\x01",
            "It really is the place of tomorrow's conference.\x02",
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

    def lambda_6E7A():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6E7A)
    WaitChrThread(0x10A, 1)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#12P#00603F──I think it's the first time we meet.\x02\x03",
            "#00600FAlex Dudley, Crossbell\x01",
            "Police, Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702FUh uh...you've got a big reputation.\x02\x03",
            "You're having various hardships dealing\x01",
            "with the Trade Conference security, right?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00604FHmph, starting from a certain organization, there's \x01",
            "the spreading of a suspicious bunch of people.\x02\x03",
            "It appears you know many things\x01",
            "about activities we do not...\x02",
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
            "#12P#00601FCould I have you come with me\x01",
            "at the police and ask about that?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70AC():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_70AC)
    Sleep(50)

    def lambda_70BC():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_70BC)
    Sleep(50)

    def lambda_70CC():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_70CC)
    Sleep(50)

    def lambda_70DC():
        TurnDirection(0x9, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_70DC)
    Sleep(50)

    def lambda_70EC():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_70EC)
    Sleep(50)

    def lambda_70FC():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_70FC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_7121():

        label("loc_7121")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_7121")

    QueueWorkItem2(0x101, 2, lambda_7121)

    def lambda_7133():

        label("loc_7133")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_7133")

    QueueWorkItem2(0x102, 2, lambda_7133)

    def lambda_7145():

        label("loc_7145")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_7145")

    QueueWorkItem2(0x9, 2, lambda_7145)

    def lambda_7157():

        label("loc_7157")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_7157")

    QueueWorkItem2(0x109, 2, lambda_7157)

    def lambda_7169():

        label("loc_7169")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_7169")

    QueueWorkItem2(0x105, 2, lambda_7169)

    def lambda_717B():

        label("loc_717B")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_717B")

    QueueWorkItem2(0x104, 2, lambda_717B)

    ChrTalk(
        0x101,
        "#00011FMr. Dudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FHey now...seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702FUh uh, under what charges?\x02\x03",
            "I don't remember having done anything\x01",
            "against Crossbell criminal laws.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00602FWell, just for an arbitrary interview.\x02\x03",
            "#00607FIf you aren't guilty of anything,\x01",
            "then I'd really want you to──!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(341, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xA, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7300():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7300)
    ClearChrFlags(0xB, 0x80)

    def lambda_7316():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_7316)
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

    def lambda_737B():
        OP_96(0xFE, 0x7A4A4, 0x0, 0x7B700, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_737B)
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
        "#00205F...Gone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12P#NWow, it's that clone thing\x01",
            "made with talisman arts?\x02",
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
            "#40W...It's farewell for tonight.\x02\x03",
            "#30WBut I have the feeling we'll\x01",
            "be able to meet again soon.\x07\x00\x02",
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
            "#5P#00201F...Mr. Lloyd.\x01",
            "Should we search the environs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FNo...there's no need for that.\x02\x03",
            "#00001FAt any rate, it appears we need to go\x01",
            "back to the Support Section and talk.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    TurnDirection(0x10A, 0x101, 500)

    ChrTalk(
        0x10A,
        (
            "#5P#00606FYeah... I'm reluctant, but\x01",
            "we can't do differently.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7799")
    AddCraft(0x2, 0x1AF)
    AddCraft(0x0, 0x1AF)
    Jump("loc_77B7")

    label("loc_7799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_77AF")
    AddCraft(0x2, 0x19B)
    AddCraft(0x0, 0x19B)
    Jump("loc_77B7")

    label("loc_77AF")

    AddCraft(0x2, 0x187)
    AddCraft(0x0, 0x187)

    label("loc_77B7")

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

    # Function_21_3350 end

    def Function_22_77DE(): pass

    label("Function_22_77DE")


    def lambda_77E3():
        OP_96(0xFE, 0x7A120, 0x96, 0x32A28, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77E3)
    WaitChrThread(0xFE, 1)

    def lambda_7801():
        OP_96(0xFE, 0x7A120, 0x96, 0x335E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7801)
    Sleep(300)

    def lambda_781E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_781E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_77DE end

    def Function_23_782F(): pass

    label("Function_23_782F")


    def lambda_7834():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7834)

    def lambda_784E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_784E)
    WaitChrThread(0xFE, 1)

    def lambda_7863():
        OP_95(0xFE, 501000, 0, 296900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7863)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x3C, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_23_782F end

    def Function_24_7898(): pass

    label("Function_24_7898")


    def lambda_789D():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_789D)

    def lambda_78B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_78B7)
    WaitChrThread(0xFE, 1)

    def lambda_78CC():
        OP_95(0xFE, 499700, 0, 295200, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78CC)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_24_7898 end

    def Function_25_78FA(): pass

    label("Function_25_78FA")


    def lambda_78FF():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78FF)

    def lambda_7919():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7919)
    WaitChrThread(0xFE, 1)

    def lambda_792E():
        OP_95(0xFE, 501700, 0, 294900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_792E)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x3C, 0x1F4)
    Return()

    # Function_25_78FA end

    def Function_26_795C(): pass

    label("Function_26_795C")


    def lambda_7961():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7961)

    def lambda_797B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_797B)
    WaitChrThread(0xFE, 1)

    def lambda_7990():
        OP_95(0xFE, 499300, 0, 293200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7990)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_26_795C end

    def Function_27_79B1(): pass

    label("Function_27_79B1")


    def lambda_79B6():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79B6)

    def lambda_79D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_79D0)
    WaitChrThread(0xFE, 1)

    def lambda_79E5():
        OP_95(0xFE, 501800, 0, 293000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79E5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_27_79B1 end

    def Function_28_7A06(): pass

    label("Function_28_7A06")


    def lambda_7A0B():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A0B)

    def lambda_7A25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7A25)
    WaitChrThread(0xFE, 1)

    def lambda_7A3A():
        OP_95(0xFE, 500300, 0, 292400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A3A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_7A06 end

    def Function_29_7A5B(): pass

    label("Function_29_7A5B")

    SetChrPos(0x101, 500300, 0, 296300, 0)

    def lambda_7A71():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A71)
    WaitChrThread(0xFE, 1)

    def lambda_7A8F():
        OP_95(0xFE, 497200, 0, 299700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A8F)
    WaitChrThread(0xFE, 1)

    def lambda_7AAD():
        OP_95(0xFE, 497200, 200, 301200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AAD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_29_7A5B end

    def Function_30_7ACE(): pass

    label("Function_30_7ACE")

    SetChrPos(0x10A, 501300, 200, 295600, 0)
    Sleep(700)

    def lambda_7AE7():
        OP_95(0xFE, 498600, 200, 300600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AE7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_30_7ACE end

    def Function_31_7B08(): pass

    label("Function_31_7B08")

    SetChrPos(0x10A, 501300, 200, 294600, 0)
    Sleep(1800)

    def lambda_7B21():
        OP_95(0xFE, 500200, 0, 300600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B21)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_7B08 end

    def Function_32_7B42(): pass

    label("Function_32_7B42")

    SetChrPos(0x102, 500300, 0, 295300, 0)
    Sleep(1300)

    def lambda_7B5B():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B5B)
    WaitChrThread(0xFE, 1)

    def lambda_7B79():
        OP_95(0xFE, 497100, 0, 299900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B79)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_32_7B42 end

    def Function_33_7B9A(): pass

    label("Function_33_7B9A")

    SetChrPos(0x105, 500300, 0, 294300, 0)
    Sleep(1900)

    def lambda_7BB3():
        OP_95(0xFE, 499500, 0, 298400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BB3)
    WaitChrThread(0xFE, 1)

    def lambda_7BD1():
        OP_95(0xFE, 498100, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BD1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_33_7B9A end

    def Function_34_7BF2(): pass

    label("Function_34_7BF2")

    SetChrPos(0x109, 500300, 0, 294300, 0)
    Sleep(2500)

    def lambda_7C0B():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C0B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_34_7BF2 end

    def Function_35_7C2C(): pass

    label("Function_35_7C2C")


    def lambda_7C31():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7C31)
    WaitChrThread(0x109, 1)
    Return()

    # Function_35_7C2C end

    def Function_36_7C4B(): pass

    label("Function_36_7C4B")

    Sleep(300)

    def lambda_7C53():
        OP_95(0xFE, 502700, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7C53)
    WaitChrThread(0x105, 1)

    def lambda_7C71():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7C71)
    WaitChrThread(0x105, 1)
    Return()

    # Function_36_7C4B end

    def Function_37_7C8B(): pass

    label("Function_37_7C8B")

    Sleep(550)

    def lambda_7C93():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C93)
    WaitChrThread(0x104, 1)

    def lambda_7CB1():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7CB1)
    WaitChrThread(0x104, 1)
    Return()

    # Function_37_7C8B end

    def Function_38_7CCB(): pass

    label("Function_38_7CCB")

    Sleep(200)

    def lambda_7CD3():
        OP_95(0xFE, 502500, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7CD3)
    WaitChrThread(0xFE, 1)

    def lambda_7CF1():
        OP_95(0xFE, 505900, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7CF1)
    WaitChrThread(0xFE, 1)

    def lambda_7D0F():
        OP_95(0xFE, 509000, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7D0F)
    WaitChrThread(0xFE, 1)

    def lambda_7D2D():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7D2D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_7CCB end

    def Function_39_7D47(): pass

    label("Function_39_7D47")

    OP_93(0x10A, 0x5A, 0x1F4)
    Sleep(900)

    def lambda_7D56():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7D56)
    WaitChrThread(0x10A, 1)

    def lambda_7D74():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7D74)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_39_7D47 end

    def Function_40_7D8E(): pass

    label("Function_40_7D8E")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(850)

    def lambda_7D9D():
        OP_95(0xFE, 502500, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7D9D)
    WaitChrThread(0xFE, 1)

    def lambda_7DBB():
        OP_95(0xFE, 505900, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7DBB)
    WaitChrThread(0xFE, 1)

    def lambda_7DD9():
        OP_95(0xFE, 509000, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7DD9)
    WaitChrThread(0xFE, 1)

    def lambda_7DF7():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7DF7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_40_7D8E end

    def Function_41_7E11(): pass

    label("Function_41_7E11")

    Sleep(300)

    def lambda_7E19():
        OP_95(0xFE, 500000, 0, 202400, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7E19)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_41_7E11 end

    def Function_42_7E33(): pass

    label("Function_42_7E33")


    def lambda_7E38():
        OP_95(0xFE, 500000, 0, 203700, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7E38)
    WaitChrThread(0xFE, 1)

    def lambda_7E56():
        OP_95(0xFE, 499400, 0, 200700, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7E56)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_42_7E33 end

    def Function_43_7E77(): pass

    label("Function_43_7E77")


    def lambda_7E7C():
        OP_95(0xFE, 500000, 0, 204000, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7E7C)
    WaitChrThread(0xFE, 1)

    def lambda_7E9A():
        OP_95(0xFE, 500400, 0, 200000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7E9A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_43_7E77 end

    def Function_44_7EBB(): pass

    label("Function_44_7EBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EDD")
    Sound(840, 0, 100, 0)
    Sleep(1500)
    Sound(840, 0, 100, 0)
    Sleep(2000)
    Jump("Function_44_7EBB")

    label("loc_7EDD")

    Return()

    # Function_44_7EBB end

    def Function_45_7EDE(): pass

    label("Function_45_7EDE")

    Sound(868, 2, 20, 0)
    Sound(825, 2, 20, 0)
    Sleep(200)
    OP_25(0x364, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(300)
    OP_25(0x364, 0x28)
    OP_25(0x339, 0x28)
    Return()

    # Function_45_7EDE end

    def Function_46_7F01(): pass

    label("Function_46_7F01")

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

    # Function_46_7F01 end

    def Function_47_7FB7(): pass

    label("Function_47_7FB7")

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

    # Function_47_7FB7 end

    def Function_48_8018(): pass

    label("Function_48_8018")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a sturdy padlock\x01",
            "at the duct entrance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_48_8018 end

    SaveToFile()

Try(main)
