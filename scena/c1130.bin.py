from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1130.bin",                # FileName
        "c1130",                    # MapName
        "c1130",                    # Location
        0x0019,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 25, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1130",                  # 0
        "Cathar",               # 1
        "Novels",               # 2
        "Shanna",               # 3
        "Abby",                 # 4
        "Miles",               # 5
        "Nielsen",             # 6
        "Keya",                 # 7
        "Leyte",                 # 8
        "Cathar",               # 9
    ))

    AddCharChip((
        "chr/ch28200.itc",                   # 00
        "chr/ch28202.itc",                   # 01
        "chr/ch29402.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch20302.itc",                   # 04
        "chr/ch34200.itc",                   # 05
        "chr/ch34202.itc",                   # 06
        "chr/ch20202.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch08200.itc",                   # 09
        "chr/ch45100.itc",                   # 0A
        "chr/ch20200.itc",                   # 0B
        "chr/ch29400.itc",                   # 0C
        "chr/ch45102.itc",                   # 0D
    ))

    DeclNpc(29309,   4000,    4294957857, 90,   261,  0x0, 0,   0,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(18040,   180,     4294957597, 180,  261,  0x0, 0,   12,  0,   0,   0,   0,   6,   255,  0)
    DeclNpc(13199,   4000,    10529,   180,  325,  0x0, 0,   3,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(12649,   4000,    10529,   180,  325,  0x0, 1,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(7699,    150,     7980,    270,  325,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(10420,   29,      4294966796, 180,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8699,    150,     7980,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(8699,    150,     7980,    90,   389,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(6290,    0,       8000,    1300,    7700,    1500,    7980,    0x007E, 0,  12, 0x0000)
    DeclActor(2750,    0,       11140,   1000,    2750,    1200,    11140,   0x007C, 0,  35, 0x0000)
    DeclActor(18610,   0,       4294962796, 1000,    18610,   1200,    4294962796, 0x007C, 0,  4,  0x0000)
    DeclActor(23750,   0,       4294957796, 1000,    23750,   1200,    4294957796, 0x007C, 0,  36, 0x0000)
    DeclActor(6500,    0,       4294962796, 1000,    6500,    1200,    4294962796, 0x007C, 0,  37, 0x0000)
    DeclActor(9300,    0,       4294962796, 1000,    9300,    1200,    4294962796, 0x007C, 0,  38, 0x0000)
    DeclActor(21300,   0,       4294962796, 1000,    21300,   1200,    4294962796, 0x007C, 0,  39, 0x0000)
    DeclActor(23750,   0,       4294960696, 1000,    23750,   1200,    4294960696, 0x007C, 0,  40, 0x0000)
    DeclActor(23750,   0,       4294952596, 1000,    23750,   1200,    4294952596, 0x007C, 0,  41, 0x0000)
    DeclActor(23750,   0,       4294949696, 1000,    23750,   1200,    4294949696, 0x007C, 0,  42, 0x0000)
    DeclActor(18500,   4000,    11800,   1000,    18500,   5200,    11800,   0x007C, 0,  43, 0x0000)
    DeclActor(21500,   4000,    11800,   1000,    21450,   5200,    11800,   0x007C, 0,  44, 0x0000)
    DeclActor(26400,   4000,    11800,   1000,    26400,   5200,    11800,   0x007C, 0,  45, 0x0000)
    DeclActor(29400,   4000,    11800,   1000,    29400,   5200,    11800,   0x007C, 0,  46, 0x0000)
    DeclActor(31800,   4000,    9200,    1000,    31750,   5200,    9200,    0x007C, 0,  47, 0x0000)
    DeclActor(31800,   4000,    6450,    1000,    31800,   5200,    6450,    0x007C, 0,  48, 0x0000)
    DeclActor(31800,   4000,    1440,    1000,    31800,   5200,    1440,    0x007C, 0,  49, 0x0000)
    DeclActor(31750,   4000,    4294965646, 1000,    31750,   5200,    4294965646, 0x007C, 0,  50, 0x0000)
    DeclActor(31750,   4000,    4294960606, 1000,    31750,   5200,    4294960606, 0x007C, 0,  51, 0x0000)
    DeclActor(21500,   0,       4294948796, 1000,    21500,   1200,    4294948796, 0x007C, 0,  52, 0x0000)
    DeclActor(18500,   0,       4294948796, 1000,    18500,   1200,    4294948796, 0x007C, 0,  53, 0x0000)
    DeclActor(13500,   0,       4294948796, 1000,    13500,   1200,    4294948796, 0x007C, 0,  54, 0x0000)
    DeclActor(10500,   0,       4294948796, 1000,    10500,   1200,    4294948796, 0x007C, 0,  55, 0x0000)

    ChipFrameInfo(1508, 0)                                       # 0

    ScpFunction((
        "Function_0_5E4",          # 00, 0
        "Function_1_69C",          # 01, 1
        "Function_2_725",          # 02, 2
        "Function_3_C12",          # 03, 3
        "Function_4_D0F",          # 04, 4
        "Function_5_DC4",          # 05, 5
        "Function_6_1A9E",         # 06, 6
        "Function_7_27BC",         # 07, 7
        "Function_8_28FD",         # 08, 8
        "Function_9_2B84",         # 09, 9
        "Function_10_35C6",        # 0A, 10
        "Function_11_37C5",        # 0B, 11
        "Function_12_3DFE",        # 0C, 12
        "Function_13_3E60",        # 0D, 13
        "Function_14_3F95",        # 0E, 14
        "Function_15_5498",        # 0F, 15
        "Function_16_5587",        # 10, 16
        "Function_17_57BF",        # 11, 17
        "Function_18_593B",        # 12, 18
        "Function_19_59EC",        # 13, 19
        "Function_20_5B64",        # 14, 20
        "Function_21_5EC4",        # 15, 21
        "Function_22_5F87",        # 16, 22
        "Function_23_5FE4",        # 17, 23
        "Function_24_63D1",        # 18, 24
        "Function_25_67B3",        # 19, 25
        "Function_26_6BD7",        # 1A, 26
        "Function_27_76D9",        # 1B, 27
        "Function_28_7AC9",        # 1C, 28
        "Function_29_7B25",        # 1D, 29
        "Function_30_A6EE",        # 1E, 30
        "Function_31_B5A0",        # 1F, 31
        "Function_32_B6AC",        # 20, 32
        "Function_33_B93D",        # 21, 33
        "Function_34_C084",        # 22, 34
        "Function_35_CA7A",        # 23, 35
        "Function_36_CF70",        # 24, 36
        "Function_37_D047",        # 25, 37
        "Function_38_D0CE",        # 26, 38
        "Function_39_D157",        # 27, 39
        "Function_40_D1DA",        # 28, 40
        "Function_41_D25D",        # 29, 41
        "Function_42_D309",        # 2A, 42
        "Function_43_D396",        # 2B, 43
        "Function_44_D78E",        # 2C, 44
        "Function_45_E066",        # 2D, 45
        "Function_46_E90A",        # 2E, 46
        "Function_47_EC26",        # 2F, 47
        "Function_48_F3BD",        # 30, 48
        "Function_49_F85C",        # 31, 49
        "Function_50_FD0A",        # 32, 50
        "Function_51_10114",       # 33, 51
        "Function_52_1092B",       # 34, 52
        "Function_53_109D7",       # 35, 53
        "Function_54_10AC9",       # 36, 54
        "Function_55_10BBB",       # 37, 55
    ))


    def Function_0_5E4(): pass

    label("Function_0_5E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_624"),
        (1, "loc_630"),
        (2, "loc_63C"),
        (3, "loc_648"),
        (4, "loc_654"),
        (5, "loc_660"),
        (6, "loc_66C"),
        (SWITCH_DEFAULT, "loc_678"),
    )


    label("loc_624")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_630")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_63C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_648")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_654")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_660")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_66C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_678")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_684")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_69B")

    Return()

    # Function_0_5E4 end

    def Function_1_69C(): pass

    label("Function_1_69C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_724")
    OP_95(0xFE, 29310, 4000, 9100, 1000, 0x0)
    OP_95(0xFE, 17140, 4000, 9100, 1000, 0x0)
    OP_95(0xFE, 17140, 4000, 6840, 1000, 0x0)
    OP_95(0xFE, 27790, 4000, 6840, 1000, 0x0)
    OP_95(0xFE, 27790, 4000, -9440, 1000, 0x0)
    OP_95(0xFE, 29310, 4000, -9440, 1000, 0x0)
    Jump("Function_1_69C")

    label("loc_724")

    Return()

    # Function_1_69C end

    def Function_2_725(): pass

    label("Function_2_725")

    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_774")
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    Jump("loc_C02")

    label("loc_774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7BE")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 30720, 4000, -9860, 90)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_C02")

    label("loc_7BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7EB")
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    Jump("loc_C02")

    label("loc_7EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_825")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_87B")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 30720, 4000, -9860, 90)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8B9")
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8F7")
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_95D")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 5000, 30, 8720, 90)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 30740, 4000, -7340, 90)
    Jump("loc_C02")

    label("loc_95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9E6")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 19380, 20, -9760, 225)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xC, 16430, 30, -9880, 135)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0x8, 7700, 150, 7980, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_9E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A40")
    SetChrFlags(0xA, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 30740, 4000, -7340, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2A")
    SetChrFlags(0xE, 0x10)

    label("loc_A2A")

    SetChrPos(0x9, 27020, 4019, -10540, 45)
    Jump("loc_C02")

    label("loc_A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A79")
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AA9")
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_B99")
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_B08")
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 13560, 0, -6140, 270)
    BeginChrThread(0xD, 0, 0, 0)
    Jump("loc_B6D")

    label("loc_B08")

    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xC, 13560, 30, -4990, 180)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 13560, 0, -6140, 0)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0x8, 7700, 150, 7980, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_B6D")

    Jump("loc_B83")

    label("loc_B72")

    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)

    label("loc_B83")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BD7")
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_C02")

    label("loc_BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C02")
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C11")
    ClearScenarioFlags(0x22, 0)
    Event(0, 34)

    label("loc_C11")

    Return()

    # Function_2_725 end

    def Function_3_C12(): pass

    label("Function_3_C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2B")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_C31")

    label("loc_C2B")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C7A")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB9")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_CB9")

    OP_65(0x16, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CCA")
    OP_66(0x16, 0x1)

    label("loc_CCA")

    OP_65(0x15, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CDB")
    OP_66(0x15, 0x1)

    label("loc_CDB")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CEC")
    OP_66(0x2, 0x1)

    label("loc_CEC")

    OP_65(0x14, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CFD")
    OP_66(0x14, 0x1)

    label("loc_CFD")

    OP_65(0x13, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D0E")
    OP_66(0x13, 0x1)

    label("loc_D0E")

    Return()

    # Function_3_C12 end

    def Function_4_D0F(): pass

    label("Function_4_D0F")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"One-minute cooking, sweets\" is available.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_DC0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Light popcorn\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_DC0")

    TalkEnd(0xFF)
    Return()

    # Function_4_D0F end

    def Function_5_DC4(): pass

    label("Function_5_DC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAA")

    ChrTalk(
        0xFE,
        (
            "Hello,\x01",
            "Welcome to the Crossbell City Library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Well, today as a user\x01",
            "As expected there are not many.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a big tree has also appeared,\x01",
            "People who refrain from going outside\x01",
            "Is not there a lot?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F31")

    label("loc_EAA")


    ChrTalk(
        0xFE,
        (
            "Today, users also\x01",
            "There are not many indeed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a librarian in the library,\x01",
            "To people who come to borrow\x01",
            "We will respond in good faith.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F31")

    Jump("loc_1A9A")

    label("loc_F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FCA")

    ChrTalk(
        0xFE,
        (
            "Previously, when a hunter attacked the city\x01",
            "I feel the same fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why is this ……\x01",
            "I am full of such unreasonable feelings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1088")

    ChrTalk(
        0xFE,
        (
            "\"Crossbell independent country\" … …\x01",
            "At last we can not go back to the place\x01",
            "I feel I've come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two major powers, following this declaration,\x01",
            "What kind of attitude will come out?\x01",
            "…… Honesty is full of anxiety … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_1088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1208")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1180")

    ChrTalk(
        0xFE,
        (
            "Night of raid, already finished work\x01",
            "I had left here … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This administrative district has police headquarters\x01",
            "In the center, really terrible\x01",
            "You seem to have been injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Another week has passed … …\x01",
            "The town was wrapped in flames\x01",
            "I can not forget that night.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1203")

    label("loc_1180")


    ChrTalk(
        0xFE,
        (
            "Another week has passed … …\x01",
            "The town was wrapped in flames\x01",
            "I can not forget that night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To this independent advocate\x01",
            "Is it a warning ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1203")

    Jump("loc_1A9A")

    label("loc_1208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1286")

    ChrTalk(
        0xFE,
        (
            "It is natural, but …\x01",
            "The police headquarters are in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The matter of Mainz, safely\x01",
            "I hope to solve it … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_1286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_139C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1351")

    ChrTalk(
        0xFE,
        (
            "Today is the citizen's hall\x01",
            "Citizen forum\x01",
            "It seems to be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come and stay at national independence ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Residents' voting is approaching,\x01",
            "It is time to give your opinion\x01",
            "You have to consolidate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1397")

    label("loc_1351")


    ChrTalk(
        0xFE,
        (
            "Come and stay at national independence ……\x01",
            "It is time to give your opinion\x01",
            "You have to consolidate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1397")

    Jump("loc_1A9A")

    label("loc_139C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_14CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1444")

    ChrTalk(
        0xFE,
        (
            "Well, because this book is an academic note\x01",
            "Return it to that shelf, … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, in the gap of the bookshelf\x01",
            "How to return a book, why\x01",
            "I wonder if this is fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C5")

    label("loc_1444")


    ChrTalk(
        0xFE,
        (
            "To put the book back on the bookshelf\x01",
            "It looks a bit like a puzzle, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just exactly without gaps\x01",
            "When it was stored,\x01",
            "It is kind of a touching thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C5")

    Jump("loc_1A9A")

    label("loc_14CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_161F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1599")

    ChrTalk(
        0xFE,
        (
            "Hello.\x01",
            "Welcome to the Crossbell City Library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even books that I am currently lending\x01",
            "If you say,\x01",
            "I can do it even if I make a reservation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even I, the director, anytime\x01",
            "Please do not hesitate to consult us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_161A")

    label("loc_1599")


    ChrTalk(
        0xFE,
        (
            "Even books that I am currently lending\x01",
            "If you say,\x01",
            "I can do it even if I make a reservation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even I, the director, anytime\x01",
            "Please do not hesitate to consult us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161A")

    Jump("loc_1A9A")

    label("loc_161F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_162D")
    Jump("loc_1A9A")

    label("loc_162D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16CF")

    ChrTalk(
        0xFE,
        (
            "The leaders of each country,\x01",
            "Last night was Michelin's\x01",
            "You heard that you stayed at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, you surely\x01",
            "Delicious and tasty meals\x01",
            "I guess it was made a calling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_16CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1768")

    ChrTalk(
        0xFE,
        (
            "Thanks to the Commerce Council\x01",
            "Today, it seems like a festival somehow\x01",
            "The mood is drifting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, whatever you do not do\x01",
            "I feel a little fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_1768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_18DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184C")

    ChrTalk(
        0xFE,
        (
            "A lot of ancient documents in the tower of Hoshi\x01",
            "Listening to the story that there was\x01",
            "The director is overjoyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, here\x01",
            "Carry all out\x01",
            "It seems I am going to … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Space-like in my underground archive\x01",
            "Did you have room for it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18D7")

    label("loc_184C")


    ChrTalk(
        0xFE,
        (
            "Apparently the director is an old document\x01",
            "Carry out everything here\x01",
            "It seems I am going to … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Space-like in my underground archive\x01",
            "Did you have room for it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D7")

    Jump("loc_1A9A")

    label("loc_18DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_197F")

    ChrTalk(
        0xFE,
        (
            "Nielsenさんは、\x01",
            "As a free reporter you can see the continent\x01",
            "He seems to be busy and flying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything This time around for the first time in about three years\x01",
            "Even my homecool was pleased.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_197F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A1D")

    ChrTalk(
        0xFE,
        (
            "When the director, today\x01",
            "Nielsenさんが来るからって\x01",
            "I am fidgeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, well\x01",
            "Nielsenさんとお話するのが\x01",
            "You seem to like it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_1A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1A9A")

    ChrTalk(
        0xFE,
        (
            "Hello.\x01",
            "Welcome to the Crossbell City Library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have something you are looking for\x01",
            "Please call out anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9A")

    TalkEnd(0xFE)
    Return()

    # Function_5_DC4 end

    def Function_6_1A9E(): pass

    label("Function_6_1A9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1AAF")
    Jump("loc_27B8")

    label("loc_1AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BCA")

    ChrTalk(
        0xFE,
        (
            "A part is still a lot … …\x01",
            "Finally the reconstruction of the city\x01",
            "You seem to have calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fortunately, there were no damage to the station or airport\x01",
            "Because I did not have it,\x01",
            "I can be there ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Raids aimed at transportation\x01",
            "You can think enough.\x01",
            "…… That's frightening when I think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C44")

    label("loc_1BCA")


    ChrTalk(
        0xFE,
        (
            "To study the history of Crossbell\x01",
            "This library is essential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's time for Leman's laboratory\x01",
            "Canned food may be good, though ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C44")

    Jump("loc_27B8")

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFD")

    ChrTalk(
        0xFE,
        (
            "Raid incident at Mainz … …\x01",
            "It is also occupying it now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The work of the empire? Or the Republic?\x01",
            "Clearly, either line\x01",
            "It is thought well enough ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D7F")

    label("loc_1CFD")


    ChrTalk(
        0xFE,
        (
            "Whether you are an empire or a republic\x01",
            "The situation in Mainz is a good attack material.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Clearly, either line\x01",
            "It is thought well enough ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7F")

    Jump("loc_27B8")

    label("loc_1D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E88")

    ChrTalk(
        0xFE,
        (
            "Recently in various parts of Crossbell,\x01",
            "It is different from the so-called ordinary demon\x01",
            "It seems that a monster has appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything, painted in the church scripture\x01",
            "I caught something like a demon\x01",
            "There seems to be some rumors like that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To this crossbell,\x01",
            "I wonder what's going on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F40")

    label("loc_1E88")


    ChrTalk(
        0xFE,
        (
            "Knowledge of the ancient Zemrian civilization\x01",
            "If it remains in the present age\x01",
            "I guess everything will be understood, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fu, I guess he is a bad guy.\x01",
            "In a place I did not do anything,\x01",
            "Even though there is nothing to see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F40")

    Jump("loc_27B8")

    label("loc_1F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2003")

    ChrTalk(
        0xFE,
        (
            "Hmm, next is the independence of the ancient world\x01",
            "It is also possible to summarize papers in a theme\x01",
            "It might be funny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The commonalities found there,\x01",
            "To uncover something other history\x01",
            "You may be connected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B8")

    label("loc_2003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_21CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F8")

    ChrTalk(
        0xFE,
        "Proposal of national independence, or …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "History of Crossbell until the Middle Ages\x01",
            "Looking back …… Such a story in the past\x01",
            "Not that it was not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can see modern circumstances,\x01",
            "That it was successful\x01",
            "Once in a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21CA")

    label("loc_20F8")


    ChrTalk(
        0xFE,
        (
            "However, even though it has been\x01",
            "Because it was useless, it is useless this time ……\x01",
            "It is today's world that I can not say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This proposition will rock the entire continent\x01",
            "If it develops to the movement ……\x01",
            "Or maybe it's going to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21CA")

    Jump("loc_27B8")

    label("loc_21CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_21F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EA")
    Call(0, 20)
    Jump("loc_21ED")

    label("loc_21EA")

    Call(0, 21)

    label("loc_21ED")

    Jump("loc_27B8")

    label("loc_21F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_236D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D7")

    ChrTalk(
        0xFE,
        (
            "Because this child was fishing a book,\x01",
            "I was helping to find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, but I'm impressed.\x01",
            "Although it is small like this\x01",
            "You are interested in me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For those studying history\x01",
            "There is nothing I'm happy about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2368")

    label("loc_22D7")


    ChrTalk(
        0xFE,
        (
            "Well, but I'm impressed.\x01",
            "Although it is small like this\x01",
            "You are interested in me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For those studying history\x01",
            "There is nothing I'm happy about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2368")

    Jump("loc_27B8")

    label("loc_236D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2525")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_239A")
    Call(0, 7)
    Jump("loc_2520")

    label("loc_239A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247E")

    ChrTalk(
        0xFE,
        "Western Zemria Trade Council,?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this crossbell\x01",
            "An international conference on this scale\x01",
            "How long have you been able to open for the first time in a year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, this 3 day event\x01",
            "In the later world as \"the history of the continent\"\x01",
            "There will be no doubt that it will be transmitted.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2520")

    label("loc_247E")


    ChrTalk(
        0xFE,
        (
            "This three day event,\x01",
            "In the later world as \"the history of the continent\"\x01",
            "There is no doubt that it will be transmitted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One scene of such history\x01",
            "In this way you can see something\x01",
            "I am obediently pleased.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2520")

    Jump("loc_27B8")

    label("loc_2525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_254A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2542")
    Call(0, 7)
    Jump("loc_2545")

    label("loc_2542")

    Call(0, 8)

    label("loc_2545")

    Jump("loc_27B8")

    label("loc_254A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_25F3")

    ChrTalk(
        0xFE,
        (
            "I do not know what it is on rainy days,\x01",
            "The research is really going well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When listening to rain sounds, I will take extra things\x01",
            "I do not need to think about it … …\x01",
            "You can concentrate anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B8")

    label("loc_25F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_27B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2711")

    ChrTalk(
        0xFE,
        (
            "I am in Leman Autonomous Region\x01",
            "It is a student at a state university.\x01",
            "So he's studying history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way I have been told twice\x01",
            "I tried to obtain my doctorate but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The papers were not accepted for the first time and they were completely defeated.\x01",
            "The second time it can not be submitted within the deadline and it is battleless.\x01",
            "…… Oh, well, I'm strikingly losing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27B8")

    label("loc_2711")


    ChrTalk(
        0xFE,
        (
            "Now for the opportunity of next year,\x01",
            "I am reworking my paper again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Even if you do not take a Ph.D.\x01",
            "I can finish the university itself.\x01",
            "It is no longer noisy once this is done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B8")

    TalkEnd(0xFE)
    Return()

    # Function_6_1A9E end

    def Function_7_27BC(): pass

    label("Function_7_27BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2881")

    ChrTalk(
        0xFE,
        (
            "Investigation of the tower of Hoshi, you guys\x01",
            "He took charge of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Too many books are going to disappear suddenly,\x01",
            "I do not care what it means ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, even with a single volume\x01",
            "It was good that the book was left.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28FC")

    label("loc_2881")


    ChrTalk(
        0xFE,
        (
            "Anyway, even with a single volume\x01",
            "It was good that the book was left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Milesさんに言って\x01",
            "I will let you investigate again later\x01",
            "I'm gonna get it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28FC")

    Return()

    # Function_7_27BC end

    def Function_8_28FD(): pass

    label("Function_8_28FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF5")

    ChrTalk(
        0xFE,
        (
            "Apparently to the tower of Hoshi\x01",
            "A large number of ancient documents\x01",
            "It was left behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, the state of the book is not so much\x01",
            "It seems not good, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, anyway\x01",
            "Such valuable materials have so far\x01",
            "I have never been left untouched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a person exploring history,\x01",
            "I have kept management under control\x01",
            "I feel strong indignation in the guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(… … it is exactly as you say.\x01",
            "It is a painful story of the ear … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Oh well.\x01",
            "However, regarding the management of the tower\x01",
            "It is all responsibility of the former commander. )\x02\x03",
            "#00302F(Even though we are sick\x01",
            "Why do not you think? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B83")

    label("loc_2AF5")


    ChrTalk(
        0xFE,
        (
            "Apparently to the tower of Hoshi\x01",
            "A large number of ancient documents\x01",
            "It was left behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, the state of the book is not so much\x01",
            "It seems not good, but …\x01",
            "Anyway, I'd love to see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B83")

    Return()

    # Function_8_28FD end

    def Function_9_2B84(): pass

    label("Function_9_2B84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C23")

    ChrTalk(
        0xFE,
        (
            "あの事件でAbbyが\x01",
            "Because I feel uneasy, even a fun book\x01",
            "I thought about reading it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all the classic\x01",
            "\"Mark and Deep Forest Witch\"\x01",
            "Wonder if it is good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_2C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2C31")
    Jump("loc_35C2")

    label("loc_2C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D37")

    ChrTalk(
        0xFE,
        (
            "Mr. Dieter's speech ……\x01",
            "It was really shocking content.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I thought,\x01",
            "The powerful battle of the two major powers\x01",
            "I was fine …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To protect the future of these children,\x01",
            "As it stands this way independent claim\x01",
            "Is there no choice but to continue …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DE3")

    label("loc_2D37")


    ChrTalk(
        0xFE,
        (
            "Although I thought,\x01",
            "The powerful battle of the two major powers\x01",
            "I was fine …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To protect the future of these children,\x01",
            "As it stands this way independent claim\x01",
            "Is there no choice but to continue …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE3")

    Jump("loc_35C2")

    label("loc_2DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DF6")
    Jump("loc_35C2")

    label("loc_2DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ECF")

    ChrTalk(
        0xFE,
        (
            "A terrible affair in the mining town\x01",
            "It seems to be happening ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the town, that is what\x01",
            "Abbyくらいの子供も\x01",
            "I think there are many people … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, as soon as possible, you guys\x01",
            "I want you to release safely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F50")

    label("loc_2ECF")


    ChrTalk(
        0xFE,
        (
            "To the town, that is what\x01",
            "Abbyくらいの子供も\x01",
            "I think there are many people … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, as soon as possible, you guys\x01",
            "I want you to release safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F50")

    Jump("loc_35C2")

    label("loc_2F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F7B")

    ChrTalk(
        0xFE,
        "Well, that is …\x02",
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_2F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2FDA")

    ChrTalk(
        0xFE,
        (
            "Oh, mommy too\x01",
            "I did not notice, but it is true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did you even go shopping?\x02",
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_2FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3061")

    ChrTalk(
        0xFE,
        (
            "今日もKeyaちゃんは熱心に\x01",
            "You seem to be doing research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ふふ、Abbyには\x01",
            "Enviously it is enviable\x01",
            "It looks like it can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_3061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3141")

    ChrTalk(
        0xFE,
        (
            "うちのAbbyも来年にもなれば、\x01",
            "I am going to be able to attend Sunday school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because this girl likes books,\x01",
            "I wonder if you can study well\x01",
            "I think ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huhu, is not it stupid to think so?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31CF")

    label("loc_3141")


    ChrTalk(
        0xFE,
        (
            "Abbyには、とにかく元気よく\x01",
            "And I want you to grow straight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I asked this child for something,\x01",
            "There is no other place to stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CF")

    Jump("loc_35C2")

    label("loc_31D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328A")

    ChrTalk(
        0xFE,
        "ふふ、Abbyはお利口さんね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, then.\x01",
            "Today we are going down on our way home.\x01",
            "I'll buy ice cream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "really! Is it?\x01",
            "I did it, I am happy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32D3")

    label("loc_328A")


    ChrTalk(
        0xFE,
        (
            "Huhu, that is it.\x01",
            "What is the taste?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm, melon taste!\x02",
    )

    CloseMessageWindow()

    label("loc_32D3")

    Jump("loc_35C2")

    label("loc_32D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3382")

    ChrTalk(
        0xFE,
        (
            "ふふ、Abbyったら\x01",
            "I got tired from the sightseeing of the unveiling ceremony,\x01",
            "It seems I have become Onemu-san.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Have such a safe face ……\x01",
            "It's really cute.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33CE")

    label("loc_3382")


    ChrTalk(
        0xFE,
        (
            "ふふ、Abbyったら\x01",
            "Have such a safe face ……\x01",
            "It's really cute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33CE")

    Jump("loc_35C2")

    label("loc_33D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3454")

    ChrTalk(
        0xFE,
        (
            "This library is really quiet.\x01",
            "It is comfortable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Besides, the smell unique to the old book\x01",
            "What a feeling\x01",
            "It calms down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_3454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3541")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350B")

    ChrTalk(
        0xFE,
        "And the empty goddess#8REarth#The shedding tears ……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(18, 0, 70, 0)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "I descend to the earth,\x01",
            "It soaked me in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "People just look at the sight ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_353C")

    label("loc_350B")


    ChrTalk(
        0xFE,
        (
            "People just look at the sight ……\x01",
            "And …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_353C")

    Jump("loc_35C2")

    label("loc_3541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_35C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355C")
    Call(0, 10)
    Jump("loc_35C2")

    label("loc_355C")


    ChrTalk(
        0xFE,
        (
            "うちのAbbyは、\x01",
            "Keyaちゃんのことが\x01",
            "I really love it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huhu, of course I am, too.\x02",
    )

    CloseMessageWindow()

    label("loc_35C2")

    TalkEnd(0xFE)
    Return()

    # Function_9_2B84 end

    def Function_10_35C6(): pass

    label("Function_10_35C6")


    ChrTalk(
        0xA,
        "Oh, everyone … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "あっ、Keyaおねーちゃんの\x01",
            "Oya-chan and Oya-chan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hey, today\x01",
            "Keyaおねえちゃんは来ないのー？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FOh, sorry.\x01",
            "I am going to Sunday school today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FちゃんとKeyaちゃんにも伝えておくから\x01",
            "Can you endure for today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yes, I understand!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well then,\x01",
            "Keyaおねーちゃんに\x01",
            "Nice to meet you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHehe, Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FIndeed, even in such a place\x01",
            "It seems to be a popular person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FYes, drift\x01",
            "Keyaちゃんって感じだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 0)
    Return()

    # Function_10_35C6 end

    def Function_11_37C5(): pass

    label("Function_11_37C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3801")

    ChrTalk(
        0xFE,
        (
            "It's exciting!\x01",
            "Mommy, read it soon ~!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_380F")
    Jump("loc_3DF6")

    label("loc_380F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3865")

    ChrTalk(
        0xFE,
        (
            "Hey, Mommy.\x01",
            "Everyone says something outside,\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3873")
    Jump("loc_3DF6")

    label("loc_3873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_38C7")

    ChrTalk(
        0xFE,
        (
            "Hey, Mama …\x01",
            "The face of the face is bad,\x01",
            "What's wrong …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_38C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3908")

    ChrTalk(
        0xFE,
        (
            "ねえHey, Mommy.\x01",
            "What kind of imitation is this word?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C5")

    ChrTalk(
        0xFE,
        (
            "あれ、Keyaおねえちゃん、\x01",
            "Before I knew it, I got home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if you notice it\x01",
            "I did bye bye ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it's good to see you again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A24")

    label("loc_39C5")


    ChrTalk(
        0xFE,
        (
            "Well, if you notice it\x01",
            "I did bye bye ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it's good to see you again.\x02",
    )

    CloseMessageWindow()

    label("loc_3A24")

    Jump("loc_3DF6")

    label("loc_3A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AA6")

    ChrTalk(
        0xFE,
        (
            "Keyaおねーちゃん、\x01",
            "Alone\x01",
            "It is amazing to read your book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I also\x01",
            "I have to study.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B5B")

    ChrTalk(
        0xFE,
        (
            "I will come soon\x01",
            "Keyaおねーちゃんと同じように\x01",
            "You can go to Higuchi prefecture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I go to Hatoyo\x01",
            "It would be nice to meet your sister.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BE5")

    ChrTalk(
        0xFE,
        (
            "あのね、Keyaおねーちゃん、\x01",
            "Today I have something to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, sister's\x01",
            "I do not have to play jama.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C60")

    ChrTalk(
        0xFE,
        "…… Hmm … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, Mama …\x01",
            "People were amazing and amazing ……\x01",
            "…… Mumbo … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C78")

    label("loc_3C60")


    ChrTalk(
        0xFE,
        "…… ー ー ー ー ー ………\x02",
    )

    CloseMessageWindow()

    label("loc_3C78")

    Jump("loc_3DF6")

    label("loc_3C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D30")

    ChrTalk(
        0xFE,
        (
            "Mom, from your book\x01",
            "I say that it smells nice … …\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because mommy is better\x01",
            "Keep it all along forever\x01",
            "It smells nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D5B")

    label("loc_3D30")


    ChrTalk(
        0xFE,
        (
            "From your book, it's nice scent\x01",
            "Should I?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D5B")

    Jump("loc_3DF6")

    label("loc_3D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D90")

    ChrTalk(
        0xFE,
        "Doki Doki, so is it ~?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3DF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DAB")
    Call(0, 10)
    Jump("loc_3DF6")

    label("loc_3DAB")


    ChrTalk(
        0xFE,
        (
            "Keyaおねーちゃんに\x01",
            "Nice to meet you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Because I am waiting here.\x02",
    )

    CloseMessageWindow()

    label("loc_3DF6")

    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_37C5 end

    def Function_12_3DFE(): pass

    label("Function_12_3DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E0F")
    Call(0, 14)
    Jump("loc_3E5F")

    label("loc_3E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E20")
    Call(0, 13)
    Jump("loc_3E5F")

    label("loc_3E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E31")
    Call(0, 14)
    Jump("loc_3E5F")

    label("loc_3E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_3E5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E54")
    Call(0, 13)
    Jump("loc_3E57")

    label("loc_3E54")

    Call(0, 14)

    label("loc_3E57")

    Jump("loc_3E5F")

    label("loc_3E5C")

    Call(0, 14)

    label("loc_3E5F")

    Return()

    # Function_12_3DFE end

    def Function_13_3E60(): pass

    label("Function_13_3E60")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F15")

    ChrTalk(
        0x8,
        (
            "The directors, today is the tower of Hoshi\x01",
            "Find the ancient documents that were found\x01",
            "It seems to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, just like a boy\x01",
            "Because I make a lively look\x01",
            "It seems pretty lovely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F91")

    label("loc_3F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_3F91")

    ChrTalk(
        0x8,
        (
            "When the director was a director,\x01",
            "またNielsenさんと\x01",
            "You seem to be talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Already break time\x01",
            "I have finished ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F91")

    TalkEnd(0x8)
    Return()

    # Function_13_3E60 end

    def Function_14_3F95(): pass

    label("Function_14_3F95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 7)), scpexpr(EXPR_END)), "loc_3FC8")
    Call(0, 32)
    Return()

    label("loc_3FC8")

    Call(0, 30)
    Return()

    label("loc_3FCC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_416E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CB")

    ChrTalk(
        0xC,
        (
            "The town has its usual aspect as usual\x01",
            "It seems I regained it ……\x01",
            "It seems that there is also unease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Such an eerie big tree appeared\x01",
            "I think that it is unavoidable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For the citizens for a while at home\x01",
            "Even with slow reading,\x01",
            "I want you to calm your mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4169")

    label("loc_40CB")


    ChrTalk(
        0xC,
        (
            "The town has its usual aspect as usual\x01",
            "It seems I regained it ……\x01",
            "It seems that there is also unease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For the citizens for a while at home\x01",
            "Even with slow reading,\x01",
            "I want you to calm your mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4169")

    Jump("loc_5494")

    label("loc_416E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4423")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_437A")
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Ooo, Lloyd … …\x01",
            "It was safe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYou are the uncle … ….\x01",
            "I was relieved to see a face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, it's totally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "When Lloyd was wanted\x01",
            "I was surprised when I heard it … …\x01",
            "I believe it is a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "Uncle or Mister……\x01",
            "Thank you.\x02\x03",
            "#00001FThere are various things I want to talk about,\x01",
            "I do not have time anyway now.\x02\x03",
            "First of all, until the state of the outside calms down\x01",
            "Please do not leave the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh … ok.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Lloyd, you guys\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 4)
    Jump("loc_441E")

    label("loc_437A")


    ChrTalk(
        0xC,
        (
            "Actually, I came to the library exactly\x01",
            "Nielsenさんも\x01",
            "You got trapped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In a completely ridiculous situation\x01",
            "It is what became … … Lloyd guys as well\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_441E")

    Jump("loc_5494")

    label("loc_4423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_465F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45CE")

    ChrTalk(
        0xC,
        (
            "B, Lloyd.\x01",
            "Did you hear the speech of Mayor Dieter.\x01",
            "And defense forces ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah, we also\x01",
            "It's just a surprise situation.\x01",
            "I am researching various things now.\x02\x03",
            "Anyway, my uncle.\x01",
            "Now I feel calm and progress\x01",
            "I want you to be watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I am worried about various things,\x01",
            "First of all, I feel uneasy\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Lloyd guys are doing their best, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYes, thank you, old man.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_465A")

    label("loc_45CE")


    ChrTalk(
        0xC,
        (
            "I am worried about various things … ….\x01",
            "First of all it can not be calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But, why is Mr. Dieter\x01",
            "I guess I got into such a tough way … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_465A")

    Jump("loc_5494")

    label("loc_465F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4756")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F4")

    ChrTalk(
        0xC,
        (
            "City and the Chamber of Commerce organized\x01",
            "Charity event\x01",
            "It seems to be quite exciting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm, I have to donate later.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4751")

    label("loc_46F4")


    ChrTalk(
        0xC,
        (
            "Anything, human beings,\x01",
            "The spirit of mutual respect is vital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm, I have to donate later.\x02",
    )

    CloseMessageWindow()

    label("loc_4751")

    Jump("loc_5494")

    label("loc_4756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_47F6")

    ChrTalk(
        0xC,
        (
            "I do not know who the armed group is … …\x01",
            "It is quite stupid at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I tried to rule people with violence ……\x01",
            "I am wrong and I can not forgive you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5494")

    label("loc_47F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_486A")

    ChrTalk(
        0xC,
        "Hmm, it's raining outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To prevent moisture from entering,\x01",
            "Today I will enter an underground library\x01",
            "Let's stop it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5494")

    label("loc_486A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_48DB")

    ChrTalk(
        0xC,
        (
            "Mother's lunch box, also today\x01",
            "I was doing a good job as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Thanks to that, I will be able to work hard from the afternoon as well.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5494")

    label("loc_48DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_495B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F6")
    Call(0, 15)
    Jump("loc_4956")

    label("loc_48F6")


    ChrTalk(
        0xC,
        (
            "Well, what I've done\x01",
            "You do not forget your wife's bento.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But my mother\x01",
            "It was saved because it delivered it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4956")

    Jump("loc_5494")

    label("loc_495B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_497E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4976")
    Call(0, 20)
    Jump("loc_4979")

    label("loc_4976")

    Call(0, 21)

    label("loc_4979")

    Jump("loc_5494")

    label("loc_497E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_49B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_49A4")
    Call(0, 18)
    Jump("loc_49B0")

    label("loc_49A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_49B0")
    Call(0, 17)

    label("loc_49B0")

    Jump("loc_4B4F")

    label("loc_49B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A9F")

    ChrTalk(
        0xC,
        "いや、Keya君は実に勉強熱心だね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At home, one at a time\x01",
            "You can only lend up to three volumes\x01",
            "I'm stoked … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, only for excellent users\x01",
            "Even in a system that can increase the number of loans\x01",
            "I guess I'll seriously consider this time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B4F")

    label("loc_4A9F")


    ChrTalk(
        0xC,
        (
            "At home, one at a time\x01",
            "You can only lend up to three volumes\x01",
            "I'm stoked … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, only for excellent users\x01",
            "Even in a system that can increase the number of loans\x01",
            "I guess I'll seriously consider this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B4F")

    Jump("loc_5494")

    label("loc_4B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4D88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4B8B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B7A")
    Call(0, 18)
    Jump("loc_4B86")

    label("loc_4B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_4B86")
    Call(0, 17)

    label("loc_4B86")

    Jump("loc_4D83")

    label("loc_4B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD3")

    ChrTalk(
        0xC,
        (
            "Hmm, the VIP of each country\x01",
            "It is a swaying face for running pedestrians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Especially, what I want to pay attention to\x01",
            "After all it is Olivert Prince.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Beginning with Libert's contribution to the accident,\x01",
            "That \"Arseille\"\x01",
            "Returning to the Imperial City using … etc …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In a different meaning from Chancellor\x01",
            "Because it will surprise the world,\x01",
            "I can not keep an eye on every move.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D83")

    label("loc_4CD3")


    ChrTalk(
        0xC,
        (
            "Among the nationally famous VIPs\x01",
            "What I want to pay attention to\x01",
            "After all it is Olivert Prince.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In a different meaning from Chancellor\x01",
            "Because it will surprise the world,\x01",
            "I can not keep an eye on every move.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D83")

    Jump("loc_5494")

    label("loc_4D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4DB6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4DA5")
    Call(0, 18)
    Jump("loc_4DB1")

    label("loc_4DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_4DB1")
    Call(0, 17)

    label("loc_4DB1")

    Jump("loc_5494")

    label("loc_4DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_4F06")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4E8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDD")
    Call(0, 16)
    Jump("loc_4E85")

    label("loc_4DDD")


    ChrTalk(
        0xC,
        (
            "He took the Fürlitza Prize\x01",
            "After first raising its name,\x01",
            "Is it over ten years already …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "When will you leave autonomous state again\x01",
            "I do not know,\x01",
            "I'm really happy for coming back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E85")

    Jump("loc_4F01")

    label("loc_4E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_4EF3")

    ChrTalk(
        0xC,
        (
            "ふむ、Nielsenさんが来ると\x01",
            "I will not stop talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well work, and … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F01")

    label("loc_4EF3")

    Call(0, 26)
    TalkEnd(0xC)
    OP_93(0xC, 0x10E, 0x0)
    Return()

    label("loc_4F01")

    Jump("loc_5494")

    label("loc_4F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_516A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F7")

    ChrTalk(
        0xC,
        (
            "Today, from now on, special\x01",
            "The customer will show his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Huhu, I'm looking forward to talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FA special customer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "ああ、Nielsenさんと言って\x01",
            "He is active internationally\x01",
            "He is a journalist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Maybe, already a while\x01",
            "I think it will come ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you like, Lloyd's guys too\x01",
            "I'll introduce you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHe is active internationally\x01",
            "A journalist ……\x01",
            "It certainly might be interesting.\x02\x03",
            "#00002FYeah, if I have free time then\x01",
            "I will drop in later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x133, 2)
    SetScenarioFlags(0x0, 4)
    Jump("loc_5165")

    label("loc_50F7")


    ChrTalk(
        0xC,
        (
            "Nielsenさんは、\x01",
            "I should be back in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you like, Lloyd's guys too\x01",
            "I'll introduce you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5165")

    Jump("loc_5494")

    label("loc_516A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5422")

    ChrTalk(
        0xC,
        "Oh, is not it Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To be with friends,\x01",
            "Finally at the Special Affairs Division\x01",
            "Is the activity resumed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, thanks.\x02\x03",
            "If there is something for the uncle,\x01",
            "Also we can always\x01",
            "I am glad if you rely on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, I will ask you at that time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even so, as before\x01",
            "You seem to have become more dependable.\x01",
            "I am also really happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, such a thing ….\x01",
            "It is still going from now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, I personally have more\x01",
            "I think that it is okay to stretch my heart.\x01",
            "But that is with Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I support you in the future.\x01",
            "Even for the house, any time\x01",
            "Do not hesitate to come and visit me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYup.\x01",
            "Thank you, uncle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F(Cecil's father ……\x01",
            "It is a very warm person. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x133, 5)
    Jump("loc_5494")

    label("loc_5422")


    ChrTalk(
        0xC,
        (
            "You guys at the Special Affairs Support Division\x01",
            "I support you anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even for the house, any time\x01",
            "Do not hesitate to come and visit me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5494")

    TalkEnd(0xC)
    Return()

    # Function_14_3F95 end

    def Function_15_5498(): pass

    label("Function_15_5498")


    ChrTalk(
        0xC,
        (
            "What a mother.\x01",
            "Have you ever had any errands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Oh no, it is rude to say what.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hehe, forgetting your lunch box\x01",
            "You have come to the delivery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh! Is it?\x01",
            "That did not notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sorry about that.\x01",
            "It was saved because it delivered it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    Return()

    # Function_15_5498 end

    def Function_16_5587(): pass

    label("Function_16_5587")


    ChrTalk(
        0xC,
        (
            "Hmm, Lloyd.\x01",
            "Apparently the story ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Did you have a meaningful story?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, well.\x01",
            "I studied variously.\x02\x03",
            "#00000FBy the way, the uncle\x01",
            "Nielsenさんのことを\x01",
            "Did you know from before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "ああ、Nielsenさんは\x01",
            "I originally came from Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He told Crosbell Corp.\x01",
            "Since I was enrolled\x01",
            "I have been making friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, well with Guy\x01",
            "It seems that the relationship was deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FOh, it looks like that.\x02\x03",
            "#00003F(We and Mr. Grace's\x01",
            "I wonder if it was close to a relationship. )\x02\x03",
            "(… of course Nori something\x01",
            "I wonder why it is different at all. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 6)
    Return()

    # Function_16_5587 end

    def Function_17_57BF(): pass

    label("Function_17_57BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58B9")

    ChrTalk(
        0xC,
        (
            "Ursula is on the edge of the intermittent road\x01",
            "I will ask you to investigate \"Tower of Hoshi\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There are many old documents in that place\x01",
            "She seems to have been left untreated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "With your eyes, to collect books\x01",
            "How much will it cost?\x01",
            "Please judge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well then, I have asked for you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_593A")

    label("loc_58B9")


    ChrTalk(
        0xC,
        (
            "There is a tower of Hoshi,\x01",
            "On the way of the Ursula interchange in the south\x01",
            "I have just passed through the forest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Investigation of the old document that it is in the tower,\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_593A")

    Return()

    # Function_17_57BF end

    def Function_18_593B(): pass

    label("Function_18_593B")


    ChrTalk(
        0xC,
        (
            "Collect all the books of the tower\x01",
            "I could not do it\x01",
            "Sorry to the contrary ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even with this magazine alone\x01",
            "It's pretty valuable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thank you, Lloyd - kun.\x01",
            "If there is something again, I will ask you.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_18_593B end

    def Function_19_59EC(): pass

    label("Function_19_59EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_5A0C")
    Call(0, 28)
    Return()

    label("loc_5A0C")

    Call(0, 26)
    Return()

    label("loc_5A10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5AAC")

    ChrTalk(
        0xFE,
        (
            "Sudden martial law ……\x01",
            "This is being chased by the president\x01",
            "It can be said as evidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tyranny does not last long … …\x01",
            "This is a thing of the world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B60")

    label("loc_5AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5B42")

    ChrTalk(
        0xFE,
        "…………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Continental Strongest Hunting Corps ……\x01",
            "It is what is behind it ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Why do you decide it as an empire?\x01",
            "Is it easy……)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B60")

    label("loc_5B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B5D")
    Call(0, 20)
    Jump("loc_5B60")

    label("loc_5B5D")

    Call(0, 21)

    label("loc_5B60")

    TalkEnd(0xFE)
    Return()

    # Function_19_59EC end

    def Function_20_5B64(): pass

    label("Function_20_5B64")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "Yes, this magical book\x01",
            "Ancient artifacts in the Middle Ages#8RArtifact#A study book …\x01",
            "You can say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I see……\x01",
            "So about the author\x01",
            "Do you know detailed information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, I once built a \"tower\"\x01",
            "What the alchemist left behind is\x01",
            "There seems to be no mistake … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Newly on their identity\x01",
            "It looks like it will not be obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, still valuable material\x01",
            "There is no difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, but the ones left\x01",
            "It is regretful that this alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "However, the neutral alchemist\x01",
            "From that time there are many mysterious … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Books that lead to their identity\x01",
            "It is doubtful whether it was … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes, it is exactly as I say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, books quietly\x01",
            "I hope that it was gone\x01",
            "The mystery is deepening.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5EB8")

    ChrTalk(
        0x101,
        (
            "#00000F(Uncle's … ….\x01",
            "The books we have found\x01",
            "It seems to be investigating. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yeah, apparently for a novelty discovery\x01",
            "It seems I did not connect … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EB8")

    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x16B, 4)
    Return()

    # Function_20_5B64 end

    def Function_21_5EC4(): pass

    label("Function_21_5EC4")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Hmm, is the medieval alchemist …?\x01",
            "The mystery is deepening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, but this magical book\x01",
            "It is very interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I agree,\x01",
            "There is still room for analysis\x01",
            "Let's look further in detail.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_21_5EC4 end

    def Function_22_5F87(): pass

    label("Function_22_5F87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FA5")
    Call(0, 15)
    Jump("loc_5FE0")

    label("loc_5FA5")


    ChrTalk(
        0xFE,
        (
            "Hehe, if you dad\x01",
            "Sometimes you forget your lunch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FE0")

    TalkEnd(0xFE)
    Return()

    # Function_22_5F87 end

    def Function_23_5FE4(): pass

    label("Function_23_5FE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_61C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6002")
    Call(0, 25)
    Jump("loc_61BB")

    label("loc_6002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6143")

    ChrTalk(
        0xE,
        (
            "#01105FOh, that's right.\x01",
            "I forgot to go shopping for dinner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHahaha, I have time until night\x01",
            "It is slow and okay.\x02\x03",
            "From such a thing,\x01",
            "Shizuku's wedding books\x01",
            "Choose firmly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01109FYes, thanks.\x02\x03",
            "#01110FBut I will go shopping properly\x01",
            "Everyone is looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_61BB")

    label("loc_6143")


    ChrTalk(
        0xE,
        (
            "#01103FWell, in a hospital of Shizuku\x01",
            "I'd like to have a book to take, which one is good.\x02\x03",
            "#01109F(Grinding ……)\x01",
            "Yes, this is also interesting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61BB")

    Jump("loc_63CD")

    label("loc_61C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_63CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61DB")
    Call(0, 24)
    Jump("loc_63CD")

    label("loc_61DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_633F")

    ChrTalk(
        0xE,
        (
            "#01109FLook at it, Lloyd.\x01",
            "This book is in the central square\x01",
            "There is a picture of a big bell.\x02\x03",
            "#01100FThat bell was originally\x01",
            "It was in the \"Fort of the Sun\".\x02\x03",
            "#01111FWell, that is big ……\x01",
            "Was not it hard to carry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F（はは、Keyaの知的好奇心は\x01",
            "It seems more than our imagination. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F(Hehe, I look forward to the future.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_63CD")

    label("loc_633F")


    ChrTalk(
        0xE,
        (
            "#01100FA big bell in the central square,\x01",
            "It was in the \"Fort of the Sun\".\x02\x03",
            "#01111FWell, that is big ……\x01",
            "Was not it hard to carry?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63CD")

    TalkEnd(0xFE)
    Return()

    # Function_23_5FE4 end

    def Function_24_63D1(): pass

    label("Function_24_63D1")

    EventBegin(0x0)
    Fade(500)
    OP_68(29830, 4720, -6800, 0)
    MoveCamera(51, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20650, 0)
    SetChrPos(0x101, 29220, 4019, -7320, 90)
    SetChrPos(0x102, 28690, 4030, -6360, 90)
    SetChrPos(0x103, 28670, 4030, -8220, 90)
    SetChrPos(0x104, 27620, 4030, -7320, 90)
    SetChrPos(0x109, 27220, 4030, -6140, 90)
    SetChrPos(0x105, 27190, 4030, -8580, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xE, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    EndChrThread(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0xE,
        "#5P#01101FUh ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#5P#01110FOh, this is it.\x01",
            "…… Hey there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FKeya……\x01",
            "Do you have something to investigate?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#01109FOh, everyone.\x02\x03",
            "#01110FYes, a little old story\x01",
            "I'm trying to collect books that I saw.\x02\x03",
            "After reading a book,\x01",
            "I got interested in various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FEr, Why … ….\x02\x03",
            "#00105F\"Cross Bell medieval history\"\x01",
            "\"Crossbell footprint seen from ruins\" … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FMum, rather than saying the old story\x01",
            "It looks like a proper history book or paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00202FKeya、スゴすぎです……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FHaha, scholars or something in the future\x01",
            "Are you getting down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01100Fえー、Keyaそうなのかなー？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FHuhu, parents stupid It is very interesting here.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0xE, 0x5A, 0x0)
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x151, 7)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 28570, 4019, -7240, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 29310, 4000, -9440, 90)
    BeginChrThread(0x8, 0, 0, 1)
    EventEnd(0x5)
    Return()

    # Function_24_63D1 end

    def Function_25_67B3(): pass

    label("Function_25_67B3")

    EventBegin(0x0)
    Fade(500)
    OP_68(29830, 4720, -6800, 0)
    MoveCamera(51, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20650, 0)
    SetChrPos(0x101, 29220, 4019, -7320, 90)
    SetChrPos(0x102, 28690, 4030, -6360, 90)
    SetChrPos(0x103, 28670, 4030, -8220, 90)
    SetChrPos(0x104, 27620, 4030, -7320, 90)
    SetChrPos(0x109, 27220, 4030, -6140, 90)
    SetChrPos(0x105, 27190, 4030, -8580, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x10E, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    EndChrThread(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0xE,
        "#01110FOh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FKeya、何の本を読んでるんだ？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01109FYeah, this time in Shizuku\x01",
            "I will bring a book to have a visit\x01",
            "I was looking for him.\x02\x03",
            "#01111FWhich way is it?\x01",
            "This book and so on\x01",
            "It looks interesting ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FOh, but that shelf … …\x01",
            "Is not it a corner of Braille books?\x02\x03",
            "\"It sounds interesting\" ….\x01",
            "もしかしてKeyaちゃん、\x01",
            "Can you read this book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01105FYes, I can read it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FYou can read it,\x01",
            "Such lightly …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FDid you learn at Sunday school?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01100FNo, while playing with Suzuku\x01",
            "I remembered it.\x02\x03",
            "\"Marc and the witch of the deep forest\"\x01",
            "Because it was translated into a Braille book,\x01",
            "Was it quite easy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FSo that's the book I know\x01",
            "I might remember earlier ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FHuhu, how fast is this swallowing\x01",
            "Keyaならではですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0xE, 0x5A, 0x0)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x170, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 28570, 4019, -7240, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 29310, 4000, -9440, 90)
    BeginChrThread(0x8, 0, 0, 1)
    EventEnd(0x5)
    Return()

    # Function_25_67B3 end

    def Function_26_6BD7(): pass

    label("Function_26_6BD7")

    EventBegin(0x0)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Fade(500)
    OP_68(12700, 1000, -5500, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 11240, 30, -5300, 90)
    SetChrPos(0x102, 11210, 20, -6440, 90)
    SetChrPos(0x109, 10000, 30, -5300, 90)
    SetChrPos(0x105, 10010, 30, -6440, 90)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "I see……\x01",
            "That is an interesting way of thinking.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6CA0():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_6CA0)
    Sleep(50)
    TurnDirection(0xD, 0x102, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_END)), "loc_6DC0")

    ChrTalk(
        0xC,
        (
            "Oh, are not you Lloyd guys?\x01",
            "You came just right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is where you come,\x01",
            "さっき話したNielsenさんだよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FThis is a journalist …\x02\x03",
            "#00000FUh, nice to meet you.\x01",
            "Crossbell Police & Special Affairs Support Division\x01",
            "We call it Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F10")

    label("loc_6DC0")


    ChrTalk(
        0xC,
        "Oh, are not you Lloyd guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUncle, who is that …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "ああ、彼はNielsenさんといってね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He is active internationally\x01",
            "有名なHe is a journalist.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "ささ、Nielsenさん。\x01",
            "Recently they are recently something\x01",
            "It is Crossbell Police Department of Special Affairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FUh, nice to meet you.\x01",
            "We call it Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    label("loc_6F10")


    ChrTalk(
        0xD,
        (
            "Hmm, that's the Special Support Section.\x01",
            "And you\x01",
            "Mr. Lloyd's leader ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hehe is a good voice with a sense of cleanliness.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00001FExcuse me … … maybe your eyes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, I was injured earlier.\x01",
            "At that time I lost the light.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x0)
    ClearChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 4570, 40, -1570, 90)
    OP_68(12490, 1000, -4720, 3000)
    MoveCamera(45, 24, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(21000, 3000)
    OP_95(0x8, 13110, 30, -2100, 2000, 0x0)
    Sleep(100)
    TurnDirection(0x8, 0xC, 500)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "Director, still in a place like this\x01",
            "You got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The break time has already been over\x01",
            "I am passing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 500)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "Sorry, apparently\x01",
            "It seems they have talked.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "So, sorry.\x01",
            "Because I will return to work ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)

    ChrTalk(
        0xD,
        (
            "Yes, if you do not mind\x01",
            "Let me exchange information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, at that time anytime\x01",
            "Please come.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    TurnDirection(0xD, 0x102, 500)

    ChrTalk(
        0xC,
        (
            "Well then, Lloyd guys as well.\x01",
            "I leave that after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, yes ….\x02",
    )

    CloseMessageWindow()

    def lambda_721B():
        OP_95(0x8, 24560, 4019, 80, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_721B)
    OP_93(0xC, 0x0, 0x1F4)
    OP_95(0xC, 13110, 30, -2100, 2000, 0x0)

    def lambda_7250():
        OP_95(0xC, 4570, 40, -1570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7250)
    Sleep(1000)
    OP_68(12280, 1000, -5990, 2000)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#00105FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, again\x01",
            "I will introduce myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Nice to meet you.\x01",
            "I'm letting a reporter freelance\x01",
            "Nielsenと言う者です。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, here it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F（Nielsenさん――\x01",
            "What I heard somewhere\x01",
            "Something like … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, with the support department\x01",
            "Would definitely hope to see you again\x01",
            "I am honored so I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I am sorry suddenly,\x01",
            "What you want to ask of everyone\x01",
            "I do have …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Will not you have some time?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FYeah, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, in reality now\x01",
            "About the case religious case of the example\x01",
            "I am conducting an investigation … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Some in its content\x01",
            "There are unknown parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As a leading actor in the case resolution\x01",
            "To everyone involved in this case\x01",
            "I'd like to interview you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FCoverage of the case incident, … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehu, everything in various ways\x01",
            "I talk about that I'm grasping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Lloyd, what are you going to do?\x02\x03",
            "(The content is the content,\x01",
            "Too much extra thing\x01",
            "I do not think I can say it … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(That's right ……)\x02\x03",
            "#00003F(By attending the interview,\x01",
            "I can organize again about the incident\x01",
            "Maybe it is … …)\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 27)
    SetChrChipByIndex(0x8, 0x0)
    SetChrPos(0x8, 29310, 4000, -9440, 90)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 7700, 150, 7980, 270)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Return()

    # Function_26_6BD7 end

    def Function_27_76D9(): pass

    label("Function_27_76D9")

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
            "Nielsenの取材に協力する\x01",      # 0
            "I think once\x01",                  # 1
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
        (0, "loc_7753"),
        (1, "loc_79D8"),
        (SWITCH_DEFAULT, "loc_7AC8"),
    )


    label("loc_7753")


    ChrTalk(
        0x101,
        (
            "#00001FAlright, we are\x01",
            "I will cooperate if you do not mind.\x02\x03",
            "but……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, there will be a stand,\x01",
            "Regarding things hard to tell\x01",
            "You can let me face it down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And what I have heard here is\x01",
            "In principle we will off the record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FI see……\x01",
            "Thank you for understanding.\x02\x03",
            "#00005FBut what about the place?\x01",
            "ここだと問題がありそうbut……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, then on the second floor\x01",
            "How about discourse space?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As soon as a person comes in,\x01",
            "I think it's a great place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Findeed.\x01",
            "Let's go quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(128, 3000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Interview coverage on cult incident\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6E, 0x4, 0x2)
    StopBGM(0xBB8)
    WaitBGM()
    Call(0, 29)
    Jump("loc_7AC8")

    label("loc_79D8")


    ChrTalk(
        0x101,
        (
            "#00006FExcuse me.\x01",
            "Now I have other projects ……\x02\x03",
            "#00001FIs it okay if I accept it later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, for a while\x01",
            "Because I am here\x01",
            "Even so, it does not matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then, if convenient,\x01",
            "Please call out anytime.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AC0")
    EventEnd(0x5)

    label("loc_7AC0")

    SetScenarioFlags(0x133, 3)
    Jump("loc_7AC8")

    label("loc_7AC8")

    Return()

    # Function_27_76D9 end

    def Function_28_7AC9(): pass

    label("Function_28_7AC9")

    TalkBegin(0xD)

    ChrTalk(
        0xD,
        "…… Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Interview on the case incident,\x01",
            "Could you go out with me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Call(0, 27)
    TalkEnd(0xD)
    Return()

    # Function_28_7AC9 end

    def Function_29_7B25(): pass

    label("Function_29_7B25")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x2)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0xD, 0xD)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)
    OP_68(28650, 5020, -15570, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20760, 0)
    SetChrPos(0xD, 30640, 4100, -17100, 270)
    SetChrPos(0x101, 25380, 4100, -17100, 90)
    SetChrPos(0x102, 25380, 4100, -15900, 90)
    SetChrPos(0x109, 26700, 4100, -18660, 0)
    SetChrPos(0x105, 28500, 4100, -18680, 0)
    PlayBGM("ed7516", 0)
    Sound(128, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#11PThis time I got involved in the interview,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PSo, first of all,\x01",
            "I will start it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PDenying the goddess,\x01",
            "To worship the devil\x01",
            "That doctrine D∴ G organization ----\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAround 10 years ago, in every part of the continent\x01",
            "I repeated the abduction of young children\x01",
            "The worst criminal group -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PFirst of all, this abduction case\x01",
            "Six years before we saw convergence once\x01",
            "I want to go back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "At that time, the cults scattered throughout the continent\x01",
            "Detect and caught the lodge all at once\x01",
            "大規模な作戦が行われたわけbut……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAbout the power that carried out this strategy\x01",
            "Everyone knows, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6PYeah, that is -\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KSix years ago, the D∴ G group's\x01",
            "What are the forces that executed the campaign cleansing strategy?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Military and police organization of each country\x01",      # 0
            "National Association of Rakuten Associations\x01",          # 1
            "Both\x01",                  # 2
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
        (0, "loc_7F32"),
        (1, "loc_7FBC"),
        (2, "loc_804A"),
        (SWITCH_DEFAULT, "loc_8098"),
    )


    label("loc_7F32")


    ChrTalk(
        0x101,
        (
            "#00000F#6PIt is an army / police organization in each country.\x02\x03",
            "#00006F… Well, that's not all.\x02\x03",
            "#00001FThe Association of Rakuten Associations of each country also\x01",
            "I heard that they cooperated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8098")

    label("loc_7FBC")


    ChrTalk(
        0x101,
        (
            "#00000F#6PIt is an Association of Association of Raccoons of countries.\x02\x03",
            "#00006F… Well, of course not only that.\x02\x03",
            "#00001FMilitary and police organizations of each country also\x01",
            "I heard that they cooperated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8098")

    label("loc_804A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00001F#6PArmy and police organization of each country,\x01",
            "And it is the Association of Assault Horsemen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8098")

    label("loc_8098")


    ChrTalk(
        0x102,
        (
            "#00100F#6PCertainly, the size of the case\x01",
            "In consideration of size, international\x01",
            "The investigation system was established.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PYeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAnd, in such regime,\x01",
            "Flippers Casius Bright\x01",
            "Total command -\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105F#6PWell, sorry.\x01",
            "Can I have a minute?\x02\x03",
            "#00101FWhen it comes to Casius Bright ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#12PWell, maybe -\x01",
            "The command of the commander of the Ribeel army\x01",
            "Do you mean Brigadier Cassius?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PYeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAfter retiring the kingdom army once,\x01",
            "He has been active as a fighter for about 10 years,\x01",
            "I heard he returned to the Kingdom again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12POh, quite\x01",
            "You seem to have an interesting career.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PThat's right, though -\x02\x03",
            "#00108FI have not noticed it until now\x01",
            "Maybe \"Bright\" ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P- Oh, I'm also in training at department 1\x01",
            "I was surprised when I saw the investigation material and knew it.\x02\x03",
            "#00001FBrigadier Cassius Bright,\x01",
            "It is the father of Esther Bright.\x02\x03",
            "Joshua seems to be adopted though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)

    ChrTalk(
        0x102,
        "#00105F#6PAnd after all …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#12PIt is an unexpected connection …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PAlso in the chase battle\x01",
            "Although it seemed to be quite a thing … ….\x02\x03",
            "#10302FNo way it's such a celebrity\x01",
            "That was my daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PHmm, everyone is Brigadier General Cassius\x01",
            "Did you know her daughter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAs I am also a reporter,\x01",
            "彼女の活躍は知る所but……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(50)

    ChrTalk(
        0x101,
        "#00002F#6PWell, there are various relationships.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PExcuse me,\x01",
            "I broke the story of the story ……\x02\x03",
            "#00100FPlease continue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PWell, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThen, it was a hoardman at the time\x01",
            "According to the command of Casius Bright\x01",
            "実行された検挙作戦but……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBy that strategy,\x01",
            "About 90 of the group members\x01",
            "It is said to have been destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBy the way,\x01",
            "I participated from this crossbell\x01",
            "Crossbell Police Sergei Group -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PCurrently you\x01",
            "Sergei, the section manager,\x01",
            "Two people who were regarded as non-standard newcomers -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PWith Arios Mc Rain\x01",
            "He is Brother of Mr. Lloyd\x01",
            "It is Mr. Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P…… Apparently about the incident\x01",
            "To a considerably deep place\x01",
            "You are investigating.\x02\x03",
            "#00008FAnd to the relationship between me and my brother ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6PCertainly, the information about that\x01",
            "Only a part of the police\x01",
            "知られていないはずbut……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PYeah, this business too\x01",
            "As long as it continues, in various directions\x01",
            "Because the face will become useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAnd with Mr. Guy\x01",
            "Let me make friends through coverage several times\x01",
            "Because I had it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P…… Yes, Mr. Guy has a life\x01",
            "It became indebted to us in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P……HM,\x01",
            "Let's restore the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11Pthen\x01",
            "Another person from crossbell -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAs a private advisor\x01",
            "Ian Grimwood attorney\x01",
            "I am involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIan lawyer from that time\x01",
            "As a person familiar with human rights issues\x01",
            "It's famous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PTo collect information on abduction victims in each country\x01",
            "I heard that I contributed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6Pby the way,\x01",
            "The teacher himself also remarked.\x02\x03",
            "#00100FIndeed, cooperation in that form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAlso in this case\x01",
            "Depends on church officials and mysterious organizations\x01",
            "It is said that intervention was secretly -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThrough their work, the remaining power\x01",
            "It is said that it was completely destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6P(Church officials ……)\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)

    ChrTalk(
        0x109,
        (
            "#10101F#12P(To be sure, at Altair Lodge\x01",
            "Father Kevin met\x01",
            "It was a story about being involved. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6P(Incidentally, the mysterious organization is\x01",
            "I guess it is about \"association\" of the example. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11P(Huh, neither of them is okay\x01",
            "They are people who can not grasp the substance. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PHM……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(50)

    ChrTalk(
        0xD,
        (
            "#11Panyway--\x01",
            "Then the cult incident\x01",
            "It should have ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBut a few months ago, the incident was\x01",
            "What has not been over yet\x01",
            "It turns out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PThe reason is, as you all know ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYes, it is a remnant of the cult\x01",
            "The presence of Joachim Günter\x01",
            "It is because it came to light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PYeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBy the way he is a variety of cults\x01",
            "裏事情に詳しかったようbut……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PJoachim Günter,\x01",
            "Was it the leader of the cult?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KJoachim Günter\x01",
            "Were you the leader of the D∴G organization?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exactly\x01",            # 0
            "One of the executive priests\x01",      # 1
            "Just a mission member\x01",        # 2
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
        (0, "loc_9011"),
        (1, "loc_90BD"),
        (2, "loc_9105"),
        (SWITCH_DEFAULT, "loc_919C"),
    )


    label("loc_9011")


    ChrTalk(
        0x101,
        (
            "#00001F#6PYes, he is real\x01",
            "Located at the top of the cult -\x02\x03",
            "#00011F(- not it.\x01",
            "What am I talking about? )\x02\x03",
            "#00006F- Not,\x01",
            "He is one of the executive priests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_919C")

    label("loc_90BD")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00001F#6PNo, it is not.\x01",
            "He is one of the executive priests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_919C")

    label("loc_9105")


    ChrTalk(
        0x101,
        (
            "#00001F#6PNo, he is just a cult member -\x02\x03",
            "#00011F(- not it.\x01",
            "What am I talking about? )\x02\x03",
            "#00006F- Not,\x01",
            "He is one of the executive priests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_919C")

    label("loc_919C")


    ChrTalk(
        0x102,
        (
            "#00103F#6PYeah, that is\x01",
            "The person himself was also allowed to admit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PHowever, he has the face of a researcher,\x01",
            "He was also the supervisor of various experiments.\x02\x03",
            "#00001FThat's why the variety of cults\x01",
            "I think that it was detailed to internal circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PHmm, it is a convincing goverment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAnd I was in that position\x01",
            "He was a ceremony who went throughout the country\x01",
            "Study based on the results …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PFrom the case of seizure six years ago\x01",
            "Succeeded to escape the difficulties,\x01",
            "Humiliated latent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAfter that, at the facility \"paradise\"\x01",
            "Hold the weakness of former Hartmann chairman\x01",
            "I fell to the cross bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThen, eventually\x01",
            "Drugs with the name \"true wisdom\"\x01",
            "\"Gnostic\" was completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI can not understand the details … …\x01",
            "In order to accomplish with the ambitions of the cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PAmbassador's ambition …\x02\x03",
            "#00108F（確か、Keyaちゃんを\x01",
            "To become \"God\"\x01",
            "I was saying that … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6P(Oh, it's a red gnostic\x01",
            "Something took with Joachim\x01",
            "It looked like it was visible … …)\x02\x03",
            "#00006F(In the end,\x01",
            "I do not understand anything. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P…… Hmm, as usual\x01",
            "不明な箇所も多いわけbut……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBy the story so far,\x01",
            "About the outline of the incident\x01",
            "I think that Oita was able to be organized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PFinally based on those,\x01",
            "D∴G Roots of the Church -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI would like to consider that\x01",
            "Are you sure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PThe root of the cult … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PYes, Lloyd said,\x01",
            "Over the years ago the root of the cult\x01",
            "Do you think you go back?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KD∴ G roots of the group\x01",
            "Can you think of going back over many years?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Over 1200 years ago\x01",      # 0
            "Over 500 years ago\x01",        # 1
            "Over 50 years ago\x01",          # 2
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
        (0, "loc_9779"),
        (1, "loc_9866"),
        (2, "loc_98BE"),
        (SWITCH_DEFAULT, "loc_9982"),
    )


    label("loc_9779")


    ChrTalk(
        0x101,
        (
            "#00008F#6P(Over 1200 years ago ……\x01",
            "No, even if it seems like\x01",
            "There is no way to know so far. )\x02\x03",
            "#00003F(From information obtained so far\x01",
            "What can be said reliably … …)\x02\x03",
            "#00001FProbably over 500 years ago -\x01",
            "It is thought that it dates back to the medieval era.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9982")

    label("loc_9866")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00001F#6PProbably over 500 years ago -\x01",
            "It should go back to the medieval era.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9982")

    label("loc_98BE")


    ChrTalk(
        0x101,
        (
            "#00011F#6P(50 years ago ……\x01",
            "No, that can not be such a recent thing. )\x02\x03",
            "#00003F(From information obtained so far\x01",
            "What can be said reliably … …)\x02\x03",
            "#00001FProbably over 500 years ago -\x01",
            "It should go back to the medieval era.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9982")

    label("loc_9982")


    ChrTalk(
        0xD,
        "#11PHmm, why is that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P…… No, in fact we are\x01",
            "I am listening directly from Joachim.\x02\x03",
            "#00008FIt existed 500 years ago in this place\x01",
            "A group of alchemists -\x02\x03",
            "#00001FFrom the time of the cult\x01",
            "They used their skills.\x02\x03",
            "#00006FHowever,\x01",
            "前身については不明but……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIndeed, Joachim\x01",
            "Gunther said that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAlchemist who existed in this place -\x01",
            "In other words, \"Tower of Hoshi\"\x01",
            "They are those who are supposed to build.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PKnowledge that was traditional only\x01",
            "To be supported in this form … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#12PHuh, it is certainly a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PHmm, and that is\x01",
            "Lloyd's\x01",
            "The girl who keeps me -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PShe is from that age as well\x01",
            "Is it possible to think?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013F#6P…………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6POne thing, about the incident\x01",
            "How far do you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI'm sorry, a bit of now,\x01",
            "It was a remark that lacked delicacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThis is the information I had\x01",
            "Together with the information I got from everyone\x01",
            "It is a \"delusion\" which suddenly got up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI swear to the goddess\x01",
            "I will never touch it\x01",
            "Please rest assured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PNo……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#11P…… Hmm, for now tentatively\x01",
            "Is it a place like this for the coverage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PToday really\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThanks to you,\x01",
            "I got meaningful information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6P… Well, this is it.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)

    ChrTalk(
        0xD,
        (
            "#11PWhile doing so\x01",
            "We have to head for the next interview soon.\x01",
            "It came time to not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PThen excuse me with this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI can talk with you again\x01",
            "I am looking forward to the opportunity.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xD, 0xA)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 30000, 4030, -17070, 270)
    OP_0D()
    Sleep(500)
    OP_93(0xD, 0x0, 0x1F4)

    def lambda_9FE9():
        OP_95(0xD, 28680, 4019, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_9FE9)
    OP_68(27600, 5000, 300, 8600)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    OP_6F(0x1)

    def lambda_A032():
        OP_95(0xD, 9240, -490, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_A032)
    OP_68(23120, 4000, 0, 6000)
    Sleep(6500)
    Fade(500)
    SetChrFlags(0xD, 0x80)
    OP_68(28410, 4420, -15830, 0)
    MoveCamera(59, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20710, 0)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10105F#12PIt was a story that I could not see my eyes,\x01",
            "It is a very light footstep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300F#11PHmm, it is a big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PWhat I should say …\x01",
            "He was a wonderful person.\x02\x03",
            "#00000FKeyaの件については\x01",
            "Apparently I can trust him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5PI see …\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    Sleep(500)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#5PAh--!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)

    ChrTalk(
        0x101,
        "#00005F#12PWhat's wrong, Erie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PI finally remembered.\x01",
            "今の人はマルセル・Nielsen――\x02\x03",
            "Around 10 years ago I won the Fülitza Prize\x01",
            "Award-winning, famous from Crossbell\x01",
            "You are a journalist.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10305F#11POh, I am not really familiar with it\x01",
            "When I say the Füritsa Prize ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6POh, the most excellent each year\x01",
            "A gift to a journalist\x01",
            "It should have been an international award.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PI see……\x01",
            "So that insight?\x02\x03",
            "#10105FBut what does it mean to be from Crossbell …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PYeah, once\x01",
            "At the Crossbell Times\x01",
            "You should have been a reporter.\x02\x03",
            "#00108FAnd, just the award winning interview -\x01",
            "At the battlefield coverage at that time,\x01",
            "She seems to have lost the light of the eye.\x02\x03",
            "#00100FBut, after that, actively\x01",
            "Continuing to interview around the continents,\x01",
            "He is contributing to a number of news magazines.\x02\x03",
            "#00104FAs a journalist\x01",
            "Knowing people - that kind of person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PWell, it is also ridiculous\x01",
            "It is a big person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PNielsenさんか……\x02\x03",
            "#00000FIf the opportunity arises,\x01",
            "I'd love to talk to you in the future.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Interview coverage on cult incident\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A671")
    OP_2C(0x6E, 0x2)
    Jump("loc_A685")

    label("loc_A671")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A685")
    OP_2C(0x6E, 0x1)

    label("loc_A685")

    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, 27640, 4030, -13760, 0)
    OP_69(0xFF, 0x0)
    OP_29(0x6E, 0x1, 0x0)
    OP_29(0x6E, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_29_7B25 end

    def Function_30_A6EE(): pass

    label("Function_30_A6EE")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51115.itc", 0x1E)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis345.itp")
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A816")
    SetChrPos(0x101, 5000, 30, 8000, 90)
    SetChrPos(0x102, 5000, 30, 9000, 90)
    SetChrPos(0x103, 5000, 30, 7000, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_A875")

    label("loc_A816")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_A875")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000Fこんにちは、Milesおじさん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hey, Lloyd.\x01",
            "Maybe, look at the request\x01",
            "Did he come or not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FOh, that sort of thing.\x02\x03",
            "If it is okay, let me know the circumstances\x01",
            "Can I get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSure, it was left in the tower of Hoshi\x01",
            "Did you want to collect old documents?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "On the edge of the Ursula interstate\x01",
            "A ruin called \"Tower of Hoshi\"\x01",
            "Do you know what it is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That was before, by the guard\x01",
            "The investigation was forbidden … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Recently, as long as you have permission\x01",
            "It seems that it has become possible to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FCertainly, recently\x01",
            "That is how it is.\x02\x03",
            "#10100FIn that place the former commander remains unexamined\x01",
            "It's a place I left … …\x02\x03",
            "For information gathering, even civilians\x01",
            "Subject to submission of report\x01",
            "I was able to investigate.\x02\x03",
            "Lately, monsters are also\x01",
            "It seems that it does not come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, is that so ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ACF3")

    ChrTalk(
        0xC,
        (
            "Well, during this time,\x01",
            "例のNielsenさんが\x01",
            "I heard that he started investigating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So there's something interesting\x01",
            "She seems to have found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat reporter says … …\x02\x03",
            "#00005Fで、でもNielsenさんって、\x01",
            "Somehow my eyes ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, I see. …\x01",
            "At that time the Cross Bell Times\x01",
            "You seem to have taken the reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "No, they are really active people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFC9")

    label("loc_ACF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_END)), "loc_AE7F")

    ChrTalk(
        0xC,
        (
            "Well, during this time,\x01",
            "例のNielsenさんが\x01",
            "I heard that he started investigating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So there's something interesting\x01",
            "She seems to have found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNielsenさん……\x01",
            "The old man had said before.\x01",
            "He is a journalist.\x02\x03",
            "Bother to such a place\x01",
            "To investigate,\x01",
            "You seem to have someone with action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, in fact he is\x01",
            "I am blind, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At that time the Cross Bell Times\x01",
            "You seem to have taken the reporter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFC9")

    label("loc_AE7F")


    ChrTalk(
        0xC,
        (
            "Well, during this time,\x01",
            "私の知り合いのNielsenさんという\x01",
            "A reporter is in the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So there's something interesting\x01",
            "She seems to have found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fへえ、Bother to such a place\x01",
            "To investigate,\x01",
            "You seem to have someone with action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, in fact he is\x01",
            "I am blind, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At that time the Cross Bell Times\x01",
            "You seem to have taken the reporter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFC9")


    ChrTalk(
        0x105,
        (
            "#10300FSo, that \"interesting thing\"\x01",
            "Is it \"ancient document\" that was requested, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FI see …\x01",
            "When I was pursuing \"silver\" before,\x01",
            "I do not feel like seeing you.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00300F\"Tower of the Stars\"\x01",
            "It was on the middle floor and the top floor\x01",
            "Fluffy deck bookshelf … …\x02\x03",
            "That was being put there\x01",
            "Is it an old document?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)

    ChrTalk(
        0xC,
        (
            "Oh, have you been there?\x01",
            "It is not too early to talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As a library, valuable ancient documents\x01",
            "I was left in such a place\x01",
            "I can not overlook it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "How about it, I wonder if I can ask.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FCertainly, the important role of the library\x01",
            "It is one work I should say, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FBut … … such a large number of books\x01",
            "We only carry with us,\x01",
            "As expected, is not it?\x02\x03",
            "#10106FIf you want to carry it out,\x01",
            "How many round trips … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FThat 's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, to that extent\x01",
            "I do not mean to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To you guys to bring out the book\x01",
            "As a preparatory measure, such labor and expense\x01",
            "I would like you to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The guard and the city hall as well\x01",
            "We already have permission.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B453")

    ChrTalk(
        0x103,
        "#00202FIndeed, is that something like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FBased on the survey results,\x01",
            "We will move forward with the collection plan of the book.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4B8")

    label("loc_B453")


    ChrTalk(
        0x105,
        (
            "#10304FIndeed, that's what it is.\x02\x03",
            "#10300FBased on the survey results,\x01",
            "We will move forward with the collection plan of the book.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4B8")


    ChrTalk(
        0x102,
        (
            "#00100FCertainly, once\x01",
            "If we climbed the \"tower\"\x01",
            "You may be qualified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "How are you going to take care?\x02",
    )

    CloseMessageWindow()
    OP_29(0x71, 0x1, 0x0)
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B544")
    Call(0, 33)

    label("loc_B544")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B57E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_B588")

    label("loc_B57E")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B588")

    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_A6EE end

    def Function_31_B5A0(): pass

    label("Function_31_B5A0")

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
            "undertake\x01",      # 0
            "quit\x01",          # 1
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
        (0, "loc_B602"),
        (1, "loc_B607"),
        (SWITCH_DEFAULT, "loc_B6AB"),
    )


    label("loc_B602")

    Jump("loc_B6AB")

    label("loc_B607")


    ChrTalk(
        0x101,
        (
            "#00000FSorry old man.\x01",
            "Now a little\x01",
            "I can not take my hand …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, that's right.\x01",
            "Then it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then,\x01",
            "If there is no hand\x01",
            "Please call me again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x152, 7)
    Jump("loc_B6AB")

    label("loc_B6AB")

    Return()

    # Function_31_B5A0 end

    def Function_32_B6AC(): pass

    label("Function_32_B6AC")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51115.itc", 0x1E)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B7A8")
    SetChrPos(0x101, 5000, 30, 8000, 90)
    SetChrPos(0x102, 5000, 30, 9000, 90)
    SetChrPos(0x103, 5000, 30, 7000, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_B807")

    label("loc_B7A8")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_B807")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "To you guys \"tower of Hoshi\"\x01",
            "An ancient document that it is placed\x01",
            "I would like you to conduct an investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As preparation for carrying books,\x01",
            "I want to know the labor and cost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "How do you accept, I wonder?\x02",
    )

    CloseMessageWindow()
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E1")
    Call(0, 33)

    label("loc_B8E1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B91B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_B925")

    label("loc_B91B")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B925")

    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_B6AC end

    def Function_33_B93D(): pass

    label("Function_33_B93D")


    ChrTalk(
        0x101,
        (
            "#00002FYes, I understand.\x01",
            "I will underwrite it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Thank you, I will be saved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Wait a moment then.\x01",
            "Please contact the guard,\x01",
            "Let's have the seal of the star tower unraveled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FOh, then\x01",
            "Please leave it to yourself.\x02\x03",
            "Directly to Sonya command\x01",
            "It will be quick to contact you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BA55():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA55)
    Sleep(50)

    def lambda_BA65():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BA65)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA90")

    def lambda_BA85():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BA85)
    Sleep(50)

    label("loc_BA90")


    def lambda_BA95():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BA95)
    Sleep(50)

    def lambda_BAA5():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BAA5)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FYou know.\x01",
            "That seems to be quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, I will ask you if you like.\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x10E, 0x1F4)
    Sleep(300)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x109, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x1, 0x3)
    Sound(823, 0, 100, 0)
    Sleep(2700)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sonja's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Yes,\x01",
            "Here Sogna Belts.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10100FCommand, cheers for good work.\x01",
            "It is Noel · seeker.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sonja's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, noel.\x01",
            "I wonder what happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10103FWell, actually …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noel looks at the tower of Hoshi\x01",
            "I explained what I underwrote.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sonja's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, for example.\x02\x03",
            "A story has arrived here as well.\x01",
            "Surely if you are\x01",
            "It can be said that you are qualified.\x02\x03",
            "To keep the blockade soon,\x01",
            "To the troops circulating around\x01",
            "I will contact you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10101FHaa, thank you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sonja's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please be careful.\x01",
            "… … I will be rude.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 40, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x1, 0x3)
    SetChrSubChip(0x109, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(300)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_93(0x109, 0x10E, 0x0)
    OP_93(0x109, 0x5A, 0x1F4)

    ChrTalk(
        0x109,
        "#10100F…… Yes, this is fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FThank you, Noel.\x02",
    )

    CloseMessageWindow()

    def lambda_BEA2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BEA2)
    Sleep(50)

    def lambda_BEB2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BEB2)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BEDD")

    def lambda_BED2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BED2)
    Sleep(50)

    label("loc_BEDD")


    def lambda_BEE2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BEE2)
    Sleep(50)

    def lambda_BEF2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BEF2)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Ha, smoothly and smoothly\x01",
            "Things carry it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The size of this face is also\x01",
            "It is unique from mission support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHehe, it is.\x02\x03",
            "Well then, get ready\x01",
            "Shall I head to the Tower of Hoshi?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, let's do that.\x02\x03",
            "#00002FMilesおじさん、\x01",
            "Please wait looking forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, be careful.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Old document survey of the tower】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x71, 0x1, 0x1)
    SetScenarioFlags(0x153, 0)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_33_B93D end

    def Function_34_C084(): pass

    label("Function_34_C084")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C14D")
    SetChrPos(0x101, 5000, 30, 8000, 90)
    SetChrPos(0x102, 5000, 30, 9000, 90)
    SetChrPos(0x103, 5000, 30, 7000, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_C1AC")

    label("loc_C14D")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_C1AC")

    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd 's bookshelf' s book\x01",
            "消えていた事をMilesに報告した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00003F… That is why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, not to mention such a large number of books\x01",
            "Who took it …?! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even so, no one has noticed … …\x01",
            "I can not think of common sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F……sorry but\x01",
            "We have no clue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…… Ha, it can not be helped ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At least, what kind of books are there\x01",
            "I just wanted to know but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FAh, no way,\x01",
            "A few volumes are left untouched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FFor the time being\x01",
            "I was able to recover … ….\x02\x03",
            "About the tendency of other books\x01",
            "You may understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Huh, it is true! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHowever, the content is to us\x01",
            "It's gibberish.\x02\x03",
            "Whether it is worthwhile\x01",
            "I do not know but …\x01",
            "I'll hand it over for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Book collected in the tower\x01",
            "Milesに渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "Th-This is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FApparently,\x01",
            "It looks like a book in the medieval times.\x02\x03",
            "Since I'm old and sorry,\x01",
            "It may not be possible to distinguish letters\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0x109,
        "#10105FWell, what did you do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's amazing … …\x01",
            "Either here or here …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "This book is a medieval magical book!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMagical book … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "An old man wrote it,\x01",
            "Alchemy and magic\x01",
            "A book on how to handle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I do not know unless I decipher it,\x01",
            "As far as seeing the illustration on top\x01",
            "First of all, there is no mistake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FOh\x01",
            "That's a pretty valuable book.\x02\x03",
            "#00003FBut in that place\x01",
            "That it remained … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C76C")

    ChrTalk(
        0x103,
        (
            "#00200FTo those who took the book\x01",
            "It was not a very important book,\x01",
            "Is that correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FA clue for that person from this book\x01",
            "It looks hard to find.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7FA")

    label("loc_C76C")


    ChrTalk(
        0x105,
        (
            "#10300FTo those who took the book\x01",
            "It was not a very important book … …\x01",
            "Where is it?\x02\x03",
            "A clue for that person from this book\x01",
            "It looks hard to find.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7FA")


    ChrTalk(
        0x101,
        "#00001FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FThere's a cryptic mystery left … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No,\x01",
            "It collected valuable books\x01",
            "It will not change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You guys did a good job.\x01",
            "I asked again and it was a correct answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FHaha … I'm afraid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This book is in the underground library\x01",
            "Let me carefully save it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Nielsenさんたちとも\x01",
            "I can seem to think a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thank you, Lloyd - kun.\x01",
            "If there is something again, I will ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FOh, yeah.\x01",
            "I'll be waiting anytime.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Old document survey of the tower】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA44")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_CA4E")

    label("loc_CA44")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_CA4E")

    OP_29(0x71, 0x1, 0x5)
    OP_29(0x71, 0x1, 0x6)
    OP_29(0x71, 0x4, 0x10)
    SetScenarioFlags(0x0, 5)
    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_34_C084 end

    def Function_35_CA7A(): pass

    label("Function_35_CA7A")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CB69")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Library News ~\x01",
            "Responding to your request,\x01",
            "The following books were added.\x01",
            "· Doctor Glenn 13 volumes\x01",
            "· Doctor Glenn 14 volumes\x01",
            "※ We are in the bookshelf on the first floor.\x01",
            "If you are interested, please come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_CF6D")

    label("loc_CB69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CC7D")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Library News ~\x01",
            "Responding to your request,\x01",
            "The following books were added.\x01",
            "· Doctor Glenn 9 volume\x01",
            "· Doctor Glenn 10 volumes\x01",
            "· Doctor Glenn 11 volumes\x01",
            "· Doctor Glenn 12 volumes\x01",
            "※ We are in the bookshelf on the first floor.\x01",
            "If you are interested, please come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_CF6D")

    label("loc_CC7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CD56")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Library News ~\x01",
            "Responding to your request,\x01",
            "The following books were added.\x01",
            "· 1 minute cooking (sweets)\x01",
            "※ We are in the bookshelf on the first floor.\x01",
            "If you are interested, please come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_CF6D")

    label("loc_CD56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CE64")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Library News ~\x01",
            "Responding to your request,\x01",
            "The following books were added.\x01",
            "· Doctor Glenn 5 volumes\x01",
            "· Doctor Glenn 6 volumes\x01",
            "· Doctor Glenn 7 volumes\x01",
            "· Dark Doctor Glen Vol. 8\x01",
            "※ We are in the bookshelf on the first floor.\x01",
            "If you are interested, please come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_CF6D")

    label("loc_CE64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CF6D")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Library News ~\x01",
            "Responding to your request,\x01",
            "The following books were added.\x01",
            "· Dark doctor Glenn 1 volume\x01",
            "· Dark Doctor Glen 2\x01",
            "· Dark doctor Glenn Vol. 3\x01",
            "· Dark Doctor Glen 4\x01",
            "※ We are in the bookshelf on the first floor.\x01",
            "If you are interested, please come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_CF6D")

    EventEnd(0x3)
    Return()

    # Function_35_CA7A end

    def Function_36_CF70(): pass

    label("Function_36_CF70")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is \"Marc and Deep Forest Witch\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read the first volume]\x01",      # 0
            "【Read the middle volume】\x01",      # 1
            "【Read the second volume】\x01",      # 2
            "【quit】\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D01B")
    UseItem(0x2D6, 0xFF)

    label("loc_D01B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D02F")
    UseItem(0x2DD, 0xFF)

    label("loc_D02F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D043")
    UseItem(0x2DE, 0xFF)

    label("loc_D043")

    TalkEnd(0xFF)
    Return()

    # Function_36_CF70 end

    def Function_37_D047(): pass

    label("Function_37_D047")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are \"beautiful people who moved the continent\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【I read a book】\x01",      # 0
            "【quit】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0CA")
    UseItem(0x2D7, 0xFF)

    label("loc_D0CA")

    TalkEnd(0xFF)
    Return()

    # Function_37_D047 end

    def Function_38_D0CE(): pass

    label("Function_38_D0CE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is \"effective usage of five extra\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【I read a book】\x01",      # 0
            "【quit】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D153")
    UseItem(0x2D8, 0xFF)

    label("loc_D153")

    TalkEnd(0xFF)
    Return()

    # Function_38_D0CE end

    def Function_39_D157(): pass

    label("Function_39_D157")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is \"Recommendation of railroad mania\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【I read a book】\x01",      # 0
            "【quit】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1D6")
    UseItem(0x2D5, 0xFF)

    label("loc_D1D6")

    TalkEnd(0xFF)
    Return()

    # Function_39_D157 end

    def Function_40_D1DA(): pass

    label("Function_40_D1DA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is \"Cross Bell Kaikaku Complete Works\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【I read a book】\x01",      # 0
            "【quit】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D259")
    UseItem(0x2D9, 0xFF)

    label("loc_D259")

    TalkEnd(0xFF)
    Return()

    # Function_40_D1DA end

    def Function_41_D25D(): pass

    label("Function_41_D25D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is \"a saint and a white wolf\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read the first volume]\x01",      # 0
            "【Read the second volume】\x01",      # 1
            "【quit】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2F1")
    UseItem(0x2DF, 0xFF)

    label("loc_D2F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D305")
    UseItem(0x2E0, 0xFF)

    label("loc_D305")

    TalkEnd(0xFF)
    Return()

    # Function_41_D25D end

    def Function_42_D309(): pass

    label("Function_42_D309")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is \"Alcan Shell fan book\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【I read a book】\x01",      # 0
            "【quit】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D392")
    UseItem(0x2DA, 0xFF)

    label("loc_D392")

    TalkEnd(0xFF)
    Return()

    # Function_42_D309 end

    def Function_43_D396(): pass

    label("Function_43_D396")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D3AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D781")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "A to Z")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【IBC】\x01",      # 0
            "【ZCF】\x01",      # 1
            "【quit】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5B4")
    SetChrName("")
    MenuTitle(-1, 25, 0, "IBC (International Bank of Crossbell)")
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Abbreviation for \"Cross Bell International Bank\".\x01",
            "Huge assets gathering from all over the continent\x01",
            "It is a giant bank to manage and operate,\x01",
            "Not only crossbell, but also international finance ·\x01",
            "He has supported the economic market over the years.\x02\x03",
            "In addition to developing investment activities and financial products,\x01",
            "We are also involved in the management of theme parks,\x01",
            "Even in the Epstein Foundation's \"Conducted Network Planning\"\x01",
            "We are proactively providing funds.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D5B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D77C")
    MenuTitle(-1, 25, 0, "ZCF (Zeiss Central Factory)")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Abbreviation for \"Zeiss Central Studio\".\x01",
            "Based in Zeiss City of Ribeire,\x01",
            "The inventor of the auction, Dr. Epstein's\x01",
            "Dr. A. Russell, a direct disciple,\x01",
            "Founded in cooperation with Zeiss Watchmaker Association\x01",
            "\"Zeiss Technology Studio\" as the predecessor.\x02\x03",
            "In developing the leading airship ahead of the world\x01",
            "Successful continental leader manufacturer,\x01",
            "In recent years the Liberan army affiliation\x01",
            "I completed a high-speed cruiser \"Arseille\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D77C")

    Jump("loc_D3AD")

    label("loc_D781")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_43_D396 end

    def Function_44_D78E(): pass

    label("Function_44_D78E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D7A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E059")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "A line")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Alcan Shell】\x01",        # 0
            "【Alteria Country】\x01",        # 1
            "【Vernes】\x01",            # 2
            "[Eleven Empire]\x01",        # 3
            "【Epstein Foundation】\x01",      # 4
            "【quit】\x01",                # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D995")
    MenuTitle(-1, 25, 0, "Alkane shell")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It exists in cross-bell autonomous state\x01",
            "Internationally famous troupe.\x02\x03",
            "With acrobatic performance\x01",
            "On a brilliant and passionate stage\x01",
            "It continues to attract many spectators.\x02\x03",
            "Known for the \"Fire Dance\"\x01",
            "Current signboard actress Iria · Platier\x01",
            "Especially popular, even in neighboring countries\x01",
            "Many enthusiastic fans.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D995")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAFA")
    MenuTitle(-1, 25, 0, "Alteria Country")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A city state that is the headquarters of the Seven Yigh Church.\x01",
            "Located in the center of the continent of Zemria,\x01",
            "A large number of believers and religious officials from all over the continent\x01",
            "It is also known as a sacred place to gather.\x02\x03",
            "\"Liturgy Ministry\" supervising the whole ritual,\x01",
            "\"Confucius Department\" to manage the goddess's secret,\x01",
            "Such as the \"Buddhist office\" who is in charge of the defense of cities,\x01",
            "Various organizations exist.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DAFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC87")
    MenuTitle(-1, 25, 0, "Verne Company")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Based in the Republic of Calvert\x01",
            "A huge comprehensive technology maker.\x02\x03",
            "Erebonia Empire with Rheinfault\x01",
            "It is famous as an established long-established store of weapons and weapons that make up two positions,\x01",
            "Since the invention was invented,\x01",
            "We are engaged in the research and development of all conductive products.\x02\x03",
            "Among other things, in the field of power driven vehicles,\x01",
            "Starting with a power bus, from private cars to special vehicles\x01",
            "We are developing various products.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DC87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEB7")
    MenuTitle(-1, 25, 0, "Eleventh Empire")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Located west of Crossbell Autonomous Region,\x01",
            "A giant empire that sets up the emblem of \"Golden Troops\".\x01",
            "Current emperor is Jugendrase L'Arnor.\x02\x03",
            "Although it is a country of the old regime which the large nobility dominates,\x01",
            "Military origin known from the \"Akira Iron Blood\" known by its synonym\x01",
            "Under the command of Gillius Osbourne's Prime Minister,\x01",
            "Railroads are spread all over the country and are being modernized.\x02\x03",
            "In addition to regular armored army, large aristocratic private troops etc.\x01",
            "Hold a huge military power,\x01",
            "I am constantly straining the neighboring countries.\x02\x03",
            "In addition, to resolve the incident that occurred in Libert last year\x01",
            "A son of Emperor, Prince Oliver will cooperate.\x01",
            "It became a big topic within the Empire.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DEB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E054")
    MenuTitle(-1, 25, 0, "Epstein Foundation")
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Genius leaders who invented the auction,\x01",
            "Foundation that inherited the achievement of Dr. C · Epstein.\x01",
            "As a research institution, manufacturers' aspect is also strong,\x01",
            "It is particularly excellent in the fields of communication and information processing.\x02\x03",
            "magic#4RArts#\"Tactical auction\" that can trigger\x01",
            "In addition to being the only manufacturer developing,\x01",
            "In recent years we have developed communication and information processing technology\x01",
            "We are focusing on \"power network planning\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E054")

    Jump("loc_D7A5")

    label("loc_E059")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_44_D78E end

    def Function_45_E066(): pass

    label("Function_45_E066")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E07D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8FD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Ka line")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Kaitou B】\x01",                          # 0
            "【CARBODD REPUBLIC】\x01",                # 1
            "【Cross Bell Autonomous Region】\x01",                # 2
            "【Crystal Circuit / Quartz】\x01",              # 3
            "[Ancient artifacts / artifacts]\x01",      # 4
            "【quit】\x01",                          # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E320")
    MenuTitle(-1, 25, 0, "Kaiten B")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The great thief of the deadly demon that hangs over the continent.\x01",
            "From the jewelry to the guiding tank,\x01",
            "Regardless of country or individual, I work a lot of theft,\x01",
            "From its vivid and brilliant way, some are enthusiastic\x01",
            "It is popular enough to have fans.\x02\x03",
            "Sending pretty messy messages to various places,\x01",
            "Although it sometimes exposes the figure with the mask and white cloak,\x01",
            "The identity is enveloped in a mystery.\x01",
            "In recent years, the person himself himself talks about \"release of beauty\"\x01",
            "Eleventh Empireで実行された、不可解ながらも\x01",
            "A brilliant series of crime is new to the topic.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E320")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E487")
    MenuTitle(-1, 25, 0, "Republic of Calvert")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Democratization was accomplished about a hundred years ago\x01",
            "Republic located east of Crossbell Autonomous Region.\x01",
            "The current head of state is President Rock Smith.\x02\x03",
            "Having a vast land area,\x01",
            "Because I accepted immigrants from the east\x01",
            "Have diverse cultural backgrounds.\x02\x03",
            "After concluding the \"treaty of non-war,\" calm down\x01",
            "見せているが、歴史上Eleventh Empireと\x01",
            "I have repeated collisions many times.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E487")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E609")
    MenuTitle(-1, 25, 0, "Crossbell Autonomous Region")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An autonomous state in the western part of the continent.\x01",
            "Eleventh Empire、Republic of Calvertという\x01",
            "It is sandwiched between two major countries,\x01",
            "It has been the subject of fierce territorial disputes,\x01",
            "It was established as an autonomous state 70 years ago.\x02\x03",
            "Currently, the central Crosbell city is a continental continent\x01",
            "It has grown into a giant trade city,\x01",
            "Transcontinental railroad connecting the empire - Republic\x01",
            "It is a relay point of international regular airship.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E609")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E716")
    MenuTitle(-1, 25, 0, "Crystal circuit / quartz")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Purified and processed fragments of Seven Yellow Stone \"Sepis\"\x01",
            "Circuit with crystal structure.\x02\x03",
            "At the same time as being an energy source,\x01",
            "Although it is also a device that causes various phenomena,\x01",
            "If it is not set inside the orb\x01",
            "It does not exert its effect.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E716")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8F8")
    MenuTitle(-1, 25, 0, "Ancient artifacts / artifacts")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "While operating with the same power as the auction\x01",
            "Diverter of ancient civilization with different working principle.\x02\x03",
            "In the era of \"Ancient Zemria civilization\"\x01",
            "It is said that it was created and in contemporary technology\x01",
            "Analysis is considered impossible.\x02\x03",
            "It may be rarely discovered from remains in continents,\x01",
            "Strong power beyond human excellence now\x01",
            "Many things to demonstrate.\x02\x03",
            "For that reason, the Seven Yigh Church held artifacts\x01",
            "It is defined as \"gift of the goddess who was too early\"\x01",
            "It is said that it is responsible for its collection and management.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E8F8")

    Jump("loc_E07D")

    label("loc_E8FD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_45_E066 end

    def Function_46_E90A(): pass

    label("Function_46_E90A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E921")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC19")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Sa line")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Seven Year Society】\x01",                # 0
            "【Seven Yellow Stones / Septium】\x01",      # 1
            "【quit】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAC5")
    MenuTitle(-1, 25, 0, "Seven Chaos Church")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Most widely believed in the continent of Zemria\x01",
            "Religious organizations that serve \"the goddess of the sky Eidos\".\x01",
            "Alteria Countryに総本山を持つ。\x02\x03",
            "Although the influence has declined since the power revolution\x01",
            "Even now it has strong influence across the continent,\x01",
            "Through fields such as academic, educational, medical,\x01",
            "It is in a position to enlighten the people.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EAC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC14")
    MenuTitle(-1, 25, 0, "Seven Yellow Stone / Septium")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Seven kinds of precious stones distributed throughout the continent.\x01",
            "As an old jewel,\x01",
            "It has been prized as a symbol of mystery.\x02\x03",
            "It is too small to become a jewel in modern times\x01",
            "Purify and process the fragment \"Sepis\"\x01",
            "With the invention of the technology to make quartz,\x01",
            "The importance of the Seven Yarrow resources\x01",
            "It has risen at a stroke among the continental countries.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC14")

    Jump("loc_E921")

    label("loc_EC19")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_46_E90A end

    def Function_47_EC26(): pass

    label("Function_47_EC26")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3B0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "TA row · top")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Collapse】\x01",                    # 0
            "【Fishing public division】\x01",                  # 1
            "【Power Revolution】\x01",                  # 2
            "【Conductor / Orgement】\x01",      # 3
            "【quit】\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDC3")
    MenuTitle(-1, 25, 0, "Great collapse")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is said to have occurred about 1,200 years ago,\x01",
            "The collapse of the ancient Zemrian civilization.\x01",
            "It is said that a natural disaster is the cause, but details are unknown.\x02\x03",
            "《Great collapse》によって文明が失われた後、\x01",
            "People followed the long dark era.\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EDC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF4D")
    MenuTitle(-1, 25, 0, "Fishing public division")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Acting for spreading fishing culture,\x01",
            "Professional group of fishing.\x01",
            "Former nobility fishing enthusiast,\x01",
            "Established by Mr. H. Fischer,\x01",
            "We are headquartered in Grancell city of Liber.\x02\x03",
            "Starting from searching, surveying and cultivating fishing spots,\x01",
            "Excavation and education of new generation fishermen, more recently\x01",
            "We also involved in the development of fishing tools and fishing foods,\x01",
            "We have expanded the range of our activities year by year.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1D7")
    MenuTitle(-1, 25, 0, "Power revolution")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "About 50 years ago,\x01",
            "Occurred when the invention was invented\x01",
            "Technological innovation on continental scale.\x02\x03",
            "Despite being an epoch-making invention\x01",
            "People of those days were skeptical,\x01",
            "Epstein Foundationの導力通信器や\x01",
            "As the ZCF's leading airships come into the world,\x01",
            "Its usefulness was recognized throughout the continent.\x02\x03",
            "Currently from daily necessities such as heating and lighting\x01",
            "Weapons like railroads, airships, tanks and cannons\x01",
            "Everything is made to be powerful,\x01",
            "For the people the orbment no longer\x01",
            "It has become indispensable.\x02\x03",
            "In recent years, along with the miniaturization of power-assisted engines,\x01",
            "Verne CompanyやRheinfaultによって\x01",
            "Development of high-performance guided vehicles is progressing,\x01",
            "Popularization to the general level has also begun.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F1D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3AB")
    MenuTitle(-1, 25, 0, "Conductor / Orgement")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "C · Epstein by Dr.\x01",
            "Invented, drawing out the power from the Seven Yao stone,\x01",
            "A generic term for machines that cause various phenomena.\x02\x03",
            "With the movement of the structure / gear inside the orbment,\x01",
            "By mutually interfering crystal circuits processed seven oysters\x01",
            "Express a myriad of variations phenomena.\x02\x03",
            "The usefulness of the auction is\x01",
            "In addition to abundance, \"If time goes by inside\x01",
            "It will be that the power will be restored \"and the external combustion · internal combustion engine\x01",
            "Economic efficiency is much higher when compared.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F3AB")

    Jump("loc_EC3D")

    label("loc_F3B0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_47_EC26 end

    def Function_48_F3BD(): pass

    label("Function_48_F3BD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F3D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F84F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Ta line down")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Magic Magic / Oval Arts】\x01",      # 0
            "【Conducted network plan】\x01",          # 1
            "[Toho People Street]\x01",                      # 2
            "【quit】\x01",                        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5A5")
    MenuTitle(-1, 25, 0, "Dynamic magic / oval arts")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Epstein Foundationによって特別に設計された\x01",
            "Crystal circuit on \"Tactical Orbement\"#8RQuotes#By incorporating\x01",
            "\"Magic\" that can be activated.\x02\x03",
            "Generally called \"arts\"\x01",
            "As a technology that anyone can use depending on training\x01",
            "It is spreading to military, police, guilds, etc.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F5A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F712")
    MenuTitle(-1, 25, 0, "Conducted network plan")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Epstein Foundationが研究開発を進めている\x01",
            "Innovative information network plan.\x01",
            "Terminals are connected with a power cable,\x01",
            "Enabling enormous exchange of information and processing.\x02\x03",
            "Originally developed in collaboration with ZCF of Libert\x01",
            "It was being advanced, but now IBC\x01",
            "Received funds, to Crossbell City\x01",
            "Full-scale test introduction started.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F712")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F84A")
    MenuTitle(-1, 25, 0, "Eastern People")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Republic of Calvertに存在する、\x01",
            "A large-scale city built by Toho-immigrants.\x01",
            "Various cultures, people, supplies go and go,\x01",
            "It is called \"intersection of east and western culture\".\x02\x03",
            "Exotic buildings stand side by side\x01",
            "It is famous as a sightseeing spot,\x01",
            "The presence of gigantic syndicate is also whispered.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F84A")

    Jump("loc_F3D4")

    label("loc_F84F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_48_F3BD end

    def Function_49_F85C(): pass

    label("Function_49_F85C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F873")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCFD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Na Ha line")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【One hundred day campaign】\x01",      # 0
            "[Treaty of non-war]\x01",      # 1
            "【quit】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB28")
    MenuTitle(-1, 25, 0, "A hundred days war")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀暦１１９２年、Eleventh Empire・\x01",
            "An aggressive war between Ribeau kingdoms.\x01",
            "帝国による宣戦布告から、Seven Chaos Churchの\x01",
            "Until the end of the war realized with brokerage,\x01",
            "Because it saw settlement in about 100 days\x01",
            "This is called.\x02\x03",
            "Initially Libert was forced into inferiority,\x01",
            "The majority of the country was occupied by the Imperial Army,\x01",
            "A state-of-the-art security flying boat of those days\x01",
            "By the shocking counter attack strategy used\x01",
            "I instantly overturned the situation.\x02\x03",
            "Regarding the reason for opening up the battlefield in the first place,\x01",
            "Because both countries kept silence\x01",
            "Although I was never revealed,\x01",
            "Later \"mistakes arising from unhappy misunderstandings\"\x01",
            "In the expression that, from the Imperial Government to Libert\x01",
            "A formal apology statement was issued.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FB28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCF8")
    MenuTitle(-1, 25, 0, "A non-war treaty")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In seventeen calendars 1202, the King of Liber ·\x01",
            "Eleventh Empire・Republic of Calvertの\x01",
            "International treaty concluded between the three countries.\x01",
            "Proposed by Queen Alicia of Libert,\x01",
            "A signing ceremony was held at Elbe Rikyu in the country.\x02\x03",
            "There is no legal enforcement in this Convention,\x01",
            "条約締結後は、Crossbell Autonomous Region近郊で\x01",
            "It depended on each of the empire and republic which had been deployed\x01",
            "Large-scale military exercises are withdrawn,\x01",
            "Tension condition has been relaxed considerably,\x01",
            "It can be said that the effect surely appears.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FCF8")

    Jump("loc_F873")

    label("loc_FCFD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_49_F85C end

    def Function_50_FD0A(): pass

    label("Function_50_FD0A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10107")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Ma Ya line")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Mishram】\x01",                        # 0
            "【Association of Shogakushi / Blaser Guild】\x01",      # 1
            "【quit】\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEC7")
    MenuTitle(-1, 25, 0, "Michelin")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A luxury resort located south of Lake Elm.\x01",
            "Two years ago, after IBC began development\x01",
            "Resort hotels and theme parks\x01",
            "It became a popular spot in a row.\x02\x03",
            "Called \"Mitishi\"\x01",
            "The local mascot character also\x01",
            "Popular with citizens and tourists.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FEC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10102")
    MenuTitle(-1, 25, 0, "Association of Shogaku / Blaser Guild")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Work for local peace and civilian protection\x01",
            "Hitter fighter#6RBracer#Private groups.\x01",
            "Because there are branches all over the continent of Zemria,\x01",
            "He has a considerable influence and voice.\x02\x03",
            "Prioritize the safety of civilians more than anything\x01",
            "Although the philosophy behaving is ideal,\x01",
            "On the contrary unless security of civilians is threatened,\x01",
            "Investigation right / arrest right to state / public power\x01",
            "There is also a weak point in the organizational agreement that it can not be exercised.\x02\x03",
            "In the crossbell,\x01",
            "From having many international projects\x01",
            "\"Wind of the Sword\" Arios · McLae begins\x01",
            "Excellent talent gathered and gained the support of citizens.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10102")

    Jump("loc_FD21")

    label("loc_10107")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_50_FD0A end

    def Function_51_10114(): pass

    label("Function_51_10114")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1012B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1091E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "La line")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Rheinfault Corporation]\x01",        # 0
            "【Democratic Republic】\x01",        # 1
            "【Leman Autonomous Region】\x01",            # 2
            "【Liber Kingdom】\x01",            # 3
            "【Hunting Corps / Jaeger】\x01",      # 4
            "【quit】\x01",                  # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1035A")
    MenuTitle(-1, 25, 0, "Rheinfault")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Eleventh Empireに本拠を置く\x01",
            "A huge comprehensive technology maker.\x01",
            "Originally of cannon and heavy weapons using explosive\x01",
            "It was a weapon workshop that was specializing in manufacturing.\x02\x03",
            "Since the invention was invented,\x01",
            "In addition to conducting guns and powered weapons,\x01",
            "We also expanded to fields such as power train and airship,\x01",
            "Republic of Calvertの《Verne Company》と並んで、\x01",
            "It has grown to be called the world largest manufacturer.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1035A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104FB")
    MenuTitle(-1, 25, 0, "Democratic Republic")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The principal country located in the northern part of the continent.\x01",
            "Although it is a difficult north country,\x01",
            "It is blessed with rich forests and lakes,\x01",
            "Fascinated by its scenic landscape,\x01",
            "Many visit for sightseeing purpose.\x02\x03",
            "It is also famous as a medical advanced country,\x01",
            "Medical equipment manufacturers representing the continent concentrated,\x01",
            "I am producing many excellent doctors.\x01",
            "Crossbell Autonomous Regionの聖ウルスラ医科大学も\x01",
            "Democratic Republicの協力によって設立された。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_104FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105EF")
    MenuTitle(-1, 25, 0, "Leman Autonomous Region")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An autonomous state located in the central part of the continent.\x01",
            "Epstein Foundationの本部があり、\x01",
            "It is also home to Dr. C · Epstein.\x02\x03",
            "In addition, have chapters in every continent\x01",
            "It is famous also that there is a headquarters of the Association of Association of Associations.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_105EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107F2")
    MenuTitle(-1, 25, 0, "Kingdom of Libert")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The kingdom located in the southwest part of the continent of Zemria.\x01",
            "It is a traditional country colored by rich nature,\x01",
            "Currently, under the reign of Old Queen Alicia 嘦 世,\x01",
            "I keep pride in peace.\x02\x03",
            "Although it is inferior to national strengths from neighboring countries,\x01",
            "Abundant Seven Young stone resources and excellent technology,\x01",
            "Depending on skillful foreign policy\x01",
            "I have built an equal relationship.\x02\x03",
            "Last year, on the Lake Valeria in the middle of the kingdom\x01",
            "A mysterious gigantic structure (details unknown) emerged,\x01",
            "The incident that the power of the whole kingdom stops\x01",
            "I got up, but due to the work of the military and the fighter association\x01",
            "It was solved without any problems and regained calm.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_107F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10919")
    MenuTitle(-1, 25, 0, "Hunting Corps / Jaeger")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Among the mercenary units operating in continental countries\x01",
            "Particularly used to point to excellent troops.\x02\x03",
            "Flexible contract according to size and purpose can be done,\x01",
            "Because you can expect high combat strength,\x01",
            "Often used as soldiers,\x01",
            "Some countries prohibit their operation by law.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10919")

    Jump("loc_1012B")

    label("loc_1091E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_51_10114 end

    def Function_52_1092B(): pass

    label("Function_52_1092B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a \"dark doctor Glenn\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Reading Volume 13】\x01",      # 0
            "【Reading Volume 14】\x01",      # 1
            "【quit】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109BF")
    UseItem(0x2D2, 0xFF)

    label("loc_109BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109D3")
    UseItem(0x2D3, 0xFF)

    label("loc_109D3")

    TalkEnd(0xFF)
    Return()

    # Function_52_1092B end

    def Function_53_109D7(): pass

    label("Function_53_109D7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a \"dark doctor Glenn\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Reading Volume 9】\x01",      # 0
            "【Reading Volume 10】\x01",      # 1
            "【Reading Volume 11】\x01",      # 2
            "【Reading Volume 12】\x01",      # 3
            "【quit】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A89")
    UseItem(0x2CE, 0xFF)

    label("loc_10A89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A9D")
    UseItem(0x2CF, 0xFF)

    label("loc_10A9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AB1")
    UseItem(0x2D0, 0xFF)

    label("loc_10AB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AC5")
    UseItem(0x2D1, 0xFF)

    label("loc_10AC5")

    TalkEnd(0xFF)
    Return()

    # Function_53_109D7 end

    def Function_54_10AC9(): pass

    label("Function_54_10AC9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a \"dark doctor Glenn\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Read 5 volumes】\x01",      # 0
            "【Reading Volume 6】\x01",      # 1
            "【Reading Volume 7】\x01",      # 2
            "【Reading Volume 8】\x01",      # 3
            "【quit】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B7B")
    UseItem(0x2CA, 0xFF)

    label("loc_10B7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B8F")
    UseItem(0x2CB, 0xFF)

    label("loc_10B8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BA3")
    UseItem(0x2CC, 0xFF)

    label("loc_10BA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BB7")
    UseItem(0x2CD, 0xFF)

    label("loc_10BB7")

    TalkEnd(0xFF)
    Return()

    # Function_54_10AC9 end

    def Function_55_10BBB(): pass

    label("Function_55_10BBB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a \"dark doctor Glenn\" on the bookshelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Read 1 volume】\x01",      # 0
            "【Read 2 volumes】\x01",      # 1
            "【Reading Volume 3】\x01",      # 2
            "【Reading Volume 4】\x01",      # 3
            "【quit】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C6D")
    UseItem(0x2C6, 0xFF)

    label("loc_10C6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C81")
    UseItem(0x2C7, 0xFF)

    label("loc_10C81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C95")
    UseItem(0x2C8, 0xFF)

    label("loc_10C95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CA9")
    UseItem(0x2C9, 0xFF)

    label("loc_10CA9")

    TalkEnd(0xFF)
    Return()

    # Function_55_10BBB end

    SaveToFile()

Try(main)
