from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0180.bin",                # FileName
        "c0180",                    # MapName
        "c0180",                    # Location
        0x0005,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0180",                  # 0
        "Janetta",             # 1
        "Eugene",             # 2
        "Theodore",             # 3
        "Chiluru",                 # 4
        "corona",                 # 5
        "Lima",                   # 6
        "Marsun",               # 7
        "tourist",                 # 8
        "tourist",                 # 9
        "Citizen",                   # 10
        "girl",                 # 11
        "tourist",                 # 12
        "tourist",                 # 13
        "Citizen",                   # 14
        "Citizen",                   # 15
        "tourist",                 # 16
        "tourist",                 # 17
        "Citizen",                   # 18
        "Citizen",                   # 19
        "tourist",                 # 20
        "tourist",                 # 21
        "Citizen",                   # 22
        "boy",                 # 23
        "tourist",                 # 24
        "Donovan",           # 25
        "Citizen",                   # 26
        "Citizen",                   # 27
        "Citizen",                   # 28
        "Citizen",                   # 29
        "Ryu",                 # 30
        "Henry",                 # 31
        "peach",                   # 32
        "Singh",                   # 33
        "Black moon",                   # 34
        "Suzuku",                 # 35
        "Keya",                 # 36
        "Zeit",               # 37
        "Tsao",                 # 38
        "Rector",               # 39
        "Zile",                 # 40
        "Arseille",             # 41
        "SE control",                 # 42
    ))

    AddCharChip((
        "chr/ch26600.itc",                   # 00
        "chr/ch28700.itc",                   # 01
        "chr/ch28800.itc",                   # 02
        "chr/ch22700.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch26200.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch33100.itc",                   # 07
        "chr/ch33200.itc",                   # 08
        "chr/ch20100.itc",                   # 09
        "chr/ch22300.itc",                   # 0A
        "chr/ch22000.itc",                   # 0B
        "chr/ch34300.itc",                   # 0C
        "chr/ch24500.itc",                   # 0D
        "chr/ch22100.itc",                   # 0E
        "chr/ch33000.itc",                   # 0F
        "chr/ch33300.itc",                   # 10
        "chr/ch20400.itc",                   # 11
        "chr/ch21300.itc",                   # 12
        "chr/ch20000.itc",                   # 13
        "chr/ch20102.itc",                   # 14
        "chr/ch21102.itc",                   # 15
        "chr/ch21400.itc",                   # 16
        "chr/ch33202.itc",                   # 17
        "chr/ch48800.itc",                   # 18
        "chr/ch30300.itc",                   # 19
        "chr/ch21100.itc",                   # 1A
    ))

    DeclNpc(11409,   4294967107, 4294960746, 180,  385,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294957956, 4294967096, 4294963356, 270,  389,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294958656, 4294967096, 4294963326, 90,   389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294953656, 4294967096, 6610,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294961606, 4294967096, 3660,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294960606, 4294967096, 3660,    0,    389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294959606, 4294967096, 3660,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294952746, 4294967096, 4294962516, 270,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294951517, 4294967246, 4294962516, 90,   389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294951517, 4294967246, 4294962516, 90,   389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294952746, 4294967096, 4294962516, 270,  389,  0x0, 0,   10,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294960577, 4294967096, 5000,    0,    389,  0x0, 0,   11,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294961706, 4294967096, 5000,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294960296, 4294967096, 4294963016, 270,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294959737, 4294967096, 4294964296, 225,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4294956637, 4294967096, 4294964517, 135,  389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(4294956317, 4294967096, 4294963386, 90,   389,  0x0, 0,   16,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4294956677, 4294967096, 4294966226, 0,    389,  0x0, 0,   17,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4294957677, 4294967096, 4294966226, 0,    389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4294960577, 4294967096, 5000,    0,    389,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4294961706, 4294967096, 5000,    0,    389,  0x0, 0,   9,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(4294951517, 4294967246, 4294962516, 90,   389,  0x0, 0,   26,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(4294952746, 4294967096, 4294961976, 270,  385,  0x0, 0,   22,  0,   0,   1,   0,   28,  255,  0)
    DeclNpc(4294961777, 4294967096, 3869,    15,   389,  0x0, 0,   24,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(3809,    4294967096, 7099,    0,    389,  0x0, 0,   25,  0,   0,   0,   0,   12,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1664, 0)                                       # 0

    ScpFunction((
        "Function_0_680",          # 00, 0
        "Function_1_730",          # 01, 1
        "Function_2_75B",          # 02, 2
        "Function_3_777",          # 03, 3
        "Function_4_A96",          # 04, 4
        "Function_5_D9B",          # 05, 5
        "Function_6_1210",         # 06, 6
        "Function_7_12FE",         # 07, 7
        "Function_8_1373",         # 08, 8
        "Function_9_13CD",         # 09, 9
        "Function_10_143C",        # 0A, 10
        "Function_11_1488",        # 0B, 11
        "Function_12_14EB",        # 0C, 12
        "Function_13_1C13",        # 0D, 13
        "Function_14_1C62",        # 0E, 14
        "Function_15_1CBC",        # 0F, 15
        "Function_16_1D3D",        # 10, 16
        "Function_17_1D9F",        # 11, 17
        "Function_18_1DF5",        # 12, 18
        "Function_19_1E6E",        # 13, 19
        "Function_20_1EFD",        # 14, 20
        "Function_21_1F8D",        # 15, 21
        "Function_22_2013",        # 16, 22
        "Function_23_2070",        # 17, 23
        "Function_24_20F1",        # 18, 24
        "Function_25_215E",        # 19, 25
        "Function_26_21D3",        # 1A, 26
        "Function_27_2223",        # 1B, 27
        "Function_28_267A",        # 1C, 28
        "Function_29_2A42",        # 1D, 29
        "Function_30_2B30",        # 1E, 30
        "Function_31_2BE4",        # 1F, 31
        "Function_32_2F75",        # 20, 32
        "Function_33_3019",        # 21, 33
        "Function_34_3116",        # 22, 34
        "Function_35_314E",        # 23, 35
        "Function_36_317A",        # 24, 36
        "Function_37_31B7",        # 25, 37
        "Function_38_31E8",        # 26, 38
        "Function_39_3BF0",        # 27, 39
        "Function_40_5212",        # 28, 40
        "Function_41_52E8",        # 29, 41
        "Function_42_533D",        # 2A, 42
        "Function_43_5392",        # 2B, 43
        "Function_44_53E7",        # 2C, 44
        "Function_45_543C",        # 2D, 45
        "Function_46_5486",        # 2E, 46
        "Function_47_6591",        # 2F, 47
        "Function_48_65D5",        # 30, 48
        "Function_49_6619",        # 31, 49
        "Function_50_665D",        # 32, 50
        "Function_51_66A1",        # 33, 51
        "Function_52_74C2",        # 34, 52
        "Function_53_750D",        # 35, 53
        "Function_54_7558",        # 36, 54
        "Function_55_75A3",        # 37, 55
        "Function_56_75EE",        # 38, 56
        "Function_57_7639",        # 39, 57
    ))


    def Function_0_680(): pass

    label("Function_0_680")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6B8"),
        (1, "loc_6C4"),
        (2, "loc_6D0"),
        (3, "loc_6DC"),
        (4, "loc_6E8"),
        (5, "loc_6F4"),
        (6, "loc_700"),
        (SWITCH_DEFAULT, "loc_70C"),
    )


    label("loc_6B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_700")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_70C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_718")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_72F")

    Return()

    # Function_0_680 end

    def Function_1_730(): pass

    label("Function_1_730")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75A")
    OP_94(0xFE, 0xFFFFC4AA, 0xFFFFEFCA, 0xFFFFCD24, 0xFFFFE46C, 0x3E8)
    Sleep(300)
    Jump("Function_1_730")

    label("loc_75A")

    Return()

    # Function_1_730 end

    def Function_2_75B(): pass

    label("Function_2_75B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_776")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_2_75B")

    label("loc_776")

    Return()

    # Function_2_75B end

    def Function_3_777(): pass

    label("Function_3_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B7")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1D, -6820, -200, -3460, 105)
    SetChrPos(0x1E, -7510, -200, -4550, 105)
    BeginChrThread(0x1E, 0, 0, 0)
    Jump("loc_9E4")

    label("loc_7B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7C5")
    Jump("loc_9E4")

    label("loc_7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7EE")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_7EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_817")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_840")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_853")
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_9E4")

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_87C")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_87C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8A5")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_8A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8D8")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_8D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8FF")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_9E4")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_90D")
    Jump("loc_9E4")

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_966")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_9E4")

    label("loc_966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9A8")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x14)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_9E4")

    label("loc_9A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9BB")
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_9E4")

    label("loc_9BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9E4")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x17)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)

    label("loc_9E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_9F8")
    ClearScenarioFlags(0x22, 0)
    Event(0, 30)
    Jump("loc_A2F")

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_A0C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 31)
    Jump("loc_A2F")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_A20")
    ClearScenarioFlags(0x22, 2)
    Event(0, 38)
    Jump("loc_A2F")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_A2F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 33)

    label("loc_A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A40")
    Event(0, 39)

    label("loc_A40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6D")
    Event(0, 51)
    Jump("loc_A95")

    label("loc_A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A95")
    Event(0, 46)

    label("loc_A95")

    Return()

    # Function_3_777 end

    def Function_4_A96(): pass

    label("Function_4_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B89")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x168, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C67")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x168, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CF8")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x46, 0x1A4, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D35")
    SetMapObjFrame(0xFF, "ibc_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "heiyue", 0x0, 0x1)
    Jump("loc_D64")

    label("loc_D35")

    SetMapObjFrame(0xFF, "ibc_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "heiyue", 0x1, 0x1)

    label("loc_D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D86")
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    Jump("loc_D9A")

    label("loc_D86")

    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)

    label("loc_D9A")

    Return()

    # Function_4_A96 end

    def Function_5_D9B(): pass

    label("Function_5_D9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DAC")
    Jump("loc_120C")

    label("loc_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E69")

    ChrTalk(
        0xFE,
        (
            "Ha, Mr. Sa'zark of that night,\x01",
            "It was cool …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do such a serious look\x01",
            "\"I know what you are good\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, it was really the best time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EE1")

    label("loc_E69")


    ChrTalk(
        0xFE,
        (
            "Indeed,\x01",
            "Up to ticket of alkane shell\x01",
            "To give me a gift ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, I'm really happy.\x02",
    )

    CloseMessageWindow()

    label("loc_EE1")

    Jump("loc_120C")

    label("loc_EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EF4")
    Jump("loc_120C")

    label("loc_EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1076")

    ChrTalk(
        0xFE,
        (
            "~ Ah, I like Pearl as well\x01",
            "I want a nice boyfriend who is reliable ~.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Oh, dont, it must not be ……\x01",
            "I have to bring water to Mr. Ohana properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, I'm sorry.\x01",
            "Now I pour a lot of it from Akashi Machi!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F(Well, it was a baby baby word ……\x01",
            "This guy gets a point high. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(What is the point ……)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10BD")

    label("loc_1076")


    ChrTalk(
        0xFE,
        (
            "Uhufu, I'm sorry.\x01",
            "Pour a lot now and give it from Kamakyushi ~?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BD")

    Jump("loc_120C")

    label("loc_10C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_10D0")
    Jump("loc_120C")

    label("loc_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_120C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1192")

    ChrTalk(
        0xFE,
        (
            "Well, here is\x01",
            "The view is nice and nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, by the way, me,\x01",
            "It is not squashing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the manager to the implant\x01",
            "I was appointed a watering clerk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0xB4, 0x0)
    SetChrFlags(0xFE, 0x10)
    Jump("loc_120C")

    label("loc_1192")


    ChrTalk(
        0xFE,
        (
            "Uhufu, now bring water from Makuh.\x01",
            "Take a cup and grow up healthily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Why the baby word?\x02",
    )

    CloseMessageWindow()

    label("loc_120C")

    TalkEnd(0xFE)
    Return()

    # Function_5_D9B end

    def Function_6_1210(): pass

    label("Function_6_1210")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A1")

    ChrTalk(
        0xFE,
        (
            "Recently, every time I get back from my trip\x01",
            "Building that was approaching completion gradually … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bottom of the seat was like that.\x01",
            "Pretty awesome … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12FA")

    label("loc_12A1")


    ChrTalk(
        0xFE,
        (
            "Well, the building was seen … ….\x01",
            "I guess I should go to the next place soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "To the house … I will return next time.\x02",
    )

    CloseMessageWindow()

    label("loc_12FA")

    TalkEnd(0xFE)
    Return()

    # Function_6_1210 end

    def Function_7_12FE(): pass

    label("Function_7_12FE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well ~ but after all we are\x01",
            "The aura is out ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, Theodore.\x01",
            "All this is my calculation error.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_12FE end

    def Function_8_1373(): pass

    label("Function_8_1373")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "……\x01",
            "\"If it is in practice wearing it is not ballet.\"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I was stupid I believed you.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1373 end

    def Function_9_13CD(): pass

    label("Function_9_13CD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "For building such a splendid building\x01",
            "I thought my husband was involved ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, so much we are proud\x01",
            "There is not it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_13CD end

    def Function_10_143C(): pass

    label("Function_10_143C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Fluffy, that's what it is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh, after all\x01",
            "Daddy is amazing ♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_143C end

    def Function_11_1488(): pass

    label("Function_11_1488")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Look, see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That building, ne,\x01",
            "Daddy and power with my colleagues\x01",
            "I made it together.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1488 end

    def Function_12_14EB(): pass

    label("Function_12_14EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1698")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160C")

    ChrTalk(
        0xFE,
        "Is it a terrorist who aims at the leaders of both countries …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just this information\x01",
            "It is impossible to get caught,\x01",
            "It is certain that it became a good attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless, regarding the security shift\x01",
            "In the interview yesterday, Dudley\x01",
            "Until you follow the adjusted one … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, each person,\x01",
            "I just put a cure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1693")

    label("loc_160C")


    ChrTalk(
        0xFE,
        (
            "Regardless, regarding the security shift\x01",
            "In the interview yesterday, Dudley\x01",
            "Until you follow the adjusted one … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, each person,\x01",
            "I just put a cure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1693")

    Jump("loc_1C0F")

    label("loc_1698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1975")

    ChrTalk(
        0xFE,
        (
            "Yeah, you guys.\x01",
            "Anything to unveil security\x01",
            "I heard that you participated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How was the summit leaders looking at?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, it was truly amazing force.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FOh, what kind\x01",
            "Seriously Aura and Mon\x01",
            "I felt like I could see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed, firmly\x01",
            "You are not feeling it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what kind,\x01",
            "I also feel that kind of atmosphere\x01",
            "Of course it is important, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somewhere when actually touched by the side\x01",
            "Is not it important to be drunk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, it certainly is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FA little\x01",
            "I do not have confidence though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, well, that area also has experience\x01",
            "It gets important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, to you anyway\x01",
            "It looks like it was a good experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It pushed me into security\x01",
            "To Sergei's dude,\x01",
            "Please be grateful for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, of course.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 3)
    Jump("loc_1A27")

    label("loc_1975")


    ChrTalk(
        0xFE,
        (
            "As you felt,\x01",
            "What is the aura of the leaders?\x01",
            "Each is unique and authentic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anyway I want to say,\x01",
            "To oppose such a great deal\x01",
            "It was also important that not being swallowed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A27")

    Jump("loc_1C0F")

    label("loc_1A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1C0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B87")

    ChrTalk(
        0xFE,
        (
            "You, you guys.\x01",
            "Has anything changed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, well\x01",
            "There is no big deal.\x02\x03",
            "Is the policeman directing vigilance here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, to get in touch with each direction\x01",
            "This place is convenient for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, for the time being\x01",
            "It does not change another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You guys continue the activities of the military.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, that's OK.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C0F")

    label("loc_1B87")


    ChrTalk(
        0xFE,
        (
            "But, well, the population of various places\x01",
            "It is not as good as a memorial day but it is saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is an unveiling ceremony tomorrow\x01",
            "I wish it would not be like today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0F")

    TalkEnd(0xFE)
    Return()

    # Function_12_14EB end

    def Function_13_1C13(): pass

    label("Function_13_1C13")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It is on the roof of a department store,\x01",
            "There is no such a good spot\x01",
            "I did not do it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1C13 end

    def Function_14_1C62(): pass

    label("Function_14_1C62")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Wow, the wind feels good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The view is nice,\x01",
            "This is a very nice place.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1C62 end

    def Function_15_1CBC(): pass

    label("Function_15_1CBC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "By the way,\x01",
            "You know little outside the city, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, even now in Almorika village\x01",
            "I wonder if I should take you there.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1CBC end

    def Function_16_1D3D(): pass

    label("Function_16_1D3D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Fuwa, To the direction of Tokoro\x01",
            "There are lots of green colors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is there a crossbell over there too?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1D3D end

    def Function_17_1D9F(): pass

    label("Function_17_1D9F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Among them, really\x01",
            "I wonder what has become of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am enjoying the unveiling ceremony too much.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1D9F end

    def Function_18_1DF5(): pass

    label("Function_18_1DF5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "But, that covering\x01",
            "I wonder how to remove it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way, everyone from below\x01",
            "I will not pull it … …\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1DF5 end

    def Function_19_1E6E(): pass

    label("Function_19_1E6E")

    TalkBegin(0xFE)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xFE,
        "#4SCare!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way to two people in such a place\x01",
            "I can not wait to see you! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, that, please sign! It is!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1E6E end

    def Function_20_1EFD(): pass

    label("Function_20_1EFD")

    TalkBegin(0xFE)
    TurnDirection(0x16, 0x15, 0)

    ChrTalk(
        0xFE,
        (
            "Wait a minute.\x01",
            "If you become so loud\x01",
            "It is troublesome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To get a sign on it,\x01",
            "I am the destination!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0xE1, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_1EFD end

    def Function_21_1F8D(): pass

    label("Function_21_1F8D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, they both look at the stage\x01",
            "I'm always a handsome guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a bit frustrating,\x01",
            "My wife will fall in love\x01",
            "You will understand.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1F8D end

    def Function_22_2013(): pass

    label("Function_22_2013")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, with Theodor like the real thing\x01",
            "Eugene in front of me ……\x01",
            "It seems to be stunned.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2013 end

    def Function_23_2070(): pass

    label("Function_23_2070")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Anything, just about to come\x01",
            "The conference's performance begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know the difficult thing,\x01",
            "I would like the mayors to do their best.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2070 end

    def Function_24_20F1(): pass

    label("Function_24_20F1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If you send cheers from here,\x01",
            "I wonder if they will reach the mayors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Frauleay, Mayor!\x01",
            "…… Anyway.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_20F1 end

    def Function_25_215E(): pass

    label("Function_25_215E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, no matter how many times you look\x01",
            "It's a nice building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is Crossbell's new landmark?\x01",
            "You said well.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_215E end

    def Function_26_21D3(): pass

    label("Function_26_21D3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hehe, look at that roof of that building\x01",
            "The scenery is wonderful, is not it?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_21D3 end

    def Function_27_2223(): pass

    label("Function_27_2223")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_226D")

    ChrTalk(
        0xFE,
        (
            "That big tree …\x01",
            "Pale light is also fantastic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_226D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_227B")
    Jump("loc_2676")

    label("loc_227B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_232C")

    ChrTalk(
        0xFE,
        (
            "President Dieter and Secretary of Defense Arios,\x01",
            "If these two people are relieved\x01",
            "You can leave the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It may be a long battle,\x01",
            "I definitely have to win independence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_232C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23CB")

    ChrTalk(
        0xFE,
        (
            "Arios says,\x01",
            "To protect the Orchis Tower\x01",
            "It seems that he was truly performing brilliantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I felt it again but this town is\x01",
            "Just as I expected that person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_23CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2483")

    ChrTalk(
        0xFE,
        (
            "It seems that the armed group suddenly appeared … …\x01",
            "It is somehow to prevent it\x01",
            "I wonder if I could not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the police and the guard\x01",
            "I have to get more firm\x01",
            "I can not sleep at ease with confidence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_2483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2491")
    Jump("loc_2676")

    label("loc_2491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2505")

    ChrTalk(
        0xFE,
        (
            "There is something accident in the direction of the highway\x01",
            "It seems there was a problem but I am worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are quite a few ambulances\x01",
            "It seems I was out … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_2505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_259E")

    ChrTalk(
        0xFE,
        (
            "Since I came to take a rest here\x01",
            "Somehow it will stay long in department stores\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you hit the wind here,\x01",
            "Shopping tiredness also blows away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2676")

    ChrTalk(
        0xFE,
        (
            "Huhu, I can see the Orkis Tower somehow\x01",
            "I feel I got used to the scenery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ten years and 20 years later,\x01",
            "I guess the cityscape will change, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Only the presence of that building,\x01",
            "It will not change as it is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2676")

    TalkEnd(0xFE)
    Return()

    # Function_27_2223 end

    def Function_28_267A(): pass

    label("Function_28_267A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26D5")

    ChrTalk(
        0xFE,
        (
            "Why\x01",
            "The big tree is floating?\x01",
            "It is full of mischievous people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_26D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_26E3")
    Jump("loc_2A3E")

    label("loc_26E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2765")

    ChrTalk(
        0xFE,
        (
            "Arios, from Yu Genki\x01",
            "You got it for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not understand well,\x01",
            "Maybe it's getting stubborn!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_2765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_27CC")

    ChrTalk(
        0xFE,
        (
            "I am Arios McRae …\x01",
            "Yu Genki!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Shakiene, spa papa para!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_27CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2837")

    ChrTalk(
        0xFE,
        (
            "Something, Mainz is better\x01",
            "I heard that it is hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess it's not easy to get bad, bad guy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_2837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2845")
    Jump("loc_2A3E")

    label("loc_2845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2905")

    ChrTalk(
        0xFE,
        (
            "Cute cars are\x01",
            "When I went through,\x01",
            "The sound sounded like a breeze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Peepeepipa,\x01",
            "It is feeling like Phu Poipu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ARE, what was it all along?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2971")

    label("loc_2905")


    ChrTalk(
        0xFE,
        (
            "Cute cars are\x01",
            "When I went through,\x01",
            "The sound sounded like a breeze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ARE, what was it all along?\x02",
    )

    CloseMessageWindow()

    label("loc_2971")

    Jump("loc_2A3E")

    label("loc_2976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_29F8")

    ChrTalk(
        0xFE,
        (
            "Farewell likes me,\x01",
            "Nanami is nothing special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even at a savory store,\x01",
            "Do not make me make it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_29F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A3E")

    ChrTalk(
        0xFE,
        (
            "Well, it is nice weather today.\x01",
            "The air of the poor is good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3E")

    TalkEnd(0xFE)
    Return()

    # Function_28_267A end

    def Function_29_2A42(): pass

    label("Function_29_2A42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2AAB")

    NpcTalk(
        0xFE,
        "Daughter",
        "Today 's rain is going to be fine in the afternoon.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Daughter",
        "Hehuu, you may also be seen with a rainbow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B2C")

    label("loc_2AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2B2C")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Huhu, how come the city of rain\x01",
            "I wonder if I will tickle my heart so much.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "A sad atmosphere\x01",
            "I am emotional and I can not afford it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B2C")

    TalkEnd(0xFE)
    Return()

    # Function_29_2A42 end

    def Function_30_2B30(): pass

    label("Function_30_2B30")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(9900, 2800, 25300, 0)
    MoveCamera(30, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(23750, 0)
    OP_68(5550, 4800, 33000, 10000)
    MoveCamera(10, -5, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(21000, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_2B30 end

    def Function_31_2BE4(): pass

    label("Function_31_2BE4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch20600.itc", 0x21)
    LoadChrToIndex("chr/ch22200.itc", 0x22)
    LoadChrToIndex("chr/ch45000.itc", 0x23)
    LoadChrToIndex("chr/ch47600.itc", 0x24)
    SoundLoad(835)
    SoundLoad(821)
    SetChrChipByIndex(0x2B, 0x1E)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2C, 0x20)
    SetChrSubChip(0x2C, 0x5)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x22)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x4)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x23)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrChipByIndex(0x29, 0x24)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrChipByIndex(0x23, 0x7)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x21, 0x8)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x24, 0xB)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0x19, 0xFF)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    BeginChrThread(0x2C, 3, 0, 0)
    SetChrPos(0x2B, -12800, -200, 6900, 225)
    SetChrPos(0x2A, -14000, -200, 6500, 135)
    SetChrPos(0x2C, -13000, -200, 4800, 0)
    SetChrPos(0x25, -10700, -200, 7100, 135)
    SetChrPos(0x26, -9500, -200, 7100, 225)
    SetChrPos(0x27, -10200, -200, 5900, 0)
    SetChrPos(0x28, -11900, -200, 4900, 135)
    SetChrPos(0x29, -11200, -200, 4100, 315)
    SetChrPos(0x23, -7200, -200, 4800, 0)
    SetChrPos(0x21, -5100, -200, 5600, 0)
    SetChrPos(0x24, -5000, -200, 4100, 0)
    SetChrPos(0x22, -3200, -200, 5000, 0)
    SetChrPos(0x8, -1800, -200, 4500, 0)
    SetChrPos(0xB, -5400, -200, 6800, 0)
    SetChrPos(0x19, -3000, -200, 6900, 0)
    SetChrPos(0x11, -8400, -200, 4900, 0)
    OP_68(-8000, 4800, 5500, 0)
    MoveCamera(12, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12500, 0)
    OP_68(-8000, 2500, 5500, 10000)
    MoveCamera(12, 5, 0, 10000)
    SetCameraDistance(12000, 10000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x2B, 3, 0, 32)
    BeginChrThread(0x2A, 3, 0, 32)
    BeginChrThread(0x25, 3, 0, 32)
    BeginChrThread(0x26, 3, 0, 32)
    BeginChrThread(0x27, 3, 0, 32)
    BeginChrThread(0x28, 3, 0, 32)
    BeginChrThread(0x23, 3, 0, 35)
    Sleep(100)
    BeginChrThread(0x21, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x24, 3, 0, 35)
    Sleep(100)
    BeginChrThread(0x22, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x8, 3, 0, 35)
    Sleep(100)
    BeginChrThread(0xB, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x19, 3, 0, 35)
    Sleep(8000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_2BE4 end

    def Function_32_2F75(): pass

    label("Function_32_2F75")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2FAD"),
        (1, "loc_2FB5"),
        (2, "loc_2FBD"),
        (3, "loc_2FC5"),
        (4, "loc_2FCD"),
        (5, "loc_2FD5"),
        (6, "loc_2FDD"),
        (SWITCH_DEFAULT, "loc_2FE5"),
    )


    label("loc_2FAD")

    Sleep(200)
    Jump("loc_2FED")

    label("loc_2FB5")

    Sleep(400)
    Jump("loc_2FED")

    label("loc_2FBD")

    Sleep(600)
    Jump("loc_2FED")

    label("loc_2FC5")

    Sleep(800)
    Jump("loc_2FED")

    label("loc_2FCD")

    Sleep(1000)
    Jump("loc_2FED")

    label("loc_2FD5")

    Sleep(1200)
    Jump("loc_2FED")

    label("loc_2FDD")

    Sleep(1400)
    Jump("loc_2FED")

    label("loc_2FE5")

    Sleep(1600)
    Jump("loc_2FED")

    label("loc_2FED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3018")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(1000)
    Jump("loc_2FED")

    label("loc_3018")

    Return()

    # Function_32_2F75 end

    def Function_33_3019(): pass

    label("Function_33_3019")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(496)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x20, 0x80)
    ClearChrFlags(0x30, 0x80)
    OP_78(0x2, 0x30)
    OP_49()
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    OP_FF(0x2, 0x15E, 0x15E, 0x15E)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x30, -30000, 10000, 50000, 135)
    OP_D5(0x30, 0x0, 0x20F58, 0x0, 0x0)
    BeginChrThread(0x30, 1, 0, 34)
    BeginChrThread(0x31, 1, 0, 37)
    OP_68(7750, 5200, 37650, 0)
    MoveCamera(30, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(29000, 0)
    MoveCamera(45, -10, 0, 8000)
    SetCameraDistance(42500, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    StopSound(496, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t3520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_3019 end

    def Function_34_3116(): pass

    label("Function_34_3116")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -30000, 10000, 60000)
    OP_9F(0x1, 5000, 10000, 50000)
    OP_9F(0x1, 20000, 12000, 0)
    OP_9F(0x2, 0xFE, 14000, 0x7)
    Return()

    # Function_34_3116 end

    def Function_35_314E(): pass

    label("Function_35_314E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3179")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(1000)
    Jump("Function_35_314E")

    label("loc_3179")

    Return()

    # Function_35_314E end

    def Function_36_317A(): pass

    label("Function_36_317A")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Return()

    # Function_36_317A end

    def Function_37_31B7(): pass

    label("Function_37_31B7")

    Sound(496, 2, 20, 0)
    Sleep(300)
    OP_25(0x1F0, 0x1E)
    Sleep(300)
    OP_25(0x1F0, 0x28)
    Sleep(300)
    OP_25(0x1F0, 0x32)
    Sleep(300)
    OP_25(0x1F0, 0x3C)
    Sleep(300)
    OP_25(0x1F0, 0x46)
    Sleep(300)
    OP_25(0x1F0, 0x50)
    Return()

    # Function_37_31B7 end

    def Function_38_31E8(): pass

    label("Function_38_31E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch20600.itc", 0x21)
    LoadChrToIndex("chr/ch22200.itc", 0x22)
    LoadChrToIndex("chr/ch45000.itc", 0x23)
    LoadChrToIndex("chr/ch47600.itc", 0x24)
    SoundLoad(851)
    SoundLoad(3603)
    SoundLoad(3604)
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2B, 0x1E)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, -12800, -200, 6900, 0)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -14000, -200, 6500, 0)
    SetChrChipByIndex(0x2C, 0x20)
    SetChrSubChip(0x2C, 0x5)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, -13000, -200, 4800, 0)
    BeginChrThread(0x2C, 3, 0, 0)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -10700, -200, 7100, 0)
    SetChrChipByIndex(0x26, 0x22)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, -9700, -200, 7100, 0)
    SetChrChipByIndex(0x27, 0x4)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -9900, -200, 5900, 0)
    SetChrChipByIndex(0x28, 0x23)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, -11400, -200, 4900, 0)
    SetChrChipByIndex(0x29, 0x24)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, -10900, -200, 4100, 0)
    SetChrChipByIndex(0x23, 0x7)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -7200, -200, 4800, 0)
    SetChrChipByIndex(0x21, 0x8)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -5100, -200, 5600, 0)
    SetChrChipByIndex(0x24, 0xB)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -4800, -200, 4100, 0)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -3200, -200, 5000, 0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1800, -200, 4500, 0)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -6400, -200, 6800, 0)
    OP_4B(0x19, 0xFF)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -3000, -200, 6900, 0)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -8900, -200, 4900, 0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x20, 0x80)
    VolumeBGM(0x5A, 0x3E8)
    OP_68(-7000, 4100, 10500, 0)
    MoveCamera(37, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    Sound(851, 2, 100, 0)
    OP_68(-7000, 1100, 10500, 5000)
    MoveCamera(37, 11, 0, 5000)
    FadeToBright(2000, 0)
    BeginChrThread(0x23, 3, 0, 35)
    BeginChrThread(0xB, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x21, 3, 0, 35)
    BeginChrThread(0x19, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x24, 3, 0, 35)
    BeginChrThread(0x22, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x8, 3, 0, 35)
    BeginChrThread(0x11, 3, 0, 35)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x21,
        "#11PThat's amazing … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#11PWith that building, IBC leverage\x01",
            "Finally did it finish! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#11PNo way, that beautiful building\x01",
            "It was built …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#11PAfter all, Mayor Dieter\x01",
            "To do is too much deck!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-10000, 700, 7000, 0)
    MoveCamera(37, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 1500)
    OP_6F(0x79)
    BeginChrThread(0x25, 3, 0, 36)
    OP_63(0x25, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x25,
        "#11P#4SSud: ── ─!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x25, 3)
    TurnDirection(0x25, 0x26, 500)

    ChrTalk(
        0x25,
        (
            "#6PHenry Henry!\x01",
            "Let's go exploring, explore!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x25, 500)

    ChrTalk(
        0x26,
        "#11PWell, I'm getting angry again ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#11Poh dear……\x01",
            "I do not know how I feel.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3738():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_3738)
    Sleep(50)

    def lambda_3748():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_3748)

    ChrTalk(
        0x27,
        "#11P…… Su, it's awesome ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3804")

    ChrTalk(
        0x28,
        (
            "#12PIt is certainly a terrible building … …\x01",
            "You can not think of it in Calvert!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12PWell, my home is in this town.\x01",
            "I feel like I can understand that ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3894")

    label("loc_3804")


    NpcTalk(
        0x28,
        "boy",
        (
            "#12PIt is certainly a terrible building … …\x01",
            "You can not think of it in Calvert!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x28,
        "boy",
        (
            "#12PWell, my home is in this town.\x01",
            "I feel like I can understand that ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3894")

    OP_68(-13300, 700, 7000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x2A,
        (
            "#12P#06000FHehu ……\x01",
            "Everyone, it is really exciting.\x02\x03",
            "#06002FHey, Kaea-chan.\x01",
            "Is it such a big building?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#11P#01105F#30W…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(150)

    ChrTalk(
        0x2A,
        (
            "#5P#06005FKa'a-chan …?\x01",
            "You are there.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x2B, 0x2A, 500)

    ChrTalk(
        0x2B,
        (
            "#11P#01109FOh, sorry, Shizuku.\x02\x03",
            "#01110FWell, it's really big!\x02\x03",
            "The color is also blue and white,\x01",
            "Be cool and cool!\x02\x03",
            "#01108F#30WBut ………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#5P#06008FIs it? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#11P#01102FAh\x01",
            "No, nothing.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-10460, 6100, 24340, 4000)
    MoveCamera(17, -5, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(15820, 4000)
    OP_93(0x2B, 0x0, 0x12C)
    OP_6F(0x79)
    SetChrFlags(0x2B, 0x4)
    SetChrPos(0x2B, -15500, 1200, -2900, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x2B,
        (
            "#01106F#3603V#40W#12P#N(why……\x01",
            "I should have seen him for the first time … …)\x02\x03",
            "#01112F#3604V#30W(Kea, that building ……\x01",
            "I feel like I've seen it somewhere. )\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE14)
    OP_C9(0x1, 0x80000000)
    StopSound(851, 2000, 100)
    SetCameraDistance(15320, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x64, 0x64)
    Sleep(100)
    OP_24(0x353)
    Sleep(1000)
    SetScenarioFlags(0x22, 6)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_31E8 end

    def Function_39_3BF0(): pass

    label("Function_39_3BF0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("apl/ch50237.itc", 0x1F)
    SetChrPos(0x101, 12000, 0, 1000, 180)
    SetChrPos(0x102, 12000, 0, 1000, 180)
    SetChrPos(0x103, 12000, 0, 1000, 180)
    SetChrPos(0x109, 12000, 0, 1000, 180)
    SetChrPos(0x105, 12000, 0, 1000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2D, 0x1E)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, -12000, -200, 6900, 0)
    OP_68(11250, 1000, -2300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    SetCameraDistance(14500, 4000)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(600)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(600)
    BeginChrThread(0x103, 3, 0, 42)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 43)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 44)
    WaitChrThread(0x105, 3)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_68(-12000, 1000, 6900, 3000)
    MoveCamera(33, 16, 0, 3000)
    SetCameraDistance(12500, 3000)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x2D,
        (
            "#03204F#11PGiggle\x01",
            "It seems that you came in a hurry\x01",
            "What is more.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-12000, 900, 5400, 3000)
    MoveCamera(37, 19, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(14000, 3000)
    SetChrPos(0x101, -4000, -200, -1000, 270)
    SetChrPos(0x102, -4000, -200, -1000, 270)
    SetChrPos(0x103, -4000, -200, -1500, 270)
    SetChrPos(0x109, -4000, -200, -1000, 270)
    SetChrPos(0x105, -4000, -200, -1500, 270)

    def lambda_3E7E():
        OP_95(0xFE, -12600, -200, 3900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E7E)
    Sleep(300)

    def lambda_3E9B():
        OP_95(0xFE, -12200, -200, 2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E9B)
    Sleep(600)

    def lambda_3EB8():
        OP_95(0xFE, -11500, -200, 3700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EB8)
    Sleep(600)

    def lambda_3ED5():
        OP_95(0xFE, -10200, -200, 3800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3ED5)
    Sleep(300)

    def lambda_3EF2():
        OP_95(0xFE, -10200, -200, 2800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3EF2)
    WaitChrThread(0x101, 1)

    def lambda_3F10():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F10)
    WaitChrThread(0x103, 1)

    def lambda_3F21():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3F21)
    WaitChrThread(0x102, 1)

    def lambda_3F32():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3F32)
    WaitChrThread(0x109, 1)

    def lambda_3F43():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3F43)
    WaitChrThread(0x105, 1)

    def lambda_3F54():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3F54)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00001FMr. Tsao ……\x01",
            "Is it safe alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#12PWas it Mr. Lau?\x01",
            "Who is the usual escort?\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7114", 0)
    OP_93(0x2D, 0xB4, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x2D,
        (
            "Huh, I got busy a bit\x01",
            "We are arranging variously.\x02\x03",
            "And that noisy people\x01",
            "Because I lost it from the town.\x02\x03",
            "I also waved the major\x01",
            "I can walk under the blue sky.\x02",
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

    ChrTalk(
        0x103,
        (
            "#12P#00211F……As usual\x01",
            "It is fishy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FTo young executives who are \"Black Monday\"\x01",
            "I think that blue sky does not suit you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03209FHaha, well that might be true\x02\x03",
            "#03200F─ ─ There is no time for each other,\x01",
            "I will enter into the main subject.\x02\x03",
            "#03206FActually last night, \"Silver#2RIn#From the palace\x01",
            "There was a sudden contact.\x02\x03",
            "Black moon#4RUs#Long-term contract with\x01",
            "I told you to abort.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10108FAh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PThat is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03201FOh I was quite surprised\x02\x03",
            "I managed to hold back\x01",
            "Equivalent, stubborn#2RHard#Seemingly …\x02\x03",
            "#03206FThat puts me in a tough spot\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FIt is for us\x01",
            "What relationship is … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03202F── Yesterday, on the southern coast of Elm\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10101FCould it be…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FWe were together\x01",
            "You seem to already have it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03204FYes, and with the Association\x01",
            "Those of the \"snake\"\x01",
            "To the thing that it appeared.\x02\x03",
            "#03201FOn all \"silver\"\x01",
            "What is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00008F….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12P… … The obligation to talk to you\x01",
            "I think that it is not … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03202FThat means that, to her again\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00110F#12P…!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00006F… … It is useless, Erie.\x01",
            "It is not an ordinary opponent.\x02\x03",
            "#00011FIf we're not careful we'll divulge…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FWhew.\x01",
            "Pretty stupid#4RAppointment#You know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03209FHuh, again\x01",
            "Was the \"silver\" hall a woman?\x02\x03",
            "#03210FProbably with superhuman inner comedy\x01",
            "He was changing his mind and body\x01",
            "Were you there?\x02\x03",
            "#03204FWith that physical ability\x01",
            "I am convinced of his success in the stage.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2D, 500)

    ChrTalk(
        0x101,
        "#12P#00010FUgh..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201F….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03204FNo, I was concerned.\x01",
            "Before the alkane shell related\x01",
            "I examined the schedule.\x02\x03",
            "#03210FThen \"silver\"\x01",
            "The timing to refuse this work\x01",
            "Agreed with the day of the performance etc.\x02\x03",
            "No, thanks to everyone\x01",
            "Finally I was confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006F….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12P……\"Her\x01",
            "What are you planning to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03205FNothing for now\x02\x03",
            "#03209FWell, I knew the identity\x01",
            "For me alone, the hand of threatening\x01",
            "Thought though …\x02\x03",
            "#03202FAs there were others related to the guild,\x01",
            "Here also to shut down your mouth\x01",
            "I will not go.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x109,
        "#10110F…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10306FThat's a bad joke\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F…… If the story is only that\x01",
            "Because I am in a hurry, will I be rude?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03204FHaha, well I guess that's it\x02\x03",
            "#03210F── Thank you for the information now\x01",
            "Let's give you a strange story.\x02\x03",
            "I'm Randy, but ….\x01",
            "About three hours ago, in Mainz's mountain path\x01",
            "He seems to have visited a certain point.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#12P#00011F#4S!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FR-really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03204FRegarding the trend of \"red constellation\"\x01",
            "I had a special surveillance team.\x02\x03",
            "#03200FSo it was information from one of those observers\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10301FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#12PSo then where was that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03203FCurrently, the Crossbell Guard\x01",
            "Before the falls laying the line of defense ……\x02\x03",
            "#03201FFrom the hill in the vicinity\x01",
            "It is said that we got off the cliffs with Zile.\x02\x03",
            "Since I was going to be noticed\x01",
            "I hesitate to give up tracking.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00101F#11PLloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYeah. That's better information than we could have hoped for\x02\x03",
            "#00000F── Mr. Tsao.\x01",
            "I appreciate the information …!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E45():
        TurnDirection(0xFE, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E45)

    ChrTalk(
        0x2D,
        (
            "#5P#03200FHuh, if you do your best\x01",
            "It will also be beneficial here.\x02\x03",
            "#03204FWell, Mr. Randy\x01",
            "Please be careful not to die.\x02\x03",
            "#03210FThey're strong. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FUnderstood\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x258)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00007FOK, please contact the section chief with Enigma\x01",
            "Let's go to Mainz Mountain soon!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F72():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4F72)
    Sleep(50)

    def lambda_4F82():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4F82)
    Sleep(50)

    def lambda_4F92():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4F92)
    Sleep(50)

    def lambda_4FA2():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4FA2)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x103,
        "#12P#00201FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107FUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PWe have to catch him!\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_5024():

        label("loc_5024")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5024")

    QueueWorkItem2(0x2D, 2, lambda_5024)
    OP_68(-7000, 900, 3400, 4000)
    SetCameraDistance(15500, 4000)
    BeginChrThread(0x105, 3, 0, 45)
    Sleep(300)
    BeginChrThread(0x109, 3, 0, 45)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 45)
    Sleep(400)
    BeginChrThread(0x103, 3, 0, 45)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 45)
    Sleep(4000)
    EndChrThread(0x2D, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(-12000, 1000, 6900, 0)
    MoveCamera(33, 16, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_63(0x2D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x2D)
    OP_93(0x2D, 0xB4, 0x1F4)
    Sleep(150)
    SetChrChipByIndex(0x2D, 0x1F)
    SetChrSubChip(0x2D, 0x0)
    Sleep(90)
    SetChrSubChip(0x2D, 0x1)
    Sleep(90)
    SetChrSubChip(0x2D, 0x2)
    Sleep(90)
    Sound(318, 0, 60, 0)
    SetChrSubChip(0x2D, 0x3)
    Sleep(200)

    ChrTalk(
        0x2D,
        (
            "#03204F#5PHa ha …… Such a stinky smell\x01",
            "Sometimes it's not bad.\x02\x03",
            "#03200FWell then-\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2D, 0x2)
    Sleep(90)
    SetChrSubChip(0x2D, 0x1)
    Sleep(90)
    SetChrSubChip(0x2D, 0x0)
    Sleep(90)
    SetChrChipByIndex(0x2D, 0x1E)
    SetChrSubChip(0x2D, 0x0)
    Sleep(200)
    SetCameraDistance(12000, 1000)
    OP_93(0x2D, 0x0, 0x15E)
    OP_6F(0x79)

    ChrTalk(
        0x2D,
        (
            "#03203F#11PThis is the do or die moment\x02\x03",
            "#03202F─ ─ Apparently also here\x01",
            "It seems necessary to give full power.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(11500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x166, 2)
    OP_29(0xAA, 0x1, 0x5)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    NewScene("c0100", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_39_3BF0 end

    def Function_40_5212(): pass

    label("Function_40_5212")


    def lambda_5217():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5217)

    def lambda_5231():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5231)
    WaitChrThread(0xFE, 1)

    def lambda_5246():
        OP_95(0xFE, 10500, -200, -3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5246)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x13B, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(100)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(100)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Return()

    # Function_40_5212 end

    def Function_41_52E8(): pass

    label("Function_41_52E8")


    def lambda_52ED():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52ED)

    def lambda_5307():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5307)
    WaitChrThread(0xFE, 1)

    def lambda_531C():
        OP_95(0xFE, 12000, -200, -3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_531C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_41_52E8 end

    def Function_42_533D(): pass

    label("Function_42_533D")


    def lambda_5342():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5342)

    def lambda_535C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_535C)
    WaitChrThread(0xFE, 1)

    def lambda_5371():
        OP_95(0xFE, 10500, -200, -2300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5371)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_42_533D end

    def Function_43_5392(): pass

    label("Function_43_5392")


    def lambda_5397():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5397)

    def lambda_53B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_53B1)
    WaitChrThread(0xFE, 1)

    def lambda_53C6():
        OP_95(0xFE, 12000, -200, -2300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53C6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_43_5392 end

    def Function_44_53E7(): pass

    label("Function_44_53E7")


    def lambda_53EC():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53EC)

    def lambda_5406():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5406)
    WaitChrThread(0xFE, 1)

    def lambda_541B():
        OP_95(0xFE, 11800, -200, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_541B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_44_53E7 end

    def Function_45_543C(): pass

    label("Function_45_543C")

    OP_92(0xFE, 0x1388, 0xFFFFF830, 0x1F4)

    def lambda_544E():
        OP_95(0xFE, 5000, -200, -2000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_544E)
    WaitChrThread(0xFE, 1)

    def lambda_546C():
        OP_95(0xFE, 10000, -200, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_546C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_543C end

    def Function_46_5486(): pass

    label("Function_46_5486")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03500.itp")
    SetChrChipByIndex(0x2E, 0x1E)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, -2960, -200, 7150, 15)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    OP_78(0x1, 0x2F)
    SetChrPos(0x2F, -17280, -200, 6420, 90)
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    Fade(1000)
    OP_68(-2900, 780, 7160, 0)
    MoveCamera(57, 18, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(8260, 0)
    SetCameraDistance(10260, 3000)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(1000)
    OP_68(5540, 2800, -6730, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7220, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x109, 11990, -20, 570, 180)
    SetChrPos(0x105, 11990, -20, 570, 180)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 49)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 50)
    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x105, 3)

    def lambda_5686():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5686)
    Sleep(50)

    def lambda_5696():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5696)
    Sleep(50)

    def lambda_56A6():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_56A6)
    Sleep(50)

    def lambda_56B6():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_56B6)
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00005FAh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FThere was …\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    Fade(1000)
    OP_68(-19590, 20100, 22530, 0)
    MoveCamera(27, 2, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(1530, 0)
    OP_0D()
    OP_68(-13810, 9200, 12250, 9000)
    MoveCamera(27, 2, 0, 9000)
    OP_6E(780, 9000)
    SetCameraDistance(37930, 9000)
    OP_6F(0x1)
    Sleep(800)
    OP_68(1610, 2500, 790, 5000)
    MoveCamera(350, -3, 0, 5000)
    OP_6E(780, 5000)
    SetCameraDistance(5910, 5000)
    OP_6F(0x1)
    Sleep(1000)

    ChrTalk(
        0x2E,
        (
            "#03506FGiggle\x02\x03",
            "#03510F…… But what is crossbell?\x01",
            "I do not understand in translation.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-1640, 1400, 4800, 0)
    MoveCamera(7, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12380, 0)
    SetCameraDistance(10380, 3000)
    SetChrPos(0x101, -3960, -200, 1110, 15)
    SetChrPos(0x102, -2460, -200, 1110, 15)
    SetChrPos(0x109, -3460, -200, 110, 15)
    SetChrPos(0x105, -1960, -200, 110, 15)

    def lambda_58DD():
        OP_98(0x101, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58DD)
    Sleep(50)

    def lambda_58FA():
        OP_98(0x102, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58FA)
    Sleep(50)

    def lambda_5917():
        OP_98(0x109, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5917)
    Sleep(50)

    def lambda_5934():
        OP_98(0x105, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5934)
    Sleep(50)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        (
            "#6P#00001F… … What I want to say is\x01",
            "I understand somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F- commonly known as \"Orkis Tower\".\x02\x03",
            "250 Age on the ground, 40 stories\x01",
            "The world's first skyscraper building.\x02\x03",
            "#00100FIn addition to the new city government, corporate floor,\x01",
            "International conference halls are also available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FIt is certainly a masterpiece, is not it?\x02\x03",
            "#10100FEven though I'm so far away\x01",
            "It looks like he looks so big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, because I'm still hiding\x01",
            "I do not know what kind of design … ….\x02\x03",
            "#10302FYou have completed one more thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, half of the staff of the city is already\x01",
            "She seems to be moving over there.\x02\x03",
            "#00004FThe actual office of the building is\x01",
            "It will be at the time of the trade meeting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#6P#03500FAnd the leaders of the same line\x01",
            "That's why I'm going to break through.\x02\x03",
            "#03506FWhew.\x01",
            "What is Dieter Crois?\x01",
            "It looks like more people than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F….\x02\x03",
            "#00001F── Crossbell Police,\x01",
            "I will ask you as the Special Affairs Support Division.\x02\x03",
            "Rector Alain Dor.\x01",
            "Please cooperate to confirm your identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#6P#03504FCutting ……\x02\x03",
            "#03500FSeriously.\x01",
            "─ ─ If you say that you do not want it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F…… Certainly in Crossbell\x01",
            "Empire against Republic government officials\x01",
            "We can not exercise legally binding power.\x02\x03",
            "#00101FHowever, it is an identity to the last\x01",
            "Only when it is obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FOn the contrary if you can not clarify\x01",
            "At the same level as ordinary foreigners\x01",
            "I can interrogate … ….\x02\x03",
            "#10300FIndeed, that's what it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "#6P#03504FHm, have you come so?\x02",
    )

    CloseMessageWindow()
    OP_93(0x2E, 0xB4, 0x1F4)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x2E,
        (
            "……it can not be helped.\x01",
            "It seems like when you paid a yearly burden.\x02\x03",
            "No, my affiliation is ──\x02",
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
    OP_63(0x2E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x2E, 0x2D, 0x1F4)

    ChrTalk(
        0x2E,
        "#6P#03505FHmm……?\x02",
    )

    CloseMessageWindow()

    def lambda_5F6C():
        OP_93(0x101, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F6C)
    Sleep(50)

    def lambda_5F7C():
        OP_93(0x102, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F7C)
    Sleep(50)

    def lambda_5F8C():
        OP_93(0x109, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5F8C)
    Sleep(50)

    def lambda_5F9C():
        OP_93(0x105, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5F9C)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(5510, 2800, 17730, 0)
    MoveCamera(32, 9, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#N#00005FWhat happened?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x2E,
        (
            "#N#03505FOh, it's a building over there.\x02\x03",
            "#03506F…… something black people\x01",
            "Have you not flew around the roof?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#N#00011FHuh……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#N#11P#00105FWell, no way … ….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#N#11P#10305FOh, maybe\x01",
            "Is that \"silver\" a person?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#N#11P#10105FBut,\x01",
            "Is it from this daytime?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrFlags(0x2E, 0x80)
    OP_0D()
    SetChrPos(0x101, 0, -200, 5110, 30)
    SetChrPos(0x102, 2000, -200, 5110, 30)
    SetChrPos(0x109, 1000, -200, 4110, 30)
    SetChrPos(0x105, 2500, -200, 4110, 30)
    Fade(500)
    OP_68(-5750, 2800, 3270, 0)
    MoveCamera(53, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5280, 0)
    OP_0D()
    OP_93(0x109, 0x10E, 0x3E8)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10111FAhh! Is it?\x02",
    )

    CloseMessageWindow()

    def lambda_6227():
        OP_93(0x101, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6227)
    Sleep(50)

    def lambda_6237():
        OP_93(0x102, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6237)
    Sleep(50)

    def lambda_6247():
        OP_93(0x105, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6247)

    ChrTalk(
        0x101,
        "#00011FOh, it is!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_628A():
        OP_95(0x101, -16360, -200, 4810, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_628A)
    Sleep(100)

    def lambda_62A7():
        OP_95(0x102, -16360, -200, 6110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_62A7)
    Sleep(50)

    def lambda_62C4():
        OP_95(0x109, -15060, -200, 4810, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62C4)
    Sleep(50)

    def lambda_62E1():
        OP_95(0x105, -15060, -200, 6110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_62E1)
    Sleep(50)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    Fade(500)
    OP_68(-20920, 2800, 4200, 0)
    MoveCamera(54, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5220, 0)
    SetChrPos(0x101, -11360, -200, 4810, 270)
    SetChrPos(0x102, -11360, -200, 6110, 270)
    SetChrPos(0x109, -10060, -200, 4810, 270)
    SetChrPos(0x105, -10060, -200, 6110, 270)

    def lambda_6386():
        OP_95(0x101, -16180, -200, 5770, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6386)
    Sleep(100)

    def lambda_63A3():
        OP_95(0x102, -16149, -200, 6900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63A3)
    Sleep(50)

    def lambda_63C0():
        OP_95(0x109, -14800, -200, 5880, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63C0)
    Sleep(50)

    def lambda_63DD():
        OP_95(0x105, -15150, -200, 6830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_63DD)
    WaitChrThread(0x102, 1)

    def lambda_63FB():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63FB)
    WaitChrThread(0x105, 1)

    def lambda_640C():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_640C)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#5P#00105Fま だ か\x01",
            "Go down at this subway! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FOh, impossible ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHaha!\x01",
            "I will not believe it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FCut …… Common sense so far\x01",
            "It's an opponent you do not pass ……\x02\x03",
            "#00007FBelow this is the back street!\x01",
            "Anyway get off the stairs!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 3)
    NewScene("c0500", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_46_5486 end

    def Function_47_6591(): pass

    label("Function_47_6591")


    def lambda_6596():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6596)

    def lambda_65A7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65A7)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 6830, -200, -3780, 2000, 0x0)
    Return()

    # Function_47_6591 end

    def Function_48_65D5(): pass

    label("Function_48_65D5")


    def lambda_65DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_65DA)

    def lambda_65EB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_65EB)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 8000, -200, -4990, 2000, 0x0)
    Return()

    # Function_48_65D5 end

    def Function_49_6619(): pass

    label("Function_49_6619")


    def lambda_661E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_661E)

    def lambda_662F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_662F)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 8850, -200, -3200, 2000, 0x0)
    Return()

    # Function_49_6619 end

    def Function_50_665D(): pass

    label("Function_50_665D")


    def lambda_6662():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6662)

    def lambda_6673():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6673)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 9880, -200, -4810, 2000, 0x0)
    Return()

    # Function_50_665D end

    def Function_51_66A1(): pass

    label("Function_51_66A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_68(11860, 1800, -3520, 0)
    MoveCamera(53, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10770, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_676D")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x104, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_6864")

    label("loc_676D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_67EB")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x109, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_6864")

    label("loc_67EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6864")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x105, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_6864")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_68CF")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 55)
    Jump("loc_694A")

    label("loc_68CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_690F")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 56)
    Jump("loc_694A")

    label("loc_690F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_694A")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 57)

    label("loc_694A")

    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    OP_6F(0x1)

    ChrTalk(
        0x1A2,
        (
            "#6PThis is the rooftop of the department store ……\x01",
            "Well, is not it a nice view?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHehe, is not it?\x01",
            "From here you can see the entire city.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#5PWell, it was more than I thought!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11PThat's right, the Orkis Tower …!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6A97")

    def lambda_6A61():

        label("loc_6A61")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6A61")

    QueueWorkItem2(0x101, 1, lambda_6A61)

    def lambda_6A73():

        label("loc_6A73")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6A73")

    QueueWorkItem2(0x102, 1, lambda_6A73)

    def lambda_6A85():

        label("loc_6A85")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6A85")

    QueueWorkItem2(0x104, 1, lambda_6A85)
    Jump("loc_6B1A")

    label("loc_6A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6ADB")

    def lambda_6AA5():

        label("loc_6AA5")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6AA5")

    QueueWorkItem2(0x101, 1, lambda_6AA5)

    def lambda_6AB7():

        label("loc_6AB7")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6AB7")

    QueueWorkItem2(0x102, 1, lambda_6AB7)

    def lambda_6AC9():

        label("loc_6AC9")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6AC9")

    QueueWorkItem2(0x109, 1, lambda_6AC9)
    Jump("loc_6B1A")

    label("loc_6ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6B1A")

    def lambda_6AE9():

        label("loc_6AE9")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6AE9")

    QueueWorkItem2(0x101, 1, lambda_6AE9)

    def lambda_6AFB():

        label("loc_6AFB")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6AFB")

    QueueWorkItem2(0x102, 1, lambda_6AFB)

    def lambda_6B0D():

        label("loc_6B0D")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6B0D")

    QueueWorkItem2(0x105, 1, lambda_6B0D)

    label("loc_6B1A")


    def lambda_6B1F():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6B1F)
    Sleep(500)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6B51")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    Jump("loc_6B88")

    label("loc_6B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6B6F")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    Jump("loc_6B88")

    label("loc_6B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6B88")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x105, 0x1)

    label("loc_6B88")

    Fade(500)
    OP_68(-8320, 2600, 1920, 0)
    MoveCamera(26, -1, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7370, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6C7E")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x104, -1960, -200, 110, 0)

    def lambda_6C0D():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6C0D)
    Sleep(50)

    def lambda_6C2A():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C2A)
    Sleep(50)

    def lambda_6C47():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C47)
    Sleep(50)

    def lambda_6C64():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C64)
    Jump("loc_6DFF")

    label("loc_6C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6D41")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x109, -1960, -200, 110, 0)

    def lambda_6CD0():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6CD0)
    Sleep(50)

    def lambda_6CED():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6CED)
    Sleep(50)

    def lambda_6D0A():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D0A)
    Sleep(50)

    def lambda_6D27():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6D27)
    Jump("loc_6DFF")

    label("loc_6D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6DFF")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x105, -1960, -200, 110, 0)

    def lambda_6D93():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6D93)
    Sleep(50)

    def lambda_6DB0():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6DB0)
    Sleep(50)

    def lambda_6DCD():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DCD)
    Sleep(50)

    def lambda_6DEA():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6DEA)

    label("loc_6DFF")

    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x1A2,
        "Is that … ….!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Still wrapped in veil\x01",
            "That sense of Sonzai is amazing!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5PSasa, Ely sister also\x01",
            "To more, and to my side!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHuh, I understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FPu Fu\x01",
            "Be careful not to fall.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1620, -2300, 8900, 0)
    MoveCamera(48, 26, 2, 0)
    OP_6E(700, 0)
    SetCameraDistance(20270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6F87")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x104, -1960, -200, 3110, 0)
    Jump("loc_7026")

    label("loc_6F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6FD9")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x109, -1960, -200, 3110, 0)
    Jump("loc_7026")

    label("loc_6FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_7026")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x105, -1960, -200, 3110, 0)

    label("loc_7026")

    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell, the view from the roof is\x01",
            "Are you satisfied?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Oh, I got a tan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "You guidance of your city\x01",
            "It was rather bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "What I should say …\x01",
            "It is likely to be a good memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FRight, you can say that\x01",
            "Anything else.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)
    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "I will be in the morning of the day after tomorrow\x01",
            "I plan to return to Cal bird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "and again,\x01",
            "It is enclosed by the adults\x01",
            "That's why I study everyday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It is a person who stands on a person\x01",
            "That is fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FShin kun ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_723B")

    ChrTalk(
        0x104,
        "#00303F……got it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_728A")

    label("loc_723B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_7264")

    ChrTalk(
        0x109,
        "#10103F……I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_728A")

    label("loc_7264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_728A")

    ChrTalk(
        0x105,
        "#10303F……I see.\x02",
    )

    CloseMessageWindow()

    label("loc_728A")


    ChrTalk(
        0x101,
        (
            "#12P#00000FBy the way, Shin\x01",
            "Are you going to Sunday school?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "Oh, Kenbun\x01",
            "It is for once by spreading it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Well, everyone around me\x01",
            "Afraid of adults,\x01",
            "I will not try to come near.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_END)), "loc_73EC")

    ChrTalk(
        0x1A2,
        (
            "That's why,\x01",
            "Did I say I was crying with Kea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "You can talk to a cod that you are talking about\x01",
            "It was pretty fun and fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FHaha, is that so?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7405")

    label("loc_73EC")


    ChrTalk(
        0x101,
        "#12P#00008FShin …\x02",
    )

    CloseMessageWindow()

    label("loc_7405")


    ChrTalk(
        0x1A2,
        (
            "… or what to say,\x01",
            "I told you a stupid story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Anyway, the guiding direction is enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Then send it to the office.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOh, that's OK.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 4)
    SetScenarioFlags(0x22, 5)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_66A1 end

    def Function_52_74C2(): pass

    label("Function_52_74C2")


    def lambda_74C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_74C7)

    def lambda_74D8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_74D8)
    WaitChrThread(0x1A2, 1)
    OP_95(0x1A2, 14590, -200, -3020, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_52_74C2 end

    def Function_53_750D(): pass

    label("Function_53_750D")


    def lambda_7512():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7512)

    def lambda_7523():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7523)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 13970, -200, -4930, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_53_750D end

    def Function_54_7558(): pass

    label("Function_54_7558")


    def lambda_755D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_755D)

    def lambda_756E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_756E)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 13740, -200, -1810, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_54_7558 end

    def Function_55_75A3(): pass

    label("Function_55_75A3")


    def lambda_75A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_75A8)

    def lambda_75B9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75B9)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_55_75A3 end

    def Function_56_75EE(): pass

    label("Function_56_75EE")


    def lambda_75F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_75F3)

    def lambda_7604():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7604)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_56_75EE end

    def Function_57_7639(): pass

    label("Function_57_7639")


    def lambda_763E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_763E)

    def lambda_764F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_764F)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_57_7639 end

    SaveToFile()

Try(main)
