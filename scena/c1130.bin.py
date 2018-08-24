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
        "Function_5_DD1",          # 05, 5
        "Function_6_1C2B",         # 06, 6
        "Function_7_2AFE",         # 07, 7
        "Function_8_2C49",         # 08, 8
        "Function_9_2F4C",         # 09, 9
        "Function_10_395D",        # 0A, 10
        "Function_11_3B04",        # 0B, 11
        "Function_12_4086",        # 0C, 12
        "Function_13_40E8",        # 0D, 13
        "Function_14_426D",        # 0E, 14
        "Function_15_58C7",        # 0F, 15
        "Function_16_5996",        # 10, 16
        "Function_17_5BCE",        # 11, 17
        "Function_18_5DB8",        # 12, 18
        "Function_19_5E8B",        # 13, 19
        "Function_20_601F",        # 14, 20
        "Function_21_63AB",        # 15, 21
        "Function_22_6489",        # 16, 22
        "Function_23_64E8",        # 17, 23
        "Function_24_68D4",        # 18, 24
        "Function_25_6CDB",        # 19, 25
        "Function_26_7132",        # 1A, 26
        "Function_27_7C61",        # 1B, 27
        "Function_28_80E3",        # 1C, 28
        "Function_29_8144",        # 1D, 29
        "Function_30_AF97",        # 1E, 30
        "Function_31_BF11",        # 1F, 31
        "Function_32_C022",        # 20, 32
        "Function_33_C2DF",        # 21, 33
        "Function_34_C9B5",        # 22, 34
        "Function_35_D4DF",        # 23, 35
        "Function_36_DA6A",        # 24, 36
        "Function_37_DB60",        # 25, 37
        "Function_38_DBF4",        # 26, 38
        "Function_39_DC8D",        # 27, 39
        "Function_40_DD1D",        # 28, 40
        "Function_41_DDC3",        # 29, 41
        "Function_42_DE89",        # 2A, 42
        "Function_43_DF0F",        # 2B, 43
        "Function_44_E410",        # 2C, 44
        "Function_45_EF8B",        # 2D, 45
        "Function_46_FB44",        # 2E, 46
        "Function_47_FF73",        # 2F, 47
        "Function_48_10987",       # 30, 48
        "Function_49_10EB8",       # 31, 49
        "Function_50_11524",       # 32, 50
        "Function_51_11A27",       # 33, 51
        "Function_52_12581",       # 34, 52
        "Function_53_12647",       # 35, 53
        "Function_54_12756",       # 36, 54
        "Function_55_12862",       # 37, 55
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
            "The "One Minute Cooking\x01",
            "- Sweets Edition" is\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_DCD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Light\x01",
            "Popcorn"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_DCD")

    TalkEnd(0xFF)
    Return()

    # Function_4_D0F end

    def Function_5_DD1(): pass

    label("Function_5_DD1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBD")

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
            "...*sigh*, as expected,\x01",
            "there aren't many\x01",
            "visitors today.\x02",
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
    Jump("loc_F2E")

    label("loc_EBD")


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
            "As the librarian, it's\x01",
            "my duty to have faith in\x01",
            "our borrowers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2E")

    Jump("loc_1C27")

    label("loc_F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FE4")

    ChrTalk(
        0xFE,
        (
            "I feel fear, the same as\x01",
            "when those jaegers came\x01",
            "to attack us before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why did something like this\x01",
            "have to happen? ...I'm filled\x01",
            "with feelings like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C27")

    label("loc_FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10ED")

    ChrTalk(
        0xFE,
        (
            ""Crossbell Independent State"...\x01",
            "I feel we've finally arrived at a\x01",
            "place where we cannot turn back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of attitude the major powers\x01",
            "will take, having received the announcement. To\x01",
            "be honest, I'm full of anxiety about this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C27")

    label("loc_10ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121E")

    ChrTalk(
        0xFE,
        (
            "The night of the attack,\x01",
            "I finished work and had\x01",
            "just left, but...\x02",
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
            "An entire week has passed since then,\x01",
            "but... I can't forget the fires that\x01",
            "raged in the city that night.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12D5")

    label("loc_121E")


    ChrTalk(
        0xFE,
        (
            "An entire week has passed since then,\x01",
            "but... I can't forget the fires that\x01",
            "raged in the city that night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it was a\x01",
            "warning regarding the\x01",
            "independence proposal...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D5")

    Jump("loc_1C27")

    label("loc_12DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1377")

    ChrTalk(
        0xFE,
        (
            "I suppose it's only natural,\x01",
            "but the people over at\x01",
            "police HQ are flustered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope the Mainz\x01",
            "incident's resolved\x01",
            "peacefully, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C27")

    label("loc_1377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1458")

    ChrTalk(
        0xFE,
        (
            "I heard that a citizen's\x01",
            "forum is being held at\x01",
            "City Meeting Hall today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The question of state\x01",
            "independence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The referendum's\x01",
            "approaching. I'll need to\x01",
            "make up my mind before long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14AD")

    label("loc_1458")


    ChrTalk(
        0xFE,
        (
            "The question of state\x01",
            "independence... I'll need to\x01",
            "make up my mind before long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AD")

    Jump("loc_1C27")

    label("loc_14B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_15F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156B")

    ChrTalk(
        0xFE,
        (
            "Umm, this is a science\x01",
            "book, so it goes on the\x01",
            "shelf over there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Why is returning books\x01",
            "to the gaps in the shelves\x01",
            "this much fun, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15EC")

    label("loc_156B")


    ChrTalk(
        0xFE,
        (
            "Returning books to the\x01",
            "gaps in the shelves is a\x01",
            "bit like a puzzle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It feels good putting\x01",
            "books in just the right\x01",
            "spot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15EC")

    Jump("loc_1C27")

    label("loc_15F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_177E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DC")

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
            "Now, if you tell me a\x01",
            "book that's on loan, I\x01",
            "can reserve it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please feel free to ask\x01",
            "either myself or the head\x01",
            "librarian about it anytime.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1779")

    label("loc_16DC")


    ChrTalk(
        0xFE,
        (
            "Now, if you tell me a\x01",
            "book that's on loan, I\x01",
            "can reserve it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please feel free to ask\x01",
            "either myself or the head\x01",
            "librarian about it anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1779")

    Jump("loc_1C27")

    label("loc_177E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_178C")
    Jump("loc_1C27")

    label("loc_178C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_182A")

    ChrTalk(
        0xFE,
        (
            "I heard the heads of state\x01",
            "stayed at the Michelam state\x01",
            "guest house last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm sure they had\x01",
            "wonderful and delicious\x01",
            "food.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C27")

    label("loc_182A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18BE")

    ChrTalk(
        0xFE,
        (
            "Thanks to the trade\x01",
            "conference, there's a\x01",
            "festival-like mood in the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm excited to see\x01",
            "what they're going to\x01",
            "do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C27")

    label("loc_18BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C8")

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
            "If possible, I'd like to\x01",
            "collect all of them,\x01",
            "but...\x02",
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
    Jump("loc_1A59")

    label("loc_19C8")


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

    label("loc_1A59")

    Jump("loc_1C27")

    label("loc_1A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_1B07")

    ChrTalk(
        0xFE,
        (
            "As a freelance journalist,\x01",
            "Nielsen has been busy flying\x01",
            "all over the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that today is\x01",
            "his first trip home in\x01",
            "around three years.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C27")

    label("loc_1B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1BA0")

    ChrTalk(
        0xFE,
        (
            "That head librarian. He's\x01",
            "restless today just\x01",
            "because Nielsen is coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, it seems he likes\x01",
            "talking with Nielsen\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C27")

    label("loc_1BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C27")

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
            "If you are looking for\x01",
            "some book, please feel\x01",
            "free to ask me anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C27")

    TalkEnd(0xFE)
    Return()

    # Function_5_DD1 end

    def Function_6_1C2B(): pass

    label("Function_6_1C2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C3C")
    Jump("loc_2AFA")

    label("loc_1C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D99")

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
    Jump("loc_1E30")

    label("loc_1D99")


    ChrTalk(
        0xFE,
        (
            "This library is indispensable\x01",
            "when it comes to researching\x01",
            "Crossbell's history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before long, a lab in\x01",
            "Lｳman might be a good\x01",
            "addition, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E30")

    Jump("loc_2AFA")

    label("loc_1E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1F77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFC")

    ChrTalk(
        0xFE,
        (
            "The attack on Mainz...\x01",
            "To think it's occupied,\x01",
            "even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was it the Empire's doing? Or the\x01",
            "Republic's? To put it bluntly, it's\x01",
            "likely the doing of one of them...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F72")

    label("loc_1EFC")


    ChrTalk(
        0xFE,
        (
            "No matter by the Empire\x01",
            "or Republic, Mainz is\x01",
            "attack material.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got to think along\x01",
            "those lines, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F72")

    Jump("loc_2AFA")

    label("loc_1F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_215A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2093")

    ChrTalk(
        0xFE,
        (
            "Lately, monsters different than the\x01",
            "so-called normal monsters have been\x01",
            "appearing throughout Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumor has it that these monsters\x01",
            "seem to be ones written in the\x01",
            "Church's Testaments, but...\x02",
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
    Jump("loc_2155")

    label("loc_2093")


    ChrTalk(
        0xFE,
        (
            "If Ancient Zemurian knowledge\x01",
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

    label("loc_2155")

    Jump("loc_2AFA")

    label("loc_215A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_222A")

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
    Jump("loc_2AFA")

    label("loc_222A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_242E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2345")

    ChrTalk(
        0xFE,
        (
            "A state independence\x01",
            "proposal, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looking back at Crossbell history's up\x01",
            "to the middle ages... It's not the case\x01",
            "that nothing similar has ever happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As we understand by the current\x01",
            "situation, not a single one of\x01",
            "them was successful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2429")

    label("loc_2345")


    ChrTalk(
        0xFE,
        (
            "Nevertheless, given today's society, we say\x01",
            "for certain that this time will be another\x01",
            "failure just because it failed in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will this proposal grow into a\x01",
            "movement that shakes the\x01",
            "continent? Or will it go well?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2429")

    Jump("loc_2AFA")

    label("loc_242E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2451")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2449")
    Call(0, 20)
    Jump("loc_244C")

    label("loc_2449")

    Call(0, 21)

    label("loc_244C")

    Jump("loc_2AFA")

    label("loc_2451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_25E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2540")

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
            "nothing could make me\x01",
            "happier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25DD")

    label("loc_2540")


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
            "nothing could make me\x01",
            "happier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DD")

    Jump("loc_2AFA")

    label("loc_25E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_260F")
    Call(0, 7)
    Jump("loc_27B8")

    label("loc_260F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270E")

    ChrTalk(
        0xFE,
        (
            "The West Zemuria Trade\x01",
            "Conference, huh.\x02",
        )
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
    Jump("loc_27B8")

    label("loc_270E")


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

    label("loc_27B8")

    Jump("loc_2AFA")

    label("loc_27BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_27E2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_27DA")
    Call(0, 7)
    Jump("loc_27DD")

    label("loc_27DA")

    Call(0, 8)

    label("loc_27DD")

    Jump("loc_2AFA")

    label("loc_27E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_28DE")

    ChrTalk(
        0xFE,
        (
            "I don't know why, but I\x01",
            "make amazing research\x01",
            "progress on rainy days.\x02",
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
    Jump("loc_2AFA")

    label("loc_28DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2AFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A35")

    ChrTalk(
        0xFE,
        (
            "I'm a student of Lｳman\x01",
            "State University. I\x01",
            "study history there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, I attempted\x01",
            "to earn a doctorate\x01",
            "twice before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The first time, my thesis was rejected and I\x01",
            "failed. The second time, I couldn't hand it in\x01",
            "during the term and failed by default. ...In\x01",
            "other words, a splendid string of losses.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AFA")

    label("loc_2A35")


    ChrTalk(
        0xFE,
        (
            "Right now, I'm polishing\x01",
            "up my thesis for another\x01",
            "attempt next year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It's not the case that failing to earn\x01",
            "a doctorate mean one's university studies\x01",
            "are over. I'm stubborn like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFA")

    TalkEnd(0xFE)
    Return()

    # Function_6_1C2B end

    def Function_7_2AFE(): pass

    label("Function_7_2AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD7")

    ChrTalk(
        0xFE,
        (
            "You all investigated the\x01",
            "Tower of Stargaze for\x01",
            "me, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think most of the books\x01",
            "suddenly disappeared. I\x01",
            "wonder what happened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, thank goodness a\x01",
            "few books were left.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C48")

    label("loc_2BD7")


    ChrTalk(
        0xFE,
        (
            "Anyway, thank goodness a\x01",
            "few books were left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Miles and I plan to\x01",
            "examine it once again in\x01",
            "the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C48")

    Return()

    # Function_7_2AFE end

    def Function_8_2C49(): pass

    label("Function_8_2C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E83")

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
            "Honestly, the condition\x01",
            "of the books doesn't\x01",
            "seem that good, but...\x02",
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
            "As a student of history,\x01",
            "I resent the careless\x01",
            "management of the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(...It's as he says.\x01",
            "That hurts to hear...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(I guess. It's just, management\x01",
            "of the tower was left to that\x01",
            "previous commander.)\x02\x03",
            "#00302F(We shouldn't worry over\x01",
            "something that can't be helped,\x01",
            "right?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F4B")

    label("loc_2E83")


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

    label("loc_2F4B")

    Return()

    # Function_8_2C49 end

    def Function_9_2F4C(): pass

    label("Function_9_2F4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3007")

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
    Jump("loc_3959")

    label("loc_3007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3015")
    Jump("loc_3959")

    label("loc_3015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3140")

    ChrTalk(
        0xFE,
        (
            "Dieter's address... It\x01",
            "was amazingly shocking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can hardly believe it. To think the\x01",
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
    Jump("loc_321C")

    label("loc_3140")


    ChrTalk(
        0xFE,
        (
            "I can hardly believe it. To think the\x01",
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

    label("loc_321C")

    Jump("loc_3959")

    label("loc_3221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_322F")
    Jump("loc_3959")

    label("loc_322F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E6")

    ChrTalk(
        0xFE,
        (
            "It seems a terrible\x01",
            "incident happened in\x01",
            "Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think there are a lot\x01",
            "of kids like Abbie\x01",
            "there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I hope everyone\x01",
            "is freed ASAP.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_334B")

    label("loc_32E6")


    ChrTalk(
        0xFE,
        (
            "I think there are a lot\x01",
            "of kids like Abbie\x01",
            "there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I hope everyone\x01",
            "is freed ASAP.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334B")

    Jump("loc_3959")

    label("loc_3350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3378")

    ChrTalk(
        0xFE,
        "Hmm, that's right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3959")

    label("loc_3378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33CC")

    ChrTalk(
        0xFE,
        (
            "Ah, it's true that mom\x01",
            "didn't notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you out shopping?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3959")

    label("loc_33CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3465")

    ChrTalk(
        0xFE,
        (
            "It looks like KeA's\x01",
            "enthusiastically investigating\x01",
            "something today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I guess it can't\x01",
            "be helped if Abbie's\x01",
            "jealous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3959")

    label("loc_3465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3542")

    ChrTalk(
        0xFE,
        (
            "Our Abbie will be the\x01",
            "right age to go to\x01",
            "Sunday School next year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He loves books, so I\x01",
            "think he'll study hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Thinking about\x01",
            "stuff like this might\x01",
            "make me a doting parent.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35AC")

    label("loc_3542")


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
            "In short, there's\x01",
            "nothing else I wish for\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AC")

    Jump("loc_3959")

    label("loc_35B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3699")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3658")

    ChrTalk(
        0xFE,
        (
            "Haha, Abbie's quite\x01",
            "clever.\x02",
        )
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
            "Really!? Yes! I'm so\x01",
            "happy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3694")

    label("loc_3658")


    ChrTalk(
        0xFE,
        (
            "Haha, then what flavor\x01",
            "do you want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm... Melon!\x02",
    )

    CloseMessageWindow()

    label("loc_3694")

    Jump("loc_3959")

    label("loc_3699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3793")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3747")

    ChrTalk(
        0xFE,
        (
            "Haha. Abbie tired after seeing\x01",
            "the unveiling ceremony, and it\x01",
            "looks like he fell asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a peaceful\x01",
            "expression... It's\x01",
            "really cute.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_378E")

    label("loc_3747")


    ChrTalk(
        0xFE,
        (
            "Haha, seeing Abbie's\x01",
            "peaceful face like\x01",
            "this... It's really cute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_378E")

    Jump("loc_3959")

    label("loc_3793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_380D")

    ChrTalk(
        0xFE,
        (
            "This library is really\x01",
            "very quiet and\x01",
            "comfortable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And the smell of old\x01",
            "books is calming\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3959")

    label("loc_380D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_38F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C2")

    ChrTalk(
        0xFE,
        (
            "And as for Aidios'\x01",
            "flowing tears...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(18, 0, 70, 0)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "They fell upon the\x01",
            "ground, and spread\x01",
            "throughout the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The people could only\x01",
            "watch...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38F2")

    label("loc_38C2")


    ChrTalk(
        0xFE,
        (
            "The people could only\x01",
            "watch... And then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F2")

    Jump("loc_3959")

    label("loc_38F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3959")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3912")
    Call(0, 10)
    Jump("loc_3959")

    label("loc_3912")


    ChrTalk(
        0xFE,
        (
            "Our Abbie really loves\x01",
            "KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Myself as well, I\x01",
            "suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3959")

    TalkEnd(0xFE)
    Return()

    # Function_9_2F4C end

    def Function_10_395D(): pass

    label("Function_10_395D")


    ChrTalk(
        0xA,
        "Ah, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, it's KeA big brother\x01",
            "and sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hey, is KeA coming\x01",
            "today?\x02",
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
            "#00102FWe'll tell KeA you asked\x01",
            "about her. You'll just have\x01",
            "to make do for today, okay?\x02",
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
        "Then, tell KeA for me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHaha, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FI see, so she's even\x01",
            "popular in a place like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FYep, that's KeA for you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 0)
    Return()

    # Function_10_395D end

    def Function_11_3B04(): pass

    label("Function_11_3B04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B44")

    ChrTalk(
        0xFE,
        (
            "So excited... Mom, hurry\x01",
            "up and ready it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_407E")

    label("loc_3B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B52")
    Jump("loc_407E")

    label("loc_3B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3BA6")

    ChrTalk(
        0xFE,
        (
            "Hey, mom. They're saying\x01",
            "something outside. I\x01",
            "wonder what it is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_407E")

    label("loc_3BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3BB4")
    Jump("loc_407E")

    label("loc_3BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3C00")

    ChrTalk(
        0xFE,
        (
            "Hey mom... You don't\x01",
            "look so good. Did\x01",
            "something happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_407E")

    label("loc_3C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3C37")

    ChrTalk(
        0xFE,
        (
            "Hey, mom. What do those\x01",
            "words mean?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_407E")

    label("loc_3C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CEA")

    ChrTalk(
        0xFE,
        (
            "Huh, KeA? Just when did\x01",
            "she leave?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. If I'd noticed I'd\x01",
            "have properly said\x01",
            "goodbye...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, we'll see each\x01",
            "other again, so it's\x01",
            "fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D5A")

    label("loc_3CEA")


    ChrTalk(
        0xFE,
        (
            "Hmm. If I'd noticed I'd\x01",
            "have properly said\x01",
            "goodbye...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, we'll see each\x01",
            "other again, so it's\x01",
            "fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D5A")

    Jump("loc_407E")

    label("loc_3D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3DC3")

    ChrTalk(
        0xFE,
        (
            "KeA's reading books all\x01",
            "by herself. Amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I've got to study\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_407E")

    label("loc_3DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E42")

    ChrTalk(
        0xFE,
        (
            "I'm going to be going to\x01",
            "Sunday School like KeA\x01",
            "pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ehehe, I hope I see her\x01",
            "at Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_407E")

    label("loc_3E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3EB6")

    ChrTalk(
        0xFE,
        (
            "You know, KeA said she\x01",
            "had something to\x01",
            "research today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That why you mustn't\x01",
            "interrupt her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_407E")

    label("loc_3EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F22")

    ChrTalk(
        0xFE,
        "...Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey mom, there's a lot\x01",
            "of people out there...\x01",
            "...*mumble*...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F31")

    label("loc_3F22")


    ChrTalk(
        0xFE,
        "...Zzz...\x02",
    )

    CloseMessageWindow()

    label("loc_3F31")

    Jump("loc_407E")

    label("loc_3F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FCA")

    ChrTalk(
        0xFE,
        (
            "Mom, they say books have\x01",
            "a nice smell, but... I\x01",
            "don't get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, you've had a\x01",
            "nice smell this whole\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FF2")

    label("loc_3FCA")


    ChrTalk(
        0xFE,
        (
            "Do books really have a\x01",
            "nice smell?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF2")

    Jump("loc_407E")

    label("loc_3FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_402D")

    ChrTalk(
        0xFE,
        (
            "So excited... And then,\x01",
            "and then!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_407E")

    label("loc_402D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_407E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4048")
    Call(0, 10)
    Jump("loc_407E")

    label("loc_4048")


    ChrTalk(
        0xFE,
        "Say hi to KeA for me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll be waiting here.\x02",
    )

    CloseMessageWindow()

    label("loc_407E")

    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_3B04 end

    def Function_12_4086(): pass

    label("Function_12_4086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4097")
    Call(0, 14)
    Jump("loc_40E7")

    label("loc_4097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40A8")
    Call(0, 13)
    Jump("loc_40E7")

    label("loc_40A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40B9")
    Call(0, 14)
    Jump("loc_40E7")

    label("loc_40B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_40E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40DC")
    Call(0, 13)
    Jump("loc_40DF")

    label("loc_40DC")

    Call(0, 14)

    label("loc_40DF")

    Jump("loc_40E7")

    label("loc_40E4")

    Call(0, 14)

    label("loc_40E7")

    Return()

    # Function_12_4086 end

    def Function_13_40E8(): pass

    label("Function_13_40E8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41D1")

    ChrTalk(
        0x8,
        (
            "The head librarian and the others are\x01",
            "looking into the ancient documents\x01",
            "discovered at the Tower of Stargaze today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They had lively expressions on\x01",
            "their faces like that of little\x01",
            "boys. It was kind of cute.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4269")

    label("loc_41D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_4269")

    ChrTalk(
        0x8,
        (
            "If you are looking for the head\x01",
            "librarian, it seems he's\x01",
            "discussing something with Nielsen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even though break time's\x01",
            "already over...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4269")

    TalkEnd(0x8)
    Return()

    # Function_13_40E8 end

    def Function_14_426D(): pass

    label("Function_14_426D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 7)), scpexpr(EXPR_END)), "loc_42A0")
    Call(0, 32)
    Return()

    label("loc_42A0")

    Call(0, 30)
    Return()

    label("loc_42A4")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4472")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43BF")

    ChrTalk(
        0xC,
        (
            "The city is more or less back to\x01",
            "normal, but... There are still\x01",
            "things to be worried about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think the appearance of\x01",
            "that weird huge tree\x01",
            "couldn't have been helped.\x02",
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
    Jump("loc_446D")

    label("loc_43BF")


    ChrTalk(
        0xC,
        (
            "The city is more or less back to\x01",
            "normal, but... There are still\x01",
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

    label("loc_446D")

    Jump("loc_58C3")

    label("loc_4472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4758")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469E")
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Oh, Lloyd... You're\x01",
            "safe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYou too, uncle. What a\x01",
            "relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah, totally.\x02",
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
            "Uncle... Thank you.\x02\x03",
            "#00001FThere's a lot of things I need\x01",
            "to tell you, but I don't have\x01",
            "time for that right now.\x02\x03",
            "Please. For now, don't leave the\x01",
            "building until the situation\x01",
            "outside has calmed down.\x02",
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
            "Lloyd, and the rest of\x01",
            "you as well. Please be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 4)
    Jump("loc_4753")

    label("loc_469E")


    ChrTalk(
        0xC,
        (
            "Actually, Nielsen had just\x01",
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

    label("loc_4753")

    Jump("loc_58C3")

    label("loc_4758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_499C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490C")

    ChrTalk(
        0xC,
        (
            "L-Lloyd. Did you hear\x01",
            "Dieter's address? And\x01",
            "about the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah, we were surprised by\x01",
            "that as well. There's a lot of\x01",
            "things we need to look into.\x02\x03",
            "Anyway, uncle. For now, I want\x01",
            "to you relax and just watch\x01",
            "the developments.\x02",
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
            "There are a lot of\x01",
            "worrying things, but I'll\x01",
            "see if I can't relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Do your best, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYeah, thanks uncle.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4997")

    label("loc_490C")


    ChrTalk(
        0xC,
        (
            "There are a lot of\x01",
            "worrying things, but I'll\x01",
            "see if I can't relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But, just why did Dieter\x01",
            "put forward such a\x01",
            "strong policy...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4997")

    Jump("loc_58C3")

    label("loc_499C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A47")

    ChrTalk(
        0xC,
        (
            "The charity event held by the\x01",
            "city and the Merchants\x01",
            "Association looks rather lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. I'll have to put in\x01",
            "my own donation later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4AE4")

    label("loc_4A47")


    ChrTalk(
        0xC,
        (
            "No matter what anyone says, the\x01",
            "spirit of helping each other is an\x01",
            "indispensable part of humanity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. I'll have to put in\x01",
            "my own donation later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE4")

    Jump("loc_58C3")

    label("loc_4AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4BA2")

    ChrTalk(
        0xC,
        (
            "I don't know who the armed\x01",
            "group is, but... Good\x01",
            "grief, how utterly foolish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Something like ruling people\x01",
            "by force... It can't be\x01",
            "forgiven, no mistake about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C3")

    label("loc_4BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C38")

    ChrTalk(
        0xC,
        (
            "Hmm, it's raining\x01",
            "outside, huh.\x02",
        )
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
    Jump("loc_58C3")

    label("loc_4C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4CBA")

    ChrTalk(
        0xC,
        (
            "My wife's lunch box is\x01",
            "well done as usual\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks to it, I'll be\x01",
            "able to do my best this\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C3")

    label("loc_4CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD5")
    Call(0, 15)
    Jump("loc_4D53")

    label("loc_4CD5")


    ChrTalk(
        0xC,
        (
            "Ah, I'll never forget the\x01",
            "love she puts into them,\x01",
            "each and every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But, I'm glad my wife\x01",
            "came to give it to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D53")

    Jump("loc_58C3")

    label("loc_4D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4D7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D73")
    Call(0, 20)
    Jump("loc_4D76")

    label("loc_4D73")

    Call(0, 21)

    label("loc_4D76")

    Jump("loc_58C3")

    label("loc_4D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4DB2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4DA1")
    Call(0, 18)
    Jump("loc_4DAD")

    label("loc_4DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_4DAD")
    Call(0, 17)

    label("loc_4DAD")

    Jump("loc_4F4C")

    label("loc_4DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E98")

    ChrTalk(
        0xC,
        (
            "Ah, KeA is quite\x01",
            "studious.\x02",
        )
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
    Jump("loc_4F4C")

    label("loc_4E98")


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

    label("loc_4F4C")

    Jump("loc_58C3")

    label("loc_4F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_519E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4F88")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4F77")
    Call(0, 18)
    Jump("loc_4F83")

    label("loc_4F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_4F83")
    Call(0, 17)

    label("loc_4F83")

    Jump("loc_5199")

    label("loc_4F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50DB")

    ChrTalk(
        0xC,
        (
            "Hmm, I only got a brief\x01",
            "look at the VIP's faces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Among them, Prince\x01",
            "Olivert caught my\x01",
            "attention the most.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "After helping resolve the incident\x01",
            "in Liberl, he used the Arseille to\x01",
            "return to the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In contrast, the Blood and Iron\x01",
            "Chancellor shocked the world, and\x01",
            "his every move commands attention.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5199")

    label("loc_50DB")


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
            "In contrast, the Blood and Iron\x01",
            "Chancellor shocked the world, and\x01",
            "his every move commands attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5199")

    Jump("loc_58C3")

    label("loc_519E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_51CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_51BB")
    Call(0, 18)
    Jump("loc_51C7")

    label("loc_51BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_51C7")
    Call(0, 17)

    label("loc_51C7")

    Jump("loc_58C3")

    label("loc_51CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_5350")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_52B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F3")
    Call(0, 16)
    Jump("loc_52B0")

    label("loc_51F3")


    ChrTalk(
        0xC,
        (
            "He won the Fuelitzer Prize and\x01",
            "suddenly became famous. It's been\x01",
            "ten years since then, huh...\x02",
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

    label("loc_52B0")

    Jump("loc_534B")

    label("loc_52B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_533D")

    ChrTalk(
        0xC,
        (
            "Hmm. Now that Nielsen's back,\x01",
            "I'll need to have a chat with\x01",
            "him no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now then, there's work\x01",
            "to do...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_534B")

    label("loc_533D")

    Call(0, 26)
    TalkEnd(0xC)
    OP_93(0xC, 0x10E, 0x0)
    Return()

    label("loc_534B")

    Jump("loc_58C3")

    label("loc_5350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_55A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553A")

    ChrTalk(
        0xC,
        (
            "A special guest is going\x01",
            "to show his face here,\x01",
            "starting today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, I'm looking\x01",
            "forward to speaking with\x01",
            "him.\x02",
        )
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
            "I think he'll be here in\x01",
            "a little bit, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you like, I'll\x01",
            "introduce him to all of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FA famous international\x01",
            "journalist, huh... That does\x01",
            "seem pretty interesting.\x02\x03",
            "#00002FHmm. Then, we'll stop by if\x01",
            "we're free.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x133, 2)
    SetScenarioFlags(0x0, 4)
    Jump("loc_559B")

    label("loc_553A")


    ChrTalk(
        0xC,
        (
            "Nielsen should be here\x01",
            "in a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you like, I'll\x01",
            "introduce him to all of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_559B")

    Jump("loc_58C3")

    label("loc_55A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_58C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_585D")

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
        (
            "Yeah, I'll be counting\x01",
            "on you, then.\x02",
        )
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
            "#00006FAh, don't say that... We\x01",
            "still have a long way to\x01",
            "go.\x02",
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
            "Feel free to visit my\x01",
            "home as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FSure. Thanks, uncle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F(Cecil's uncle... A very\x01",
            "gentle man.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x133, 5)
    Jump("loc_58C3")

    label("loc_585D")


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

    label("loc_58C3")

    TalkEnd(0xC)
    Return()

    # Function_14_426D end

    def Function_15_58C7(): pass

    label("Function_15_58C7")


    ChrTalk(
        0xC,
        (
            "What is it, Leyte? Need\x01",
            "something?\x02",
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
            "Haha. You forgot your\x01",
            "lunchbox so I brought it\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh!? I hadn't noticed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sorry. Thanks for\x01",
            "bringing it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    Return()

    # Function_15_58C7 end

    def Function_16_5996(): pass

    label("Function_16_5996")


    ChrTalk(
        0xC,
        (
            "Hmm, Lloyd. It seems\x01",
            "your conversation is\x01",
            "over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Did you have a useful\x01",
            "discussion?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, I guess. I\x01",
            "definitely learned\x01",
            "something.\x02\x03",
            "#00000FBy the way uncle, did\x01",
            "you know Nielsen before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah. Like me, Nielsen\x01",
            "is originally from\x01",
            "Crossbell, after all.\x02",
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
            "By the way, it seems he\x01",
            "was also close with Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYeah, seems that way.\x02\x03",
            "#00003F(That seems similar to\x01",
            "our relationship with\x01",
            "Grace.)\x02\x03",
            "(...Of course, the mood\x01",
            "is totally different,\x01",
            "though.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 6)
    Return()

    # Function_16_5996 end

    def Function_17_5BCE(): pass

    label("Function_17_5BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CF7")

    ChrTalk(
        0xC,
        (
            "Please investigate the "Tower\x01",
            "of Stargaze" on the outskirts\x01",
            "of St. Ursula Byroad for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I heard that a great\x01",
            "many ancient documents\x01",
            "were left there.\x02",
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
        (
            "I'll be counting on you,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5DB7")

    label("loc_5CF7")


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
            "Please take care of investigating\x01",
            "the ancient documents that are in\x01",
            "the tower for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB7")

    Return()

    # Function_17_5BCE end

    def Function_18_5DB8(): pass

    label("Function_18_5DB8")


    ChrTalk(
        0xC,
        (
            "It's really too bad that we\x01",
            "couldn't recover all of the\x01",
            "books from Tower, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even just having this\x01",
            "grimoire is quite\x01",
            "valuable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks, guys. I'll let\x01",
            "you know if I ever need\x01",
            "your help again.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_18_5DB8 end

    def Function_19_5E8B(): pass

    label("Function_19_5E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_5EAB")
    Call(0, 28)
    Return()

    label("loc_5EAB")

    Call(0, 26)
    Return()

    label("loc_5EAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5F59")

    ChrTalk(
        0xFE,
        (
            "A sudden declaration of martial\x01",
            "law... Once could say it's proof\x01",
            "the President is cornered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This oppression won't\x01",
            "last long... This is\x01",
            "normal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_601B")

    label("loc_5F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5FFD")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(The strongest jaegers on\x01",
            "the continent... Who\x01",
            "could be behind them...?)\x02",
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
    Jump("loc_601B")

    label("loc_5FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_601B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6018")
    Call(0, 20)
    Jump("loc_601B")

    label("loc_6018")

    Call(0, 21)

    label("loc_601B")

    TalkEnd(0xFE)
    Return()

    # Function_19_5E8B end

    def Function_20_601F(): pass

    label("Function_20_601F")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "Hmm, it appears this grimoire\x01",
            "is a study of artifacts from\x01",
            "the middle ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I see... And did you\x01",
            "learn anything about its\x01",
            "author?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes. There's no mistake that this\x01",
            "was left behind by the alchemists\x01",
            "who once built the Tower, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It doesn't seem like\x01",
            "there's any proof of\x01",
            "their identities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well even so, there's no\x01",
            "mistake that this is\x01",
            "valuable data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm. But it's really too\x01",
            "bad that this was the\x01",
            "only thing left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Also, there a lot of mysteries\x01",
            "regarding the middle age\x01",
            "alchemists even today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We're not sure if any document\x01",
            "connected to their identities\x01",
            "even exists, but...\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_639F")

    ChrTalk(
        0x101,
        (
            "#00000F(Uncle... It looks like\x01",
            "they're researching the\x01",
            "book we found.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes. But it looks like\x01",
            "they haven't found\x01",
            "anything new...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_639F")

    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x16B, 4)
    Return()

    # Function_20_601F end

    def Function_21_63AB(): pass

    label("Function_21_63AB")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Hmm. Middle age\x01",
            "alchemists, huh... The\x01",
            "mystery only deepens.\x02",
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

    # Function_21_63AB end

    def Function_22_6489(): pass

    label("Function_22_6489")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_64E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64A7")
    Call(0, 15)
    Jump("loc_64E4")

    label("loc_64A7")


    ChrTalk(
        0xFE,
        (
            "Haha, you do forget your\x01",
            "lunchbox sometimes,\x01",
            "don't you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64E4")

    TalkEnd(0xFE)
    Return()

    # Function_22_6489 end

    def Function_23_64E8(): pass

    label("Function_23_64E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_66B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6506")
    Call(0, 25)
    Jump("loc_66B3")

    label("loc_6506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_664D")

    ChrTalk(
        0xE,
        (
            "#01105F...Ah, come to think of\x01",
            "it, I forgot to go\x01",
            "shopping for dinner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha. There's still time\x01",
            "until evening, so relax.\x02\x03",
            "More important, make sure\x01",
            "you pick out a good get-\x01",
            "well book for Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01109FYeah. Thanks, Lloyd.\x02\x03",
            "#01110FI'll get those\x01",
            "ingredients, so look\x01",
            "forward to it, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_66B3")

    label("loc_664D")


    ChrTalk(
        0xE,
        (
            "#01103FHmm, a get-well book for\x01",
            "Shizuku.\x02\x03",
            "#01109F(*rustle*...) Yeah, this\x01",
            "one's interesting too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66B3")

    Jump("loc_68D0")

    label("loc_66B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_68D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66D3")
    Call(0, 24)
    Jump("loc_68D0")

    label("loc_66D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6840")

    ChrTalk(
        0xE,
        (
            "#01109FLook at this, Lloyd. This book\x01",
            "has a picture of the huuuge\x01",
            "bell in Central Square.\x02\x03",
            "#01100FOriginally, that bell was at\x01",
            "the Fort of Sun, it says.\x02\x03",
            "#01111FHmm, it's so big... I wonder\x01",
            "if carrying it here was tough?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Haha. It looks like KeA\x01",
            "is more curious than we\x01",
            "thought.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F(Haha. I wonder what's\x01",
            "next for her.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_68D0")

    label("loc_6840")


    ChrTalk(
        0xE,
        (
            "#01100FThe big bell in Central\x01",
            "square was at the Fort\x01",
            "of Sun, it says.\x02\x03",
            "#01111FHmm, it's so big... I\x01",
            "wonder if carrying it\x01",
            "here was tough?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D0")

    TalkEnd(0xFE)
    Return()

    # Function_23_64E8 end

    def Function_24_68D4(): pass

    label("Function_24_68D4")

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
            "#5P#01110FAh, this is it. ...Here\x01",
            "we go.\x02",
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
            "#01110FYeah, I was just\x01",
            "collecting books with\x01",
            "folk tales.\x02\x03",
            "I read one and became\x01",
            "interested in them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FUm, let's see...\x02\x03",
            "#00105F"Crossbell Middle Ages History"\x01",
            "and "Looking at Crossbell's\x01",
            "Past through Ruins"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FT-These aren't folk\x01",
            "tales, they're bona-fide\x01",
            "history books and theses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00202FKeA, you're amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FHaha. Are you gonna be a\x01",
            "researcher or something\x01",
            "when you grow up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01100FUmm, you really think\x01",
            "so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha. It's rare to dote\x01",
            "on one's daughter this\x01",
            "much.\x02",
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

    # Function_24_68D4 end

    def Function_25_6CDB(): pass

    label("Function_25_6CDB")

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
        (
            "#00000FKeA, you're reading a\x01",
            "book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01109FYeah. I'm looking for a\x01",
            "book for Shizuku's get-\x01",
            "well present.\x02\x03",
            "#01111FWhat should I pick...? A\x01",
            "book like this seems\x01",
            "pretty interesting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThat shelf... Isn't that\x01",
            "the braille corner?\x02\x03",
            "Looks interesting, you\x01",
            "say... Can you read\x01",
            "this, KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01105FI can, but...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F"I can, but...?", she\x01",
            "says, so casually...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FDid you learn this in\x01",
            "Sunday School?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01100FNo, I learned it when I was playing with\x01",
            "Shizuku.\x02\x03",
            "Books like "Mark and the Witch of the Deep\x01",
            "Forest" have been translated to braille\x01",
            "already, so it must be pretty easy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI feel like it might be\x01",
            "fast even for a book you\x01",
            "already know, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FHaha. This comprehension\x01",
            "speed is characteristic\x01",
            "of KeA.\x02",
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

    # Function_25_6CDB end

    def Function_26_7132(): pass

    label("Function_26_7132")

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
            "interesting way to put\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7201():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_7201)
    Sleep(50)
    TurnDirection(0xD, 0x102, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_END)), "loc_7309")

    ChrTalk(
        0xC,
        (
            "Oh, if it isn't Lloyd\x01",
            "and everyone. Good\x01",
            "timing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The man I was just\x01",
            "talking to is Nielsen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FThis man is Nielsen...\x02\x03",
            "#00000FUmm, how do you do. I'm Lloyd\x01",
            "Bannings of the Crossbell\x01",
            "Police Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742F")

    label("loc_7309")


    ChrTalk(
        0xC,
        "Oh, if it isn't Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUncle, is that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah, he's Nielsen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He's a famous\x01",
            "international\x01",
            "journalist.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "Come now, Nielsen. They're the\x01",
            "Special Support Section, and\x01",
            "subject of all the recent rumors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FUmm, how do you do. I'm\x01",
            "Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    label("loc_742F")


    ChrTalk(
        0xD,
        (
            "Hmm, that Special Support\x01",
            "Section, huh. And you're\x01",
            "Lloyd, their leader...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha, you've got a nice\x01",
            "clean voice.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00001FI'm sorry but... Are\x01",
            "your eyes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, it's from an old\x01",
            "accident. I lost my\x01",
            "sight back then.\x02",
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
            "Head librarian, so\x01",
            "you're still here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Break time's already\x01",
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
            "Sorry, it seems I caught\x01",
            "caught up in\x01",
            "conversation again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "And so, I'm sorry. I've\x01",
            "got to get back to\x01",
            "work...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)

    ChrTalk(
        0xD,
        (
            "Alright. If you like,\x01",
            "let's exchange notes\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sure. I'll be here, as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    TurnDirection(0xD, 0x102, 500)

    ChrTalk(
        0xC,
        (
            "Then, Lloyd and\x01",
            "everyone. I leave the\x01",
            "rest to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAh, sure...\x02",
    )

    CloseMessageWindow()

    def lambda_7749():
        OP_95(0x8, 24560, 4019, 80, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7749)
    OP_93(0xC, 0x0, 0x1F4)
    OP_95(0xC, 13110, 30, -2100, 2000, 0x0)

    def lambda_777E():
        OP_95(0xC, 4570, 40, -1570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_777E)
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
            "Let me introduce myself\x01",
            "once again.\x02",
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
            "#00108F(Nielsen... Where have I\x01",
            "heard that name\x01",
            "before...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes. I definitely wanted to\x01",
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
        (
            "I don't think it will\x01",
            "take very much of your\x01",
            "valuable time, though.\x02",
        )
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
            "You see, right now I'm\x01",
            "investigating that cult\x01",
            "incident, but...\x02",
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
            "I'd like to interview you all as\x01",
            "figures connected to the incident\x01",
            "and central to its resolution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FA cult incident\x01",
            "interview, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha. You speak as if\x01",
            "you already know a lot\x01",
            "about it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Lloyd, what should we do?)\x02\x03",
            "(The subject being what it\x01",
            "is, I don't think we can say\x01",
            "too much about it, but...)\x02",
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

    # Function_26_7132 end

    def Function_27_7C61(): pass

    label("Function_27_7C61")

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
            "Think about it for now\x01",      # 1
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
        (0, "loc_7CDF"),
        (1, "loc_7FCB"),
        (SWITCH_DEFAULT, "loc_80E2"),
    )


    label("loc_7CDF")


    ChrTalk(
        0x101,
        (
            "#00001FUnderstood. If you're\x01",
            "okay with it, please\x01",
            "allow us to help.\x02\x03",
            "But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I understand. Given your position, there\x01",
            "are some things that are hard to say. I\x01",
            "don't mind if you refuse to answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And as a general rule,\x01",
            "your responses today\x01",
            "will be off the record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FI see... Thank you for\x01",
            "your understanding.\x02\x03",
            "#00005FBut what about the\x01",
            "location. Doing it here\x01",
            "might be a problem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In that case, how about\x01",
            "the discussion space on\x01",
            "2F?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We'll know immediately if\x01",
            "anyone comes, so I think\x01",
            "it's the perfect place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou're certainly right\x01",
            "about that. In that\x01",
            "case, let's head there.\x02",
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
            "Quest [Cult Incident\x01",
            "Coverage Assistance]\x01\x07\x00",
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
    Jump("loc_80E2")

    label("loc_7FCB")


    ChrTalk(
        0x101,
        (
            "#00006FSorry. We have other\x01",
            "cases to deal with right\x01",
            "now...\x02\x03",
            "#00001FIs it okay if we accept\x01",
            "your request later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes. I'll be here a\x01",
            "while longer so I don't\x01",
            "particularly mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Once you think you can\x01",
            "handle it, please come\x01",
            "speak with me.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80DA")
    EventEnd(0x5)

    label("loc_80DA")

    SetScenarioFlags(0x133, 3)
    Jump("loc_80E2")

    label("loc_80E2")

    Return()

    # Function_27_7C61 end

    def Function_28_80E3(): pass

    label("Function_28_80E3")

    TalkBegin(0xD)

    ChrTalk(
        0xD,
        "...You're Lloyd, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Care to join me for that\x01",
            "cult incident interview?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Call(0, 27)
    TalkEnd(0xD)
    Return()

    # Function_28_80E3 end

    def Function_29_8144(): pass

    label("Function_29_8144")

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
            "#11PThanks for joining me\x01",
            "for this interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThen, let's begin by\x01",
            "sorting out the initial\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThe D∴G Cult, whose creed\x01",
            "was to reject the Goddess\x01",
            "and worship demons─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PSeveral decades ago, they\x01",
            "serially kidnapped young children\x01",
            "from all over the continent.\x02",
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
            "conducted to expose and eliminate the cult\x01",
            "lodges all over the continent, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PDo you all know the power\x01",
            "by which that operation\x01",
            "was carried out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6PYes, that's─\x02",
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
            "#1KThe power that conducted the DG Cult\x01",
            "elimination operation six years ago?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Military and police from several nations\x01",      # 0
            "Bracer Guilds from several nations\x01",            # 1
            "Both of them\x01",                                  # 2
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
        (0, "loc_85D2"),
        (1, "loc_867A"),
        (2, "loc_8722"),
        (SWITCH_DEFAULT, "loc_878D"),
    )


    label("loc_85D2")


    ChrTalk(
        0x101,
        (
            "#00000F#6PMilitary and police from\x01",
            "several nations, right?\x02\x03",
            "#00006F...No, it wasn't just\x01",
            "them.\x02\x03",
            "#00001FI heard Bracer Guilds\x01",
            "from several nations\x01",
            "cooperated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_878D")

    label("loc_867A")


    ChrTalk(
        0x101,
        (
            "#00000F#6PBracer guilds from\x01",
            "several nations, right?\x02\x03",
            "#00006F...No, it wasn't just\x01",
            "them.\x02\x03",
            "#00001FI heard military and\x01",
            "police from several\x01",
            "nations cooperated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_878D")

    label("loc_8722")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00001F#6PMilitary and police forces,\x01",
            "and also the Bracer Guilds\x01",
            "from several nations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_878D")

    label("loc_878D")


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
            "position of Supreme Commander─\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105F#6PE-Excuse me. May I\x01",
            "interrupt?\x02\x03",
            "#00101FThe man named Cassius\x01",
            "Bright is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#12PC-Could you be talking about\x01",
            "General Bright, Commander of\x01",
            "the Liberl Royal Army?\x02",
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
            "#11PHe retired from the royal army and\x01",
            "was active for 10 years as a\x01",
            "bracer. Then, he rejoined the army.\x02",
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
            "#00106F#6PT-That's true, but─\x02\x03",
            "#00108FI didn't realize it\x01",
            "until now, but that name\x01",
            ""Bright" is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P─I was surprised when I realized it\x01",
            "while reviewing investigation documents\x01",
            "during my Section One training.\x02\x03",
            "#00001FCassius Bright is Estelle Bright's real\x01",
            "father.\x02\x03",
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
        (
            "#10105F#12PAn unexpected\x01",
            "connection, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PI thought she was quite\x01",
            "something during that\x01",
            "chase battle, but...\x02\x03",
            "#10302FI never thought she was\x01",
            "the daughter of someone\x01",
            "famous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PHmm, so you know the\x01",
            "daughter of General\x01",
            "Bright, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAs a reporter, I'm aware\x01",
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
        (
            "#00002F#6PWell, we're connected in\x01",
            "many ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PSorry for\x01",
            "interrupting...\x02\x03",
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
            "of Bracer Cassius Bright, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThat operation was thought to\x01",
            "have eliminated 90 percent of\x01",
            "the cult's influence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBy the way, at that time, the\x01",
            "Sergei Team of the Crossbell Police\x01",
            "participated in the operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThe current chief of your\x01",
            "Special Support section,\x01",
            "along with two others─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThat Arios MacLaine and\x01",
            "Guy, Lloyd's older\x01",
            "brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P...It seems you've\x01",
            "deeply investigated this\x01",
            "case.\x02\x03",
            "#00008FAnd even the connection\x01",
            "between my brother and\x01",
            "I...\x02",
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
            "#11PI've interviewed Guy\x01",
            "himself many times, you\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P...Yes. Guy helped me in\x01",
            "various ways when he was\x01",
            "alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P...Hmm, let's return to\x01",
            "the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PFrom there, there was\x01",
            "another from Crossbell\x01",
            "who became involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIt was Lawyer Ian\x01",
            "Grimwood, who served as\x01",
            "a civilian adviser.\x02",
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
            "#11PI heard he contributed to\x01",
            "intelligence gathering\x01",
            "regarding the abductees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PCome to think of it, he\x01",
            "said that himself.\x02\x03",
            "#00100FI see, so that's how he\x01",
            "cooperated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAlso, it was said that Church\x01",
            "officials and a mysterious\x01",
            "organization secretly intervened─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAnd because of that, the\x01",
            "remaining cult influence\x01",
            "was said to be eliminated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P(Church officials,\x01",
            "huh...)\x02",
        )
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
            "we met at Altair Lodge.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6P(And the mysterious\x01",
            "organization is probably\x01",
            "Ouroboros.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11P(Hehe. Neither group is\x01",
            "well understood even to\x01",
            "this day, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PHmm...\x02",
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
            "#11PAnyhow─ The cult\x01",
            "incident should have\x01",
            "concluded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBut several months ago,\x01",
            "it became clear that it\x01",
            "had not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAnd the reason for that is\x01",
            "something that I'm sure\x01",
            "you all are aware of...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYes. It was because of the\x01",
            "appearance of Dr. Joachim\x01",
            "Gunther, a cult survivor.\x02",
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
            "#11PIt seems he had\x01",
            "knowledge of the cult's\x01",
            "inner workings, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIn the end, was Joachim\x01",
            "Gunther the cult leader?\x02",
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
            "#1KWas Joachim Gunther the\x01",
            "D∴G Cult leader?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Yes, he was\x01",                         # 0
            "He was one of the high priests\x01",      # 1
            "He was a simple cultist\x01",             # 2
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
        (0, "loc_97E1"),
        (1, "loc_9889"),
        (2, "loc_98D6"),
        (SWITCH_DEFAULT, "loc_9974"),
    )


    label("loc_97E1")


    ChrTalk(
        0x101,
        (
            "#00001F#6PExactly. His position\x01",
            "was cult leader─\x02\x03",
            "#00011F(─That's not right! What\x01",
            "am I saying?)\x02\x03",
            "#00006F─That's not right. He\x01",
            "was one of the high\x01",
            "priests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9974")

    label("loc_9889")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00001F#6PNo, incorrect. He was\x01",
            "one of the high priests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9974")

    label("loc_98D6")


    ChrTalk(
        0x101,
        (
            "#00001F#6PNo, he was a simple\x01",
            "cultist─\x02\x03",
            "#00011F(─That's not right! What\x01",
            "am I saying?)\x02\x03",
            "#00006F─That's not right. He\x01",
            "was one of the high\x01",
            "priests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9974")

    label("loc_9974")


    ChrTalk(
        0x102,
        (
            "#00103F#6PYes, he said that\x01",
            "himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PIt's just, he had a flair\x01",
            "for research and supervised\x01",
            "many experiments.\x02\x03",
            "#00001FI think that's why he was\x01",
            "familiar with the cult's\x01",
            "inner workings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PHmm, a reasonable\x01",
            "theory.\x02",
        )
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
            "#11PThen, at the facility called "Paradise",\x01",
            "he seized upon Chairman Hartmann's\x01",
            "weakness and escaped to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThen, he finally completed\x01",
            "Gnosis, a medicine whose\x01",
            "name means "True Wisdom".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI don't know the particulars,\x01",
            "but... He did it to fulfill\x01",
            "the cult's ambition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PThe cult's ambition...\x02\x03",
            "#00108F(Indeed, he did refer to\x01",
            "KeA as a God, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6P(Yeah, I could see that from\x01",
            "the people Joachim dosed\x01",
            "with red Gnosis, but...)\x02\x03",
            "#00006F(In the end, we didn't'\x01",
            "learn any of those details.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P...Hmm. As always,\x01",
            "there's many unclear\x01",
            "points, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI think we've outlined\x01",
            "most of what happened in\x01",
            "the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PBut finally, the roots\x01",
            "of the D∴G Cult's\x01",
            "origin─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIs it alright if we\x01",
            "consider that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PThe cult's roots...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PYes. By the way Lloyd, about how\x01",
            "many years ago are the cult's\x01",
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
            "roots thought to stretch back?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "1200 years ago\x01",      # 0
            " 500 years ago\x01",      # 1
            "  50 years ago\x01",      # 2
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
        (0, "loc_9FB1"),
        (1, "loc_A096"),
        (2, "loc_A0EB"),
        (SWITCH_DEFAULT, "loc_A1C2"),
    )


    label("loc_9FB1")


    ChrTalk(
        0x101,
        (
            "#00008F#6P(1200 years ago...? No.\x01",
            "Though it's possible, I\x01",
            "don't think that's it.)\x02\x03",
            "#00003F(Based on everything we\x01",
            "know so far, the answer\x01",
            "definitely is...)\x02\x03",
            "#00001FMost likely 500 years\x01",
            "ago─ To Crossbell's\x01",
            "middle age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1C2")

    label("loc_A096")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00001F#6PMost likely 500 years\x01",
            "ago─ To Crossbell's\x01",
            "middle age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1C2")

    label("loc_A0EB")


    ChrTalk(
        0x101,
        (
            "#00011F#6P(50 years ago...? No, it\x01",
            "wouldn't have been that\x01",
            "recent.)\x02\x03",
            "#00003F(Based on everything we\x01",
            "know so far, the answer\x01",
            "definitely is...)\x02\x03",
            "#00001FMost likely 500 years\x01",
            "ago─ To Crossbell's\x01",
            "middle age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1C2")

    label("loc_A1C2")


    ChrTalk(
        0xD,
        "#11PHmm, and why is that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PActually, we heard this\x01",
            "from Joachim himself.\x02\x03",
            "#00008F500 years ago, there was\x01",
            "a group of alchemists in\x01",
            "this land─\x02\x03",
            "#00001FThe cult used the\x01",
            "technology of those\x01",
            "days, he said...\x02\x03",
            "#00006FSince then, their\x01",
            "ancestors have become\x01",
            "unknown, but...\x02",
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
            "#11PThe alchemists that once existed in\x01",
            "this land─ In other words, the same\x01",
            "ones that built the Tower of Stargaze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PTo think the handed down\x01",
            "knowledge of the cult would\x01",
            "have this kind of foundation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#12PHehe, that's certainly\x01",
            "surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PHmm, and the girl that\x01",
            "was entrusted to you\x01",
            "all─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PWould you believe that\x01",
            "girl is from back then?\x02",
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
            "lacked tact.\x02",
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
            "#11PI swear on the Goddess I\x01",
            "won't broadcast it, so\x01",
            "please relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PD-Don't worry about\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#11P...Hmm. I suppose that\x01",
            "about does it for this\x01",
            "interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThanks for your help\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI was able to obtain\x01",
            "some useful information\x01",
            "thanks to you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6P...Us too.\x02",
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
            "#11PThat's right, it's about\x01",
            "time for me to be heading\x01",
            "to my next interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIf you'll excuse me,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PI'd love to speak with\x01",
            "you all again, should\x01",
            "the opportunity arise.\x02",
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

    def lambda_A830():
        OP_95(0xD, 28680, 4019, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_A830)
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

    def lambda_A879():
        OP_95(0xD, 9240, -490, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_A879)
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
            "#10105F#12PI don't know what you\x01",
            "guys were talking about,\x01",
            "but he's rather carefree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#11PHmm, he's really\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PHow to say this... He's\x01",
            "a surprising man, in\x01",
            "many ways.\x02\x03",
            "#00000FAnd with regard to the\x01",
            "matter of KeA, it seems\x01",
            "believable.\x02",
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
            "just now was Marcell Nielsen─\x02\x03",
            "He's a famous journalist from\x01",
            "Crossbell who won the\x01",
            "Fuelitzer Prize 10 years ago.\x02",
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
            "#10305F#11PWow. I don't know too much\x01",
            "about these things, but\x01",
            "the Fuelitzer Prize...\x02",
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
            "#10101F#12PI see... So that's where\x01",
            "his insight comes from,\x01",
            "huh.\x02\x03",
            "#10105FBut if he's from\x01",
            "Crossbell, that means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PYes, he was once a reporter for\x01",
            "Crossbell News.\x02\x03",
            "#00108FAnd the coverage for which he won the\x01",
            "award─ was war coverage in which he\x01",
            "lost his sight.\x02\x03",
            "#00100FBut after that, he continued covering\x01",
            "news throughout the continent,\x01",
            "contributing to many news magazines.\x02\x03",
            "#00104FHe's famous among journalists─ He's\x01",
            "that kind of person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PHmm. In that case, he's\x01",
            "an unthinkably big deal,\x01",
            "eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PNielsen, huh...\x02\x03",
            "#00000FI'd like to speak with\x01",
            "him again if we get\x01",
            "another chance.\x02",
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
            "Quest [Cult Incident\x01",
            "Coverage Assistance]\x01\x07\x00",
            "completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF1A")
    OP_2C(0x6E, 0x2)
    Jump("loc_AF2E")

    label("loc_AF1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF2E")
    OP_2C(0x6E, 0x1)

    label("loc_AF2E")

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

    # Function_29_8144 end

    def Function_30_AF97(): pass

    label("Function_30_AF97")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0BF")
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
    Jump("loc_B11E")

    label("loc_B0BF")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_B11E")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FGood day, Uncle Miles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ah, Lloyd. Did you see\x01",
            "my request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYeah, that's exactly it.\x02\x03",
            "Can you tell us the\x01",
            "situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt was about wanting to collect\x01",
            "ancient documents remaining in\x01",
            "the Tower of Stargaze, right?\x02",
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
            "You know about the Tower of\x01",
            "Stargaze ruin on the outskirts\x01",
            "of St. Ursula Byroad, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For a while now, investigation\x01",
            "has been prohibited by the\x01",
            "Guardian Force, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Lately, investigations\x01",
            "are permitted with\x01",
            "special permission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FThat is indeed the case.\x02\x03",
            "#10100FThe previous commander left that place\x01",
            "uninvestigated.\x02\x03",
            "For gathering information, even\x01",
            "regular citizens are permitted entry\x01",
            "on the condition they file a report...\x02\x03",
            "Because it seems the monsters have\x01",
            "disappeared recently as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, is that right...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B5A8")

    ChrTalk(
        0xC,
        (
            "Yes, and Nielsen went\x01",
            "inside to investigate\x01",
            "the other day.\x02",
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
            "#00005FB-But Nielsen's eyes\x01",
            "were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, that's right, but... That\x01",
            "was when we was taken along as\x01",
            "a Crossbell Times reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ah, what a dynamic guy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B877")

    label("loc_B5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_END)), "loc_B725")

    ChrTalk(
        0xC,
        (
            "Yes, and Nielsen went\x01",
            "inside to investigate\x01",
            "the other day.\x02",
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
            "#00000FNielsen... He's that\x01",
            "journalist you were\x01",
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
            "Yeah. Actually, he has\x01",
            "poor vision, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems a Crossbell\x01",
            "Times reporter took him\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B877")

    label("loc_B725")


    ChrTalk(
        0xC,
        (
            "Yes, and the other day, my\x01",
            "reporter friend Nielsen\x01",
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
            "place to investigate? Nielsen\x01",
            "seems like a real go-getter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah. Actually, he has\x01",
            "poor vision, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems a Crossbell\x01",
            "Times reporter took him\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B877")


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
            "chasing after Yin.\x02",
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
            "The ancient documents\x01",
            "you're looking for must be\x01",
            "there.\x02",
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
            "Oh, you went there\x01",
            "already, did you?\x01",
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
        (
            "How 'bout it? Can I\x01",
            "count on you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThat is indeed an\x01",
            "important function of\x01",
            "the library, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FBut... Isn't it impossible for us\x01",
            "to transport such a huge quantity\x01",
            "of books just by ourselves?\x02\x03",
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
            "Yeah, of course I've no\x01",
            "intention of asking you\x01",
            "to do all that.\x02",
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
            "I've already secured permission\x01",
            "for your investigation from the\x01",
            "Guardian Force and City Hall.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BDB7")

    ChrTalk(
        0x103,
        (
            "#00202FI see, so that's how it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIn the end, you're just\x01",
            "advancing your plan to\x01",
            "collect the books.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE29")

    label("loc_BDB7")


    ChrTalk(
        0x105,
        (
            "#10304FI see. So that's how it\x01",
            "is.\x02\x03",
            "#10300FIn the end, you're just\x01",
            "advancing your plan to\x01",
            "collect the books.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE29")


    ChrTalk(
        0x102,
        (
            "#00100FWe're certainly\x01",
            "qualified, having climbed\x01",
            "the tower once before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How 'bout it? Will you\x01",
            "accept?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x71, 0x1, 0x0)
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEB5")
    Call(0, 33)

    label("loc_BEB5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BEEF")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_BEF9")

    label("loc_BEEF")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_BEF9")

    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_AF97 end

    def Function_31_BF11(): pass

    label("Function_31_BF11")

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
            "Cancel\x01",      # 1
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
        (0, "loc_BF6F"),
        (1, "loc_BF74"),
        (SWITCH_DEFAULT, "loc_C021"),
    )


    label("loc_BF6F")

    Jump("loc_C021")

    label("loc_BF74")


    ChrTalk(
        0x101,
        (
            "#00000FSorry uncle. Our hands\x01",
            "are full at the\x01",
            "moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, I see. It can't be\x01",
            "helped, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, if you get free,\x01",
            "please come speak with\x01",
            "me again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x152, 7)
    Jump("loc_C021")

    label("loc_C021")

    Return()

    # Function_31_BF11 end

    def Function_32_C022(): pass

    label("Function_32_C022")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51115.itc", 0x1E)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C11E")
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
    Jump("loc_C17D")

    label("loc_C11E")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_C17D")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "I'd like you all to investigate\x01",
            "the ancient documents that were\x01",
            "left in the Tower of Stargaze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To prepare to collect them, I\x01",
            "want to know what kind of cost\x01",
            "and effort will be required.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How 'bout it? Will you\x01",
            "accept?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C283")
    Call(0, 33)

    label("loc_C283")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C2BD")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_C2C7")

    label("loc_C2BD")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_C2C7")

    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_C022 end

    def Function_33_C2DF(): pass

    label("Function_33_C2DF")


    ChrTalk(
        0x101,
        (
            "#00002FYeah, got it. We'll take\x01",
            "it on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks. This really\x01",
            "helps me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "One moment please. I'll\x01",
            "contact the Guardian Force and\x01",
            "have them remove the barrier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FOh, please leave that to\x01",
            "me.\x02\x03",
            "It'll be faster if I\x01",
            "contact Commander Sonya\x01",
            "personally.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C3F4():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C3F4)
    Sleep(50)

    def lambda_C404():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C404)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C42F")

    def lambda_C424():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C424)
    Sleep(50)

    label("loc_C42F")


    def lambda_C434():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C434)
    Sleep(50)

    def lambda_C444():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C444)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FYeah, that seems like a\x01",
            "good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Then, please do.\x02",
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
            "─Yes, this is Commander\x01",
            "Sonya.\x02",
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
            "#10100FCommander, this is Noｱl\x01",
            "Seeker.\x02",
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
            "Oh, Noｱl. What's going\x01",
            "on?\x02",
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
            "Noｱl explained the tower\x01",
            "investigation request.\x02",
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
            "Oh, that.\x02\x03",
            "We know about the\x01",
            "request. You all are\x01",
            "certainly qualified.\x02\x03",
            "We'll remove the barrier\x01",
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
            "#10101FThank you ma'am!\x02",
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
            "Be careful. ...Bｴlz out.\x07\x00\x02",
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

    def lambda_C7D1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C7D1)
    Sleep(50)

    def lambda_C7E1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C7E1)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C80C")

    def lambda_C801():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C801)
    Sleep(50)

    label("loc_C80C")


    def lambda_C811():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C811)
    Sleep(50)

    def lambda_C821():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C821)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Yeah, that went\x01",
            "smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The Support Section sure\x01",
            "knows all the right\x01",
            "people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha, that's right.\x02\x03",
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
            "Quest [Tower Documents\x01",
            "Investigation]\x07\x00",
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

    # Function_33_C2DF end

    def Function_34_C9B5(): pass

    label("Function_34_C9B5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA7E")
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
    Jump("loc_CADD")

    label("loc_CA7E")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_CADD")

    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others\x01",
            "reported that the books on\x01",
            "the shelves had disappeared.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F...So, that's what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "N-No way! You're saying\x01",
            "someone took that many\x01",
            "books?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And what's more, they\x01",
            "were taken without\x01",
            "anyone noticing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...It's unfortunate, but\x01",
            "we have no idea what\x01",
            "happened to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Well, I suppose it\x01",
            "can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wanted to at least\x01",
            "find out what kind of\x01",
            "books they were, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FAh, well actually there\x01",
            "were a few books\x01",
            "remaining on the shelves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FThose were the only ones we\x01",
            "were able to collect, you\x01",
            "see...\x02\x03",
            "You might be able to get at\x01",
            "least some clue about the other\x01",
            "books by examining these.\x02",
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
            "#00000FIt's just, the contents\x01",
            "are unintelligible to\x01",
            "us.\x02\x03",
            "I have no idea how\x01",
            "valuable they are,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd handed over the\x01",
            "books they collected in\x01",
            "the tower.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "This is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThey appear to be books\x01",
            "from the middle ages for\x01",
            "some reason.\x02\x03",
            "They're old and stained, so\x01",
            "you might not be able to\x01",
            "make out the characters.\x02",
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
            "I-Incredible... This...\x01",
            "and this too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is a grimoire from\x01",
            "the middle ages!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FA grimoire... you say?\x02",
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
            "I won't know for sure until I\x01",
            "decode it, but from the schematics\x01",
            "alone, there's no mistake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FWow... It seems like a\x01",
            "pretty valuable book.\x02\x03",
            "#00003FBut, the fact that it\x01",
            "was still there means...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D198")

    ChrTalk(
        0x103,
        (
            "#00200FIt wasn't that important\x01",
            "to the one who took the\x01",
            "rest of them... right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIt seems difficult to get\x01",
            "any clue about them just\x01",
            "from this book, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D238")

    label("loc_D198")


    ChrTalk(
        0x105,
        (
            "#10300FIt wasn't that important\x01",
            "to the one who took the\x01",
            "rest of them... right?\x02\x03",
            "It seems difficult to get\x01",
            "any clue about them just\x01",
            "from this book, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D238")


    ChrTalk(
        0x101,
        "#00001FYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FThere's nothing left but\x01",
            "a complete mystery...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, no. That doesn't change\x01",
            "the fact that you collected\x01",
            "some valuable books for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Good work everyone. I\x01",
            "knew I could count on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha. It was our\x01",
            "pleasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll carefully store\x01",
            "this book in the\x01",
            "basement archives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Nielsen and the others\x01",
            "will be able to study\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks, guys. I'll let\x01",
            "you know if I ever need\x01",
            "your help again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAh, yes. We'll be\x01",
            "waiting.\x02",
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
            "Quest [Tower Documents\x01",
            "Investigation]\x07\x00\x01",
            "completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D4A9")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_D4B3")

    label("loc_D4A9")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_D4B3")

    OP_29(0x71, 0x1, 0x5)
    OP_29(0x71, 0x1, 0x6)
    OP_29(0x71, 0x4, 0x10)
    SetScenarioFlags(0x0, 5)
    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_34_C9B5 end

    def Function_35_D4DF(): pass

    label("Function_35_D4DF")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D5E3")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～Library News～\x01",
            "To answer your requests, the\x01",
            "books below have been added.\x01",
            "・Back-Alley Dr. Glenn Vol. 13\x01",
            "・Back-Alley Dr. Glenn Vol. 14\x01",
            "※These are on the 1F shelves.\x01",
            "Interested persons, please have a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_DA67")

    label("loc_D5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D71D")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～Library News～\x01",
            "To answer your requests, the\x01",
            "books below have been added.\x01",
            "・Back-Alley Dr. Glenn Vol. 9\x01",
            "・Back-Alley Dr. Glenn Vol. 10\x01",
            "・Back-Alley Dr. Glenn Vol. 11\x01",
            "・Back-Alley Dr. Glenn Vol. 12\x01",
            "※These are on the 1F shelves.\x01",
            "Interested persons, please have a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_DA67")

    label("loc_D71D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D7FE")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～Library News～\x01",
            "To answer your requests, the\x01",
            "book below has been added.\x01",
            "・One Minute Cooking - Sweets Edition\x01",
            "※This is on the 1F shelves.\x01",
            "Interested persons, please have a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_DA67")

    label("loc_D7FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D935")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～Library News～\x01",
            "To answer your requests, the\x01",
            "books below have been added.\x01",
            "・Back-Alley Dr. Glenn Vol. 5\x01",
            "・Back-Alley Dr. Glenn Vol. 6\x01",
            "・Back-Alley Dr. Glenn Vol. 7\x01",
            "・Back-Alley Dr. Glenn Vol. 8\x01",
            "※These are on the 1F shelves.\x01",
            "Interested persons, please have a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_DA67")

    label("loc_D935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DA67")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～Library News～\x01",
            "To answer your requests, the\x01",
            "books below have been added.\x01",
            "・Back-Alley Dr. Glenn Vol. 1\x01",
            "・Back-Alley Dr. Glenn Vol. 2\x01",
            "・Back-Alley Dr. Glenn Vol. 3\x01",
            "・Back-Alley Dr. Glenn Vol. 4\x01",
            "※These are on the 1F shelves.\x01",
            "Interested persons, please have a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_DA67")

    EventEnd(0x3)
    Return()

    # Function_35_D4DF end

    def Function_36_DA6A(): pass

    label("Function_36_DA6A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Mark and the Witch of\x01",
            "the Deep Forest" is on\x01",
            "the shelf.\x02",
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
            "[Cancel]\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB34")
    UseItem(0x2D6, 0xFF)

    label("loc_DB34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB48")
    UseItem(0x2DD, 0xFF)

    label("loc_DB48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB5C")
    UseItem(0x2DE, 0xFF)

    label("loc_DB5C")

    TalkEnd(0xFF)
    Return()

    # Function_36_DA6A end

    def Function_37_DB60(): pass

    label("Function_37_DB60")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Beauties that Moved the\x01",
            "Continent" is on the\x01",
            "shelf.\x02",
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
            "[Cancel]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBF0")
    UseItem(0x2D7, 0xFF)

    label("loc_DBF0")

    TalkEnd(0xFF)
    Return()

    # Function_37_DB60 end

    def Function_38_DBF4(): pass

    label("Function_38_DBF4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""How to Use 5 Extra\x01",
            "Minutes Effectively" is\x01",
            "on the shelf.\x02",
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
            "[Cancel]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC89")
    UseItem(0x2D8, 0xFF)

    label("loc_DC89")

    TalkEnd(0xFF)
    Return()

    # Function_38_DBF4 end

    def Function_39_DC8D(): pass

    label("Function_39_DC8D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Railway Mania\x01",
            "Recommendations" is on\x01",
            "the shelf.\x02",
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
            "[Cancel]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD19")
    UseItem(0x2D5, 0xFF)

    label("loc_DD19")

    TalkEnd(0xFF)
    Return()

    # Function_39_DC8D end

    def Function_40_DD1D(): pass

    label("Function_40_DD1D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Strange and Wonderful\x01",
            "Crossbell, The Complete\x01",
            "Works" is on the shelf.\x02",
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
            "[Cancel]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDBF")
    UseItem(0x2D9, 0xFF)

    label("loc_DDBF")

    TalkEnd(0xFF)
    Return()

    # Function_40_DD1D end

    def Function_41_DDC3(): pass

    label("Function_41_DDC3")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""The Goddess and the\x01",
            "White Wolf" is on the\x01",
            "shelf.\x02",
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
            "[Cancel]\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE71")
    UseItem(0x2DF, 0xFF)

    label("loc_DE71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE85")
    UseItem(0x2E0, 0xFF)

    label("loc_DE85")

    TalkEnd(0xFF)
    Return()

    # Function_41_DDC3 end

    def Function_42_DE89(): pass

    label("Function_42_DE89")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Arc-en-Ciel Fanbook" is\x01",
            "on the shelf.\x02",
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
            "[Cancel]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF0B")
    UseItem(0x2DA, 0xFF)

    label("loc_DF0B")

    TalkEnd(0xFF)
    Return()

    # Function_42_DE89 end

    def Function_43_DF0F(): pass

    label("Function_43_DF0F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DF26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E403")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 1")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[IBC]\x01",         # 0
            "[ZCF]\x01",         # 1
            "[Cancel]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1A2")
    SetChrName("")
    MenuTitle(-1, 25, 0, "IBC (International Bank of Crossbell)")
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An abbreviation for International Bank of Crossbell.\x01",
            "A megabank that manages and invests enormous wealth,\x01",
            "gathered from throughout the continent. It has\x01",
            "supported for many years not only Crossbell, but\x01",
            "also international financial and economic markets.\x02\x03",
            "In addition to developing investment and financial\x01",
            "products, they manage a theme park among other\x01",
            "things. In addition, they also supply the funds for\x01",
            "the Epstein Foundation's Orbal Network Project.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3FE")
    MenuTitle(-1, 25, 0, "ZCF (Zeiss Central Factory)")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An abbreviation for Zeiss Central Factory. Based in Liberl\x01",
            "Kingdom's city of Zeiss, their predecessor was the Zeiss\x01",
            "Technology Factory, established jointly with the Zeiss\x01",
            "Clockmaker Association by Professor A. Russell, personal\x01",
            "pupil of Professor Epstein, the inventor of orbments.\x02\x03",
            "They were the first company to successfully develop an orbal\x01",
            "airship, and are the leading orbal equipment maker on the\x01",
            "continent. In recent years, they completed the Arseille, a\x01",
            "high-speed cruiser used by the Liberl Royal Army.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E3FE")

    Jump("loc_DF26")

    label("loc_E403")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_43_DF0F end

    def Function_44_E410(): pass

    label("Function_44_E410")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E427")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF7E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 2")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Arc-en-Ciel]\x01",               # 0
            "[Holy City of Arteria]\x01",      # 1
            "[Verne Company]\x01",             # 2
            "[Erebonian Empire]\x01",          # 3
            "[Epstein Foundation]\x01",        # 4
            "[Cancel]\x01",                    # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E648")
    MenuTitle(-1, 25, 0, "Arc-en-Ciel")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An internationally famous troupe in Crossbell State.\x02\x03",
            "Their acrobatic performances and magnificent,\x01",
            "passionate plays continue to draw large audiences.\x02\x03",
            "Known by the stage name "Flame Dancer", currently\x01",
            "featured actress Ilya Platiｲre is especially popular\x01",
            "and has many crazy fans even in foreign countries.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E648")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E860")
    MenuTitle(-1, 25, 0, "Holy Nation of Arteria")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "City-state that is the HQ of the Septian Church.\x01",
            "Located in the central part of the Zemuria Continent,\x01",
            "it is known as a holy place where believers and\x01",
            "religious officials from all over the continent gather.\x02\x03",
            "Various organizations exist there, such as the\x01",
            ""Congregation for Divine Worship" that supervises most\x01",
            "rituals, the "Congregation for the Sacraments", said to\x01",
            "manage the Goddess' sacraments, and the "Papal Guard",\x01",
            "in charge of city defense.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E860")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA2D")
    MenuTitle(-1, 25, 0, "Verne Company")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Large integrated technology manufacturer based in\x01",
            "the Calvard Republic.\x02\x03",
            "On par with the Erebonian Empire's Reinford\x01",
            "Corporation, they are a well-established arms\x01",
            "maker that has researched and developed all kinds\x01",
            "of orbal goods since orbments were invented.\x02\x03",
            "Among them, they have developed a variety of\x01",
            "orbally powered vehicles, from orbal buses to\x01",
            "private cars and rail vehicles.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EA2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED89")
    MenuTitle(-1, 25, 0, "Erebonian Empire")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Situated to the west of Crossbell State, a gigantic\x01",
            "empire with the Golden Stallion as its symbol. The\x01",
            "current emperor is Eugent Reise Arnor.\x02\x03",
            "The country is ruled by an ancient system of noble\x01",
            "families, but under the command of Chancellor Giliath\x01",
            "Osborne, also known as the Blood and Iron Chancellor,\x01",
            "who came up through the military, the railway network\x01",
            "was spread throughout the nation, modernizing it.\x02\x03",
            "In addition to mechanization of the regular army, he\x01",
            "preserved the great military might of the noble\x01",
            "families' private armies which has strained relations\x01",
            "with foreign countries.\x02\x03",
            "Furthermore, the emperor's son, Prince Olivert,\x01",
            "cooperated in the resolution of the phenomenon that\x01",
            "ocurred in Liberl last year. In the Empire, it has\x01",
            "become a popular topic of conversation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ED89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF79")
    MenuTitle(-1, 25, 0, "Epstein Foundation")
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Foundation that inherited the achievements of Professor C.\x01",
            "Epstein, genius orbal scholar and inventor of orbments. As a\x01",
            "research institution and manufacturer, they are conspicuous\x01",
            "in the fields of communication and data processing.\x02\x03",
            "In addition to manufacturing tactical orbments that can\x01",
            "invoke arts, they have put effort into the Orbal Network\x01",
            "Project, developing communication and data processing\x01",
            "technologies.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF79")

    Jump("loc_E427")

    label("loc_EF7E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_44_E410 end

    def Function_45_EF8B(): pass

    label("Function_45_EF8B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EFA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB37")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 3")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Phantom Thief B]\x01",               # 0
            "[Calvard Republic]\x01",              # 1
            "[Crossbell State]\x01",               # 2
            "[Crystal Circuits/Quartz]\x01",       # 3
            "[Ancient Relics/Artifacts]\x01",      # 4
            "[Cancel]\x01",                        # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F339")
    MenuTitle(-1, 25, 0, "Phantom Thief B")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Great phantom thief who is active throughout the continent.\x01",
            "From jewels to orbal tanks, and regardless of the country\x01",
            "or person, he has carried out many thefts. Because of his\x01",
            "brilliant and splendid criminal techniques, he is famous\x01",
            "and has even earned himself some enthusiastic fans.\x02\x03",
            "He sends messages to various places detailing his plans,\x01",
            "sometimes showing himself in a mask and clad in a white\x01",
            "cloak, but his true identity is shrouded in mystery. In\x01",
            "recent years, he himself spoke of a "Liberation Movement of\x01",
            "Beauty". Although he unexpectedly performed them in the\x01",
            "Erebonian Empire, his magnificent series of crimes gave\x01",
            "rise to new topics of discussion.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F339")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F526")
    MenuTitle(-1, 25, 0, "Calvard Republic")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Republic set to the east of Crossbell. It became a\x01",
            "democracy about one hundred years ago. The current\x01",
            "ruler is President Rocksmith.\x02\x03",
            "Possessing a vast territory, it has a diverse cultural\x01",
            "background due to its acceptance of immigrants from\x01",
            "the East.\x02\x03",
            "Though after signing the Non-Aggression Pact they have\x01",
            "calmed down, historically, conflicts between Calvard\x01",
            "and the Erebonian Empire have occurred many a time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F526")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F765")
    MenuTitle(-1, 25, 0, "Crossbell State")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Autonomous state situated in the west part of the Zemuria\x01",
            "continent. Located between the two major powers of the\x01",
            "Erebonian Empire and Calvard Republic, although there were\x01",
            "fierce territorial conflicts, it was established as an\x01",
            "autonomous state 70 years ago.\x02\x03",
            "In present day, the central Crossbell City has grown into\x01",
            "the continent's largest and most prominent trade city. It\x01",
            "has a transcontinental railroad connecting the Empire and\x01",
            "the Republic and is an international hub for airship travel.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F765")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8A5")
    MenuTitle(-1, 25, 0, "Crystal Circuits/Quartz")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Circuits with a crystalline structure of\x01",
            "refined and processed sepith, fragments of\x01",
            "septium.\x02\x03",
            "They are energy sources as well as devices that\x01",
            "cause various phenomena. However they do not\x01",
            "exhibit effects if not set into an orbment.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F8A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB32")
    MenuTitle(-1, 25, 0, "Ancient Relics/Artifacts")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Orbments of an ancient civilization. Though they\x01",
            "operate using the orbments same orbal power, the\x01",
            "principles of operation are different.\x02\x03",
            "Said to have been created during the Ancient Zemurian\x01",
            "civilization, analysis is considered impossible given\x01",
            "current technology.\x02\x03",
            "Rarely discovered in ruins across the continent, they\x01",
            "exhibit powers surpassing even current human\x01",
            "understanding to no small degree.\x02\x03",
            "For this reason, Artifacts are defined by the Septian\x01",
            "Church as "Premature Gifts from the Goddess," and it\x01",
            "is said they have the duty to collect and manage them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FB32")

    Jump("loc_EFA2")

    label("loc_FB37")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_45_EF8B end

    def Function_46_FB44(): pass

    label("Function_46_FB44")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FB5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF66")
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
            "[Cancel]\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD8B")
    MenuTitle(-1, 25, 0, "Septian Church")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The religious organization devoted to the Sky Goddess\x01",
            "Aidios, who is most widely worshipped on the continent.\x01",
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

    label("loc_FD8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF61")
    MenuTitle(-1, 25, 0, "Septium")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A group of seven types of precious stones distributed\x01",
            "throughout the continent. Since ancient times, they\x01",
            "were highly valued as gemstones and mystic symbols.\x02\x03",
            "In present day, due to technology invented to make\x01",
            "quartz by processing and refining fragments too small\x01",
            "to be turned into jewels called Sepith, the\x01",
            "importance of septium resources has suddenly risen in\x01",
            "each country across the continent.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FF61")

    Jump("loc_FB5B")

    label("loc_FF66")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_46_FB44 end

    def Function_47_FF73(): pass

    label("Function_47_FF73")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FF8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1097A")
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
            "[Cancel]\x01",                 # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1018C")
    MenuTitle(-1, 25, 0, "Great Collapse")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The collapse of the Ancient Zemurian civilization thought to\x01",
            "have occurred approximately 1200 years ago. Though the cause\x01",
            "was said to have been a cataclysm, the details are unknown.\x02\x03",
            "After the civilization was lost because of the Great\x01",
            "Collapse, the people went through a long period of Dark\x01",
            "Ages.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1018C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103A2")
    MenuTitle(-1, 25, 0, "Fisherman's Guild")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A group of fishing professionals acting to popularize\x01",
            "fishing culture. Originally a noble and lover of\x01",
            "fishing, Mr. H. Fisher founded it and set up its HQ in\x01",
            "Liberl Kingdom's Grancel City.\x02\x03",
            "They search, investigate and develop fishing spots,\x01",
            "and also, discover talents and train new-generation\x01",
            "fishermen. Furthermore, in recent years, they have\x01",
            "engaged in development of fishing tools and baits.\x01",
            "Each year, they broaden the scope of their activities.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_103A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1072C")
    MenuTitle(-1, 25, 0, "Orbal Revolution")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The continent-scale technological revolution caused by\x01",
            "the development of orbments almost fifty years ago.\x02\x03",
            "In spite of the groundbreaking invention, the people of\x01",
            "those days met orbments with skepticism. However, as the\x01",
            "Epstein Foundation's orbal communication devices and the\x01",
            "ZCF's orbally-powered airship went out into the world,\x01",
            "the usefulness of orbments was acknowledged throughout\x01",
            "the continent.\x02\x03",
            "Nowadays, from heating, lighting and daily necessities to\x01",
            "rail and airships, tanks, guns and weapons, everything\x01",
            "you can think of has become orbally-powered. Orbments\x01",
            "have already become indispensable.\x02\x03",
            "In recent years, accompanied by miniaturization of\x01",
            "engines, Verne Corp. and Reinford Corp. have continued to\x01",
            "develop high performance orbally-powered cars and they\x01",
            "are starting to become popular with ordinary people.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1072C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10975")
    MenuTitle(-1, 25, 0, "Orbments")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Generic term for machines developed by Professor C. Epstein\x01",
            "which draw out orbal power from septium, producing various\x01",
            "effects.\x02\x03",
            "The orbment's internal structure and gear movements cause\x01",
            "crystal circuits of processed septium to mutually interfere,\x01",
            "causing a countless number of potential effects to manifest.\x02\x03",
            "In addition to their usefulness and effect variation, "with\x01",
            "time, the internal orbal power recovers." For this reason,\x01",
            "orbments have far higher economic efficiency than burning or\x01",
            "internal combustion.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10975")

    Jump("loc_FF8A")

    label("loc_1097A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_47_FF73 end

    def Function_48_10987(): pass

    label("Function_48_10987")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1099E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EAB")
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
            "[Eastern Quarter]\x01",            # 2
            "[Cancel]\x01",                     # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B56")
    MenuTitle(-1, 25, 0, "Orbal Arts")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By inserting quartz in specially designed\x01",
            "Tactical Orbments made by the Epstein\x01",
            "Foundation, "Magic" can be invoked.\x02\x03",
            "Generally called "Arts", with training,\x01",
            "anyone can use these techniques, making\x01",
            "them popular in the CGF, police and guild.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D02")
    MenuTitle(-1, 25, 0, "Orbal Network Project")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An innovative information network project promoted by\x01",
            "the Epstein Foundation. With terminals connected by\x01",
            "orbal cables, it is possible to exchange vast\x01",
            "quantities of information.\x02\x03",
            "Though originally developed together with Liberl's\x01",
            "ZCF, currently, the IBC has started to providing funds\x01",
            "for a full-scale trial installation in Crossbell City.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10D02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EA6")
    MenuTitle(-1, 25, 0, "Eastern Quarter")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Large-scale district made up of people of Eastern\x01",
            "descent in the Calvard Republic. Various cultures,\x01",
            "people and goods come and go, and it has been called\x01",
            ""the intersection of Eastern and Western culture".\x02\x03",
            "Though exotic buildings stand in rows and it is\x01",
            "famous as a tourist attraction, there are rumors of\x01",
            "a large syndicate of Easterners.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10EA6")

    Jump("loc_1099E")

    label("loc_10EAB")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_48_10987 end

    def Function_49_10EB8(): pass

    label("Function_49_10EB8")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10ECF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11517")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 7")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Hundred Days' War]\x01",        # 0
            "[Non-Aggression Pact]\x01",      # 1
            "[Cancel]\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112A2")
    MenuTitle(-1, 25, 0, "Hundred Days War")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A war between the Erebonian Empire and Liberl Kingdom in\x01",
            "year 1192 of the Septian Calendar. It is called this\x01",
            "because it ended in the approximately one hundred days\x01",
            "between the Empire's declaration of war and the\x01",
            "mediation by the Septian Church.\x02\x03",
            "At first, Liberl was forced into an inferior position.\x01",
            "Though most of the country was occupied by Imperial\x01",
            "troops, at the same time, a cutting-edge defense airship\x01",
            "was used in a shocking counteroffensive strategy. In the\x01",
            "blink of an eye, the war situation was reversed.\x02\x03",
            "As for the original reason for the outbreak of war,\x01",
            "because both countries kept their silence, in the end it\x01",
            "was not brought to light, but the Imperial government\x01",
            "later wrote in its official apology to Liberl that it\x01",
            "had been "due to an unfortunate misunderstanding".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_112A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11512")
    MenuTitle(-1, 25, 0, "Non-Aggression Pact")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "International treaty entered into by Liberl Kingdom, the\x01",
            "Erebonian Empire and the Calvard Republic in year 1202 of\x01",
            "the Septian Calendar. It was proposed by Queen Alicia of\x01",
            "Liberl and signed at Erbe Royal Villa in the same country.\x02\x03",
            "There is no legal compelling force in the treaty, but\x01",
            "after entering into it, the developing large-scale\x01",
            "military exercises on the outskirts of the Crossbell State\x01",
            "by both the Empire and Republic were broken up, greatly\x01",
            "easing the state of tension. It can certainly be said the\x01",
            "treaty had a visible effect.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11512")

    Jump("loc_10ECF")

    label("loc_11517")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_49_10EB8 end

    def Function_50_11524(): pass

    label("Function_50_11524")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1153B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A1A")
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
            "[Cancel]\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11714")
    MenuTitle(-1, 25, 0, "Michelam")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "High-class health resort situated southeast of Elm\x01",
            "Lake. Since IBC started work on the project two\x01",
            "years ago, a resort hotel and theme park have been\x01",
            "constructed and it has become a popular attraction.\x02\x03",
            "Even the local mascot character Mishy is gaining a\x01",
            "lot of popularity from the citizens and tourists.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11714")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A15")
    MenuTitle(-1, 25, 0, "Bracer Guild")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Nongovernmental organization of "bracers" who work to\x01",
            "protect regional peace and civilians. Because of its\x01",
            "branches in various places throughout the continent, they\x01",
            "have no small degree of influence.\x02\x03",
            "Though their ideal is to protect civilians above all\x01",
            "else, they have a weakness due to their organization's\x01",
            "code that, as long as civilian safety is not threatened,\x01",
            "they cannot exercise the rights of investigation and\x01",
            "arrest against nations and public authorities.\x02\x03",
            "As for the Crossbell branch, because of the occurrence of\x01",
            "many international incidents, they have assembled capable\x01",
            "people, starting with the Divine Blade of Wind, Arios\x01",
            "MacLaine, and they have earned the citizens' support.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11A15")

    Jump("loc_1153B")

    label("loc_11A1A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_50_11524 end

    def Function_51_11A27(): pass

    label("Function_51_11A27")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11A3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12574")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Section 9")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Reinford Company]\x01",               # 0
            "[Principality of Remiferia]\x01",      # 1
            "[Lｳman State]\x01",                   # 2
            "[Liberl Kingdom]\x01",                 # 3
            "[Jaegers]\x01",                        # 4
            "[Cancel]\x01",                         # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CE3")
    MenuTitle(-1, 25, 0, "Reinford Corporation")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Large integrated technology manufacturer based in the\x01",
            "Erebonian Empire. It was originally an arms workshop\x01",
            "specializing in guns and heavy weapons using gunpowder.\x02\x03",
            "Since the development of orbments, they have turned\x01",
            "their hand towards not only orbal guns and weapons but\x01",
            "also orbal rail and airships. Together with the Verne\x01",
            "Corporation of the Calvard Republic, it has grown to\x01",
            "call itself one of the world's two large manufacturers.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11CE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F67")
    MenuTitle(-1, 25, 0, "Principality of Remiferia")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A principality situated in the northern part of the\x01",
            "Zemuria continent. Although a rigid northern country,\x01",
            "it is blessed with abundant forests and lakes, and\x01",
            "many people visit with the goal of sightseeing,\x01",
            "charmed by those scenic and beautiful landscapes.\x02\x03",
            "Also famous for its advanced medical care,\x01",
            "representatives from the continent's medical equipment\x01",
            "makers are concentrated there, and it has turned out\x01",
            "many excellent doctors. Additionally, Crossbell's St.\x01",
            "Ursula Medical College was established with\x01",
            "cooperation from the Principality of Remiferia.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11F67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120C1")
    MenuTitle(-1, 25, 0, "Lｳman State")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An autonomous state in the central part of the Zemuria\x01",
            "continent. The HQ of the Epstein Foundation is there,\x01",
            "as well as the hometown of Professor C. Epstein.\x02\x03",
            "Additionally, it is also famous for being home to the\x01",
            "Bracer Guild HQ with its branches throughout\x01",
            "continent.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_120C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123E1")
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
            "Though its national power is inferior to its\x01",
            "neighbors, through its abundant septium resources,\x01",
            "excellent technology and skillful foreign policy, it\x01",
            "has built relationships on an equal footing with them.\x02\x03",
            "Last year, a mysterious gigantic structure (details\x01",
            "unknown) appeared in Valleria Lake in the center of\x01",
            "the kingdom. Though a strange phenomenon where all\x01",
            "orbments in the country stopped functioning occurred,\x01",
            "through the work of the army and the Bracer Guild, the\x01",
            "matter was resolved peacefully, restoring order.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_123E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1256F")
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

    label("loc_1256F")

    Jump("loc_11A3E")

    label("loc_12574")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_51_11A27 end

    def Function_52_12581(): pass

    label("Function_52_12581")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Volumes of "Back-Alley\x01",
            "Doctor Glenn" are on the\x01",
            "shelf.\x02",
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
            "[Cancel]\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1262F")
    UseItem(0x2D2, 0xFF)

    label("loc_1262F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12643")
    UseItem(0x2D3, 0xFF)

    label("loc_12643")

    TalkEnd(0xFF)
    Return()

    # Function_52_12581 end

    def Function_53_12647(): pass

    label("Function_53_12647")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Volumes of "Back-Alley\x01",
            "Doctor Glenn" are on the\x01",
            "shelf.\x02",
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
            "[Cancel]\x01",              # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12716")
    UseItem(0x2CE, 0xFF)

    label("loc_12716")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1272A")
    UseItem(0x2CF, 0xFF)

    label("loc_1272A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1273E")
    UseItem(0x2D0, 0xFF)

    label("loc_1273E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12752")
    UseItem(0x2D1, 0xFF)

    label("loc_12752")

    TalkEnd(0xFF)
    Return()

    # Function_53_12647 end

    def Function_54_12756(): pass

    label("Function_54_12756")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Volumes of "Back-Alley\x01",
            "Doctor Glenn" are on the\x01",
            "shelf.\x02",
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
            "[Cancel]\x01",             # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12822")
    UseItem(0x2CA, 0xFF)

    label("loc_12822")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12836")
    UseItem(0x2CB, 0xFF)

    label("loc_12836")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1284A")
    UseItem(0x2CC, 0xFF)

    label("loc_1284A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1285E")
    UseItem(0x2CD, 0xFF)

    label("loc_1285E")

    TalkEnd(0xFF)
    Return()

    # Function_54_12756 end

    def Function_55_12862(): pass

    label("Function_55_12862")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Volumes of "Back-Alley\x01",
            "Doctor Glenn" are on the\x01",
            "shelf.\x02",
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
            "[Cancel]\x01",             # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1292E")
    UseItem(0x2C6, 0xFF)

    label("loc_1292E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12942")
    UseItem(0x2C7, 0xFF)

    label("loc_12942")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12956")
    UseItem(0x2C8, 0xFF)

    label("loc_12956")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1296A")
    UseItem(0x2C9, 0xFF)

    label("loc_1296A")

    TalkEnd(0xFF)
    Return()

    # Function_55_12862 end

    SaveToFile()

Try(main)
