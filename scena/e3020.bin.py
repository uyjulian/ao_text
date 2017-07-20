from ScenarioHelper import *

def main():
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
        "Positive knight Abbas",         # 1
        "Yona",                   # 2
        "Waji",                   # 3
        "Tio",                 # 4
        "Franc",                 # 5
        "Lisha",               # 6
        "Randy",               # 7
        "Grace",               # 8
        "Noel",                 # 9
        "Erie",                 # 10
        "McDowell",         # 11
        "God wolf Zeit",           # 12
        "Dudley investigator",         # 13
        "Adjunct Ventos",       # 14
        "Adjunctive Juno",         # 15
        "Knight Cesar",           # 16
        "Adjunct Marcus",         # 17
        "Sister · Lease",       # 18
        "Father Kevin",             # 19
        "Noel",                 # 20
        "Franc",                 # 21
        "Grace",               # 22
        " ",                      # 23
        "SE control",                 # 24
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
        "Function_9_2387",         # 09, 9
        "Function_10_36B5",        # 0A, 10
        "Function_11_36F7",        # 0B, 11
        "Function_12_3C50",        # 0C, 12
        "Function_13_3D0D",        # 0D, 13
        "Function_14_4367",        # 0E, 14
        "Function_15_4382",        # 0F, 15
        "Function_16_50D2",        # 10, 16
        "Function_17_5BB6",        # 11, 17
        "Function_18_60B6",        # 12, 18
        "Function_19_60DB",        # 13, 19
        "Function_20_61DB",        # 14, 20
        "Function_21_7076",        # 15, 21
        "Function_22_72CF",        # 16, 22
        "Function_23_858D",        # 17, 23
        "Function_24_88C2",        # 18, 24
        "Function_25_8CBC",        # 19, 25
        "Function_26_8CD2",        # 1A, 26
        "Function_27_8CEB",        # 1B, 27
        "Function_28_937E",        # 1C, 28
        "Function_29_939E",        # 1D, 29
        "Function_30_A533",        # 1E, 30
        "Function_31_A9EE",        # 1F, 31
        "Function_32_B2F2",        # 20, 32
        "Function_33_B321",        # 21, 33
        "Function_34_B344",        # 22, 34
        "Function_35_B369",        # 23, 35
        "Function_36_B381",        # 24, 36
        "Function_37_B3A4",        # 25, 37
        "Function_38_B3BE",        # 26, 38
        "Function_39_BF25",        # 27, 39
        "Function_40_C163",        # 28, 40
        "Function_41_C66B",        # 29, 41
        "Function_42_C690",        # 2A, 42
        "Function_43_CBEB",        # 2B, 43
        "Function_44_CC0B",        # 2C, 44
        "Function_45_D082",        # 2D, 45
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
            "As you can see,\x01",
            "Our \"dolls\" are undertaken by us.\x02\x03",
            "Be extra careful\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10404F#6PHuh, there you are.\x01",
            "External law#4RWay#Hunting \"─ ─ No\" Protection of a thousand#2RClouds#hand#2RThe#\".\x02\x03",
            "#10402Fnickname#4RIt's different#I just changed my mind\x01",
            "Do not become disrespectful.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(140, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Haha, of course\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#12102F#6PBut \"a thousand arms#6RRufina#From the palace\x01",
            "What is Mengaku that I received ……\x02\x03",
            "You don't need to worry about it, Graham\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(145, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thanks a lot\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("Sister · Lease")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "….\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00008F#12P(Sounds like there's a lot going on)\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(85, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Lloyd.\x01",
            "I think that it is serious but it is not possible.\x02\x03",
            "In the current situation of Crossbell\x01",
            "You can not help outside from outside.\x02\x03",
            "If you were to hold the key, until now you\x01",
            "Cross-bell culture#2RLater#The bond that you came.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00005F#12PCultivated bonds…\x02\x03",
            "#00004F─ ─ All right.\x01",
            "I will keep in mind the liver.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    OP_70(0x1, 0x20)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("Sister · Lease")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mr. Lloyd, goddess#4REidos#Protection of.\x02\x03",
            "And that about Ellie,\x01",
            "Thank you.\x07\x00\x02",
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
        "#00011F#12PWhat was that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#11PActive Camoflauge Activaed\x02\x03",
            "Of course it is not perfect,\x01",
            "If you use it will slow down\x01",
            "There are disadvantages, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11PIf you infiltrate like this\x01",
            "Immediately a high mobility type doll\x01",
            "It will appear in interception.\x02\x03",
            "#10401FEven if we meet with each other\x01",
            "Firstly you will not win\x01",
            "Have them attract themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PI see…\x01",
            "Will it sneak into that gap?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3C#12PHmm, the hand guards of the star cup,\x01",
            "Shall I give it to you?\x02",
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

    def Function_9_2387(): pass

    label("Function_9_2387")

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
            "#10406F#5P── I managed to infiltrate\x01",
            "The cross bell itself is \"treasure\"\x01",
            "It's like being integrated.\x02\x03",
            "#10401FI have to move carefully from here\x01",
            "Dolls will come flying again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PDepending on this flying boat\x01",
            "Is there a limit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3CCertainly, this is the size of this ship\x01",
            "If you go down to the ground it will be through pre-prime grass\x01",
            "It will be captured in the \"net\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PYes, even as it is, even the landing\x01",
            "It will be impossible …\x02\x03",
            "#10400FTherefore, the \"clearance\" of the power field of the seven angers\x01",
            "I'm thinking of going through discovery and discovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PA \"crack\" in the power?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CHmm, the force field of the seven ia dozen is originally,\x01",
            "It is a huge one that covers the earth itself.\x02\x03",
            "#01200FBut between big streams\x01",
            "Sometimes \"gaps\" may occur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see…\x02\x03",
            "#00000FIf such a \"gap\"\x01",
            "Is not it noticed when landing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5PEhe, that's the idea\x02\x03",
            "#10402FSo, the point where you are now,\x01",
            "It's just that place.\x02",
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
            "#00001FNakasuzu of Ursula's intermittent ……\x01",
            "Is it near the place where the eidhide beast appeared before?\x02\x03",
            "#00005FBut it's amazing you could find it\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 200, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10404FBefore the incident happens\x01",
            "I checked with Abbas.\x02\x03",
            "#10402FSo, after a little tiny work\x01",
            "You escaped the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 10, -1, -1)

    AnonymousTalk(
        0x101,
        "#00011FI-I see\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 20, -1, -1)

    AnonymousTalk(
        0x107,
        "#01203F#3CHah, very well prepared\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 200, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10404F#0CWell, now it's only here\x01",
            "We will continue to land the \"gap\"\x01",
            "I need to find and go.\x02",
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
            "#10403F#5PSo then what do we do?\x02\x03",
            "#10400FAnyway, there is a \"barrier\"\x01",
            "I can not put it in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P… … That's right.\x01",
            "Still let me let you down.\x02\x03",
            "#00008FThe situation of the crossbell even a little\x01",
            "I want to know … ….\x02\x03",
            "#00001FHow is Ursula Hospital going?\x01",
            "I feel like making it sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#5PHe, Roger\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#11P#3CWell then let us disembark\x02",
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
        "#01200F#5P#3CHmm? What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PNo, I've been thinking this but\x02\x03",
            "#00001FWhy is Zeit\x01",
            "Can you help us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PAnd about the story of the Dragon in Liberl\x02\x03",
            "#10401FYou guys saint beast goes around \"treasure\"\x01",
            "For the fate, just \"watch over\"\x01",
            "I could not intervene, did I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3CNatural#2ROnly#─ There is old \"covenant\".\x02\x03",
            "#01200FHowever, now that the \"treasure of the phantom\" was lost,\x01",
            "My original mission has already ended.\x02\x03",
            "This tied down \"contraindication#4RGoldfish#\"Was also lost,\x01",
            "It is possible to move freely to a certain extent.\x02\x03",
            "A little to the children of men\x01",
            "I will lend you the power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400F#5PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PSo even in the mafia military dog case\x01",
            "Did he help us …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CHmm. That's right\x02\x03",
            "#01200FI can not help unlimited … …\x01",
            "For a while only\x01",
            "Let me become power as it is.\x02\x03",
            "Once in a while as a \"police dog\"\x01",
            "It is also registered body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PHaha, I understand.\x01",
            "I will thank you for your help.\x02",
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
            "#10404F#5PFor a while with this Menz\x01",
            "It is likely to be moving.\x02\x03",
            "#10400F── When you want to get off the ground\x01",
            "Please speak to Abbas.\x02\x03",
            "Also inside this \"Mercapa\"\x01",
            "Several facilities are in place.\x02\x03",
            "#10404FEquipment, tools, workshop functions ----\x01",
            "Talk to the crew if necessary.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00000F#11PRight, got it\x02",
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
            "Wazy joined the party\x07\x00\x02",
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
            "Wagez S craft\x01\x07\x02",
            "\"Akashic arm\"\x07\x05",
            "I have learned.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Akashic arm\"\x07\x05",
            "Do you want to register S break?",
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
            "【Yes】\x01",      # 0
            "【No】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332D")
    SetChrChipPat(0x4, 0x6, 0x12D)

    label("loc_332D")

    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "For a while, Zeit\x01",
            "I will participate as a party member.\x02\x03",
            "Because I do not have Enigma\x01",
            "I can not customize quartz\x01",
            "You can use strong upper arts.\x02\x03",
            "However, because I do not have S craft,\x01",
            "You need to be careful.\x07\x00\x02",
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
            "In Merkava\x01",
            "One Lloyd will act,\x01",
            "Other members are waiting in the ship.\x02\x03",
            "However, in the camp menu\x01",
            "It is possible to manipulate items of all members,\x01",
            "You can also refer to the shop / workshop.\x07\x00\x02",
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

    # Function_9_2387 end

    def Function_10_36B5(): pass

    label("Function_10_36B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36F6")
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Jump("Function_10_36B5")

    label("loc_36F6")

    Return()

    # Function_10_36B5 end

    def Function_11_36F7(): pass

    label("Function_11_36F7")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A96")

    ChrTalk(
        0x8,
        "#12100F#11POk what should we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6POh, once in this place\x01",
            "I decided to get off.\x02\x03",
            "#00000FThat's right, you guys\x01",
            "It is said that there was such a background.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11PAll conflicts inside the church -\x01",
            "Archbishop Ellarda critical of the Order\x01",
            "It is to censor the eyes.\x02\x03",
            "No one knows the highest rank\x01",
            "Head of bad group#2Rhead#It is said that\x01",
            "No one thinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PThat's true\x02\x03",
            "#00005FOh, but the scriptures#4RTestament#Or a holy war,\x01",
            "A word with a bit of religion\x01",
            "I feel like I'm using it, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12105F#11POh really?\x02\x03",
            "#12100FOn the contrary it became an imprudent impression\x01",
            "I thought I could make it misleading … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, certainly\x01",
            "Because it was a team with a unique atmosphere\x01",
            "I guess it was a fake devil.\x02\x03",
            "#00000F─ ─ So,\x01",
            "Can you descend immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11PWell, the position of the \"gap\" is\x01",
            "It is accurately grasped.\x02\x03",
            "Once you're prepared, come tell me\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1A0, 1)
    Jump("loc_3B05")

    label("loc_3A96")


    ChrTalk(
        0x8,
        (
            "#12100F#11PThe position of the \"gap\" is\x01",
            "It is accurately grasped.\x02\x03",
            "I descend to Nakasu on the Ursula intertrial road\x01",
            "Once you're prepared, come tell me\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B05")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Descend in Mercava\x01",      # 0
            "quit\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B59"),
        (1, "loc_3BF7"),
        (SWITCH_DEFAULT, "loc_3C4F"),
    )


    label("loc_3B59")


    ChrTalk(
        0x8,
        (
            "#12102F#11Punderstood.\x01",
            "Once in a while, check the location.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_3BD7")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x8, 0x0)
    Call(0, 12)
    Call(0, 5)
    Call(0, 7)
    Jump("loc_3BF2")

    label("loc_3BD7")

    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x0, -1500, -1500, 6000, 45)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_3BF2")

    Jump("loc_3C4F")

    label("loc_3BF7")


    ChrTalk(
        0x8,
        (
            "#12100F#11PThen if you are ready\x01",
            "Tell a voice.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x0, -1500, -1500, 6000, 45)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_3C4F")

    label("loc_3C4F")

    Return()

    # Function_11_36F7 end

    def Function_12_3C50(): pass

    label("Function_12_3C50")

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

    # Function_12_3C50 end

    def Function_13_3D0D(): pass

    label("Function_13_3D0D")

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
            "#00203F#12P#N…… of the force field of the seventy-eight\x01",
            "Newly sensing \"gaps\" …\x02\x03",
            "#00202FPassing data through\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#01909F#5PYes, roger\x02\x03",
            "#01901F(Catapult … …)\x01",
            "I could identify the coordinates -!\x02\x03",
            "Cross Bell Northeast Area,\x01",
            "\"Almorico village\" Nearby!\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        "#00002F#12PAmazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11PHmm. This really helps\x02\x03",
            "Not to mention the plateau's sensitivity,\x01",
            "With specialized operators\x01",
            "The operational efficiency of the ship does not rise significantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909F#5PErr …\x01",
            "I am still immature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11PHuh, from now on efficiently\x01",
            "I heard you can find a place to get off.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(200)

    ChrTalk(
        0x105,
        (
            "#10400F#5POk then what should we do?\x02\x03",
            "A new place as it is#4Rpoint#Into\x01",
            "Do you want to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12POh, the state of Almorika village too\x01",
            "It is likely to be verified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#11PInstitution maximum, destination,\x01",
            "Above \"Almorika village\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#12P#NWhile maintaining alert attitude,\x01",
            "I will head to the destination.\x02",
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

    def lambda_425A():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_425A)
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
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_435D")
    FadeToDark(0, 0, -1)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4352")
    Call(0, 6)
    Jump("loc_4355")

    label("loc_4352")

    Call(0, 5)

    label("loc_4355")

    Call(0, 7)
    Jump("loc_4366")

    label("loc_435D")

    NewScene("e3020", 102, 0, 0)
    IdleLoop()

    label("loc_4366")

    Return()

    # Function_13_3D0D end

    def Function_14_4367(): pass

    label("Function_14_4367")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4381")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_14_4367")

    label("loc_4381")

    Return()

    # Function_14_4367 end

    def Function_15_4382(): pass

    label("Function_15_4382")

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
            "#00204F#12P#NNew \"crack\" detected\x02\x03",
            "#00202FMr. Fran.\x01",
            "I will send the data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909F#5PYes.\x01",
            "(Kata kata kata ……)\x02\x03",
            "#01905F── It came out!\x01",
            "Crossbell Northwest Area ……\x02\x03",
            "#01901FMainz Mountain Pass\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        (
            "#00002F#12PDirections to Mainz ……\x01",
            "Do not spread the area where you can act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11PWell, over there, this movement\x01",
            "I heard that it is noticed soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P#NSpeaking of Mainz direction ……,\x01",
            "A different force than \"Black Moon\"\x01",
            "Resistance activity#8Rresistance#You should have been doing it.\x02\x03",
            "#10701FAnything leader\x01",
            "I objected to the state of Defense Forces\x01",
            "It seems to be a former guard member.\x02",
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

    def lambda_4797():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4797)
    SetChrFlags(0x107, 0x20)

    def lambda_47A9():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_47A9)
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
        "#00011F#5PR-really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PClearly all the crew members to the defense army\x01",
            "I thought that it was … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PWell it's understandable\x02\x03",
            "It caused enormous damage to the guard\x01",
            "\"Red constellation\" waving giant\x01",
            "It's about moving around.\x02\x03",
            "That fraud#4RGinka#Those who can not bear\x01",
            "It would not be surprising if it came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01901F#5PWell then\x01",
            "Probably your sister too …!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00006F#11P……Disagreeable.\x01",
            "I am sorry, but I do not think so.\x02\x03",
            "#00008FNoel swallows everything on\x01",
            "I will preserve the current crossbell\x01",
            "I chose the road.\x02\x03",
            "#00013FThat determination\x01",
            "I think that it will not bend easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01912F#5P#30WAhah, that's true\x02\x03",
            "#01908F#30WMy sister really\x01",
            "Strong … … It's clumsy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#5PFran…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PAnyway, in any case,\x01",
            "Its resistance force#8Rresistance#It is\x01",
            "I want to keep in touch.\x02\x03",
            "#10400FIn some cases \"black moon\" together,\x01",
            "It may become power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PYes. Let's go check it out\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#5POh that's right Rixia\x02\x03",
            "#00000FBefore that I went to Ursula hospital\x01",
            "Shall we stay?\x02",
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
            "#00003F#5PMr. Ilya said to you\x01",
            "I was anxious to meet him.\x02\x03",
            "#00002FI think that there are various things … ….\x01",
            "Why do not you show me a cheerful face?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)

    ChrTalk(
        0x106,
        (
            "#10706F#12PNo, I'll refrain for now\x02\x03",
            "#10708FI am still in front of Mr. Ilya\x01",
            "I can not stand it with my chest stretched … ….\x02\x03",
            "#10710FAt least release Crossbell City\x01",
            "Until we regain the alkane shell\x01",
            "Please be patient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PIt's frustrating though … ….\x01",
            "I feel I understand your feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10709F#12PAhah, sorry\x02\x03",
            "#10702FOh, of course if you have a chance\x01",
            "I am going to Ursula Hospital\x01",
            "I do not care … …!!\x02\x03",
            "#10704FI, in front of the hospital\x01",
            "I will keep you waiting ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, got it\x02\x03",
            "#00000F(Even so, Leecha … ….\x01",
            "As expected, this is what it is supposed to be. )\x02",
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
            "Rixia joined the party\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F4F")
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1A9)
    Jump("loc_4F57")

    label("loc_4F4F")

    AddCraft(0x5, 0x195)
    AddCraft(0x0, 0x195)

    label("loc_4F57")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Lisha are Combi Craft\x01\x07\x02",
            "\"Special blade Ssangyong shoot\"\x07\x05",
            "I have learned.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By consuming CP by 100\x01",
            "A powerful combination attack can be launched.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_50C8")
    FadeToDark(0, 0, -1)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50BD")
    Call(0, 6)
    Jump("loc_50C0")

    label("loc_50BD")

    Call(0, 5)

    label("loc_50C0")

    Call(0, 7)
    Jump("loc_50D1")

    label("loc_50C8")

    NewScene("e3020", 102, 0, 0)
    IdleLoop()

    label("loc_50D1")

    Return()

    # Function_15_4382 end

    def Function_16_50D2(): pass

    label("Function_16_50D2")

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
            "#02109F#11PUwwa … ….\x01",
            "Really, wow flying boat!\x02\x03",
            "#02110FNo way, the Seven Yi Shrine\x01",
            "I did not have a ship like this!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12100F#5P…… Again\x01",
            "Even if you do not want us to say something else.\x02\x03",
            "If it is an article\x01",
            "From now on, we will protect all the churches\x01",
            "Let me prepare you for not receiving it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10409F#11PHaha, well, I made an article\x01",
            "Only in the case of Yota story\x01",
            "I do not think so.\x02\x03",
            "#10402FSuch as info about the Organization\x02",
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
            "#02104F#5PDon't worry, I will keep my promise\x02\x03",
            "#02100FThe identity of that Lisha Mao\x01",
            "Mystery devil \"Silver#2RIn#\"Even like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10706F#12P#NPlease \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#12P(Hey Lloyd..)\x02\x03",
            "#00301F(Even if you really brought me\x01",
            "Was it good? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11P(Well, for a moment,\x01",
            "I think that promises are guardians. )\x02",
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
            "#00201F#11PIn the western part of Crossbell\x01",
            "I sensed a new \"gap\".\x02",
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
            "#01908F#5P(Catapult … …)\x01",
            "Identify accurate coordinates.\x02\x03",
            "#01903FAround the half way point on the West Crossbell Highway\x02\x03",
            "#01901FTo police schools and detention centers\x01",
            "It is near the branch point.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        "#00001F#11PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PWhen I escape from the detention center,\x01",
            "To Gassia's Osan\x01",
            "Were you asked for help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11POh … … what are you saying?\x01",
            "It became power.\x02\x03",
            "#00008FWhat has become of it from that?\x01",
            "I am worried … ….\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(50)

    ChrTalk(
        0x105,
        (
            "#10406F#5PBut to the police school\x01",
            "It is not a good idea to go.\x02\x03",
            "#10401FAs you escaped\x01",
            "Security will also be strengthened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P#NIf you could say otherwise\x01",
            "Only Belgaard gate where the defense army is … …\x02\x03",
            "#10701FThat's a problem\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#02106F#11PWell, when I visit Nokonoko\x01",
            "I guarantee you will be caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01908F#5P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P……Anyways\x01",
            "Let's get off as much as you desire.\x02\x03",
            "#00001FTo what extent the Defense Forces\x01",
            "I want to check if I am wary,\x01",
            "I am also concerned about the state of wandering of the eidolon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PRoger\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PBefore the mining town\x01",
            "\"Legislation\" was established.\x02\x03",
            "Because I can get down at any time\x01",
            "Please speak out if necessary.\x02",
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
            "Randy joined the party\x07\x00\x02",
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
            "Randy's S craft\x01\x07\x02",
            "\"Berserger\"\x07\x05",
            "I have learned.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Berserger\"\x07\x05",
            "Do you want to register S break?",
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
            "【Yes】\x01",      # 0
            "【No】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B5D")
    SetChrChipPat(0x3, 0x6, 0x129)

    label("loc_5B5D")

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

    # Function_16_50D2 end

    def Function_17_5BB6(): pass

    label("Function_17_5BB6")

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
            "After that, Noel summarized the luggage\x01",
            "I went aboard Melcova with Lloyd's.\x07\x00\x02",
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

    def lambda_5D9F():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D9F)

    def lambda_5DB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DB4)
    Sleep(100)

    def lambda_5DC8():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5DC8)

    def lambda_5DDD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_5DDD)
    Sleep(500)

    def lambda_5DF1():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5DF1)

    def lambda_5E06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_5E06)
    Sleep(100)

    def lambda_5E1A():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E1A)

    def lambda_5E2F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5E2F)
    Sleep(500)

    def lambda_5E43():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E43)

    def lambda_5E58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5E58)
    Sleep(100)

    def lambda_5E6C():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E6C)

    def lambda_5E81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5E81)
    Sleep(800)

    def lambda_5E95():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5E95)

    def lambda_5EAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5EAA)
    Sleep(2000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_5ED3():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5ED3)

    def lambda_5EE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_5EE8)
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

    def lambda_5F59():

        label("loc_5F59")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5F59")

    QueueWorkItem2(0x101, 2, lambda_5F59)

    def lambda_5F6B():

        label("loc_5F6B")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5F6B")

    QueueWorkItem2(0x103, 2, lambda_5F6B)

    def lambda_5F7D():

        label("loc_5F7D")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5F7D")

    QueueWorkItem2(0x104, 2, lambda_5F7D)

    def lambda_5F8F():

        label("loc_5F8F")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5F8F")

    QueueWorkItem2(0x105, 2, lambda_5F8F)

    def lambda_5FA1():

        label("loc_5FA1")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5FA1")

    QueueWorkItem2(0x106, 2, lambda_5FA1)
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
            "And the franc that I met\x01",
            "After hugging Noel without asking questions\x01",
            "I cried … …\x02\x03",
            "Noel also aspires a sister\x01",
            "My eyes were moistened and tears floated.\x07\x00\x02",
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

    # Function_17_5BB6 end

    def Function_18_60B6(): pass

    label("Function_18_60B6")


    def lambda_60BB():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60BB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_60B6 end

    def Function_19_60DB(): pass

    label("Function_19_60DB")

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

    def lambda_6162():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_6162)
    WaitChrThread(0x1C, 2)
    Sleep(500)

    def lambda_6182():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_6182)
    WaitChrThread(0x1C, 2)
    Sleep(1500)

    def lambda_61A2():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_61A2)
    WaitChrThread(0x1C, 2)
    Sleep(500)

    def lambda_61C2():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_61C2)
    WaitChrThread(0x1C, 2)
    Return()

    # Function_19_60DB end

    def Function_20_61DB(): pass

    label("Function_20_61DB")

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
            "#00204F#11P─ ─ in the Michelin direction\x01",
            "I sensed a \"gap\".\x02\x03",
            "#00202FFran, sending telemetry\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01908F#5PSob…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PAlready……\x01",
            "When are you crying?\x02\x03",
            "#10101FEveryone is gonna laugh at you\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#11PAhah, it's fine\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10709F#12P#NHehu ……\x01",
            "Something is enviable.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(836, 0, 100, 0)

    ChrTalk(
        0xC,
        (
            "#01909F#5PEheh, excuse me\x02\x03",
            "#01900F(Catapult … …)\x01",
            "─ ─ It was able to be identified!\x02\x03",
            "#01903FMichelam recreation area,\x01",
            "Near the hotel · Delfinia ……\x02\x03",
            "#01901FThat lake bath#8RLake beach#It is around!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#12POh what a coincidence\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11PHuff, this time it's elegant\x01",
            "It's hard to say a vacation though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#02105F#5POh, could it be\x02\x03",
            "Everyone at the beach\x01",
            "Did you ever go to play?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    def lambda_66B2():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_66B2)
    Sleep(50)

    def lambda_66C2():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_66C2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00002F#11PYeah, well\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PAfter the trade conference\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02106F#5POh that's so boring\x02\x03",
            "#02101FFor such a fun event\x01",
            "Why will not you call me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PNo, we are\x01",
            "It was an invited status.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10408F#5PIf I think about it now, that invitation too\x01",
            "It seemed like something was wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#12P#NIndeed…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#11P….\x02",
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
            "#00003F#11P─ ─ Anyway,\x01",
            "The next destination was decided.\x02\x03",
            "#00008FThe \"red constellation\" unit\x01",
            "She seems to be guarding … …\x02\x03",
            "#00001FNoel, how big is it?\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PI agree……\x01",
            "I think there is a single company.\x02\x03",
            "#10113FEven if you hit this number of people\x01",
            "To be honest, you will not win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#11PGo some way.\x01",
            "You can distribute your strength … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10701F#12P#NIn that case, I can-\x02",
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
            "#01203F#11P#3CNo, this is my turn\x02\x03",
            "#01201FIf you return to the original figure, considerable strength\x01",
            "You should be attracted.\x02",
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

    def lambda_6B7F():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6B7F)
    Sleep(50)

    def lambda_6B8F():
        TurnDirection(0x104, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6B8F)
    Sleep(50)

    def lambda_6B9F():
        TurnDirection(0x109, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6B9F)
    Sleep(50)

    def lambda_6BAF():
        TurnDirection(0x106, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6BAF)
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
        "#00205F#5PZeit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5PUh, is that ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3CI am the last one\x01",
            "I will devote myself to helping.\x02\x03",
            "Oil is gathering fellows,\x01",
            "Now that we are accumulating power,\x01",
            "It will not be necessary to help you soon.\x02\x03",
            "#01203FWell, even with the last big service\x01",
            "You should think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PThank you, Zeit\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#5PYeah, it really saves us\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PAlthough it is said, in a fairly severe battle\x01",
            "It seems no mistake to become it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5PStill Michelam\x01",
            "Not only the chairperson but also Ellie.\x02\x03",
            "#00007FPrepare thorough preparation ……\x01",
            "Let's free two people!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E19():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6E19)
    Sleep(50)

    def lambda_6E29():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6E29)
    Sleep(50)

    def lambda_6E39():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6E39)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x103,
        "#00201F#5PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#11PGot it!\x02",
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
            "Zeit left the party\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noel joined the party\x07\x00\x02",
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
            "Noel is S craft\x01\x07\x02",
            "\"Armed Force\"\x07\x05",
            "I have learned.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Armed Force\"\x07\x05",
            "Do you want to register S break?",
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
            "【Yes】\x01",      # 0
            "【No】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7014")
    SetChrChipPat(0x8, 0x6, 0x141)

    label("loc_7014")

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

    # Function_20_61DB end

    def Function_21_7076(): pass

    label("Function_21_7076")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F(… if you descended here\x01",
            "Soon with the \"red constellation\" unit\x01",
            "It will be a battle. )\x02\x03",
            "#00013F(I can not supply it ……\x01",
            "Are you ready for everything? )\x02",
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
            "【There are still other things to do】\x01",        # 0
            "【Descend to Michelin】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7174"),
        (1, "loc_7182"),
        (SWITCH_DEFAULT, "loc_72CE"),
    )


    label("loc_7174")

    FadeToBright(0, 0)
    Jump("loc_72CE")

    label("loc_7182")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71C5")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_72B5")

    label("loc_71C5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71E8")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_72B5")

    label("loc_71E8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_720B")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_72B5")

    label("loc_720B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_722E")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_72B5")

    label("loc_722E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7251")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_72B5")

    label("loc_7251")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7274")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_72B5")

    label("loc_7274")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7297")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_72B5")

    label("loc_7297")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B5")
    SetScenarioFlags(0x3C, 7)

    label("loc_72B5")

    PartySelect(2)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1310", 0, 0, 0)
    IdleLoop()
    Jump("loc_72CE")

    label("loc_72CE")

    Return()

    # Function_21_7076 end

    def Function_22_72CF(): pass

    label("Function_22_72CF")

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
            "#02101F#6P── Well then, Chairperson.\x01",
            "Your decision has not changed yet, is it?\x02",
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
            "Well …. Also in this\x01",
            "There will be someone against you.\x02\x03",
            "But I have to start from here\x01",
            "We do not think we can move forward.\x02\x03",
            "How tentatively#4RRice#Order and\x01",
            "Even if he lost his hegemony.\x02",
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
        "#00108F#11PRight…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PA declaration cancelling Crossbell Independence \x02\x03",
            "#10400FIndeed it is one of former government delegates\x01",
            "It is a card unique to Chairperson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#5PBut, specifically\x01",
            "How do you declare that declaration?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01908F#6PIt must be transmitted to citizens and defense forces\x01",
            "The effect is thin, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PAbout that, Jonah\x01",
            "There seems to be an idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(99360, 1250, -104040, 1000)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0xF, 0x2)
    SetChrSubChip(0x12, 0x1)
    SetChrSubChip(0x105, 0x0)

    def lambda_789F():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_789F)
    Sleep(50)

    def lambda_78AF():
        TurnDirection(0x106, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_78AF)
    Sleep(50)

    def lambda_78BF():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_78BF)
    Sleep(50)

    def lambda_78CF():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_78CF)
    Sleep(50)

    def lambda_78DF():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_78DF)
    Sleep(50)

    def lambda_78EF():
        TurnDirection(0x13, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_78EF)
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
            "Oh, on the tangram hills\x01",
            "Link the power net with the Leman Autonomous Region\x01",
            "There is a radio booster for the experiment.\x02\x03",
            "From there overcome a gap\x01",
            "You should be able to get hacked.\x02\x03",
            "About 10 minutes\x01",
            "You ought to have somehow.\x02",
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
            "#00305F#5PI do not know well …\x01",
            "The essential point is that the street screens\x01",
            "Can you take over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11PYes, that and the direction of the Defense Forces\x01",
            "You can also access all terminals.\x02\x03",
            "#00202FConditions issued by Sonja Command also\x01",
            "I wonder if it can be cleared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#6PIf the legitimacy of the president side shakes\x01",
            "Defense forces will be on standby for a while …\x02\x03",
            "#12102FIt would make it easier to move\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#11P…\x02",
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

    def lambda_7C00():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7C00)
    Sleep(50)

    def lambda_7C10():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_7C10)
    Sleep(50)

    def lambda_7C20():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7C20)
    Sleep(50)

    def lambda_7C30():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7C30)
    Sleep(50)

    def lambda_7C40():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7C40)
    Sleep(50)

    def lambda_7C50():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7C50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x13, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00108F#11PLloyd…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503F#5PHmm Lloyd\x02\x03",
            "#02500FInvalid declaration of \"Independent State\"\x01",
            "It is only my opinion to the last.\x02\x03",
            "If you are the leader you oppose\x01",
            "I do not intend to move to execution?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00000F#11PNo. Please carry on\x02\x03",
            "#00003FOnce Mr. Dieter … …\x01",
            "When he was president of IBC he\x01",
            "I was talking about \"justice\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11P…\x02",
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
            "After all, people justice justice\x01",
            "It is a living thing that you are seeking.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because \"justice\" is\x01",
            "It is because it is \"grounds\" for people to trust society.\x07\x00\x02",
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
            "The government problems… the mafia problems…\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Even if the police do not control it\x01",
            "Because it is economically blessed\x01",
            "Many citizens are not bothered by their lives.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "However, even in such circumstances\x01",
            "After all, people say \"justice\"\x01",
            "I have no choice but to ask somewhere.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Can trust society in whatever form\x01",
            "It is because I want a sense of security.\x07\x00\x02",
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
            "That's why I am\x01",
            "I would like to expect from you.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You guys, you guys\x01",
            "A figure pursuing \"justice\" … …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is visible to citizens in a visible form\x01",
            "I think that being presented is important.\x07\x00\x02",
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
        "#02505F#5PDieter said that…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11PDid he really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#11PAlthough it has not been a year yet\x01",
            "I feel very nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PThe President's words at that time\x02\x03",
            "#00008FIs that because it is true?\x01",
            "Or is it just a pose?\x01",
            "To be honest, I do not know ….\x02\x03",
            "#00001FStill in our hearts\x01",
            "It is certain that there was a reverberation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#11PRight…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#02103F#6PHmm, they are interesting words\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PWell, so … ….\x01",
            "I will redeem that word to himself\x01",
            "I want to stick it.\x02\x03",
            "#00003FFor us, and for him\x02\x03",
            "#00001FMore than anything, citizens and defense army people\x01",
            "To make you think about it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503F#5PUnderstood\x02\x03",
            "#02500FNow, I'm chewing up to myself\x01",
            "Let me reflect it in the declaration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#11PYes, please do\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#6PIt's decided then\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02104F#6PThen, concrete arrangements\x01",
            "Let's be hardened!\x02\x03",
            "#02110FJonah, Fran? Chan!\x01",
            "Technical support is good!\x02",
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
        "#02302F#11PHa. Leave it to me\x02",
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
            "Thus, by McDowell's chairman\x01",
            "\"Crossbell independent country\" invalid declaration\x01",
            "Specific arrangements have been compacted.\x02\x03",
            "By Jonah and Fran\x01",
            "Hacking on the power net\x01",
            "It has technical prospects … …\x02\x03",
            "After that all they could do was wait for the right timing\x07\x00\x02",
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

    # Function_22_72CF end

    def Function_23_858D(): pass

    label("Function_23_858D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F(Experimental radio booster ……\x01",
            "From here we hacked the power net\x01",
            "Make declaration of invalidity of \"Crossbell independent country\". )\x02\x03",
            "#00001F(I can not turn back ……\x01",
            "Are you ready for the mind? )\x02",
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
            "【There are still other things to do】\x01",          # 0
            "【Heading to Booster Point】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_86AF"),
        (1, "loc_86BD"),
        (SWITCH_DEFAULT, "loc_88C1"),
    )


    label("loc_86AF")

    FadeToBright(0, 0)
    Jump("loc_88C1")

    label("loc_86BD")

    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_877E")
    FadeToBright(1000, 0)
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)

    def lambda_870B():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_870B)
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

    label("loc_877E")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87BE")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_88AE")

    label("loc_87BE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87E1")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_88AE")

    label("loc_87E1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8804")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_88AE")

    label("loc_8804")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8827")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_88AE")

    label("loc_8827")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_884A")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_88AE")

    label("loc_884A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_886D")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_88AE")

    label("loc_886D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8890")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_88AE")

    label("loc_8890")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88AE")
    SetScenarioFlags(0x3C, 7)

    label("loc_88AE")

    PartySelect(2)
    SetScenarioFlags(0x23, 0)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Jump("loc_88C1")

    label("loc_88C1")

    Return()

    # Function_23_858D end

    def Function_24_88C2(): pass

    label("Function_24_88C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05802.itc", 0x1E)
    LoadChrToIndex("apl/ch51770.itc", 0x1F)
    SoundLoad(952)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_88F0")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_88F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8903")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_8903")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8916")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_8916")

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
            "#01901F#5P─ ─ Camera preparation is OK!\x01",
            "Voice test is also perfect!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PThis also came directly above the booster.\x02\x03",
            "You can start anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02109F#11POkay ok.\x02\x03",
            "#02100FChairperson, is it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#02501F#5POh, please begin.\x02",
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
            "#02304F#11PHey, then let's start.\x02\x03",
            "#02301FFrom the radio booster,\x01",
            "Start hacking to the power net.\x02",
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

    # Function_24_88C2 end

    def Function_25_8CBC(): pass

    label("Function_25_8CBC")

    Sound(938, 0, 60, 0)
    Sound(836, 0, 60, 0)
    Sleep(800)
    Sound(836, 0, 60, 0)
    Return()

    # Function_25_8CBC end

    def Function_26_8CD2(): pass

    label("Function_26_8CD2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8CEA")
    OP_A1(0xFE, 0x7D0, 0x2, 0x0, 0x1)
    Jump("Function_26_8CD2")

    label("loc_8CEA")

    Return()

    # Function_26_8CD2 end

    def Function_27_8CEB(): pass

    label("Function_27_8CEB")

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
            "#02302F#11P\"Alright!\x01",
            "I grabbed the communication function!\x02",
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
        "#01901F#5PCamera, I will switch!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#02110F#11PYes, you do!\x02",
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
            "── Hello, everyone.\x02\x03",
            "Cross Bell correspondence affiliation,\x01",
            "He is a Grace-Lin coverage reporter.\x02\x03",
            "As a precaution to say\x01",
            "Crossbell News Agency\x01",
            "I do not know at all.\x02\x03",
            "Because it is a report by my own dogmatism\x01",
            "Please acknowledge it.\x02\x03",
            "…… Well, immediately,\x01",
            "I would like to introduce someone.\x02\x03",
            "\"Cross Bell Autonomous Region\" representative,\x01",
            "Henry McDaill is Chairperson!\x02",
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
            "── Citizens of Crossbell,\x01",
            "And I'm watching this video\x01",
            "I will tell it to all people.\x02\x03",
            "\"Crossbell Autonomous Legislative Assembly\" Chairperson,\x01",
            "It is Henry MacDael.\x02",
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

    # Function_27_8CEB end

    def Function_28_937E(): pass

    label("Function_28_937E")

    Sound(938, 2, 70, 0)

    label("loc_9384")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_939D")
    Sound(836, 0, 60, 0)
    Sleep(700)
    Jump("loc_9384")

    label("loc_939D")

    Return()

    # Function_28_937E end

    def Function_29_939E(): pass

    label("Function_29_939E")

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
            "#00005F── of the \"barrier\"\x01",
            "I found out how to release! Is it?\x02",
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
    SetChrName("Jorgg Aged")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, that and three of them\x01",
            "God machine#4RIron#\"The way to suppress the power of.\x02\x03",
            "The key is in the Great Bell\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        (
            "#00201F#12P#N\"Great Bell\" ……\x01",
            "Did you go to the tower or the monastery?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10401F#6PThat is the barrier and the dolls\x01",
            "Is not it strengthening?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 70, -1, -1)
    SetChrName("Jorgg Aged")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, what is strengthening\x01",
            "It should be the power of \"treasure\" to the last.\x02\x03",
            "But perhaps at the moment\x01",
            "\"Treasure\" is not perfect.\x02\x03",
            "\"Miraculous\" of that common sense\x01",
            "To make it manifest over a wide range\x01",
            "It seems necessary to rely on a unique \"place\".\x02\x03",
            "By big bells\x01",
            "It is a \"place\" created by \"resonance\".\x07\x00\x02",
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
        "#10708F#12PSo the Great Bells had that function…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#12PWell then, the resonance of the bell\x01",
            "Once stopped …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, 70, -1, -1)
    SetChrName("Jorgg Aged")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, that enormous barrier\x01",
            "It may be able to be released ……\x02\x03",
            "I extinguished the Galleria Fortress\x01",
            "White \"God machine#4RIron#\"The power of\x01",
            "It will be suppressed to a certain extent.\x02\x03",
            "Well, that's just speculation\x07\x00\x02",
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
            "#00305F#12PNo, worth the try\x01",
            "I guess there are some …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PWell … with that barrier\x01",
            "The white doll was the biggest obstacle.\x02\x03",
            "As long as there are two,\x01",
            "Liberating Crossbell City\x01",
            "It was impossible forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PAnd then …\x01",
            "Are \"towers\" and \"monasteries\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11POh, the big bell carried to the battlefield\x01",
            "It seems that it was returned to the central square of the city.\x02\x03",
            "#00000FI can not afford it,\x01",
            "If the bells of \"towers\" and \"monasteries\" resonate\x01",
            "I can stop it …!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 70, -1, -1)
    SetChrName("Jorgg Aged")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, neither \"association\"\x01",
            "It is a protecting place.\x07\x00\x02",
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
        "#00013F#12POh right….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P#NThat was the case…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(110, 70, -1, -1)
    SetChrName("Jorgg Aged")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Apparently \"Mon Monarchy\" is\x01",
            "There seems to be Campanella.\x02\x03",
            "And \"Tower of Hoshi\" is …\x01",
            "It seems there is Ariane Road.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x106,
        "#10701F#12P…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PThat woman knight who defies all belief…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PThat's honestly a problem..\x02\x03",
            "#10408FIf you are a \"clown\"\x01",
            "Although it may be managed somehow ……\x02\x03",
            "#10401FThe \"Steel Saint\" is the other party,\x01",
            "It can only be said as impregnable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PIs she that strong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5POh, it's terrible for \"association\"\x01",
            "The user is stupid, but ……\x02\x03",
            "Both of these girls\x01",
            "It is an existence that draws a line.\x02\x03",
            "#10401FIt's as if you can not win with human body#22R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#\x01",
            "It has been decided#12R噵 噵 噵 噵 噵 噵#It is such strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#12PT-that much\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PWaji, even at the church\x01",
            "\"Guardian Knight#8RDominion#Called\x01",
            "It seems to be a special existence … …\x02\x03",
            "#00101FWe can't rely on her at all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5POh, even if I use the power of the \"Stigmata\"\x01",
            "I will not pass that armor.\x02\x03",
            "#10408FIf I could handle it\x01",
            "I wonder if he is the president of Uchi ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5PBut the entire continent is in this situation\x02\x03",
            "To be sure as President Sernart\x01",
            "I can not let you move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PSigh.. That's true.\x02\x03",
            "#10408F…… If Kevin is at such a time\x01",
            "I can depend on a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#11PWe don't have time to dispair\x02\x03",
            "#00001FMitsuaki who can overcome this situation\x01",
            "Finally I saw it.\x02\x03",
            "Dare to here\x01",
            "You should try stepping into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F#12PRight.\x02",
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
            "#10701F#12PNo matter what experts ……\x01",
            "One point that can break down\x01",
            "I think that it is not zero.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400F#5PHmmm\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PRight…\x01",
            "In such a place#2RStomach#If it's the case\x01",
            "It will not reach Bells.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#12Plet's go!\x01",
            "To \"Tower\" and \"Monastery\"!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, 70, -1, -1)
    SetChrName("Jorgg Aged")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well I wish you luck\x02\x03",
            "At least there is Ariane Road\x01",
            "You should postpone the tower.\x02\x03",
            "Not to mention her, even the warriors\x01",
            "I hope to have a return.\x07\x00\x02",
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
            "\"Moon's monastery\" is on the way of Mainz mountain path\x01",
            "You can go from the branch of the tunnel road.\x07\x00\x02",
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

    # Function_29_939E end

    def Function_30_A533(): pass

    label("Function_30_A533")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    PartySelect(2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A55A")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_A55A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A56D")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_A56D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A580")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_A580")

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
        "#00105F#12PA-amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PThe Father Founder Tsundzu said\x01",
            "The supporter is,\x01",
            "Were they escha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5POh, in hope of the principals\x01",
            "It seems he brought him from Libert.\x02\x03",
            "#10402FBut this is our chance\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12107F#5PWell, unlocking the optical camouflage\x01",
            "Descend to the south entrance … …!\x02\x03",
            "You can leave throught the hatch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P#NWe're counting on you\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_A8B9():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_A8B9)
    Sleep(50)

    def lambda_A8C9():
        TurnDirection(0xF, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_A8C9)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0xF, 0)
    Sleep(150)

    ChrTalk(
        0x12,
        "#02507F#6P#NGo with Aidos!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xC, 0x2)
    Sleep(50)

    ChrTalk(
        0xC,
        "#01901F#5PGuys, please be careful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02110F#6P#NI am from the sky\x01",
            "I will interview you!\x02",
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
            "#02302F#5PWell, here also from the power net\x01",
            "I'll do a backup.\x02",
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

    # Function_30_A533 end

    def Function_31_A9EE(): pass

    label("Function_31_A9EE")

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
        "#5PStructural integrity down 70!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PShe wont hold much more!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#13801F#11PLure them away! Increase speed!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Kevin Guardian",
        (
            "#04303F#11PUgh, this is bad\x02\x03",
            "#04308FWhen it comes to this……\x01",
            "Is there nothing left to do with me?\x02",
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
        "#5PFather Graham?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PNo way…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#13807F#5Pwait……!\x01",
            "It is suddenly too!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Kevin Guardian",
        (
            "#04304F#11PIf you can not step here\x01",
            "I can not face her sister who succeeded her name.\x02\x03",
            "#04300FAll of you - support me\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#5PUnderstood\x02",
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
        "#11PMode \"S#2RStigma#\"Launch ……!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x19,
        "#13808F#5PKevin…\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Kevin Guardian",
        (
            "#04304F#11PReis, don't worry\x02\x03",
            "#04302FYour job and … …\x01",
            "I will leave the enemy caught!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#13801F#5PUnderstood\x02",
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
        "Kevin Guardian",
        "#04303F#11P#3C#40W#19A\"In our abyss#2RA glitter#Deep blue#2RBlue#It's engraved … …. \"\x02",
    )

    CloseMessageWindow()
    Sound(895, 0, 100, 0)
    BeginChrThread(0x1F, 0, 0, 36)
    PlayEffect(0x0, 0xFF, 0x1A, 0x3, 0, 400, -100, 0, 0, 0, 650, 650, 650, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x1A, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    NpcTalk(
        0x1A,
        "Kevin Guardian",
        "#04303F#11P#3C#40W#21A\"Go up to heaven and purgatory#4RAwkward#Let it be a pillar of light to illuminate … …. \"\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    BeginChrThread(0x1F, 1, 0, 37)
    PlayEffect(0x3, 0xFF, 0x1A, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x17,
        "#5PMerkaba functions restored!\x05\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x18,
        (
            "#11PRecognize the \"Stigmata\" pattern!\x01",
            "Start deploying to the outside!\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "#13807F#11PEnemy Iron, variant!\x01",
            "Expanding the main gun and thrusting in!\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x1A,
        "Kevin Guardian",
        (
            "#04301F#11P#40W#18AThe guardian knight fifth place,\x01",
            "\"A thousand guards#2RClouds#hand#2RThe#\"Order … …\x02",
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
        "Kevin Guardian",
        "#04307F#11P#4S#15AActivate Stigmata!\x02",
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

    # Function_31_A9EE end

    def Function_32_B2F2(): pass

    label("Function_32_B2F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B320")
    OP_7D(0xFF, 0x50, 0x50, 0x0, 0x1F4)
    Sleep(100)
    Sleep(700)
    OP_7D(0xFF, 0xC8, 0xC8, 0x0, 0x1F4)
    Sleep(600)
    Sleep(100)
    Jump("Function_32_B2F2")

    label("loc_B320")

    Return()

    # Function_32_B2F2 end

    def Function_33_B321(): pass

    label("Function_33_B321")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B343")
    Sleep(100)
    Sound(840, 0, 70, 0)
    Sleep(700)
    Sleep(600)
    Sleep(100)
    Jump("Function_33_B321")

    label("loc_B343")

    Return()

    # Function_33_B321 end

    def Function_34_B344(): pass

    label("Function_34_B344")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B368")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_34_B344")

    label("loc_B368")

    Return()

    # Function_34_B344 end

    def Function_35_B369(): pass

    label("Function_35_B369")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B380")
    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("Function_35_B369")

    label("loc_B380")

    Return()

    # Function_35_B369 end

    def Function_36_B381(): pass

    label("Function_36_B381")

    Sound(934, 0, 50, 0)
    Sleep(1500)

    label("loc_B38A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3A3")
    Sound(934, 0, 30, 0)
    Sleep(1500)
    Jump("loc_B38A")

    label("loc_B3A3")

    Return()

    # Function_36_B381 end

    def Function_37_B3A4(): pass

    label("Function_37_B3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3BD")
    Sound(929, 0, 50, 0)
    Sleep(2200)
    Jump("Function_37_B3A4")

    label("loc_B3BD")

    Return()

    # Function_37_B3A4 end

    def Function_38_B3BE(): pass

    label("Function_38_B3BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B3E3")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_B3E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B3F6")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_B3F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B409")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_B409")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B41C")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_B41C")

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
            "#02310F#5P─ ─ Shima well Well,\x01",
            "Even tons appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01908F#5PReally, Ka'a-chan\x01",
            "Did you make it appear …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PYeah ….\x01",
            "I do not think he will make a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3C\"A big trees\" ----\x01",
            "The completed form of a treasure by a person?\x02\x03",
            "#01201FYomoyas the imagination of the sons of men\x01",
            "What is it you can do to here …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#5PThat big tree\x01",
            "What kind of power do you have?\x01",
            "You do not even know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3C…… Well.\x01",
            "Just from that blue light\x01",
            "I feel something extraordinary.\x02\x03",
            "#01200FAll of the power of Seven Ya … …\x01",
            "Especially \"vision\" \"time\" \"sky\"\x01",
            "Should we say we have to have both sides together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6POriginally \"Zero's treasure\" is\x01",
            "To reproduce the \"treasure of the phantom\"\x01",
            "Created with the hands of the Clois family …\x02\x03",
            "#00108FIn the process \"time\" and \"sky\"\x01",
            "I wonder if it is possessed together …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3CWell, honestly also to me\x01",
            "How far can you do?\x01",
            "I have no idea.\x02\x03",
            "#01201FRather than say -\x01",
            "\"There is nothing you can not do\"\x01",
            "Maybe I can say it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12POh lord\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12100F#5PPower that challenges Aidos herself\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#11PEither way …\x01",
            "What we do does not change.\x02\x03",
            "#00008FArios, Mariavel,\x01",
            "Mr. Ian's teachers ……\x02\x03",
            "#00013FWhile confirming their true intention,\x01",
            "You just get back Ka'aa with this hand.\x02",
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
        "#10107F#12PYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02110F#6PWait ~, what to say,\x01",
            "Seriously the warrior shook me!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)

    def lambda_BA9D():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_BA9D)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0xC, 0x2)

    def lambda_BAB2():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BAB2)
    Sleep(50)

    def lambda_BAC2():
        TurnDirection(0x102, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BAC2)
    Sleep(50)

    def lambda_BAD2():
        TurnDirection(0x103, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BAD2)
    Sleep(50)

    def lambda_BAE2():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BAE2)
    Sleep(50)

    def lambda_BAF2():
        TurnDirection(0x109, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BAF2)
    Sleep(50)

    def lambda_BB02():
        TurnDirection(0x106, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_BB02)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    SetChrFlags(0x13, 0x20)

    def lambda_BB2C():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_BB2C)
    ClearChrFlags(0x13, 0x20)

    ChrTalk(
        0x10A,
        (
            "#00606F#11P…… Grace.\x01",
            "Why are you here?\x02\x03",
            "#00601FWith Mr. MacDaely,\x01",
            "Did not you get off the ship?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10A, 500)

    ChrTalk(
        0xF,
        (
            "#02103F#5PIt's silly ~.\x01",
            "Is not my own way right?\x02\x03",
            "#02100FBesides, we have cross-border citizens\x01",
            "You should want to know the story this time.\x02\x03",
            "#02109FWell, that around\x01",
            "Eject the followers\x02",
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
        "#00006F#11PR-right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#11PThat makes me more worried \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PEither way, before getting on\x01",
            "It seems better to prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12PI agree……\x01",
            "What is awaiting\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PThe battle of various places was over,\x01",
            "Now anywhere on the crossbell\x01",
            "I will be able to get off at Mercava.\x02\x03",
            "#10400FIf we need to go anywhere, just ask\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#00000F#11PYeah, got it\x02",
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

    # Function_38_B3BE end

    def Function_39_BF25(): pass

    label("Function_39_BF25")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F(\"Big Big Tree\" ……\x01",
            "With Kia and over there\x01",
            "All the truth is waiting … …)\x02\x03",
            "#00013F(Are you ready……?)\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【There are still other things to do】\x01",        # 0
            "【Heading for \"Ao no Taiki\"】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BFFA"),
        (1, "loc_C008"),
        (SWITCH_DEFAULT, "loc_C162"),
    )


    label("loc_BFFA")

    FadeToBright(0, 0)
    Jump("loc_C162")

    label("loc_C008")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C059")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_C149")

    label("loc_C059")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C07C")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_C149")

    label("loc_C07C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C09F")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_C149")

    label("loc_C09F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0C2")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_C149")

    label("loc_C0C2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0E5")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_C149")

    label("loc_C0E5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C108")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_C149")

    label("loc_C108")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C12B")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_C149")

    label("loc_C12B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C149")
    SetScenarioFlags(0x3C, 7)

    label("loc_C149")

    PartySelect(2)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x23, 7)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Jump("loc_C162")

    label("loc_C162")

    Return()

    # Function_39_BF25 end

    def Function_40_C163(): pass

    label("Function_40_C163")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    SoundLoad(498)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C18B")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_C18B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C19E")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_C19E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C1B1")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_C1B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C1C4")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_C1C4")

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
            "#01901F#5PConfirmed sight of enemy ship at 5 o'clock!\x02\x03",
            "Red constellation affiliation,\x01",
            "\"Beautiful issue\"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12PIt showed up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12P#N\"Red constellation\" is in operation\x01",
            "Is it an amphibious assault ship … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#12POh, since I was around\x01",
            "Operating an amphibious assault ship\x01",
            "The story was out, but ….\x02\x03",
            "#00311FNo way, I guess so far\x01",
            "You are familiar with … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PBecause of this plan, the Clois family\x01",
            "You may have funded it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11PApparently the technology of \"association\"\x01",
            "It seems to be used … …\x02\x03",
            "#10408FAbbas, can we evade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12100F#5PWe will figure it out\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02302F#5PWell, it seems to be overkill,\x01",
            "You will not lose with speed, right?\x02",
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

    # Function_40_C163 end

    def Function_41_C66B(): pass

    label("Function_41_C66B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C68F")
    OP_82(0x2, 0x2, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_41_C66B")

    label("loc_C68F")

    Return()

    # Function_41_C66B end

    def Function_42_C690(): pass

    label("Function_42_C690")

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
        "#02311F#5PWhaaaa!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10712F#12P#NThis is!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10110F#12P#NNo way…\x01",
            "Electromagnetic lightning thrown in the air! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#12P#N……There is no mistake!\x01",
            "It is put into practical use even at the Foundation!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x1, 0x1, 0x1E, 0x1, 0, 0, 0, 0, 0, 0, 80, 80, 80, 0xFF, 0, 0, 0, 0)

    def lambda_CA0E():
        OP_96(0xFE, 0x2710, 0xFFFFFD12, 0x4E20, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CA0E)

    ChrTalk(
        0x10A,
        "#00610F#12P#NUnderhanded as we thought!\x02",
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
            "#10410F#12PUgh… that did it\x02\x03",
            "#10407FIt went around starboard starboard!\x01",
            "Abbas, against the impact field!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        (
            "#12107F#11PRoger!\x02\x03",
            "All members, crouching\x01",
            "Prepare for shock!\x02",
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

    # Function_42_C690 end

    def Function_43_CBEB(): pass

    label("Function_43_CBEB")

    Sound(204, 0, 100, 0)

    label("loc_CBF1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CC0A")
    Sound(203, 0, 100, 0)
    Sleep(900)
    Jump("loc_CBF1")

    label("loc_CC0A")

    Return()

    # Function_43_CBEB end

    def Function_44_CC0B(): pass

    label("Function_44_CC0B")

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
        "#00010F#12PCut …!\x02",
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
        "#02106F#6P#NHa ha ha! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xC,
        (
            "#01911F#5P── It's okay!\x01",
            "Damage to the ship, minor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10407F#11PAlright, in front of the nose\x01",
            "Focus on the impact field!\x02\x03",
            "While forcibly breaking through the minefield,\x01",
            "I will head to \"Taiki\" as it is!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#12107F#11P#4SI got it.\x02",
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

    # Function_44_CC0B end

    def Function_45_D082(): pass

    label("Function_45_D082")

    OP_F4(0x5)
    Return()

    # Function_45_D082 end

    SaveToFile()

Try(main)
