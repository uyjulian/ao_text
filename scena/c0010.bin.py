from ScenarioHelper import *

def main():
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
        "Station staff lux",             # 1
        "Station worker Lisa",               # 2
        "Station staff Aim",             # 3
        "Station worker Shenry",         # 4
        "Station staff Margus",           # 5
        "Opinion officer Quattro",         # 6
        "Fay",                 # 7
        "Billy",                 # 8
        "Businessman",           # 9
        "tourist",                 # 10
        "tourist",                 # 11
        "Old man",                   # 12
        "old woman",                   # 13
        "tourist",                 # 14
        "tourist",                 # 15
        "boy",                 # 16
        "Muller",               # 17
        "Inspector Mahlow",         # 18
        "Raymond investigator",       # 19
        "Oriental style man",             # 20
        "Oriental style man",             # 21
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
        "Function_4_C63",          # 04, 4
        "Function_5_C67",          # 05, 5
        "Function_6_115B",         # 06, 6
        "Function_7_12C6",         # 07, 7
        "Function_8_12CA",         # 08, 8
        "Function_9_17B1",         # 09, 9
        "Function_10_1922",        # 0A, 10
        "Function_11_1CB7",        # 0B, 11
        "Function_12_1CBB",        # 0C, 12
        "Function_13_2085",        # 0D, 13
        "Function_14_2089",        # 0E, 14
        "Function_15_277D",        # 0F, 15
        "Function_16_2915",        # 10, 16
        "Function_17_291F",        # 11, 17
        "Function_18_2AEB",        # 12, 18
        "Function_19_2D03",        # 13, 19
        "Function_20_2E43",        # 14, 20
        "Function_21_2F94",        # 15, 21
        "Function_22_327E",        # 16, 22
        "Function_23_33E8",        # 17, 23
        "Function_24_3583",        # 18, 24
        "Function_25_371D",        # 19, 25
        "Function_26_3832",        # 1A, 26
        "Function_27_38C6",        # 1B, 27
        "Function_28_3B5A",        # 1C, 28
        "Function_29_3B91",        # 1D, 29
        "Function_30_3BDE",        # 1E, 30
        "Function_31_3BE8",        # 1F, 31
        "Function_32_3BF2",        # 20, 32
        "Function_33_3C73",        # 21, 33
        "Function_34_45C3",        # 22, 34
        "Function_35_4F87",        # 23, 35
        "Function_36_51DA",        # 24, 36
        "Function_37_53A9",        # 25, 37
        "Function_38_549B",        # 26, 38
        "Function_39_562E",        # 27, 39
        "Function_40_5A7F",        # 28, 40
        "Function_41_5DD3",        # 29, 41
        "Function_42_5E09",        # 2A, 42
        "Function_43_6A00",        # 2B, 43
        "Function_44_6BA5",        # 2C, 44
        "Function_45_7637",        # 2D, 45
        "Function_46_7750",        # 2E, 46
        "Function_47_776F",        # 2F, 47
        "Function_48_778E",        # 30, 48
        "Function_49_77BA",        # 31, 49
        "Function_50_7803",        # 32, 50
        "Function_51_830A",        # 33, 51
        "Function_52_8382",        # 34, 52
        "Function_53_83FA",        # 35, 53
        "Function_54_8433",        # 36, 54
        "Function_55_84C6",        # 37, 55
        "Function_56_84FF",        # 38, 56
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
            "There is a car magazine 'separate volume car star'.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('闪耀色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5F")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Paint pattern\x01\x07\x02",
            "\"Shine color\"\x07\x00",
            "I learned.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('闪耀色彩', 1)

    label("loc_C5F")

    TalkEnd(0xFF)
    Return()

    # Function_3_BBC end

    def Function_4_C63(): pass

    label("Function_4_C63")

    Call(0, 5)
    Return()

    # Function_4_C63 end

    def Function_5_C67(): pass

    label("Function_5_C67")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C7B")
    Call(0, 6)
    Jump("loc_1157")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E8C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D66")

    ChrTalk(
        0x8,
        (
            "Today we also crossbell station\x01",
            "Please use it,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I will be going to the Republic soon,\x01",
            "It is followed by Empire Way\x01",
            "It is scheduled to start sequentially.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are in a hurry, as soon as possible\x01",
            "Please purchase a ticket.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DE3")

    label("loc_D66")


    ChrTalk(
        0x8,
        (
            "I will be going to the Republic soon,\x01",
            "It is followed by Empire Way\x01",
            "It is scheduled to start sequentially.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are in a hurry, as soon as possible\x01",
            "Please purchase a ticket.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE3")

    Jump("loc_E87")

    label("loc_DE8")


    ChrTalk(
        0x8,
        (
            "Escape to the roof of the train\x01",
            "When I heard that I jumped over,\x01",
            "Indeed I suspected my ears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, nobody will imitate it\x01",
            "It seems necessary to keep in mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E87")

    Jump("loc_1157")

    label("loc_E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6C")

    ChrTalk(
        0x8,
        (
            "Today we also crossbell station\x01",
            "Please use it,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "During the trade conference,\x01",
            "The security of the home by the imperial army\x01",
            "It is being strengthened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since inspection and so on will become strict\x01",
            "Please acknowledge it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FEB")

    label("loc_F6C")


    ChrTalk(
        0x8,
        (
            "During the trade conference,\x01",
            "The security of the home by the imperial army\x01",
            "It is being strengthened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since inspection and so on will become strict\x01",
            "Please acknowledge it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEB")

    Jump("loc_1157")

    label("loc_FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1157")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D4")

    ChrTalk(
        0x8,
        (
            "Today we also crossbell station\x01",
            "Please use it,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "During the trade conference,\x01",
            "The railway is in service as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tickets are on the second floor space\x01",
            "As you can purchase,\x01",
            "Please come over there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1157")

    label("loc_10D4")


    ChrTalk(
        0x8,
        (
            "During the trade conference,\x01",
            "The railway is in service as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tickets are on the second floor space\x01",
            "As you can purchase,\x01",
            "Please come over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1157")

    TalkEnd(0x8)
    Return()

    # Function_5_C67 end

    def Function_6_115B(): pass

    label("Function_6_115B")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_122A")

    ChrTalk(
        0x8,
        (
            "Currently, train service\x01",
            "Both to Imperial and Republic\x01",
            "I will wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is hard for customers\x01",
            "We are sorry for the inconvenience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'm in trouble!\x01",
            "An important negotiation in the empire\x01",
            "Even though … …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12BD")

    label("loc_122A")


    ChrTalk(
        0x8,
        (
            "I'm sorry but,\x01",
            "Recovery time is also undecided now\x01",
            "We now have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How about customers?\x01",
            "I want to get an understanding …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Well, business talks, negotiations …!\x02",
    )

    CloseMessageWindow()

    label("loc_12BD")

    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_6_115B end

    def Function_7_12C6(): pass

    label("Function_7_12C6")

    Call(0, 8)
    Return()

    # Function_7_12C6 end

    def Function_8_12CA(): pass

    label("Function_8_12CA")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AD")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1335")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1335")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1354")
    OP_AF(0x8B)
    Jump("loc_13D6")

    label("loc_1354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1364")
    OP_AF(0x8A)
    Jump("loc_13D6")

    label("loc_1364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1374")
    OP_AF(0x89)
    Jump("loc_13D6")

    label("loc_1374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1384")
    OP_AF(0x88)
    Jump("loc_13D6")

    label("loc_1384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1394")
    OP_AF(0x87)
    Jump("loc_13D6")

    label("loc_1394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_13A4")
    OP_AF(0x86)
    Jump("loc_13D6")

    label("loc_13A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_13B4")
    OP_AF(0x85)
    Jump("loc_13D6")

    label("loc_13B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13C4")
    OP_AF(0x84)
    Jump("loc_13D6")

    label("loc_13C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_13D4")
    OP_AF(0x83)
    Jump("loc_13D6")

    label("loc_13D4")

    OP_AF(0x82)

    label("loc_13D6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17A8")

    label("loc_13E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F9")
    Jump("loc_17A8")

    label("loc_13F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1423")
    Call(0, 9)
    Jump("loc_17A8")

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1531")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1497")

    ChrTalk(
        0x9,
        "How about a station railway accompanied by a trip?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also the latest issue of Crossbell Times\x01",
            "We have arrived.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152C")

    label("loc_1497")


    ChrTalk(
        0x9,
        (
            "Arrests for escapists and terrorists … …\x01",
            "I do not think such a thing happens at once\x01",
            "It is a story I do not hear easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Several coincidences overlapped,\x01",
            "Is that what you mean?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152C")

    Jump("loc_17A8")

    label("loc_1531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1643")

    ChrTalk(
        0x9,
        (
            "Mr. Marlow, an inspector,\x01",
            "He is a second-time employee from the Republican Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Departed from the Imperial Army\x01",
            "With the inspector Quattoro,\x01",
            "I do not get along well with each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Elegantly the Empire and the Republic\x01",
            "Because I am quarreling with conflict,\x01",
            "It may be unavoidable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16F0")

    label("loc_1643")


    ChrTalk(
        0x9,
        (
            "Mr. Marlow and the quattro, inspectors,\x01",
            "I do not get along well with each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Elegantly the Empire and the Republic\x01",
            "Because I am quarreling with conflict,\x01",
            "It may be unavoidable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F0")

    Jump("loc_17A8")

    label("loc_16F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17A8")

    ChrTalk(
        0x9,
        (
            "This morning is a publishing house of the empire\x01",
            "Reporters of \"Empire Times\"\x01",
            "It seems that he came to the interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It is done in Crossbell\x01",
            "As an international conference,\x01",
            "It seems that attention is also quite high.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A8")

    Jump("loc_12D7")

    label("loc_17AD")

    TalkEnd(0x9)
    Return()

    # Function_8_12CA end

    def Function_9_17B1(): pass

    label("Function_9_17B1")

    OP_4B(0x9, 0xFF)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1898")

    NpcTalk(
        0x11,
        "Citizen",
        (
            "Eee, the ticket refund\x01",
            "It is not a story that I can do it!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Citizen",
        (
            "For today's trip,\x01",
            "Hurry up and prepare … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I really am sorry.\x01",
            "As of now, we confirm the facts … ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1919")

    label("loc_1898")


    NpcTalk(
        0x11,
        "Citizen",
        (
            "Totally, to play Son\x01",
            "Always a customer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I really am sorry.\x01",
            "As of now, we confirm the facts … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1919")

    OP_4C(0x9, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_9_17B1 end

    def Function_10_1922(): pass

    label("Function_10_1922")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1936")
    Call(0, 17)
    Jump("loc_1CB3")

    label("loc_1936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D8")

    ChrTalk(
        0xFE,
        (
            "That police brother,\x01",
            "I guess it was kind of sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you chasing someone?\x01",
            "Especially a suspicious guy came in\x01",
            "It did not look like it … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B11")

    label("loc_19D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A99")

    ChrTalk(
        0xFE,
        (
            "If it is only fake brand quotient,\x01",
            "What is it that even a terrorist stayed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I did not know the face,\x01",
            "Until then you can get messed up by ordinary people\x01",
            "Is it thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "In a way it's a terrible story …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1B11")

    label("loc_1A99")


    ChrTalk(
        0xFE,
        (
            "If it is only fake brand quotient,\x01",
            "Terrorists to the general public\x01",
            "Is it something you can miss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "In a way it's a terrible story …\x02",
    )

    CloseMessageWindow()

    label("loc_1B11")

    Jump("loc_1CB3")

    label("loc_1B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1BB7")

    ChrTalk(
        0xFE,
        (
            "Imperial government exclusive train\x01",
            "The 3rd home which is stopped,\x01",
            "Imperial troops are strictly guarding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not mind seeing it,\x01",
            "Do not get inadvertently approaching.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB3")

    label("loc_1BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CB3")

    ChrTalk(
        0xFE,
        (
            "Imperial government exclusive train this morning\x01",
            "\"Eisengraf\" is\x01",
            "You have arrived at Home 1.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because there is regular train service,\x01",
            "I am moved to the third home now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is not rare to see it,\x01",
            "If you have the opportunity to go home\x01",
            "You should do something by all means.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB3")

    TalkEnd(0xFE)
    Return()

    # Function_10_1922 end

    def Function_11_1CB7(): pass

    label("Function_11_1CB7")

    Call(0, 12)
    Return()

    # Function_11_1CB7 end

    def Function_12_1CBB(): pass

    label("Function_12_1CBB")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D5E")

    ChrTalk(
        0xA,
        (
            "I'm sorry but,\x01",
            "Currently in response to a train accident\x01",
            "It is very crowded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ticket purchase · reservation etc\x01",
            "We can not accept it,\x01",
            "Please acknowledge it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2081")

    label("loc_1D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F81")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E54")

    ChrTalk(
        0xA,
        (
            "Tickets for Imperial\x01",
            "An old lady who I bought,\x01",
            "He was kind enough to be kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Whatever long-standing business\x01",
            "It seems that it is the one who continues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I did not ask you in detail,\x01",
            "I hope you do your best on your part.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1EE3")

    label("loc_1E54")


    ChrTalk(
        0xA,
        (
            "Tickets for Imperial\x01",
            "An old lady who I bought,\x01",
            "He was kind enough to be kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To the empire to go to business or something.\x01",
            "I hope you do your best on your part.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE3")

    Jump("loc_1F7C")

    label("loc_1EE8")


    ChrTalk(
        0xA,
        (
            "I was caught in Altair City\x01",
            "Fake brand trader,\x01",
            "I heard he was an old lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Perhaps, at that time\x01",
            "I was buying a ticket\x01",
            "I wonder if she was an old lady … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7C")

    Jump("loc_2081")

    label("loc_1F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2021")

    ChrTalk(
        0xA,
        (
            "From a security standpoint now\x01",
            "Baggage inspection at the entrance\x01",
            "We have thoroughness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sorry for troubling you,\x01",
            "Please understand and\x01",
            "We appreciate your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2081")

    label("loc_2021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2081")

    ChrTalk(
        0xA,
        (
            "This is a ticket counter\x01",
            "We now have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please refer when purchasing.\x02",
    )

    CloseMessageWindow()

    label("loc_2081")

    TalkEnd(0xA)
    Return()

    # Function_12_1CBB end

    def Function_13_2085(): pass

    label("Function_13_2085")

    Call(0, 14)
    Return()

    # Function_13_2085 end

    def Function_14_2089(): pass

    label("Function_14_2089")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2218")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A4")

    ChrTalk(
        0xB,
        (
            "Oh … I'm sorry,\x01",
            "Would you mind waiting a moment?\x02",
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
            "Currently occurred in the West Crossbell Highway\x01",
            "Due to the derailment accident, train service\x01",
            "I will wait.\x02\x03",
            "In addition, the restoration today\x01",
            "It is in a state where the outlook is not established now.\x01",
            "Please acknowledge it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2213")

    label("loc_21A4")


    ChrTalk(
        0xB,
        (
            "Refundable\x01",
            "An announcement on the premises ……\x01",
            "It is seriously tricky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As soon as the train is restored\x01",
            "I hope to give it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2213")

    Jump("loc_2779")

    label("loc_2218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_242A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230B")

    ChrTalk(
        0xB,
        (
            "Oh … I'm sorry,\x01",
            "Would you mind waiting a moment?\x02",
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
            "A train bound for the Republic and the Imperial\x01",
            "I am planning to depart soon.\x02\x03",
            "Do not get rushing like rushing\x01",
            "Please be careful enough.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_238D")

    label("loc_230B")


    ChrTalk(
        0xB,
        (
            "Rushed ride\x01",
            "Become a source of injury or death,\x01",
            "It is very dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you do not make it in time,\x01",
            "Calm down to the next train\x01",
            "Please wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238D")

    Jump("loc_2425")

    label("loc_2392")


    ChrTalk(
        0xB,
        (
            "If you are rushing in,\x01",
            "I do not think there are people riding the roof of the train\x01",
            "I was surprised……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… It is better to be careful with the announcement\x01",
            "Is not it a nice thing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2425")

    Jump("loc_2779")

    label("loc_242A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_25C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_253E")

    ChrTalk(
        0xB,
        (
            "Oh … I'm sorry,\x01",
            "Would you mind waiting a moment?\x02",
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
            "At Crossbell station,\x01",
            "Based on the Taiki Railway Public Corporation Agreement\x01",
            "We are conducting an inspection.\x02\x03",
            "Those who head towards the Imperial Republic\x01",
            "Fill in your immigration application form,\x01",
            "Please submit to the inspector.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_25C3")

    label("loc_253E")


    ChrTalk(
        0xB,
        (
            "From Crossbell Station\x01",
            "To go to the Empire / Republic,\x01",
            "It is necessary to undergo an inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It is a bit troublesome,\x01",
            "Please accept your understanding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C3")

    Jump("loc_2779")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2779")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E8")

    ChrTalk(
        0xB,
        (
            "Oh … I'm sorry,\x01",
            "Would you mind waiting a moment?\x02",
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
            "Imperial government special train today\x01",
            "With the arrival of \"Eisengraf\"\x01",
            "We are strengthening the security system.\x02\x03",
            "With that in mind,\x01",
            "Do not enter the third home,\x01",
            "We ask for your understanding.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2779")

    label("loc_26E8")


    ChrTalk(
        0xB,
        (
            "Excuse me, I was on the campus\x01",
            "I'm in charge of the announcement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you use railroad\x01",
            "Are there any unclear points?\x01",
            "Please do not hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2779")

    TalkEnd(0xB)
    Return()

    # Function_14_2089 end

    def Function_15_277D(): pass

    label("Function_15_277D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2841")

    ChrTalk(
        0xFE,
        (
            "His Excellency and Prince Oliver,\x01",
            "You see the two figures\x01",
            "Since when was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As an Ichigo soldier\x01",
            "We were able to welcome government officials,\x01",
            "It is a pleasure to be totally altogether.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2888")

    label("loc_2841")


    ChrTalk(
        0xFE,
        (
            "……? I am standing on that first floor\x01",
            "The big guy in black clothes, as if I saw somewhere ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2888")

    Jump("loc_2911")

    label("loc_288D")


    ChrTalk(
        0xFE,
        (
            "In the meantime, that big black guy's giant\x01",
            "You seem to have gone somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I never thought that … …\x01",
            "Hmm, it is probably due to mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2911")

    TalkEnd(0xFE)
    Return()

    # Function_15_277D end

    def Function_16_2915(): pass

    label("Function_16_2915")

    TalkBegin(0xFE)
    Call(0, 17)
    TalkEnd(0xFE)
    Return()

    # Function_16_2915 end

    def Function_17_291F(): pass

    label("Function_17_291F")

    OP_4B(0xE, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5E")

    ChrTalk(
        0xE,
        (
            "So, the damage situation of the train is\x01",
            "How are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As long as we received contact,\x01",
            "It seems to be quite severe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you do not do it well, the train itself\x01",
            "It may be useless …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm … Then,\x01",
            "For the time being, another train\x01",
            "I have no choice but to arrange it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, now,\x01",
            "Resume train service\x01",
            "I have to think first.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2AE2")

    label("loc_2A5E")


    ChrTalk(
        0xE,
        (
            "The possibility that the track itself was damaged\x01",
            "There will be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As soon as the train removal work is over,\x01",
            "Let's face the scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, that's OK.\x02",
    )

    CloseMessageWindow()

    label("loc_2AE2")

    OP_4C(0xE, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_17_291F end

    def Function_18_2AEB(): pass

    label("Function_18_2AEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2AFF")
    Call(0, 9)
    Jump("loc_2CFF")

    label("loc_2AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B79")

    ChrTalk(
        0xFE,
        (
            "Hmm, the train soon\x01",
            "It looks like I'm out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is no choice, even going to buy\x01",
            "Would you wait for the next train?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFF")

    label("loc_2B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B87")
    Jump("loc_2CFF")

    label("loc_2B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C68")

    ChrTalk(
        0xFE,
        (
            "I am a port city at the westernmost extremity of the Republic,\x01",
            "I came from Altair City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However,\x01",
            "After all it seems to be developing huge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The republic is pretty prosperous,\x01",
            "Compared to crossbell\x01",
            "I can think of the countryside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2CFF")

    label("loc_2C68")


    ChrTalk(
        0xFE,
        (
            "I am a port city at the westernmost extremity of the Republic,\x01",
            "I came from Altair City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However,\x01",
            "After all it seems to be developing huge.\x01",
            "The Republic seems to be a country.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFF")

    TalkEnd(0xFE)
    Return()

    # Function_18_2AEB end

    def Function_19_2D03(): pass

    label("Function_19_2D03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D17")
    Call(0, 6)
    Jump("loc_2E3F")

    label("loc_2D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2DAA")

    ChrTalk(
        0xFE,
        (
            "The station staff was speaking … …\x01",
            "The remnants of terrorists in the Republic\x01",
            "She seems to have been caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that he was hiding for a while,\x01",
            "I can not be relieved for the time being.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E3F")

    label("loc_2DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E36")

    ChrTalk(
        0xFE,
        "It is a business trip to the empire from now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am worried about the state of the plenary session … …\x01",
            "In the \"Empire Times\" over there\x01",
            "It will be featured and there is no problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E3F")

    label("loc_2E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E3F")

    label("loc_2E3F")

    TalkEnd(0xFE)
    Return()

    # Function_19_2D03 end

    def Function_20_2E43(): pass

    label("Function_20_2E43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2E9D")

    ChrTalk(
        0xFE,
        "However, it is a derailment accident … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband, my husband\x01",
            "What happened? Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2EF3")

    ChrTalk(
        0xFE,
        "I finally arrived at the crossbell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will go sightseeing as soon as I take a break.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F87")

    ChrTalk(
        0xFE,
        (
            "After this,\x01",
            "Altair souvenir burnt chestnut\x01",
            "I ate everything in the train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Already dinner\x01",
            "Even if I can not eat it\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F90")

    label("loc_2F90")

    TalkEnd(0xFE)
    Return()

    # Function_20_2E43 end

    def Function_21_2F94(): pass

    label("Function_21_2F94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_303E")

    ChrTalk(
        0xFE,
        (
            "Have you happened to falling rocks too?\x01",
            "Or is it an artificial thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it is an artificial … …\x01",
            "Reparation that makes eyeballs protrude\x01",
            "I will charge the perpetrator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327A")

    label("loc_303E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30DD")

    ChrTalk(
        0xFE,
        (
            "Anything, at the border gate\x01",
            "It seems that the state of tension is continuing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will make independent advocacy\x01",
            "That's it.\x01",
            "I have to count my minutes and I am young.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327A")

    label("loc_30DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_30EB")
    Jump("loc_327A")

    label("loc_30EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_327A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3222")

    ChrTalk(
        0xFE,
        (
            "The Osborne Prime Minister of the Empire,\x01",
            "Be a former chairman of the autonomous state legislature\x01",
            "She seems to be connected with Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But when Hartmann in exile\x01",
            "Behind the Empire 's exile release,\x01",
            "It is whispered that there was a foundation of the Prime Minister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it seems to be your own disadvantage,\x01",
            "Truncate without mercy.\x01",
            "\"Chancellor of iron\" is such a man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_327A")

    label("loc_3222")


    ChrTalk(
        0xFE,
        (
            "If it seems to be your own disadvantage,\x01",
            "Truncate without mercy.\x01",
            "\"Chancellor of iron\" is such a man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_327A")

    TalkEnd(0xFE)
    Return()

    # Function_21_2F94 end

    def Function_22_327E(): pass

    label("Function_22_327E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_32F6")

    ChrTalk(
        0xFE,
        (
            "To stop the railroad,\x01",
            "I wonder what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if I can return to the country properly …\x02",
    )

    CloseMessageWindow()
    Jump("loc_33E4")

    label("loc_32F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_338B")

    ChrTalk(
        0xFE,
        (
            "How is that blonde child?\x01",
            "It is unusual behavior behaving suspiciously from a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… What is the police?\x01",
            "I hesitate to depend on you\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E4")

    label("loc_338B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3399")
    Jump("loc_33E4")

    label("loc_3399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33E4")

    ChrTalk(
        0xFE,
        "I wonder if the train has come yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am tired of waiting.\x02",
    )

    CloseMessageWindow()

    label("loc_33E4")

    TalkEnd(0xFE)
    Return()

    # Function_22_327E end

    def Function_23_33E8(): pass

    label("Function_23_33E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_348A")

    ChrTalk(
        0xFE,
        (
            "No matter how long the train is\x01",
            "If you think you will not leave … …\x01",
            "A derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if we will stay at Cross Bell today.\x01",
            "I hope the hotel room can be taken, but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357F")

    label("loc_348A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34FE")

    ChrTalk(
        0xFE,
        (
            "From now it is with Kalesh\x01",
            "I'm traveling to the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the hot springs in the eastern people street … ….\x01",
            "I have to enjoy a lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357F")

    label("loc_34FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3576")

    ChrTalk(
        0xFE,
        (
            "Crossbell also has sightseeing spots\x01",
            "There seems to be quite a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems buses also pass,\x01",
            "Let's go a couple of times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357F")

    label("loc_3576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_357F")

    label("loc_357F")

    TalkEnd(0xFE)
    Return()

    # Function_23_33E8 end

    def Function_24_3583(): pass

    label("Function_24_3583")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3600")

    ChrTalk(
        0xFE,
        (
            "Ticket's ahead\x01",
            "I got a refund.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I plan to travel a lot,\x01",
            "It can not be helped this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3719")

    label("loc_3600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3680")

    ChrTalk(
        0xFE,
        (
            "From now on Canojo\x01",
            "I took him to the trip … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I can spin so much.\x01",
            "What should I do if Mira is missing …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3719")

    label("loc_3680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_368E")
    Jump("loc_3719")

    label("loc_368E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3719")

    ChrTalk(
        0xFE,
        (
            "Now, at Crossbell\x01",
            "The trade meeting\x01",
            "I guess you are doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was rumored\x01",
            "What is Orkis Tower,\x01",
            "Let's go see it ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3719")

    TalkEnd(0xFE)
    Return()

    # Function_24_3583 end

    def Function_25_371D(): pass

    label("Function_25_371D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_374E")

    ChrTalk(
        0xFE,
        "Hey, what happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_374E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3793")

    ChrTalk(
        0xFE,
        (
            "Little … … little … ….\x01",
            "The watch … … turn around … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_3793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3825")

    ChrTalk(
        0xFE,
        (
            "burp……\x01",
            "Altair City, it was a lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is a big river called Curie River,\x01",
            "A lot of boats are passing ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_3825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_382E")

    label("loc_382E")

    TalkEnd(0xFE)
    Return()

    # Function_25_371D end

    def Function_26_3832(): pass

    label("Function_26_3832")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hey hey, are you serious ……\x01",
            "What about cargo from the Republic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Consult with a father for a while\x01",
            "Also contact the shipping address ……\x01",
            "Wow, it looks like you will be busy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_3832 end

    def Function_27_38C6(): pass

    label("Function_27_38C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38EB")
    Call(0, 33)
    Return()

    label("loc_38EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4B")

    ChrTalk(
        0xFE,
        (
            "#12400FOlivier Renheim,\x01",
            "A lute called a white coat\x01",
            "He is a performer who left the house.\x02\x03",
            "Dazzling place,\x01",
            "There are lively places and meals etc.\x01",
            "It could be thought of as a destination.\x02\x03",
            "As you mentioned above,\x01",
            "Old city, back street, port area etc.\x01",
            "You can say that it is a good line.\x02\x03",
            "If you have difficulty bringing\x01",
            "It does not matter if it matches somewhat painful eyes.\x01",
            "I beg you to do my best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3B56")

    label("loc_3A4B")


    ChrTalk(
        0xFE,
        (
            "#12400FAs Olivier's destination,\x01",
            "Dazzling places, bustling places and\x01",
            "You can think of meals etc.\x02\x03",
            "As you mentioned above,\x01",
            "Old city, back street, port area etc.\x01",
            "You can say that it is a good line.\x02\x03",
            "If you have difficulty bringing\x01",
            "It does not matter if it matches somewhat painful eyes.\x01",
            "I beg you to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B56")

    TalkEnd(0xFE)
    Return()

    # Function_27_38C6 end

    def Function_28_3B5A(): pass

    label("Function_28_3B5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8C")
    Call(0, 36)
    Jump("loc_3B8F")

    label("loc_3B8C")

    Call(0, 37)

    label("loc_3B8F")

    Return()

    label("loc_3B90")

    Return()

    # Function_28_3B5A end

    def Function_29_3B91(): pass

    label("Function_29_3B91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC4")
    Call(0, 42)
    Jump("loc_3BC7")

    label("loc_3BC4")

    Call(0, 43)

    label("loc_3BC7")

    Return()

    label("loc_3BC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BDA")
    Jump("loc_3BDA")

    label("loc_3BDA")

    TalkEnd(0xFE)
    Return()

    # Function_29_3B91 end

    def Function_30_3BDE(): pass

    label("Function_30_3BDE")

    TalkBegin(0xFE)
    Call(0, 32)
    TalkEnd(0xFE)
    Return()

    # Function_30_3BDE end

    def Function_31_3BE8(): pass

    label("Function_31_3BE8")

    TalkBegin(0xFE)
    Call(0, 32)
    TalkEnd(0xFE)
    Return()

    # Function_31_3BE8 end

    def Function_32_3BF2(): pass

    label("Function_32_3BF2")

    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)

    ChrTalk(
        0x1B,
        (
            "…… Yatsura Yatsura\x01",
            "It seems like I'm going to escape by train ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "…… Hung, shallow … …\x01",
            "Even if you can escape from us …\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)
    OP_4C(0x1C, 0xFF)
    Return()

    # Function_32_3BF2 end

    def Function_33_3C73(): pass

    label("Function_33_3C73")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CBA")
    FadeToDark(500, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12400.itp")
    Jump("loc_3CBF")

    label("loc_3CBA")

    Fade(500)

    label("loc_3CBF")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D63")
    FadeToBright(500, 0)

    label("loc_3D63")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4408")

    NpcTalk(
        0x18,
        "Giant in black clothes",
        "#12400F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305F(Hey Lloyd … ….\x01",
            "Somehow it's atmosphere\x01",
            "I guess you have a guy … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(Maybe,\x01",
            "This time the client … …)\x02\x03",
            "#00000FExcuse me.\x01",
            "I am a person in the Special Affairs Division … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x18,
        "Giant in black clothes",
        (
            "#12404FI was waiting.\x01",
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
    SetChrName("Giant in black clothes")

    AnonymousTalk(
        0xFF,
        (
            "My name is Muller ……\x01",
            "Music manager in the empire\x01",
            "It is those who do.\x02\x03",
            "Although it is short,\x01",
            "Let me hopefully keep you informed.\x02",
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
            "#6P#00006FO, music manager ……?\x01",
            "(I can not see it at all, but …).\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101F(If anything\x01",
            "It is a feeling of SP, is not it? …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105F(Before that, I will have a similar title\x01",
            "Something I've heard of … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#12405F… … Did you do something?\x02",
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
            "#6P#00012FNo……\x02\x03",
            "#00000FLet me see……\x01",
            "Then about the request\x01",
            "Can you give me a detailed explanation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FCertainly \"musical instruments\" are missing\x01",
            "It was a story about getting on.\x02\x03",
            "#10302FTo tell you,\x01",
            "Is he the person who manages it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FOh, that's right.\x02\x03",
            "For ourselves, for a performance trip\x01",
            "I entered the crossbell … …\x02\x03",
            "#12406FIn a space where I looked a little,\x01",
            "I got stuck with that musician.\x02\x03",
            "#12400FThere is no Ate to look for in a town where you do not know selfishly,\x01",
            "I was in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FIt certainly seems tough, is not it …?\x01",
            "Crosband city is wide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12401FOh, there are also it … …\x01",
            "There is a problem that is a little troublesome.\x02\x03",
            "#12400FCan I ask for a search immediately?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x76, 0x1, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Jump("loc_4473")

    label("loc_4408")


    ChrTalk(
        0x18,
        (
            "#12400FTo you guys,\x01",
            "I got missing in the city\x01",
            "I'd like to ask for a search for \"musicians\".\x02\x03",
            "Can I ask for a search immediately?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4473")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C9")
    Call(0, 34)
    Jump("loc_45A1")

    label("loc_44C9")


    ChrTalk(
        0x101,
        (
            "#6P#00006FThat……\x01",
            "I'm sorry.\x02\x03",
            "Now I have another job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12405FHM……\x01",
            "That's too bad.\x02\x03",
            "#12400FIf there is no hand\x01",
            "It will be appreciated if you call out.\x02\x03",
            "Anyway, you are in a hurry.\x01",
            "I beg you to do my best.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x156, 1)

    label("loc_45A1")

    SetChrPos(0x0, 17460, 0, -4190, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x18, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_33_3C73 end

    def Function_34_45C3(): pass

    label("Function_34_45C3")


    ChrTalk(
        0x101,
        (
            "#6P#00000FOK,\x01",
            "Please choose for me.\x02\x03",
            "#00000FThen, search\x01",
            "About \"musicians\"\x01",
            "Would you please let me know in detail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FWell, OK.\x02\x03",
            "The name of the musicians ……\x01",
            "\"Olivier · Renheim\".\x02\x03",
            "A blonde man in his twenties,\x01",
            "Coat a white coat\x01",
            "I have a lute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FHmm, when you have an instrument\x01",
            "It looks very noticeable.\x02\x03",
            "#10300FIt is difficult to find it\x01",
            "I do not feel like it seems to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FOh, that alone\x01",
            "To find and take home\x01",
            "Although there is not much problem … …\x02\x03",
            "#12406FOlivier,\x01",
            "There is a problem in character a little.\x02\x03",
            "I have not even asked\x01",
            "Put his neck in trouble on his own,\x01",
            "I will make it even more troublesome.\x02\x03",
            "#12400FTo be honest, with a nasty person\x01",
            "You can say that.\x02",
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
        "#6P#00105FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FIn order not to hinder the performance trip,\x01",
            "I would like you to find out promptly … …\x01",
            "Well, hope for that is not good.\x02\x03",
            "#12406FAt the very least, before the evil stand out\x01",
            "It will be appreciated if you catch it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FI'm gonna have a manager.\x01",
            "That's a huge speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FAnd for the time being, the image\x01",
            "I got it to a certain extent.\x02\x03",
            "#00000FIn the other place\x01",
            "Does not it work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12405FYeah, if you say it is strong … …\x02\x03",
            "#12400FDazzling place,\x01",
            "Or a lively place\x01",
            "It will tend to like it.\x02\x03",
            "#12406FA gourmander wears a meal at a place\x01",
            "Although there is a possibility of sitting there … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FAnyway the fire kind of trouble\x01",
            "That is a place you think is likely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FThen,\x01",
            "Old town, red light district, back street ……\x01",
            "It seems likely to be around that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12404FOh, it can be said that it is a good line … …\x02\x03",
            "#12400F…… Actually, the entertainment district\x01",
            "I already finished looking all along.\x01",
            "You should not mind removing it from the search range.\x02\x03",
            "#12406FProbably I will come looking and stepping on\x01",
            "I wonder what he avoids the most places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FI see, I see … ….\x02\x03",
            "#00100FBut, if I say a place that seems to be bustling\x01",
            "Today the port area may also enter.\x02\x03",
            "#00100FCertainly, Mikei in the park\x01",
            "You should be doing a business trip event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FHM……\x01",
            "Well it is likely to narrow down\x01",
            "Is it such a place?\x02\x03",
            "#12406FSorry, a little more information\x01",
            "I wish I could have offered it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FNo, it was helpful.\x02\x03",
            "#00000FThen, immediately for the investigation\x01",
            "I will match it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FI beg you to do my best.\x02\x03",
            "If you have difficulty bringing\x01",
            "Even if it matches somewhat painful eyes\x01",
            "I do not care.\x02",
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
            "#6P#00006FRyo, OK.\x01",
            "(Really, what kind of relationship?)\x02",
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
            "Quest 【Searching for performers】\x07\x00",
            "I started!\x02",
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

    # Function_34_45C3 end

    def Function_35_4F87(): pass

    label("Function_35_4F87")

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

    def lambda_5049():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5049)
    Sleep(50)

    def lambda_5066():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5066)
    Sleep(50)

    def lambda_5083():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5083)
    Sleep(50)

    def lambda_50A0():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_50A0)
    Sleep(50)

    def lambda_50BD():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_50BD)
    Sleep(50)

    def lambda_50DA():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50DA)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#00000FWell, at the Crossbell station\x01",
            "I came here ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FTo be sure, the official inspector of the station\x01",
            "You were requesting a support request, were not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, let's visit at once.\x02",
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

    # Function_35_4F87 end

    def Function_36_51DA(): pass

    label("Function_36_51DA")

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
            "Oh, maybe\x01",
            "Are you the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, looking at the support request\x01",
            "I heard.\x02\x03",
            "I am a republican inspector\x01",
            "Was that all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Especially, from the Republic of Calvert\x01",
            "Mr. Murrow of an inspector who is on loan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I would like to explain the work at once,\x01",
            "You get a request, do not you?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    EventEnd(0x5)
    Return()

    # Function_36_51DA end

    def Function_37_53A9(): pass

    label("Function_37_53A9")

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
            "Hmm, you guys.\x01",
            "You get a request, do not you?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    EventEnd(0x5)
    Return()

    # Function_37_53A9 end

    def Function_38_549B(): pass

    label("Function_38_549B")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Receive a request\x01",      # 0
            "To give up\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5543")

    ChrTalk(
        0x101,
        "#00000FYes, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I appreciate it.\x01",
            "So let me explain.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 39)
    Jump("loc_562D")

    label("loc_5543")


    ChrTalk(
        0x101,
        (
            "#00003FExcuse me,\x01",
            "Now I have another job ……\x02\x03",
            "May I ask again later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Hmm, if somewhat\x01",
            "Flexibility is good, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I am busy for quite a while.\x01",
            "Please do as soon as possible.\x02",
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

    label("loc_562D")

    Return()

    # Function_38_549B end

    def Function_39_562E(): pass

    label("Function_39_562E")


    ChrTalk(
        0x19,
        (
            "Well, to you guys\x01",
            "I do not want to ask anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Examination work of the train to the Republic,\x01",
            "I'd like to ask for that help.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5796")

    ChrTalk(
        0x101,
        (
            "#00005FIs it a train inspection?\x02\x03",
            "#00000FOnce before, the empire's inspector\x01",
            "Because I've helped with my work\x01",
            "I think that you can roughly understand.\x02\x03",
            "Suspicious persons and suspicious objects\x01",
            "Whether you are not on the train\x01",
            "I check it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "That's right.\x01",
            "If you have experience, talk is quick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_582D")

    label("loc_5796")


    ChrTalk(
        0x101,
        (
            "#00003FExamination, saying … …\x02\x03",
            "#00000FSuspicious persons and suspicious objects\x01",
            "Whether you are not on the train\x01",
            "Is not it a check?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "That's right.\x01",
            "Understanding is quick and it will be saved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_582D")


    ChrTalk(
        0x19,
        (
            "Anyway, now at the trade meeting\x01",
            "There is a warning level everywhere\x01",
            "It is a situation that is going up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "In addition to usual more strict confirmation\x01",
            "We also have cooperation with the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Even if there are any hands of inspectors now\x01",
            "It's a missing situation.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x50, 0x1F4)
    Sound(801, 0, 100, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice of station staff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "…… Soon, the first home\x01",
            "A train bound for the Republic will arrive.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you are riding\x01",
            "Take care of your feet,\x01",
            "Please hurry to the home.\x07\x00\x02",
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
            "Apparently the intended train\x01",
            "It seems they came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "For details, at home\x01",
            "I will talk to you.\x02",
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
            "Quest 【Work assistance of Republic examiner】\x07\x00",
            "I started!\x02",
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

    # Function_39_562E end

    def Function_40_5A7F(): pass

    label("Function_40_5A7F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 4)), scpexpr(EXPR_END)), "loc_5C7B")

    ChrTalk(
        0x101,
        (
            "#5P#00006FAt the entrance a little while ago\x01",
            "The key was hanging … ….\x02\x03",
            "#00013FApparently Ms. Kirika\x01",
            "It seems I removed it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C36")

    ChrTalk(
        0x10A,
        (
            "#00601F#6PHung, although it is an emergency,\x01",
            "As usual things …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C7B")

    ChrTalk(
        0x109,
        (
            "#10108F#6PBecause it is illegal\x01",
            "I can not admire it ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C7B")


    ChrTalk(
        0x104,
        (
            "#6P#00306FBut there's really noone here\x02\x03",
            "#00301FTranscontinental railroad\x01",
            "If it stops it's the way it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FWell … … people from the railroad corporation\x01",
            "Opposition officers of the Empire and Republic also\x01",
            "He seems to have been removed from the country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FKirika and Rector are\x01",
            "Was it the third home train?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FAh……\x01",
            "Let's get down to home.\x02",
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

    # Function_40_5A7F end

    def Function_41_5DD3(): pass

    label("Function_41_5DD3")

    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(900)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(600)

    def lambda_5DEC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5DEC)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_41_5DD3 end

    def Function_42_5E09(): pass

    label("Function_42_5E09")

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
        "… …. Ah, you guys ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Good, seeing the request\x01",
            "You must have come! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIs cheers for good work,\x01",
            "Raymond.\x02\x03",
            "#00005F… …. Is that one of you?\x01",
            "Donovan police … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Oh, hey\x01",
            "There are various things … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Briefly, the circumstances\x01",
            "May I talk to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThank you.\x02\x03",
            "#00101FAt the request, also a fake brand trader\x01",
            "You seem to be chasing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "With the reform of the new mayor's mayor\x01",
            "Fake brand quotient properly\x01",
            "I was able to control regulations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Even with Section two\x01",
            "Enforcement has been strengthened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Meanwhile,\x01",
            "Example fake brand trader\x01",
            "Enter the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Thanks to persistent tenacity,\x01",
            "Finally the transaction site\x01",
            "I succeeded in suppressing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FFake brand quotient ……\x01",
            "Um, I came through the Tangram gate.\x01",
            "It was someone who was a tourist.\x02\x03",
            "#10105FBy the way,\x01",
            "What kind of person was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSpeaking of which, to introduce passengers\x01",
            "I asked Noel for help.\x02\x03",
            "#00003FWell, I guess so ….\x02",
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
        "#00200FMy mouth is bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FI was surprised\x01",
            "My voice is great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FSprinter-like\x01",
            "My feet are fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FAnyway, if expressed in one word\x01",
            "\"A ridiculous person\" … Kana.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x109,
        "#10105FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHuh, it looks interesting\x01",
            "I would definitely like to meet him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F… Well, whatever\x01",
            "Is not that big Venus?\x02\x03",
            "Mr. Bar\x01",
            "I will stop it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Yes, well ….\x01",
            "I was glad there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "After that, eventually\x01",
            "I was able to escape.\x01",
            "…… at awful speed.\x02",
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
        "#00206FI do not care for that old lady …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSo …\x01",
            "A fake brand dealer who ran away\x01",
            "That's why I am in this station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Oh, exactly!\x01",
            "As expected, it is good to see ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Apparently, towards the Empire\x01",
            "You seem to be going high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "He bought the police completely\x01",
            "I guess they are thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I looked at the second home,\x01",
            "It seems like I'm waiting for the train without delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUntil Empire Destination arrives\x01",
            "I still have time ……\x01",
            "It's a great opportunity to catch it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F……Hmm?\x01",
            "There is a settlement there\x01",
            "It means that it is in order … …\x02\x03",
            "#00303FWhat we do is to do\x01",
            "Is not it almost there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Well, there it is ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Donovan seems to be busy,\x01",
            "This matter was left to me by my side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "But …. mostly me alone\x01",
            "Restrain that fake brand quotient\x01",
            "Do not feel confident …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, yes.\x01",
            "Even though I have confidence …\x01",
            "It is certain that they are short of people.\x02\x03",
            "#00001FWithin this wide station,\x01",
            "I have to lay a siege network properly\x01",
            "The possibility of escape is likely high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Right?\x01",
            "So, I will cheer for you guys\x01",
            "I asked for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I want to ask,\x01",
            "Bogus fake with me\x01",
            "Supporting role to arrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Also, a fake brand trader\x01",
            "Not to get out of the station\x01",
            "It's a watching role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Once I caught a fake brand merchant\x01",
            "If you guys thought that,\x01",
            "I wonder if you can help me?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x0)
    Call(0, 44)
    EventEnd(0x5)
    Return()

    # Function_42_5E09 end

    def Function_43_6A00(): pass

    label("Function_43_6A00")

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
            "I want to ask,\x01",
            "Bogus fake with me\x01",
            "Supporting role to arrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Also, a fake brand trader\x01",
            "Not to get out of the station\x01",
            "It's a watching role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Once I caught a fake brand merchant\x01",
            "If you guys thought that,\x01",
            "I wonder if you can help me?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 44)
    EventEnd(0x5)
    Return()

    # Function_43_6A00 end

    def Function_44_6BA5(): pass

    label("Function_44_6BA5")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BF8")
    Jump("loc_6D19")

    label("loc_6BF8")


    ChrTalk(
        0x101,
        (
            "#00006F……Excuse me,\x01",
            "There are other jobs now ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Well, I see.\x01",
            "It can not be helped … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Well then,\x01",
            "I will be here a little more\x01",
            "I will wait for the plane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "When time is available,\x01",
            "If you come and help me\x01",
            "I wonder if it will save you ~.\x02",
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

    label("loc_6D19")


    ChrTalk(
        0x101,
        (
            "#00000F… Well, I understand.\x01",
            "I will cooperate by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Oh, thank you!\x01",
            "I'll wear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Well then … First of all\x01",
            "Bogus fake with me\x01",
            "Let's decide on the group to arrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Who is on this side\x01",
            "Will you follow me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FLet me see……\x01",
            "How should we sort it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FAs Mr. Lloyd's as an investigator\x01",
            "I think that you should accompany you.\x02\x03",
            "#00211F…… Raymond alone\x01",
            "I am slightly worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Well, that's not it … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I'd like to say … … but,\x01",
            "Surely that way is safe ~.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012FLet me see……\x01",
            "Is it supposed to be a two person investigator?\x02\x03",
            "#00000FPlease have another one come for support,\x01",
            "The rest of the 4 people watch the station guard\x01",
            "It looks good to consolidate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell then……\x01",
            "Who will you bring later?\x02",
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
            "I will bring Ellie\x01",        # 0
            "Take Tio\x01",        # 1
            "I will take Randy\x01",      # 2
            "Take Noel\x01",        # 3
            "I will bring you a machine\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70FE")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#00000FEllie, follow me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00100FYes, I understand.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x1)
    Jump("loc_72AE")

    label("loc_70FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716B")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#00000FTio, follow me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#00200FIt is okay.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x2)
    Jump("loc_72AE")

    label("loc_716B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71D8")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00000FRandy, follow me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#00309FLove it.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x3)
    Jump("loc_72AE")

    label("loc_71D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7249")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        "#00000FNoel, follow me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#10100FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x4)
    Jump("loc_72AE")

    label("loc_7249")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#00000FWadi, follow me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        "#10304FLeader as you say.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x5)

    label("loc_72AE")

    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00003FEveryone else\x01",
            "Please monitor the entrance and exit of the station.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_72F0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_72F0)
    Sleep(50)

    def lambda_7300():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7300)
    Sleep(50)

    def lambda_7310():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7310)
    Sleep(50)

    def lambda_7320():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7320)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00001FBecause that is about that old lady\x01",
            "There is a possibility that it can come out by any chance.\x01",
            "Please be careful enough.\x02",
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

    def lambda_740D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_740D)

    def lambda_741A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_741A)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)

    ChrTalk(
        0x1B,
        (
            "…… Yatsura, on the premises\x01",
            "You do not seem to find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Already on the train\x01",
            "Perhaps it is riding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "… … I will hurry.\x02",
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
            "Quest 【Tracking fake brand quotient】\x07\x00",
            "I started!\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75C1")
    AddParty(0x1, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 3)
    Jump("loc_7619")

    label("loc_75C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75DC")
    AddParty(0x2, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 4)
    Jump("loc_7619")

    label("loc_75DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75F7")
    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 5)
    Jump("loc_7619")

    label("loc_75F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7612")
    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 6)
    Jump("loc_7619")

    label("loc_7612")

    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 7)

    label("loc_7619")

    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_44_6BA5 end

    def Function_45_7637(): pass

    label("Function_45_7637")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_774F")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_767A"),
        (1, "loc_7694"),
        (2, "loc_76AE"),
        (3, "loc_76C8"),
        (4, "loc_76E2"),
        (5, "loc_76FC"),
        (6, "loc_7716"),
        (SWITCH_DEFAULT, "loc_7730"),
    )


    label("loc_767A")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_774A")

    label("loc_7694")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_774A")

    label("loc_76AE")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_774A")

    label("loc_76C8")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_774A")

    label("loc_76E2")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_774A")

    label("loc_76FC")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_774A")

    label("loc_7716")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_774A")

    label("loc_7730")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_774A")

    label("loc_774A")

    Jump("Function_45_7637")

    label("loc_774F")

    Return()

    # Function_45_7637 end

    def Function_46_7750(): pass

    label("Function_46_7750")

    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Return()

    # Function_46_7750 end

    def Function_47_776F(): pass

    label("Function_47_776F")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    Return()

    # Function_47_776F end

    def Function_48_778E(): pass

    label("Function_48_778E")

    Sleep(600)
    OP_95(0xFE, 19770, 30, 7340, 2000, 0x0)
    OP_95(0xFE, 23810, 0, 7440, 2000, 0x0)
    Return()

    # Function_48_778E end

    def Function_49_77BA(): pass

    label("Function_49_77BA")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 19710, 30, 8420, 2000, 0x0)
    Sound(100, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(500)
    OP_95(0xFE, 23490, 0, 8520, 2000, 0x0)
    Return()

    # Function_49_77BA end

    def Function_50_7803(): pass

    label("Function_50_7803")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 3)), scpexpr(EXPR_END)), "loc_7A39")

    ChrTalk(
        0x104,
        (
            "#00306FLloyd's\x01",
            "I went to the Republic\x01",
            "I was surprised when I heard it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FThat was supposed to happen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHuhu, without being contacted\x01",
            "Sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, I tentatively\x01",
            "The fake brand merchant was caught\x01",
            "By doing it in a result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHaha, let's do it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F9B")

    label("loc_7A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 4)), scpexpr(EXPR_END)), "loc_7B9B")

    ChrTalk(
        0x102,
        (
            "#00106FLloyd's\x01",
            "I went to the Republic\x01",
            "I was surprised when I heard that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, to such a thing\x01",
            "I wish I was becoming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI should have contacted you.\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, I tentatively\x01",
            "The fake brand merchant was caught\x01",
            "By doing it in a result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHaha, let's do it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F9B")

    label("loc_7B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 5)), scpexpr(EXPR_END)), "loc_7CFB")

    ChrTalk(
        0x109,
        (
            "#10106FLloyd's\x01",
            "I went to the Republic\x01",
            "I was surprised when I heard that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWhew, it can not be\x01",
            "It is said that it was such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, it's tropical.\x01",
            "It was an emergency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, I tentatively\x01",
            "The fake brand merchant was caught\x01",
            "By doing it in a result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FWell, let's do it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F9B")

    label("loc_7CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 6)), scpexpr(EXPR_END)), "loc_7E51")

    ChrTalk(
        0x105,
        (
            "#10306FLloyd's\x01",
            "When I heard that I went to the Republic\x01",
            "I was also surprised at the flowing stone servant … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, to such a thing\x01",
            "I wish I was becoming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha ……\x01",
            "I'm sorry, I did not get in touch with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, I tentatively\x01",
            "The fake brand merchant was caught\x01",
            "By doing it in a result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FWell, let's do it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F9B")

    label("loc_7E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 7)), scpexpr(EXPR_END)), "loc_7F9B")

    ChrTalk(
        0x109,
        (
            "#10106FLloyd's\x01",
            "I went to the Republic\x01",
            "I was surprised when I heard that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, to such a thing\x01",
            "I wish I was becoming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FIt was an emergency.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, I tentatively\x01",
            "The fake brand merchant was caught\x01",
            "By doing it in a result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FWell, let's do it.\x02",
    )

    CloseMessageWindow()

    label("loc_7F9B")


    ChrTalk(
        0x1A,
        (
            "Well, I am also at the desk of the second investigation department\x01",
            "I have to make a record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "I will be rude around here.\x02",
    )

    CloseMessageWindow()

    def lambda_8003():

        label("loc_8003")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8003")

    QueueWorkItem2(0x103, 1, lambda_8003)

    def lambda_8015():

        label("loc_8015")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8015")

    QueueWorkItem2(0x104, 1, lambda_8015)

    def lambda_8027():

        label("loc_8027")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8027")

    QueueWorkItem2(0x109, 1, lambda_8027)

    def lambda_8039():

        label("loc_8039")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8039")

    QueueWorkItem2(0x105, 1, lambda_8039)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 3)), scpexpr(EXPR_END)), "loc_807A")

    ChrTalk(
        0x102,
        "#00109FHehe, thanks for your hard work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8131")

    label("loc_807A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 4)), scpexpr(EXPR_END)), "loc_80AB")

    ChrTalk(
        0x103,
        "#00202FI appreciate your work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8131")

    label("loc_80AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 5)), scpexpr(EXPR_END)), "loc_80D4")

    ChrTalk(
        0x104,
        "#00309FHello, I am tired.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8131")

    label("loc_80D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 6)), scpexpr(EXPR_END)), "loc_8105")

    ChrTalk(
        0x109,
        "#10109FHahaha, good tired!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8131")

    label("loc_8105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 7)), scpexpr(EXPR_END)), "loc_8131")

    ChrTalk(
        0x105,
        "#10302FHuh, I was tired.\x02",
    )

    CloseMessageWindow()

    label("loc_8131")


    ChrTalk(
        0x1A,
        (
            "No, this time to you guys\x01",
            "I was endured until the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Never me alone\x01",
            "You can catch that old lady\x01",
            "I think I did not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Thank you so much for today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FNo, this is it.\x02\x03",
            "#00000FIf there is something again\x01",
            "Please contact the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Oh, I'm begging for you!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x10E, 0x1F4)

    def lambda_8245():
        OP_95(0xFE, 3980, 30, 220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8245)
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
            "Quest 【Tracking fake brand quotient】\x07\x00",
            "Achieved!\x02",
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

    # Function_50_7803 end

    def Function_51_830A(): pass

    label("Function_51_830A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "← To Republic / 1st Line Home\x01",
            "Republic of Altair City 35 minutes\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_51_830A end

    def Function_52_8382(): pass

    label("Function_52_8382")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To Empire · Line 2 → Home →\x01",
            "Empire Galleria Fortress 32 minutes\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_52_8382 end

    def Function_53_83FA(): pass

    label("Function_53_83FA")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell Autonomous Region\x01",
            "There is a timetable.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_53_83FA end

    def Function_54_8433(): pass

    label("Function_54_8433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_844A")
    Call(0, 56)
    Return()

    label("loc_844A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ ※ Office inspection officer ※ ※\x01",
            "Access other than stakeholders\x01",
            "Strictly prohibited.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_54_8433 end

    def Function_55_84C6(): pass

    label("Function_55_84C6")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell Autonomous Region\x01",
            "There is a route map.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_55_84C6 end

    def Function_56_84FF(): pass

    label("Function_56_84FF")

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
            "#12P#00200F…… In the meantime,\x01",
            "It looks like there is no one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FThe railway was also suspended,\x01",
            "Empire, republican inspector\x01",
            "I guess they were allowed to leave the house.\x02\x03",
            "#00100FThe station staff also,\x01",
            "Now in different places\x01",
            "I wonder if she is evacuating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FWell, the reason why it remains in such a place\x01",
            "I guess it would not be much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FNow to Mr. Kirika\x01",
            "Let's go meet.\x02\x03",
            "To the home from the entrance of the lower floor\x01",
            "You ought to get off.\x02",
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

    # Function_56_84FF end

    SaveToFile()

Try(main)
