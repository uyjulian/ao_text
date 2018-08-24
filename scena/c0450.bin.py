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
        "Function_9_9AD",          # 09, 9
        "Function_10_B04",         # 0A, 10
        "Function_11_B08",         # 0B, 11
        "Function_12_20C3",        # 0C, 12
        "Function_13_20C7",        # 0D, 13
        "Function_14_3248",        # 0E, 14
        "Function_15_413E",        # 0F, 15
        "Function_16_4C36",        # 10, 16
        "Function_17_4D55",        # 11, 17
        "Function_18_4E77",        # 12, 18
        "Function_19_4F27",        # 13, 19
        "Function_20_4F91",        # 14, 20
        "Function_21_4FBB",        # 15, 21
        "Function_22_4FE5",        # 16, 22
        "Function_23_517B",        # 17, 23
        "Function_24_5217",        # 18, 24
        "Function_25_52A2",        # 19, 25
        "Function_26_52CD",        # 1A, 26
        "Function_27_5302",        # 1B, 27
        "Function_28_532F",        # 1C, 28
        "Function_29_6027",        # 1D, 29
        "Function_30_7D39",        # 1E, 30
        "Function_31_7D84",        # 1F, 31
        "Function_32_7DC8",        # 20, 32
        "Function_33_7E13",        # 21, 33
        "Function_34_7E5E",        # 22, 34
        "Function_35_7EA9",        # 23, 35
        "Function_36_7EF4",        # 24, 36
        "Function_37_7F3F",        # 25, 37
        "Function_38_7F8A",        # 26, 38
        "Function_39_7FD5",        # 27, 39
        "Function_40_8020",        # 28, 40
        "Function_41_806B",        # 29, 41
        "Function_42_80B6",        # 2A, 42
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
            "The "Delicious Hot Pot\x01",
            "Dishes Pressure Cooker\x01",
            "Edition" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_9A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Satiating\x01",
            "Hot Pot"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_9A9")

    TalkEnd(0xFF)
    Return()

    # Function_8_8DA end

    def Function_9_9AD(): pass

    label("Function_9_9AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7D")

    ChrTalk(
        0xC,
        (
            "Oh, everyone... Do you\x01",
            "need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My Quincy Company's "Armorica\x01",
            "Honey Company" plan is\x01",
            "progressing steadily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please look forward to\x01",
            "our success, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B00")

    label("loc_A7D")


    ChrTalk(
        0xC,
        (
            "My Quincy Company's "Armorica\x01",
            "Honey Company" plan is\x01",
            "progressing steadily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please look forward to\x01",
            "our success, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B00")

    TalkEnd(0xFE)
    Return()

    # Function_9_9AD end

    def Function_10_B04(): pass

    label("Function_10_B04")

    Call(0, 11)
    Return()

    # Function_10_B04 end

    def Function_11_B08(): pass

    label("Function_11_B08")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA0")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "My, you're the\x01",
            "police's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FRight. Can we ask your\x01",
            "situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes. Right now, we have\x01",
            "taken in our former guests\x01",
            "and several evacuees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We have reserve food available\x01",
            "too, so we should be able to\x01",
            "last about a month, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyhow, not knowing the\x01",
            "details of the situation\x01",
            "adds to the anxiety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For now, we've kept the\x01",
            "chaos to a minimum, but\x01",
            "if this goes on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FWe'll immediately begin\x01",
            "acting to resolve this\x01",
            "situation.\x02\x03",
            "So we'd like you to keep\x01",
            "an eye on things for a\x01",
            "while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, understood. Please\x01",
            "take care of yourselves,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 6)

    label("loc_DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2C")

    ChrTalk(
        0xB,
        (
            "Welcome to Hotel\x01",
            "Millenium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhuhu. At this hotel, we\x01",
            "handle any needs a guest\x01",
            "may have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you would like to\x01",
            "stay with us, please,\x01",
            "just say the word.\x02",
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
            "If you stay at the hotel\x01",
            "or a bar-inn, you can\x01",
            "recover CP.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A normal bar-inn sets CP\x01",
            "to 100, and the high-class\x01",
            "hotel sets it to 200.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F29")
    SetScenarioFlags(0x0, 0)

    label("loc_F29")

    SetScenarioFlags(0x136, 5)

    label("loc_F2C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20BF")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Rest\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F88")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_F88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA8")
    OP_AF(0x45)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20BA")

    label("loc_FA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FBC")
    Jump("loc_20BA")

    label("loc_FBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20BA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_111D")

    ChrTalk(
        0xB,
        (
            "We got the info on the President's\x01",
            "arrest, and the evacuees have\x01",
            "returned to their homes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The details regarding that huge tree are unclear,\x01",
            "but for now the mist is clearing up, and I get\x01",
            "the impression the city is settling down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, we have to\x01",
            "prepare everything we can\x01",
            "now, while we still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BA")

    label("loc_111D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D")

    ChrTalk(
        0xB,
        (
            "When martial law and the travel\x01",
            "restriction info came in, we immediately\x01",
            "considered taking in evacuees, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As you might expect, that mist\x01",
            "and those doll soldiers were\x01",
            "outside our expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems everyone's opposition\x01",
            "to the President couldn't be\x01",
            "any greater, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If pushed, I'd say it's\x01",
            "due to everyone's great\x01",
            "uneasiness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1333")

    label("loc_129D")


    ChrTalk(
        0xB,
        (
            "It seems everyone's opposition\x01",
            "to the President couldn't be\x01",
            "any greater, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If pushed, I'd say it's\x01",
            "due to everyone's great\x01",
            "uneasiness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1333")

    Jump("loc_20BA")

    label("loc_1338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1515")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1449")

    ChrTalk(
        0xB,
        (
            "I saw the President's\x01",
            "address through the hotel's\x01",
            "orbal net connection, but...\x02",
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
            "I think it's best if\x01",
            "they all return to their\x01",
            "home countries, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1510")

    label("loc_1449")


    ChrTalk(
        0xB,
        (
            "It seems orbal rail\x01",
            "service was shut down\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, starting on a\x01",
            "journey home now is out\x01",
            "of the question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Also, it's hard to get\x01",
            "info on the airship lines'\x01",
            "operational status.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1510")

    Jump("loc_20BA")

    label("loc_1515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15EF")

    ChrTalk(
        0xB,
        (
            "Evening is the same color as that fire\x01",
            "in Entertainment district... The events\x01",
            "of that day were truly a nightmare.\x02",
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
    Jump("loc_20BA")

    label("loc_15EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1682")

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
            "We citizens can be proud\x01",
            "of the men and women of\x01",
            "the CGF.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BA")

    label("loc_1682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D6")

    ChrTalk(
        0xB,
        (
            "Because of yesterday's\x01",
            "train accident, the rail\x01",
            "schedule is in disarray...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In the end, many customers\x01",
            "asked for one-day\x01",
            "extensions of their stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Though thankfully, service\x01",
            "has been restored as of\x01",
            "this morning somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was able to send a notice\x01",
            "this morning that all of\x01",
            "our guests are safe.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1854")

    label("loc_17D6")


    ChrTalk(
        0xB,
        (
            "I was able to send a notice\x01",
            "this morning that all of\x01",
            "our guests are safe.\x02",
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

    label("loc_1854")

    Jump("loc_20BA")

    label("loc_1859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1914")

    ChrTalk(
        0xB,
        (
            "I heard a train accident\x01",
            "occurred near West\x01",
            "Crossbell Highway, but...\x02",
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
    Jump("loc_20BA")

    label("loc_1914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1AF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2C")

    ChrTalk(
        0xB,
        (
            "Our reservation service\x01",
            "using the orbal net is\x01",
            "very popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although not too many of\x01",
            "our guests are using it\x01",
            "just yet...\x02",
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
    Jump("loc_1AF3")

    label("loc_1A2C")


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
            "And depending on the device,\x01",
            "it's possible to send or receive\x01",
            "orbal mail 24 hours a day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF3")

    Jump("loc_20BA")

    label("loc_1AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B94")

    ChrTalk(
        0xB,
        (
            "The state independence\x01",
            "referendum, huh...\x02",
        )
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
    Jump("loc_20BA")

    label("loc_1B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1C12")

    ChrTalk(
        0xB,
        (
            "Uhuhu, it's finally time\x01",
            "for the conference's\x01",
            "main session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Mayor Dieter's got to do\x01",
            "his best for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BA")

    label("loc_1C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CE8")

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
            "come stay with us at some point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BA")

    label("loc_1CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DDA")

    ChrTalk(
        0xB,
        (
            "The trade conference starting tomorrow\x01",
            "will draw a lot of attention to our hotel\x01",
            "business, whether we like it or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The agreements they'll sign will\x01",
            "probably impact the number of\x01",
            "tourists and visitors going forward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BA")

    label("loc_1DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E99")

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
            "Please, feel free to ask\x01",
            "about them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F54")

    label("loc_1E99")


    ChrTalk(
        0xB,
        (
            "There are few places in\x01",
            "Entertainment district that\x01",
            "can be enjoyed on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even so, it's annoying to go out,\x01",
            "so we have all sorts of room\x01",
            "service available at our hotel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F54")

    Jump("loc_20BA")

    label("loc_1F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_20BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2018")

    ChrTalk(
        0xB,
        (
            "Welcome to Hotel\x01",
            "Millenium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhuhu. At this hotel, we\x01",
            "handle any needs a guest\x01",
            "may have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you should desire our\x01",
            "services, please just\x01",
            "say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20BA")

    label("loc_2018")


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
            "This hotel answers all\x01",
            "of our guests' various\x01",
            "needs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BA")

    Jump("loc_F36")

    label("loc_20BF")

    TalkEnd(0xB)
    Return()

    # Function_11_B08 end

    def Function_12_20C3(): pass

    label("Function_12_20C3")

    Call(0, 13)
    Return()

    # Function_12_20C3 end

    def Function_13_20C7(): pass

    label("Function_13_20C7")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2230")

    ChrTalk(
        0x8,
        (
            "Hello. Welcome to Hotel\x01",
            "Millenium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On this floor we handle same-day\x01",
            "lodging reservations, so please\x01",
            "feel free to ask me about it.\x02",
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
            "If you stay at the hotel\x01",
            "or a bar-inn, you can\x01",
            "recover CP.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A normal bar-inn sets CP\x01",
            "to 100, and the high-class\x01",
            "hotel sets it to 200.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x136, 5)

    label("loc_2230")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_223A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3244")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Rest\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_228C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_228C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22AC")
    OP_AF(0x45)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_323F")

    label("loc_22AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C0")
    Jump("loc_323F")

    label("loc_22C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_323F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23F4")

    ChrTalk(
        0x8,
        (
            "Per the manager's instructions,\x01",
            "were reinforcing our emergency\x01",
            "preparations even more than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, it's not the\x01",
            "case that we're buying\x01",
            "only domestic goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We discussed it with the\x01",
            "government, and we're looking for\x01",
            "a way to import foreign goods.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323F")

    label("loc_23F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_251B")

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
            "Since we learned the doll soldiers\x01",
            "aren't attacking citizens for now,\x01",
            "things calmed down a little, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, I want to do\x01",
            "something about this\x01",
            "situation as soon as I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323F")

    label("loc_251B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A4")

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
            "I can't understand why\x01",
            "the President is so\x01",
            "insistent.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_261F")

    label("loc_25A4")


    ChrTalk(
        0x8,
        (
            "...Hmm. For now, I won't\x01",
            "say anything\x01",
            "unnecessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For better or worse, all\x01",
            "I can do is see how\x01",
            "things turn out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_261F")

    Jump("loc_323F")

    label("loc_2624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_270D")

    ChrTalk(
        0x8,
        (
            "Thankfully, this hotel didn't\x01",
            "suffer any major damage on\x01",
            "the day of the attack, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Arc-en-Ciel is... How\x01",
            "cruel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know what the attacker's\x01",
            "motive was, but... An act like\x01",
            "that can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323F")

    label("loc_270D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27BD")

    ChrTalk(
        0x8,
        (
            "It seems there are a lot of\x01",
            "people who think the attack on\x01",
            "Mainz was an Imperial plot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If that's really true...\x01",
            "then what was the anti-\x01",
            "war treaty for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323F")

    label("loc_27BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2884")

    ChrTalk(
        0x8,
        (
            "We got a lot of\x01",
            "cancellations today thanks\x01",
            "to yesterday's accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The transcontinental railroad is like\x01",
            "our lifeline... It's a relief to\x01",
            "learn it didn't suffer much damage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323F")

    label("loc_2884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2904")

    ChrTalk(
        0x8,
        (
            "Hmm, a train accident,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They don't happen that\x01",
            "often in Crossbell... I\x01",
            "wonder what the cause was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323F")

    label("loc_2904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E8")

    ChrTalk(
        0x8,
        (
            "Doris has been working\x01",
            "harder lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's good at cleaning, of\x01",
            "course, but she's been getting\x01",
            "more popular with the guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It must be because Aaron\x01",
            "was put in charge of her\x01",
            "training.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A54")

    label("loc_29E8")


    ChrTalk(
        0x8,
        (
            "Doris has been working\x01",
            "harder lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It must be because Aaron\x01",
            "was put in charge of her\x01",
            "training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A54")

    Jump("loc_323F")

    label("loc_2A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B53")

    ChrTalk(
        0x8,
        (
            "I'm Crossbellian, but I\x01",
            "worked in an Imperial\x01",
            "hotel before.\x02",
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
            "Ever since I came here,\x01",
            "I've had an easier time\x01",
            "at work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C03")

    label("loc_2B53")


    ChrTalk(
        0x8,
        (
            "The Imperial hotel was a good environment\x01",
            "in which to learn the service trade, but\x01",
            "working there was tiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ever since I came here,\x01",
            "I've had an easier time\x01",
            "at work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C03")

    Jump("loc_323F")

    label("loc_2C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD3")

    ChrTalk(
        0x8,
        (
            "I saw Orchis Tower on\x01",
            "the way home from work\x01",
            "yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's so impressive, it's\x01",
            "indescribable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Next time, I want to get\x01",
            "a good look at it from\x01",
            "up close.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D5E")

    label("loc_2CD3")


    ChrTalk(
        0x8,
        (
            "Though it was from far away,\x01",
            "the impressiveness of Orchis\x01",
            "Tower was overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Next time, I want to\x01",
            "look at it from up\x01",
            "close.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5E")

    Jump("loc_323F")

    label("loc_2D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E4B")

    ChrTalk(
        0x8,
        (
            "I wonder if the\x01",
            "customers went to see\x01",
            "the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There were fireworks\x01",
            "too. It must've been\x01",
            "worth seeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The majesty of Orchis\x01",
            "Tower... I want to have a\x01",
            "look at it myself soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EEB")

    label("loc_2E4B")


    ChrTalk(
        0x8,
        (
            "There were fireworks at\x01",
            "the unveiling ceremony. It\x01",
            "must've been worth seeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The majesty of Orchis\x01",
            "Tower... I want to have a\x01",
            "look at it myself soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EEB")

    Jump("loc_323F")

    label("loc_2EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3062")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE0")

    ChrTalk(
        0x8,
        (
            "Welcome. There's nice\x01",
            "weather today.\x02",
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
            "spot, perhaps I can guide\x01",
            "you to a suitable one?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_305D")

    label("loc_2FE0")


    ChrTalk(
        0x8,
        (
            "Welcome. There's nice\x01",
            "weather today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're looking for a nice\x01",
            "spot, perhaps I can guide\x01",
            "you to a suitable one?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_305D")

    Jump("loc_323F")

    label("loc_3062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_31AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311F")

    ChrTalk(
        0x8,
        "Good morning. Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're going out in this\x01",
            "rainy weather, allow us to\x01",
            "lend you an umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need one, please\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31A5")

    label("loc_311F")


    ChrTalk(
        0x8,
        (
            "If you're going out in this\x01",
            "rainy weather, allow us to\x01",
            "lend you an umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need one, please\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A5")

    Jump("loc_323F")

    label("loc_31AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_323F")

    ChrTalk(
        0x8,
        (
            "Hello. Welcome to Hotel\x01",
            "Millenium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On this floor we handle same-day\x01",
            "lodging reservations, so please\x01",
            "feel free to ask me about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323F")

    Jump("loc_223A")

    label("loc_3244")

    TalkEnd(0x8)
    Return()

    # Function_13_20C7 end

    def Function_14_3248(): pass

    label("Function_14_3248")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3342")

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
            "Crossbell is in such distress... I intend\x01",
            "to make use of the whole of my experience\x01",
            "in order to support the manager.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_3342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_33F5")

    ChrTalk(
        0xFE,
        (
            "Because she's offering use of the\x01",
            "hotel for free, I understand the\x01",
            "manager cares for people over mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm happy to be able to\x01",
            "work for someone like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_33F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_34E4")

    ChrTalk(
        0xFE,
        (
            "We've had steadily fewer guests in the days\x01",
            "since the declaration of independence,\x01",
            "but... This morning's speech was decisive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never heard of a situation\x01",
            "like this. We'll have to revise\x01",
            "our management policies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_34E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D5")

    ChrTalk(
        0xFE,
        (
            "Thankfully the scars on\x01",
            "the city from the attack\x01",
            "aren't too severe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the CGF suffered\x01",
            "great damage, and they\x01",
            "even got Ilya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something like this\x01",
            "mustn't happen again... I\x01",
            "was just thinking that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3662")

    label("loc_35D5")


    ChrTalk(
        0xFE,
        (
            "But the CGF suffered\x01",
            "great damage, and they\x01",
            "even got Ilya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something like this\x01",
            "mustn't happen again... I\x01",
            "was just thinking that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3662")

    Jump("loc_413A")

    label("loc_3667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_36EE")

    ChrTalk(
        0xFE,
        (
            "We're still getting\x01",
            "everything back to normal\x01",
            "after yesterday's attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about the\x01",
            "people of Mainz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_36EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_37A8")

    ChrTalk(
        0xFE,
        (
            "I heard the derailment was the\x01",
            "doing of an unknown monster,\x01",
            "but... That's very strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It could be some kind of\x01",
            "ill omen. I don't want to\x01",
            "think about it, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_37A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3875")

    ChrTalk(
        0xFE,
        (
            "It's about time to check\x01",
            "in the guests,\x01",
            "however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like the effects\x01",
            "of the train accident\x01",
            "will be felt right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, thank goodness\x01",
            "you arrived safely,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_3875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_390A")

    ChrTalk(
        0xFE,
        (
            "It's rare for the deluxe\x01",
            "suite to be unoccupied\x01",
            "at this time of year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got to be sure to\x01",
            "target interested\x01",
            "individuals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_390A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4A")

    ChrTalk(
        0xFE,
        (
            "The state independence referendum...\x01",
            "Basically they're just looking for a\x01",
            "majority to approve it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone old like me can't\x01",
            "forget the threat from\x01",
            "the major powers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, in addition to our hotel,\x01",
            "this is a time when Crossbell State\x01",
            "itself may need to change as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B08")

    label("loc_3A4A")


    ChrTalk(
        0xFE,
        (
            "Someone old like me can't\x01",
            "forget the threat from\x01",
            "the major powers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, in addition to our hotel,\x01",
            "this is a time when Crossbell State\x01",
            "itself may need to change as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B08")

    Jump("loc_413A")

    label("loc_3B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BA7")

    ChrTalk(
        0xFE,
        (
            "It's finally time for\x01",
            "the trade conference's\x01",
            "main session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got to place our\x01",
            "hopes with Mayor Dieter\x01",
            "and Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_3BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C50")

    ChrTalk(
        0xFE,
        (
            "I heard all floors of\x01",
            "Orchis Tower are connected\x01",
            "to the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Our hotel is getting\x01",
            "more reservations through\x01",
            "the orbal net every day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_3C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D27")

    ChrTalk(
        0xFE,
        (
            "Doris was unreliable a\x01",
            "little while ago, but we\x01",
            "can rest easy now.\x02",
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
    Jump("loc_3DC8")

    label("loc_3D27")


    ChrTalk(
        0xFE,
        (
            "I'm so happy so see\x01",
            "Doris' improvement.\x02",
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

    label("loc_3DC8")

    Jump("loc_413A")

    label("loc_3DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE6")

    ChrTalk(
        0xFE,
        (
            "Though it's not as much as during\x01",
            "the Anniversary Festival, we've\x01",
            "gotten more customers lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it's because of the orbal\x01",
            "network reservation system the\x01",
            "manager had installed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Hotel Millenium\x01",
            "has a bright future\x01",
            "ahead of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F95")

    label("loc_3EE6")


    ChrTalk(
        0xFE,
        (
            "The fusion of tradition and\x01",
            "reform... That's the future Manager\x01",
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

    label("loc_3F95")

    Jump("loc_413A")

    label("loc_3F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_413A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40A2")

    ChrTalk(
        0xFE,
        (
            "This year marks the 60th anniversary of\x01",
            "this hotel's opening. By the way, it's also\x01",
            "the 30th year since I started working here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before I knew it, I was the one\x01",
            "who's been here the longest. Haha,\x01",
            "the times sure do move quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_413A")

    label("loc_40A2")


    ChrTalk(
        0xFE,
        (
            "I've worked for this hotel for 30\x01",
            "years... And before I realized it,\x01",
            "I became the most senior employee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, the times sure do\x01",
            "move quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_413A")

    TalkEnd(0xFE)
    Return()

    # Function_14_3248 end

    def Function_15_413E(): pass

    label("Function_15_413E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_41E4")

    ChrTalk(
        0xFE,
        (
            "All of the evacuees were\x01",
            "finally able to leave.\x02",
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
    Jump("loc_4C32")

    label("loc_41E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4296")

    ChrTalk(
        0xFE,
        (
            "Regardless of the situation...\x01",
            "It's been a while since the\x01",
            "hotel was this busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As an employee of Hotel\x01",
            "Millenium, I will do my\x01",
            "best to serve our guests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_43DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4363")

    ChrTalk(
        0xFE,
        (
            "I don't understand the current\x01",
            "situation very well but... Right now\x01",
            "I'm full of complicated feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's true that the\x01",
            "independence was approved\x01",
            "by our votes, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43D8")

    label("loc_4363")


    ChrTalk(
        0xFE,
        (
            "...It's useless thinking\x01",
            "about what would have\x01",
            "happened if we hadn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then... I have to\x01",
            "focus on work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D8")

    Jump("loc_4C32")

    label("loc_43DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_44F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_440F")
    Call(0, 42)
    Return()

    label("loc_440F")


    ChrTalk(
        0xFE,
        (
            "The cry of monsters, the sound\x01",
            "of gunfire, the shouting of\x01",
            "police and screaming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...When I remember that\x01",
            "day's attack, it makes\x01",
            "me shiver, even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why did something like\x01",
            "that have to happen to\x01",
            "this city?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_44F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4565")

    ChrTalk(
        0xFE,
        (
            "The Mainz incident... I\x01",
            "really can't believe it\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope it's resolved\x01",
            "quickly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4647")

    ChrTalk(
        0xFE,
        (
            "I heard a lot of people were injured\x01",
            "in yesterday's train accident, but\x01",
            "thankfully no one died.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But among them, there were a lot of\x01",
            "people with serious injuries. Anyway,\x01",
            "I hope they get better quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46A3")

    ChrTalk(
        0xFE,
        (
            "A train accident... How\x01",
            "awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I'm worried about the\x01",
            "passengers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_46A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_47AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4733")

    ChrTalk(
        0xFE,
        (
            "Now then, I've got to do\x01",
            "my best with work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I mustn't forget to\x01",
            "smile for our guests.\x01",
            "(*smiles*)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47A8")

    label("loc_4733")


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
            "words, but it makes me\x01",
            "feel needed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47A8")

    Jump("loc_4C32")

    label("loc_47AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4871")

    ChrTalk(
        0xFE,
        (
            "Opening night of Arc-en-\x01",
            "Ciel's renewal performance\x01",
            "is rapidly approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, I couldn't get tickets,\x01",
            "but I'm still looking forward to\x01",
            "seeing their performance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_49B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4934")

    ChrTalk(
        0xFE,
        (
            "Everyone, did you go the\x01",
            "Times Department Store\x01",
            "roof?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard it's a good spot\x01",
            "for viewing Orchis\x01",
            "Tower.\x02",
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
    Jump("loc_49B2")

    label("loc_4934")


    ChrTalk(
        0xFE,
        (
            "I heard the Times Department\x01",
            "Store roof is a good spot\x01",
            "for viewing Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, why not try\x01",
            "going there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49B2")

    Jump("loc_4C32")

    label("loc_49B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4A86")

    ChrTalk(
        0xFE,
        (
            "I heard the VIPs are planning\x01",
            "to visit various places after\x01",
            "the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm happy they're getting to see\x01",
            "our state, but... It must be tough\x01",
            "on all the security personnel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B10")

    ChrTalk(
        0xFE,
        (
            "I feel like Aaron has\x01",
            "been scolding me less,\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Might I have improved\x01",
            "some? Haha. If true,\x01",
            "that's good news.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BBB")

    ChrTalk(
        0xFE,
        (
            "On rainy days, the carpet gets\x01",
            "stained with mud no matter what\x01",
            "I do, and cleaning it is a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But seeing it clean\x01",
            "again gives me a good\x01",
            "feeling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C32")

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
            "Please don't forget to\x01",
            "lock your room when you\x01",
            "go out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C32")

    TalkEnd(0xFE)
    Return()

    # Function_15_413E end

    def Function_16_4C36(): pass

    label("Function_16_4C36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4CC8")

    ChrTalk(
        0xFE,
        (
            "Hmm, now what shall I do\x01",
            "today?\x02",
        )
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
    Jump("loc_4D51")

    label("loc_4CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4D51")

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
            "Hmm. I think I'll stay\x01",
            "here on my trips to\x01",
            "Crossbell going forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D51")

    TalkEnd(0xFE)
    Return()

    # Function_16_4C36 end

    def Function_17_4D55(): pass

    label("Function_17_4D55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4DE0")

    ChrTalk(
        0xFE,
        (
            "Haha. Passing the time\x01",
            "in this hotel doesn't\x01",
            "seem too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We should pass the time\x01",
            "at the casino if you ask\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E73")

    label("loc_4DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4E73")

    ChrTalk(
        0xFE,
        (
            "Haha. We came by orbal rail\x01",
            "this time, but our travel\x01",
            "fatigue is totally gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The price may be a bit\x01",
            "steep, but it's worth\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E73")

    TalkEnd(0xFE)
    Return()

    # Function_17_4D55 end

    def Function_18_4E77(): pass

    label("Function_18_4E77")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Me and my little sister were on our way\x01",
            "home, when we were surrounded by this\x01",
            "fog. We're taking refuge in this hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I honestly feared for\x01",
            "our very lives.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4E77 end

    def Function_19_4F27(): pass

    label("Function_19_4F27")

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

    # Function_19_4F27 end

    def Function_20_4F91(): pass

    label("Function_20_4F91")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm worried about\x01",
            "everyone...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_4F91 end

    def Function_21_4FBB(): pass

    label("Function_21_4FBB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I want to return home\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_4FBB end

    def Function_22_4FE5(): pass

    label("Function_22_4FE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F0")

    ChrTalk(
        0xFE,
        (
            "Just where did the\x01",
            "barrier protecting the\x01",
            "city come from!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And just what are those\x01",
            "creepy monsters!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because I missed my chance to return\x01",
            "to my country after the President's speech,\x01",
            "I have to deal with this!? Give me a break!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5177")

    label("loc_50F0")


    ChrTalk(
        0xFE,
        (
            "Just because I missed my chance to return\x01",
            "to my country after the President's speech,\x01",
            "I have to deal with this!? Give me a break!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5177")

    TalkEnd(0xFE)
    Return()

    # Function_22_4FE5 end

    def Function_23_517B(): pass

    label("Function_23_517B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If I understood the\x01",
            "situation, I could return\x01",
            "home immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, we're lucky\x01",
            "to have gotten this nice\x01",
            "a room free of charge.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_517B end

    def Function_24_5217(): pass

    label("Function_24_5217")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Being able to shelter in\x01",
            "this hotel is a real\x01",
            "silver lining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But this situation...\x01",
            "Just how long will it go\x01",
            "on, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_5217 end

    def Function_25_52A2(): pass

    label("Function_25_52A2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Ehehe, this room is so\x01",
            "biiig♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_52A2 end

    def Function_26_52CD(): pass

    label("Function_26_52CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 6)), scpexpr(EXPR_END)), "loc_52FE")
    Call(0, 29)
    Jump("loc_5301")

    label("loc_52FE")

    Call(0, 28)

    label("loc_5301")

    Return()

    # Function_26_52CD end

    def Function_27_5302(): pass

    label("Function_27_5302")

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

    # Function_27_5302 end

    def Function_28_532F(): pass

    label("Function_28_532F")

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
            "─Alright, see you\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'm looking forward to\x01",
            "working with you.\x02",
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

    def lambda_552E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_552E)

    def lambda_553F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF79A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_553F)
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
            "You're Derrick of\x01",
            "Armorica, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Yeah, that's right...\x01",
            "Can I help you with\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI should have said this earlier,\x01",
            "but... We're the Crossbell\x01",
            "Police Special Support Section.\x02\x03",
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
            "my old man, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "He even called the\x01",
            "police... Wow, that's\x01",
            "rich.\x02",
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
            "...I know the story in general\x01",
            "already. He's trying to investigate\x01",
            "my recent actions, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "It's nothing\x01",
            "particularly shady. Go\x01",
            "ahead, ask me anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F(Hmm... An unexpected\x01",
            "reaction.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Then I'll get straight\x01",
            "to the point.\x02\x03",
            "#00001FIt seems that you've been\x01",
            "hanging around Minneth\x01",
            "for the past few days...\x02\x03",
            "What for, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Well, whatever. It's not\x01",
            "like my old man can do\x01",
            "anything about it now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Minneth helped me out\x01",
            "with a certain something\x01",
            "a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Regarding improving the\x01",
            "village.\x02",
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

    ChrTalk(
        0x109,
        "#10105FImproving the village?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYou'd keep something\x01",
            "important like that from the\x01",
            "chief and proceed anyway?\x02\x03",
            "#00006FI'd say that's not good no\x01",
            "matter the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I've talked to chief\x01",
            "about it many times.\x02",
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
            "village like ours has a future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "For the continued\x01",
            "existence of the village,\x01",
            "reform is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "My old man doesn't\x01",
            "understand that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI see... So that's why\x01",
            "you've been meeting with\x01",
            "Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Unlike my dad, he\x01",
            "actually gave me some\x01",
            "good ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "He helped me discover a\x01",
            "huge possibility for our\x01",
            "Armorica beekeeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Before long, I plan to\x01",
            "start a grand enterprise\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FMan, this conversation\x01",
            "is going nowhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Hmph... Well that's all\x01",
            "I can tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "That should be fine, right?\x01",
            "I've got to be getting back\x01",
            "to the village.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DD3():
        OP_95(0xFE, 74620, 0, 5690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5DD3)
    Sleep(2000)

    def lambda_5DF0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DF0)
    Sleep(50)

    def lambda_5E00():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E00)
    Sleep(50)

    def lambda_5E10():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E10)
    Sleep(50)

    def lambda_5E20():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E20)
    Sleep(50)

    def lambda_5E30():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E30)
    Sleep(50)

    def lambda_5E40():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E40)
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
            "#00003FAnyway... Since we're\x01",
            "here.\x02\x03",
            "#00000FWhy don't we try meeting\x01",
            "directly with Minneth?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F11():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F11)
    Sleep(50)

    def lambda_5F21():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5F21)
    Sleep(50)

    def lambda_5F31():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5F31)
    Sleep(50)

    def lambda_5F41():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5F41)
    Sleep(50)

    def lambda_5F51():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5F51)

    ChrTalk(
        0x104,
        (
            "#00303FI see... We might figure\x01",
            "something out.\x02\x03",
            "#00300FAlrighty then. Let's\x01",
            "make our way inside,\x01",
            "shall we?\x02",
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

    # Function_28_532F end

    def Function_29_6027(): pass

    label("Function_29_6027")

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
        "#00001FAlright... Here we go.\x02",
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
            "Oh... Did you forget\x01",
            "something?\x02\x03",
            "I don't remember\x01",
            "ordering any room\x01",
            "service...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou are Minneth, correct?\x02\x03",
            "#00004FI know it's sudden, but\x01",
            "we're the Crossbell Police\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh you're from the\x01",
            "police...\x02\x03",
            "In that case, please\x01",
            "come in. The door's\x01",
            "unlocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F(I think he's slightly\x01",
            "fakin' cordiality for\x01",
            "some reason.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(He might be more\x01",
            "skilled than we\x01",
            "thought.)\x02\x03",
            "#00005FUmm... Excuse us, then.\x02",
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
            "#11PPleased to make your\x01",
            "acquaintance. I am\x01",
            "Minneth, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhat business might you\x01",
            "have today?\x02",
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
            "#11POf course. I'll do\x01",
            "anything within my power\x01",
            "to assist you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PDid some incident occur\x01",
            "around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat's not it... What we want to\x01",
            "ask is concerning you,\x01",
            "personally.\x02\x03",
            "We want to know what kind of\x01",
            "person you are and what you're\x01",
            "planning on doing in Armorica...\x02\x03",
            "#00001FJust some general questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11POh?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0xC,
        (
            "#11PWell fine, then. I\x01",
            "suppose it can't be\x01",
            "helped.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    ChrTalk(
        0xC,
        (
            "#11PAhem... I am employed at\x01",
            "a certain company...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POn this trip I am\x01",
            "focusing on product and\x01",
            "business development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAnd my visits to Armorica\x01",
            "are for an important deal\x01",
            "for my "Quincy Company".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FW-What!? You mean that\x01",
            "Quincy Company?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_681F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_681F)
    Sleep(50)

    def lambda_682F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_682F)
    Sleep(50)

    def lambda_683F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_683F)
    Sleep(50)

    def lambda_684F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_684F)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FFirst I've heard of\x01",
            "them. You know them,\x01",
            "milady?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00105FUmm... The Quincy Company is a famous\x01",
            "candy maker abroad.\x02\x03",
            "#00104FThey're one of the biggest\x01",
            "confectioners. You can get their\x01",
            "imported products in Crossbell even now.\x02",
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
            "who made them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHaha, I guess it can't\x01",
            "be helped, then.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A0A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A0A)
    Sleep(50)

    def lambda_6A1A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A1A)
    Sleep(50)

    def lambda_6A2A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6A2A)
    Sleep(50)

    def lambda_6A3A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A3A)
    Sleep(50)

    def lambda_6A4A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6A4A)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11PI myself dislike sweets.\x01",
            "I've never been\x01",
            "interested in them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWe've developed our\x01",
            "business for many years to\x01",
            "arrive at this point...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P...Whoops. It seems we\x01",
            "have digressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAh... N-No. We're sorry\x01",
            "too.\x02\x03",
            "#00003F...Ahem. What about the\x01",
            ""deal" in Armorica you\x01",
            "mentioned earlier?\x02\x03",
            "#00001FThat "deal"... Does it\x01",
            "have anything to do with\x01",
            "the chief's son, Derrick?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe heard it was connected\x01",
            "with development of the\x01",
            "village...\x02",
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
            "#11PHmm, well Derrick already broke\x01",
            "information silence himself, so I\x01",
            "suppose there's no use hiding it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHaha, we've built up a\x01",
            "good working\x01",
            "relationship.\x02",
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
        (
            "#00001FCan you give us the\x01",
            "details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHaha, sure, why not.\x02",
    )

    CloseMessageWindow()
    OP_68(167980, 1500, 3640, 3000)

    def lambda_6D7C():
        OP_95(0xFE, 164960, 0, 5520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6D7C)
    Sleep(500)

    def lambda_6D99():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D99)
    Sleep(50)

    def lambda_6DA9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6DA9)
    Sleep(50)

    def lambda_6DB9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6DB9)
    Sleep(50)

    def lambda_6DC9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6DC9)
    Sleep(50)

    def lambda_6DD9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6DD9)
    Sleep(50)

    def lambda_6DE9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6DE9)
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
            "#5PTo that end, I have been\x01",
            "given a certain mission\x01",
            "from our main office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PNamely, to establish a\x01",
            "foothold for expanding our\x01",
            "business into Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FIn other words... You're\x01",
            "establishing a Quincy Company\x01",
            "subsidiary in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PHaha, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIn the beginning I thought the\x01",
            "department store in the city might be\x01",
            "best, but... That was when I found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PThat terribly high\x01",
            "quality "honey" that is\x01",
            "made in Armorica.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHoney... Made from the\x01",
            "lotus flowers in\x01",
            "Armorica.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHarold is always saying\x01",
            "good things about its\x01",
            "quality...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(169610, 1500, 3430, 3000)

    def lambda_70C1():
        OP_95(0xFE, 168410, 0, 5520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_70C1)
    Sleep(500)

    def lambda_70DE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70DE)
    Sleep(50)

    def lambda_70EE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_70EE)
    Sleep(50)

    def lambda_70FE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_70FE)
    Sleep(50)

    def lambda_710E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_710E)
    Sleep(50)

    def lambda_711E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_711E)
    Sleep(50)

    def lambda_712E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_712E)
    WaitChrThread(0xC, 1)

    def lambda_713F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_713F)
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
            "#11PAnd I call this plan...\x01",
            "The "Armorica Honey\x01",
            "Company"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FThe Armorica Honey\x01",
            "Company...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FThat has a nice ring to\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#11PIn other words, we'll sell\x01",
            "candy based on Armorica's\x01",
            "abundant honey.\x02",
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
            "Derrick, the next chief,\x01",
            "with this idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI asked him if he'd like to\x01",
            "manage factory construction\x01",
            "and the new business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FDerrick would manage a\x01",
            "subsidiary of Quincy\x01",
            "Company?\x02",
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
            "#00105FBut a factory... Where\x01",
            "do you plan to build it?\x02",
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
            "#10304FWith those conditions, I\x01",
            "can see why Derrick's on\x01",
            "board.\x02\x03",
            "After all, Derrick was\x01",
            "specifically looking to\x01",
            "improve the village...\x02\x03",
            "#10302FIt doesn't seem like\x01",
            "such a bad deal for\x01",
            "either you or Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHaha, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PTo be honest, I felt Derrick's genius\x01",
            "and strong sense of responsibility\x01",
            "warranted such a position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHaha, that's all I have\x01",
            "to say. Everything make\x01",
            "sense?\x02",
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
            "#00003FThank you for telling\x01",
            "us.\x02\x03",
            "#00000FI think that clears\x01",
            "quite a few things up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PDo you have anything\x01",
            "more to discuss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, sorry to take up\x01",
            "your time.\x02\x03",
            "If you'll excuse us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PNo problem. Come again\x01",
            "anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PTake care.\x02",
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
            "#00106F*sigh*... How to put\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, what he told us\x01",
            "was pretty amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThat Minneth... He's\x01",
            "more skilled than we\x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FRegarding his plan... It\x01",
            "seems like a lot of work,\x01",
            "but it seems profitable too.\x02\x03",
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
            "#00003FYeah... Let's return to\x01",
            "Armorica.\x02\x03",
            "#00001FWe need to report this\x01",
            "to Chief Tolta.\x02",
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

    # Function_29_6027 end

    def Function_30_7D39(): pass

    label("Function_30_7D39")


    def lambda_7D3E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D3E)

    def lambda_7D4F():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D4F)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 167730, 0, 2860, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_30_7D39 end

    def Function_31_7D84(): pass

    label("Function_31_7D84")


    def lambda_7D89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7D89)

    def lambda_7D9A():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D9A)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 169150, 0, 2870, 2000, 0x0)
    Return()

    # Function_31_7D84 end

    def Function_32_7DC8(): pass

    label("Function_32_7DC8")


    def lambda_7DCD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7DCD)

    def lambda_7DDE():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7DDE)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 170230, 0, 1900, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_32_7DC8 end

    def Function_33_7E13(): pass

    label("Function_33_7E13")


    def lambda_7E18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7E18)

    def lambda_7E29():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E29)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 167400, 0, 1860, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_33_7E13 end

    def Function_34_7E5E(): pass

    label("Function_34_7E5E")


    def lambda_7E63():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7E63)

    def lambda_7E74():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E74)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 168250, 0, 1200, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_34_7E5E end

    def Function_35_7EA9(): pass

    label("Function_35_7EA9")


    def lambda_7EAE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7EAE)

    def lambda_7EBF():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7EBF)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 169670, 0, 1220, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_35_7EA9 end

    def Function_36_7EF4(): pass

    label("Function_36_7EF4")


    def lambda_7EF9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EF9)

    def lambda_7F0A():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F0A)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 68440, 0, 10210, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_36_7EF4 end

    def Function_37_7F3F(): pass

    label("Function_37_7F3F")


    def lambda_7F44():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7F44)

    def lambda_7F55():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7F55)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 67120, 0, 8910, 2000, 0x0)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_37_7F3F end

    def Function_38_7F8A(): pass

    label("Function_38_7F8A")


    def lambda_7F8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7F8F)

    def lambda_7FA0():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7FA0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 70510, 0, 9150, 2000, 0x0)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_38_7F8A end

    def Function_39_7FD5(): pass

    label("Function_39_7FD5")


    def lambda_7FDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7FDA)

    def lambda_7FEB():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7FEB)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 67540, 0, 7130, 2000, 0x0)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_39_7FD5 end

    def Function_40_8020(): pass

    label("Function_40_8020")


    def lambda_8025():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8025)

    def lambda_8036():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8036)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 69250, 0, 6220, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_40_8020 end

    def Function_41_806B(): pass

    label("Function_41_806B")


    def lambda_8070():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8070)

    def lambda_8081():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8081)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 70730, 0, 7540, 2000, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_41_806B end

    def Function_42_80B6(): pass

    label("Function_42_80B6")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8254")

    ChrTalk(
        0x9,
        (
            "Now then, I've got to do\x01",
            "the cleaning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(She could be our maid\x01",
            "for the pageant.)\x02\x03",
            "#00000FUmm, excuse me. I'd like\x01",
            "to ask you something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked Doris to\x01",
            "participate in the\x01",
            "charity event pageant.\x07\x00\x02",
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
            "#00003FI see... Excuse us,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 7)
    Jump("loc_82CB")

    label("loc_8254")


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
            "I'm happy to receive it,\x01",
            "but there's work I can't\x01",
            "get away from...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82CB")

    TalkEnd(0x9)
    Return()

    # Function_42_80B6 end

    SaveToFile()

Try(main)
