from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0410.bin",                # FileName
        "e0410",                    # MapName
        "e0410",                    # Location
        0x00A0,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 270, 1, 160, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0410",                  # 0
        "Elderly Man",            # 1
        "Trader  ",               # 2
        "Father",                 # 3
        "Girl",                   # 4
        "Young Man",              # 5
        "Little Sister",          # 6
        "Big Brother",            # 7
        "Keeper",                 # 8
        "Shing",                  # 9
        "Girl",                   # 10
        "Woman",                  # 11
        "Rope",                   # 12
        "Dummy",                  # 13
        "Passenger",              # 14
        "Passenger",              # 15
        "Passenger",              # 16
        "Passenger",              # 17
        "Passenger",              # 18
        "Passenger",              # 19
        "Passenger",              # 20
        "Passenger",              # 21
        "Passenger",              # 22
        "Passenger",              # 23
        "Passenger",              # 24
        "Passenger",              # 25
        "Jaeger",                 # 26
        "Jaeger",                 # 27
        "Jaeger",                 # 28
        "Jaeger",                 # 29
        "Jaeger",                 # 30
        "Jaeger",                 # 31
        "Kilika",                 # 32
        "Lechter",                # 33
        "Fake Brand Trader",      # 34
        "Republican Terrorist",   # 35
        "Republican Terrorist",   # 36
        "Republican Terrorist",   # 37
        "Heiyue Member",          # 38
        "Heiyue Member",          # 39
    ))

    AddCharChip((
        "chr/ch20802.itc",                   # 00
        "chr/ch21802.itc",                   # 01
        "chr/ch21002.itc",                   # 02
        "chr/ch22302.itc",                   # 03
        "chr/ch22802.itc",                   # 04
        "chr/ch22102.itc",                   # 05
        "chr/ch22002.itc",                   # 06
        "chr/ch47602.itc",                   # 07
        "chr/ch45000.itc",                   # 08
        "chr/ch44202.itc",                   # 09
        "chr/ch21902.itc",                   # 0A
    ))

    DeclNpc(2200,    150,     5739,    180,  421,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(4294965037, 150,     1700,    0,    421,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(1769,    150,     699,     180,  421,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(2849,    150,     699,     180,  421,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(4294965046, 150,     4294965546, 180,  421,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(2200,    150,     3230,    180,  421,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(2220,    150,     1730,    0,    421,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(4294965556, 150,     709,     180,  421,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(4294964207, 0,       19,      270,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2279,    150,     4294965537, 180,  421,  0x0, 0,   9,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4294965096, 150,     4294964046, 0,    421,  0x0, 0,   10,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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

    DeclEvent(0x0000, 0, 35,  0.0,                   10.5,                  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -5.25,                 -0.0,                  1.0])
    DeclEvent(0x0000, 0, 36,  0.0,                   -10.0,                 0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.0,                   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 44,  0.0,                   0.0,                   0.0,                   0.0,                   [1.0,                  0.0,                   0.0,                   0.0,                   0.0,                   1.0,                   0.0,                   0.0,                   0.0,                   0.0,                   1.0,                   0.0,                   0.0,                   0.0,                   0.0,                   1.0])
    DeclEvent(0x0000, 0, 19,  0.0,                   9.199999809265137,     0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.599999904632568,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 20,  3.5,                   -7.849999904632568,    0.0,                   6.25,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3999999761581421,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.75,                 3.1399998664855957,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 21,  3.5,                   7.849999904632568,     0.0,                   6.25,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3999999761581421,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.75,                 -3.1399998664855957,   -0.0,                  1.0])

    ChipFrameInfo(2304, 0)                                       # 0

    ScpFunction((
        "Function_0_900",          # 00, 0
        "Function_1_9B8",          # 01, 1
        "Function_2_ADF",          # 02, 2
        "Function_3_C65",          # 03, 3
        "Function_4_CFE",          # 04, 4
        "Function_5_DB4",          # 05, 5
        "Function_6_E73",          # 06, 6
        "Function_7_EE0",          # 07, 7
        "Function_8_F5C",          # 08, 8
        "Function_9_FC4",          # 09, 9
        "Function_10_1026",        # 0A, 10
        "Function_11_114C",        # 0B, 11
        "Function_12_1254",        # 0C, 12
        "Function_13_12DC",        # 0D, 13
        "Function_14_1358",        # 0E, 14
        "Function_15_2359",        # 0F, 15
        "Function_16_2392",        # 10, 16
        "Function_17_48FA",        # 11, 17
        "Function_18_509D",        # 12, 18
        "Function_19_538B",        # 13, 19
        "Function_20_546A",        # 14, 20
        "Function_21_54D8",        # 15, 21
        "Function_22_5546",        # 16, 22
        "Function_23_59F6",        # 17, 23
        "Function_24_5F2B",        # 18, 24
        "Function_25_644C",        # 19, 25
        "Function_26_6B7E",        # 1A, 26
        "Function_27_6B87",        # 1B, 27
        "Function_28_70B6",        # 1C, 28
        "Function_29_7484",        # 1D, 29
        "Function_30_8444",        # 1E, 30
        "Function_31_8D54",        # 1F, 31
        "Function_32_91DE",        # 20, 32
        "Function_33_A201",        # 21, 33
        "Function_34_A44B",        # 22, 34
        "Function_35_C54F",        # 23, 35
        "Function_36_C599",        # 24, 36
        "Function_37_C5E3",        # 25, 37
        "Function_38_C61A",        # 26, 38
        "Function_39_C654",        # 27, 39
        "Function_40_C68E",        # 28, 40
        "Function_41_C6C8",        # 29, 41
        "Function_42_C702",        # 2A, 42
        "Function_43_C73C",        # 2B, 43
        "Function_44_F2C0",        # 2C, 44
        "Function_45_10F67",       # 2D, 45
        "Function_46_10FC3",       # 2E, 46
        "Function_47_11019",       # 2F, 47
        "Function_48_11053",       # 30, 48
        "Function_49_110AA",       # 31, 49
        "Function_50_11101",       # 32, 50
    ))


    def Function_0_900(): pass

    label("Function_0_900")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_940"),
        (1, "loc_94C"),
        (2, "loc_958"),
        (3, "loc_964"),
        (4, "loc_970"),
        (5, "loc_97C"),
        (6, "loc_988"),
        (SWITCH_DEFAULT, "loc_994"),
    )


    label("loc_940")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_94C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_958")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_964")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_970")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_97C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_988")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_994")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_9A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_9B7")

    Return()

    # Function_0_900 end

    def Function_1_9B8(): pass

    label("Function_1_9B8")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrSubChip(0x11, 0x1)
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_A7F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 14)
    Jump("loc_ADE")

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_A93")
    ClearScenarioFlags(0x22, 1)
    Event(0, 16)
    Jump("loc_ADE")

    label("loc_A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_AA7")
    ClearScenarioFlags(0x22, 2)
    Event(0, 17)
    Jump("loc_ADE")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_ABB")
    ClearScenarioFlags(0x22, 3)
    Event(0, 18)
    Jump("loc_ADE")

    label("loc_ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_ACF")
    ClearScenarioFlags(0x22, 4)
    Event(0, 43)
    Jump("loc_ADE")

    label("loc_ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_ADE")
    ClearScenarioFlags(0x22, 5)
    Event(0, 44)

    label("loc_ADE")

    Return()

    # Function_1_9B8 end

    def Function_2_ADF(): pass

    label("Function_2_ADF")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C26")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 4, 0x80)
    ModifyEventFlags(1, 5, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    SetMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC8")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 6)), scpexpr(EXPR_END)), "loc_B6B")
    ModifyEventFlags(0, 3, 0x80)

    label("loc_B6B")

    OP_78(0x3, 0x13)
    SetChrPos(0x13, 0, 0, -9450, 0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_C21")

    label("loc_BC8")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ClearMapObjFlags(0x2, 0x10)
    SetMapObjFlags(0x2, 0x2)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_C21")

    Jump("loc_C64")

    label("loc_C26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C64")
    SetMapObjFlags(0x2, 0x10)
    BeginChrThread(0x13, 3, 0, 15)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0xF0, 0x0, 0x0, 0x20)

    label("loc_C64")

    Return()

    # Function_2_ADF end

    def Function_3_C65(): pass

    label("Function_3_C65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_END)), "loc_CDF")

    ChrTalk(
        0xFE,
        (
            "I-I'm sorry but, could\x01",
            "you wait a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I absolutely have the\x01",
            "ticket. I'll find it for\x01",
            "sure!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFA")

    label("loc_CDF")

    Call(0, 25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CFA")
    Call(0, 26)

    label("loc_CFA")

    TalkEnd(0xFE)
    Return()

    # Function_3_C65 end

    def Function_4_CFE(): pass

    label("Function_4_CFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_END)), "loc_D95")

    ChrTalk(
        0xFE,
        (
            "If I settle this business\x01",
            "negotiation, there's no\x01",
            "doubt I'll profit greatly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mwhuhuhu, I can't help\x01",
            "but look forward to it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB0")

    label("loc_D95")

    Call(0, 24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB0")
    Call(0, 26)

    label("loc_DB0")

    TalkEnd(0xFE)
    Return()

    # Function_4_CFE end

    def Function_5_DB4(): pass

    label("Function_5_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_END)), "loc_E57")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Today I'm going to visit\x01",
            "my parents' home in the\x01",
            "Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My daughter hasn't seen her\x01",
            "grandparents in a while and\x01",
            "looks very happy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_E72")

    label("loc_E57")

    Call(0, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E72")
    Call(0, 26)

    label("loc_E72")

    Return()

    # Function_5_DB4 end

    def Function_6_E73(): pass

    label("Function_6_E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_END)), "loc_EC4")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Grandpa, grandma, I'm\x01",
            "coming now, so wait for\x01",
            "me, 'k?♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_EDF")

    label("loc_EC4")

    Call(0, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EDF")
    Call(0, 26)

    label("loc_EDF")

    Return()

    # Function_6_E73 end

    def Function_7_EE0(): pass

    label("Function_7_EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_END)), "loc_F40")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm going back to my\x01",
            "homeland, Ord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wonder how mom is\x01",
            "doing.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_F5B")

    label("loc_F40")

    Call(0, 22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F5B")
    Call(0, 26)

    label("loc_F5B")

    Return()

    # Function_7_EE0 end

    def Function_8_F5C(): pass

    label("Function_8_F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_END)), "loc_FA8")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Geez, I don't care about\x01",
            "you anymore, big\x01",
            "brother!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_FC3")

    label("loc_FA8")

    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC3")
    Call(0, 31)

    label("loc_FC3")

    Return()

    # Function_8_F5C end

    def Function_9_FC4(): pass

    label("Function_9_FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_END)), "loc_100A")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh", what a totally\x01",
            "uncute little sister.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1025")

    label("loc_100A")

    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1025")
    Call(0, 31)

    label("loc_1025")

    Return()

    # Function_9_FC4 end

    def Function_10_1026(): pass

    label("Function_10_1026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_END)), "loc_1130")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10CD")

    ChrTalk(
        0xFE,
        (
            "Haha. It appears that this\x01",
            "trip was quite meaningful\x01",
            "for Lord Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is thanks to all of\x01",
            "you as well. Thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1128")

    label("loc_10CD")


    ChrTalk(
        0xFE,
        (
            "Yes, the weather is\x01",
            "bright and nice today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, ideal weather for\x01",
            "a train ride.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1128")

    TalkEnd(0xFE)
    Jump("loc_114B")

    label("loc_1130")

    Call(0, 29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114B")
    Call(0, 31)

    label("loc_114B")

    Return()

    # Function_10_1026 end

    def Function_11_114C(): pass

    label("Function_11_114C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_END)), "loc_1238")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(
        0xFE,
        (
            "In any case, I'm going\x01",
            "to come to Crossbell\x01",
            "again for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Until then, farewell.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1230")

    label("loc_11C8")


    NpcTalk(
        0xFE,
        "Boy",
        (
            "What, do you still need\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Boy",
        (
            "Hmph, I'm busy. Don't\x01",
            "talk to me without a\x01",
            "reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1230")

    TalkEnd(0xFE)
    Jump("loc_1253")

    label("loc_1238")

    Call(0, 29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1253")
    Call(0, 31)

    label("loc_1253")

    Return()

    # Function_11_114C end

    def Function_12_1254(): pass

    label("Function_12_1254")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_END)), "loc_12BD")

    ChrTalk(
        0xFE,
        (
            "*mumble*... I wonder how\x01",
            "long until departure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*aahn*, I don't want to\x01",
            "go...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D8")

    label("loc_12BD")

    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12D8")
    Call(0, 31)

    label("loc_12D8")

    TalkEnd(0xFE)
    Return()

    # Function_12_1254 end

    def Function_13_12DC(): pass

    label("Function_13_12DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_END)), "loc_1339")

    ChrTalk(
        0xFE,
        (
            "What is it? You're\x01",
            "finished, aren't you? Then\x01",
            "get out of here already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1354")

    label("loc_1339")

    Call(0, 27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1354")
    Call(0, 31)

    label("loc_1354")

    TalkEnd(0xFE)
    Return()

    # Function_13_12DC end

    def Function_14_1358(): pass

    label("Function_14_1358")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    LoadChrToIndex("chr/ch24202.itc", 0x20)
    LoadChrToIndex("chr/ch24402.itc", 0x21)
    LoadChrToIndex("chr/ch24502.itc", 0x22)
    LoadChrToIndex("chr/ch27602.itc", 0x23)
    LoadChrToIndex("chr/ch33102.itc", 0x24)
    LoadChrToIndex("chr/ch33202.itc", 0x25)
    LoadChrToIndex("chr/ch32302.itc", 0x26)
    LoadChrToIndex("chr/ch22302.itc", 0x27)
    LoadChrToIndex("chr/ch21802.itc", 0x28)
    SoundLoad(450)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis008.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -2000, 150, -750, 0)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, -2000, 150, 750, 180)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -2600, 150, 3300, 180)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -1600, 150, -3300, 0)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -2600, 150, -3300, 0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 2600, 150, 750, 180)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 1800, 150, 1800, 0)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 1800, 150, 3300, 180)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -1600, 150, 4350, 0)
    SetChrChipByIndex(0x1C, 0x27)
    SetChrSubChip(0x1C, 0x2)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 2600, 150, -4350, 180)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 1600, 150, -4350, 180)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0x0, 0xF0, 0x0, 0x20)
    BeginChrThread(0x101, 3, 0, 15)
    OP_68(0, 900, -1000, 0)
    MoveCamera(312, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(19000, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Sound(450, 2, 100, 0)
    SetCameraDistance(16500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-2300, 900, 350, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Sergeant Major Noｱl")

    AnonymousTalk(
        0xFF,
        (
            "*sigh*... Still, I'm glad we\x01",
            "accomplished the mission.\x02\x03",
            "Honestly, I wondered if I would\x01",
            "just be holding everyone else back.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#6P#00002FHaha, you sure are a worrywart.\x02\x03",
            "#00004FIt's because Commander Sonya has such high\x01",
            "expectations for you, Sergeant Major, that\x01",
            "she recommended you, you know.\x02\x03",
            "#00000FAnyway. I'm repeating myself, but I'm\x01",
            "looking forward to working with you from\x01",
            "now on.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x109,
        "Master Sgt. Noｱl",
        (
            "#10109F#11PYes, likewise!\x02\x03",
            "#10105F...Ah, but Lloyd. Could\x01",
            "I say one thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHmm?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x109,
        "Master Sgt. Noｱl",
        (
            "#10106F#11PYou see, we'll be working\x01",
            "together for quite some\x01",
            "time, you see...\x02\x03",
            "#10102FSince I'm not even wearing\x01",
            "the uniform, "Sergeant\x01",
            "Major" is... overly formal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FY-Yeah, that's true.\x02\x03",
            "#00000FWhat do we do then? Do\x01",
            "you mind if I address\x01",
            "you informally?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x109,
        "Master Sgt. Noｱl",
        "#10109F#11PNo, please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FThen, Noｱl─ It's great to be\x01",
            "working with you again.\x02\x03",
            "#00002FThat's right. If you're okay\x01",
            "with it, address me more\x01",
            "informally too.\x02\x03",
            "We're the same age and are\x01",
            "working together, so I don't\x01",
            "want you to worry about that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10111F#11PHUH!? Me? And you?\x02\x03",
            "#10106F............No, no,\x01",
            "that's just impossible!\x02\x03",
            "#10101FAfter all, I'm a novice\x01",
            "as a police officer. I\x01",
            "have so much to learn!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FWell, I don't think you have to\x01",
            "think of it as that formal...\x02\x03",
            "#00000FEven Elie and Randy talk to\x01",
            "each other casually without\x01",
            "regard to their age difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PWell, uhhm... How to say\x01",
            "this, it's like a part\x01",
            "of my personality...\x02\x03",
            "Once I've set out to do\x01",
            "something, it's not that\x01",
            "easy to change...\x02\x03",
            "#10101FBut, if you say so,\x01",
            "Lloyd, I'll do my best\x01",
            "to somehow─!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FAh, well. You don't have\x01",
            "to force yourself.\x02\x03",
            "#00002FHaha... Formal to the\x01",
            "core, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PAhaha... Maybe it's my\x01",
            "dad's influence.\x02\x03",
            "#10100FHe was strict and\x01",
            "disciplined Fran and I\x01",
            "ever since we were little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FOh. Your father, huh.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FWait, haven't I met your\x01",
            "mother several times?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PDad... He passed away around ten\x01",
            "years ago.\x02\x03",
            "#10100FHe served in the Crossbell\x01",
            "Guardian Force and, um, there was\x01",
            "an accident while he was on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FI see... Sorry for\x01",
            "bringing it up.\x02\x03",
            "#00001FSo... Was that why you\x01",
            "joined the CGF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#11PI wonder... I never really\x01",
            "thought of it that way, though.\x02\x03",
            "#10104FBut, I'm sure I wanted to\x01",
            "protect this land of Crossbell,\x01",
            "the same as my father did.\x02\x03",
            "#10100FIn that way, Fran and I are the\x01",
            "same, though our assignments\x01",
            "differ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FI see...\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00008F......\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F#11PLloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FSorry, nevermind.\x02\x03",
            "#00002F─But, I'm really glad\x01",
            "you came.\x02\x03",
            "We're lacking members...\x01",
            "And no one can say what\x01",
            "the future holds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#11PAhaha. It's an honor to\x01",
            "hear you say that,\x01",
            "but...\x02\x03",
            "#10102FWith the mafia gone,\x01",
            "order in the city has\x01",
            "improved, right?\x02\x03",
            "Heiyue is still there\x01",
            "but they're not making\x01",
            "any conspicuous moves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FThat's how it is on the\x01",
            "surface.\x02\x03",
            "#00008FHowever, you could say the\x01",
            "Revache organization was\x01",
            "carrying out a certain role.\x02\x03",
            "#00001FIn a way, they were\x01",
            "maintaining order in\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(450, 1000, 100)
    Sleep(1000)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("r0040", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1358 end

    def Function_15_2359(): pass

    label("Function_15_2359")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2391")
    OP_82(0xA, 0xA, 0x5DC, 0x2EE)
    Sleep(3500)
    OP_82(0xA, 0xA, 0x4B0, 0x1F4)
    Sleep(3500)
    Jump("Function_15_2359")

    label("loc_2391")

    Return()

    # Function_15_2359 end

    def Function_16_2392(): pass

    label("Function_16_2392")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248E")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆Max bond with Elie in Zero\x01",          # 0
            "◆Max bond with Tio in Zero\x01",           # 1
            "◆Max bond with Randy in Zero\x01",         # 2
            "◆Max bond with everyone in Zero\x01",      # 3
            "◆No change\x01",                           # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2463"),
        (1, "loc_246B"),
        (2, "loc_2473"),
        (3, "loc_247B"),
        (4, "loc_2489"),
        (SWITCH_DEFAULT, "loc_2489"),
    )


    label("loc_2463")

    SetScenarioFlags(0x25, 3)
    Jump("loc_248E")

    label("loc_246B")

    SetScenarioFlags(0x25, 4)
    Jump("loc_248E")

    label("loc_2473")

    SetScenarioFlags(0x25, 5)
    Jump("loc_248E")

    label("loc_247B")

    SetScenarioFlags(0x25, 3)
    SetScenarioFlags(0x25, 4)
    SetScenarioFlags(0x25, 5)
    Jump("loc_248E")

    label("loc_2489")

    Jump("loc_248E")

    label("loc_248E")

    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    LoadChrToIndex("chr/ch24202.itc", 0x20)
    LoadChrToIndex("chr/ch24402.itc", 0x21)
    LoadChrToIndex("chr/ch24502.itc", 0x22)
    LoadChrToIndex("chr/ch27602.itc", 0x23)
    LoadChrToIndex("chr/ch33102.itc", 0x24)
    LoadChrToIndex("chr/ch33202.itc", 0x25)
    LoadChrToIndex("chr/ch32302.itc", 0x26)
    LoadChrToIndex("chr/ch22302.itc", 0x27)
    LoadChrToIndex("chr/ch21802.itc", 0x28)
    LoadChrToIndex("apl/ch51029.itc", 0x29)
    SoundLoad(450)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis229.itp")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x121, 2)
    ClearScenarioFlags(0x121, 3)
    ClearScenarioFlags(0x121, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_255B")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis224.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_255B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_259E")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis225.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_25E1")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis226.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25E1")

    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -2000, 150, -750, 0)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, -2000, 150, 750, 180)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -2600, 150, 3300, 180)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -1600, 150, -3300, 0)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -2600, 150, -3300, 0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 2600, 150, 750, 180)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 1800, 150, 1800, 0)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 1800, 150, 3300, 180)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -1600, 150, 4350, 0)
    SetChrChipByIndex(0x1C, 0x27)
    SetChrSubChip(0x1C, 0x2)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 2600, 150, -4350, 180)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 1600, 150, -4350, 180)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0x0, 0xF0, 0x0, 0x20)
    BeginChrThread(0x101, 3, 0, 15)
    OP_68(-3500, 500, 0, 0)
    MoveCamera(270, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Sound(450, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10105FThe mafia was keeping\x01",
            "public order in\x01",
            "Crossbell...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThat's just how it turned out.\x02\x03",
            "#00001F...Try to think about the unique\x01",
            "situation Crossbell is in.\x02\x03",
            "Although it has autonomy, it's not\x01",
            "independent. Interference from the\x01",
            "two major powers is a constant.\x02\x03",
            "Its criminal law is full of holes\x01",
            "and it has hardly any immigration\x01",
            "regulations...\x02\x03",
            "#00003FSo it's not surprising that criminal\x01",
            "organizations or terrorists would\x01",
            "dominate, to say nothing of Heiyue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FAh...\x02\x03",
            "...Then, Revache's role\x01",
            "was to suppress all of\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FI don't want to admit it, but...\x01",
            "I can't deny it brought a\x01",
            "certain order to the underworld.\x02\x03",
            "#00006F...And out of the blue, they got\x01",
            "involved in the cult incident\x01",
            "and were wiped out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FAnd the balance of power\x01",
            "collapsed, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah... The same could be said of the\x01",
            "Imperial and Republic faction\x01",
            "congressmen who lost their seats.\x02\x03",
            "Having lost their spokesmen, it's\x01",
            "likely that pressure from both nations\x01",
            "will be more overt than before.\x02\x03",
            "#00013F...I think that's why the mayor is\x01",
            "expecting great things from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FI see... I finally\x01",
            "understand.\x02\x03",
            "#10100FIs it that why Elie, Randy\x01",
            "and Tio temporarily left the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, to be able to cooperate with\x01",
            "diverse groups and handle more advanced\x01",
            "activities, given the new situation.\x02\x03",
            "I myself trained at Section One and had\x01",
            "many things beaten into me...\x02\x03",
            "#00002FAnd, because we were short-handed, we\x01",
            "asked for new assets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha... Just being\x01",
            "selected was an honor.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2300, 900, -150, 0)
    MoveCamera(240, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#12P#10105FBut, now that I think\x01",
            "about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PHmm, what's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FThe other new member...\x01",
            "It's "him", the guy I\x01",
            "met before, right?\x02\x03",
            "How surprising. Why him?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#5PAah... "Him".\x02\x03",
            "#00006FWell, we had just started\x01",
            "looking for new members,\x01",
            "when he paid us a visit.\x02\x03",
            "He even had a recommendation\x01",
            "from the new mayor. We\x01",
            "couldn't turn him down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10111FA r-recommendation from\x01",
            "the mayor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5PYeah, it looks like he got it\x01",
            "as a thank you for helping with\x01",
            "the crisis at the IBC building.\x02\x03",
            "#00006F...I wonder where he heard we\x01",
            "were looking for new members in\x01",
            "the first place.\x02\x03",
            "Though he himself nonchalantly\x01",
            "said it "sounded\x01",
            "interesting"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FUhhm... Are things going\x01",
            "to be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PW-Well... He's not a bad guy. That\x01",
            "much is certain.\x02\x03",
            "#00002FOn the other hand, his career\x01",
            "history is unknown, he knows way too\x01",
            "much about the underworld and he\x01",
            "even works as host or something...\x02\x03",
            "#00006F...Saying it out loud like this, I'm\x01",
            "starting to get worried myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(400)
    Sound(2496, 255, 100, 0)
    Sleep(800)

    ChrTalk(
        0x109,
        (
            "#12P#10112FAhaha. I-It'll be fine.\x02\x03",
            "#10102FIt's true that he is sarcastic\x01",
            "and foul-mouthed, but I don't\x01",
            "think he's a bad person either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PHaha... It's a relief to\x01",
            "hear you say that.\x02\x03",
            "#00002FTo be honest, I wondered\x01",
            "if you two would get\x01",
            "along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FH-Hmm... He did make fun\x01",
            "of me, but...\x02\x03",
            "#10100FIf I had to say, it\x01",
            "seems he has more fun\x01",
            "teasing you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PUgh... Don't remind me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FAhaha... (I wonder if it's\x01",
            "better to not tell him that\x01",
            "Fran was taken with him...?)\x02",
        )
    )

    CloseMessageWindow()
    Sound(800, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Conductor's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Attention passengers.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We will arrive in\x01",
            "Crossbell City,\x01",
            "Crossbell State shortly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please transfer here for\x01",
            "airship routes to Liberl\x01",
            "and Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Furthermore, in accordance with Zemurian Rail\x01",
            "Corporation rules, this train will stop for\x01",
            "approximately 30 minutes at Crossbell Station.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Persons continuing to the Erebonia\x01",
            "region require an entry permit and\x01",
            "must submit to an inspection.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00002F#5PHaha. Since it's just one\x01",
            "stop away, we arrived in\x01",
            "the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10104FRight...\x02\x03",
            "#10102FAlthough, having been away\x01",
            "from home for a few days,\x01",
            "it feels kind of nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PYou're right...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(19500, 1500)
    Fade(250)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    OP_0D()
    Sleep(1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    SetMessageWindowPos(80, 200, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00004F#5P(...Just a while longer\x01",
            "and we'll be all\x01",
            "together again, huh...)\x02\x03",
            "#00002F(KeA... I hope she\x01",
            "didn't feel lonely.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3978")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWith whom did you talk at IBC 16F\x01",
            "the night of the Cult incident?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_38C4")
    MenuCmd(1, 0, "[Elie]")

    label("loc_38C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_38D6")
    MenuCmd(1, 0, "[Tio]")

    label("loc_38D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_38EA")
    MenuCmd(1, 0, "[Randy]")

    label("loc_38EA")

    MenuCmd(2, 0, -1, 100, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3928"),
        (1, "loc_3941"),
        (2, "loc_396B"),
        (SWITCH_DEFAULT, "loc_3973"),
    )


    label("loc_3928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3939")
    SetScenarioFlags(0x121, 2)
    Jump("loc_393C")

    label("loc_3939")

    SetScenarioFlags(0x121, 3)

    label("loc_393C")

    Jump("loc_3973")

    label("loc_3941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_395B")
    SetScenarioFlags(0x121, 3)
    Jump("loc_395E")

    label("loc_395B")

    SetScenarioFlags(0x121, 4)

    label("loc_395E")

    Jump("loc_3966")

    label("loc_3963")

    SetScenarioFlags(0x121, 4)

    label("loc_3966")

    Jump("loc_3973")

    label("loc_396B")

    SetScenarioFlags(0x121, 4)
    Jump("loc_3973")

    label("loc_3973")

    Jump("loc_39A6")

    label("loc_3978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3989")
    SetScenarioFlags(0x121, 2)
    Jump("loc_39A6")

    label("loc_3989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_399A")
    SetScenarioFlags(0x121, 3)
    Jump("loc_39A6")

    label("loc_399A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_39A6")
    SetScenarioFlags(0x121, 4)

    label("loc_39A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 2)), scpexpr(EXPR_END)), "loc_3E11")
    Sleep(300)

    ChrTalk(
        0x101,
        "#00004F#5P(Also...)\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x1C2, 0x3C)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    OP_4B(0x101, 0x3)
    SetChrSubChip(0x101, 0x1)
    OP_68(-2700, 900, 2040, 0)

    NpcTalk(
        0x15,
        "Elie",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00112F#N#11P...U-Umm... I should get\x01",
            "back to Bell.\x02\x03",
            "#00113FThere may be something I\x01",
            "can do for "uncle" and\x01",
            "the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 160, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00004FY-Yeah... I should\x01",
            "resupply and check our\x01",
            "equipment while I can.\x02\x03",
            "#00002F...Later.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x15,
        "Elie",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00102F#N#11PYes...\x02\x03",
            "#00113F...Umm, as for the sequel to what\x01",
            "just happened... Even if it comes\x01",
            "after this is all resolved...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 160, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00005FEh.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x15,
        "Elie",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00112F#N#11PN-Nevermind.\x02\x03",
            "#00109FS-See you later!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2300, 900, -150, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_4C(0x101, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x1C2, 0x64)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#5P(...Since then, we've both\x01",
            "been busy and there hasn't\x01",
            "been any progress at all...)\x02\x03",
            "(When Elie comes back,\x01",
            "somehow, I'll have to...\x01",
            "that sequel...)\x02\x03",
            "#00011F(No, no, it's not the\x01",
            "sequel! I must think about\x01",
            "her more seriously...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100F...Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)

    ChrTalk(
        0x101,
        (
            "#00011F#5PN-No, it's nothing!\x02\x03",
            "#00012FAnyway, I'm so tired! I\x01",
            "want rest on the SSS\x01",
            "sofa!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x109,
        (
            "#12P#10105F(A suspicious\x01",
            "reaction...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_487F")

    label("loc_3E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_42F4")
    Sleep(300)

    ChrTalk(
        0x101,
        "#00004F#5P(Also...)\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x1C2, 0x3C)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    OP_4B(0x101, 0x3)
    SetChrSubChip(0x101, 0x1)
    OP_68(-2700, 900, 2040, 0)

    NpcTalk(
        0x15,
        "Tio",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00204F#N#11P...Michelam Theme Park.\x02\x03",
            "When this mess is\x01",
            "resolved, please take me\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 160, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00011FWhaaa... Are you really okay with\x01",
            "that!?\x02\x03",
            "#00001FAh, but... Wouldn't a little more\x01",
            "serious promise be better?\x02\x03",
            "Something like, "whenever I'm in\x01",
            "trouble, no matter what happens,\x01",
            "come save me." Something like that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x15,
        "Tio",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00204F#N#11PNo, this will be fine.\x02\x03",
            "#00208FAnd, if this situation is not\x01",
            "safely resolved, this promise\x01",
            "will not be fulfilled...\x02\x03",
            "#00202FIn that sense, I think it is\x01",
            "plenty serious, isn't it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2300, 900, -150, 0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_4C(0x101, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x1C2, 0x64)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#5P(...Since then we've both\x01",
            "been busy and haven't had the\x01",
            "chance to go there yet...)\x02\x03",
            "(When Tio comes back, I\x01",
            "absolutely must keep that\x01",
            "promise.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105F...Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005F#5PAh, sorry.\x02\x03",
            "#00000F...By the way, Noｱl,\x01",
            "have you ever gone to\x01",
            "the theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FAt Michelam? Yes,\x01",
            "although just once, with\x01",
            "Fran.\x02\x03",
            "#10109FThe attractions are fun\x01",
            "too, but Mishy's cute!\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x109, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#5PI-I see... (Mishy is\x01",
            "super popular, eh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_487F")

    label("loc_42F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_487F")
    Sleep(300)

    ChrTalk(
        0x101,
        "#00004F#5P(Also...)\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x1C2, 0x3C)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(300)
    OP_4B(0x101, 0x3)
    SetChrSubChip(0x101, 0x1)
    OP_68(-2700, 900, 2040, 0)

    NpcTalk(
        0x15,
        "Randy",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00303F#N#11P...If the CGF advances,\x01",
            "we'll be the ones\x01",
            "fighting 'til the end.\x02\x03",
            "#00300FI don't want to push\x01",
            "milady and PeTiote too\x01",
            "hard.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00004F...Yeah, I know.\x02\x03",
            "#00000FYou and I have to stop\x01",
            "them somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 50, -1, -1)
    SetChrName("Randy")

    NpcTalk(
        0x15,
        "Randy",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00302F#N#11PThat's about it.\x02\x03",
            "#00309FI've got your back─\x01",
            "buddy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(0xD),
            "#00005FAh...\x02\x03",
            "#00002F...Roger that!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2300, 900, -150, 0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_4C(0x101, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x1C2, 0x64)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00008F#5P(Buddy, eh?)\x02\x03",
            "#00003F(Honestly, I can't think I'm\x01",
            "balanced as a man, yet.)\x02\x03",
            "#00000F(I'll have to try even harder\x01",
            "if I want to stand shoulder-\x01",
            "to-shoulder with him...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105F...Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005F#5PAh, sorry.\x02\x03",
            "#00000FBy the way, Noｱl, what\x01",
            "do you think of Randy?\x02\x03",
            "I want to get the\x01",
            "opinion of a CGF member\x01",
            "rather than a detective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FRandy?\x02\x03",
            "#10104FLet's see... As you might expect,\x01",
            "I feel he's not your average\x01",
            "soldier.\x02\x03",
            "#10100FHe's strong individually of\x01",
            "course, but I heard he has amazing\x01",
            "unit-level tactics as well...\x02\x03",
            "I think he's blazing through the\x01",
            "rehabilitation training he's doing\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PI see...\x02\x03",
            "#00008F(...Come to think of it,\x01",
            "Randy said he'd be using a\x01",
            "rifle in this training...)\x02\x03",
            "(I wonder if he's getting\x01",
            "over his time as a jaeger\x01",
            "a little.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_487F")

    OP_68(-2300, 1400, -150, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    StopSound(450, 1000, 100)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_01.pmf", 0x235, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2392 end

    def Function_17_48FA(): pass

    label("Function_17_48FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SoundLoad(450)
    LoadChrToIndex("chr/ch24202.itc", 0x1E)
    LoadChrToIndex("chr/ch24402.itc", 0x1F)
    LoadChrToIndex("chr/ch24502.itc", 0x20)
    LoadChrToIndex("chr/ch24102.itc", 0x21)
    LoadChrToIndex("chr/ch24002.itc", 0x22)
    LoadChrToIndex("chr/ch27602.itc", 0x23)
    LoadChrToIndex("chr/ch27802.itc", 0x24)
    LoadChrToIndex("chr/ch27702.itc", 0x25)
    LoadChrToIndex("chr/ch27902.itc", 0x26)
    LoadChrToIndex("chr/ch33102.itc", 0x27)
    LoadChrToIndex("chr/ch23502.itc", 0x28)
    LoadChrToIndex("chr/ch33202.itc", 0x29)
    LoadChrToIndex("chr/ch33002.itc", 0x2A)
    LoadChrToIndex("chr/ch20402.itc", 0x2B)
    LoadChrToIndex("chr/ch20502.itc", 0x2C)
    LoadChrToIndex("chr/ch21302.itc", 0x2D)
    LoadChrToIndex("chr/ch32402.itc", 0x2E)
    LoadChrToIndex("chr/ch32302.itc", 0x2F)
    LoadChrToIndex("chr/ch32202.itc", 0x30)
    LoadChrToIndex("chr/ch22302.itc", 0x31)
    LoadChrToIndex("chr/ch21802.itc", 0x32)
    LoadChrToIndex("chr/ch22002.itc", 0x33)
    LoadChrToIndex("chr/ch22102.itc", 0x34)
    LoadChrToIndex("chr/ch21902.itc", 0x35)
    LoadChrToIndex("chr/ch42802.itc", 0x3C)
    LoadChrToIndex("chr/ch42902.itc", 0x3D)
    LoadChrToIndex("chr/ch43002.itc", 0x3E)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0xF0, 0x0, 0x0, 0x20)
    BeginChrThread(0x101, 3, 0, 15)
    Sound(450, 2, 100, 0)
    OP_68(0, 900, 7000, 0)
    MoveCamera(303, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0x15, -2600, 150, -4350, 180)
    SetChrPos(0x16, -2600, 150, -750, 0)
    SetChrPos(0x17, -2600, 150, 650, 180)
    SetChrPos(0x18, -2600, 150, 4350, 0)
    SetChrPos(0x19, -1600, 150, -4350, 180)
    SetChrPos(0x1A, -1600, 150, 3150, 180)
    SetChrPos(0x1B, 1800, 150, -1800, 180)
    SetChrPos(0x1C, 1800, 150, 3150, 180)
    SetChrPos(0x1D, 2800, 150, 650, 180)
    SetChrPos(0x1E, 2800, 150, 3150, 180)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x2B)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x2D)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x29)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x21, -1600, 150, -1800, 180)
    SetChrPos(0x22, 1800, 150, 4350, 0)
    SetChrPos(0x23, 2800, 150, 4350, 0)
    SetChrChipByIndex(0x21, 0x3E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x3E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x3E)
    SetChrSubChip(0x23, 0x0)
    FadeToBright(1000, 0)
    OP_68(0, 900, -5000, 7000)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 900, 7000, 0)
    SetChrPos(0x15, -2600, 150, -4350, 180)
    SetChrPos(0x16, -1600, 150, -1800, 180)
    SetChrPos(0x17, -1600, 150, 1800, 0)
    SetChrPos(0x18, -1600, 150, 5650, 180)
    SetChrPos(0x19, 1800, 150, -4350, 180)
    SetChrPos(0x1A, 1800, 150, -1800, 180)
    SetChrPos(0x1B, 2800, 150, -1800, 180)
    SetChrPos(0x1C, 2800, 150, 650, 180)
    SetChrPos(0x1D, 2800, 150, 4350, 0)
    SetChrPos(0x1E, 2800, 150, 5650, 180)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x27)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x31)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x2F)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x2B)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x34)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x21, -2600, 150, 650, 180)
    SetChrPos(0x22, -1600, 150, -750, 0)
    SetChrPos(0x23, 1800, 150, 3150, 180)
    SetChrChipByIndex(0x21, 0x3E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x3E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x3C)
    SetChrSubChip(0x23, 0x0)
    FadeToBright(1000, 0)
    OP_68(0, 900, -5000, 7000)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 900, 7000, 0)
    SetChrPos(0x15, -2600, 150, -3150, 0)
    SetChrPos(0x16, -2600, 150, -1800, 180)
    SetChrPos(0x17, -2600, 150, 4350, 0)
    SetChrPos(0x18, -1600, 150, -4350, 180)
    SetChrPos(0x19, -1600, 150, 650, 180)
    SetChrPos(0x1A, -1600, 150, 4350, 0)
    SetChrPos(0x1B, 1800, 150, -1800, 180)
    SetChrPos(0x1C, 1800, 150, -750, 0)
    SetChrPos(0x1D, 1800, 150, 3150, 180)
    SetChrPos(0x1E, 2800, 150, 1800, 0)
    SetChrChipByIndex(0x15, 0x27)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x2B)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2D)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x2F)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x35)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x30)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x2C)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x21, 1800, 150, 5650, 180)
    SetChrPos(0x22, 2800, 150, -4350, 180)
    SetChrPos(0x23, 2800, 150, 5650, 180)
    SetChrChipByIndex(0x21, 0x3E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x3E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x3E)
    SetChrSubChip(0x23, 0x0)
    FadeToBright(1000, 0)
    OP_68(0, 900, -5000, 7000)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 900, 7000, 0)
    SetChrPos(0x15, -2600, 150, -750, 0)
    SetChrPos(0x16, -2600, 150, 5650, 180)
    SetChrPos(0x17, -1600, 150, -3150, 0)
    SetChrPos(0x18, -1600, 150, 650, 180)
    SetChrPos(0x19, -1600, 150, 5650, 180)
    SetChrPos(0x1A, 1800, 150, -4350, 180)
    SetChrPos(0x1B, 1800, 150, 4350, 0)
    SetChrPos(0x1C, 2800, 150, -5650, 0)
    SetChrPos(0x1D, 2800, 150, -750, 0)
    SetChrPos(0x1E, 2800, 150, 650, 180)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x28)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x30)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x2E)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x26)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x35)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x21, -2600, 150, 1800, 0)
    SetChrPos(0x22, -2600, 150, 3150, 180)
    SetChrPos(0x23, 1800, 150, -1800, 180)
    SetChrChipByIndex(0x21, 0x3E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x3E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x3D)
    SetChrSubChip(0x23, 0x0)
    FadeToBright(1000, 0)
    OP_68(0, 900, -5000, 7000)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(450, 1000, 100)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("r1020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_48FA end

    def Function_18_509D(): pass

    label("Function_18_509D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearScenarioFlags(0x156, 7)
    OP_68(270, 1000, -8380, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -570, 0, -8020, 0)
    SetChrPos(0x1, 990, 0, -8210, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004FAlright then. We're\x01",
            "responsible for the two\x01",
            "rear cars.\x02\x03",
            "#00001FIt looks like there's a\x01",
            "lot of passengers.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_520D")

    ChrTalk(
        0x102,
        (
            "#00100FIndeed. In any case,\x01",
            "let's check them one-by-\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x0)
    Jump("loc_5384")

    label("loc_520D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5270")

    ChrTalk(
        0x103,
        (
            "#00200FIndeed. Anyway, let's\x01",
            "check them in order\x01",
            "until we're done.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x1)
    Jump("loc_5384")

    label("loc_5270")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52C5")

    ChrTalk(
        0x104,
        (
            "#00304FWell anyway, let's make\x01",
            "sure to hit them all.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x2)
    Jump("loc_5384")

    label("loc_52C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5315")

    ChrTalk(
        0x109,
        (
            "#10100FYes. Anyway, let's check\x01",
            "them carefully.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x3)
    Jump("loc_5384")

    label("loc_5315")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5384")

    ChrTalk(
        0x105,
        (
            "#10300F*sigh*, at any rate, it\x01",
            "looks like we can only check\x01",
            "all of them thoroughly.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x4)

    label("loc_5384")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_509D end

    def Function_19_538B(): pass

    label("Function_19_538B")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53F1")

    ChrTalk(
        0x101,
        (
            "#00003F...Car no. 3's that way.\x01",
            "Let's first check all the\x01",
            "car no. 4 passengers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5453")

    label("loc_53F1")


    ChrTalk(
        0x101,
        (
            "#00003F...We're not responsible for\x01",
            "the forward cars. Let's focus\x01",
            "on our inspection for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5453")

    Sleep(50)
    SetChrPos(0x0, -10, 0, 7470, 180)
    EventEnd(0x4)
    Return()

    # Function_19_538B end

    def Function_20_546A(): pass

    label("Function_20_546A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F...Our inspection isn't\x01",
            "over yet. There's no way\x01",
            "we can leave the train.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)
    Return()

    # Function_20_546A end

    def Function_21_54D8(): pass

    label("Function_21_54D8")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F...Our inspection isn't\x01",
            "over yet. There's no way\x01",
            "we can leave the train.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, 7850, 270)
    EventEnd(0x4)
    Return()

    # Function_21_54D8 end

    def Function_22_5546(): pass

    label("Function_22_5546")

    EventBegin(0x0)
    Fade(500)
    OP_68(-2120, 1000, -1250, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -500, 0, -2100, 270)
    SetChrPos(0x1, -500, 0, -3080, 315)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're\x01",
            "assistant inspectors.\x02\x03",
            "Sorry to trouble you, but\x01",
            "may we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Mom...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5671")

    ChrTalk(
        0x102,
        (
            "#00105F(It looks like he didn't\x01",
            "hear you.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_578B")

    label("loc_5671")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56B8")

    ChrTalk(
        0x103,
        (
            "#00205F(It looks like he didn't\x01",
            "hear you...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_578B")

    label("loc_56B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56F8")

    ChrTalk(
        0x104,
        (
            "#00305F(Hm, he's not listening,\x01",
            "huh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_578B")

    label("loc_56F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5745")

    ChrTalk(
        0x109,
        (
            "#10105F(Uhhm... It looks like\x01",
            "he didn't hear you.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_578B")

    label("loc_5745")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_578B")

    ChrTalk(
        0x105,
        (
            "#10302F(Hehe, it looks like he\x01",
            "didn't hear you.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_578B")


    ChrTalk(
        0x101,
        "#00006F#4SUH, EXCUSE ME―\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5850")
    Jump("loc_589A")

    label("loc_5850")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5870")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_589A")

    label("loc_5870")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5890")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_589A")

    label("loc_5890")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_589A")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        "Oh, ah... Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I spaced out for a bit\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Um, you're inspectors,\x01",
            "right? Do your thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, well then―\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F―I've checked your hand luggage\x01",
            "and entry permit. Thank you for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, well you're very\x01",
            "welcome.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 4)
    OP_29(0x79, 0x1, 0x5)
    ClearChrFlags(0xC, 0x10)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_5546 end

    def Function_23_59F6(): pass

    label("Function_23_59F6")

    EventBegin(0x0)
    Fade(500)
    OP_68(1540, 1000, 90, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 500, 0, 440, 90)
    SetChrPos(0x1, 500, 0, -530, 90)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5ADE")
    Jump("loc_5B28")

    label("loc_5ADE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5AFE")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B28")

    label("loc_5AFE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B1E")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B28")

    label("loc_5B1E")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B28")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5BDE")
    Jump("loc_5C28")

    label("loc_5BDE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BFE")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C28")

    label("loc_5BFE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C1E")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C28")

    label("loc_5C1E")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C28")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FUmm, we're assistant\x01",
            "inspectors.\x02\x03",
            "Sorry to trouble you, but\x01",
            "may we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Inspection,\x01",
            "inspectiooon♪ Do your\x01",
            "thing, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, then allow me to\x01",
            "check.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F―I've checked your hand luggage\x01",
            "and entry permit. Thank you for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, don't worry about\x01",
            "it. It was the natural\x01",
            "thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Nice work, guys☆\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E3E")

    ChrTalk(
        0x102,
        "#00102F*giggle*, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F0D")

    label("loc_5E3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E7A")

    ChrTalk(
        0x103,
        (
            "#00202FHaha, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F0D")

    label("loc_5E7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EAE")

    ChrTalk(
        0x104,
        "#00309FHaha, thanks guys.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F0D")

    label("loc_5EAE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EE0")

    ChrTalk(
        0x109,
        "#10109FHaha, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F0D")

    label("loc_5EE0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F0D")

    ChrTalk(
        0x105,
        "#10309FHehe, thank you.\x02",
    )

    CloseMessageWindow()

    label("loc_5F0D")

    SetScenarioFlags(0x1CA, 3)
    OP_29(0x79, 0x1, 0x6)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_59F6 end

    def Function_24_5F2B(): pass

    label("Function_24_5F2B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1090, 1000, 2420, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -470, 0, 2090, 270)
    SetChrPos(0x1, -470, 0, 3000, 225)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6013")
    Jump("loc_605D")

    label("loc_6013")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6033")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_605D")

    label("loc_6033")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6053")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_605D")

    label("loc_6053")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_605D")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FPardon us, we're\x01",
            "assistant inspectors.\x02\x03",
            "Sorry to trouble you, but\x01",
            "may we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, I was waiting for\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Here you go. Please\x01",
            "check them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FO-Okay...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61A0")

    ChrTalk(
        0x102,
        (
            "#00105F(He's awfully hyper,\x01",
            "isn't he.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6284")

    label("loc_61A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61D7")

    ChrTalk(
        0x103,
        "#00200F(He's awfully hyper.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6284")

    label("loc_61D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6211")

    ChrTalk(
        0x104,
        "#00306F(He's rather hyper, eh?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6284")

    label("loc_6211")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_624A")

    ChrTalk(
        0x109,
        "#10105F(He's strangely hyper.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6284")

    label("loc_624A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6284")

    ChrTalk(
        0x105,
        (
            "#10303F(Hehe, he's quite hyper,\x01",
            "eh?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6284")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F―I've checked your hand luggage\x01",
            "and entry permit. Thank you for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hahaha. You guys saw it\x01",
            "too, right? This bundle\x01",
            "of contracts, I mean!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Actually, I'm heading to\x01",
            "a certain huge business\x01",
            "negotiation right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it goes well, I'll\x01",
            "certainly make a killing...\x01",
            "Maaan, I'm so excited!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-Is that so. Good luck,\x01",
            "then.\x02\x03",
            "#00003F(I see, so that's why\x01",
            "he's hyper.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 2)
    OP_29(0x79, 0x1, 0x7)
    ClearChrFlags(0x9, 0x10)
    SetChrSubChip(0x9, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_5F2B end

    def Function_25_644C(): pass

    label("Function_25_644C")

    EventBegin(0x0)
    Fade(500)
    OP_68(570, 1000, 5250, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 500, 0, 5450, 90)
    SetChrPos(0x1, 500, 0, 4450, 90)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6534")
    Jump("loc_657E")

    label("loc_6534")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6554")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_657E")

    label("loc_6554")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6574")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_657E")

    label("loc_6574")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_657E")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're\x01",
            "assistant inspectors.\x02\x03",
            "Sorry to trouble you, but\x01",
            "may we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, of course. I don't\x01",
            "mind.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F―I checked your hand\x01",
            "luggage and entry\x01",
            "permit.\x02\x03",
            "#00001FHowever...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Hm? What is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6759")

    ChrTalk(
        0x102,
        (
            "#00101FYes, it seems there's no\x01",
            "boarding ticket in your\x01",
            "hand luggage.\x02\x03",
            "Do you know anything\x01",
            "about that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_696A")

    label("loc_6759")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67DB")

    ChrTalk(
        0x103,
        (
            "#00201FYes, it seems there's no\x01",
            "boarding ticket in your\x01",
            "hand luggage.\x02\x03",
            "Do you know anything\x01",
            "about that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_696A")

    label("loc_67DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6860")

    ChrTalk(
        0x104,
        (
            "#00301FActually, it looks like\x01",
            "there's no boarding ticket\x01",
            "in your hand luggage.\x02\x03",
            "Know anything about that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_696A")

    label("loc_6860")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68E7")

    ChrTalk(
        0x109,
        (
            "#10101FYes, it looks like there's\x01",
            "no boarding ticket in your\x01",
            "hand luggage.\x02\x03",
            "Do you know anything about\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_696A")

    label("loc_68E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_696A")

    ChrTalk(
        0x105,
        (
            "#10304FYeah, it looks like\x01",
            "there's no boarding ticket\x01",
            "in your hand luggage.\x02\x03",
            "#10302FKnow anything about that?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_696A")

    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "N-No ticket, you say!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That can't be! I\x01",
            "remember putting it in\x01",
            "there―\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(1000)
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "...It's not there. It's\x01",
            "not anywhere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maybe in my clothes\x01",
            "pockets? No, but―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I-I'm sorry but, could\x01",
            "you wait a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure it's here\x01",
            "somewhere. I'll definitely\x01",
            "find it for you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FA-Alright... We'll ask\x01",
            "you again when we're\x01",
            "finished with the others.\x02\x03",
            "#00003F(Let's continue the\x01",
            "inspection and come back\x01",
            "to him later.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 1)
    OP_29(0x79, 0x1, 0x8)
    ClearChrFlags(0x8, 0x10)
    SetChrSubChip(0x8, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_644C end

    def Function_26_6B7E(): pass

    label("Function_26_6B7E")

    ModifyEventFlags(0, 3, 0x80)
    SetScenarioFlags(0x158, 6)
    Return()

    # Function_26_6B7E end

    def Function_27_6B87(): pass

    label("Function_27_6B87")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1900, 1000, -1610, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -520, 0, -3000, 270)
    SetChrPos(0x1, -520, 0, -2100, 270)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x0, 0)
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6C6F")
    Jump("loc_6CB9")

    label("loc_6C6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C8F")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CB9")

    label("loc_6C8F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CAF")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CB9")

    label("loc_6CAF")

    OP_52(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CB9")

    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FPardon us, we're\x01",
            "assistant inspectors.\x02\x03",
            "Sorry to trouble you, but\x01",
            "may we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Humph. You say that, but\x01",
            "it's not like I can\x01",
            "refuse, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Check them quickly, and\x01",
            "don't waste my time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FAlright. Excuse me.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F―I've checked your hand luggage\x01",
            "and entry permit. Thank you for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "...Hmph. I don't need\x01",
            "your thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You've no further business\x01",
            "with me, right? Leave\x01",
            "then, and make it quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FA-Alright. Excuse us.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F53")

    ChrTalk(
        0x102,
        (
            "#00106F(*sigh*, this job is\x01",
            "quite stressful, isn't\x01",
            "it.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70A0")

    label("loc_6F53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FA1")

    ChrTalk(
        0x103,
        (
            "#00206F(*sigh*, this is a\x01",
            "nerve-wracking job,\x01",
            "huh.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70A0")

    label("loc_6FA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FF3")

    ChrTalk(
        0x104,
        (
            "#00306F(*sigh*, this job is\x01",
            "pretty stressful too,\x01",
            "huh.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70A0")

    label("loc_6FF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7046")

    ChrTalk(
        0x109,
        (
            "#10106F(*sigh*, this job is\x01",
            "rather stressful, isn't\x01",
            "it.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70A0")

    label("loc_7046")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70A0")

    ChrTalk(
        0x105,
        (
            "#10304F(Hehe. Being an\x01",
            "inspector is a pretty\x01",
            "stressful job too, eh?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A0")

    OP_5A()
    SetScenarioFlags(0x1CB, 0)
    OP_29(0x79, 0x1, 0x9)
    ClearChrFlags(0x12, 0x10)
    SetChrSubChip(0x12, 0x0)
    EventEnd(0x5)
    Return()

    # Function_27_6B87 end

    def Function_28_70B6(): pass

    label("Function_28_70B6")

    EventBegin(0x0)
    Fade(500)
    OP_68(1240, 1000, -2420, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 490, 0, -1970, 90)
    SetChrPos(0x1, 490, 0, -3000, 90)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "Uhuhu. Compared to other\x01",
            "trains, the Eisengraf is\x01",
            "in a whole other league.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "*drool*... Oopsie, no, I\x01",
            "mustn't do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-Is she drooling?)\x02\x03",
            "#00000FExcuse us, we're\x01",
            "assistant inspectors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Ah, I'm busy train\x01",
            "watching now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "My permit's in my bag,\x01",
            "so feel free to inspect\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FU-Understood. Then...\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F―I've checked your hand luggage\x01",
            "and entry permit. Thank you for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "*mumble*... I wonder how\x01",
            "long until departure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "*aahn*, I don't want to\x01",
            "go...!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7374")

    ChrTalk(
        0x102,
        (
            "#00103F(...S-She looks like\x01",
            "quite focused.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7477")

    label("loc_7374")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73BC")

    ChrTalk(
        0x103,
        (
            "#00203F(...She didn't turn\x01",
            "around even once.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7477")

    label("loc_73BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73F6")

    ChrTalk(
        0x104,
        "#00306F(...Not listenin', huh?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_7477")

    label("loc_73F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_743E")

    ChrTalk(
        0x109,
        (
            "#10106F(...She likes trains\x01",
            "quite a lot, eh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7477")

    label("loc_743E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7477")

    ChrTalk(
        0x105,
        (
            "#10302F(Hehe, she's not\x01",
            "listening.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7477")

    OP_5A()
    SetScenarioFlags(0x1CA, 7)
    OP_29(0x79, 0x1, 0xA)
    EventEnd(0x5)
    Return()

    # Function_28_70B6 end

    def Function_29_7484(): pass

    label("Function_29_7484")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1170, 1000, -100, 0)
    MoveCamera(324, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x0, -530, 0, 410, 270)
    SetChrPos(0x1, -530, 0, -410, 270)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_756C")
    Jump("loc_75B6")

    label("loc_756C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_758C")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_75B6")

    label("loc_758C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_75AC")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_75B6")

    label("loc_75AC")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75B6")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FUmm, we're assistant\x01",
            "inspectors.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F(This suit... Could he\x01",
            "be with Heiyue?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Hmm, is there a problem?\x02",
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)
    Sleep(300)
    OP_93(0x10, 0x5A, 0x1F4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7CEA")
    OP_29(0x79, 0x1, 0xB)

    ChrTalk(
        0x10,
        "Hmm? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F―Wait, Shing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "―You guys! You're the\x01",
            "Special Support Section!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7778")

    ChrTalk(
        0x10,
        "And Elie's with you too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHaha. Hello Shing.\x02",
    )

    CloseMessageWindow()

    label("loc_7778")


    ChrTalk(
        0x10,
        (
            "But, what are you doing\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, as a job for the\x01",
            "SSS, we're helping the\x01",
            "inspector.\x02\x03",
            "And so, we'd like to\x01",
            "check your hand luggage\x01",
            "and entry permits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I see. So the Support\x01",
            "Section does these kinds\x01",
            "of jobs too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, whatever. If\x01",
            "that's how it is, then\x01",
            "get it over with.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F―Alright. I've checked\x01",
            "your hand luggage and\x01",
            "entry permit.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79C2")

    ChrTalk(
        0x102,
        (
            "#00100FThanks for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Haha. If it's for you,\x01",
            "Elie, this is nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "We'll meet again\x01",
            "someday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, I'm looking\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CE5")

    label("loc_79C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AF2")

    ChrTalk(
        0x103,
        (
            "#00200FThank you for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "(Hmm, there's a girl\x01",
            "like this in Support\x01",
            "Section too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F...Do I have something\x01",
            "on my face?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        "N-No, it's nothing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Then, see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FYeah. Be well too,\x01",
            "Shing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CE5")

    label("loc_7AF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B98")

    ChrTalk(
        0x104,
        (
            "#00300FThanks for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, I only did what\x01",
            "had to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Then, see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FYeah. Be well too,\x01",
            "Shing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CE5")

    label("loc_7B98")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C41")

    ChrTalk(
        0x109,
        (
            "#10100FThank you for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, I only did what\x01",
            "had to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Then, see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FYeah. Be well too,\x01",
            "Shing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CE5")

    label("loc_7C41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7CE5")

    ChrTalk(
        0x105,
        (
            "#10300FThank you for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, I only did what\x01",
            "had to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Then, see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FYeah. Be well too,\x01",
            "Shing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CE5")

    Jump("loc_8429")

    label("loc_7CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_8051")
    OP_29(0x79, 0x1, 0xB)

    ChrTalk(
        0x10,
        "Hmm? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F―Wait, aren't you from\x01",
            "Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "―You guys! You're the\x01",
            "Special Support Section!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E2B")

    ChrTalk(
        0x10,
        "And Elie's with you too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHaha. Hello Shing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Y-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "And? What are you doing\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E4D")

    label("loc_7E2B")


    ChrTalk(
        0x10,
        (
            "It's just, why are you\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E4D")


    ChrTalk(
        0x101,
        (
            "#00000FWell, as a job for the\x01",
            "SSS, we're helping the\x01",
            "inspector.\x02\x03",
            "And so, we'd like to\x01",
            "check your hand luggage\x01",
            "and entry permits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I see. So the Support\x01",
            "Section does these kinds\x01",
            "of jobs too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, whatever. If\x01",
            "that's how it is, then\x01",
            "get it over with.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F―Alright. I've checked\x01",
            "your hand luggage and\x01",
            "entry permit.\x02\x03",
            "Thanks for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, I only did what\x01",
            "had to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If you're done, then get\x01",
            "out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FS-Sure... Excuse us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8429")

    label("loc_8051")


    NpcTalk(
        0x10,
        "Boy",
        "Hmm? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0xC)

    ChrTalk(
        0x101,
        (
            "#00000FUmm, we're assistant\x01",
            "inspectors.\x02\x03",
            "Sorry to trouble you, but\x01",
            "may we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yes, I have no problem\x01",
            "with that of course.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Boy",
        (
            "Yeah, just get it over\x01",
            "with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FO-Okay...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81B8")

    ChrTalk(
        0x102,
        (
            "#00105F(I wonder... is this kid\x01",
            "Heiyue too? He's rather\x01",
            "arrogant...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8337")

    label("loc_81B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8215")

    ChrTalk(
        0x103,
        (
            "#00205F(Could this kid be\x01",
            "Heiyue too? He seems\x01",
            "rather arrogant...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8337")

    label("loc_8215")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8269")

    ChrTalk(
        0x104,
        (
            "#00303F(Is this kiddo Heiyue\x01",
            "too? He's kinda\x01",
            "arrogant...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8337")

    label("loc_8269")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82BF")

    ChrTalk(
        0x109,
        (
            "#10105F(Is this kid Heiyue too?\x01",
            "He seems quite\x01",
            "arrogant...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8337")

    label("loc_82BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8337")

    ChrTalk(
        0x105,
        (
            "#10304F(Is this kid related to the\x01",
            "Heiyue too, I wonder? He seems\x01",
            "to be quite arrogant, though...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8337")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F―I've checked your hand luggage\x01",
            "and entry permit. Thank you for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Ah, no, you're welcome.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Boy",
        (
            "Hmph. If you've finished\x01",
            "your business, then get\x01",
            "out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()

    label("loc_8429")

    OP_5A()
    SetScenarioFlags(0x1CA, 6)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    ClearChrFlags(0xF, 0x10)
    SetChrSubChip(0xF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_29_7484 end

    def Function_30_8444(): pass

    label("Function_30_8444")

    EventBegin(0x0)
    Fade(500)
    OP_68(1640, 1000, 2570, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 520, 0, 2930, 90)
    SetChrPos(0x1, 520, 0, 2090, 90)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_852C")
    Jump("loc_8576")

    label("loc_852C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_854C")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8576")

    label("loc_854C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_856C")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8576")

    label("loc_856C")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8576")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_862C")
    Jump("loc_8676")

    label("loc_862C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_864C")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8676")

    label("loc_864C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_866C")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8676")

    label("loc_866C")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8676")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're\x01",
            "assistant inspectors.\x02\x03",
            "Sorry to trouble you, but\x01",
            "may we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Ugh, do I have to?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)
    SetChrSubChip(0xE, 0x0)

    ChrTalk(
        0xE,
        (
            "H-Hey! What are you\x01",
            "saying to the\x01",
            "inspector!?\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8813")
    Jump("loc_885D")

    label("loc_8813")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8833")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_885D")

    label("loc_8833")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8853")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_885D")

    label("loc_8853")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_885D")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xE,
        (
            "Sorry, my little sister\x01",
            "was terribly rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "She's a real moron, so\x01",
            "please forgive her.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xD,
        (
            "What are you doing\x01",
            "calling me a moron!? The\x01",
            "real moron is―\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Umm, we can start,\x01",
            "right?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89D1")

    ChrTalk(
        0x102,
        "#00100F(Yes, I think so.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A97")

    label("loc_89D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A05")

    ChrTalk(
        0x103,
        "#00200F(I think you can.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A97")

    label("loc_8A05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A37")

    ChrTalk(
        0x104,
        "#00300F(Yeah, I guess.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A97")

    label("loc_8A37")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A6A")

    ChrTalk(
        0x109,
        "#10100F(Yes, I think...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A97")

    label("loc_8A6A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A97")

    ChrTalk(
        0x105,
        "#10300F(Hehe, I guess.)\x02",
    )

    CloseMessageWindow()

    label("loc_8A97")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B33")
    Jump("loc_8B7D")

    label("loc_8B33")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8B53")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B7D")

    label("loc_8B53")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B73")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B7D")

    label("loc_8B73")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B7D")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F―I've checked your hand luggage\x01",
            "and entry permit. Thank you for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No, no, I should be\x01",
            "thanking you. I'm sorry my\x01",
            "little sister troubled you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xD,
        (
            "What are you doing saying\x01",
            "something like that!? The real\x01",
            "one who troubled them is―\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003F(We should leave. And\x01",
            "quickly.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CA, 5)
    OP_29(0x79, 0x1, 0xD)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_8444 end

    def Function_31_8D54(): pass

    label("Function_31_8D54")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(270, 1000, -8380, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -570, 0, -8020, 90)
    SetChrPos(0x1, 990, 0, -8210, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x8, 770, 0, -16190, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FAlright, I guess that's\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E74")

    ChrTalk(
        0x102,
        (
            "#00105FCome to think of it, we\x01",
            "haven't checked the old man's\x01",
            "ticket in car No. 4 yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_903C")

    label("loc_8E74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EE9")

    ChrTalk(
        0x103,
        (
            "#00205FCome to think of it, we\x01",
            "haven't checked the old man's\x01",
            "ticket in car No. 4, have we.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_903C")

    label("loc_8EE9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F57")

    ChrTalk(
        0x104,
        (
            "#00305FI guess we haven't checked\x01",
            "the ol' man's ticket in\x01",
            "the 4th vehicle yet, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_903C")

    label("loc_8F57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FCC")

    ChrTalk(
        0x109,
        (
            "#10105FCome to think of it, we\x01",
            "haven't checked the old man's\x01",
            "ticket in car No. 4, have we.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_903C")

    label("loc_8FCC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_903C")

    ChrTalk(
        0x105,
        (
            "#10305FCome to think of it, we\x01",
            "haven't checked the old man's\x01",
            "ticket in car No. 4, have we.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_903C")


    ChrTalk(
        0x101,
        (
            "#00003FThat's right. Then,\x01",
            "let's head back and―\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "―G-Give me back my\x01",
            "ticket!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9102")

    ChrTalk(
        0x102,
        "#00101F―Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_91A5")

    label("loc_9102")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_912C")

    ChrTalk(
        0x103,
        "#00201F―Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_91A5")

    label("loc_912C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9156")

    ChrTalk(
        0x104,
        "#00301F―Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_91A5")

    label("loc_9156")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9180")

    ChrTalk(
        0x109,
        "#10101F―Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_91A5")

    label("loc_9180")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91A5")

    ChrTalk(
        0x105,
        "#10301F―Lloyd!\x02",
    )

    CloseMessageWindow()

    label("loc_91A5")


    ChrTalk(
        0x101,
        "#00000FYeah, let's go!\x02",
    )

    CloseMessageWindow()
    Call(0, 32)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_91D8")
    Call(0, 34)
    Jump("loc_91DB")

    label("loc_91D8")

    Call(0, 33)

    label("loc_91DB")

    EventEnd(0x5)
    Return()

    # Function_31_8D54 end

    def Function_32_91DE(): pass

    label("Function_32_91DE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearScenarioFlags(0x156, 7)
    Call(0, 2)
    LoadChrToIndex("chr/ch20800.itc", 0x1E)
    LoadChrToIndex("chr/ch21800.itc", 0x1F)
    LoadChrToIndex("chr/ch21000.itc", 0x20)
    LoadChrToIndex("chr/ch22300.itc", 0x21)
    LoadChrToIndex("chr/ch22800.itc", 0x22)
    LoadChrToIndex("chr/ch47600.itc", 0x23)
    ClearChrFlags(0x8, 0x8)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    ClearChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x20)
    SetChrPos(0x8, -50, 0, 1590, 180)
    SetChrPos(0x9, -550, 0, -250, 0)
    SetChrPos(0xC, 670, 0, -180, 0)
    SetChrPos(0xA, -1670, 0, -2540, 45)
    SetChrPos(0xB, -2540, 0, -2720, 90)
    SetChrPos(0x101, 460, 0, 7860, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9310")
    SetChrPos(0x102, -480, 0, 8210, 180)
    Jump("loc_93A3")

    label("loc_9310")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9336")
    SetChrPos(0x103, -480, 0, 8210, 180)
    Jump("loc_93A3")

    label("loc_9336")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_935C")
    SetChrPos(0x104, -480, 0, 8210, 180)
    Jump("loc_93A3")

    label("loc_935C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9382")
    SetChrPos(0x109, -480, 0, 8210, 180)
    Jump("loc_93A3")

    label("loc_9382")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93A3")
    SetChrPos(0x105, -480, 0, 8210, 180)

    label("loc_93A3")

    OP_68(120, 1000, 220, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "I'm telling you! It must\x01",
            "have been one of those\x01",
            "two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now who was it!? Confess\x01",
            "already!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    def lambda_9444():
        OP_95(0x101, 460, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9444)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9488")

    def lambda_946E():
        OP_95(0x102, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_946E)
    Jump("loc_953F")

    label("loc_9488")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94B7")

    def lambda_949D():
        OP_95(0x103, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_949D)
    Jump("loc_953F")

    label("loc_94B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94E6")

    def lambda_94CC():
        OP_95(0x104, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_94CC)
    Jump("loc_953F")

    label("loc_94E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9515")

    def lambda_94FB():
        OP_95(0x109, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_94FB)
    Jump("loc_953F")

    label("loc_9515")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_953F")

    def lambda_952A():
        OP_95(0x105, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_952A)

    label("loc_953F")

    OP_68(70, 1000, 2830, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16500, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00005FExcuse us. Did something\x01",
            "happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, you're those\x01",
            "inspectors from before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is just awful. I've\x01",
            "been falsely accused by\x01",
            "this old―\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "What!? Have you no\x01",
            "shame?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FEveryone, please! Calm\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96BF")

    ChrTalk(
        0x102,
        (
            "#00101FUmm, can you first tell\x01",
            "us what the problem is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97F3")

    label("loc_96BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9712")

    ChrTalk(
        0x103,
        (
            "#00200FUmm, could you first\x01",
            "tell us what the problem\x01",
            "is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97F3")

    label("loc_9712")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9760")

    ChrTalk(
        0x104,
        (
            "#00303FFor starters, could you\x01",
            "tell us the problem?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97F3")

    label("loc_9760")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97B0")

    ChrTalk(
        0x109,
        (
            "#10101FAnyhow, could you tell\x01",
            "us what the problem is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97F3")

    label("loc_97B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97F3")

    ChrTalk(
        0x105,
        (
            "#10304FAnyway, could you tell\x01",
            "us the problem?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97F3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 550, 0, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9835")
    SetChrPos(0x102, -540, 0, 1100, 180)
    Jump("loc_98C8")

    label("loc_9835")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_985B")
    SetChrPos(0x103, -540, 0, 1100, 180)
    Jump("loc_98C8")

    label("loc_985B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9881")
    SetChrPos(0x104, -540, 0, 1100, 180)
    Jump("loc_98C8")

    label("loc_9881")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98A7")
    SetChrPos(0x109, -540, 0, 1100, 180)
    Jump("loc_98C8")

    label("loc_98A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98C8")
    SetChrPos(0x105, -540, 0, 1100, 180)

    label("loc_98C8")

    SetChrPos(0x8, -1580, 0, -60, 90)
    SetChrPos(0x9, -550, 0, -1300, 0)
    SetChrPos(0xC, 540, 0, -1300, 0)
    OP_68(-1060, 1000, 820, 0)
    MoveCamera(307, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18110, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FI see. The ticket this\x01",
            "gentleman purchased is to Ored\x01",
            "State in the No. 4 car...\x02\x03",
            "And there are two people in\x01",
            "this car with that exact same\x01",
            "ticket.\x02\x03",
            "#00001FTherefore, it's possible one\x01",
            "of them stole your ticket. Is\x01",
            "that what you're saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yeah, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "―Anyway, the fact that I had the\x01",
            "ticket when I entered the platform\x01",
            "is the unmistakable truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Given that, there's no way\x01",
            "that I could have lost it in\x01",
            "this short amount of time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That is, unless I was\x01",
            "robbed.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FUmm, as you might expect,\x01",
            "we can't decide anything\x01",
            "based on just that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Good, good! Just let him\x01",
            "say whatever he wants!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, he's just\x01",
            "senile!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "Damn you! That again!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FCalm down, both of you.\x02\x03",
            "#00001FAnyhow, nothing will be settled\x01",
            "if you just keep throwing your\x01",
            "emotions at each other.\x02\x03",
            "#00003FAnd so, allow me to ask the two\x01",
            "of you with a ticket a simple\x01",
            "question.\x02\x03",
            "#00001FThe reason you both are\x01",
            "traveling to Ored― Could you\x01",
            "tell us that, at the very least?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "The reason for going to\x01",
            "Ored?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmph. Will that really\x01",
            "be proof of innocence or\x01",
            "guilt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. If one of you is really\x01",
            "a thief, it's possible they\x01",
            "had no destination in mind.\x02\x03",
            "#00004FIn that case, the thief\x01",
            "could reveal some kind of\x01",
            "fault.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EBD")

    ChrTalk(
        0x102,
        (
            "#00105FI see. Indeed, that's\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FBA")

    label("loc_9EBD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EFE")

    ChrTalk(
        0x103,
        (
            "#00203FI see. Indeed, that's\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FBA")

    label("loc_9EFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F3E")

    ChrTalk(
        0x104,
        (
            "#00305FI see. That's indeed\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FBA")

    label("loc_9F3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F7F")

    ChrTalk(
        0x109,
        (
            "#10105FI see. Indeed, that's\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FBA")

    label("loc_9F7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FBA")

    ChrTalk(
        0x105,
        (
            "#10302FI see. That's indeed\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FBA")


    ChrTalk(
        0x8,
        (
            "Hmph, well hurry it up\x01",
            "then. Answer him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmph, that's an easy\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm a trader. I have\x01",
            "important negotiations to\x01",
            "conduct in Ored State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Incidentally, this is my\x01",
            "contract. My client is the\x01",
            "Ryｹshin Company in Ored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Stealing a ticket from such a\x01",
            "man... I've no reason to do\x01",
            "such a petty thing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "G-Grrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...I see.\x02\x03",
            "#00001FAnd what about you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "U-Umm, Ored is my\x01",
            "hometown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Isn't going back home a\x01",
            "reason for traveling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, that's fine...\x02\x03",
            "#00008F(Hmm. For now, I can\x01",
            "decide anything based on\x01",
            "what I heard, huh.)\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_32_91DE end

    def Function_33_A201(): pass

    label("Function_33_A201")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A24C")

    ChrTalk(
        0x102,
        (
            "#00103F(...It looks like this\x01",
            "is all we can do.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A367")

    label("loc_A24C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A294")

    ChrTalk(
        0x103,
        (
            "#00203F(...It appears this is\x01",
            "all we can do.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A367")

    label("loc_A294")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2D7")

    ChrTalk(
        0x104,
        (
            "#00303F(...Seems this is all we\x01",
            "can do.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A367")

    label("loc_A2D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A324")

    ChrTalk(
        0x109,
        (
            "#10103F(...It looks like this\x01",
            "is all we can do...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A367")

    label("loc_A324")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A367")

    ChrTalk(
        0x105,
        (
            "#10303F(...Looks like this is\x01",
            "all we can do.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A367")


    ChrTalk(
        0x101,
        (
            "#00003F(Right... Looks like all we\x01",
            "can do is report this to\x01",
            "Marlowe, the expert here.)\x02\x03",
            "#00000FExcuse us everyone. Please\x01",
            "wait here for a little\x01",
            "while.\x02\x03",
            "I'm going to call my\x01",
            "superior.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_A201 end

    def Function_34_A44B(): pass

    label("Function_34_A44B")

    Sleep(1000)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_4B(0x10, 0x0)
    SetChrPos(0x10, 460, 0, 9210, 180)
    SetChrPos(0xF, -480, 0, 9860, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "Haha, how fun. There's a\x01",
            "liar in this car!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A505():
        OP_93(0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A505)

    def lambda_A512():
        OP_93(0x1, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A512)
    OP_68(460, 1000, 5040, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16210, 3000)

    def lambda_A54D():
        OP_95(0x10, 460, 0, 5470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A54D)

    def lambda_A567():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_A567)

    def lambda_A578():
        OP_95(0xF, -480, 0, 5970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A578)

    def lambda_A592():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A592)
    Sleep(2000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x1, 0x8)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A6EB")

    ChrTalk(
        0x101,
        (
            "#00005F―Shing?\x02\x03",
            "#00001FH-Hey. It's a rule. You\x01",
            "can't change cars during\x01",
            "the inspection―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, you've already\x01",
            "finished the inspection,\x01",
            "right? Be flexible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, but... *sigh*,\x01",
            "whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "At any rate, it looks\x01",
            "like something fun is\x01",
            "going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I'll participate too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A74F")

    label("loc_A6EB")


    ChrTalk(
        0x101,
        "#00005F―Shing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Haha. It looks like\x01",
            "something fun is going\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I'll participate too!\x02",
    )

    CloseMessageWindow()

    label("loc_A74F")


    ChrTalk(
        0x101,
        "#00005FP-Participate...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    OP_68(-470, 1000, 1440, 0)
    MoveCamera(307, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17200, 0)
    SetChrPos(0x101, -550, 0, 1100, 90)
    SetChrPos(0x10, 540, 0, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A7EA")
    SetChrPos(0x102, -540, 0, 2100, 135)
    Jump("loc_A87D")

    label("loc_A7EA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A810")
    SetChrPos(0x103, -540, 0, 2100, 135)
    Jump("loc_A87D")

    label("loc_A810")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A836")
    SetChrPos(0x104, -540, 0, 2100, 135)
    Jump("loc_A87D")

    label("loc_A836")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A85C")
    SetChrPos(0x109, -540, 0, 2100, 135)
    Jump("loc_A87D")

    label("loc_A85C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A87D")
    SetChrPos(0x105, -540, 0, 2100, 135)

    label("loc_A87D")

    SetChrPos(0xF, 540, 0, 2500, 180)
    OP_93(0x8, 0x5A, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00001F...And, what are you\x01",
            "going to do about this\x01",
            "liar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Yeah, then first of all,\x01",
            "let's have that trader\x01",
            "answer.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A916():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A916)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A940")

    def lambda_A933():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A933)
    Jump("loc_A9C3")

    label("loc_A940")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A962")

    def lambda_A955():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A955)
    Jump("loc_A9C3")

    label("loc_A962")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A984")

    def lambda_A977():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A977)
    Jump("loc_A9C3")

    label("loc_A984")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9A6")

    def lambda_A999():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A999)
    Jump("loc_A9C3")

    label("loc_A9A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9C3")

    def lambda_A9BB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A9BB)

    label("loc_A9C3")


    ChrTalk(
        0x10,
        (
            "Earlier, you said you\x01",
            "have business with\x01",
            "Ryｹshin Company, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "What kind of business,\x01",
            "exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*, why do I have to\x01",
            "go along with this\x01",
            "child's game...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, the deal is about\x01",
            "purchasing rare vegetables\x01",
            "and spices from Ored State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ored is known for its\x01",
            "agriculture―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And, Ryｹshin Company is an affiliate\x01",
            "of the Heiyue Group who runs the\x01",
            "Republic's Eastern Quarter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I don't think there's\x01",
            "any room for suspicion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Haha. Like you say,\x01",
            "there is a Ryｹshin\x01",
            "Company in Ored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "But unfortunately... They're\x01",
            "still in the process of\x01",
            "gaining a foothold there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "They're not at a stage\x01",
            "to be taking deals with\x01",
            "outsiders, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "What? How do you know\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "You heard him. ―So what\x01",
            "should I do?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0xF,
        "―Yes, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You... I've remained silent this whole\x01",
            "time and listened, while you were\x01",
            "extremely rude towards the young master!\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7114", 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xF,
        (
            "#5SHmph, remember this... He\x01",
            "is Lord Shing, grandson\x01",
            "of a Heiyue elder!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "An elder's grandchild?\x01",
            "What a joke...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "T-That suit you're\x01",
            "wearing... I'm sure I've\x01",
            "seen it somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "N-No way... It can't be\x01",
            "true...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x10,
        "Hehe, do you get it now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "By the way, what's your\x01",
            "real motive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "W-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, whatever. You'll go to\x01",
            "another room later and tell\x01",
            "the inspector everything.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF70")

    ChrTalk(
        0x102,
        "#00103F(...He's good.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_B054")

    label("loc_AF70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFAB")

    ChrTalk(
        0x103,
        (
            "#00203F(...This kid is\x01",
            "amazing.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B054")

    label("loc_AFAB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFED")

    ChrTalk(
        0x104,
        (
            "#00303F(...That Shing knows his\x01",
            "stuff.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B054")

    label("loc_AFED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B024")

    ChrTalk(
        0x109,
        "#10105F(...Shing's amazing.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_B054")

    label("loc_B024")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B054")

    ChrTalk(
        0x105,
        "#10304F(Hehe, impressive.)\x02",
    )

    CloseMessageWindow()

    label("loc_B054")


    ChrTalk(
        0x101,
        (
            "#00003F(Yeah, how should I put\x01",
            "it... He's got quite the\x01",
            "presence.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "―Alright. You're next.\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FShing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "M-Me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The culprit is that man\x01",
            "who was lying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, I don't remember\x01",
            "anyone saying that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I've a little something\x01",
            "to ask you, too. You're\x01",
            "from Ored, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Y-Yes... I'm returning\x01",
            "home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, then you'll know\x01",
            "this for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Aside from agriculture,\x01",
            "Ored State is famous for\x01",
            "being secluded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It also has many hot\x01",
            "springs... Among these,\x01",
            "which is in Ored?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "①Elmo Hot Springs\x01",
            "②Parm Hot Springs\x01",
            "③Ored Hot Springs\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "―Now, answer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "U-Uhhm... Isn't it\x01",
            "obvious that it's ③,\x01",
            "Ored Hot Springs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...I see. Haha...\x01",
            "Bwahaha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FW-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "You made light of me\x01",
            "thinking I'm a child,\x01",
            "eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Ored Hot Springs?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "There's no hot springs\x01",
            "with such a clichｳ name\x01",
            "in the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If you were really from\x01",
            "Ored, you'd answer like\x01",
            "this: "None of those."\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "Huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Haha. Shall I ask you\x01",
            "another question?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Although I think only\x01",
            "worse faults will come\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "So where are you really\x01",
            "from?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "U-Uhhm... well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, I didn't think to\x01",
            "expressly say it, but\x01",
            "actually, I'm Republican.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But I've got a house in\x01",
            "Ored... P-Please believe\x01",
            "me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, I wonder about\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    TurnDirection(0x10, 0x101, 500)

    ChrTalk(
        0x10,
        (
            "...So, Special Support\x01",
            "Section. What do you\x01",
            "make of all this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Based on the interviews,\x01",
            "we know both of them are\x01",
            "liars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "But which of them stole\x01",
            "the ticket?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FY-Yeah, let me think...\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
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
            "#1KBetween the trader and the young man,\x01",
            "who is likely to be the ticket robber?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "The Trader\x01",         # 0
            "The Young Man\x01",      # 1
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
        (0, "loc_B78B"),
        (1, "loc_BA01"),
        (SWITCH_DEFAULT, "loc_BB87"),
    )


    label("loc_B78B")

    OP_2C(0x79, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003FI guess it's the trader.\x02\x03",
            "#00000FThis person seems to\x01",
            "have many secrets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hey, you... Don't\x01",
            "disappoint me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Did you really think\x01",
            "seriously about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FY-Yeah... I'm sorry.\x02\x03",
            "#00008F...I see, here I have to\x01",
            "think by process of\x01",
            "elimination.\x02\x03",
            "#00001FThe fictional contract the\x01",
            "trader showed us...\x02\x03",
            "I don't know his reasons, but\x01",
            "he carefully prepared such a\x01",
            "thing intentionally.\x02\x03",
            "#00003FIt would be unnatural for him\x01",
            "to commit a minor offense\x01",
            "like stealing a ticket.\x02\x03",
            "If Ored isn't his final\x01",
            "destination, it's possible\x01",
            "it's a stopover...\x02\x03",
            "#00001FThen that means... The thief\x01",
            "is you, isn't it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB87")

    label("loc_BA01")

    OP_2C(0x79, 0x2)

    ChrTalk(
        0x101,
        (
            "#00003FI guess it's him.\x02\x03",
            "#00001FThe fictional contract the\x01",
            "trader showed us...\x02\x03",
            "I don't know his reasons, but\x01",
            "he carefully prepared such a\x01",
            "thing intentionally.\x02\x03",
            "#00003FIt would be unnatural for him\x01",
            "to commit a minor offense\x01",
            "like stealing a ticket.\x02\x03",
            "If Ored isn't his final\x01",
            "destination, it's possible\x01",
            "it's a stopover...\x02\x03",
            "#00001FThen that means... The thief\x01",
            "is you, isn't it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB87")

    label("loc_BB87")


    ChrTalk(
        0xC,
        "U-Uuuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hmph, you pass.\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x1F4)

    ChrTalk(
        0x10,
        (
            "Hey, you. Even if you\x01",
            "feign ignorance, you\x01",
            "can't hide it anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If you're a man,\x01",
            "honestly confess here\x01",
            "and now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5SP-Please, let it\x01",
            "slide!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_BCEF():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BCEF)
    Sleep(50)

    def lambda_BCFF():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BCFF)
    Sleep(300)

    ChrTalk(
        0x8,
        "W-What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hey, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "M-My mother was taken to\x01",
            "a Republic hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I have to hurry there no\x01",
            "matter what!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Suddenly I don't get it\x01",
            "anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "In any case, tell us\x01",
            "your circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "R-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually, I'm a student trying to get\x01",
            "into St. Ursula Medical College...\x01",
            "But we're a poor family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My mother worked so hard to send\x01",
            "me to Crossbell... And I study\x01",
            "while doing part-time jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the middle of all that, I\x01",
            "got word my mother suddenly\x01",
            "collapsed... And so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "―You wanted to visit your mother\x01",
            "but didn't have the mira. And so,\x01",
            "you stole the ticket. Is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Y-Yes... It's no lie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "While I'm here like\x01",
            "this, my mother is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmm, although you said\x01",
            "that, but we can't\x01",
            "overlook a theft...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Alright, I'll pay for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_C0BE():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C0BE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0E8")

    def lambda_C0DB():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C0DB)
    Jump("loc_C16B")

    label("loc_C0E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C10A")

    def lambda_C0FD():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C0FD)
    Jump("loc_C16B")

    label("loc_C10A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C12C")

    def lambda_C11F():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C11F)
    Jump("loc_C16B")

    label("loc_C12C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C14E")

    def lambda_C141():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C141)
    Jump("loc_C16B")

    label("loc_C14E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C16B")

    def lambda_C163():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C163)

    label("loc_C16B")


    def lambda_C170():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C170)
    Sleep(50)

    def lambda_C180():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C180)
    Sleep(300)

    ChrTalk(
        0xC,
        "Huh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1BD")

    ChrTalk(
        0x102,
        "#00105FShing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C25D")

    label("loc_C1BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1E8")

    ChrTalk(
        0x103,
        "#00205FThat's...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C25D")

    label("loc_C1E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C212")

    ChrTalk(
        0x104,
        "#00305FH-Hey...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C25D")

    label("loc_C212")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C23A")

    ChrTalk(
        0x109,
        "#10105FUmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C25D")

    label("loc_C23A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C25D")

    ChrTalk(
        0x105,
        "#10305FWow...\x02",
    )

    CloseMessageWindow()

    label("loc_C25D")

    TurnDirection(0x10, 0x8, 500)

    ChrTalk(
        0x10,
        (
            "I'll return your ticket,\x01",
            "old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "And, can you let this\x01",
            "go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "W-Well, if I can get back my\x01",
            "ticket, I have no interest in\x01",
            "aggravating the situation further.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xC, 500)

    ChrTalk(
        0x10,
        "And you―\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Y-Yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Visiting your mom with a\x01",
            "stolen ticket?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "What would she think of\x01",
            "that? Do you think she'd\x01",
            "be happy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "W-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Listen up. I'm paying,\x01",
            "but this isn't a gift...\x01",
            "It's merely a loan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I won't set a term, but\x01",
            "you're going to pay me\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uh, sorry... And thank\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I-I'll pay you back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, make sure you keep\x01",
            "that promise.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 500)

    ChrTalk(
        0x10,
        (
            "That takes care of that.\x01",
            "All that's left is to\x01",
            "call the lead inspector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'll explain the\x01",
            "situation myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FR-Right...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 4)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_A44B end

    def Function_35_C54F(): pass

    label("Function_35_C54F")

    EventBegin(0x1)
    SetScenarioFlags(0x156, 7)
    Call(0, 2)
    SetChrPos(0x0, 100, 0, -8640, 0)
    OP_68(100, 1000, -8640, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    EventEnd(0x4)
    Return()

    # Function_35_C54F end

    def Function_36_C599(): pass

    label("Function_36_C599")

    EventBegin(0x1)
    ClearScenarioFlags(0x156, 7)
    Call(0, 2)
    SetChrPos(0x0, 90, 0, 8340, 180)
    OP_68(90, 1000, 8340, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    EventEnd(0x4)
    Return()

    # Function_36_C599 end

    def Function_37_C5E3(): pass

    label("Function_37_C5E3")

    SetChrPos(0xFE, -400, 0, -4300, 0)

    def lambda_C5F9():
        OP_95(0xFE, -400, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C5F9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_37_C5E3 end

    def Function_38_C61A(): pass

    label("Function_38_C61A")

    SetChrPos(0xFE, -400, 0, -5500, 0)
    Sleep(50)

    def lambda_C633():
        OP_95(0xFE, -400, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C633)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_38_C61A end

    def Function_39_C654(): pass

    label("Function_39_C654")

    SetChrPos(0xFE, 400, 0, -4600, 0)
    Sleep(50)

    def lambda_C66D():
        OP_95(0xFE, 400, 0, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C66D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_39_C654 end

    def Function_40_C68E(): pass

    label("Function_40_C68E")

    SetChrPos(0xFE, 400, 0, -5600, 0)
    Sleep(100)

    def lambda_C6A7():
        OP_95(0xFE, 400, 0, 2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C6A7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_40_C68E end

    def Function_41_C6C8(): pass

    label("Function_41_C6C8")

    SetChrPos(0xFE, 400, 0, -6600, 0)
    Sleep(50)

    def lambda_C6E1():
        OP_95(0xFE, 500, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C6E1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_41_C6C8 end

    def Function_42_C702(): pass

    label("Function_42_C702")

    SetChrPos(0xFE, 400, 0, -7700, 0)
    Sleep(100)

    def lambda_C71B():
        OP_95(0xFE, 400, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C71B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_42_C702 end

    def Function_43_C73C(): pass

    label("Function_43_C73C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch07302.itc", 0x1E)
    LoadChrToIndex("chr/ch12402.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis236.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis237.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03400.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11500.itp")
    OP_68(-2000, 1000, 2550, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 1400, 0, -7500, 315)
    SetChrPos(0x102, 1400, 0, -8500, 315)
    SetChrPos(0x103, 2300, 0, -8500, 315)
    SetChrPos(0x104, 2300, 0, -7500, 315)
    SetChrPos(0xF4, 3200, 0, -8500, 315)
    SetChrPos(0xF5, 3200, 0, -7500, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x27, 0x1E)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -2100, 150, 1800, 0)
    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, -2100, 150, 3300, 180)
    PlayBGM("ed7302", 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetChrSubChip(0x27, 0x2)
    Sleep(300)

    ChrTalk(
        0x27,
        "#5P#03402F─You've arrived.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x28, 0x1)

    ChrTalk(
        0x28,
        "#11P#11509FHi, it's been a while.\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 1000, -6000, 2000)
    MoveCamera(323, 21, 0, 2000)
    SetCameraDistance(18000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00006F...Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FI see, you contacted the\x01",
            "Support Section car from the\x01",
            "train's communicator, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "#03404F#6PVery perceptive.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1470, 1000, 2540, 0)
    MoveCamera(306, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16650, 0)
    SetCameraDistance(16149, 3000)
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x104, 3, 0, 39)
    BeginChrThread(0x103, 3, 0, 40)
    BeginChrThread(0xF4, 3, 0, 41)
    BeginChrThread(0xF5, 3, 0, 42)
    WaitChrThread(0xF5, 3)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB8E")

    AnonymousTalk(
        0x27,
        (
            "Looking at you again, you do have a\x01",
            "distinguished lineup.\x02\x03",
            "You're together with the youngest\x01",
            "2nd Lt. of the State Guard and a\x01",
            "Gralsritter Dominion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF00")

    label("loc_CB8E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC45")

    AnonymousTalk(
        0x27,
        (
            "Looking at you again, you do have a\x01",
            "distinguished lineup.\x02\x03",
            "You're together with the youngest\x01",
            "2nd Lt. of the State Guard and a\x01",
            "legendary assassin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF00")

    label("loc_CC45")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD07")

    AnonymousTalk(
        0x27,
        (
            "Looking at you again, you do have\x01",
            "a distinguished lineup.\x02\x03",
            "You're together with the youngest\x01",
            "2nd Lt. of the State Guard and\x01",
            "the Section One Chief Detective.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF00")

    label("loc_CD07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDAD")

    AnonymousTalk(
        0x27,
        (
            "Looking at you again,\x01",
            "you do have a\x01",
            "distinguished lineup.\x02\x03",
            "You're together with a\x01",
            "Gralsritter Dominion and\x01",
            "a legendary assassin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF00")

    label("loc_CDAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE5A")

    AnonymousTalk(
        0x27,
        (
            "Looking at you again, you\x01",
            "do have a distinguished\x01",
            "lineup.\x02\x03",
            "You're together with\x01",
            "Section One chief detective\x01",
            "and a Gralsritter Dominion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF00")

    label("loc_CE5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF00")

    AnonymousTalk(
        0x27,
        (
            "Looking at you again, you\x01",
            "do have a distinguished\x01",
            "lineup.\x02\x03",
            "You're together with\x01",
            "Section One chief detective\x01",
            "and a legendary assassin.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF00")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF93")

    ChrTalk(
        0x109,
        (
            "#6P#10103F...Unfortunately, I'm\x01",
            "currently on loan to the\x01",
            "SSS again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CFDD")

    ChrTalk(
        0x105,
        (
            "#6P#10402FNaturally, you already\x01",
            "know my background.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFDD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D009")

    ChrTalk(
        0x106,
        "#6P#10701F............\x02",
    )

    CloseMessageWindow()

    label("loc_D009")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D062")

    ChrTalk(
        0x10A,
        (
            "#6P#00603FHmph... For the sake of\x01",
            "diplomacy, I'll leave it\x01",
            "at that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D062")


    ChrTalk(
        0x102,
        (
            "#6P#00106FI didn't think you'd be\x01",
            "still in Crossbell.\x02\x03",
            "#00101FHave you been in the\x01",
            "city this whole time?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x28,
        (
            "Yeah, I had a lot of things to look\x01",
            "into...\x02\x03",
            "But now, it seems I can finally go\x01",
            "back to Erebonia.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis238.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis291.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis292.itp")

    ChrTalk(
        0x101,
        "#00011F#12PThings to look into...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_END)), "loc_D5AB")

    ChrTalk(
        0x28,
        (
            "#11504FBy the way, aside from us\x01",
            "there's someone from Liberl\x01",
            "who's making their move...\x02\x03",
            "#11500FAny chance you know them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYeah... It's Reins from\x01",
            "R&A Research.\x02\x03",
            "#00001FCould you be cooperating\x01",
            "with him as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PWe are. We're exchanging\x01",
            "information with each other\x01",
            "regarding this matter.\x02\x03",
            "#03402FEven though they're a private\x01",
            "intelligence agency, they have an\x01",
            "excellent information network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11504FAlthough, since they're shorthanded, they\x01",
            "can't send people everywhere and they're\x01",
            "probably having a lot of trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PThat aside...\x02\x03",
            "#00301FHasn't your boss, the Blood\x01",
            "and Iron Chancellor, been\x01",
            "shot and gone missin'?\x02\x03",
            "Is it alright for you to\x01",
            "laze around in a place like\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D657")

    label("loc_D5AB")


    ChrTalk(
        0x104,
        (
            "#00306F#12PBy the way, hasn't your boss,\x01",
            "the Blood and Iron Chancellor,\x01",
            "been shot and gone missin'?\x02\x03",
            "#00301FIs it alright for you to laze\x01",
            "around in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D657")


    ChrTalk(
        0x28,
        (
            "#11505FAh... You mean old man Osborne.\x02\x03",
            "#11506FEven if I'd hurried back, it's not\x01",
            "like I could've saved him...\x02\x03",
            "#11510FAnd if it's that old man we're talking\x01",
            "about, what happened to him and what\x01",
            "happened in Crossbell were probably\x01",
            "both within his expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00105FHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#12P"Expections"...!? That\x01",
            "he'd be shot!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FRegarding Crossbell you\x01",
            "mean... this incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11501FTo that old man, everything is a Piece\x01",
            "on a game board.\x02\x03",
            "#11503FCrossbell obtaining a Sept-Terrion, to\x01",
            "say nothing of independence, scheming\x01",
            "to rule over the entire continent...\x02\x03",
            "The Imperial Army defeating the Noble\x01",
            "Alliance and occupying the Imperial\x01",
            "capital...\x02\x03",
            "#11508FAnd as a result, that he'd be shot and\x01",
            "mortally wounded, and an inextricable\x01",
            "civil war would start...\x02\x03",
            "To say nothing of holding back a\x01",
            "Republican invasion by creating an\x01",
            "inviolable Barrier called Crossbell.\x02\x03",
            "#11500FEverything probably developed as that\x01",
            "old man envisioned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#12P...Kh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FN-No way...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB1D")

    ChrTalk(
        0x105,
        "#6P#10401F...What a monster.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB9C")

    label("loc_DB1D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB6B")

    ChrTalk(
        0x10A,
        (
            "#6P#00610FTo think he was that\x01",
            "much of a monster...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB9C")

    label("loc_DB6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB9C")

    ChrTalk(
        0x106,
        "#6P#10703FWhat a monster...\x02",
    )

    CloseMessageWindow()

    label("loc_DB9C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DBD2")

    ChrTalk(
        0x109,
        "#6P#10110FU-Unbelievable...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DC7B")

    label("loc_DBD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC2A")

    ChrTalk(
        0x106,
        (
            "#6P#10703F...It's a little hard to\x01",
            "believe all of a\x01",
            "sudden...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC7B")

    label("loc_DC2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC7B")

    ChrTalk(
        0x10A,
        (
            "#6P#00610FAs you might expect, we\x01",
            "can't accept that,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC7B")


    ChrTalk(
        0x27,
        (
            "#03401F#5PWell, Ouroboros seems to be\x01",
            "on the move in the Empire,\x01",
            "but...\x02\x03",
            "The true terror might be\x01",
            "the Blood and Iron\x01",
            "Chancellor himself.\x02\x03",
            "#03403FUsing even himself as a\x01",
            "Piece, giving rise to an\x01",
            "unruly, turbulent period...\x02\x03",
            "#03401FHe is truly a remarkable\x01",
            "character─ No, a monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PI thought he was a\x01",
            "dangerous old man, but to\x01",
            "go to those lengths...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101F... Has President Dieter\x01",
            "noticed that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03405F#5PWell, I wonder.\x02\x03",
            "#03403FI can tell you this... The\x01",
            "performance of the character called\x01",
            "Dieter Crois is superlative.\x02\x03",
            "#03401FHowever, as an actual politician...\x01",
            "I can't help but feel that he's\x01",
            "problematic.\x02\x03",
            "I mean to say that he's able to\x01",
            "operate in politics only as a\x01",
            "manager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PThat's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PWell, he is a banker at his\x01",
            "core.\x02\x03",
            "#03402FEven the Crois Clan's mission\x01",
            "seems to have been left\x01",
            "entirely to his daughter.\x02",
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
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#12P#00205FHow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P...You knew?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11504FWell, we have our sources.\x02\x03",
            "#11508FThe child you sheltered at\x01",
            "that auction...\x02\x03",
            "#11501FWe roughly know the story of\x01",
            "how she became a "core" and\x01",
            "the Sept-Terrion was born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P............\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E21E")

    ChrTalk(
        0x105,
        (
            "#6P#10408FOh man... To think the\x01",
            "worldly powers learned\x01",
            "that much...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E21E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E282")

    ChrTalk(
        0x10A,
        (
            "#6P#00603FAs expected of the\x01",
            "Intelligence Division and\x01",
            "the Rocksmith Agency...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E282")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2A7")

    ChrTalk(
        0x109,
        "#6P#10101FKh...\x02",
    )

    CloseMessageWindow()

    label("loc_E2A7")


    ChrTalk(
        0x27,
        (
            "#03400F#5PI don't want you to\x01",
            "misunderstand, but... He and I\x01",
            "are mere intelligence officers.\x02\x03",
            "We aren't thinking of doing\x01",
            "anything about the Sept-Terrion\x01",
            "ourselves.\x02\x03",
            "#03403FHowever, as for this incident,\x01",
            "which is chance to plunge the\x01",
            "entire continent into chaos...\x02\x03",
            "#03401FWhat we really want to know is\x01",
            "the indentity of the "mastermind"\x01",
            "who pictured all this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FThe... real mastermind!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PLike I just told you, President Dieter's\x01",
            "manager side is simply too strong.\x02\x03",
            "And that Mariabell, though mysterious,\x01",
            "seems more taken with field of orbal\x01",
            "technology than that of politics.\x02\x03",
            "#03400FOn the other hand, the Divine Blade of\x01",
            "Wind... He's excessively self disciplined\x01",
            "and too stoic to be the mastermind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11501FEven old man Osborne and Ouroboros...\x02\x03",
            "They've each capitalized on the situation in\x01",
            "Crossbell to further their own interests, but\x01",
            "they're not acting on their own initiative.\x02\x03",
            "#11503F─There has to be someone.\x02\x03",
            "#11508FPolitics, economy, history, the international\x01",
            "situation...\x02\x03",
            "The Crois clan, the D∴G Cult, even all of\x01",
            "Ouroboros' actions...\x02\x03",
            "#11501FEverything went through them, they influenced\x01",
            "everything, and painted the current picture.\x01",
            "That's who I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PHey now... You can't be\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FThis feels a little like\x01",
            "a conspiracy theory...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FIndeed... I feel like\x01",
            "there's a missing piece\x01",
            "of the puzzle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_E944")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00013F#11P(...No way...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9B1")

    label("loc_E944")


    ChrTalk(
        0x101,
        (
            "#00008F#11P(Who in the world could\x01",
            "be...?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9B1")

    ChrTalk(
        0x10A,
        (
            "#00608F#6P#30W(...It can't be...\x01",
            "No...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9B1")

    Sleep(500)

    ChrTalk(
        0x27,
        (
            "#03404F#5PWell, I thought you might\x01",
            "be able to ascertain\x01",
            "that, but...\x02\x03",
            "It appears that you don't\x01",
            "have evidence either, so\x01",
            "let's leave it at that.\x02\x03",
            "#03402FTime is short, so let us\x01",
            "get down to our other\x01",
            "business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12POther business...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11504FYes, it's simple.\x02\x03",
            "#11507FWe're thinking of giving you\x01",
            "a hand with the "Orchis Tower\x01",
            "Infiltration Operation"!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#00011F#12PWhaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#12PHey now, isn't this too\x01",
            "sudden!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PI understand the outline of the\x01",
            "incident and as such have no need\x01",
            "to remain in Crossbell, but...\x02\x03",
            "Leaving things like this would\x01",
            "leave me with a bit of a guilty\x01",
            "conscience.\x02\x03",
            "#03400FWhat happens to Crossbell going\x01",
            "forward likely depends on all of\x01",
            "you, but...\x02\x03",
            "It will be problematic for us if\x01",
            "this stalemate continues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11504FIt would feel bad throwing\x01",
            "in the towel just before\x01",
            "clearing "Pom!", right?\x02\x03",
            "#11502FWell, this is the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00109FThe same, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211F...By the way, when did\x01",
            "you get a "Pom!"\x01",
            "account?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EEC2")

    ChrTalk(
        0x105,
        (
            "#6P#10404FWell, if our combat strength\x01",
            "goes up, the operation's\x01",
            "success rate will increase too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFDC")

    label("loc_EEC2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF52")

    ChrTalk(
        0x10A,
        (
            "#6P#00606FHowever, it's true that if our combat\x01",
            "strength goes up, the operation\x01",
            "success rate will increase as well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFDC")

    label("loc_EF52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EFDC")

    ChrTalk(
        0x106,
        (
            "#6P#10703FHowever, it's true that if our combat\x01",
            "strength goes up, the operation\x01",
            "success rate might increase as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFDC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F03E")

    ChrTalk(
        0x109,
        (
            "#6P#10108FIt's a little\x01",
            "complicated, but... I\x01",
            "think we can consider it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0DA")

    label("loc_F03E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F08A")

    ChrTalk(
        0x106,
        (
            "#6P#10708FMaybe we should consult\x01",
            "with the chief.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0DA")

    label("loc_F08A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F0DA")

    ChrTalk(
        0x10A,
        (
            "#6P#00601FWe'll consult with Chief\x01",
            "Sergei and consider it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0DA")


    ChrTalk(
        0x101,
        (
            "#00006F#12P...Understood.\x02\x03",
            "#00000FWe'll guide you to our\x01",
            "base, so please, follow\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16650, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and friends\x01",
            "introduced Kilika and Lechter\x01",
            "to Chief Sergei...\x02\x03",
            "After exchanging intel with\x01",
            "each other, it was decided they\x01",
            "would help with the operation.\x02\x03",
            "Then, the Orchis Tower hacking\x01",
            "conducted by Chief Roberts\x01",
            "finally succeeded and...\x02\x03",
            "They decided to carry out the\x01",
            ""Orchis Tower Infiltration\x01",
            "Operation" immediately.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 2)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_C73C end

    def Function_44_F2C0(): pass

    label("Function_44_F2C0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x15, 0x4)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrPos(0x15, -1900, 150, 3200, 180)
    SetChrSubChip(0x15, 0x1)
    SetChrChipByIndex(0x16, 0x6)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrPos(0x16, -1900, 150, 1700, 0)
    SetChrSubChip(0x16, 0x2)
    SetChrChipByIndex(0x17, 0x0)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrPos(0x17, -2230, 150, -3170, 0)
    SetChrChipByIndex(0x18, 0xA)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrPos(0x18, 2240, 150, -1750, 180)
    SetChrChipByIndex(0x19, 0x1)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrPos(0x19, 2200, 150, 5740, 180)
    LoadChrToIndex("chr/ch24100.itc", 0x1E)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x2)
    OP_68(-110, 1000, 2300, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, -420, 0, -6700, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F40E")
    SetChrPos(0x102, 280, 0, -7500, 0)
    Jump("loc_F4A1")

    label("loc_F40E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F434")
    SetChrPos(0x103, 280, 0, -7500, 0)
    Jump("loc_F4A1")

    label("loc_F434")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F45A")
    SetChrPos(0x104, 280, 0, -7500, 0)
    Jump("loc_F4A1")

    label("loc_F45A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F480")
    SetChrPos(0x109, 280, 0, -7500, 0)
    Jump("loc_F4A1")

    label("loc_F480")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F4A1")
    SetChrPos(0x105, 280, 0, -7500, 0)

    label("loc_F4A1")

    SetChrPos(0x1A1, -90, 0, -8180, 0)
    SetChrChipByIndex(0x29, 0x1E)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, -40, 0, -3180, 0)

    def lambda_F4DA():
        OP_95(0x29, -40, 0, 1990, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_F4DA)
    SoundLoad(450)
    Sound(450, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "H-Hey, that old woman...\x01",
            "She came in from the\x01",
            "roof, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Yeah... Who in the world\x01",
            "is she?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x29, 1)
    OP_63(0x29, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x29, 0x10E, 0x1F4)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        (
            "#5SHmph, shut up! This\x01",
            "isn't a show!!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x15)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "EEK!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "S-Scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FThere she is!!\x02",
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-290, 1000, 500, 2000)
    MoveCamera(315, 25, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(17960, 2000)
    OP_93(0x29, 0xB4, 0x1F4)

    def lambda_F688():
        OP_95(0xFE, -420, 0, 150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F688)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F6CC")

    def lambda_F6B2():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F6B2)
    Jump("loc_F783")

    label("loc_F6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F6FB")

    def lambda_F6E1():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F6E1)
    Jump("loc_F783")

    label("loc_F6FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F72A")

    def lambda_F710():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F710)
    Jump("loc_F783")

    label("loc_F72A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F759")

    def lambda_F73F():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F73F)
    Jump("loc_F783")

    label("loc_F759")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F783")

    def lambda_F76E():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F76E)

    label("loc_F783")


    def lambda_F788():
        OP_95(0xFE, -90, 0, -1650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_F788)
    WaitChrThread(0x1A1, 1)

    ChrTalk(
        0x29,
        "What...!!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        "#5SSuch persistence!#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        (
            "#5SYou guys don't know when\x01",
            "to quit!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F8EE")

    ChrTalk(
        0x102,
        (
            "#00106FHonestly, that's my\x01",
            "line, but...\x02\x03",
            "#00101FYou don't have anywhere\x01",
            "to run. Please surrender\x01",
            "peacefully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAE0")

    label("loc_F8EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F964")

    ChrTalk(
        0x103,
        (
            "#00206FRight back at you.\x02\x03",
            "#00200FYou've nowhere to run...\x01",
            "Please, resign yourself\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAE0")

    label("loc_F964")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F9DC")

    ChrTalk(
        0x104,
        (
            "#00306FThat's my line.\x02\x03",
            "#00302FWell, you haven't\x01",
            "anywhere to run. It's\x01",
            "time to pay the piper.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAE0")

    label("loc_F9DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FA63")

    ChrTalk(
        0x109,
        (
            "#10106FI-I feel like we should\x01",
            "be saying that...\x02\x03",
            "#10101FAnyway, escape is\x01",
            "impossible. Surrender\x01",
            "peacefully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAE0")

    label("loc_FA63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FAE0")

    ChrTalk(
        0x105,
        (
            "#10306FOh man, look who's\x01",
            "talking, madame.\x02\x03",
            "#10302FI think going along's in\x01",
            "your best interest,\x01",
            "though?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAE0")


    ChrTalk(
        0x1A1,
        (
            "R-Right, that's right!\x01",
            "Give up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Hah... What do you think\x01",
            "you're saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        "Listen, remember this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "As long as this continent\x01",
            "exists... There's nowhere\x01",
            "I can't escape from!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x29, 0x0, 0x1F4)
    OP_95(0x29, 0, 0, 8290, 4000, 0x0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(200)

    def lambda_FBD7():
        OP_95(0xFE, -10, 0, 10140, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_FBD7)
    Sleep(200)

    def lambda_FBF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_FBF4)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FD-Damn it... She's not\x01",
            "making any sense!\x02\x03",
            "#00007FAnyway, after her,\x01",
            "everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        "Waaaaaaaaait!\x02",
    )

    CloseMessageWindow()

    def lambda_FC75():
        OP_95(0xFE, -420, 0, 10450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FC75)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FCBC")

    def lambda_FCA2():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FCA2)
    Jump("loc_FD73")

    label("loc_FCBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FCEB")

    def lambda_FCD1():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FCD1)
    Jump("loc_FD73")

    label("loc_FCEB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FD1A")

    def lambda_FD00():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FD00)
    Jump("loc_FD73")

    label("loc_FD1A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FD49")

    def lambda_FD2F():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FD2F)
    Jump("loc_FD73")

    label("loc_FD49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FD73")

    def lambda_FD5E():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FD5E)

    label("loc_FD73")

    Sleep(100)

    def lambda_FD7B():
        OP_95(0xFE, -90, 0, 10050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_FD7B)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x2, 0x0, 0x0, 0x1, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    LoadChrToIndex("chr/ch20400.itc", 0x1F)
    LoadChrToIndex("chr/ch20402.itc", 0x20)
    LoadChrToIndex("chr/ch22800.itc", 0x21)
    LoadChrToIndex("chr/ch22802.itc", 0x22)
    LoadChrToIndex("chr/ch24400.itc", 0x23)
    LoadChrToIndex("chr/ch24402.itc", 0x24)
    LoadChrToIndex("chr/ch12500.itc", 0x25)
    LoadChrToIndex("chr/ch12553.itc", 0x26)
    LoadChrToIndex("chr/ch31500.itc", 0x27)
    LoadChrToIndex("chr/ch31553.itc", 0x28)
    OP_68(-1580, 1000, 2240, 0)
    MoveCamera(310, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1A1, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x1A1, 0x80)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1A1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, -230, 0, -4950, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FEA0")
    SetChrPos(0x102, 130, 0, -6140, 0)
    Jump("loc_FF33")

    label("loc_FEA0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FEC6")
    SetChrPos(0x103, 130, 0, -6140, 0)
    Jump("loc_FF33")

    label("loc_FEC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FEEC")
    SetChrPos(0x104, 130, 0, -6140, 0)
    Jump("loc_FF33")

    label("loc_FEEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FF12")
    SetChrPos(0x109, 130, 0, -6140, 0)
    Jump("loc_FF33")

    label("loc_FF12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FF33")
    SetChrPos(0x105, 130, 0, -6140, 0)

    label("loc_FF33")

    SetChrPos(0x1A1, -40, 0, -7350, 0)
    SetChrChipByIndex(0x2A, 0x20)
    SetChrSubChip(0x2A, 0x0)
    EndChrThread(0x2A, 0x0)
    SetChrBattleFlags(0x2A, 0x4)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -2800, 150, 3210, 180)
    SetChrChipByIndex(0x2B, 0x22)
    SetChrSubChip(0x2B, 0x0)
    EndChrThread(0x2B, 0x0)
    SetChrBattleFlags(0x2B, 0x4)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, -1730, 150, 3210, 180)
    SetChrChipByIndex(0x2C, 0x24)
    SetChrSubChip(0x2C, 0x0)
    EndChrThread(0x2C, 0x0)
    SetChrBattleFlags(0x2C, 0x4)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, -2290, 150, 1730, 0)
    SetChrChipByIndex(0x2D, 0x25)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 460, 0, 9210, 180)
    OP_A7(0x2D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2E, 0x27)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, -480, 0, 9860, 180)
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x29, -10, 0, -6170, 0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x2A,
        "Man",
        (
            "The train's departed...\x01",
            "Looks like we can\x01",
            "finally take a breather.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2B,
        "Man",
        (
            "Yeah... With this, it's\x01",
            "goodbye to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2B,
        "Man",
        (
            "I honestly feel bad towards\x01",
            "our comrades who were\x01",
            "caught by Heiyue, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2C,
        "Man",
        (
            "What, it just means our\x01",
            "preparations were\x01",
            "insufficient this time.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2C,
        "Man",
        (
            "One day we'll punish\x01",
            "those guys for sure...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2D,
        "Man's Voice",
        (
            "Ohh... it seems you're\x01",
            "having quite the interesting\x01",
            "conversation, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2C, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(500)

    def lambda_10260():
        OP_95(0xFE, 30, 0, 1880, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_10260)

    def lambda_1027A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_1027A)
    Sleep(600)

    def lambda_1028E():
        OP_95(0xFE, -110, 0, 2990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1028E)

    def lambda_102A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_102A8)
    WaitChrThread(0x2D, 1)
    OP_93(0x2D, 0x10E, 0x12C)
    WaitChrThread(0x2E, 1)
    OP_93(0x2E, 0x10E, 0x1F4)
    SetChrSubChip(0x2A, 0x1)
    SetChrSubChip(0x2B, 0x1)
    SetChrSubChip(0x2C, 0x2)

    NpcTalk(
        0x2A,
        "Man",
        "Ah... Aah... You're...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x2B,
        "Man",
        "Heiyue!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x2C,
        "Man",
        (
            "C-Crap... You followed\x01",
            "us!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "Master Cao would never\x01",
            "let you go, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "Gentlemen of the Anti-\x01",
            "Immigration League...\x01",
            "You're coming with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "We'll transfer to a\x01",
            "Crossbell-bound train when\x01",
            "we reach Altair City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "W-We're finished...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x29,
        "Elderly Woman's Voice",
        "─Move aside, ya brats!\x02",
    )

    CloseMessageWindow()
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x2E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x2A, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x2B, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x2C, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_104CA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_104CA)
    Sleep(50)

    def lambda_104DA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_104DA)

    ChrTalk(
        0x2D,
        "Huh...\x02",
    )

    CloseMessageWindow()

    def lambda_104F3():
        OP_95(0xFE, 10, 0, 2460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_104F3)
    Sleep(1850)
    Sound(811, 0, 100, 0)
    Sound(815, 0, 50, 0)
    Sound(833, 0, 20, 0)
    BeginChrThread(0x2D, 1, 0, 45)
    WaitChrThread(0x29, 1)
    Sound(811, 0, 100, 0)
    Sound(815, 0, 40, 0)
    BeginChrThread(0x2E, 1, 0, 46)
    WaitChrThread(0x2E, 1)

    ChrTalk(
        0x2D,
        "Argh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "Gwoh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Ow ow ow... Damn\x01",
            "blockheads, didn't I\x01",
            "tell you to move!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "This is no time to be\x01",
            "standing still!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2C, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2A)
    OP_64(0x2B)
    OP_64(0x2C)

    ChrTalk(
        0x2C,
        "(U-Umm...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "(What's with this lady?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x29, 0x10E, 0x1F4)

    ChrTalk(
        0x29,
        "...Hmmm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Could it be that you\x01",
            "guys are... being chased\x01",
            "by these guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "Y-Yeah... Honestly,\x01",
            "we're saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        "You're our savior!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Hmph, I don't get it,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "...To oppose those guys,\x01",
            "I need as many allies as\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        (
            "#5SGuys! If you feel like you're\x01",
            "in my debt, even just a\x01",
            "little, then come with me!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        (
            "#5SIf it goes well, you\x01",
            "might be able to get\x01",
            "away too!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "H-HUUUH...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "Really...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        "Come on, don't dawdle!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Republican Terrorists")

    AnonymousTalk(
        0xFF,
        "R-Right!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0x29, 0x0, 0x1F4)
    BeginChrThread(0x29, 1, 0, 47)
    Sleep(200)
    BeginChrThread(0x2B, 1, 0, 49)
    Sleep(600)
    BeginChrThread(0x2C, 1, 0, 50)
    Sleep(600)
    BeginChrThread(0x2A, 1, 0, 48)
    Sleep(3000)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x1A1, 0x80)
    BeginChrThread(0x101, 1, 0, 47)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_108D2")
    BeginChrThread(0x102, 1, 0, 47)
    Jump("loc_10939")

    label("loc_108D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_108ED")
    BeginChrThread(0x103, 1, 0, 47)
    Jump("loc_10939")

    label("loc_108ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10908")
    BeginChrThread(0x104, 1, 0, 47)
    Jump("loc_10939")

    label("loc_10908")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10923")
    BeginChrThread(0x109, 1, 0, 47)
    Jump("loc_10939")

    label("loc_10923")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10939")
    BeginChrThread(0x105, 1, 0, 47)

    label("loc_10939")

    Sleep(300)
    BeginChrThread(0x1A1, 1, 0, 47)
    Sleep(2000)

    ChrTalk(
        0x1A1,
        "#7AW-Waaait!!\x02",
    )

    WaitChrThread(0x1A1, 1)
    OP_57(0x0)
    OP_5A()
    Sleep(700)

    ChrTalk(
        0x2E,
        "Guh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "W-What the heck\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    OP_71(0x2, 0x0, 0x0, 0x1, 0x8)
    OP_78(0x6, 0x14)
    SetChrPos(0x14, -1000, 0, 7800, 90)
    ClearMapObjFlags(0x6, 0x4)
    OP_78(0x3, 0x13)
    SetChrPos(0x13, 0, 0, 8800, 0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    OP_68(100, 1000, -6850, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1A1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, -20, 0, -7440, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10A71")
    SetChrPos(0x102, -650, 0, -8160, 0)
    Jump("loc_10B04")

    label("loc_10A71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10A97")
    SetChrPos(0x103, -650, 0, -8160, 0)
    Jump("loc_10B04")

    label("loc_10A97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10ABD")
    SetChrPos(0x104, -650, 0, -8160, 0)
    Jump("loc_10B04")

    label("loc_10ABD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10AE3")
    SetChrPos(0x109, -650, 0, -8160, 0)
    Jump("loc_10B04")

    label("loc_10AE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B04")
    SetChrPos(0x105, -650, 0, -8160, 0)

    label("loc_10B04")

    SetChrPos(0x1A1, 550, 0, -8490, 0)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x15, 0x6)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrPos(0x15, 2210, 150, -3270, 0)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrPos(0x16, 2210, 150, -1710, 180)
    SetChrChipByIndex(0x17, 0x0)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrPos(0x17, -2240, 0, -750, 0)
    SetChrChipByIndex(0x18, 0xA)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrPos(0x18, -2240, 0, 3210, 180)
    SetChrChipByIndex(0x19, 0x9)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrPos(0x19, 2340, 0, 5690, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_68(-1640, 1000, 8480, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(20000, 3000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(20, 1000, -6050, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16210, 0)
    OP_0D()

    ChrTalk(
        0x1A1,
        "*pant, pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "L-Looks like she's\x01",
            "climbed on the roof\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FBy the way, it looked\x01",
            "like someone was\x01",
            "following her...\x02\x03",
            "#00001FDid she have hidden\x01",
            "allies!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "T-That's impossible... All of her\x01",
            "underlings should've been\x01",
            "arrested a long time ago, right!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10DC0")

    ChrTalk(
        0x102,
        (
            "#00101FA-At any rate... Let's\x01",
            "chase after them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F06")

    label("loc_10DC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E03")

    ChrTalk(
        0x103,
        (
            "#00201FAnyway... Let's chase\x01",
            "after them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F06")

    label("loc_10E03")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E57")

    ChrTalk(
        0x104,
        (
            "#00301FTch, I don't really get\x01",
            "it, but... After 'em,\x01",
            "now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F06")

    label("loc_10E57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10EB0")

    ChrTalk(
        0x109,
        (
            "#10101FI-I don't really get it,\x01",
            "but... Let's chase after\x01",
            "them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F06")

    label("loc_10EB0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10F06")

    ChrTalk(
        0x105,
        (
            "#10302FWe can't just let them\x01",
            "go, right? Let's chase\x01",
            "after them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F06")


    ChrTalk(
        0x101,
        (
            "#00003FY-You're right.\x02\x03",
            "#00001F─Alright, resume the\x01",
            "pursuit!\x02",
        )
    )

    CloseMessageWindow()
    StopSound(451, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_F2C0 end

    def Function_45_10F67(): pass

    label("Function_45_10F67")

    OP_93(0xFE, 0x10E, 0x0)
    OP_82(0xC8, 0x12C, 0xBB8, 0x190)
    Fade(500)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0x4BA, 0x0, 0x99C, 0x1388, 0x0)
    OP_A6(0xFE, 0x1E, 0xA, 0x190, 0x1F4)
    SetChrSubChip(0xFE, 0x1)
    Sound(514, 0, 60, 0)
    Return()

    # Function_45_10F67 end

    def Function_46_10FC3(): pass

    label("Function_46_10FC3")

    OP_93(0xFE, 0xB4, 0x0)
    OP_82(0xC8, 0x12C, 0xBB8, 0x190)
    Fade(500)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFFC22, 0x0, 0x13CE, 0x1388, 0x0)
    OP_A6(0xFE, 0x1E, 0xA, 0x190, 0x1F4)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_46_10FC3 end

    def Function_47_11019(): pass

    label("Function_47_11019")

    OP_95(0xFE, 0, 0, 8350, 4000, 0x0)

    def lambda_11032():
        OP_95(0xFE, 0, 0, 10000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11032)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_47_11019 end

    def Function_48_11053(): pass

    label("Function_48_11053")

    Fade(500)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -2790, 0, 2570, 180)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, -230, 0, 2530, 4000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    BeginChrThread(0xFE, 2, 0, 47)
    Return()

    # Function_48_11053 end

    def Function_49_110AA(): pass

    label("Function_49_110AA")

    Fade(500)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -1720, 0, 2580, 180)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, -230, 0, 2530, 4000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    BeginChrThread(0xFE, 2, 0, 47)
    Return()

    # Function_49_110AA end

    def Function_50_11101(): pass

    label("Function_50_11101")

    Fade(500)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -2280, 0, 2400, 0)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, -230, 0, 2530, 4000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    BeginChrThread(0xFE, 2, 0, 47)
    Return()

    # Function_50_11101 end

    SaveToFile()

Try(main)
