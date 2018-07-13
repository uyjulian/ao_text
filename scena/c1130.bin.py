from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Cassal",                 # 1
        "Novaase",                # 2
        "Shannah",                # 3
        "Abbie",                  # 4
        "Miles",                  # 5
        "Nielsen",                # 6
        "KeA",                    # 7
        "Leyte",                  # 8
        "Cassal",                 # 9
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
        "Function_5_DD3",          # 05, 5
        "Function_6_1C59",         # 06, 6
        "Function_7_2B6E",         # 07, 7
        "Function_8_2CC2",         # 08, 8
        "Function_9_2FCD",         # 09, 9
        "Function_10_3A43",        # 0A, 10
        "Function_11_3C06",        # 0B, 11
        "Function_12_41CE",        # 0C, 12
        "Function_13_4230",        # 0D, 13
        "Function_14_43D3",        # 0E, 14
        "Function_15_5A73",        # 0F, 15
        "Function_16_5B4A",        # 10, 16
        "Function_17_5D97",        # 11, 17
        "Function_18_5F81",        # 12, 18
        "Function_19_606A",        # 13, 19
        "Function_20_6202",        # 14, 20
        "Function_21_6593",        # 15, 21
        "Function_22_666D",        # 16, 22
        "Function_23_66CD",        # 17, 23
        "Function_24_6ADB",        # 18, 24
        "Function_25_6EF2",        # 19, 25
        "Function_26_734B",        # 1A, 26
        "Function_27_7E77",        # 1B, 27
        "Function_28_82F7",        # 1C, 28
        "Function_29_835C",        # 1D, 29
        "Function_30_B28C",        # 1E, 30
        "Function_31_C265",        # 1F, 31
        "Function_32_C36B",        # 20, 32
        "Function_33_C62A",        # 21, 33
        "Function_34_CD93",        # 22, 34
        "Function_35_D8CF",        # 23, 35
        "Function_36_DEA0",        # 24, 36
        "Function_37_DF94",        # 25, 37
        "Function_38_E026",        # 26, 38
        "Function_39_E0BD",        # 27, 39
        "Function_40_E14B",        # 28, 40
        "Function_41_E1EF",        # 29, 41
        "Function_42_E2B1",        # 2A, 42
        "Function_43_E335",        # 2B, 43
        "Function_44_E866",        # 2C, 44
        "Function_45_F454",        # 2D, 45
        "Function_46_10020",       # 2E, 46
        "Function_47_10458",       # 2F, 47
        "Function_48_10E89",       # 30, 48
        "Function_49_113B1",       # 31, 49
        "Function_50_11A2A",       # 32, 50
        "Function_51_11F30",       # 33, 51
        "Function_52_12AAE",       # 34, 52
        "Function_53_12B6F",       # 35, 53
        "Function_54_12C79",       # 36, 54
        "Function_55_12D80",       # 37, 55
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
            "The "One Minute Cooking - Sweets Edition" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_DCF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Light Popcorn"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_DCF")

    TalkEnd(0xFF)
    Return()

    # Function_4_D0F end

    def Function_5_DD3(): pass

    label("Function_5_DD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBF")

    ChrTalk(
        0xFE,
        (
            "Hello, and welcome to\x01",
            "Crossbell City Library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*, as expected, there\x01",
            "aren't many visitors today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There must be many who are\x01",
            "avoiding going out due to the\x01",
            "appearance of that huge tree.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F1A")

    label("loc_EBF")


    ChrTalk(
        0xFE,
        (
            "There's not many\x01",
            "visitors today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a librarian, it's\x01",
            " \x01",
            "in our borrowers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1A")

    Jump("loc_1C55")

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FD0")

    ChrTalk(
        0xFE,
        (
            "I feel fear, the same as when those\x01",
            "jaegers came to attack us before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why did something like this have to happen?\x01",
            "...I'm filled with feelings like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C55")

    label("loc_FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10EA")

    ChrTalk(
        0xFE,
        (
            "The "Independent State of Crossbell"... \x01",
            "I feel we've finally arrived to a point\x01",
            "from which we cannot turn back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of attitude the two major powers\x01",
            "will take, having received the announcement.\x01",
            "To be honest, I'm full of anxiety about this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C55")

    label("loc_10EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121C")

    ChrTalk(
        0xFE,
        (
            "The night of the attack, I had\x01",
            "finished work and just left, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems this Governmental\x01",
            "District suffered serious damage,\x01",
            "with police HQ at its center.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An entire week has passed since then, but... \x01",
            "I can't forget the fires that\x01",
            "raged in the city that night.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12D4")

    label("loc_121C")


    ChrTalk(
        0xFE,
        (
            "An entire week has passed since then, but... \x01",
            "I can't forget the fires that\x01",
            "raged in the city that night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it was a warning regarding\x01",
            "the independence proposal...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D4")

    Jump("loc_1C55")

    label("loc_12D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1377")

    ChrTalk(
        0xFE,
        (
            "I suppose it's only natural, but the\x01",
            "people over at police HQ are flustered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope the Mainz incident is\x01",
            "resolved peacefully, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C55")

    label("loc_1377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144C")

    ChrTalk(
        0xFE,
        (
            "I heard a civic forum\x01",
            "will be held at City\x01",
            "Meeting Hall today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The state independence question...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The referendum's approaching. \x01",
            "I'll need to make up my\x01",
            "mind before long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_149E")

    label("loc_144C")


    ChrTalk(
        0xFE,
        (
            "The state independence question...\x01",
            "I'll need to make up my\x01",
            "mind before long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149E")

    Jump("loc_1C55")

    label("loc_14A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_15E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155E")

    ChrTalk(
        0xFE,
        (
            "Umm, this is a science book, \x01",
            "so it goes on the shelf over there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. Why is returning books\x01",
            "to the gaps in the shelves\x01",
            "this much fun, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15DF")

    label("loc_155E")


    ChrTalk(
        0xFE,
        (
            "Returning books to the gaps in the\x01",
            "shelves is a bit like a puzzle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It feels good\x01",
            "putting books in\x01",
            "just the right spot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15DF")

    Jump("loc_1C55")

    label("loc_15E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_177F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D6")

    ChrTalk(
        0xFE,
        (
            "Hello, and welcome to\x01",
            "Crossbell City Library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you ask for a book\x01",
            "that is currently on loan,\x01",
            "we can reserve it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please feel free to ask either myself\x01",
            "or the head librarian about it anytime.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_177A")

    label("loc_16D6")


    ChrTalk(
        0xFE,
        (
            "If you ask for a book\x01",
            "that is currently on loan,\x01",
            "we can reserve it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please feel free to ask either myself\x01",
            "or the head librarian about it anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177A")

    Jump("loc_1C55")

    label("loc_177F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_178D")
    Jump("loc_1C55")

    label("loc_178D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1826")

    ChrTalk(
        0xFE,
        (
            "I heard the heads of state\x01",
            "stayed at the Michelam\x01",
            "guest house last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I'm sure they\x01",
            "had wonderful and\x01",
            "delicious food.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C55")

    label("loc_1826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18BA")

    ChrTalk(
        0xFE,
        (
            "Due to the Trade\x01",
            "Conference, there is a\x01",
            "festival-like mood in the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I'm excited to see\x01",
            "what they are going to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C55")

    label("loc_18BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D5")

    ChrTalk(
        0xFE,
        (
            "When he heard there was a large quantity of\x01",
            "ancient documents at the Tower of Stargaze,\x01",
            "the head librarian was overjoyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, it seems\x01",
            "he would like to carry\x01",
            "all of them here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do we have enough space\x01",
            "in our basement archive?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A66")

    label("loc_19D5")


    ChrTalk(
        0xFE,
        (
            "It seems the head librarian\x01",
            "plans to transport all the\x01",
            "ancient documents here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do we have enough space\x01",
            "in our basement archive?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A66")

    Jump("loc_1C55")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_1B28")

    ChrTalk(
        0xFE,
        (
            "As a freelance journalist,\x01",
            "Mr. Nielsen has been busy \x01",
            "flying all over the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that today is his first trip home\x01",
            "in around three years and he's happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C55")

    label("loc_1B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1BCD")

    ChrTalk(
        0xFE,
        (
            "That head librarian...\x01",
            "He's restless today just because \x01",
            "Mr. Nielsen is coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, it seems he\x01",
            "likes talking with\x01",
            "Mr. Nielsen very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C55")

    label("loc_1BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C55")

    ChrTalk(
        0xFE,
        (
            "Hello, and welcome to\x01",
            "Crossbell City Library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are looking for some books,\x01",
            "please feel free to ask me anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C55")

    TalkEnd(0xFE)
    Return()

    # Function_5_DD3 end

    def Function_6_1C59(): pass

    label("Function_6_1C59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C6A")
    Jump("loc_2B6A")

    label("loc_1C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC7")

    ChrTalk(
        0xFE,
        (
            "There's still a ways to go, but...\x01",
            "It seems the reconstruction is\x01",
            "finally coming together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thankfully, because the station and\x01",
            "airport were undamaged, I was able\x01",
            "to come to Crossbell again, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got to think about attacks\x01",
            "targeting transportation facilities.\x01",
            "...That's a scary thing to think about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E62")

    label("loc_1DC7")


    ChrTalk(
        0xFE,
        (
            "This library is indispensable when it\x01",
            "comes to researching Crossbell's history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be nice confining myself\x01",
            "in a research room at Leman...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E62")

    Jump("loc_2B6A")

    label("loc_1E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1FB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2C")

    ChrTalk(
        0xFE,
        (
            "The attack on Mainz... \x01",
            "To think it's occupied, even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An Imperial deed? Or a Republican one?\x01",
            "To put it bluntly, it's likely it's\x01",
            "an act from one of them...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FB4")

    label("loc_1F2C")


    ChrTalk(
        0xFE,
        (
            "No matter by the Empire or\x01",
            "Republic, Mainz is attack material.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To put it bluntly, it's likely it's\x01",
            "an act from one of them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB4")

    Jump("loc_2B6A")

    label("loc_1FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CF")

    ChrTalk(
        0xFE,
        (
            "Lately, monsters different than the\x01",
            "so-called normal ones have been\x01",
            "appearing throughout Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumor has it that these monsters\x01",
            "seem to be ones written in the\x01",
            "Church Testaments, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder just what is\x01",
            "happening in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_219E")

    label("loc_20CF")


    ChrTalk(
        0xFE,
        (
            "If Ancient Zemurian civilization knowledge\x01",
            "remained in present day, I'm sure\x01",
            "we'd know everything, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. No, I mustn't. If I ask\x01",
            "the impossible, I'll lose sight\x01",
            "of what I actually can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219E")

    Jump("loc_2B6A")

    label("loc_21A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2273")

    ChrTalk(
        0xFE,
        (
            "Hmm. Next, it might be interesting to\x01",
            "put together an essay with the theme\x01",
            "of independence throughout history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Discovering the common\x01",
            "points might connect events\x01",
            "elsewhere in history.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B6A")

    label("loc_2273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2486")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_239A")

    ChrTalk(
        0xFE,
        "A state independence proposal, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looking back at Crossbell history up to\x01",
            "the Middle Ages period... It's not such\x01",
            "a thing didn't happen in the past too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As we can understand by the\x01",
            "current situation, something like\x01",
            "that wasn't successful even once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2481")

    label("loc_239A")


    ChrTalk(
        0xFE,
        (
            "Nevertheless, these are times in which we\x01",
            "can't clearly say that it will be a failure \x01",
            "again since it's been like that until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will this proposal turn into a\x01",
            "movement that will shake the\x01",
            "continent? Or will it go well?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2481")

    Jump("loc_2B6A")

    label("loc_2486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_24A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A1")
    Call(0, 20)
    Jump("loc_24A4")

    label("loc_24A1")

    Call(0, 21)

    label("loc_24A4")

    Jump("loc_2B6A")

    label("loc_24A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_263A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2598")

    ChrTalk(
        0xFE,
        (
            "This kid was looking for\x01",
            "a book, so I helped her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, but how wonderful. To think\x01",
            "she has an interest in history\x01",
            "even though she's so small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To a student of history,\x01",
            "nothing could make me happier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2635")

    label("loc_2598")


    ChrTalk(
        0xFE,
        (
            "Ah, but how wonderful. To think\x01",
            "she has an interest in history\x01",
            "even though she's so small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To a student of history,\x01",
            "nothing could make me happier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2635")

    Jump("loc_2B6A")

    label("loc_263A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2815")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2667")
    Call(0, 7)
    Jump("loc_2810")

    label("loc_2667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2766")

    ChrTalk(
        0xFE,
        "The West Zemuria Trade Conference, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder how many years it's\x01",
            "been since we had a conference\x01",
            "of this scale in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, it's certain the events\x01",
            "of the next three days will go\x01",
            "down in "continental history."\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2810")

    label("loc_2766")


    ChrTalk(
        0xFE,
        (
            "It's certain that the events\x01",
            "of the next three days will go\x01",
            "down in "continental history."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be able to see one\x01",
            "scene of that history\x01",
            "like this is a true joy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2810")

    Jump("loc_2B6A")

    label("loc_2815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_283A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2832")
    Call(0, 7)
    Jump("loc_2835")

    label("loc_2832")

    Call(0, 8)

    label("loc_2835")

    Jump("loc_2B6A")

    label("loc_283A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2936")

    ChrTalk(
        0xFE,
        (
            "I don't know why, but I make amazing\x01",
            "research progress on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps it's because I can progress my research without\x01",
            "thinking of anything unnecessary because of the sound\x01",
            "of the rain... Anyway, I'm able to concentrate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B6A")

    label("loc_2936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2B6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA4")

    ChrTalk(
        0xFE,
        (
            "I'm a student at the autonomous\x01",
            "state of Leman university. \x01",
            "I research history there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, I attempted to\x01",
            "earn a doctorate twice before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The first time, my thesis was rejected and I\x01",
            "failed. The second time, I couldn't hand it\x01",
            "in during the term and failed by default. \x01",
            "...In other words, a splendid string of losses.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B6A")

    label("loc_2AA4")


    ChrTalk(
        0xFE,
        (
            "Right now, I'm polishing up my thesis\x01",
            "for another attempt next year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It's not the case that failing to earn a\x01",
            "doctorate means one's university studies\x01",
            "are over. I'm stubborn like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B6A")

    TalkEnd(0xFE)
    Return()

    # Function_6_1C59 end

    def Function_7_2B6E(): pass

    label("Function_7_2B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C40")

    ChrTalk(
        0xFE,
        (
            "You all investigated the \x01",
            "Tower of Stargaze, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think most of the books suddenly disappeared.\x01",
            "I wonder what happened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, thank goodness\x01",
            "some books were left.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CC1")

    label("loc_2C40")


    ChrTalk(
        0xFE,
        (
            "Anyway, thank goodness\x01",
            "some books were left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll tell Mr. Miles because\x01",
            "I too would like to examine\x01",
            "it in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC1")

    Return()

    # Function_7_2B6E end

    def Function_8_2CC2(): pass

    label("Function_8_2CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F04")

    ChrTalk(
        0xFE,
        (
            "It seems a large number of\x01",
            "ancient documents remain\x01",
            "at the Tower of Stargaze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, the condition of the books\x01",
            "doesn't seem that good, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, we can't continue to\x01",
            "overlook such important material\x01",
            "as we have up until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As someone who research history,\x01",
            "I resent the careless\x01",
            "management of the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(...It's as he says.\x01",
            "This hurts to hear...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(I guess. It's just, management\x01",
            "of the tower was left to that\x01",
            "previous Commander.)\x02\x03",
            "#00302F(We shouldn't worry over something\x01",
            "that can't be helped, right?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FCC")

    label("loc_2F04")


    ChrTalk(
        0xFE,
        (
            "It seems a large number of\x01",
            "ancient documents remain\x01",
            "at the Tower of Stargaze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, the condition of the books\x01",
            "doesn't seem that good, but... Anyway,\x01",
            "I want to have a look at them soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCC")

    Return()

    # Function_8_2CC2 end

    def Function_9_2FCD(): pass

    label("Function_9_2FCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3088")

    ChrTalk(
        0xFE,
        (
            "Abbie is anxious due to that\x01",
            "incident, so I was thinking\x01",
            "of reading him a book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if the standard\x01",
            ""Mark and the Witch of the\x01",
            "Deep Forest" would be good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A3F")

    label("loc_3088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3096")
    Jump("loc_3A3F")

    label("loc_3096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31C9")

    ChrTalk(
        0xFE,
        (
            "Mr. Dieter's address...\x01",
            "It was amazingly shocking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can hardly believe it. To think the two\x01",
            "major powers would nonchalantly conduct\x01",
            "a secret feud during this peace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To protect our children's future,\x01",
            "don't we have no choice but to\x01",
            "continue to claim independence?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32A9")

    label("loc_31C9")


    ChrTalk(
        0xFE,
        (
            "I can hardly believe it. To think the two\x01",
            "major powers would nonchalantly conduct\x01",
            "a secret feud during this peace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To protect our children's future,\x01",
            "don't we have no choice but to\x01",
            "continue to claim independence?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32A9")

    Jump("loc_3A3F")

    label("loc_32AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32BC")
    Jump("loc_3A3F")

    label("loc_32BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_33FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3382")

    ChrTalk(
        0xFE,
        (
            "It seems a terrible incident\x01",
            "happened in Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think there are\x01",
            "a lot of kids like\x01",
            "Abbie there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I hope everyone\x01",
            "is freed as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33F6")

    label("loc_3382")


    ChrTalk(
        0xFE,
        (
            "I think there are\x01",
            "a lot of kids like\x01",
            "Abbie there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I hope everyone\x01",
            "is freed as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F6")

    Jump("loc_3A3F")

    label("loc_33FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3420")

    ChrTalk(
        0xFE,
        "Hmm, let's see...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A3F")

    label("loc_3420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_347C")

    ChrTalk(
        0xFE,
        (
            "My, it's true. Mama\x01",
            "didn't notice too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe she went out shopping?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A3F")

    label("loc_347C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3516")

    ChrTalk(
        0xFE,
        (
            "It looks like KeA's enthusiastically\x01",
            "investigating something today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I guess it\x01",
            "can't be helped if\x01",
            "Abbie's jealous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A3F")

    label("loc_3516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_367F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3610")

    ChrTalk(
        0xFE,
        (
            "Our Abbie will be the right age\x01",
            "to go to Sunday School next year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because he loves books,\x01",
            "I think he'll be able to do\x01",
            "well in studying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. Thinking about stuff like this \x01",
            "might make me a doting parent.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_367A")

    label("loc_3610")


    ChrTalk(
        0xFE,
        (
            "I want to raise Abbie to\x01",
            "be cheerful and honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In short, there's nothing\x01",
            "else I wish for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367A")

    Jump("loc_3A3F")

    label("loc_367F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3769")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3727")

    ChrTalk(
        0xFE,
        "Uh uh, Abbie's quite clever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright. We'll take a\x01",
            "detour on the way home\x01",
            "and buy some ice cream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Really!? Yes!\x01",
            "I'm so happy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3764")

    label("loc_3727")


    ChrTalk(
        0xFE,
        (
            "Uh uh, then what\x01",
            "flavor do you want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm... Melon!\x02",
    )

    CloseMessageWindow()

    label("loc_3764")

    Jump("loc_3A3F")

    label("loc_3769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3869")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381B")

    ChrTalk(
        0xFE,
        (
            "Uh uh. Abbie is tired after seeing\x01",
            "the unveiling ceremony, and it\x01",
            "looks like he fell asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a peaceful expression...\x01",
            "It's really cute.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3864")

    label("loc_381B")


    ChrTalk(
        0xFE,
        (
            "Uh uh, seeing Abbie's\x01",
            "peaceful face like this... \x01",
            "It's really cute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3864")

    Jump("loc_3A3F")

    label("loc_3869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_38DE")

    ChrTalk(
        0xFE,
        (
            "This library is very\x01",
            "quiet and comfortable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, the smell of\x01",
            "old books is\x01",
            "calming somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A3F")

    label("loc_38DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_39DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_399D")

    ChrTalk(
        0xFE,
        "And as for Aidios' flowing tears...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(18, 0, 70, 0)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "They fell upon the ground, and\x01",
            "spread throughout the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The people could only watch the scene...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39D7")

    label("loc_399D")


    ChrTalk(
        0xFE,
        (
            "The people could only watch the scene...\x01",
            "And then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D7")

    Jump("loc_3A3F")

    label("loc_39DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F7")
    Call(0, 10)
    Jump("loc_3A3F")

    label("loc_39F7")


    ChrTalk(
        0xFE,
        (
            "My Abbie really\x01",
            "likes KeA.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, myself as well, of course.\x02",
    )

    CloseMessageWindow()

    label("loc_3A3F")

    TalkEnd(0xFE)
    Return()

    # Function_9_2FCD end

    def Function_10_3A43(): pass

    label("Function_10_3A43")


    ChrTalk(
        0xA,
        "My, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, it's sis KeA's big\x01",
            "brother and big sister!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hey, is sis KeA\x01",
            "coming today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAh, sorry. She's going\x01",
            "to Sunday School today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWe'll tell KeA you asked about her. \x01",
            "You'll just have to make do for today, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yeah, got it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Then, say hi\x01",
            "to sis KeA\x01",
            "for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FI see, so she's even popular\x01",
            "in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FYes, that's\x01",
            "KeA for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 0)
    Return()

    # Function_10_3A43 end

    def Function_11_3C06(): pass

    label("Function_11_3C06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C46")

    ChrTalk(
        0xFE,
        (
            "So excited... Mama,\x01",
            "hurry up and read it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C6")

    label("loc_3C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3C54")
    Jump("loc_41C6")

    label("loc_3C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3CA9")

    ChrTalk(
        0xFE,
        (
            "Hey, mama. They're saying\x01",
            "something outside.\x01",
            "I wonder what it is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C6")

    label("loc_3CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CB7")
    Jump("loc_41C6")

    label("loc_3CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D04")

    ChrTalk(
        0xFE,
        (
            "Hey mama... You don't\x01",
            "look so good. Did\x01",
            "something happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C6")

    label("loc_3D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D3C")

    ChrTalk(
        0xFE,
        (
            "Hey, mama. What do\x01",
            "those words mean?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C6")

    label("loc_3D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3E6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF6")

    ChrTalk(
        0xFE,
        (
            "Huh, sis KeA? \x01",
            "Just when did she leave?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, if I had noticed I'd\x01",
            "properly have said bye bye...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, we'll see each other again, so it's fine.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E68")

    label("loc_3DF6")


    ChrTalk(
        0xFE,
        (
            "Hmm, if I had noticed I'd\x01",
            "properly have said bye bye...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, we'll see each other again, so it's fine.\x02",
    )

    CloseMessageWindow()

    label("loc_3E68")

    Jump("loc_41C6")

    label("loc_3E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3ED1")

    ChrTalk(
        0xFE,
        (
            "Sis KeA's reads\x01",
            "books all by herself. \x01",
            "Amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I've got\x01",
            "to study too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C6")

    label("loc_3ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F54")

    ChrTalk(
        0xFE,
        (
            "I'm going to be going\x01",
            "to Sunday School like\x01",
            "sis KeA pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ehehe, I hope I see\x01",
            "her at Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C6")

    label("loc_3F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3FCE")

    ChrTalk(
        0xFE,
        (
            "You know, sis KeA said she had\x01",
            "something to research today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why you mustn't\x01",
            "interrupt her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C6")

    label("loc_3FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4066")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_404C")

    ChrTalk(
        0xFE,
        "...*zzz zzz*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey mama...\x01",
            "There were so many people...it was amazing...\x01",
            "...*mumble*...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4061")

    label("loc_404C")


    ChrTalk(
        0xFE,
        "...*zzz zzz*...\x02",
    )

    CloseMessageWindow()

    label("loc_4061")

    Jump("loc_41C6")

    label("loc_4066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410C")

    ChrTalk(
        0xFE,
        (
            "Mama, you say books\x01",
            "have a nice smell, but...\x01",
            "I don't get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, you always\x01",
            "have a way more delicate\x01",
            "and nicer smell, mama.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4134")

    label("loc_410C")


    ChrTalk(
        0xFE,
        (
            "Do books really\x01",
            "have a nice smell?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4134")

    Jump("loc_41C6")

    label("loc_4139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4171")

    ChrTalk(
        0xFE,
        "*thump thump*...and then, and then!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_41C6")

    label("loc_4171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_41C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418C")
    Call(0, 10)
    Jump("loc_41C6")

    label("loc_418C")


    ChrTalk(
        0xFE,
        (
            "Say hi to sis\x01",
            "KeA for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll be waiting here.\x02",
    )

    CloseMessageWindow()

    label("loc_41C6")

    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_3C06 end

    def Function_12_41CE(): pass

    label("Function_12_41CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_41DF")
    Call(0, 14)
    Jump("loc_422F")

    label("loc_41DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41F0")
    Call(0, 13)
    Jump("loc_422F")

    label("loc_41F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4201")
    Call(0, 14)
    Jump("loc_422F")

    label("loc_4201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_422C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4224")
    Call(0, 13)
    Jump("loc_4227")

    label("loc_4224")

    Call(0, 14)

    label("loc_4227")

    Jump("loc_422F")

    label("loc_422C")

    Call(0, 14)

    label("loc_422F")

    Return()

    # Function_12_41CE end

    def Function_13_4230(): pass

    label("Function_13_4230")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4331")

    ChrTalk(
        0x8,
        (
            "Today, it seems that the head librarian and\x01",
            "the others are trying to look into the ancient\x01",
            "documents discovered at the Tower of Stargaze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They have lively expressions\x01",
            "on their faces like that of \x01",
            "little boys. It was kind of cute.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43CF")

    label("loc_4331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_43CF")

    ChrTalk(
        0x8,
        (
            "If you are looking for the head\x01",
            "librarian, it seems he's discussing \x01",
            "something with Mr. Nielsen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even though break\x01",
            "time is already over...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43CF")

    TalkEnd(0x8)
    Return()

    # Function_13_4230 end

    def Function_14_43D3(): pass

    label("Function_14_43D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_440A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 7)), scpexpr(EXPR_END)), "loc_4406")
    Call(0, 32)
    Return()

    label("loc_4406")

    Call(0, 30)
    Return()

    label("loc_440A")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_45D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4524")

    ChrTalk(
        0xC,
        (
            "The city is more or less back to\x01",
            "normal, but... There're still\x01",
            "things to be worried about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think the appearance of that weird\x01",
            "huge tree couldn't have been helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'd like the citizens to\x01",
            "spend some time reading\x01",
            "at home and calm down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_45D1")

    label("loc_4524")


    ChrTalk(
        0xC,
        (
            "The city is more or less back to\x01",
            "normal, but... There're still\x01",
            "things to be worried about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'd like the citizens to\x01",
            "spend some time reading\x01",
            "at home and calm down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45D1")

    Jump("loc_5A6F")

    label("loc_45D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_48BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47FC")
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Oh, Lloyd...\x01",
            "You're safe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYou too, uncle.\x01",
            "What a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah, seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I was surprised when I heard you were\x01",
            "a wanted man, but... I believe it's\x01",
            "just a misunderstanding, and in you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "Uncle...\x01",
            "Thank you.\x02\x03",
            "#00001FThere's a lot of things I need to tell you,\x01",
            "but I don't have time for that right now.\x02\x03",
            "Please. For now, don't leave the building\x01",
            "until the situation outside has calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah... Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Lloyd, and you all as well.\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 4)
    Jump("loc_48B5")

    label("loc_47FC")


    ChrTalk(
        0xC,
        (
            "Actually, Mr. Nielsen had just\x01",
            "come to the library, and now\x01",
            "he's stuck here as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This has seriously turned into\x01",
            "an unthinkable situation...\x01",
            "Please be careful, all of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B5")

    Jump("loc_5A6F")

    label("loc_48BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4B2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A8C")

    ChrTalk(
        0xC,
        (
            "L-Lloyd. Did you hear\x01",
            "Mayor Dieter's address?\x01",
            "And about the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah, we were surprised by\x01",
            "that as well. There's a lot of\x01",
            "things we need to look into.\x02\x03",
            "Anyway, uncle. For now, I\x01",
            "want you to relax and just\x01",
            "watch the developments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "S-Sure, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There are a lot of worrying things,\x01",
            "but the first thing to do\x01",
            "is to just calm down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Do your best, Lloyd, and you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B25")

    label("loc_4A8C")


    ChrTalk(
        0xC,
        (
            "There are a lot of worrying things,\x01",
            "but the first one to do is to calm down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But, just why did Mr. Dieter put\x01",
            "forward such a strong policy...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B25")

    Jump("loc_5A6F")

    label("loc_4B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD6")

    ChrTalk(
        0xC,
        (
            "The charity event held by the\x01",
            "city and the Merchants\x01",
            "Associations looks rather lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm. I'll have to put in my own donation later.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4C73")

    label("loc_4BD6")


    ChrTalk(
        0xC,
        (
            "No matter what anyone says, the spirit of helping\x01",
            "each other is an indispensable part of humanity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm. I'll have to put in my own donation later.\x02",
    )

    CloseMessageWindow()

    label("loc_4C73")

    Jump("loc_5A6F")

    label("loc_4C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4D31")

    ChrTalk(
        0xC,
        (
            "I don't know who the armed group is, but...\x01",
            "Good grief, how utterly foolish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Something like ruling people by force...\x01",
            "It can't be forgiven, no mistake about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6F")

    label("loc_4D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4DC7")

    ChrTalk(
        0xC,
        "Hmm, it's raining outside, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So that moisture doesn't come in,\x01",
            "I've held off on entering the\x01",
            "basement archive for the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6F")

    label("loc_4DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4E4B")

    ChrTalk(
        0xC,
        (
            "My wife lunch box is well\x01",
            "done as usual today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Thanks to it, I'll be able to do my best this afternoon too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A6F")

    label("loc_4E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4EEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E66")
    Call(0, 15)
    Jump("loc_4EE9")

    label("loc_4E66")


    ChrTalk(
        0xC,
        (
            "*sigh*, I'll never forget the love she\x01",
            "puts into them, each and every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But, I'm glad my wife\x01",
            "came to bring it to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EE9")

    Jump("loc_5A6F")

    label("loc_4EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F09")
    Call(0, 20)
    Jump("loc_4F0C")

    label("loc_4F09")

    Call(0, 21)

    label("loc_4F0C")

    Jump("loc_5A6F")

    label("loc_4F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_50E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4F48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4F37")
    Call(0, 18)
    Jump("loc_4F43")

    label("loc_4F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_4F43")
    Call(0, 17)

    label("loc_4F43")

    Jump("loc_50E4")

    label("loc_4F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5030")

    ChrTalk(
        0xC,
        "Well, KeA is quite studious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm sorry we can only\x01",
            "lend three books to one\x01",
            "person at a time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, but I'll have to give a system\x01",
            "where more can be lent to frequent\x01",
            "users some serious thought.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_50E4")

    label("loc_5030")


    ChrTalk(
        0xC,
        (
            "I'm sorry we can only\x01",
            "lend three books to one\x01",
            "person at a time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, but I'll have to give a system\x01",
            "where more can be lent to frequent\x01",
            "users some serious thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50E4")

    Jump("loc_5A6F")

    label("loc_50E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_533A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5120")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_510F")
    Call(0, 18)
    Jump("loc_511B")

    label("loc_510F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_511B")
    Call(0, 17)

    label("loc_511B")

    Jump("loc_5335")

    label("loc_5120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5276")

    ChrTalk(
        0xC,
        (
            "Hmm, I only got a brief\x01",
            "look at the VIPs' faces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Among them, Prince Olivert\x01",
            "caught my attention the most.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "After helping resolve the incident\x01",
            "in Liberl, he used the "Arseille"\x01",
            "to return to the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In contrast, since the Blood and Iron\x01",
            "Chancellor shocks the world,\x01",
            "his every move has to be followed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5335")

    label("loc_5276")


    ChrTalk(
        0xC,
        (
            "If you ask me, Prince Olivert\x01",
            "commands the most attention\x01",
            "out of all the VIPs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In contrast, since the Blood and Iron\x01",
            "Chancellor shocks the world,\x01",
            "his every move has to be followed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5335")

    Jump("loc_5A6F")

    label("loc_533A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5368")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5357")
    Call(0, 18)
    Jump("loc_5363")

    label("loc_5357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_5363")
    Call(0, 17)

    label("loc_5363")

    Jump("loc_5A6F")

    label("loc_5368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_54F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5452")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_538F")
    Call(0, 16)
    Jump("loc_544D")

    label("loc_538F")


    ChrTalk(
        0xC,
        (
            "He won the Fulitzer Prize and\x01",
            "suddenly became famous. \x01",
            "It's been ten years since then, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't know when he's going\x01",
            "to leave the state again, but\x01",
            "I sure am glad he's back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_544D")

    Jump("loc_54EC")

    label("loc_5452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_54DE")

    ChrTalk(
        0xC,
        (
            "Hmm. Now that Mr. Nielsen's back, I'll need\x01",
            "to have a chat with him no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Now then, there's work to do...\x02",
    )

    CloseMessageWindow()
    Jump("loc_54EC")

    label("loc_54DE")

    Call(0, 26)
    TalkEnd(0xC)
    OP_93(0xC, 0x10E, 0x0)
    Return()

    label("loc_54EC")

    Jump("loc_5A6F")

    label("loc_54F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5744")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56DB")

    ChrTalk(
        0xC,
        (
            "A special guest is going to show\x01",
            "his face here, starting today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hu hu, I'm looking forward to speaking with him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FA special guest?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, a famous\x01",
            "international journalist\x01",
            "by the name of Nielsen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think he'll be here\x01",
            "in a little bit, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I you like, I'll introduce\x01",
            "him to all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FA famous international\x01",
            "journalist, huh... That does\x01",
            "seem pretty interesting.\x02\x03",
            "#00002FHmm. Then, we'll stop\x01",
            "by if we're free.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x133, 2)
    SetScenarioFlags(0x0, 4)
    Jump("loc_573F")

    label("loc_56DB")


    ChrTalk(
        0xC,
        (
            "Mr. Neilsen should\x01",
            "be here in a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I you like, I'll introduce\x01",
            "him to all of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_573F")

    Jump("loc_5A6F")

    label("loc_5744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5A6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A09")

    ChrTalk(
        0xC,
        "Oh, if it isn't Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You're here with your friends.\x01",
            "Does that mean the Special Support\x01",
            "Section has finally restarted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, thankfully.\x02\x03",
            "If you ever need anything,\x01",
            "we'd be happy to take care\x01",
            "of it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah, I'll be counting on you, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But even so, you guys look\x01",
            "more reliable than before.\x01",
            "I'm happy for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FAh, don't say that...\x01",
            "We still have a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. Personally, I think it would be\x01",
            "good if you had a little more pride.\x01",
            "That's why you're you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll be rooting for you.\x01",
            "Feel free to visit\x01",
            "my home as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FSure. \x01",
            "Thanks, uncle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F(Miss Cecil's father... \x01",
            "A very gentle man.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x133, 5)
    Jump("loc_5A6F")

    label("loc_5A09")


    ChrTalk(
        0xC,
        (
            "I'll be rooting for the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please feel free to\x01",
            "visit my home as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A6F")

    TalkEnd(0xC)
    Return()

    # Function_14_43D3 end

    def Function_15_5A73(): pass

    label("Function_15_5A73")


    ChrTalk(
        0xC,
        (
            "What is it, Leyte?\x01",
            "Do you need anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "My oh my. How rude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Uh uh, you forgot your lunchbox\x01",
            "so I brought it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh!? \x01",
            "I hadn't noticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sorry. Thanks\x01",
            "for bringing it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    Return()

    # Function_15_5A73 end

    def Function_16_5B4A(): pass

    label("Function_16_5B4A")


    ChrTalk(
        0xC,
        (
            "Hmm, Lloyd. It seems your\x01",
            "conversation is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Did you have a useful discussion?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, I guess. I definitely\x01",
            "learned something.\x02\x03",
            "#00000FBy the way uncle,\x01",
            "did you know Mr.\x01",
            "Nielsen before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah. Like me, Mr. Nielsen is \x01",
            "originally from Crossbell, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We became good friends when\x01",
            "he was working for Crossbell\x01",
            "News back in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, it seems he was\x01",
            "also pretty close with Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYeah, seems that way.\x02\x03",
            "#00003F(That seems similar to our\x01",
            "relationship with Miss Grace.)\x02\x03",
            "(...Of course, the mood is\x01",
            "totally different, though.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 6)
    Return()

    # Function_16_5B4A end

    def Function_17_5D97(): pass

    label("Function_17_5D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EC0")

    ChrTalk(
        0xC,
        (
            "Please investigate the "Tower of Stargaze"\x01",
            "on the outskirts of St. Ursula Byroad for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I heard that a great many ancient\x01",
            "documents were left there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I want you to look into the\x01",
            "cost required to collect\x01",
            "them with your own eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'll be counting on you, then.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5F80")

    label("loc_5EC0")


    ChrTalk(
        0xC,
        (
            "The Tower of Stargaze along St.\x01",
            "Ursula Byroad to the south, right\x01",
            "as you come out of the woods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please take care of investigating the ancient\x01",
            "documents that are in the tower for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F80")

    Return()

    # Function_17_5D97 end

    def Function_18_5F81(): pass

    label("Function_18_5F81")


    ChrTalk(
        0xC,
        (
            "It's really too bad that we\x01",
            "couldn't recover all of the\x01",
            "books from the tower, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even just having these\x01",
            "grimoires is quite valuable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks, Lloyd and friends. I'll be counting\x01",
            "on your help in the future as well.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_18_5F81 end

    def Function_19_606A(): pass

    label("Function_19_606A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_608E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_608A")
    Call(0, 28)
    Return()

    label("loc_608A")

    Call(0, 26)
    Return()

    label("loc_608E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6137")

    ChrTalk(
        0xFE,
        (
            "A sudden declaration of martial law...\x01",
            "One could say it's proof\x01",
            "the President is cornered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This oppression won't last\x01",
            "long... This is normal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61FE")

    label("loc_6137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_61E0")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(The strongest Jaeger corps on the continent...\x01",
            "Who could be behind them...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(It'd be easy to decide\x01",
            "it's the Empire, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61FE")

    label("loc_61E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_61FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61FB")
    Call(0, 20)
    Jump("loc_61FE")

    label("loc_61FB")

    Call(0, 21)

    label("loc_61FE")

    TalkEnd(0xFE)
    Return()

    # Function_19_606A end

    def Function_20_6202(): pass

    label("Function_20_6202")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "Hmm, it appears this grimoire\x01",
            "is a study of artifacts from\x01",
            "the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I see... And did\x01",
            "you learn anything\x01",
            "about its author?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes. There's no mistake that this\x01",
            "was left behind by the alchemists\x01",
            "who once built the "Tower", but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It doesn't seem like there's\x01",
            "any proof of their identities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well even so, there's no mistake\x01",
            "that this is valuable data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm. But it's really too bad that\x01",
            "this was all that was left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Also, there's a lot of mysteries regarding\x01",
            "the Middle Ages alchemists even today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We're not even sure if any document \x01",
            "connected to their identities even exists...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes, it's as you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. The fact that the books\x01",
            "completely disappeared only\x01",
            "deepens the mystery.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6587")

    ChrTalk(
        0x101,
        (
            "#00000F(Uncle... It looks like\x01",
            "they're researching the\x01",
            "books we found.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes. But it looks like they\x01",
            "haven't found anything new...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6587")

    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x16B, 4)
    Return()

    # Function_20_6202 end

    def Function_21_6593(): pass

    label("Function_21_6593")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Hmm. Middle Ages alchemists...\x01",
            "The mystery only deepens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, but this grimoire\x01",
            "is very interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Agreed. There's still room\x01",
            "for further analysis, so I'll\x01",
            "look into it a little more.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_21_6593 end

    def Function_22_666D(): pass

    label("Function_22_666D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_66C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_668B")
    Call(0, 15)
    Jump("loc_66C9")

    label("loc_668B")


    ChrTalk(
        0xFE,
        (
            "Uh uh, you do forget your\x01",
            "lunchbox sometimes, don't you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66C9")

    TalkEnd(0xFE)
    Return()

    # Function_22_666D end

    def Function_23_66CD(): pass

    label("Function_23_66CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_68A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66EB")
    Call(0, 25)
    Jump("loc_689E")

    label("loc_66EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6834")

    ChrTalk(
        0xE,
        (
            "#01105F...Ah, come to think of it, I forgot\x01",
            "to go shopping for dinner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha. There's still time\x01",
            "until evening, so relax.\x02\x03",
            "More importanty, make sure\x01",
            "you pick out a good get-\x01",
            "well book for Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01109FYeah. Thanks, Lloyd.\x02\x03",
            "#01110FI'll get those ingredients,\x01",
            "so look forward to it, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_689E")

    label("loc_6834")


    ChrTalk(
        0xE,
        (
            "#01103FHmm, a get-well\x01",
            "book for Shizuku.\x02\x03",
            "#01109F(*rustle*...) Yeah, this one\x01",
            "looks interesting too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_689E")

    Jump("loc_6AD7")

    label("loc_68A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6AD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68BE")
    Call(0, 24)
    Jump("loc_6AD7")

    label("loc_68BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A45")

    ChrTalk(
        0xE,
        (
            "#01109FLook at this, Lloyd. This book\x01",
            "has a picture of the huuuge\x01",
            "bell in Central Square.\x02\x03",
            "#01100FOriginally, that bell was at\x01",
            "the "Fort of Sun", it says.\x02\x03",
            "#01111FHmm, it's so big... I wonder\x01",
            "if carrying it here was tough?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Ha ha. It looks like KeA is\x01",
            "more curious than we thought.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F(Uh uh, I'm looking forward to\x01",
            "how she'll be in the future.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6AD7")

    label("loc_6A45")


    ChrTalk(
        0xE,
        (
            "#01100FThe big bell in Central square\x01",
            "was at the "Fort of Sun", it says.\x02\x03",
            "#01111FHmm, it's so big... I wonder\x01",
            "if carrying it here was tough?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AD7")

    TalkEnd(0xFE)
    Return()

    # Function_23_66CD end

    def Function_24_6ADB(): pass

    label("Function_24_6ADB")

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
        "#5P#01101FUmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#5P#01110FAh, this is it.\x01",
            "...Here we go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FKeA... Are you looking\x01",
            "for something?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#01109FAh, everyone.\x02\x03",
            "#01110FYeah, I was just collecting\x01",
            "books with folk tales.\x02\x03",
            "I read one and became\x01",
            "interested in them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FUm, let's see...\x02\x03",
            "#00105F"Crossbell Middle Ages History" and \x01",
            ""Looking at Crossbell's Past through Ruins"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FT-These aren't folk tales, they're\x01",
            "bona-fide history books and theses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00202FKeA, you are too amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FHa ha. Are you gonna be a researcher\x01",
            "or something when you grow up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01100FUmm, I wonder if KeA will be one?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu. It's rare to dote on\x01",
            "one's daughter this much.\x02",
        )
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

    # Function_24_6ADB end

    def Function_25_6EF2(): pass

    label("Function_25_6EF2")

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
        "#01110FAh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAre you reading a book, KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01109FYeah, I'm looking for\x01",
            "a book for Shizuku's\x01",
            "get-well present...\x02\x03",
            "#01111FWhat should I pick...?\x01",
            "A book like this seems\x01",
            "pretty interesting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThat shelf... Isn't that\x01",
            "the braille corner?\x02\x03",
            ""Seems pretty interesting"...\x01",
            "Can you read that, KeA?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01105FYup, I can...so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F"I can...so?",\x01",
            "you say that casually...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FDid you learn this in Sunday School?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01100FNo, I learned it when I\x01",
            "was playing with Shizuku.\x02\x03",
            "Books like "Mark and the Witch of the Deep\x01",
            "Forest" have been translated to braille\x01",
            "already, so it was pretty easy, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI feel like it might be fast even\x01",
            "for a book you already know, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FUh uh. This comprehension speed\x01",
            "is characteristic of KeA.\x02",
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

    # Function_25_6EF2 end

    def Function_26_734B(): pass

    label("Function_26_734B")

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
            "I see... That's an\x01",
            "interesting way to put it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_741A():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_741A)
    Sleep(50)
    TurnDirection(0xD, 0x102, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_END)), "loc_752D")

    ChrTalk(
        0xC,
        (
            "Oh, if it isn't Lloyd and\x01",
            "everyone. Good timing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The man I was just talking\x01",
            "to is Mr. Nielsen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FSo you're that journalist...\x02\x03",
            "#00000FUmm, how do you do. \x01",
            "I'm Lloyd Bannings of the Crossbell\x01",
            "Police Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_752D")


    ChrTalk(
        0xC,
        "Oh, if it isn't Lloyd and everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUncle, who is this person...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, he's Mr. Nielsen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He's a famous\x01",
            "international journalist.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "Mr. Nielsen, they're the\x01",
            "Special Support Section, and\x01",
            "subject of all the recent rumors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FUmm, how do you do.\x01",
            "I'm Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    label("loc_7667")


    ChrTalk(
        0xD,
        (
            "Hmm, that Special Support\x01",
            "Section. And you're their\x01",
            "leader, Mr. Lloyd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hu hu, you've got a nice clean voice.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00001FI'm sorry but... Are your eyes...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, it's from an old accident.\x01",
            "I lost my sight back then.\x02",
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
            "Head librarian, \x01",
            "so you are still here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Break time is already\x01",
            "over, you know?\x02",
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
            "I'm sorry, it seems I got\x01",
            "caught deep in talk again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "And so, I'm sorry. I've\x01",
            "got to get back to work...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)

    ChrTalk(
        0xD,
        (
            "Yeah. If you like, let's\x01",
            "exchange notes again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, please come\x01",
            "whenever you like.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    TurnDirection(0xD, 0x102, 500)

    ChrTalk(
        0xC,
        (
            "Then, Lloyd and everyone.\x01",
            "I leave the rest to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAh, sure...\x02",
    )

    CloseMessageWindow()

    def lambda_7984():
        OP_95(0x8, 24560, 4019, 80, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7984)
    OP_93(0xC, 0x0, 0x1F4)
    OP_95(0xC, 13110, 30, -2100, 2000, 0x0)

    def lambda_79B9():
        OP_95(0xC, 4570, 40, -1570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_79B9)
    Sleep(1000)
    OP_68(12280, 1000, -5990, 2000)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#00105FUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, let me introduce\x01",
            "myself once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "How do you do. I'm\x01",
            "Nielsen, a freelance\x01",
            "journalist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, nice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(Mr. Nielsen... \x01",
            "Where have I heard\x01",
            "this name before...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, I definitely wanted to\x01",
            "meet with the Support Section\x01",
            "at least once. What an honor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Sorry to start with a request,\x01",
            "but there's something I'd like\x01",
            "you all to do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Can I have some of your time?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FYes, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You see, right now \x01",
            "I'm investigating that\x01",
            "Cult incident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "There's several unclear\x01",
            "points in the data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'd like to interview all of you as\x01",
            "figures connected to and central to\x01",
            "the resolution of the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FA Cult incident interview, is it...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu. You speak as if you already\x01",
            "know a lot about it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Lloyd, what should we do?)\x02\x03",
            "(The data is what it is\x01",
            "and I think we can't\x01",
            "say too much...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(That's right...)\x02\x03",
            "#00003F(But by going along with this\x01",
            "interview, we might be able to sort\x01",
            "out the incident all over again...)\x02",
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

    # Function_26_734B end

    def Function_27_7E77(): pass

    label("Function_27_7E77")

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
            "Cooperate with Nielsen\x01",      # 0
            "Think About It For Now\x01",      # 1
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
        (0, "loc_7EF5"),
        (1, "loc_81E5"),
        (SWITCH_DEFAULT, "loc_82F6"),
    )


    label("loc_7EF5")


    ChrTalk(
        0x101,
        (
            "#00001FUnderstood. If you're okay with us,\x01",
            "please allow us to help.\x02\x03",
            "However...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I understand. Given your position, there\x01",
            "are some things that are hard to say. \x01",
            "I don't mind if you refuse to answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And as a general rule, your answers\x01",
            "today will be off the record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FI see... Thank you for\x01",
            "your understanding.\x02\x03",
            "#00005FBut what about the location. \x01",
            "Doing it here might be a problem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In that case, how about the\x01",
            "discussion space on 2F?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We'll know immediately if anyone comes,\x01",
            "so I think it's the perfect place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou're certainly right about that.\x01",
            "In that case, let's head there.\x02",
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
            "Quest [Cult Incident Coverage Assistance] \x07\x00",
            "started!\x02",
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
    Jump("loc_82F6")

    label("loc_81E5")


    ChrTalk(
        0x101,
        (
            "#00006FSorry. We have other cases\x01",
            "to deal with right now...\x02\x03",
            "#00001FIs it okay if we accept your request later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes. I'll be here awhile\x01",
            "longer so I don't\x01",
            "particularly mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Please come speak with me\x01",
            "when it's convenient for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82EE")
    EventEnd(0x5)

    label("loc_82EE")

    SetScenarioFlags(0x133, 3)
    Jump("loc_82F6")

    label("loc_82F6")

    Return()

    # Function_27_7E77 end

    def Function_28_82F7(): pass

    label("Function_28_82F7")

    TalkBegin(0xD)

    ChrTalk(
        0xD,
        "...You're Mr. Lloyd, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Care to join me for that\x01",
            "Cult incident interview?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Call(0, 27)
    TalkEnd(0xD)
    Return()

    # Function_28_82F7 end

    def Function_29_835C(): pass

    label("Function_29_835C")

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
            "#11PThank you very much for \x01",
            "joining me for this interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThen, let's begin by sorting\x01",
            "out the initial situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThe D∴G Cult, whose creed\x01",
            "was to reject the Goddess\x01",
            "and worship demons──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PSeveral decades ago, they serially\x01",
            "kidnapped young children from\x01",
            "all over the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PFirst I want to look at the\x01",
            "resolution of those kidnappings\x01",
            "by going back to six years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Back then, a large-scale operation was\x01",
            "conducted to expose and eliminate the\x01",
            "Cult lodges all over the continent, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PDo you all know the powers by which\x01",
            "that operation was carried out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6PYes, those were―\x02",
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
            "#1KThe powers that conducted the D∴G Cult\x01",
            "elimination operation six years ago were?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Military and Police from Several Nations\x01",      # 0
            "Bracer Guilds from Several Nations\x01",            # 1
            "Both of Them\x01",                                  # 2
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
        (0, "loc_8807"),
        (1, "loc_88AF"),
        (2, "loc_895B"),
        (SWITCH_DEFAULT, "loc_89C6"),
    )


    label("loc_8807")


    ChrTalk(
        0x101,
        (
            "#00000F#6PMilitary and police from several nations, right?\x02\x03",
            "#00006F...No, it wasn't just them.\x02\x03",
            "#00001FI heard Bracer Guilds from\x01",
            "several nations cooperated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C6")

    label("loc_88AF")


    ChrTalk(
        0x101,
        (
            "#00000F#6PBracer Guilds from several nations, right?\x02\x03",
            "#00006F...No, it wasn't just them.\x02\x03",
            "#00001FI heard military and police from\x01",
            "several nations cooperated too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C6")

    label("loc_895B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00001F#6PMilitary and police forces, and also\x01",
            "the Bracer Guilds from several nations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C6")

    label("loc_89C6")


    ChrTalk(
        0x102,
        (
            "#00100F#6PIndeed. Because of the scale of the\x01",
            "incident, an international committee\x01",
            "was formed to investigate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PYes, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAnd within that committee,\x01",
            "Bracer Cassius Bright took the\x01",
            "position of Supreme Commander―\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105F#6PE-Excuse me. \x01",
            "May I interrupt?\x02\x03",
            "#00101FThe man named Cassius Bright is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#12PC-Could you be talking about\x01",
            "Brigadier General Bright, Commander\x01",
            "of the Liberl Royal Army?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PYes, precisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PHe retired from the Royal Army\x01",
            "and was active for about 10 years as \x01",
            "a Bracer. Then, he rejoined the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHmm, that's a pretty\x01",
            "interesting career path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PT-That's true, but―\x02\x03",
            "#00108FI didn't realize it until now,\x01",
            "but that name "Bright" is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P―Yeah. I too was surprised when I realized\x01",
            "it while reviewing investigation documents\x01",
            "during my Section One training.\x02\x03",
            "#00001FCassius Bright is Estelle\x01",
            "Bright's real father.\x02\x03",
            "Joshua is his adopted son, though.\x02",
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
        "#00105F#6PI-I knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#12PAn unexpected connection...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PI thought she was quite something\x01",
            "during that chase battle, but...\x02\x03",
            "#10302FI never thought she was the\x01",
            "daughter of someone so famous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PHmm, so you know the daughter of\x01",
            "Brigadier General Bright, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAs a journalist, I'm aware\x01",
            "of her exploits, but...\x02",
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
        "#00002F#6PWell, we're connected in many ways.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PI'm sorry for having\x01",
            "interrupted you...\x02\x03",
            "#00100FPlease continue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PYes, well then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThen, at that time, the elimination\x01",
            "operation was carried out by the command\x01",
            "of Cassius Bright, a Bracer at that time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThat operation was thought to\x01",
            "have eliminated 90 percent of\x01",
            "the Cult's influence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBy the way, at that time,\x01",
            "the Sergei Squad of the Crossbell\x01",
            "Police participated in the operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PMr. Sergei, the current section chief\x01",
            "of the Special Support Section,\x01",
            "along with two others―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThat Arios MacLaine\x01",
            "and Mr. Lloyd's older\x01",
            "brother, Mr. Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P...It seems you've\x01",
            "deeply investigated\x01",
            "this case.\x02\x03",
            "#00008FAnd even the connection between big brother and I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6PIndeed. Even within the\x01",
            "police, they only know\x01",
            "part of the story, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PWell if you've been in the\x01",
            "business for as long as I have,\x01",
            "you develop a lot of connections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI've interviewed \x01",
            "Mr. Guy himself many\x01",
            "times, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P...Yes. Mr. Guys helped me in\x01",
            "various ways when he was alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P...Hmm.\x01",
            "Let's return to the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAfter that, there was another person\x01",
            "from Crossbell who became involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIt was Lawyer Ian\x01",
            "Grimwood, as a\x01",
            "civilian adviser.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PEven back then, Lawyer Ian\x01",
            "was famous for his knowledge\x01",
            "regarding civil rights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI heard he contributed to intelligence\x01",
            "gathering regarding the abductees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PCome to think of it,\x01",
            "he said that himself.\x02\x03",
            "#00100FI see, so that's how he cooperated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAlso, it was said that Church\x01",
            "officials and a mysterious\x01",
            "organization secretly intervened―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAnd because of that, the remaining Cult\x01",
            "influence was said to be eliminated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6P(Church officials, huh...)\x02",
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
            "#10101F#12P(It probably has something\x01",
            "to do with Father Kevin, who\x01",
            "we met at the Altair Lodge.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6P(And the mysterious organization\x01",
            "is probably that "Society".)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11P(Hu hu. Neither of them haven't been\x01",
            "pinned down, even to this day, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PHm...\x02",
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
            "#11PAnyhow― \x01",
            "The Cult incident should\x01",
            "have concluded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBut several months ago,\x01",
            "it became clear\x01",
            "that it had not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PAnd you too are aware of the reason...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYes. It was because of the\x01",
            "appearance of Dr. Joachim\x01",
            "Gｸnther, a Cult survivor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PYes, it's as you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIt seems he had knowledge of\x01",
            "the Cult's inner workings, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIn the end, was Joachim\x01",
            "Gｸnther the Cult leader?\x02",
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
            "#1KWas Joachim Gｸnther\x01",
            "the D∴G Cult leader?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Yes, He Was\x01",                         # 0
            "He Was One of the High Priests\x01",      # 1
            "He Was a Simple Cultist\x01",             # 2
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
        (0, "loc_9A7B"),
        (1, "loc_9B27"),
        (2, "loc_9B7B"),
        (SWITCH_DEFAULT, "loc_9C19"),
    )


    label("loc_9A7B")


    ChrTalk(
        0x101,
        (
            "#00001F#6PExactly. His position\x01",
            "was the Cult leader―\x02\x03",
            "#00011F(―That's not right.\x01",
            "What am I saying?)\x02\x03",
            "#00006F―That's not right. He was\x01",
            "one of the High Priests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C19")

    label("loc_9B27")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00001F#6PNo, that's incorrect. He was\x01",
            "one of the High Priests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C19")

    label("loc_9B7B")


    ChrTalk(
        0x101,
        (
            "#00001F#6PNo, he was a simple cultist―\x02\x03",
            "#00011F(―That's not right.\x01",
            "What am I saying?)\x02\x03",
            "#00006F―That's not right. He was\x01",
            "one of the High Priests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C19")

    label("loc_9C19")


    ChrTalk(
        0x102,
        (
            "#00103F#6PYes, he confirmed\x01",
            "that himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PHowever, he had a flair for research\x01",
            "and supervised many experiments.\x02\x03",
            "#00001FI think that's why he was familiar\x01",
            "with the Cult's inner workings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PHmm, a reasonable theory.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAnd, from that position of his, he used\x01",
            "results from rituals performed all over\x01",
            "the continent to further his research...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PHaving succeeded in evading\x01",
            "the exposition operation six\x01",
            "years ago, he hid himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThen, at the facility called "Paradise", he\x01",
            "seized upon former Chairman Hartmann's\x01",
            "weakness and escaped to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThen, he finally completed\x01",
            ""Gnosis", a drug whose\x01",
            "name means "True Wisdom".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI don't know the particulars, but...\x01",
            "He did it to fulfill the Cult's ambition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PThe Cult's ambition...\x02\x03",
            "#00108F(Indeed, he did say\x01",
            "it was to make KeA\x01",
            "a "God", but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6P(Yeah, it also seems that Joachim\x01",
            "could see something when he\x01",
            "assumed the red Gnosis, but...)\x02\x03",
            "#00006F(In the end, we didn't' learn\x01",
            "any of those details.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P...Hmm. As always, there's\x01",
            "many unclear points, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI think we've outlined\x01",
            "most of what happened\x01",
            "in the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBut finally, the roots of\x01",
            "the D∴G Cult's origin―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIs it alright if we\x01",
            "discuss those?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PThe Cult's roots...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PYes. By the way Mr. Lloyd, about\x01",
            "how many years ago are the Cult's\x01",
            "roots thought to stretch back to?\x02",
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
            "#1KHow many years ago are the D∴G Cult's\x01",
            "roots thought to stretch back?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "1200 Years Ago\x01",      # 0
            "500 Years Ago\x01",       # 1
            "50 Years Ago\x01",        # 2
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
        (0, "loc_A279"),
        (1, "loc_A35F"),
        (2, "loc_A3B5"),
        (SWITCH_DEFAULT, "loc_A487"),
    )


    label("loc_A279")


    ChrTalk(
        0x101,
        (
            "#00008F#6P(1200 years ago...? No.\x01",
            "Though it's possible,\x01",
            "I don't think that's it.)\x02\x03",
            "#00003F(Based on everything we know\x01",
            "so far, the answer definitely is...)\x02\x03",
            "#00001FMost likely 500 years ago―\x01",
            "To Crossbell's Middle Ages.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A487")

    label("loc_A35F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00001F#6PMost likely 500 years ago―\x01",
            "To Crossbell's Middle Ages.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A487")

    label("loc_A3B5")


    ChrTalk(
        0x101,
        (
            "#00011F#6P(50 years ago...? No, it\x01",
            "shouldn't be that recent.)\x02\x03",
            "#00003F(Based on everything we know so\x01",
            "far, the answer definitely is...)\x02\x03",
            "#00001FMost likely 500 years ago―\x01",
            "To Crossbell's Middle Ages.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A487")

    label("loc_A487")


    ChrTalk(
        0xD,
        "#11PHmm, and why is that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P...Actually, we heard this\x01",
            "from Joachim himself.\x02\x03",
            "#00008F500 years ago, there was a group\x01",
            "of alchemists in this land―\x02\x03",
            "#00001FThe Cult used the technology\x01",
            "of those days, he said...\x02\x03",
            "#00006FSince then, their ancestors\x01",
            "have become unknown, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI see, so Joachim\x01",
            "Gｸnther said all that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThe alchemists that once existed in this\x01",
            "land― In other words, the same ones\x01",
            "who built the "Tower of Stargaze".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PTo think that handed down knowledge\x01",
            "would've been backed in this way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#12PHu hu, that's certainly surprising.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PHmm, and the girl\x01",
            "that was entrusted\x01",
            "to you all―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PCould you believe that\x01",
            "girl is from back then too?\x02",
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
        "#00013F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PJust how much do you\x01",
            "know about the incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PSorry, that remark\x01",
            "lacked a little tact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PCombining my information\x01",
            "with yours gave me a\x01",
            "sudden "wild idea".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI swear on the Goddess\x01",
            "I won't broadcast it,\x01",
            "so please relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PN-No...\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#11P...Hmm. I suppose this about\x01",
            "does it for this interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThank you very much \x01",
            "for your help today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI was able to obtain some useful\x01",
            "information thanks to you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6P...No, it's the same for us too.\x02",
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
            "#11PWhile we were doing this, it's arrived\x01",
            "the time for me to be heading to my\x01",
            "next interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PIf you'll excuse me, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI'd love to speak with you all again, \x01",
            "should the opportunity arise.\x02",
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

    def lambda_AB1F():
        OP_95(0xD, 28680, 4019, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_AB1F)
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

    def lambda_AB68():
        OP_95(0xD, 9240, -490, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_AB68)
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
            "#10105F#12PI don't know what you guys were talking\x01",
            "about, but he's rather carefree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300F#11PHmm, he's really something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PHow to say this...\x01",
            "He's a surprising man, in many ways.\x02\x03",
            "#00000FAnd with regard to the matter of\x01",
            "KeA, it seems we can trust him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5PRight...\x02",
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
        "#00105F#5PAh!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)

    ChrTalk(
        0x101,
        "#00005F#12PWhat is it, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PI just remembered. That man\x01",
            "just now was Marcel Nielsen―\x02\x03",
            "He's a famous journalist\x01",
            "from Crossbell who won the\x01",
            "Fulitzer Prize 10 years ago.\x02",
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
            "#10305F#11PWow. I don't know too much about these\x01",
            "things, but the Fulitzer Prize...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYeah, it's an international award\x01",
            "conferred on the most outstanding\x01",
            "journalist each year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PI see... So that's where his\x01",
            "insight comes from, eh?\x02\x03",
            "#10105FBut if he's from Crossbell, that means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PYes, he was once\x01",
            "a reporter for\x01",
            "Crossbell News.\x02\x03",
            "#00108FAnd the coverage for which he\x01",
            "won the award― Was war coverage\x01",
            "in which he lost his sight.\x02\x03",
            "#00100FBut after that, he continued covering\x01",
            "news throughout the continent,\x01",
            "contributing to many news magazines.\x02\x03",
            "#00104FHe's famous among journalists―\x01",
            "He's that kind of person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHmm. In that case, he's an\x01",
            "unthinkably big deal, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PMr. Nielsen, huh...\x02\x03",
            "#00000FI'd like to speak with him\x01",
            "again if we get another chance.\x02",
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
            "Quest [Cult Incident Coverage Assistance] \x07\x00",
            "completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B20F")
    OP_2C(0x6E, 0x2)
    Jump("loc_B223")

    label("loc_B20F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B223")
    OP_2C(0x6E, 0x1)

    label("loc_B223")

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

    # Function_29_835C end

    def Function_30_B28C(): pass

    label("Function_30_B28C")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3B4")
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
    Jump("loc_B413")

    label("loc_B3B4")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_B413")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FGood day, uncle Miles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hi, Lloyd.\x01",
            "Could it be that you came\x01",
            "because you saw my request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYeah, that's it exactly.\x02\x03",
            "Can you tell us\x01",
            "the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt was about wanting to collect ancient documents\x01",
            "remaining in the Tower of Stargaze, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You know about the "Tower of\x01",
            "Stargaze" ruins on the outskirts\x01",
            "of St. Ursula Byroad, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For awhile now, investigation has been\x01",
            "prohibited by the Guardian Force, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But lately, investigations are\x01",
            "allowed with special permission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FThat is indeed\x01",
            "the case, lately.\x02\x03",
            "#10100FThe previous Commander left\x01",
            "that place uninvestigated.\x02\x03",
            "For gathering information, even\x01",
            "regular citizens are permitted entry\x01",
            "on the condition they file a report...\x02\x03",
            "Because it seems the monsters\x01",
            "have disappeared recently, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, is that right...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B8D1")

    ChrTalk(
        0xC,
        (
            "Yes, and Mr. Nielsen\x01",
            "went in to investigate\x01",
            "the other day, he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And it seems he found\x01",
            "some interesting things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat reporter...\x02\x03",
            "#00005FB-But Mr. Nielsen's\x01",
            "eyes were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, that's right, but...\x01",
            "That was when he was taken along\x01",
            "by a Crossbell Times reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ah, what a dynamic guy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBA0")

    label("loc_B8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_END)), "loc_BA54")

    ChrTalk(
        0xC,
        (
            "Yes, and Mr. Nielsen\x01",
            "went in to investigate\x01",
            "the other day, he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And it seems he found\x01",
            "some interesting things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Nielsen... \x01",
            "He's that journalist you were\x01",
            "telling us about, uncle.\x02\x03",
            "Going specifically to\x01",
            "cover a place like that.\x01",
            "What a dynamic guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah. Actually,\x01",
            "he's blind, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems a Crossbell Times\x01",
            "reporter took him there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBA0")

    label("loc_BA54")


    ChrTalk(
        0xC,
        (
            "Yes, and the other day, my\x01",
            "journalist friend, Mr. Nielsen,\x01",
            "went there to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And it seems he found\x01",
            "some interesting things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWow, going to that sort of\x01",
            "place to investigate? Mr.\x01",
            "Niesen seems very dynamic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah. Actually,\x01",
            "he's blind, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems a Crossbell Times\x01",
            "reporter took him there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBA0")


    ChrTalk(
        0x105,
        (
            "#10300FAnd regarding the "interesting\x01",
            "things" found, those are the "ancient\x01",
            "documents" mentioned in the request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FOh right... I feel like\x01",
            "I saw them when we were\x01",
            "chasing after "Yin".\x02",
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
            "#00300FThere were enormous\x01",
            "bookshelves halfway up the\x01",
            "tower and on the top floor.\x02\x03",
            "The ancient documents you're\x01",
            "looking for must be there.\x02",
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
            "Oh, you went there already, did you?\x01",
            "This'll be quick then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The library can't consider\x01",
            "leaving such valuable ancient\x01",
            "documents in a place like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "How about it? Can I count on you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThat's indeed an important\x01",
            "function of the library, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FBut...isn't it impossible for us\x01",
            "to transport such a huge quantity\x01",
            "of books with just ourselves?\x02\x03",
            "#10106FI wonder how many trips it'll\x01",
            "take us to get them all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FT-That's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, of course I've no intention\x01",
            "of asking you to do all that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To prepare for transporting the documents,\x01",
            "I want all of you to investigate the labor\x01",
            "and expense that will be required.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've already secured permission for your\x01",
            "investigation from the Guardian Force and City Hall.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0F9")

    ChrTalk(
        0x103,
        "#00202FI see, so that's how it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FAnd based on the investigation results,\x01",
            "you'll proceed with a plan to collect the books.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C17B")

    label("loc_C0F9")


    ChrTalk(
        0x105,
        (
            "#10304FI see. So that's it.\x02\x03",
            "#10300FAnd based on the investigation results,\x01",
            "you'll proceed with a plan to collect the books.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C17B")


    ChrTalk(
        0x102,
        (
            "#00100FWe're certainly\x01",
            "qualified, having climbed\x01",
            "the "Tower" once before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "How about it? Will you accept?\x02",
    )

    CloseMessageWindow()
    OP_29(0x71, 0x1, 0x0)
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C209")
    Call(0, 33)

    label("loc_C209")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C243")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_C24D")

    label("loc_C243")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_C24D")

    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_B28C end

    def Function_31_C265(): pass

    label("Function_31_C265")

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
            "Accept\x01",      # 0
            "Quit\x01",        # 1
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
        (0, "loc_C2C1"),
        (1, "loc_C2C6"),
        (SWITCH_DEFAULT, "loc_C36A"),
    )


    label("loc_C2C1")

    Jump("loc_C36A")

    label("loc_C2C6")


    ChrTalk(
        0x101,
        (
            "#00000FSorry uncle.\x01",
            "Now we're\x01",
            "a little busy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, I see. It can't\x01",
            "be helped, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, if you get\x01",
            "free, please come\x01",
            "speak with me again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x152, 7)
    Jump("loc_C36A")

    label("loc_C36A")

    Return()

    # Function_31_C265 end

    def Function_32_C36B(): pass

    label("Function_32_C36B")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51115.itc", 0x1E)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C467")
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
    Jump("loc_C4C6")

    label("loc_C467")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_C4C6")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "I'd like you all to investigate\x01",
            "the ancient documents that were\x01",
            "left in the "Tower of Stargaze".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To prepare to collect them, I want to know\x01",
            "what kind of cost and effort will be required.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "How about it? Will you accept?\x02",
    )

    CloseMessageWindow()
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5CE")
    Call(0, 33)

    label("loc_C5CE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C608")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_C612")

    label("loc_C608")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_C612")

    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_C36B end

    def Function_33_C62A(): pass

    label("Function_33_C62A")


    ChrTalk(
        0x101,
        (
            "#00002FYeah, got it.\x01",
            "We'll take it on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Thank you. This really helps me out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "One moment please. \x01",
            "I'll contact the Guardian Force and\x01",
            "have them remove the blockade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FOh, please leave\x01",
            "that to me then.\x02\x03",
            "It'll be faster if I contact\x01",
            "Commander Sonya personally.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C749():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C749)
    Sleep(50)

    def lambda_C759():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C759)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C784")

    def lambda_C779():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C779)
    Sleep(50)

    label("loc_C784")


    def lambda_C789():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C789)
    Sleep(50)

    def lambda_C799():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C799)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FYeah, that seems\x01",
            "like a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ooh, then please do.\x02",
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
    SetChrName("Sonya's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Yes, this is Commander\x01",
            "Sonya of the Guardian Force.\x02",
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
            "#10100FThank you for your hard work, Commander.\x01",
            "This is Noｱl Seeker speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sonya's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, Noｱl.\x01",
            "Has something happened?\x02",
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
            "#10103FYes, actually...\x02",
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
            "Noｱl explained they took on\x01",
            "the tower investigation request.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sonya's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, that matter.\x02\x03",
            "We know about the request too. \x01",
            "You all are certainly qualified.\x01\x02\x03",
            "We'll remove the blockade\x01",
            "immediately. I'll contact\x01",
            "our unit in the area.\x02",
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
            "#10101FThank you very much, ma'am!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sonya's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Be very careful.\x01",
            "...Then, I'll excuse myself\x07\x00\x02",
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
        "#10100F...Ok, all set.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FThanks Noｱl.\x02",
    )

    CloseMessageWindow()

    def lambda_CBAA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CBAA)
    Sleep(50)

    def lambda_CBBA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CBBA)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CBE5")

    def lambda_CBDA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CBDA)
    Sleep(50)

    label("loc_CBE5")


    def lambda_CBEA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CBEA)
    Sleep(50)

    def lambda_CBFA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CBFA)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Yes, that\x01",
            "went smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The Support Section sure\x01",
            "knows all the right people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, that's right.\x02\x03",
            "Then, shall we head for\x01",
            "the Tower of Stargaze?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, let's.\x02\x03",
            "#00002FUncle Miles, please look\x01",
            "forward to our results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I will. Take care.\x02",
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
            "Quest [Ancient Documents Investigation]\x07\x00",
            " started!\x02",
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

    # Function_33_C62A end

    def Function_34_CD93(): pass

    label("Function_34_CD93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE5C")
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
    Jump("loc_CEBB")

    label("loc_CE5C")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_CEBB")

    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others reported that the\x01",
            "books on the shelves had disappeared.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00003F...So, that's what happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "N-No way! You're saying\x01",
            "someone took that many books?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And what's more, they were\x01",
            "taken without anyone noticing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...It's unfortunate, but we have\x01",
            "no idea what happened to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Well, I suppose it can't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wanted to at least find out what\x01",
            "kind of books they were, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FAh, well actually there were a few\x01",
            "books remaining on the shelves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FThose were the only ones we were\x01",
            "able to collect, you see...\x02\x03",
            "You might be able to get at least some clue\x01",
            "about the other books by examining these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "R-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt's just, the content\x01",
            "is unintelligible to us.\x02\x03",
            "I have no idea\x01",
            "how valuable\x01",
            "they're, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Handed over the books\x01",
            "collected in the tower.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "T-These are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSomehow, they appear to be\x01",
            "books from the Middle Ages.\x02\x03",
            "They're old and stained,\x01",
            "though it might be possible\x01",
            "to make out the characters.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0x109,
        "#10105FW-What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I-Incredible... \x01",
            "This...and this too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "These are grimoires from the Middle Ages!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FGrimoires...you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Instructions on how to use\x01",
            "alchemy and magic tools,\x01",
            "recorded by someone long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I won't know for sure until I decode them,\x01",
            "but from the schematics alone, \x01",
            "there's no mistake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FWow... They seem like\x01",
            "pretty valuable books.\x02\x03",
            "#00003FBut, the fact that they\x01",
            "were still there means...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D570")

    ChrTalk(
        0x103,
        (
            "#00200FThey weren't that important\x01",
            "to the one who took the\x01",
            "rest of them, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIt seems difficult to get any clue\x01",
            "about them just from these books, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D615")

    label("loc_D570")


    ChrTalk(
        0x105,
        (
            "#10300FThey weren't that important\x01",
            "to the one who took the\x01",
            "rest of them... right?\x02\x03",
            "It seems difficult to get any clue\x01",
            "about them just from these books, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D615")


    ChrTalk(
        0x101,
        "#00001FRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FAn inexplicable mystery remains...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, no. That doesn't change\x01",
            "the fact that you collected\x01",
            "a few valuable books for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Good work everyone. \x01",
            "I knew I could count on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FAhaha. It was our pleasure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll carefully store these books\x01",
            "in the basement archives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll be able to study them\x01",
            "with Mr. Nielsen and others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks, Lloyd and friends. I'll be counting\x01",
            "on your help in the future as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAh, yes. \x01",
            "We'll be waiting.\x02",
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
            "Quest [Ancient Documents Investigation]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D899")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_D8A3")

    label("loc_D899")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_D8A3")

    OP_29(0x71, 0x1, 0x5)
    OP_29(0x71, 0x1, 0x6)
    OP_29(0x71, 0x4, 0x10)
    SetScenarioFlags(0x0, 5)
    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_34_CD93 end

    def Function_35_D8CF(): pass

    label("Function_35_D8CF")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D9DF")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　～Library News～\x01",
            "To answer your requests, the\x01",
            "books below have been added.\x01",
            "  ・Back-Alley Dr. Glenn Vol. 13\x01",
            "  ・Back-Alley Dr. Glenn Vol. 14\x01",
            "※These are on the 1F shelves.\x01",
            "  Interested persons, please have a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_DE9D")

    label("loc_D9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DB29")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　～Library News～\x01",
            "To answer your requests, the\x01",
            "books below have been added.\x01",
            "  ・Back-Alley Dr. Glenn Vol. 9\x01",
            "  ・Back-Alley Dr. Glenn Vol. 10\x01",
            "  ・Back-Alley Dr. Glenn Vol. 11\x01",
            "  ・Back-Alley Dr. Glenn Vol. 12\x01",
            "※These are on the 1F shelves.\x01",
            "  Interested persons, please have a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_DE9D")

    label("loc_DB29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DC14")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　～Library News～\x01",
            "To answer your requests, the\x01",
            "book below has been added.\x01",
            "  ・One Minute Cooking - Sweets Edition\x01",
            "※This is on the 1F shelves.\x01",
            "  Interested persons, please have a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_DE9D")

    label("loc_DC14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DD5B")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　～Library News～\x01",
            "To answer your requests, the\x01",
            "books below have been added.\x01",
            "  ・Back-Alley Dr. Glenn Vol. 5\x01",
            "  ・Back-Alley Dr. Glenn Vol. 6\x01",
            "  ・Back-Alley Dr. Glenn Vol. 7\x01",
            "  ・Back-Alley Dr. Glenn Vol. 8\x01",
            "※These are on the 1F shelves.\x01",
            "  Interested persons, please have a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_DE9D")

    label("loc_DD5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DE9D")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　～Library News～\x01",
            "To answer your requests, the\x01",
            "books below have been added.\x01",
            "  ・Back-Alley Dr. Glenn Vol. 1\x01",
            "  ・Back-Alley Dr. Glenn Vol. 2\x01",
            "  ・Back-Alley Dr. Glenn Vol. 3\x01",
            "  ・Back-Alley Dr. Glenn Vol. 4\x01",
            "※These are on the 1F shelves.\x01",
            "  Interested persons, please have a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_DE9D")

    EventEnd(0x3)
    Return()

    # Function_35_D8CF end

    def Function_36_DEA0(): pass

    label("Function_36_DEA0")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Mark and the Witch of the Deep Forest] is on the shelf.\x02",
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
            "[Read First Volume]\x01",       # 0
            "[Read Second Volume]\x01",      # 1
            "[Read Last Volume]\x01",        # 2
            "[Quit]\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF68")
    UseItem(0x2D6, 0xFF)

    label("loc_DF68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF7C")
    UseItem(0x2DD, 0xFF)

    label("loc_DF7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF90")
    UseItem(0x2DE, 0xFF)

    label("loc_DF90")

    TalkEnd(0xFF)
    Return()

    # Function_36_DEA0 end

    def Function_37_DF94(): pass

    label("Function_37_DF94")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Beauties that Moved the Continent] is on the shelf.\x02",
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
            "[Read the Book]\x01",      # 0
            "[Quit]\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E022")
    UseItem(0x2D7, 0xFF)

    label("loc_E022")

    TalkEnd(0xFF)
    Return()

    # Function_37_DF94 end

    def Function_38_E026(): pass

    label("Function_38_E026")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[How to Use 5 Extra Minutes Effectively] is on the shelf.\x02",
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
            "[Read the Book]\x01",      # 0
            "[Quit]\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0B9")
    UseItem(0x2D8, 0xFF)

    label("loc_E0B9")

    TalkEnd(0xFF)
    Return()

    # Function_38_E026 end

    def Function_39_E0BD(): pass

    label("Function_39_E0BD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Railway Mania Recommendations] is on the shelf.\x02",
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
            "[Read the Book]\x01",      # 0
            "[Quit]\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E147")
    UseItem(0x2D5, 0xFF)

    label("loc_E147")

    TalkEnd(0xFF)
    Return()

    # Function_39_E0BD end

    def Function_40_E14B(): pass

    label("Function_40_E14B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Strange and Wonderful Crossbell,\x01",
            "The Complete Works] is on the shelf.\x02",
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
            "[Read the Book]\x01",      # 0
            "[Quit]\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1EB")
    UseItem(0x2D9, 0xFF)

    label("loc_E1EB")

    TalkEnd(0xFF)
    Return()

    # Function_40_E14B end

    def Function_41_E1EF(): pass

    label("Function_41_E1EF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[The Saint and the White Wolf] is on the shelf.\x02",
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
            "[Read First Volume]\x01",      # 0
            "[Read Last Volume]\x01",       # 1
            "[Quit]\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E299")
    UseItem(0x2DF, 0xFF)

    label("loc_E299")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2AD")
    UseItem(0x2E0, 0xFF)

    label("loc_E2AD")

    TalkEnd(0xFF)
    Return()

    # Function_41_E1EF end

    def Function_42_E2B1(): pass

    label("Function_42_E2B1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Arc-en-ciel Fanbook] is on the shelf.\x02",
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
            "[Read the Book]\x01",      # 0
            "[Quit]\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E331")
    UseItem(0x2DA, 0xFF)

    label("loc_E331")

    TalkEnd(0xFF)
    Return()

    # Function_42_E2B1 end

    def Function_43_E335(): pass

    label("Function_43_E335")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E34C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E859")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 1")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[IBC]\x01",       # 0
            "[ZCF]\x01",       # 1
            "[Quit]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5F5")
    SetChrName("")
    MenuTitle(-1, 25, 0, "IBC (International Bank of Crossbell)")
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An abbreviation for "International Bank of Crossbell".\x01",
            "A megabank that manages and invests enormous wealth,\x01",
            "gathered from throughout the continent. It has supported for\x01",
            "many years not only Crossbell, but also the international\x01",
            "monetary circulation and the economic market.\x02\x03",
            "In addition to development of investment activity and\x01",
            "financial products, they handle management of a theme park\x01",
            "among other things. In addition, they also supply the funds\x01",
            "for the "Epstein Foundation Orbal Network Project".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E5F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E854")
    MenuTitle(-1, 25, 0, "ZCF (Zeiss Central Factory)")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An abbreviation for "Zeiss Central Factory".\x01",
            "Based in Liberl Kingdom's city of Zeiss, their\x01",
            "predecessor was the "Zeiss Technology Factory",\x01",
            "established in joint with the Zeiss Clockmaker\x01",
            "Association by Professor A. Russell, personal pupil\x01",
            "of Professor Epstein, the orbments inventor.\x02\x03",
            "They are the first company to successfully develop an orbal\x01",
            "airship, and are the leading orbal equipment maker on the\x01",
            "continent. In recent years, they completed the "Arseille",\x01",
            "a high-speed cruiser used by the Liberl Royal Army.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E854")

    Jump("loc_E34C")

    label("loc_E859")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_43_E335 end

    def Function_44_E866(): pass

    label("Function_44_E866")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E87D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F447")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 2")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Arc-en-ciel]\x01",                 # 0
            "[Holy Nation of Arteria]\x01",      # 1
            "[Verne Corporation]\x01",           # 2
            "[Erebonian Empire]\x01",            # 3
            "[Epstein Foundation]\x01",          # 4
            "[Quit]\x01",                        # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAB7")
    MenuTitle(-1, 25, 0, "Arc-en-Ciel")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An internationally famous troupe in\x01",
            "the autonomous state of Crossbell.\x02\x03",
            "Their acrobatic performances and\x01",
            "magnificent and passionate plays\x01",
            "continue to draw large audiences.\x02\x03",
            "Known by the stage name "Flame Dancer",\x01",
            "currently featured actress Ilya Platiｲre\x01",
            "is especially popular and has many crazy\x01",
            "fans even in foreign countries.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EAB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECD7")
    MenuTitle(-1, 25, 0, "Holy Nation of Arteria")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The city-state that is the HQ of the Septian Church.\x01",
            "Located in the central part of the Zemuria Continent,\x01",
            "it is known as a holy place where believers and\x01",
            "religious officials from all over the continent gather.\x02\x03",
            "Various organizations exist there, such as the\x01",
            ""Congregation for Divine Worship" that supervises\x01",
            "most rituals, the "Congregation for the Sacraments",\x01",
            "said to manage the Goddess' sacraments, and the\x01",
            ""Papal Guard", in charge of the city defense.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ECD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEE7")
    MenuTitle(-1, 25, 0, "Verne Company")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Large integrated technology manufacturer\x01",
            "with their base in the Calvard Republic.\x02\x03",
            "Though, forming a pair with the Erebonian Empire's\x01",
            "Reinford Corporation, they are a well-established arms\x01",
            "manufacturer that have researched and developed\x01",
            "all kinds of orbal goods since orbments were invented.\x02\x03",
            "Above all, regarding their orbal driving vehicles field,\x01",
            "starting with orbal buses, they develop many goods\x01",
            "from private cars to special railroad vehicles.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EEE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F24E")
    MenuTitle(-1, 25, 0, "Erebonian Empire")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Situated to the west of Crossbell State, a gigantic\x01",
            "empire with the "Golden Stallion" as its symbol.\x01",
            "The current emperor is Eugent Reise Arnor.\x02\x03",
            "The country is ruled by an ancient system of noble families,\x01",
            "but under the command of Chancellor Giliath Osborne,\x01",
            "also known as the "Blood and Iron Chancellor", who came \x01",
            "up through the military, the railway network was spread out \x01",
            "in the whole nation, modernizing it.\x02\x03",
            "In addition to the regular military mechanization, he\x01",
            "preserved the great military might of the nobles' families\x01",
            "private armies which has strained relations with foreign\x01",
            "countries.\x02\x03",
            "Furthermore, the emperor's son, Prince Olivert, cooperated\x01",
            "in the resolution of the phenomenon that happened in Liberl\x01",
            "last year. In the Empire, it has become a popular topic of\x01",
            "conversation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F24E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F442")
    MenuTitle(-1, 25, 0, "Epstein Foundation")
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Foundation that inherited the achievements of\x01",
            "Professor C. Epstein, genius orbal scholar and inventor\x01",
            "of orbments. As a research institution and manufacturer,\x01",
            "they are conspicuous in the fields of communication and\x01",
            "data processing.\x02\x03",
            "In addition to manufacturing "Tactical Orbments"\x01",
            "that can invoke Arts, they have put effort into the\x01",
            ""Orbal Network Project", developing communication\x01",
            "and data processing technologies.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F442")

    Jump("loc_E87D")

    label("loc_F447")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_44_E866 end

    def Function_45_F454(): pass

    label("Function_45_F454")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F46B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10013")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 3")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Phantom Thief B]\x01",                    # 0
            "[Calvard Republic]\x01",                   # 1
            "[Autonomous State Of Crossbell]\x01",      # 2
            "[Crystal Circuits/Quartz]\x01",            # 3
            "[Ancient Relics/Artifacts]\x01",           # 4
            "[Quit]\x01",                               # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F811")
    MenuTitle(-1, 25, 0, "Phantom Thief B")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Great phantom thief who is active all over the continent.\x01",
            "From jewels to orbal tanks, and regardless of the\x01",
            "country or person, he has carried out many thefts.\x01",
            "Because of his brilliant and splendid criminal techniques,\x01",
            "he is also famous for having earned himself some\x01",
            "enthusiastic fans.\x02\x03",
            "He sends messages to various places detailing his plans,\x01",
            "sometimes showing himself with a mask and clad in a\x01",
            "white cloak, but his true identity is shrouded in mystery.\x01",
            "In recent years, he himself spoke of a "Liberation Movement\x01",
            "of Beauty". Although he unexpectedly performed them in the\x01",
            "Erebonian Empire, his magnificent series of crimes gave rise\x01",
            "to new topics of discussion.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F811")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9FF")
    MenuTitle(-1, 25, 0, "Calvard Republic")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Republic set to the east of the autonomous state\x01",
            "of Crossbell. It became a democracy about one\x01",
            "hundred years ago.\x01",
            "The current ruler is President Rocksmith.\x02\x03",
            "Possessing a vast territory, it has a\x01",
            "diverse cultural background due to \x01",
            "accepting immigrants from the East.\x02\x03",
            "Though after signing the Non-Aggression Pact\x01",
            "they hae calmed down, historically, conflicts with\x01",
            "the Erebonian Empire have occurred many a time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F9FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC3A")
    MenuTitle(-1, 25, 0, "Crossbell State")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Autonomous state situated in the west part of the\x01",
            "Zemuria continent. Located between the two major\x01",
            "powers of the Erebonian Empire and Calvard Republic,\x01",
            "though there were fierce territorial conflicts, it was\x01",
            "established as an autonomous state 70 years ago.\x02\x03",
            "In present day, the central Crossbell City has grown\x01",
            "into the continent most prominent, huge trade city. It has\x01",
            "a transcontinental railroad connecting the Empire and the\x01",
            "Republic and is an international periodic airship relay\x01",
            "point.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD81")
    MenuTitle(-1, 25, 0, "Crystal Circuits/Quartz")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Circuits with a crystalline structure of refined\x01",
            "and processed "Sepith", fragments of Septium.\x02\x03",
            "They are energy sources as well as devices that\x01",
            "cause different phenomenons, however they do\x01",
            "not exhibit effects if not set into an orbment.\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1000E")
    MenuTitle(-1, 25, 0, "Ancient Relics/Artifacts")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Orbments of an ancient civilization. Though they\x01",
            "operate using the orbments same orbal power, the\x02\x03",
            "principles of operation are different. Said to have been\x01",
            "created during the "Ancient Zemurian Civilization",\x01",
            "analysis is considered impossible given current technology.\x02\x03",
            "Rarely discovered in ruins across the continent,\x01",
            "they exhibit powers surpassing even current\x01",
            "human understand to no small degree.\x02\x03",
            "For this reason, for the Septian Church Artifacts are\x01",
            "defined as "Premature Gifts from the Goddess," and it is\x01",
            "said they have the duty to collect and manage them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1000E")

    Jump("loc_F46B")

    label("loc_10013")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_45_F454 end

    def Function_46_10020(): pass

    label("Function_46_10020")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10037")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1044B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 4")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Septian Church]\x01",      # 0
            "[Septium]\x01",             # 1
            "[Quit]\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10267")
    MenuTitle(-1, 25, 0, "Septian Church")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The religious organization devoted to the "Sky Goddess\x01",
            "Aidios", who is most widely worshipped on the continent.\x01",
            "Its High Seat is in the Holy Nation of Arteria.\x02\x03",
            "Though its influence declined after the orbal revolution,\x01",
            "it is strongly influential in the continent even now.\x01",
            "Through the fields of scholarship, education and medical\x01",
            "care, they are in a position of instructing the masses.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10267")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10446")
    MenuTitle(-1, 25, 0, "Septium")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A group of seven types of precious stones distributed \x01",
            "throughout the continent. Since ancient times, they were \x01",
            "highly valued as gemstones and mystic symbols.\x02\x03",
            "In present day, due to technology invented to make\x01",
            "Quartz by processing and refining the fragments\x01",
            "too small to be turned into jewels called "Sepith",\x01",
            "the importance of Septium resources has suddenly \x01",
            "risen in each country across the continent.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10446")

    Jump("loc_10037")

    label("loc_1044B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_46_10020 end

    def Function_47_10458(): pass

    label("Function_47_10458")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1046F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E7C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 5")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Great Collapse]\x01",         # 0
            "[Fisherman's Guild]\x01",      # 1
            "[Orbal Revolution]\x01",       # 2
            "[Orbments]\x01",               # 3
            "[Quit]\x01",                   # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10679")
    MenuTitle(-1, 25, 0, "Great Collapse")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is the collapse of the Ancient Zemurian Civilization\x01",
            "thought to have occurred approximately 1200 years ago.\x01",
            "Though the cause was said to have been a cataclysm,\x01",
            "the details are unknown.\x02\x03",
            "After the civilization was lost because of the "Great\x01",
            "Collapse", the people went through a long period of\x01",
            ""Dark Ages".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10679")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1088A")
    MenuTitle(-1, 25, 0, "Fisherman's Guild")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A group of fishing professionals acting\x01",
            "to popularize fishing culture.\x01",
            "Originally a noble and fishing lover,\x01",
            "Mr. H. Fisher founded it and set up HQ\x01",
            "in Liberl Kingdom's Grancel City.\x02\x03",
            "They search, investigate and develop fishing spots, and\x01",
            "also, discover talents and train new-generation fishermen.\x01",
            "Furthermore, in recent years, they have engaged in develop-\x01",
            "ment of fishing tools and baits. Each year, they broaden\x01",
            "the scope of their activities.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1088A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C34")
    MenuTitle(-1, 25, 0, "Orbal Revolution")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is the continent-scale technological\x01",
            "revolution caused by the development\x01",
            "of orbments almost fifty years ago.\x02\x03",
            "In spite of the groundbreaking invention, the people\x01",
            "of those days met orbments with skepticism. However,\x01",
            "as the Epstein Foundation orbal communication devices\x01",
            "and the ZCF's orbally-powered airship went out into the\x01",
            "world, the usefulness of orbments was acknowledged\x01",
            "throughout the continent.\x02\x03",
            "Nowadays, from heating, lighting and daily necessities\x01",
            "to rail and airships, tanks, guns and weapons,\x01",
            "everything you can think of has become orbally-powered.\x01",
            "Orbments have already become an indispensable\x01",
            "thing to people.\x02\x03",
            "In recent years, together with miniaturization of orbally-\x01",
            "powered machines, Verne Corp. and Reinford Corp. have\x01",
            "continued to develop high efficiency orbally-driven cars and\x01",
            "they have begun to spread through the common class.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10C34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E77")
    MenuTitle(-1, 25, 0, "Orbments")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Generic term for machines developed by\x01",
            "Professor C. Epstein which draw out orbal\x01",
            "power from Septium, producing various effects.\x02\x03",
            "The orbment's internal structure and gear\x01",
            "movements cause the crystal circuits of\x01",
            "processed Septium to mutually interfere,\x01",
            "causing a countless number of effects to manifest.\x02\x03",
            "In addition to their usefulness and effect variation,\x01",
            ""with time, the internal orbal power recovers." For this\x01",
            "reason, orbments have far higher economic efficiency\x01",
            "than burning or internal combustion.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10E77")

    Jump("loc_1046F")

    label("loc_10E7C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_47_10458 end

    def Function_48_10E89(): pass

    label("Function_48_10E89")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10EA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113A4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 6")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Orbal Arts]\x01",                 # 0
            "[Orbal Network Project]\x01",      # 1
            "[Eastern District]\x01",           # 2
            "[Quit]\x01",                       # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11054")
    MenuTitle(-1, 25, 0, "Orbal Arts")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By inserting Quartz in specially designed\x01",
            ""Tactical Orbments" by the Epstein\x01",
            "Foundation, "Magic" can be invoked.\x02\x03",
            "Generally called "Arts," with training,\x01",
            "anyone can use these techniques, making\x01",
            "them popular in the CGF, police and Guild.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11054")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111FE")
    MenuTitle(-1, 25, 0, "Orbal Network Project")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An innovative information network project\x01",
            "promoted by the Epstein Foundation.\x01",
            "With terminals connected by orbal cables it is\x01",
            "possible to exchange vast quantities of information.\x02\x03",
            "Though originally developed together with Liberl's ZCF,\x01",
            "currently, the IBC has started to provide funds for a\x01",
            "full-scale trial installation in Crossbell City.\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_111FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1139F")
    MenuTitle(-1, 25, 0, "Eastern District")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Large-scale district built up by people of\x01",
            "Eastern descent in the Calvard Republic.\x01",
            "Various cultures, people and goods come and go, and it has\x01",
            "been called "the intersection of East and West cultures."\x02\x03",
            "Though exotic buildings stand in rows and it is\x01",
            "famous as a tourist attraction, there are rumors\x01",
            "of a large syndicate of Easterners.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1139F")

    Jump("loc_10EA0")

    label("loc_113A4")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_48_10E89 end

    def Function_49_113B1(): pass

    label("Function_49_113B1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_113C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A1D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 7")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Hundred Days War]\x01",         # 0
            "[Non-Aggression Pact]\x01",      # 1
            "Quit]\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11796")
    MenuTitle(-1, 25, 0, "Hundred Days War")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A war between the Erebonian Empire and Liberl\x01",
            "Kingdom in year 1192 of the Septian Calendar.\x01",
            "It is called like this because it ended in\x01",
            "approximately one hundred days between\x01",
            "the Empire's declaration of war and the\x01",
            "mediation by the Septian Church.\x02\x03",
            "At first, Liberl was forced into an inferior position.\x01",
            "Though most of the country was occupied by\x01",
            "Empire troops, at the same time, a cutting-edge defense\x01",
            "airship was used in a shocking counteroffensive strategy.\x01",
            "In the blink of an eye, the war situation was reversed.\x02\x03",
            "As for the original reason for the outbreak of\x01",
            "war, because both countries kept their silence,\x01",
            "in the end it was not brought to light, but the\x01",
            "Imperial government later wrote in its official\x01",
            "apology to Liberl that it had been "due to an\x01",
            "unfortunate misunderstanding."\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11796")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A18")
    MenuTitle(-1, 25, 0, "Non-Aggression Pact")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "International treaty entered into by Liberl Kingdom,\x01",
            "the Erebonian Empire and the Calvard Republic\x01",
            "in year 1202 of the Septian Calendar.\x01",
            "It was proposed by Queen Alicia of Liberl\x01",
            "and signed at Erbe Royal Villa in the same country.\x02\x03",
            "There is no legal compelling force in the treaty, but after\x01",
            "entering into it, the developing large-scale military\x01",
            "exercises on the outskirts of the autonomous state of\x01",
            "Crossbell by both the Empire and Republic were broken up,\x01",
            "greatly easing the state of tension. It could be said\x01",
            "the effects of the treaty were materialized.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11A18")

    Jump("loc_113C8")

    label("loc_11A1D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_49_113B1 end

    def Function_50_11A2A(): pass

    label("Function_50_11A2A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11A41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F23")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 8")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Michelam]\x01",          # 0
            "[Bracer Guild]\x01",      # 1
            "[Quit]\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C29")
    MenuTitle(-1, 25, 0, "Michelam")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "High class health resort situated southeast of Elm Lake.\x01",
            "Since IBC started work on the project two years ago,\x01",
            "a resort hotel and theme park have been constructed\x01",
            "and it has become equal to a popular spot.\x02\x03",
            "Even the local mascot character called\x01",
            ""Michey" is gaining a lot of popularity\x01",
            "from the citizens and the tourists.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11C29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F1E")
    MenuTitle(-1, 25, 0, "Bracer Guild")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Nongovernmental organization of "Bracers" who\x01",
            "work to protect regional peace and protect civilians.\x01",
            "Because of the branches in various places on the\x01",
            "continent, the influence they have is not small.\x02\x03",
            "Though their ideal is to protect civilians above all\x01",
            "else, they have a weakness due to their organization\x01",
            "code that, as long as civilian safety is not threatened,\x01",
            "they cannot exercise the rights of investigation and\x01",
            "arrest towards the state and public authorities.\x02\x03",
            "As for Crossbell, because of the happening of many\x01",
            "international incidents, they have assembled capable\x01",
            "people, starting with the "Divine Blade of Wind", Arios\x01",
            "MacLaine, and they have earned the citizens' support.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11F1E")

    Jump("loc_11A41")

    label("loc_11F23")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_50_11A2A end

    def Function_51_11F30(): pass

    label("Function_51_11F30")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11F47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AA1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 9")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Reinford Corporation]\x01",           # 0
            "[Principality of Remiferia]\x01",      # 1
            "[Autonomous State of Leman]\x01",      # 2
            "[Liberl Kingdom]\x01",                 # 3
            "[Jaegers]\x01",                        # 4
            "[Quit]\x01",                           # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121FF")
    MenuTitle(-1, 25, 0, "Reinford Corporation")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Large integrated technology manufacturer\x01",
            "based in the Erebonian Empire.\x01",
            "It was originally an arms workshop specializing\x01",
            "in guns and heavy weapons using gunpowder.\x02\x03",
            "Since the development of orbments, they have\x01",
            "turned their hands towards not only orbal guns and\x01",
            "weapons but also orbal rail and airships.\x01",
            "Together with the "Verne Corporation" of the Calvard\x01",
            "Republic, it has grown to call itself one of the world's\x01",
            "two large manufacturers.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_121FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1248F")
    MenuTitle(-1, 25, 0, "Principality of Remiferia")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A principality situated in the north part of the Zemuria\x01",
            "continent. Although a rigid northern country, it is\x01",
            "blessed with abundant forests and lakes, many\x01",
            "people visit with the goal of sightseeing, charmed\x01",
            "by those scenic beauty landscapes.\x02\x03",
            "Also famous for its advanced medical care,\x01",
            "representatives from the continent's medical equipment\x01",
            "makers are concentrated there, and it has turned out many\x01",
            "excellent doctors. Additionally, the autonomous state of \x01",
            "Crossbell's St. Ursula Medical College was established \x01",
            "with cooperation from the Principality of Remiferia.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1248F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125F0")
    MenuTitle(-1, 25, 0, "Autonomous State of Leman")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An autonomous state in the central part of the Zemuria\x01",
            "continent. The HQ of the Epstein Foundation is there,\x01",
            "as well as the hometown of Professor C. Epstein.\x02\x03",
            "Additionally, it is also famous for the Bracer Guild HQ\x01",
            "with its branches everywhere on the continent.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_125F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1290E")
    MenuTitle(-1, 25, 0, "Liberl Kingdom")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Kingdom located in the southwest part of the Zemuria\x01",
            "continent. It is a long-established country colored in\x01",
            "rich nature, currently under the rule of elderly Queen\x01",
            "Alicia II, maintaining a proud peace.\x02\x03",
            "Though its national power is inferior to surrounding\x01",
            "countries, through its abundant Septium resources,\x01",
            "excellent technology and skillful foreign policy, it has\x01",
            "built relationships on an equal footing.\x02\x03",
            "Last year, a mysterious gigantic structure (details\x01",
            "unknown) appeared in Valleria Lake in the center of the\x01",
            "kingdom. Though a strange phenomenon where all orbments\x01",
            "in the country stopped functioning occurred, through the\x01",
            "work of the army and the Bracer Guild, the matter was\x01",
            "resolved peacefully, restoring order.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1290E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A9C")
    MenuTitle(-1, 25, 0, "Jaegers")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Among active mercenary units in the continent, a title\x01",
            "used to identify the especially excellent among them.\x02\x03",
            "Their scale and objectives are flexible according to the\x01",
            "contract. Because you can expect high fighting strength,\x01",
            "they are often used as private armies, and there are\x01",
            "countries where their use is prohibited by law.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12A9C")

    Jump("loc_11F47")

    label("loc_12AA1")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_51_11F30 end

    def Function_52_12AAE(): pass

    label("Function_52_12AAE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Volumes of [Back-Alley Dr. Glenn] are on the shelf.\x02",
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
            "[Read Volume 13]\x01",      # 0
            "[Read Volume 14]\x01",      # 1
            "[Quit]\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B57")
    UseItem(0x2D2, 0xFF)

    label("loc_12B57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B6B")
    UseItem(0x2D3, 0xFF)

    label("loc_12B6B")

    TalkEnd(0xFF)
    Return()

    # Function_52_12AAE end

    def Function_53_12B6F(): pass

    label("Function_53_12B6F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Volumes of [Back-Alley Dr. Glenn] are on the shelf.\x02",
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
            "[Read Volume 9]\x01",       # 0
            "[Read Volume 10]\x01",      # 1
            "[Read Volume 11]\x01",      # 2
            "[Read Volume 12]\x01",      # 3
            "[Quit]\x01",                # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C39")
    UseItem(0x2CE, 0xFF)

    label("loc_12C39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C4D")
    UseItem(0x2CF, 0xFF)

    label("loc_12C4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C61")
    UseItem(0x2D0, 0xFF)

    label("loc_12C61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C75")
    UseItem(0x2D1, 0xFF)

    label("loc_12C75")

    TalkEnd(0xFF)
    Return()

    # Function_53_12B6F end

    def Function_54_12C79(): pass

    label("Function_54_12C79")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Volumes of [Back-Alley Dr. Glenn] are on the shelf.\x02",
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
            "[Read Volume 5]\x01",      # 0
            "[Read Volume 6]\x01",      # 1
            "[Read Volume 7]\x01",      # 2
            "[Read Volume 8]\x01",      # 3
            "[Quit]\x01",               # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D40")
    UseItem(0x2CA, 0xFF)

    label("loc_12D40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D54")
    UseItem(0x2CB, 0xFF)

    label("loc_12D54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D68")
    UseItem(0x2CC, 0xFF)

    label("loc_12D68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D7C")
    UseItem(0x2CD, 0xFF)

    label("loc_12D7C")

    TalkEnd(0xFF)
    Return()

    # Function_54_12C79 end

    def Function_55_12D80(): pass

    label("Function_55_12D80")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Volumes of [Back-Alley Dr. Glenn] are on the shelf.\x02",
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
            "[Read Volume 1]\x01",      # 0
            "[Read Volume 2]\x01",      # 1
            "[Read Volume 3]\x01",      # 2
            "[Read Volume 4]\x01",      # 3
            "[Quit]\x01",               # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E47")
    UseItem(0x2C6, 0xFF)

    label("loc_12E47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E5B")
    UseItem(0x2C7, 0xFF)

    label("loc_12E5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E6F")
    UseItem(0x2C8, 0xFF)

    label("loc_12E6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E83")
    UseItem(0x2C9, 0xFF)

    label("loc_12E83")

    TalkEnd(0xFF)
    Return()

    # Function_55_12D80 end

    SaveToFile()

Try(main)
