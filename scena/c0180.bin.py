from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Jeanetta",               # 1
        "Eugene",                 # 2
        "Theodore",               # 3
        "Chiruru",                # 4
        "Corona",                 # 5
        "Rimah",                  # 6
        "Melson",                 # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Citizen",                # 10
        "Girl",                   # 11
        "Tourist",                # 12
        "Tourist",                # 13
        "Citizen",                # 14
        "Citizen",                # 15
        "Tourist",                # 16
        "Tourist",                # 17
        "Citizen",                # 18
        "Citizen",                # 19
        "Tourist",                # 20
        "Tourist",                # 21
        "Citizen",                # 22
        "Boy",                    # 23
        "Tourist",                # 24
        "Inspector Donovan",      # 25
        "Citizen",                # 26
        "Citizen",                # 27
        "Citizen",                # 28
        "Citizen",                # 29
        "Ryｹ",                   # 30
        "Henri",                  # 31
        "Momo",                   # 32
        "Shing",                  # 33
        "Heiyue",                 # 34
        "Shizuku",                # 35
        "KeA",                    # 36
        "Zeit",                   # 37
        "Cao",                    # 38
        "Lechter",                # 39
        "Seire",                  # 40
        "Arseille",               # 41
        "SE制御",                 # 42
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
        "Function_7_136B",         # 07, 7
        "Function_8_13EB",         # 08, 8
        "Function_9_1455",         # 09, 9
        "Function_10_14DD",        # 0A, 10
        "Function_11_151E",        # 0B, 11
        "Function_12_158C",        # 0C, 12
        "Function_13_1D8C",        # 0D, 13
        "Function_14_1DE9",        # 0E, 14
        "Function_15_1E4A",        # 0F, 15
        "Function_16_1EF7",        # 10, 16
        "Function_17_1F55",        # 11, 17
        "Function_18_1FC4",        # 12, 18
        "Function_19_2044",        # 13, 19
        "Function_20_20E1",        # 14, 20
        "Function_21_2171",        # 15, 21
        "Function_22_2218",        # 16, 22
        "Function_23_2287",        # 17, 23
        "Function_24_2345",        # 18, 24
        "Function_25_23C3",        # 19, 25
        "Function_26_2448",        # 1A, 26
        "Function_27_2497",        # 1B, 27
        "Function_28_29CF",        # 1C, 28
        "Function_29_2D95",        # 1D, 29
        "Function_30_2EBA",        # 1E, 30
        "Function_31_2F6E",        # 1F, 31
        "Function_32_32FF",        # 20, 32
        "Function_33_33A3",        # 21, 33
        "Function_34_34A0",        # 22, 34
        "Function_35_34D8",        # 23, 35
        "Function_36_3504",        # 24, 36
        "Function_37_3541",        # 25, 37
        "Function_38_3572",        # 26, 38
        "Function_39_3F42",        # 27, 39
        "Function_40_56FC",        # 28, 40
        "Function_41_57D2",        # 29, 41
        "Function_42_5827",        # 2A, 42
        "Function_43_587C",        # 2B, 43
        "Function_44_58D1",        # 2C, 44
        "Function_45_5926",        # 2D, 45
        "Function_46_5970",        # 2E, 46
        "Function_47_6ADD",        # 2F, 47
        "Function_48_6B21",        # 30, 48
        "Function_49_6B65",        # 31, 49
        "Function_50_6BA9",        # 32, 50
        "Function_51_6BED",        # 33, 51
        "Function_52_7A2D",        # 34, 52
        "Function_53_7A78",        # 35, 53
        "Function_54_7AC3",        # 36, 54
        "Function_55_7B0E",        # 37, 55
        "Function_56_7B59",        # 38, 56
        "Function_57_7BA4",        # 39, 57
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E80")

    ChrTalk(
        0xFE,
        (
            "*sigh*, Southwark was\x01",
            "cool that night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Saying "Someone like me understands\x01",
            "your good qualities" with such a\x01",
            "serious look on his face...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I had the\x01",
            "greatest time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EF9")

    label("loc_E80")


    ChrTalk(
        0xFE,
        (
            "And, who would have thought\x01",
            "he'd give me Arc-en-Ciel\x01",
            "tickets as a present...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I'm a really\x01",
            "lucky person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF9")

    Jump("loc_120C")

    label("loc_EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F0C")
    Jump("loc_120C")

    label("loc_F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106C")

    ChrTalk(
        0xFE,
        (
            "*haaah*, I want a\x01",
            "reliable boyfriend like\x01",
            "Pearl...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Whoopsie, oh no, no... I\x01",
            "must water the flowers\x01",
            "properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I am sorry. I'm going\x01",
            "to sprinkle a lot of water\x01",
            "on you babies now, 'k?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F(Wha, baby taaalk...\x01",
            "This gets a lot of\x01",
            "points.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(W-What kind of\x01",
            "points...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10C0")

    label("loc_106C")


    ChrTalk(
        0xFE,
        (
            "Uhuhu, I am sorry. I'm going\x01",
            "to sprinkle a lot of water\x01",
            "on you babies now, 'k?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C0")

    Jump("loc_120C")

    label("loc_10C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_10D3")
    Jump("loc_120C")

    label("loc_10D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_120C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119E")

    ChrTalk(
        0xFE,
        (
            "Phew, this place has a\x01",
            "lovely view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, by the way, it's not\x01",
            "the case that I'm\x01",
            "skipping work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The manager put me in\x01",
            "charge of watering these\x01",
            "plants.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0xB4, 0x0)
    SetChrFlags(0xFE, 0x10)
    Jump("loc_120C")

    label("loc_119E")


    ChrTalk(
        0xFE,
        (
            "Uhuhu, I'll give you\x01",
            "water now, 'k? Drink a\x01",
            "lot and grow healthy, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(W-Why the baby talk?)\x02",
    )

    CloseMessageWindow()

    label("loc_120C")

    TalkEnd(0xFE)
    Return()

    # Function_5_D9B end

    def Function_6_1210(): pass

    label("Function_6_1210")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12DC")

    ChrTalk(
        0xFE,
        (
            "Recently, that building has been\x01",
            "getting closer to completion each\x01",
            "time I come back from a journey...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So that's what it was\x01",
            "like under the sheet. I\x01",
            "think it's quite cool...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1367")

    label("loc_12DC")


    ChrTalk(
        0xFE,
        (
            "Well then, I got to see the\x01",
            "building... I guess it's time\x01",
            "to go on my next journey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for going home...\x01",
            "I'll do that next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1367")

    TalkEnd(0xFE)
    Return()

    # Function_6_1210 end

    def Function_7_136B(): pass

    label("Function_7_136B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Maaan, as expected\x01",
            "people like us give out\x01",
            "a certain aura, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry Theodore, this was\x01",
            "all my miscalculation.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_136B end

    def Function_8_13EB(): pass

    label("Function_8_13EB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "...Shit, "They won't\x01",
            "find us in our practice\x01",
            "clothes" my ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was stupid trusting\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_13EB end

    def Function_9_1455(): pass

    label("Function_9_1455")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "To think my husband was\x01",
            "involved in the construction of\x01",
            "such a magnificent building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I couldn't be more\x01",
            "proud.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_1455 end

    def Function_10_14DD(): pass

    label("Function_10_14DD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Whooah, I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ehehe, I knew papa was\x01",
            "amazing♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_14DD end

    def Function_11_151E(): pass

    label("Function_11_151E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Hey Rimah, look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That building was made by\x01",
            "papa and his colleagues\x01",
            "joining forces, you know.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_151E end

    def Function_12_158C(): pass

    label("Function_12_158C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_174B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C0")

    ChrTalk(
        0xFE,
        (
            "Terrorists after both\x01",
            "nations' VIPs...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't be swayed by this\x01",
            "information alone, but it's true\x01",
            "that it mentally prepared me well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, the security\x01",
            "shifts will be as Dudley\x01",
            "explained yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All we need now is for\x01",
            "everyone to do their\x01",
            "very best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1746")

    label("loc_16C0")


    ChrTalk(
        0xFE,
        (
            "Anyway, the security\x01",
            "shifts will be as Dudley\x01",
            "explained yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All we need now is for\x01",
            "everyone to do their\x01",
            "very best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1746")

    Jump("loc_1D88")

    label("loc_174B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A93")

    ChrTalk(
        0xFE,
        (
            "Hi guys. It looks like you\x01",
            "took part in the unveiling\x01",
            "ceremony security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How'd you like seeing\x01",
            "the VIPs from up close?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, they really had an\x01",
            "amazing presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah, how to say it, it\x01",
            "felt like I could see\x01",
            "their auras for real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see, so you felt it\x01",
            "really well, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what can I say? Of\x01",
            "course it's important to\x01",
            "feel the atmosphere too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it's important to not get\x01",
            "overwhelmed when you're close\x01",
            "enough to touch them, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, you're certainly\x01",
            "right about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI-I'm not all that\x01",
            "confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Well experience is\x01",
            "important too, after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, it looks\x01",
            "like it was a good\x01",
            "experience for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make sure to thank Sergei\x01",
            "for getting you into the\x01",
            "security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAlright, we will.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 3)
    Jump("loc_1B3C")

    label("loc_1A93")


    ChrTalk(
        0xFE,
        (
            "Like you've felt, each\x01",
            "VIP's "aura" is a unique\x01",
            "and real thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, what I want to say is\x01",
            "that it's important to not lose\x01",
            "yourself when accompanying VIPs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B3C")

    Jump("loc_1D88")

    label("loc_1B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB1")

    ChrTalk(
        0xFE,
        (
            "Oh, you guys. Anything\x01",
            "out of the ordinary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, well, nothing of\x01",
            "import.\x02\x03",
            "Inspector, are you in\x01",
            "charge of security here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah. This is a convenient\x01",
            "place to get in touch with\x01",
            "whoever's needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, nothing's out of\x01",
            "the ordinary for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continue to stand by as\x01",
            "the reserve unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D88")

    label("loc_1CB1")


    ChrTalk(
        0xFE,
        (
            "Still, it's a big help that the\x01",
            "crowds throughout the city are less\x01",
            "than at the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though come tomorrow, things probably\x01",
            "aren't going to be like today because\x01",
            "of the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D88")

    TalkEnd(0xFE)
    Return()

    # Function_12_158C end

    def Function_13_1D8C(): pass

    label("Function_13_1D8C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The department store rooftop,\x01",
            "eh? I can't believe they've\x01",
            "made such a nice spot.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1D8C end

    def Function_14_1DE9(): pass

    label("Function_14_1DE9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Phew, the wind feels\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The view is nice too.\x01",
            "This is a really lovely\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1DE9 end

    def Function_15_1E4A(): pass

    label("Function_15_1E4A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Come to think of it, our\x01",
            "child knows almost nothing of\x01",
            "the world outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I guess I'll bring\x01",
            "her to Armorica Village\x01",
            "or something next time.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1E4A end

    def Function_16_1EF7(): pass

    label("Function_16_1EF7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Wooow, there's lots of\x01",
            "green far far away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if that's\x01",
            "Crossbell too.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1EF7 end

    def Function_17_1F55(): pass

    label("Function_17_1F55")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I wonder what's really\x01",
            "going on inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really looking\x01",
            "forward to the unveiling\x01",
            "ceremony.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1F55 end

    def Function_18_1FC4(): pass

    label("Function_18_1FC4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "However... I wonder how\x01",
            "they're going to remove\x01",
            "that cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't tell me we'll all\x01",
            "have to pull from\x01",
            "below...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1FC4 end

    def Function_19_2044(): pass

    label("Function_19_2044")

    TalkBegin(0xFE)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xFE,
        "#4SEEEEEK!!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I never dreamt of\x01",
            "meeting you two in a\x01",
            "place like this!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "E-Excuse me, may I\x01",
            "please have an\x01",
            "autograph!!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2044 end

    def Function_20_20E1(): pass

    label("Function_20_20E1")

    TalkBegin(0xFE)
    TurnDirection(0x16, 0x15, 0)

    ChrTalk(
        0xFE,
        (
            "H-Hey now. If you're\x01",
            "that loud you'll bother\x01",
            "everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And as for getting their\x01",
            "autographs... I'll be\x01",
            "the first!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0xE1, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_20E1 end

    def Function_21_2171(): pass

    label("Function_21_2171")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, they're both more\x01",
            "handsome and burly than\x01",
            "how they appear on stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a tiny bit frustrating,\x01",
            "but I can understand why my\x01",
            "wife fell for them.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2171 end

    def Function_22_2218(): pass

    label("Function_22_2218")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Aah, Sir Theodore and Sir Eugene in\x01",
            "the flesh, right before my eyes...\x01",
            "I think I'm going to faint.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2218 end

    def Function_23_2287(): pass

    label("Function_23_2287")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I understand that the\x01",
            "conference's main session\x01",
            "will now start in earnest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't understand difficult\x01",
            "things, but I hope the mayor and\x01",
            "the others will do their very best.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2287 end

    def Function_24_2345(): pass

    label("Function_24_2345")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I wonder if my cheers\x01",
            "will reach the mayor and\x01",
            "the others from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hooray, hooray, mayor!\x01",
            "...Just kidding.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_2345 end

    def Function_25_23C3(): pass

    label("Function_25_23C3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*, no matter how\x01",
            "many times I see it, It's\x01",
            "an astonishing building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Many say it's\x01",
            "Crossbell's newest\x01",
            "landmark.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_23C3 end

    def Function_26_2448(): pass

    label("Function_26_2448")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Haha. I'm sure the view\x01",
            "from that building's\x01",
            "rooftop is wonderful.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_2448 end

    def Function_27_2497(): pass

    label("Function_27_2497")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24F7")

    ChrTalk(
        0xFE,
        (
            "That huge tree... The pale\x01",
            "blue light it gives off\x01",
            "makes it seem magical.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CB")

    label("loc_24F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2505")
    Jump("loc_29CB")

    label("loc_2505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_25C4")

    ChrTalk(
        0xFE,
        (
            "With our security in the hands of\x01",
            "President Dieter and Secretary of\x01",
            "Defense Arios, we can rest easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll probably be a long\x01",
            "fight, but we must win\x01",
            "our independence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CB")

    label("loc_25C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_266D")

    ChrTalk(
        0xFE,
        (
            "Mr. Arios did some\x01",
            "really great things to\x01",
            "protect Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've felt it before, but this\x01",
            "city is what it is because of\x01",
            "that man's presence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CB")

    label("loc_266D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2747")

    ChrTalk(
        0xFE,
        (
            "It seems an armed group has suddenly\x01",
            "appeared, but... I wonder if this\x01",
            "could have been prevented somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The police and CGF have to get\x01",
            "their act together or I won't\x01",
            "be able to sleep at night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CB")

    label("loc_2747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2755")
    Jump("loc_29CB")

    label("loc_2755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_27F8")

    ChrTalk(
        0xFE,
        (
            "I'm worried. It seems some\x01",
            "kind of accident has\x01",
            "happened along the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looked like quite a\x01",
            "number of ambulances\x01",
            "went towards it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CB")

    label("loc_27F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_28CA")

    ChrTalk(
        0xFE,
        (
            "Because I decided to rest here, I\x01",
            "ended up staying at the department\x01",
            "store longer than I wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the breeze hits you in this\x01",
            "place, it blows your shopping\x01",
            "fatigue away, doesn't it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CB")

    label("loc_28CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_29CB")

    ChrTalk(
        0xFE,
        (
            "Haha. I feel I've completely\x01",
            "gotten used to this scene with\x01",
            "Orchis Tower in it, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The townscape will probably\x01",
            "change a lot in these next\x01",
            "10 or 20 years, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think only the presence\x01",
            "of that building will\x01",
            "remain unchanged.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CB")

    TalkEnd(0xFE)
    Return()

    # Function_27_2497 end

    def Function_28_29CF(): pass

    label("Function_28_29CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A25")

    ChrTalk(
        0xFE,
        (
            "How can such a huge tree\x01",
            "float? The world is full\x01",
            "of mysteries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D91")

    label("loc_2A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A33")
    Jump("loc_2D91")

    label("loc_2A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2AC5")

    ChrTalk(
        0xFE,
        (
            "They say that Arios has\x01",
            "become a secretary after\x01",
            "being a bracer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it,\x01",
            "but now he's probably\x01",
            "invincible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D91")

    label("loc_2AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B22")

    ChrTalk(
        0xFE,
        (
            "I'm Arios MacLaine...\x01",
            "I'm a bracer!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*clang*, *bam bam bam\x01",
            "bam bam*!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D91")

    label("loc_2B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2BA0")

    ChrTalk(
        0xFE,
        (
            "They say something\x01",
            "really bad is happening\x01",
            "at Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if the bad guys\x01",
            "will be caught quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D91")

    label("loc_2BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2BAE")
    Jump("loc_2D91")

    label("loc_2BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2CB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5B")

    ChrTalk(
        0xFE,
        (
            "When the ambulances\x01",
            "passed by, they sounded\x01",
            "strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wasn't like "pi-po\x01",
            "pi-po", but "pu-po pu-\x01",
            "po" you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, what happened?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2CAE")

    label("loc_2C5B")


    ChrTalk(
        0xFE,
        (
            "When the ambulances\x01",
            "passed by, they sounded\x01",
            "strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, what happened?\x02",
    )

    CloseMessageWindow()

    label("loc_2CAE")

    Jump("loc_2D91")

    label("loc_2CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D48")

    ChrTalk(
        0xFE,
        (
            "I like the rooftop too,\x01",
            "but it's a problem that\x01",
            "there's nothing here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't they make a place\x01",
            "to eat or something like\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D91")

    label("loc_2D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D91")

    ChrTalk(
        0xFE,
        (
            "Hehe, there's nice\x01",
            "weather today too.\x01",
            "Rooftop air is nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D91")

    TalkEnd(0xFE)
    Return()

    # Function_28_29CF end

    def Function_29_2D95(): pass

    label("Function_29_2D95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E1B")

    NpcTalk(
        0xFE,
        "Girl",
        (
            "They say today's rain is\x01",
            "going to clear up this\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Girl",
        (
            "Haha. Maybe we'll even\x01",
            "see a rainbow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB6")

    label("loc_2E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2EB6")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Haha. I wonder why rain\x01",
            "in the city tickles my\x01",
            "heart so much.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "This sorrowful atmosphere\x01",
            "is so emotionally\x01",
            "unbearable...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EB6")

    TalkEnd(0xFE)
    Return()

    # Function_29_2D95 end

    def Function_30_2EBA(): pass

    label("Function_30_2EBA")

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

    # Function_30_2EBA end

    def Function_31_2F6E(): pass

    label("Function_31_2F6E")

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

    # Function_31_2F6E end

    def Function_32_32FF(): pass

    label("Function_32_32FF")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3337"),
        (1, "loc_333F"),
        (2, "loc_3347"),
        (3, "loc_334F"),
        (4, "loc_3357"),
        (5, "loc_335F"),
        (6, "loc_3367"),
        (SWITCH_DEFAULT, "loc_336F"),
    )


    label("loc_3337")

    Sleep(200)
    Jump("loc_3377")

    label("loc_333F")

    Sleep(400)
    Jump("loc_3377")

    label("loc_3347")

    Sleep(600)
    Jump("loc_3377")

    label("loc_334F")

    Sleep(800)
    Jump("loc_3377")

    label("loc_3357")

    Sleep(1000)
    Jump("loc_3377")

    label("loc_335F")

    Sleep(1200)
    Jump("loc_3377")

    label("loc_3367")

    Sleep(1400)
    Jump("loc_3377")

    label("loc_336F")

    Sleep(1600)
    Jump("loc_3377")

    label("loc_3377")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33A2")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(1000)
    Jump("loc_3377")

    label("loc_33A2")

    Return()

    # Function_32_32FF end

    def Function_33_33A3(): pass

    label("Function_33_33A3")

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

    # Function_33_33A3 end

    def Function_34_34A0(): pass

    label("Function_34_34A0")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -30000, 10000, 60000)
    OP_9F(0x1, 5000, 10000, 50000)
    OP_9F(0x1, 20000, 12000, 0)
    OP_9F(0x2, 0xFE, 14000, 0x7)
    Return()

    # Function_34_34A0 end

    def Function_35_34D8(): pass

    label("Function_35_34D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3503")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(1000)
    Jump("Function_35_34D8")

    label("loc_3503")

    Return()

    # Function_35_34D8 end

    def Function_36_3504(): pass

    label("Function_36_3504")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Return()

    # Function_36_3504 end

    def Function_37_3541(): pass

    label("Function_37_3541")

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

    # Function_37_3541 end

    def Function_38_3572(): pass

    label("Function_38_3572")

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
        "#11PAmazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#11PWith IBC's support, they\x01",
            "finally completed it!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#11PAnd it's such a\x01",
            "beautiful building at\x01",
            "that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#11PEverything Mayor Dieter\x01",
            "does is on a whole other\x01",
            "scale!\x02",
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
        "#11P#4SC-Cooooool!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x25, 3)
    TurnDirection(0x25, 0x26, 500)

    ChrTalk(
        0x25,
        (
            "#6PHey Henri! Let's go\x01",
            "explore it! C'mon!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x25, 500)

    ChrTalk(
        0x26,
        (
            "#11PW-We'll get in trouble\x01",
            "again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#11PI... understand how you\x01",
            "feel, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3AA5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_3AA5)
    Sleep(50)

    def lambda_3AB5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_3AB5)

    ChrTalk(
        0x27,
        "#11P...Wow...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3B80")

    ChrTalk(
        0x28,
        (
            "#12PI-It sure is incredible...\x01",
            "You'd never see anything\x01",
            "like it in Calvard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12PHmm, I think I understand\x01",
            "why we're so obsessed\x01",
            "with this city...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C24")

    label("loc_3B80")


    NpcTalk(
        0x28,
        "Boy",
        (
            "#12PI-It sure is incredible...\x01",
            "You'd never see anything\x01",
            "like it in Calvard!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x28,
        "Boy",
        (
            "#12PHmm, I think I understand\x01",
            "why we're so obsessed\x01",
            "with this city...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C24")

    OP_68(-13300, 700, 7000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x2A,
        (
            "#12P#06000FHaha... Everyone's so\x01",
            "excited.\x02\x03",
            "#06002FHey KeA, is it really\x01",
            "that big?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#11P#01105F#30W............\x02",
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
            "#5P#06005FKeA...? You're there,\x01",
            "aren't you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x2B, 0x2A, 500)

    ChrTalk(
        0x2B,
        (
            "#11P#01109FAh─ Sorry, Shizuku.\x02\x03",
            "#01110FUmm, it's super big!\x02\x03",
            "Its blue and white\x01",
            "colors are pretty, and\x01",
            "it's slim and cool!\x02\x03",
            "#01108F#30WBut...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#5P#06008F? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#11P#01102FAh... No, nevermind.\x02",
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
            "#01106F#3603V#40W#12P#N(What's this...? It's my\x01",
            "first time seeing it,\x01",
            "and yet...)\x02\x03",
            "#01112F#3604V#30W(I feel like I've seen\x01",
            "that building somewhere\x01",
            "before...)\x02",
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

    # Function_38_3572 end

    def Function_39_3F42(): pass

    label("Function_39_3F42")

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
            "#03204F#11PHehe... I'm glad you\x01",
            "came quickly.\x02",
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

    def lambda_41C6():
        OP_95(0xFE, -12600, -200, 3900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41C6)
    Sleep(300)

    def lambda_41E3():
        OP_95(0xFE, -12200, -200, 2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_41E3)
    Sleep(600)

    def lambda_4200():
        OP_95(0xFE, -11500, -200, 3700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4200)
    Sleep(600)

    def lambda_421D():
        OP_95(0xFE, -10200, -200, 3800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_421D)
    Sleep(300)

    def lambda_423A():
        OP_95(0xFE, -10200, -200, 2800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_423A)
    WaitChrThread(0x101, 1)

    def lambda_4258():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4258)
    WaitChrThread(0x103, 1)

    def lambda_4269():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4269)
    WaitChrThread(0x102, 1)

    def lambda_427A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_427A)
    WaitChrThread(0x109, 1)

    def lambda_428B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_428B)
    WaitChrThread(0x105, 1)

    def lambda_429C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_429C)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00001FMr. Cao... Are you ok\x01",
            "alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#12PLau, was it? Where's the\x01",
            "bodyguard who's always\x01",
            "with you?\x02",
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
            "Hehe. We're a little busy so I'm\x01",
            "having him do a few things for me.\x02\x03",
            "By the way, those dangerous people\x01",
            "have left the city, right?\x02\x03",
            "Thus, it means I too can\x01",
            "triumphantly walk under the blue\x01",
            "sky.\x02",
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
        "#12P#00211F...Shady as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAlthough I think the blue sky\x01",
            "doesn't suit you, the youngest\x01",
            "leader in all of Heiyue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03209FHaha, that is true.\x02\x03",
            "#03200F─Neither you nor I have\x01",
            "time to waste, so allow me\x01",
            "to get down to business.\x02\x03",
            "#03206FLast night, we were\x01",
            "suddenly contacted by Yin,\x01",
            "you see.\x02\x03",
            "He told us he is\x01",
            "discontinuing his long-\x01",
            "term contract with us.\x02",
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
        "#10108FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03201FAs you might imagine, I\x01",
            "was shocked.\x02\x03",
            "I tried to stop him, but\x01",
            "he was rather\x01",
            "obstinate...\x02\x03",
            "#03206FFor the life of me, I\x01",
            "couldn't understand why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003F...Is that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FAnd what that have to do\x01",
            "with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03202F─What on earth happened\x01",
            "on the south bank of Elm\x01",
            "Lake yesterday?\x02",
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
        "#10101FCould it be that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FLooks like you've\x01",
            "already learned we were\x01",
            "together, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03204FYes, and that the Bracer\x01",
            "Guild and the Snake\x01",
            "people showed up too.\x02\x03",
            "#03201FWhat in the world has\x01",
            "happened to Master Yin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00008F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12P...I think we have no\x01",
            "obligation to tell you\x01",
            "about it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03202FThen, as I suspected,\x01",
            "something has really\x01",
            "happened to her, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00110F#12P...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00006F...It's no use, Elie.\x01",
            "He's not your common\x01",
            "opponent.\x02\x03",
            "#00011FIf we're not careful\x01",
            "we'll divulge─ oh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FOh boy. You're quite the\x01",
            "crafty one, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03209FHehe. As I suspected,\x01",
            "Master Yin is a woman, hm?\x02\x03",
            "#03210FI suppose that she used a\x01",
            "superhuman neigong to alter\x01",
            "her qi and figure, correct?\x02\x03",
            "#03204FHaving such abilities, I\x01",
            "can understand her success\x01",
            "on the stage.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2D, 500)

    ChrTalk(
        0x101,
        "#12P#00010FUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03204FWell since I was interested, I looked\x01",
            "into the schedules of the Arc-en-Ciel\x01",
            "staff members previously.\x02\x03",
            "#03210FThe timing of Master Yin's refusal of\x01",
            "our jobs coincided with performance\x01",
            "days.\x02\x03",
            "Dear me, thanks to you all, I've\x01",
            "finally come to believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12P...What're you planning\x01",
            "to do with "her"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03205F─For now, nothing.\x02\x03",
            "#03209FWell, if I was the only one who knew\x01",
            "her true identity, I was thinking of\x01",
            "threatening her with it, but...\x02\x03",
            "#03202FSince those guild people were\x01",
            "involved, it's not the case that I\x01",
            "can silence you all here.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x109,
        "#10110F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10306FWhat a bad joke...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FIf this is all you have to\x01",
            "say, you'll have to excuse\x01",
            "us, since we're busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03204FHehe, come on, don't say that.\x02\x03",
            "#03210F─As thank you for the information\x01",
            "you provided me, I will offer you\x01",
            "some welcome news.\x02\x03",
            "Randy, was it? It appears that he\x01",
            "visited a certain place on Mainz\x01",
            "Mountain Path about three hours ago.\x02",
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
        "#12P#00205FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03204FWe have a specialized unit\x01",
            "for monitoring the actions\x01",
            "of Red Constellation.\x02\x03",
            "#03200FThe information came from\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10301FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#12PAnd, the place is\x01",
            "question was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03203FBefore the waterfall where\x01",
            "the CGF has set up their\x01",
            "current defensive line...\x02\x03",
            "#03201FHe descended below the cliffs\x01",
            "from high ground nearby using\x01",
            "a climbing rope.\x02\x03",
            "After that, they gave up the\x01",
            "pursuit because it seems he\x01",
            "noticed them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00101F#11PLloyd...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYeah, this is an\x01",
            "extremely useful info.\x02\x03",
            "#00000F─Mr. Cao, thank you!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_52EC():
        TurnDirection(0xFE, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_52EC)

    ChrTalk(
        0x2D,
        (
            "#5P#03200FHehe. If you do your\x01",
            "best, we'll benefit too,\x01",
            "after all.\x02\x03",
            "#03204FWell, please be careful\x01",
            "to not die together with\x01",
            "Randy.\x02\x03",
            "#03210F─"They" are strong. Very\x01",
            "strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003F...Understood.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x258)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00007FAlright, let's contact the chief\x01",
            "via ENIGMA and leave for Mainz\x01",
            "Mountain Path immediately.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_543E():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_543E)
    Sleep(50)

    def lambda_544E():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_544E)
    Sleep(50)

    def lambda_545E():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_545E)
    Sleep(50)

    def lambda_546E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_546E)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x103,
        "#12P#00201FYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PWe must catch up to him\x01",
            "somehow!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_54EC():

        label("loc_54EC")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_54EC")

    QueueWorkItem2(0x2D, 2, lambda_54EC)
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
            "#03204F#5PHaha... Such immaturity\x01",
            "isn't bad every now and\x01",
            "then.\x02\x03",
            "#03200FWell then─\x02",
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
            "#03203F#11PThis is a critical moment,\x01",
            "huh.\x02\x03",
            "#03202F─It appears I'll need to\x01",
            "bring all of our abilities\x01",
            "into play as well.\x02",
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

    # Function_39_3F42 end

    def Function_40_56FC(): pass

    label("Function_40_56FC")


    def lambda_5701():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5701)

    def lambda_571B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_571B)
    WaitChrThread(0xFE, 1)

    def lambda_5730():
        OP_95(0xFE, 10500, -200, -3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5730)
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

    # Function_40_56FC end

    def Function_41_57D2(): pass

    label("Function_41_57D2")


    def lambda_57D7():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57D7)

    def lambda_57F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_57F1)
    WaitChrThread(0xFE, 1)

    def lambda_5806():
        OP_95(0xFE, 12000, -200, -3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5806)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_41_57D2 end

    def Function_42_5827(): pass

    label("Function_42_5827")


    def lambda_582C():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_582C)

    def lambda_5846():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5846)
    WaitChrThread(0xFE, 1)

    def lambda_585B():
        OP_95(0xFE, 10500, -200, -2300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_585B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_42_5827 end

    def Function_43_587C(): pass

    label("Function_43_587C")


    def lambda_5881():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5881)

    def lambda_589B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_589B)
    WaitChrThread(0xFE, 1)

    def lambda_58B0():
        OP_95(0xFE, 12000, -200, -2300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_58B0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_43_587C end

    def Function_44_58D1(): pass

    label("Function_44_58D1")


    def lambda_58D6():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_58D6)

    def lambda_58F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_58F0)
    WaitChrThread(0xFE, 1)

    def lambda_5905():
        OP_95(0xFE, 11800, -200, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5905)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_44_58D1 end

    def Function_45_5926(): pass

    label("Function_45_5926")

    OP_92(0xFE, 0x1388, 0xFFFFF830, 0x1F4)

    def lambda_5938():
        OP_95(0xFE, 5000, -200, -2000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5938)
    WaitChrThread(0xFE, 1)

    def lambda_5956():
        OP_95(0xFE, 10000, -200, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5956)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_5926 end

    def Function_46_5970(): pass

    label("Function_46_5970")

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

    def lambda_5B70():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B70)
    Sleep(50)

    def lambda_5B80():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B80)
    Sleep(50)

    def lambda_5B90():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B90)
    Sleep(50)

    def lambda_5BA0():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5BA0)
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
        "#11P#00005FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FThere he is...\x02",
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
            "#03506FPhew...\x02\x03",
            "#03510F...Man, I don't get this\x01",
            "Crossbell place at all.\x02",
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

    def lambda_5DC6():
        OP_98(0x101, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DC6)
    Sleep(50)

    def lambda_5DE3():
        OP_98(0x102, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DE3)
    Sleep(50)

    def lambda_5E00():
        OP_98(0x109, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E00)
    Sleep(50)

    def lambda_5E1D():
        OP_98(0x105, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E1D)
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
            "#6P#00001FI think I understand\x01",
            "what you're trying to\x01",
            "say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F─Alias Orchis Tower.\x02\x03",
            "At 250 arge tall and 40 stories,\x01",
            "it's the world's first skyscraper.\x02\x03",
            "#00100FIn addition to the new City Hall, it\x01",
            "has corporate floors and facilities\x01",
            "for international conferences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FIt's incredible!\x02\x03",
            "#10100FIt's that big even\x01",
            "though we're this far\x01",
            "away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHehe. It's still\x01",
            "covered, so we don't\x01",
            "know its design, but...\x02\x03",
            "#10302FThey say it's basically\x01",
            "completed, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah. Half of the city\x01",
            "employees have already been\x01",
            "transferred there.\x02\x03",
            "#00004FThough the actual unveiling\x01",
            "is going to be at the start\x01",
            "of that trade conference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#6P#03500FSo he plans to dumbfound\x01",
            "all those heads of state,\x01",
            "does he?\x02\x03",
            "#03506FBoy oh boy. That Dieter\x01",
            "Crois is more of a\x01",
            "character than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F............\x02\x03",
            "#00001F─As Crossbell Police,\x01",
            "Special Support Section,\x01",
            "I ask you this.\x02\x03",
            "Mr. Lechter Arundel.\x01",
            "Please confirm your\x01",
            "identity for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#6P#03504FHaha...\x02\x03",
            "#03500FHow serious. ─And if I\x01",
            "refuse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F...It's true that Crossbell's\x01",
            "laws don't apply to Imperial and\x01",
            "Republic government officials.\x02\x03",
            "#00101FHowever, that's only if a\x01",
            "person's identity is clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FConversely, if it's not clear,\x01",
            "they'll be treated the same as\x01",
            "an ordinary foreigner.\x02\x03",
            "#10300FI see. So that's how it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#6P#03504FHmm, so it's come to\x01",
            "this, has it?\x02",
        )
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
            "...No choice then. Looks like my\x01",
            "time is up.\x02\x03",
            "Fine, I'm with─\x02",
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
        "#6P#03505FHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_64C0():
        OP_93(0x101, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64C0)
    Sleep(50)

    def lambda_64D0():
        OP_93(0x102, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64D0)
    Sleep(50)

    def lambda_64E0():
        OP_93(0x109, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_64E0)
    Sleep(50)

    def lambda_64F0():
        OP_93(0x105, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_64F0)
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
        "#N#00005FIs something wrong?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x2E,
        (
            "#N#03505FYeah, those buildings\x01",
            "over there.\x02\x03",
            "#03506F...Wasn't there a black\x01",
            "shadow jumping around\x01",
            "the rooftops...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#N#00011FHuh?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#N#11P#00105FI-It couldn't be...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#N#11P#10305FWoah, could it be Yin?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#N#11P#10105FB-But... Isn't it\x01",
            "daytime?\x02",
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
        "#10111FHuh!?\x02",
    )

    CloseMessageWindow()

    def lambda_677C():
        OP_93(0x101, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_677C)
    Sleep(50)

    def lambda_678C():
        OP_93(0x102, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_678C)
    Sleep(50)

    def lambda_679C():
        OP_93(0x105, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_679C)

    ChrTalk(
        0x101,
        "#00011FD-Damn!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_67D8():
        OP_95(0x101, -16360, -200, 4810, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67D8)
    Sleep(100)

    def lambda_67F5():
        OP_95(0x102, -16360, -200, 6110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_67F5)
    Sleep(50)

    def lambda_6812():
        OP_95(0x109, -15060, -200, 4810, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6812)
    Sleep(50)

    def lambda_682F():
        OP_95(0x105, -15060, -200, 6110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_682F)
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

    def lambda_68D4():
        OP_95(0x101, -16180, -200, 5770, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68D4)
    Sleep(100)

    def lambda_68F1():
        OP_95(0x102, -16149, -200, 6900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68F1)
    Sleep(50)

    def lambda_690E():
        OP_95(0x109, -14800, -200, 5880, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_690E)
    Sleep(50)

    def lambda_692B():
        OP_95(0x105, -15150, -200, 6830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_692B)
    WaitChrThread(0x102, 1)

    def lambda_6949():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6949)
    WaitChrThread(0x105, 1)

    def lambda_695A():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_695A)
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
            "#5P#00105FN-No way! He rappelled\x01",
            "down this rope!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI-I don't believe\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FAhaha! I can't believe\x01",
            "it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FUgh. Common sense\x01",
            "doesn't apply to this\x01",
            "guy.\x02\x03",
            "#00007FBack Street is below!\x01",
            "Let's head down!\x02",
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

    # Function_46_5970 end

    def Function_47_6ADD(): pass

    label("Function_47_6ADD")


    def lambda_6AE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6AE2)

    def lambda_6AF3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AF3)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 6830, -200, -3780, 2000, 0x0)
    Return()

    # Function_47_6ADD end

    def Function_48_6B21(): pass

    label("Function_48_6B21")


    def lambda_6B26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B26)

    def lambda_6B37():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B37)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 8000, -200, -4990, 2000, 0x0)
    Return()

    # Function_48_6B21 end

    def Function_49_6B65(): pass

    label("Function_49_6B65")


    def lambda_6B6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6B6A)

    def lambda_6B7B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6B7B)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 8850, -200, -3200, 2000, 0x0)
    Return()

    # Function_49_6B65 end

    def Function_50_6BA9(): pass

    label("Function_50_6BA9")


    def lambda_6BAE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6BAE)

    def lambda_6BBF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6BBF)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 9880, -200, -4810, 2000, 0x0)
    Return()

    # Function_50_6BA9 end

    def Function_51_6BED(): pass

    label("Function_51_6BED")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6CB9")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x104, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_6DB0")

    label("loc_6CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6D37")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x109, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_6DB0")

    label("loc_6D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6DB0")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x105, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_6DB0")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6E1B")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 55)
    Jump("loc_6E96")

    label("loc_6E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6E5B")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 56)
    Jump("loc_6E96")

    label("loc_6E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6E96")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 57)

    label("loc_6E96")

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
            "#6PThe department store\x01",
            "rooftop... Wow, what a\x01",
            "nice view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*. Amazing, right?\x01",
            "From here, you look out\x01",
            "over the entire city.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5PYeah, it's better than I\x01",
            "thought!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11POh yeah, Orchis Tower!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6FF3")

    def lambda_6FBD():

        label("loc_6FBD")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6FBD")

    QueueWorkItem2(0x101, 1, lambda_6FBD)

    def lambda_6FCF():

        label("loc_6FCF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6FCF")

    QueueWorkItem2(0x102, 1, lambda_6FCF)

    def lambda_6FE1():

        label("loc_6FE1")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6FE1")

    QueueWorkItem2(0x104, 1, lambda_6FE1)
    Jump("loc_7076")

    label("loc_6FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_7037")

    def lambda_7001():

        label("loc_7001")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_7001")

    QueueWorkItem2(0x101, 1, lambda_7001)

    def lambda_7013():

        label("loc_7013")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_7013")

    QueueWorkItem2(0x102, 1, lambda_7013)

    def lambda_7025():

        label("loc_7025")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_7025")

    QueueWorkItem2(0x109, 1, lambda_7025)
    Jump("loc_7076")

    label("loc_7037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_7076")

    def lambda_7045():

        label("loc_7045")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_7045")

    QueueWorkItem2(0x101, 1, lambda_7045)

    def lambda_7057():

        label("loc_7057")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_7057")

    QueueWorkItem2(0x102, 1, lambda_7057)

    def lambda_7069():

        label("loc_7069")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_7069")

    QueueWorkItem2(0x105, 1, lambda_7069)

    label("loc_7076")


    def lambda_707B():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_707B)
    Sleep(500)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_70AD")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    Jump("loc_70E4")

    label("loc_70AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_70CB")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    Jump("loc_70E4")

    label("loc_70CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_70E4")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x105, 0x1)

    label("loc_70E4")

    Fade(500)
    OP_68(-8320, 2600, 1920, 0)
    MoveCamera(26, -1, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7370, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_71DA")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x104, -1960, -200, 110, 0)

    def lambda_7169():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_7169)
    Sleep(50)

    def lambda_7186():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7186)
    Sleep(50)

    def lambda_71A3():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71A3)
    Sleep(50)

    def lambda_71C0():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_71C0)
    Jump("loc_735B")

    label("loc_71DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_729D")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x109, -1960, -200, 110, 0)

    def lambda_722C():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_722C)
    Sleep(50)

    def lambda_7249():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7249)
    Sleep(50)

    def lambda_7266():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7266)
    Sleep(50)

    def lambda_7283():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7283)
    Jump("loc_735B")

    label("loc_729D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_735B")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x105, -1960, -200, 110, 0)

    def lambda_72EF():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_72EF)
    Sleep(50)

    def lambda_730C():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_730C)
    Sleep(50)

    def lambda_7329():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7329)
    Sleep(50)

    def lambda_7346():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7346)

    label("loc_735B")

    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x1A2,
        "Is that it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It's still wrapped in\x01",
            "the veil, but that\x01",
            "presence is amazing!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5PC'mon Elie! A little\x01",
            "further forward, and\x01",
            "closer to me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHaha, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F*sigh*, please be very\x01",
            "careful to not fall.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1620, -2300, 8900, 0)
    MoveCamera(48, 26, 2, 0)
    OP_6E(700, 0)
    SetCameraDistance(20270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_74DE")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x104, -1960, -200, 3110, 0)
    Jump("loc_757D")

    label("loc_74DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_7530")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x109, -1960, -200, 3110, 0)
    Jump("loc_757D")

    label("loc_7530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_757D")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x105, -1960, -200, 3110, 0)

    label("loc_757D")

    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00000FAnd, have you gotten\x01",
            "enough of the scenery up\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "I have, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Your guys' guided tour\x01",
            "wasn't too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "How should I put it... I\x01",
            "think it'll make a good\x01",
            "memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FI see. Well I'm glad you\x01",
            "think so.\x02",
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
            "I'll be heading back to\x01",
            "Calvard the morning\x01",
            "after next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "And once again, I'll be\x01",
            "surrounded by adults and\x01",
            "study every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "That's the fate of one\x01",
            "who's in charge of\x01",
            "others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FShing...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_77A7")

    ChrTalk(
        0x104,
        "#00303F...I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_77EA")

    label("loc_77A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_77CB")

    ChrTalk(
        0x109,
        "#10103F...I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_77EA")

    label("loc_77CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_77EA")

    ChrTalk(
        0x105,
        "#10303F...I see.\x02",
    )

    CloseMessageWindow()

    label("loc_77EA")


    ChrTalk(
        0x101,
        (
            "#12P#00000FBy the way, do you go to\x01",
            "Sunday School, Shing?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "Yeah. Just to broaden my\x01",
            "horizons, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Well, everyone fears the\x01",
            "adults around me, so they\x01",
            "don't even try to approach me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_END)), "loc_7961")

    ChrTalk(
        0x1A2,
        (
            "So that's why... KeA and\x01",
            "Shizuku, were they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Being able to talk with\x01",
            "kids like them was quite\x01",
            "refreshing and fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FHaha, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_797A")

    label("loc_7961")


    ChrTalk(
        0x101,
        "#12P#00008FShing...\x02",
    )

    CloseMessageWindow()

    label("loc_797A")


    ChrTalk(
        0x1A2,
        (
            "...This conversation is\x01",
            "pointless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Anyway, that'll be fine\x01",
            "for today's tour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Escort me back to the\x01",
            "office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FSure, got it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 4)
    SetScenarioFlags(0x22, 5)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_6BED end

    def Function_52_7A2D(): pass

    label("Function_52_7A2D")


    def lambda_7A32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_7A32)

    def lambda_7A43():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_7A43)
    WaitChrThread(0x1A2, 1)
    OP_95(0x1A2, 14590, -200, -3020, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_52_7A2D end

    def Function_53_7A78(): pass

    label("Function_53_7A78")


    def lambda_7A7D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7A7D)

    def lambda_7A8E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A8E)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 13970, -200, -4930, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_53_7A78 end

    def Function_54_7AC3(): pass

    label("Function_54_7AC3")


    def lambda_7AC8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7AC8)

    def lambda_7AD9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AD9)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 13740, -200, -1810, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_54_7AC3 end

    def Function_55_7B0E(): pass

    label("Function_55_7B0E")


    def lambda_7B13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7B13)

    def lambda_7B24():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7B24)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_55_7B0E end

    def Function_56_7B59(): pass

    label("Function_56_7B59")


    def lambda_7B5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7B5E)

    def lambda_7B6F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7B6F)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_56_7B59 end

    def Function_57_7BA4(): pass

    label("Function_57_7BA4")


    def lambda_7BA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7BA9)

    def lambda_7BBA():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7BBA)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_57_7BA4 end

    SaveToFile()

Try(main)
