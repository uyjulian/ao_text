from ScenarioHelper import *

def main():
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
        "Old man",                   # 1
        "merchant",                   # 2
        "father",                     # 3
        "girl",                 # 4
        "Adolescents",                   # 5
        "sister",                     # 6
        "Brother",                     # 7
        "Director",                 # 8
        "Singh",                   # 9
        "Daughter",                     # 10
        "Woman",                   # 11
        "rope",                 # 12
        "dummy",                 # 13
        "passenger",                   # 14
        "passenger",                   # 15
        "passenger",                   # 16
        "passenger",                   # 17
        "passenger",                   # 18
        "passenger",                   # 19
        "passenger",                   # 20
        "passenger",                   # 21
        "passenger",                   # 22
        "passenger",                   # 23
        "passenger",                   # 24
        "passenger",                   # 25
        "A hunter",                   # 26
        "A hunter",                   # 27
        "A hunter",                   # 28
        "A hunter",                   # 29
        "A hunter",                   # 30
        "A hunter",                   # 31
        "Kirika",                 # 32
        "Rector",               # 33
        "Fake brand quotient",           # 34
        "Republic-based terrorists",     # 35
        "Republic-based terrorists",     # 36
        "Republic-based terrorists",     # 37
        "Black moon member",             # 38
        "Black moon member",             # 39
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
        "Function_4_D09",          # 04, 4
        "Function_5_D8E",          # 05, 5
        "Function_6_E3E",          # 06, 6
        "Function_7_EAF",          # 07, 7
        "Function_8_F2C",          # 08, 8
        "Function_9_F91",          # 09, 9
        "Function_10_FE5",         # 0A, 10
        "Function_11_1104",        # 0B, 11
        "Function_12_1216",        # 0C, 12
        "Function_13_129B",        # 0D, 13
        "Function_14_1310",        # 0E, 14
        "Function_15_2223",        # 0F, 15
        "Function_16_225C",        # 10, 16
        "Function_17_45B8",        # 11, 17
        "Function_18_4D5B",        # 12, 18
        "Function_19_5028",        # 13, 19
        "Function_20_50E4",        # 14, 20
        "Function_21_5149",        # 15, 21
        "Function_22_51AE",        # 16, 22
        "Function_23_5680",        # 17, 23
        "Function_24_5BD9",        # 18, 24
        "Function_25_60E4",        # 19, 25
        "Function_26_67A1",        # 1A, 26
        "Function_27_67AA",        # 1B, 27
        "Function_28_6CCD",        # 1C, 28
        "Function_29_70C8",        # 1D, 29
        "Function_30_8006",        # 1E, 30
        "Function_31_88EB",        # 1F, 31
        "Function_32_8D66",        # 20, 32
        "Function_33_9D47",        # 21, 33
        "Function_34_9FF7",        # 22, 34
        "Function_35_BF66",        # 23, 35
        "Function_36_BFB0",        # 24, 36
        "Function_37_BFFA",        # 25, 37
        "Function_38_C031",        # 26, 38
        "Function_39_C06B",        # 27, 39
        "Function_40_C0A5",        # 28, 40
        "Function_41_C0DF",        # 29, 41
        "Function_42_C119",        # 2A, 42
        "Function_43_C153",        # 2B, 43
        "Function_44_E84A",        # 2C, 44
        "Function_45_104C2",       # 2D, 45
        "Function_46_1051E",       # 2E, 46
        "Function_47_10574",       # 2F, 47
        "Function_48_105AE",       # 30, 48
        "Function_49_10605",       # 31, 49
        "Function_50_1065C",       # 32, 50
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_END)), "loc_CEA")

    ChrTalk(
        0xFE,
        (
            "Well, sorry,\x01",
            "Wait a moment and do not worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There must be absolutely tickets.\x01",
            "I will definitely search and see!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D05")

    label("loc_CEA")

    Call(0, 25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D05")
    Call(0, 26)

    label("loc_D05")

    TalkEnd(0xFE)
    Return()

    # Function_3_C65 end

    def Function_4_D09(): pass

    label("Function_4_D09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_END)), "loc_D6F")

    ChrTalk(
        0xFE,
        (
            "If this deal is settled\x01",
            "It is a mistake mistake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Muffu, you can not help it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8A")

    label("loc_D6F")

    Call(0, 24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8A")
    Call(0, 26)

    label("loc_D8A")

    TalkEnd(0xFE)
    Return()

    # Function_4_D09 end

    def Function_5_D8E(): pass

    label("Function_5_D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_END)), "loc_E22")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Today is the future\x01",
            "To parents in the Republic\x01",
            "Go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My daughter for the first time in a long time\x01",
            "As I see grandparents\x01",
            "You seem to be very happy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_E3D")

    label("loc_E22")

    Call(0, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3D")
    Call(0, 26)

    label("loc_E3D")

    Return()

    # Function_5_D8E end

    def Function_6_E3E(): pass

    label("Function_6_E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_END)), "loc_E93")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Grandpa, grandma,\x01",
            "I'm waiting for you to go from now ♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_EAE")

    label("loc_E93")

    Call(0, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EAE")
    Call(0, 26)

    label("loc_EAE")

    Return()

    # Function_6_E3E end

    def Function_7_EAF(): pass

    label("Function_7_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_END)), "loc_F10")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "From now on,\x01",
            "I am going home to Oled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Mother is fine.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_F2B")

    label("loc_F10")

    Call(0, 22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2B")
    Call(0, 26)

    label("loc_F2B")

    Return()

    # Function_7_EAF end

    def Function_8_F2C(): pass

    label("Function_8_F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_END)), "loc_F75")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Already, about your older brother\x01",
            "I do not know it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_F90")

    label("loc_F75")

    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F90")
    Call(0, 31)

    label("loc_F90")

    Return()

    # Function_8_F2C end

    def Function_9_F91(): pass

    label("Function_9_F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_END)), "loc_FC9")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Fuu, you are a very cute little sister.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_FE4")

    label("loc_FC9")

    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE4")
    Call(0, 31)

    label("loc_FE4")

    Return()

    # Function_9_F91 end

    def Function_10_FE5(): pass

    label("Function_10_FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_END)), "loc_10E8")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1095")

    ChrTalk(
        0xFE,
        (
            "Hehu, apparently this trip\x01",
            "It is quite meaningful for Mr. Sin\x01",
            "You seem to have become something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is also thanks to everyone.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E0")

    label("loc_1095")


    ChrTalk(
        0xFE,
        (
            "Hmm, I am cheerful today.\x01",
            "It is good weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, it is a perfect train weather.\x02",
    )

    CloseMessageWindow()

    label("loc_10E0")

    TalkEnd(0xFE)
    Jump("loc_1103")

    label("loc_10E8")

    Call(0, 29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1103")
    Call(0, 31)

    label("loc_1103")

    Return()

    # Function_10_FE5 end

    def Function_11_1104(): pass

    label("Function_11_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_END)), "loc_11FA")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1181")

    ChrTalk(
        0xFE,
        (
            "Tentatively,\x01",
            "I'm surely someday again\x01",
            "I will come to the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… It is farewell until that time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11F2")

    label("loc_1181")


    NpcTalk(
        0xFE,
        "boy",
        "What, still there is something for you?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "boy",
        (
            "I am busy, I'm busy.\x01",
            "Do not call out to us unnecessarily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F2")

    TalkEnd(0xFE)
    Jump("loc_1215")

    label("loc_11FA")

    Call(0, 29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1215")
    Call(0, 31)

    label("loc_1215")

    Return()

    # Function_11_1104 end

    def Function_12_1216(): pass

    label("Function_12_1216")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_END)), "loc_127C")

    ChrTalk(
        0xFE,
        (
            "Grumbling ……\x01",
            "How long does it take to leave?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I have regrets … ___ ___ 0\x02",
    )

    CloseMessageWindow()
    Jump("loc_1297")

    label("loc_127C")

    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1297")
    Call(0, 31)

    label("loc_1297")

    TalkEnd(0xFE)
    Return()

    # Function_12_1216 end

    def Function_13_129B(): pass

    label("Function_13_129B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_END)), "loc_12F1")

    ChrTalk(
        0xFE,
        (
            "What do you do, no more?\x01",
            "If it is you, please go early.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_130C")

    label("loc_12F1")

    Call(0, 27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_130C")
    Call(0, 31)

    label("loc_130C")

    TalkEnd(0xFE)
    Return()

    # Function_13_129B end

    def Function_14_1310(): pass

    label("Function_14_1310")

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
    SetChrName("Sergeant Noel")

    AnonymousTalk(
        0xFF,
        (
            "Fu … … but safely\x01",
            "I am glad that my duties have been settled.\x02\x03",
            "To be honest, I will pull my legs\x01",
            "I did not know what to do.\x02",
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
            "#6P#00002FHaha, I'm worried.\x02\x03",
            "#00004FSonja commander\x01",
            "Because I thought that she was prospective\x01",
            "I guess it was recommended.\x02\x03",
            "#00000FAnyway, from now on\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x109,
        "Sergeant Noel",
        (
            "#10109F#11PYes, this is it!\x02\x03",
            "#10105FAh, but Lloyd.\x01",
            "Is it OK for a moment?\x02",
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
        "Sergeant Noel",
        (
            "#10106F#11PFor the time being,\x01",
            "I will be indebted to the official … …\x02\x03",
            "#10102FBecause I am not wearing military uniforms either\x01",
            "That \"Chief\" is kinda … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FOh, oh, is that so?\x02\x03",
            "#00000FBut what shall we do?\x01",
            "Do you mind if I ask you to abandon it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x109,
        "Sergeant Noel",
        "#10109F#11PYes, that is fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FThen then Noel ─ ─\x01",
            "Thank you again.\x02\x03",
            "#00002FYes, if you like it too\x01",
            "Go to Frank more.\x02\x03",
            "I am the same age and I am a colleague\x01",
            "I do not want to mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10111F#11PHuh!?\x01",
            "I do not care about Mr. Lloyd! Is it?\x02\x03",
            "#10106F….\x01",
            "Impossible impossible, that's impossible!\x02\x03",
            "#10101FTo the end as a policeman is a brand new,\x01",
            "Because I'm in the status to study!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FNo, it's so hard\x01",
            "I do not think that … …\x02\x03",
            "#00000FErie and Randy\x01",
            "It is a tame mouth without age difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PNo, that … …\x01",
            "Something like sex … …\x02\x03",
            "Once you assume that\x01",
            "I wonder if I can not change it easily ……\x02\x03",
            "#10101FBut if Lloyd says so\x01",
            "Work somehow and get in a mouth ─ ─!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FNo.\x01",
            "Because you do not have to push yourself.\x02\x03",
            "#00002Fmy mother……\x01",
            "It is a spiritual athlete's disposition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PHaha ……\x01",
            "It may be influence of my father.\x02\x03",
            "#10100FIt's a tough person, and I and Fran\x01",
            "Because I was disciplined when I was small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FOh, my father 's.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FWell, to your mother\x01",
            "I have met several times … but …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PMy father……\x01",
            "He died about ten years ago.\x02\x03",
            "#10100FI belong to the Crossbell Guard,\x01",
            "That, in the accident under duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F………I see.\x01",
            "I heard bad things.\x02\x03",
            "#00001FPossibly …\x01",
            "Did you also enter the guard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#11PHow is that …?\x01",
            "I have never realized so much.\x02\x03",
            "#10104FBut like my father\x01",
            "I wanted to protect the land called Crossbell\x01",
            "It may be certain.\x02\x03",
            "#10100FIn that sense, even though the affiliation is different\x01",
            "Francs may be the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FI see……\x02",
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
        "#6P#00008F…………………….\x02",
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
            "#6P#00004FSorry, nothing.\x02\x03",
            "#00002F─ ─ But you came\x01",
            "This was really saved.\x02\x03",
            "There are things that I am short of hands\x01",
            "…… What will happen in the future\x01",
            "Honestly I can not predict it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#11PHaha, if you say so\x01",
            "I'm honored, but ….\x02\x03",
            "#10102FBut, when the mafia is gone\x01",
            "The public security in the city was also improved, right?\x02\x03",
            "\"Black moon#4RHayuue#\"Remains but\x01",
            "There seems to be no noticeable movement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F… … on the surface.\x02\x03",
            "#00008FHowever, one thing can be said\x01",
            "The organization \"Rubache\"\x01",
            "It has played a certain role.\x02\x03",
            "#00001FIn the sense of protecting the security of Crossbell.\x02",
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

    # Function_14_1310 end

    def Function_15_2223(): pass

    label("Function_15_2223")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_225B")
    OP_82(0xA, 0xA, 0x5DC, 0x2EE)
    Sleep(3500)
    OP_82(0xA, 0xA, 0x4B0, 0x1F4)
    Sleep(3500)
    Jump("Function_15_2223")

    label("loc_225B")

    Return()

    # Function_15_2223 end

    def Function_16_225C(): pass

    label("Function_16_225C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2351")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆ Partially Achievements Achievement of a bond with Eli\x01",      # 0
            "◆ First part achievement Tied with Tio Achieved\x01",      # 1
            "◆ The first part achievement Randy's bonds achieved\x01",      # 2
            "◆ Partial achievements All members' bonds achieved\x01",          # 3
            "◆ Do not change\x01",                      # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2326"),
        (1, "loc_232E"),
        (2, "loc_2336"),
        (3, "loc_233E"),
        (4, "loc_234C"),
        (SWITCH_DEFAULT, "loc_234C"),
    )


    label("loc_2326")

    SetScenarioFlags(0x25, 3)
    Jump("loc_2351")

    label("loc_232E")

    SetScenarioFlags(0x25, 4)
    Jump("loc_2351")

    label("loc_2336")

    SetScenarioFlags(0x25, 5)
    Jump("loc_2351")

    label("loc_233E")

    SetScenarioFlags(0x25, 3)
    SetScenarioFlags(0x25, 4)
    SetScenarioFlags(0x25, 5)
    Jump("loc_2351")

    label("loc_234C")

    Jump("loc_2351")

    label("loc_2351")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_241E")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis224.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_241E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_2461")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis225.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_24A4")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis226.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24A4")

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
            "#10105FMafia is crossbell\x01",
            "I kept security … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, as a result, though.\x02\x03",
            "#00001F…… Crossbell is placed\x01",
            "Think about a special situation.\x02\x03",
            "Even with autonomy\x01",
            "As a nation, it is not independent,\x01",
            "We are constantly receiving interference from the two major powers.\x02\x03",
            "Laws that crack down on crime are full of holes\x01",
            "There are almost no entry restrictions … …\x02\x03",
            "#00003FOriginally, rather than black moon\x01",
            "Other criminal organizations and terrorists\x01",
            "Domination#4RA bracket#It is a strange place to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FAh……\x02\x03",
            "… Well then until now\x01",
            "The role of Rubatche to suppress it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FI do not want to admit it ….\x01",
            "As a result a certain order to the back society\x01",
            "I can not deny having brought it.\x02\x03",
            "#00006F…… It has nothing to foresee\x01",
            "In the form of being involved in disaster called \"cult\"\x01",
            "It has disappeared …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108FIs the collapse of the power balance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh……\x01",
            "Imperialists and republican lawmakers\x01",
            "The same can be said for the case that we have lost control.\x02\x03",
            "As the spokesperson no longer exists\x01",
            "On the contrary, the pressure from both countries is more than ever\x01",
            "The possibility of becoming blatant will be high.\x02\x03",
            "#00013F── That's why the new mayor\x01",
            "Support Section#6RUs#I think that I am expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FI see……\x01",
            "I finally agreed.\x02\x03",
            "#10100FElly and Randy seniors,\x01",
            "Tio is temporarily away as well\x01",
            "That was the reason, was not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, before a new aspect\x01",
            "As much as possible in cooperation with each side\x01",
            "Ensure more sophisticated activities.\x02\x03",
            "I also let me train in one lesson\x01",
            "I knocked down a lot of things ……\x02\x03",
            "#00002FFurthermore, because there was not enough manpower\x01",
            "I also requested a new strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHehu ……\x01",
            "I am honored to call you.\x02",
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
        "#12P#10105FBut, by the way, …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PWhat's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FAnother new member is\x01",
            "He 's met before, is not he?\x02\x03",
            "To be honest, I was surprised\x01",
            "What is the background?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#5POh ─ ─ \"He\".\x02\x03",
            "#00006FNo, I need new people\x01",
            "To the arrowhead we started looking for\x01",
            "Please visit this place.\x02\x03",
            "Nomination from the new Mayor as well\x01",
            "I've been installing it.\x01",
            "I could not refuse to refuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10111FThen, is the recommendation of the mayor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5POh, to the crisis of the IBC building\x01",
            "In exchange for a reward for lending\x01",
            "It seems that she got a letter of recommendation.\x02\x03",
            "#00006F… … Firstly, the Special Affairs Division\x01",
            "I'm looking for a new member\x01",
            "Where did you hear it?\x02\x03",
            "The person himself / herself said \"It looks interesting\"\x01",
            "I was saying that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FEr …\x01",
            "Is that okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PWell, well ….\x01",
            "It is certain that it is not a bad person.\x02\x03",
            "#00002FWell, history is unknown,\x01",
            "It is familiar to the underlying society,\x01",
            "I am doing a host, though.\x02\x03",
            "#00006F… … What are you talking about?\x01",
            "It has become increasingly uneasy.\x02",
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
            "#12P#10112FThat's fine.\x02\x03",
            "#10102FMy mouth is bad though it's definitely sarcastic\x01",
            "I did not seem to be a bad girl … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5Pmy mother……\x01",
            "I will be saved if you say so.\x02\x03",
            "#00002FTo be honest, Sori is with you\x01",
            "Because I thought it would not fit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FWell, hmm … ….\x01",
            "Certainly I was also made fun of\x01",
            "I did it … ….\x02\x03",
            "#10100FIf anything\x01",
            "It is better for you to play Mr. Lloyd\x01",
            "He seems to be enjoyable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PUg ……\x01",
            "I'd like you to forgive me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FHaha ……\x01",
            "(The franc was making noise\x01",
            "Is it better not to say? )\x02",
        )
    )

    CloseMessageWindow()
    Sound(800, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice of conductor")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── We will tell passengers.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Soon, Crossbell Autonomous Region,\x01",
            "I will arrive at Cros Bell City.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To Libert and Remiferia\x01",
            "Customers using a regular airship\x01",
            "Please change.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Based on the Continental Railroad Corporation Agreement,\x01",
            "The train at Crossbell station\x01",
            "I will stop for about 30 minutes.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Those who head to Erebonia\x01",
            "Fill in your immigration application form,\x01",
            "Please submit to the inspector.\x07\x00\x02",
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
            "#00002F#5PBecause it is only one station\x01",
            "It was a blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10104FYeah ….\x02\x03",
            "#10102FStill a few days, if you are out\x01",
            "I feel somewhat nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PThat's right.\x02",
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
            "#00004F#5P(…… All of them are complete\x01",
            "After a little more … …)\x02\x03",
            "#00002F(Keya …\x01",
            "I hope not to be lonely. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3694")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWho did you speak with at the IBC Building 16F in the evening of a cult incident?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_35D6")
    MenuCmd(1, 0, "【Erie】")

    label("loc_35D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_35ED")
    MenuCmd(1, 0, "[Tio]")

    label("loc_35ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_3606")
    MenuCmd(1, 0, "【Randy】")

    label("loc_3606")

    MenuCmd(2, 0, -1, 100, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3644"),
        (1, "loc_365D"),
        (2, "loc_3687"),
        (SWITCH_DEFAULT, "loc_368F"),
    )


    label("loc_3644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3655")
    SetScenarioFlags(0x121, 2)
    Jump("loc_3658")

    label("loc_3655")

    SetScenarioFlags(0x121, 3)

    label("loc_3658")

    Jump("loc_368F")

    label("loc_365D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_367F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_3677")
    SetScenarioFlags(0x121, 3)
    Jump("loc_367A")

    label("loc_3677")

    SetScenarioFlags(0x121, 4)

    label("loc_367A")

    Jump("loc_3682")

    label("loc_367F")

    SetScenarioFlags(0x121, 4)

    label("loc_3682")

    Jump("loc_368F")

    label("loc_3687")

    SetScenarioFlags(0x121, 4)
    Jump("loc_368F")

    label("loc_368F")

    Jump("loc_36C2")

    label("loc_3694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_36A5")
    SetScenarioFlags(0x121, 2)
    Jump("loc_36C2")

    label("loc_36A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_36B6")
    SetScenarioFlags(0x121, 3)
    Jump("loc_36C2")

    label("loc_36B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_36C2")
    SetScenarioFlags(0x121, 4)

    label("loc_36C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 2)), scpexpr(EXPR_END)), "loc_3B20")
    Sleep(300)

    ChrTalk(
        0x101,
        "#00004F#5P(in addition……)\x02",
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
        "Erie",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00112F#N#11P……Let me see……\x01",
            "I will return to the bell.\x02\x03",
            "#00113FTo some uncle sama\x01",
            "I may be able to cooperate\x01",
            "Because it may not be ……\x02",
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
            "#00004FOh, ah ……\x01",
            "I will supply with you as well.\x01",
            "I will check the equipment.\x02\x03",
            "#00002F… … Also, later.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x15,
        "Erie",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00102F#N#11PYeah ….\x02\x03",
            "#00113F…… That, the continuation of the moment ago,\x01",
            "Even after solving all … …\x02",
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
        "Erie",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00112F#N#11PNothing, nothing.\x02\x03",
            "#00109FWell then, see you later!\x07\x00\x02",
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
            "#00004F#5P(… … I have been busy with each other since then\x01",
            "I have not made much progress though … …)\x02\x03",
            "(When Ellie comes back\x01",
            "Somehow managed to continue at that time ─ ─)\x02\x03",
            "#00011F(No no, it is not a continuation!\x01",
            "I have to think more seriously … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100F…… Lloyd?\x02",
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
            "#00011F#5PNo, that is nothing!\x02\x03",
            "#00012FEven so, I am tired!\x01",
            "I would like to take a day off on the sofa of the support department soon!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x109,
        "#12P#10105F(Lloyd's reaction is suspicious … …)\x02",
    )

    CloseMessageWindow()
    Jump("loc_453D")

    label("loc_3B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_3FC6")
    Sleep(300)

    ChrTalk(
        0x101,
        "#00004F#5P(in addition……)\x02",
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
            "#00204F#N#11P…… Michelin theme park.\x02\x03",
            "If this turmoil resolved successfully\x01",
            "Please take me over there.\x02",
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
            "#00011FWell …\x01",
            "Is that okay with you! Is it?\x02\x03",
            "#00001FNo, but …\x01",
            "A little more serious\x01",
            "Is not it better to promise?\x02\x03",
            "When Tio is in trouble\x01",
            "Even if there is anything going to help.\x07\x00\x02",
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
            "#00204F#N#11PNo, this is enough.\x02\x03",
            "#00208FBesides, we must solve this situation\x01",
            "This promise can not be fulfilled …\x02\x03",
            "#00202FIn that sense,\x01",
            "It might be serious.\x07\x00\x02",
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
            "#00004F#5P(… … I have been busy with each other since then\x01",
            "I have not been to play yet ….)\x02\x03",
            "(When Tio comes back\x01",
            "I absolutely must keep that promise. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105F…… Lloyd?\x02",
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
            "#00005F#5POh, sorry.\x02\x03",
            "#00000F…… That reminds me Noel\x01",
            "Have you been to a theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FIs it Michelin?\x01",
            "Yeah, before the franc and only once.\x02\x03",
            "#10109FThe attraction is interesting, though\x01",
            "Missi is cute, is not it ~!\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x109, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#5PIs that so … ….\x01",
            "(It is extremely popular, Missi.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_453D")

    label("loc_3FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_453D")
    Sleep(300)

    ChrTalk(
        0x101,
        "#00004F#5P(in addition……)\x02",
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
            "#00303F#N#11P──When the guard rushes\x01",
            "It will be us who can move to the end.\x02\x03",
            "#00300FMiss and Tio are in\x01",
            "I do not want to make it unreasonable.\x02",
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
            "#00004F…… Oh, I know.\x02\x03",
            "#00000FWith me and Randy\x01",
            "I need to stop eating somehow.\x02",
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
            "#00302F#N#11PThat's it.\x02\x03",
            "#00309FI left the back to you - a buddy.\x07\x00\x02",
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
            "#00005FAh……\x02\x03",
            "#00002F── Okay!\x07\x00\x02",
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
            "#00008F#5P(Aibo? …)\x02\x03",
            "#00003F(Honestly, there is still a balance as a man\x01",
            "I do not think that it is taken away. )\x02\x03",
            "#00000F(I really wanted to line up my shoulders.\x01",
            "I have to work harder … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105F…… Lloyd?\x02",
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
            "#00005F#5POh, sorry.\x02\x03",
            "#00000FBy the way, from the eyes of Noel\x01",
            "How about Randy?\x02\x03",
            "Rather than being a policeman,\x01",
            "As a security guard ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FAre you Randy-senpai?\x02\x03",
            "#10104FI agree……\x01",
            "After all it feels unusual.\x02\x03",
            "#10100FOf course the fighting power of individuals is, of course,\x01",
            "Tactical level tactics as well\x01",
            "I heard that it is quite amazing … ….\x02\x03",
            "Even in rehabilitation training I am doing now\x01",
            "It seems you are skipping a lot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PI see……\x02\x03",
            "#00008F(… … Randy,\x01",
            "The rifle with this training\x01",
            "I was saying to use it … …)\x02\x03",
            "(A bit about the hunting era\x01",
            "I wonder if it was blown out …? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_453D")

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

    # Function_16_225C end

    def Function_17_45B8(): pass

    label("Function_17_45B8")

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

    # Function_17_45B8 end

    def Function_18_4D5B(): pass

    label("Function_18_4D5B")

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
            "#00004FWell, our responsibilities are\x01",
            "Two in the back half.\x02\x03",
            "#00001FThe passengers ……\x01",
            "It looks pretty good.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EBC")

    ChrTalk(
        0x102,
        (
            "#00100FLooks like, every single person\x01",
            "Let's check thoroughly.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x0)
    Jump("loc_5021")

    label("loc_4EBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F1F")

    ChrTalk(
        0x103,
        (
            "#00200FAnyway, in order from the end\x01",
            "Let's definitely end it.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x1)
    Jump("loc_5021")

    label("loc_4F1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F74")

    ChrTalk(
        0x104,
        (
            "#00304FWell, anyway\x01",
            "You only have to hit it from one end.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x2)
    Jump("loc_5021")

    label("loc_4F74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FCD")

    ChrTalk(
        0x109,
        (
            "#10100FYes, certainly anyway\x01",
            "Let's finish the check.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x3)
    Jump("loc_5021")

    label("loc_4FCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5021")

    ChrTalk(
        0x105,
        (
            "#10300FFuh, anyway from the edge\x01",
            "It seems to only crush it.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x4)

    label("loc_5021")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_4D5B end

    def Function_19_5028(): pass

    label("Function_19_5028")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5081")

    ChrTalk(
        0x101,
        (
            "#00003F…… This is the third pair.\x01",
            "Let's investigate all four passengers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50CD")

    label("loc_5081")


    ChrTalk(
        0x101,
        (
            "#00003F…… The previous car is out of charge of us.\x01",
            "Let's focus on the inspection of the place now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50CD")

    Sleep(50)
    SetChrPos(0x0, -10, 0, 7470, 180)
    EventEnd(0x4)
    Return()

    # Function_19_5028 end

    def Function_20_50E4(): pass

    label("Function_20_50E4")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F…… The examination has not ended yet.\x01",
            "I can not get out of the train.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)
    Return()

    # Function_20_50E4 end

    def Function_21_5149(): pass

    label("Function_21_5149")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F…… The examination has not ended yet.\x01",
            "I can not get out of the train.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, 7850, 270)
    EventEnd(0x4)
    Return()

    # Function_21_5149 end

    def Function_22_51AE(): pass

    label("Function_22_51AE")

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
            "#00000FExcuse me,\x01",
            "He is an assistant adviser.\x02\x03",
            "Sorry to trouble you,\x01",
            "Baggage and immigration application form\x01",
            "Could you confirm it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…… Mother …………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52D9")

    ChrTalk(
        0x102,
        (
            "#00105FApparently,\x01",
            "It sounds like your voice has not arrived. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5401")

    label("loc_52D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5328")

    ChrTalk(
        0x103,
        (
            "#00205FApparently,\x01",
            "It seems that your voice has not arrived. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5401")

    label("loc_5328")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5366")

    ChrTalk(
        0x104,
        "#00305F(Hmm, do not get into my ears.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5401")

    label("loc_5366")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53B5")

    ChrTalk(
        0x109,
        (
            "#10105FEr …\x01",
            "It seems that your voice has not arrived. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5401")

    label("loc_53B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5401")

    ChrTalk(
        0x105,
        (
            "#10302F(Huh, apparently.\x01",
            "You do not seem to hear it. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5401")


    ChrTalk(
        0x101,
        "#00006F#4SExcuse me--\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54CB")
    Jump("loc_5515")

    label("loc_54CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54EB")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5515")

    label("loc_54EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_550B")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5515")

    label("loc_550B")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5515")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        "Oh, ah … I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I was a bit scared.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, are you a person in charge?\x01",
            "Those who check it, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, soon -\x02",
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
            "#00004F- Baggage and immigration application form both\x01",
            "confirmed.\x01",
            "Thanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, you are welcome.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 4)
    OP_29(0x79, 0x1, 0x5)
    ClearChrFlags(0xC, 0x10)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_51AE end

    def Function_23_5680(): pass

    label("Function_23_5680")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5768")
    Jump("loc_57B2")

    label("loc_5768")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5788")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B2")

    label("loc_5788")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57A8")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B2")

    label("loc_57A8")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57B2")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5868")
    Jump("loc_58B2")

    label("loc_5868")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5888")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58B2")

    label("loc_5888")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58A8")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58B2")

    label("loc_58A8")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58B2")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FUm, I am a person who is assistant adviser.\x02\x03",
            "Sorry to trouble you,\x01",
            "Baggage and immigration application form\x01",
            "Could you confirm it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Rinken, Rinken ♪\x01",
            "Older brothers, thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, then.\x01",
            "I will have you look it up.\x02",
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
            "#00004F- Baggage and immigration application form both\x01",
            "confirmed.\x01",
            "Thanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What is it?\x01",
            "It's a matter of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Onii-chan\x01",
            "Good job your job ☆\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ACD")

    ChrTalk(
        0x102,
        "#00102FHehe, thank you very much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BBB")

    label("loc_5ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B12")

    ChrTalk(
        0x103,
        (
            "#00202FHuhu, thanks\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BBB")

    label("loc_5B12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B4C")

    ChrTalk(
        0x104,
        "#00309FThank you very much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BBB")

    label("loc_5B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B86")

    ChrTalk(
        0x109,
        "#10109FHehe, thank you very much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BBB")

    label("loc_5B86")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BBB")

    ChrTalk(
        0x105,
        "#10309FThank you very much.\x02",
    )

    CloseMessageWindow()

    label("loc_5BBB")

    SetScenarioFlags(0x1CA, 3)
    OP_29(0x79, 0x1, 0x6)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_5680 end

    def Function_24_5BD9(): pass

    label("Function_24_5BD9")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5CC1")
    Jump("loc_5D0B")

    label("loc_5CC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5CE1")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D0B")

    label("loc_5CE1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D01")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D0B")

    label("loc_5D01")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D0B")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "He is an assistant adviser.\x02\x03",
            "Sorry to trouble you,\x01",
            "Baggage and immigration application form\x01",
            "Could you confirm it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hehe, I was waiting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Come on, please check it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHaha …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E38")

    ChrTalk(
        0x102,
        "#00105F(The tension is badly high.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F3F")

    label("loc_5E38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E7C")

    ChrTalk(
        0x103,
        "#00200F(The tension is burning high, is not it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F3F")

    label("loc_5E7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EBE")

    ChrTalk(
        0x104,
        "#00306F(The tension is too high.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F3F")

    label("loc_5EBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F00")

    ChrTalk(
        0x109,
        "#10105F(Strangely, the tension is high.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F3F")

    label("loc_5F00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F3F")

    ChrTalk(
        0x105,
        "#10303F(Huh, you have a lot of tension.\x02",
    )

    CloseMessageWindow()

    label("loc_5F3F")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F- Baggage and immigration application form both\x01",
            "confirmed.\x01",
            "Thanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Muhuu, have you seen?\x01",
            "A bunch of this agreement!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Actually, I am going\x01",
            "In a place to head for a big big deal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it gathers up, the morning is sure -\x01",
            "Well, I'm looking forward to it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FIs that so …?\x01",
            "Hopefully it will go.\x02\x03",
            "#00003F(I see, this tension is\x01",
            "Is that the reason? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 2)
    OP_29(0x79, 0x1, 0x7)
    ClearChrFlags(0x9, 0x10)
    SetChrSubChip(0x9, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_5BD9 end

    def Function_25_60E4(): pass

    label("Function_25_60E4")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_61CC")
    Jump("loc_6216")

    label("loc_61CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_61EC")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6216")

    label("loc_61EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_620C")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6216")

    label("loc_620C")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6216")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FAh, I'm an assistant adviser.\x02\x03",
            "Sorry to trouble you,\x01",
            "Baggage and immigration application form\x01",
            "Could you confirm it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, of course.\x02",
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
            "#00004F- Baggage and immigration application form both\x01",
            "confirmed.\x02\x03",
            "#00001Fbut……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Hmm? What is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63D1")

    ChrTalk(
        0x102,
        (
            "#00101FYes, apparently\x01",
            "A ride ticket in baggage\x01",
            "It looks like it was not there.\x02\x03",
            "Do you have a mindset?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_63D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6453")

    ChrTalk(
        0x103,
        (
            "#00201FYes, apparently\x01",
            "A ride ticket in baggage\x01",
            "It looks like it was not there.\x02\x03",
            "Is there something in mind?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_6453")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64CF")

    ChrTalk(
        0x104,
        (
            "#00301FOh, apparently\x01",
            "A ride ticket in baggage\x01",
            "It looks like it was not.\x02\x03",
            "Is there something I did not recognize?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_64CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_654B")

    ChrTalk(
        0x109,
        (
            "#10101FYes, apparently\x01",
            "A ride ticket in baggage\x01",
            "I can not find it.\x02\x03",
            "Do you have a mindset?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_654B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65C5")

    ChrTalk(
        0x105,
        (
            "#10304FOh, apparently\x01",
            "A ride ticket in baggage\x01",
            "I do not see it.\x02\x03",
            "#10302FDoes it make sense?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65C5")

    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "If there are no tickets, tickets! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That should not be,\x01",
            "Within the bag properly -\x02",
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
        "… … no, there is not anywhere!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Clothes pocket? No, but -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, sorry,\x01",
            "Wait a moment and do not worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Absolutely there should be.\x01",
            "Always be able to find out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FIs that … Yes.\x01",
            "Well then I will ask again.\x02\x03",
            "#00003F(It can not be helped, this person\x01",
            "Do you keep doing review and postponing? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 1)
    OP_29(0x79, 0x1, 0x8)
    ClearChrFlags(0x8, 0x10)
    SetChrSubChip(0x8, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_60E4 end

    def Function_26_67A1(): pass

    label("Function_26_67A1")

    ModifyEventFlags(0, 3, 0x80)
    SetScenarioFlags(0x158, 6)
    Return()

    # Function_26_67A1 end

    def Function_27_67AA(): pass

    label("Function_27_67AA")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6892")
    Jump("loc_68DC")

    label("loc_6892")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68B2")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68DC")

    label("loc_68B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68D2")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68DC")

    label("loc_68D2")

    OP_52(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68DC")

    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "He is an assistant adviser.\x02\x03",
            "Sorry to trouble you,\x01",
            "Baggage and immigration application form\x01",
            "Could you confirm it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Fuu, say that\x01",
            "You have no right to turn me down, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Then, one by one\x01",
            "Do not take a confirmation\x01",
            "I wonder if I can finish early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FHello, I'm sorry.\x02",
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
            "#00004F- Baggage and immigration application form both\x01",
            "confirmed.\x01",
            "Thanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "…… Fuu, so\x01",
            "I do not need the word of thanking that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You do not have any errands any longer, do you?\x01",
            "If it is you, please go early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, I will excuse you.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B6B")

    ChrTalk(
        0x102,
        (
            "#00106F(Well, this work is\x01",
            "I use the nerve pretty. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CB7")

    label("loc_6B6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BB8")

    ChrTalk(
        0x103,
        (
            "#00206F(Fuu … ….\x01",
            "This work uses nerves. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CB7")

    label("loc_6BB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C09")

    ChrTalk(
        0x104,
        (
            "#00306F(Huh, this work too\x01",
            "You use the nerves pretty much. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CB7")

    label("loc_6C09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C5A")

    ChrTalk(
        0x109,
        (
            "#10106F(Fuu, quite\x01",
            "It might be a work that uses nerves. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CB7")

    label("loc_6C5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CB7")

    ChrTalk(
        0x105,
        (
            "#10304F(Huh, even an inspector\x01",
            "It is quite stressful\x01",
            "It's a job to collect. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CB7")

    OP_5A()
    SetScenarioFlags(0x1CB, 0)
    OP_29(0x79, 0x1, 0x9)
    ClearChrFlags(0x12, 0x10)
    SetChrSubChip(0x12, 0x0)
    EventEnd(0x5)
    Return()

    # Function_27_67AA end

    def Function_28_6CCD(): pass

    label("Function_28_6CCD")

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
            "Uhufu, after all\x01",
            "\"Eisengraf\" is\x01",
            "It is different from other trains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Jueling ……\x01",
            "Oops, I dont.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Yo, drool …?\x02\x03",
            "#00000FExcuse me,\x01",
            "He is an assistant adviser.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Ah, now\x01",
            "I am busy with train watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Since it is in a bag for an application,\x01",
            "You can carelessly examine it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI understand.\x01",
            "In that case …\x02",
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
            "#00004F- Baggage and immigration application form both\x01",
            "confirmed.\x01",
            "Thanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Grumbling ……\x01",
            "How long does it take to leave?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oh, I have regrets … ___ ___ 0\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FA8")

    ChrTalk(
        0x102,
        (
            "#00103F(…, not much, much\x01",
            "You seem to be concentrating. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70BB")

    label("loc_6FA8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FFD")

    ChrTalk(
        0x103,
        (
            "#00203F(… … Finally,\x01",
            "I never turned around. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70BB")

    label("loc_6FFD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7039")

    ChrTalk(
        0x104,
        "#00306F(… … I heard it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_70BB")

    label("loc_7039")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7082")

    ChrTalk(
        0x109,
        (
            "#10106F(…, equivalent,\x01",
            "I like trains. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70BB")

    label("loc_7082")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70BB")

    ChrTalk(
        0x105,
        "#10302F(Huh, I have not heard.)\x02",
    )

    CloseMessageWindow()

    label("loc_70BB")

    OP_5A()
    SetScenarioFlags(0x1CA, 7)
    OP_29(0x79, 0x1, 0xA)
    EventEnd(0x5)
    Return()

    # Function_28_6CCD end

    def Function_29_70C8(): pass

    label("Function_29_70C8")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_71B0")
    Jump("loc_71FA")

    label("loc_71B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_71D0")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_71FA")

    label("loc_71D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_71F0")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_71FA")

    label("loc_71F0")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71FA")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FWell, it is a person who is an assistant adviser.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F(This suit ……\x01",
            "Perhaps it is an employee of \"Black Moon\"? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Hmm, is there any problem?\x02",
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)
    Sleep(300)
    OP_93(0x10, 0x5A, 0x1F4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_78E2")
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
        "#00011F- Well, Shin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "- You,\x01",
            "The Special Affairs Support Division!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73D3")

    ChrTalk(
        0x10,
        (
            "Besides, Ely sister\x01",
            "Together with!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHuhu, Hello, Shin.\x02",
    )

    CloseMessageWindow()

    label("loc_73D3")


    ChrTalk(
        0x10,
        (
            "However, in such a place\x01",
            "What on earth are you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, at the job of the Special Affairs Support Division\x01",
            "I am helping the occupation officer's work.\x02\x03",
            "So carry your baggage and immigration application\x01",
            "I would like to confirm ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Indeed, the support department\x01",
            "Doing such a job, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Oh well, in that case\x01",
            "Please do it quickly.\x02",
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
            "#00004F- Alright.\x01",
            "Baggage and immigration application form both\x01",
            "It is confirmed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_75F6")

    ChrTalk(
        0x102,
        "#00100FThank you for your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hehe, for your sister\x01",
            "This much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I hope to see you again someday!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FYes, I'm looking forward to it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_78DD")

    label("loc_75F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_770E")

    ChrTalk(
        0x103,
        "#00200FThanks for your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "(Fum, in the support section\x01",
            "There are such girls too. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F…… What on my face?\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        "No, no, nothing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "- Well then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FOh, Shin is fine, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_78DD")

    label("loc_770E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77AC")

    ChrTalk(
        0x104,
        "#00300FThank you for your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Huang, I will give you another matter\x01",
            "I did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "- Well then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FOh, Shin is fine, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_78DD")

    label("loc_77AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_784A")

    ChrTalk(
        0x109,
        "#10100FThank you for your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Huang, I will give you another matter\x01",
            "I did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "- Well then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FOh, Shin is fine, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_78DD")

    label("loc_784A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78DD")

    ChrTalk(
        0x105,
        "#10300FI appreciate your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Huang, I will give you another matter\x01",
            "I did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "- Well then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FOh, Shin is fine, too.\x02",
    )

    CloseMessageWindow()

    label("loc_78DD")

    Jump("loc_7FEB")

    label("loc_78E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7C0D")
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
        "#00005F- Well, are you a black moon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "- You,\x01",
            "The Special Affairs Support Division!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A26")

    ChrTalk(
        0x10,
        (
            "Besides, Ely sister\x01",
            "Together with!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHuhu, Hello, Shin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Well, yeah ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "So what on earth are you doing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A48")

    label("loc_7A26")


    ChrTalk(
        0x10,
        "But what on earth do you do?\x02",
    )

    CloseMessageWindow()

    label("loc_7A48")


    ChrTalk(
        0x101,
        (
            "#00000FOh, at the job of the Special Affairs Support Division\x01",
            "I am helping the occupation officer's work.\x02\x03",
            "So carry your baggage and immigration application\x01",
            "I would like to confirm ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Indeed, the support department\x01",
            "Doing such a job, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Oh well, in that case\x01",
            "Please do it quickly.\x02",
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
            "#00004F- Alright.\x01",
            "Baggage and immigration application form both\x01",
            "It is confirmed.\x02\x03",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Huang, I will give you another matter\x01",
            "I did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Go ahead quickly when you are done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FOh, ah … … I will rude it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FEB")

    label("loc_7C0D")


    NpcTalk(
        0x10,
        "boy",
        "Hmm? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0xC)

    ChrTalk(
        0x101,
        (
            "#00000FUm, I am a person who is assistant adviser.\x02\x03",
            "Sorry to trouble you,\x01",
            "Baggage and immigration application form\x01",
            "Could you confirm it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "boy",
        "Oh, but please do it quickly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FHaha …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D6C")

    ChrTalk(
        0x102,
        (
            "#00105F(Is this child also a member of the black moon?\x01",
            "Attitude is quite large though ….)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0D")

    label("loc_7D6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DD5")

    ChrTalk(
        0x103,
        (
            "#00205F(Is this child also related to black moon?\x01",
            "It seems that attitude seems to be quite large, but …).\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0D")

    label("loc_7DD5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E3E")

    ChrTalk(
        0x104,
        (
            "#00303F(Is this boy also a black moon official?\x01",
            "Somewhat, the attitude is fluffy … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0D")

    label("loc_7E3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EAB")

    ChrTalk(
        0x109,
        (
            "#10105F(Is this child also related to black moon?\x01",
            "It seems that attitude is considerably large, but …).\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0D")

    label("loc_7EAB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F0D")

    ChrTalk(
        0x105,
        (
            "#10304F(Is this child also related to black moon?\x01",
            "It seems that attitude seems to be quite large, but …).\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F0D")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00004F- Baggage and immigration application form both\x01",
            "confirmed.\x01",
            "Thanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Oh my goodnight.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "boy",
        (
            "Huun, once you have finished using it\x01",
            "You are going quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FOh, ah ……\x02",
    )

    CloseMessageWindow()

    label("loc_7FEB")

    OP_5A()
    SetScenarioFlags(0x1CA, 6)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    ClearChrFlags(0xF, 0x10)
    SetChrSubChip(0xF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_29_70C8 end

    def Function_30_8006(): pass

    label("Function_30_8006")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80EE")
    Jump("loc_8138")

    label("loc_80EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_810E")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8138")

    label("loc_810E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_812E")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8138")

    label("loc_812E")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8138")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81EE")
    Jump("loc_8238")

    label("loc_81EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_820E")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8238")

    label("loc_820E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_822E")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8238")

    label("loc_822E")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8238")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FAh, I'm an assistant adviser.\x02\x03",
            "Sorry to trouble you,\x01",
            "Baggage and immigration application form\x01",
            "Could you confirm it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, why is that\x01",
            "Do I have to do it?\x02",
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
            "Hey hey,\x01",
            "What are you talking to the inspector!\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83D4")
    Jump("loc_841E")

    label("loc_83D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_83F4")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_841E")

    label("loc_83F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8414")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_841E")

    label("loc_8414")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_841E")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xE,
        (
            "Excuse me,\x01",
            "My sister 's rude disbelief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "This guy is stupid.\x01",
            "Please forgive me.\x02",
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
            "What is a fool, fool!\x01",
            "About the older brother -\x02",
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
        "#00006FWell, for the first time it is OK?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8591")

    ChrTalk(
        0x102,
        "#00100F(Yes, I guess.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8672")

    label("loc_8591")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85CB")

    ChrTalk(
        0x103,
        "#00200F(Yes, I think.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8672")

    label("loc_85CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8603")

    ChrTalk(
        0x104,
        "#00300F(Oh, I guess.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8672")

    label("loc_8603")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_863D")

    ChrTalk(
        0x109,
        "#10100F(Yes, I think.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8672")

    label("loc_863D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8672")

    ChrTalk(
        0x105,
        "#10300F(Huh, I guess.)\x02",
    )

    CloseMessageWindow()

    label("loc_8672")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_870E")
    Jump("loc_8758")

    label("loc_870E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_872E")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8758")

    label("loc_872E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_874E")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8758")

    label("loc_874E")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8758")

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
            "#00004F- Baggage and immigration application form both\x01",
            "confirmed.\x01",
            "Thanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No problem\x01",
            "My younger sister was sorry to trouble you.\x02",
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
            "What is it, if you say that?\x01",
            "Onii-chan is better -\x02",
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
        "#00003F(It seems better to go away earlier.)\x02",
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

    # Function_30_8006 end

    def Function_31_88EB(): pass

    label("Function_31_88EB")

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
        "#00000FWell, have we all confirmed this?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A02")

    ChrTalk(
        0x102,
        (
            "#00105FSpeaking of which,\x01",
            "Take your grandfather's ticket\x01",
            "I have not checked it yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BA1")

    label("loc_8A02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A6E")

    ChrTalk(
        0x103,
        (
            "#00205FSpeaking of which,\x01",
            "Take your grandfather's ticket\x01",
            "I have not checked it yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BA1")

    label("loc_8A6E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AD2")

    ChrTalk(
        0x104,
        (
            "#00305FSpeaking of which,\x01",
            "Take the grandfather's ticket\x01",
            "I have not confirmed it yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BA1")

    label("loc_8AD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B3E")

    ChrTalk(
        0x109,
        (
            "#10105FSpeaking of which,\x01",
            "Take your grandfather's ticket\x01",
            "I have not checked it yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BA1")

    label("loc_8B3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BA1")

    ChrTalk(
        0x105,
        (
            "#10305FSpeaking of which,\x01",
            "Take your grandfather's ticket\x01",
            "I did not check it yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BA1")


    ChrTalk(
        0x101,
        (
            "#00003FOh yeah, well then\x01",
            "Go back to confirmation at once -\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        "- Let me get back my tickets!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C6B")

    ChrTalk(
        0x102,
        "#00101F- Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D26")

    label("loc_8C6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C9D")

    ChrTalk(
        0x103,
        "#00201F- Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D26")

    label("loc_8C9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CCB")

    ChrTalk(
        0x104,
        "#00301F- Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D26")

    label("loc_8CCB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CFD")

    ChrTalk(
        0x109,
        "#10101F- Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D26")

    label("loc_8CFD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D26")

    ChrTalk(
        0x105,
        "#10301F- Lloyd!\x02",
    )

    CloseMessageWindow()

    label("loc_8D26")


    ChrTalk(
        0x101,
        "#00000FOh, let's head right away!\x02",
    )

    CloseMessageWindow()
    Call(0, 32)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8D60")
    Call(0, 34)
    Jump("loc_8D63")

    label("loc_8D60")

    Call(0, 33)

    label("loc_8D63")

    EventEnd(0x5)
    Return()

    # Function_31_88EB end

    def Function_32_8D66(): pass

    label("Function_32_8D66")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E98")
    SetChrPos(0x102, -480, 0, 8210, 180)
    Jump("loc_8F2B")

    label("loc_8E98")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EBE")
    SetChrPos(0x103, -480, 0, 8210, 180)
    Jump("loc_8F2B")

    label("loc_8EBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EE4")
    SetChrPos(0x104, -480, 0, 8210, 180)
    Jump("loc_8F2B")

    label("loc_8EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F0A")
    SetChrPos(0x109, -480, 0, 8210, 180)
    Jump("loc_8F2B")

    label("loc_8F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F2B")
    SetChrPos(0x105, -480, 0, 8210, 180)

    label("loc_8F2B")

    OP_68(120, 1000, 220, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "So, to one of you two\x01",
            "I say that it is fixed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now, which one?\x01",
            "Let's get white quickly!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    def lambda_8FDF():
        OP_95(0x101, 460, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8FDF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9023")

    def lambda_9009():
        OP_95(0x102, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9009)
    Jump("loc_90DA")

    label("loc_9023")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9052")

    def lambda_9038():
        OP_95(0x103, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9038)
    Jump("loc_90DA")

    label("loc_9052")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9081")

    def lambda_9067():
        OP_95(0x104, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9067)
    Jump("loc_90DA")

    label("loc_9081")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90B0")

    def lambda_9096():
        OP_95(0x109, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9096)
    Jump("loc_90DA")

    label("loc_90B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90DA")

    def lambda_90C5():
        OP_95(0x105, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_90C5)

    label("loc_90DA")

    OP_68(70, 1000, 2830, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16500, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FUmm, what happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, the one who was the inspector just before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Somehow,\x01",
            "This old man eats Ichamon -\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "what--\x01",
            "Well done!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FPlease calm down!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_922E")

    ChrTalk(
        0x102,
        (
            "#00101FUm, first of all, talk\x01",
            "May I ask you a favor?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9365")

    label("loc_922E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_927D")

    ChrTalk(
        0x103,
        (
            "#00200FUm, first of all, talk\x01",
            "Would you like to ask?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9365")

    label("loc_927D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92CC")

    ChrTalk(
        0x104,
        (
            "#00303FTentatively, first of all\x01",
            "Do not you tell me a story?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9365")

    label("loc_92CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_931D")

    ChrTalk(
        0x109,
        (
            "#10101FTentatively, first of all\x01",
            "Could you tell me a story?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9365")

    label("loc_931D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9365")

    ChrTalk(
        0x105,
        (
            "#10304FAnyway, first\x01",
            "Can you tell me a story?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9365")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 550, 0, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93A7")
    SetChrPos(0x102, -540, 0, 1100, 180)
    Jump("loc_943A")

    label("loc_93A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93CD")
    SetChrPos(0x103, -540, 0, 1100, 180)
    Jump("loc_943A")

    label("loc_93CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93F3")
    SetChrPos(0x104, -540, 0, 1100, 180)
    Jump("loc_943A")

    label("loc_93F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9419")
    SetChrPos(0x109, -540, 0, 1100, 180)
    Jump("loc_943A")

    label("loc_9419")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_943A")
    SetChrPos(0x105, -540, 0, 1100, 180)

    label("loc_943A")

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
            "#00003FIndeed, my grandfather\x01",
            "Tickets purchased are specified for 4th companion\x01",
            "To Oleto Autonomous Region ……\x02\x03",
            "And exactly the same ticket\x01",
            "There were two people in this car who had … …\x02\x03",
            "#00001FIn other words, either of them\x01",
            "It may have stolen the ticket -\x01",
            "Is that what you want to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "- Anyway, I\x01",
            "Have a ticket to home\x01",
            "It is undeniable fact that I entered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And during this short time\x01",
            "There is no way I can lose my tickets!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even as it is a victim of theft\x01",
            "I do not see it.\x02",
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
            "#00006FUm, asserts as a fossil\x01",
            "I think that I can not … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's okay,\x01",
            "Please do not hesitate to tell me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You just said to be blurred!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "You still say that …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FTentatively -\x01",
            "Both of you please calm down.\x02\x03",
            "#00001FAnyways,\x01",
            "Just hitting emotions\x01",
            "Things that fit will not fit.\x02\x03",
            "#00003FSo, for two of you with tickets\x01",
            "Please give me a brief question.\x02\x03",
            "#00001FReason for aiming at the destination -\x01",
            "That's the minimum.\x01",
            "Could you tell me?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "Also why aim for your destination?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hun, so\x01",
            "Can you prove innocence?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, if the ticket really\x01",
            "For a criminal if it is a thief\x01",
            "It may not be your desired destination.\x02\x03",
            "#00004FIn that case, if the criminal\x01",
            "I may give out some kind of rag.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99C3")

    ChrTalk(
        0x102,
        (
            "#00105FI see,\x01",
            "Certainly there is a possibility.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE2")

    label("loc_99C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A0E")

    ChrTalk(
        0x103,
        (
            "#00203FI see,\x01",
            "Certainly there is a possibility.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE2")

    label("loc_9A0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A55")

    ChrTalk(
        0x104,
        (
            "#00305FI see,\x01",
            "Certainly that possibility.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE2")

    label("loc_9A55")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AA0")

    ChrTalk(
        0x109,
        (
            "#10105FI see,\x01",
            "Certainly there is a possibility.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE2")

    label("loc_9AA0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AE2")

    ChrTalk(
        0x105,
        (
            "#10302FI see,\x01",
            "Certainly there is a possibility.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AE2")


    ChrTalk(
        0x8,
        (
            "Hmm, if you do not do good, hurry up.\x01",
            "Let's answer quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hun, that much cheap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am a merchant.\x01",
            "From now on in Oleto Autonomous province\x01",
            "I have an important contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way this is the contract -\x01",
            "The deal is in Oredo\x01",
            "\"meteor#4RDuct#It is a business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Such a human being steals a ticket,\x01",
            "There is no way I can do the Secco?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Daughter …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……I see.\x02\x03",
            "#00001FBy the way, who are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Er, um, I\x01",
            "Oredo autonomous state is my hometown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…… Does not Reason make a reason?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, such a thing ……\x02\x03",
            "#00008F(Well, for the time being, I tried asking\x01",
            "I can not judge it by just this. )\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_32_8D66 end

    def Function_33_9D47(): pass

    label("Function_33_9D47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DA2")

    ChrTalk(
        0x102,
        (
            "#00103F(… … apparently, to us\x01",
            "It seems like you have done so far. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F1D")

    label("loc_9DA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E05")

    ChrTalk(
        0x103,
        (
            "#00203F(… apparently, to us\x01",
            "It seems like you have done so far. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F1D")

    label("loc_9E05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E62")

    ChrTalk(
        0x104,
        (
            "#00303F(… apparently, to us\x01",
            "It looks like you can do it. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F1D")

    label("loc_9E62")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EC5")

    ChrTalk(
        0x109,
        (
            "#10103F(… apparently, to us\x01",
            "It looks like you can do it. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F1D")

    label("loc_9EC5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F1D")

    ChrTalk(
        0x105,
        (
            "#10303F(… apparently, to us\x01",
            "It seems like you can do it. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F1D")


    ChrTalk(
        0x101,
        (
            "#00003F(That's right ……\x01",
            "Afterwards to Mr. Marlow\x01",
            "It seems to only report. )\x02\x03",
            "#00000FUm, everyone for a while\x01",
            "Please stay on this occasion.\x02\x03",
            "Now I will call on the top.\x02",
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

    # Function_33_9D47 end

    def Function_34_9FF7(): pass

    label("Function_34_9FF7")

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
            "Haha, that's funny.\x01",
            "There is lies in this car!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A0B4():
        OP_93(0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A0B4)

    def lambda_A0C1():
        OP_93(0x1, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A0C1)
    OP_68(460, 1000, 5040, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16210, 3000)

    def lambda_A0FC():
        OP_95(0x10, 460, 0, 5470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A0FC)

    def lambda_A116():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_A116)

    def lambda_A127():
        OP_95(0xF, -480, 0, 5970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A127)

    def lambda_A141():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A141)
    Sleep(2000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x1, 0x8)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A2AA")

    ChrTalk(
        0x101,
        (
            "#00005F- Shin?\x02\x03",
            "#00001FWait a moment.\x01",
            "While traveling around, move the vehicle\x01",
            "The rule does not mean -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hun, already an inspection\x01",
            "You have done a lot, do not you?\x01",
            "Make it as flexible as that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FAbsolutely ……\x01",
            "Well, whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Anyway, something funny\x01",
            "It seems to be getting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I will join you too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A312")

    label("loc_A2AA")


    ChrTalk(
        0x101,
        "#00005F- Shin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Huh, something funny\x01",
            "It seems to be getting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I will join you too!\x02",
    )

    CloseMessageWindow()

    label("loc_A312")


    ChrTalk(
        0x101,
        "#00005FWell, let's participate …\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3AD")
    SetChrPos(0x102, -540, 0, 2100, 135)
    Jump("loc_A440")

    label("loc_A3AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3D3")
    SetChrPos(0x103, -540, 0, 2100, 135)
    Jump("loc_A440")

    label("loc_A3D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3F9")
    SetChrPos(0x104, -540, 0, 2100, 135)
    Jump("loc_A440")

    label("loc_A3F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A41F")
    SetChrPos(0x109, -540, 0, 2100, 135)
    Jump("loc_A440")

    label("loc_A41F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A440")
    SetChrPos(0x105, -540, 0, 2100, 135)

    label("loc_A440")

    SetChrPos(0xF, 540, 0, 2500, 180)
    OP_93(0x8, 0x5A, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00001F…… and what is stupidity is\x01",
            "What on earth is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Oh, first\x01",
            "Let the merchant there answer.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A4CF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A4CF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4F9")

    def lambda_A4EC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A4EC)
    Jump("loc_A57C")

    label("loc_A4F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A51B")

    def lambda_A50E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A50E)
    Jump("loc_A57C")

    label("loc_A51B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A53D")

    def lambda_A530():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A530)
    Jump("loc_A57C")

    label("loc_A53D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A55F")

    def lambda_A552():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A552)
    Jump("loc_A57C")

    label("loc_A55F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A57C")

    def lambda_A574():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A574)

    label("loc_A57C")


    ChrTalk(
        0x10,
        (
            "You - you earlier, \"Meteor Shokai\" and\x01",
            "You said you had a deal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "To what extent is it specific?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huh, why did I\x01",
            "To such a children's game ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, dealings are\x01",
            "Unusual vegetables in Oredo Autonomous Region\x01",
            "It is a purchase of spices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Speaking of Oredo is a popular place of agriculture -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Besides, \"Meteor Shokai\"\x01",
            "Participate the eastern citizens of the Republic\x01",
            "Affiliated company of \"Kuroyu moon group\" -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… I do not think there's any doubt?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Juhu, as Kisama says certainly\x01",
            "Oled has \"meteor shower\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "But unfortunately -\x01",
            "Still foothold within autonomous state\x01",
            "It is trying to keep it together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Very outsider with humans\x01",
            "You can do business\x01",
            "It is not in the stage?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "what?\x01",
            "Why do you understand such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Because it is - what will you do?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0xF,
        "- Yes, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You, silently from a little while ago\x01",
            "As long as you listen to the baby\x01",
            "Too rude against me -!\x02",
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
            "#5SEee, keep it down -\x01",
            "He is a grandson of the elder \"Elder\"\x01",
            "Shin will let you!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Elder grandchild ~? Such a joke ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "Oh, the suits you wear ……\x01",
            "I certainly remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "That's … such … really … really.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x10,
        "Huh, you finally understood?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "By the way what is the real purpose?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Huh, oh well.\x01",
            "Later I went to a separate room\x01",
            "Talk to the inspector everything.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA97")

    ChrTalk(
        0x102,
        "#00103F(… … Shin, I'll do it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB96")

    label("loc_AA97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAD7")

    ChrTalk(
        0x103,
        "#00203F(… this child is incredible.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB96")

    label("loc_AAD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB19")

    ChrTalk(
        0x104,
        "#00303F(… … Shin nobody, do not do it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB96")

    label("loc_AB19")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB59")

    ChrTalk(
        0x109,
        "#10105F(… …. That's amazing, Shin.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB96")

    label("loc_AB59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB96")

    ChrTalk(
        0x105,
        "#10304F(Huh, it's a big taste.)\x02",
    )

    CloseMessageWindow()

    label("loc_AB96")


    ChrTalk(
        0x101,
        (
            "#00003F(Oh, what I should say\x01",
            "Dignity is enough. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "- Then, you are the next.\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FShin …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, I am?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The criminal was lying.\x01",
            "That guy … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hun, who said such a thing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "A bit for you too\x01",
            "There is something I would like to ask.\x01",
            "You sure are from Oleid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Is that … Yes.\x01",
            "From now on …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hum, if you understand this, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "In Oread Autonomous province, besides agriculture\x01",
            "Famous places for the unexplored area -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "There are many hot springs … …\x01",
            "Which of the following springs is in Oledo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "El Molo hot spring\x01",
            "嘇 Palm Hot Spring\x01",
            "嘊 Oredo hot spring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "- Come on, answer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Huh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, uh ……\x01",
            "Such a thing, to Oredo hot spring of\x01",
            "Is not it decided?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "……Really.\x01",
            "Huh … … Huh ha ha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, what do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I\x01",
            "You thought that it was a kid, you despised?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Oledo hot spring ~?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I wonder if that's solid,\x01",
            "Autonomous state itself was named\x01",
            "There is no hot spring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If you are really a human of Oredo\x01",
            "I guess I answered.\x01",
            "\"There is no answer among them\".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "Huh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Huhun, furthermore\x01",
            "Would you like to issue a problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Although boro is\x01",
            "I think that it will be only one after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "So where are you from, really?\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "Well, that is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Um, maybe I should say something\x01",
            "I thought that it was not,\x01",
            "Actually, I am from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But now I have a house in Oredo ……\x01",
            "Please, believe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hun, how are you.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    TurnDirection(0x10, 0x101, 500)

    ChrTalk(
        0x10,
        (
            "--so,\x01",
            "How about the Special Affairs Support Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "In any case, both of us\x01",
            "I understood that it was a stupid thing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Which is the ticket thief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FOh, oh … That's right.\x02",
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
            "#1KMerchant and youth, ticket thief\x01",
            "What is the high possibility?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "merchant\x01",      # 0
            "Adolescents\x01",      # 1
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
        (0, "loc_B26D"),
        (1, "loc_B48F"),
        (SWITCH_DEFAULT, "loc_B5D7"),
    )


    label("loc_B26D")

    OP_2C(0x79, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003FIt is a merchant's person.\x02\x03",
            "#00000FThis person,\x01",
            "There seems to be plenty of secret affairs … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hey, you …\x01",
            "Do not let me down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Are you really thinking seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FOh, sorry.\x02\x03",
            "#00008FI see.\x01",
            "You should think about it by erasing method.\x02\x03",
            "#00001FMerchant showed me\x01",
            "Fictional contract … ….\x02\x03",
            "I do not know the purpose,\x01",
            "Bother to take such a thing\x01",
            "We are prepared carefully.\x02\x03",
            "#00003FTicket thief\x01",
            "It is also said that committing a misdemeanor\x01",
            "It is an unnatural impression.\x02\x03",
            "Even if the destination is\x01",
            "Even if it is not Oredo\x01",
            "It is possible to get off on the way … …\x02\x03",
            "#00001FAnd then …\x01",
            "You are the criminal, are not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5D7")

    label("loc_B48F")

    OP_2C(0x79, 0x2)

    ChrTalk(
        0x101,
        (
            "#00003FI guess he's here.\x02\x03",
            "#00001FMerchant showed me\x01",
            "Fictional contract … ….\x02\x03",
            "I do not know the purpose,\x01",
            "Bother to take such a thing\x01",
            "We are prepared carefully.\x02\x03",
            "#00003FTicket thief\x01",
            "It is also said that committing a misdemeanor\x01",
            "It is an unnatural impression.\x02\x03",
            "Even if the destination is\x01",
            "Even if it is not Oredo\x01",
            "It is possible to get off on the way … …\x02\x03",
            "#00001FAnd then …\x01",
            "You are the criminal, are not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5D7")

    label("loc_B5D7")


    ChrTalk(
        0xC,
        "Uu……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hm, that's a passing score.\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x1F4)

    ChrTalk(
        0x10,
        (
            "Hey, you\x01",
            "Even if you do not know any more\x01",
            "You can not hide it through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If you are a guy, this place\x01",
            "Be honest and whitish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5SPlease, miss it!#3S\x02",
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

    def lambda_B73F():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B73F)
    Sleep(50)

    def lambda_B74F():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B74F)
    Sleep(300)

    ChrTalk(
        0x8,
        "What, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hey, you -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The mother's republic\x01",
            "I was taken to a hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So why\x01",
            "I have to hurry to the hospital -!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Suddenly I do not understand Wake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Anyway let's tell you the circumstances.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Is that … Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually, I, Ursula Medical University\x01",
            "Aiming students ……\x01",
            "But parents are poor families ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Until my mother impossible\x01",
            "Have them send it out to the crossbell …\x01",
            "I am studying while playing bite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In such a situation,\x01",
            "Suddenly my mother fell down\x01",
            "A news comes in … … so ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "- I would like to visit,\x01",
            "I stole my ticket because there is no Mira.\x01",
            "Is that something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Is that … Yes.\x01",
            "This is not a lie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "While doing this now mother -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell\x01",
            "To lose theft … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Yosh, I will give Mira.\x02",
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

    def lambda_BAC8():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BAC8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAF2")

    def lambda_BAE5():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BAE5)
    Jump("loc_BB75")

    label("loc_BAF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB14")

    def lambda_BB07():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BB07)
    Jump("loc_BB75")

    label("loc_BB14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB36")

    def lambda_BB29():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BB29)
    Jump("loc_BB75")

    label("loc_BB36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB58")

    def lambda_BB4B():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BB4B)
    Jump("loc_BB75")

    label("loc_BB58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB75")

    def lambda_BB6D():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BB6D)

    label("loc_BB75")


    def lambda_BB7A():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BB7A)
    Sleep(50)

    def lambda_BB8A():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BB8A)
    Sleep(300)

    ChrTalk(
        0xC,
        "Huh……?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBD1")

    ChrTalk(
        0x102,
        "#00105FShin, you …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC7C")

    label("loc_BBD1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBFD")

    ChrTalk(
        0x103,
        "#00205FThat is….\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC7C")

    label("loc_BBFD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC2B")

    ChrTalk(
        0x104,
        "#00305FHey ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC7C")

    label("loc_BC2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC57")

    ChrTalk(
        0x109,
        "#10105FUh……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC7C")

    label("loc_BC57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC7C")

    ChrTalk(
        0x105,
        "#10305FOh\x02",
    )

    CloseMessageWindow()

    label("loc_BC7C")

    TurnDirection(0x10, 0x8, 500)

    ChrTalk(
        0x10,
        (
            "Old man, your ticket\x01",
            "I will let you return it with responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well,\x01",
            "Will not you hold Hoko?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if the ticket returns\x01",
            "I do not feel ashamed of separating things … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xC, 500)

    ChrTalk(
        0x10,
        "And you -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Is that … Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Did you get in on the stolen ticket?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "What if my mother knows it.\x01",
            "Do you think that it will be pleased?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, Mira will give out\x01",
            "This is not a transfer -\x01",
            "I lend it to the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Although no time limit is stipulated,\x01",
            "I will definitely return it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uoo, sorry ….\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Be sure to return it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hm, let's keep promises.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 500)

    ChrTalk(
        0x10,
        (
            "That's why,\x01",
            "Then call another official inspector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I will explain the circumstances.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, ah ……\x02",
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

    # Function_34_9FF7 end

    def Function_35_BF66(): pass

    label("Function_35_BF66")

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

    # Function_35_BF66 end

    def Function_36_BFB0(): pass

    label("Function_36_BFB0")

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

    # Function_36_BFB0 end

    def Function_37_BFFA(): pass

    label("Function_37_BFFA")

    SetChrPos(0xFE, -400, 0, -4300, 0)

    def lambda_C010():
        OP_95(0xFE, -400, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C010)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_37_BFFA end

    def Function_38_C031(): pass

    label("Function_38_C031")

    SetChrPos(0xFE, -400, 0, -5500, 0)
    Sleep(50)

    def lambda_C04A():
        OP_95(0xFE, -400, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C04A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_38_C031 end

    def Function_39_C06B(): pass

    label("Function_39_C06B")

    SetChrPos(0xFE, 400, 0, -4600, 0)
    Sleep(50)

    def lambda_C084():
        OP_95(0xFE, 400, 0, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C084)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_39_C06B end

    def Function_40_C0A5(): pass

    label("Function_40_C0A5")

    SetChrPos(0xFE, 400, 0, -5600, 0)
    Sleep(100)

    def lambda_C0BE():
        OP_95(0xFE, 400, 0, 2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C0BE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_40_C0A5 end

    def Function_41_C0DF(): pass

    label("Function_41_C0DF")

    SetChrPos(0xFE, 400, 0, -6600, 0)
    Sleep(50)

    def lambda_C0F8():
        OP_95(0xFE, 500, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C0F8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_41_C0DF end

    def Function_42_C119(): pass

    label("Function_42_C119")

    SetChrPos(0xFE, 400, 0, -7700, 0)
    Sleep(100)

    def lambda_C132():
        OP_95(0xFE, 400, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C132)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_42_C119 end

    def Function_43_C153(): pass

    label("Function_43_C153")

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
        "#5P#03402FYou came.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x28, 0x1)

    ChrTalk(
        0x28,
        "#11P#11509FYo. Long time\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 1000, -6000, 2000)
    MoveCamera(323, 21, 0, 2000)
    SetCameraDistance(18000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00006FGood to see you \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIndeed, from the communication equipment of the train\x01",
            "I contacted the support department car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "#03404F#6PGreetings\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C558")

    AnonymousTalk(
        0x27,
        (
            "Huff … …. Looking at it again\x01",
            "Extensively#4RYes Yes#It looks tamey.\x02\x03",
            "With young lieutenant defense military\x01",
            "The principal guardian of the star cup is with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C805")

    label("loc_C558")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5E4")

    AnonymousTalk(
        0x27,
        (
            "Huff … …. Looking at it again\x01",
            "Extensively#4RYes Yes#It looks tamey.\x02\x03",
            "With young lieutenant defense military\x01",
            "There is no legendary hitter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C805")

    label("loc_C5E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C676")

    AnonymousTalk(
        0x27,
        (
            "Huff … …. Looking at it again\x01",
            "Extensively#4RYes Yes#It looks tamey.\x02\x03",
            "With young lieutenant defense military\x01",
            "The chief investigator of department is together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C805")

    label("loc_C676")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6FA")

    AnonymousTalk(
        0x27,
        (
            "Huff … …. Looking at it again\x01",
            "Extensively#4RYes Yes#It looks tamey.\x02\x03",
            "With the guardian of the star cup\x01",
            "There is no legendary hitter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C805")

    label("loc_C6FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C784")

    AnonymousTalk(
        0x27,
        (
            "Huff … …. Looking at it again\x01",
            "Extensively#4RYes Yes#It looks tamey.\x02\x03",
            "With chief investigator of department 1\x01",
            "The principal guardian of the star cup is with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C805")

    label("loc_C784")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C805")

    AnonymousTalk(
        0x27,
        (
            "Huff … …. Looking at it again\x01",
            "Extensively#4RYes Yes#It looks tamey.\x02\x03",
            "With chief investigator of department 1\x01",
            "There is no legendary hitter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C805")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C88A")

    ChrTalk(
        0x109,
        (
            "#6P#10103F…… Unfortunately now,\x01",
            "I am re - entering the support department.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C88A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8D5")

    ChrTalk(
        0x105,
        (
            "#6P#10402FOf course, my background\x01",
            "Are you grasping it soon?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C90D")

    ChrTalk(
        0x106,
        "#6P#10701F….\x02",
    )

    CloseMessageWindow()

    label("loc_C90D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C958")

    ChrTalk(
        0x10A,
        (
            "#6P#00603FHun … … socializing\x01",
            "Let's do that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C958")


    ChrTalk(
        0x102,
        (
            "#6P#00106FNo way,\x01",
            "What is left in the crossbell\x01",
            "I did not think.\x02\x03",
            "#00101FHave you been here since that day?\x02",
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
            "Oh, to find out\x01",
            "It was because of various things.\x02\x03",
            "However, at last\x01",
            "I can return to Elebonia.\x02",
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
        "#00011F#12PLook into?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_END)), "loc_CDFD")

    ChrTalk(
        0x28,
        (
            "#11504FBy the way, besides us\x01",
            "A stakeholder in Libert\x01",
            "I'm moving though ….\x02\x03",
            "#11500FDid you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh …… R & A Research\x01",
            "Raines, are not you?\x02\x03",
            "#00001FAre you working with him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PYes, for this matter\x01",
            "We are exchanging information with each other.\x02\x03",
            "#03402FFor a private research company\x01",
            "I have an excellent information network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11504FWell, if it is private, it will be a shortage of people\x01",
            "Do not turn people around in all directions\x01",
            "I guess I'm having a hard time though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell that aside\x02\x03",
            "#00301F\"Chairman of Iron and Blood#8RThe boss of the center#\"But\x01",
            "I guess it is missing because it is shot.\x02\x03",
            "Is it ok for you to be messing around here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE81")

    label("loc_CDFD")


    ChrTalk(
        0x104,
        (
            "#00306F#12PTsukemasa#8RThe boss of the center#\"But\x01",
            "I guess it is missing because it is shot.\x02\x03",
            "#00301FIs it ok for you to be messing around here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE81")


    ChrTalk(
        0x28,
        (
            "#11505FAh……\x01",
            "Do you mean Giulian's Osan?\x02\x03",
            "#11506FI got home in a hurry\x01",
            "I do not wish to be helped.\x02\x03",
            "#11510FBesides, if you try that osan,\x01",
            "Both things and crossbells\x01",
            "I guess it is in the assumed phase.\x02",
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
            "#00007F#12PI suppose … …\x01",
            "I will be shot! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FCrossbell's thing is …\x01",
            "It's about this incident, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11501FFor that Ossan\x01",
            "Everything is a \"piece\" of play board.\x02\x03",
            "#11503FCrossbell gained treasure,\x01",
            "Familiarity of the entire continent, not independence\x01",
            "Theory#4RMukuro#What I already do ……\x02\x03",
            "To the extent that the Imperial army came back\x01",
            "The aristocratic power occupied the capital … …\x02\x03",
            "#11508FAs a result, I was shot\x01",
            "Due to the serious injury of being moribund\x01",
            "The civil war of the muddy started … …\x02\x03",
            "Nevertheless, it is called a crossbell.\x01",
            "By making an inviolable \"wall\"\x01",
            "That the invasion of the Republic has been halted.\x02\x03",
            "#11500FFor that Ossan\x01",
            "It would have been the development that all assumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#12PUgh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FN-no way\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D2FC")

    ChrTalk(
        0x105,
        "#6P#10401F… … It's a girl, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D363")

    label("loc_D2FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D337")

    ChrTalk(
        0x10A,
        "#6P#00610FHe was that much of a monster…\x02",
    )

    CloseMessageWindow()
    Jump("loc_D363")

    label("loc_D337")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D363")

    ChrTalk(
        0x106,
        "#6P#10703F……monster……\x02",
    )

    CloseMessageWindow()

    label("loc_D363")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D39E")

    ChrTalk(
        0x109,
        "#6P#10110FAnd I can not believe it ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_D435")

    label("loc_D39E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3EC")

    ChrTalk(
        0x106,
        (
            "#6P#10703F… … In the hiatus\x01",
            "It is a bit unbelievable …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D435")

    label("loc_D3EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D435")

    ChrTalk(
        0x10A,
        (
            "#6P#00610FAs expected\x01",
            "It's not something I can do … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D435")


    ChrTalk(
        0x27,
        (
            "#03401F#5PWell \"association\" is also towards the empire\x01",
            "It seems to be moving ….\x02\x03",
            "The truly terrifying thing is,\x01",
            "Maybe it 's the bureaucrats for iron and blood.\x02\x03",
            "#03403FMy own#2RVisiting#Even use it as a \"piece\"\x01",
            "Producing a turbulent era of rough … …\x02\x03",
            "#03401FExactly a gift#4RMuscle#─ ─ No monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PI thought that it was a cheeky osean\x01",
            "It's just there … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101F…… President Dieter\x01",
            "Do you realize that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03405F#5PI wonder about that\x02\x03",
            "#03403FWhat is it supposed to say like this ……\x01",
            "A person named Dieter · Crois\x01",
            "Performance is super class.\x02\x03",
            "#03401FBut as an actual politician … …\x01",
            "You can not help feeling a little doubtful.\x02\x03",
            "Only from the viewpoint of management\x01",
            "In the sense that it does not move politics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PThat is….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PWell, to the last\x01",
            "Roots are bankers.\x02\x03",
            "#03402FEven with the mission of the \"Clois family\"\x01",
            "It seems like I can leave it to my daughter.\x02",
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
        "#12P#00205FThat is….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12PYou knew that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11504FWell, here in this\x01",
            "I have an information source.\x02\x03",
            "#11508FAt that auction meeting\x01",
            "Protected chibico ……\x02\x03",
            "#11501FThat child became a \"nucleus\"\x01",
            "How was \"Treasure\" born?\x01",
            "I have a rough grasp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P….\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D9C5")

    ChrTalk(
        0x105,
        (
            "#6P#10408FWhew ……\x01",
            "Secular powers up there\x01",
            "It is said that he is grabbing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA12")

    ChrTalk(
        0x10A,
        (
            "#6P#00603FAs expected to the Imperial Army Information Bureau\x01",
            "Is it Rock Smith Institution ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA3A")

    ChrTalk(
        0x109,
        "#6P#10101FDamn\x02",
    )

    CloseMessageWindow()

    label("loc_DA3A")


    ChrTalk(
        0x27,
        (
            "#03400F#5PI do not want you to misunderstand me ….\x01",
            "Even for me, even for him there\x01",
            "Only people in the information field.\x02\x03",
            "With my personal existence\x01",
            "Wondering what to do with \"treasure\"\x01",
            "I do not think.\x02\x03",
            "#03403FHowever, it makes the whole continent confused\x01",
            "Opportunity#4RTrigger#This affair that became … …\x02\x03",
            "#03401FDrawing that picture \"True Match#4RFixer#\"But\x01",
            "I just want to know who it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FTrue …… Masterpiece#4RFixer#It is! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PAs I said earlier,\x01",
            "President Dieter is to the last\x01",
            "The aspect as a manager is too strong.\x02\x03",
            "Mr. Mariavell is also unknown but\x01",
            "Besides politics, we are going to\x01",
            "It seems they underwrite them one after another.\x02\x03",
            "#03400FBut \"Wind sword of the wind\" is … …\x01",
            "It is too self-sustaining to say the black screen\x01",
            "It will be too stoic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11501FEven if it is a Giulious Osan\x01",
            "Even if it is \"an association\" …\x02\x03",
            "You can use the situation of Crossbell,\x01",
            "We cooperated with the coincidence of interests\x01",
            "It is not acting on its own initiative.\x02\x03",
            "#11503FSomeone has to be behind them\x02\x03",
            "#11508FGovernment, econonmy, history, international affairs….\x02\x03",
            "Clois family, D∴ G sect,\x01",
            "Until the movement of \"association\" … …\x02\x03",
            "#11501Fall#4R噵 噵#Before reaching you\x01",
            "Working on each side\x01",
            "The guy who drew the picture so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12POi oi, seriously\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FA bit like a conspiracy argument\x01",
            "Do you feel it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FCertainly … … Puzzle piece\x01",
            "I feel like I'm missing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_E011")
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
        "#00013F#11P(……… No way …………)\x02",
    )

    CloseMessageWindow()
    Jump("loc_E076")

    label("loc_E011")


    ChrTalk(
        0x101,
        "#00008F#11P(Who in the world…)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E076")

    ChrTalk(
        0x10A,
        "#00608F#6P#30W(It couldn't be…)\x02",
    )

    CloseMessageWindow()

    label("loc_E076")

    Sleep(500)

    ChrTalk(
        0x27,
        (
            "#03404F#5PWell, confirmation around that\x01",
            "I thought I could do it … ….\x02\x03",
            "There seems to be no confirmation to you also,\x01",
            "Let's keep this level.\x02\x03",
            "#03402FI do not have time, and in another issue\x01",
            "I will let you enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12POne more issue?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11504FYeah. It's simple really\x02\x03",
            "#11507F\"Orkis Tower Capture Operation\",\x01",
            "I'm trying to help out!\x02",
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
        "#00011F#12PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#12PCome on,\x01",
            "It is suddenly too! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03404F#5PAs the outline of the incident was found,\x01",
            "The need to stay on the crossbell\x01",
            "I do not have it ….\x02\x03",
            "I mean leaving as it is\x01",
            "Because I am a little awake.\x02\x03",
            "#03400FWhat will happen to the crossbell in the future\x01",
            "I guess it depends on you … ….\x02\x03",
            "Even if you are in chronic stalemate\x01",
            "It is troubling here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11504F\"Pomutto\" even before clearing\x01",
            "I do not feel uncomfortable to throw it.\x02\x03",
            "#11502FWell, that's the same feeling\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00109FSame feeling…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211F…… In what time\x01",
            "Account of \"Pomutto\"\x01",
            "You got it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E4FE")

    ChrTalk(
        0x105,
        (
            "#6P#10404FBut well, as the strength increases\x01",
            "It seems that the success rate of the strategy will rise as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5B1")

    label("loc_E4FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E558")

    ChrTalk(
        0x10A,
        (
            "#6P#00606FBut surely, if the strength increases\x01",
            "Will the success rate of the strategy also increase?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5B1")

    label("loc_E558")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E5B1")

    ChrTalk(
        0x106,
        (
            "#6P#10703FBut surely, as the strength increases\x01",
            "The success rate of the strategy is likely to rise as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E60D")

    ChrTalk(
        0x109,
        (
            "#6P#10108FIt's a bit complicated but … ….\x01",
            "You may consider it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6B0")

    label("loc_E60D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E65D")

    ChrTalk(
        0x106,
        (
            "#6P#10708FEven if I consult the section chief\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6B0")

    label("loc_E65D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6B0")

    ChrTalk(
        0x10A,
        (
            "#6P#00601FConsult Sergei also\x01",
            "Maybe you should consider it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6B0")


    ChrTalk(
        0x101,
        (
            "#00006F#12PUnderstood….\x02\x03",
            "#00000FWe will guide you to this base\x01",
            "Please come with us.\x02",
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
            "After that, Lloyd's\x01",
            "Introducing Kirika to Mr. Sergei … …\x02\x03",
            "After exchanging information with each other\x01",
            "I was supposed to cooperate with the strategy.\x02\x03",
            "And by Roberts chief\x01",
            "Hacking to the Orchis Tower\x01",
            "At last he succeeded …\x02\x03",
            "\"Orkis Tower Capture Strategy\"\x01",
            "It was decided to be decided immediately.\x07\x00\x02",
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

    # Function_43_C153 end

    def Function_44_E84A(): pass

    label("Function_44_E84A")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E998")
    SetChrPos(0x102, 280, 0, -7500, 0)
    Jump("loc_EA2B")

    label("loc_E998")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9BE")
    SetChrPos(0x103, 280, 0, -7500, 0)
    Jump("loc_EA2B")

    label("loc_E9BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9E4")
    SetChrPos(0x104, 280, 0, -7500, 0)
    Jump("loc_EA2B")

    label("loc_E9E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA0A")
    SetChrPos(0x109, 280, 0, -7500, 0)
    Jump("loc_EA2B")

    label("loc_EA0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA2B")
    SetChrPos(0x105, 280, 0, -7500, 0)

    label("loc_EA2B")

    SetChrPos(0x1A1, -90, 0, -8180, 0)
    SetChrChipByIndex(0x29, 0x1E)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, -40, 0, -3180, 0)

    def lambda_EA64():
        OP_95(0x29, -40, 0, 1990, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_EA64)
    SoundLoad(450)
    Sound(450, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "Hey, that old lady ……\x01",
            "I came in from the top of the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Yup……\x01",
            "What is it, that person.\x02",
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
            "#5SYeah, it's loud!\x01",
            "It is not a spectacle! It is!#3S\x02",
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
        "Huh! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Okay, scary! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FLet's! It is!\x02",
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

    def lambda_EC26():
        OP_95(0xFE, -420, 0, 150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EC26)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC6A")

    def lambda_EC50():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EC50)
    Jump("loc_ED21")

    label("loc_EC6A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC99")

    def lambda_EC7F():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EC7F)
    Jump("loc_ED21")

    label("loc_EC99")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ECC8")

    def lambda_ECAE():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ECAE)
    Jump("loc_ED21")

    label("loc_ECC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ECF7")

    def lambda_ECDD():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ECDD)
    Jump("loc_ED21")

    label("loc_ECF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED21")

    def lambda_ED0C():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ED0C)

    label("loc_ED21")


    def lambda_ED26():
        OP_95(0xFE, -90, 0, -1650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_ED26)
    WaitChrThread(0x1A1, 1)

    ChrTalk(
        0x29,
        "Become It is!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        "#5SWhat a persistent person!#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        "#5SYou guys are too bad!#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EE97")

    ChrTalk(
        0x102,
        (
            "#00106FTo be honest, this line of words\x01",
            "What is it ……\x02\x03",
            "#00101F… … There is no escape anymore.\x01",
            "Please surrender to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0A8")

    label("loc_EE97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF16")

    ChrTalk(
        0x103,
        (
            "#00206FThat word,\x01",
            "I will return it as it is.\x02\x03",
            "#00200FThere should not be an escape place anymore ……\x01",
            "Please do not apologize.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0A8")

    label("loc_EF16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF90")

    ChrTalk(
        0x104,
        (
            "#00306FThis is the dialogue of this one.\x02\x03",
            "#00302FWell, is not it anymore?\x01",
            "It's a guy when you pay your annual salary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0A8")

    label("loc_EF90")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F022")

    ChrTalk(
        0x109,
        (
            "#10106FHere, this serif\x01",
            "I feel like that ….\x02\x03",
            "#10101F……Anyways.\x01",
            "Escape is impossible anymore.\x01",
            "Please give up and down quietly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0A8")

    label("loc_F022")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F0A8")

    ChrTalk(
        0x105,
        (
            "#10306FWell, only for you\x01",
            "I do not want to be told Madam.\x02\x03",
            "#10302FWho is quiet\x01",
            "I think it is for myself … ….?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0A8")


    ChrTalk(
        0x1A1,
        (
            "That's right!\x01",
            "Give up ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Happy\x01",
            "If I think what to say … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        "Okay, remember when!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "As long as this continent ……\x01",
            "I can not get away with me\x01",
            "That is impossible!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x29, 0x0, 0x1F4)
    OP_95(0x29, 0, 0, 8290, 4000, 0x0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(200)

    def lambda_F19B():
        OP_95(0xFE, -10, 0, 10140, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_F19B)
    Sleep(200)

    def lambda_F1B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_F1B8)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FDamn it … damn\x01",
            "I do not understand the meaning … …!\x02\x03",
            "#00007FAnyway, we'll chase everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        "wait~~~~~~!\x02",
    )

    CloseMessageWindow()

    def lambda_F237():
        OP_95(0xFE, -420, 0, 10450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F237)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F27E")

    def lambda_F264():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F264)
    Jump("loc_F335")

    label("loc_F27E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F2AD")

    def lambda_F293():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F293)
    Jump("loc_F335")

    label("loc_F2AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F2DC")

    def lambda_F2C2():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F2C2)
    Jump("loc_F335")

    label("loc_F2DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F30B")

    def lambda_F2F1():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F2F1)
    Jump("loc_F335")

    label("loc_F30B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F335")

    def lambda_F320():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F320)

    label("loc_F335")

    Sleep(100)

    def lambda_F33D():
        OP_95(0xFE, -90, 0, 10050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_F33D)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F462")
    SetChrPos(0x102, 130, 0, -6140, 0)
    Jump("loc_F4F5")

    label("loc_F462")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F488")
    SetChrPos(0x103, 130, 0, -6140, 0)
    Jump("loc_F4F5")

    label("loc_F488")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F4AE")
    SetChrPos(0x104, 130, 0, -6140, 0)
    Jump("loc_F4F5")

    label("loc_F4AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F4D4")
    SetChrPos(0x109, 130, 0, -6140, 0)
    Jump("loc_F4F5")

    label("loc_F4D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F4F5")
    SetChrPos(0x105, 130, 0, -6140, 0)

    label("loc_F4F5")

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
            "The train also started …\x01",
            "I think I will finally get a breath.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2B,
        "Man",
        (
            "Ah……\x01",
            "Crossbell and this is Osaraba.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2B,
        "Man",
        (
            "To fellows who were caught in the black moon\x01",
            "To be honest, I am sorry, but …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2C,
        "Man",
        (
            "What is the preparation this time\x01",
            "Just saying it was not enough.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2C,
        "Man",
        (
            "In any case,\x01",
            "Make sure to sanction … …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2D,
        "Voice of a man",
        (
            "HOW … … Interesting story\x01",
            "It seems to be doing.\x02",
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

    def lambda_F7B2():
        OP_95(0xFE, 30, 0, 1880, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_F7B2)

    def lambda_F7CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_F7CC)
    Sleep(600)

    def lambda_F7E0():
        OP_95(0xFE, -110, 0, 2990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_F7E0)

    def lambda_F7FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_F7FA)
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
            "Oh … oh ……\x01",
            "You are …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x2B,
        "Man",
        "Black moon ……! Is it?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x2C,
        "Man",
        (
            "Damn it … damn\x01",
            "Was it being tailed …?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "Mr. Tsao will tell you\x01",
            "It will not be missed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "Anti-East / immigrant policy-minded people … …\x01",
            "We will have you come with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "Depending on the City of Altair,\x01",
            "To the crossbell\x01",
            "Shall I transfer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "Well, why do not you …\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x29,
        "Voice of an old woman",
        "── Anyone, there's a brat!\x02",
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

    def lambda_FA14():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_FA14)
    Sleep(50)

    def lambda_FA24():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_FA24)

    ChrTalk(
        0x2D,
        "Huh……\x02",
    )

    CloseMessageWindow()

    def lambda_FA3D():
        OP_95(0xFE, 10, 0, 2460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_FA3D)
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
        "Go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "Hooh! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Aitata …\x01",
            "This Noromaga,\x01",
            "So I told you! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Do not you think?\x01",
            "It's not the time to stop!\x02",
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
        "(Er, uh … ….)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "(What is this, old lady.\x02",
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x29, 0x10E, 0x1F4)

    ChrTalk(
        0x29,
        "…… …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "You mean, maybe … …\x01",
            "Have you been chased by these guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "Oh, ah ……\x01",
            "To be honest, I was saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        "You are an benefactor!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        "Hun, I do not know what it is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "…… To counter them\x01",
            "Even one person needs a lot of friends.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        (
            "#5SYou guys!\x01",
            "If you feel a bit even a little\x01",
            "Come with me!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x29,
        (
            "#5SWell,\x01",
            "You can escape as well\x01",
            "It might be!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "Well, yeah …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "Really……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        "Do not play horror, mot!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Republic-based terrorists")

    AnonymousTalk(
        0xFF,
        "Wow, I understand! It is!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE44")
    BeginChrThread(0x102, 1, 0, 47)
    Jump("loc_FEAB")

    label("loc_FE44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE5F")
    BeginChrThread(0x103, 1, 0, 47)
    Jump("loc_FEAB")

    label("loc_FE5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE7A")
    BeginChrThread(0x104, 1, 0, 47)
    Jump("loc_FEAB")

    label("loc_FE7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE95")
    BeginChrThread(0x109, 1, 0, 47)
    Jump("loc_FEAB")

    label("loc_FE95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FEAB")
    BeginChrThread(0x105, 1, 0, 47)

    label("loc_FEAB")

    Sleep(300)
    BeginChrThread(0x1A1, 1, 0, 47)
    Sleep(2000)

    ChrTalk(
        0x1A1,
        "#7AWait, wait ~! It is!\x02",
    )

    WaitChrThread(0x1A1, 1)
    OP_57(0x0)
    OP_5A()
    Sleep(700)

    ChrTalk(
        0x2E,
        "Damn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "Wow, what was it ……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FFE6")
    SetChrPos(0x102, -650, 0, -8160, 0)
    Jump("loc_10079")

    label("loc_FFE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1000C")
    SetChrPos(0x103, -650, 0, -8160, 0)
    Jump("loc_10079")

    label("loc_1000C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10032")
    SetChrPos(0x104, -650, 0, -8160, 0)
    Jump("loc_10079")

    label("loc_10032")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10058")
    SetChrPos(0x109, -650, 0, -8160, 0)
    Jump("loc_10079")

    label("loc_10058")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10079")
    SetChrPos(0x105, -650, 0, -8160, 0)

    label("loc_10079")

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
        "Ha Ha……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "Well, on the roof again\x01",
            "It seems they climbed …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI mean,\x01",
            "I was bringing someone\x01",
            "It looks like … ….\x02\x03",
            "#00001FMaybe a friend\x01",
            "Were you hiding? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "Well, that should be ……\x01",
            "Her novicles last long\x01",
            "Everyone should have arrested ~! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10318")

    ChrTalk(
        0x102,
        (
            "#00101FAnd anyway … …\x01",
            "Let's follow now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1045E")

    label("loc_10318")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1035D")

    ChrTalk(
        0x103,
        (
            "#00201Fanyway……\x01",
            "Let 's keep going now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1045E")

    label("loc_1035D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_103B2")

    ChrTalk(
        0x104,
        (
            "#00301FWell, I do not know well …\x01",
            "Let's chase after now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1045E")

    label("loc_103B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10407")

    ChrTalk(
        0x109,
        (
            "#10101FOkay, I do not understand well ….\x01",
            "Let's follow now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1045E")

    label("loc_10407")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1045E")

    ChrTalk(
        0x105,
        (
            "#10302FTentatively,\x01",
            "Is not it okay to leave it on?\x01",
            "Let's follow now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1045E")


    ChrTalk(
        0x101,
        (
            "#00003FThat 's right.\x02\x03",
            "#00001F── Okay, I will continue pursuing!\x02",
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

    # Function_44_E84A end

    def Function_45_104C2(): pass

    label("Function_45_104C2")

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

    # Function_45_104C2 end

    def Function_46_1051E(): pass

    label("Function_46_1051E")

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

    # Function_46_1051E end

    def Function_47_10574(): pass

    label("Function_47_10574")

    OP_95(0xFE, 0, 0, 8350, 4000, 0x0)

    def lambda_1058D():
        OP_95(0xFE, 0, 0, 10000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1058D)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_47_10574 end

    def Function_48_105AE(): pass

    label("Function_48_105AE")

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

    # Function_48_105AE end

    def Function_49_10605(): pass

    label("Function_49_10605")

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

    # Function_49_10605 end

    def Function_50_1065C(): pass

    label("Function_50_1065C")

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

    # Function_50_1065C end

    SaveToFile()

Try(main)
