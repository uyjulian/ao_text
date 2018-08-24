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
        "Function_9_2497",         # 09, 9
        "Function_10_39F3",        # 0A, 10
        "Function_11_3A35",        # 0B, 11
        "Function_12_401E",        # 0C, 12
        "Function_13_40DB",        # 0D, 13
        "Function_14_478D",        # 0E, 14
        "Function_15_47A8",        # 0F, 15
        "Function_16_5571",        # 10, 16
        "Function_17_6192",        # 11, 17
        "Function_18_66C7",        # 12, 18
        "Function_19_66EC",        # 13, 19
        "Function_20_67EC",        # 14, 20
        "Function_21_76AE",        # 15, 21
        "Function_22_7902",        # 16, 22
        "Function_23_8E4C",        # 17, 23
        "Function_24_9188",        # 18, 24
        "Function_25_9584",        # 19, 25
        "Function_26_959A",        # 1A, 26
        "Function_27_95B3",        # 1B, 27
        "Function_28_9C88",        # 1C, 28
        "Function_29_9CA8",        # 1D, 29
        "Function_30_B021",        # 1E, 30
        "Function_31_B507",        # 1F, 31
        "Function_32_BE7F",        # 20, 32
        "Function_33_BEAE",        # 21, 33
        "Function_34_BED1",        # 22, 34
        "Function_35_BEF6",        # 23, 35
        "Function_36_BF0E",        # 24, 36
        "Function_37_BF31",        # 25, 37
        "Function_38_BF4B",        # 26, 38
        "Function_39_CB55",        # 27, 39
        "Function_40_CDA7",        # 28, 40
        "Function_41_D2F8",        # 29, 41
        "Function_42_D31D",        # 2A, 42
        "Function_43_D8B7",        # 2B, 43
        "Function_44_D8D7",        # 2C, 44
        "Function_45_DD5F",        # 2D, 45
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
            "As planned, we'll take\x01",
            "on the "Doll".\x02\x03",
            "Be careful now, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10404F#6PHeh, likewise, Heretic\x01",
            "Hunter... No, the\x01",
            "Thousand-Hand Guardian.\x02\x03",
            "#10402FEven if you did change\x01",
            "your title, not even you\x01",
            "get a pass from this.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(140, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Haha, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#12102F#6PHowever... A title derived\x01",
            "from Rufina, the Thousand\x01",
            "Arms herself is...\x02\x03",
            "It's a good one, Lord\x01",
            "Graham.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(145, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "... Thank you.\x02",
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
        (
            "#00008F#12P(Seems like a lot of\x01",
            "things are going on...)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(85, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─Lloyd. It's gonna be tough from here on, but\x01",
            "do your best, alright?\x02\x03",
            "In Crossbell's current situation, relying on\x01",
            "help from the outside isn't possible.\x02\x03",
            "If there's something right now that you\x01",
            "should absolutely put your faith into, that's\x01",
            "the bonds that you've built in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00005F#12PThe bonds I've built...\x02\x03",
            "#00004F─I understand. I'll keep\x01",
            "that in mind.\x02",
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
            "Lloyd, may Aidios bless\x01",
            "you with her divine\x01",
            "protection.\x02\x03",
            "And, please take good\x01",
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
        "#00011F#12PWhat was that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#11PI activated an optical\x01",
            "camouflage mechanism.\x02\x03",
            "Of course, it's not perfect by\x01",
            "any means. The drawback is that\x01",
            "our speed drops when it's used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11PIf we infiltrated in our current\x01",
            "state, that high-mobility type doll\x01",
            "would immediately get the drop on us.\x02\x03",
            "#10401FEven if we fought it on even footing,\x01",
            "we'd have no chance. We'll have the\x01",
            "No. 5 attract its attention instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PI see... That'll be our\x01",
            "chance to get in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3C#12PHm, so you'll finally show us the\x01",
            "true potential of the Gralsritter's\x01",
            ""Protectors of the Skies".\x02",
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

    def Function_9_2497(): pass

    label("Function_9_2497")

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
            "#10406F#5P─Somehow we managed to break through,\x01",
            "but it seems that Crossbell itself\x01",
            "has become one with the Sept-Terrion.\x02\x03",
            "#10401FIf we aren't careful with our\x01",
            "movement, the dolls will likely\x01",
            "engage us again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PSo this airship does\x01",
            "have limits after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3CIndeed, if we were to try to land, we'd\x01",
            "get caught in the "net" of the Pleroma\x01",
            "Grass, due to the size of this ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PExactly. As it is, landing\x01",
            "isn't an option...\x02\x03",
            "#10400FI'm thinking about searching\x01",
            "for a "gap" in the septium\x01",
            "vein force field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#11PA "gap" in the force\x01",
            "field...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CBy nature, the septium vein\x01",
            "spawns a forcefield that spans\x01",
            "the entirety of the planet.\x02\x03",
            "#01200FHowever, a "gap" may appear\x01",
            "amongst it's bigger streams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see...\x02\x03",
            "#00000FThat means if we land\x01",
            "within that 'gap', we'll\x01",
            "pass through unnoticed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5PHeh, you got it.\x02\x03",
            "#10402FAnd so, the point we're\x01",
            "at now is the place\x01",
            "we've been looking for.\x02",
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
            "#00001FSt. Ursula Byroad's\x01",
            "sandbank... Near where that\x01",
            "Cryptid appeared before...\x02\x03",
            "#00005FStill, you did a good job\x01",
            "finding this place.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 200, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10404FHeh. Before this chain of\x01",
            "events occurred, I searched\x01",
            "for it with Abbas.\x02\x03",
            "#10402FAnd, after working a little\x01",
            "of our magic, we managed to\x01",
            "escape Crossbell.\x02",
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
        (
            "#01203F#3CIt was a very well\x01",
            "thought out plan.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 200, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10404F#0CWell, this is the only place we've\x01",
            "found for now, so we'll need to\x01",
            "find more "gaps" in the future.\x02",
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
            "#10403F#5P─So, what's the plan?\x02\x03",
            "#10400FBecause it's surrounded by a\x01",
            "barrier, we wouldn't be able\x01",
            "to get into Crossbell anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P...You're right. Even so,\x01",
            "let's touch down for now.\x02\x03",
            "#00008FI want to learn about the\x01",
            "situation in Crossbell,\x01",
            "even if just a little...\x02\x03",
            "#00001FI also want to confirm\x01",
            "what's going on at St.\x01",
            "Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#5PHaha, roger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#11P#3CThen, let us descend.\x02",
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
        "#01200F#5P#3CHmm, what troubles you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11POh, well it's a bit late\x01",
            "for this but...\x02\x03",
            "#00001FZeit, why are you\x01",
            "helping us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PAccording to what the dragon of Liberl\x01",
            "said...\x02\x03",
            "#10401FRegarding the destiny surrounding the\x01",
            "Sept-Terrions, you divine beasts are only\x01",
            "allowed to act only as observers. Meaning\x01",
            "you can't intervene, is that correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3CSo it is─ We made an ancient\x01",
            ""oath".\x02\x03",
            "#01200FHowever, now that the Sept-\x01",
            "Terrion of Mirage has been lost,\x01",
            "my original mission has ended.\x02\x03",
            "Therefore, the "taboo" that\x01",
            "bound me has faded and I can act\x01",
            "freely to a certain extent.\x02\x03",
            "I can at least provide some\x01",
            "assistance to the children of\x01",
            "man.\x02",
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
            "#00008F#11PSo that's why you helped\x01",
            "us in the mafia military\x01",
            "dogs case too...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CYes, precisely.\x02\x03",
            "#01200FI can't support you indefinitely,\x01",
            "but... I'll support you as I have\x01",
            "been for some time already.\x02\x03",
            "I am still registered as a\x01",
            ""police dog" for the time being,\x01",
            "so make use of me as you wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PHaha, got it. Thanks for\x01",
            "lending us your\x01",
            "strength.\x02",
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
            "#10404F#5PSo it seems that we'll move\x01",
            "around with this formation\x01",
            "for a little while.\x02\x03",
            "#10400F─When you feel like landing,\x01",
            "talk to Abbas.\x02\x03",
            "Also, within the Merkabah,\x01",
            "you'll find a few facilities\x01",
            "for your own use.\x02\x03",
            "#10404FEquipment, tools, workshop\x01",
            "functions─ If you need them,\x01",
            "let the crew know.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00000F#11PAlright, roger that.\x02",
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
            "Wazy and Zeit have\x01",
            "joined the party.\x07\x00\x02",
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
            "Akashic Arm\x07\x05",
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
            " as\x01",
            "S-Break?",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363C")
    SetChrChipPat(0x4, 0x6, 0x12D)

    label("loc_363C")

    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "For the time being, Zeit has joined as a\x01",
            "party member.\x02\x03",
            "Because he doesn't carry an Enigma II, you\x01",
            "cannot customize quartz, but he does have\x01",
            "powerful high-level arts at his disposal.\x02\x03",
            "However, because he doesn't have an\x01",
            "S-Craft, you'll need to be careful.\x07\x00\x02",
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
            "Furthermore─ Although only Lloyd will move\x01",
            "while onboard the Merkabah, the other\x01",
            "members will be on standby inside the ship.\x02\x03",
            "However, it is possible to manage all\x01",
            "members using the camp menu, and also when\x01",
            "using the shops.\x07\x00\x02",
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

    # Function_9_2497 end

    def Function_10_39F3(): pass

    label("Function_10_39F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A34")
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Jump("Function_10_39F3")

    label("loc_3A34")

    Return()

    # Function_10_39F3 end

    def Function_11_3A35(): pass

    label("Function_11_3A35")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E55")

    ChrTalk(
        0x8,
        (
            "#12100F#11P─So, what do you plan to\x01",
            "do now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PWell, we've decided to\x01",
            "land, at least.\x02\x03",
            "#00000FBy the way, I would've\x01",
            "never imagined you guys to\x01",
            "have such a background.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11PEverything was planned to confuse those inside\x01",
            "the church... To mislead the eyes of Archbishop\x01",
            "Eralda who criticizes our sacred order.\x02\x03",
            "No one would ever think that one of the highest\x01",
            "ranked Gralsritter is acting as the head of a\x01",
            "group of thugs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PWell, I guess you're right.\x02\x03",
            "#00005FAh, but I feel like you were\x01",
            "using faith-related words like\x01",
            "Testaments, crusade and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12105F#11PHmm, really?\x02\x03",
            "#12100FOn the contrary, I thought I\x01",
            "could deceive you by making\x01",
            "a shameless impression...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, your delinquent group really\x01",
            "does have a unique atmosphere. I\x01",
            "guess it really did deceive us.\x02\x03",
            "#00000F─So, can we land right away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11PYes. We were able to\x01",
            "pinpoint a "gap".\x02\x03",
            "Just let me know when\x01",
            "you're ready.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1A0, 1)
    Jump("loc_3ED0")

    label("loc_3E55")


    ChrTalk(
        0x8,
        (
            "#12100F#11PWe've pinpointed the "gap".\x02\x03",
            "Just let me know when\x01",
            "you're ready to land at the\x01",
            "St. Ursula Byroad sandbank.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED0")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Land the Merkabah\x01",      # 0
            "Cancel\x01",                 # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F23"),
        (1, "loc_3FBB"),
        (SWITCH_DEFAULT, "loc_401D"),
    )


    label("loc_3F23")


    ChrTalk(
        0x8,
        (
            "#12102F#11PRoger. Confirm the place\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_3F9B")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x8, 0x0)
    Call(0, 12)
    Call(0, 5)
    Call(0, 7)
    Jump("loc_3FB6")

    label("loc_3F9B")

    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x0, -1500, -1500, 6000, 45)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_3FB6")

    Jump("loc_401D")

    label("loc_3FBB")


    ChrTalk(
        0x8,
        (
            "#12100F#11PIn that case, just let\x01",
            "me know when you're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x0, -1500, -1500, 6000, 45)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_401D")

    label("loc_401D")

    Return()

    # Function_11_3A35 end

    def Function_12_401E(): pass

    label("Function_12_401E")

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

    # Function_12_401E end

    def Function_13_40DB(): pass

    label("Function_13_40DB")

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
            "#00203F#12P#N...Detected a new Gap in\x01",
            "the septium vein force\x01",
            "field...\x02\x03",
            "#00202FSending the data now.\x02",
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
            "Coordinates identified!\x02\x03",
            "It's near Armorica\x01",
            "Village, in NE\x01",
            "Crossbell!\x02",
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
            "#12102F#11PYes, they're quite helpful.\x02\x03",
            "There's Plato's senses, of course, but\x01",
            "having a dedicated operator greatly\x01",
            "raises the ship's operational efficiency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909F#5PEhehe... I'm still\x01",
            "inexperienced, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11PHaha. It looks like we'll be\x01",
            "able to efficiently search for\x01",
            "landing spots from now on.\x02",
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
            "Want to try going to the\x01",
            "new point?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PYeah. It looks like we\x01",
            "can check on the\x01",
            "situation in Armorica.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#11PAll ahead full. Set\x01",
            "course for the Armorica\x01",
            "Village airspace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#12P#NCourse laid in.\x01",
            "Maintaining high alert.\x02",
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

    def lambda_4680():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4680)
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
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_4783")
    FadeToDark(0, 0, -1)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4778")
    Call(0, 6)
    Jump("loc_477B")

    label("loc_4778")

    Call(0, 5)

    label("loc_477B")

    Call(0, 7)
    Jump("loc_478C")

    label("loc_4783")

    NewScene("e3020", 102, 0, 0)
    IdleLoop()

    label("loc_478C")

    Return()

    # Function_13_40DB end

    def Function_14_478D(): pass

    label("Function_14_478D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47A7")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_14_478D")

    label("loc_47A7")

    Return()

    # Function_14_478D end

    def Function_15_47A8(): pass

    label("Function_15_47A8")

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
            "#00204F#12P#NNew Gap detected.\x02\x03",
            "#00202FFran, sending you the\x01",
            "data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909F#5PYes ma'am. (*type type\x01",
            "type*...)\x02\x03",
            "#01905F─Here it is! Northwest\x01",
            "Crossbell...\x02\x03",
            "#01901FA point in the middle of\x01",
            "Mainz Mountain Path!\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        (
            "#00002F#12PThe Mainz area, huh? The\x01",
            "areas where we can act\x01",
            "have increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11PWell, they've probably\x01",
            "started to notice our\x01",
            "actions as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P#N... According to information from\x01",
            "Heiyue, a resistance is being\x01",
            "mounted in the Mainz region.\x02\x03",
            "#10701FI heard the leader is a former\x01",
            "CGF member who objected to\x01",
            "joining the State Guard.\x02",
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

    def lambda_4BDF():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BDF)
    SetChrFlags(0x107, 0x20)

    def lambda_4BF1():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4BF1)
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
        "#00011F#5PR-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PI thought all CGF members\x01",
            "would have joined the\x01",
            "State Guard for sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PWell, it's understandable.\x02\x03",
            "Red Constellation is still on the\x01",
            "move after all, and they gave the\x01",
            "CGF a run for their money.\x02\x03",
            "It's not surprising that someone\x01",
            "else saw through their deception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01901F#5PT-Then.. My sister could\x01",
            "be...!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00006F#11P... No. Unfortunately, I\x01",
            "don't think that's the case.\x02\x03",
            "#00008FAfter taking it all in, Noｱl\x01",
            "chose the path of protecting\x01",
            "the current Crossbell.\x02\x03",
            "#00013FI don't think it'll be so\x01",
            "easy to change her decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01912F#5P#30W...Ahaha, that's true.\x02\x03",
            "#01908F#30WBig sis is really\x01",
            "strong... And darn\x01",
            "stubborn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#5P...Fran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PWell in any case, I'd\x01",
            "like to make contact\x01",
            "with this resistance.\x02\x03",
            "#10400FDepending on the\x01",
            "situation, they could be\x01",
            "of help, like Heiyue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#11PYeah. Anyway, let's try\x01",
            "touching down.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#5P... By the way, Rixia.\x02\x03",
            "#00000FBefore that, do you want\x01",
            "to stop by St. Ursula\x01",
            "Hospital?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#10712F#12PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PIlya really wanted to see\x01",
            "you, you know?\x02\x03",
            "#00002FA lot has happened,\x01",
            "but... Why don't you show\x01",
            "her your happy face?\x02",
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
            "#10708FI can't stand in front of Ilya\x01",
            "with confidence yet...\x02\x03",
            "#10710FPlease, let me endure at least\x01",
            "until after we've freed Crossbell\x01",
            "City and taken back Arc-en-Ciel.\x02",
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
            "#00206F#5PIt's frustrating, but...\x01",
            "I think I understand how\x01",
            "you feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10709F#12PAhaha... Sorry, it's just...\x02\x03",
            "#10702FOh, if you have something to\x01",
            "do there, I don't mind going\x01",
            "to St. Ursula Hospital...!\x02\x03",
            "#10704FI'll just, well, wait for\x01",
            "you in front of the\x01",
            "hospital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, understood.\x02\x03",
            "#00000F(Nevertheless, Rixia...\x01",
            "She really has an honest\x01",
            "personality.)\x02",
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
            "Rixia has joined the\x01",
            "party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53EE")
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1A9)
    Jump("loc_53F6")

    label("loc_53EE")

    AddCraft(0x5, 0x195)
    AddCraft(0x0, 0x195)

    label("loc_53F6")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Rixia learned the\x01\x07\x02",
            ""Double Dragon Strike"\x07\x05",
            " Combi Craft.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By each expending 100 CP,\x01",
            "a powerful combination\x01",
            "attack can be unleashed.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_5567")
    FadeToDark(0, 0, -1)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_555C")
    Call(0, 6)
    Jump("loc_555F")

    label("loc_555C")

    Call(0, 5)

    label("loc_555F")

    Call(0, 7)
    Jump("loc_5570")

    label("loc_5567")

    NewScene("e3020", 102, 0, 0)
    IdleLoop()

    label("loc_5570")

    Return()

    # Function_15_47A8 end

    def Function_16_5571(): pass

    label("Function_16_5571")

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
            "#02109F#11PWooow... It really is a\x01",
            "great airship!\x02\x03",
            "#02110FI can't believe the\x01",
            "Church had ships like\x01",
            "this at their disposal!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12100F#5P...I'll say it again. I beg\x01",
            "you not to tell a word of this\x01",
            "to anyone.\x02\x03",
            "If it were to appear in a news\x01",
            "article, be prepared to never\x01",
            "again have Church support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10409F#11PHaha. Even if it was featured\x01",
            "in an article, maybe it would\x01",
            "just be thought of as drivel.\x02\x03",
            "#10402FLike with Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12107F#5PWazy!\x02",
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
            "#02104F#5PDon't worry, I'll keep\x01",
            "my promise.\x02\x03",
            "#02100FEven about Rixia Mao's\x01",
            "true identity being the\x01",
            "mysterious demon, Yin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10706F#12P#N...Please, no more.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#12P(Say, Lloyd...)\x02\x03",
            "#00301F(Was it really a good\x01",
            "idea to take her along?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11P(W-Well, i think she's\x01",
            "someone who stays true\x01",
            "to her promises...)\x02",
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
            "#00201F#11PI sensed a new Gap in\x01",
            "the western part of\x01",
            "Crossbell.\x02",
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
            "#01908F#5P(*type type*...) Correct\x01",
            "coordinates pinpointed.\x02\x03",
            "#01903FWest Crossbell Highway,\x01",
            "the midpoint...\x02\x03",
            "#01901FNear the fork in the road\x01",
            "to the police academy and\x01",
            "prison areas.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        "#00001F#11PIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PYou said that when you\x01",
            "escaped from prison you were\x01",
            "helped by ol' man Garcｵa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah... No matter what\x01",
            "you say, he ended up\x01",
            "helping me greatly.\x02\x03",
            "#00008FI'm concerned about what\x01",
            "happened to him after\x01",
            "that though...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(50)

    ChrTalk(
        0x105,
        (
            "#10406F#5PHowever, going to the\x01",
            "police academy area isn't a\x01",
            "good plan.\x02\x03",
            "#10401FBecause you escaped,\x01",
            "they've probably reinforced\x01",
            "security there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P#NHaving said that, Bellguard Gate,\x01",
            "where the State Guard is stationed,\x01",
            "is the only other place we can go...\x02\x03",
            "#10701FThat's a bit of a problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#02106F#11PWell, it's a no-brainer that\x01",
            "you would be arrested on the\x01",
            "spot if they saw you there.\x02",
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
            "#00003F#11P...In any case, let's just try to land.\x02\x03",
            "#00001FI want to confirm to what extent the\x01",
            "State Guard is guarding and I'm also\x01",
            "worried about Cryptids wandering around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PRoger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PI established a "magic\x01",
            "circle" within the mining\x01",
            "town some time ago, too.\x02\x03",
            "We can land whenever you\x01",
            "want, so just say the\x01",
            "word whenever needed.\x02",
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
            "Randy has joined the\x01",
            "party.\x07\x00\x02",
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
            "Randy learned the\x01\x07\x02",
            "Berserker\x07\x05",
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
            " as\x01",
            "S-Break?",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6139")
    SetChrChipPat(0x3, 0x6, 0x129)

    label("loc_6139")

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

    # Function_16_5571 end

    def Function_17_6192(): pass

    label("Function_17_6192")

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
            "Afterwards, Noｱl collected her\x01",
            "belongings and boarded the Merkabah\x01",
            "with Lloyd and the others.\x07\x00\x02",
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

    def lambda_6397():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6397)

    def lambda_63AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_63AC)
    Sleep(100)

    def lambda_63C0():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_63C0)

    def lambda_63D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_63D5)
    Sleep(500)

    def lambda_63E9():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_63E9)

    def lambda_63FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_63FE)
    Sleep(100)

    def lambda_6412():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6412)

    def lambda_6427():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6427)
    Sleep(500)

    def lambda_643B():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_643B)

    def lambda_6450():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6450)
    Sleep(100)

    def lambda_6464():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6464)

    def lambda_6479():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6479)
    Sleep(800)

    def lambda_648D():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_648D)

    def lambda_64A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_64A2)
    Sleep(2000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_64CB():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_64CB)

    def lambda_64E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_64E0)
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

    def lambda_6551():

        label("loc_6551")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6551")

    QueueWorkItem2(0x101, 2, lambda_6551)

    def lambda_6563():

        label("loc_6563")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6563")

    QueueWorkItem2(0x103, 2, lambda_6563)

    def lambda_6575():

        label("loc_6575")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6575")

    QueueWorkItem2(0x104, 2, lambda_6575)

    def lambda_6587():

        label("loc_6587")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6587")

    QueueWorkItem2(0x105, 2, lambda_6587)

    def lambda_6599():

        label("loc_6599")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6599")

    QueueWorkItem2(0x106, 2, lambda_6599)
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
            "started to shed tears after hugging\x01",
            "Noｱl without saying a word...\x02\x03",
            "While calming her younger sister,\x01",
            "Noｱl's eyes also brimmed with tears.\x07\x00\x02",
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

    # Function_17_6192 end

    def Function_18_66C7(): pass

    label("Function_18_66C7")


    def lambda_66CC():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_66CC)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_66C7 end

    def Function_19_66EC(): pass

    label("Function_19_66EC")

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

    def lambda_6773():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_6773)
    WaitChrThread(0x1C, 2)
    Sleep(500)

    def lambda_6793():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_6793)
    WaitChrThread(0x1C, 2)
    Sleep(1500)

    def lambda_67B3():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_67B3)
    WaitChrThread(0x1C, 2)
    Sleep(500)

    def lambda_67D3():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_67D3)
    WaitChrThread(0x1C, 2)
    Return()

    # Function_19_66EC end

    def Function_20_67EC(): pass

    label("Function_20_67EC")

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
            "#00204F#11P─Sensed a 'Gap' in the\x01",
            "Michelam area.\x02\x03",
            "#00202FFran, I'm sending the\x01",
            "coordinates.\x02",
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
            "#10106F#12PJeez... How long are you\x01",
            "going to cry for?\x02\x03",
            "#10101FEveryone will laugh at\x01",
            "you, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PHaha, it's alright,\x01",
            "Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10709F#12P#NHaha... Somehow I'm\x01",
            "envious.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(836, 0, 100, 0)

    ChrTalk(
        0xC,
        (
            "#01909F#5PEhehe... I'm sorry.\x02\x03",
            "#01900F(*type type*...) ─Got\x01",
            "it!\x02\x03",
            "#01903FNear Hotel Delphinia at\x01",
            "Michelam Health\x01",
            "Resort...\x02\x03",
            "#01901FIt's at Lake Beach!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#12P*whew*, that's one crazy\x01",
            "coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11PHehe, we can hardly call\x01",
            "it a vacation this time,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#02105F#5PMy, could it be that...\x02\x03",
            "You all went to have fun\x01",
            "at the beach?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    def lambda_6CCD():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6CCD)
    Sleep(50)

    def lambda_6CDD():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6CDD)
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
        (
            "#00204F#5PAfter the trade\x01",
            "conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02106F#5PGeez, how cold of you.\x02\x03",
            "#02101FWhy didn't you call me\x01",
            "for such an enjoyable\x01",
            "event?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11PWell, we were invited...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10408F#5PThinking about it, that\x01",
            "invitation could have had some\x01",
            "ulterior motives as well.\x02",
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
            "#00003F#11P─At any rate, our next\x01",
            "destination is decided.\x02\x03",
            "#00008FA Red Constellation unit\x01",
            "seems to guarding the\x01",
            "place...\x02\x03",
            "#00001FNoｱl, do you know its\x01",
            "size?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PLet's see... I think\x01",
            "there's one division.\x02\x03",
            "#10113FEven with these numbers,\x01",
            "I honestly don't think\x01",
            "we can beat them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#11PIf we could disperse\x01",
            "their forces with a\x01",
            "diversion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#12P#NIn that case, leave it\x01",
            "to m──\x02",
        )
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
            "#01203F#11P#3CNo, I'll take care of\x01",
            "that.\x02\x03",
            "#01201FIf I return to my original\x01",
            "form, I'll be able to lure\x01",
            "quite a few of them.\x02",
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

    def lambda_71C4():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_71C4)
    Sleep(50)

    def lambda_71D4():
        TurnDirection(0x104, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_71D4)
    Sleep(50)

    def lambda_71E4():
        TurnDirection(0x109, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_71E4)
    Sleep(50)

    def lambda_71F4():
        TurnDirection(0x106, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_71F4)
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
        "#00001F#5PHmm... Are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3CI intend to lend my\x01",
            "assistance fully until\x01",
            "the very end.\x02\x03",
            "Save your energy and\x01",
            "gather your comrades. I\x01",
            "will do what I can.\x02\x03",
            "#01203FWell, just consider this\x01",
            "my final service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PThank you, Zeit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#5PYeah. This is seriously\x01",
            "a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PEven so, I think it's\x01",
            "going to be quite a hard\x01",
            "fight for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5PNevertheless, not only is\x01",
            "the Chairman is at Michelam,\x01",
            "but Elie is there too.\x02\x03",
            "#00007FLet's be sure we're fully\x01",
            "ready... And do whatever it\x01",
            "takes to rescue them!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7497():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7497)
    Sleep(50)

    def lambda_74A7():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_74A7)
    Sleep(50)

    def lambda_74B7():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_74B7)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x103,
        "#00201F#5P...Sir!\x02",
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
            "Noｱl has joined the\x01",
            "party.\x07\x00\x02",
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
            "Armed Force\x07\x05",
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
            " as\x01",
            "S-Break?",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_764C")
    SetChrChipPat(0x8, 0x6, 0x141)

    label("loc_764C")

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

    # Function_20_67EC end

    def Function_21_76AE(): pass

    label("Function_21_76AE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F(...Once we land here,\x01",
            "we'll immediately engage\x01",
            "Red Constellation.)\x02\x03",
            "#00013F(We won't be able to\x01",
            "resupply... Are we fully\x01",
            "ready?)\x02",
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
            "[We Have Other Things to Do]\x01",      # 0
            "[Land at Michelam]\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_77A7"),
        (1, "loc_77B5"),
        (SWITCH_DEFAULT, "loc_7901"),
    )


    label("loc_77A7")

    FadeToBright(0, 0)
    Jump("loc_7901")

    label("loc_77B5")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77F8")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_78E8")

    label("loc_77F8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_781B")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_78E8")

    label("loc_781B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_783E")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_78E8")

    label("loc_783E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7861")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_78E8")

    label("loc_7861")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7884")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_78E8")

    label("loc_7884")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78A7")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_78E8")

    label("loc_78A7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78CA")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_78E8")

    label("loc_78CA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78E8")
    SetScenarioFlags(0x3C, 7)

    label("loc_78E8")

    PartySelect(2)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1310", 0, 0, 0)
    IdleLoop()
    Jump("loc_7901")

    label("loc_7901")

    Return()

    # Function_21_76AE end

    def Function_22_7902(): pass

    label("Function_22_7902")

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
            "#02101F#6P─Then, Chairman. Your\x01",
            "resolution hasn't\x01",
            "wavered at all?\x02",
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
            "Yes... Among all of you there's\x01",
            "probably some who disagree.\x02\x03",
            "However, if we don't start from\x01",
            "here, I think we won't be able to\x01",
            "move forward.\x02\x03",
            "Even if we lost temporary order and\x01",
            "hegemony.\x02",
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
        "#00108F#11PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PThe Independent State of Crossbell\x01",
            "declaration of invalidity, eh?\x02\x03",
            "#10400FIt is indeed a card that none other than\x01",
            "His Excellency the Chairman, a former\x01",
            "government representative, could play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#5PHowever, in what form\x01",
            "that announcement will\x01",
            "be made?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01908F#6PIf it's not conveyed to the citizens\x01",
            "and the State Guard in an effective\x01",
            "way, its effect will be weak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PIt seems Jona has an\x01",
            "idea regarding that.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(99360, 1250, -104040, 1000)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0xF, 0x2)
    SetChrSubChip(0x12, 0x1)
    SetChrSubChip(0x105, 0x0)

    def lambda_7F78():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7F78)
    Sleep(50)

    def lambda_7F88():
        TurnDirection(0x106, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_7F88)
    Sleep(50)

    def lambda_7F98():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7F98)
    Sleep(50)

    def lambda_7FA8():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7FA8)
    Sleep(50)

    def lambda_7FB8():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7FB8)
    Sleep(50)

    def lambda_7FC8():
        TurnDirection(0x13, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7FC8)
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
            "Yeah. There's an experimental\x01",
            "signal booster used to connect the\x01",
            "orbal net to Lｳman on Tangram\x02\x03",
            "Hill.\x02\x03",
            "If I can get an opening there, I\x01",
            "should be able to hack it.\x02\x03",
            "If it's only for about ten\x01",
            "minutes, I should be able to make\x01",
            "it last somehow.\x02",
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
            "Basically, you want to take over\x01",
            "those monitors on the streets?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PYes, and I can also\x01",
            "access all the terminals\x01",
            "in the State Guard areas.\x02\x03",
            "#00202FI think it will also\x01",
            "fulfill Commander Sonya's\x01",
            "terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#6PIf the validity of the President's\x01",
            "side sways, the State Guard will\x01",
            "watch the situation for a while...\x02\x03",
            "#12102FMoving around would become easier\x01",
            "for sure.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#11P...............\x02",
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

    def lambda_8357():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8357)
    Sleep(50)

    def lambda_8367():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_8367)
    Sleep(50)

    def lambda_8377():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8377)
    Sleep(50)

    def lambda_8387():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8387)
    Sleep(50)

    def lambda_8397():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8397)
    Sleep(50)

    def lambda_83A7():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_83A7)
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
            "#02503F#5PHmm, Lloyd.\x02\x03",
            "#02500FIn the end, the "independent\x01",
            "state" declaration of invalidity\x01",
            "is nothing more than my own idea.\x02\x03",
            "We don't have to put it in effect\x01",
            "if you, the leader, are against\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00000F#11P─No, please go ahead.\x02\x03",
            "#00003FOnce, Mr. Dieter... He\x01",
            "spoke about "justice",\x01",
            "when he was IBC President.\x02",
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
            "In the end, people are\x01",
            "creatures that seek\x01",
            "justice.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because the thing called\x01",
            "Justice is the foundation\x01",
            "of a reliable society.\x07\x00\x02",
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
            "Political corruption,\x01",
            "mafia problems...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Even if the police don't control those\x01",
            "problems, many people won't struggle throughout\x01",
            "their lives because of economic prosperity.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "However, even in this situation,\x01",
            "as you'd expect, people must\x01",
            "seek Justice somewhere.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because no matter what shape it takes,\x01",
            "people desire a sense of security. To those\x01",
            "people, that's a safe and reliable society.\x07\x00\x02",
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
            "That's exactly why I─\x01",
            "Why I want to expect\x01",
            "great things from you.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You guys, in your own\x01",
            "way, appear to be\x01",
            "pursuing Justice...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I think it's important to\x01",
            "demonstrate that to the citizens\x01",
            "in a form they can see.\x07\x00\x02",
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
        (
            "#02505F#5PDieter said those\x01",
            "things...\x02",
        )
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
            "#00208F#11PNot even a year has\x01",
            "passed, and yet I feel\x01",
            "very nostalgic about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P─The President's words back\x01",
            "then.\x02\x03",
            "#00008FI honestly don't know if those\x01",
            "came from his true feelings or\x01",
            "if he was just posing, but...\x02\x03",
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
        (
            "#02103F#6PHmm, they really are\x01",
            "very interesting words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYes, that's why... I want to\x01",
            "trust his words once more.\x02\x03",
            "#00003FFor our sake, and his too.\x02\x03",
            "#00001FAnd more importantly, to give\x01",
            "the the citizens and the State\x01",
            "Guard both a chance to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503F#5P─I understand.\x02\x03",
            "#02500FI'll simplify those words\x01",
            "in my own style and reflect\x01",
            "them in the declaration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#11PYes, please do.\x02",
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
            "#02104F#6PThen let's hammer out\x01",
            "the plan's specifics!\x02\x03",
            "#02110FJona, Fran! We'll leave\x01",
            "the technical support to\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01909F#5PRight!\x02",
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
            "Thus, the specifics of a plan for the\x01",
            ""Independent State of Crossbell" declaration of\x01",
            "invalidity by Chairman MacDowell were decided.\x02\x03",
            "A practical forecast to wage the hacking of the\x01",
            "orbal net was conducted by Jona and Fran...\x02\x03",
            "What remained was only to pick the right time.\x07\x00\x02",
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

    # Function_22_7902 end

    def Function_23_8E4C(): pass

    label("Function_23_8E4C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F(The experimental signal booster...\x01",
            "We'll hack the orbal net and deliver the\x01",
            "declaration of invalidity from there.)\x02\x03",
            "#00001FThere's no going back. Are we ready for\x01",
            "this?\x02",
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
            "[We Have Other Things to Do]\x01",      # 0
            "[Head to the Booster Site]\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8F75"),
        (1, "loc_8F83"),
        (SWITCH_DEFAULT, "loc_9187"),
    )


    label("loc_8F75")

    FadeToBright(0, 0)
    Jump("loc_9187")

    label("loc_8F83")

    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_9044")
    FadeToBright(1000, 0)
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)

    def lambda_8FD1():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8FD1)
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

    label("loc_9044")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9084")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_9174")

    label("loc_9084")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90A7")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_9174")

    label("loc_90A7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90CA")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_9174")

    label("loc_90CA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90ED")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_9174")

    label("loc_90ED")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9110")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_9174")

    label("loc_9110")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9133")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_9174")

    label("loc_9133")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9156")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_9174")

    label("loc_9156")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9174")
    SetScenarioFlags(0x3C, 7)

    label("loc_9174")

    PartySelect(2)
    SetScenarioFlags(0x23, 0)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Jump("loc_9187")

    label("loc_9187")

    Return()

    # Function_23_8E4C end

    def Function_24_9188(): pass

    label("Function_24_9188")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05802.itc", 0x1E)
    LoadChrToIndex("apl/ch51770.itc", 0x1F)
    SoundLoad(952)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_91B6")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_91B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_91C9")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_91C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_91DC")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_91DC")

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
            "#01901F#5P─The camera preparations\x01",
            "are ok! The sound test\x01",
            "is perfect too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PWe have arrived directly\x01",
            "above the booster.\x02\x03",
            "You can begin anytime\x01",
            "you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02109F#11POkay, okay.\x02\x03",
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
            "#02304F#11PHehe, let's begin then.\x02\x03",
            "#02301F─Begin hacking the orbal\x01",
            "net from the signal\x01",
            "booster.\x02",
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

    # Function_24_9188 end

    def Function_25_9584(): pass

    label("Function_25_9584")

    Sound(938, 0, 60, 0)
    Sound(836, 0, 60, 0)
    Sleep(800)
    Sound(836, 0, 60, 0)
    Return()

    # Function_25_9584 end

    def Function_26_959A(): pass

    label("Function_26_959A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_95B2")
    OP_A1(0xFE, 0x7D0, 0x2, 0x0, 0x1)
    Jump("Function_26_959A")

    label("loc_95B2")

    Return()

    # Function_26_959A end

    def Function_27_95B3(): pass

    label("Function_27_95B3")

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
            "#02302F#11PAlright! I've got\x01",
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
        "#01901F#5PSwitching to camera!\x02",
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
            "─Everyone, good morning.\x02\x03",
            "Crossbell News Reporter Grace Lynn\x01",
            "here.\x02\x03",
            "I'm here to inform you that\x01",
            "Crossbell News has no relation to\x01",
            "this matter.\x02\x03",
            "This is my own arbitrary report,\x01",
            "so please understand.\x02\x03",
            "...Well then, I know this is\x01",
            "sudden, but I'd like to introduce\x01",
            "someone to you.\x02\x03",
            "His Grace Chairman Henry\x01",
            "MacDowell, representative of the\x01",
            "Autonomous State of Crossbell!\x02",
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
            "─I am speaking to both citizens of\x01",
            "Crossbell as well as all people\x01",
            "watching this transmission.\x02\x03",
            "I am Henry Macdowell, Chairman of\x01",
            "the congress of the Autonomous\x01",
            "State of Crossbell.\x02",
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

    # Function_27_95B3 end

    def Function_28_9C88(): pass

    label("Function_28_9C88")

    Sound(938, 2, 70, 0)

    label("loc_9C8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CA7")
    Sound(836, 0, 60, 0)
    Sleep(700)
    Jump("loc_9C8E")

    label("loc_9CA7")

    Return()

    # Function_28_9C88 end

    def Function_29_9CA8(): pass

    label("Function_29_9CA8")

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
            "#00005F─You figured out a way\x01",
            "to release the Barrier!?\x02",
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
            "Yes, and also a way to\x01",
            "suppress the power of\x01",
            "those three Aions.\x02\x03",
            "The key lies in those\x01",
            ""great bells".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        (
            "#00201F#12P#NGreat bells... You mean\x01",
            "those at the Tower and\x01",
            "Temple?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10401F#6PAre you saying that\x01",
            "they're strengthening the\x01",
            "barrier and those dolls?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 70, -1, -1)
    SetChrName("Meister Jｶrg")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. After all, the Sept-Terrion is what's\x01",
            "strengthening them.\x02\x03",
            "However, as it is now, the Sept-Terrion\x01",
            "is probably imperfect.\x02\x03",
            "In order to manifest that unconventional\x01",
            ""miracle" across a vast area, it seems\x01",
            "that they rely on particular "locations".\x02\x03",
            "Those "locations" are where "resonance"\x01",
            "is born from the great bells.\x07\x00\x02",
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
        (
            "#10708F#12PThose great bells have\x01",
            "that kind of ability...?\x02",
        )
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
            "Yes, you may be able to release\x01",
            "that gigantic barrier...\x02\x03",
            "It may also be possible to suppress\x01",
            "the power of the white Aion that\x01",
            "annihilated Garrelia Fortress.\x02\x03",
            "Well, I can't say for certain,\x01",
            "though.\x07\x00\x02",
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
            "#00305F#12PWell, isn't it worth a\x01",
            "try...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PYes... That barrier and the\x01",
            "white doll are our biggest\x01",
            "obstacles.\x02\x03",
            "Until those two have been dealt\x01",
            "with, freeing Crossbell City\x01",
            "will be an impossible task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PSo that means... We're\x01",
            "going to the Tower and\x01",
            "Temple?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah, the great bell that was taken to the\x01",
            "Ancient Battlefield seems to have been\x01",
            "returned to Central Square in the city.\x02\x03",
            "#00000FWe can't do anything about that, but if\x01",
            "it's the bells located at the Tower and\x01",
            "the Temple, we can stop their resonance!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 70, -1, -1)
    SetChrName("Meister Jｶrg")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, both are places\x01",
            "that the Society is\x01",
            "guarding.\x07\x00\x02",
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
        "#00013F#12PBy the way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P#N...That seems to be the\x01",
            "case.\x02",
        )
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
            "Campanella is stationed\x01",
            "at the Temple of Moon.\x02\x03",
            "And as for the Tower of\x01",
            "Stargaze... Arianrhod\x01",
            "should be on guard there.\x07\x00\x02",
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
        (
            "#00301F#12PThat eccentric female\x01",
            "knight, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P...That's going to be a\x01",
            "problem.\x02\x03",
            "#10408FWe could do something about\x01",
            "the Fool, but...\x02\x03",
            "#10401FI can only say that it'll be\x01",
            "impossible to win against\x01",
            "that Steel Maiden head on.\x02",
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
            "#10406F#5PYeah. Terrifying people\x01",
            "exist within Ouroboros,\x01",
            "but...\x02\x03",
            "She and so-called masters\x01",
            "are in completely\x01",
            "separate leagues.\x02\x03",
            "#10401FHer strength is like if\x01",
            "someone decided that no\x01",
            "man could ever best her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#12PT-That much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PWazy, you hold the title\x01",
            "of Dominion in the\x01",
            "Church...\x02\x03",
            "#00101FEven so, you wouldn't be\x01",
            "able to oppose her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PYeah. Even if I used my Stigma\x01",
            "powers, I doubt it would be effective\x01",
            "against that armor of hers.\x02\x03",
            "#10408FIf there was someone who could oppose\x01",
            "her, that would be the Grand Master,\x01",
            "I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PHowever, this situation\x01",
            "affect the whole of\x01",
            "Zemuria.\x02\x03",
            "As you might expect,\x01",
            "there's no way Grand Master\x01",
            "Selnate can assist us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P*sigh*, that's right.\x02\x03",
            "#10408F...If Kevin were here,\x01",
            "we could at least manage\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#11P─We don't have time to worry.\x02\x03",
            "#00001FWe've finally seen a glimmer\x01",
            "of hope of breaking through\x01",
            "this deadlock of a situation.\x02\x03",
            "For now, our only choice is\x01",
            "to try charging in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F#12PYou got that right.\x02",
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
            "#10701F#12PNo matter how strong someone\x01",
            "is... I think there's always\x01",
            "a way to defeat them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400F#5PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PRight... If we falter\x01",
            "here, we won't reach\x01",
            "Bell and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#12PLet's go! To the Tower\x01",
            "and Temple!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, 70, -1, -1)
    SetChrName("Meister Jｶrg")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, I wish you all the\x01",
            "best.\x02\x03",
            "You should at least\x01",
            "leave the Tower, where\x01",
            "Arianrhod is, for last.\x02\x03",
            "That is, if you don't\x01",
            "want to be bested by her\x01",
            "valkyries.\x07\x00\x02",
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
            "You can now go to the Temple\x01",
            "of Moon from the tunnel road\x01",
            "fork on Mainz Mountain Path.\x07\x00\x02",
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

    # Function_29_9CA8 end

    def Function_30_B021(): pass

    label("Function_30_B021")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    PartySelect(2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B048")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_B048")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B05B")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_B05B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B06E")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_B06E")

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
        "#00105F#12PA-Amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PSo the helpers that spiky\x01",
            "headed Priest was talkin' about\x01",
            "were Estelle and the others!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5PYeah, it seems he took\x01",
            "them along from Liberl\x01",
            "at their strong request.\x02\x03",
            "#10402F─More importantly,\x01",
            "that's our chance.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12107F#5PYes, I'll descend to the\x01",
            "south exit while releasing\x01",
            "the optical camouflage!\x02\x03",
            "Descend from the bilge\x01",
            "hatch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12PGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P#NPlease go ahead.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_B3D3():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_B3D3)
    Sleep(50)

    def lambda_B3E3():
        TurnDirection(0xF, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_B3E3)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0xF, 0)
    Sleep(150)

    ChrTalk(
        0x12,
        (
            "#02507F#6P#N─May the Goddess protect\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xC, 0x2)
    Sleep(50)

    ChrTalk(
        0xC,
        (
            "#01901F#5PEveryone, please be\x01",
            "careful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02110F#6P#NI'll cover this from the\x01",
            "skies!\x02",
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
            "#02302F#5PWell, I'll back you up\x01",
            "from the orbal net too.\x02",
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

    # Function_30_B021 end

    def Function_31_B507(): pass

    label("Function_31_B507")

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
        "#5P─Surface armor at 70%!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PW-We won't last much\x01",
            "longer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#13801F#11PEnemy Aion, accelerating\x01",
            "even more!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        (
            "#04303F#11PUgh... Not good.\x02\x03",
            "#04308FIn that case... Looks\x01",
            "like that's my only\x01",
            "choice.\x02",
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
        "#11PNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#13807F#5PWait! It's too sudden!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        (
            "#04304F#11PIf I can't do my best here... I\x01",
            "won't be able to face that older\x01",
            "sister of yours who I succeeded.\x02\x03",
            "#04300FEveryone, back me up.\x02",
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
        "#11PActivating Stigma Mode!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x19,
        "#13808F#5PKevin...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        (
            "#04304F#11PDon't worry, Ries.\x02\x03",
            "#04302FAs for your job... I\x01",
            "leave capturing the\x01",
            "enemy to you!\x02",
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
        (
            "#04303F#11P#3C#40W#19A"O azure Seal of mine\x01",
            "shining from the\x01",
            "Abyss..."\x02",
        )
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
            "#04303F#11P#3C#40W#21A"Ascend to the sky and change\x01",
            "into a pillar of light\x01",
            "illuminating purgatory..."\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    BeginChrThread(0x1F, 1, 0, 37)
    PlayEffect(0x3, 0xFF, 0x1A, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x17,
        (
            "#5P─Converging the\x01",
            "Merkabah's full orbal\x01",
            "power!\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x18,
        (
            "#11PStigma pattern\x01",
            "recognised! Commencing\x01",
            "deployment!\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "#13807F#11PVariation in enemy Aion!\x01",
            "It's deploying its main\x01",
            "armament and ramming us!\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x1A,
        "Dominion Kevin",
        (
            "#04301F#11P#40W#18AIn the name of the 5th\x01",
            "Dominion, the Thousand Hand\x01",
            "Guardian, I command thee...\x02",
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
        (
            "#04307F#11P#4S#15AStigma Cannon\x01",
            "Mechidels── Activate!\x02",
        )
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

    # Function_31_B507 end

    def Function_32_BE7F(): pass

    label("Function_32_BE7F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BEAD")
    OP_7D(0xFF, 0x50, 0x50, 0x0, 0x1F4)
    Sleep(100)
    Sleep(700)
    OP_7D(0xFF, 0xC8, 0xC8, 0x0, 0x1F4)
    Sleep(600)
    Sleep(100)
    Jump("Function_32_BE7F")

    label("loc_BEAD")

    Return()

    # Function_32_BE7F end

    def Function_33_BEAE(): pass

    label("Function_33_BEAE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BED0")
    Sleep(100)
    Sound(840, 0, 70, 0)
    Sleep(700)
    Sleep(600)
    Sleep(100)
    Jump("Function_33_BEAE")

    label("loc_BED0")

    Return()

    # Function_33_BEAE end

    def Function_34_BED1(): pass

    label("Function_34_BED1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BEF5")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_34_BED1")

    label("loc_BEF5")

    Return()

    # Function_34_BED1 end

    def Function_35_BEF6(): pass

    label("Function_35_BEF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF0D")
    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("Function_35_BEF6")

    label("loc_BF0D")

    Return()

    # Function_35_BEF6 end

    def Function_36_BF0E(): pass

    label("Function_36_BF0E")

    Sound(934, 0, 50, 0)
    Sleep(1500)

    label("loc_BF17")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF30")
    Sound(934, 0, 30, 0)
    Sleep(1500)
    Jump("loc_BF17")

    label("loc_BF30")

    Return()

    # Function_36_BF0E end

    def Function_37_BF31(): pass

    label("Function_37_BF31")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF4A")
    Sound(929, 0, 50, 0)
    Sleep(2200)
    Jump("Function_37_BF31")

    label("loc_BF4A")

    Return()

    # Function_37_BF31 end

    def Function_38_BF4B(): pass

    label("Function_38_BF4B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF70")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_BF70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF83")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_BF83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF96")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_BF96")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BFA9")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_BFA9")

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
            "#02310F#5P─Still though, something\x01",
            "absurd has appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01908F#5PIs it really true that\x01",
            "KeA made it appear...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PYes... There seems to be\x01",
            "no doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3CThe Azure Tree─ The complete\x01",
            "form of the man-made Sept-\x01",
            "Terrion.\x02\x03",
            "#01201FTo think the deeply-rooted\x01",
            "delusions of the children of\x01",
            "man managed to create it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#5PEven you don't know what\x01",
            "kind of power that tree\x01",
            "holds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3C...Correct. I only feel something\x01",
            "uncommon from that azure light.\x02\x03",
            "#01200FIt possesses the powers of all septium\x01",
            "elements... but especially those of\x01",
            "Mirage, Time and Space, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PThe Sept-Terrion of Zero was originally\x01",
            "created by the Crois clan to reproduce\x01",
            "the Sept-Terrion of Mirage...\x02\x03",
            "#00108FThen in the process, did it also gain\x01",
            "the powers of Time and Space...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3CYes. To be honest, even\x01",
            "I can't fathom what it\x01",
            "is capable of.\x02\x03",
            "#01201F─Or rather, it could be\x01",
            "said that "there's\x01",
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
        (
            "#12100F#5PA power that rivals the\x01",
            "Goddess' own, eh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#11PIn any case... What\x01",
            "we're going to do won't\x01",
            "change.\x02\x03",
            "#00008FArios, Mariabell, Lawyer\x01",
            "Ian and the others...\x02\x03",
            "#00013FWe'll see what they're\x01",
            "really up to and get KeA\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#12PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02110F#6PMaaan, how should I put\x01",
            "it... I'm seriously\x01",
            "shaking with excitement!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)

    def lambda_C6C9():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_C6C9)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0xC, 0x2)

    def lambda_C6DE():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C6DE)
    Sleep(50)

    def lambda_C6EE():
        TurnDirection(0x102, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C6EE)
    Sleep(50)

    def lambda_C6FE():
        TurnDirection(0x103, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C6FE)
    Sleep(50)

    def lambda_C70E():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C70E)
    Sleep(50)

    def lambda_C71E():
        TurnDirection(0x109, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C71E)
    Sleep(50)

    def lambda_C72E():
        TurnDirection(0x106, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_C72E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    SetChrFlags(0x13, 0x20)

    def lambda_C758():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C758)
    ClearChrFlags(0x13, 0x20)

    ChrTalk(
        0x10A,
        (
            "#00606F#11P...Grace. Why are you\x01",
            "here?\x02\x03",
            "#00601FDidn't you get off the\x01",
            "ship with Chairman\x01",
            "MacDowell?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10A, 500)

    ChrTalk(
        0xF,
        (
            "#02103F#5POh, shut up. It's my own\x01",
            "decision, alright?\x02\x03",
            "#02100FAlso, Crossbell citizens\x01",
            "will be wanting to know\x01",
            "the facts.\x02\x03",
            "#02109FLet me support you in\x01",
            "that regard, alright?㈱\x02",
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
        "#00006F#11PH-Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#11PI have a bad feeling\x01",
            "about this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PIn any event, before\x01",
            "goin' there we'd best\x01",
            "prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12PRight... We don't know\x01",
            "what's waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PBattles in the area have ceased so\x01",
            "we can descend in the Merkabah\x01",
            "wherever we want in Crossbell now.\x02\x03",
            "#10400FJust give the order when needed.\x02",
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

    # Function_38_BF4B end

    def Function_39_CB55(): pass

    label("Function_39_CB55")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F(The Azure Tree... KeA\x01",
            "and the entire truth are\x01",
            "waiting for us there...)\x02\x03",
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
            "     [Head to the Azure Tree]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CC3E"),
        (1, "loc_CC4C"),
        (SWITCH_DEFAULT, "loc_CDA6"),
    )


    label("loc_CC3E")

    FadeToBright(0, 0)
    Jump("loc_CDA6")

    label("loc_CC4C")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC9D")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_CD8D")

    label("loc_CC9D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCC0")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_CD8D")

    label("loc_CCC0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCE3")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_CD8D")

    label("loc_CCE3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD06")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_CD8D")

    label("loc_CD06")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD29")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_CD8D")

    label("loc_CD29")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD4C")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_CD8D")

    label("loc_CD4C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD6F")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_CD8D")

    label("loc_CD6F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD8D")
    SetScenarioFlags(0x3C, 7)

    label("loc_CD8D")

    PartySelect(2)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x23, 7)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Jump("loc_CDA6")

    label("loc_CDA6")

    Return()

    # Function_39_CB55 end

    def Function_40_CDA7(): pass

    label("Function_40_CDA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    SoundLoad(498)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CDCF")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_CDCF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CDE2")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_CDE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CDF5")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_CDF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE08")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_CE08")

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
            "#01901F#5P─Confirmed sighting at 5\x01",
            "o'clock!\x02\x03",
            "It's Red Constellation's\x01",
            "Beowulf!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12PSo they showed up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12P#NRed Constellation's\x01",
            "warship, huh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#12PYeah. They've been talkin' 'bout\x01",
            "buyin' a warship since back when\x01",
            "I was still there, but...\x02\x03",
            "#00311FI don't believe it! They got\x01",
            "their hands on one already!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PThe Crois clan may have\x01",
            "provided them with the funds\x01",
            "for the current plan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11PIt appears they're also\x01",
            "using some of the\x01",
            "Society's technologies...\x02\x03",
            "#10408FAbbas, can you shake it\x01",
            "off?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12100F#5PI'll do what I can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02302F#5PWell, it's not only huge\x01",
            "but rugged too. We won't\x01",
            "lose to it in speed, right?\x02",
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

    # Function_40_CDA7 end

    def Function_41_D2F8(): pass

    label("Function_41_D2F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D31C")
    OP_82(0x2, 0x2, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_41_D2F8")

    label("loc_D31C")

    Return()

    # Function_41_D2F8 end

    def Function_42_D31D(): pass

    label("Function_42_D31D")

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
            "#10110F#12P#NNo way... They scattered\x01",
            "electromagnetic mines in\x01",
            "the sky!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#12P#N...No doubt! Those are\x01",
            "in use at the foundation\x01",
            "as well!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x1, 0x1, 0x1E, 0x1, 0, 0, 0, 0, 0, 0, 80, 80, 80, 0xFF, 0, 0, 0, 0)

    def lambda_D6AF():
        OP_96(0xFE, 0x2710, 0xFFFFFD12, 0x4E20, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_D6AF)

    ChrTalk(
        0x10A,
        (
            "#00610F#12P#NThey're no strangers to\x01",
            "combat, as expected!\x02",
        )
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
            "#10410F#12PGuh... Now they've done it.\x02\x03",
            "#10407FThey've circled around to\x01",
            "the starboard bow! Abbas,\x01",
            "deploy the anti-shock field!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        (
            "#12107F#11P─Roger!\x02\x03",
            "All crew, get down and\x01",
            "brace for impact!\x02",
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

    # Function_42_D31D end

    def Function_43_D8B7(): pass

    label("Function_43_D8B7")

    Sound(204, 0, 100, 0)

    label("loc_D8BD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D8D6")
    Sound(203, 0, 100, 0)
    Sleep(900)
    Jump("loc_D8BD")

    label("loc_D8D6")

    Return()

    # Function_43_D8B7 end

    def Function_44_D8D7(): pass

    label("Function_44_D8D7")

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
            "#01911F#5P─I-It's all right! Minor\x01",
            "damage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10407F#11PAlright, focus the anti-shock\x01",
            "field on the nose!\x02\x03",
            "Let's head to the Huge Tree by\x01",
            "forcing our way through the\x01",
            "minefield, just like this!\x02",
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

    # Function_44_D8D7 end

    def Function_45_DD5F(): pass

    label("Function_45_DD5F")

    OP_F4(0x5)
    Return()

    # Function_45_DD5F end

    SaveToFile()

Try(main)
