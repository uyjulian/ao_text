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
        "Function_4_C65",          # 04, 4
        "Function_5_C69",          # 05, 5
        "Function_6_1224",         # 06, 6
        "Function_7_13F5",         # 07, 7
        "Function_8_13F9",         # 08, 8
        "Function_9_193C",         # 09, 9
        "Function_10_1AC4",        # 0A, 10
        "Function_11_1EE7",        # 0B, 11
        "Function_12_1EEB",        # 0C, 12
        "Function_13_231E",        # 0D, 13
        "Function_14_2322",        # 0E, 14
        "Function_15_2B36",        # 0F, 15
        "Function_16_2CF8",        # 10, 16
        "Function_17_2D02",        # 11, 17
        "Function_18_2EDB",        # 12, 18
        "Function_19_3160",        # 13, 19
        "Function_20_3308",        # 14, 20
        "Function_21_34BB",        # 15, 21
        "Function_22_37F1",        # 16, 22
        "Function_23_39B7",        # 17, 23
        "Function_24_3BC2",        # 18, 24
        "Function_25_3D86",        # 19, 25
        "Function_26_3E9B",        # 1A, 26
        "Function_27_3F56",        # 1B, 27
        "Function_28_4258",        # 1C, 28
        "Function_29_428F",        # 1D, 29
        "Function_30_42DC",        # 1E, 30
        "Function_31_42E6",        # 1F, 31
        "Function_32_42F0",        # 20, 32
        "Function_33_4379",        # 21, 33
        "Function_34_4CDA",        # 22, 34
        "Function_35_57EA",        # 23, 35
        "Function_36_5A32",        # 24, 36
        "Function_37_5C42",        # 25, 37
        "Function_38_5D41",        # 26, 38
        "Function_39_5EF4",        # 27, 39
        "Function_40_6420",        # 28, 40
        "Function_41_680E",        # 29, 41
        "Function_42_6844",        # 2A, 42
        "Function_43_7551",        # 2B, 43
        "Function_44_7736",        # 2C, 44
        "Function_45_81B2",        # 2D, 45
        "Function_46_82CB",        # 2E, 46
        "Function_47_82EA",        # 2F, 47
        "Function_48_8309",        # 30, 48
        "Function_49_8335",        # 31, 49
        "Function_50_837E",        # 32, 50
        "Function_51_8FA1",        # 33, 51
        "Function_52_9022",        # 34, 52
        "Function_53_90AC",        # 35, 53
        "Function_54_90F5",        # 36, 54
        "Function_55_917B",        # 37, 55
        "Function_56_91B0",        # 38, 56
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
            "It's a car magazine,\x01",
            ""Car Star Extra".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x373, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C61")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Learned the \x07\x02",
            ""Shine\x01",
            "Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x373, 1)

    label("loc_C61")

    TalkEnd(0xFF)
    Return()

    # Function_3_BBC end

    def Function_4_C65(): pass

    label("Function_4_C65")

    Call(0, 5)
    Return()

    # Function_4_C65 end

    def Function_5_C69(): pass

    label("Function_5_C69")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C7D")
    Call(0, 6)
    Jump("loc_1220")

    label("loc_C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_EE1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D83")

    ChrTalk(
        0x8,
        (
            "Thank you very much for\x01",
            "using Crossbell Station\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Republic-bound train will\x01",
            "be departing soon, the Empire-\x01",
            "bound one will then follow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Passengers in a hurry,\x01",
            "please hurry and\x01",
            "purchase your tickets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E25")

    label("loc_D83")


    ChrTalk(
        0x8,
        (
            "The Republic-bound train will\x01",
            "be departing soon, the Empire-\x01",
            "bound one will then follow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Passengers in a hurry,\x01",
            "please hurry and\x01",
            "purchase your tickets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E25")

    Jump("loc_EDC")

    label("loc_E2A")


    ChrTalk(
        0x8,
        (
            "When I heard that a criminal on\x01",
            "the loose jumped onto the train's\x01",
            "roof, I could hardly believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, it seems\x01",
            "we'll need to warn people\x01",
            "not to imitate them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDC")

    Jump("loc_1220")

    label("loc_EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDC")

    ChrTalk(
        0x8,
        (
            "Thank you very much for\x01",
            "using Crossbell Station\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For the duration of the trade\x01",
            "conference, platform security will\x01",
            "be reinforced by the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please be understanding\x01",
            "of the stricter\x01",
            "inspections.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1080")

    label("loc_FDC")


    ChrTalk(
        0x8,
        (
            "For the duration of the trade\x01",
            "conference, platform security will\x01",
            "be reinforced by the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please be understanding\x01",
            "of the stricter\x01",
            "inspections.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1080")

    Jump("loc_1220")

    label("loc_1085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1220")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117E")

    ChrTalk(
        0x8,
        (
            "Thank you very much for\x01",
            "using Crossbell Station\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The trade conference is\x01",
            "underway, but the railway\x01",
            "service is operating as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tickets can be bought on\x01",
            "the second floor, so\x01",
            "please, head over there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1220")

    label("loc_117E")


    ChrTalk(
        0x8,
        (
            "The trade conference is\x01",
            "underway, but the railway\x01",
            "service is operating as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tickets can be bought on\x01",
            "the second floor, so\x01",
            "please, head over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1220")

    TalkEnd(0x8)
    Return()

    # Function_5_C69 end

    def Function_6_1224(): pass

    label("Function_6_1224")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132A")

    ChrTalk(
        0x8,
        (
            "Currently, train service\x01",
            "to both the Empire and the\x01",
            "Republic are suspended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We apologize to our\x01",
            "customers for any\x01",
            "inconvenience, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "No way, that's a problem! I've\x01",
            "got an important business\x01",
            "negotiation in the Empire!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13EC")

    label("loc_132A")


    ChrTalk(
        0x8,
        (
            "We are terribly sorry, but we\x01",
            "do not know when the service\x01",
            "will resume at this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please understand, my\x01",
            "good sir...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "No way, my business\x01",
            "negotiation, my business\x01",
            "negotiatiooon!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13EC")

    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_6_1224 end

    def Function_7_13F5(): pass

    label("Function_7_13F5")

    Call(0, 8)
    Return()

    # Function_7_13F5 end

    def Function_8_13F9(): pass

    label("Function_8_13F9")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1406")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1938")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1458")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1458")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1508")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1477")
    OP_AF(0x8B)
    Jump("loc_14F9")

    label("loc_1477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1487")
    OP_AF(0x8A)
    Jump("loc_14F9")

    label("loc_1487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1497")
    OP_AF(0x89)
    Jump("loc_14F9")

    label("loc_1497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_14A7")
    OP_AF(0x88)
    Jump("loc_14F9")

    label("loc_14A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_14B7")
    OP_AF(0x87)
    Jump("loc_14F9")

    label("loc_14B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_14C7")
    OP_AF(0x86)
    Jump("loc_14F9")

    label("loc_14C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_14D7")
    OP_AF(0x85)
    Jump("loc_14F9")

    label("loc_14D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_14E7")
    OP_AF(0x84)
    Jump("loc_14F9")

    label("loc_14E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_14F7")
    OP_AF(0x83)
    Jump("loc_14F9")

    label("loc_14F7")

    OP_AF(0x82)

    label("loc_14F9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1933")

    label("loc_1508")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151C")
    Jump("loc_1933")

    label("loc_151C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1933")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1546")
    Call(0, 9)
    Jump("loc_1933")

    label("loc_1546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1688")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E1")

    ChrTalk(
        0x9,
        (
            "Would you like a station\x01",
            "boxed lunch to go along\x01",
            "with your trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have the latest issue\x01",
            "of Crossbell Times as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1683")

    label("loc_15E1")


    ChrTalk(
        0x9,
        (
            "A criminal on the loose and the arrest\x01",
            "of terrorists... You don't often hear of\x01",
            "such things happening at the same time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Could it just be a\x01",
            "coincidence?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1683")

    Jump("loc_1933")

    label("loc_1688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1853")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AF")

    ChrTalk(
        0x9,
        (
            "Inspector Marlowe was\x01",
            "transferred from the\x01",
            "Republican Army.\x02",
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
            "The Empire and Republic have an\x01",
            "antagonistic relationship, so\x01",
            "it probably can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_184E")

    label("loc_17AF")


    ChrTalk(
        0x9,
        (
            "Inspectors Marlow and\x01",
            "Quattro don't go along\x01",
            "well at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The Empire and Republic have an\x01",
            "antagonistic relationship, so\x01",
            "it probably can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184E")

    Jump("loc_1933")

    label("loc_1853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1933")

    ChrTalk(
        0x9,
        (
            "This morning it appears that even\x01",
            "journalists of the Imperial Chronicle, an\x01",
            "Imperial publisher, came for coverage.\x02",
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

    label("loc_1933")

    Jump("loc_1406")

    label("loc_1938")

    TalkEnd(0x9)
    Return()

    # Function_8_13F9 end

    def Function_9_193C(): pass

    label("Function_9_193C")

    OP_4B(0x9, 0xFF)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A21")

    NpcTalk(
        0x11,
        "Citizen",
        (
            "Damn, it doesn't matter\x01",
            "if I can refund my\x01",
            "ticket!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Citizen",
        (
            "I diligently prepared\x01",
            "for today's trip, you\x01",
            "know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm t-terribly sorry. At\x01",
            "present, we're trying to\x01",
            "confirm the facts...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ABB")

    label("loc_1A21")


    NpcTalk(
        0x11,
        "Citizen",
        (
            "Seriously. The customers\x01",
            "are always the ones who\x01",
            "suffer, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm t-terribly sorry. At\x01",
            "present, we're trying to\x01",
            "confirm the facts...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABB")

    OP_4C(0x9, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_9_193C end

    def Function_10_1AC4(): pass

    label("Function_10_1AC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1AD8")
    Call(0, 17)
    Jump("loc_1EE3")

    label("loc_1AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CD3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B89")

    ChrTalk(
        0xFE,
        (
            "That policeman looks\x01",
            "like he's looking for\x01",
            "someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is he chasing someone? I didn't\x01",
            "see anyone particularly\x01",
            "suspicious enter the station...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCE")

    label("loc_1B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4C")

    ChrTalk(
        0xFE,
        (
            "Not just a fake brand\x01",
            "trader, but even\x01",
            "terrorists...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't know their faces,\x01",
            "so they could even slip in\x01",
            "among normal people, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's some scary\x01",
            "stuff...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1CCE")

    label("loc_1C4C")


    ChrTalk(
        0xFE,
        (
            "Not only a fake brand trader,\x01",
            "but even terrorists could have\x01",
            "slipped in among normal people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's some scary\x01",
            "stuff...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCE")

    Jump("loc_1EE3")

    label("loc_1CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D8D")

    ChrTalk(
        0xFE,
        (
            "Platform No. 3, where the\x01",
            "Eisengraf is stopped, is strictly\x01",
            "guarded by the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't mind if you give\x01",
            "it a look, but take care\x01",
            "not to get too close.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE3")

    label("loc_1D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1EE3")

    ChrTalk(
        0xFE,
        (
            "This morning, the Eisengraf, the train\x01",
            "for exclusive use by the Imperial\x01",
            "government, arrived at platform No. 1.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since the other trains are in\x01",
            "regular service, it's been\x01",
            "moved to platform No. 3.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You don't see it every day, you know, so if\x01",
            "you get the chance, you should definitely\x01",
            "go take a look at it on the platform.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE3")

    TalkEnd(0xFE)
    Return()

    # Function_10_1AC4 end

    def Function_11_1EE7(): pass

    label("Function_11_1EE7")

    Call(0, 12)
    Return()

    # Function_11_1EE7 end

    def Function_12_1EEB(): pass

    label("Function_12_1EEB")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1FB6")

    ChrTalk(
        0xA,
        (
            "We're terribly sorry, but because\x01",
            "we're dealing with a train accident\x01",
            "right now, there's a lot of confusion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please be aware that you\x01",
            "can neither purchase nor\x01",
            "reserve tickets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231A")

    label("loc_1FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2204")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B4")

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
            "It seems she's someone\x01",
            "who has been doing\x01",
            "trades for many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I didn't hear the full\x01",
            "details, but I wish her\x01",
            "good luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2157")

    label("loc_20B4")


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
            "She was going to do trades\x01",
            "in the Empire or something.\x01",
            "I wish her good luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2157")

    Jump("loc_21FF")

    label("loc_215C")


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

    label("loc_21FF")

    Jump("loc_231A")

    label("loc_2204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_22B8")

    ChrTalk(
        0xA,
        (
            "At present, for security\x01",
            "reasons, we are thoroughly\x01",
            "checking hand bags upon entry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We apologize for the\x01",
            "inconvenience, but please\x01",
            "understand and cooperate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231A")

    label("loc_22B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_231A")

    ChrTalk(
        0xA,
        (
            "This is the ticket\x01",
            "counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please speak to me if\x01",
            "you wish to make a\x01",
            "purchase.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231A")

    TalkEnd(0xA)
    Return()

    # Function_12_1EEB end

    def Function_13_231E(): pass

    label("Function_13_231E")

    Call(0, 14)
    Return()

    # Function_13_231E end

    def Function_14_2322(): pass

    label("Function_14_2322")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245A")

    ChrTalk(
        0xB,
        (
            "Ah... I am sorry, could\x01",
            "you please wait a\x01",
            "moment?\x02",
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
            "At present, train service is on\x01",
            "hold due to a derailment along West\x01",
            "Crossbell Highway.\x02\x03",
            "Furthermore, service is expected to\x01",
            "be down for the rest of the day. We\x01",
            "thank you for your understanding.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_24C8")

    label("loc_245A")


    ChrTalk(
        0xB,
        (
            "An announcement for\x01",
            "dealing with refunds...\x01",
            "That must be tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I hope service is\x01",
            "restored quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C8")

    Jump("loc_2B32")

    label("loc_24CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2744")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2690")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D2")

    ChrTalk(
        0xB,
        (
            "Ah... I am sorry, could\x01",
            "you please wait a\x01",
            "moment?\x02",
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
            "Trains bound for the\x01",
            "Republic and Empire will\x01",
            "be departing shortly.\x02\x03",
            "Please take care not to\x01",
            "rush onto the train at\x01",
            "the last second.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_268B")

    label("loc_25D2")


    ChrTalk(
        0xB,
        (
            "Rushing onto the train at the last\x01",
            "second is a cause of accidents.\x01",
            "Doing so is quite dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you cannot make it in\x01",
            "time, please remain calm and\x01",
            "wait for the next train.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268B")

    Jump("loc_273F")

    label("loc_2690")


    ChrTalk(
        0xB,
        (
            "It's not just last second rushes.\x01",
            "I was shocked that someone jumped\x01",
            "onto the roof of a moving train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Should we warn people\x01",
            "against doing so with an\x01",
            "announcement?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273F")

    Jump("loc_2B32")

    label("loc_2744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2945")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2891")

    ChrTalk(
        0xB,
        (
            "Ah... I am sorry, could\x01",
            "you please wait a\x01",
            "moment?\x02",
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
            "The inspections performed at Crossbell\x01",
            "Station are based on Transcontinental\x01",
            "Railway Corporation rules.\x02\x03",
            "Passengers headed to the Empire and\x01",
            "Republic must complete an entry application\x01",
            "and present it to the inspector.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2940")

    label("loc_2891")


    ChrTalk(
        0xB,
        (
            "Passengers going from Crossbell\x01",
            "Station to the Empire or Republic\x01",
            "must undergo an inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We apologize for the\x01",
            "inconvenience, and appreciate\x01",
            "your understanding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2940")

    Jump("loc_2B32")

    label("loc_2945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAB")

    ChrTalk(
        0xB,
        (
            "Ah... I am sorry, could\x01",
            "you please wait a\x01",
            "moment?\x02",
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
            "Due to the arrival of the Eisengraf, the train\x01",
            "for exclusive use of the Imperial government,\x01",
            "security has been tightened today.\x02\x03",
            "Accordingly, passengers may not enter platform\x01",
            "No. 3 while it is stopped there. We appreciate\x01",
            "your understanding.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B32")

    label("loc_2AAB")


    ChrTalk(
        0xB,
        (
            "Excuse me, I am in\x01",
            "charge of the\x01",
            "announcements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Do you have any questions\x01",
            "about use of the railway?\x01",
            "Please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B32")

    TalkEnd(0xB)
    Return()

    # Function_14_2322 end

    def Function_15_2B36(): pass

    label("Function_15_2B36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1A")

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
            "As a simple Imperial soldier, it's\x01",
            "an incredible honor to be able to\x01",
            "welcome our government officials.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2C78")

    label("loc_2C1A")


    ChrTalk(
        0xFE,
        (
            "...Hmm? That large man in black\x01",
            "on the first floor... I think\x01",
            "I've seen him somewhere...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C78")

    Jump("loc_2CF4")

    label("loc_2C7D")


    ChrTalk(
        0xFE,
        (
            "Before I knew it, that\x01",
            "large man in black\x01",
            "vanished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, he couldn't be...\x01",
            "Yes, it's probably my\x01",
            "imagination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF4")

    TalkEnd(0xFE)
    Return()

    # Function_15_2B36 end

    def Function_16_2CF8(): pass

    label("Function_16_2CF8")

    TalkBegin(0xFE)
    Call(0, 17)
    TalkEnd(0xFE)
    Return()

    # Function_16_2CF8 end

    def Function_17_2D02(): pass

    label("Function_17_2D02")

    OP_4B(0xE, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E3E")

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
            "Based on what they told\x01",
            "us, it's pretty bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If handled poorly, the\x01",
            "train itself could be\x01",
            "totaled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm... In that case, we\x01",
            "can only arrange an\x01",
            "alternate train for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, resuming service\x01",
            "must be our top priority\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2ED2")

    label("loc_2E3E")


    ChrTalk(
        0xE,
        (
            "There's a considerable\x01",
            "chance that the track\x01",
            "itself is damaged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Let's head to the scene\x01",
            "as soon as the train is\x01",
            "cleared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, roger.\x02",
    )

    CloseMessageWindow()

    label("loc_2ED2")

    OP_4C(0xE, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_17_2D02 end

    def Function_18_2EDB(): pass

    label("Function_18_2EDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2EEF")
    Call(0, 9)
    Jump("loc_315C")

    label("loc_2EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F8F")

    ChrTalk(
        0xFE,
        (
            "Hmm, it appears the\x01",
            "train will depart soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be helped then. I think\x01",
            "I'll go shopping or something\x01",
            "and wait for the next train.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_315C")

    label("loc_2F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F9D")
    Jump("loc_315C")

    label("loc_2F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_315C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A4")

    ChrTalk(
        0xFE,
        (
            "I came from Altair City,\x01",
            "the westernmost harbor\x01",
            "city of the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, Crossbell has\x01",
            "really had staggering\x01",
            "growth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Republic is pretty prosperous,\x01",
            "but compared to Crossbell, you can\x01",
            "consider it the countryside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_315C")

    label("loc_30A4")


    ChrTalk(
        0xFE,
        (
            "I came from Altair City,\x01",
            "the westernmost harbor\x01",
            "city of the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, Crossbell has really had\x01",
            "staggering growth. It makes you feel\x01",
            "like the Republic is countryside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_315C")

    TalkEnd(0xFE)
    Return()

    # Function_18_2EDB end

    def Function_19_3160(): pass

    label("Function_19_3160")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3174")
    Call(0, 6)
    Jump("loc_3304")

    label("loc_3174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_323A")

    ChrTalk(
        0xFE,
        (
            "I heard from a station attendant...\x01",
            "It appears terrorist remnants were\x01",
            "caught in the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They'd been hiding for a\x01",
            "while, but now we can feel\x01",
            "safe for the time being.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3304")

    label("loc_323A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32FB")

    ChrTalk(
        0xFE,
        (
            "I'm going on a business\x01",
            "trip to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about how the main session\x01",
            "will go, but... It will be featured in the\x01",
            "Imperial Chronicle, so there's no problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3304")

    label("loc_32FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3304")

    label("loc_3304")

    TalkEnd(0xFE)
    Return()

    # Function_19_3160 end

    def Function_20_3308(): pass

    label("Function_20_3308")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3360")

    ChrTalk(
        0xFE,
        (
            "A d-derailment\x01",
            "accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband... How is my\x01",
            "husband!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B7")

    label("loc_3360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_33D2")

    ChrTalk(
        0xFE,
        (
            "I have finally arrived\x01",
            "in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After taking a rest, I\x01",
            "will go sightsee\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B7")

    label("loc_33D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34AE")

    ChrTalk(
        0xFE,
        (
            "What am I going to do with you... You\x01",
            "already ate all the roasted chestnuts we\x01",
            "bought in Altair as a souvenir on the train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, don't come\x01",
            "crying to me if you can't\x01",
            "eat your dinner tonight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B7")

    label("loc_34AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34B7")

    label("loc_34B7")

    TalkEnd(0xFE)
    Return()

    # Function_20_3308 end

    def Function_21_34BB(): pass

    label("Function_21_34BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_355D")

    ChrTalk(
        0xFE,
        (
            "Was it a rock fall? Or\x01",
            "something unnatural?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it was something unnatural...\x01",
            "I'll demand eye-popping\x01",
            "reparations from the perpetrator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37ED")

    label("loc_355D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3607")

    ChrTalk(
        0xFE,
        (
            "It seems a state of\x01",
            "tension continues at the\x01",
            "border gates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's what happens when you\x01",
            "propose independence. Youngsters\x01",
            "should know their place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37ED")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3615")
    Jump("loc_37ED")

    label("loc_3615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376D")

    ChrTalk(
        0xFE,
        (
            "They say Imperial Chancellor\x01",
            "Osborne had ties with\x01",
            "Hartmann, the former chairman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, rumor has it that the\x01",
            "chancellor took measures to deport\x01",
            "him in case Hartmann defected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He would've cast him away without mercy\x01",
            "if he became a liability. That's the kind\x01",
            "of man the Blood and Iron Chancellor is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_37ED")

    label("loc_376D")


    ChrTalk(
        0xFE,
        (
            "He would've cast him away without mercy\x01",
            "if he became a liability. That's the kind\x01",
            "of man the Blood and Iron Chancellor is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37ED")

    TalkEnd(0xFE)
    Return()

    # Function_21_34BB end

    def Function_22_37F1(): pass

    label("Function_22_37F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3884")

    ChrTalk(
        0xFE,
        (
            "For the railway to be\x01",
            "stopped... What on earth\x01",
            "could have happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I'll be able\x01",
            "to return to my\x01",
            "country...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B3")

    label("loc_3884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3957")

    ChrTalk(
        0xFE,
        (
            "What's with that blonde man?\x01",
            "He's been acting suspicious\x01",
            "for some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...What, is he a police officer? He\x01",
            "doesn't look too dependable... I wonder\x01",
            "if everything will be all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B3")

    label("loc_3957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3965")
    Jump("loc_39B3")

    label("loc_3965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39B3")

    ChrTalk(
        0xFE,
        (
            "The train just isn't\x01",
            "coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm getting tired of\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B3")

    TalkEnd(0xFE)
    Return()

    # Function_22_37F1 end

    def Function_23_39B7(): pass

    label("Function_23_39B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A80")

    ChrTalk(
        0xFE,
        (
            "Just when I was thinking\x01",
            "the train'd never depart...\x01",
            "A derailment happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll be spending the night\x01",
            "in Crossbell. I hope I'll be able\x01",
            "to get a room at the hotel...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BBE")

    label("loc_3A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B02")

    ChrTalk(
        0xFE,
        (
            "I'm going on a trip to\x01",
            "the Republic with my\x01",
            "boyfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to enjoy the\x01",
            "Eastern Quarter hot\x01",
            "springs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BBE")

    label("loc_3B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BB5")

    ChrTalk(
        0xFE,
        (
            "It seems like there's a fair\x01",
            "number of tourist attractions in\x01",
            "Crossbell as well, isn't there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can get to many of\x01",
            "them by bus. Maybe I'll\x01",
            "go see a few.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BBE")

    label("loc_3BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3BBE")

    label("loc_3BBE")

    TalkEnd(0xFE)
    Return()

    # Function_23_39B7 end

    def Function_24_3BC2(): pass

    label("Function_24_3BC2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3C5D")

    ChrTalk(
        0xFE,
        (
            "I finished refunding the\x01",
            "tickets I bought\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was looking forward to\x01",
            "this trip, but there's\x01",
            "nothing I can do about this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D82")

    label("loc_3C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3CDF")

    ChrTalk(
        0xFE,
        (
            "I'm going on a trip with\x01",
            "my girlfriend, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She wants to do so much.\x01",
            "I wonder if I have\x01",
            "enough mira...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D82")

    label("loc_3CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3CED")
    Jump("loc_3D82")

    label("loc_3CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D82")

    ChrTalk(
        0xFE,
        (
            "They say that there's a\x01",
            "trade conference being held\x01",
            "in Crossbell right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I should go\x01",
            "see the rumored Orchis\x01",
            "Tower?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D82")

    TalkEnd(0xFE)
    Return()

    # Function_24_3BC2 end

    def Function_25_3D86(): pass

    label("Function_25_3D86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3DBC")

    ChrTalk(
        0xFE,
        (
            "Hey, hey, did something\x01",
            "happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E97")

    label("loc_3DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E09")

    ChrTalk(
        0xFE,
        (
            "Tick tick... tick\x01",
            "tick... The clock...\x01",
            "spins and spins...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E97")

    label("loc_3E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E8E")

    ChrTalk(
        0xFE,
        (
            "*belch*... Altair City\x01",
            "was super fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The big Cyre river is\x01",
            "there you know, and a lot\x01",
            "of boats travel on it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E97")

    label("loc_3E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E97")

    label("loc_3E97")

    TalkEnd(0xFE)
    Return()

    # Function_25_3D86 end

    def Function_26_3E9B(): pass

    label("Function_26_3E9B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hey now, for real? What\x01",
            "happened to the cargo\x01",
            "from the Republic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now I'll have to consult with\x01",
            "the old man, contact the delivery\x01",
            "addresses... Man, I'm gonna be busy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_3E9B end

    def Function_27_3F56(): pass

    label("Function_27_3F56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F7B")
    Call(0, 33)
    Return()

    label("loc_3F7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4117")

    ChrTalk(
        0xFE,
        (
            "#12400FOlivier Lenheim is a musician who\x01",
            "dresses in a white coat and carries a\x01",
            "lute.\x02\x03",
            "He probably thought of a suspicious\x01",
            "place, a lively place or a meal spot\x01",
            "as his destination.\x02\x03",
            "I think you're on the right track with\x01",
            "Downtown, Back Street and Waterfront\x01",
            "Area you mentioned earlier.\x02\x03",
            "If you have trouble taking him with\x01",
            "you, I don't mind if you use force.\x01",
            "Please, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4254")

    label("loc_4117")


    ChrTalk(
        0xFE,
        (
            "#12400FOlivier probably thought of a\x01",
            "suspicious place, a lively place or a\x01",
            "meal spot as his destination.\x02\x03",
            "I think you're on the right track with\x01",
            "Downtown, Back Street and Waterfront\x01",
            "Area you mentioned earlier.\x02\x03",
            "If you have trouble taking him with\x01",
            "you, I don't mind if you use force.\x01",
            "Please, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4254")

    TalkEnd(0xFE)
    Return()

    # Function_27_3F56 end

    def Function_28_4258(): pass

    label("Function_28_4258")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_428E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_428A")
    Call(0, 36)
    Jump("loc_428D")

    label("loc_428A")

    Call(0, 37)

    label("loc_428D")

    Return()

    label("loc_428E")

    Return()

    # Function_28_4258 end

    def Function_29_428F(): pass

    label("Function_29_428F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42C2")
    Call(0, 42)
    Jump("loc_42C5")

    label("loc_42C2")

    Call(0, 43)

    label("loc_42C5")

    Return()

    label("loc_42C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D8")
    Jump("loc_42D8")

    label("loc_42D8")

    TalkEnd(0xFE)
    Return()

    # Function_29_428F end

    def Function_30_42DC(): pass

    label("Function_30_42DC")

    TalkBegin(0xFE)
    Call(0, 32)
    TalkEnd(0xFE)
    Return()

    # Function_30_42DC end

    def Function_31_42E6(): pass

    label("Function_31_42E6")

    TalkBegin(0xFE)
    Call(0, 32)
    TalkEnd(0xFE)
    Return()

    # Function_31_42E6 end

    def Function_32_42F0(): pass

    label("Function_32_42F0")

    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)

    ChrTalk(
        0x1B,
        (
            "...As expected, they\x01",
            "planned to escape on the\x01",
            "train...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "...Hmph, how foolish...\x01",
            "To think they can escape\x01",
            "us...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)
    OP_4C(0x1C, 0xFF)
    Return()

    # Function_32_42F0 end

    def Function_33_4379(): pass

    label("Function_33_4379")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43C0")
    FadeToDark(500, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12400.itp")
    Jump("loc_43C5")

    label("loc_43C0")

    Fade(500)

    label("loc_43C5")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4469")
    FadeToBright(500, 0)

    label("loc_4469")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AE5")

    NpcTalk(
        0x18,
        "Large Man in Black",
        "#12400F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305F(Hey Lloyd. I'm not\x01",
            "getting a real good vibe\x01",
            "from this guy.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(Don't tell me he's the\x01",
            "client...)\x02\x03",
            "#00000FExcuse us. We're from\x01",
            "the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x18,
        "Large Man in Black",
        (
            "#12404FI've been waiting. Thank\x01",
            "you for coming.\x02",
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
            "Mueller's the name. I'm an Imperial\x01",
            "music manager.\x02\x03",
            "Pleased to make your acquaintance.\x02",
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
            "#6P#00006FA music manager, you\x01",
            "say? (He doesn't look\x01",
            "the part at all...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101F(If pushed, I'd say he\x01",
            "seems like a bodyguard.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105F(I feel like we heard a\x01",
            "similar name before...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#12405F...Is something wrong?\x02",
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
            "#00000FU-Umm... Then, could you\x01",
            "please explain the\x01",
            "details of your request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FA "musician" has gone\x01",
            "missing, if I'm not\x01",
            "mistaken.\x02\x03",
            "#10302FI presume you are their\x01",
            "manager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FYes, exactly.\x02\x03",
            "We came to Crossbell on\x01",
            "tour, but...\x02\x03",
            "#12406FThe moment I took my eyes\x01",
            "off him, we got\x01",
            "separated.\x02\x03",
            "#12400FI'm in a bind, searching\x01",
            "aimlessly through this\x01",
            "unfamiliar city, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FThat seems difficult...\x01",
            "Crossbell City is quite\x01",
            "large, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12401FYeah, that's also\x01",
            "true... That's a bit of\x01",
            "a problem, too.\x02\x03",
            "#12400FCan you begin the search\x01",
            "immediately?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x76, 0x1, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Jump("loc_4B64")

    label("loc_4AE5")


    ChrTalk(
        0x18,
        (
            "#12400FI'd like you to search\x01",
            "within the city for the\x01",
            ""Musician" who went missing.\x02\x03",
            "Can you begin the search\x01",
            "immediately?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B64")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB6")
    Call(0, 34)
    Jump("loc_4CB8")

    label("loc_4BB6")


    ChrTalk(
        0x101,
        (
            "#6P#00006FUmm... I'm terribly\x01",
            "sorry.\x02\x03",
            "We're currently busy\x01",
            "with other things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12405FHm... Too bad then.\x02\x03",
            "#12400FIt would be a big help\x01",
            "if you'd speak with me\x01",
            "again once you're free.\x02\x03",
            "After all, I'm in a\x01",
            "hurry too. Please, I'm\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x156, 1)

    label("loc_4CB8")

    SetChrPos(0x0, 17460, 0, -4190, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x18, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_33_4379 end

    def Function_34_4CDA(): pass

    label("Function_34_4CDA")


    ChrTalk(
        0x101,
        (
            "#6P#00000FUnderstood. Please,\x01",
            "leave it to us.\x02\x03",
            "#00000FThen, can we ask you\x01",
            "about the "musician"\x01",
            "we'll be searching for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FHmm, very well.\x02\x03",
            "His name is... Olivier\x01",
            "Lenheim.\x02\x03",
            "20 years old, blond hair.\x01",
            "Wears a white coat, and\x01",
            "carries a lute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FHmm. If he's carrying\x01",
            "his instrument with him,\x01",
            "he's sure to stand out.\x02\x03",
            "#10300FI bet finding him won't\x01",
            "be that hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FWell, if all I had to do was find\x01",
            "him and drag him back here, it\x01",
            "wouldn't be too bad, but...\x02\x03",
            "#12406FOlivier has a slight...\x01",
            "personality problem.\x02\x03",
            "Even if unbidden, he sticks his\x01",
            "nose in other people's trouble,\x01",
            "and it creates even more trouble.\x02\x03",
            "#12400FYou could honestly say he's a\x01",
            "troublesome character.\x02",
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
        "#6P#00105FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FI'd love if you could find him quickly\x01",
            "so as not to impede our tour, but...\x01",
            "that might be asking a bit much.\x02\x03",
            "#12406FIt'd be a great help if you could at\x01",
            "least catch him before he makes too\x01",
            "much of a fool of himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FThough you're his manager, you\x01",
            "sure have a certain way of\x01",
            "speaking about him, don't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FW-Well, I have a basic\x01",
            "idea of how he is, at\x01",
            "least.\x02\x03",
            "#00000FFinally, do you have an\x01",
            "idea where he might have\x01",
            "gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12405FRight, if I had to say...\x02\x03",
            "#12400FHe tends to like shady or\x01",
            "lively places.\x02\x03",
            "#12406FHe's a gourmet, so it's\x01",
            "possible he's at a\x01",
            "restaurant somewhere, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FWell, they're all places\x01",
            "where trouble is likely\x01",
            "to occur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FIf that's the case, then Downtown,\x01",
            "Entertainment District and Back Street\x01",
            "are the places that come to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12404FYeah, I think you guys are on the\x01",
            "right track.\x02\x03",
            "#12400FActually, I just finished searching\x01",
            "Entertainment District. You should be\x01",
            "able to exclude it from your search.\x02\x03",
            "#12406FHe'll likely avoid places where I'm\x01",
            "likely to come search for him, so you\x01",
            "should avoid places like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FI-I see...\x02\x03",
            "#00100FSpeaking of lively places,\x01",
            "maybe we can add Waterfront\x01",
            "Area to that list for today.\x02\x03",
            "#00100FI think they're having a\x01",
            "Mishy tour event in\x01",
            "Waterfront Park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FHmm... I suppose that's\x01",
            "all for the places he\x01",
            "might have gone.\x02\x03",
            "#12406FSorry. I would have liked\x01",
            "to provide you with a\x01",
            "little more info, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FNo, that was helpful.\x02\x03",
            "#00000FLet's get to searching,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12400FPlease, I'm counting on you.\x02\x03",
            "If you're having trouble getting\x01",
            "him to come with you, I don't\x01",
            "mind if you use a little force.\x02",
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
            "#6P#00006FU-Understood... (Just\x01",
            "what kind of relationship\x01",
            "do they have?)\x02",
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
            "Quest [Search for\x01",
            "Musician]\x07\x00",
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

    # Function_34_4CDA end

    def Function_35_57EA(): pass

    label("Function_35_57EA")

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

    def lambda_58AC():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58AC)
    Sleep(50)

    def lambda_58C9():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58C9)
    Sleep(50)

    def lambda_58E6():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_58E6)
    Sleep(50)

    def lambda_5903():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5903)
    Sleep(50)

    def lambda_5920():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5920)
    Sleep(50)

    def lambda_593D():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_593D)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#00000FWe're here. Crossbell\x01",
            "Station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThe station inspector\x01",
            "sent a support request,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. Let's ask him\x01",
            "about it.\x02",
        )
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

    # Function_35_57EA end

    def Function_36_5A32(): pass

    label("Function_36_5A32")

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
            "Oh, could you all be the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. We're here to ask\x01",
            "about your support\x01",
            "request.\x02\x03",
            "You're the Republican\x01",
            "inspections officer,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Indeed. I am Inspector\x01",
            "Marlowe. I transferred here\x01",
            "from the Republican army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'd like to explain the job\x01",
            "immediately. You're accepting\x01",
            "my request, correct?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    EventEnd(0x5)
    Return()

    # Function_36_5A32 end

    def Function_37_5C42(): pass

    label("Function_37_5C42")

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
            "Oh, it's you guys.\x01",
            "You're accepting my\x01",
            "request, correct?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    EventEnd(0x5)
    Return()

    # Function_37_5C42 end

    def Function_38_5D41(): pass

    label("Function_38_5D41")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept\x01",      # 0
            "Refuse\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DDC")

    ChrTalk(
        0x101,
        "#00000FYes, we accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "That's great. Then allow\x01",
            "me to explain.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 39)
    Jump("loc_5EF3")

    label("loc_5DDC")


    ChrTalk(
        0x101,
        (
            "#00003FSorry, our hands are\x01",
            "full with other work\x01",
            "right now...\x02\x03",
            "Can we ask you again\x01",
            "later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Hmm. Well if it's not\x01",
            "for too long, I can\x01",
            "accomodate. However...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "As you can see, I'm busy\x01",
            "too. Please return as\x01",
            "soon as you can.\x02",
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

    label("loc_5EF3")

    Return()

    # Function_38_5D41 end

    def Function_39_5EF4(): pass

    label("Function_39_5EF4")


    ChrTalk(
        0x19,
        (
            "What I'd like you all to\x01",
            "do is the following:\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'd like your help with\x01",
            "inspection of the\x01",
            "Republic-bound train.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_608F")

    ChrTalk(
        0x101,
        (
            "#00005FA train inspection, is it?\x02\x03",
            "#00000FWe helped an Imperial train\x01",
            "inspector once before, so we\x01",
            "know how it's done.\x02\x03",
            "We're checking to see if\x01",
            "there's suspicious persons or\x01",
            "contraband on board, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Precisely. Since you\x01",
            "have some experience,\x01",
            "this'll be quick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6151")

    label("loc_608F")


    ChrTalk(
        0x101,
        (
            "#00003FAn inspection, meaning...\x02\x03",
            "#00000FWe're to check to see if\x01",
            "there's suspicious persons or\x01",
            "contraband on board, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Precisely. It's helpful\x01",
            "that you understand\x01",
            "things quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6151")


    ChrTalk(
        0x19,
        (
            "After all, due to the trade\x01",
            "conference, security has been\x01",
            "increased all over the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "In addition to stricter\x01",
            "checking than usual, we're also\x01",
            "cooperating with the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "The current situation is such that\x01",
            "no matter how many inspectors we\x01",
            "have, it's not enough.\x02",
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
            "...Attention passengers. The\x01",
            "next train to the Republic is\x01",
            "now arriving on platform No. 1.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please watch your step\x01",
            "and hurry to the\x01",
            "platform.\x07\x00\x02",
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
            "It seems our train will\x01",
            "be here very soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'll give you the\x01",
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
            "Quest [Republic\x01",
            "Inspection Assistance]\x07\x00\x01",
            "started!\x02",
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

    # Function_39_5EF4 end

    def Function_40_6420(): pass

    label("Function_40_6420")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 4)), scpexpr(EXPR_END)), "loc_6655")

    ChrTalk(
        0x101,
        (
            "#5P#00006FThe doors were locked\x01",
            "before, but...\x02\x03",
            "#00013FIt appears that Miss\x01",
            "Kilika and Captain\x01",
            "Lechter unlocked them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6601")

    ChrTalk(
        0x10A,
        (
            "#00601F#6PHmph, it's true it's an\x01",
            "emergency situation, doing\x01",
            "whatever they want is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6601")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6655")

    ChrTalk(
        0x109,
        (
            "#10108F#6PI can't say I approve\x01",
            "since it's illegal,\x01",
            "however...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6655")


    ChrTalk(
        0x104,
        (
            "#6P#00306FAaanyway, no one's here,\x01",
            "huh.\x02\x03",
            "#00301FCan't be helped, with\x01",
            "the transcontinental\x01",
            "railway stopped.\x02",
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
            "#6P#00200FKilika and Lechter are\x01",
            "on the train on platform\x01",
            "No. 3, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FYeah... Let's head down\x01",
            "to the platform.\x02",
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

    # Function_40_6420 end

    def Function_41_680E(): pass

    label("Function_41_680E")

    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(900)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(600)

    def lambda_6827():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6827)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_41_680E end

    def Function_42_6844(): pass

    label("Function_42_6844")

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
        "...Ah, you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Thank goodness, you saw\x01",
            "the request and came for\x01",
            "it, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FGood day to you, Mr.\x01",
            "Raymond.\x02\x03",
            "#00005F...Oh, are you alone? I\x01",
            "don't see Inspector\x01",
            "Donovan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Yes, something happened\x01",
            "and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Can I briefly explain\x01",
            "the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FPlease do.\x02\x03",
            "#00101FBased on the request, it\x01",
            "seems you're chasing that\x01",
            "fake brand trader again?\x02",
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
            "Because of legal reforms enacted by the new\x01",
            "mayor, it was decided to carry out enforcement\x01",
            "action against fake brand traders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Even Section Two has\x01",
            "strengthened its\x01",
            "enforcement efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "While doing so, that\x01",
            "fake brand trader\x01",
            "entered Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Thanks to persistent stakeouts,\x01",
            "we finally succeeded in\x01",
            "locating their exchange site.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FThe fake brand trader... Umm,\x01",
            "she was some passenger who\x01",
            "came via Tangram Gate, right?\x02\x03",
            "#10105FBy the way, in the end, what\x01",
            "kind of person was she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh right, you gave us a\x01",
            "hand guiding the\x01",
            "passengers.\x02\x03",
            "#00003FHmm, let's see, that\x01",
            "person was...\x02",
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
        "#00106FVery loud.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FQuick-footed like a\x01",
            "sprinter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FTo summarize, "one hell\x01",
            "of a person", I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x109,
        "#10105FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHehe, she seems interesting,\x01",
            "so I'd definitely like to\x01",
            "meet her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F...Well, in any case,\x01",
            "weren't you amazin'!?\x02\x03",
            "To be able to catch that\x01",
            "old lady!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Yes, well... Everything\x01",
            "went fine up to that\x01",
            "point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "But after that, in the end, she\x01",
            "managed to run away. ...And at a\x01",
            "frightening speed I might add.\x02",
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
        (
            "#00206FThat old lady never\x01",
            "learns...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FAnd so... the fake brand\x01",
            "trader is in this\x01",
            "station, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Yeah, exactly! I knew\x01",
            "you were quick-witted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "It appears she plans to\x01",
            "flee to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Haha, I guess she's\x01",
            "thinking that she's lost\x01",
            "the police completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "When I looked at platform No.\x01",
            "2, she seemed to be calmly\x01",
            "waiting for the train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThere's still time until the\x01",
            "Empire-bound train arrives. It'll\x01",
            "be the perfect chance to catch her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F...Hm? But, if\x01",
            "everything's all set...\x02\x03",
            "#00303FWe have hardly anything\x01",
            "to do, right?\x02",
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
            "Since Inspector Donovan\x01",
            "is busy, I was entrusted\x01",
            "with this case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "However... I just don't have\x01",
            "confidence I'll be able to catch\x01",
            "that fake brand trader alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FH-Hmm. Setting aside whether\x01",
            "you're confident or not... It's a\x01",
            "fact that you're shorthanded.\x02\x03",
            "#00001FIn this big train station, if you\x01",
            "don't surround her properly it's\x01",
            "very possible she'll escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I know, right? That's\x01",
            "why I asked for your\x01",
            "support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I'd like to ask you to act in\x01",
            "a support role and arrest the\x01",
            "fake brand trader with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "And, to stand guard and make\x01",
            "sure the fake brand trader\x01",
            "doesn't leave the station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I was thinking you all have already\x01",
            "caught the fake brand trader once.\x01",
            "Well, will you help me out?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x0)
    Call(0, 44)
    EventEnd(0x5)
    Return()

    # Function_42_6844 end

    def Function_43_7551(): pass

    label("Function_43_7551")

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
            "I'd like to ask you to act in\x01",
            "a support role and arrest the\x01",
            "fake brand trader with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "And, to stand guard and make\x01",
            "sure the fake brand trader\x01",
            "doesn't leave the station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I was thinking you all have already\x01",
            "caught the fake brand trader once.\x01",
            "Well, will you help me out?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 44)
    EventEnd(0x5)
    Return()

    # Function_43_7551 end

    def Function_44_7736(): pass

    label("Function_44_7736")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7785")
    Jump("loc_78A8")

    label("loc_7785")


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
            "Hmm, I see. It can't be\x01",
            "helped then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Then, I'll wait here a\x01",
            "little longer for a good\x01",
            "chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "If you're free, it'd be\x01",
            "a big help if you could\x01",
            "give me a hand.\x02",
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

    label("loc_78A8")


    ChrTalk(
        0x101,
        (
            "#00000F...I see, understood.\x01",
            "We'd love to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Ohh, thank you! I'm in\x01",
            "your debt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Then... First of all, let's\x01",
            "decide the group that will arrest\x01",
            "the fake brand trader with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Who's going to come with\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FLet's see... How should\x01",
            "we divide?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FBeing a detective, I\x01",
            "think you should\x01",
            "accompany him, Lloyd.\x02\x03",
            "#00211F...I'd be slightly\x01",
            "worried if it was just\x01",
            "Mr. Raymond.\x02",
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
            "...Is what I want to\x01",
            "say, but that's a more\x01",
            "reliable way for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012FU-Umm... So we've got two\x01",
            "detectives for the time\x01",
            "being.\x02\x03",
            "#00000FLet's have one more person\x01",
            "support us, and the remaining\x01",
            "four will secure the station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThen... Who are you\x01",
            "taking with you?\x02",
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
            "Bring Elie\x01",       # 0
            "Bring Tio\x01",        # 1
            "Bring Randy\x01",      # 2
            "Bring Noｱl\x01",      # 3
            "Bring Wazy\x01",       # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C68")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#00000FElie, you're with me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00100FYes, understood.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x1)
    Jump("loc_7E0A")

    label("loc_7C68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CD2")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#00000FTio, you're with me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#00200FRoger that.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x2)
    Jump("loc_7E0A")

    label("loc_7CD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D3E")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00000FRandy, you're with me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#00309FSure thing.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x3)
    Jump("loc_7E0A")

    label("loc_7D3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DA7")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        "#00000FNoｱl, you're with me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#10100FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x4)
    Jump("loc_7E0A")

    label("loc_7DA7")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#00000FWazy, you're with me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        "#10304FAs you command, leader.\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x5)

    label("loc_7E0A")

    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00003FEveryone else, survey\x01",
            "the station entrances\x01",
            "and exits.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7E59():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E59)
    Sleep(50)

    def lambda_7E69():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7E69)
    Sleep(50)

    def lambda_7E79():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E79)
    Sleep(50)

    def lambda_7E89():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E89)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00001FBecause it's that old lady we're\x01",
            "talking about, anything could\x01",
            "happen. Be ready for anything.\x02",
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

    def lambda_7F89():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7F89)

    def lambda_7F96():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7F96)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)

    ChrTalk(
        0x1B,
        (
            "...I can't seem to spot\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "They might have boarded\x01",
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
            "Quest [Pursuing the Fake\x01",
            "Brand Trader]\x07\x00",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_813C")
    AddParty(0x1, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 3)
    Jump("loc_8194")

    label("loc_813C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8157")
    AddParty(0x2, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 4)
    Jump("loc_8194")

    label("loc_8157")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8172")
    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 5)
    Jump("loc_8194")

    label("loc_8172")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_818D")
    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 6)
    Jump("loc_8194")

    label("loc_818D")

    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 7)

    label("loc_8194")

    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_44_7736 end

    def Function_45_81B2(): pass

    label("Function_45_81B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_82CA")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_81F5"),
        (1, "loc_820F"),
        (2, "loc_8229"),
        (3, "loc_8243"),
        (4, "loc_825D"),
        (5, "loc_8277"),
        (6, "loc_8291"),
        (SWITCH_DEFAULT, "loc_82AB"),
    )


    label("loc_81F5")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_82C5")

    label("loc_820F")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_82C5")

    label("loc_8229")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_82C5")

    label("loc_8243")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_82C5")

    label("loc_825D")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_82C5")

    label("loc_8277")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_82C5")

    label("loc_8291")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_82C5")

    label("loc_82AB")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_82C5")

    label("loc_82C5")

    Jump("Function_45_81B2")

    label("loc_82CA")

    Return()

    # Function_45_81B2 end

    def Function_46_82CB(): pass

    label("Function_46_82CB")

    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Return()

    # Function_46_82CB end

    def Function_47_82EA(): pass

    label("Function_47_82EA")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    Return()

    # Function_47_82EA end

    def Function_48_8309(): pass

    label("Function_48_8309")

    Sleep(600)
    OP_95(0xFE, 19770, 30, 7340, 2000, 0x0)
    OP_95(0xFE, 23810, 0, 7440, 2000, 0x0)
    Return()

    # Function_48_8309 end

    def Function_49_8335(): pass

    label("Function_49_8335")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 19710, 30, 8420, 2000, 0x0)
    Sound(100, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(500)
    OP_95(0xFE, 23490, 0, 8520, 2000, 0x0)
    Return()

    # Function_49_8335 end

    def Function_50_837E(): pass

    label("Function_50_837E")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 3)), scpexpr(EXPR_END)), "loc_85C9")

    ChrTalk(
        0x104,
        (
            "#00306FI was surprised when I\x01",
            "heard you guys went to\x01",
            "the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FSo that's how it turned\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, I'm sorry for not\x01",
            "even contacting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, the fake brand trader's\x01",
            "been caught for now and\x01",
            "everything turned out all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha. Let's call it\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BDB")

    label("loc_85C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 4)), scpexpr(EXPR_END)), "loc_8740")

    ChrTalk(
        0x102,
        (
            "#00106FI was surprised when I\x01",
            "heard you went to the\x01",
            "Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh man, to think things\x01",
            "turned out like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWe should've at least\x01",
            "contacted you. We're\x01",
            "sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, the fake brand trader's\x01",
            "been caught for now and\x01",
            "everything turned out all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha. Let's call it\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BDB")

    label("loc_8740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 5)), scpexpr(EXPR_END)), "loc_88D8")

    ChrTalk(
        0x109,
        (
            "#10106FI was surprised when I\x01",
            "heard you guys went to\x01",
            "the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh man, who could've\x01",
            "thought things would\x01",
            "turn out like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, sorry, sorry. It\x01",
            "was an emergency\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, the fake brand trader's\x01",
            "been caught for now and\x01",
            "everything turned out all right.\x02",
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
        (
            "#00204FWell, let's say it\x01",
            "turned out fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BDB")

    label("loc_88D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 6)), scpexpr(EXPR_END)), "loc_8A63")

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
            "#00300FOh man, to think things\x01",
            "turned out like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha... Sorry, we\x01",
            "didn't even contact you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, the fake brand trader's\x01",
            "been caught for now and\x01",
            "everything turned out all right.\x02",
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
        (
            "#00204FWell, let's say it\x01",
            "turned out fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BDB")

    label("loc_8A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 7)), scpexpr(EXPR_END)), "loc_8BDB")

    ChrTalk(
        0x109,
        (
            "#10106FI was surprised when I\x01",
            "heard you guys went to\x01",
            "the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh man, to think things\x01",
            "turned out like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHehe. It was an\x01",
            "emergency, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, the fake brand trader's\x01",
            "been caught for now and\x01",
            "everything turned out all right.\x02",
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
        (
            "#00204FWell, let's say it\x01",
            "turned out fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BDB")


    ChrTalk(
        0x1A,
        (
            "Well then, I have to\x01",
            "make a report at Section\x01",
            "Two...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "I'll excuse myself here.\x02",
    )

    CloseMessageWindow()

    def lambda_8C38():

        label("loc_8C38")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8C38")

    QueueWorkItem2(0x103, 1, lambda_8C38)

    def lambda_8C4A():

        label("loc_8C4A")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8C4A")

    QueueWorkItem2(0x104, 1, lambda_8C4A)

    def lambda_8C5C():

        label("loc_8C5C")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8C5C")

    QueueWorkItem2(0x109, 1, lambda_8C5C)

    def lambda_8C6E():

        label("loc_8C6E")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8C6E")

    QueueWorkItem2(0x105, 1, lambda_8C6E)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 3)), scpexpr(EXPR_END)), "loc_8CC0")

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, thank you for\x01",
            "your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D96")

    label("loc_8CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 4)), scpexpr(EXPR_END)), "loc_8CF5")

    ChrTalk(
        0x103,
        (
            "#00202FThanks for your hard\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D96")

    label("loc_8CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 5)), scpexpr(EXPR_END)), "loc_8D2C")

    ChrTalk(
        0x104,
        (
            "#00309FHaha, thanks for\x01",
            "everythin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D96")

    label("loc_8D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 6)), scpexpr(EXPR_END)), "loc_8D67")

    ChrTalk(
        0x109,
        (
            "#10109FHaha, thanks for your\x01",
            "hard work!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D96")

    label("loc_8D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 7)), scpexpr(EXPR_END)), "loc_8D96")

    ChrTalk(
        0x105,
        (
            "#10302FHehe, that was good\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D96")


    ChrTalk(
        0x1A,
        (
            "Well, you all helped me\x01",
            "until the very end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "If I'd been alone, I\x01",
            "never would've managed\x01",
            "to arrest that old lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Thanks so much for your\x01",
            "help today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FDon't mention it.\x02\x03",
            "#00000FPlease, contact the\x01",
            "Support Section if you\x01",
            "ever need our help again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Yeah, I'll be counting\x01",
            "on you!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x10E, 0x1F4)

    def lambda_8ED5():
        OP_95(0xFE, 3980, 30, 220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8ED5)
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
            "Quest [Pursuing the Fake\x01",
            "Brand Trader]\x07\x00",
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

    # Function_50_837E end

    def Function_51_8FA1(): pass

    label("Function_51_8FA1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "←Calvard-Bound - Platform Number 1\x01",
            "   Altair City, Calvard   35 minutes\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_51_8FA1 end

    def Function_52_9022(): pass

    label("Function_52_9022")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Erebonia-Bound - Platform Number 2→\x01",
            "    Garrelia Fortress, Erebonia   32 minutes\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_52_9022 end

    def Function_53_90AC(): pass

    label("Function_53_90AC")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a train schedule\x01",
            "for the Crossbell State\x01",
            "region.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_53_90AC end

    def Function_54_90F5(): pass

    label("Function_54_90F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_910C")
    Call(0, 56)
    Return()

    label("loc_910C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※※ Inspector's Office ※※\x01",
            "Authorized Personnel Only\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_54_90F5 end

    def Function_55_917B(): pass

    label("Function_55_917B")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Crossbell State route map.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_55_917B end

    def Function_56_91B0(): pass

    label("Function_56_91B0")

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
            "#12P#00200F...As expected, it seems\x01",
            "there's no one inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FRail service is suspended and\x01",
            "the Imperial and Republican\x01",
            "inspectors have been recalled.\x02\x03",
            "#00100FThe station attendants are\x01",
            "probably sheltering elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FWell, we've no reason\x01",
            "stick around a place\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FLet's go meet Kilika and\x01",
            "the others.\x02\x03",
            "We should be able to get\x01",
            "to the platform from the\x01",
            "lower entrance.\x02",
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

    # Function_56_91B0 end

    SaveToFile()

Try(main)
