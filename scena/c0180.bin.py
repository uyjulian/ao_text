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
        "Function_6_1238",         # 06, 6
        "Function_7_138E",         # 07, 7
        "Function_8_140E",         # 08, 8
        "Function_9_1478",         # 09, 9
        "Function_10_1507",        # 0A, 10
        "Function_11_154E",        # 0B, 11
        "Function_12_15BB",        # 0C, 12
        "Function_13_1E00",        # 0D, 13
        "Function_14_1E5B",        # 0E, 14
        "Function_15_1EBA",        # 0F, 15
        "Function_16_1F6F",        # 10, 16
        "Function_17_1FC9",        # 11, 17
        "Function_18_203B",        # 12, 18
        "Function_19_20C5",        # 13, 19
        "Function_20_216B",        # 14, 20
        "Function_21_2201",        # 15, 21
        "Function_22_22B0",        # 16, 22
        "Function_23_231F",        # 17, 23
        "Function_24_23B9",        # 18, 24
        "Function_25_243B",        # 19, 25
        "Function_26_24CB",        # 1A, 26
        "Function_27_252A",        # 1B, 27
        "Function_28_2AB3",        # 1C, 28
        "Function_29_2E97",        # 1D, 29
        "Function_30_2FC7",        # 1E, 30
        "Function_31_307B",        # 1F, 31
        "Function_32_340C",        # 20, 32
        "Function_33_34B0",        # 21, 33
        "Function_34_35AD",        # 22, 34
        "Function_35_35E5",        # 23, 35
        "Function_36_3611",        # 24, 36
        "Function_37_364E",        # 25, 37
        "Function_38_367F",        # 26, 38
        "Function_39_40DE",        # 27, 39
        "Function_40_5921",        # 28, 40
        "Function_41_59F7",        # 29, 41
        "Function_42_5A4C",        # 2A, 42
        "Function_43_5AA1",        # 2B, 43
        "Function_44_5AF6",        # 2C, 44
        "Function_45_5B4B",        # 2D, 45
        "Function_46_5B95",        # 2E, 46
        "Function_47_6E40",        # 2F, 47
        "Function_48_6E84",        # 30, 48
        "Function_49_6EC8",        # 31, 49
        "Function_50_6F0C",        # 32, 50
        "Function_51_6F50",        # 33, 51
        "Function_52_7E2A",        # 34, 52
        "Function_53_7E75",        # 35, 53
        "Function_54_7EC0",        # 36, 54
        "Function_55_7F0B",        # 37, 55
        "Function_56_7F56",        # 38, 56
        "Function_57_7FA1",        # 39, 57
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
    Jump("loc_1234")

    label("loc_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7F")

    ChrTalk(
        0xFE,
        (
            "*sigh*, Mr. Southwark\x01",
            "was cool that night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Saying to me with such a serious faces\x01",
            ""Someone like me understands your good qualities"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, I had the greatest time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F01")

    label("loc_E7F")


    ChrTalk(
        0xFE,
        (
            "And also, who could have thought,\x01",
            "he even gave me Arc-en-ciel\x01",
            "tickets as a present...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, I'm a really lucky person.\x02",
    )

    CloseMessageWindow()

    label("loc_F01")

    Jump("loc_1234")

    label("loc_F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F14")
    Jump("loc_1234")

    label("loc_F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1082")

    ChrTalk(
        0xFE,
        (
            "*haaah*, I too want a reliable \x01",
            "boyfriend like Miss Pearl has...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Whoopsie, oh no, no...\x01",
            "I must water the flowers properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I am sorry.\x01",
            "I'm going to sprinkle a lot of\x01",
            "water on you babies now, 'k?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F(Wha, baby taaalk...\x01",
            "This gets a lot of points.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(W-What kind of points...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10D6")

    label("loc_1082")


    ChrTalk(
        0xFE,
        (
            "Uhuhu, I am sorry.\x01",
            "I'm going to sprinkle a lot of\x01",
            "water on you babies now, 'k?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D6")

    Jump("loc_1234")

    label("loc_10DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_10E9")
    Jump("loc_1234")

    label("loc_10E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1234")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C6")

    ChrTalk(
        0xFE,
        (
            "*phew*, this place has a\x01",
            "nicely amazing view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, by the way, it's not\x01",
            "that I'm skipping work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was put in charge of watering the\x01",
            "plantation's plants by the manager.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0xB4, 0x0)
    SetChrFlags(0xFE, 0x10)
    Jump("loc_1234")

    label("loc_11C6")


    ChrTalk(
        0xFE,
        (
            "Uhuhu, I'll give you water now, 'k?\x01",
            "Drink a lot and grow healthy, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(W-Why the baby talk?)\x02",
    )

    CloseMessageWindow()

    label("loc_1234")

    TalkEnd(0xFE)
    Return()

    # Function_5_D9B end

    def Function_6_1238(): pass

    label("Function_6_1238")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1301")

    ChrTalk(
        0xFE,
        (
            "A building that, recently, every time I came back from\x01",
            "a journey, was gradually approaching completion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So it was like this under the sheet.\x01",
            "I think it's quite cool...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_138A")

    label("loc_1301")


    ChrTalk(
        0xFE,
        (
            "Well then, I could see the building...\x01",
            "I guess it's time to go on my next journey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "As for going home...I'll do that next time.\x02",
    )

    CloseMessageWindow()

    label("loc_138A")

    TalkEnd(0xFE)
    Return()

    # Function_6_1238 end

    def Function_7_138E(): pass

    label("Function_7_138E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Maaan, as expected people like\x01",
            "us give out a certain aura, eh?\x02",
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

    # Function_7_138E end

    def Function_8_140E(): pass

    label("Function_8_140E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "...Shit, "They won't find us in\x01",
            "our practice clothes" my ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I was stupid trusting you.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_140E end

    def Function_9_1478(): pass

    label("Function_9_1478")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "To think that my husband was involved in the\x01",
            "construction of such a magnificent building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, I couldn't be more proud.\x01\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_1478 end

    def Function_10_1507(): pass

    label("Function_10_1507")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Whooah, I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eheheh, I knew that\x01",
            "papa was amazing♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_1507 end

    def Function_11_154E(): pass

    label("Function_11_154E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Hey Rimah, look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You see, that building\x01",
            "was made by papa and his\x01",
            "colleagues joining forces.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_154E end

    def Function_12_15BB(): pass

    label("Function_12_15BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1790")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1701")

    ChrTalk(
        0xFE,
        "Terrorists aiming at both nations' VIPs...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't get swayed by just because\x01",
            "of this information, but it's true that\x01",
            "it mentally readied me well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, for the guard shift\x01",
            "we'll abide at what Dudley\x01",
            "adjusted yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What remains is for all men\x01",
            "to do their very best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_178B")

    label("loc_1701")


    ChrTalk(
        0xFE,
        (
            "Anyway, for the guard shift\x01",
            "we'll abide at what Dudley\x01",
            "adjusted yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What remains is for all men\x01",
            "to do their very best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178B")

    Jump("loc_1DFC")

    label("loc_1790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC9")

    ChrTalk(
        0xFE,
        (
            "Hi guys. It looks like you\x01",
            "took part in the inauguration\x01",
            "ceremony security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How was seeing the VIPs from up close?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, they really had a great presence.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah, how to say, it\x01",
            "felt like I could see\x01",
            "that aura for real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see, you've felt it\x01",
            "really well, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what can I say about it.\x01",
            "Of course it's important to\x01",
            "feel such an atmosphere too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it's important to not get swallowed by\x01",
            "that when you're practically nearby too, see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, it's really so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI-I'm not really\x01",
            "confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha, well, for that \x01",
            "experience weighs too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at any rate, it looks like it was\x01",
            "a good personal experience for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "See that you properly thank\x01",
            "that Sergei for pushing you\x01",
            "into the security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, of course.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 3)
    Jump("loc_1B90")

    label("loc_1AC9")


    ChrTalk(
        0xFE,
        (
            "Like you've felt, each\x01",
            "VIPs' "aura" is a unique\x01",
            "and real thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anyway, what I want to say is that\x01",
            "if you make enemy of such big shots it's\x01",
            "important to not get swallowed by it. Yes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B90")

    Jump("loc_1DFC")

    label("loc_1B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2A")

    ChrTalk(
        0xFE,
        (
            "Hey, you guys.\x01",
            "Something out of the ordinary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, well, no\x01",
            "big accidents.\x02\x03",
            "Inspector, are you in charge of vigilance here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, this place is convenient in many\x01",
            "ways to get in touch with all quarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at any rate, at present here too\x01",
            "there's nothing out of the ordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Continue with your reserve activities.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DFC")

    label("loc_1D2A")


    ChrTalk(
        0xFE,
        (
            "Still, it helps that the crowds in all places\x01",
            "are less than at the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, come tomorrow, because of the inauguration\x01",
            "ceremony, things are probably going to be not like today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DFC")

    TalkEnd(0xFE)
    Return()

    # Function_12_15BB end

    def Function_13_1E00(): pass

    label("Function_13_1E00")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The department store rooftop, eh?\x01",
            "Never thought they'd \x01",
            "made such a nice spot.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1E00 end

    def Function_14_1E5B(): pass

    label("Function_14_1E5B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*phew*, the wind feels good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The view is also nice, this\x01",
            "is a very cool spot.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1E5B end

    def Function_15_1EBA(): pass

    label("Function_15_1EBA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Now that I think about it, our child doesn't \x01",
            "know almost anything outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hu hu, I guess that next time I'll bring\x01",
            "her to Armorica Village or the likes.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1EBA end

    def Function_16_1F6F(): pass

    label("Function_16_1F6F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Woow, there's green color\x01",
            "all far far away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is over there Crossbell too?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1F6F end

    def Function_17_1FC9(): pass

    label("Function_17_1FC9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I wonder what's really\x01",
            "going on inside there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't really wait for the inauguration ceremony.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1FC9 end

    def Function_18_203B(): pass

    label("Function_18_203B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "However... I wonder how they're\x01",
            "going to take away that cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't tell me that we all\x01",
            "will have to pull from below...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_203B end

    def Function_19_20C5(): pass

    label("Function_19_20C5")

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
            "I would've never dreamt to be able\x01",
            "to meet you two in such a place!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "E-Excuse me, please give me an autograph!!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_20C5 end

    def Function_20_216B(): pass

    label("Function_20_216B")

    TalkBegin(0xFE)
    TurnDirection(0x16, 0x15, 0)

    ChrTalk(
        0xFE,
        (
            "H-Hey now.\x01",
            "If you are so loud \x01",
            "you'll cause trouble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, getting their autographs...\x01",
            "I'll be the first to have them!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0xE1, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_216B end

    def Function_21_2201(): pass

    label("Function_21_2201")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, they're both more handsome and\x01",
            "burly than how they appear on stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a tiny bit mortifying,\x01",
            "but I think I understand why\x01",
            "even my wife fell for them.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2201 end

    def Function_22_22B0(): pass

    label("Function_22_22B0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Aah, sir Theodore and sir Eugene\x01",
            "in real flesh, in front of my eyes...\x01",
            "I think I'm going to faint.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_22B0 end

    def Function_23_231F(): pass

    label("Function_23_231F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "They say that the conference\x01",
            "we'll really start now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't get complex things, but I hope that\x01",
            "the mayor and the others do their best.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_231F end

    def Function_24_23B9(): pass

    label("Function_24_23B9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I wonder if I sent my cheers from here\x01",
            "they'd reach the mayor and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hooray, hooray, mayor!\x01",
            "...Kidding.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_23B9 end

    def Function_25_243B(): pass

    label("Function_25_243B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*haah*, no matter how many times I see it,\x01",
            "It's an astonishing building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's very well said that it's\x01",
            "Crossbell new landmark.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_243B end

    def Function_26_24CB(): pass

    label("Function_26_24CB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hu hu, I am sure that the scenery gazed\x01",
            "at from that building rooftop is splendid.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_24CB end

    def Function_27_252A(): pass

    label("Function_27_252A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2587")

    ChrTalk(
        0xFE,
        (
            "That big tree... The azure pale light\x01",
            "gives it a fantastic aspect too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2595")
    Jump("loc_2AAF")

    label("loc_2595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2677")

    ChrTalk(
        0xFE,
        (
            "President Dieter and Secretary of Defense Arios...\x01",
            "We can have peace of mind with these two men\x01",
            "and entrust Crossbell to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It will probably turn into a long fight,\x01",
            "but we must win our independence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2725")

    ChrTalk(
        0xFE,
        (
            "Mr. Arios did really some\x01",
            "great things in order to\x01",
            "protect Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I felt it again, but this city is what\x01",
            "it is because of that man's presence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2822")

    ChrTalk(
        0xFE,
        (
            "It seems an armed group has suddenly appeared, but...\x01",
            "I wonder if this could have been \x01",
            "prevented in a way or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Police and CGF must get their\x01",
            "act together a lot more or I won't be\x01",
            "able to feel at peace and sleep at night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2830")
    Jump("loc_2AAF")

    label("loc_2830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_28D6")

    ChrTalk(
        0xFE,
        (
            "I'm worried because it appears that some\x01",
            "accident has happened in the highway area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looked like quite the number\x01",
            "of ambulances went out...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_28D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_29A1")

    ChrTalk(
        0xFE,
        (
            "Because I took some rest here,\x01",
            "it turned out that I somehow\x01",
            "overstayed at the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the breeze hits you in this place,\x01",
            "even the shopping fatigue gets blown away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_29A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2AAF")

    ChrTalk(
        0xFE,
        (
            "Uh uh, somehow I feel I got completely used to\x01",
            "the scenery where you can see Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the next ten or twenty years, the city\x01",
            "scenery is probably going to change too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think only the presence of \x01",
            "that building will stay unchanged.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAF")

    TalkEnd(0xFE)
    Return()

    # Function_27_252A end

    def Function_28_2AB3(): pass

    label("Function_28_2AB3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2B0D")

    ChrTalk(
        0xFE,
        (
            "How could such a huge tree sprout?\x01",
            "The world is full of mysteries.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2B1B")
    Jump("loc_2E93")

    label("loc_2B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2BB1")

    ChrTalk(
        0xFE,
        (
            "They say that Mr. Arios has become\x01",
            "a secretary after being a Bracer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but now\x01",
            "he's probably invincible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C0E")

    ChrTalk(
        0xFE,
        (
            "I'm Arios MacLaine...\x01",
            "I'm a Bracer!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*blink*, *pam pam pam pam pam*!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C8C")

    ChrTalk(
        0xFE,
        (
            "Somehow they say that at Mainz\x01",
            "something really bad is happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Won't the bad guys get caught fast?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2C9A")
    Jump("loc_2E93")

    label("loc_2C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2DB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D55")

    ChrTalk(
        0xFE,
        (
            "When the ambulances\x01",
            "passed by, their sounds\x01",
            "were strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wasn't like "piipoo piipoo",\x01",
            "but "puupoo puupoo" you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why were those like that?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2DAB")

    label("loc_2D55")


    ChrTalk(
        0xFE,
        (
            "When the ambulances\x01",
            "passed by, they sounds\x01",
            "were strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eh, what happened?\x02",
    )

    CloseMessageWindow()

    label("loc_2DAB")

    Jump("loc_2E93")

    label("loc_2DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2E40")

    ChrTalk(
        0xFE,
        (
            "I like the rooftop too, but it's\x01",
            "a problem there's nothing here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't they make a place to\x01",
            "eat or something like that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E93")

    ChrTalk(
        0xFE,
        (
            "Eh eh, today too the weather's good.\x01",
            "The air on the rooftop is nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E93")

    TalkEnd(0xFE)
    Return()

    # Function_28_2AB3 end

    def Function_29_2E97(): pass

    label("Function_29_2E97")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F21")

    NpcTalk(
        0xFE,
        "Girl",
        "They say today's rain is going to clear in the afternoon.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Girl",
        "Uh uh, maybe we could see the rainbow too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FC3")

    label("loc_2F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FC3")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Uh uh, I wonder why the city in\x01",
            "the rain tickles my heart this much.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "This sorrowful atmosphere is\x01",
            "so emotionally unbearable...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC3")

    TalkEnd(0xFE)
    Return()

    # Function_29_2E97 end

    def Function_30_2FC7(): pass

    label("Function_30_2FC7")

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

    # Function_30_2FC7 end

    def Function_31_307B(): pass

    label("Function_31_307B")

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

    # Function_31_307B end

    def Function_32_340C(): pass

    label("Function_32_340C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3444"),
        (1, "loc_344C"),
        (2, "loc_3454"),
        (3, "loc_345C"),
        (4, "loc_3464"),
        (5, "loc_346C"),
        (6, "loc_3474"),
        (SWITCH_DEFAULT, "loc_347C"),
    )


    label("loc_3444")

    Sleep(200)
    Jump("loc_3484")

    label("loc_344C")

    Sleep(400)
    Jump("loc_3484")

    label("loc_3454")

    Sleep(600)
    Jump("loc_3484")

    label("loc_345C")

    Sleep(800)
    Jump("loc_3484")

    label("loc_3464")

    Sleep(1000)
    Jump("loc_3484")

    label("loc_346C")

    Sleep(1200)
    Jump("loc_3484")

    label("loc_3474")

    Sleep(1400)
    Jump("loc_3484")

    label("loc_347C")

    Sleep(1600)
    Jump("loc_3484")

    label("loc_3484")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34AF")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(1000)
    Jump("loc_3484")

    label("loc_34AF")

    Return()

    # Function_32_340C end

    def Function_33_34B0(): pass

    label("Function_33_34B0")

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

    # Function_33_34B0 end

    def Function_34_35AD(): pass

    label("Function_34_35AD")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -30000, 10000, 60000)
    OP_9F(0x1, 5000, 10000, 50000)
    OP_9F(0x1, 20000, 12000, 0)
    OP_9F(0x2, 0xFE, 14000, 0x7)
    Return()

    # Function_34_35AD end

    def Function_35_35E5(): pass

    label("Function_35_35E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3610")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(1000)
    Jump("Function_35_35E5")

    label("loc_3610")

    Return()

    # Function_35_35E5 end

    def Function_36_3611(): pass

    label("Function_36_3611")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Return()

    # Function_36_3611 end

    def Function_37_364E(): pass

    label("Function_37_364E")

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

    # Function_37_364E end

    def Function_38_367F(): pass

    label("Function_38_367F")

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
        "#11PA-Amazing...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#11PThat building was finally finished\x01",
            "with the IBC support!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#11PWho would've thought such a nice\x01",
            "building could be constructed...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#11PAs I thought, Mayor Dieter\x01",
            "is one to do too huge things!\x02",
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
            "#6PHey, Henri!\x01",
            "Let's go explore it, explore!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x25, 500)

    ChrTalk(
        0x26,
        "#11PT-They'll get angry at us again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#11PWell...\x01",
            "I guess I get how you feel.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BDD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_3BDD)
    Sleep(50)

    def lambda_3BED():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_3BED)

    ChrTalk(
        0x27,
        "#11P...I-Incredible...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3CD1")

    ChrTalk(
        0x28,
        (
            "#12PI-Indeed, it's a cool building...\x01",
            "Impossible to think something like that in Calvard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12PHmm, I feel I understand why our\x01",
            "guys are fussing over this city...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D85")

    label("loc_3CD1")


    NpcTalk(
        0x28,
        "Boy",
        (
            "#12PI-Indeed, it's a cool building...\x01",
            "Impossible to think something like that in Calvard!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x28,
        "Boy",
        (
            "#12PHmm, I feel I understand why our\x01",
            "guys are fussing over this city...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D85")

    OP_68(-13300, 700, 7000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x2A,
        (
            "#12P#06000FHeehee...\x01",
            "Everyone is really excited.\x02\x03",
            "#06002FHey, hey KeA.\x01",
            "Is it a building that much big?\x02",
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
            "#5P#06005FKeA...?\x01",
            "You're there, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x2B, 0x2A, 500)

    ChrTalk(
        0x2B,
        (
            "#11P#01109FAh──sorry, Shizuku.\x02\x03",
            "#01110FEhm, it's incredibly big!\x02\x03",
            "The azure and white colors are pretty too,\x01",
            "and it's slender and cool!\x02\x03",
            "#01108F#30W...But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#5P#06008F? Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#11P#01102FAh... \x01",
            "No, it's nothing.\x02",
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
            "#01106F#3603V#40W#12P#N(I wonder what is it...\x01",
            "It's my first time seeing it, and yet...)\x02\x03",
            "#01112F#3604V#30W(That building, KeA...\x01",
            "Feels like she has seen it once somewhere.)\x02",
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

    # Function_38_367F end

    def Function_39_40DE(): pass

    label("Function_39_40DE")

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
            "#03204F#11PHu hu...\x01",
            "I am glad you came quickly.\x01\x02",
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

    def lambda_4365():
        OP_95(0xFE, -12600, -200, 3900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4365)
    Sleep(300)

    def lambda_4382():
        OP_95(0xFE, -12200, -200, 2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4382)
    Sleep(600)

    def lambda_439F():
        OP_95(0xFE, -11500, -200, 3700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_439F)
    Sleep(600)

    def lambda_43BC():
        OP_95(0xFE, -10200, -200, 3800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43BC)
    Sleep(300)

    def lambda_43D9():
        OP_95(0xFE, -10200, -200, 2800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43D9)
    WaitChrThread(0x101, 1)

    def lambda_43F7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43F7)
    WaitChrThread(0x103, 1)

    def lambda_4408():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4408)
    WaitChrThread(0x102, 1)

    def lambda_4419():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4419)
    WaitChrThread(0x109, 1)

    def lambda_442A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_442A)
    WaitChrThread(0x105, 1)

    def lambda_443B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_443B)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00001FMr. Cao...\x01",
            "Are you ok alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#12PMr. ...Lau, was he?\x01",
            "Where's the bodyguard\x01",
            "who's always with you?\x02",
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
            "Hu hu, since we became a little\x01",
            "busy, I'm making him do many\x01",
            "kinds of arrangements.\x02\x03",
            "By the way, those vicious\x01",
            "persons have gone away\x01",
            "from the city, right?\x02\x03",
            "Thus, it means I too\x01",
            "can triumphantly walk\x01",
            "under the blue sky.\x02",
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
        "#12P#00211F...Shady as alway.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAlthough I think the blue sky doesn't suit you,\x01",
            "the youngest manager of all in the "Heiyue".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03209FHa ha, that is true.\x02\x03",
            "#03200F──You and I have no time to waste,\x01",
            "so allow me to get to the main topic.\x02\x03",
            "#03206FThe truth is, last night I received\x01",
            "a sudden notice from Master "Yin".\x02\x03",
            "The Master came to say that he is closing the\x01",
            "long-time contract he had with us "Heiyue".\x02",
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
            "#5P#03201FMy, that really shocked me.\x02\x03",
            "I somehow tried to stop him,\x01",
            "but he was very obstinate...\x02\x03",
            "#03206FI was greatly perplexed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003F...Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FAnd what that has got\x01",
            "to do with us...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03202F──What on earth happened at\x01",
            "Elm Lake south bank yesterday?\x02",
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
            "#12P#10301FIt looks like you already caught\x01",
            "wind that we were together, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03204FYes, and that the Bracer Guild\x01",
            "and the "Snake" persons\x01",
            "showed up too.\x02\x03",
            "#03201FWhat on earth has happened\x01",
            "to Master "Yin"?\x02",
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
            "#00103F#12P...I think we have no obligation\x01",
            "to tell you about it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03202FSo that means something has\x01",
            "really happened to her, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00110F#12P......!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00006F...It's no use, Elie.\x01",
            "He's not your common opponent.\x02\x03",
            "#00011FIf we ineptly talk, then information──ah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FOh boy.\x01",
            "You're quite the crafty one, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03209FHu hu, so as I suspected\x01",
            "master "Yin" is a woman, hm?\x02\x03",
            "#03210FI suppose that she used a\x01",
            "superhuman neigong to alter\x01",
            "her qi and figure, am I right?\x02\x03",
            "#03204FHaving that much physical abilities, even\x01",
            "her success on the stage is understandable.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2D, 500)

    ChrTalk(
        0x101,
        "#12P#00010FKh......\x02",
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
            "#5P#03204FWell, since I was very interested,\x01",
            "I researched the Arc-en-ciel \x01",
            "members' schedule before.\x02\x03",
            "#03210FThen, when Master "Yin"\x01",
            "refused our jobs, it coincided\x01",
            "with public performance days...\x02\x03",
            "Dear me, thanks to you all,\x01",
            "I finally had conviction.\x02",
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
            "#5P#03205F──For now, nothing.\x02\x03",
            "#03209FWell, since I'm the only one\x01",
            "who discovered her identity, I\x01",
            "thought to threaten her too, but...\x02\x03",
            "#03202FSince there were also people of the\x01",
            "Guild involved, it's not that I can\x01",
            "silence you all here.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x109,
        "#10110F......!\x02",
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
            "#12P#00003F...If this is what you only have to say,\x01",
            "we'll excuse us, since we're busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03204FHu hu, come on, don't say that.\x02\x03",
            "#03210F─As thank you for the information you provided me,\x01",
            "I will offer you some welcome news.\x02\x03",
            "Mr. ...Randy, was he...?\x01",
            "It appears that he visited a certain place of\x01",
            "Mainz Mountain Path about three hours ago.\x02",
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
            "#5P#03204FWe have a specialized monitoring unit\x01",
            "for the "Red Constellation" movements.\x02\x03",
            "#03200FThe information came from them.\x02",
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
        "#00107F#12PSo, what about the place in question?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#5P#03203FBefore the waterfall where the CGF have\x01",
            "spreaded their defense line at present...\x02\x03",
            "#03201FHe descended below the cliff with a rope,\x01",
            "from a high ground point nearby.\x02\x03",
            "After that, since it seems he noticed them,\x01",
            "they say they gave up pursuing him.\x02",
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
            "#12P#00004FYeah, this is an extremely useful info.\x02\x03",
            "#00000F──Mr. Cao, thank you...!\x01\x02",
        )
    )

    CloseMessageWindow()

    def lambda_54FE():
        TurnDirection(0xFE, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_54FE)

    ChrTalk(
        0x2D,
        (
            "#5P#03200FHu hu, if you do your best,\x01",
            "we will benefit too.\x02\x03",
            "#03204FWell, please be careful to not\x01",
            "die together with Mr. Randy.\x02\x03",
            "#03210F──"They" are strong, very.\x02",
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
            "#5P#00007FAlright, let's contact Chief via ENIGMA and \x01",
            "immediately set out to Mainz Mountain Path.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5645():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5645)
    Sleep(50)

    def lambda_5655():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5655)
    Sleep(50)

    def lambda_5665():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5665)
    Sleep(50)

    def lambda_5675():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5675)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x103,
        "#12P#00201FYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PWe must catch up to him in some way...!\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_56FD():

        label("loc_56FD")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_56FD")

    QueueWorkItem2(0x2D, 2, lambda_56FD)
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
            "#03204F#5PHa ha... Every now and then, even\x01",
            "such immatureness is not bad.\x02\x03",
            "#03200FWell then── \x02",
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
            "#03203F#11PThis is a critical situation, eh?\x02\x03",
            "#03202F──It appears that I too will need to\x01",
            "bring all of our abilities into play.\x02",
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

    # Function_39_40DE end

    def Function_40_5921(): pass

    label("Function_40_5921")


    def lambda_5926():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5926)

    def lambda_5940():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5940)
    WaitChrThread(0xFE, 1)

    def lambda_5955():
        OP_95(0xFE, 10500, -200, -3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5955)
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

    # Function_40_5921 end

    def Function_41_59F7(): pass

    label("Function_41_59F7")


    def lambda_59FC():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59FC)

    def lambda_5A16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A16)
    WaitChrThread(0xFE, 1)

    def lambda_5A2B():
        OP_95(0xFE, 12000, -200, -3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A2B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_41_59F7 end

    def Function_42_5A4C(): pass

    label("Function_42_5A4C")


    def lambda_5A51():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A51)

    def lambda_5A6B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A6B)
    WaitChrThread(0xFE, 1)

    def lambda_5A80():
        OP_95(0xFE, 10500, -200, -2300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A80)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_42_5A4C end

    def Function_43_5AA1(): pass

    label("Function_43_5AA1")


    def lambda_5AA6():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AA6)

    def lambda_5AC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5AC0)
    WaitChrThread(0xFE, 1)

    def lambda_5AD5():
        OP_95(0xFE, 12000, -200, -2300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AD5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_43_5AA1 end

    def Function_44_5AF6(): pass

    label("Function_44_5AF6")


    def lambda_5AFB():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AFB)

    def lambda_5B15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5B15)
    WaitChrThread(0xFE, 1)

    def lambda_5B2A():
        OP_95(0xFE, 11800, -200, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B2A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_44_5AF6 end

    def Function_45_5B4B(): pass

    label("Function_45_5B4B")

    OP_92(0xFE, 0x1388, 0xFFFFF830, 0x1F4)

    def lambda_5B5D():
        OP_95(0xFE, 5000, -200, -2000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B5D)
    WaitChrThread(0xFE, 1)

    def lambda_5B7B():
        OP_95(0xFE, 10000, -200, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B7B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_5B4B end

    def Function_46_5B95(): pass

    label("Function_46_5B95")

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

    def lambda_5D95():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D95)
    Sleep(50)

    def lambda_5DA5():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DA5)
    Sleep(50)

    def lambda_5DB5():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5DB5)
    Sleep(50)

    def lambda_5DC5():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5DC5)
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
            "#03506F*whistle*...\x02\x03",
            "#03510F...Man, Crossbell is\x01",
            "really incomprehensible.\x02",
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

    def lambda_5FED():
        OP_98(0x101, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FED)
    Sleep(50)

    def lambda_600A():
        OP_98(0x102, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_600A)
    Sleep(50)

    def lambda_6027():
        OP_98(0x109, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6027)
    Sleep(50)

    def lambda_6044():
        OP_98(0x105, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6044)
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
            "#6P#00001F...Somehow I understand\x01",
            "what you want to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F──Its nickname is "Orchis Tower".\x02\x03",
            "It's the world's first super\x01",
            "high-rise building, being 250\x01",
            "arge above ground and 40 stories.\x02\x03",
            "#00100FIn addition to the new City Hall, it\x01",
            "has a floor for enterprises, a room for\x01",
            "international conferences and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FIndeed a masterpiece...\x02\x03",
            "#10100FAlthough we are so far from it,\x01",
            "it looks that big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, since it's still covered,\x01",
            "I don't know what design it has, but...\x02\x03",
            "#10302FThey say it's basically completed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, it seems that half of the hall\x01",
            "employees have already moved there.\x02\x03",
            "#00004FAlthough the actual unveiling of the\x01",
            "building is going to take place at\x01",
            "the time of the Trade Conference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#6P#03500FSo he plans to take aback the\x01",
            "VIPs who're going to be there, eh?\x02\x03",
            "#03506FBoy oh boy.\x01",
            "Dieter Crois is a more talented\x01",
            "man than I thought him to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F............\x02\x03",
            "#00001F──I will ask this as Crossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "Mr. Lechter Arundel.\x01",
            "Please cooperate to confirm your identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#6P#03504FEh eh...\x02\x03",
            "#03500FHow diligent.\x01",
            "──And if I said I don't want to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F...It's true that in Crossbell, legal binding force\x01",
            "can't be exercised towards persons connected\x01",
            "to the Imperial and Republican governments.\x02\x03",
            "#00101FHowever, that is only in case we clearly\x01",
            "know someone's identity, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FConversely, if it's not clear, you\x01",
            "can be examined at the same\x01",
            "level of a common foreigner...\x02\x03",
            "#10300FI see, is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "#6P#03504FHm, so it's come, eh?\x02",
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
            "...It can't be helped.\x01",
            "It looks like the time of\x01",
            "reckoning has arrived.\x02\x03",
            "Okay, I'm affiliated to──\x02",
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
        "#6P#03505FHmm...?\x02",
    )

    CloseMessageWindow()

    def lambda_67C4():
        OP_93(0x101, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67C4)
    Sleep(50)

    def lambda_67D4():
        OP_93(0x102, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_67D4)
    Sleep(50)

    def lambda_67E4():
        OP_93(0x109, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_67E4)
    Sleep(50)

    def lambda_67F4():
        OP_93(0x105, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_67F4)
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
            "#N#03505FYes, the buildings over there.\x02\x03",
            "#03506F...Wasn't the black shadow of a man\x01",
            "skipping around the rooftops...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#N#00011FWhat...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#N#11P#00105FD-Don't tell me that...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#N#11P#10305FEeh, could it be\x01",
            "that "Yin" guy?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#N#11P#10105FB-But...\x01",
            "Isn't it daytime?\x02",
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
        "#10111FAAAH!?\x02",
    )

    CloseMessageWindow()

    def lambda_6A95():
        OP_93(0x101, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A95)
    Sleep(50)

    def lambda_6AA5():
        OP_93(0x102, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6AA5)
    Sleep(50)

    def lambda_6AB5():
        OP_93(0x105, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6AB5)

    ChrTalk(
        0x101,
        "#00011FD-Damn!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6AF1():
        OP_95(0x101, -16360, -200, 4810, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AF1)
    Sleep(100)

    def lambda_6B0E():
        OP_95(0x102, -16360, -200, 6110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6B0E)
    Sleep(50)

    def lambda_6B2B():
        OP_95(0x109, -15060, -200, 4810, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B2B)
    Sleep(50)

    def lambda_6B48():
        OP_95(0x105, -15060, -200, 6110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6B48)
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

    def lambda_6BED():
        OP_95(0x101, -16180, -200, 5770, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BED)
    Sleep(100)

    def lambda_6C0A():
        OP_95(0x102, -16149, -200, 6900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C0A)
    Sleep(50)

    def lambda_6C27():
        OP_95(0x109, -14800, -200, 5880, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C27)
    Sleep(50)

    def lambda_6C44():
        OP_95(0x105, -15150, -200, 6830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C44)
    WaitChrThread(0x102, 1)

    def lambda_6C62():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C62)
    WaitChrThread(0x105, 1)

    def lambda_6C73():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C73)
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
            "#5P#00105FN-No way, did he go\x01",
            "down here with this rope!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FI-Incredible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FAhaha!\x01",
            "What an absurd thing to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FKh...to think that he was an opponent to\x01",
            "whom common sense doesn't apply that much...\x02\x03",
            "#00007FBack Street is below here!\x01",
            "Anyway, let's go down using the stairs!\x02",
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

    # Function_46_5B95 end

    def Function_47_6E40(): pass

    label("Function_47_6E40")


    def lambda_6E45():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E45)

    def lambda_6E56():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E56)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 6830, -200, -3780, 2000, 0x0)
    Return()

    # Function_47_6E40 end

    def Function_48_6E84(): pass

    label("Function_48_6E84")


    def lambda_6E89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6E89)

    def lambda_6E9A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E9A)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 8000, -200, -4990, 2000, 0x0)
    Return()

    # Function_48_6E84 end

    def Function_49_6EC8(): pass

    label("Function_49_6EC8")


    def lambda_6ECD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6ECD)

    def lambda_6EDE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6EDE)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 8850, -200, -3200, 2000, 0x0)
    Return()

    # Function_49_6EC8 end

    def Function_50_6F0C(): pass

    label("Function_50_6F0C")


    def lambda_6F11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6F11)

    def lambda_6F22():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F22)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 9880, -200, -4810, 2000, 0x0)
    Return()

    # Function_50_6F0C end

    def Function_51_6F50(): pass

    label("Function_51_6F50")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_701C")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x104, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_7113")

    label("loc_701C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_709A")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x109, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_7113")

    label("loc_709A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_7113")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x105, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_7113")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_717E")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 55)
    Jump("loc_71F9")

    label("loc_717E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_71BE")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 56)
    Jump("loc_71F9")

    label("loc_71BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_71F9")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 57)

    label("loc_71F9")

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
            "#6PThis is the department store rooftop...\x01",
            "Eeh, isn't this quite the view?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*, amazing, right? From here, you can\x01",
            "take an extensive view of the entire city.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#5PYes, it's more than I thought!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11POh, right, the Orchis Tower...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_737D")

    def lambda_7347():

        label("loc_7347")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_7347")

    QueueWorkItem2(0x101, 1, lambda_7347)

    def lambda_7359():

        label("loc_7359")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_7359")

    QueueWorkItem2(0x102, 1, lambda_7359)

    def lambda_736B():

        label("loc_736B")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_736B")

    QueueWorkItem2(0x104, 1, lambda_736B)
    Jump("loc_7400")

    label("loc_737D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_73C1")

    def lambda_738B():

        label("loc_738B")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_738B")

    QueueWorkItem2(0x101, 1, lambda_738B)

    def lambda_739D():

        label("loc_739D")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_739D")

    QueueWorkItem2(0x102, 1, lambda_739D)

    def lambda_73AF():

        label("loc_73AF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_73AF")

    QueueWorkItem2(0x109, 1, lambda_73AF)
    Jump("loc_7400")

    label("loc_73C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_7400")

    def lambda_73CF():

        label("loc_73CF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_73CF")

    QueueWorkItem2(0x101, 1, lambda_73CF)

    def lambda_73E1():

        label("loc_73E1")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_73E1")

    QueueWorkItem2(0x102, 1, lambda_73E1)

    def lambda_73F3():

        label("loc_73F3")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_73F3")

    QueueWorkItem2(0x105, 1, lambda_73F3)

    label("loc_7400")


    def lambda_7405():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_7405)
    Sleep(500)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_7437")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    Jump("loc_746E")

    label("loc_7437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_7455")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    Jump("loc_746E")

    label("loc_7455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_746E")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x105, 0x1)

    label("loc_746E")

    Fade(500)
    OP_68(-8320, 2600, 1920, 0)
    MoveCamera(26, -1, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7370, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_7564")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x104, -1960, -200, 110, 0)

    def lambda_74F3():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_74F3)
    Sleep(50)

    def lambda_7510():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7510)
    Sleep(50)

    def lambda_752D():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_752D)
    Sleep(50)

    def lambda_754A():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_754A)
    Jump("loc_76E5")

    label("loc_7564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_7627")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x109, -1960, -200, 110, 0)

    def lambda_75B6():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_75B6)
    Sleep(50)

    def lambda_75D3():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75D3)
    Sleep(50)

    def lambda_75F0():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75F0)
    Sleep(50)

    def lambda_760D():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_760D)
    Jump("loc_76E5")

    label("loc_7627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_76E5")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x105, -1960, -200, 110, 0)

    def lambda_7679():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_7679)
    Sleep(50)

    def lambda_7696():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7696)
    Sleep(50)

    def lambda_76B3():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76B3)
    Sleep(50)

    def lambda_76D0():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_76D0)

    label("loc_76E5")

    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x1A2,
        "Is that it...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It's still enveloped by the veil,\x01",
            "but that presence is amazing!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5PCome on, come on, Miss Elie,\x01",
            "more to the front, and more near me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F*sigh*, please be very careful\x01",
            "to not fall down.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1620, -2300, 8900, 0)
    MoveCamera(48, 26, 2, 0)
    OP_6E(700, 0)
    SetCameraDistance(20270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_7880")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x104, -1960, -200, 3110, 0)
    Jump("loc_791F")

    label("loc_7880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_78D2")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x109, -1960, -200, 3110, 0)
    Jump("loc_791F")

    label("loc_78D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_791F")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x105, -1960, -200, 3110, 0)

    label("loc_791F")

    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00000FSo, were you satisfied with\x01",
            "the scenery from the rooftop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Yeah, satisfied.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Even your guide of the city\x01",
            "was not bad at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "How to say it... It seems\x01",
            "it'll become a good memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FI see, telling us this\x01",
            "makes us glad.\x02",
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
            "I have plans to return to Calvard\x01",
            "on the day after tomorrow's morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Then, I'll once again be\x01",
            "surrounded by adults and\x01",
            "every day fixed studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "That's the fate of someone\x01",
            "who will be useful to others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FShing...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_7B79")

    ChrTalk(
        0x104,
        "#00303F...Hm, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7BBF")

    label("loc_7B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_7BA0")

    ChrTalk(
        0x109,
        "#10103F...I get it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7BBF")

    label("loc_7BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_7BBF")

    ChrTalk(
        0x105,
        "#10303F...I see.\x02",
    )

    CloseMessageWindow()

    label("loc_7BBF")


    ChrTalk(
        0x101,
        (
            "#12P#00000FBy the way, Shing, are you\x01",
            "going to Sunday School?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "Yeah, in order to broaden my\x01",
            "information, more or less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Well, everyone fears the adults\x01",
            "surrounding me, so they don't\x01",
            "even try to approach me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_END)), "loc_7D4F")

    ChrTalk(
        0x1A2,
        (
            "So that's why...\x01",
            "KeA and Shizuku, were they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "To be able to talk to children like\x01",
            "them was quite refreshing and fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FHa ha, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D68")

    label("loc_7D4F")


    ChrTalk(
        0x101,
        "#12P#00008FShing...\x02",
    )

    CloseMessageWindow()

    label("loc_7D68")


    ChrTalk(
        0x1A2,
        (
            "...Well, I ended up doing\x01",
            "a worthless conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "At any rate, I had plenty of touring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Now escort me to the office.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, all right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 4)
    SetScenarioFlags(0x22, 5)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_6F50 end

    def Function_52_7E2A(): pass

    label("Function_52_7E2A")


    def lambda_7E2F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_7E2F)

    def lambda_7E40():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_7E40)
    WaitChrThread(0x1A2, 1)
    OP_95(0x1A2, 14590, -200, -3020, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_52_7E2A end

    def Function_53_7E75(): pass

    label("Function_53_7E75")


    def lambda_7E7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7E7A)

    def lambda_7E8B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E8B)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 13970, -200, -4930, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_53_7E75 end

    def Function_54_7EC0(): pass

    label("Function_54_7EC0")


    def lambda_7EC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EC5)

    def lambda_7ED6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7ED6)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 13740, -200, -1810, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_54_7EC0 end

    def Function_55_7F0B(): pass

    label("Function_55_7F0B")


    def lambda_7F10():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7F10)

    def lambda_7F21():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7F21)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_55_7F0B end

    def Function_56_7F56(): pass

    label("Function_56_7F56")


    def lambda_7F5B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7F5B)

    def lambda_7F6C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7F6C)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_56_7F56 end

    def Function_57_7FA1(): pass

    label("Function_57_7FA1")


    def lambda_7FA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7FA6)

    def lambda_7FB7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7FB7)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_57_7FA1 end

    SaveToFile()

Try(main)
