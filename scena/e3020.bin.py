from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3020.bin",                # FileName
        "e3020",                    # MapName
        "e3020",                    # Location
        0x00D0,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("e3020", "e3020_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e3020",                  # 0
        "Knight Abbas",           # 1
        "Jona",                   # 2
        "Wazy",                   # 3
        "Tio",                    # 4
        "Fran",                   # 5
        "Rixia",                  # 6
        "Randy",                  # 7
        "Grace",                  # 8
        "Noｱl",                  # 9
        "Elie",                   # 10
        "Chairman MacDowell",     # 11
        "Divine Wolf Zeit",       # 12
        "Detective Dudley",       # 13
        "Squire Ventos",          # 14
        "Squire Juno",            # 15
        "Squire Cesar",           # 16
        "Squire Marcus",          # 17
        "Sister Ries",            # 18
        "Father Kevin",           # 19
        "Noｱl",                  # 20
        "Fran",                   # 21
        "Grace",                  # 22
        " ",                      # 23
        "SE制御",                 # 24
    ))

    AddCharChip((
        "chr/ch06712.itc",                   # 00
        "chr/ch06100.itc",                   # 01
        "chr/ch03100.itc",                   # 02
        "chr/ch03102.itc",                   # 03
        "chr/ch00202.itc",                   # 04
        "chr/ch06902.itc",                   # 05
        "chr/ch03200.itc",                   # 06
        "chr/ch00300.itc",                   # 07
        "chr/ch06000.itc",                   # 08
        "chr/ch02900.itc",                   # 09
        "chr/ch00102.itc",                   # 0A
        "chr/ch05800.itc",                   # 0B
        "chr/ch02710.itc",                   # 0C
        "chr/ch00900.itc",                   # 0D
        "chr/ch48400.itc",                   # 0E
        "chr/ch48402.itc",                   # 0F
        "chr/ch02702.itc",                   # 10
        "chr/ch02708.itc",                   # 11
        "chr/ch00200.itc",                   # 12
        "chr/ch00302.itc",                   # 13
        "chr/ch02902.itc",                   # 14
        "chr/ch03202.itc",                   # 15
        "chr/ch00902.itc",                   # 16
        "chr/ch06102.itc",                   # 17
        "chr/ch06002.itc",                   # 18
        "chr/ch05802.itc",                   # 19
        "chr/ch06710.itc",                   # 1A
        "chr/ch06900.itc",                   # 1B
    ))

    DeclNpc(4294967257, 490,     2500,    0,    261,  0x0, 0,   0,   0,   255, 255, 1,   26,  255,  0)
    DeclNpc(4294964177, 4294965946, 7039,    315,  389,  0x0, 0,   1,   0,   255, 255, 1,   34,  255,  0)
    DeclNpc(101790,  150,     4294873337, 90,   389,  0x0, 0,   2,   0,   0,   0,   1,   15,  255,  0)
    DeclNpc(4294964177, 4294965946, 7039,    315,  389,  0x0, 0,   18,  0,   0,   0,   1,   2,   255,  0)
    DeclNpc(3000,    4294965946, 6960,    45,   389,  0x0, 0,   5,   0,   255, 255, 1,   31,  255,  0)
    DeclNpc(4294965796, 0,       4294965796, 0,    389,  0x0, 0,   6,   0,   0,   0,   1,   19,  255,  0)
    DeclNpc(98970,   170,     4294966326, 0,    389,  0x0, 0,   7,   0,   0,   0,   1,   6,   255,  0)
    DeclNpc(4294964296, 4294965806, 6000,    0,    389,  0x0, 0,   8,   0,   255, 255, 1,   37,  255,  0)
    DeclNpc(100309,  170,     959,     270,  389,  0x0, 0,   9,   0,   0,   0,   1,   12,  255,  0)
    DeclNpc(100169,  100,     4294864576, 270,  389,  0x0, 0,   10,  0,   0,   0,   1,   0,   255,  0)
    DeclNpc(98440,   100,     4294866186, 180,  389,  0x0, 0,   11,  0,   255, 255, 1,   39,  255,  0)
    DeclNpc(97610,   0,       4294870227, 180,  405,  0x0, 0,   12,  0,   255, 255, 1,   22,  255,  0)
    DeclNpc(97639,   170,     959,     90,   389,  0x0, 0,   13,  0,   255, 255, 1,   24,  255,  0)
    DeclNpc(103569,  0,       4294870207, 270,  257,  0x0, 0,   14,  0,   0,   0,   1,   43,  255,  0)
    DeclNpc(103949,  0,       4294967087, 270,  257,  0x0, 0,   14,  0,   0,   0,   1,   46,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   14,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   14,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   9,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   8,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(102510,  0,       4294870276, 1000,    103570,  1500,    4294870206, 0x007E, 1,  42, 0x0000)
    DeclActor(102710,  0,       4294967096, 400,     103950,  1500,    4294967086, 0x007E, 1,  45, 0x0000)
    DeclActor(2350,    0,       4294875066, 800,     2350,    1500,    4294875066, 0x007C, 1,  48, 0x0000)
    DeclActor(103750,  0,       4294861656, 2000,    103750,  1500,    4294861656, 0x007C, 1,  49, 0x0000)

    ChipFrameInfo(1260, 0)                                       # 0

    ScpFunction((
        "Function_0_4EC",          # 00, 0
        "Function_1_59C",          # 01, 1
        "Function_2_116A",         # 02, 2
        "Function_3_12CA",         # 03, 3
        "Function_4_12EA",         # 04, 4
        "Function_5_13FF",         # 05, 5
        "Function_6_14BC",         # 06, 6
        "Function_7_1573",         # 07, 7
        "Function_8_1A5F",         # 08, 8
        "Function_9_23F2",         # 09, 9
        "Function_10_38C5",        # 0A, 10
        "Function_11_3907",        # 0B, 11
        "Function_12_3F17",        # 0C, 12
        "Function_13_3FD4",        # 0D, 13
        "Function_14_46BB",        # 0E, 14
        "Function_15_46D6",        # 0F, 15
        "Function_16_54E7",        # 10, 16
        "Function_17_60CD",        # 11, 17
        "Function_18_6609",        # 12, 18
        "Function_19_662E",        # 13, 19
        "Function_20_672E",        # 14, 20
        "Function_21_75DE",        # 15, 21
        "Function_22_7853",        # 16, 22
        "Function_23_8D58",        # 17, 23
        "Function_24_909F",        # 18, 24
        "Function_25_949F",        # 19, 25
        "Function_26_94B5",        # 1A, 26
        "Function_27_94CE",        # 1B, 27
        "Function_28_9BDD",        # 1C, 28
        "Function_29_9BFD",        # 1D, 29
        "Function_30_AF90",        # 1E, 30
        "Function_31_B482",        # 1F, 31
        "Function_32_BE10",        # 20, 32
        "Function_33_BE3F",        # 21, 33
        "Function_34_BE62",        # 22, 34
        "Function_35_BE87",        # 23, 35
        "Function_36_BE9F",        # 24, 36
        "Function_37_BEC2",        # 25, 37
        "Function_38_BEDC",        # 26, 38
        "Function_39_CAF9",        # 27, 39
        "Function_40_CD49",        # 28, 40
        "Function_41_D2C5",        # 29, 41
        "Function_42_D2EA",        # 2A, 42
        "Function_43_D87B",        # 2B, 43
        "Function_44_D89B",        # 2C, 44
        "Function_45_DD3E",        # 2D, 45
    ))


    def Function_0_4EC(): pass

    label("Function_0_4EC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_524"),
        (1, "loc_530"),
        (2, "loc_53C"),
        (3, "loc_548"),
        (4, "loc_554"),
        (5, "loc_560"),
        (6, "loc_56C"),
        (SWITCH_DEFAULT, "loc_578"),
    )


    label("loc_524")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_530")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_53C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_548")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_554")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_560")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_56C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_578")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_584")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_59B")

    Return()

    # Function_0_4EC end

    def Function_1_59C(): pass

    label("Function_1_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_6F5")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 104200, 100, 5070, 90)
    Jump("loc_61E")

    label("loc_5F5")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 97740, 0, -98460, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)

    label("loc_61E")

    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrPos(0x10, 100250, 100, -104800, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x16)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_F57")

    label("loc_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_84E")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74E")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 104200, 100, 5070, 90)
    Jump("loc_777")

    label("loc_74E")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 97740, 0, -98460, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)

    label("loc_777")

    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrPos(0x10, 100250, 100, -104800, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x16)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_F57")

    label("loc_84E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_963")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2110, -1490, 6190, 315)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x16)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_F57")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A8D")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 97620, 170, 970, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -3050, 0, -2960, 0)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x19)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A88")
    SetChrFlags(0x12, 0x10)

    label("loc_A88")

    Jump("loc_F57")

    label("loc_A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_BCF")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 97740, 0, -98460, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1340, 0, -1280, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 97640, 170, 960, 90)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrPos(0x8, 140, 0, -1320, 89)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x18)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrPos(0xF, 100170, 100, -102720, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x19)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC5")
    SetChrFlags(0xB, 0x10)

    label("loc_BC5")

    SetChrFlags(0x13, 0x10)
    Jump("loc_F57")

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_CD8")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrPos(0xE, 100170, 100, -102720, 270)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3750, 0, -2770, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, 2620, 0, -2780, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD3")
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_CD3")

    Jump("loc_F57")

    label("loc_CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_DC1")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 100560, 0, 2190, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 100170, 100, -102720, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x18)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrPos(0xF, 98440, 100, -101110, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 7)), scpexpr(EXPR_END)), "loc_DBC")
    SetChrFlags(0xF, 0x10)

    label("loc_DBC")

    Jump("loc_F57")

    label("loc_DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E4E")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDE")
    SetChrFlags(0xB, 0x10)

    label("loc_DDE")

    SetChrPos(0xB, 97740, 0, -98460, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1410, 0, -100570, 270)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_F57")

    label("loc_E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_EEC")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrPos(0x8, -2110, -1490, 6190, 315)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE7")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_EE7")

    Jump("loc_F57")

    label("loc_EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_F57")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F41")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    Jump("loc_F57")

    label("loc_F41")

    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7C")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F93")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAA")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC1")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_FD8")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 4)
    Jump("loc_1169")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_FEC")
    ClearScenarioFlags(0x22, 1)
    Event(0, 8)
    Jump("loc_1169")

    label("loc_FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1003")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 1)
    Event(0, 9)
    Jump("loc_1169")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1017")
    ClearScenarioFlags(0x22, 3)
    Event(0, 13)
    Jump("loc_1169")

    label("loc_1017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_102B")
    ClearScenarioFlags(0x22, 4)
    Event(0, 15)
    Jump("loc_1169")

    label("loc_102B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_103F")
    ClearScenarioFlags(0x22, 5)
    Event(0, 16)
    Jump("loc_1169")

    label("loc_103F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1059")
    ClearScenarioFlags(0x22, 6)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 17)
    Jump("loc_1169")

    label("loc_1059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_106D")
    ClearScenarioFlags(0x22, 7)
    Event(0, 20)
    Jump("loc_1169")

    label("loc_106D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_1081")
    ClearScenarioFlags(0x23, 0)
    Event(0, 22)
    Jump("loc_1169")

    label("loc_1081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1095")
    ClearScenarioFlags(0x23, 1)
    Event(0, 24)
    Jump("loc_1169")

    label("loc_1095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_10A9")
    ClearScenarioFlags(0x23, 2)
    Event(0, 27)
    Jump("loc_1169")

    label("loc_10A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_10C0")
    ClearScenarioFlags(0x23, 3)
    SetScenarioFlags(0x0, 0)
    Event(0, 29)
    Jump("loc_1169")

    label("loc_10C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_10D4")
    ClearScenarioFlags(0x23, 4)
    Event(0, 30)
    Jump("loc_1169")

    label("loc_10D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_END)), "loc_10E8")
    ClearScenarioFlags(0x23, 5)
    Event(0, 31)
    Jump("loc_1169")

    label("loc_10E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_10FC")
    ClearScenarioFlags(0x23, 6)
    Event(0, 38)
    Jump("loc_1169")

    label("loc_10FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 7)), scpexpr(EXPR_END)), "loc_1110")
    ClearScenarioFlags(0x23, 7)
    Event(0, 40)
    Jump("loc_1169")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 0)), scpexpr(EXPR_END)), "loc_1124")
    ClearScenarioFlags(0x24, 0)
    Event(0, 42)
    Jump("loc_1169")

    label("loc_1124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 1)), scpexpr(EXPR_END)), "loc_1138")
    ClearScenarioFlags(0x24, 1)
    Event(0, 44)
    Jump("loc_1169")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 2)), scpexpr(EXPR_END)), "loc_114C")
    ClearScenarioFlags(0x24, 2)
    Event(0, 3)
    Jump("loc_1169")

    label("loc_114C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_1169")
    ClearScenarioFlags(0x24, 3)
    SetChrPos(0x0, 102230, 0, -105070, 90)

    label("loc_1169")

    Return()

    # Function_1_59C end

    def Function_2_116A(): pass

    label("Function_2_116A")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1187")
    OP_24(0x1F2)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_11A6")

    label("loc_1187")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")
    Sound(498, 1, 50, 0)
    Jump("loc_11A6")

    label("loc_11A0")

    Sound(498, 1, 100, 0)

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11C0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_11D7")

    label("loc_11C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11D7")

    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1203")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)

    label("loc_1203")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1214")
    OP_66(0x3, 0x1)

    label("loc_1214")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF4080FF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1236")
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x1)
    Jump("loc_123C")

    label("loc_1236")

    OP_10(0x7, 0x0)
    OP_10(0x0, 0x1)

    label("loc_123C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_126A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1261")
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_126A")

    label("loc_1261")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_126A")

    ClearMapObjFlags(0x3, 0x10)
    SetMapFlags(0x10000)
    SetScenarioFlags(0x26, 0)
    SetScenarioFlags(0x26, 4)
    SetScenarioFlags(0x26, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_END)), "loc_128A")
    SetScenarioFlags(0x26, 2)

    label("loc_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1296")
    SetScenarioFlags(0x26, 1)

    label("loc_1296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_12A2")
    SetScenarioFlags(0x26, 3)

    label("loc_12A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_12B1")
    SetScenarioFlags(0x27, 0)
    ClearScenarioFlags(0x26, 6)

    label("loc_12B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_12BD")
    SetScenarioFlags(0x26, 5)

    label("loc_12BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12C9")
    SetScenarioFlags(0x27, 1)

    label("loc_12C9")

    Return()

    # Function_2_116A end

    def Function_3_12CA(): pass

    label("Function_3_12CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -150, 0, -88230, 180)
    EventEnd(0x5)
    Return()

    # Function_3_12CA end

    def Function_4_12EA(): pass

    label("Function_4_12EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    SoundLoad(132)
    SoundLoad(497)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1311")
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_1311")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetEventSkip(0x0, "loc_13C4")
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, -30000, 990000, 0)

    def lambda_1352():
        OP_96(0x1E, 0xFFF0BDC0, 0xFFFEA070, 0xF4A10, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1352)
    OP_F0(0x1, 0x7D0)
    OP_68(-1005000, -50000, 1005000, 0)
    MoveCamera(145, -35, 0, 0)
    MoveCamera(140, -30, 0, 2500)
    OP_6E(500, 0)
    SetCameraDistance(35000, 0)
    Sleep(2000)
    StopSound(132, 1000, 80)
    StopSound(497, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_13C4")

    EndChrThread(0x1E, 0x1)
    SetChrPos(0x0, 0, 0, -2940, 0)
    OP_31(0x1)
    Sleep(0)
    OP_6F(0xFF)
    OP_69(0xFF, 0x0)
    Sound(498, 1, 100, 0)
    Sleep(1500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x6)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_4_12EA end

    def Function_5_13FF(): pass

    label("Function_5_13FF")

    SoundLoad(132)
    SoundLoad(497)
    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_14BB")
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1050000, 120000, 920000, 0)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)

    def lambda_144E():
        OP_96(0x1E, 0xFFEFFA70, 0xEA60, 0xE7EF0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_144E)
    OP_F0(0x1, 0x7D0)
    OP_68(-976190, -500, 1037099, 0)
    MoveCamera(35, 39, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(230250, 0)
    Sleep(2000)
    StopSound(132, 1000, 80)
    StopSound(497, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    SetEventSkip(0x1, 0x0)

    label("loc_14BB")

    Return()

    # Function_5_13FF end

    def Function_6_14BC(): pass

    label("Function_6_14BC")

    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_1572")
    FadeToBright(1000, 0)
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)

    def lambda_14F9():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_14F9)
    OP_F0(0x1, 0x7D0)
    OP_68(-1000000, 0, 800000, 0)
    MoveCamera(30, -7, 0, 0)
    MoveCamera(20, -7, 0, 3000)
    OP_6E(500, 0)
    SetCameraDistance(111000, 0)
    Sleep(300)
    Sound(499, 0, 100, 0)
    Sleep(1700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    StopBGM(0x7D0)
    WaitBGM()
    SetEventSkip(0x1, 0x0)

    label("loc_1572")

    Return()

    # Function_6_14BC end

    def Function_7_1573(): pass

    label("Function_7_1573")

    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B3")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_16A3")

    label("loc_15B3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D6")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_16A3")

    label("loc_15D6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F9")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_16A3")

    label("loc_15F9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161C")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_16A3")

    label("loc_161C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_163F")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_16A3")

    label("loc_163F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1662")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_16A3")

    label("loc_1662")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1685")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_16A3")

    label("loc_1685")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A3")
    SetScenarioFlags(0x3C, 7)

    label("loc_16A3")

    PartySelect(2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_END)),
        (0, "loc_175C"),
        (1, "loc_1775"),
        (3, "loc_178E"),
        (5, "loc_17A7"),
        (7, "loc_17C0"),
        (9, "loc_17D9"),
        (51, "loc_17F2"),
        (17, "loc_180B"),
        (19, "loc_1824"),
        (21, "loc_183D"),
        (23, "loc_1856"),
        (24, "loc_186F"),
        (25, "loc_1888"),
        (26, "loc_18A1"),
        (27, "loc_18BA"),
        (28, "loc_18D3"),
        (29, "loc_18EC"),
        (33, "loc_1905"),
        (35, "loc_191E"),
        (37, "loc_1937"),
        (41, "loc_1950"),
        (43, "loc_1969"),
        (46, "loc_1982"),
        (52, "loc_199B"),
        (47, "loc_19B4"),
        (48, "loc_19D6"),
        (50, "loc_19F8"),
        (49, "loc_1A1A"),
        (42, "loc_1A3C"),
        (SWITCH_DEFAULT, "loc_1A5E"),
    )


    label("loc_175C")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("c0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1775")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r0000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_178E")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r0030", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17A7")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17C0")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1030", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17D9")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17F2")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1610", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_180B")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1824")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2030", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_183D")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2050", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1856")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r3000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_186F")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t0500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1888")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t0000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18A1")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t1310", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18BA")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t2500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18D3")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t2000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18EC")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t1500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1905")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m1000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_191E")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2070", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1937")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t6000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1950")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m4200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1969")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m4000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1982")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m4250", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_199B")

    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_19B4")

    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("c0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_19D6")

    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t0000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_19F8")

    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1610", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1A1A")

    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t1500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1A3C")

    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m9000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1A5E")

    Return()

    # Function_7_1573 end

    def Function_8_1A5F(): pass

    label("Function_8_1A5F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17002.eff")
    SoundLoad(493)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    ClearMapObjFlags(0x1, 0x4)
    OP_32(0x4, 0x0, 0x52)
    OP_32(0x4, 0x5, 0x64)
    OP_42(0x4, 0x441, 0xFF)
    OP_42(0x4, 0x5ED, 0xFF)
    OP_42(0x4, 0x651, 0xFF)
    OP_38(0x4, 0x81, 0x1)
    OP_38(0x4, 0x82, 0x2)
    OP_38(0x4, 0x83, 0x2)
    OP_38(0x4, 0x84, 0x2)
    OP_38(0x4, 0x85, 0x2)
    OP_38(0x4, 0x86, 0x1)
    OP_42(0x4, 0xA1, 0x2)
    OP_42(0x4, 0x94, 0x3)
    OP_42(0x4, 0xB8, 0x4)
    OP_42(0x4, 0x89, 0x5)
    AddCraft(0x4, 0xC1)
    AddCraft(0x4, 0xC3)
    OP_32(0x6, 0x0, 0x55)
    OP_32(0x6, 0x5, 0x64)
    OP_38(0x6, 0x81, 0x2)
    OP_38(0x6, 0x82, 0x2)
    OP_38(0x6, 0x83, 0x2)
    OP_38(0x6, 0x84, 0x2)
    OP_38(0x6, 0x85, 0x2)
    OP_38(0x6, 0x86, 0x2)
    OP_42(0x6, 0x474, 0xFF)
    OP_42(0x6, 0x477, 0xFF)
    OP_42(0x6, 0x478, 0xFF)
    OP_42(0x6, 0x3A, 0x3)
    OP_42(0x6, 0x27, 0x4)
    SetChrChipPat(0x4, 0x1, 0x1F)
    LoadChrChipPat()
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    AddCraft(0x6, 0xD2)
    AddCraft(0x6, 0xD3)
    AddCraft(0x6, 0xD4)
    RemoveCraft(0x6, 0x53)
    RemoveCraft(0x6, 0x61)
    RemoveCraft(0x6, 0x69)
    RemoveCraft(0x6, 0x72)
    RemoveCraft(0x6, 0x79)
    RemoveCraft(0x6, 0x7C)
    RemoveCraft(0x6, 0x85)
    RemoveCraft(0x6, 0x87)
    RemoveCraft(0x6, 0x34)
    RemoveCraft(0x6, 0x3E)
    RemoveCraft(0x6, 0x48)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrChipByIndex(0x15, 0xF)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x14)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -750, 0)
    SetChrPos(0x15, -3100, -1350, 7100, 315)
    OP_68(-280, 1800, -1040, 0)
    MoveCamera(44, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(1170, 1800, 3900, 3000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-1360, 3800, 2000, 0)
    OP_68(-1360, 1800, 2720, 4000)
    MoveCamera(44, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17820, 0)
    Sleep(1000)
    Sound(943, 2, 70, 0)
    OP_71(0x1, 0x1, 0x1E, 0x0, 0x8)
    OP_79(0x1)
    Sound(143, 0, 50, 0)
    OP_24(0x3AF)
    Sleep(500)
    SetChrSubChip(0x105, 0x2)
    OP_70(0x1, 0x1F)
    Sound(72, 0, 100, 0)
    Sleep(300)
    SetMessageWindowPos(85, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──As per arrangements,\x01",
            "we'll take that "doll".\x02\x03",
            "Be very careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10404F#6PHu hu, likewise,\x01",
            ""Heretic Hunter" ──no, "Thousand Protector".\x02\x03",
            "#10402FYou just changed your nickname,\x01",
            "so may you not be dismissed.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(140, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ha ha, indeed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#12102F#6PTo think you received the nickname from\x01",
            "Lady Rufina, the Thousand Arms...\x02\x03",
            "She gave you a nice alias, Lord Graham.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(145, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...Thank you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("Sister Ries")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "............\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00008F#12P(A lot of things seem to have happened...)\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(85, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Lloyd.\x01",
            "I think it's hard, but do your very best.\x02\x03",
            "In the present situation in Crossbell,\x01",
            "you can't count on help from the outside.\x02\x03",
            "If there's something crucial, that's the bonds\x01",
            "you've fostered until now in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00005F#12PThe bonds I've fostered...\x02\x03",
            "#00004F──I understand.\x01",
            "I'll bear it in mind.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    OP_70(0x1, 0x20)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("Sister Ries")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mr. Lloyd, may Aidios protect you.\x02\x03",
            "Also, please take\x01",
            "care of Miss Elie.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000F#12PYes, of course!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_70(0x1, 0x1E)
    Sound(73, 0, 100, 0)
    Sleep(300)
    SetCameraDistance(19650, 3000)
    StopBGM(0xBB8)
    Sleep(1000)
    Sound(943, 2, 60, 0)
    OP_71(0x1, 0x2F, 0x4C, 0x0, 0x8)
    Sleep(500)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x79)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7542", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_79(0x1)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(1002, 0, 40, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 2000, 0, 12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(
        0x101,
        "#00011F#12PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#11PI activated an optical camouflage mechanism.\x02\x03",
            "Naturally it's not perfect,\x01",
            "it also has the demerit that,\x01",
            "when used, the speed drops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11PIf we infiltrated like this,\x01",
            "that high mobility type of doll\x01",
            "would immediately ambush us.\x02\x03",
            "#10401FSince even if we fought it\x01",
            "openly we would have no chance,\x01",
            "we'll have the No. 5 lure it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PI see...\x01",
            "We'll use that as a chance to infiltrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3C#12PHm, then I shall see the skills\x01",
            "of the Grals' protectors.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20650, 2000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x105, 0x4)
    OP_6F(0x79)
    OP_24(0x3AF)
    SetScenarioFlags(0x22, 2)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1A5F end

    def Function_9_23F2(): pass

    label("Function_9_23F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SoundLoad(497)
    SoundLoad(498)
    SoundLoad(132)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis335.itp")
    CreatePortrait(1, 198, 150, 214, 166, 0, 0, 512, 256, 488, 0, 504, 16, 0xFFFFFF, 0x0, "c_vis335.itp")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 100230, 50, -102650, 270)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x105, 98470, 50, -101100, 180)
    SetChrChipByIndex(0x107, 0x10)
    SetChrSubChip(0x107, 0x0)
    SetChrPos(0x107, 100400, 0, -101700, 270)
    BeginChrThread(0x107, 3, 0, 0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 750, 0, -2500, 270)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    OP_4B(0x15, 0xFF)
    SetChrChipByIndex(0x16, 0xE)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    OP_4B(0x16, 0xFF)
    SetChrPos(0x15, -750, 0, -2000, 90)
    SetChrPos(0x16, -750, 0, -3000, 90)
    SetMapObjFlags(0x0, 0x1000)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    OP_68(-1000000, 1500, 1000000, 0)
    MoveCamera(120, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(50000, 0)
    MoveCamera(135, 10, 0, 6000)
    SetCameraDistance(40000, 6000)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0xFFFF)
    Sleep(500)
    Sound(498, 2, 100, 0)
    OP_68(1500, 1000, 500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    OP_68(1500, 1000, -2500, 6000)
    FadeToBright(1000, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_63(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_68(100110, 3000, -101660, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17730, 0)
    OP_68(100110, 1000, -101660, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10406F#5P──Somehow we managed to infiltrate,\x01",
            "but it seems that Crossbell itself has\x01",
            "become one with the "Sept-Terrion".\x02\x03",
            "#10401FIf we don't move carefully from now on,\x01",
            "dolls will probably come at us again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PSo there's a limit to how much\x01",
            "we can count on this airship, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3CIndeed, if we touched ground, because\x01",
            "of this ship size we would be detected\x01",
            "by the Pleroma Grass-mediated "net".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PYes, at this rate we\x01",
            "can't touch down...\x02\x03",
            "#10400FThat's why I want to detect and discover\x01",
            "a "gap" in the Septium vein force field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PA "gap" in the force field...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CHm, by nature, the Septium vein force field\x01",
            "is a giant thing covering the entire land.\x02\x03",
            "#01200FHowever, among its big streams,\x01",
            "sometimes "gaps" are born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see...\x02\x03",
            "#00000FIt means that if we land on such\x01",
            "a "gap" we won't be noticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5PHu hu, exactly.\x02\x03",
            "#10402FAnd so, the point where we're now\x01",
            "it's just a place like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(1300)
    SetMessageWindowPos(30, 10, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00001FSt. Ursula Byroad's sandbank...\x01",
            "Near where that Cryptid appeared before?\x02\x03",
            "#00005FStill, you did well in finding it, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 200, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10404FHu hu, before the accident happened,\x01",
            "I searched for it with Abbas.\x02\x03",
            "#10402FSo, after having done a little trick,\x01",
            "we escaped from Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 10, -1, -1)

    AnonymousTalk(
        0x101,
        "#00011FI-I see.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 20, -1, -1)

    AnonymousTalk(
        0x107,
        "#01203F#3CHm, thoroughly prepared.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 200, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10404F#0CWell, we can only do it here for the present,\x01",
            "so in the future we need to go look for "gaps" \x01",
            "where it seems we can land.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10403F#5P──So, what do we do?\x02\x03",
            "#10400FBecause the "barrier" is there,\x01",
            "we can't get into Crossbell anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P...You're right.\x01",
            "Even so, let's touch ground for now.\x02\x03",
            "#00008FI want to learn about Crossbell\x01",
            "situation, even if just a little...\x02\x03",
            "#00001FI want to confirm what's going on\x01",
            "at St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#5PHu hu, roger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#11P#3CThen, let's land.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(200)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x105)
    Sleep(500)

    ChrTalk(
        0x107,
        "#01200F#5P#3CHm, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PWell, I know it's late to say this, but...\x02\x03",
            "#00001FZeit, why are you helping us?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PAlso, according to what the Liberl dragon said...\x02\x03",
            "#10401FRegarding the destiny surrounding the "Sept-\x01",
            "Terrions", because you divine beasts only "watch\x01",
            "over", you can't intervene, am I not right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3CSo it is── We made an ancient "oath".\x02\x03",
            "#01200FHowever, with the lost "Sept-Terrion of Mirage"\x01",
            "at present, my original duty is already over.\x02\x03",
            "Therefore, the "taboo" that binded me has faded and\x01",
            "that means I can act freely to a certain extent.\x02\x03",
            "At least to give a little help\x01",
            "to the children of man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PSo that's why you helped us in the\x01",
            "mafia military dogs case too...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CHm, precisely.\x02\x03",
            "#01200FI can't support you indefinitely, but...\x01",
            "I'll help you out like I'm doing\x01",
            "only for some time.\x02\x03",
            "Well, I'm also registered as\x01",
            "a "police dog" or whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PHa ha, got it.\x01",
            "I'll gladly accept your help.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x105, 0x0)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#10404F#5PSo it seems that we'll move around\x01",
            "with this formation for a little while.\x02\x03",
            "#10400F──When you want to land,\x01",
            "talk to Abbas.\x02\x03",
            "Also, even inside this "Merkabah" \x01",
            "there're a few facilities ready.\x02\x03",
            "#10404FEquipments, tools, factory──\x01",
            "If you need them, tell the crew.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00000F#11PYeah, roger.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17980, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wazy and Zeit have joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x4, 0x12D)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wazy has learned the\x01\x07\x02",
            ""Akashic Arm"\x07\x05",
            " S-Craft.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Set "Akashic Arm"\x07\x05",
            " as S-Break?",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_351C")
    SetChrChipPat(0x4, 0x6, 0x12D)

    label("loc_351C")

    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "For the time being, Zeit has\x01",
            "joined as a party member.\x02\x03",
            "Because he doesn't have an Enigma II,\x01",
            "you can't customize Quartz but he can\x01",
            "use some powerful high level Arts.\x02\x03",
            "However, you need to pay attention\x01",
            "because he doesn't have an S-Craft.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Furthermore── only Lloyd can move\x01",
            "inside the Merkabah. Other members\x01",
            "are on standby inside the ship.\x02\x03",
            "However, because it's possible to manage all\x01",
            "members' items in the camp menu, you can \x01",
            "browse them in the shop and factory.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    ClearChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 103570, 0, -97090, 270)
    OP_4C(0x15, 0xFF)
    ClearChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 103950, 0, -210, 270)
    OP_4C(0x16, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearMapObjFlags(0x0, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x6, 0xFF)
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 100150, 0, -100950, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x20, 5)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x26, 4)
    SetScenarioFlags(0x26, 6)
    SetScenarioFlags(0x1A0, 0)
    OP_29(0xAF, 0x4, 0x2)
    OP_29(0xAF, 0x1, 0x0)
    Sound(498, 2, 100, 0)
    ClearScenarioFlags(0x32, 0)
    ClearScenarioFlags(0x32, 1)
    ClearScenarioFlags(0x32, 2)
    ClearScenarioFlags(0x32, 3)
    ClearScenarioFlags(0x32, 4)
    ClearScenarioFlags(0x32, 5)
    ClearScenarioFlags(0x32, 6)
    ClearScenarioFlags(0x32, 7)
    ClearScenarioFlags(0x33, 0)
    ClearScenarioFlags(0x33, 1)
    ClearScenarioFlags(0x33, 2)
    ClearScenarioFlags(0x33, 3)
    ClearScenarioFlags(0x33, 4)
    ClearScenarioFlags(0x33, 5)
    ClearScenarioFlags(0x33, 6)
    ClearScenarioFlags(0x33, 7)
    ClearScenarioFlags(0x34, 0)
    ClearScenarioFlags(0x34, 1)
    ClearScenarioFlags(0x34, 2)
    ClearScenarioFlags(0x34, 3)
    ClearScenarioFlags(0x34, 4)
    ClearScenarioFlags(0x34, 5)
    ClearScenarioFlags(0x34, 6)
    ClearScenarioFlags(0x34, 7)
    ClearScenarioFlags(0x31, 6)
    ClearScenarioFlags(0x31, 4)
    ClearScenarioFlags(0x2F, 6)
    ClearScenarioFlags(0x31, 3)
    ClearScenarioFlags(0x2D, 6)
    ClearScenarioFlags(0x2D, 4)
    ClearScenarioFlags(0x2D, 2)
    ClearScenarioFlags(0x2B, 6)
    ClearScenarioFlags(0x35, 0)
    ClearScenarioFlags(0x35, 1)
    ClearScenarioFlags(0x35, 2)
    ClearScenarioFlags(0x35, 3)
    ClearScenarioFlags(0x35, 4)
    ClearScenarioFlags(0x35, 5)
    ClearScenarioFlags(0x35, 6)
    ClearScenarioFlags(0x35, 7)
    ClearScenarioFlags(0x36, 0)
    ClearScenarioFlags(0x36, 1)
    ClearScenarioFlags(0x36, 2)
    ClearScenarioFlags(0x36, 3)
    ClearScenarioFlags(0x36, 4)
    ClearScenarioFlags(0x36, 5)
    ClearScenarioFlags(0x36, 6)
    ClearScenarioFlags(0x36, 7)
    ClearScenarioFlags(0x37, 0)
    ClearScenarioFlags(0x37, 1)
    ClearScenarioFlags(0x37, 2)
    ClearScenarioFlags(0x37, 3)
    ClearScenarioFlags(0x37, 4)
    ClearScenarioFlags(0x37, 5)
    ClearScenarioFlags(0x37, 6)
    ClearScenarioFlags(0x37, 7)
    ClearScenarioFlags(0x31, 7)
    ClearScenarioFlags(0x31, 5)
    ClearScenarioFlags(0x2F, 7)
    ClearScenarioFlags(0x2F, 5)
    ClearScenarioFlags(0x2D, 7)
    ClearScenarioFlags(0x2D, 5)
    ClearScenarioFlags(0x2D, 3)
    ClearScenarioFlags(0x2B, 7)
    EventEnd(0x5)
    Return()

    # Function_9_23F2 end

    def Function_10_38C5(): pass

    label("Function_10_38C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3906")
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Jump("Function_10_38C5")

    label("loc_3906")

    Return()

    # Function_10_38C5 end

    def Function_11_3907(): pass

    label("Function_11_3907")

    EventBegin(0x0)
    Fade(500)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-220, -500, 6740, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrSubChip(0x8, 0x1)
    SetChrPos(0x101, -1500, -1500, 6000, 45)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D43")

    ChrTalk(
        0x8,
        "#12100F#11P──So, what will you do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PWell, for now we decided to\x01",
            "try to land in this place.\x02\x03",
            "#00000FBy the way, I would've never\x01",
            "imagined you all had such a background.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11PAll of this is because there's a conflict within \x01",
            "the Church── it was to fool the eyes of Archbishop \x01",
            "Eralda who is unfavorable towards the Knights.\x02\x03",
            "No one would ever think that one of\x01",
            "the highest Knights is acting as the\x01",
            ""head" of a delinquent group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PWell, I guess you're right.\x02\x03",
            "#00005FAh, but, I have a feeling like you were\x01",
            "repeatedly using words inclined to the \x01",
            "Church like "Testaments", "Holy War"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12105F#11PHm, is that so?\x02\x03",
            "#12100FRather, I thought they could deceive by\x01",
            "making a shameless impression...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PW-Well, for sure I think you deceived\x01",
            "him because you were a team\x01",
            "with a peculiar air.\x02\x03",
            "#00000F──So, can we\x01",
            "land right away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11PHm, we could correctly pinpoint\x01",
            "the "gap" location.\x02\x03",
            "Tell me, if you're ready.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1A0, 1)
    Jump("loc_3DC8")

    label("loc_3D43")


    ChrTalk(
        0x8,
        (
            "#12100F#11PWe could correctly pinpoint\x01",
            "the "gap" location.\x02\x03",
            "Tell me, when you're ready to land\x01",
            "at St. Ursula Byroad's sandbank.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC8")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Land with the Merkabah\x01",      # 0
            "Quit\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E1E"),
        (1, "loc_3EB6"),
        (SWITCH_DEFAULT, "loc_3F16"),
    )


    label("loc_3E1E")


    ChrTalk(
        0x8,
        (
            "#12102F#11PRoger.\x01",
            "Confirm the place for now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_3E96")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x8, 0x0)
    Call(0, 12)
    Call(0, 5)
    Call(0, 7)
    Jump("loc_3EB1")

    label("loc_3E96")

    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x0, -1500, -1500, 6000, 45)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_3EB1")

    Jump("loc_3F16")

    label("loc_3EB6")


    ChrTalk(
        0x8,
        (
            "#12100F#11PThen, you can talk to me\x01",
            "when you are prepared.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x0, -1500, -1500, 6000, 45)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_3F16")

    label("loc_3F16")

    Return()

    # Function_11_3907 end

    def Function_12_3F17(): pass

    label("Function_12_3F17")

    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -750, 0)
    OP_68(0, 500, 3500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_68(0, 5000, 3500, 3000)
    Sleep(2000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 1)
    Return()

    # Function_12_3F17 end

    def Function_13_3FD4(): pass

    label("Function_13_3FD4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    LoadEffect(0x0, "event/ev17086.eff")
    SoundLoad(938)
    SoundLoad(132)
    SoundLoad(497)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-560, 2900, 4130, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -750, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-560, 1100, 4130, 3500)
    Sound(938, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00203F#12P#N...Sensing a new "gap" in the\x01",
            "Septium vein force field...\x02\x03",
            "#00202FI will send the data over.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#01909F#5PYes, roger.\x02\x03",
            "#01901F(*clak clak*...)\x01",
            "I could pinpoint the coordinates!\x02\x03",
            "Crossbell north-east area,\x01",
            "nearby "Armorica Village"!\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        "#00002F#12PAmazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11PThey're quite the help.\x02\x03",
            "Plato's responsiveness is useful of course, but \x01",
            "also having a dedicated operator greatly raises\x01",
            "the ship's operational efficiency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909F#5PEhehe...\x01",
            "I'm still inexperienced, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11PHu hu, it seems that from now on we can search\x01",
            "efficiently for places where we can land.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(200)

    ChrTalk(
        0x105,
        (
            "#10400F#5PSo, what do we do?\x02\x03",
            "Do you want to go to\x01",
            "the new point now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PYeah, I want to confirm the\x01",
            "situation in Armorica Village too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#11PFull engines, destination,\x01",
            ""Armorica Village" airspace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#12P#NHeading to the destination\x01",
            "while maintaining high alert.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19110, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_24(0x3AA)
    EndChrThread(0x103, 0x0)
    EndChrThread(0xC, 0x0)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    OP_F3(100000)
    ClearChrFlags(0x1E, 0x80)
    OP_78(0x0, 0x1E)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)
    PlayEffect(0x0, 0x0, 0x1E, 0x5, -4250, 1750, -10250, 0, 0, 0, 1500, 1500, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1E, 0x5, 4250, 1750, -10250, 0, 0, 0, 1500, 1500, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-1000000, 0, 800000, 0)
    MoveCamera(330, -7, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(111000, 0)
    MoveCamera(340, -7, 0, 3000)

    def lambda_45AE():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_45AE)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    Sound(499, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    StopSound(497, 3000, 100)
    Sleep(2000)
    StopSound(132, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0xFFFF)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    Sleep(500)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetScenarioFlags(0x26, 2)
    SetScenarioFlags(0x1A1, 2)
    OP_29(0xAF, 0x1, 0x3)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 2, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_46B1")
    FadeToDark(0, 0, -1)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46A6")
    Call(0, 6)
    Jump("loc_46A9")

    label("loc_46A6")

    Call(0, 5)

    label("loc_46A9")

    Call(0, 7)
    Jump("loc_46BA")

    label("loc_46B1")

    NewScene("e3020", 102, 0, 0)
    IdleLoop()

    label("loc_46BA")

    Return()

    # Function_13_3FD4 end

    def Function_14_46BB(): pass

    label("Function_14_46BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46D5")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_14_46BB")

    label("loc_46D5")

    Return()

    # Function_14_46BB end

    def Function_15_46D6(): pass

    label("Function_15_46D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    SoundLoad(938)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-560, 2900, 4130, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -950, 0)
    SetChrPos(0x106, -1400, 0, -1150, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-560, 1100, 4130, 3500)
    Sound(938, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#00204F#12P#NSensed a new "gap".\x02\x03",
            "#00202FMiss Fran, I will send\x01",
            "you the data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909F#5PYeees.\x01",
            "(*clak clak clak*...)\x02\x03",
            "#01905F──Here it is!\x01",
            "Crossbell north-west area...\x02\x03",
            "#01901FA point midway Mainz Mountain Path!\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        (
            "#00002F#12PThe Mainz area, eh...?\x01",
            "The areas where we can move to has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11PWell, they've probably started\x01",
            "to notice our movements too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P#N...Speaking of the Mainz area,\x01",
            "it's where a different force than the \x01",
            ""Heiyue" should be putting up a resistance.\x02\x03",
            "#10701FIt seems that leader is a former\x01",
            "CGF member who contested\x01",
            "the present State Guard.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x103, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrChipByIndex(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-1230, 1100, 3390, 1000)
    SetCameraDistance(19800, 1000)

    def lambda_4B2A():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B2A)
    SetChrFlags(0x107, 0x20)

    def lambda_4B3C():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4B3C)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)
    SetChrSubChip(0xC, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    OP_6F(0x79)
    ClearChrFlags(0x107, 0x20)

    ChrTalk(
        0x101,
        "#00011F#5PI-Is that so!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PI thought for sure that all the members\x01",
            "would have joined the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PWell, it's not surprising.\x02\x03",
            "The "Red Constellation" that caused\x01",
            "such serious damage to the CGF is\x01",
            "moving around triumphantly.\x02\x03",
            "It's no wonder that someone who can't\x01",
            "stand the deceit would come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01901F#5PT-Then, maybe\x01",
            "big sis too...!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00006F#11P...No.\x01",
            "Unfortunately, I don't think that's the case.\x02\x03",
            "#00008FAfter swallowing down everything,\x01",
            "Noｱl chose the path to protect\x01",
            "the current Crossbell.\x02\x03",
            "#00013FI think she won't bend\x01",
            "that decision easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01912F#5P#30W...Ahaha, you're right.\x02\x03",
            "#01908F#30WBig sis is really strong...\x01",
            "She's awkward, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#5P...Miss Fran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PWell, in any case I'd like\x01",
            "to make contact with this\x01",
            ""Resistance".\x02\x03",
            "#10400FDepending on the situation, they\x01",
            "could be of help like the "Heiyue".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PYeah, let's try to land now.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#5P...By the way, Rixia.\x02\x03",
            "#00000FBefore that, do you want to\x01",
            "stop by St. Ursula Hospital?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#10712F#12PWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PMiss Ilya really wanted\x01",
            "to see you, you know?\x02\x03",
            "#00002FMany things have happened, but...\x01",
            "Why don't you show her your happy face?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)

    ChrTalk(
        0x106,
        (
            "#10706F#12P...No, I'll pass.\x02\x03",
            "#10708FI can't stand in front of Miss\x01",
            "Ilya with confidence yet...\x02\x03",
            "#10710FPlease, let me endure at least until\x01",
            "after we have freed Crossbell City\x01",
            "and taken the Arc-en-ciel back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PIt is frustrating, but...\x01",
            "I think I understand how you feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10709F#12PAhaha...I'm sorry.\x02\x03",
            "#10702FAh, of course if you have something\x01",
            "to do there, I don't mind going to\x01",
            "St. Ursula Hospital...!\x02\x03",
            "#10704FI will, well, wait for you\x01",
            "in front of the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, got it.\x02\x03",
            "#00000F(Nevertheless, Rixia...\x01",
            "She really has an honest personality.)\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20050, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Rixia has joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_535F")
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1A9)
    Jump("loc_5367")

    label("loc_535F")

    AddCraft(0x5, 0x195)
    AddCraft(0x0, 0x195)

    label("loc_5367")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Rixia have learned the\x01\x07\x02",
            ""Double Dragon Strike" Combi Craft.\x07\x05\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By each expending 100 CP, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -1520, 0, -100980, 180)
    SetChrChipByIndex(0xA, 0x2)
    BeginChrThread(0xA, 0, 0, 0)
    SetScenarioFlags(0x26, 5)
    SetScenarioFlags(0x1A1, 7)
    OP_29(0xAF, 0x1, 0x7)
    Sleep(300)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 2, 100, 0)
    OP_24(0x3AA)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_54DD")
    FadeToDark(0, 0, -1)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54D2")
    Call(0, 6)
    Jump("loc_54D5")

    label("loc_54D2")

    Call(0, 5)

    label("loc_54D5")

    Call(0, 7)
    Jump("loc_54E6")

    label("loc_54DD")

    NewScene("e3020", 102, 0, 0)
    IdleLoop()

    label("loc_54E6")

    Return()

    # Function_15_46D6 end

    def Function_16_54E7(): pass

    label("Function_16_54E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    SoundLoad(938)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-560, 2900, 4130, 0)
    MoveCamera(39, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19800, 0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 1300, 0, -1500, 0)
    SetChrPos(0x106, -1400, 0, -1150, 0)
    SetChrPos(0x104, 200, 0, -750, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xF, -750, 500, 3300, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-560, 1100, 4130, 3500)
    FadeToBright(1000, 0)
    Sleep(3000)
    OP_63(0xF, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#02109F#11PWooow...\x01",
            "It really is a great airship!\x02\x03",
            "#02110FI can't believe the Church\x01",
            "had such ships!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12100F#5P...I'll repeat it again, I beg you\x01",
            "to not tell a word to anyone.\x02\x03",
            "If it were to appear in a news article,\x01",
            "be prepared to never have the\x01",
            "Church support in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10409F#11PHa ha, even if it was featured\x01",
            "in an article, maybe they'll just\x01",
            "think about it as a kind of drivel.\x02\x03",
            "#10402FLike with the "Society".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12107F#5PWazy...!\x02",
    )

    CloseMessageWindow()
    OP_68(-230, 1100, 2950, 1000)
    SetCameraDistance(19800, 1000)
    OP_93(0xF, 0xB4, 0x1F4)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0xF,
        (
            "#02104F#5PDon't worry, I'll keep my promise.\x02\x03",
            "#02100FEven about Rixia Mao's true identity\x01",
            "being the mysterious demon, "Yin"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10706F#12P#N...Please.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#12P(Say, Lloyd...)\x02\x03",
            "#00301F(Was it really a good idea\x01",
            "to take her along?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11P(W-Well, i think she's someone\x01",
            "who keeps her promises...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-790, 1100, 4000, 1000)
    OP_6F(0x79)
    Sound(938, 2, 100, 0)

    ChrTalk(
        0x103,
        (
            "#00201F#11PI sensed a new "gap" in the\x01",
            "west part of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0x13B, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#01908F#5P(*clak clak*...)\x01",
            "Correct coordinates pinpointed.\x02\x03",
            "#01903FWest Crossbell Highway, midway...\x02\x03",
            "#01901FNearby the fork in the road towards the\x01",
            "Police Academy and prison areas.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        "#00001F#11PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PYou said that when you escaped\x01",
            "from prison you were helped by\x01",
            "ol' man Garcｵa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah... No matter what you\x01",
            "can say, he gave me a help.\x02\x03",
            "#00008FI'm concerned about what\x01",
            "happened to him after that, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(50)

    ChrTalk(
        0x105,
        (
            "#10406F#5PHowever, it's not a good plan\x01",
            "going to the Police Academy area.\x02\x03",
            "#10401FBecause you escaped, they would've\x01",
            "strengthened security too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P#NHaving said that, we only have Bellguard Gate where\x01",
            "the State Guard is as another place we can go to...\x02\x03",
            "#10701FThat's a bit of a problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#02106F#11PWell, it's certain that you would be\x01",
            "arrested if you went there carelessly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01908F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P...In any case, \x01",
            "let's just try to land.\x02\x03",
            "#00001FI want to confirm to what extent the\x01",
            "State Guard is guarding and I'm also\x01",
            "worried about Cryptids loitering around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PA "magic circle" was set before\x01",
            "the mining town too.\x02\x03",
            "Since we can land whenever you want,\x01",
            "just say the word if you need to.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20050, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    EndChrThread(0x103, 0x0)
    EndChrThread(0xC, 0x0)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy has joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x3, 0x129)
    AddCraft(0x3, 0x168)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy has learned the\x01\x07\x02",
            ""Berserker"\x07\x05",
            " S-Craft.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Set "Berserker"\x07\x05",
            " as S-Break?",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6074")
    SetChrChipPat(0x3, 0x6, 0x129)

    label("loc_6074")

    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x0, -150, 0, -88230, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x26, 3)
    SetScenarioFlags(0x1A2, 7)
    OP_29(0xAF, 0x1, 0xD)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_16_54E7 end

    def Function_17_60CD(): pass

    label("Function_17_60CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06900.itc", 0x1E)
    LoadChrToIndex("apl/ch51027.itc", 0x1F)
    LoadChrToIndex("apl/ch51712.itc", 0x20)
    SoundLoad(498)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x101, 500, 0, -104000, 0)
    SetChrPos(0x1B, -500, 0, -104000, 0)
    SetChrPos(0x106, 500, 0, -104000, 0)
    SetChrPos(0x103, -500, 0, -104000, 0)
    SetChrPos(0x104, 500, 0, -104000, 0)
    SetChrPos(0x105, -500, 0, -104000, 0)
    SetChrPos(0x107, 0, 0, -104000, 0)
    SetChrPos(0x1C, 0, 0, -85000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Noｱl collected her bags and\x01",
            "joined the Merkabah with Lloyd and the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7514", 0)
    Sound(498, 2, 100, 0)
    OP_68(0, 1250, -102500, 0)
    OP_68(0, 1250, -93000, 6000)
    MoveCamera(45, 25, 0, 0)
    MoveCamera(45, 20, 0, 6000)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)

    def lambda_62CB():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62CB)

    def lambda_62E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62E0)
    Sleep(100)

    def lambda_62F4():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_62F4)

    def lambda_6309():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_6309)
    Sleep(500)

    def lambda_631D():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_631D)

    def lambda_6332():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_6332)
    Sleep(100)

    def lambda_6346():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6346)

    def lambda_635B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_635B)
    Sleep(500)

    def lambda_636F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_636F)

    def lambda_6384():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6384)
    Sleep(100)

    def lambda_6398():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6398)

    def lambda_63AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_63AD)
    Sleep(800)

    def lambda_63C1():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_63C1)

    def lambda_63D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_63D6)
    Sleep(2000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_63FF():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_63FF)

    def lambda_6414():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_6414)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1C, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1B, 2)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x106, 2)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x107, 2)
    SetChrSubChip(0x107, 0x5)
    OP_0D()
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6485():

        label("loc_6485")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6485")

    QueueWorkItem2(0x101, 2, lambda_6485)

    def lambda_6497():

        label("loc_6497")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6497")

    QueueWorkItem2(0x103, 2, lambda_6497)

    def lambda_64A9():

        label("loc_64A9")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_64A9")

    QueueWorkItem2(0x104, 2, lambda_64A9)

    def lambda_64BB():

        label("loc_64BB")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_64BB")

    QueueWorkItem2(0x105, 2, lambda_64BB)

    def lambda_64CD():

        label("loc_64CD")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_64CD")

    QueueWorkItem2(0x106, 2, lambda_64CD)
    OP_68(0, 1250, -95000, 2500)
    SetCameraDistance(16500, 17000)
    OP_63(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0x1C, 3, 0, 19)
    Sleep(3000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Then, Fran, who came to welcome her,\x01",
            "started to sob after having hugged\x01",
            "Noｱl without saying a word...\x02\x03",
            "While calming down her younger sister, \x01",
            "Noｱl's eyes too got wet, brimming with tears.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    SetCameraDistance(16500, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 6)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_60CD end

    def Function_18_6609(): pass

    label("Function_18_6609")


    def lambda_660E():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_660E)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_6609 end

    def Function_19_662E(): pass

    label("Function_19_662E")

    OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xFFFE8E78, 0x1770, 0x0)
    Fade(250)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0x1B, 0x2)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    Sound(812, 0, 100, 0)
    Sound(811, 0, 30, 0)
    OP_A6(0x1B, 0x0, 0xA, 0x1F4, 0xBB8)
    OP_0D()
    OP_63(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1B)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x106, 0x2)
    Sleep(500)

    def lambda_66B5():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_66B5)
    WaitChrThread(0x1C, 2)
    Sleep(500)

    def lambda_66D5():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_66D5)
    WaitChrThread(0x1C, 2)
    Sleep(1500)

    def lambda_66F5():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_66F5)
    WaitChrThread(0x1C, 2)
    Sleep(500)

    def lambda_6715():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_6715)
    WaitChrThread(0x1C, 2)
    Return()

    # Function_19_662E end

    def Function_20_672E(): pass

    label("Function_20_672E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x8, 0xFF, 0xFF)
    OP_32(0x8, 0x0, 0x56)
    OP_32(0x8, 0x5, 0x64)
    OP_42(0x8, 0x455, 0xFF)
    OP_42(0x8, 0x5ED, 0xFF)
    OP_42(0x8, 0x651, 0xFF)
    OP_38(0x8, 0x81, 0x2)
    OP_38(0x8, 0x84, 0x2)
    OP_38(0x8, 0x85, 0x2)
    OP_38(0x8, 0x86, 0x2)
    OP_42(0x8, 0xB4, 0x1)
    OP_42(0x8, 0x72, 0x4)
    OP_42(0x8, 0xB9, 0x5)
    OP_42(0x8, 0xA0, 0x6)
    AddCraft(0x8, 0xEC)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis284.itp")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-850, 2900, 3210, 0)
    MoveCamera(39, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20690, 0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 1500, 0, -1500, 0)
    SetChrPos(0x106, -1500, 0, -1250, 0)
    SetChrPos(0x104, 500, 0, -750, 0)
    SetChrPos(0x109, -500, 0, -1750, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrPos(0xF, -3480, -1500, 4650, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-850, 1100, 3210, 3500)
    MoveCamera(39, 19, 0, 3500)
    OP_6E(500, 3500)
    SetCameraDistance(20690, 3500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(836, 0, 100, 0)

    ChrTalk(
        0x103,
        (
            "#00204F#11P──Sensed a "gap" in\x01",
            "the Michelam area.\x02\x03",
            "#00202FMiss Fran, I am sending the coordinates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01908F#5PYes, *sob*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PJeez...\x01",
            "For how long do you intend to cry?\x02\x03",
            "#10101FEveryone will laugh, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#11PHa ha, it's ok.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10709F#12P#NUh uh...\x01",
            "Somehow I'm envious.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(836, 0, 100, 0)

    ChrTalk(
        0xC,
        (
            "#01909F#5PEhehe...I'm sorry.\x02\x03",
            "#01900F(*clak clak*...)\x01",
            "──Pinpointed!\x02\x03",
            "#01903FNearby Hotel Delphinia at\x01",
            "Michelam Health Resort...\x02\x03",
            "#01901FIt's at that Lake Beach!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#12P*pheee*, that's a crazy coincidence.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11PHu hu, we can hardly call it a\x01",
            "refined vacation this time, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#02105F#5PMy, could it be that...\x02\x03",
            "You all went to have\x01",
            "fun at the beach?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    def lambda_6C1B():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6C1B)
    Sleep(50)

    def lambda_6C2B():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6C2B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00002F#11PYes, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PAfter the Trade Conference.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02106F#5PGeez, how cold of you.\x02\x03",
            "#02101FWhy didn't you call me\x01",
            "for such a funny event?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PWell, we were\x01",
            "invited too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10408F#5PThinking about it now, that invitation\x01",
            "could have had an ulterior motive too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#12P#N...Indeed.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#11P............\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    ChrTalk(
        0x101,
        (
            "#00003F#11P──At any rate, our next\x01",
            "destination is decided.\x02\x03",
            "#00008FA "Red Constellation" unit\x01",
            "seem to be guarding there...\x02\x03",
            "#00001FNoｱl, do you know \x01",
            "their scale?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PLet's see...\x01",
            "I think there's one company.\x02\x03",
            "#10113FEven with these numbers I\x01",
            "honestly think we wouldn't make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#11PIf we could disperse their forces\x01",
            "with some diversion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10701F#12P#NIn that case, leave it to m──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x107, 0x20)
    TurnDirection(0x107, 0x109, 500)
    Sleep(150)
    ClearChrFlags(0x107, 0x20)

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3CNo, I'll take care of that.\x02\x03",
            "#01201FIf I return to my original form,\x01",
            "I'll be able to lure many of them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    EndChrThread(0xC, 0x0)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    OP_68(-50, 1100, 2370, 1000)

    def lambda_7106():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7106)
    Sleep(50)

    def lambda_7116():
        TurnDirection(0x104, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7116)
    Sleep(50)

    def lambda_7126():
        TurnDirection(0x109, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7126)
    Sleep(50)

    def lambda_7136():
        TurnDirection(0x106, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_7136)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    SetChrSubChip(0xC, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00205F#5PZeit...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5PHmm...are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3CI intend to fully help\x01",
            "you until the very end.\x02\x03",
            "You keep saving your energies\x01",
            "and gathering your comrades.\x01",
            "Your support would be a waste.\x02\x03",
            "#01203FWell, just consider this\x01",
            "as my final big service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PThank you, Zeit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#5PYeah, you help us tons.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PEven so, I think it's going to be\x01",
            "quite a hard fight for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5PNevertheless, not only the Chairman\x01",
            "is at Michelam, Elie is also there.\x02\x03",
            "#00007FLet's prepare thoroughly...\x01",
            "And free them no matter what!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_73C5():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_73C5)
    Sleep(50)

    def lambda_73D5():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_73D5)
    Sleep(50)

    def lambda_73E5():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_73E5)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x103,
        "#00201F#5P...Yes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#11PGotcha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12PRoger!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20940, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Zeit has left the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noｱl has joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x8, 0x141)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noｱl has learned the\x01\x07\x02",
            ""Armed Force"\x07\x05",
            " S-Craft.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Set "Armed Force"\x07\x05",
            " as S-Break?",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757C")
    SetChrChipPat(0x8, 0x6, 0x141)

    label("loc_757C")

    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x6, 0xFF)
    PartySelect(1)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x33, 5)
    SetScenarioFlags(0x36, 5)
    ClearScenarioFlags(0x26, 6)
    SetScenarioFlags(0x27, 0)
    SetScenarioFlags(0x1A3, 3)
    OP_29(0xAF, 0x1, 0x11)
    SetScenarioFlags(0x33, 5)
    SetScenarioFlags(0x36, 5)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sound(498, 2, 100, 0)
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_20_672E end

    def Function_21_75DE(): pass

    label("Function_21_75DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F(...If we land here it'll be\x01",
            "immediately a battle with the\x01",
            ""Red Constellation" unit.)\x02\x03",
            "#00013F(We won't be able to resupply...\x01",
            "Are our preparations well done?)\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[We Still Have Something To Do]\x01",      # 0
            "[Land at Michelam]\x01",                   # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_76F8"),
        (1, "loc_7706"),
        (SWITCH_DEFAULT, "loc_7852"),
    )


    label("loc_76F8")

    FadeToBright(0, 0)
    Jump("loc_7852")

    label("loc_7706")

    Call(0, 6)
    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7749")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_7839")

    label("loc_7749")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_776C")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_7839")

    label("loc_776C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_778F")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_7839")

    label("loc_778F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77B2")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_7839")

    label("loc_77B2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77D5")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_7839")

    label("loc_77D5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77F8")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_7839")

    label("loc_77F8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_781B")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_7839")

    label("loc_781B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7839")
    SetScenarioFlags(0x3C, 7)

    label("loc_7839")

    PartySelect(2)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1310", 0, 0, 0)
    IdleLoop()
    Jump("loc_7852")

    label("loc_7852")

    Return()

    # Function_21_75DE end

    def Function_22_7853(): pass

    label("Function_22_7853")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis285.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02300.itp")
    AddParty(0x1, 0xFF, 0xFF)
    OP_32(0x1, 0x0, 0x58)
    OP_32(0x1, 0x5, 0x64)
    OP_42(0x1, 0x405, 0xFF)
    OP_42(0x1, 0x5ED, 0xFF)
    OP_42(0x1, 0x651, 0xFF)
    OP_38(0x1, 0x83, 0x2)
    OP_38(0x1, 0x84, 0x2)
    OP_38(0x1, 0x85, 0x2)
    OP_38(0x1, 0x86, 0x2)
    OP_42(0x1, 0xA4, 0x3)
    OP_42(0x1, 0x7E, 0x4)
    OP_42(0x1, 0x82, 0x5)
    OP_42(0x1, 0xB3, 0x6)
    SetScenarioFlags(0x20, 3)
    SetScenarioFlags(0x20, 6)
    AddCraft(0x2, 0xB1)
    OP_32(0x6, 0x0, 0x5A)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xA)
    SetChrSubChip(0x102, 0x2)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 0x19)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 0x18)
    SetChrSubChip(0xF, 0x1)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 3, 0, 0)
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x12, 98470, 70, -101100, 180)
    SetChrPos(0x101, 100150, 70, -102850, 270)
    SetChrPos(0x102, 100100, 70, -104800, 270)
    SetChrPos(0xF, 96800, 70, -102650, 90)
    SetChrPos(0x105, 96800, 70, -104800, 90)
    SetChrPos(0x103, 102350, 0, -104050, 270)
    SetChrPos(0x104, 102060, 0, -102890, 270)
    SetChrPos(0x9, 101700, 0, -105600, 315)
    SetChrPos(0x109, 96950, 0, -100550, 135)
    SetChrPos(0xC, 96050, 0, -100600, 135)
    SetChrPos(0x106, 101350, 0, -100350, 225)
    SetChrPos(0x13, 99400, 0, -98000, 180)
    SetChrPos(0x8, 97150, 0, -106150, 0)
    OP_68(98500, 1250, -103350, 0)
    MoveCamera(44, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15250, 0)
    SetCameraDistance(16250, 3000)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xF,
        (
            "#02101F#6P──Then, Chairman.\x01",
            "Your resolution doesn't waver?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x12,
        (
            "Hm...among you all there's\x01",
            "probably someone contrary.\x02\x03",
            "However, if we don't start from \x01",
            "here, I think we won't be able to \x01",
            "move forward.\x02\x03",
            "Even if we lost a temporary\x01",
            "order and hegemony.\x02",
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
        0x102,
        "#00108F#11PYes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PThe "Independent State of Crossbell"\x01",
            "declaration of invalidity, eh?\x02\x03",
            "#10400FIndeed a card that none other than His Grace\x01",
            "the Chairman, who is a former government \x01",
            "representative, could play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#5PHowever, in what form that announcement\x01",
            "will concretely be made?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01908F#6PIf it's not conveyed to the citizens and the\x01",
            "State Guard, its effect will be weak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PIn that regard, it appears\x01",
            "that Jona has an idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(99360, 1250, -104040, 1000)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0xF, 0x2)
    SetChrSubChip(0x12, 0x1)
    SetChrSubChip(0x105, 0x0)

    def lambda_7EBA():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7EBA)
    Sleep(50)

    def lambda_7ECA():
        TurnDirection(0x106, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_7ECA)
    Sleep(50)

    def lambda_7EDA():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7EDA)
    Sleep(50)

    def lambda_7EEA():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7EEA)
    Sleep(50)

    def lambda_7EFA():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7EFA)
    Sleep(50)

    def lambda_7F0A():
        TurnDirection(0x13, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7F0A)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x13, 0)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "Yeah. There's a signal booster \x01",
            "experimentally used to connect the \x01",
            "orbal net to Leman on Tangram Hill.\x02\x03",
            "If I can get an opening there,\x01",
            "I should be able to hack it.\x02\x03",
            "If it's for about ten minutes,\x01",
            "I should be able to make it last \x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x104,
        (
            "#00305F#5PI don't really get it, but...\x01",
            "In short, you want to take over\x01",
            "those screens on the streets?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PYes, I can also access all the\x01",
            "terminals in the State Guard areas.\x02\x03",
            "#00202FI think it will also fulfill\x01",
            "Commander Sonya's terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#6PIf the validity of the President's\x01",
            "side sways, the State Guard will\x01",
            "watch the situation for a while...\x02\x03",
            "#12102FMoving around would\x01",
            "become easier for sure.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#11P............\x02",
    )

    CloseMessageWindow()
    OP_68(98990, 1250, -103480, 1000)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)
    SetChrSubChip(0xF, 0x0)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_828E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_828E)
    Sleep(50)

    def lambda_829E():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_829E)
    Sleep(50)

    def lambda_82AE():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_82AE)
    Sleep(50)

    def lambda_82BE():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_82BE)
    Sleep(50)

    def lambda_82CE():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_82CE)
    Sleep(50)

    def lambda_82DE():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_82DE)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x13, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00108F#11PLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503F#5PHm, Lloyd.\x02\x03",
            "#02500FThe "Independent State" declaration of\x01",
            "invalidity is nothing more than my idea.\x02\x03",
            "You don't intend to put it in effect since you, \x01",
            "who are the leader, are against it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00000F#11P──No, please.\x02\x03",
            "#00003FOnce, Mr. Dieter...\x01",
            "He spoke about "justice",\x01",
            "when he was the IBC President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11PAh...\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(80, 30, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the end, people are creatures\x01",
            "that seek justice.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because the thing called "justice" is\x01",
            "the foundation of a reliable society.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    SetMessageWindowPos(10, 100, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Political corruption, mafia problems...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Even if the police don't control them,\x01",
            "many people will be fixed for life\x01",
            "because of economic prosperity.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "However, even if in this situation,\x01",
            "as you'd expect, people must\x01",
            "seek "justice" somewhere.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because no matter what shape it takes, people desire\x01",
            "a sense of security which is a reliable society.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    SetMessageWindowPos(250, 50, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That's exactly why I──\x01",
            "Why I want to expect great things from you.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You guys, in your own way,\x01",
            "appear to be pursuing "justice"...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I think it's important to demonstrate that\x01",
            "to the citizens in a form they can see.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    VolumeBGM(0x64, 0x3E8)

    ChrTalk(
        0x12,
        "#02505F#5PDieter said those things...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11PThat happened too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#11PA year hasn't even passed, and yet\x01",
            "I feel very nostalgic about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P──The President's words back then.\x02\x03",
            "#00008FI honestly don't know if those\x01",
            "came from his true feelings\x01",
            "or were just a pose, but...\x02\x03",
            "#00001FEven so, it's true that they\x01",
            "echoed in our hearts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#11PYou're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#02103F#6PHm, they really are very interesting words.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYes, that's why...\x01",
            "I want to trust at him\x01",
            "those words again.\x02\x03",
            "#00003FFor our sake, and his too.\x02\x03",
            "#00001FAnd more importantly, to give the opportunity\x01",
            "to the citizens and the State Guard to think too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503F#5P──I understand.\x02\x03",
            "#02500FI'll simplify those words in my own style\x01",
            "and reflect them in the declaration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#11PYes, please do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#6PThen it's decided.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02104F#6PThen let's make the plan\x01",
            "specifics more solid!\x02\x03",
            "#02110FJona, Fran!\x01",
            "We'll leave the practical support to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01909F#5PYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#02302F#11PYeah, leave it to me.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16750, 1500)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thus, the plan specifics of the "Independent\x01",
            "State of Crossbell" declaration of invalidity\x01",
            "by Chairman MacDowell were worked out.\x02\x03",
            "A practical forecast to wage the\x01",
            "hacking to the orbal net was\x01",
            "done by Jona and Fran...\x02\x03",
            "What remained was only to choose the timing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e4400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_7853 end

    def Function_23_8D58(): pass

    label("Function_23_8D58")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F(The experimental signal booster...\x01",
            "We'll hack the orbal net and deliver the\x01",
            "declaration of invalidity from there.)\x02\x03",
            "#00001F(We can't go back...\x01",
            "Have we readied our resolve?)\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[We Still Have Other Things To Do]\x01",      # 0
            "[Head to the Booster Site]\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8E8C"),
        (1, "loc_8E9A"),
        (SWITCH_DEFAULT, "loc_909E"),
    )


    label("loc_8E8C")

    FadeToBright(0, 0)
    Jump("loc_909E")

    label("loc_8E9A")

    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_8F5B")
    FadeToBright(1000, 0)
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)

    def lambda_8EE8():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8EE8)
    OP_F0(0x1, 0x7D0)
    OP_68(-1000000, 0, 800000, 0)
    MoveCamera(30, -7, 0, 0)
    MoveCamera(20, -7, 0, 3000)
    OP_6E(500, 0)
    SetCameraDistance(111000, 0)
    Sleep(300)
    Sound(499, 0, 100, 0)
    Sleep(1700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    SetEventSkip(0x1, 0x0)

    label("loc_8F5B")

    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F9B")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_908B")

    label("loc_8F9B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FBE")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_908B")

    label("loc_8FBE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FE1")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_908B")

    label("loc_8FE1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9004")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_908B")

    label("loc_9004")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9027")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_908B")

    label("loc_9027")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_904A")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_908B")

    label("loc_904A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_906D")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_908B")

    label("loc_906D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_908B")
    SetScenarioFlags(0x3C, 7)

    label("loc_908B")

    PartySelect(2)
    SetScenarioFlags(0x23, 0)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Jump("loc_909E")

    label("loc_909E")

    Return()

    # Function_23_8D58 end

    def Function_24_909F(): pass

    label("Function_24_909F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05802.itc", 0x1E)
    LoadChrToIndex("apl/ch51770.itc", 0x1F)
    SoundLoad(952)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_90CD")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_90CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_90E0")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_90E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_90F3")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_90F3")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_71(0x1, 0x1E, 0x1E, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x12, 0, 500, 2400, 0)
    SetChrPos(0xF, 900, 500, 1750, 0)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, 2150, -1500, 7300, 90)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 750, 250, 400, 0)
    SetChrPos(0x106, -950, 0, -1650, 0)
    OP_68(0, 3300, 2000, 0)
    OP_68(0, 1500, 2000, 3500)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xC,
        (
            "#01901F#5P──The camera preparations are ok!\x01",
            "The sound test too is perfect!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PWe have arrived right above the booster.\x02\x03",
            "You can begin anytime you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02109F#11POkkay, okkay.\x02\x03",
            "#02100FChairman, can we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#02501F#5PYes, begin.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_68(-2830, -750, 6760, 2000)
    MoveCamera(45, 30, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#02304F#11PHe he, let's begin then.\x02\x03",
            "#02301F──Begin hacking the orbal net\x01",
            "from the signal booster.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(952, 2, 80, 0)
    BeginChrThread(0x1F, 1, 0, 25)
    SetCameraDistance(16000, 3000)
    BeginChrThread(0x9, 0, 0, 26)
    Sleep(1000)
    StopSound(498, 1000, 100)
    StopSound(952, 1000, 70)
    EndChrThread(0x1F, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0x0)
    OP_24(0x3B8)
    SetScenarioFlags(0x22, 1)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_909F end

    def Function_25_949F(): pass

    label("Function_25_949F")

    Sound(938, 0, 60, 0)
    Sound(836, 0, 60, 0)
    Sleep(800)
    Sound(836, 0, 60, 0)
    Return()

    # Function_25_949F end

    def Function_26_94B5(): pass

    label("Function_26_94B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_94CD")
    OP_A1(0xFE, 0x7D0, 0x2, 0x0, 0x1)
    Jump("Function_26_94B5")

    label("loc_94CD")

    Return()

    # Function_26_94B5 end

    def Function_27_94CE(): pass

    label("Function_27_94CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    LoadChrToIndex("chr/ch05802.itc", 0x1E)
    LoadChrToIndex("apl/ch51770.itc", 0x1F)
    LoadChrToIndex("apl/ch51714.itc", 0x20)
    SoundLoad(952)
    SoundLoad(938)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_71(0x1, 0x1E, 0x1E, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x12, 0, 500, 2400, 0)
    SetChrPos(0xF, 900, 500, 1750, 0)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, 2150, -1500, 7300, 90)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 750, 250, 400, 0)
    SetChrPos(0x106, -950, 0, -1650, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_68(-3150, -750, 7150, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(17000, 5000)
    BeginChrThread(0x9, 0, 0, 26)
    Sound(952, 2, 70, 0)
    BeginChrThread(0x1F, 1, 0, 28)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x9, 0x0)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x1F, 0x1)
    StopSound(938, 1000, 100)
    StopSound(952, 1000, 70)
    Sound(839, 0, 100, 0)
    Sleep(400)
    Sound(839, 0, 100, 0)

    ChrTalk(
        0x9,
        (
            "#02302F#11PAlright! I've got the\x01",
            "communications control!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1500, 2000, 2000)
    MoveCamera(45, 25, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        "#01901F#5PSwitching the camera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#02110F#11PYes, alright!\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_68(0, 1800, 2000, 2000)
    MoveCamera(45, 20, 0, 2000)
    OP_6F(0x79)
    Fade(250)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 0x20)
    OP_A0(0xF, 1500, 0x0, 0x2)
    OP_0D()
    OP_70(0x1, 0x21)
    Sound(72, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xF,
        (
            "──Everyone, good morning.\x02\x03",
            "Reporter Grace Lynn here,\x01",
            "working for the Crossbell \x01",
            "News Service.\x02\x03",
            "I'm telling you just in case,\x01",
            "Crossbell News is not related\x01",
            "at all to this specific matter.\x02\x03",
            "This is my own arbitrary report,\x01",
            "please understand.\x02\x03",
            "...Well then, I know this is \x01",
            "sudden, but I'd like to introduce \x01",
            "someone to you.\x02\x03",
            "His Grace Chairman Henry MacDowell,\x01",
            "representative of the "autonomous \x01",
            "state of Crossbell"!\x02",
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
    OP_70(0x1, 0x22)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7566", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x12,
        (
            "──I am speaking to the citizens\x01",
            "of Crossbell and to all the persons\x01",
            "who are watching this transmission.\x02\x03",
            "I am Henry Macdowell, Chairman of\x01",
            "the "autonomous state of Crossbell \x01",
            "congress".\x02",
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
    SetCameraDistance(21000, 3000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x3B8)
    OP_24(0x3AA)
    SetScenarioFlags(0x23, 6)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_94CE end

    def Function_28_9BDD(): pass

    label("Function_28_9BDD")

    Sound(938, 2, 70, 0)

    label("loc_9BE3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9BFC")
    Sound(836, 0, 60, 0)
    Sleep(700)
    Jump("loc_9BE3")

    label("loc_9BFC")

    Return()

    # Function_28_9BDD end

    def Function_29_9BFD(): pass

    label("Function_29_9BFD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    ClearMapObjFlags(0x1, 0x4)
    OP_70(0x1, 0x23)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00005F──You figured out a way\x01",
            "to release the "barrier"!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7580", 0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x104, 650, 0, -1250, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x103, -1460, 0, -1190, 0)
    SetChrPos(0x109, -700, 0, -1770, 0)
    SetChrPos(0x106, 200, 0, -2200, 0)
    OP_68(660, 700, 3830, 0)
    MoveCamera(44, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    SetCameraDistance(21850, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetMessageWindowPos(100, 70, -1, -1)
    SetChrName("Meister Jｶrg")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hm, also a way to suppress the\x01",
            "power of those three "Aions".\x02\x03",
            "The key lies in those "big bells".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        (
            "#00201F#12P#N"Big bells"...\x01",
            "Those at the Tower and Temple?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10401F#6PDo you mean that those are strengthening\x01",
            "the barrier and the dolls?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 70, -1, -1)
    SetChrName("Meister Jｶrg")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, what's strengthening them\x01",
            "is the "Sept-Terrion", after all.\x02\x03",
            "However, probably the "Sept-Terrion"\x01",
            "is not perfect as of now.\x02\x03",
            "In order to make manifest that unconventional\x01",
            ""miracle" across a vast area, it seems that\x01",
            "they have to rely on particular "locations".\x02\x03",
            "The "locations" where the "resonance"\x01",
            "is born from the big bells.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#10708F#12PThose big bells have such an ability...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#12PS-So if we stop the\x01",
            "bells' resonance...!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, 70, -1, -1)
    SetChrName("Meister Jｶrg")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hm, you could be able to release\x01",
            "that gigantic barrier...\x02\x03",
            "It could also be possible to suppress the\x01",
            "power of that white "Aion" that annihilated \x01",
            "Garrelia Fortress to a certain degree.\x02\x03",
            "Well, I can't say it for sure, though.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x104,
        (
            "#00305F#12PWell, isn't it\x01",
            "worth a try...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PYes...that barrier and the white\x01",
            "doll are the biggest obstacles.\x02\x03",
            "Until there're those two,\x01",
            "freeing Crossbell City\x01",
            "would be forever impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PAnd that means...\x01",
            "We're going to the "Tower" and "Temple", eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah, the big bell that was taken to the\x01",
            "Ancient Battlefield seems to have been\x01",
            "returned to the city Central Square.\x02\x03",
            "#00000FWe can't do anything with that, but\x01",
            "if it's the "Tower" and "Temple" bells,\x01",
            "we can stop their resonance...!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 70, -1, -1)
    SetChrName("Meister Jｶrg")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, both are places that\x01",
            "the "Society" is guarding.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013F#12PNow that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P#N...It is indeed like that.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(110, 70, -1, -1)
    SetChrName("Meister Jｶrg")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems that Campanella\x01",
            "is at the "Temple of Moon".\x02\x03",
            "And as for the "Tower of Stargaze"...\x01",
            "Arianrhod should be there.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x106,
        "#10701F#12P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PThat eccentric female knight, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P...That's really a problem.\x02\x03",
            "#10408FWe could do something\x01",
            "about the "Fool", but...\x02\x03",
            "#10401FI can only say that it'll be impossible\x01",
            "to win against that "Steel Maiden".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P...Is she that strong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PYeah. Terrific people hang\x01",
            "around the "Society", but...\x02\x03",
            "She's someone on a complete different\x01",
            "level from even such experts.\x02\x03",
            "#10401FHer strength is like it was decided\x01",
            "that no man could ever beat her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#12PS-She's that much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PWazy, it seems you're \x01",
            "someone special called\x01",
            ""Dominion" in the Church...\x02\x03",
            "#00101FEven so, you wouldn't be able to oppose her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PYeah. Even if I used my "Stigma" powers,\x01",
            "I doubt it would be effective against that armor.\x02\x03",
            "#10408FIf someone could oppose her, that would\x01",
            "be our secretary-general, I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PHowever, this is the situation\x01",
            "the entire Zemuria is in.\x02\x03",
            "As you can expect, there's no way that\x01",
            "secretary-general Selnert could act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P*sigh*, that's right.\x02\x03",
            "#10408F...If Kevin were here in such a time,\x01",
            "we could do at least something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#11P──We have no time to be distressed.\x02\x03",
            "#00001FWe finally came to see a hope to be\x01",
            "able to break this situation deadlock.\x02\x03",
            "We can only dare to\x01",
            "try to break in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F#12PI know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#12P#NAgreed.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#10701F#12PNo matter how much of an expert someone is...\x01",
            "I think there's always a chance to beat it.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400F#5PHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PRight...\x01",
            "If we trip in such a place,\x01",
            "we won't reach Bell and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#12PLet's go!\x01",
            "To the "Tower" and "Temple"!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, 70, -1, -1)
    SetChrName("Meister Jｶrg")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, I hope the best for you.\x02\x03",
            "You should at least leave the "Tower"\x01",
            "where Arianrhod is for last.\x02\x03",
            "If you don't want to be killed\x01",
            "by her walkｸres too.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(22850, 2000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can go to the "Temple of Moon" from the\x01",
            "tunnel road fork midway of Mainz Mountain Path.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PartySelect(1)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A4, 2)
    OP_29(0xAF, 0x1, 0x15)
    OP_29(0xAF, 0x4, 0x10)
    OP_29(0xB0, 0x4, 0x2)
    OP_29(0xB0, 0x1, 0x0)
    PlayBGM("ed7570", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 2, 100, 0)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_29_9BFD end

    def Function_30_AF90(): pass

    label("Function_30_AF90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    PartySelect(2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AFB7")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_AFB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AFCA")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_AFCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AFDD")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_AFDD")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0xB)
    SetChrSubChip(0x12, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_70(0x1, 0x26)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x12, -3300, 0, 250, 45)
    SetChrPos(0xF, -3800, 0, -1000, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x104, 650, 0, -1250, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x103, -1460, 0, -1190, 0)
    SetChrPos(0x109, -700, 0, -1770, 0)
    SetChrPos(0x106, 200, 0, -2200, 0)
    OP_68(410, 800, 4070, 0)
    MoveCamera(44, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(21500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105F#12PA-Amazing...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PSo the helpers that spiky\x01",
            "head Father was talkin' about\x01",
            "were dear Estelle and the others!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5PYeah, it seems he took them along\x01",
            "from Liberl at their strong request.\x02\x03",
            "#10402F──More importantly, that's our chance.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12107F#5PUhm, I'll descend to the south exit while\x01",
            "releasing the optical camouflage...!\x02\x03",
            "Descend from the bilge hatch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12PGot it...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P#NThank you.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_B34A():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_B34A)
    Sleep(50)

    def lambda_B35A():
        TurnDirection(0xF, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_B35A)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0xF, 0)
    Sleep(150)

    ChrTalk(
        0x12,
        "#02507F#6P#N──May the Goddess protect you.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xC, 0x2)
    Sleep(50)

    ChrTalk(
        0xC,
        "#01901F#5PEveryone, please be careful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02110F#6P#NI'll collect data\x01",
            "from the skies!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x9, 0x1)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#02302F#5PWell, I'll back you up from\x01",
            "the orbal net too.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 1500)
    StopSound(498, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_AF90 end

    def Function_31_B482(): pass

    label("Function_31_B482")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11402.itc", 0x1E)
    LoadChrToIndex("apl/ch51025.itc", 0x1F)
    LoadChrToIndex("chr/ch11502.itc", 0x20)
    LoadEffect(0x0, "event/ev10037.eff")
    LoadEffect(0x1, "event/ev17103.eff")
    LoadEffect(0x2, "event/ev17104.eff")
    LoadEffect(0x3, "event/ev17105.eff")
    SoundLoad(825)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x17, 0xF)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0xF)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetMapObjFrame(0x6, "base02", 0x2, "sky_ani2")
    SetMapObjFrame(0x6, "base03", 0x2, "sky_ani2")
    SetChrPos(0x1A, 0, 500, 2400, 0)
    SetChrPos(0x19, -3100, -1350, 7100, 315)
    SetChrPos(0x17, 3100, -1350, 7100, 45)
    SetChrPos(0x18, 0, -1350, 6700, 0)
    OP_68(-1590, 1500, 4910, 0)
    MoveCamera(39, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    SetCameraDistance(19850, 2500)
    BeginChrThread(0x17, 0, 0, 32)
    BeginChrThread(0x17, 1, 0, 34)
    BeginChrThread(0x1F, 2, 0, 33)
    Sound(825, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x17,
        "#5P──Surface armor, 70% damaged!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PW-We won't last more than this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#13801F#11PEnemy Aion, accelerating even more!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        (
            "#04303F#11PCr...that's bad.\x02\x03",
            "#04308FIn that case...\x01",
            "I can only use that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x19, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x19, 0x1)
    Sleep(50)
    SetChrSubChip(0x18, 0x1)
    Sleep(50)
    SetChrSubChip(0x17, 0x2)

    ChrTalk(
        0x17,
        "#5PLord Graham...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PDon't tell me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#13807F#5PWait...!\x01",
            "It's too sudden!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        (
            "#04304F#11PIf I can't do my best here, I won't be able to\x01",
            "face your older sister who I succeeded to.\x02\x03",
            "#04300FEveryone, support me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#5P...Acknowledged.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x18, 0x0)
    Sleep(50)
    SetChrSubChip(0x17, 0x0)
    Sleep(300)
    Sound(1002, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1800, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1800, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1300, -200, 4500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x18,
        "#11PActivating Mode Stigma...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x19,
        "#13808F#5PKevin...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        (
            "#04304F#11PDon't worry, Ries.\x02\x03",
            "#04302FAs for your job...\x01",
            "I leave seizing the enemy to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#13801F#5P...All right!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x19, 0x0)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrPos(0x1A, 0, 500, 3300, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    BeginChrThread(0x1A, 0, 0, 35)
    OP_68(-1560, 1500, 5150, 800)
    OP_6F(0x79)
    SetCameraDistance(17800, 25000)
    Sleep(500)

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        "#04303F#11P#3C#40W#19A"O azure seal of mine shining from the abyss..."\x02",
    )

    CloseMessageWindow()
    Sound(895, 0, 100, 0)
    BeginChrThread(0x1F, 0, 0, 36)
    PlayEffect(0x0, 0xFF, 0x1A, 0x3, 0, 400, -100, 0, 0, 0, 650, 650, 650, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x1A, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        (
            "#04303F#11P#3C#40W#21A"Ascend to the sky and change into a pillar \x01",
            "of light illuminating the purgatory..."\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    BeginChrThread(0x1F, 1, 0, 37)
    PlayEffect(0x3, 0xFF, 0x1A, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x17,
        "#5P──Converging the entire "Merkabah"'s orbal power!\x05\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x18,
        (
            "#11P"Stigma" pattern recognised!\x01",
            "Starting to deploy it to the outside!\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "#13807F#11PVariation in enemy Aion!\x01",
            "Deploying main armament and dashing at us!\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        (
            "#04301F#11P#40W#18AIn the name of the 5th Dominion, the\x01",
            ""Thousand Protector", I command you...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    Fade(500)
    EndChrThread(0x1A, 0x0)
    SetChrSubChip(0x1A, 0x5)
    SetCameraDistance(16800, 800)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        "#04307F#11P#4S#15A"Stigma Cannon" Mechidels──activate!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19800, 3000)
    Sound(829, 0, 100, 0)
    FadeToDark(3000, 16777215, -1)
    Sleep(1500)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1F, 0x2)
    OP_0D()
    StopSound(825, 1000, 70)
    StopSound(498, 1000, 100)
    Sleep(1000)
    SetScenarioFlags(0x23, 5)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_B482 end

    def Function_32_BE10(): pass

    label("Function_32_BE10")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BE3E")
    OP_7D(0xFF, 0x50, 0x50, 0x0, 0x1F4)
    Sleep(100)
    Sleep(700)
    OP_7D(0xFF, 0xC8, 0xC8, 0x0, 0x1F4)
    Sleep(600)
    Sleep(100)
    Jump("Function_32_BE10")

    label("loc_BE3E")

    Return()

    # Function_32_BE10 end

    def Function_33_BE3F(): pass

    label("Function_33_BE3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BE61")
    Sleep(100)
    Sound(840, 0, 70, 0)
    Sleep(700)
    Sleep(600)
    Sleep(100)
    Jump("Function_33_BE3F")

    label("loc_BE61")

    Return()

    # Function_33_BE3F end

    def Function_34_BE62(): pass

    label("Function_34_BE62")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BE86")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_34_BE62")

    label("loc_BE86")

    Return()

    # Function_34_BE62 end

    def Function_35_BE87(): pass

    label("Function_35_BE87")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BE9E")
    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("Function_35_BE87")

    label("loc_BE9E")

    Return()

    # Function_35_BE87 end

    def Function_36_BE9F(): pass

    label("Function_36_BE9F")

    Sound(934, 0, 50, 0)
    Sleep(1500)

    label("loc_BEA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BEC1")
    Sound(934, 0, 30, 0)
    Sleep(1500)
    Jump("loc_BEA8")

    label("loc_BEC1")

    Return()

    # Function_36_BE9F end

    def Function_37_BEC2(): pass

    label("Function_37_BEC2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BEDB")
    Sound(929, 0, 50, 0)
    Sleep(2200)
    Jump("Function_37_BEC2")

    label("loc_BEDB")

    Return()

    # Function_37_BEC2 end

    def Function_38_BEDC(): pass

    label("Function_38_BEDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF01")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_BF01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF14")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_BF14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF27")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_BF27")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF3A")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_BF3A")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_4B(0xF, 0xFF)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x14)
    OP_70(0x1, 0x27)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    OP_68(0, 700, 3000, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(20000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#02310F#5P──Still though, something\x01",
            "absurd has appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01908F#5PIs it really true that KeA\x01",
            "made that appear...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PYes...\x01",
            "Is seems there are no doubts about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3CThe "Tree of Azure"── The complete\x01",
            "form of the man-made Sept-Terrion.\x02\x03",
            "#01201FTo think that the deeply-rooted delusions of\x01",
            "the children of man could manage to do that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#5PEven you don't know\x01",
            "what kind of power\x01",
            "that tree holds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3C...Hm.\x01",
            "I only feel something uncommon\x01",
            "from that azure light.\x02\x03",
            "#01200FIt owns all the Septium forces...\x01",
            "But especially "mirage",\x01",
            ""time" and "space" I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PThe "Sept-Terrion of Zero" was\x01",
            "originally created by the Crois clan\x01",
            "to reproduce the "Sept-Terrion of Mirage"...\x02\x03",
            "#00108FDoes it mean that in the process it\x01",
            "even earned "time" and "space"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3CHm, frankly even I\x01",
            "can't fathom what\x01",
            "is capable of.\x02\x03",
            "#01201F──Or rather, it could\x01",
            "be said that "there's\x01",
            "nothing it can't do".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12PWhat the...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12100F#5PA power that rivals the Goddess', eh...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#11PIn any case...\x01",
            "What we'll do doesn't change.\x02\x03",
            "#00008FMr. Arios, Miss Mariabell,\x01",
            "Lawyer Ian and the others...\x02\x03",
            "#00013FWe'll confirm their real intentions\x01",
            "and get KeA back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#12P...Yes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02110F#6PMaaan, how should I put it,\x01",
            "I'm seriously shaking with excitement!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)

    def lambda_C658():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_C658)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0xC, 0x2)

    def lambda_C66D():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C66D)
    Sleep(50)

    def lambda_C67D():
        TurnDirection(0x102, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C67D)
    Sleep(50)

    def lambda_C68D():
        TurnDirection(0x103, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C68D)
    Sleep(50)

    def lambda_C69D():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C69D)
    Sleep(50)

    def lambda_C6AD():
        TurnDirection(0x109, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C6AD)
    Sleep(50)

    def lambda_C6BD():
        TurnDirection(0x106, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_C6BD)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    SetChrFlags(0x13, 0x20)

    def lambda_C6E7():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C6E7)
    ClearChrFlags(0x13, 0x20)

    ChrTalk(
        0x10A,
        (
            "#00606F#11P...Grace.\x01",
            "Why are you here?\x02\x03",
            "#00601FDidn't you get off the ship\x01",
            "with Chairman MacDowell?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10A, 500)

    ChrTalk(
        0xF,
        (
            "#02103F#5POh, shut up.\x01",
            "It's my own decision, alright?\x02\x03",
            "#02100FAlso, even Crossbell citizens\x01",
            "should be wanting to know the facts.\x02\x03",
            "#02109FWell, let me support\x01",
            "you on that regard㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F#11PY-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#11PI am feeling somewhat uneasy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PIn any event, before goin' there\x01",
            "it would be better to prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12PRight...\x01",
            "We don't know what\x01",
            "will await us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PFightings have ceased in every place\x01",
            "so we could descend with the Merkabah\x01",
            "wherever we want in Crossbell now.\x02\x03",
            "#10400FJust give the order if you need to.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#00000F#11PYeah, all right.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A7, 1)
    OP_29(0xB2, 0x4, 0x2)
    OP_29(0xB2, 0x1, 0x0)
    SetScenarioFlags(0x34, 6)
    SetScenarioFlags(0x37, 6)
    SetScenarioFlags(0x20, 5)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7150", "ed7563")
    ReplaceBGM("ed7101", "ed7563")
    ReplaceBGM("ed7116", "ed7563")
    ReplaceBGM("ed7117", "ed7563")
    ReplaceBGM("ed7111", "ed7563")
    ReplaceBGM("ed7113", "ed7563")
    Sleep(500)
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_38_BEDC end

    def Function_39_CAF9(): pass

    label("Function_39_CAF9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F(The "Tree of Azure"...\x01",
            "KeA and the entire\x01",
            "truth are waiting there...)\x02\x03",
            "#00013F(Are we prepared...?)\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "[We Still Have Other Things to Do]\x01",      # 0
            "[Head to the "Tree of Azure"]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CBE0"),
        (1, "loc_CBEE"),
        (SWITCH_DEFAULT, "loc_CD48"),
    )


    label("loc_CBE0")

    FadeToBright(0, 0)
    Jump("loc_CD48")

    label("loc_CBEE")

    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC3F")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_CD2F")

    label("loc_CC3F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC62")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_CD2F")

    label("loc_CC62")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC85")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_CD2F")

    label("loc_CC85")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCA8")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_CD2F")

    label("loc_CCA8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCCB")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_CD2F")

    label("loc_CCCB")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCEE")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_CD2F")

    label("loc_CCEE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD11")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_CD2F")

    label("loc_CD11")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD2F")
    SetScenarioFlags(0x3C, 7)

    label("loc_CD2F")

    PartySelect(2)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x23, 7)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Jump("loc_CD48")

    label("loc_CD48")

    Return()

    # Function_39_CAF9 end

    def Function_40_CD49(): pass

    label("Function_40_CD49")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    SoundLoad(498)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CD71")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_CD71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CD84")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_CD84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CD97")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_CD97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CDAA")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_CDAA")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x14)
    OP_70(0x1, 0x28)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x6, "base02", 0x2, "sky_ani2")
    SetMapObjFrame(0x6, "base03", 0x2, "sky_ani2")
    BeginChrThread(0x101, 3, 0, 41)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    OP_68(370, 700, 3790, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20750, 0)
    SetCameraDistance(20000, 1500)
    Sound(498, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xC,
        (
            "#01901F#5P──Confirmed a sighting at 5 o'clock!\x02\x03",
            "It's the "Beowulf" belonging\x01",
            "to the Red Constellation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12PSo they showed up...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12P#NThe warship in use to the\x01",
            ""Red Constellation"...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#12PYeah, there were talkings 'bout\x01",
            "makin' use of a warship\x01",
            "since my times there...\x02\x03",
            "#00311FBut I can't believe they can use\x01",
            "something like that already...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PMaybe for their current plan the Crois\x01",
            "clan furnished them with funds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11PIt appears they're also using some\x01",
            "of the "Society"'s technologies...\x02\x03",
            "#10408FAbbas, can you shake it off?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12100F#5PI'll try to do something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02302F#5PWell, it's not only huge but rugged too,\x01",
            "we won't lose in speed to that, right?\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sound(499, 0, 80, 0)
    SetMapObjFrame(0x6, "base02", 0x2, "sky_ani3")
    SetMapObjFrame(0x6, "base03", 0x2, "sky_ani3")
    OP_68(370, 700, 790, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x24, 0)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_CD49 end

    def Function_41_D2C5(): pass

    label("Function_41_D2C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D2E9")
    OP_82(0x2, 0x2, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_41_D2C5")

    label("loc_D2E9")

    Return()

    # Function_41_D2C5 end

    def Function_42_D2EA(): pass

    label("Function_42_D2EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("apl/ch51216.itc", 0x1F)
    LoadChrToIndex("apl/ch51217.itc", 0x20)
    LoadChrToIndex("apl/ch51218.itc", 0x21)
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    LoadChrToIndex("apl/ch51220.itc", 0x23)
    LoadChrToIndex("apl/ch51223.itc", 0x24)
    LoadChrToIndex("apl/ch51224.itc", 0x25)
    LoadChrToIndex("apl/ch51774.itc", 0x26)
    LoadEffect(0x0, "event/ev17053.eff")
    LoadEffect(0x1, "event/ev17021.eff")
    LoadEffect(0x2, "event/ev17057.eff")
    SoundLoad(498)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    OP_F3(100000)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    SetChrPos(0x1E, 17000, -750, 13000, 0)
    OP_68(370, 700, 3790, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x101, 0, 0, 32)
    BeginChrThread(0x101, 1, 0, 34)
    BeginChrThread(0x1F, 2, 0, 33)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(498, 2, 100, 0)
    BeginChrThread(0x1F, 1, 0, 43)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#02311F#5PUwaaaaah!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10712F#12P#NT-Those are...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10110F#12P#NNo way...\x01",
            "It scattered electromagnetic mines in the sky!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#12P#N...No doubt! Those are in\x01",
            "use at the Foundation too!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x1, 0x1, 0x1E, 0x1, 0, 0, 0, 0, 0, 0, 80, 80, 80, 0xFF, 0, 0, 0, 0)

    def lambda_D676():
        OP_96(0xFE, 0x2710, 0xFFFFFD12, 0x4E20, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_D676)

    ChrTalk(
        0x10A,
        "#00610F#12P#NThey're used to battles for sure...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopEffect(0x0, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1F, 0x2)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10410F#12PKh...now they've done it.\x02\x03",
            "#10407FThey circled around to the starboard bow!\x01",
            "Abbas, deploy the anti-shock field!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        (
            "#12107F#11P──Roger!\x02\x03",
            "All people, squat down and\x01",
            "brace for the impact!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x24)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x106, 0x25)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    OP_0D()
    Sound(920, 0, 100, 0)
    Sound(921, 0, 100, 0)
    Sound(922, 0, 100, 0)
    PlayEffect(0x2, 0x2, 0xFF, 0x0, 5000, 0, 18000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x24, 1)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_D2EA end

    def Function_43_D87B(): pass

    label("Function_43_D87B")

    Sound(204, 0, 100, 0)

    label("loc_D881")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D89A")
    Sound(203, 0, 100, 0)
    Sleep(900)
    Jump("loc_D881")

    label("loc_D89A")

    Return()

    # Function_43_D87B end

    def Function_44_D89B(): pass

    label("Function_44_D89B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("apl/ch51216.itc", 0x1F)
    LoadChrToIndex("apl/ch51217.itc", 0x20)
    LoadChrToIndex("apl/ch51218.itc", 0x21)
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    LoadChrToIndex("apl/ch51220.itc", 0x23)
    LoadChrToIndex("apl/ch51223.itc", 0x24)
    LoadChrToIndex("apl/ch51224.itc", 0x25)
    LoadChrToIndex("apl/ch51774.itc", 0x26)
    LoadEffect(0x0, "event/ev17057.eff")
    SoundLoad(498)
    SoundLoad(825)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x24)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x106, 0x25)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    OP_68(370, 700, 3790, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x101, 0, 0, 32)
    BeginChrThread(0x1F, 2, 0, 33)
    Sound(498, 2, 100, 0)
    Sound(825, 2, 100, 0)
    FadeToBright(1000, 0)
    Sound(833, 0, 100, 0)
    Sound(200, 0, 50, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x3E8)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00010F#12PShi...!\x02",
    )

    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(500)
    OP_82(0x14, 0x14, 0xBB8, 0x1F4)
    Sleep(500)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 34)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#02106F#6P#NEeeeeeeek!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xC,
        (
            "#01911F#5P──I-It's all right!\x01",
            "The damage to the ship is slight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10407F#11PAlright, focus the anti-shock\x01",
            "field to the front nose!\x02\x03",
            "Let's head like this to the "huge tree" while\x01",
            "forcing our way through the minefield!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#12107F#11P#4SRoger!\x02",
    )

    CloseMessageWindow()
    Sound(920, 0, 100, 0)
    Sound(921, 0, 100, 0)
    Sound(922, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 0, 13000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    Sound(499, 0, 100, 0)
    SetMapObjFrame(0x6, "base02", 0x2, "sky_ani3")
    SetMapObjFrame(0x6, "base03", 0x2, "sky_ani3")
    OP_68(370, 700, 790, 1000)
    StopSound(498, 1000, 100)
    StopSound(825, 1000, 100)
    EndChrThread(0x1F, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x24, 2)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_D89B end

    def Function_45_DD3E(): pass

    label("Function_45_DD3E")

    OP_F4(0x5)
    Return()

    # Function_45_DD3E end

    SaveToFile()

Try(main)
