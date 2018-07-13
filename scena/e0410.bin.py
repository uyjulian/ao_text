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
        "Function_5_DB6",          # 05, 5
        "Function_6_E8D",          # 06, 6
        "Function_7_EFA",          # 07, 7
        "Function_8_F7A",          # 08, 8
        "Function_9_FE2",          # 09, 9
        "Function_10_1043",        # 0A, 10
        "Function_11_1166",        # 0B, 11
        "Function_12_1273",        # 0C, 12
        "Function_13_1313",        # 0D, 13
        "Function_14_1386",        # 0E, 14
        "Function_15_2443",        # 0F, 15
        "Function_16_247C",        # 10, 16
        "Function_17_4BC7",        # 11, 17
        "Function_18_536A",        # 12, 18
        "Function_19_56B1",        # 13, 19
        "Function_20_5799",        # 14, 20
        "Function_21_5805",        # 15, 21
        "Function_22_5871",        # 16, 22
        "Function_23_5D36",        # 17, 23
        "Function_24_62A6",        # 18, 24
        "Function_25_67DD",        # 19, 25
        "Function_26_6EF3",        # 1A, 26
        "Function_27_6EFC",        # 1B, 27
        "Function_28_7434",        # 1C, 28
        "Function_29_7833",        # 1D, 29
        "Function_30_8897",        # 1E, 30
        "Function_31_91C0",        # 1F, 31
        "Function_32_96B9",        # 20, 32
        "Function_33_A81C",        # 21, 33
        "Function_34_AA6C",        # 22, 34
        "Function_35_CC6C",        # 23, 35
        "Function_36_CCB6",        # 24, 36
        "Function_37_CD00",        # 25, 37
        "Function_38_CD37",        # 26, 38
        "Function_39_CD71",        # 27, 39
        "Function_40_CDAB",        # 28, 40
        "Function_41_CDE5",        # 29, 41
        "Function_42_CE1F",        # 2A, 42
        "Function_43_CE59",        # 2B, 43
        "Function_44_FA5B",        # 2C, 44
        "Function_45_1177E",       # 2D, 45
        "Function_46_117DA",       # 2E, 46
        "Function_47_11830",       # 2F, 47
        "Function_48_1186A",       # 30, 48
        "Function_49_118C1",       # 31, 49
        "Function_50_11918",       # 32, 50
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
            "I-I'm sorry, could you\x01",
            "wait a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I absolutely have the ticket.\x01",
            "I'll find it out for sure!\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_END)), "loc_D97")

    ChrTalk(
        0xFE,
        (
            "If I settle this business negotiation,\x01",
            "I have no doubt I'll have great profits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mwhuhuhu, I can't help to look forward to it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB2")

    label("loc_D97")

    Call(0, 24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB2")
    Call(0, 26)

    label("loc_DB2")

    TalkEnd(0xFE)
    Return()

    # Function_4_CFE end

    def Function_5_DB6(): pass

    label("Function_5_DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_END)), "loc_E71")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Today I'm going to go visit\x01",
            "my parents' home in the\x01",
            "Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My daughter too wanted to see\x01",
            "her grandparents in a while, so\x01",
            "she looks like to be very happy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_E8C")

    label("loc_E71")

    Call(0, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8C")
    Call(0, 26)

    label("loc_E8C")

    Return()

    # Function_5_DB6 end

    def Function_6_E8D(): pass

    label("Function_6_E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_END)), "loc_EDE")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Grandpa, grandma, I'm coming\x01",
            "now, so wait for me, 'k?♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_EF9")

    label("loc_EDE")

    Call(0, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF9")
    Call(0, 26)

    label("loc_EF9")

    Return()

    # Function_6_E8D end

    def Function_7_EFA(): pass

    label("Function_7_EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_END)), "loc_F5E")
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
        "...I wonder if mother is healthy.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_F79")

    label("loc_F5E")

    Call(0, 22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F79")
    Call(0, 26)

    label("loc_F79")

    Return()

    # Function_7_EFA end

    def Function_8_F7A(): pass

    label("Function_8_F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_END)), "loc_FC6")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Geez, I don't care about you\x01",
            "anymore, big brother!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_FE1")

    label("loc_FC6")

    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE1")
    Call(0, 31)

    label("loc_FE1")

    Return()

    # Function_8_F7A end

    def Function_9_FE2(): pass

    label("Function_9_FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_END)), "loc_1027")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*sigh", what a really uncute little sister.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1042")

    label("loc_1027")

    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1042")
    Call(0, 31)

    label("loc_1042")

    Return()

    # Function_9_FE2 end

    def Function_10_1043(): pass

    label("Function_10_1043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_END)), "loc_114A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10EE")

    ChrTalk(
        0xFE,
        (
            "Hu hu, it appears that this trip\x01",
            "has become quite meaningful\x01",
            "for Lord Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This too is thanks to all of you.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1142")

    label("loc_10EE")


    ChrTalk(
        0xFE,
        (
            "Hm, today the weather\x01",
            "is bright and nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hu hu, the ideal train weather.\x02",
    )

    CloseMessageWindow()

    label("loc_1142")

    TalkEnd(0xFE)
    Jump("loc_1165")

    label("loc_114A")

    Call(0, 29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1165")
    Call(0, 31)

    label("loc_1165")

    Return()

    # Function_10_1043 end

    def Function_11_1166(): pass

    label("Function_11_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_END)), "loc_1257")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11E7")

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
        "...Until then, it's farewell.\x02",
    )

    CloseMessageWindow()
    Jump("loc_124F")

    label("loc_11E7")


    NpcTalk(
        0xFE,
        "Boy",
        "What, do you still need something?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Boy",
        (
            "Hmph, I'm busy. Don't talk\x01",
            "to me without a reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124F")

    TalkEnd(0xFE)
    Jump("loc_1272")

    label("loc_1257")

    Call(0, 29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1272")
    Call(0, 31)

    label("loc_1272")

    Return()

    # Function_11_1166 end

    def Function_12_1273(): pass

    label("Function_12_1273")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_END)), "loc_12F4")

    ChrTalk(
        0xFE,
        (
            "*mumble mumble*... I wonder how \x01",
            "many minutes are left till departure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aahn, I don't want to part...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_130F")

    label("loc_12F4")

    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_130F")
    Call(0, 31)

    label("loc_130F")

    TalkEnd(0xFE)
    Return()

    # Function_12_1273 end

    def Function_13_1313(): pass

    label("Function_13_1313")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_END)), "loc_1367")

    ChrTalk(
        0xFE,
        (
            "What is it, your business is over, right?\x01",
            "Then go away, fast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1382")

    label("loc_1367")

    Call(0, 27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1382")
    Call(0, 31)

    label("loc_1382")

    TalkEnd(0xFE)
    Return()

    # Function_13_1313 end

    def Function_14_1386(): pass

    label("Function_14_1386")

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
    SetChrName("Sgt. Noｱl")

    AnonymousTalk(
        0xFF,
        (
            "*sigh*... Still, I'm glad I could\x01",
            "do my duties without problems.\x02\x03",
            "Honestly, I was nervous that\x01",
            "I would've stood in your way.\x02",
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
            "#6P#00002FHa ha, you're prone to worry, eh?\x02\x03",
            "#00004FEven Commander Sonya recommended you,\x01",
            "Master Sergeant, because she thought\x01",
            "you were an acceptable match for us.\x02\x03",
            "#00000FAt any rate, once again, it's a\x01",
            "pleasure to work with you from now on.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x109,
        "Sgt. Noｱl",
        (
            "#10109F#11PYes, likewise!\x02\x03",
            "#10105F...Ah, but, Mr. Lloyd.\x01",
            "Could you please...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHm?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x109,
        "Sgt. Noｱl",
        (
            "#10106F#11PWell, from now on, I'm going to\x01",
            "officially impose on you for some time...\x02\x03",
            "#10102FSince I'm not even wearing the uniform, that\x01",
            ""Master Sergeant" is a little...you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FY-Yeah, that's true.\x02\x03",
            "#00000FWhat do we do then?\x01",
            "Do you mind addressing you informally?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x109,
        "Sgt. Noｱl",
        "#10109F#11PNo, I don't. Please do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FThen, Noｱl──\x01",
            "It's a pleasure to work with you.\x02\x03",
            "#00002FRight, so if you're fine with it too,\x01",
            "let's address each other more directly.\x02\x03",
            "Because we have the same age and are colleagues, \x01",
            "I'd like you to not fuss about that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10111F#11PEEH!?\x01",
            "Addressing Mr. Lloyd directly!?\x02\x03",
            "#10106F............\x01",
            "No, no, that's just impossible!\x02\x03",
            "#10101FAfter all, I'm a newbie as a detective\x01",
            "and I'm learning under you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FNo, I think it's not something\x01",
            "to consider so seriously...\x02\x03",
            "#00000FEven Elie and Randy talk to each other casually\x01",
            "without minding the difference in age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PWell, uhhm...\x01",
            "How to say, it seems it's disposition...\x02\x03",
            "It's like if I set to do it once, I'd\x01",
            "quite never be able to revert back...\x02\x03",
            "#10101FHowever, if Mr. Lloyd says so, somehow\x01",
            "I'll try to make an effort to talk casually──!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FN-No. You don't have\x01",
            "to force yourself.\x02\x03",
            "#00002FHa ha...\x01",
            "You have a virile temperament at heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PAhaha...\x01",
            "Maybe it's my dad's influence.\x02\x03",
            "#10100FBeing him a severe man he disciplined\x01",
            "Fran and I since we were little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FEeh, your father is like that?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FWait, I met your mother\x01",
            "many times, however...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PDad...\x01",
            "He passed away about ten years ago.\x02\x03",
            "#10100FHe was in the Crossbell CGF and...\x01",
            "You know...it happened in an incident while on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F...I see.\x01",
            "I asked you something bad.\x02\x03",
            "#00001FCould it be that...\x01",
            "Your joining the CGF was...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#11PI wonder...?\x01",
            "I don't think I have realized it at all.\x02\x03",
            "#10104FHowever, it can be possible that\x01",
            "I did it because I wanted to protect\x01",
            "the land of Crossbell like my dad.\x02\x03",
            "#10100FIn that sense, Fran could be the same,\x01",
            "although she chose a different post.\x02",
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
        "#6P#00008F............\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F#11PMr. Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FSorry, it's nothing.\x02\x03",
            "#00002F──However, you coming at the\x01",
            "SSS has really helped us.\x02\x03",
            "It's true we're lacking members, but...\x01",
            "...We can't predict what will\x01",
            "happen in the future, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#11PAhaha, it's an honor to\x01",
            "be said something like that...\x02\x03",
            "#10102FBut, with the mafia gone, even the city\x01",
            "public order has improved, right?\x02\x03",
            "The "Heiyue" are still there, but it seems\x01",
            "they aren't doing any conspicuous moves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F...Just on the surface.\x02\x03",
            "#00008FHowever, what I can say is that\x01",
            "the "Revache" organisation was\x01",
            "carrying out a certain role.\x02\x03",
            "#00001FIn a sense, they were keeping\x01",
            "public order in Crossbell.\x02",
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

    # Function_14_1386 end

    def Function_15_2443(): pass

    label("Function_15_2443")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_247B")
    OP_82(0xA, 0xA, 0x5DC, 0x2EE)
    Sleep(3500)
    OP_82(0xA, 0xA, 0x4B0, 0x1F4)
    Sleep(3500)
    Jump("Function_15_2443")

    label("loc_247B")

    Return()

    # Function_15_2443 end

    def Function_16_247C(): pass

    label("Function_16_247C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2578")

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
        (0, "loc_254D"),
        (1, "loc_2555"),
        (2, "loc_255D"),
        (3, "loc_2565"),
        (4, "loc_2573"),
        (SWITCH_DEFAULT, "loc_2573"),
    )


    label("loc_254D")

    SetScenarioFlags(0x25, 3)
    Jump("loc_2578")

    label("loc_2555")

    SetScenarioFlags(0x25, 4)
    Jump("loc_2578")

    label("loc_255D")

    SetScenarioFlags(0x25, 5)
    Jump("loc_2578")

    label("loc_2565")

    SetScenarioFlags(0x25, 3)
    SetScenarioFlags(0x25, 4)
    SetScenarioFlags(0x25, 5)
    Jump("loc_2578")

    label("loc_2573")

    Jump("loc_2578")

    label("loc_2578")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_2645")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis224.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_2688")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis225.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_26CB")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis226.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26CB")

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
            "#10105FThe mafia was keeping public\x01",
            "order in Crossbell...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FAccordingly, though.\x02\x03",
            "#00001F...Try to think about the unique\x01",
            "situation Crossbell is in.\x02\x03",
            "Although it has autonomy, it's not\x01",
            "independent as a state and it's always\x01",
            "hindered by the two major powers.\x02\x03",
            "The law managing crimes is full of holes and\x01",
            "it almost doesn't have immigration regulations...\x02\x03",
            "#00003FProperly speaking, it's a place where the \x01",
            "rampancy of the Heiyue or other criminal\x01",
            "organizations and terrorists is not strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FAh...\x02\x03",
            "...Then, until now, Revache's role\x01",
            "was to keep at bait all that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FI don't want to admit it, but...\x01",
            "I can't deny that it brought a set\x01",
            "order to the underground world.\x02\x03",
            "#00006F...And out of the blue, they got\x01",
            "annihilated by getting involved\x01",
            "in the "Cult" incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108FA power balance collapse, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x01",
            "It could be said the same for the Imperial Faction and\x01",
            "Republican Faction congressmen who lost their standing.\x02\x03",
            "Having lost their spokesmen, there's a\x01",
            "high possibility that pressure from both\x01",
            "countries will become more open than before.\x02\x03",
            "#00013F──That's why I think that the new mayor\x01",
            "is having expectations from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FI see...\x01",
            "I finally understand.\x02\x03",
            "#10100FIs it that the reason why Miss Elie,\x01",
            "senior Randy and Tio temporarily\x01",
            "left the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, in order to be able to do more advanced \x01",
            "activities cooperating as much as possible \x01",
            "with all quarters in lieu of the new situation.\x02\x03",
            "I too got trained at Section One\x01",
            "and learned many things...\x02\x03",
            "#00002FFurthermore, because we lacked help,\x01",
            "we requested for new fighting potential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FUh uh...\x01",
            "It's an honor to have been called here.\x02",
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
        "#12P#10105FBut, now that I think about it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PHm, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FAbout "him"...the other new\x01",
            "member I met before, you know?\x02\x03",
            "Frankly speaking, it was so unexpected\x01",
            "that I'm wondering about the whole story...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#5PAah── "Him", eh?\x02\x03",
            "#00006FWell, just when we had begun\x01",
            "to look for new staff, \x01",
            "he came to visit us...\x02\x03",
            "Because he even had a\x01",
            "recommendation from the new\x01",
            "mayor, we couldn't turn him down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10111FA r-recommendation from the mayor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5PYeah, it appears he received a letter\x01",
            "of recommendations as a thank you for\x01",
            "having helped with the IBC crisis.\x02\x03",
            "#00006F...And to begin with, it seems he had\x01",
            "heard from somewhere that the SSS\x01",
            "was looking for new members.\x02\x03",
            "Though he himself nonchalantly said\x01",
            "that it seemed something fun to do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FUhhm...\x01",
            "Are things going to be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PW-Well...\x01",
            "For sure he's not a bad guy.\x02\x03",
            "#00002FWell, his personal history is unknown,\x01",
            "he knows the underworld very well and\x01",
            "he even works as host or something...\x02\x03",
            "#00006F...Saying it myself, somehow\x01",
            "I've started to become worried.\x02",
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
            "#12P#10112FI-It's all right.\x02\x03",
            "#10102FIt's true that he has a caustic and foul tongue,\x01",
            "but it didn't look like a bad kid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PHa ha...\x01",
            "Hearing that from you I'm relieved.\x02\x03",
            "#00002FBecause, frankly speaking, I thought\x01",
            "that you two wouldn't be able to cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FU-Uhhhm...\x01",
            "It's true that I too ended up\x01",
            "being made fun of by him, but...\x02\x03",
            "#10100FIf I had to say, it seems\x01",
            "that he has more fun by\x01",
            "teasing you, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PUgh...\x01",
            "Although I'd wish he didn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FAhaha...\x01",
            "(I wonder if it's better to not tell him\x01",
            "that Fran kicked a fuss about him...?)\x02",
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
            "──To all the passengers.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We will arrive shortly at the autonomous\x01",
            "state of Crossbell, Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Customers using airliners\x01",
            "going to Liberl and Remiferia,\x01",
            "please make a transfer.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Furthermore, in accordance with the Zemurian\x01",
            "Railroad Public Corporation Rules, this train will\x01",
            "stop for about 30 minutes at Crossbell Station.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Persons headed to the Erebonia region,\x01",
            "above presenting entry written permits,\x01",
            "are asked to be subjected to inspections.\x07\x00\x02",
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
            "#00002F#5PHa ha, since it's just one stop away,\x01",
            "we arrived in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10104FYes...\x02\x03",
            "#10102FAlthough, having being away for some days,\x01",
            "somehow feels kind of nostalgic.\x02",
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
            "#00004F#5P(...Just a little bit more and\x01",
            "we will be all together...)\x02\x03",
            "#00002F(KeA...\x01",
            "I hope she didn't feel lonely.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BCF")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3B1B")
    MenuCmd(1, 0, "[Elie]")

    label("loc_3B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_3B2D")
    MenuCmd(1, 0, "[Tio]")

    label("loc_3B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_3B41")
    MenuCmd(1, 0, "[Randy]")

    label("loc_3B41")

    MenuCmd(2, 0, -1, 100, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B7F"),
        (1, "loc_3B98"),
        (2, "loc_3BC2"),
        (SWITCH_DEFAULT, "loc_3BCA"),
    )


    label("loc_3B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3B90")
    SetScenarioFlags(0x121, 2)
    Jump("loc_3B93")

    label("loc_3B90")

    SetScenarioFlags(0x121, 3)

    label("loc_3B93")

    Jump("loc_3BCA")

    label("loc_3B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_3BB2")
    SetScenarioFlags(0x121, 3)
    Jump("loc_3BB5")

    label("loc_3BB2")

    SetScenarioFlags(0x121, 4)

    label("loc_3BB5")

    Jump("loc_3BBD")

    label("loc_3BBA")

    SetScenarioFlags(0x121, 4)

    label("loc_3BBD")

    Jump("loc_3BCA")

    label("loc_3BC2")

    SetScenarioFlags(0x121, 4)
    Jump("loc_3BCA")

    label("loc_3BCA")

    Jump("loc_3BFD")

    label("loc_3BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3BE0")
    SetScenarioFlags(0x121, 2)
    Jump("loc_3BFD")

    label("loc_3BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_3BF1")
    SetScenarioFlags(0x121, 3)
    Jump("loc_3BFD")

    label("loc_3BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_3BFD")
    SetScenarioFlags(0x121, 4)

    label("loc_3BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 2)), scpexpr(EXPR_END)), "loc_4099")
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
            "#00112F#N#11P...U-Umm...\x01",
            "I should get back to Bell.\x02\x03",
            "#00113FThere may be something I can\x01",
            "do for "uncle" and the others.\x01\x02",
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
            "#00004FY-Yeah...\x01",
            "I should resupply and check\x01",
            "our equipment while I can.\x02\x03",
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
            "#00113F...Umm, as for the sequel to what just happened...\x01",
            "Even if it comes after this is all resolved...\x02",
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
            "#00005FHuh.\x07\x00\x02",
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
            "#00004F#5P(...Since then we both have been busy\x01",
            "and there hasn't been any progress at all...)\x02\x03",
            "(When Elie comes back, somehow,\x01",
            "I'll have to...that sequel──)\x02\x03",
            "#00011F(No, no, it's not the sequel!\x01",
            "I must think about her more seriously...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100F...Mr. Lloyd?\x02",
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
            "#00012FAt any rate, man, how tired I am!\x01",
            "I want to quickly go to rest on the SSS sofa!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x109,
        "#12P#10105F(Mr. Lloyd's reaction is suspicious...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B4C")

    label("loc_4099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_458E")
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
            "When this mess is safely resolved,\x01",
            "please take me there.\x02",
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
            "#00011FEeh...?\x01",
            "Are you really alright with that!?\x02\x03",
            "#00001FAh, but...\x01",
            "Wouldn't a little more serious\x01",
            "promise be better?\x02\x03",
            "Something like, "whenever I'm in trouble, \x01",
            "no matter what happens, come save me." \x01",
            "Something like that.\x07\x00\x02",
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
            "#00208FAnd, if this situation is not safely resolved,\x01",
            "this promise will not be fulfilled...\x02\x03",
            "#00202FIn that sense, I think it\x01",
            "is plenty serious, isn't it.\x07\x00\x02",
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
            "#00004F#5P(...Since then we both have been busy\x01",
            "and we didn't go to have fun there yet...)\x02\x03",
            "(When Tio comes back, I'll absolutely\x01",
            "must keep that promise.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105F...Mr. Lloyd?\x02",
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
            "#00000F...By the way, Noｱl, have you\x01",
            "ever gone to the Theme Park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FAt Michelam?\x01",
            "Yes, although only once, with Fran.\x02\x03",
            "#10109FThe attractions are fun too,\x01",
            "but Michey's cute!\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x109, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#5PI-I see...\x01",
            "(Michey is super popular, eh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4C")

    label("loc_458E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_4B4C")
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
            "#00303F#N#11P──If the CGF advance, we'll\x01",
            "be the ones to work the hardest.\x02\x03",
            "#00300FI don't want to push milady\x01",
            "and peTiote too hard.\x02",
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
            "#00309FI've got your back──buddy.\x07\x00\x02",
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
            "#00005FYeah...\x02\x03",
            "#00002F──Understood!\x07\x00\x02",
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
            "#00008F#5P(Buddy, eh...?)\x02\x03",
            "#00003F(Honestly, I can't think I'm\x01",
            "balanced as a man, yet.)\x02\x03",
            "#00000F(To really be able to be on par with him,\x01",
            "I must do my best more too...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105F...Mr. Lloyd?\x02",
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
            "#00000FBy the way, Noｱl, I wonder how do you\x01",
            "judge Randy from your point of view?\x02\x03",
            "From a member of the CGF\x01",
            "more than from a detective's one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FSenior Randy?\x02\x03",
            "#10104FLet's see...\x01",
            "As you can expect, he's peculiar.\x02\x03",
            "#10100FOf course he has individual fighting strength,\x01",
            "but I also heard he has fairly amazing\x01",
            "fighting skills at a unit level...\x02\x03",
            "I think he's quite blazing through the\x01",
            "rehabilitation training is doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PI see...\x02\x03",
            "#00008F(...Now that I think about it,\x01",
            "Randy said he'd have used\x01",
            "rifles in this training...)\x02\x03",
            "(Could it be that he has broken \x01",
            "through his jaeger period a little...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B4C")

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

    # Function_16_247C end

    def Function_17_4BC7(): pass

    label("Function_17_4BC7")

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

    # Function_17_4BC7 end

    def Function_18_536A(): pass

    label("Function_18_536A")

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
            "#00004FWell then, what we're in charge of\x01",
            "are the two vehicles in the back.\x02\x03",
            "#00001FAs for passengers...\x01",
            "It looks like there're quite many.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5503")

    ChrTalk(
        0x102,
        (
            "#00100FYes it does. In any case, let's check\x01",
            "them carefully one by one.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x0)
    Jump("loc_56AA")

    label("loc_5503")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_556C")

    ChrTalk(
        0x103,
        (
            "#00200FYes. In any case, let's check them\x01",
            "in order from start to finish.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x1)
    Jump("loc_56AA")

    label("loc_556C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55D5")

    ChrTalk(
        0x104,
        (
            "#00304FWell, in any case we can only\x01",
            "comb them all from start to finish.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x2)
    Jump("loc_56AA")

    label("loc_55D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_563B")

    ChrTalk(
        0x109,
        (
            "#10100FYes. In any case, let's go and\x01",
            "finish to check them carefully.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x3)
    Jump("loc_56AA")

    label("loc_563B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56AA")

    ChrTalk(
        0x105,
        (
            "#10300F*sigh*, at any rate, it looks like we can\x01",
            "only check all of them thoroughly.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x4)

    label("loc_56AA")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_536A end

    def Function_19_56B1(): pass

    label("Function_19_56B1")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571A")

    ChrTalk(
        0x101,
        (
            "#00003F...That the 3rd vehicle.\x01",
            "First, let's check all the 4th vehicle passengers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5782")

    label("loc_571A")


    ChrTalk(
        0x101,
        (
            "#00003F...We aren't in charge of the vehicles in front.\x01",
            "Let's focus on our on-spot inspection now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5782")

    Sleep(50)
    SetChrPos(0x0, -10, 0, 7470, 180)
    EventEnd(0x4)
    Return()

    # Function_19_56B1 end

    def Function_20_5799(): pass

    label("Function_20_5799")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F...The on-spot inspection is not over yet.\x01",
            "We can't get off the train.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)
    Return()

    # Function_20_5799 end

    def Function_21_5805(): pass

    label("Function_21_5805")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F...The on-spot inspection is not over yet.\x01",
            "We can't get off the train.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, 7850, 270)
    EventEnd(0x4)
    Return()

    # Function_21_5805 end

    def Function_22_5871(): pass

    label("Function_22_5871")

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
            "Inspector Assistants.\x02\x03",
            "I'm sorry to trouble you\x01",
            "but could we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Mother...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59A4")

    ChrTalk(
        0x102,
        (
            "#00105F(It looks like he\x01",
            "didn't hear you.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABF")

    label("loc_59A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59EB")

    ChrTalk(
        0x103,
        (
            "#00205F(It looks like he\x01",
            "didn't hear you...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABF")

    label("loc_59EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A2B")

    ChrTalk(
        0x104,
        "#00305F(Hm, he's not listening, huh?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5ABF")

    label("loc_5A2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A78")

    ChrTalk(
        0x109,
        (
            "#10105F(Uhhm...\x01",
            "It looks like he didn't hear you.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABF")

    label("loc_5A78")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ABF")

    ChrTalk(
        0x105,
        (
            "#10302F(Hu hu, it looks like\x01",
            "he didn't hear you.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ABF")


    ChrTalk(
        0x101,
        "#00006F#4SUhhm, excuse us...\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B87")
    Jump("loc_5BD1")

    label("loc_5B87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BA7")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BD1")

    label("loc_5BA7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BC7")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BD1")

    label("loc_5BC7")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BD1")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        "Eh, aah...I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I was spacing out a little.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uhhm, you're Inspectors, right?\x01",
            "Please, do your checking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, so, let's see...\x02",
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
            "#00004FI checked your hand luggage\x01",
            "and entry permit.\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ah, no, you're welcome.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 4)
    OP_29(0x79, 0x1, 0x5)
    ClearChrFlags(0xC, 0x10)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_5871 end

    def Function_23_5D36(): pass

    label("Function_23_5D36")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E1E")
    Jump("loc_5E68")

    label("loc_5E1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E3E")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E68")

    label("loc_5E3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E5E")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E68")

    label("loc_5E5E")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E68")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F1E")
    Jump("loc_5F68")

    label("loc_5F1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F3E")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F68")

    label("loc_5F3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F5E")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F68")

    label("loc_5F5E")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F68")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FUhhm, we're Inspector Assistants.\x02\x03",
            "I'm sorry to trouble you\x01",
            "but could we check your hand\x01",
            "luggages and entry permits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, but of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "On-the-spot inspection, on-the-spot inspectiooon♪\x01",
            "Do your best, misters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, then let me\x01",
            "check at once.\x02",
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
            "#00004FI checked your hand luggages\x01",
            "and entry permits.\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, you're welcome. It's only\x01",
            "reasonable to cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thank you for your hard\x01",
            "work, misteeers☆\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61BA")

    ChrTalk(
        0x102,
        "#00102F*giggle*, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6288")

    label("loc_61BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61F7")

    ChrTalk(
        0x103,
        (
            "#00202FUh uh, thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6288")

    label("loc_61F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6227")

    ChrTalk(
        0x104,
        "#00309FHa ha, thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6288")

    label("loc_6227")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_625A")

    ChrTalk(
        0x109,
        "#10109FUh uh, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6288")

    label("loc_625A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6288")

    ChrTalk(
        0x105,
        "#10309FHu hu, thank you.\x02",
    )

    CloseMessageWindow()

    label("loc_6288")

    SetScenarioFlags(0x1CA, 3)
    OP_29(0x79, 0x1, 0x6)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_5D36 end

    def Function_24_62A6(): pass

    label("Function_24_62A6")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_638E")
    Jump("loc_63D8")

    label("loc_638E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_63AE")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_63D8")

    label("loc_63AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63CE")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_63D8")

    label("loc_63CE")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63D8")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FPardon us, we're\x01",
            "Inspector Assistants.\x02\x03",
            "I'm sorry to trouble you\x01",
            "but could we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hu hu, I was waiting for you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Come now, go ahead and check!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FR-Right...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6515")

    ChrTalk(
        0x102,
        "#00105F(Awfully hyper, eh?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_65FA")

    label("loc_6515")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_654D")

    ChrTalk(
        0x103,
        "#00200F(He is awfully hyper.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_65FA")

    label("loc_654D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6586")

    ChrTalk(
        0x104,
        "#00306F(He's very hyper, huh?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_65FA")

    label("loc_6586")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65BF")

    ChrTalk(
        0x109,
        "#10105F(He's strangely hyper.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_65FA")

    label("loc_65BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65FA")

    ChrTalk(
        0x105,
        "#10303F(Hu hu, he's quite hyper, eh?)\x02",
    )

    CloseMessageWindow()

    label("loc_65FA")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004FI checked your hand luggage\x01",
            "and entry permit.\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mwhuhuhu, you saw it too, right?\x01",
            "This sheaf of contracts, I mean!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Actually, I'm going to do certain\x01",
            "big business negotiations now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I'll settle them, I'll greatly profit for sure...\x01",
            "Maaan, I can't help but looking forward to it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-Is that so...?\x01",
            "I hope it goes well.\x02\x03",
            "#00003F(I see, so he's hyper\x01",
            "for this reason, eh?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 2)
    OP_29(0x79, 0x1, 0x7)
    ClearChrFlags(0x9, 0x10)
    SetChrSubChip(0x9, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_62A6 end

    def Function_25_67DD(): pass

    label("Function_25_67DD")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_68C5")
    Jump("loc_690F")

    label("loc_68C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68E5")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_690F")

    label("loc_68E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6905")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_690F")

    label("loc_6905")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_690F")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're Inspector Assistants.\x02\x03",
            "I'm sorry to trouble you\x01",
            "but could we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yeah, of course, I don't mind.\x02",
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
            "#00004FI checked your hand luggage\x01",
            "and entry permit.\x02\x03",
            "#00001FHowever...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Hm? Is something the matter?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AFB")

    ChrTalk(
        0x102,
        (
            "#00101FYes, it looks like there is \x01",
            "no boarding ticket in \x01",
            "your hand luggage.\x02\x03",
            "Could you have any clue?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CE5")

    label("loc_6AFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B79")

    ChrTalk(
        0x103,
        (
            "#00201FYes, it looks like there's \x01",
            "no boarding ticket in \x01",
            "your hand luggage.\x02\x03",
            "Do you have any clue?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CE5")

    label("loc_6B79")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BED")

    ChrTalk(
        0x104,
        (
            "#00301FYeah, Looks like there's \x01",
            "no boardin' ticket in \x01",
            "your hand luggage.\x02\x03",
            "Got any clue?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CE5")

    label("loc_6BED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C62")

    ChrTalk(
        0x109,
        (
            "#10101FYes, we can't see\x01",
            "any boarding ticket in \x01",
            "your hand luggage.\x02\x03",
            "Do you have any clue?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CE5")

    label("loc_6C62")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CE5")

    ChrTalk(
        0x105,
        (
            "#10304FYeah, it looks like there's \x01",
            "no boarding ticket in \x01",
            "your hand luggage...\x02\x03",
            "#10302FDo you have any clue?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CE5")

    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "You say there's no t-ticket!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But that can't be, I've\x01",
            "properly put it in my bag...\x02",
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
        "...No, no, it's nowhere!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Maybe in my clothes pockets? No, at any rate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I-I'm sorry, could you\x01",
            "wait a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I absolutely have the ticket.\x01",
            "I'll find it out for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FY-Yes...\x01",
            "Then, we'll ask you again.\x02\x03",
            "#00003F(It can't be helped, we'll leave this person\x01",
            "for later and continue with the inspection.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 1)
    OP_29(0x79, 0x1, 0x8)
    ClearChrFlags(0x8, 0x10)
    SetChrSubChip(0x8, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_67DD end

    def Function_26_6EF3(): pass

    label("Function_26_6EF3")

    ModifyEventFlags(0, 3, 0x80)
    SetScenarioFlags(0x158, 6)
    Return()

    # Function_26_6EF3 end

    def Function_27_6EFC(): pass

    label("Function_27_6EFC")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6FE4")
    Jump("loc_702E")

    label("loc_6FE4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7004")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_702E")

    label("loc_7004")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7024")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_702E")

    label("loc_7024")

    OP_52(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_702E")

    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FPardon us, we're\x01",
            "Inspector Assistants.\x02\x03",
            "I'm sorry to trouble you\x01",
            "but could we check your hand\x01",
            "luggage and entry permit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "*sigh*, you say such a thing but I have\x01",
            "no right to refuse, am I correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "In this case, you should\x01",
            "check thoroughly and\x01",
            "finish quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Right, I'm sorry.\x02",
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
            "#00004FI checked your hand luggage\x01",
            "and entry permit.\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "...*sigh*, like I told you, I\x01",
            "don't need such words of thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Your business is over, right?\x01",
            "Then go away, fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FY-Yes, excuse us.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72E1")

    ChrTalk(
        0x102,
        (
            "#00106F(*sigh*, this job is\x01",
            "quite stressful, eh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741E")

    label("loc_72E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7329")

    ChrTalk(
        0x103,
        (
            "#00206F(*sigh*, this is a\x01",
            "stressful job, eh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741E")

    label("loc_7329")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_737A")

    ChrTalk(
        0x104,
        (
            "#00306F(*sigh*, this job too\x01",
            "is quite stressful, huh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741E")

    label("loc_737A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73CA")

    ChrTalk(
        0x109,
        (
            "#10106F(*sigh*, this is quite\x01",
            "the stressful job, eh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741E")

    label("loc_73CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_741E")

    ChrTalk(
        0x105,
        (
            "#10304F(Hu hu, even the\x01",
            "Inspector one is a\x01",
            "stressful job, eh?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_741E")

    OP_5A()
    SetScenarioFlags(0x1CB, 0)
    OP_29(0x79, 0x1, 0x9)
    ClearChrFlags(0x12, 0x10)
    SetChrSubChip(0x12, 0x0)
    EventEnd(0x5)
    Return()

    # Function_27_6EFC end

    def Function_28_7434(): pass

    label("Function_28_7434")

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
            "Uhuhu, as expected,\x01",
            "the "Eisengraf" is on a different\x01",
            "league with the other trains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "*drool*...\x01",
            "Oopsie, dear me, dear me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(S-She's drooling...?)\x02\x03",
            "#00000FExcuse us, we're\x01",
            "Inspector Assistants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Ah, I'm currently busy\x01",
            "with train watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The permit is in the bag, so\x01",
            "you can feel free to inspect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FU-Understood.\x01",
            "Then...\x02",
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
            "#00004FI checked your hand luggage\x01",
            "and entry permit.\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "*mumble mumble*... I wonder how \x01",
            "many minutes are left till departure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "*aahn*, I don't want to part...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7722")

    ChrTalk(
        0x102,
        (
            "#00103F(...S-She looks like\x01",
            "quite focused, eh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7826")

    label("loc_7722")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_776A")

    ChrTalk(
        0x103,
        (
            "#00203F(...She didn't turn\x01",
            "around even once.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7826")

    label("loc_776A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77A4")

    ChrTalk(
        0x104,
        "#00306F(...Not listenin', huh?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_7826")

    label("loc_77A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77EC")

    ChrTalk(
        0x109,
        (
            "#10106F(...She likes trains\x01",
            "quite a lot, eh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7826")

    label("loc_77EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7826")

    ChrTalk(
        0x105,
        "#10302F(Hu hu, she's not listening.)\x02",
    )

    CloseMessageWindow()

    label("loc_7826")

    OP_5A()
    SetScenarioFlags(0x1CA, 7)
    OP_29(0x79, 0x1, 0xA)
    EventEnd(0x5)
    Return()

    # Function_28_7434 end

    def Function_29_7833(): pass

    label("Function_29_7833")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_791B")
    Jump("loc_7965")

    label("loc_791B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_793B")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7965")

    label("loc_793B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_795B")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7965")

    label("loc_795B")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7965")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FUhhm, we're Inspector Assistants...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F(This suit...\x01",
            "Could he be a "Heiyue" member?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Hm, is there any problem?\x02",
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)
    Sleep(300)
    OP_93(0x10, 0x5A, 0x1F4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_80D4")
    OP_29(0x79, 0x1, 0xB)

    ChrTalk(
        0x10,
        "Hm? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F...Wait, Shing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...You're from\x01",
            "the SSS!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B28")

    ChrTalk(
        0x10,
        (
            "And there's Miss\x01",
            "Elie with you too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F*giggle*, hello Shing.\x02",
    )

    CloseMessageWindow()

    label("loc_7B28")


    ChrTalk(
        0x10,
        (
            "But, what are you\x01",
            "doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, as a job for the SSS, we're\x01",
            "helping the Inspector here.\x02\x03",
            "That's why we'd like to check your\x01",
            "hand luggages and permits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I understand, so the Support Section\x01",
            "does even these kind of jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Oh, well, if that's the situation,\x01",
            "just finish it quickly.\x02",
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
            "#00004F...Alright.\x01",
            "I finished checking your hand\x01",
            "luggages and permits.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D8E")

    ChrTalk(
        0x102,
        "#00100FThank you for your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hu hu, this is nothing if\x01",
            "it's to help out Miss Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "We'll see for sure one day!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, I'll look forward to it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_80CF")

    label("loc_7D8E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EC1")

    ChrTalk(
        0x103,
        "#00200FThank you for your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "(Hm, there's also this girl\x01",
            "in the Support Section.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F...Do I have something on my face?\x02",
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
        "...Then, see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FYeah, be well too, Shing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_80CF")

    label("loc_7EC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F70")

    ChrTalk(
        0x104,
        "#00300FThanks for your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, I only did what\x01",
            "it had to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Then, see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FYeah, be well too, Shing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_80CF")

    label("loc_7F70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8022")

    ChrTalk(
        0x109,
        "#10100FThank you for your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, I only did what\x01",
            "it had to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Then, see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FYeah, be well too, Shing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_80CF")

    label("loc_8022")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80CF")

    ChrTalk(
        0x105,
        "#10300FThank you for your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, I only did what\x01",
            "it had to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Then, see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FYeah, be well too, Shing.\x02",
    )

    CloseMessageWindow()

    label("loc_80CF")

    Jump("loc_887C")

    label("loc_80D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_844A")
    OP_29(0x79, 0x1, 0xB)

    ChrTalk(
        0x10,
        "Hm? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F...Wait, aren't you the Heiyue...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...You're from\x01",
            "the SSS!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8207")

    ChrTalk(
        0x10,
        (
            "And there's Miss\x01",
            "Elie with you too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F*giggle*, hello Shing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Y-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "So, what're you doing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8225")

    label("loc_8207")


    ChrTalk(
        0x10,
        "But, what are you doing?\x02",
    )

    CloseMessageWindow()

    label("loc_8225")


    ChrTalk(
        0x101,
        (
            "#00000FWell, as a job for the SSS, we're\x01",
            "helping the Inspector here.\x02\x03",
            "That's why we'd like to check your\x01",
            "hand luggages and permits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I understand, so the Support Section\x01",
            "does even these kind of jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Oh, well, if that's the situation,\x01",
            "just finish it quickly.\x02",
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
            "#00004F...Alright.\x01",
            "I finished checking your hand\x01",
            "luggages and entry permits.\x02\x03",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, I only did what\x01",
            "it had to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "If you've finished your business, go away now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FY-Yeah...excuse us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_887C")

    label("loc_844A")


    NpcTalk(
        0x10,
        "Boy",
        "Hm? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0xC)

    ChrTalk(
        0x101,
        (
            "#00000FUhhm, we're Inspector Assistants.\x02\x03",
            "I'm sorry to trouble you\x01",
            "but could we check your hand\x01",
            "luggages and entry permits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Yes, of course we don't mind.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Boy",
        "Yeah, but just get it over with it fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85CB")

    ChrTalk(
        0x102,
        (
            "#00105F(Is this kid related to the Heiyue too, I wonder?\x01",
            "Somehow he's quite arrogant...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8789")

    label("loc_85CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8642")

    ChrTalk(
        0x103,
        (
            "#00205F(Is this kid related to the Heiyue too, I wonder?\x01",
            "He appears to be quite arrogant...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8789")

    label("loc_8642")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86AC")

    ChrTalk(
        0x104,
        (
            "#00303F(Is this kiddo related to the Heiyue too?\x01",
            "Somehow he's very arrogant...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8789")

    label("loc_86AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8711")

    ChrTalk(
        0x109,
        (
            "#10105F(Is this kid related to the Heiyue too?\x01",
            "He seems quite arrogant...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8789")

    label("loc_8711")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8789")

    ChrTalk(
        0x105,
        (
            "#10304F(Is this kid related to the Heiyue too, I wonder?\x01",
            "He seems to be quite arrogant, though...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8789")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004FI finished checking your hand\x01",
            "luggages and entry permits.\x01",
            "Thank you for your cooperation.\x02",
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
            "Hmph, if you've finished your\x01",
            "business, then go away now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FY-Yes...\x02",
    )

    CloseMessageWindow()

    label("loc_887C")

    OP_5A()
    SetScenarioFlags(0x1CA, 6)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    ClearChrFlags(0xF, 0x10)
    SetChrSubChip(0xF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_29_7833 end

    def Function_30_8897(): pass

    label("Function_30_8897")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_897F")
    Jump("loc_89C9")

    label("loc_897F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_899F")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89C9")

    label("loc_899F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89BF")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89C9")

    label("loc_89BF")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_89C9")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A7F")
    Jump("loc_8AC9")

    label("loc_8A7F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8A9F")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8AC9")

    label("loc_8A9F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8ABF")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8AC9")

    label("loc_8ABF")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8AC9")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're Inspector Assistants.\x02\x03",
            "I'm sorry to trouble you\x01",
            "but could we check your hand\x01",
            "luggages and entry permits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What, why do I have to\x01",
            "let you do such thing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)
    SetChrSubChip(0xE, 0x0)

    ChrTalk(
        0xE,
        (
            "H-Hey...\x01",
            "What're you saying to the Inspector!?\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C89")
    Jump("loc_8CD3")

    label("loc_8C89")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8CA9")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8CD3")

    label("loc_8CA9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CC9")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8CD3")

    label("loc_8CC9")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8CD3")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xE,
        (
            "I'm sorry, my little sister\x01",
            "was really rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "She's a real moron,\x01",
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
            "Moron? What's with the moron!?\x01",
            "Also, big brother, you...\x02",
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
        "#00006F(Ehhm, I can start, right?)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E40")

    ChrTalk(
        0x102,
        "#00100F(Yes, I think.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F07")

    label("loc_8E40")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E74")

    ChrTalk(
        0x103,
        "#00200F(I think you can.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F07")

    label("loc_8E74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EA6")

    ChrTalk(
        0x104,
        "#00300F(Yeah, I guess.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F07")

    label("loc_8EA6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8ED9")

    ChrTalk(
        0x109,
        "#10100F(Yes, I think...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F07")

    label("loc_8ED9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F07")

    ChrTalk(
        0x105,
        "#10300F(Hu hu, I guess.)\x02",
    )

    CloseMessageWindow()

    label("loc_8F07")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FA3")
    Jump("loc_8FED")

    label("loc_8FA3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8FC3")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8FED")

    label("loc_8FC3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FE3")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8FED")

    label("loc_8FE3")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8FED")

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
            "#00004FI checked your hand\x01",
            "luggages and entry permits.\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No, no, I'm sorry for my little\x01",
            "sister to have caused you trouble.\x02",
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
            "What's with that? If you put it like this,\x01",
            "then it's you big brother that...\x02",
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
        "#00003F(It looks like it's better to get away fast.)\x02",
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

    # Function_30_8897 end

    def Function_31_91C0(): pass

    label("Function_31_91C0")

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
        "#00000FWell then, did we check everyone?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92F1")

    ChrTalk(
        0x102,
        (
            "#00105FNow that you mention it, we didn't\x01",
            "check the old mister's ticket in the\x01",
            "4th vehicle yet, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_92F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9377")

    ChrTalk(
        0x103,
        (
            "#00205FNow that you mention it, we didn't\x01",
            "check the old mister's ticket in the\x01",
            "4th vehicle yet, am I right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_9377")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93F3")

    ChrTalk(
        0x104,
        (
            "#00305FNow that you mention it, we didn't\x01",
            "check the ol' man's ticket in the\x01",
            "4th vehicle yet, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_93F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9471")

    ChrTalk(
        0x109,
        (
            "#10105FNow that you mention it, we didn't\x01",
            "check the old mister's ticket in the\x01",
            "4th vehicle yet, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94ED")

    label("loc_9471")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94ED")

    ChrTalk(
        0x105,
        (
            "#10305FNow that you mention it, we didn't\x01",
            "check the old man's ticket in the\x01",
            "4th vehicle yet, right...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94ED")


    ChrTalk(
        0x101,
        (
            "#00003FYes, you're right. Then, let's\x01",
            "go back immediately and che...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        "...G-Give me back my ticket!!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95C9")

    ChrTalk(
        0x102,
        "#00101F...Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9678")

    label("loc_95C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95F8")

    ChrTalk(
        0x103,
        "#00201F...Mr. Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9678")

    label("loc_95F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9623")

    ChrTalk(
        0x104,
        "#00301F...Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9678")

    label("loc_9623")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9652")

    ChrTalk(
        0x109,
        "#10101F...Mr. Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9678")

    label("loc_9652")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9678")

    ChrTalk(
        0x105,
        "#10301F...Lloyd!\x02",
    )

    CloseMessageWindow()

    label("loc_9678")


    ChrTalk(
        0x101,
        "#00000FYeah, let's go at once!\x02",
    )

    CloseMessageWindow()
    Call(0, 32)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_96B3")
    Call(0, 34)
    Jump("loc_96B6")

    label("loc_96B3")

    Call(0, 33)

    label("loc_96B6")

    EventEnd(0x5)
    Return()

    # Function_31_91C0 end

    def Function_32_96B9(): pass

    label("Function_32_96B9")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97EB")
    SetChrPos(0x102, -480, 0, 8210, 180)
    Jump("loc_987E")

    label("loc_97EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9811")
    SetChrPos(0x103, -480, 0, 8210, 180)
    Jump("loc_987E")

    label("loc_9811")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9837")
    SetChrPos(0x104, -480, 0, 8210, 180)
    Jump("loc_987E")

    label("loc_9837")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_985D")
    SetChrPos(0x109, -480, 0, 8210, 180)
    Jump("loc_987E")

    label("loc_985D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_987E")
    SetChrPos(0x105, -480, 0, 8210, 180)

    label("loc_987E")

    OP_68(120, 1000, 220, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "That's why I'm saying that\x01",
            "it must be one of you two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Come now, who did it!?\x01",
            "Confess at once!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    def lambda_9926():
        OP_95(0x101, 460, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9926)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_996A")

    def lambda_9950():
        OP_95(0x102, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9950)
    Jump("loc_9A21")

    label("loc_996A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9999")

    def lambda_997F():
        OP_95(0x103, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_997F)
    Jump("loc_9A21")

    label("loc_9999")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99C8")

    def lambda_99AE():
        OP_95(0x104, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_99AE)
    Jump("loc_9A21")

    label("loc_99C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99F7")

    def lambda_99DD():
        OP_95(0x109, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_99DD)
    Jump("loc_9A21")

    label("loc_99F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A21")

    def lambda_9A0C():
        OP_95(0x105, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A0C)

    label("loc_9A21")

    OP_68(70, 1000, 2830, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16500, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FExcuse us, has something happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, the Inspectors from before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, it's awful.\x01",
            "This old man is falsely accu...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "What the...\x01",
            "How dare you shamelessly...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FP-Please calm down!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B9E")

    ChrTalk(
        0x102,
        (
            "#00101FExcuse me, can we, first of all,\x01",
            "hear the entire story?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D0C")

    label("loc_9B9E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BF9")

    ChrTalk(
        0x103,
        (
            "#00200FExcuse me, could we, first of all,\x01",
            "hear the entire story?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D0C")

    label("loc_9BF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C57")

    ChrTalk(
        0x104,
        (
            "#00303FFor starters, could we, first of all,\x01",
            "hear the entire story?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D0C")

    label("loc_9C57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CB4")

    ChrTalk(
        0x109,
        (
            "#10101FAt any rate, could we, first of all,\x01",
            "hear the entire story?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D0C")

    label("loc_9CB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D0C")

    ChrTalk(
        0x105,
        (
            "#10304FIn any case, could we, first of all,\x01",
            "hear the entire story?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D0C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 550, 0, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D4E")
    SetChrPos(0x102, -540, 0, 1100, 180)
    Jump("loc_9DE1")

    label("loc_9D4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D74")
    SetChrPos(0x103, -540, 0, 1100, 180)
    Jump("loc_9DE1")

    label("loc_9D74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D9A")
    SetChrPos(0x104, -540, 0, 1100, 180)
    Jump("loc_9DE1")

    label("loc_9D9A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DC0")
    SetChrPos(0x109, -540, 0, 1100, 180)
    Jump("loc_9DE1")

    label("loc_9DC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DE1")
    SetChrPos(0x105, -540, 0, 1100, 180)

    label("loc_9DE1")

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
            "#00003FI understand. The ticket this gentleman\x01",
            "purchased is assigned to the 4th vehicle\x01",
            "and bound to the autonomous state of Ord...\x02\x03",
            "Also, in this vehicle there're two persons\x01",
            "who have the same exact ticket...\x02\x03",
            "#00001FIn other words, it's possible that one\x01",
            "of these two men stole the ticket.\x01",
            "Is this what you want to say, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yeah, that's exactly it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...At any rate, it's a sure fact\x01",
            "that I entered the platform\x01",
            "with the ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, there's no way that I could've\x01",
            "lost it in this short amount of time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's it, unless I\x01",
            "got robbed, you see.\x02",
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
            "#00006FUhhm, as you can imagine\x01",
            "we can't conclude that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's ok, it's ok, let him\x01",
            "say whatever he wants!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "After all, he's just senile.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "Damn you, you're still...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FFor now...\x01",
            "Please settle down you two.\x02\x03",
            "#00001FIn any case, nothing will be\x01",
            "settled if you just keep knocking\x01",
            "ideas against each other.\x02\x03",
            "#00003FAnd so, please let me ask a simple\x01",
            "question to you two who have a ticket.\x02\x03",
            "#00001FThe motive for going to your destination...\x01",
            "Could you at the very least tell us that?\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "T-The motive for going...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmph, and with that you'd be able\x01",
            "to have a proof of innocence?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, if, hypothetically, the ticket was\x01",
            "really stolen, then it's possible that\x01",
            "the culprit has got no set destination.\x02\x03",
            "#00004FIn that case, the culprit could\x01",
            "reveal some kind of fault.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A460")

    ChrTalk(
        0x102,
        (
            "#00105FI understand, it's true\x01",
            "that's possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A57D")

    label("loc_A460")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4B2")

    ChrTalk(
        0x103,
        (
            "#00203FI understand, it is true\x01",
            "that could be possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A57D")

    label("loc_A4B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4F1")

    ChrTalk(
        0x104,
        (
            "#00305FGot it, that could\x01",
            "be likely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A57D")

    label("loc_A4F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A53B")

    ChrTalk(
        0x109,
        (
            "#10105FI understand, it's true\x01",
            "that's possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A57D")

    label("loc_A53B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A57D")

    ChrTalk(
        0x105,
        (
            "#10302FI understand, that\x01",
            "could be possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A57D")


    ChrTalk(
        0x8,
        (
            "Hmph, then let's strike while the iron\x01",
            "is hot. Come on, answer at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmph, that's an easy request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm a trader.\x01",
            "I have important negotiations\x01",
            "at the autonomous state of Ord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Incidentally, this is the written contract.\x01",
            "My client is the "Ryｹshin Company"\x01",
            "located in Ord. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Stealing the ticket from such a man...\x01",
            "I have no reason to do a petty thing, right?\x02",
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
            "E-Ehm, my hometown is in the\x01",
            "autonomous state of Ord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Isn't going back to my village a motive?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, I'm not saying that...\x02\x03",
            "#00008F(Uhmm, from what I asked them,\x01",
            "I can't use just that for judging.)\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_32_96B9 end

    def Function_33_A81C(): pass

    label("Function_33_A81C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A867")

    ChrTalk(
        0x102,
        (
            "#00103F(...It looks like this\x01",
            "is all we can do.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A985")

    label("loc_A867")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8AF")

    ChrTalk(
        0x103,
        (
            "#00203F(...It appears this\x01",
            "is all we can do.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A985")

    label("loc_A8AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8F2")

    ChrTalk(
        0x104,
        (
            "#00303F(...Seems this\x01",
            "is all we can do.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A985")

    label("loc_A8F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A93F")

    ChrTalk(
        0x109,
        (
            "#10103F(...It looks like this\x01",
            "is all we can do...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A985")

    label("loc_A93F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A985")

    ChrTalk(
        0x105,
        (
            "#10303F(...It looks like this\x01",
            "is all we can do.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A985")


    ChrTalk(
        0x101,
        (
            "#00003F(Right...\x01",
            "It seems that we can only report this to\x01",
            "Mr. Marlowe who is the expert here.)\x02\x03",
            "#00000FExcuse us, please wait\x01",
            "here for a little while.\x02\x03",
            "I'm going to call my superior now.\x02",
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

    # Function_33_A81C end

    def Function_34_AA6C(): pass

    label("Function_34_AA6C")

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
            "Ha ha, how fun.\x01",
            "There's a liar in this vehicle!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AB2B():
        OP_93(0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AB2B)

    def lambda_AB38():
        OP_93(0x1, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AB38)
    OP_68(460, 1000, 5040, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16210, 3000)

    def lambda_AB73():
        OP_95(0x10, 460, 0, 5470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_AB73)

    def lambda_AB8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_AB8D)

    def lambda_AB9E():
        OP_95(0xF, -480, 0, 5970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_AB9E)

    def lambda_ABB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_ABB8)
    Sleep(2000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x1, 0x8)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AD4C")

    ChrTalk(
        0x101,
        (
            "#00005F...Shing?\x02\x03",
            "#00001FW-Wait a moment.\x01",
            "There's a rule that you can't move to other\x01",
            "vehicles while the on-the-spot inspection is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmph, you've already finished\x01",
            "the inspection, right?\x01",
            "Be flexible about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, but...\x01",
            "*sigh*, whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "At any rate, it appears that\x01",
            "something fun is going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Let me participate too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADB6")

    label("loc_AD4C")


    ChrTalk(
        0x101,
        "#00005F...Shing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hu hu, it appears that\x01",
            "something fun is going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Let me participate too!\x02",
    )

    CloseMessageWindow()

    label("loc_ADB6")


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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE51")
    SetChrPos(0x102, -540, 0, 2100, 135)
    Jump("loc_AEE4")

    label("loc_AE51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE77")
    SetChrPos(0x103, -540, 0, 2100, 135)
    Jump("loc_AEE4")

    label("loc_AE77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE9D")
    SetChrPos(0x104, -540, 0, 2100, 135)
    Jump("loc_AEE4")

    label("loc_AE9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEC3")
    SetChrPos(0x109, -540, 0, 2100, 135)
    Jump("loc_AEE4")

    label("loc_AEC3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEE4")
    SetChrPos(0x105, -540, 0, 2100, 135)

    label("loc_AEE4")

    SetChrPos(0xF, 540, 0, 2500, 180)
    OP_93(0x8, 0x5A, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00001F...So, what about that\x01",
            ""liar" thing you said?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Yeah, then, first of all, let's\x01",
            "have that trader answer.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AF7A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF7A)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFA4")

    def lambda_AF97():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF97)
    Jump("loc_B027")

    label("loc_AFA4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFC6")

    def lambda_AFB9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AFB9)
    Jump("loc_B027")

    label("loc_AFC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFE8")

    def lambda_AFDB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AFDB)
    Jump("loc_B027")

    label("loc_AFE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B00A")

    def lambda_AFFD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AFFD)
    Jump("loc_B027")

    label("loc_B00A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B027")

    def lambda_B01F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B01F)

    label("loc_B027")


    ChrTalk(
        0x10,
        (
            "Before, you said you have a client\x01",
            "called "Ryｹshin Company", eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Concretely, what's the contract content?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*, why do I have to go\x01",
            "along with this child's game...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, the deal is about purchasing\x01",
            "rare vegetables and spices from\x01",
            "the autonomous state of Ord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Speaking of Ord, it's a thriving place for agriculture...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also, the "Ryｹshin Company" is an\x01",
            "affiliate company of the "Heiyue Group"\x01",
            "who runs the Republican Eastern District...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...I don't think there's any room for suspicion...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hu hu, like you say, there's\x01",
            "a "Ryｹshin Company" in Ord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "But unfortunately...\x01",
            "It's still in the process of consolidating\x01",
            "a foothold in the autonomous state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It's not quite at the stage\x01",
            "to be able to take deals\x01",
            "with outsiders, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "What?\x01",
            "How do you know such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Well...what should I do?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0xF,
        "...Yes, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You, I was staying silent and\x01",
            "heard you were extremely rude\x01",
            "towards the young master...!\x02",
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
            "#5SHmph, remember this...\x01",
            "This person is a "Heiyue" elder's\x01",
            "grandchild, Lord Shing!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "An elder's grandchild? What a joke...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "T-The suit you're wearing...\x01",
            "I'm sure I saw it somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "N-No way... It can't be true...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x10,
        "Hu hu, did you get it now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Incidentally, what's your real motive?\x02",
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
            "Hmph, whatever.\x01",
            "You'll tell everything later to\x01",
            "the Inspector in another room.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B629")

    ChrTalk(
        0x102,
        "#00103F(...Shing, he's good.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_B710")

    label("loc_B629")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B664")

    ChrTalk(
        0x103,
        "#00203F(...This kid is amazing.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_B710")

    label("loc_B664")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6AA")

    ChrTalk(
        0x104,
        "#00303F(...That Shing, he knows his stuff.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_B710")

    label("loc_B6AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6E0")

    ChrTalk(
        0x109,
        "#10105F(...Amazing, Shing.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_B710")

    label("loc_B6E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B710")

    ChrTalk(
        0x105,
        "#10304F(Hu hu, impressive \x02",
    )

    CloseMessageWindow()

    label("loc_B710")


    ChrTalk(
        0x101,
        (
            "#00003F(Yeah, how to say it, he's\x01",
            "got quite the presence.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...So, your turn now.\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FShing...?\x02",
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
        "Hmph, who said such a thing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I have a little something\x01",
            "I want to ask you too.\x01",
            "You're from Ord, am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Y-Yes...\x01",
            "I'm going back to my village...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hm, then you'll know this for sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Aside from agriculture, the autonomous\x01",
            "state of Ord is famous for being secluded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It also has many hot springs...\x01",
            "Among these, which one is in Ord?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "①Elmo Hot Springs\x01",
            "②Parm Hot Springs\x01",
            "③Ord Hot Springs\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Now, answer!\x02",
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
            "U-Uhhm...\x01",
            "Isn't it obvious that it's\x01",
            "③Ord Hot Springs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...I see.\x01",
            "Hu hu...bwah hah.\x02",
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
            "thinking that I'm a child, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Ord Hot Springs?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "There're no hot springs\x01",
            "with such a clichｳ name\x01",
            "in the autonomous state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If you were really from Ord,\x01",
            "you'd have answered like this:\x01",
            ""No one among those", eh.\x02",
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
            "Heheh, should I pose \x01",
            "you another question?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Although I think only\x01",
            "other faults will come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "So, where're you from, really?\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "E-Eehhm...well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, I didn't think to\x01",
            "expressly say it, but\x01",
            "actually, I'm a Republican.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But now I've got a house in Ord...\x01",
            "P-Please believe me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hmph, I wonder.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    TurnDirection(0x10, 0x101, 500)

    ChrTalk(
        0x10,
        (
            "...So, how do you see this as\x01",
            "the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Aside from the content, we understood\x01",
            "that both of them, are liars, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Which one is the ticket robber?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FY-Yeah...let's see...\x02",
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
        (0, "loc_BE7F"),
        (1, "loc_C0E2"),
        (SWITCH_DEFAULT, "loc_C263"),
    )


    label("loc_BE7F")

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
            "Hey, you...\x01",
            "Don't disappoint me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Did you really think seriously about it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FA-Ah...I'm sorry.\x02\x03",
            "#00008F...I see, here I have to\x01",
            "think by elimination.\x02\x03",
            "#00001FThe fictional written contract\x01",
            "the trader has showed us...\x02\x03",
            "I don't know his reasons,\x01",
            "but he carefully prepared\x01",
            "such a thing on purpose.\x02\x03",
            "#00003FStealing a ticket is a\x01",
            "minor offense, so it's\x01",
            "an unnatural impression.\x02\x03",
            "If the destination isn't\x01",
            "Ord, a stopover could\x01",
            "be possible...\x02\x03",
            "#00001FAnd that means...\x01",
            "That you're the culprit, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C263")

    label("loc_C0E2")

    OP_2C(0x79, 0x2)

    ChrTalk(
        0x101,
        (
            "#00003FI guess it's him.\x02\x03",
            "#00001FThe fictional written contract\x01",
            "the trader has showed us...\x02\x03",
            "I don't know his reasons,\x01",
            "but he carefully prepared\x01",
            "such a thing on purpose.\x02\x03",
            "#00003FStealing a ticket is a\x01",
            "minor offense, so it's\x01",
            "an unnatural impression.\x02\x03",
            "If the destination isn't\x01",
            "Ord, a stopover could\x01",
            "be possible...\x02\x03",
            "#00001FAnd that means...\x01",
            "That you're the culprit, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C263")

    label("loc_C263")


    ChrTalk(
        0xC,
        "U-Uuuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hm, you get a passing mark.\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x1F4)

    ChrTalk(
        0x10,
        (
            "Hey, you, even if you\x01",
            "feign ignorance, you can't\x01",
            "keep covering anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If you're a man, honestly\x01",
            "confess here and now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5SP-Please, let it slide!#3S\x02",
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

    def lambda_C3DD():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C3DD)
    Sleep(50)

    def lambda_C3ED():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C3ED)
    Sleep(300)

    ChrTalk(
        0x8,
        "W-What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hey, you―\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "M-My mother was carried\x01",
            "to a Republican hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's why I must hurry up to\x01",
            "the hospital no matter what...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FE-Ehm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Suddenly I don't get it anymore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "In any case, tell us your circumstances.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Y-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually, I'm a student who's aiming\x01",
            "at St. Ursula Medical College...\x01",
            "But we're a poor family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My mother did so much to\x01",
            "send me to Crossbell...\x01",
            "I study while doing side jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In this situation, I received\x01",
            "a notice that my mother \x01",
            "suddenly collapsed...and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...You wanted to visit her but not\x01",
            "having mira, you stole a ticket.\x01",
            "Is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Y-Yes...\x01",
            "This isn't a lie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "While I'm here like this, my mother...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmmm, although you said that,\x01",
            "we can't overlook a theft...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "All right, I'll pay for you.\x02",
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

    def lambda_C7A4():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C7A4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C7CE")

    def lambda_C7C1():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C7C1)
    Jump("loc_C851")

    label("loc_C7CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C7F0")

    def lambda_C7E3():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C7E3)
    Jump("loc_C851")

    label("loc_C7F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C812")

    def lambda_C805():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C805)
    Jump("loc_C851")

    label("loc_C812")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C834")

    def lambda_C827():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C827)
    Jump("loc_C851")

    label("loc_C834")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C851")

    def lambda_C849():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C849)

    label("loc_C851")


    def lambda_C856():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C856)
    Sleep(50)

    def lambda_C866():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C866)
    Sleep(300)

    ChrTalk(
        0xC,
        "Huh...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8A9")

    ChrTalk(
        0x102,
        "#00105FShing...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C947")

    label("loc_C8A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8D2")

    ChrTalk(
        0x103,
        "#00205FWell...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C947")

    label("loc_C8D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8FC")

    ChrTalk(
        0x104,
        "#00305FH-Hey...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C947")

    label("loc_C8FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C924")

    ChrTalk(
        0x109,
        "#10105FEhm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C947")

    label("loc_C924")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C947")

    ChrTalk(
        0x105,
        "#10305FEeh...\x02",
    )

    CloseMessageWindow()

    label("loc_C947")

    TurnDirection(0x10, 0x8, 500)

    ChrTalk(
        0x10,
        (
            "Old man, I'll take responsibility and\x01",
            "have him give you back your ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "So, please, could\x01",
            "you bury the hatchet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "W-Well, if I can get back the ticket, I have\x01",
            "no interest in aggravating the situation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xC, 500)

    ChrTalk(
        0x10,
        "And you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Y-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Going to visit her with a stolen ticket?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "What if your mother knew about that?\x01",
            "Do you think she would be happy?\x02",
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
            "Listen, I'm paying but\x01",
            "this is not a cede―\x01",
            "It's a mere loan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I won't set a term, but you'll\x01",
            "absolutely return the mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uuh, I'm sorry...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I will, I will pay you back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hm, keep your promise.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 500)

    ChrTalk(
        0x10,
        (
            "Being this the case, go call the\x01",
            "Inspector in charge later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I'll explain the situation myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FY-Yes...\x02",
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

    # Function_34_AA6C end

    def Function_35_CC6C(): pass

    label("Function_35_CC6C")

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

    # Function_35_CC6C end

    def Function_36_CCB6(): pass

    label("Function_36_CCB6")

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

    # Function_36_CCB6 end

    def Function_37_CD00(): pass

    label("Function_37_CD00")

    SetChrPos(0xFE, -400, 0, -4300, 0)

    def lambda_CD16():
        OP_95(0xFE, -400, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CD16)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_37_CD00 end

    def Function_38_CD37(): pass

    label("Function_38_CD37")

    SetChrPos(0xFE, -400, 0, -5500, 0)
    Sleep(50)

    def lambda_CD50():
        OP_95(0xFE, -400, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CD50)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_38_CD37 end

    def Function_39_CD71(): pass

    label("Function_39_CD71")

    SetChrPos(0xFE, 400, 0, -4600, 0)
    Sleep(50)

    def lambda_CD8A():
        OP_95(0xFE, 400, 0, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CD8A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_39_CD71 end

    def Function_40_CDAB(): pass

    label("Function_40_CDAB")

    SetChrPos(0xFE, 400, 0, -5600, 0)
    Sleep(100)

    def lambda_CDC4():
        OP_95(0xFE, 400, 0, 2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CDC4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_40_CDAB end

    def Function_41_CDE5(): pass

    label("Function_41_CDE5")

    SetChrPos(0xFE, 400, 0, -6600, 0)
    Sleep(50)

    def lambda_CDFE():
        OP_95(0xFE, 500, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CDFE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_41_CDE5 end

    def Function_42_CE1F(): pass

    label("Function_42_CE1F")

    SetChrPos(0xFE, 400, 0, -7700, 0)
    Sleep(100)

    def lambda_CE38():
        OP_95(0xFE, 400, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CE38)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_42_CE1F end

    def Function_43_CE59(): pass

    label("Function_43_CE59")

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
        "#5P#03402F──You have arrived.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x28, 0x1)

    ChrTalk(
        0x28,
        "#11P#11509FHi, been awhile.\x02",
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
            "#6P#00200FI see, you contacted the Support Section\x01",
            "vehicle from the train receiver, right?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2AC")

    AnonymousTalk(
        0x27,
        (
            "Uh uh...looking at you again,\x01",
            "you have a distinguished lineup.\x02\x03",
            "You're together with the youngest\x01",
            "2nd Lt. of the State Guard and\x01",
            "a Gralsritter Dominion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D638")

    label("loc_D2AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D369")

    AnonymousTalk(
        0x27,
        (
            "Uh uh...looking at you again,\x01",
            "you have a distinguished lineup.\x02\x03",
            "You're together with the youngest \x01",
            "2nd Lt. of the State Guard and\x01",
            "a legendary assassin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D638")

    label("loc_D369")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D42D")

    AnonymousTalk(
        0x27,
        (
            "Uh uh...looking at you again,\x01",
            "you have a distinguished lineup.\x02\x03",
            "You're together with the youngest \x01",
            "2nd Lt. of the State Guard and\x01",
            "Section One chief detective.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D638")

    label("loc_D42D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4D9")

    AnonymousTalk(
        0x27,
        (
            "Uh uh...looking at you again,\x01",
            "you have a distinguished lineup.\x02\x03",
            "You're together with a Gralsritter \x01",
            "Dominion and a legendary assassin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D638")

    label("loc_D4D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D58C")

    AnonymousTalk(
        0x27,
        (
            "Uh uh...looking at you again,\x01",
            "you have a distinguished lineup.\x02\x03",
            "You're together with Section One\x01",
            "chief detective and a Gralsritter \x01",
            "Dominion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D638")

    label("loc_D58C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D638")

    AnonymousTalk(
        0x27,
        (
            "Uh uh...looking at you again,\x01",
            "you have a distinguished lineup.\x02\x03",
            "You're together with Section One\x01",
            "chief detective and a legendary \x01",
            "assassin.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D638")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6CB")

    ChrTalk(
        0x109,
        (
            "#6P#10103F...Unfortunately, I'm currently\x01",
            "again on loan to the SSS.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D71E")

    ChrTalk(
        0x105,
        (
            "#6P#10402FNaturally you already got\x01",
            "a grasp on my background.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D71E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D74A")

    ChrTalk(
        0x106,
        "#6P#10701F............\x02",
    )

    CloseMessageWindow()

    label("loc_D74A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D79B")

    ChrTalk(
        0x10A,
        (
            "#6P#00603FHmph...just for diplomacy,\x01",
            "I'll leave it at that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D79B")


    ChrTalk(
        0x102,
        (
            "#6P#00106FI didn't think that\x01",
            "you'd be still in\x01",
            "Crossbell.\x02\x03",
            "#00101FHave you been in the city since then?\x02",
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
            "Yeah, I had many things\x01",
            "to research...\x02\x03",
            "But, now it seems I can finally\x01",
            "go back to Erebonia.\x02",
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
        "#00011F#12PThings to research...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_END)), "loc_DCCA")

    ChrTalk(
        0x28,
        (
            "#11504FBy the way, aside from us\x01",
            "there's someone from Liberl\x01",
            "who's making his move...\x02\x03",
            "#11500FCould you know about him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYeah...Mr. Reins\x01",
            "of the R&A Research.\x02\x03",
            "#00001FCould it be that you're cooperating with him too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PYes. We're exchanging information\x01",
            "with each other regarding this matter.\x02\x03",
            "#03402FAlthough a private intelligence agency,\x01",
            "they have an excellent information net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11504FAlthough, since they are shorthanded,\x01",
            "they can't send people in every place and\x01",
            "they're probably having many hardships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PThat aside...\x02\x03",
            "#00301FHasn't your boss, the "Blood and Iron Chancellor",\x01",
            "been shot and gone missin'?\x02\x03",
            "Is it alright for you to loaf in such a place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD6D")

    label("loc_DCCA")


    ChrTalk(
        0x104,
        (
            "#00306F#12PBy the way, hasn't your boss, the "Blood and Iron \x01",
            "Chancellor", been shot and gone missin'?\x02\x03",
            "#00301FIs it alright for you to loaf in such a place?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD6D")


    ChrTalk(
        0x28,
        (
            "#11505FAah...\x01",
            "Talking about old man Giliath?\x02\x03",
            "#11506FEven if I had gone back in a hurry,\x01",
            "it's not that I could've saved him...\x02\x03",
            "#11510FAlso, considering that old man, what\x01",
            "happened to him and in Crossbell are\x01",
            "probably among the situations he predicted.\x02",
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
        "#6P#00105FWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#12P"Predicted"...\x01",
            "That he would've been shot!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FWith Crossbell you mean...\x01",
            "This incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11501FTo that old man, everything is\x01",
            "a "piece" on a game board.\x02\x03",
            "#11503FCrossbell obtaining a Sept-Terrion,\x01",
            "let alone the independence, scheming\x01",
            "to rule over the entire continent...\x02\x03",
            "That with the Imperial Army defeated the Noble \x01",
            "Alliance would've occupied the Imperial capital...\x02\x03",
            "#11508FAs a result, by getting shot and\x01",
            "mortally wounded, that a quandary\x01",
            "civil war would've started...\x02\x03",
            "To say nothing of holding back\x01",
            "a Republican invasion by making an\x01",
            "inviolable "barrier" called Crossbell.\x02\x03",
            "#11500FTo that old man, everything probably\x01",
            "developed as he had envisioned.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E242")

    ChrTalk(
        0x105,
        "#6P#10401F...A real monster.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2BF")

    label("loc_E242")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E290")

    ChrTalk(
        0x10A,
        "#6P#00610FTo think he was that much of a monster...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2BF")

    label("loc_E290")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2BF")

    ChrTalk(
        0x106,
        "#6P#10703F...A monster...\x02",
    )

    CloseMessageWindow()

    label("loc_E2BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2F5")

    ChrTalk(
        0x109,
        "#6P#10110FU-Unbelievable...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E3A5")

    label("loc_E2F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E34D")

    ChrTalk(
        0x106,
        (
            "#6P#10703F...It's a little hard to\x01",
            "believe all of a sudden...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3A5")

    label("loc_E34D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E3A5")

    ChrTalk(
        0x10A,
        (
            "#6P#00610FAs you can imagine, it's not\x01",
            "something we can swallow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3A5")


    ChrTalk(
        0x27,
        (
            "#03401F#5PWell, the "Society" seem to be on\x01",
            "the move in the Empire region, but...\x02\x03",
            "What is really terrifying could be\x01",
            "the "Blood and Iron Chancellor".\x02\x03",
            "#03403FUsing even himself as a "piece", giving\x01",
            "rise to an unruly, turbulent period...\x02\x03",
            "#03401FTruly a remarkable character──no, a monster.\x02",
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
            "#00306F#12PI thought he was a dangerous grampa,\x01",
            "but to go to those lengths...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101F...Has President Dieter\x01",
            "noticed that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03405F#5PWell, I wonder.\x02\x03",
            "#03403FI can tell you this...\x01",
            "The performance of the character\x01",
            "called Dieter Crois is superlative.\x02\x03",
            "#03401FHowever, as an actual politician...\x01",
            "I can't help but feel a little problem.\x02\x03",
            "He can only move politics by the\x01",
            "point of view of a manager, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PWell...\x02",
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
            "#03404F#5PWell, after all, his roots\x01",
            "are those of a banker.\x02\x03",
            "#03402FEven the "Crois clan" mission seems to\x01",
            "have been left entirely to the daughter.\x02",
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
            "#11504FWell, we have our\x01",
            "information sources.\x02\x03",
            "#11508FThe tyke you sheltered\x01",
            "at that auction...\x02\x03",
            "#11501FWe roughly know the story that\x01",
            "she became a "core" and the\x01",
            ""Sept-Terrion" was born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P............\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E968")

    ChrTalk(
        0x105,
        (
            "#6P#10408FOh boy...\x01",
            "To think that the worldly\x01",
            "powers grasped that much...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E968")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9E1")

    ChrTalk(
        0x10A,
        (
            "#6P#00603FNothing less to be expected from the Imperial \x01",
            "Intelligence and the Rocksmith agencies...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA06")

    ChrTalk(
        0x109,
        "#6P#10101FKh...\x02",
    )

    CloseMessageWindow()

    label("loc_EA06")


    ChrTalk(
        0x27,
        (
            "#03400F#5PI don't want you to misunderstand, but...\x01",
            "He and I are mere people\x01",
            "from the intelligence field.\x02\x03",
            "We aren't thinking to fuss\x01",
            "about the "Sept-Terrion"\x01",
            "on our own discretion.\x02\x03",
            "#03403FHowever, as for this incident that\x01",
            "became the opportunity to throw the\x01",
            "entire continent into turmoil...\x02\x03",
            "#03401FWe want to know who is the real wirepuller,\x01",
            "the "fixer" who pictured all this.\x02",
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
        "#6P#00101FThe...real fixer!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PLike I just told you, President \x01",
            "Dieter has got too much a\x01",
            "manager side, after all.\x02\x03",
            "Miss Mariabell too, although mysterious,\x01",
            "seems to undertake single handed the orbal\x01",
            "technology field more than the politics one.\x02\x03",
            "#03400FOn the other hand, the "Divine Blade of Wind"...\x01",
            "He's excessively self disciplined and too much\x01",
            "stoic to be a wirepuller.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11501FOld man Giliath, the "Society"...\x01\x02\x03",
            "He used Crossbell situation and\x01",
            "cooperated in a community of interests,\x01",
            "but he isn't moving on his own initiative.\x02\x03",
            "#11503F──There has to be someone.\x02\x03",
            "#11508FPolitics, economy, history,\x01",
            "international situation...\x02\x03",
            "The Crois clan, the D∴G Cult, even\x01",
            "all the "Society" movements...\x02\x03",
            "#11501FA guy who lead everything,\x01",
            "who drew the picture up to\x01",
            "here while influencing all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12PHey now...are you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FI too have a small feeling like\x01",
            "it smells of a conspiracy theory...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FIndeed... I feel like there is\x01",
            "a missing piece of the puzzle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_F0AD")
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
    Jump("loc_F114")

    label("loc_F0AD")


    ChrTalk(
        0x101,
        "#00008F#11P(Who in the world could be...?)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F114")

    ChrTalk(
        0x10A,
        "#00608F#6P#30W(...No way...no...)\x02",
    )

    CloseMessageWindow()

    label("loc_F114")

    Sleep(500)

    ChrTalk(
        0x27,
        (
            "#03404F#5PWell, I thought you would have been\x01",
            "able to ascertain about that, but...\x02\x03",
            "It appears that you too don't have\x01",
            "evidence, so let's leave it at that.\x02\x03",
            "#03402FThere is no time, so let us\x01",
            "get to our other business.\x02",
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
            "#11504FHm, it's simple.\x02\x03",
            "#11507FWe're thinking to give you a hand with the\x01",
            ""Orchis Tower Breaking Into Operation"!\x02",
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
        "#00011F#12PEEH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#12PHey now, isn't this too\x01",
            "much out of the blue!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PI understood the outline of\x01",
            "the incident and I have no\x01",
            "need to remain in Crossbell, but...\x02\x03",
            "Going away like this would make me\x01",
            "pursued by remorses just a little.\x02\x03",
            "#03400FIt should be depending on you\x01",
            "what will be of Crossbell, however...\x02\x03",
            "If you got trapped into a chronic deadlock,\x01",
            "it would be troublesome for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11504FIt would feel bad quitting just\x01",
            "before clearing "Pom!", right?\x02\x03",
            "#11502FWell, it's the same thing as that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00109FThe same thing you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211F...By the way, when\x01",
            "did you obtain a\x01",
            ""Pom!" account?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F63F")

    ChrTalk(
        0x105,
        (
            "#6P#10404FWell, if our fighting potential goes up, even\x01",
            "the operation success rate will increase too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F757")

    label("loc_F63F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F6CE")

    ChrTalk(
        0x10A,
        (
            "#6P#00606FHowever, it's true that if our fighting\x01",
            "potential goes up, the operation\x01",
            "success rate will increase too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F757")

    label("loc_F6CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F757")

    ChrTalk(
        0x106,
        (
            "#6P#10703FHowever, it's true that if our fighting\x01",
            "potential goes up, the operation\x01",
            "success rate could increase too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F757")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F7BE")

    ChrTalk(
        0x109,
        (
            "#6P#10108FIt's a little complicated, but...\x01",
            "It could be nice considering it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F870")

    label("loc_F7BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F818")

    ChrTalk(
        0x106,
        (
            "#6P#10708FIt could be all right if we\x01",
            "consulted with the Chief.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F870")

    label("loc_F818")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F870")

    ChrTalk(
        0x10A,
        (
            "#6P#00601FI could be considerable if we\x01",
            "consulted with Mr. Sergei.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F870")


    ChrTalk(
        0x101,
        (
            "#00006F#12P...I understand.\x02\x03",
            "#00000FWe'll guide you to our base,\x01",
            "so please, follow us.\x02",
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
            "Afterwards, Lloyd and friends introduced\x01",
            "Kilika and Lechter to Chief Sergei...\x02\x03",
            "After exchanging intel with each other, it was \x01",
            "decided they would be helping with the operation.\x02\x03",
            "Then, Orchis Tower hacking\x01",
            "by Chief Roberts was finally\x01",
            "successful and...\x02\x03",
            "The "Orchis Tower Breaking Into Operation"\x01",
            "was decided to be carried out immediately.\x07\x00\x02",
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

    # Function_43_CE59 end

    def Function_44_FA5B(): pass

    label("Function_44_FA5B")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FBA9")
    SetChrPos(0x102, 280, 0, -7500, 0)
    Jump("loc_FC3C")

    label("loc_FBA9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FBCF")
    SetChrPos(0x103, 280, 0, -7500, 0)
    Jump("loc_FC3C")

    label("loc_FBCF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FBF5")
    SetChrPos(0x104, 280, 0, -7500, 0)
    Jump("loc_FC3C")

    label("loc_FBF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FC1B")
    SetChrPos(0x109, 280, 0, -7500, 0)
    Jump("loc_FC3C")

    label("loc_FC1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FC3C")
    SetChrPos(0x105, 280, 0, -7500, 0)

    label("loc_FC3C")

    SetChrPos(0x1A1, -90, 0, -8180, 0)
    SetChrChipByIndex(0x29, 0x1E)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, -40, 0, -3180, 0)

    def lambda_FC75():
        OP_95(0x29, -40, 0, 1990, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_FC75)
    SoundLoad(450)
    Sound(450, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "H-Hey, that old woman...\x01",
            "She came in from the roof, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Yes...\x01",
            "Who in the world is she?\x02",
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
            "#5SHmph, shut up!\x01",
            "It's not a show!!#3S\x02",
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

    def lambda_FE20():
        OP_95(0xFE, -420, 0, 150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FE20)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE64")

    def lambda_FE4A():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FE4A)
    Jump("loc_FF1B")

    label("loc_FE64")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE93")

    def lambda_FE79():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FE79)
    Jump("loc_FF1B")

    label("loc_FE93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FEC2")

    def lambda_FEA8():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FEA8)
    Jump("loc_FF1B")

    label("loc_FEC2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FEF1")

    def lambda_FED7():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FED7)
    Jump("loc_FF1B")

    label("loc_FEF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FF1B")

    def lambda_FF06():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FF06)

    label("loc_FF1B")


    def lambda_FF20():
        OP_95(0xFE, -90, 0, -1650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_FF20)
    WaitChrThread(0x1A1, 1)

    ChrTalk(
        0x29,
        "What...!!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        "#5SWhat persistent guys!#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        "#5SYou don't know when to quit!#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1008D")

    ChrTalk(
        0x102,
        (
            "#00106FHonestly, we should\x01",
            "be saying that...\x02\x03",
            "#00101F...You don't have anywhere to run.\x01",
            "Please surrender peacefully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102C5")

    label("loc_1008D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10123")

    ChrTalk(
        0x103,
        (
            "#00206FThose words...\x01",
            "I will return them to you.\x02\x03",
            "#00200FYou don't have anywhere to run...\x01",
            "Please, resign yourself already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102C5")

    label("loc_10123")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1019E")

    ChrTalk(
        0x104,
        (
            "#00306FRight back at you.\x02\x03",
            "#00302FWell, you haven't anywhere to run.\x01",
            "It's time to pay the piper.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102C5")

    label("loc_1019E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10234")

    ChrTalk(
        0x109,
        (
            "#10106FI-I feel like we should be\x01",
            "saying that to you...\x02\x03",
            "#10101F...Anyway.\x01",
            "Escaping is impossible.\x01",
            "Please surrender calmly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102C5")

    label("loc_10234")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_102C5")

    ChrTalk(
        0x105,
        (
            "#10306FOh boy, I don't want to be told\x01",
            "that from you, madame.\x02\x03",
            "#10302FWhat about considering to\x01",
            "calm down for your sake...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102C5")


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
            "Hah...\x01",
            "And I was thinking what were you going to say...\x02",
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
            "Until this continent exists...\x01",
            "I can get away wherever\x01",
            "and whenever I want!!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x29, 0x0, 0x1F4)
    OP_95(0x29, 0, 0, 8290, 4000, 0x0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(200)

    def lambda_103D0():
        OP_95(0xFE, -10, 0, 10140, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_103D0)
    Sleep(200)

    def lambda_103ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_103ED)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FD-Damn it...\x01",
            "She makes no sense...!\x02\x03",
            "#00007FIn any case, let's chase her, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        "Waaaaaaaaait!\x02",
    )

    CloseMessageWindow()

    def lambda_10474():
        OP_95(0xFE, -420, 0, 10450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10474)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_104BB")

    def lambda_104A1():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_104A1)
    Jump("loc_10572")

    label("loc_104BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_104EA")

    def lambda_104D0():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_104D0)
    Jump("loc_10572")

    label("loc_104EA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10519")

    def lambda_104FF():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_104FF)
    Jump("loc_10572")

    label("loc_10519")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10548")

    def lambda_1052E():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1052E)
    Jump("loc_10572")

    label("loc_10548")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10572")

    def lambda_1055D():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1055D)

    label("loc_10572")

    Sleep(100)

    def lambda_1057A():
        OP_95(0xFE, -90, 0, 10050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_1057A)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1069F")
    SetChrPos(0x102, 130, 0, -6140, 0)
    Jump("loc_10732")

    label("loc_1069F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106C5")
    SetChrPos(0x103, 130, 0, -6140, 0)
    Jump("loc_10732")

    label("loc_106C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106EB")
    SetChrPos(0x104, 130, 0, -6140, 0)
    Jump("loc_10732")

    label("loc_106EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10711")
    SetChrPos(0x109, 130, 0, -6140, 0)
    Jump("loc_10732")

    label("loc_10711")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10732")
    SetChrPos(0x105, 130, 0, -6140, 0)

    label("loc_10732")

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
            "The train has started to move...\x01",
            "It seems that we can finally take a breather.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2B,
        "Man",
        (
            "Yeah...\x01",
            "With this, it's goodbye to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2B,
        "Man",
        (
            "I feel bad towards our comrades\x01",
            "who were caught by Heiyue, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2C,
        "Man",
        (
            "What, it just means that we\x01",
            "lacked in preparations.\x02",
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
            "Ooh...it seems you're having\x01",
            "a funny conversation, eh?\x02",
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

    def lambda_10A45():
        OP_95(0xFE, 30, 0, 1880, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_10A45)

    def lambda_10A5F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_10A5F)
    Sleep(600)

    def lambda_10A73():
        OP_95(0xFE, -110, 0, 2990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_10A73)

    def lambda_10A8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_10A8D)
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
        (
            "Ah...aah...\x01",
            "You're...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2B,
        "Man",
        "Heiyue...!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x2C,
        "Man",
        (
            "C-Crap...\x01",
            "You put a tail on us...!?\x02",
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
            "Anti-Eastern Immigration Leaugue gentlemen...\x01",
            "You'll have to come with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "As soon as we reach Altair City,\x01",
            "we'll transfer to a Crossbell\x01",
            "bound train.\x02",
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
        "──Move aside, you brats!\x02",
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

    def lambda_10CCA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_10CCA)
    Sleep(50)

    def lambda_10CDA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_10CDA)

    ChrTalk(
        0x2D,
        "Huh...\x02",
    )

    CloseMessageWindow()

    def lambda_10CF3():
        OP_95(0xFE, 10, 0, 2460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_10CF3)
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
            "Ow ow ow...\x01",
            "Damn blockheads, didn't\x01",
            "I tell you to move!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "I can't stay still\x01",
            "in such a place!!\x02",
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
        "(E-Eeehm...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "(Who's this granny?)\x02",
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
            "Could it be that you were...\x01",
            "Chased by these guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "Y-Yeah...\x01",
            "Honestly, you've helped us.\x02",
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
        "Hmph, I don't get it, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "...To oppose those guys, I need\x01",
            "as many comrades as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        (
            "#5SYou guys! If you feel \x01",
            "indebted  even just a little,\x01",
            "then come with me!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        (
            "#5SIf it goes well,\x01",
            "you could be able\x01",
            "to get away too!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "E-EEH...!?\x02",
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
        "A-All right!!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_110C5")
    BeginChrThread(0x102, 1, 0, 47)
    Jump("loc_1112C")

    label("loc_110C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_110E0")
    BeginChrThread(0x103, 1, 0, 47)
    Jump("loc_1112C")

    label("loc_110E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_110FB")
    BeginChrThread(0x104, 1, 0, 47)
    Jump("loc_1112C")

    label("loc_110FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11116")
    BeginChrThread(0x109, 1, 0, 47)
    Jump("loc_1112C")

    label("loc_11116")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1112C")
    BeginChrThread(0x105, 1, 0, 47)

    label("loc_1112C")

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
        "Kh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "W-What the heck happened...\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11263")
    SetChrPos(0x102, -650, 0, -8160, 0)
    Jump("loc_112F6")

    label("loc_11263")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11289")
    SetChrPos(0x103, -650, 0, -8160, 0)
    Jump("loc_112F6")

    label("loc_11289")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112AF")
    SetChrPos(0x104, -650, 0, -8160, 0)
    Jump("loc_112F6")

    label("loc_112AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112D5")
    SetChrPos(0x109, -650, 0, -8160, 0)
    Jump("loc_112F6")

    label("loc_112D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112F6")
    SetChrPos(0x105, -650, 0, -8160, 0)

    label("loc_112F6")

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
            "I-It seems she's climbed\x01",
            "on the roof again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FBy the way, it looked\x01",
            "like she had someone\x01",
            "following her...\x02\x03",
            "#00001FDid she have some \x01",
            "comrades in hiding!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "B-But that's impossible...\x01",
            "All of her underlings should've\x01",
            "been arrested a long time ago!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_115BB")

    ChrTalk(
        0x102,
        (
            "#00101FA-At any rate...\x01",
            "Let's follow them now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11718")

    label("loc_115BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11602")

    ChrTalk(
        0x103,
        (
            "#00201FAt any rate...\x01",
            "Let's follow them now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11718")

    label("loc_11602")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1165E")

    ChrTalk(
        0x104,
        (
            "#00301FTsk, I don't really get it, but...\x01",
            "Let's go after 'em now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11718")

    label("loc_1165E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_116B5")

    ChrTalk(
        0x109,
        (
            "#10101FI-I don't get it well, but...\x01",
            "Let's chase after them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11718")

    label("loc_116B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11718")

    ChrTalk(
        0x105,
        (
            "#10302FAt any rate, it's not ok\x01",
            "to let them go, right?\x01",
            "Let's follow them now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11718")


    ChrTalk(
        0x101,
        (
            "#00003FY-You're right.\x02\x03",
            "#00001F──Fine, let's resume the pursuit!\x02",
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

    # Function_44_FA5B end

    def Function_45_1177E(): pass

    label("Function_45_1177E")

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

    # Function_45_1177E end

    def Function_46_117DA(): pass

    label("Function_46_117DA")

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

    # Function_46_117DA end

    def Function_47_11830(): pass

    label("Function_47_11830")

    OP_95(0xFE, 0, 0, 8350, 4000, 0x0)

    def lambda_11849():
        OP_95(0xFE, 0, 0, 10000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11849)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_47_11830 end

    def Function_48_1186A(): pass

    label("Function_48_1186A")

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

    # Function_48_1186A end

    def Function_49_118C1(): pass

    label("Function_49_118C1")

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

    # Function_49_118C1 end

    def Function_50_11918(): pass

    label("Function_50_11918")

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

    # Function_50_11918 end

    SaveToFile()

Try(main)
