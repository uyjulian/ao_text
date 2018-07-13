from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0450.bin",                # FileName
        "c0450",                    # MapName
        "c0450",                    # Location
        0x0024,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 36, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0450",                  # 0
        "Receptionist Kyle",      # 1
        "Doris",                  # 2
        "Aaron",                  # 3
        "Manager Laetitia",       # 4
        "Minneth",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Citizen",                # 8
        "Girl",                   # 9
        "Citizen",                # 10
        "Citizen",                # 11
        "Tourist",                # 12
        "Citizen",                # 13
        "Citizen",                # 14
        "Citizen",                # 15
        "Derrick",                # 16
    ))

    AddCharChip((
        "chr/ch45200.itc",                   # 00
        "chr/ch22000.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch27500.itc",                   # 03
        "chr/ch27900.itc",                   # 04
        "chr/ch33002.itc",                   # 05
        "chr/ch32402.itc",                   # 06
        "chr/ch22002.itc",                   # 07
        "chr/ch22300.itc",                   # 08
        "chr/ch24400.itc",                   # 09
        "chr/ch21300.itc",                   # 0A
        "chr/ch33000.itc",                   # 0B
        "chr/ch21002.itc",                   # 0C
        "chr/ch20302.itc",                   # 0D
        "chr/ch23800.itc",                   # 0E
    ))

    DeclNpc(65440,   0,       59970,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4090,    9,       59900,   225,  261,  0x0, 0,   2,   0,   0,   2,   0,   15,  255,  0)
    DeclNpc(50740,   0,       9750,    90,   261,  0x0, 0,   3,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(4294963306, 0,       7000,    90,   261,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(168410,  0,       5519,    180,  389,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(60049,   150,     65010,   180,  389,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(61630,   150,     65010,   180,  389,  0x0, 0,   6,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(189949,  500,     58349,   90,   389,  0x0, 0,   7,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(190759,  0,       61840,   45,   389,  0x0, 0,   8,   0,   0,   4,   0,   19,  255,  0)
    DeclNpc(153649,  0,       61220,   180,  389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(153639,  0,       60250,   0,    389,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(115000,  0,       62779,   0,    389,  0x0, 0,   11,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(112550,  500,     6699,    0,    389,  0x0, 0,   12,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(112550,  500,     9300,    180,  389,  0x0, 0,   13,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(115000,  0,       8409,    45,   389,  0x0, 0,   14,  0,   0,   5,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(68130,   10,      11650,   1200,    68130,   1500,    11650,   0x007C, 0,  26, 0x0000)
    DeclActor(4294963796, 0,       7000,    1500,    4294963306, 1500,    7000,    0x007E, 0,  10, 0x0000)
    DeclActor(64300,   0,       59970,   1500,    65440,   1500,    59970,   0x007E, 0,  12, 0x0000)
    DeclActor(117500,  0,       4000,    1200,    117500,  650,     4000,    0x007C, 0,  8,  0x0000)
    DeclActor(68130,   10,      11650,   1200,    68130,   1500,    11650,   0x007C, 0,  27, 0x0000)

    ChipFrameInfo(1008, 0)                                       # 0

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_4A0",          # 01, 1
        "Function_2_501",          # 02, 2
        "Function_3_52C",          # 03, 3
        "Function_4_557",          # 04, 4
        "Function_5_582",          # 05, 5
        "Function_6_5AD",          # 06, 6
        "Function_7_735",          # 07, 7
        "Function_8_8DA",          # 08, 8
        "Function_9_9AF",          # 09, 9
        "Function_10_B5E",         # 0A, 10
        "Function_11_B62",         # 0B, 11
        "Function_12_21A7",        # 0C, 12
        "Function_13_21AB",        # 0D, 13
        "Function_14_334A",        # 0E, 14
        "Function_15_42C8",        # 0F, 15
        "Function_16_4DBD",        # 10, 16
        "Function_17_4EDB",        # 11, 17
        "Function_18_5009",        # 12, 18
        "Function_19_50B9",        # 13, 19
        "Function_20_5123",        # 14, 20
        "Function_21_5152",        # 15, 21
        "Function_22_517C",        # 16, 22
        "Function_23_5311",        # 17, 23
        "Function_24_53B4",        # 18, 24
        "Function_25_543F",        # 19, 25
        "Function_26_546A",        # 1A, 26
        "Function_27_549F",        # 1B, 27
        "Function_28_54CC",        # 1C, 28
        "Function_29_6233",        # 1D, 29
        "Function_30_80AC",        # 1E, 30
        "Function_31_80F7",        # 1F, 31
        "Function_32_813B",        # 20, 32
        "Function_33_8186",        # 21, 33
        "Function_34_81D1",        # 22, 34
        "Function_35_821C",        # 23, 35
        "Function_36_8267",        # 24, 36
        "Function_37_82B2",        # 25, 37
        "Function_38_82FD",        # 26, 38
        "Function_39_8348",        # 27, 39
        "Function_40_8393",        # 28, 40
        "Function_41_83DE",        # 29, 41
        "Function_42_8429",        # 2A, 42
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_428"),
        (1, "loc_434"),
        (2, "loc_440"),
        (3, "loc_44C"),
        (4, "loc_458"),
        (5, "loc_464"),
        (6, "loc_470"),
        (SWITCH_DEFAULT, "loc_47C"),
    )


    label("loc_428")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_434")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_440")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_44C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_458")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_464")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_470")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_47C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_488")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_49F")

    Return()

    # Function_0_3F0 end

    def Function_1_4A0(): pass

    label("Function_1_4A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_500")
    OP_95(0xFE, 72280, 0, 9750, 1000, 0x0)
    OP_95(0xFE, 72280, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 9750, 1000, 0x0)
    Jump("Function_1_4A0")

    label("loc_500")

    Return()

    # Function_1_4A0 end

    def Function_2_501(): pass

    label("Function_2_501")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52B")
    OP_94(0xFE, 0x604, 0xD714, 0x17C0, 0xFB9A, 0x3E8)
    Sleep(300)
    Jump("Function_2_501")

    label("loc_52B")

    Return()

    # Function_2_501 end

    def Function_3_52C(): pass

    label("Function_3_52C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_556")
    OP_94(0xFE, 0xFAD1, 0x141E, 0x11B66, 0x2652, 0x3E8)
    Sleep(300)
    Jump("Function_3_52C")

    label("loc_556")

    Return()

    # Function_3_52C end

    def Function_4_557(): pass

    label("Function_4_557")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_581")
    OP_94(0xFE, 0x2E158, 0xEA92, 0x2F5B2, 0xF604, 0x3E8)
    Sleep(300)
    Jump("Function_4_557")

    label("loc_581")

    Return()

    # Function_4_557 end

    def Function_5_582(): pass

    label("Function_5_582")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AC")
    OP_94(0xFE, 0x1BEC2, 0x1E0A, 0x1C6E2, 0x2AD0, 0x3E8)
    Sleep(300)
    Jump("Function_5_582")

    label("loc_5AC")

    Return()

    # Function_5_582 end

    def Function_6_5AD(): pass

    label("Function_6_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BB")
    Jump("loc_734")

    label("loc_5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_624")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0xD)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jump("loc_734")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_632")
    Jump("loc_734")

    label("loc_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_640")
    Jump("loc_734")

    label("loc_640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_64E")
    Jump("loc_734")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_65C")
    Jump("loc_734")

    label("loc_65C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_66A")
    Jump("loc_734")

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_678")
    Jump("loc_734")

    label("loc_678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_69B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_696")
    ClearChrFlags(0xC, 0x80)

    label("loc_696")

    Jump("loc_734")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A9")
    Jump("loc_734")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6B7")
    Jump("loc_734")

    label("loc_6B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C5")
    Jump("loc_734")

    label("loc_6C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6FF")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    Jump("loc_734")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_734")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)

    label("loc_734")

    Return()

    # Function_6_5AD end

    def Function_7_735(): pass

    label("Function_7_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_751")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CF")

    label("loc_751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CF")

    label("loc_76D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_780")
    Jump("loc_7CF")

    label("loc_780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CF")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CF")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7CF")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FD")
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x0, 0x1)

    label("loc_7FD")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82C")
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x4, 0x1)

    label("loc_82C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_84B")
    OP_10(0x0, 0x0)
    OP_10(0x12, 0x1)
    OP_10(0x11, 0x0)
    OP_10(0x13, 0x1)
    Jump("loc_857")

    label("loc_84B")

    OP_10(0x0, 0x1)
    OP_10(0x12, 0x0)
    OP_10(0x11, 0x1)
    OP_10(0x13, 0x0)

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_89D")
    SetMapObjFrame(0xFF, "hikari00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c0450:Layer15", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_89D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D9")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c0450:Layer15", 0x0, 0x1)

    label("loc_8D9")

    Return()

    # Function_7_735 end

    def Function_8_8DA(): pass

    label("Function_8_8DA")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The "Delicious Hot Pot Dishes\x01",
            "Pressure Cooker Edition" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_9AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Satiating Hot Pot"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_9AB")

    TalkEnd(0xFF)
    Return()

    # Function_8_8DA end

    def Function_9_9AF(): pass

    label("Function_9_9AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAE")

    ChrTalk(
        0xC,
        (
            "Oh, everyone...\x01",
            "Do you still need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My Quincy Company and Armorica Village\x01",
            ""Armorica Honey Company" plan is\x01",
            "progressing steadily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I would be glad if you looked forward\x01",
            "to our success too, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B5A")

    label("loc_AAE")


    ChrTalk(
        0xC,
        (
            "My Quincy Company and Armorica Village\x01",
            ""Armorica Honey Company" plan is\x01",
            "progressing steadily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I would be glad if you looked forward\x01",
            "to our success too, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5A")

    TalkEnd(0xFE)
    Return()

    # Function_9_9AF end

    def Function_10_B5E(): pass

    label("Function_10_B5E")

    Call(0, 11)
    Return()

    # Function_10_B5E end

    def Function_11_B62(): pass

    label("Function_11_B62")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E25")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "My, you're the police's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. Can we ask\x01",
            "your situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes. Right now, we have taken in both\x01",
            "the guests who were already lodging\x01",
            "here and a great number of evacuees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We have reserve food available too, so we\x01",
            "should be able to last about a month, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In any case, not knowing\x01",
            "the details of the situation\x01",
            "is adding to the anxiety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For now, we have kept the chaos to\x01",
            "a minimum, but if this goes on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FWe'll immediately begin to act\x01",
            "to resolve this situation.\x02\x03",
            "So we'd like you to keep an eye\x01",
            "on things for a while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, understood. Please take\x01",
            "care of yourselves, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 6)

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FB1")

    ChrTalk(
        0xB,
        "Welcome to "Hotel Millennium".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhuhu. At this hotel,\x01",
            "we handle any needs\x01",
            "a guest may have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you would like to stay with us,\x01",
            "please just say the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you stay at a hotel or a\x01",
            "bar-inn, you can recover CP.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A normal bar-inn sets CP to 100,\x01",
            "and the high-class hotels set it to 200.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAE")
    SetScenarioFlags(0x0, 0)

    label("loc_FAE")

    SetScenarioFlags(0x136, 5)

    label("loc_FB1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21A3")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Rest\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_100B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_100B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102B")
    OP_AF(0x45)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_219E")

    label("loc_102B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_103F")
    Jump("loc_219E")

    label("loc_103F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_219E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11AC")

    ChrTalk(
        0xB,
        (
            "We got the info on the President's\x01",
            "restriction, and the evacuees\x01",
            "have returned to their homes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The details regarding that huge tree are unclear,\x01",
            "but for now the mist has cleared up, and the\x01",
            "impression is that the city is settling down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, we have to make all\x01",
            "kinds of preparations now,\x01",
            "while we still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_11AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1402")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134E")

    ChrTalk(
        0xB,
        (
            "When the martial law and the movement restrictions\x01",
            "were made known, we immediately considered\x01",
            "taking in evacuees, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As you can imagine, that mist and those\x01",
            "doll soldiers were outside our expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems everyone's opposition to the\x01",
            "President couldn't be any greater, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If pushed, I would say that the impression\x01",
            "I have is that there is great uneasiness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FD")

    label("loc_134E")


    ChrTalk(
        0xB,
        (
            "It seems everyone's opposition to the\x01",
            "President couldn't be any greater, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If pushed, I would say that the impression\x01",
            "I have is that there is great uneasiness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FD")

    Jump("loc_219E")

    label("loc_1402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_15F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150E")

    ChrTalk(
        0xB,
        (
            "I saw the President's\x01",
            "address through the hotel's\x01",
            "orbal net connection...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As expected, it was probably\x01",
            "very disturbing to our guests\x01",
            "from outside the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think it's best if they all return\x01",
            "to their home countries, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15F0")

    label("loc_150E")


    ChrTalk(
        0xB,
        (
            "It seems orbal rail service\x01",
            "was shut down today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Our guests have no way to go back, so\x01",
            "going home now is out of the question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We can't obtain thorough information,\x01",
            "including the airships operations situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F0")

    Jump("loc_219E")

    label("loc_15F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_16E5")

    ChrTalk(
        0xB,
        (
            "The Entertainment District dyed in the colors\x01",
            "of twilight and flames... I can only say that\x01",
            "the scene of that day was truly a nightmare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Anyway, I must do\x01",
            "everything I can to restore\x01",
            "normalcy as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_16E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1778")

    ChrTalk(
        0xB,
        (
            "It seems the CGF are\x01",
            "fighting hard in the\x01",
            "Mainz region even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We citizens can be proud of\x01",
            "the men and women of the CGF.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_1778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_195D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D1")

    ChrTalk(
        0xB,
        (
            "Because of yesterday's train accident,\x01",
            "the rail schedule's in disarray...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In the end, many guests asked for\x01",
            "one-day extensions of their stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Though thankfully, service has been\x01",
            "restored as of this morning somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even all the guests who\x01",
            "were forced to stay here\x01",
            "were able to start back for good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1958")

    label("loc_18D1")


    ChrTalk(
        0xB,
        (
            "Even all the guests who\x01",
            "were forced to stay here\x01",
            "were able to start back for good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This too is thanks to\x01",
            "the Guardian Force.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1958")

    Jump("loc_219E")

    label("loc_195D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A18")

    ChrTalk(
        0xB,
        (
            "I heard a train accident occurred\x01",
            "near West Crossbell Highway, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've got to gather information\x01",
            "on that so our guests returning\x01",
            "home today won't be confused.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_1A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2B")

    ChrTalk(
        0xB,
        (
            "Our reservation service using\x01",
            "the orbal net is very popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although not too many of our\x01",
            "guests are using it yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As the orbal network expands, the number\x01",
            "of reservations will surely rise with\x01",
            "the number of communication devices.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BF1")

    label("loc_1B2B")


    ChrTalk(
        0xB,
        (
            "An amazing benefit of the orbal net\x01",
            "is that we can take reservations\x01",
            "even outside of working hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Differently from the phone,\x01",
            "it's possible to send or receive\x01",
            "orbal mail 24 hours a day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF1")

    Jump("loc_219E")

    label("loc_1BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C8E")

    ChrTalk(
        0xB,
        "The question of state independence...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's a difficult question to be\x01",
            "sure, but I think asking the\x01",
            "people directly has meaning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_1C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D0C")

    ChrTalk(
        0xB,
        (
            "Uhuhu, it's finally time for\x01",
            "the conference's main session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Mayor Dieter's got to\x01",
            "do his best for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_1D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1DDD")

    ChrTalk(
        0xB,
        (
            "Since becoming manager, I've\x01",
            "invited various past dignitaries\x01",
            "to stay at this hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Though it's not possible this time,\x01",
            "I'd like each of the dignitaries to\x01",
            "come stay with us sometime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_1DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1ECC")

    ChrTalk(
        0xB,
        (
            "The Trade Conference starting tomorrow\x01",
            "will draw a lot of attention to our hotel\x01",
            "business, whether we like it or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The agreements they sign will\x01",
            "probably impact the number of\x01",
            "tourists and visitors going forward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219E")

    label("loc_1ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2041")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8B")

    ChrTalk(
        0xB,
        "It's raining today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This hotel introduces guests to\x01",
            "tourist attractions that can be\x01",
            "enjoyed even on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please, feel free\x01",
            "to ask about them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_203C")

    label("loc_1F8B")


    ChrTalk(
        0xB,
        (
            "There are few places in\x01",
            "Entertainment District that\x01",
            "can be enjoyed on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even so, it is annoying to go\x01",
            "out, so we have all sort of\x01",
            "room service at our hotel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_203C")

    Jump("loc_219E")

    label("loc_2041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_219E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20FC")

    ChrTalk(
        0xB,
        "Welcome to "Hotel Millennium".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhuhu. At this hotel,\x01",
            "we handle any needs\x01",
            "a guest may have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you should desire our\x01",
            "services, just say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_219E")

    label("loc_20FC")


    ChrTalk(
        0xB,
        (
            "From the salon to room service,\x01",
            "you can order any of our various\x01",
            "services through the orbal net...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This hotel answers all of\x01",
            "our guests' various needs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219E")

    Jump("loc_FBB")

    label("loc_21A3")

    TalkEnd(0xB)
    Return()

    # Function_11_B62 end

    def Function_12_21A7(): pass

    label("Function_12_21A7")

    Call(0, 13)
    Return()

    # Function_12_21A7 end

    def Function_13_21AB(): pass

    label("Function_13_21AB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_230B")

    ChrTalk(
        0x8,
        (
            "Welcome to\x01",
            ""Hotel Millennium".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On this floor we handle same-day\x01",
            "lodging reservations, so please\x01",
            "feel free to ask about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you stay at a hotel or a\x01",
            "bar-inn, you can recover CP.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A normal bar-inn sets CP to 100,\x01",
            "and the high-class hotels set it to 200.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x136, 5)

    label("loc_230B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2315")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3346")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Rest\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2365")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2365")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2385")
    OP_AF(0x45)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3341")

    label("loc_2385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2399")
    Jump("loc_3341")

    label("loc_2399")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3341")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24D2")

    ChrTalk(
        0x8,
        (
            "Per the manager's instructions,\x01",
            "we're reinforcing our emergency\x01",
            "preparations even more than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, it is not the\x01",
            "case that we are buying\x01",
            "only domestic goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We discussed it with the\x01",
            "government, and we are looking for\x01",
            "a way to import foreign goods.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_24D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_25FB")

    ChrTalk(
        0x8,
        (
            "The rush of people in here\x01",
            "coincident with the appearance\x01",
            "of this mist was a total panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though the doll soldiers aren't\x01",
            "attacking citizens for now, things\x01",
            "have calmed down a little, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, I wish they'd do something\x01",
            "about this situation as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_25FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2704")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2684")

    ChrTalk(
        0x8,
        (
            "...I was surprised at\x01",
            "this morning's address.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can understand why the\x01",
            "President is so insistent...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26FF")

    label("loc_2684")


    ChrTalk(
        0x8,
        (
            "...Hmm. For now,\x01",
            "I won't say anything\x01",
            "unnecessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For better or worse,\x01",
            "all I can do is see\x01",
            "how things turn out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26FF")

    Jump("loc_3341")

    label("loc_2704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_27F2")

    ChrTalk(
        0x8,
        (
            "Thankfully, this hotel didn't suffer any\x01",
            "major damage on the day of the attack, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Arc-en-ciel is...\x01",
            "How very awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know what the attackers'\x01",
            "motive was, but... An act like\x01",
            "that can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_27F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_28AA")

    ChrTalk(
        0x8,
        (
            "It seems like there are a lot\x01",
            "of people who think the attack\x01",
            "on Mainz was an Imperial plot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If that's really true... Then what\x01",
            "was the Non-Aggression Pact for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_28AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_296E")

    ChrTalk(
        0x8,
        (
            "We got a lot of\x01",
            "cancellations today due\x01",
            "to yesterday's accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The transcontinental railroad is like\x01",
            "our lifeline... It's a relief to learn\x01",
            "it didn't suffer much damage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_296E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_29EF")

    ChrTalk(
        0x8,
        "Hmm, a train accident, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those don't happen that\x01",
            "often in Crossbell...\x01",
            "I wonder what the cause was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_29EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADC")

    ChrTalk(
        0x8,
        (
            "Miss Doris has been\x01",
            "working harder lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's good at cleaning, of course, but she's\x01",
            "been getting more popular with the guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It must be because Mr. Aaron\x01",
            "was put in charge of her training.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B51")

    label("loc_2ADC")


    ChrTalk(
        0x8,
        (
            "Miss Doris has been\x01",
            "working harder lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It must be because Mr. Aaron\x01",
            "was put in charge of her training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B51")

    Jump("loc_3341")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C50")

    ChrTalk(
        0x8,
        (
            "I'm Crossbellan, \x01",
            "but I worked in an\x01",
            "Imperial hotel before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm not sure how to say this,\x01",
            "but the Imperial nobles wear\x01",
            "out your nerves, day after day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ever since I came here, I've\x01",
            "had an easier time at work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D00")

    label("loc_2C50")


    ChrTalk(
        0x8,
        (
            "The Imperial hotel was a good environment\x01",
            "in which to learn the service trade,\x01",
            "but working there was tiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ever since I came here, I've\x01",
            "had an easier time at work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D00")

    Jump("loc_3341")

    label("loc_2D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD5")

    ChrTalk(
        0x8,
        (
            "I saw Orchis Tower on\x01",
            "the way home from work\x01",
            "yesterday, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's so impressive\x01",
            "I can't even describe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Next time, I want to get a\x01",
            "good look at it from up close.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E59")

    label("loc_2DD5")


    ChrTalk(
        0x8,
        (
            "Though it was from far away, the majesty\x01",
            "of Orchis Tower was overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Next time, I want to look\x01",
            "at it from up close.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E59")

    Jump("loc_3341")

    label("loc_2E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2FF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4A")

    ChrTalk(
        0x8,
        (
            "I wonder if the customers went\x01",
            "to see the inauguration ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There were fireworks too.\x01",
            "It must've been worth seeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The majesty of Orchis Tower... \x01",
            "I want to have a look at it myself soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FEE")

    label("loc_2F4A")


    ChrTalk(
        0x8,
        (
            "There were fireworks at the inauguration\x01",
            "ceremony. It must've been worth seeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The majesty of Orchis Tower... \x01",
            "I want to have a look at it myself soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FEE")

    Jump("loc_3341")

    label("loc_2FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E2")

    ChrTalk(
        0x8,
        (
            "Welcome. There's\x01",
            "nice weather today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although the police are on\x01",
            "alert around town, this is\x01",
            "perfect sightseeing weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're looking for a nice\x01",
            "spot, perhaps I can suggest\x01",
            "you a suitable one?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_315E")

    label("loc_30E2")


    ChrTalk(
        0x8,
        (
            "Welcome. There's\x01",
            "nice weather today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're looking for a nice\x01",
            "spot, perhaps I can suggest\x01",
            "you a suitable one?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_315E")

    Jump("loc_3341")

    label("loc_3163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3226")

    ChrTalk(
        0x8,
        (
            "Good morning,\x01",
            "and welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are going out in this\x01",
            "rainy weather, allow us to\x01",
            "lend you an umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If you need one, please do not hesitate to ask.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32AE")

    label("loc_3226")


    ChrTalk(
        0x8,
        (
            "If you are going out in this\x01",
            "rainy weather, allow us to\x01",
            "lend you an umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If you need one, please do not hesitate to ask.\x02",
    )

    CloseMessageWindow()

    label("loc_32AE")

    Jump("loc_3341")

    label("loc_32B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3341")

    ChrTalk(
        0x8,
        (
            "Welcome to\x01",
            ""Hotel Millennium".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On this floor we handle same-day\x01",
            "lodging reservations, so please\x01",
            "feel free to ask about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3341")

    Jump("loc_2315")

    label("loc_3346")

    TalkEnd(0x8)
    Return()

    # Function_13_21AB end

    def Function_14_334A(): pass

    label("Function_14_334A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3447")

    ChrTalk(
        0xFE,
        (
            "Just now, Manager Laetitia declared\x01",
            "her intention to operate without\x01",
            "regard to profit for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell is in in such distress... I intend\x01",
            "to make use of the whole of my experience\x01",
            "in order to support the manager.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C4")

    label("loc_3447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_34FC")

    ChrTalk(
        0xFE,
        (
            "Because she is offering use of the\x01",
            "hotel for free, I understand the\x01",
            "manager cares for people over mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am happy to be able to\x01",
            "work for someone like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C4")

    label("loc_34FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_35EC")

    ChrTalk(
        0xFE,
        (
            "We have had steadily fewer guests in the days\x01",
            "since the declaration of independence...\x01",
            "This morning's speech was decisive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have never heard of a situation\x01",
            "like this. We will have to revise\x01",
            "our management policies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C4")

    label("loc_35EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E8")

    ChrTalk(
        0xFE,
        (
            "Thankfully the scars left on the city\x01",
            "from the attack aren't too great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the CGF suffered great damage, \x01",
            "and they even got Miss Ilya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something like this\x01",
            "mustn't happen again... \x01",
            "I was just thinking that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_377C")

    label("loc_36E8")


    ChrTalk(
        0xFE,
        (
            "But the CGF suffered great damage, \x01",
            "and they even got Miss Ilya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something like this\x01",
            "mustn't happen again... \x01",
            "I was just thinking that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_377C")

    Jump("loc_42C4")

    label("loc_3781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3815")

    ChrTalk(
        0xFE,
        (
            "About yesterday's attack...\x01",
            "It seems the situation is\x01",
            "still far from being settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am worried about\x01",
            "the people of Mainz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C4")

    label("loc_3815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_38D1")

    ChrTalk(
        0xFE,
        (
            "I heard the derailment was the\x01",
            "doing of an unknown monster...\x01",
            "That is a very disturbing story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It could be some kind of ill omen.\x01",
            "I don't want to think about it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C4")

    label("loc_38D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_399C")

    ChrTalk(
        0xFE,
        (
            "It's about time to check\x01",
            "in the guests, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like the effects of the train\x01",
            "accident will be felt right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a good thing that\x01",
            "everyone made it safely...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C4")

    label("loc_399C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A43")

    ChrTalk(
        0xFE,
        (
            "It's not that rare for the deluxe\x01",
            "suite to be unoccupied\x01",
            "at this time of year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, if you\x01",
            "want to lodge there,\x01",
            "now is your chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C4")

    label("loc_3A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BAB")

    ChrTalk(
        0xFE,
        (
            "The question about state independence...\x01",
            "Although basically many want it realized,\x01",
            "it seems there're also different opinions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone old like me can't\x01",
            "forget the threat from\x01",
            "the two major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, like this hotel did, this is a time\x01",
            "when the autonomous state of Crossbell\x01",
            "itself may need to change as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C75")

    label("loc_3BAB")


    ChrTalk(
        0xFE,
        (
            "Someone old like me can't\x01",
            "forget the threat from\x01",
            "the two major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, like this hotel did, this is a time\x01",
            "when the autonomous state of Crossbell\x01",
            "itself may need to change as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C75")

    Jump("loc_42C4")

    label("loc_3C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3D13")

    ChrTalk(
        0xFE,
        (
            "It is finally time for the Trade\x01",
            "Conference's main session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have to place our\x01",
            "hopes with Mayor Dieter\x01",
            "and Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C4")

    label("loc_3D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3DBD")

    ChrTalk(
        0xFE,
        (
            "I heard all floors of Orchis Tower\x01",
            "are connected to the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. Our hotel is getting more reservations\x01",
            "through the orbal net every day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C4")

    label("loc_3DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E99")

    ChrTalk(
        0xFE,
        (
            "Miss Doris was unreliable\x01",
            "a little while ago, but\x01",
            "we can rest easy now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To see the next generation learn from\x01",
            "experience... To me, in charge of her\x01",
            "training, there is no greater joy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F40")

    label("loc_3E99")


    ChrTalk(
        0xFE,
        (
            "I'm so happy to see\x01",
            "Miss Doris's improvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To see the next generation learn from\x01",
            "experience... To me, in charge of her\x01",
            "training, there is no greater joy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F40")

    Jump("loc_42C4")

    label("loc_3F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4119")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405F")

    ChrTalk(
        0xFE,
        (
            "Though they're not as many as at\x01",
            "the Anniversary Festival, we've\x01",
            "gotten more customers lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it's because of the orbal net reservation\x01",
            "system the manager had installed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear me, "Hotel Millennium"\x01",
            "has a bright future ahead of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4114")

    label("loc_405F")


    ChrTalk(
        0xFE,
        (
            "The fusion of tradition and reform... \x01",
            "That's the future that Manager\x01",
            "Laetitia has in mind for this hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was unsure at first,\x01",
            "but now, I trust the\x01",
            "manager completely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4114")

    Jump("loc_42C4")

    label("loc_4119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_42C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4227")

    ChrTalk(
        0xFE,
        (
            "This year marks the 60th anniversary of\x01",
            "this hotel's opening. By the way, it is also\x01",
            "the 30th year since I started working here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before I knew it, I was the one\x01",
            "who has been here the longest.\x01",
            "Dear me, the times sure do move quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_42C4")

    label("loc_4227")


    ChrTalk(
        0xFE,
        (
            "I have worked for this hotel for 30\x01",
            "years... And before I realized it,\x01",
            "I became the most senior employee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear me, the times sure\x01",
            "do move quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42C4")

    TalkEnd(0xFE)
    Return()

    # Function_14_334A end

    def Function_15_42C8(): pass

    label("Function_15_42C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_436C")

    ChrTalk(
        0xFE,
        (
            "Finally, all the evacuees\x01",
            "were able to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though the situation is\x01",
            "like this... I'm happy to hear\x01",
            "words of thanks from everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DB9")

    label("loc_436C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_441E")

    ChrTalk(
        0xFE,
        (
            "Regardless of the situation...\x01",
            "It's been awhile since the\x01",
            "hotel was this busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As an employee of Hotel Millennium,\x01",
            "I will do my best to serve our guests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DB9")

    label("loc_441E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_454E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E0")

    ChrTalk(
        0xFE,
        (
            "I don't understand the current\x01",
            "situation very well and right now\x01",
            "I'm full of complicated feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's true that the independence\x01",
            "was realized by us and...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4549")

    label("loc_44E0")


    ChrTalk(
        0xFE,
        (
            "...Somehow it's no use thinking\x01",
            "if we didn't had done it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now then... I have to focus on work.\x02",
    )

    CloseMessageWindow()

    label("loc_4549")

    Jump("loc_4DB9")

    label("loc_454E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4664")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4580")
    Call(0, 42)
    Return()

    label("loc_4580")


    ChrTalk(
        0xFE,
        (
            "The cry of monsters, the sound of gunfire,\x01",
            "the shouting of police and screaming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...When I remember that day's attack,\x01",
            "it makes me shiver, even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why did something like that have to happen to this city?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DB9")

    label("loc_4664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_46D7")

    ChrTalk(
        0xFE,
        (
            "The Mainz incident... \x01",
            "I really can't believe it happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope it's resolved quickly...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DB9")

    label("loc_46D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_47B7")

    ChrTalk(
        0xFE,
        (
            "I heard a lot of people were injured\x01",
            "in yesterday's train accident,\x01",
            "but thankfully no one died.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But among them, there were a lot of\x01",
            "people with serious wounds. Anyway,\x01",
            "I hope they get better quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DB9")

    label("loc_47B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_481A")

    ChrTalk(
        0xFE,
        (
            "A train accident...\x01",
            "How really awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I'm worried about the passengers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DB9")

    label("loc_481A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4923")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A9")

    ChrTalk(
        0xFE,
        "Now then, I've got to do my best with work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I mustn't forget to smile\x01",
            "for our guests. (*smile*)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_491E")

    label("loc_48A9")


    ChrTalk(
        0xFE,
        (
            "Working hard for others\x01",
            "gives me a good feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's hard to put into\x01",
            "words, but it makes\x01",
            "me feel needed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_491E")

    Jump("loc_4DB9")

    label("loc_4923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_49F9")

    ChrTalk(
        0xFE,
        (
            "The opening night of Arc-en-\x01",
            "ciel's renewal performance\x01",
            "is rapidly approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, I couldn't get a ticket, \x01",
            "but I'm still looking forward to see\x01",
            "what kind of performance will be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DB9")

    label("loc_49F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ABC")

    ChrTalk(
        0xFE,
        (
            "Everyone, did you go the\x01",
            "Times department store roof?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard it's a good spot\x01",
            "for viewing Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you get the chance,\x01",
            "why not try going there?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B3A")

    label("loc_4ABC")


    ChrTalk(
        0xFE,
        (
            "I heard the Times department\x01",
            "store roof is a good spot\x01",
            "for viewing Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, why not\x01",
            "try going there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B3A")

    Jump("loc_4DB9")

    label("loc_4B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C0D")

    ChrTalk(
        0xFE,
        (
            "I heard the VIPs are planning\x01",
            "to visit various places after\x01",
            "the inauguration ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd be happy if I could see them \x01",
            "somewhere, but with all the\x01",
            "security personnel it'd be hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DB9")

    label("loc_4C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C9C")

    ChrTalk(
        0xFE,
        (
            "I feel like Mr. Aaron has\x01",
            "been scolding me less, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Might I have improved some?\x01",
            "Uh uh, if true, that's good news.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DB9")

    label("loc_4C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4D42")

    ChrTalk(
        0xFE,
        (
            "On rainy days, the carpets get\x01",
            "stained with mud no matter what.\x01",
            "Cleaning them is a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But seeing them\x01",
            "clean again gives\x01",
            "me a good feeling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DB9")

    label("loc_4D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4DB9")

    ChrTalk(
        0xFE,
        (
            "Good morning. Are you\x01",
            "staying with us today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please don't forget to lock\x01",
            "your room when you go out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DB9")

    TalkEnd(0xFE)
    Return()

    # Function_15_42C8 end

    def Function_16_4DBD(): pass

    label("Function_16_4DBD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4E50")

    ChrTalk(
        0xFE,
        "Hmm, now what shall we do today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It might be best to take advantage\x01",
            "of this hotel's services, as the\x01",
            "manager suggested.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ED7")

    label("loc_4E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4ED7")

    ChrTalk(
        0xFE,
        (
            "This hotel has top-class\x01",
            "room service, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I think we'll stay here on\x01",
            "trips to Crossbell next time too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ED7")

    TalkEnd(0xFE)
    Return()

    # Function_16_4DBD end

    def Function_17_4EDB(): pass

    label("Function_17_4EDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4F71")

    ChrTalk(
        0xFE,
        (
            "Uh uh. Passing the time in this\x01",
            "hotel doesn't seem too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although if you ask me,\x01",
            "we should pass the time at the casino.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5005")

    label("loc_4F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5005")

    ChrTalk(
        0xFE,
        (
            "Uh uh. We came by orbal rail\x01",
            "this time, but our travel\x01",
            "fatigue is totally gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The price may be a bit\x01",
            "steep, but it's worth it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5005")

    TalkEnd(0xFE)
    Return()

    # Function_17_4EDB end

    def Function_18_5009(): pass

    label("Function_18_5009")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My little sister and I were on our way home, \x01",
            "when we were surrounded by this fog.\x01",
            "We're taking refuge in this hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I honestly feared\x01",
            "for our very lives.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_5009 end

    def Function_19_50B9(): pass

    label("Function_19_50B9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "When the fog appeared,\x01",
            "big brother carried me\x01",
            "on his back in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ehehe, he's so cool㈱\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_50B9 end

    def Function_20_5123(): pass

    label("Function_20_5123")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Everyone will be worried by now...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_5123 end

    def Function_21_5152(): pass

    label("Function_21_5152")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I want to return home soon...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_5152 end

    def Function_22_517C(): pass

    label("Function_22_517C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5287")

    ChrTalk(
        0xFE,
        (
            "Just where did the barrier\x01",
            "protecting the city went to!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And just what are those\x01",
            "creepy monsters...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because I missed my chance to return\x01",
            "to my country after the President's speech,\x01",
            "I have to deal with this! Give me a break!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_530D")

    label("loc_5287")


    ChrTalk(
        0xFE,
        (
            "Just because I missed my chance to return\x01",
            "to my country after the President's speech,\x01",
            "I have to deal with this! Give me a break!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_530D")

    TalkEnd(0xFE)
    Return()

    # Function_22_517C end

    def Function_23_5311(): pass

    label("Function_23_5311")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If I had understood the\x01",
            "situation, I could've returned\x01",
            "home immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, I'm lucky\x01",
            "to have gotten this nice\x01",
            "a room free of charge.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_5311 end

    def Function_24_53B4(): pass

    label("Function_24_53B4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Being able to shelter in this\x01",
            "hotel is a real silver lining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But this situation... Just how\x01",
            "long will it go on, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_53B4 end

    def Function_25_543F(): pass

    label("Function_25_543F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Ehehe, this room is so biiig♪\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_543F end

    def Function_26_546A(): pass

    label("Function_26_546A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_549E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 6)), scpexpr(EXPR_END)), "loc_549B")
    Call(0, 29)
    Jump("loc_549E")

    label("loc_549B")

    Call(0, 28)

    label("loc_549E")

    Return()

    # Function_26_546A end

    def Function_27_549F(): pass

    label("Function_27_549F")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_27_549F end

    def Function_28_54CC(): pass

    label("Function_28_54CC")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    EndChrThread(0xA, 0x0)
    LoadChrToIndex("chr/ch32300.itc", 0x1E)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, 68000, 0, 12400, 315)
    OP_68(68140, 1500, 9270, 0)
    MoveCamera(312, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21270, 0)
    SetChrPos(0x101, 67400, 0, 9530, 0)
    SetChrPos(0x102, 68780, 0, 9180, 0)
    SetChrPos(0x103, 66670, 0, 8520, 0)
    SetChrPos(0x104, 68370, 0, 8240, 0)
    SetChrPos(0x109, 67410, 0, 7270, 0)
    SetChrPos(0x105, 69430, 0, 7040, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x17,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Alright, see you tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'm looking forward to working with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x17, 68000, 0, 13400, 315)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)

    def lambda_56CD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_56CD)

    def lambda_56DE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF79A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_56DE)
    WaitChrThread(0x17, 1)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sound(104, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x17,
        "Oh... You guys are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us.\x02\x03",
            "You're Mr. Derrick of\x01",
            "Armorica Village, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Yeah, that's right...\x01",
            "Can I help you with anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI should have said this earlier, but... \x01",
            "We're the Crossbell Police Special Support Section.\x02\x03",
            "Can we ask you a few questions?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x17)

    ChrTalk(
        0x17,
        "I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "You're here because of\x01",
            "my father, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "He even called the police... \x01",
            "Hmph, that's rich.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FU-Umm, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...I know the story in general already. \x01",
            "He's trying to investigate my recent\x01",
            "actions, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I'm not doing anything\x01",
            "particularly shady.\x01",
            "Go ahead, ask me anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F(Hmm... An unexpected reaction.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Then I'll get straight to the point.\x02\x03",
            "#00001FIt seems that you've been hanging \x01",
            "around with a Mr. Minneth for the\x01",
            "past few days...\x02\x03",
            "What for, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Well, whatever. It's not\x01",
            "like my father can do\x01",
            "anything about it now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Mr. Minneth helped me out with\x01",
            "a certain something a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Regarding improving the village.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FI-Improving the village...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FY-You'd keep something important\x01",
            "like that from the Village Chief\x01",
            "and proceed anyway?\x02\x03",
            "#00006FI'd say that's not good\x01",
            "no matter the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I've talked to the Village Chief...\x01",
            "To my father about it many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "But all he said was "you've lost sight\x01",
            "of your ideals", and "sudden changes\x01",
            "aren't good". Stuff like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "But even if you maintain things the\x01",
            "way they are, I don't think a rural\x01",
            "village like that has a future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "For the continued existence of\x01",
            "the village, reform is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "My father doesn't\x01",
            "understand that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI see... So that is why\x01",
            "you have been meeting\x01",
            "with Mr. Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Unlike my father, he actually\x01",
            "gave me some good ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "He helped me discover a\x01",
            "huge possibility for our\x01",
            "Armorica Village beekeeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Before long, I plan\x01",
            "to start a grand\x01",
            "enterprise with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FW-What can I say,\x01",
            "it's a crazy story...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Hmph... Well that's\x01",
            "all I can tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Should be fine, right? I've got to\x01",
            "be getting back to the village now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5FD2():
        OP_95(0xFE, 74620, 0, 5690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5FD2)
    Sleep(2000)

    def lambda_5FEF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FEF)
    Sleep(50)

    def lambda_5FFF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FFF)
    Sleep(50)

    def lambda_600F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_600F)
    Sleep(50)

    def lambda_601F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_601F)
    Sleep(50)

    def lambda_602F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_602F)
    Sleep(50)

    def lambda_603F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_603F)
    WaitChrThread(0x17, 1)
    SetChrFlags(0x17, 0x80)
    OP_0D()

    ChrTalk(
        0x102,
        "#00105FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FThere he went...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_68(68210, 1500, 8580, 2000)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FAnyway... \x01",
            "We're already here, so...\x02\x03",
            "#00000FWhy don't we try\x01",
            "meeting directly with\x01",
            "Mr. Minneth?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_611D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_611D)
    Sleep(50)

    def lambda_612D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_612D)
    Sleep(50)

    def lambda_613D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_613D)
    Sleep(50)

    def lambda_614D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_614D)
    Sleep(50)

    def lambda_615D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_615D)

    ChrTalk(
        0x104,
        (
            "#00303FI see... We might\x01",
            "figure something out.\x02\x03",
            "#00300FAlrighty then. Let's make\x01",
            "our way inside, shall we?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x174, 6)
    OP_29(0x82, 0x1, 0x6)
    OP_D7(0x1E)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 50740, 0, 9750, 90)
    BeginChrThread(0xA, 0, 0, 1)
    SetChrPos(0x0, 68510, 0, 9710, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_28_54CC end

    def Function_29_6233(): pass

    label("Function_29_6233")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    EndChrThread(0xA, 0x0)
    OP_4B(0xC, 0xFF)
    OP_68(68560, 1500, 10330, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20260, 0)
    SetChrPos(0x101, 67900, 0, 11200, 0)
    SetChrPos(0x102, 69690, 0, 9980, 315)
    SetChrPos(0x103, 66720, 0, 10430, 45)
    SetChrPos(0x104, 68370, 0, 9740, 0)
    SetChrPos(0x109, 67410, 0, 8770, 0)
    SetChrPos(0x105, 69430, 0, 8540, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00001FAlright...\x01",
            "Here we go.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(600)
    Sound(808, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(330, 20, -1, -1)
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh... \x01",
            "Who is it?\x02\x03",
            "I don't remember ordering\x01",
            "any room service...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou are Mr. Minneth, correct?\x02\x03",
            "#00004FThis may be sudden, but we\x01",
            "are the Crossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "#00000FWe have two or three\x01",
            "questions for you...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh my, you're from\x01",
            "the police...\x02\x03",
            "In that case,\x01",
            "please come in.\x01",
            "The door's unlocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F(S-Somehow I think he's\x01",
            "slightly fakin' cordiality.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(He might be more skilled\x01",
            "than we thought.)\x02\x03",
            "#00005FUmm... \x01",
            "Excuse us, then.\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x1, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    OP_68(169250, 1500, 2800, 0)
    MoveCamera(311, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19200, 0)
    SetChrPos(0xC, 168410, 0, 5520, 180)
    SetChrPos(0x101, 168960, 0, -2080, 0)
    SetChrPos(0x102, 168960, 0, -2080, 0)
    SetChrPos(0x103, 168960, 0, -2080, 0)
    SetChrPos(0x104, 168960, 0, -2080, 0)
    SetChrPos(0x109, 168960, 0, -2080, 0)
    SetChrPos(0x105, 168960, 0, -2080, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_68(169610, 1500, 3430, 3000)
    BeginChrThread(0x101, 3, 0, 30)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 32)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 34)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 35)
    WaitChrThread(0x105, 3)
    OP_6F(0x1)

    ChrTalk(
        0xC,
        (
            "#11PPleased to make your acquaintance.\x01",
            "I am Minneth, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhat business might\x01",
            "you have with me today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FLike we said earlier...\x01",
            "We just want to ask you\x01",
            "a few questions.\x02\x03",
            "#00001FWill you cooperate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POf course. I'll do anything\x01",
            "within my power to assist you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PDid some incident\x01",
            "occur around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat's not it... What we\x01",
            "want to ask is concerning\x01",
            "you, personally.\x02\x03",
            "We want to know what kind of person\x01",
            "you're and what you're planning on\x01",
            "doing in Armorica Village...\x02\x03",
            "#00001FJust some general questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11POh...?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0xC,
        (
            "#11PWell fine, then. \x01",
            "I suppose it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    ChrTalk(
        0xC,
        (
            "#11P*ahem*... I am employed\x01",
            "at a certain company...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PMy job consists in focusing on\x01",
            "product and business development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAnd my visits to Armorica Village\x01",
            "are for an important deal for my\x01",
            ""Quincy Company".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FW-What! You mean that\x01",
            "Quincy Company?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A71():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A71)
    Sleep(50)

    def lambda_6A81():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6A81)
    Sleep(50)

    def lambda_6A91():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A91)
    Sleep(50)

    def lambda_6AA1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6AA1)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FIt's the first time I've heard of 'em\x01",
            "You know those folks, milady?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00105FUmm... The Quincy Company is\x01",
            "a famous candy maker abroad.\x02\x03",
            "#00104FThey're one of the biggest\x01",
            "confectioners. You can get their\x01",
            "imported products in Crossbell too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI think I remember\x01",
            "buying their chocolate\x01",
            "often when I was a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm, I wasn't aware of\x01",
            "who made those things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PUh uh, I guess it can't\x01",
            "be helped, then.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6C73():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C73)
    Sleep(50)

    def lambda_6C83():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C83)
    Sleep(50)

    def lambda_6C93():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C93)
    Sleep(50)

    def lambda_6CA3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6CA3)
    Sleep(50)

    def lambda_6CB3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6CB3)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11PAlthough this is my position, \x01",
            "I myself don't like sweet things. \x01",
            "I've never been interested in them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PDue to my efforts in the sales field for \x01",
            "many years, I have been recognised,\x01",
            "and achieved my current position...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P...Oh, it seems\x01",
            "I have digressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAh... N-No.\x01",
            "We're sorry too.\x02\x03",
            "#00003F...*ahem*. What about the\x01",
            ""deal" in Armorica Village\x01",
            "you mentioned earlier?\x02\x03",
            "#00001FThat "deal"... Does it have\x01",
            "anything to do with the Village\x01",
            "Chief's son, Mr. Derrick?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt seems like it's concerning\x01",
            "development of the village itself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POh... So you already\x01",
            "know that, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHmm, well Mr. Derrick already broke\x01",
            "information silence himself, so I \x01",
            "suppose there's no use hiding it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PUh uh, we've built up a\x01",
            "good working relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FAs we thought...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FCan you give us the details?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PUh uh, sure, why not.\x02",
    )

    CloseMessageWindow()
    OP_68(167980, 1500, 3640, 3000)

    def lambda_7057():
        OP_95(0xFE, 164960, 0, 5520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7057)
    Sleep(500)

    def lambda_7074():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7074)
    Sleep(50)

    def lambda_7084():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7084)
    Sleep(50)

    def lambda_7094():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7094)
    Sleep(50)

    def lambda_70A4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_70A4)
    Sleep(50)

    def lambda_70B4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_70B4)
    Sleep(50)

    def lambda_70C4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_70C4)
    WaitChrThread(0xC, 1)
    OP_6F(0x1)

    ChrTalk(
        0xC,
        (
            "#5PWe at the Quincy Company work\x01",
            "hard every day for the future\x01",
            "of our confectionery business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PTo that end, I have been given a\x01",
            "certain mission from our main office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PAnd that is, to establish a\x01",
            "foothold for expanding our\x01",
            "business into Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FIn other words... \x01",
            "You're establishing a Quincy Company\x01",
            "subsidiary in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PUh uh, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PSo, to start, I went to the city department\x01",
            "store to look for some hints...\x01",
            "That was when I found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PThat terrifically high quality "honey" \x01",
            "that is made in Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHoney... Made from the lotus\x01",
            "flower fields in Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FMr. Harold is always saying\x01",
            "good things about its quality...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(169610, 1500, 3430, 3000)

    def lambda_73BC():
        OP_95(0xFE, 168410, 0, 5520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_73BC)
    Sleep(500)

    def lambda_73D9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73D9)
    Sleep(50)

    def lambda_73E9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_73E9)
    Sleep(50)

    def lambda_73F9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_73F9)
    Sleep(50)

    def lambda_7409():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7409)
    Sleep(50)

    def lambda_7419():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7419)
    Sleep(50)

    def lambda_7429():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7429)
    WaitChrThread(0xC, 1)

    def lambda_743A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_743A)
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11PHoney, brought forth from the abundant\x01",
            "natural bounty of the lotus fields,\x01",
            "passed down through the generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POnce I saw it, a plan to develop a\x01",
            "new confectionery brand was revealed\x01",
            "to me as if from the Goddess herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAnd I call this plan... \x01",
            "The "Armorica Honey Company"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FThe Armorica Honey Company...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FThat has a nice ring to it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#11PIn other words, we'll sell candies\x01",
            "which use Armorica Village's honey\x01",
            "abundantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PBut in order to do that, we'll need\x01",
            "the cooperation of the Armorica\x01",
            "Village residents as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThat's why I approached\x01",
            "Mr. Derrick, the next\x01",
            "Village Chief, with this idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI asked him if he'd like to manage factory\x01",
            "construction and the new business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FMr. Derrick would manage a \x01",
            "subsidiary of Quincy Company...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POf course, my company would use our\x01",
            "know-how and marketing, and the lotus\x01",
            "fields would be overseen by our staff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POn the condition that we don't\x01",
            "cause trouble and life for the\x01",
            "villagers is made easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FBut a factory...\x01",
            "Where do you plan\x01",
            "to build it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWe're still discussing it,\x01",
            "but I was thinking the\x01",
            "village's private property.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt's only ever been used as a\x01",
            "storage area, so I think we'll be\x01",
            "able to secure everyone's agreement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWith those conditions,\x01",
            "I can see the possibilities\x01",
            "of realizing as quite high.\x02\x03",
            "All the more with Derrick, \x01",
            "who is looking to improve the village...\x02\x03",
            "#10302FIt doesn't seem like\x01",
            "such a bad deal for\x01",
            "either you or Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PUh uh, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PTo be honest, I felt his talent and strong sense\x01",
            "of responsibility warranted such a position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PUh uh, that's all I have to say.\x01",
            "Everything makes sense?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x101,
        (
            "#00003FThank you very much\x01",
            "for telling us.\x02\x03",
            "#00000FI think that\x01",
            "clears quite a\x01",
            "few things up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PDo you have anything more to discuss?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, sorry to take\x01",
            "up your time.\x02\x03",
            "If you'll\x01",
            "excuse us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PNo problem at all.\x01",
            "Come again anytime.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PPlease take care\x01",
            "on your way back.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    OP_68(68880, 1500, 9870, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 68000, 0, 13400, 180)
    SetChrPos(0x102, 68000, 0, 13400, 180)
    SetChrPos(0x103, 68000, 0, 13400, 180)
    SetChrPos(0x104, 68000, 0, 13400, 180)
    SetChrPos(0x109, 68000, 0, 13400, 180)
    SetChrPos(0x105, 68000, 0, 13400, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x1, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x105, 3, 0, 41)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 40)
    Sleep(500)
    OP_68(69520, 1500, 7610, 3000)
    BeginChrThread(0x104, 3, 0, 39)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 38)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 37)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 36)
    WaitChrThread(0x101, 3)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        (
            "#00106F*sigh*...\x01",
            "How to put this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, what he told us\x01",
            "was pretty amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FMr. Minneth... \x01",
            "He is more skilled than we thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FRegardin' his plan... It seems like a lot\x01",
            "of work, but it seems profitable too.\x02\x03",
            "#00301FI mean, damn.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x109,
        (
            "#10101FBut with this, I think\x01",
            "we have the whole story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x01",
            "Let's return to Armorica Village for now.\x02\x03",
            "#00001FWe need to report this to Village Chief Tolta.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_6233 end

    def Function_30_80AC(): pass

    label("Function_30_80AC")


    def lambda_80B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_80B1)

    def lambda_80C2():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80C2)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 167730, 0, 2860, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_30_80AC end

    def Function_31_80F7(): pass

    label("Function_31_80F7")


    def lambda_80FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_80FC)

    def lambda_810D():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_810D)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 169150, 0, 2870, 2000, 0x0)
    Return()

    # Function_31_80F7 end

    def Function_32_813B(): pass

    label("Function_32_813B")


    def lambda_8140():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8140)

    def lambda_8151():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8151)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 170230, 0, 1900, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_32_813B end

    def Function_33_8186(): pass

    label("Function_33_8186")


    def lambda_818B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_818B)

    def lambda_819C():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_819C)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 167400, 0, 1860, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_33_8186 end

    def Function_34_81D1(): pass

    label("Function_34_81D1")


    def lambda_81D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_81D6)

    def lambda_81E7():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_81E7)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 168250, 0, 1200, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_34_81D1 end

    def Function_35_821C(): pass

    label("Function_35_821C")


    def lambda_8221():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8221)

    def lambda_8232():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8232)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 169670, 0, 1220, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_35_821C end

    def Function_36_8267(): pass

    label("Function_36_8267")


    def lambda_826C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_826C)

    def lambda_827D():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_827D)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 68440, 0, 10210, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_36_8267 end

    def Function_37_82B2(): pass

    label("Function_37_82B2")


    def lambda_82B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_82B7)

    def lambda_82C8():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_82C8)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 67120, 0, 8910, 2000, 0x0)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_37_82B2 end

    def Function_38_82FD(): pass

    label("Function_38_82FD")


    def lambda_8302():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8302)

    def lambda_8313():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8313)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 70510, 0, 9150, 2000, 0x0)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_38_82FD end

    def Function_39_8348(): pass

    label("Function_39_8348")


    def lambda_834D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_834D)

    def lambda_835E():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_835E)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 67540, 0, 7130, 2000, 0x0)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_39_8348 end

    def Function_40_8393(): pass

    label("Function_40_8393")


    def lambda_8398():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8398)

    def lambda_83A9():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_83A9)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 69250, 0, 6220, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_40_8393 end

    def Function_41_83DE(): pass

    label("Function_41_83DE")


    def lambda_83E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_83E3)

    def lambda_83F4():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_83F4)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 70730, 0, 7540, 2000, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_41_83DE end

    def Function_42_8429(): pass

    label("Function_42_8429")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85D6")

    ChrTalk(
        0x9,
        "Now then, I've got to do the cleaning...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(She could be our [Maid]\x01",
            "for the pageant.)\x02\x03",
            "#00000FUmm, excuse me. We'd like to\x01",
            "ask you a little something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You asked her to participate \x01",
            "in the charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        "A-A pageant, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "U-Umm, excuse me... I'm happy to\x01",
            "get this invitation, but there's\x01",
            "work I can't get away from...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... Excuse\x01",
            "us, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 7)
    Jump("loc_864D")

    label("loc_85D6")


    ChrTalk(
        0x9,
        (
            "An invitation to a\x01",
            "pageant is a little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm happy to receive it, but there's\x01",
            "work I can't get away from...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_864D")

    TalkEnd(0x9)
    Return()

    # Function_42_8429 end

    SaveToFile()

Try(main)
