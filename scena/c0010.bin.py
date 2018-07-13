from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0010.bin",                # FileName
        "c0010",                    # MapName
        "c0010",                    # Location
        0x0003,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 3, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0010",                  # 0
        "Station Attendant Lux",  # 1
        "Station Attendant Lisa", # 2
        "Station Attendant Heim", # 3
        "Attendant Schenly",      # 4
        "Attendant Maggis",       # 5
        "Inspector Quattro",      # 6
        "Fei",                    # 7
        "Billy",                  # 8
        "Businessman",            # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Elderly Man",            # 12
        "Elderly Woman",          # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Boy",                    # 16
        "Mueller",                # 17
        "Inspector Marlowe",      # 18
        "Detective Raymond",      # 19
        "Eastern-looking Man",    # 20
        "Eastern-looking Man",    # 21
    ))

    AddCharChip((
        "chr/ch46600.itc",                   # 00
        "chr/ch46400.itc",                   # 01
        "chr/ch30200.itc",                   # 02
        "chr/ch12500.itc",                   # 03
        "chr/ch31500.itc",                   # 04
        "chr/ch00100.itc",                   # 05
        "chr/ch00200.itc",                   # 06
        "chr/ch00300.itc",                   # 07
        "chr/ch02900.itc",                   # 08
        "chr/ch03000.itc",                   # 09
        "chr/ch28300.itc",                   # 0A
        "chr/ch28400.itc",                   # 0B
        "chr/ch28500.itc",                   # 0C
        "chr/ch32700.itc",                   # 0D
        "chr/ch27600.itc",                   # 0E
        "chr/ch32200.itc",                   # 0F
        "chr/ch32400.itc",                   # 10
        "chr/ch33000.itc",                   # 11
        "chr/ch20900.itc",                   # 12
        "chr/ch22100.itc",                   # 13
        "chr/ch22000.itc",                   # 14
        "chr/ch22200.itc",                   # 15
        "chr/ch32202.itc",                   # 16
        "chr/ch32402.itc",                   # 17
        "chr/ch33002.itc",                   # 18
        "chr/ch20902.itc",                   # 19
        "chr/ch22102.itc",                   # 1A
        "chr/ch22002.itc",                   # 1B
        "chr/ch22202.itc",                   # 1C
        "chr/ch27602.itc",                   # 1D
        "chr/ch23600.itc",                   # 1E
    ))

    DeclNpc(4750,    0,       7500,    180,  257,  0x0, 0,   10,  0,   0,   0,   0,   5,   255,  0)
    DeclNpc(9500,    0,       7500,    180,  257,  0x0, 0,   11,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(33000,   4000,    8000,    270,  257,  0x0, 0,   11,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(33000,   4000,    4294959296, 270,  257,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(18260,   0,       10229,   180,  257,  0x0, 0,   10,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(28000,   4000,    10000,   180,  385,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294913916, 0,       52599,   270,  385,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(2809,    29,      2299,    45,   389,  0x0, 0,   30,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   14,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   16,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   17,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   18,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   19,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   20,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   21,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(19209,   0,       4294963146, 270,  385,  0x0, 0,   0,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(28000,   4000,    10000,   180,  385,  0x0, 0,   1,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(14090,   29,      19,      90,   385,  0x0, 0,   2,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(15550,   0,       9319,    90,   385,  0x0, 0,   3,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(16600,   0,       9319,    270,  385,  0x0, 0,   4,   0,   0,   0,   0,   31,  255,  0)

    DeclActor(4750,    0,       6500,    1000,    4750,    1500,    7500,    0x007E, 0,  4,  0x0000)
    DeclActor(9500,    0,       6500,    1000,    9500,    1500,    7500,    0x007E, 0,  7,  0x0000)
    DeclActor(32000,   4000,    8000,    1000,    33000,   5500,    8000,    0x007E, 0,  11, 0x0000)
    DeclActor(32000,   4000,    4294959296, 1000,    33000,   5500,    4294959296, 0x007E, 0,  13, 0x0000)
    DeclActor(20560,   0,       4090,    1000,    20560,   1500,    4090,    0x007C, 0,  51, 0x0000)
    DeclActor(20130,   0,       4294962486, 1000,    20130,   1500,    4294962486, 0x007C, 0,  52, 0x0000)
    DeclActor(31150,   4000,    1130,    1000,    31150,   5500,    1130,    0x007C, 0,  53, 0x0000)
    DeclActor(28100,   4000,    11510,   1000,    28100,   5500,    11510,   0x007C, 0,  54, 0x0000)
    DeclActor(30940,   4000,    4294965396, 1000,    30940,   5500,    4294965396, 0x007C, 0,  55, 0x0000)
    DeclActor(3250,    0,       4294958496, 1200,    3250,    400,     4294958496, 0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1448, 0)                                       # 0

    ScpFunction((
        "Function_0_5A8",          # 00, 0
        "Function_1_660",          # 01, 1
        "Function_2_AE6",          # 02, 2
        "Function_3_BBC",          # 03, 3
        "Function_4_C6D",          # 04, 4
        "Function_5_C71",          # 05, 5
        "Function_6_1252",         # 06, 6
        "Function_7_143C",         # 07, 7
        "Function_8_1440",         # 08, 8
        "Function_9_1988",         # 09, 9
        "Function_10_1B29",        # 0A, 10
        "Function_11_1F59",        # 0B, 11
        "Function_12_1F5D",        # 0C, 12
        "Function_13_23A0",        # 0D, 13
        "Function_14_23A4",        # 0E, 14
        "Function_15_2C25",        # 0F, 15
        "Function_16_2E01",        # 10, 16
        "Function_17_2E0B",        # 11, 17
        "Function_18_3013",        # 12, 18
        "Function_19_32A4",        # 13, 19
        "Function_20_346D",        # 14, 20
        "Function_21_3631",        # 15, 21
        "Function_22_39B3",        # 16, 22
        "Function_23_3B60",        # 17, 23
        "Function_24_3D8F",        # 18, 24
        "Function_25_3F64",        # 19, 25
        "Function_26_4070",        # 1A, 26
        "Function_27_4127",        # 1B, 27
        "Function_28_4451",        # 1C, 28
        "Function_29_4488",        # 1D, 29
        "Function_30_44D5",        # 1E, 30
        "Function_31_44DF",        # 1F, 31
        "Function_32_44E9",        # 20, 32
        "Function_33_457D",        # 21, 33
        "Function_34_4F73",        # 22, 34
        "Function_35_5AF3",        # 23, 35
        "Function_36_5D58",        # 24, 36
        "Function_37_5F6B",        # 25, 37
        "Function_38_6064",        # 26, 38
        "Function_39_621B",        # 27, 39
        "Function_40_6754",        # 28, 40
        "Function_41_6B47",        # 29, 41
        "Function_42_6B7D",        # 2A, 42
        "Function_43_78CF",        # 2B, 43
        "Function_44_7AB3",        # 2C, 44
        "Function_45_8592",        # 2D, 45
        "Function_46_86AB",        # 2E, 46
        "Function_47_86CA",        # 2F, 47
        "Function_48_86E9",        # 30, 48
        "Function_49_8715",        # 31, 49
        "Function_50_875E",        # 32, 50
        "Function_51_93BF",        # 33, 51
        "Function_52_944B",        # 34, 52
        "Function_53_94DB",        # 35, 53
        "Function_54_9533",        # 36, 54
        "Function_55_95BA",        # 37, 55
        "Function_56_9611",        # 38, 56
    ))


    def Function_0_5A8(): pass

    label("Function_0_5A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5E8"),
        (1, "loc_5F4"),
        (2, "loc_600"),
        (3, "loc_60C"),
        (4, "loc_618"),
        (5, "loc_624"),
        (6, "loc_630"),
        (SWITCH_DEFAULT, "loc_63C"),
    )


    label("loc_5E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_5F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_600")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_60C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_618")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_624")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_630")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_63C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_648")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_65F")

    Return()

    # Function_0_5A8 end

    def Function_1_660(): pass

    label("Function_1_660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_687")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_A77")

    label("loc_687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7A0")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, 1940, 0, 3880, 45)
    SetChrPos(0x13, 5700, 0, 3470, 315)
    SetChrPos(0x17, 4900, 30, 1340, 315)
    SetChrPos(0x14, 3750, 200, -5340, 0)
    SetChrChipByIndex(0x14, 0x19)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrPos(0x15, 19240, 30, -7910, 90)
    SetChrPos(0x16, 30700, 4019, 9620, 135)
    SetChrPos(0x10, 4400, 0, 5200, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x11, 10570, 0, 5190, 0)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0xC, 18260, 0, 10230, 270)
    SetChrPos(0xE, 16980, 0, 10250, 90)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x10)
    Jump("loc_A77")

    label("loc_7A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_911")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_875")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 5790, 200, -5340, 0)
    SetChrChipByIndex(0x10, 0x1D)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 3750, 200, -5340, 0)
    SetChrChipByIndex(0x13, 0x18)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 13490, 200, -9000, 0)
    SetChrChipByIndex(0x15, 0x1A)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 12490, 200, -9000, 0)
    SetChrChipByIndex(0x16, 0x1B)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 29290, 4000, -450, 90)
    SetChrFlags(0x17, 0x10)
    Jump("loc_8D9")

    label("loc_875")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 29680, 4000, 1320, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 3750, 200, -5340, 0)
    SetChrChipByIndex(0x12, 0x17)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 13490, 200, -9000, 0)
    SetChrChipByIndex(0x14, 0x19)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)

    label("loc_8D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90C")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1B, 0x10)
    SetChrFlags(0x1C, 0x10)

    label("loc_90C")

    Jump("loc_A77")

    label("loc_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9C4")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 29680, 4000, 1320, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 13490, 200, -9000, 0)
    SetChrChipByIndex(0x12, 0x17)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 12490, 200, -9000, 0)
    SetChrChipByIndex(0x17, 0x1C)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 3750, 200, -5340, 0)
    SetChrChipByIndex(0x15, 0x1A)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BF")
    ClearChrFlags(0x19, 0x80)

    label("loc_9BF")

    Jump("loc_A77")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A77")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 13490, 200, -9000, 0)
    SetChrChipByIndex(0x11, 0x16)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 29680, 4000, 1320, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 3750, 200, -5340, 0)
    SetChrChipByIndex(0x14, 0x19)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 11000, 200, -5560, 0)
    SetChrChipByIndex(0x16, 0x1B)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A77")
    ClearChrFlags(0x18, 0x80)

    label("loc_A77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA0")
    SetMapFlags(0x10000000)
    Event(0, 35)

    label("loc_AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_AB4")
    ClearScenarioFlags(0x22, 0)
    Event(0, 40)
    Jump("loc_AE5")

    label("loc_AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_AC8")
    ClearScenarioFlags(0x22, 1)
    Event(0, 50)
    Jump("loc_AE5")

    label("loc_AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_AE5")
    ClearScenarioFlags(0x22, 2)
    SetChrPos(0x0, 19270, 30, 7590, 270)

    label("loc_AE5")

    Return()

    # Function_1_660 end

    def Function_2_AE6(): pass

    label("Function_2_AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B25")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B6E")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B87")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)

    label("loc_B87")

    ClearMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA1")
    SetMapObjFlags(0x2, 0x10)

    label("loc_BA1")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BBB")
    SetMapObjFlags(0x1, 0x10)

    label("loc_BBB")

    Return()

    # Function_2_AE6 end

    def Function_3_BBC(): pass

    label("Function_3_BBC")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a car magazine, "Car Star Extra".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x373, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C69")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "You learned the\x01\x07\x02",
            ""Shine Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x373, 1)

    label("loc_C69")

    TalkEnd(0xFF)
    Return()

    # Function_3_BBC end

    def Function_4_C6D(): pass

    label("Function_4_C6D")

    Call(0, 5)
    Return()

    # Function_4_C6D end

    def Function_5_C71(): pass

    label("Function_5_C71")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C85")
    Call(0, 6)
    Jump("loc_124E")

    label("loc_C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_EF5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D86")

    ChrTalk(
        0x8,
        (
            "Thank you very much\x01",
            "for using Crossbell\x01",
            "Station today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Soon the Republic bound\x01",
            "train will depart, and then\x01",
            "the Empire one will follow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are in a haste, please hurry\x01",
            "and purchase your tickets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E1F")

    label("loc_D86")


    ChrTalk(
        0x8,
        (
            "Soon the Republic bound\x01",
            "train will depart, and then\x01",
            "the Empire one will follow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are in a haste, please hurry\x01",
            "and purchase your tickets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1F")

    Jump("loc_EF0")

    label("loc_E24")


    ChrTalk(
        0x8,
        (
            "When I heard that a criminal on\x01",
            "the loose jumped on a train roof,\x01",
            "I really couldn't believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, it seems that we will need to give\x01",
            "a warning in order for people to not imitate him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF0")

    Jump("loc_124E")

    label("loc_EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF9")

    ChrTalk(
        0x8,
        (
            "Thank you very much\x01",
            "for using Crossbell\x01",
            "Station today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "During the duration of the trade\x01",
            "conference, the platforms security\x01",
            "is strengthened by the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please be understanding of\x01",
            "the stricter inspections.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10A2")

    label("loc_FF9")


    ChrTalk(
        0x8,
        (
            "During the duration of the trade\x01",
            "conference, the platforms security\x01",
            "is strengthened by the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please be understanding of\x01",
            "the stricter inspections.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A2")

    Jump("loc_124E")

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_124E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A8")

    ChrTalk(
        0x8,
        (
            "Thank you very much\x01",
            "for using Crossbell\x01",
            "Station today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Trade Conference is taking place, but\x01",
            "the railway service is operating as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tickets can be bought\x01",
            "on the second floor, so\x01",
            "please, head over there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_124E")

    label("loc_11A8")


    ChrTalk(
        0x8,
        (
            "The trade conference is taking place, but\x01",
            "the railway service is operating as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tickets can be bought\x01",
            "on the second floor, so\x01",
            "please, head over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124E")

    TalkEnd(0x8)
    Return()

    # Function_5_C71 end

    def Function_6_1252(): pass

    label("Function_6_1252")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_136A")

    ChrTalk(
        0x8,
        (
            "Currently both the train\x01",
            "services towards the Empire\x01",
            "and the Republic are suspended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We are really causing a great\x01",
            "disservice to our customers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "No way, that's a problem!\x01",
            "I've got an important business\x01",
            "negotiation in the Empire...!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1433")

    label("loc_136A")


    ChrTalk(
        0x8,
        (
            "I am terribly sorry, but\x01",
            "we do not even know when\x01",
            "the service will resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish for you, Mr. customer,\x01",
            "to understand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "No way, my business negotiation, \x01",
            "my business negotiatiooon...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1433")

    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_6_1252 end

    def Function_7_143C(): pass

    label("Function_7_143C")

    Call(0, 8)
    Return()

    # Function_7_143C end

    def Function_8_1440(): pass

    label("Function_8_1440")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_144D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1984")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_149D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_14BC")
    OP_AF(0x8B)
    Jump("loc_153E")

    label("loc_14BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_14CC")
    OP_AF(0x8A)
    Jump("loc_153E")

    label("loc_14CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_14DC")
    OP_AF(0x89)
    Jump("loc_153E")

    label("loc_14DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_14EC")
    OP_AF(0x88)
    Jump("loc_153E")

    label("loc_14EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_14FC")
    OP_AF(0x87)
    Jump("loc_153E")

    label("loc_14FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_150C")
    OP_AF(0x86)
    Jump("loc_153E")

    label("loc_150C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_151C")
    OP_AF(0x85)
    Jump("loc_153E")

    label("loc_151C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_152C")
    OP_AF(0x84)
    Jump("loc_153E")

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_153C")
    OP_AF(0x83)
    Jump("loc_153E")

    label("loc_153C")

    OP_AF(0x82)

    label("loc_153E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_197F")

    label("loc_154D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1561")
    Jump("loc_197F")

    label("loc_1561")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_158B")
    Call(0, 9)
    Jump("loc_197F")

    label("loc_158B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16C8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161E")

    ChrTalk(
        0x9,
        (
            "What about a station boxed lunch\x01",
            "to go along with your trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have the newest issue\x01",
            "of Crossbell Times too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C3")

    label("loc_161E")


    ChrTalk(
        0x9,
        (
            "A criminal on the loose and the arrest of\x01",
            "terrorists... You don't hear often such\x01",
            "things to happen at the same time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Could they be just\x01",
            "some coincidences?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C3")

    Jump("loc_197F")

    label("loc_16C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_18A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F5")

    ChrTalk(
        0x9,
        (
            "Inspector Marlowe was transferred\x01",
            "from the Republican Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He doesn't get along well at all with\x01",
            "Inspector Quattro who was transferred\x01",
            "from the Imperial Army...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Somehow the Empire and Republic\x01",
            "have a relationship of disputes,\x01",
            "so it probably can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_189B")

    label("loc_17F5")


    ChrTalk(
        0x9,
        (
            "Inspectors Marlow and Quattro\x01",
            "don't go along well at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Somehow the Empire and Republic\x01",
            "have a relationship of disputes, so \x01",
            "it probably can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189B")

    Jump("loc_197F")

    label("loc_18A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_197F")

    ChrTalk(
        0x9,
        (
            "This morning it appears that even\x01",
            "journalists of the "Empire Chronicle",\x01",
            "an Empire publisher, came for materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The international conference\x01",
            "taking place in Crossbell has\x01",
            "generated a lot of visibility.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197F")

    Jump("loc_144D")

    label("loc_1984")

    TalkEnd(0x9)
    Return()

    # Function_8_1440 end

    def Function_9_1988(): pass

    label("Function_9_1988")

    OP_4B(0x9, 0xFF)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A87")

    NpcTalk(
        0x11,
        "Citizen",
        (
            "Damn, it's not a matter that I\x01",
            "can get a refund for the ticket!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Citizen",
        (
            "I had assiduously prepared for\x01",
            "today's trip, you know...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm t-terribly sorry. At present, we\x01",
            "are trying to confirm the facts too...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B20")

    label("loc_1A87")


    NpcTalk(
        0x11,
        "Citizen",
        (
            "Honestly, those who gets damaged\x01",
            "are always the customers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm t-terribly sorry. At present, we\x01",
            "are trying to confirm the facts too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B20")

    OP_4C(0x9, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_9_1988 end

    def Function_10_1B29(): pass

    label("Function_10_1B29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B3D")
    Call(0, 17)
    Jump("loc_1F55")

    label("loc_1B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1D35")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF2")

    ChrTalk(
        0xFE,
        (
            "Somehow that policeman\x01",
            "was restlessly looking around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is he chasing someone?\x01",
            "I didn't see anyone who entered\x01",
            "who was particularly suspicious...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D30")

    label("loc_1BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB1")

    ChrTalk(
        0xFE,
        (
            "Not only fake brand traders,\x01",
            "but even terrorists...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't know their faces,\x01",
            "so they could even slip\x01",
            "among normal people, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's some scary stuff...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1D30")

    label("loc_1CB1")


    ChrTalk(
        0xFE,
        (
            "Not only a fake brand trader,\x01",
            "but even terrorists could have\x01",
            "slipped among normal people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's some scary stuff...\x02",
    )

    CloseMessageWindow()

    label("loc_1D30")

    Jump("loc_1F55")

    label("loc_1D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E0E")

    ChrTalk(
        0xFE,
        (
            "Platform No. 3, where the Imperial\x01",
            "government exclusive train is stopped,\x01",
            "is strictly guarded by the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't mind if you give it a look, but\x01",
            "be sure to not get carelessly close.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F55")

    label("loc_1E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F55")

    ChrTalk(
        0xFE,
        (
            "This morning, the Imperial government\x01",
            "exclusive train "Eisengraf" arrived\x01",
            "at platform No. 1.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since the other trains are in regular service\x01",
            "they're moving it to platform No. 3.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's something you can rarely see, so\x01",
            "if you get the chance to go to the platform,\x01",
            "you should definitely go take a look at it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F55")

    TalkEnd(0xFE)
    Return()

    # Function_10_1B29 end

    def Function_11_1F59(): pass

    label("Function_11_1F59")

    Call(0, 12)
    Return()

    # Function_11_1F59 end

    def Function_12_1F5D(): pass

    label("Function_12_1F5D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_202A")

    ChrTalk(
        0xA,
        (
            "I am terribly sorry, but because\x01",
            "we are dealing with a train accident\x01",
            "the confusion is really great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please, be understanding\x01",
            "that you can not buy tickets\x01",
            "nor make reservations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_239C")

    label("loc_202A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_227A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212A")

    ChrTalk(
        0xA,
        (
            "The old lady who bought a\x01",
            "ticket for the Empire just\x01",
            "now looked very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems she is someone who has\x01",
            "been doing trades for many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I didn't hear the full details, \x01",
            "but I wish her good luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_21CD")

    label("loc_212A")


    ChrTalk(
        0xA,
        (
            "The old lady who bought a\x01",
            "ticket for the Empire just\x01",
            "now looked very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She was going to do trades in the Empire\x01",
            "or something. I wish her good luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21CD")

    Jump("loc_2275")

    label("loc_21D2")


    ChrTalk(
        0xA,
        (
            "The fake brand trader who was\x01",
            "caught in Altair City seems\x01",
            "to have been an old lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Could she have been the\x01",
            "old lady who bought the\x01",
            "ticket back then...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2275")

    Jump("loc_239C")

    label("loc_227A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2339")

    ChrTalk(
        0xA,
        (
            "At present, for a security reason,\x01",
            "we are making thoroughly hand\x01",
            "baggages inspections when entering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We are troubling you\x01",
            "a lot, but please,\x01",
            "understand and cooperate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_239C")

    label("loc_2339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_239C")

    ChrTalk(
        0xA,
        "This is the ticket counter.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please speak to me if you\x01",
            "wish to make a purchase.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_239C")

    TalkEnd(0xA)
    Return()

    # Function_12_1F5D end

    def Function_13_23A0(): pass

    label("Function_13_23A0")

    Call(0, 14)
    Return()

    # Function_13_23A0 end

    def Function_14_23A4(): pass

    label("Function_14_23A4")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E5")

    ChrTalk(
        0xB,
        (
            "Ah... I am sorry, could you\x01",
            "please wait a moment?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "At present we are suspending train\x01",
            "services due to a derailment accident\x01",
            "occurred on West Crossbell Highway.\x02\x03",
            "Furthermore, there are no prospects\x01",
            "for the service to be restored today.\x01",
            "Please understand.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2583")

    label("loc_24E5")


    ChrTalk(
        0xB,
        (
            "A private announcement\x01",
            "for dealing with refunds...\x01",
            "The situation must be hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It would be nice if the railway service\x01",
            "would be restored quickly...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2583")

    Jump("loc_2C21")

    label("loc_2588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2800")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2687")

    ChrTalk(
        0xB,
        (
            "Ah... I am sorry, could you\x01",
            "please wait a moment?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "Trains bound for the Republic and\x01",
            "Empire are going to depart soon.\x02\x03",
            "Please be very careful so to\x01",
            "not cause last minute rushes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_273D")

    label("loc_2687")


    ChrTalk(
        0xB,
        (
            "Last minute rushes are the\x01",
            "source of accidents and injuries.\x01",
            "They are very dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you are not making it in time,\x01",
            "please stay calm and board\x01",
            "the next incoming train.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273D")

    Jump("loc_27FB")

    label("loc_2742")


    ChrTalk(
        0xB,
        (
            "Not only last minute rushes, but\x01",
            "even people who board jumping\x01",
            "on the train roof... That scared me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Should it be something we would better\x01",
            "warn about with an announcement?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FB")

    Jump("loc_2C21")

    label("loc_2800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_296E")

    ChrTalk(
        0xB,
        (
            "Ah... I am sorry, could you\x01",
            "please wait a moment?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "Based on the Transcontinental Railway Public\x01",
            "Company rules, on-the-spot inspections \x01",
            "are performed in Crossbell Station.\x02\x03",
            "Passengers headed to the Empire and\x01",
            "Republic regions have to fill an entry written\x01",
            "application and present it to the Inspectors.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A1A")

    label("loc_296E")


    ChrTalk(
        0xB,
        (
            "To go to the Empire and Republic\x01",
            "from Crossbell Station, going through\x01",
            "an on-the-spot inspection is needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It is a little bit bothersome,\x01",
            "but please understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1A")

    Jump("loc_2C21")

    label("loc_2A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7B")

    ChrTalk(
        0xB,
        (
            "Ah... I am sorry, could you\x01",
            "please wait a moment?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "Today, due to the "Eisengraf" arrival, \x01",
            "the Imperial government exclusive train, \x01",
            "security has been strengthened.\x02\x03",
            "In accordance to this, passengers,\x01",
            "please understand that you can not enter\x01",
            "platform No. 3 while it is stopped there.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C21")

    label("loc_2B7B")


    ChrTalk(
        0xB,
        (
            "Excuse me, I am in charge of\x01",
            "the premises announcements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Could it be you have questions\x01",
            "about the use of the railway?\x01",
            "Please, feel free to ask me anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C21")

    TalkEnd(0xB)
    Return()

    # Function_14_23A4 end

    def Function_15_2C25(): pass

    label("Function_15_2C25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D07")

    ChrTalk(
        0xFE,
        (
            "When will I see the figures of\x01",
            "His Excellency the Chancellor\x01",
            "and Prince Olivert?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a simple Empire soldier it's an\x01",
            "extreme honor to be able to welcome\x01",
            "government important persons.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2D70")

    label("loc_2D07")


    ChrTalk(
        0xFE,
        (
            "...Mh? That large man in black clothes standing\x01",
            "on the first floor...I think I saw him somewhere...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D70")

    Jump("loc_2DFD")

    label("loc_2D75")


    ChrTalk(
        0xFE,
        (
            "Before I knew it, that large man in black\x01",
            "clothes vanished somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, he couldn't be...\x01",
            "Hm, it's probably my imagination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFD")

    TalkEnd(0xFE)
    Return()

    # Function_15_2C25 end

    def Function_16_2E01(): pass

    label("Function_16_2E01")

    TalkBegin(0xFE)
    Call(0, 17)
    TalkEnd(0xFE)
    Return()

    # Function_16_2E01 end

    def Function_17_2E0B(): pass

    label("Function_17_2E0B")

    OP_4B(0xE, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5C")

    ChrTalk(
        0xE,
        (
            "So, how's the train\x01",
            "damage situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Based on what they told us,\x01",
            "it's pretty bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If handled poorly, the train\x01",
            "itself could become useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hm... In this case, we\x01",
            "can only arrange for a\x01",
            "different train for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, now we must think\x01",
            "about resuming the service\x01",
            "as out top priority.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_300A")

    label("loc_2F5C")


    ChrTalk(
        0xE,
        (
            "Even the possibility of the rail tracks\x01",
            "to have been damaged could be high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As soon as the train removal operation\x01",
            "is over, let's go to the scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, roger.\x02",
    )

    CloseMessageWindow()

    label("loc_300A")

    OP_4C(0xE, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_17_2E0B end

    def Function_18_3013(): pass

    label("Function_18_3013")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3027")
    Call(0, 9)
    Jump("loc_32A0")

    label("loc_3027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30C7")

    ChrTalk(
        0xFE,
        (
            "Uhhm, it appears the train\x01",
            "is going to depart soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be helped then, I'll go shopping or\x01",
            "something and wait for the next train.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32A0")

    label("loc_30C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_30D5")
    Jump("loc_32A0")

    label("loc_30D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E6")

    ChrTalk(
        0xFE,
        (
            "I came from Altair City, the westernmost\x01",
            "harbor city of the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, Crossbell has really\x01",
            "had a staggering growth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Republic is pretty prosperous\x01",
            "too, however, compared to Crossbell,\x01",
            "you can consider it as countryside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_32A0")

    label("loc_31E6")


    ChrTalk(
        0xFE,
        (
            "I came from Altair City, the westernmost\x01",
            "harbor city of the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, Crossbell has really\x01",
            "had a staggering growth.\x01",
            "It makes you feel like the Republic is countryside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32A0")

    TalkEnd(0xFE)
    Return()

    # Function_18_3013 end

    def Function_19_32A4(): pass

    label("Function_19_32A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_32B8")
    Call(0, 6)
    Jump("loc_3469")

    label("loc_32B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3397")

    ChrTalk(
        0xFE,
        (
            "I have heard it from a station attendant...\x01",
            "It appears that terrorists remnants\x01",
            "were caught in the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems they had been hiding for a while,\x01",
            "but now we can feel safe for the time being.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3469")

    label("loc_3397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3460")

    ChrTalk(
        0xFE,
        "I'm going on a business trip in the Empire region.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The plenary session state worries me...\x01",
            "And it is going to be featured by their\x01",
            ""Imperial Chronicle"... Will it be all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3469")

    label("loc_3460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3469")

    label("loc_3469")

    TalkEnd(0xFE)
    Return()

    # Function_19_32A4 end

    def Function_20_346D(): pass

    label("Function_20_346D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_34C6")

    ChrTalk(
        0xFE,
        "A d-derailment accident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband... \x01",
            "How is my husband!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362D")

    label("loc_34C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3538")

    ChrTalk(
        0xFE,
        "I have finally arrived in Crossbell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "After taking a rest, I will go sightsee immediately.\x02",
    )

    CloseMessageWindow()
    Jump("loc_362D")

    label("loc_3538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3624")

    ChrTalk(
        0xFE,
        (
            "What do I have to do with you...\x01",
            "You already ate in the train all the roasted\x01",
            "chestnuts we had bought in Altair as souvenir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, do not come to cry\x01",
            "to me if you will not be able\x01",
            "to eat your dinner tonight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362D")

    label("loc_3624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_362D")

    label("loc_362D")

    TalkEnd(0xFE)
    Return()

    # Function_20_346D end

    def Function_21_3631(): pass

    label("Function_21_3631")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_36D2")

    ChrTalk(
        0xFE,
        (
            "Was it a rock fall?\x01",
            "Or something unnatural?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it was something unnatural...\x01",
            "I'll demand to the perpetrator\x01",
            "an eye-popping indemnity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AF")

    label("loc_36D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3781")

    ChrTalk(
        0xFE,
        (
            "It seems that a state of tension\x01",
            "continues at the border gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's what happens when you\x01",
            "advocate independence.\x01",
            "Youngsters should know their place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AF")

    label("loc_3781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_378F")
    Jump("loc_39AF")

    label("loc_378F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391B")

    ChrTalk(
        0xFE,
        (
            "They say that the Empire Chancellor,\x01",
            "Osborne, had ties with Hartmann, the\x01",
            "autonomous state former Chairman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it is whispered that the\x01",
            "Chancellor took measures to purge\x01",
            "him in case Hartmann had defected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He would've casted him away without mercy\x01",
            "in case he had become a handicap for him.\x01",
            "That's the kind of man the "Blood and Iron\x01",
            "Chancellor" is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_39AF")

    label("loc_391B")


    ChrTalk(
        0xFE,
        (
            "He would've casted him away without mercy\x01",
            "in case he had become a handicap for him.\x01",
            "That's the kind of man the "Blood and Iron\x01",
            "Chancellor" is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39AF")

    TalkEnd(0xFE)
    Return()

    # Function_21_3631 end

    def Function_22_39B3(): pass

    label("Function_22_39B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A36")

    ChrTalk(
        0xFE,
        (
            "For the railway to be stopped...\x01",
            "I wonder what has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Will I be able to go back to my country...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B5C")

    label("loc_3A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B00")

    ChrTalk(
        0xFE,
        (
            "What's with that blonde man?\x01",
            "He's been acting suspicious since a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...What, he's an officer?\x01",
            "He doesn't look to be dependable...\x01",
            "I wonder if everything will be all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B5C")

    label("loc_3B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B0E")
    Jump("loc_3B5C")

    label("loc_3B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B5C")

    ChrTalk(
        0xFE,
        "Isn't the train coming already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm dead tired of waiting.\x02",
    )

    CloseMessageWindow()

    label("loc_3B5C")

    TalkEnd(0xFE)
    Return()

    # Function_22_39B3 end

    def Function_23_3B60(): pass

    label("Function_23_3B60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3C57")

    ChrTalk(
        0xFE,
        (
            "Just when I was thinking that the train wasn't\x01",
            "departing no matter how much time passed...\x01",
            "A derailment accident happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I will spend the night in Crossbell today.\x01",
            "I hope to be able to get a room at an hotel...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8B")

    label("loc_3C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3CE5")

    ChrTalk(
        0xFE,
        (
            "I'm journeying to the Republic\x01",
            "together with my boyfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to enjoy the most the\x01",
            "Eastern District hot springs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8B")

    label("loc_3CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3D82")

    ChrTalk(
        0xFE,
        (
            "It seems that there're many nice\x01",
            "tourist spots in Crossbell too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears you can go there by bus too.\x01",
            "Maybe I should go see some.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8B")

    label("loc_3D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D8B")

    label("loc_3D8B")

    TalkEnd(0xFE)
    Return()

    # Function_23_3B60 end

    def Function_24_3D8F(): pass

    label("Function_24_3D8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3E33")

    ChrTalk(
        0xFE,
        (
            "I just finished get refunded the\x01",
            "tickets I had bought earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a long awaited trip, but this\x01",
            "time nothing can't be done about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F60")

    label("loc_3E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3ECA")

    ChrTalk(
        0xFE,
        (
            "I'm taking my girlfriend\x01",
            "on a trip now, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Does she really want to tour that much?\x01",
            "What if I don't have enough mira...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F60")

    label("loc_3ECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3ED8")
    Jump("loc_3F60")

    label("loc_3ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F60")

    ChrTalk(
        0xFE,
        (
            "They say that there's a\x01",
            "trade conference taking\x01",
            "place in Crossbell now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should we go see that\x01",
            "rumored Orchis Tower?\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F60")

    TalkEnd(0xFE)
    Return()

    # Function_24_3D8F end

    def Function_25_3F64(): pass

    label("Function_25_3F64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3F9C")

    ChrTalk(
        0xFE,
        "Hey, hey, has something happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_406C")

    label("loc_3F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3FE3")

    ChrTalk(
        0xFE,
        (
            "Tick tick...tick tick...\x01",
            "The clock...spins spins...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_406C")

    label("loc_3FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4063")

    ChrTalk(
        0xFE,
        (
            "*belch*...\x01",
            "Altair City was so fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a big river called Cyre.\x01",
            "A lot of boats pass through it too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_406C")

    label("loc_4063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_406C")

    label("loc_406C")

    TalkEnd(0xFE)
    Return()

    # Function_25_3F64 end

    def Function_26_4070(): pass

    label("Function_26_4070")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hey now, for real...?\x01",
            "What happened to the Republic cargo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now I'll have to consult with the old\x01",
            "man, contact the delivery destination...\x01",
            "Man, I'm gonna be busy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_4070 end

    def Function_27_4127(): pass

    label("Function_27_4127")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_414C")
    Call(0, 33)
    Return()

    label("loc_414C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_430A")

    ChrTalk(
        0xFE,
        (
            "#12400FOlivier Lenheim is a performing\x01",
            "musician who dresses in a white\x01",
            "coat and carries a lute.\x02\x03",
            "He probably thought about a\x01",
            "dubious place, bustling place or\x01",
            "an eating facility as his destination.\x02\x03",
            "I can say you are on the right track\x01",
            "with the Downtown, Back Street and\x01",
            "Waterfront Area you mentioned.\x02\x03",
            "If you have troubles taking him with you,\x01",
            "I don't mind if you use a little force on him.\x01",
            "Please, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_444D")

    label("loc_430A")


    ChrTalk(
        0xFE,
        (
            "#12400FI can think as Oliver destination\x01",
            "a dubious place, bustling place\x01",
            "or an eating facility.\x02\x03",
            "I can say you are on the right track\x01",
            "with the Downtown, Backstreet and\x01",
            "Waterfront Area you mentioned.\x02\x03",
            "If you have troubles taking him with you,\x01",
            "I don't mind if you use a little force on him.\x01",
            "Please, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_444D")

    TalkEnd(0xFE)
    Return()

    # Function_27_4127 end

    def Function_28_4451(): pass

    label("Function_28_4451")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4487")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4483")
    Call(0, 36)
    Jump("loc_4486")

    label("loc_4483")

    Call(0, 37)

    label("loc_4486")

    Return()

    label("loc_4487")

    Return()

    # Function_28_4451 end

    def Function_29_4488(): pass

    label("Function_29_4488")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44BB")
    Call(0, 42)
    Jump("loc_44BE")

    label("loc_44BB")

    Call(0, 43)

    label("loc_44BE")

    Return()

    label("loc_44BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44D1")
    Jump("loc_44D1")

    label("loc_44D1")

    TalkEnd(0xFE)
    Return()

    # Function_29_4488 end

    def Function_30_44D5(): pass

    label("Function_30_44D5")

    TalkBegin(0xFE)
    Call(0, 32)
    TalkEnd(0xFE)
    Return()

    # Function_30_44D5 end

    def Function_31_44DF(): pass

    label("Function_31_44DF")

    TalkBegin(0xFE)
    Call(0, 32)
    TalkEnd(0xFE)
    Return()

    # Function_31_44DF end

    def Function_32_44E9(): pass

    label("Function_32_44E9")

    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)

    ChrTalk(
        0x1B,
        (
            "...As expected, they seem\x01",
            "to plan to run away on train...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "...Hmph, how foolish...\x01",
            "To think they can escape us, I mean...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)
    OP_4C(0x1C, 0xFF)
    Return()

    # Function_32_44E9 end

    def Function_33_457D(): pass

    label("Function_33_457D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C4")
    FadeToDark(500, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12400.itp")
    Jump("loc_45C9")

    label("loc_45C4")

    Fade(500)

    label("loc_45C9")

    OP_4B(0x18, 0xFF)
    OP_68(17080, 1300, -3920, 0)
    MoveCamera(48, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15930, 0)
    SetChrPos(0x101, 17430, 0, -3570, 90)
    SetChrPos(0x102, 17390, 0, -4750, 90)
    SetChrPos(0x104, 15510, 0, -4080, 90)
    SetChrPos(0x109, 15980, 0, -3030, 90)
    SetChrPos(0x105, 15960, 0, -5340, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_466D")
    FadeToBright(500, 0)

    label("loc_466D")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D78")

    NpcTalk(
        0x18,
        "Large Man in Black",
        "#12400F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305F(Hey, Lloyd...\x01",
            "Somehow there's a guy\x01",
            "givin' off an amazing vibe...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(Don't tell me he's\x01",
            "the request client...)\x02\x03",
            "#00000FUhm, excuse us.\x01",
            "We're from the SSS...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x18,
        "Large Man in Black",
        (
            "#12404F...I've been waiting for you.\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Large Man in Black")

    AnonymousTalk(
        0xFF,
        (
            "My name is Mueller...\x01",
            "I work as a music manager\x01",
            "in the Empire.\x02\x03",
            "It will be for a short\x01",
            "time, but I'm pleased to\x01",
            "make your acquaintance.\x02",
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
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FOh, a music manager...is it?\x01",
            "(He doesn't look the part at all...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101F(If anything I'd say he\x01",
            "gives off an SP vibe...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105F(Moreover, I think I heard a\x01",
            "similar name somewhere before...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#12405F...Is anything the matter?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x101,
        (
            "#6P#00012FN-No...\x02\x03",
            "#00000FU-Uhmm...\x01",
            "Then, could you please explain\x01",
            "the details of your request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FI believe it was about a "musician"\x01",
            "having gone missing...\x02\x03",
            "#10302FI presume that you are part\x01",
            "of the management people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FYes, exactly.\x02\x03",
            "We entered Crossbell for\x01",
            "a concert tour, however...\x02\x03",
            "#12406FWhen I took my eyes away for a moment\x01",
            "from that musician, we got separated.\x02\x03",
            "#12400FI'm in a bind with no clues to search\x01",
            "in a city I'm not acquainted with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FWell, that is difficult for sure...\x01",
            "Crossbell City is big and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12401FYeah, that's true too...\x01",
            "It's a bothersome problem.\x02\x03",
            "#12400FCan I ask you to search immediately?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x76, 0x1, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Jump("loc_4DF7")

    label("loc_4D78")


    ChrTalk(
        0x18,
        (
            "#12400FI want to ask you to search\x01",
            "for the "musician" in the\x01",
            "city who went missing.\x02\x03",
            "Can I ask you to search immediately?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF7")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E47")
    Call(0, 34)
    Jump("loc_4F51")

    label("loc_4E47")


    ChrTalk(
        0x101,
        (
            "#6P#00006FHmm...\x01",
            "I'm terribly sorry.\x02\x03",
            "We're currently busy with something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12405FHm...\x01",
            "Too bad then.\x02\x03",
            "#12400FYou would really be of help if you spoke\x01",
            "again with me in case you're free.\x02\x03",
            "After all, I'm in a hurry too.\x01",
            "Please, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x156, 1)

    label("loc_4F51")

    SetChrPos(0x0, 17460, 0, -4190, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x18, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_33_457D end

    def Function_34_4F73(): pass

    label("Function_34_4F73")


    ChrTalk(
        0x101,
        (
            "#6P#00000FUnderstood.\x01",
            "Please, leave it to us.\x02\x03",
            "#00000FThen, could we hear some\x01",
            "details about the "musician"\x01",
            "we're searching for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FHm, fine then.\x02\x03",
            "The musician's name is...\x01",
            ""Olivier Lenheim".\x02\x03",
            "He's a blonde man in his\x01",
            "twenties, dresses a white\x01",
            "coat and carries a lute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FUhm, if he carries a musical instrument\x01",
            "then it seems he pretty stands out.\x02\x03",
            "#10300FI think it won't be that difficult\x01",
            "looking for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FYes, if it were only that,\x01",
            "finding him and taking him back\x01",
            "wouldn't have been a problem, but...\x02\x03",
            "#12406FOlivier has a slight...\x01",
            "...Personality problem.\x02\x03",
            "Even if not asked, he sticks his\x01",
            "nose in others' troubles by himself\x01",
            "and causes even more troubles.\x02\x03",
            "#12400FFrankly, you can probably say\x01",
            "that he's a troublesome character.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00105FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FI wish he would be found speedily to not\x01",
            "cause hindrances for the concert tour, but...\x01",
            "Well, it surely is not a reasonable expectation.\x02\x03",
            "#12406FIt would already help me if you could catch\x01",
            "him before he becomes obtrusive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FA-Although you're his manager, you\x01",
            "sure have your way with words 'bout him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FA-At any rate, we could make an\x01",
            "idea about him to a certain level.\x02\x03",
            "#00000FLastly, do you have any clue about\x01",
            "places he could've gone to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12405FRight, if I had to say...\x02\x03",
            "#12400FHe has a tendency to\x01",
            "like dubious places\x01",
            "or bustling ones.\x02\x03",
            "#12406FBeing a gourmet, it's also possible that he's\x01",
            "staying in an eating place somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FBasically, places where troubles\x01",
            "are likely to spark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FIn that case, the Downton, the\x01",
            "Entertainment District, Back Street...\x01",
            "Places like those come to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12404FYes, I can say you're on the right track, but...\x02\x03",
            "#12400F...Actually I have already finished\x01",
            "searching the Entertainment District.\x01",
            "You could leave that outside from your search field.\x02\x03",
            "#12406FPresuming I'm coming to search for him, he's\x01",
            "probably avoiding places I'd likely go to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FS-Sure...\x02\x03",
            "#00100FHowever, speaking of bustling places,\x01",
            "today there's the Waterfront Area too.\x02\x03",
            "#00100FIf I remember correctly, they should be\x01",
            "doing a Michey's official tour event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FHm...\x01",
            "Well, could be that a place\x01",
            "where he could go?\x02\x03",
            "#12406FI'm sorry, I'd want to offer you\x01",
            "some more important information...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FNo, you have helped us.\x02\x03",
            "#00000FWell then, we'll start the\x01",
            "search immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FPlease, I'm counting on you.\x02\x03",
            "If you have troubles taking him with you,\x01",
            "I don't mind if you use a little force on him.\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FU-Understood...\x01",
            "(My, what kind of relationship do they have?)\x02",
        )
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
            "Quest [Search for Musician]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x156, 0)
    OP_29(0x76, 0x1, 0x1)
    Return()

    # Function_34_4F73 end

    def Function_35_5AF3(): pass

    label("Function_35_5AF3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(5320, 1330, 440, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, 1500, 0, -500, 90)
    SetChrPos(0x102, 1550, 0, 500, 90)
    SetChrPos(0x103, 0, 0, -500, 90)
    SetChrPos(0x104, -250, 0, 500, 90)
    SetChrPos(0x109, 1200, 0, 1500, 90)
    SetChrPos(0x105, 500, 0, -1500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(18910, 2000)

    def lambda_5BB5():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BB5)
    Sleep(50)

    def lambda_5BD2():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5BD2)
    Sleep(50)

    def lambda_5BEF():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5BEF)
    Sleep(50)

    def lambda_5C0C():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C0C)
    Sleep(50)

    def lambda_5C29():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C29)
    Sleep(50)

    def lambda_5C46():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C46)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#00000FWell then, we came to\x01",
            "Crossbell Station...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThe train station inspector has\x01",
            "sent a support request, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes. Let's go visit him immediately.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x156, 5)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 2400, 30, -10, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_35_5AF3 end

    def Function_36_5D58(): pass

    label("Function_36_5D58")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x19, 0xFF)
    OP_68(27700, 5500, 8150, 0)
    MoveCamera(46, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17910, 0)
    SetChrPos(0x101, 28020, 4000, 8480, 0)
    SetChrPos(0x102, 28930, 4000, 8280, 0)
    SetChrPos(0x103, 27000, 4000, 8080, 0)
    SetChrPos(0x104, 27960, 4000, 7100, 0)
    SetChrPos(0x109, 27060, 4000, 6800, 0)
    SetChrPos(0x105, 28850, 4000, 6940, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    TurnDirection(0x19, 0x101, 0)
    OP_0D()

    ChrTalk(
        0x19,
        (
            "Oh, could you be the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, we saw your support request\x01",
            "and came to inquire.\x02\x03",
            "You are the Republican\x01",
            "Inspector officer, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Indeed I am. I am Marlowe, the Inspector\x01",
            "who was transferred from the Republican Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I want to immediately explain the job.\x01",
            "You will accept my request, right?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    EventEnd(0x5)
    Return()

    # Function_36_5D58 end

    def Function_37_5F6B(): pass

    label("Function_37_5F6B")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x19, 0xFF)
    OP_68(27700, 5500, 8150, 0)
    MoveCamera(46, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17910, 0)
    SetChrPos(0x101, 28020, 4000, 8480, 0)
    SetChrPos(0x102, 28930, 4000, 8280, 0)
    SetChrPos(0x103, 27000, 4000, 8080, 0)
    SetChrPos(0x104, 27960, 4000, 7100, 0)
    SetChrPos(0x109, 27060, 4000, 6800, 0)
    SetChrPos(0x105, 28850, 4000, 6940, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    TurnDirection(0x19, 0x101, 0)
    OP_0D()

    ChrTalk(
        0x19,
        (
            "Hmph, it's you.\x01",
            "You will accept my request, right?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    EventEnd(0x5)
    Return()

    # Function_37_5F6B end

    def Function_38_6064(): pass

    label("Function_38_6064")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60F3")

    ChrTalk(
        0x101,
        "#00000FYes, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Thank you.\x01",
            "Then, let me explain.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 39)
    Jump("loc_621A")

    label("loc_60F3")


    ChrTalk(
        0x101,
        (
            "#00003FI'm sorry.\x01",
            "We currently have another job to attend to...\x02\x03",
            "Can we come inquire again at a later time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Hmph, well, if it's for a little,\x01",
            "I can accommodate, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "As you can see, I'm busy too.\x01",
            "Please hurry as much as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x156, 6)
    SetChrPos(0x0, 27760, 4000, 8020, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x19, 0xFF)

    label("loc_621A")

    Return()

    # Function_38_6064 end

    def Function_39_621B(): pass

    label("Function_39_621B")


    ChrTalk(
        0x19,
        (
            "Well, there's something\x01",
            "I want to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'd like to have your help with an on-the-spot\x01",
            "inspection on a Republic bound train.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_63C8")

    ChrTalk(
        0x101,
        (
            "#00005FAn on-the-spot train inspection, it is?\x02\x03",
            "#00000FSince we helped once an\x01",
            "Imperial Inspector, I think\x01",
            "we know how it's done.\x02\x03",
            "We check to see if there're\x01",
            "suspicious persons or\x01",
            "objects on board, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Precisely. If you have experience,\x01",
            "things will be faster.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_648A")

    label("loc_63C8")


    ChrTalk(
        0x101,
        (
            "#00003FAn on-the-spot inspection, meaning...\x02\x03",
            "#00000FThat we check to see if there're\x01",
            "suspicious persons or\x01",
            "objects on board, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Precisely. It helps you\x01",
            "understand things quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_648A")


    ChrTalk(
        0x19,
        (
            "After all, due to the Trade \x01",
            "Conference now, security has \x01",
            "been increased all over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "In addition to the usual strict checking attitude,\x01",
            "there's also a cooperation with the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "We're now in a situation where no matter how\x01",
            "many inspectors there're, they're not enough.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x50, 0x1F4)
    Sound(801, 0, 100, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Station Attendant's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...The Republic bound train is going\x01",
            "to arrive soon at platform No. 1.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Passengers please watch\x01",
            "your steps and hurry to\x01",
            "the platform.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0x3E8)

    ChrTalk(
        0x19,
        (
            "It seems our train\x01",
            "has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I will give you the full\x01",
            "details at the platform.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Republican Inspector Assistance]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0xFF, 0xF9, 0x0)
    SetScenarioFlags(0x22, 2)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_621B end

    def Function_40_6754(): pass

    label("Function_40_6754")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 2500, 0, -500, 90)
    SetChrPos(0x102, 2250, 0, 500, 90)
    SetChrPos(0x103, 2250, 0, -1600, 90)
    SetChrPos(0x104, 750, 0, 500, 90)
    SetChrPos(0xF4, 750, 0, -800, 90)
    SetChrPos(0xF5, 750, 0, -2000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(30000, 3300, 500, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(31000, 0)
    OP_68(4500, 1300, 500, 8000)
    MoveCamera(45, 13, 0, 8000)
    SetCameraDistance(19000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    BeginChrThread(0x101, 3, 0, 41)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 4)), scpexpr(EXPR_END)), "loc_698A")

    ChrTalk(
        0x101,
        (
            "#5P#00006FThe doors were locked before, but...\x01\x02\x03",
            "#00013FIt appears that Miss Kilika and\x01",
            "Captain Lechter unlocked them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6936")

    ChrTalk(
        0x10A,
        (
            "#00601F#6PHmph, it's true it's an emergency situation,\x01",
            "doing whatever they want is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6936")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_698A")

    ChrTalk(
        0x109,
        (
            "#10108F#6PI can't say I approve since\x01",
            "it's illegal, however...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_698A")


    ChrTalk(
        0x104,
        (
            "#6P#00306FAaanyway, no one's here, huh.\x02\x03",
            "#00301FCan't be helped, with the\x01",
            "transcontinental railway stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FRight... The railway corporation personnel and\x01",
            "even the Imperial and Republican inspectors\x01",
            "were officially forced out of the country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FMiss Kilika and Mr. Lechter are at\x01",
            "the train on platform No. 3, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FYeah...\x01",
            "Let's descend and go there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 2000, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A5, 6)
    EventEnd(0x5)
    Return()

    # Function_40_6754 end

    def Function_41_6B47(): pass

    label("Function_41_6B47")

    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(900)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(600)

    def lambda_6B60():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B60)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_41_6B47 end

    def Function_42_6B7D(): pass

    label("Function_42_6B7D")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)
    OP_68(12070, 1530, -290, 0)
    MoveCamera(43, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, 12590, 30, 60, 90)
    SetChrPos(0x102, 12400, 30, 1030, 90)
    SetChrPos(0x103, 12300, 30, -870, 90)
    SetChrPos(0x104, 11250, 30, 60, 90)
    SetChrPos(0x109, 10940, 30, 1050, 90)
    SetChrPos(0x105, 10920, 30, -950, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x1A, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0x1A,
        "...Ah, you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Thank goodness, you saw the\x01",
            "request and came for it, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThank you for your hard work,\x01",
            "Mr. Raymond.\x02\x03",
            "#00005F...Oh, are you alone?\x01",
            "I don't see Inspector Donovan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Yes, something\x01",
            "happened and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Can I explain the\x01",
            "situation briefly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FPlease.\x02\x03",
            "#00101FAccording to the request, it seems you're\x01",
            "once again chasing that fake brand trader?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Because of the legal reform done by the\x01",
            "new mayor, it was decided to properly\x01",
            "supervise the fake brand traders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Even Section Two must strengthen\x01",
            "supervision in earnest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "In this situation,\x01",
            "that fake brand trader\x01",
            "had entered Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Thanks to persistent lookouts,\x01",
            "I finally succeeded in catching\x01",
            "that person in the act...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FThe fake brand trader...\x01",
            "Uhm, she was some passenger\x01",
            "who came via Tangram Gate, right?\x02\x03",
            "#10105FBy the way, in the end,\x01",
            "what kind of person was she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh right, you gave us a hand\x01",
            "guiding the passengers.\x02\x03",
            "#00003FUuhm, let's see, that person was...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x1A)

    ChrTalk(
        0x103,
        "#00200FSarcastic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FVery loud.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FQuick-footed\x01",
            "like a sprinter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FAt any rate, in a few words,\x01",
            ""one hell of a person"...I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x109,
        "#10105FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHu hu, seems an interesting one,\x01",
            "someone I'd definitely like to meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F...Well, in any case,\x01",
            "weren't you amazin'!?\x02\x03",
            "To be able to catch\x01",
            "that old lady!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Yes, well...\x01",
            "Everything went fine up to that point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "But after that, in the end,\x01",
            "she managed to run away.\x01",
            "...At a frightening speed.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00206FThat old lady never learns...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSo...\x01",
            "Do I have to assume the escaped fake\x01",
            "brand trader is inside the train station?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Yeah, exactly!\x01",
            "I knew you were quick-witted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "It appears she plans to escape\x01",
            "to the Empire region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Hu hu, I guess she's thinking that\x01",
            "she's scattered the police completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I spotted her at platform No. 2.\x01",
            "It seems she's calmly waiting for the train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUntil the Empire bound train\x01",
            "arrives there's still time...\x01",
            "It's the perfect chance to catch her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F...Hm?\x01",
            "But, if everything is\x01",
            "already arranged, then...\x02\x03",
            "#00303FDon't we have basically\x01",
            "anything to do in it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "A-About that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Since Inspector Donovan is busy,\x01",
            "I was entrusted with this matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "However...you see, I lost the\x01",
            "confidence that I'll be able to\x01",
            "cath that fake brand trader alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FU-Uuhm.\x01",
            "Putting aside having confidence or not...\x01",
            "It's a fact that you're shorthanded.\x02\x03",
            "#00001FIn this big train station,\x01",
            "if you don't surround her properly\x01",
            "it's very possible she'll escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Right?\x01",
            "That's why I asked\x01",
            "for your support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "What I want to ask you is to\x01",
            "act in a support role to arrest\x01",
            "the fake brand trader with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Also, to be on the lookout\x01",
            "so that the fake brand trader\x01",
            "doesn't leave the train station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "You caught that fake brand\x01",
            "trader once...that's what I\x01",
            "thought. Will you help me out?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x0)
    Call(0, 44)
    EventEnd(0x5)
    Return()

    # Function_42_6B7D end

    def Function_43_78CF(): pass

    label("Function_43_78CF")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)
    OP_68(12070, 1530, -290, 0)
    MoveCamera(43, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, 12590, 30, 60, 90)
    SetChrPos(0x102, 12400, 30, 1030, 90)
    SetChrPos(0x103, 12300, 30, -870, 90)
    SetChrPos(0x104, 11250, 30, 60, 90)
    SetChrPos(0x109, 10940, 30, 1050, 90)
    SetChrPos(0x105, 10920, 30, -950, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x1A, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0x1A,
        (
            "What I want to ask you is to\x01",
            "act in a support role to arrest\x01",
            "the fake brand trader with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Also, to be on the lookout\x01",
            "so that the fake brand trader\x01",
            "doesn't leave the train station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "You caught that fake brand\x01",
            "trader once...that's what I\x01",
            "thought. Will you help me out?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 44)
    EventEnd(0x5)
    Return()

    # Function_43_78CF end

    def Function_44_7AB3(): pass

    label("Function_44_7AB3")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B00")
    Jump("loc_7C2B")

    label("loc_7B00")


    ChrTalk(
        0x101,
        (
            "#00006F...Sorry, we have\x01",
            "another job already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Uhhm, I see.\x01",
            "It can't be helped then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Then, I'll wait here\x01",
            "a little more for a\x01",
            "good chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "If you have time and could\x01",
            "come to give me a hand,\x01",
            "it'd help me greatly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x173, 4)
    SetChrPos(0x0, 11560, 30, -10, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_93(0x1A, 0x5A, 0x0)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    OP_4C(0x1C, 0xFF)
    OP_69(0xFF, 0x0)
    Return()

    label("loc_7C2B")


    ChrTalk(
        0x101,
        (
            "#00000F...I see, understood.\x01",
            "We'll definitely cooperate with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Ooh, thank you!\x01",
            "I'm in your debt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Then... First of all, let's decide\x01",
            "the group which will arrest the\x01",
            "fake brand trader with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Who could do me the favor\x01",
            "to come with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FLet's see...\x01",
            "How should we divide?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FBeing a detective, I think you\x01",
            "should accompany him, Mr. Lloyd.\x02\x03",
            "#00211F...I am slightly worried having\x01",
            "only Mr. Raymond...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "N-No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "...That's what I'd like to say, but\x01",
            "that way I'd be more reassured.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012FU-Uhm...\x01",
            "So, for now we're two detectives...\x02\x03",
            "#00000FIt seems it would be better having another\x01",
            "one come as support and leave the remaining\x01",
            "four to strengthen the train station lookout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThen...  \x01",
            "Who is going to come along?\x02",
        )
    )

    CloseMessageWindow()
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
            "Bring Elie With You.\x01",       # 0
            "Bring Tio With You.\x01",        # 1
            "Bring Randy With You.\x01",      # 2
            "Bring Noｱl With You.\x01",      # 3
            "Bring Wazy With You.\x01",       # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8061")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#00000FElie, come with us.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00100FYes, understood.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x1)
    Jump("loc_81F9")

    label("loc_8061")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80C9")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#00000FTio, come with us.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#00200FRoger that.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x2)
    Jump("loc_81F9")

    label("loc_80C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8133")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00000FRandy, come with us.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#00309FSure thing.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x3)
    Jump("loc_81F9")

    label("loc_8133")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8198")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        "#00000FNoｱl, come with us.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#10100FYessir!\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x4)
    Jump("loc_81F9")

    label("loc_8198")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#00000FWazy, come with us.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        "#10304FAs you command, leader.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x5)

    label("loc_81F9")

    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00003FEveryone else, survey the\x01",
            "station entrances and exits.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8248():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8248)
    Sleep(50)

    def lambda_8258():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8258)
    Sleep(50)

    def lambda_8268():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8268)
    Sleep(50)

    def lambda_8278():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8278)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00001FSince it concerns that old lady,\x01",
            "everything could happen.\x01",
            "Pay the utmost attention.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x102, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x1A, 1, 0, 45)
    Sleep(1500)
    OP_68(15530, 1530, 8500, 3000)
    MoveCamera(43, 27, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(18860, 3000)
    BeginChrThread(0x1B, 1, 0, 46)
    BeginChrThread(0x1C, 1, 0, 47)
    OP_6F(0x79)
    Sleep(1000)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)

    def lambda_836E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_836E)

    def lambda_837B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_837B)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)

    ChrTalk(
        0x1B,
        (
            "...I can't seem\x01",
            "to spot them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "They could have boarded\x01",
            "the train already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "...Let's hurry.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 1, 0, 48)
    BeginChrThread(0x1C, 1, 0, 49)
    Sleep(1000)
    OP_68(20050, 1530, 7050, 2000)
    MoveCamera(45, 20, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(20000, 2000)
    OP_6F(0x79)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1A, 0x1)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x1A)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Fake Brand Trader Pursuit]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x173, 5)
    SetChrPos(0x0, 11650, 30, -510, 90)
    OP_93(0x1A, 0x5A, 0x0)
    OP_4C(0x1A, 0xFF)
    OP_69(0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_851C")
    AddParty(0x1, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 3)
    Jump("loc_8574")

    label("loc_851C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8537")
    AddParty(0x2, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 4)
    Jump("loc_8574")

    label("loc_8537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8552")
    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 5)
    Jump("loc_8574")

    label("loc_8552")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_856D")
    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 6)
    Jump("loc_8574")

    label("loc_856D")

    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 7)

    label("loc_8574")

    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_44_7AB3 end

    def Function_45_8592(): pass

    label("Function_45_8592")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86AA")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_85D5"),
        (1, "loc_85EF"),
        (2, "loc_8609"),
        (3, "loc_8623"),
        (4, "loc_863D"),
        (5, "loc_8657"),
        (6, "loc_8671"),
        (SWITCH_DEFAULT, "loc_868B"),
    )


    label("loc_85D5")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_86A5")

    label("loc_85EF")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_86A5")

    label("loc_8609")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_86A5")

    label("loc_8623")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_86A5")

    label("loc_863D")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_86A5")

    label("loc_8657")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_86A5")

    label("loc_8671")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_86A5")

    label("loc_868B")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_86A5")

    label("loc_86A5")

    Jump("Function_45_8592")

    label("loc_86AA")

    Return()

    # Function_45_8592 end

    def Function_46_86AB(): pass

    label("Function_46_86AB")

    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Return()

    # Function_46_86AB end

    def Function_47_86CA(): pass

    label("Function_47_86CA")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    Return()

    # Function_47_86CA end

    def Function_48_86E9(): pass

    label("Function_48_86E9")

    Sleep(600)
    OP_95(0xFE, 19770, 30, 7340, 2000, 0x0)
    OP_95(0xFE, 23810, 0, 7440, 2000, 0x0)
    Return()

    # Function_48_86E9 end

    def Function_49_8715(): pass

    label("Function_49_8715")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 19710, 30, 8420, 2000, 0x0)
    Sound(100, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(500)
    OP_95(0xFE, 23490, 0, 8520, 2000, 0x0)
    Return()

    # Function_49_8715 end

    def Function_50_875E(): pass

    label("Function_50_875E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(13600, 1330, -370, 0)
    MoveCamera(38, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17100, 0)
    LoadChrToIndex("chr/ch30200.itc", 0x1F)
    SetChrChipByIndex(0x1A, 0x1F)
    EndChrThread(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x101, 14910, 30, 670, 270)
    SetChrPos(0x102, 15040, 30, -640, 270)
    SetChrPos(0x103, 14090, 30, 1470, 225)
    SetChrPos(0x104, 14050, 30, -1590, 315)
    SetChrPos(0x109, 12820, 30, 1230, 145)
    SetChrPos(0x105, 12790, 30, -1260, 45)
    SetChrPos(0x1A, 12140, 30, 30, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 3)), scpexpr(EXPR_END)), "loc_899C")

    ChrTalk(
        0x104,
        (
            "#00306FWhen I heard you guys\x01",
            "went to the Republic,\x01",
            "I was surprised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FIt turned out like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FSorry for not even\x01",
            "contacting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, at any rate the fake\x01",
            "brand trader was caught\x01",
            "and everything was fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FAhaha, let's say it turned out fine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FC2")

    label("loc_899C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 4)), scpexpr(EXPR_END)), "loc_8B24")

    ChrTalk(
        0x102,
        (
            "#00106FWhen I heard you\x01",
            "went to the Republic,\x01",
            "I was surprised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FGoddess gracious, to think\x01",
            "things turned out like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWe should've at least contacted\x01",
            "you. We are very sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, at any rate the fake\x01",
            "brand trader was caught\x01",
            "and everything was fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FAhaha, let's say it turned out fine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FC2")

    label("loc_8B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 5)), scpexpr(EXPR_END)), "loc_8CB7")

    ChrTalk(
        0x109,
        (
            "#10106FMr. Lloyd, when I heard\x01",
            "you went to the Republic,\x01",
            "I was surprised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh boy, who could've thought\x01",
            "things turned out like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, sorry, sorry.\x01",
            "It was an emergency situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, at any rate the fake\x01",
            "brand trader was caught\x01",
            "and everything was fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FWell, let's say it turned out fine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FC2")

    label("loc_8CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 6)), scpexpr(EXPR_END)), "loc_8E43")

    ChrTalk(
        0x105,
        (
            "#10306FLloyd, when I heard you\x01",
            "went to the Republic,\x01",
            "even I was surprised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FGoddess gracious, to think\x01",
            "things turned out like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha...\x01",
            "Sorry, we didn't even contacted you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, at any rate the fake\x01",
            "brand trader was caught\x01",
            "and everything was fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FWell, let's say it turned out fine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FC2")

    label("loc_8E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 7)), scpexpr(EXPR_END)), "loc_8FC2")

    ChrTalk(
        0x109,
        (
            "#10106FMr. Lloyd, when I heard\x01",
            "you went to the Republic,\x01",
            "I was surprised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FGoddess gracious, to think\x01",
            "things turned out like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FHu hu, it was an emergency, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, at any rate the fake\x01",
            "brand trader was caught\x01",
            "and everything was fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FWell, let's say it turned out fine.\x02",
    )

    CloseMessageWindow()

    label("loc_8FC2")


    ChrTalk(
        0x1A,
        (
            "Well then, I have to make a report\x01",
            "at Crime Investigations Section Two...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "So, I will be excusing myself here.\x02",
    )

    CloseMessageWindow()

    def lambda_903F():

        label("loc_903F")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_903F")

    QueueWorkItem2(0x103, 1, lambda_903F)

    def lambda_9051():

        label("loc_9051")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_9051")

    QueueWorkItem2(0x104, 1, lambda_9051)

    def lambda_9063():

        label("loc_9063")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_9063")

    QueueWorkItem2(0x109, 1, lambda_9063)

    def lambda_9075():

        label("loc_9075")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_9075")

    QueueWorkItem2(0x105, 1, lambda_9075)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 3)), scpexpr(EXPR_END)), "loc_90C7")

    ChrTalk(
        0x102,
        "#00109F*giggle*, thank you for your hard work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_91B7")

    label("loc_90C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 4)), scpexpr(EXPR_END)), "loc_9109")

    ChrTalk(
        0x103,
        "#00202FThank you very much for your hard work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_91B7")

    label("loc_9109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 5)), scpexpr(EXPR_END)), "loc_9141")

    ChrTalk(
        0x104,
        "#00309FHa ha, thanks for everythin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_91B7")

    label("loc_9141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 6)), scpexpr(EXPR_END)), "loc_9180")

    ChrTalk(
        0x109,
        "#10109FHu hu, thank you for your hard work!\x02",
    )

    CloseMessageWindow()
    Jump("loc_91B7")

    label("loc_9180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 7)), scpexpr(EXPR_END)), "loc_91B7")

    ChrTalk(
        0x105,
        "#10302FHu hu, thank you for all you did.\x02",
    )

    CloseMessageWindow()

    label("loc_91B7")


    ChrTalk(
        0x1A,
        (
            "No, I was helped by you\x01",
            "all until the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I think that if I had been alone,\x01",
            "I would've never been able to\x01",
            "arrest that old lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Thank you very much for today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FNo, likewise.\x02\x03",
            "#00000FIf something happens again, please\x01",
            "contact the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Yeah, I'll be counting on you!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x10E, 0x1F4)

    def lambda_92F8():
        OP_95(0xFE, 3980, 30, 220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_92F8)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrFlags(0x1A, 0x80)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Fake Brand Trader Pursuit]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x81, 0x1, 0x8)
    OP_29(0x81, 0x1, 0x9)
    OP_29(0x81, 0x4, 0x10)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 13970, 30, -400, 270)
    EventEnd(0x5)
    Return()

    # Function_50_875E end

    def Function_51_93BF(): pass

    label("Function_51_93BF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "←Republic Region Bound - Platform Number 1\x01",
            "　　　Republic Altair City   35 minutes\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_51_93BF end

    def Function_52_944B(): pass

    label("Function_52_944B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Empire Region Bound - Platform Number 2→\x01",
            "　　　　Empire Garrelia Fortress   32 minutes\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_52_944B end

    def Function_53_94DB(): pass

    label("Function_53_94DB")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a time table of the autonomous\x01",
            "state of Crossbell environs.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_53_94DB end

    def Function_54_9533(): pass

    label("Function_54_9533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_954A")
    Call(0, 56)
    Return()

    label("loc_954A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※※　Inspector Office　※※\x01",
            "Authorized Personnel Only\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_54_9533 end

    def Function_55_95BA(): pass

    label("Function_55_95BA")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a route map of the autonomous\x01",
            "state of Crossbell environs.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_55_95BA end

    def Function_56_9611(): pass

    label("Function_56_9611")

    EventBegin(0x0)
    Fade(500)
    OP_68(27750, 5100, 10310, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18910, 0)
    SetChrPos(0x101, 28770, 4000, 9430, 0)
    SetChrPos(0x102, 26280, 4000, 8830, 45)
    SetChrPos(0x103, 27490, 4000, 8660, 0)
    SetChrPos(0x104, 28740, 4000, 8290, 315)
    SetChrPos(0xF4, 25940, 4000, 7480, 0)
    SetChrPos(0xF5, 27640, 4000, 7700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#12P#00200F...It really seems there's\x01",
            "no one inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FThe railways service has been stopped\x01",
            "and the Empire and Republic inspectors\x01",
            "were called back altogether.\x02\x03",
            "#00100FEven the station attendants\x01",
            "are probably sheltering in\x01",
            "various places now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FWell, no reason to stay\x01",
            "round such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FLet's go meet Miss\x01",
            "Kilika and the others.\x02\x03",
            "We should be able to reach the platform\x01",
            "from the lower entrance by going down.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 27770, 4000, 9430, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1CD, 7)
    EventEnd(0x5)
    Return()

    # Function_56_9611 end

    SaveToFile()

Try(main)
