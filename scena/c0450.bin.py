from ScenarioHelper import *

def main():
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
        "Receiving Kyle",             # 1
        "Doris",                 # 2
        "Aaron",               # 3
        "Letizia manager",       # 4
        "Minnes",               # 5
        "tourist",                 # 6
        "tourist",                 # 7
        "Citizen",                   # 8
        "girl",                 # 9
        "Citizen",                   # 10
        "Citizen",                   # 11
        "tourist",                 # 12
        "Citizen",                   # 13
        "Citizen",                   # 14
        "Citizen",                   # 15
        "Derrick",               # 16
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
        "Function_9_989",          # 09, 9
        "Function_10_B23",         # 0A, 10
        "Function_11_B27",         # 0B, 11
        "Function_12_1F34",        # 0C, 12
        "Function_13_1F38",        # 0D, 13
        "Function_14_3052",        # 0E, 14
        "Function_15_3E46",        # 0F, 15
        "Function_16_4873",        # 10, 16
        "Function_17_4985",        # 11, 17
        "Function_18_4A94",        # 12, 18
        "Function_19_4B20",        # 13, 19
        "Function_20_4B93",        # 14, 20
        "Function_21_4BC0",        # 15, 21
        "Function_22_4BE5",        # 16, 22
        "Function_23_4D32",        # 17, 23
        "Function_24_4DDB",        # 18, 24
        "Function_25_4E46",        # 19, 25
        "Function_26_4E71",        # 1A, 26
        "Function_27_4EA6",        # 1B, 27
        "Function_28_4ED8",        # 1C, 28
        "Function_29_5B19",        # 1D, 29
        "Function_30_7861",        # 1E, 30
        "Function_31_78AC",        # 1F, 31
        "Function_32_78F0",        # 20, 32
        "Function_33_793B",        # 21, 33
        "Function_34_7986",        # 22, 34
        "Function_35_79D1",        # 23, 35
        "Function_36_7A1C",        # 24, 36
        "Function_37_7A67",        # 25, 37
        "Function_38_7AB2",        # 26, 38
        "Function_39_7AFD",        # 27, 39
        "Function_40_7B48",        # 28, 40
        "Function_41_7B93",        # 29, 41
        "Function_42_7BDE",        # 2A, 42
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
            "\"Delicious hot pot cooking pressure pot edition\" is available.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_985")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_985")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Fried pork pot\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_985")

    TalkEnd(0xFF)
    Return()

    # Function_8_8DA end

    def Function_9_989(): pass

    label("Function_9_989")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7C")

    ChrTalk(
        0xC,
        (
            "Aw, everyone ….\x01",
            "Do you still need something for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Our company with Quincy and Armorika village\x01",
            "\"Armorica · Honey Company\" plan\x01",
            "It progresses gradually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Future prospects, everyone too\x01",
            "I am fortunate to look forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B1F")

    label("loc_A7C")


    ChrTalk(
        0xC,
        (
            "Our company with Quincy and Armorika village\x01",
            "\"Armorica · Honey Company\" plan\x01",
            "It progresses gradually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Future prospects, everyone too\x01",
            "I am fortunate to look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1F")

    TalkEnd(0xFE)
    Return()

    # Function_9_989 end

    def Function_10_B23(): pass

    label("Function_10_B23")

    Call(0, 11)
    Return()

    # Function_10_B23 end

    def Function_11_B27(): pass

    label("Function_11_B27")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAE")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "Oh, everyone is the police … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, this situation\x01",
            "May I ask you a favor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, in our hotel now\x01",
            "Including guests from the original,\x01",
            "We accept many evacuees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because there is stockpile food,\x01",
            "Although it is expected to surpass about one month … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, more information\x01",
            "To everyone's concern that not entering\x01",
            "It is in a state that it is connected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Currently, it is done with minimal confusion\x01",
            "As this will continue …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FWe will be right away from now.\x01",
            "We will start action for the convergence of the situation.\x02\x03",
            "So, for a while\x01",
            "Could you please look at the situation like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, I got it.\x01",
            "Everyone please take care.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 6)

    label("loc_DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3B")

    ChrTalk(
        0xB,
        "Welcome to \"Hotel Millennium\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ufufu, at the hotel\x01",
            "To various customer's needs\x01",
            "We are responding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If there is something you want,\x01",
            "Please tell me anytime.\x02",
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
            "Accommodation in hotels and inn\x01",
            "CP can be recovered.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "CP100 for regular lodging bar,\x01",
            "At the luxury hotel CP 200 will recover.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F38")
    SetScenarioFlags(0x0, 0)

    label("loc_F38")

    SetScenarioFlags(0x136, 5)

    label("loc_F3B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F30")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",        # 0
            "To take a break\x01",      # 1
            "quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_FA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC1")
    OP_AF(0x45)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F2B")

    label("loc_FC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD5")
    Jump("loc_1F2B")

    label("loc_FD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F2B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1100")

    ChrTalk(
        0xB,
        (
            "Following a report on presidential detention,\x01",
            "Evacuation people also\x01",
            "I got back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although details are unknown about Taiki … ….\x01",
            "Tomorrow for the sunny weather\x01",
            "The street is calm as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, we\x01",
            "Various preparations within now\x01",
            "You have to proceed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123C")

    ChrTalk(
        0xB,
        (
            "In response to martial law and a notice of prohibition to go out,\x01",
            "Accepting refugees at our hotel\x01",
            "I examined it soon ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To moan, that moya\x01",
            "The appearance of a puppet soldier was unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Apparently, you also complain about your president\x01",
            "It seems that it has increased to the limit … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Right now,\x01",
            "It is the impression that the anxiety is greater.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12C6")

    label("loc_123C")


    ChrTalk(
        0xB,
        (
            "Apparently, you also complain about your president\x01",
            "It seems that it has increased to the limit … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Right now,\x01",
            "It is the impression that the anxiety is greater.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C6")

    Jump("loc_1F2B")

    label("loc_12CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_145F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A7")

    ChrTalk(
        0xB,
        (
            "The state of the speech is\x01",
            "Through the hotel's power net\x01",
            "I saw you … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I got a foreigner from a foreign country\x01",
            "To your upset\x01",
            "There was a terrible thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Somehow, everyone, until home country\x01",
            "I hope to arrive ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_145A")

    label("loc_13A7")


    ChrTalk(
        0xB,
        (
            "Conducted Railway Today\x01",
            "It seems to stop running … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, you\x01",
            "I can not talk if I can not get on the way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Including airship conditions of airships,\x01",
            "I will not gather information thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145A")

    Jump("loc_1F2B")

    label("loc_145F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1519")

    ChrTalk(
        0xB,
        (
            "A red light district dyed in the color of dusk and fire … …\x01",
            "The sight of that day is exactly what\x01",
            "There is nothing to say but a nightmare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… Anyway, as soon as possible\x01",
            "To regain everyday life\x01",
            "I will not do everything I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_15A2")

    ChrTalk(
        0xB,
        (
            "In the direction of Mainz\x01",
            "Even now the guards\x01",
            "I heard that he is fighting hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Really the guards are\x01",
            "私たちCitizenの誇りですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_15A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D4")

    ChrTalk(
        0xB,
        (
            "Yesterday because of the train accident,\x01",
            "Because the train schedule was greatly disturbed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all, staying at Crossbell\x01",
            "Some people extended the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, somehow this morning\x01",
            "I was fortunate that I could completely restore it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I got stuck\x01",
            "Customers, everyone this morning\x01",
            "Because I was able to send it safely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_175D")

    label("loc_16D4")


    ChrTalk(
        0xB,
        (
            "I was supposed to be stuck\x01",
            "Customers, everyone this morning\x01",
            "I was able to send it safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "All this,\x01",
            "It is thanks to the guards.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175D")

    Jump("loc_1F2B")

    label("loc_1762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1813")

    ChrTalk(
        0xB,
        (
            "Anything in the direction of the West Crossbell Highway\x01",
            "I heard that a train accident happened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I am going to return home from now on today.\x01",
            "In order not to confuse customers\x01",
            "First of all I have to gather information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_19CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1916")

    ChrTalk(
        0xB,
        (
            "We also offer reservation service with conductive net\x01",
            "Thanks to you I have received a favorable reception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Currently more people to use\x01",
            "Although it is certain that there are few … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To further expand the network,\x01",
            "Number of reservations made by communication device\x01",
            "I am certain that I will surpass it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19CA")

    label("loc_1916")


    ChrTalk(
        0xB,
        (
            "The wonderful point of the power net\x01",
            "Even if it is outside the reception hours\x01",
            "It is located where you can get a reservation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Unlike the communication device, the guiding mail\x01",
            "It can send and receive at any time 24 hours\x01",
            "Because it is possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CA")

    Jump("loc_1F2B")

    label("loc_19CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1A61")

    ChrTalk(
        0xB,
        "Is it the right or wrong of national independence ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although it is a very difficult problem,\x01",
            "それをCitizenに問う事は\x01",
            "I think that it is very meaningful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1ACB")

    ChrTalk(
        0xB,
        (
            "Uhufu, finally\x01",
            "The plenary session will begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To Mayor Dieter\x01",
            "I will not do my best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1BA3")

    ChrTalk(
        0xB,
        (
            "Before I got the manager,\x01",
            "In the past we have various people in the past\x01",
            "We have a track record of inviting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was sorry that there was no talk this time,\x01",
            "To some of the leaders of each country\x01",
            "We would like you to stay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1C5D")

    ChrTalk(
        0xB,
        (
            "As involved in the hotel industry\x01",
            "The commerce meeting from tomorrow\x01",
            "I will draw a lot of attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Depending on the content of the agreement\x01",
            "今後のtouristの数などに\x01",
            "It will also have an impact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1DBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D19")

    ChrTalk(
        0xB,
        "It is raining today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In the hotel, even on rainy days\x01",
            "Enjoy sightseeing spots\x01",
            "We are introducing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please feel free to\x01",
            "Please contact us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DB9")

    label("loc_1D19")


    ChrTalk(
        0xB,
        (
            "Basically, this red light district\x01",
            "Enjoy it even on rainy days\x01",
            "It's almost place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Still, for those who are busy going out,\x01",
            "We also offer various room service of our hotel\x01",
            "I recommend it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB9")

    Jump("loc_1F2B")

    label("loc_1DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1F2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E88")

    ChrTalk(
        0xB,
        "Welcome to \"Hotel Millennium\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ufufu, at the hotel\x01",
            "To various customer's needs\x01",
            "We are responding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If there is any demand,\x01",
            "Please tell me anytime.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F2B")

    label("loc_1E88")


    ChrTalk(
        0xB,
        (
            "Esthetic and meal room service,\x01",
            "For various booking services\x01",
            "Reservation service using power net ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At the hotel, various kinds of customers\x01",
            "ニーズにWe are responding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2B")

    Jump("loc_F45")

    label("loc_1F30")

    TalkEnd(0xB)
    Return()

    # Function_11_B27 end

    def Function_12_1F34(): pass

    label("Function_12_1F34")

    Call(0, 13)
    Return()

    # Function_12_1F34 end

    def Function_13_1F38(): pass

    label("Function_13_1F38")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A9")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "Welcome to \"Hotel Millennium\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At the reception, we can also make reservations for the day\x01",
            "We accept it,\x01",
            "Please do not hesitate to tell us.\x02",
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
            "Accommodation in hotels and inn\x01",
            "CP can be recovered.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "CP100 for regular lodging bar,\x01",
            "At the luxury hotel CP 200 will recover.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x136, 5)

    label("loc_20A9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_304E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",        # 0
            "To take a break\x01",      # 1
            "quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_210F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_212F")
    OP_AF(0x45)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3049")

    label("loc_212F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2143")
    Jump("loc_3049")

    label("loc_2143")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3049")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_227C")

    ChrTalk(
        0x8,
        (
            "Under the direction of the manager, for emergency\x01",
            "More than ever\x01",
            "I decided to strengthen it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, regarding various materials\x01",
            "Unlimited products within autonomous state\x01",
            "I am not going to buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Considering consultation to the government,\x01",
            "Means to buy from foreign countries\x01",
            "It is where we are beginning to search.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_227C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2379")

    ChrTalk(
        0x8,
        (
            "At the same time as the appearance of the moya\x01",
            "The state of the rushing people,\x01",
            "It was already panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "人形の兵士がCitizenを襲う事は\x01",
            "Since it is understood that it does not exist at all,\x01",
            "I calmed down a bit … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, as soon as possible this situation\x01",
            "I'd like you to do something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_2379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_247B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F0")

    ChrTalk(
        0x8,
        (
            "…… To this morning's speech\x01",
            "It was truly amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The president's argument,\x01",
            "I can understand, but …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2476")

    label("loc_23F0")


    ChrTalk(
        0x8,
        (
            "…… Hmm, for now tentatively\x01",
            "I should not say something extra\x01",
            "There is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway …\x01",
            "For a while\x01",
            "There is no choice but to watch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2476")

    Jump("loc_3049")

    label("loc_247B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_254D")

    ChrTalk(
        0x8,
        (
            "On the day of the raid, fortunately in the hotel\x01",
            "Although there was not much damage, … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The alkane shell ……\x01",
            "It is really terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I do not know what is the purpose … …\x01",
            "Such a job,\x01",
            "It can not be forgiven.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_254D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2600")

    ChrTalk(
        0x8,
        (
            "The incident occurring in Mainz\x01",
            "It is a conspiracy of the empire\x01",
            "There seems to be many people who think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If that is true … …\x01",
            "What was the battle convention?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_2600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_26B2")

    ChrTalk(
        0x8,
        (
            "Yesterday was due to the accident\x01",
            "I would like to cancel my stay\x01",
            "I received much contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The transcontinental railroad is exactly\x01",
            "Life line for us ……\x01",
            "I am relieved that the damage is minimal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_26B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_272A")

    ChrTalk(
        0x8,
        "Hmm, is there a train accident ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In Crossbell\x01",
            "It is a relatively unusual thing ……\x01",
            "What is the cause of the unification?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_272A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_287B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27FC")

    ChrTalk(
        0x8,
        (
            "最近Dorisさんの仕事ぶりが\x01",
            "The stiffness is getting better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Cleaning dolls, of course,\x01",
            "The reputation from our customers was also excellent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I also serve as an educator\x01",
            "Aaronさんの指導の賜物ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2876")

    label("loc_27FC")


    ChrTalk(
        0x8,
        (
            "最近Dorisさんの仕事ぶりが\x01",
            "The stiffness is getting better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I also serve as an educator\x01",
            "Aaronさんの指導の賜物ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2876")

    Jump("loc_3049")

    label("loc_287B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_297B")

    ChrTalk(
        0x8,
        (
            "I am a Crossbell person,\x01",
            "Previously to the hotel of the Empire\x01",
            "I have been working for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What is that saying,\x01",
            "When I was in the Empire to the nobility people\x01",
            "It is a day to wear nerve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After coming here, elongation\x01",
            "I am allowed to do the work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A1A")

    label("loc_297B")


    ChrTalk(
        0x8,
        (
            "Empire hotel services technology\x01",
            "It was a good environment to learn,\x01",
            "That was exhausting fatigue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After coming here, elongation\x01",
            "I am allowed to do the work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1A")

    Jump("loc_3049")

    label("loc_2A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B04")

    ChrTalk(
        0x8,
        (
            "Yesterday, on the way home from work\x01",
            "While watching the Orchise Tower\x01",
            "I was wondering, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, it is that powerful\x01",
            "It was more than I was listening to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Next time, I definitely went closer,\x01",
            "I would like to look up at the building.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B88")

    label("loc_2B04")


    ChrTalk(
        0x8,
        (
            "In the distance, the Orkil Tower\x01",
            "I was really overwhelmed by the force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Next time, I definitely went closer,\x01",
            "I would like to look up at the building.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B88")

    Jump("loc_3049")

    label("loc_2B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C57")

    ChrTalk(
        0x8,
        (
            "Customers see the state of the unveiling ceremony\x01",
            "Did you visit us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Fireworks were also launched for everything,\x01",
            "It was a very casual ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The tolerance of Orkis Tower ……\x01",
            "I would like to see you as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CD9")

    label("loc_2C57")


    ChrTalk(
        0x8,
        (
            "In the unveiling ceremony fireworks were also launched,\x01",
            "I heard that there was a very good response.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The tolerance of Orkis Tower ……\x01",
            "I would like to see you as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD9")

    Jump("loc_3049")

    label("loc_2CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD2")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "It is fine weather today, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the city there is a police watch system\x01",
            "Although it is laid down,\x01",
            "There is no difference in sightseeing daylight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Somewhere good spot\x01",
            "If you are looking for, according to your purpose\x01",
            "Will you show me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E5B")

    label("loc_2DD2")


    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "It is fine weather today, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Somewhere good spot\x01",
            "If you are looking for, according to your purpose\x01",
            "Will you show me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E5B")

    Jump("loc_3049")

    label("loc_2E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2A")

    ChrTalk(
        0x8,
        (
            "Good morning.\x01",
            "Welcome today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When going out in the rainy weather\x01",
            "If you let me know,\x01",
            "We also offer umbrellas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please do not hesitate to tell us.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F9E")

    label("loc_2F2A")


    ChrTalk(
        0x8,
        (
            "When going out in the rainy weather\x01",
            "If you let me know,\x01",
            "We also offer umbrellas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please do not hesitate to tell us.\x02",
    )

    CloseMessageWindow()

    label("loc_2F9E")

    Jump("loc_3049")

    label("loc_2FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3049")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "Welcome to \"Hotel Millennium\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At the reception, we can also make reservations for the day\x01",
            "We accept it,\x01",
            "Please do not hesitate to tell us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3049")

    Jump("loc_20B3")

    label("loc_304E")

    TalkEnd(0x8)
    Return()

    # Function_13_1F38 end

    def Function_14_3052(): pass

    label("Function_14_3052")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_312D")

    ChrTalk(
        0xFE,
        (
            "先ほどLetizia managerから\x01",
            "For the time being, we will operate business with outlook of profit\x01",
            "There was a manifestation of intention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now when the whole crossbell is difficult … …\x01",
            "I will make full use of my past experience\x01",
            "I am willing to support the manager with full power.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_312D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_31E6")

    ChrTalk(
        0xFE,
        (
            "With the free hotel offer at this time,\x01",
            "Manager is cherished for man, not Mira\x01",
            "I understood well that it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is possible for you to work under such circumstances\x01",
            "I think that I am truly happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_31E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32AE")

    ChrTalk(
        0xFE,
        (
            "Since the Declaration of Independence, the number of customers\x01",
            "Although it was decreasing day by day ……\x01",
            "The speech of this morning is decisive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is not a story to do at such a time, but …\x01",
            "The hotel also has to rethink its management policy\x01",
            "I will not get it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_32AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338D")

    ChrTalk(
        0xFE,
        (
            "The scratches left by the attack incident in the city\x01",
            "There is no other saying that it is too big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The damage of the guard is enormous,\x01",
            "And even to that Iria girl … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things like this\x01",
            "Never to happen again … ….\x01",
            "However, I just think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3410")

    label("loc_338D")


    ChrTalk(
        0xFE,
        (
            "The damage of the guard is enormous,\x01",
            "And even to that Iria girl … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things like this\x01",
            "Never to happen again … ….\x01",
            "However, I just think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3410")

    Jump("loc_3E42")

    label("loc_3415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_34A6")

    ChrTalk(
        0xFE,
        (
            "The raid incident that occurred yesterday …\x01",
            "The situation is still converging\x01",
            "You do not seem to be headed for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People of Mainz\x01",
            "I am really worried about everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_34A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_354D")

    ChrTalk(
        0xFE,
        (
            "A derailment accident is mysterious\x01",
            "I heard that the demon's work is … …\x01",
            "It is an eerie story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The harbinger of something sinister,\x01",
            "Although I do not want to think that … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_354D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_360A")

    ChrTalk(
        0xFE,
        (
            "It's time for check-in customers\x01",
            "It's time to see it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently the effect of a train accident\x01",
            "You seem to be appearing right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, safely\x01",
            "I hope you will arrive ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_360A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_36B4")

    ChrTalk(
        0xFE,
        (
            "This time, the deluxe room\x01",
            "Being vacant is\x01",
            "That is not so unusual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, surely\x01",
            "For those who want to stay\x01",
            "Is that the target now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_36B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_389A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37DB")

    ChrTalk(
        0xFE,
        (
            "Come and stay at national independence ……\x01",
            "Although there are many opinion that basically agree\x01",
            "You seem to have various opinions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An old man like me,\x01",
            "About the threat of the two biggest countries absolutely\x01",
            "I will only think about it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the hotel was,\x01",
            "The cross-bell autonomous state is changing now\x01",
            "It may be a necessary time, is not it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3895")

    label("loc_37DB")


    ChrTalk(
        0xFE,
        (
            "An old man like me,\x01",
            "About the threat of the two biggest countries absolutely\x01",
            "I will only think about it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the hotel was,\x01",
            "The cross-bell autonomous state is changing now\x01",
            "It may be a necessary time, is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3895")

    Jump("loc_3E42")

    label("loc_389A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3929")

    ChrTalk(
        0xFE,
        (
            "At last the Trade Council\x01",
            "The plenary session will begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, with Mayor Dieter\x01",
            "To Mr. MacDaely\x01",
            "I can not say without expectation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_3929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39C7")

    ChrTalk(
        0xFE,
        (
            "On the Orkis Tower all floors\x01",
            "It seems that a power net has been drawn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, the hotel's guiding net reservations also\x01",
            "It seems to be getting more and more successful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E42")

    label("loc_39C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA4")

    ChrTalk(
        0xFE,
        (
            "There was a place I could not rely on a while ago\x01",
            "Dorisさんですが、なかなかどうして\x01",
            "Recently I can watch with confidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can feel the growth of backwardness on my skin …\x01",
            "As a person who has been assigned an education clerk\x01",
            "There is no more pleasure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B3B")

    label("loc_3AA4")


    ChrTalk(
        0xFE,
        (
            "Dorisさんが成長してくれて\x01",
            "I am really pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can feel the growth of backwardness on my skin …\x01",
            "As a person who has been assigned an education clerk\x01",
            "I do not have any more pleasure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B3B")

    Jump("loc_3E42")

    label("loc_3B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C37")

    ChrTalk(
        0xFE,
        (
            "Although it is not as strong as the anniversary,\x01",
            "The customer's foot of our hotel\x01",
            "We are making steady progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the guiding manager of the manager manager\x01",
            "Even the reservation system is well done echoing … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, no, \"Hotel Millennium\"\x01",
            "The future is bright.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CE5")

    label("loc_3C37")


    ChrTalk(
        0xFE,
        (
            "The fusion of tradition and innovation ……\x01",
            "それがLetizia managerの目指す\x01",
            "It is the way that our hotel is located.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I was also confused at the beginning,\x01",
            "Now I am talking about the manager\x01",
            "I fully trust you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE5")

    Jump("loc_3E42")

    label("loc_3CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DBF")

    ChrTalk(
        0xFE,
        (
            "The hotel is 60th anniversary of opening this year … …\x01",
            "By the way I started working here\x01",
            "Early 30 years have passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you notice it is the oldest share.\x01",
            "No, the flow of the times is\x01",
            "It is really early.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E42")

    label("loc_3DBF")


    ChrTalk(
        0xFE,
        (
            "Start working at this hotel\x01",
            "For more than 30 years ……\x01",
            "If you notice it is the oldest share.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, the flow of the times is\x01",
            "It is really early.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E42")

    TalkEnd(0xFE)
    Return()

    # Function_14_3052 end

    def Function_15_3E46(): pass

    label("Function_15_3E46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EEE")

    ChrTalk(
        0xFE,
        (
            "Finally, the people of evacuees as usual\x01",
            "I was able to see you off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation ……\x01",
            "Everyone, please give me the word of thanks\x01",
            "I was really happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_3EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F95")

    ChrTalk(
        0xFE,
        (
            "Whatever the situation ……\x01",
            "The reason the hotel is busy so far is\x01",
            "It is quite a long time since long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a member of Hotel Millennium,\x01",
            "We will make every effort to serve you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_3F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403F")

    ChrTalk(
        0xFE,
        (
            "I am in trouble\x01",
            "I can not swallow it … ….\x01",
            "Now I am filled with complicated feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Certainly by voting,\x01",
            "I agree with each other independently … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_409E")

    label("loc_403F")


    ChrTalk(
        0xFE,
        (
            "…… When you hold your hand, something\x01",
            "It is useless to think a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well … … I will not encourage work.\x02",
    )

    CloseMessageWindow()

    label("loc_409E")

    Jump("loc_486F")

    label("loc_40A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4184")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40D5")
    Call(0, 42)
    Return()

    label("loc_40D5")


    ChrTalk(
        0xFE,
        (
            "Sound of shooting at the roar of the monster,\x01",
            "And screaming at the angry of the police force … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Remembering the day of the attack,\x01",
            "Even now I can not stop trembling … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why is this such thing in this town …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_4184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_41ED")

    ChrTalk(
        0xFE,
        (
            "Main case incident ……\x01",
            "It is a terrible story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want you to solve it as soon as possible …\x02",
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_41ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_42A5")

    ChrTalk(
        0xFE,
        (
            "In a train accident yesterday\x01",
            "Many injured people appear to have come out,\x01",
            "Fortunately it seems that nobody died.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But inside is pretty\x01",
            "Some people were seriously injured ……\x01",
            "Anyway, I want you to get better soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_42A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4306")

    ChrTalk(
        0xFE,
        (
            "It was a train accident ……\x01",
            "It is really terrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Passengers are worried.\x02",
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_4306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438C")

    ChrTalk(
        0xFE,
        "Well, I will work hard today as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, and a smile to our customers\x01",
            "I will not forget it. (Nicoli)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_440F")

    label("loc_438C")


    ChrTalk(
        0xFE,
        (
            "You scratched sweat for someone\x01",
            "It is really pleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it?\x01",
            "You are being needed,\x01",
            "I can feel it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_440F")

    Jump("loc_486F")

    label("loc_4414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_44B8")

    ChrTalk(
        0xFE,
        (
            "Of alkane shell\x01",
            "The day of the renewal performance is\x01",
            "It is finally approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tickets to flowing stones\x01",
            "I could not take it,\x01",
            "I am looking forward to what kind of stage it will be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_44B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4580")

    ChrTalk(
        0xFE,
        (
            "Customer, Times Department store's\x01",
            "Have you already been to the rooftop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I watch everything Orkis Tower\x01",
            "It is said that it is a superb spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If not yet,\x01",
            "How about going there?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45FF")

    label("loc_4580")


    ChrTalk(
        0xFE,
        (
            "The rooftop of the Times department store\x01",
            "Watch Orchise Tower\x01",
            "It is said that it is a superb spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Customers,\x01",
            "How about going there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45FF")

    Jump("loc_486F")

    label("loc_4604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_46BE")

    ChrTalk(
        0xFE,
        (
            "After the unveiling ceremony for VIP people,\x01",
            "Each place\x01",
            "I heard that you are going to be visited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you can see it somewhere\x01",
            "I'm happy, but ….\x01",
            "It is difficult because the guard is hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_46BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_474C")

    ChrTalk(
        0xFE,
        (
            "最近Aaronさんに叱られることが\x01",
            "I'm getting less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Am I growing up?\x01",
            "Huhu, if so, I'm happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_474C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47F8")

    ChrTalk(
        0xFE,
        (
            "Rainy days absolutely\x01",
            "Because mud dirt will be attached,\x01",
            "Carpet cleaning is serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But where is going to be beautiful\x01",
            "To see it,\x01",
            "It is pretty pleasant, is not it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_47F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_486F")

    ChrTalk(
        0xFE,
        (
            "Good morning.\x01",
            "Are guests staying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When going out, the key of the room\x01",
            "Please do not forget to change.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486F")

    TalkEnd(0xFE)
    Return()

    # Function_15_3E46 end

    def Function_16_4873(): pass

    label("Function_16_4873")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_48FC")

    ChrTalk(
        0xFE,
        "Hmm, what shall we do today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the manager says, the hotel's\x01",
            "I also taste the service\x01",
            "It may be unexpected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4981")

    label("loc_48FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4981")

    ChrTalk(
        0xFE,
        (
            "Of course this hotel, room\x01",
            "Service is also top notch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, in the future when traveling crossbell\x01",
            "Let's use it by all means.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4981")

    TalkEnd(0xFE)
    Return()

    # Function_16_4873 end

    def Function_17_4985(): pass

    label("Function_17_4985")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4A00")

    ChrTalk(
        0xFE,
        (
            "Hehe, indeed the hotel\x01",
            "It does not seem bad to spend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for me, to the casino\x01",
            "I'd like to get in there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A90")

    label("loc_4A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4A90")

    ChrTalk(
        0xFE,
        (
            "Hehu, this time with a leading-edge railroad\x01",
            "I came, but the tiredness of the move\x01",
            "I got it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I put a little price,\x01",
            "It is certainly worth more than the price.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A90")

    TalkEnd(0xFE)
    Return()

    # Function_17_4985 end

    def Function_18_4A94(): pass

    label("Function_18_4A94")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Between me and my sister on my way home,\x01",
            "Suddenly caught in a moya\x01",
            "I evacuated to this hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……really,\x01",
            "I felt like I was living a life.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4A94 end

    def Function_19_4B20(): pass

    label("Function_19_4B20")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Onii-chan, when a moya comes out\x01",
            "Do your thing for me\x01",
            "It ran around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, cool mind\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_4B20 end

    def Function_20_4B93(): pass

    label("Function_20_4B93")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Everyone worried about this time …\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_4B93 end

    def Function_21_4BC0(): pass

    label("Function_21_4BC0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I want to return home as soon as possible ……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_4BC0 end

    def Function_22_4BE5(): pass

    label("Function_22_4BE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CCA")

    ChrTalk(
        0xFE,
        (
            "The barrier that protected the city\x01",
            "Where the hell have you been …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Besides, that kind of bad feeling\x01",
            "What are the monuments …?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hometown on the presidential day#4RCountry#Into\x01",
            "Just by failing to go home this …\x01",
            "Please do it badly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D2E")

    label("loc_4CCA")


    ChrTalk(
        0xFE,
        (
            "Hometown on the presidential day#4RCountry#Into\x01",
            "Just by failing to go home this …\x01",
            "Please do it badly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D2E")

    TalkEnd(0xFE)
    Return()

    # Function_22_4BE5 end

    def Function_23_4D32(): pass

    label("Function_23_4D32")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "In such a situation\x01",
            "If you know, immediately\x01",
            "I went home, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in such a nice room\x01",
            "Things that passed free of charge\x01",
            "I was very lucky.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_4D32 end

    def Function_24_4DDB(): pass

    label("Function_24_4DDB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Evacuated to the hotel\x01",
            "It is unlucky happiness really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But this situation …\x01",
            "I wonder how long it will last?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_4DDB end

    def Function_25_4E46(): pass

    label("Function_25_4E46")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Well, this room okay ♪\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_4E46 end

    def Function_26_4E71(): pass

    label("Function_26_4E71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 6)), scpexpr(EXPR_END)), "loc_4EA2")
    Call(0, 29)
    Jump("loc_4EA5")

    label("loc_4EA2")

    Call(0, 28)

    label("loc_4EA5")

    Return()

    # Function_26_4E71 end

    def Function_27_4EA6(): pass

    label("Function_27_4EA6")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_27_4EA6 end

    def Function_28_4ED8(): pass

    label("Function_28_4ED8")

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
            "─ ─ yeah, see you tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I look forward to working with you.\x02",
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

    def lambda_50CD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_50CD)

    def lambda_50DE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF79A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_50DE)
    WaitChrThread(0x17, 1)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sound(104, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x17,
        "Oh … … you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FEr, I'm sorry.\x02\x03",
            "In the village of Almorika\x01",
            "Derrickさんですよね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Oh, that's right, but ….\x01",
            "Is there something for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI was sorry I was late …\x01",
            "It is a person of the police's affairs support department.\x02\x03",
            "Could you please tell us a little bit?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x17)

    ChrTalk(
        0x17,
        "……got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "You are the mayor …\x01",
            "Is it my dad's deposit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "To call the police … …\x01",
            "Hun, it's a hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FEr, Uh ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "…… I have a rough idea.\x01",
            "My recent actions\x01",
            "I will say it wash it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Separately behind the dark things\x01",
            "I am not doing it,\x01",
            "Please listen to anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F(Hm … … It is an unexpected reaction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Then, I will ask you straight away.\x02\x03",
            "#00001FIn recent days, you\x01",
            "Minnesさんという方と\x01",
            "I hear you are going out with me ……\x02\x03",
            "Well, what purpose is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "… Well, that would be nice.\x01",
            "I just got to know\x01",
            "It is impossible for my father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "少し前から、Minnesさんには\x01",
            "I am looked after for something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Mainly concerning the reform of the village.\x02",
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
        "#10105FMum, is the reform of the village …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, that important thing\x01",
            "Silence to the mayor\x01",
            "Are you proceeding?\x02\x03",
            "#00006FEverything,\x01",
            "It's not good …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Mayor … … to my father\x01",
            "I talked over and over so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "But the words to return are decided\x01",
            "'I will not lose sight of what I should be '\x01",
            "\"The rapid change is not good\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "But even if we maintain the current situation\x01",
            "In such a country village\x01",
            "I do not think there is a future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "To survive the village,\x01",
            "Reform is absolutely necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "My father told me that place,\x01",
            "I do not know ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI see……\x01",
            "そんな中、そのMinnesという\x01",
            "Having met people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "…… He is different from his father\x01",
            "He got on my consultation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "そして、In the village of Almorika\x01",
            "Great possibilities for beekeeping\x01",
            "He seems to have headlined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "In the near future, in cooperation with him\x01",
            "Launch big business\x01",
            "I have plans as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWhat?\x01",
            "It's ridiculous story …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Hun …\x01",
            "It is this place that I can talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Is not it okay?\x01",
            "I will get back to the village soon.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58B1():
        OP_95(0xFE, 74620, 0, 5690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_58B1)
    Sleep(2000)

    def lambda_58CE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58CE)
    Sleep(50)

    def lambda_58DE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58DE)
    Sleep(50)

    def lambda_58EE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58EE)
    Sleep(50)

    def lambda_58FE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58FE)
    Sleep(50)

    def lambda_590E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_590E)
    Sleep(50)

    def lambda_591E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_591E)
    WaitChrThread(0x17, 1)
    SetChrFlags(0x17, 0x80)
    OP_0D()

    ChrTalk(
        0x102,
        "#00105FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FYou have gone ……\x02",
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
            "#00003FAnyways……\x01",
            "I came here.\x02\x03",
            "#00000FHere is one,\x01",
            "Minnesという男に、\x01",
            "Let's meet directly.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A07():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A07)
    Sleep(50)

    def lambda_5A17():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A17)
    Sleep(50)

    def lambda_5A27():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A27)
    Sleep(50)

    def lambda_5A37():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A37)
    Sleep(50)

    def lambda_5A47():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A47)

    ChrTalk(
        0x104,
        (
            "#00303FI see……\x01",
            "You may know a lot.\x02\x03",
            "#00300FOkay, then\x01",
            "I wonder if I try to rush in early.\x02",
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

    # Function_28_4ED8 end

    def Function_29_5B19(): pass

    label("Function_29_5B19")

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
            "#00001FWell then……\x01",
            "I will take it right away.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(600)
    Sound(808, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(330, 20, -1, -1)
    SetChrName("Middle-aged voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Gee\x01",
            "Which way?\x02\x03",
            "Room service\x01",
            "I do not remember asking … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMinnesさん……ですね？\x02\x03",
            "#00004FSuddenly I'm sorry,\x01",
            "Cross Bell police ·\x01",
            "It is a person of the affairs support department.\x02\x03",
            "#00000FA few things, what you want to ask\x01",
            "I do have …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-aged voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Aw,\x01",
            "Do not bother the police ……\x02\x03",
            "In such a case\x01",
            "please come in.\x01",
            "Because the key is open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F(No, it's kind of cheerful\x01",
            "Please put it in. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(More than we are thinking\x01",
            "It might be a good hand … …)\x02\x03",
            "#00005FEr …\x01",
            "Well then, I will excuse you.\x02",
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
            "#11PI will see you.\x01",
            "私がMinnesにございますが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhat day is it?\x01",
            "Is not it a case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAs I said earlier … ….\x01",
            "Let me ask you a couple of questions\x01",
            "I think that I will do.\x02\x03",
            "#00001FCan you help us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POf course.\x01",
            "Whatever you can cooperate with me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PSomething around here\x01",
            "Did it happen even in the incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHouse……\x01",
            "What I want to ask is\x01",
            "About you.\x02\x03",
            "I wonder what kind of person you are,\x01",
            "What to do in the village of Almorika\x01",
            "Are you doing …?\x02\x03",
            "#00001FI'd like to ask you a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHow is it?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0xC,
        (
            "#11POh well.\x01",
            "It is almost unnecessary.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    ChrTalk(
        0xC,
        (
            "#11PKohon … I am an officer at a company\x01",
            "It is a person who is being made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThe work content is from product development\x01",
            "We are wide to the sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PTo Almorika village, our company ……\x01",
            "Because of the important transaction of \"Quincy Company\"\x01",
            "I will visit you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FEr … um …!\x01",
            "Is that Quincy AG?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6361():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6361)
    Sleep(50)

    def lambda_6371():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6371)
    Sleep(50)

    def lambda_6381():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6381)
    Sleep(50)

    def lambda_6391():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6391)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FIt's a name I heard for the first time ……\x01",
            "Does your daughter know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00105FEr … … Quincy company,\x01",
            "It is a famous sweets manufacturer from overseas.\x02\x03",
            "#00104FIn the confectionery industry it is also a big company,\x01",
            "Certainly, also on the crossbell\x01",
            "I think that the goods were imported.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, by the way, when I was a child,\x01",
            "Such a manufacturer's chocolate\x01",
            "Like having bought and eating well ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, they are makers.\x01",
            "Because I do not see much consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHehe, it also\x01",
            "It will be unavoidable.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_656C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_656C)
    Sleep(50)

    def lambda_657C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_657C)
    Sleep(50)

    def lambda_658C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_658C)
    Sleep(50)

    def lambda_659C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_659C)
    Sleep(50)

    def lambda_65AC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_65AC)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11PI am in this position myself\x01",
            "I'm not good at sweet things.\x01",
            "It used to be truly disgusting in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThanks to my active participation in sales for many years\x01",
            "Recognized for power, to the present position\x01",
            "I had him tell me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P…… Oops,\x01",
            "Have the talk diverted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, no.\x01",
            "I am sorry excuse me.\x02\x03",
            "#00003F…… Kohon.\x01",
            "In the village of Almorika\x01",
            "You said \"transactions\".\x02\x03",
            "#00001FWhat is that transaction? …\x01",
            "村長の息子、Derrickさんに\x01",
            "Is it related to that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAnything, to the development of the village\x01",
            "It seems to be related, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PGee\x01",
            "Did you know so far?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11Pふむ、Derrickさん自ら\x01",
            "If information is banned,\x01",
            "There is no meaning to hide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHehe, I have a friendly relationship with him\x01",
            "I am building it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203Falso……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FCould you tell me more about it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHuhu, that would be nice.\x02",
    )

    CloseMessageWindow()
    OP_68(167980, 1500, 3640, 3000)

    def lambda_68F2():
        OP_95(0xFE, 164960, 0, 5520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_68F2)
    Sleep(500)

    def lambda_690F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_690F)
    Sleep(50)

    def lambda_691F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_691F)
    Sleep(50)

    def lambda_692F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_692F)
    Sleep(50)

    def lambda_693F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_693F)
    Sleep(50)

    def lambda_694F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_694F)
    Sleep(50)

    def lambda_695F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_695F)
    WaitChrThread(0xC, 1)
    OP_6F(0x1)

    ChrTalk(
        0xC,
        (
            "#5POur company, Quincy,\x01",
            "For the future of the confectionery industry,\x01",
            "Everyday, I am repeatedly studying hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PMeanwhile, from the head office\x01",
            "I have given a certain mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PThat is, to this crossbell\x01",
            "Advancement of Quincy Company,\x01",
            "It is to explore the foothold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FIn other words … …\x01",
            "Quincy's subsidiary\x01",
            "To the crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PHehe, you are right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PAnd at the beginning I went to the department store in the city\x01",
            "I went to look for hints ……\x01",
            "I met him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIt is said that it is made in Almorika village,\x01",
            "Very good 'honey'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHoney …… Armorica's\x01",
            "It is the one made in the astragalus field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHarold also said that quality\x01",
            "I guaranteed …\x02",
        )
    )

    CloseMessageWindow()
    OP_68(169610, 1500, 3430, 3000)

    def lambda_6BD6():
        OP_95(0xFE, 168410, 0, 5520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6BD6)
    Sleep(500)

    def lambda_6BF3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BF3)
    Sleep(50)

    def lambda_6C03():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C03)
    Sleep(50)

    def lambda_6C13():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C13)
    Sleep(50)

    def lambda_6C23():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C23)
    Sleep(50)

    def lambda_6C33():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C33)
    Sleep(50)

    def lambda_6C43():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C43)
    WaitChrThread(0xC, 1)

    def lambda_6C54():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6C54)
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11PA source of rich nature\x01",
            "It has been handed down from generation to generation.\x01",
            "Honey produced by the astragalus field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAs I saw it, like a revelation\x01",
            "Launch a new confectionery brand\x01",
            "One plan was born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThat plan name is ……\x01",
            "\"Armorica · Honey Company\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAlmorica · Honey Company ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FIt sounds like something terrible.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#11PIn other words, honey from Almorika village\x01",
            "Confectionery used abundantly\x01",
            "We will provide it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHowever, for that purpose,\x01",
            "Cooperation of the people of Almorika village\x01",
            "It was indispensable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11Pそこで私は、In the village of Almorika\x01",
            "次期村長であるDerrickさんに、\x01",
            "I have brought this story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PConstruction of a confectionery factory, and\x01",
            "Would you like to run this new company?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FDerrickさんに\x01",
            "A subsidiary of Quincy … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POf course, its know-how and sales line\x01",
            "Prepared by our company, since then, the astragalus field\x01",
            "I manage with this staff …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI will not bother you anything,\x01",
            "And to reduce the hardship of the villagers\x01",
            "I presented the conditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FBut, factory ……\x01",
            "Where on earth will be built\x01",
            "Are you planning on doing what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PRegarding that, in the past dealings,\x01",
            "To be able to lend private property of the village\x01",
            "You have done it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POriginally only as a storeroom\x01",
            "I heard that he was not using it,\x01",
            "It depends on acceptance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FCertainly that condition,\x01",
            "The possibility of getting on the story\x01",
            "It will be quite expensive.\x02\x03",
            "村の改革を願うDerrick君ならば\x01",
            "Even so ….\x02\x03",
            "#10302FJust for you,\x01",
            "Derrick君にとっても\x01",
            "That was not a bad story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHuh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIn fact, his talent and a strong sense of responsibility\x01",
            "I felt it deserved it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P… … Huhu, my story is such a place.\x01",
            "Did you understand?\x02",
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
            "#00003F…… I will tell you a story\x01",
            "Thank you very much.\x02\x03",
            "#00000FThanks and various\x01",
            "To the part which I did not understand\x01",
            "The answer seems to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11POh, are you already talking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, let me take your time\x01",
            "I am sorry.\x02\x03",
            "With ourselves\x01",
            "I will excuse myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PNo, no what's this.\x01",
            "Also any time\x01",
            "Please come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PPlease take care.\x01",
            "I hope to return.\x02",
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
            "#00106FFuu …\x01",
            "What I should say …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, somehow a great story\x01",
            "It was heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FあのMinnesという男……\x01",
            "You seem to have been more fun than you expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FThe story was a little difficult,\x01",
            "It certainly was a story that will make a profit ……\x02\x03",
            "#00301FBut, well ….\x02",
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
            "#10101F…… But even this one information is\x01",
            "You got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh……\x01",
            "Let's return to Almorika village once.\x02\x03",
            "#00001FI have to report to the mayor of Torta.\x02",
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

    # Function_29_5B19 end

    def Function_30_7861(): pass

    label("Function_30_7861")


    def lambda_7866():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7866)

    def lambda_7877():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7877)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 167730, 0, 2860, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_30_7861 end

    def Function_31_78AC(): pass

    label("Function_31_78AC")


    def lambda_78B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_78B1)

    def lambda_78C2():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_78C2)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 169150, 0, 2870, 2000, 0x0)
    Return()

    # Function_31_78AC end

    def Function_32_78F0(): pass

    label("Function_32_78F0")


    def lambda_78F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_78F5)

    def lambda_7906():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7906)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 170230, 0, 1900, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_32_78F0 end

    def Function_33_793B(): pass

    label("Function_33_793B")


    def lambda_7940():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7940)

    def lambda_7951():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7951)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 167400, 0, 1860, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_33_793B end

    def Function_34_7986(): pass

    label("Function_34_7986")


    def lambda_798B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_798B)

    def lambda_799C():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_799C)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 168250, 0, 1200, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_34_7986 end

    def Function_35_79D1(): pass

    label("Function_35_79D1")


    def lambda_79D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_79D6)

    def lambda_79E7():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_79E7)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 169670, 0, 1220, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_35_79D1 end

    def Function_36_7A1C(): pass

    label("Function_36_7A1C")


    def lambda_7A21():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A21)

    def lambda_7A32():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A32)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 68440, 0, 10210, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_36_7A1C end

    def Function_37_7A67(): pass

    label("Function_37_7A67")


    def lambda_7A6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7A6C)

    def lambda_7A7D():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A7D)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 67120, 0, 8910, 2000, 0x0)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_37_7A67 end

    def Function_38_7AB2(): pass

    label("Function_38_7AB2")


    def lambda_7AB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7AB7)

    def lambda_7AC8():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7AC8)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 70510, 0, 9150, 2000, 0x0)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_38_7AB2 end

    def Function_39_7AFD(): pass

    label("Function_39_7AFD")


    def lambda_7B02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7B02)

    def lambda_7B13():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7B13)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 67540, 0, 7130, 2000, 0x0)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_39_7AFD end

    def Function_40_7B48(): pass

    label("Function_40_7B48")


    def lambda_7B4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7B4D)

    def lambda_7B5E():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7B5E)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 69250, 0, 6220, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_40_7B48 end

    def Function_41_7B93(): pass

    label("Function_41_7B93")


    def lambda_7B98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7B98)

    def lambda_7BA9():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7BA9)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 70730, 0, 7540, 2000, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_41_7B93 end

    def Function_42_7BDE(): pass

    label("Function_42_7BDE")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D75")

    ChrTalk(
        0x9,
        "Well, cleaning and cleaning …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(If she's in a \"maid\" frame\x01",
            "It looks like you can qualify for Miscon. )\x02\x03",
            "#00000FExcuse me.\x01",
            "It is a little consultation … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Charity event\x01",
            "I asked for participation in Miscon.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        "Mi, Miscon … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, that, I'm sorry ….\x01",
            "I am pleased with your feeling\x01",
            "I can not get out of work ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so……\x01",
            "No, I was rude.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 7)
    Jump("loc_7DD9")

    label("loc_7D75")


    ChrTalk(
        0x9,
        (
            "The teaser to Miscon\x01",
            "A little……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am pleased with your feeling\x01",
            "I can not get out of work ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD9")

    TalkEnd(0x9)
    Return()

    # Function_42_7BDE end

    SaveToFile()

Try(main)
