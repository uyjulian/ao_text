from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1010.bin",                # FileName
        "c1010",                    # MapName
        "c1010",                    # Location
        0x0013,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 19, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1010",                  # 0
        "Reception Michelle",           # 1
        "Mushroute Scott",         # 2
        "Wrestler Wenzel",     # 3
        "Zookoist Rin",             # 4
        "Friend Aolia",         # 5
        "Keya",                 # 6
        "Suzuku",                 # 7
        "Zeit",               # 8
        "Arios",               # 9
        "Kirika",                 # 10
        "chair",                   # 11
        "chair",                   # 12
        "chair",                   # 13
        "chair",                   # 14
        "chair",                   # 15
        "chair",                   # 16
        "chair",                   # 17
        "chair",                   # 18
    ))

    AddCharChip((
        "chr/ch09100.itc",                   # 00
        "chr/ch27200.itc",                   # 01
        "chr/ch27300.itc",                   # 02
        "chr/ch32000.itc",                   # 03
        "chr/ch32100.itc",                   # 04
        "chr/ch08202.itc",                   # 05
        "chr/ch08702.itc",                   # 06
        "chr/ch27202.itc",                   # 07
        "chr/ch27302.itc",                   # 08
        "chr/ch32102.itc",                   # 09
        "chr/ch02708.itc",                   # 0A
        "chr/ch08200.itc",                   # 0B
        "chr/ch08700.itc",                   # 0C
        "chr/ch02400.itc",                   # 0D
        "chr/ch07300.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(1000,    0,       12819,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294966796, 0,       43900,   0,    389,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294966796, 0,       45099,   180,  389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   13,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(114040,  0,       5860,    270,  389,  0x0, 0,   14,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(680,     0,       11370,   1700,    1000,    1500,    12820,   0x007E, 0,  3,  0x0000)
    DeclActor(5500,    0,       6000,    1200,    5500,    1500,    6000,    0x007C, 0,  14, 0x0000)
    DeclActor(8000,    0,       6000,    1200,    8000,    1500,    6000,    0x007C, 0,  15, 0x0000)
    DeclActor(5500,    0,       2500,    1200,    5500,    1500,    2500,    0x007C, 0,  15, 0x0000)
    DeclActor(8000,    0,       2500,    1200,    8000,    1500,    2500,    0x007C, 0,  15, 0x0000)

    ChipFrameInfo(1096, 0)                                       # 0

    ScpFunction((
        "Function_0_448",          # 00, 0
        "Function_1_4F8",          # 01, 1
        "Function_2_8EC",          # 02, 2
        "Function_3_98F",          # 03, 3
        "Function_4_993",          # 04, 4
        "Function_5_4645",         # 05, 5
        "Function_6_4E3E",         # 06, 6
        "Function_7_5141",         # 07, 7
        "Function_8_52B0",         # 08, 8
        "Function_9_5B31",         # 09, 9
        "Function_10_61AE",        # 0A, 10
        "Function_11_69D7",        # 0B, 11
        "Function_12_6F24",        # 0C, 12
        "Function_13_6F9D",        # 0D, 13
        "Function_14_708F",        # 0E, 14
        "Function_15_7DC4",        # 0F, 15
        "Function_16_7E97",        # 10, 16
        "Function_17_8334",        # 11, 17
        "Function_18_851E",        # 12, 18
        "Function_19_87E0",        # 13, 19
        "Function_20_87E7",        # 14, 20
        "Function_21_91E6",        # 15, 21
        "Function_22_95F9",        # 16, 22
        "Function_23_9F62",        # 17, 23
        "Function_24_A84A",        # 18, 24
        "Function_25_B4FD",        # 19, 25
        "Function_26_BA2B",        # 1A, 26
        "Function_27_BA75",        # 1B, 27
        "Function_28_D6CB",        # 1C, 28
        "Function_29_E16C",        # 1D, 29
        "Function_30_E8D6",        # 1E, 30
        "Function_31_10F5F",       # 1F, 31
        "Function_32_111D0",       # 20, 32
        "Function_33_128C4",       # 21, 33
        "Function_34_13558",       # 22, 34
        "Function_35_1403C",       # 23, 35
    ))


    def Function_0_448(): pass

    label("Function_0_448")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_480"),
        (1, "loc_48C"),
        (2, "loc_498"),
        (3, "loc_4A4"),
        (4, "loc_4B0"),
        (5, "loc_4BC"),
        (6, "loc_4C8"),
        (SWITCH_DEFAULT, "loc_4D4"),
    )


    label("loc_480")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_48C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_498")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4A4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4B0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4BC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4E0")

    label("loc_4F7")

    Return()

    # Function_0_448 end

    def Function_1_4F8(): pass

    label("Function_1_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_546")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -540, 0, 43820, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -540, 0, 45260, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_541")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x11, 0x10)

    label("loc_541")

    Jump("loc_86B")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5B9")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2760, 0, 10330, 315)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 1800, 0, 10320, 315)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -960, 0, 10340, 45)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -1960, 0, 10340, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B4")
    Event(0, 24)

    label("loc_5B4")

    Jump("loc_86B")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_64E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 2220, 0, 4610, 90)
    SetChrPos(0xA, 3840, 0, 4540, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD")
    SetChrFlags(0xB, 0x10)

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60C")
    SetChrFlags(0xA, 0x10)

    label("loc_60C")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -6000, 150, 43030, 180)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -5030, 0, 52190, 0)
    Jump("loc_86B")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_65C")
    Jump("loc_86B")

    label("loc_65C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6C7")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 2760, 0, 10330, 315)
    SetChrPos(0xC, 1800, 0, 10320, 315)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 600, 0, 39580, 90)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -1400, 0, 40910, 135)
    Jump("loc_86B")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6D5")
    Jump("loc_86B")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6E3")
    Jump("loc_86B")

    label("loc_6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F1")
    Jump("loc_86B")

    label("loc_6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6FF")
    Jump("loc_86B")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_73E")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -5030, 0, 52190, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 600, 0, 39580, 90)
    SetChrFlags(0xA, 0x10)
    Jump("loc_86B")

    label("loc_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_785")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1000, 0, 10310, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_785")
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_785")

    Jump("loc_86B")

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B1")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_7B1")

    Jump("loc_86B")

    label("loc_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_829")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -6000, 150, 43030, 180)
    SetChrPos(0x9, -6000, 150, 40820, 0)
    SetChrChipByIndex(0xA, 0x8)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0x9, 0x7)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_824")
    Event(0, 20)

    label("loc_824")

    Jump("loc_86B")

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_86B")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, -540, 0, 45260, 180)
    SetChrPos(0xC, -540, 0, 43420, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86B")
    Event(0, 20)

    label("loc_86B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_87F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 27)
    Jump("loc_8A8")

    label("loc_87F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_899")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Event(0, 29)
    Jump("loc_8A8")

    label("loc_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_8A8")
    ClearScenarioFlags(0x22, 2)
    Event(0, 31)

    label("loc_8A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B9")
    Event(0, 30)

    label("loc_8B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EB")
    SetMapFlags(0x10000000)
    Event(0, 32)

    label("loc_8EB")

    Return()

    # Function_1_4F8 end

    def Function_2_8EC(): pass

    label("Function_2_8EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_901")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)

    label("loc_901")

    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_936")
    OP_24(0x80)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_967")

    label("loc_936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_967")
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98E")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)

    label("loc_98E")

    Return()

    # Function_2_8EC end

    def Function_3_98F(): pass

    label("Function_3_98F")

    Call(0, 4)
    Return()

    # Function_3_98F end

    def Function_4_993(): pass

    label("Function_4_993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AA")
    Call(0, 25)
    Return()

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BC")
    Call(0, 28)
    Return()

    label("loc_9BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DD")
    Jump("loc_AEE")

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F0")
    Jump("loc_AEE")

    label("loc_9F0")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "#04000FOh yeah, in fact this time\x01",
            "\"Pomutto! What is a guiding game\x01",
            "It is just the beginning.\x02\x03",
            "#04011FYou guys are doing it, do not you?\x01",
            "Huh, if I can have a castor\x01",
            "Let's fight against me at the same time\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Michelle's Account\"\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 5)
    OP_E4(0x3)
    TalkEnd(0x8)
    Return()

    label("loc_AEE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D95")

    ChrTalk(
        0x8,
        "#04001Fそう……Ariosを倒したのね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F… …. Yes, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FBeing a ton as well\x01",
            "It was strength, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003F……Ariosは“理”に通じる\x01",
            "A true genuine master.\x02\x03",
            "That, too, just with talent alone\x01",
            "I can never reach …\x01",
            "It is the strength of what if there is extraordinary discipline.\x02\x03",
            "#04011FHuff, I can not get over it\x01",
            "You also became stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FHonestly, I think that there was luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt was a tough fight, but ……\x01",
            "I finally got over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FHuh, then then\x01",
            "あのKeyaってコだけね。\x02\x03",
            "#04000F待っているSuzukuちゃんのためにも、\x01",
            "Ariosと一緒に何としても\x01",
            "Please come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, sure … ….!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 6)
    Jump("loc_F2D")

    label("loc_D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E94")

    ChrTalk(
        0x8,
        (
            "#04003FAriosは“理”に通じる\x01",
            "A true genuine master.\x02\x03",
            "#04011FHuff, I can not get over it\x01",
            "You also became stronger.\x02\x03",
            "#04000F待っているSuzukuちゃんのためにも、\x01",
            "あのKeyaってコと一緒に\x01",
            "何としてもPlease come back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F2D")

    label("loc_E94")


    ChrTalk(
        0x8,
        (
            "#04004Fフフ、あとはKeyaってコを\x01",
            "Just get it back.\x02\x03",
            "#04000F待っているSuzukuちゃんのためにも、\x01",
            "Ariosと一緒に何としても\x01",
            "Please come back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2D")

    Jump("loc_4641")

    label("loc_F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_165F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1443")

    ChrTalk(
        0x8,
        (
            "#04000Fyou……\x01",
            "The president's detention, I was tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FEven the guilds,\x01",
            "Thank you for your cooperation.\x02\x03",
            "Without your cooperation,\x01",
            "I think that I could never achieve it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FUhufu, that's good.\x02\x03",
            "#04004FI wanted to manage the situation in the city\x01",
            "For me,\x01",
            "Because it was a ship over there.\x02\x03",
            "#04000FThanks guild activities as well\x01",
            "I started to be able to resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FBy the way, everyone in the guild …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYes, since the barrier was released\x01",
            "I have gotta go and go out to the city.\x02\x03",
            "#04003FBecause I could not get out of town for a while\x01",
            "It seems that problems are occurring in various places,\x01",
            "The request caught in a stroke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FThat's … it seems tough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FIf we can help\x01",
            "It was good, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FWell, leave it here.\x02\x03",
            "#04001FInstead, it appeared in wetlands\x01",
            "The unknown \"big tree\" … …\x01",
            "I will leave that up to you.\x02\x03",
            "The current role of you,\x01",
            "Is not it exactly it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, you are right.\x02\x03",
            "あそこにはKeya……\x01",
            "そしてAriosさんもいます。\x02\x03",
            "#00001FWith our hands, anything\x01",
            "I will bring you back … …!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1353")

    ChrTalk(
        0x10A,
        "#00603F…… Of course.\x02",
    )

    CloseMessageWindow()

    label("loc_1353")


    ChrTalk(
        0x8,
        (
            "#04004FUhufu, that is the only one.\x02\x03",
            "#04001F……Ariosの力は、正直言って\x01",
            "I think it can be said that you are wrong.\x02\x03",
            "It worked together.\x01",
            "I know the best of us.\x02\x03",
            "#04011FFeel free, the Special Affairs Division!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes! It is!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 5)
    Jump("loc_165A")

    label("loc_1443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1593")

    ChrTalk(
        0x8,
        (
            "#04003F……Ariosの力は、正直言って\x01",
            "I think it can be said that you are wrong.\x02\x03",
            "#04001FIt worked together.\x01",
            "I know the best of us.\x02\x03",
            "Although a tough battle is waiting for him,\x01",
            "あのKeyaってコと一緒に、\x01",
            "何としてもPlease come back.\x02\x03",
            "#04011FHuh, I handed out my resignation on my own\x01",
            "As a cross, I have to preach.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_165A")

    label("loc_1593")


    ChrTalk(
        0x8,
        (
            "#04003FAlthough a tough battle is waiting for him,\x01",
            "あのKeyaってコと一緒に、Ariosを\x01",
            "何としてもPlease come back.\x02\x03",
            "#04011FHuh, I handed out my resignation on my own\x01",
            "As a cross, I have to preach.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165A")

    Jump("loc_4641")

    label("loc_165F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1851")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D4")

    ChrTalk(
        0x8,
        (
            "#04006FSince the Declaration of Independence,\x01",
            "I could not move freely.\x02\x03",
            "No matter how much the guild is neutral,\x01",
            "Order established as an independent country\x01",
            "You can not ignore what you do.\x02\x03",
            "#04001FBut this time it is different.\x01",
            "As civilians are in danger,\x01",
            "I can not leave the guilds alone.\x02\x03",
            "#04003FRush into the Orkis Tower\x01",
            "President's arrest …\x01",
            "I will let you help me again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_184C")

    label("loc_17D4")


    ChrTalk(
        0x8,
        (
            "#04003FWhen you start a strategy,\x01",
            "Please contact me again.\x02\x03",
            "#04001FAt that time our friends\x01",
            "I will prepare thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184C")

    Jump("loc_4641")

    label("loc_1851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1958")

    ChrTalk(
        0x8,
        (
            "#04006Fフウ、まさかAriosが\x01",
            "Until you deceive your schedule\x01",
            "Mayor … … I met the president.\x02\x03",
            "I thought it was unnatural but I did not notice it,\x01",
            "It is completely my mistake.\x02\x03",
            "#04008FやっぱりSuzukuちゃんの事故の件が、\x01",
            "I wonder if it has been caught all the way ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F0")

    label("loc_1958")


    ChrTalk(
        0x8,
        (
            "#04003FAnyway … As I issued the Declaration of Independence,\x01",
            "As a neutral position as a guild\x01",
            "I have to think about the future response.\x02\x03",
            "#04008FI have to contact the headquarters … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F0")

    Jump("loc_4641")

    label("loc_19F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_END)), "loc_20A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_END)), "loc_1C7F")

    ChrTalk(
        0x8,
        (
            "#04005FOh, you guys ……\x01",
            "Ariosは見かけたかしら？\x02\x03",
            "#04006FFu, I have not come back yet …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FAriosさんなら\x01",
            "I met in the cemetery a while ago.\x02\x03",
            "What Michelle was looking for\x01",
            "I told you … …\x01",
            "Have not you gone back yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FYeah, I have not returned yet …\x01",
            "Indeed, I went to the cemetery.\x02\x03",
            "#04000F… … Well, to visit Saya's grave\x01",
            "It is not unusual to go,\x01",
            "I will come back later.\x02\x03",
            "#04011FI have tried something.\x01",
            "Because the rest is all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FIs that so?\x01",
            "Well then, I will excuse you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF7")

    label("loc_1C7F")


    ChrTalk(
        0x8,
        (
            "#04005FOh, you guys ……\x01",
            "I'd like to ask you something.\x02\x03",
            "#04001FどこかでAriosを見なかった？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005Feh……?\x01",
            "Ariosさんなら、さっき\x01",
            "I met at the cemetery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FA visit to your wife's grave\x01",
            "It seems I was doing … ….\x01",
            "what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYeah, the future response of the guild\x01",
            "To consult with the mayor,\x01",
            "I went to the Orkis Tower ….\x02\x03",
            "#04006FAriosはこの間の襲撃事件の時に\x01",
            "Please break the enigma ね.\x02\x03",
            "Something busy from that incident,\x01",
            "Because I can not prepare for a spare,\x01",
            "I'm having trouble communicating with you.\x02\x03",
            "#04008FIt will be about the end of the story soon,\x01",
            "I want you to come back to me somewhere ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHa, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FBut, indeed …\x01",
            "Ariosは墓地に行ってたのね。\x02\x03",
            "#04000FWell, to visit Saya's grave\x01",
            "It is not unusual to go,\x01",
            "I will come back later.\x02\x03",
            "#04011FIt was bad to stop it.\x01",
            "Because the rest is all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FIs that so?\x01",
            "Well then, I will excuse you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF7")

    SetScenarioFlags(0x18E, 0)
    Jump("loc_20A4")

    label("loc_1FFF")


    ChrTalk(
        0x8,
        (
            "#04008FBecause the crossbell is like this,\x01",
            "It is also in the wetland pretoromus and \"association\"\x01",
            "I can not afford to turn my hand.\x02\x03",
            "#04006FHa, after all reinforcement in the headquarters\x01",
            "I wonder if I should ask for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A4")

    Jump("loc_4641")

    label("loc_20A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2536")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238F")

    ChrTalk(
        0x8,
        (
            "#04005FOh, you guys ……\x01",
            "I'd like to ask you something.\x02\x03",
            "#04001FどこかでAriosを見なかった？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FNo, I have not seen it today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAriosさんが\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYeah, the future response of the guild\x01",
            "To consult with the mayor,\x01",
            "I'm going to the Orkis Tower ….\x02\x03",
            "#04006FAriosはこの間の襲撃事件の時に\x01",
            "Please break the enigma ね.\x02\x03",
            "Something busy from that incident,\x01",
            "Because I can not prepare for a spare,\x01",
            "I'm having trouble communicating with you.\x02\x03",
            "#04008FIt will be about the end of the story soon,\x01",
            "I want you to come back to me somewhere ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FWell, are you going away on a somewhere?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI understand,\x01",
            "Ariosさんを見かけたら\x01",
            "I will call out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FWell, that would be great if you do.\x01",
            "I'm begging for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 7)
    Jump("loc_2531")

    label("loc_238F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248C")

    ChrTalk(
        0x8,
        (
            "#04003FBecause the crossbell is like this,\x01",
            "Guilds are busy now, are not they?\x02\x03",
            "#04008FPremium grass that blooms in wetlands,\x01",
            "Also in \"cross-strait\" that intervened in the crossbell\x01",
            "I can not afford to turn my hands ……\x02\x03",
            "#04006FHa, after all reinforcement in the headquarters\x01",
            "I wonder if I should ask for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2531")

    label("loc_248C")


    ChrTalk(
        0x8,
        (
            "#04008FBecause the crossbell is like this,\x01",
            "It is also in the wetland pretoromus and \"association\"\x01",
            "I can not afford to turn my hand.\x02\x03",
            "#04006FHa, after all reinforcement in the headquarters\x01",
            "I wonder if I should ask for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2531")

    Jump("loc_4641")

    label("loc_2536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2727")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2555")
    TalkEnd(0x8)
    Call(0, 23)
    Return()

    label("loc_2555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267C")

    ChrTalk(
        0x8,
        (
            "#04001FIf this situation lasts long,\x01",
            "Guilds will have no choice but to move.\x02\x03",
            "#04003FBut it has been long since the\x01",
            "To the two major powers which will give the security maintenance capability to the spear,\x01",
            "It will give further attack materials.\x02\x03",
            "#04001FI want to make it the last resort if possible … …\x01",
            "I can not wait long if I consider the safety of civilians.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2722")

    label("loc_267C")


    ChrTalk(
        0x8,
        (
            "#04001FIf this situation lasts long,\x01",
            "Guilds will have no choice but to move.\x02\x03",
            "#04006FI want to make it the last resort if possible … …\x01",
            "I can not wait long if I consider the safety of civilians.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2722")

    Jump("loc_4641")

    label("loc_2727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_28AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2811")

    ChrTalk(
        0x8,
        (
            "#04003FWhether it is phosphorus or aeolia\x01",
            "A fierce fighter who approaches A class.\x02\x03",
            "#04008FBoth of them did not contact\x01",
            "Aligning to wetlands\x01",
            "It is stranded ……\x02\x03",
            "#04001FI do not know what it is.\x01",
            "Be wary of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28A6")

    label("loc_2811")


    ChrTalk(
        0x8,
        (
            "#04008FLynn and Eolia are not contacting\x01",
            "Aligning to wetlands\x01",
            "It is stranded ……\x02\x03",
            "#04001FI do not know what it is.\x01",
            "Be wary of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A6")

    Jump("loc_4641")

    label("loc_28AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_END)), "loc_2A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A03")

    ChrTalk(
        0x8,
        (
            "#04005FOh, you guys ……\x01",
            "Lynn and Eolia's whereabouts\x01",
            "Did you understand?\x02\x03",
            "The alert function of Enigma\x01",
            "It was a story to use it though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI need to take some procedures\x01",
            "It is likely to be managed somehow.\x02\x03",
            "As the result will be reported soon,\x01",
            "Please wait a little more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FYes, I understand.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A49")

    label("loc_2A03")


    ChrTalk(
        0x8,
        (
            "#04011FLynn and Eolia's whereabouts,\x01",
            "Find somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A49")

    Jump("loc_4641")

    label("loc_2A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2AD9")

    ChrTalk(
        0x8,
        (
            "#04003FAbout Lynn,\x01",
            "If you know something here\x01",
            "Please contact me.\x02\x03",
            "#04001FIn some cases\x01",
            "Ariosたちを呼び戻すわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4641")

    label("loc_2AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2CDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C48")

    ChrTalk(
        0x8,
        (
            "#04007FThe contact arrived just now … …\x01",
            "A train accident happened! Is it?\x02\x03",
            "#04006FNo, I was in trouble.\x01",
            "Ariosたちは今、幻獣の調査で\x01",
            "I can not come back soon ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, investigation is also important … …\x01",
            "Please leave this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FWell … … It can not be helped.\x02\x03",
            "#04000FI understood, I will leave the derailment accident.\x01",
            "Please let me know as soon as there is something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CD6")

    label("loc_2C48")


    ChrTalk(
        0x8,
        (
            "#04006FAriosたちは今、幻獣の調査で\x01",
            "I will not come back soon.\x02\x03",
            "#04000FBecause I will leave the derailment accident,\x01",
            "Please let me know as soon as there is something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD6")

    Jump("loc_4641")

    label("loc_2CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_30D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303F")

    ChrTalk(
        0x8,
        (
            "#04003FI was in a report from you\x01",
            "Flower called \"pre-prince grass\" …\x01",
            "It's not like the church's scriptures.\x02\x03",
            "#04001FJust to be sure, Scott and Lynn also\x01",
            "I had my confirmation ……\x02\x03",
            "Even near the point where the eidolon came up to now,\x01",
            "The blue flower seems to have been blooming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThe cause of the blue flower blooming itself\x01",
            "It is unknown for now but ……\x02\x03",
            "#00200FIn light of the situation,\x01",
            "There is some cause-and-effect relationship with the emergence of a phantom beast\x01",
            "It looks like you seem to be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FBy the way, the investigation situation in the guild is\x01",
            "What is it like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FOnce, it was out in yesterday\x01",
            "Of the 3 eidhards, 2 were able to get rid of it.\x02\x03",
            "#04000FToday it is getting rid of the rest of the eidolon,\x01",
            "Re-examination of the point of appearance of the eideloid until now\x01",
            "I'm trying to organize it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, suddenly again\x01",
            "It is not limited that a phantom beast does not appear.\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FYes, of course.\x02\x03",
            "#04000FSince I will contact you when I know something,\x01",
            "Please continue to investigate there as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16F, 3)
    Jump("loc_30D1")

    label("loc_303F")


    ChrTalk(
        0x8,
        (
            "#04000F今日はAriosも復帰してるし、\x01",
            "Please leave the survey here.\x02\x03",
            "#04011FSince I will contact you when I know something,\x01",
            "Please continue to investigate there as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30D1")

    Jump("loc_4641")

    label("loc_30D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_332B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32AC")

    ChrTalk(
        0x8,
        (
            "#04000FThe matter of you, \"phantom beast\"\x01",
            "I'm begging for you.\x02\x03",
            "#04006FAriosが動けない今の状況じゃ\x01",
            "Just me, I guess.\x01",
            "What is not enough to do.\x02\x03",
            "#04000FScott and somehow,\x01",
            "Please share it and hit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, please leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FSuzukuちゃんのことで\x01",
            "Ariosさんが動けないのは\x01",
            "It is unavoidable ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FI will be saved if you say so.\x02\x03",
            "#04000FYou guys are you,\x01",
            "Investigation as much as possible\x01",
            "Please go ahead.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3326")

    label("loc_32AC")


    ChrTalk(
        0x8,
        (
            "#04000FThe matter of you, \"phantom beast\"\x01",
            "I'm begging for you.\x02\x03",
            "You guys are you,\x01",
            "Investigation as much as possible\x01",
            "Please go ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3326")

    Jump("loc_4641")

    label("loc_332B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3631")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3564")

    ChrTalk(
        0x8,
        (
            "#04000F今日はAriosが本会議中の\x01",
            "It is supposed to be security.\x02\x03",
            "Even with consideration given to the leaders of each country,\x01",
            "There should be no more security system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn this case, it is a neutral position\x01",
            "The existence of a hypocrite is encouraging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes, just being strong\x01",
            "That big appointment\x01",
            "You will not be allowed to leave it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003Fとはいえ、いくらAriosでも\x01",
            "From terrorists alone\x01",
            "We can not protect the leaders.\x02\x03",
            "#04000FCooperation with police and security guards\x01",
            "It will be absolutely necessary.\x01",
            "Please support firmly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, do not miss it\x01",
            "I think I will be alert.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_362C")

    label("loc_3564")


    ChrTalk(
        0x8,
        (
            "#04005FOh yeah, remember that … …\x01",
            "I heard that Tio is coming home,\x01",
            "Eolia was very pleased.\x02\x03",
            "#04011FHuff, if I meet in the destination\x01",
            "Please give me a greeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F… Well, if you feel like it.\x02",
    )

    CloseMessageWindow()

    label("loc_362C")

    Jump("loc_4641")

    label("loc_3631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A2D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_37A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3665")
    Call(0, 13)
    Jump("loc_370F")

    label("loc_3665")


    ChrTalk(
        0x8,
        (
            "#04000F事情はAriosから聞いたわ。\x02\x03",
            "The crossbell guild is\x01",
            "I also have connections with foreign countries\x01",
            "I have all the goods of their own.\x02\x03",
            "Well, it must be okay\x01",
            "Do not worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_370F")

    Jump("loc_37A1")

    label("loc_3714")


    ChrTalk(
        0x8,
        (
            "#04000Fさっき、Ariosのほうから\x01",
            "There was contact.\x01",
            "Patient seems to have been saved.\x02\x03",
            "Huh, you too\x01",
            "Acknowledged by the Grand Duke\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A1")

    TalkEnd(0x8)
    Return()

    label("loc_37A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3996")

    ChrTalk(
        0x8,
        (
            "#04000FWell, at last\x01",
            "The trade meeting began.\x02\x03",
            "#04003FAtashi also doubted as a vigilant\x01",
            "I've cleared up the requests from various places.\x02\x03",
            "#04000FIf something happens,\x01",
            "Immediately a nearby destroyer\x01",
            "You should be able to rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100Fvery helpful.\x02\x03",
            "#00103F\"Red constellation\" and \"Black moon\"\x01",
            "Since I do not know where to go,\x01",
            "I'm not forbidden, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FYes, the opponent is the opponent,\x01",
            "Pay particular attention\x01",
            "It will be necessary.\x02\x03",
            "#04000FAnyway, as soon as I know something\x01",
            "I will contact you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3A28")

    label("loc_3996")


    ChrTalk(
        0x8,
        (
            "#04000FAtashi also doubted as a vigilant\x01",
            "I've cleared up the requests from various places.\x02\x03",
            "About red constellation and black moon\x01",
            "As soon as you know something,\x01",
            "I will contact you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A28")

    Jump("loc_4641")

    label("loc_3A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3FB1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AC4")

    ChrTalk(
        0x8,
        (
            "#04006FFuu, even so\x01",
            "He is not this grandson of Elder Black Eldon.\x02\x03",
            "#04000FWhat I say is truly terrible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAC")

    label("loc_3AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3B5B")

    ChrTalk(
        0x8,
        (
            "#04000FKeyaちゃんなら今も２階で\x01",
            "Suzukuちゃんと遊んでるわよ。\x02\x03",
            "#04011FThe trouble with the two people is fine.\x01",
            "Do not worry, I will look it up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAC")

    label("loc_3B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F07")

    ChrTalk(
        0x8,
        (
            "#04000FOh, you guys.\x01",
            "Keyaちゃんなら２階で\x01",
            "Suzukuちゃんと遊んでるわよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI'm sorry, I will take good care of you.\x01",
            "I guess the guilds are also busy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FNo, very much welcome.\x01",
            "Even for my good luck\x01",
            "It will be a good change.\x02\x03",
            "#04009FAnd when I saw that girls,\x01",
            "They seemed to have two daughters\x01",
            "Motherhood instinct is tickled ~ Ne\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x104,
        "#00306FWell, maternal instincts ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04001F…… What, are you also complaining?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FEr, uh … ….\x01",
            "そういえば、Ariosさんは？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000Fああ、Suzukuちゃんを\x01",
            "After brought from the hospital,\x01",
            "I headed for the Republic immediately.\x02\x03",
            "#04004FWhile clearing the request before the trade meeting,\x01",
            "Anxiety factor towards the Republic\x01",
            "You are being washed out as one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FHa, it is quite right …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FFor the time being guild,\x01",
            "Preparations for tomorrow seem to be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FHuh, you too\x01",
            "As much as I can today\x01",
            "Be prepared.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 5)
    Jump("loc_3FAC")

    label("loc_3F07")


    ChrTalk(
        0x8,
        (
            "#04000FKeyaちゃんなら２階で\x01",
            "Suzukuちゃんと遊んでるわよ。\x02\x03",
            "#04011FPlease leave that for those girls.\x01",
            "Ariosが共和国から戻るまで\x01",
            "I will take care of me firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FAC")

    Jump("loc_4641")

    label("loc_3FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_41E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410D")

    ChrTalk(
        0x8,
        (
            "#04000FRecently, we also requested using the power net\x01",
            "It is gradually increasing.\x02\x03",
            "On such a rainy day,\x01",
            "Especially there are many requests over the terminal.\x02\x03",
            "#04006FJust because I'm also busy\x01",
            "Work that seems to have low priority\x01",
            "You are being refused.\x02\x03",
            "#04000FSuch a request is sent to the support department\x01",
            "I think that there are times when it goes around … …\x01",
            "Please judge it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_41DB")

    label("loc_410D")


    ChrTalk(
        0x8,
        (
            "#04006FWe can only request as much as we can\x01",
            "I'd like to settle it but I am busy.\x01",
            "There is no choice but to choose.\x02\x03",
            "#04000FThe spilled request is sent to the support department\x01",
            "I think that there are times when it goes around … …\x01",
            "Please judge it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41DB")

    Jump("loc_4641")

    label("loc_41E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A8")

    ChrTalk(
        0x8,
        (
            "#04000FちなみにAriosは、\x01",
            "As soon as I return from Altair\x01",
            "I went to Remyferia.\x02\x03",
            "To the crossbell at the end of monthly trade meeting\x01",
            "Because the Grand Duke comes,\x01",
            "I heard you are helping with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAriosさんも\x01",
            "It sounds pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006Fまあ、Ariosに\x01",
            "It's not limited, but …\x02\x03",
            "#04000FAs a trade meeting is held\x01",
            "It is certain that everyone is getting busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, even the guard\x01",
            "There are also personnel changes and rehabilitation exercises\x01",
            "I think it was pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FAbout Huff and Guild\x01",
            "After all we lack human resources\x01",
            "Is it because of the urgent need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FWell, actually Esther and Joshua\x01",
            "The hole I missed was big.\x02\x03",
            "#04008FWork is on the increase,\x01",
            "いくらAriosやスコットたちが\x01",
            "Even saying it is excellent, there is a limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FCertainly … I can say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FWell, if you get busier in the future,\x01",
            "You can also turn this job\x01",
            "It could be quite possible.\x02\x03",
            "#04011Fフフ、色々とI'm begging for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, this is it.\x01",
            "Let's keep on each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 5)
    Jump("loc_4641")

    label("loc_45A8")


    ChrTalk(
        0x8,
        (
            "#04003FToward the trade meeting at the end of the month\x01",
            "I will be busy from now on.\x02\x03",
            "#04011FYou can also turn this job\x01",
            "It could be quite possible.\x01",
            "色々とI'm begging for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4641")

    TalkEnd(0x8)
    Return()

    # Function_4_993 end

    def Function_5_4645(): pass

    label("Function_5_4645")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4663")
    Call(0, 6)
    Jump("loc_471D")

    label("loc_4663")


    ChrTalk(
        0xFE,
        (
            "憧れていたKirikaさんと\x01",
            "To be able to fight with his back … …\x01",
            "It was a great experience for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will keep this crossbell still\x01",
            "In order to protect, from now on\x01",
            "I have to polish my own \"Taiho\".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_471D")

    Jump("loc_4E3A")

    label("loc_4722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_488E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4800")

    ChrTalk(
        0xFE,
        (
            "by the way,\x01",
            "Is there no one who was late for escape\x01",
            "When I was walking around the city ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow I have noticed something I knew\x01",
            "I feel like I felt.\x01",
            "That was probably ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… There should not be such a thing.\x01",
            "Sorry, forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4889")

    label("loc_4800")


    ChrTalk(
        0xFE,
        (
            "市内で、Somehow I have noticed something I knew\x01",
            "I feel like I felt.\x01",
            "That was probably ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… There should not be such a thing.\x01",
            "Sorry, forget it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4889")

    Jump("loc_4E3A")

    label("loc_488E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4934")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A9")
    Call(0, 7)
    Jump("loc_492F")

    label("loc_48A9")


    ChrTalk(
        0xFE,
        (
            "You guys ……\x01",
            "If it seems to be severe it will be a big help\x01",
            "Please do not hesitate to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As we guild,\x01",
            "As much as possible\x01",
            "Because I will do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_492F")

    Jump("loc_4E3A")

    label("loc_4934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4942")
    Jump("loc_4E3A")

    label("loc_4942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_49F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4961")
    TalkEnd(0xFE)
    Call(0, 23)
    Return()

    label("loc_4961")


    ChrTalk(
        0xFE,
        (
            "For us for a while\x01",
            "I will wait for the guild and see how things go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, the situation is never good …\x01",
            "You may as well prepare for sortie.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E3A")

    label("loc_49F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A06")
    Jump("loc_4E3A")

    label("loc_4A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4A14")
    Jump("loc_4E3A")

    label("loc_4A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4A22")
    Jump("loc_4E3A")

    label("loc_4A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A30")
    Jump("loc_4E3A")

    label("loc_4A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C05")

    ChrTalk(
        0xFE,
        (
            "Kirika先輩は、大統領のお付きとして\x01",
            "You seem to have gone to the Orkis Tower …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FBy the way, Mr. Lin also said,\x01",
            "Kirikaさんとお知り合いなんですね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, she's a user of \"Yotei flow\".\x01",
            "For me it is a senior son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A few years ago, my father passed away,\x01",
            "For a while in the Kingdom of Libert\x01",
            "I was accepting guilds … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, it is directly under the president\x01",
            "I was in an intelligence agency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, I do not see the bottom.\x01",
            "You may as well care about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 7)
    Jump("loc_4C89")

    label("loc_4C05")


    ChrTalk(
        0xFE,
        (
            "Kirika先輩は、今回の通商会議でも\x01",
            "It seems they were moving a lot … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, I do not see the bottom.\x01",
            "You may as well care about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C89")

    Jump("loc_4E3A")

    label("loc_4C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C9C")
    Jump("loc_4E3A")

    label("loc_4C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4CAA")
    Jump("loc_4E3A")

    label("loc_4CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4CB8")
    Jump("loc_4E3A")

    label("loc_4CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD7")
    TalkEnd(0xFE)
    Call(0, 21)
    Return()

    label("loc_4CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DCC")

    ChrTalk(
        0xFE,
        (
            "When I first met,\x01",
            "Just being head-poked guys\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The present ants are enough\x01",
            "I think I became one person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on without pampering\x01",
            "Because I will be tough, I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHaha … please hand softly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E3A")

    label("loc_4DCC")


    ChrTalk(
        0xFE,
        (
            "The present ants are enough\x01",
            "I think I became one person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on without pampering\x01",
            "Because I will be tough, I will do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E3A")

    TalkEnd(0xFE)
    Return()

    # Function_5_4645 end

    def Function_6_4E3E(): pass

    label("Function_6_4E3E")

    OP_4B(0x11, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        "Kirikaさん、お疲れ様でした！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Taiyoan \"Hayan#4RHinoki#A baby#4RLike this#\"… ….\x01",
            "You can see the essence of it at hand,\x01",
            "I learned very much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03404FAlthough the actual battle was long time ago\x01",
            "Surprisingly it got done somehow.\x02\x03",
            "#03400F…… Anyway, phosphorus,\x01",
            "You seem to have carried out considerable discipline.\x02\x03",
            "What was the time you got together in an interactive game eight years ago\x01",
            "I was surprised to see it as if it were mistaken.\x01",
            "Huh, I got to be relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Haha, I can not have it yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Kirikaさんやジンさんのような\x01",
            "If you bring it closer to the domain of experts\x01",
            "I'm happy, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03400FHuh, let's go forward.\x02\x03",
            "#03404FWell, another one or two years\x01",
            "To be able to win against Jin\x01",
            "I wonder if it is going to happen.\x02\x03",
            "#03402FStill weak nature for women of age\x01",
            "It seems I can not overcome it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "はは、Kirikaさんに言わせると\x01",
            "There is no shape for A gravel fighter.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0x11, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x1BB, 3)
    Return()

    # Function_6_4E3E end

    def Function_7_5141(): pass

    label("Function_7_5141")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "Honestly, being such a speech\x01",
            "I do not think the empire is silent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Be sure to take some action\x01",
            "Fetch … or,\x01",
            "It may be taking anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Contacts from Alain Doll, too,\x01",
            "Perhaps there is no difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, about that as well,\x01",
            "I can say the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The reaction of the church is also anxious … …\x01",
            "Anyway I have to take every possible measure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_7_5141 end

    def Function_8_52B0(): pass

    label("Function_8_52B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_52C1")
    Jump("loc_5B2D")

    label("loc_52C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_52CF")
    Jump("loc_5B2D")

    label("loc_52CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_54B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5425")

    ChrTalk(
        0xFE,
        (
            "From the ineffective declaration of McDowell's chairman\x01",
            "Regulation is further strengthened,\x01",
            "Transportation in ambulances was also quite restricted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The patient who can not bring him to the hospital\x01",
            "Drugs are somehow stockpiled in the city\x01",
            "Although it corresponded, … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it can be done in town and church\x01",
            "Treatment is also limited.\x01",
            "A hospital is absolutely necessary for residents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Liberation of Crossbell City ……\x01",
            "I have to make it absolutely successful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_54B2")

    label("loc_5425")


    ChrTalk(
        0xFE,
        (
            "After all, it can be done in town and church\x01",
            "Treatment is also limited.\x01",
            "A hospital is absolutely necessary for residents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Liberation of Crossbell City ……\x01",
            "I have to make it absolutely successful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54B2")

    Jump("loc_5B2D")

    label("loc_54B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55D1")

    ChrTalk(
        0xFE,
        (
            "This declaration of independence,\x01",
            "In my hometown of Remiferia\x01",
            "I wonder what measures to take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because Prince Albert is a wise person,\x01",
            "Thinking publicly about the public\x01",
            "It will be judged carefully, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While keeping in touch with Ursula hospital,\x01",
            "I have to think about how to deal with the guild.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_566B")

    label("loc_55D1")


    ChrTalk(
        0xFE,
        (
            "While keeping in touch with Ursula hospital,\x01",
            "I have to think about how to deal with the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You owe it to the lakeside,\x01",
            "Please tell me anything you are in trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_566B")

    Jump("loc_5B2D")

    label("loc_5670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_567E")
    Jump("loc_5B2D")

    label("loc_567E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_585B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_569D")
    TalkEnd(0xFE)
    Call(0, 23)
    Return()

    label("loc_569D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_579C")

    ChrTalk(
        0xFE,
        (
            "It is taken hostage by hunting corps\x01",
            "Abnormal situation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if it is not directly hurt,\x01",
            "A considerable mental load\x01",
            "It must be hanging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this condition persists,\x01",
            "Something that makes a physical disorder\x01",
            "I think it can be thoughtful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "As soon as possible I have to manage somehow ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5856")

    label("loc_579C")


    ChrTalk(
        0xFE,
        (
            "By being taken hostage by hunter corps,\x01",
            "To the people of Mainz considerable\x01",
            "There should be a mental burden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this condition persists,\x01",
            "It can be thought that the body is getting bad.\x01",
            "As soon as possible I have to manage somehow ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5856")

    Jump("loc_5B2D")

    label("loc_585B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5869")
    Jump("loc_5B2D")

    label("loc_5869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5877")
    Jump("loc_5B2D")

    label("loc_5877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5885")
    Jump("loc_5B2D")

    label("loc_5885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5893")
    Jump("loc_5B2D")

    label("loc_5893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_58A1")
    Jump("loc_5B2D")

    label("loc_58A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_58AF")
    Jump("loc_5B2D")

    label("loc_58AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_58BD")
    Jump("loc_5B2D")

    label("loc_58BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_58CB")
    Jump("loc_5B2D")

    label("loc_58CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58EA")
    TalkEnd(0xFE)
    Call(0, 21)
    Return()

    label("loc_58EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ABD")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xC,
        (
            "by the way……\x01",
            "Also for Tio\x01",
            "You have not seen me for a while, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To be sure, now to the people of Leman Autonomous Region\x01",
            "You did it, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, for a while now\x01",
            "It looks like you are over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… Ha ha, that's right.\x01",
            "Le Mans also has a guild's headquarters,\x01",
            "I also visited there for a while …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… I can not afford that,\x01",
            "I do not think Michelle will allow it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0xC, 0xB, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        "Right……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Hello … this person as usual.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_5B2D")

    label("loc_5ABD")


    ChrTalk(
        0xFE,
        (
            "Oh, Tio for the first time in a while\x01",
            "I want to hug hug … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Please tell me as soon as you come back,\x01",
            "I will fly! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B2D")

    TalkEnd(0xFE)
    Return()

    # Function_8_52B0 end

    def Function_9_5B31(): pass

    label("Function_9_5B31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_5B42")
    Jump("loc_61AA")

    label("loc_5B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5B50")
    Jump("loc_61AA")

    label("loc_5B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CA8")

    ChrTalk(
        0xFE,
        (
            "Some people who could escape\x01",
            "I quickly evacuated indoors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed until the inside of the building\x01",
            "I could not confirm it,\x01",
            "The pearl of the department store will also be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… To take such a hand,\x01",
            "I will also pretend to be president side\x01",
            "I guess it is getting ruined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, what kind of means do they have\x01",
            "It is not amusing to use it.\x01",
            "You should be careful enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5D5E")

    label("loc_5CA8")


    ChrTalk(
        0xFE,
        (
            "…… To take such a hand,\x01",
            "I will also pretend to be president side\x01",
            "I guess it is getting ruined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, what kind of means do they have\x01",
            "It is not amusing to use it.\x01",
            "You should be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D5E")

    Jump("loc_61AA")

    label("loc_5D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E6E")

    ChrTalk(
        0xFE,
        (
            "As from the same crossbell,\x01",
            "Ariosさんの気持ちは\x01",
            "I feel like understanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But to say so\x01",
            "Like a guild like this\x01",
            "I did not get out …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Even if I think about it, it can not be helped.\x01",
            "Now as a fighter, what you can do\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5EDE")

    label("loc_5E6E")


    ChrTalk(
        0xFE,
        (
            "Ariosさんの事はこの際\x01",
            "Even though I think about it, it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now as a fighter, what you can do\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EDE")

    Jump("loc_61AA")

    label("loc_5EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5EF1")
    Jump("loc_61AA")

    label("loc_5EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5F8A")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "……Is that so,\x01",
            "Almorica direction is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes … … Yes … …\x01",
            "Just to be sure, to everyone in the village\x01",
            "Please call for attention.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    Jump("loc_61AA")

    label("loc_5F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5F98")
    Jump("loc_61AA")

    label("loc_5F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5FA6")
    Jump("loc_61AA")

    label("loc_5FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5FB4")
    Jump("loc_61AA")

    label("loc_5FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5FC2")
    Jump("loc_61AA")

    label("loc_5FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5FD0")
    Jump("loc_61AA")

    label("loc_5FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5FDE")
    Jump("loc_61AA")

    label("loc_5FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5FEC")
    Jump("loc_61AA")

    label("loc_5FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_61A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_600B")
    TalkEnd(0xFE)
    Call(0, 22)
    Return()

    label("loc_600B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_609C")
    Jump("loc_60E6")

    label("loc_609C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_60BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60E6")

    label("loc_60BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60DC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60E6")

    label("loc_60DC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60E6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Compared to when I first met\x01",
            "You seem to have become quite dependable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the future you can also help each other\x01",
            "I think that it is many, and each other\x01",
            "Let 's keep going.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_61AA")

    label("loc_61A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_61AA")

    label("loc_61AA")

    TalkEnd(0xFE)
    Return()

    # Function_9_5B31 end

    def Function_10_61AE(): pass

    label("Function_10_61AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_61BF")
    Jump("loc_69D3")

    label("loc_61BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_61CD")
    Jump("loc_69D3")

    label("loc_61CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6388")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F9")

    ChrTalk(
        0xFE,
        (
            "Magical golem ……\x01",
            "It has brought out troublesome things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "During the release strategy,\x01",
            "Do not let the civilian population damage\x01",
            "Maximum consideration is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Things like that in the city\x01",
            "To wander around,\x01",
            "It can not be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the name of the guild,\x01",
            "Make sure the President's sin\x01",
            "I have to deal with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6383")

    label("loc_62F9")


    ChrTalk(
        0xFE,
        (
            "…… Things like that in the city\x01",
            "To wander around,\x01",
            "It can not be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the name of the guild,\x01",
            "Make sure the President's sin\x01",
            "I have to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6383")

    Jump("loc_69D3")

    label("loc_6388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A3")
    Call(0, 7)
    Jump("loc_645F")

    label("loc_63A3")


    ChrTalk(
        0xFE,
        (
            "Information Office Alan Dole ……\x01",
            "The name was in the Empire Guild\x01",
            "I have heard it several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are already meeting\x01",
            "I know that, but it is a nasty opponent.\x01",
            "… … Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_645F")

    Jump("loc_69D3")

    label("loc_6464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6472")
    Jump("loc_69D3")

    label("loc_6472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6628")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65AF")

    ChrTalk(
        0xFE,
        (
            "Scott confirms … …\x01",
            "In Almorika village and hospital etc\x01",
            "It seems that nothing is happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, using the topography of the mountain path\x01",
            "The hunters who have obtained the geographical advantage\x01",
            "It is difficult to retreat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this situation persists,\x01",
            "To the residents of Mainz\x01",
            "I do not know what danger is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "After all, do we have to move …?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6623")

    label("loc_65AF")


    ChrTalk(
        0xFE,
        (
            "If this situation persists,\x01",
            "To the residents of Mainz\x01",
            "I do not know what danger is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "After all, do we have to move …?\x02",
    )

    CloseMessageWindow()

    label("loc_6623")

    Jump("loc_69D3")

    label("loc_6628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6636")
    Jump("loc_69D3")

    label("loc_6636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6644")
    Jump("loc_69D3")

    label("loc_6644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6652")
    Jump("loc_69D3")

    label("loc_6652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6660")
    Jump("loc_69D3")

    label("loc_6660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_67D7")
    OP_4B(0xFE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6756")

    ChrTalk(
        0xFE,
        (
            "…… Ah … … ah ……\x01",
            "Well, after all, in the direction of the empire\x01",
            "Movement to terrorists … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Oh, of course.\x01",
            "Let's strengthen your vigilance even here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Apparently both the guild of the empire\x01",
            "It looks like I am in contact. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_67CE")

    label("loc_6756")


    ChrTalk(
        0xFE,
        (
            "Well, after all, in the direction of the empire\x01",
            "Movement to terrorists … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Oh, of course.\x01",
            "Let's strengthen your vigilance even here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67CE")

    OP_4C(0xFE, 0xFF)
    Jump("loc_69D3")

    label("loc_67D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_67E5")
    Jump("loc_69D3")

    label("loc_67E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_67F3")
    Jump("loc_69D3")

    label("loc_67F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_69CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6812")
    TalkEnd(0xFE)
    Call(0, 22)
    Return()

    label("loc_6812")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_68A3")
    Jump("loc_68ED")

    label("loc_68A3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68C3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68ED")

    label("loc_68C3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68E3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68ED")

    label("loc_68E3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68ED")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I heard about the success in Altair City.\x01",
            "You seem to have done well for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is the effort that the everyday blood bleeds out\x01",
            "It will be a signpost that leads to good results.\x01",
            "…… You should progress with this condition.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_69D3")

    label("loc_69CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_69D3")

    label("loc_69D3")

    TalkEnd(0xFE)
    Return()

    # Function_10_61AE end

    def Function_11_69D7(): pass

    label("Function_11_69D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69EC")
    Call(0, 6)
    Jump("loc_6F20")

    label("loc_69EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D6C")

    ChrTalk(
        0x11,
        (
            "#03400FYou also ….\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FKirikaさんも、\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FYeah, I was really saved!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03402FHuh, I was a little\x01",
            "I just said I did help.\x02\x03",
            "#03403FMore than that …\x01",
            "To the emergence of that \"big tree\"\x01",
            "You can not hide surprises as expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FIn the Republic\x01",
            "What kind of correspondence do you have?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03403FI can see it from Altair City\x01",
            "To the emergence of that \"big tree\"\x01",
            "It seems that he is truly surprised.\x02\x03",
            "What kind of situation will happen\x01",
            "Because I do not know, for now\x01",
            "You will have a system of waiter observation.\x02\x03",
            "#03400FTo speak more in detail\x01",
            "I can not, but I wonder why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03400FUntil I also see the end\x01",
            "I will stay here.\x02\x03",
            "#03403FHow Crossbell traces,\x01",
            "No one knows any more ……\x01",
            "Everything is hanging on you.\x02\x03",
            "#03402FNever regret it,\x01",
            "Proceed the way you believed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 7)
    Jump("loc_6F20")

    label("loc_6D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E6B")

    ChrTalk(
        0x11,
        (
            "#03400FUntil I also see the end\x01",
            "I will stay here.\x02\x03",
            "#03403FHow Crossbell traces,\x01",
            "No one knows any more ……\x01",
            "Everything is hanging on you.\x02\x03",
            "#03402FNever regret it,\x01",
            "Proceed the way you believed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6F20")

    label("loc_6E6B")


    ChrTalk(
        0x11,
        (
            "#03403FHow Crossbell traces,\x01",
            "No one knows any more ……\x01",
            "Everything is hanging on you.\x02\x03",
            "#03400FNever regret it,\x01",
            "Proceed the way you believed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F20")

    TalkEnd(0xFE)
    Return()

    # Function_11_69D7 end

    def Function_12_6F24(): pass

    label("Function_12_6F24")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F39")
    Call(0, 13)
    Jump("loc_6F99")

    label("loc_6F39")


    ChrTalk(
        0x10,
        (
            "#01400F…… You can leave this place.\x02\x03",
            "You guys in the Ursula intermission\x01",
            "I'm looking for 'Nadelia mushrooms'.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F99")

    TalkEnd(0xFE)
    Return()

    # Function_12_6F24 end

    def Function_13_6F9D(): pass

    label("Function_13_6F9D")

    OP_4B(0x10, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x10,
        (
            "#01400F… … Oh, just as I told you earlier.\x01",
            "I'm sorry but please hurry up and find it.\x02\x03",
            "Certainly, there must have been a stockpile in the back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FWell … Where was it?\x02\x03",
            "Eoria also\x01",
            "I wonder if you should try it.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_13_6F9D end

    def Function_14_708F(): pass

    label("Function_14_708F")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A shift chart of the hypocrite masters is affixed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_71C1")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：　　　 −\x01",
            "Scott: Village of Almorica\x01",
            "Wenzel: Main city Mainz\x01",
            "Rin: \"Stand by\"\x01",
            "Aeolia: Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_71C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_72A2")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：　　　 −\x01",
            "Scott: \"Waiting\"\x01",
            "Wenzel: \"Waiting\"\x01",
            "Rin: \"Stand by\"\x01",
            "Aeolia: \"Waiting\"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_72A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7383")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：　　　 −\x01",
            "Scott: \"Waiting\"\x01",
            "Wenzel: \"Waiting\"\x01",
            "Rin: \"Stand by\"\x01",
            "Aeolia: \"Waiting\"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7470")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　： オルキスタワー\x01",
            "Scott: The Belgard gate\x01",
            "Wenzel: The Belgard gate\x01",
            "Rin: Main town mining town\x01",
            "Aeolia: Main town mining town\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7557")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　： オルキスタワー\x01",
            "Scott: \"Waiting\"\x01",
            "Wenzel: \"Waiting\"\x01",
            "Rin: \"Stand by\"\x01",
            "Aeolia: \"Waiting\"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7655")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：リン・エオリアの捜索\x01",
            "Scott: Search for Lin · Aeoria\x01",
            "Wenzel: Searching for Lin · Eolia\x01",
            "Rin: * unknown\x01",
            "Aeolia: ※ unknown\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_773F")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：　《幻獣退治》\x01",
            "Scott: Tangram main gate\x01",
            "Wenzel: Tangram gate\x01",
            "Lynn: Ursula Hospital\x01",
            "Aeolia: Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_773F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_782B")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：幻獣退治及び調査\x01",
            "Scott: Tangram main gate\x01",
            "Wenzel: Tangram gate\x01",
            "Lynn: Ursula Hospital\x01",
            "Aeolia: Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_782B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7919")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：　　※休暇\x01",
            "Scott: Phantom Beast Extermination and Investigation\x01",
            "Wenzel: Phantom Beast Eradicate and Investigation\x01",
            "Phosphorus: Phantom Beast Extermination and Investigation\x01",
            "Aeolia: Phantom Beast Extermination and Investigation\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7A02")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　： オルキスタワー\x01",
            "Scott: Village of Almorica\x01",
            "Wenzel: \"Waiting\"\x01",
            "Rin: \"Stand by\"\x01",
            "Aeolia: Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7AEC")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：　ウルスラ病院\x01",
            "Scott: ※ Responding to requests\x01",
            "Wenzel: ※ Responding to requests\x01",
            "Lynn: Village of Almorika\x01",
            "Aeolia: Village of Armorika\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7BDB")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：カルバード共和国\x01",
            "Scott: Mainz in the mining town\x01",
            "Wenzel: The Belgard gate\x01",
            "Rin: ※ We are responding to requests\x01",
            "Aeolia: ※ Responding to requests\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7CC7")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：レミフェリア公国\x01",
            "Scott: \"Waiting\"\x01",
            "Wenzel: \"Waiting\"\x01",
            "Lynn: Ursula Hospital\x01",
            "Aeolia: Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7DAD")

    label("loc_7CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7DAD")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Name\x01",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x01",
            " 　Arios　：レミフェリア公国\x01",
            "Scott: Village of Almorica\x01",
            "Wenzel: Eleven Empire\x01",
            "Rin: \"Stand by\"\x01",
            "Aeolia: \"Waiting\"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7DAD")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_708F end

    def Function_15_7DC4(): pass

    label("Function_15_7DC4")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Requests to the Association of Priests\x01",
            "There are numerous projects.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E93")

    ChrTalk(
        0x101,
        (
            "#00000FAs usual, an amazing amount of requests\x01",
            "It seems to have been sent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FWell, we also\x01",
            "I can not be defeated.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_7E93")

    TalkEnd(0xFF)
    Return()

    # Function_15_7DC4 end

    def Function_16_7E97(): pass

    label("Function_16_7E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EBC")
    Call(0, 33)
    Return()

    label("loc_7EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ECF")
    Call(0, 34)
    Return()

    label("loc_7ECF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_7EE0")
    Jump("loc_8330")

    label("loc_7EE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F02")
    Call(0, 17)
    Jump("loc_7F2D")

    label("loc_7F02")


    ChrTalk(
        0xD,
        "#01109FSuzuku、あとで支援課に行こっ。\x02",
    )

    CloseMessageWindow()

    label("loc_7F2D")

    Jump("loc_8330")

    label("loc_7F32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F51")
    Jump("loc_82D4")

    label("loc_7F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_823E")
    TurnDirection(0xD, 0x1A2, 0)

    ChrTalk(
        0xD,
        (
            "#01100FHey, did you mention Shin?\x02\x03",
            "It looks like it's not a crossbell\x01",
            "When is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Is it okay?\x01",
            "Till the day after tomorrow … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01105FOh, then tomorrow's tower\x01",
            "Where do you see the Ochori ~?\x02\x03",
            "#01102FKeyaたち、デパートの屋上で\x01",
            "I'm planning to see but how about together?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "Is not it okay …?\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#01105FWell, how come?\x02\x03",
            "#01109FRyu, Henry,\x01",
            "Many other comings come\x01",
            "I think it's fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "…… If it says so far\x01",
            "You can participate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "It certainly was 11 o'clock tomorrow! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01109FWell, I'm waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(my mother……\x01",
            "I feel somewhat happy. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Well, I do not have much with other kids\x01",
            "Maybe I do not have the opportunity to play … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 2)
    TurnDirection(0xD, 0xE, 0)
    Jump("loc_82D4")

    label("loc_823E")

    TurnDirection(0xD, 0x1A2, 0)

    ChrTalk(
        0xD,
        (
            "#01100FWell then, at 11 o'clock tomorrow\x01",
            "I'm on the roof of a department store.\x02\x03",
            "#01109FBecause everyone is waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Oh, ah ……\x01",
            "Well then, see you tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 0)

    label("loc_82D4")

    Jump("loc_8330")

    label("loc_82D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8330")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82F1")
    Jump("loc_8330")

    label("loc_82F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8303")
    Call(0, 17)
    Jump("loc_8330")

    label("loc_8303")


    ChrTalk(
        0xD,
        "#01109FそれじゃあSuzukuも一緒に行こー！\x02",
    )

    CloseMessageWindow()

    label("loc_8330")

    TalkEnd(0xFE)
    Return()

    # Function_16_7E97 end

    def Function_17_8334(): pass

    label("Function_17_8334")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8455")

    ChrTalk(
        0xD,
        (
            "#01104FSuzukuー、シンも行っちゃったし\x01",
            "Want to play outside somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#06005FOh, yes, that's right.\x02\x03",
            "#06000FBut even if you go with two children\x01",
            "Is it alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01111FHmm … that surely it is so.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#01110FOh, so maybe there is a good idea.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8512")

    label("loc_8455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8512")

    ChrTalk(
        0xD,
        (
            "#01109FSo now, the blue sheet\x01",
            "I have it … ….\x01",
            "It is very big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#06002FHow nice……\x01",
            "Huh, I would like to see it, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01109FそれじゃあSuzukuも一緒に行こー！\x02",
    )

    CloseMessageWindow()

    label("loc_8512")

    SetScenarioFlags(0x1, 1)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_17_8334 end

    def Function_18_851E(): pass

    label("Function_18_851E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8556")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8543")
    Call(0, 33)
    Return()

    label("loc_8543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8556")
    Call(0, 34)
    Return()

    label("loc_8556")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_8567")
    Jump("loc_87DC")

    label("loc_8567")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8589")
    Call(0, 17)
    Jump("loc_85E2")

    label("loc_8589")


    ChrTalk(
        0xE,
        (
            "#06005FYes, but nice ……\x01",
            "What is a good idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01104FWell, I'm still cynical.\x02",
    )

    CloseMessageWindow()

    label("loc_85E2")

    Jump("loc_87DC")

    label("loc_85E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8780")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8606")
    Jump("loc_877B")

    label("loc_8606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86E4")
    TurnDirection(0xE, 0x1A2, 0)

    ChrTalk(
        0xE,
        (
            "#06002FHuh, you are Shin\x01",
            "He is a very good girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Absolutely ……\x01",
            "Well, there is not such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I do not know why,\x01",
            "Otoko carrying the \"black moon\" in the future\x01",
            "What is it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#06002FCouscous……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    TurnDirection(0xE, 0xD, 0)
    Jump("loc_877B")

    label("loc_86E4")

    TurnDirection(0xE, 0x1A2, 0)

    ChrTalk(
        0xE,
        (
            "#06002FCouscous……\x01",
            "I'm not sure, but,\x01",
            "I think Shin is a good boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "(Mum, mu … …\x01",
            "I am not like that\x01",
            "I do not think so. )\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 0)

    label("loc_877B")

    Jump("loc_87DC")

    label("loc_8780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_87DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8798")
    Jump("loc_87DC")

    label("loc_8798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87AA")
    Call(0, 17)
    Jump("loc_87DC")

    label("loc_87AA")


    ChrTalk(
        0xE,
        (
            "#06002FHehu, I understand.\x01",
            "Let's go see it together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87DC")

    TalkEnd(0xFE)
    Return()

    # Function_18_851E end

    def Function_19_87E0(): pass

    label("Function_19_87E0")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_19_87E0 end

    def Function_20_87E7(): pass

    label("Function_20_87E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2000, 1000, 2000, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20740, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04000.itp")
    SetChrPos(0x101, -2000, 0, -1000, 0)
    SetChrPos(0x102, -2000, 0, -1000, 0)
    SetChrPos(0x109, -2000, 0, -1000, 0)
    SetChrPos(0x105, -2000, 0, -1000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_88CF():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88CF)

    def lambda_88E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_88E9)
    Sleep(250)

    def lambda_88FD():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88FD)

    def lambda_8917():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8917)
    Sleep(600)

    def lambda_892B():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_892B)

    def lambda_8945():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8945)
    Sleep(250)

    def lambda_8959():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8959)

    def lambda_8973():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8973)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    OP_68(1000, 1100, 11300, 3000)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#04005FOh, you guys …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Michelle ……\x01",
            "long time no see.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x101, 500, 0, 3000, 0)
    SetChrPos(0x102, -500, 0, 3000, 0)
    SetChrPos(0x105, 0, 0, 1900, 0)
    SetChrPos(0x109, -1000, 0, 1900, 0)

    def lambda_8A54():
        OP_96(0xFE, 0x5DC, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A54)
    Sleep(100)

    def lambda_8A71():
        OP_96(0xFE, 0x1F4, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A71)
    Sleep(150)

    def lambda_8A8E():
        OP_96(0xFE, 0x7D0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8A8E)
    Sleep(100)

    def lambda_8AAB():
        OP_96(0xFE, 0x3E8, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8AAB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x105, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B6A")

    AnonymousTalk(
        0x8,
        (
            "Huh, it's been a long time.\x02\x03",
            "Capture in Altair City,\x01",
            "It was really hard work.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8BCD")

    label("loc_8B6A")


    AnonymousTalk(
        0x8,
        (
            "Huh, it's been a long time.\x02\x03",
            "though it's late\x01",
            "Capture in Altair City,\x01",
            "It was really hard work.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8BCD")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#12P#00000FThank you very much.\x01",
            "こちらこそ、Ariosさんたちの\x01",
            "It was saved because of cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FGiggle\x01",
            "Michelle seems to be well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FHuhun, of course, it's great ♪\x02\x03",
            "#04006FWell, Esther and Joshua\x01",
            "Thanks to losing it\x01",
            "I have gotten more busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FAfter all, is that so …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100Fでも、Ariosさんや\x01",
            "With other Hijackers\x01",
            "You seem to be turning well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FWell, there are not enough hands\x01",
            "I am used to it.\x02\x03",
            "#04000FLet me cut it somehow.\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, there\x01",
            "A fighter who is a friend of a civilian … …\x02\x03",
            "#10300FNo matter how busy he is\x01",
            "I can not say whining\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FExactly,\x01",
            "You know well.\x02\x03",
            "#04009FYou also police\x01",
            "It seems that it has been accepted,\x01",
            "That's why we too\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04005FWell, maybe\x01",
            "These kids … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, this is a new member of the support department.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FI recently dispatched from the guard\x01",
            "Noel · seeker!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWadi Hemisphere ……\x01",
            "Just saying\x01",
            "Can you understand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FOh\x01",
            "Funny kids are pretty\x01",
            "It seems they gathered.\x02\x03",
            "#04004FActive guards are to be said,\x01",
            "The head of that \"testament\"#2Rhead#Until\x01",
            "I do not think so.\x02\x03",
            "#04000FIn any case, the resumption of the support department\x01",
            "It is a great help for me here.\x02\x03",
            "In case of emergency\x01",
            "You can rely on it, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, of course.\x02\x03",
            "The position is different.\x01",
            "Let's work together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FHuh, since I first met\x01",
            "It has become a nice face.\x02\x03",
            "#04011FWell then … again.\x01",
            "これからThank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x139, 0)
    OP_4C(0x8, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_20_87E7 end

    def Function_21_91E6(): pass

    label("Function_21_91E6")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Fade(500)
    OP_68(-2140, 1300, 44740, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19620, 0)
    SetChrPos(0x101, -2140, 0, 45000, 90)
    SetChrPos(0x102, -2240, 0, 43520, 90)
    SetChrPos(0x109, -3420, 0, 43420, 90)
    SetChrPos(0x105, -3320, 0, 45300, 90)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0xB,
        "So, the Special Affairs Support Division.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, it's been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLong time no see,\x01",
            "To Mr. Lin, Mr. Eoria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FGuild people are\x01",
            "Were there any changes?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)

    ChrTalk(
        0xB,
        (
            "Oh, as usual\x01",
            "I'm being busy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x105, 500)

    ChrTalk(
        0xB,
        (
            "Well, what you are in there is\x01",
            "Are you newcomers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FWell, it is such a place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt is people of hush guys, right?\x01",
            "Thank you for your consideration!\x02\x03",
            "#10109FSpeaking of which, you\x01",
            "Several times heading to the Republic\x01",
            "I have seen you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x109, 500)

    ChrTalk(
        0xB,
        (
            "Oh, you are a security guard … …\x01",
            "By the way, at the Tangram gate\x01",
            "I feel I've seen it several times.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x109, 500)

    ChrTalk(
        0xC,
        (
            "Huhu, in the strategy in Altair City\x01",
            "It was quite active.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "Overcoming that cult character case,\x01",
            "You soon will be alone\x01",
            "I wonder if it has come to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHahaha, there's still a long way to go\x01",
            "I think that it is quite a lot ……\x02\x03",
            "#00000FFrom now on as long as we can\x01",
            "I will do my best.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        "Haha, that spirit.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0xC, 0x0, 0x0)
    SetScenarioFlags(0x138, 6)
    EventEnd(0x5)
    Return()

    # Function_21_91E6 end

    def Function_22_95F9(): pass

    label("Function_22_95F9")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4470, 1300, 42260, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21800, 0)
    SetChrPos(0x101, -3700, 0, 41400, 270)
    SetChrPos(0x102, -3600, 0, 42800, 270)
    SetChrPos(0x109, -2500, 0, 41000, 270)
    SetChrPos(0x105, -2400, 0, 43000, 270)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9703")
    Jump("loc_974D")

    label("loc_9703")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9723")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_974D")

    label("loc_9723")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9743")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_974D")

    label("loc_9743")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_974D")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9803")
    Jump("loc_984D")

    label("loc_9803")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9823")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_984D")

    label("loc_9823")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9843")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_984D")

    label("loc_9843")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_984D")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    OP_0D()

    ChrTalk(
        0x9,
        "#6POh, you guys ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… mission support section?\x01",
            "Hmm, it's been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FScott, Mr. Wenzel,\x01",
            "Good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10300FAre you a perpetrator?\x01",
            "Ghost, apparently\x01",
            "It seems your arms stand up.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x105, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99DF")
    Jump("loc_9A29")

    label("loc_99DF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_99FF")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A29")

    label("loc_99FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A1F")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A29")

    label("loc_9A1F")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A29")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6PThat kind of you,\x01",
            "Bad group of old city … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x109, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B14")
    Jump("loc_9B5E")

    label("loc_9B14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B34")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B5E")

    label("loc_9B34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B54")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B5E")

    label("loc_9B54")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9B5E")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6PAnd the other child there\x01",
            "Apparently it looks like a security guard.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C4F")
    Jump("loc_9C99")

    label("loc_9C4F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9C6F")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9C6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C8F")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9C99")

    label("loc_9C8F")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9C99")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6PHaha, it is quite interesting\x01",
            "It seems that newcomers have entered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10105FWa, you still are … …\x01",
            "Do you understand it only by seeing it?\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x105, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DD0")
    Jump("loc_9E1A")

    label("loc_9DD0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9DF0")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E1A")

    label("loc_9DF0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E10")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E1A")

    label("loc_9E10")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E1A")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "It is an ordinary policeman and its appearance\x01",
            "It seems to be obviously different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Work similar to a hypocrite\x01",
            "As you know, you also\x01",
            "It is to keep observation eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FHehe, thank you for your advice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PIn the future you can also help each other\x01",
            "I think that it is many, and each other\x01",
            "Let 's keep going.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x138, 7)
    EventEnd(0x5)
    Return()

    # Function_22_95F9 end

    def Function_23_9F62(): pass

    label("Function_23_9F62")

    EventBegin(0x0)
    Fade(500)
    OP_68(1480, 1200, 9530, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21690, 0)
    SetChrPos(0x101, 500, 0, 8300, 0)
    SetChrPos(0x102, 1500, 0, 8200, 0)
    SetChrPos(0x103, 1000, 0, 7000, 0)
    SetChrPos(0x109, 0, 0, 6800, 0)
    SetChrPos(0x105, 2000, 0, 6900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xC, 0xE1, 0x0)
    OP_93(0xB, 0xE1, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        "#5P#04000FOh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hi, I was saved yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FMr. Lin, Mr. Aoria … …\x01",
            "Are you all right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, somehow.\x01",
            "This is also thanks to you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "Tio, thank you later\x01",
            "I'm going to give you a good job\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xC, 500)

    ChrTalk(
        0x103,
        (
            "#12P#00203F…… I refuse to accept it.\x02\x03",
            "#00200FBut if that's the case\x01",
            "It sounds really okay, is not it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 500)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "Oh, that impossible\x01",
            "I can not do it yet ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "あれ、by the way……\x01",
            "What happened to that redhead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As usual this area\x01",
            "\"Well then I will … instead …\"\x01",
            "It's the timing I'm telling you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x105)
    OP_64(0x109)
    OP_64(0x103)

    ChrTalk(
        0x8,
        (
            "#5P#04001F… … It sounds like something happened.\x01",
            "Can you talk if it's okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F…… Yes, actually …\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy's\x01",
            "I explained that I had disappeared.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5P#04003F……I see.\x02\x03",
            "#04001FMainz occupation incident of this time … …\x01",
            "As long as \"red constellation\" is involved,\x01",
            "I was expecting somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F…… Guilds to this incident\x01",
            "How is it handled?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "…… the guard to settle the case\x01",
            "Current situation that it hits with full power,\x01",
            "For the moment it is a watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But if this situation lasts long,\x01",
            "We will have no choice but to move.\x01",
            "I see … Michelle?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)
    Sleep(50)
    TurnDirection(0x8, 0xB, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#04003FYeah ….\x02\x03",
            "#04001FIn some cases, from a neighboring country\x01",
            "Calling the honest fighters of Class A or higher,\x01",
            "You may need to intervene.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(100)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FThat's right … …! Is it?\x02",
    )

    CloseMessageWindow()

    def lambda_A621():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A621)
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        "Although it is the story of the worst case to the last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "今、Ariosさんが市長の所へ\x01",
            "I am going to negotiate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If this incident is to the guard\x01",
            "If there is no prospect of resolving … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108F… ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FWell, the safety of civilians is the first priority\x01",
            "It seems to be a natural course as a guild, though …\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    ChrTalk(
        0x8,
        (
            "#5P#04003F……Anyways,\x01",
            "That thing of that redhead boy\x01",
            "I also care about it.\x02\x03",
            "#04001FIt's a situation I do not know what will happen,\x01",
            "Please be careful of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F…… Yeah, I understand.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0xB, 0x13B, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    SetChrPos(0x0, 1000, 0, 9000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x16F, 2)
    EventEnd(0x5)
    Return()

    # Function_23_9F62 end

    def Function_24_A84A(): pass

    label("Function_24_A84A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_68(-1120, 1100, 7400, 0)
    MoveCamera(31, 10, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24030, 0)
    SetChrPos(0x101, -1750, 0, 2730, 0)
    SetChrPos(0x102, -2950, 0, 2530, 0)
    SetChrPos(0x103, -1750, 0, 1730, 0)
    SetChrPos(0x104, -2950, 0, 1530, 0)
    SetChrPos(0xF4, -1750, 0, 730, 0)
    SetChrPos(0xF5, -2950, 0, 530, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5P#04005FOh … …. you! Is it?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A9AF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A9AF)
    Sleep(50)

    def lambda_A9BF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A9BF)
    Sleep(50)

    def lambda_A9CF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_A9CF)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "Since independence declaration,\x01",
            "There was no tone but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha, I feel fine and tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FMr. Michelle, everyone … …\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00202FHehe, it is safe and than anything else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Huhu, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Tio-chan ……\x01",
            "It was really good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006F…… I'm giving greetings with a long time\x01",
            "It's not a situation either.\x02\x03",
            "#04001FIt's bad soon after reunion,\x01",
            "Can you exchange information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, that's OK.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(40, 1300, 9740, 0)
    MoveCamera(29, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22940, 0)
    SetChrPos(0x101, 300, 0, 8000, 0)
    SetChrPos(0x102, -1000, 0, 8200, 0)
    SetChrPos(0x103, 1500, 0, 8100, 0)
    SetChrPos(0x104, 0, 0, 6600, 0)
    SetChrPos(0xF4, -1300, 0, 7000, 0)
    SetChrPos(0xF5, 1600, 0, 6900, 0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "……I see,\x01",
            "It is said that it was supposed to be such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Honestly, I do not understand Wake\x01",
            "Although I was in a state\x01",
            "Finally the point of contact went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, at the West Exit\x01",
            "As I heard that the red \"Shinto machine\" appeared,\x01",
            "I thought it was something … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "No way, it is not esters.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the east exit and north entrance\x01",
            "Black month and the resistance of the guard are also\x01",
            "He seems to be helping … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hehe, this is yours\x01",
            "I wonder if there are connections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FHaha, well like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105Fby the way……\x01",
            "A \"magician\" appears in the city,\x01",
            "Is there no human damage done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah, for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Whether there are people who are not running away,\x01",
            "We are also wary of\x01",
            "I tried around this area, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently, \"magic guards\"\x01",
            "To the Cross Bell citizen absolutely\x01",
            "It does not seem to work out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF57")

    ChrTalk(
        0x105,
        (
            "#12P#10403FHmm … the President's side is good\x01",
            "It seems to be controlling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B012")

    label("loc_AF57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFB4")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FHmm … the President's side is good\x01",
            "It seems to be controlling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B012")

    label("loc_AFB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B012")

    ChrTalk(
        0x109,
        (
            "#12P#10101FApparently, the president is good\x01",
            "You seem to be controlling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B012")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B05D")

    ChrTalk(
        0x106,
        (
            "#12P#10705FIn a sense, relieved\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0E8")

    label("loc_B05D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0A8")

    ChrTalk(
        0x109,
        (
            "#12P#10105FIn a sense, relieved\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0E8")

    label("loc_B0A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0E8")

    ChrTalk(
        0x105,
        (
            "#12P#10304FIn a sense, relieved\x01",
            "Is it alright?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0E8")


    ChrTalk(
        0x101,
        (
            "#12P#00001FStill …\x01",
            "Who are you worried about?\x01",
            "It should be quite a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FWell … if this condition lasts long,\x01",
            "People who get injured or get caught\x01",
            "There is no limit not to get out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003FYeah, an innocent civilians\x01",
            "As it is in danger,\x01",
            "I can not leave the guilds alone.\x02\x03",
            "#04011FRush into the Orkis Tower\x01",
            "President's arrest …\x01",
            "I will let you help me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204FThank you very much.\x01",
            "…… I am very encouraging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003FHowever, …\x01",
            "Perhaps at the Orchis Tower\x01",
            "Ariosがいるわ。\x02\x03",
            "That Marybele missy,\x01",
            "\"Battle\" something as well\x01",
            "I will be waiting.\x02\x03",
            "#04001FSurely it will be incomprehensible … …\x01",
            "You know that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303F…… I am well-informed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FWhatever \"wall\" there is … …\x01",
            "Because we only push forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04004FHuff, preparing your heart\x01",
            "You seem to be done.\x02\x03",
            "#04001F──When you start a strategy,\x01",
            "Please contact me again.\x02\x03",
            "At that time our friends\x01",
            "I will prepare thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FWell … then, later.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 300, 0, 8000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    OP_93(0xB, 0x13B, 0x0)
    OP_93(0x9, 0x2D, 0x0)
    OP_93(0xA, 0x2D, 0x0)
    SetScenarioFlags(0x1BB, 0)
    EventEnd(0x5)
    Return()

    # Function_24_A84A end

    def Function_25_B4FD(): pass

    label("Function_25_B4FD")

    EventBegin(0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04000.itp")
    Fade(500)
    OP_68(1000, 1000, 11300, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 900, 0, 10000, 0)
    SetChrPos(0x102, 1500, 0, 9400, 0)
    SetChrPos(0x104, 300, 0, 8700, 0)
    SetChrPos(0x109, -300, 0, 9300, 0)
    SetChrPos(0x105, -1400, 0, 9350, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Oh, you came a lot.\x02\x03",
            "まだAriosは戻ってないけど\x01",
            "Are you waiting on the second floor if it is okay?\x02\x03",
            "What if I had done errands\x01",
            "You may come.\x02",
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
        0x101,
        (
            "#12P#00005FOh, is that so?\x02\x03",
            "#00008F(It is almost an evening ……\x01",
            "Did you have anything else to do? )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【There are still other things to do】\x01",          # 0
            "【Ariosが戻るのを待つ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B798"),
        (1, "loc_B825"),
        (SWITCH_DEFAULT, "loc_BA2A"),
    )


    label("loc_B798")


    ChrTalk(
        0x8,
        (
            "#5P#04011FIf that is the case, you can use it\x01",
            "Please come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FWell, I will come again.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 1000, 0, 9000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_BA2A")

    label("loc_B825")


    ChrTalk(
        0x8,
        (
            "#5P#04011FWell then, go up to the second floor\x01",
            "Please relax properly.\x02\x03",
            "I have tea and coffee prepared.\x01",
            "You can brew your own bowls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FOkay, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FWell then I will disturb you.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 4500)

    def lambda_B903():

        label("loc_B903")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B903")

    QueueWorkItem2(0x8, 2, lambda_B903)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 26)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x2)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    StopBGM(0xBB8)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, sooner\x01",
            "Ariosがギルドに戻ってきた。\x02\x03",
            "Lloyd's again, the trade council,\x01",
            "About \"black moon\" and \"red constellation\"\x01",
            "I decided to exchange information.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4C(0x8, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_BA2A")

    label("loc_BA2A")

    Return()

    # Function_25_B4FD end

    def Function_26_BA2B(): pass

    label("Function_26_BA2B")

    OP_92(0xFE, 0x1F40, 0x2AF8, 0x1F4)

    def lambda_BA3D():
        OP_95(0xFE, 8000, 0, 11000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA3D)
    WaitChrThread(0xFE, 1)

    def lambda_BA5B():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA5B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_BA2B end

    def Function_27_BA75(): pass

    label("Function_27_BA75")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    SoundLoad(4049)
    SoundLoad(4050)
    LoadChrToIndex("chr/ch09102.itc", 0x1E)
    LoadChrToIndex("chr/ch02402.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch02902.itc", 0x23)
    LoadChrToIndex("chr/ch03002.itc", 0x24)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -9300, 100, 46800, 0)
    SetChrPos(0x102, -7500, 100, 46800, 0)
    SetChrPos(0x104, -5700, 100, 46800, 0)
    SetChrPos(0x109, -11100, 100, 49400, 180)
    SetChrPos(0x105, -11100, 100, 46800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrFlags(0x8, 0x8000)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -7500, 100, 49400, 180)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    EndChrThread(0x10, 0xFF)
    SetChrPos(0x10, -9300, 100, 49400, 180)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    SetMapObjFrame(0xFF, "chair", 0x0, 0x1)
    SetMapObjFrame(0xFF, "chair_shadow", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x0, 0x12)
    OP_78(0x1, 0x13)
    OP_78(0x2, 0x14)
    OP_78(0x3, 0x15)
    OP_78(0x4, 0x16)
    OP_78(0x5, 0x17)
    OP_78(0x6, 0x18)
    OP_78(0x7, 0x19)
    OP_49()
    SetChrPos(0x12, -11100, 0, 46600, 0)
    OP_D5(0x12, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x13, -9300, 0, 46600, 0)
    OP_D5(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x14, -7500, 0, 46600, 0)
    OP_D5(0x14, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x15, -5700, 0, 46600, 0)
    OP_D5(0x15, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x16, -11100, 0, 49600, 0)
    OP_D5(0x16, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x17, -9300, 0, 49600, 0)
    OP_D5(0x17, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x18, -7500, 0, 49600, 0)
    OP_D5(0x18, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x19, -5700, 0, 49600, 0)
    OP_D5(0x19, 0x0, 0x0, 0x0, 0x0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(-8200, 900, 48300, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(19500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x10,
        (
            "#4049V#30W─ ─ I see.\x02\x03",
            "#4050VEven though \"Crimson Shokai\"\x01",
            "That there was such a back … …\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFD2)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04006FRecently, information on Teichi area\x01",
            "It was hard to enter.\x02\x03",
            "#04000FThanks, thanks, I was saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00004FNo, I hope you find it useful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FBut the information on \"red constellation\"\x01",
            "Is not it even grabbed by you?\x02\x03",
            "#10300FGuild and skirmishes with hunting soldiers\x01",
            "I hear that I often do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FIndeed there are many,\x01",
            "With the big ones of the \"red constellation\" class\x01",
            "Rare opportunities to hold a thing.\x02\x03",
            "#01400F… … If you do something wrong, you know each other\x01",
            "It can be a full war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FTo that extent ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FA little small country\x01",
            "It looks like an army level …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003F── Among the many hunting soldiers\x01",
            "\"Red constellation\" can be said to be different.\x02\x03",
            "Having connections across the continent,\x01",
            "If there is any sign of a conflict, immediately intervene\x01",
            "Promote ourselves high … …\x02\x03",
            "#04001FIt is likely that they will compete with the same hunting soldiers\x01",
            "I wonder \"West brigade brigade\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FCertainly, the young head of Rubathe\x01",
            "Was it the place where was the old nest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F…… Have a happy day.\x01",
            "It is a hunting corps gathering the fierce battlefights.\x02\x03",
            "Especially the top called \"hunter king\"\x01",
            "It was a ceremonial person … …\x02\x03",
            "#00303FSix months ago \"fighting spirit\" ──\x01",
            "It seems that my father got involved with my father.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x102,
        "#6P#00108FRandy …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008F…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#01405FHm, I guess there are various things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FOnce, for that information\x01",
            "Even the guilds have grasped.\x02\x03",
            "#04001FBy the way, \"Western brigade\" is currently\x01",
            "I heard that the activity is paused, but …\x02\x03",
            "The person of \"Red constellation\" as usual\x01",
            "You seem to be energetically active, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FYour uncle is still there.\x02\x03",
            "#00303F── Deputy head of red constellation,\x01",
            "\"Red war demon#8ROgre Rosso#\"Sigmund.\x02\x03",
            "#00301F\"Fighting spirit\" and \"hunting king\"\x01",
            "It is a comparable thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01400FThose three are particularly famous.\x02\x03",
            "#01403F── As far as I hear the story,\x01",
            "Whether I can compete or not.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FWell … that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F\"The sword of the wind\" is\x01",
            "I can not compare it … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FWell, as far as I can see\x01",
            "I wonder if it is about half or so?\x02\x03",
            "#04000FSwordsmen and hunters, the battle style is also\x01",
            "The timing to be good will also be different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F… they are.\x02\x03",
            "#00301FYou certainly are strong\x01",
            "Uncle Taku also is a genuine compound.\x02\x03",
            "If we meet each other,\x01",
            "You should not be free from something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FOh, I know.\x02\x03",
            "#01400F─ ─ But if you need it\x01",
            "You may be hostile to them.\x02\x03",
            "The problem is what they are for\x01",
            "I wonder if I entered the crossbell … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x109,
        "#10106FAfter all it is there …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FEven if you collect this information\x01",
            "I do not understand there.\x02\x03",
            "#10300FThe clues are imperial government\x01",
            "About what is involved?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#04001FThat's it ….\x01",
            "One, there is information to worry about.\x02\x03",
            "共和国方面でAriosが\x01",
            "It grabbed me though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FWhat kind of information is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FOh ─ ─ \"Black moon#4RHayuue#\"About.\x02\x03",
            "#01401FApparently, the Republic Government\x01",
            "With the elders of \"Black moon\"\x01",
            "She seems to be conducting something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00007Freally……! Is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_CAE2")

    ChrTalk(
        0x102,
        (
            "#12P#00108FWhen I say the elder of \"Black moon\"\x01",
            "Shin's your grandpa is also so ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB2C")

    label("loc_CAE2")


    ChrTalk(
        0x102,
        (
            "#12P#00108FThe elder of the \"black moon\"\x01",
            "It is more central people …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB2C")


    ChrTalk(
        0x8,
        (
            "#04006F… That's right.\x01",
            "It is another point though.\x02\x03",
            "#04001FHe led the transaction\x01",
            "Kirika・ロウランって女性なの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00107Fthat's……\x01",
            "まさか、あのKirikaさん！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FOh, at the time of the auction\x01",
            "Do you see the black-haired sister you saw?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FTo tell the truth, she is both the Association of Sagittarius\x01",
            "It is a person with a rim ……\x02\x03",
            "リベールのツァchair支部で\x01",
            "There are also experiences that I was accepting.\x02\x03",
            "#01400FHowever, retired about a year ago,\x01",
            "He moved to the information agency of Calvert.\x02\x03",
            "Name of the information agency\x01",
            "\"Rock Smith Institution\" is called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FLocksmith …\x01",
            "It is the name of the President of the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FPresident led by a new information agency\x01",
            "I heard about the story that was established … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00101FWait a moment, please!\x02\x03",
            "\"Red constellation\" and \"Black moon\"\x01",
            "You have fought before! Is it?\x02\x03",
            "Two of them, an intelligence official of the Daikoku\x01",
            "It means that they are in contact with each other …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuff, a splendid confrontation composition\x01",
            "That's why it is getting ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013FDamn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FWell, no doubt in the place of crossbells\x01",
            "Reparate war between the Empire and the Republic … …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FOf course, that possibility is also considered.\x02\x03",
            "#04001FEspecially at the commerce meeting from tomorrow\x01",
            "From Elevenia the Prince to the Prime Minister,\x01",
            "President will come from Calvert.\x02\x03",
            "Take the opponent's top by multiplying each other\x01",
            "I might be trying to kill you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FBut for that, each other,\x01",
            "It is unnatural not to hide contacts.\x02\x03",
            "If \"black moon\" or \"red constellation\" moves\x01",
            "Such a background appears in the light\x01",
            "We will invite the international community to condemn.\x02\x03",
            "#01400FWhether you are an empire or a republic\x01",
            "It does not seem to be risky that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWell, hmm … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F…… Certainly, a short-circuit attack\x01",
            "It is not a situation to set up.\x02\x03",
            "#00108FBut why then …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FFucking, uncle yours,\x01",
            "What on earth do you think about …?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00003F─ ─ Anyway,\x01",
            "The composition that is currently being completed\x01",
            "There should be some meaning.\x02\x03",
            "#00008FProbably, we do not get it\x01",
            "There should be a \"missing piece\" …\x02\x03",
            "#00001FIt seems necessary to grasp it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    ChrTalk(
        0x102,
        "#12P#00105FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHuh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FUhufu, as expected Lloyd.\x01",
            "I was deferred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01404FActually, we are in the same view.\x02\x03",
            "#01402FAbout that \"missing piece\"\x01",
            "Using the information network of the guild\x01",
            "I am in the process of attaching a hit now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)

    ChrTalk(
        0x101,
        "#12P#00002FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThen, if you know something\x01",
            "Will you tell me this too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYes, as new facts are known,\x01",
            "I will also contact the police headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01402FEven for you\x01",
            "Please let me know if you grab something.\x02\x03",
            "3 days from tomorrow\x01",
            "To survive without anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOK……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FIf something goes wrong\x01",
            "I will let you know soon.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、Zeitと共に\x01",
            "KeyaとSuzukuがギルドに戻って来た。\x02\x03",
            "Lloyd's, father daughter in the water\x01",
            "夕食に行くというAriosたちに\x01",
            "I decided to say good-by and decided to return to the support department.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c100B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_BA75 end

    def Function_28_D6CB(): pass

    label("Function_28_D6CB")

    EventBegin(0x0)
    Fade(500)
    OP_68(1000, 1000, 11300, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 900, 0, 10000, 0)
    SetChrPos(0x102, 1500, 0, 9400, 0)
    SetChrPos(0x103, -300, 0, 9300, 0)
    SetChrPos(0x104, -1400, 0, 9350, 45)
    SetChrPos(0x109, 300, 0, 8700, 0)
    SetChrPos(0x105, 900, 0, 8100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5P#04005FOh, you guys ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012Fmy mother……\x01",
            "Mr. Michelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FThat, after listening to the story\x01",
            "Please be a little worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FFu, you do not.\x01",
            "It has become a form I prompted.\x02\x03",
            "#04011FBut thanks.\x01",
            "It is pleasant to come and visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FI mean,\x01",
            "Still with Eoria\x01",
            "Did not we get in touch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003Fええ、Ariosたちが\x01",
            "I'm hitting it by hand … …\x02\x03",
            "#04008F…… Really really.\x01",
            "I wonder what he is doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FYou are worried as expected …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FHM……\x01",
            "Things that Enigma can not communicate\x01",
            "Are you going out of autonomous state?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FI thought so, too,\x01",
            "Records using stations and airports\x01",
            "It seems there is nothing.\x02\x03",
            "#04001FAlso at the Belgard and Tangram gate\x01",
            "There seems to be no traffic record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001Fthat is……\x01",
            "It is truly amusing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#12P#00203F…… If Lin's are\x01",
            "If you are in autonomous state …\x02\x03",
            "#00200FSomehow\x01",
            "It may be possible to identify it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_DBA0():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DBA0)
    Sleep(50)

    def lambda_DBB0():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DBB0)
    Sleep(50)

    def lambda_DBC0():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DBC0)
    Sleep(50)

    def lambda_DBD0():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DBD0)
    Sleep(50)

    def lambda_DBE0():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DBE0)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#11P#00005FReally……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#04005FWhat, what method! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FTo be sure, Enigma is at the research stage\x01",
            "The function should have been installed.\x02\x03",
            "#00200FOne of them is an emergency\x01",
            "It is a function to transmit an alert signal.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#12P#10105FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FWith preliminary power in the orbment\x01",
            "At specified intervals,\x01",
            "It is a mechanism to transmit a conductive wave … …\x02\x03",
            "Because it is a too weak conductive wave\x01",
            "I heard that it has not reached practical use.\x02\x03",
            "#00201FHowever, the function itself\x01",
            "Whether it remains without being cut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FWell, that weak conductive wave\x01",
            "If I managed to catch it … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04001FLynn and Eolia's whereabouts are also\x01",
            "That's why I can identify you …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204FIs it worth the try?\x02\x03",
            "#00202FAbout this function\x01",
            "Since Roberts boss is detailed\x01",
            "Let's go to IBC.\x02\x03",
            "It will probably be a power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00000FOkay, let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006F… … It does not end.\x01",
            "I will really be saved.\x02\x03",
            "#04000FIf you know something\x01",
            "こちらにもPlease contact me.\x02\x03",
            "In some cases\x01",
            "Ariosたちを呼び戻すから。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E06A():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E06A)
    Sleep(50)

    def lambda_E07A():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E07A)
    Sleep(50)

    def lambda_E08A():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E08A)
    Sleep(50)

    def lambda_E09A():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E09A)
    Sleep(50)

    def lambda_E0AA():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E0AA)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        "#12P#00100FOK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell then, then\x01",
            "Let's go to IBC.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 1000, 0, 9000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 1)
    OP_29(0xA8, 0x4, 0x10)
    OP_29(0xA9, 0x4, 0x2)
    OP_29(0xA9, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_28_D6CB end

    def Function_29_E16C(): pass

    label("Function_29_E16C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(128)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)
    OP_68(1000, 1000, 11300, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x7)
    SetChrPos(0x101, 900, 0, 10000, 180)
    SetChrPos(0x102, 1500, 0, 9400, 0)
    SetChrPos(0x103, -300, 0, 9300, 0)
    SetChrPos(0x104, -1400, 0, 9350, 45)
    SetChrPos(0x109, 300, 0, 8700, 0)
    SetChrPos(0x105, 900, 0, 8100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_E27C():
        TurnDirection(0x102, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E27C)
    Sleep(0)

    def lambda_E28C():
        TurnDirection(0x103, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E28C)
    Sleep(0)

    def lambda_E29C():
        TurnDirection(0x104, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E29C)
    Sleep(0)

    def lambda_E2AC():
        TurnDirection(0x109, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E2AC)
    Sleep(0)

    def lambda_E2BC():
        TurnDirection(0x105, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E2BC)
    Sleep(0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_4B(0x8, 0xFF)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Yes, the guiding boat\x01",
            "I arranged for a dock at the port area.\x02\x03",
            "I think that I can get on at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006FThat's right, thank you.\x02\x03",
            "#00001FSorry, Fran.\x01",
            "Asking suddenly impossible.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, this is the time\x01",
            "Because it is your support ~.\x02\x03",
            "But is it a wet swamp in the south …?\x01",
            "Please take good care of yourself, do not you think?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FOh, I will keep it for myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sound(128, 1, 50, 0)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10101FSomehow boat\x01",
            "You seem to have secured?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#00002FOh, fran quickly\x01",
            "I was saved for arranging it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006F─ ─ Regarding this time\x01",
            "It has become reliable.\x02\x03",
            "#04001FBut is it really okay?\x02\x03",
            "１時間もすればAriosたちが\x01",
            "I think that it will come back ….\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E630():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E630)
    Sleep(50)

    def lambda_E640():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E640)
    Sleep(50)

    def lambda_E650():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E650)
    Sleep(50)

    def lambda_E660():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E660)
    Sleep(50)

    def lambda_E670():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E670)
    Sleep(50)

    def lambda_E680():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E680)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x104,
        (
            "#6P#00303FNo, if it were it\x01",
            "You had better go with us before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FI agree……\x01",
            "I do not understand any situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, if they come back\x01",
            "Tell me to follow you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04000F… … I understand.\x02\x03",
            "#04003FWhether it is phosphorus or aeolia\x01",
            "A fierce fighter who approaches A class.\x02\x03",
            "Both of them did not contact\x01",
            "The fact that it is stopped together … …\x02\x03",
            "#04001FI do not know what it is.\x01",
            "Be wary of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013FYes……!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#6P#00201FOnce prepared\x01",
            "Let's go to the dock.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, 1000, 0, 9000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x165, 0)
    OP_29(0xA9, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_29_E16C end

    def Function_30_E8D6(): pass

    label("Function_30_E8D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(1000, 1000, 10800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -2000, 0, -1500, 0)
    SetChrPos(0x102, -2000, 0, -1500, 0)
    SetChrPos(0x103, -2000, 0, -1500, 0)
    SetChrPos(0x104, -2000, 0, -1500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 2000, 0, 8800, 315)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, 1900, 0, 10200, 270)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0xB, -200, 0, 10200, 90)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, -300, 0, 8800, 45)
    OP_4B(0xC, 0xFF)
    StopBGM(0xFA0)
    SetCameraDistance(20500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00001FExcuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FExcuse me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7251", 0)
    OP_68(-2000, 1000, 3000, 2000)
    MoveCamera(49, 23, 0, 2000)
    SetCameraDistance(21000, 2000)

    def lambda_EB5C():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_EB5C)
    Sleep(50)

    def lambda_EB6C():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_EB6C)
    Sleep(50)

    def lambda_EB7C():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_EB7C)
    Sleep(50)

    def lambda_EB8C():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_EB8C)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    Sleep(1000)

    def lambda_EBAF():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EBAF)

    def lambda_EBC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EBC9)
    Sleep(600)

    def lambda_EBDD():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EBDD)

    def lambda_EBF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EBF7)
    Sleep(900)

    def lambda_EC0B():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EC0B)

    def lambda_EC25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EC25)
    Sleep(600)

    def lambda_EC39():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EC39)

    def lambda_EC53():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_EC53)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#04005F#6PYou guys ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PHey, are they Lloyd? ….\x02",
    )

    CloseMessageWindow()

    def lambda_ECB1():

        label("loc_ECB1")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_ECB1")

    QueueWorkItem2(0x9, 2, lambda_ECB1)

    def lambda_ECC3():

        label("loc_ECC3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_ECC3")

    QueueWorkItem2(0xA, 2, lambda_ECC3)

    def lambda_ECD5():

        label("loc_ECD5")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_ECD5")

    QueueWorkItem2(0xC, 2, lambda_ECD5)

    def lambda_ECE7():
        OP_96(0xFE, 0x384, 0x0, 0x206C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ECE7)
    Sleep(200)

    def lambda_ED04():
        OP_96(0xFE, 0xFFFFFED4, 0x0, 0x1E78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ED04)
    Sleep(100)

    def lambda_ED21():
        OP_96(0xFE, 0x578, 0x0, 0x1C84, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ED21)
    Sleep(100)

    def lambda_ED3E():
        OP_96(0xFE, 0xC8, 0x0, 0x1A90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ED3E)
    Sleep(1500)
    Fade(500)
    OP_68(1000, 1100, 9900, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)

    def lambda_ED8E():
        OP_96(0xFE, 0xA8C, 0x0, 0x251C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ED8E)
    Sleep(100)

    def lambda_EDAB():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0x251C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_EDAB)
    WaitChrThread(0x103, 1)
    EndChrThread(0xC, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)

    ChrTalk(
        0x104,
        (
            "#00306F#12PWhew, well aligned\x01",
            "Are you lined up with shrimp claws?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt's unnecessary …\x01",
            "I would like to say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P… Well, I will not deny it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PMore than\x01",
            "何でAriosさんが……\x02\x03",
            "Haa … it's too late for my bedding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PTruly, that sign\x01",
            "It is something you did not have at all …\x02\x03",
            "If you say\x01",
            "Visiting the Orkis Tower\x01",
            "I wonder if it was recently many?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FI see …\x01",
            "To the end to respond to the guild\x01",
            "I should have gone to talk.\x02\x03",
            "#04008FNo way to make such arrangements\x01",
            "I was talking … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F…… Actually that around\x01",
            "I wanted to ask you.\x02\x03",
            "#00001FAriosさんはまだ、\x01",
            "Do you belong to the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04001F… … Last night, I resigned my resignation suddenly\x01",
            "I returned the hittermen emblem.\x02\x03",
            "#04006FI finished all the work I had,\x01",
            "The reason for taking measures in the future was\x01",
            "It seems to be like him, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206F確かにAriosさんらしい\x01",
            "It is polite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P… But, like this one suddenly\x01",
            "It is truly a problem to quit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PMoreover, \"Crossbell independent country\"\x01",
            "With the Secretary of the \"Defense Forces\" etc … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P…… That's what I said\x01",
            "I am afraid of the reaction of Erebonia.\x02\x03",
            "#5PEven threats like freezing assets\x01",
            "It's in a state I have ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P……Yeah……\x01",
            "I am afraid of the reaction of the Republic.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#11P… but ….\x01",
            "Ariosさんの気持ちも\x01",
            "I can not understand it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1800, 1100, 9580, 1000)
    MoveCamera(41, 17, 0, 1000)

    def lambda_F37E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F37E)
    Sleep(50)

    def lambda_F38E():
        TurnDirection(0xB, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_F38E)
    Sleep(50)

    def lambda_F39E():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_F39E)
    Sleep(50)

    def lambda_F3AE():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F3AE)
    Sleep(50)

    def lambda_F3BE():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F3BE)
    Sleep(50)

    def lambda_F3CE():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F3CE)
    Sleep(50)

    def lambda_F3DE():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F3DE)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        "#5PScott …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P俺もAriosさんと同じ\x01",
            "I am from Crosbell City, but … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PCertainly, it seems like it was also in a speech\x01",
            "Mysterious accident of unknown cause\x01",
            "I was awake once or twice a year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI do not know the truth, but …\x01",
            "Everyone in the Empire or Republic\x01",
            "I felt that it was awkward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P…………that is……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, recently here\x01",
            "Such accidents have not happened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P５年前、Ariosさんの奥さんと\x01",
            "Suzukuちゃんが巻き込まれた事故が\x01",
            "It may be said that it is the last.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00011FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PPossibly …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003F…… I happened to see the street five years ago\x01",
            "Explosion of flight vehicle · Accident on fire … …\x02\x03",
            "#04008FInitially a leader#8ROval engine#The runaway of\x01",
            "It was thought to be a flammable cargo … ….\x01",
            "Surely there were too many suspicious points.\x02\x03",
            "#04001FAnd caught up in that accident\x01",
            "Saya's wife dies … …\x01",
            "Suzukuちゃんは光を失った。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FWas it such a story? …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00208F…… Fragmentary information\x01",
            "I heard it to a certain extent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FそれでAriosさんは\x01",
            "I left the police station and moved to the guild …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FアタシもAriosとは\x01",
            "I am going out from then on ….\x02\x03",
            "He did not say a word\x01",
            "You must have been caught for a long time.\x02\x03",
            "#04008F…… I think so\x01",
            "I also accepted this role\x01",
            "I think I finally got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_68(1000, 1100, 9900, 1000)
    MoveCamera(41, 17, 0, 1000)
    TurnDirection(0x101, 0x8, 500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00003F── Mr. Michelle.\x02\x03",
            "#00001FAlthough I am rude, I ask you … …\x01",
            "Ariosさんのスケジュールで\x01",
            "Did you have any suspicious points?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA6C():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_FA6C)
    Sleep(50)

    def lambda_FA7C():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_FA7C)
    Sleep(50)

    def lambda_FA8C():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_FA8C)
    Sleep(50)

    def lambda_FA9C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FA9C)
    Sleep(50)

    def lambda_FAAC():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FAAC)
    Sleep(50)

    def lambda_FABC():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FABC)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x8,
        "#5P#04005FHuh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PLloyd, what do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FCommander of the \"Defense Force\" …\x02\x03",
            "To suffer suddenly\x01",
            "I think that it is too heavy role.\x02\x03",
            "#00001FMaybe, Mayor Dieter … …\x01",
            "No, I have a foundation with the President\x01",
            "Was not it being done?\x02\x03",
            "It also recently#4R噵 噵#Not a while ago#10R噵 噵 噵 噵 噵#From.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#04008F………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_FC42():
        TurnDirection(0xB, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_FC42)
    Sleep(50)

    def lambda_FC52():
        TurnDirection(0xA, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_FC52)
    Sleep(50)

    def lambda_FC62():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_FC62)
    Sleep(50)

    def lambda_FC72():
        TurnDirection(0xC, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_FC72)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    def lambda_FC92():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FC92)

    def lambda_FC9F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FC9F)

    def lambda_FCAC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FCAC)

    ChrTalk(
        0xB,
        "#12PMichelle … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "No way … is it true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006F…… Certainly, such as destinations,\x01",
            "What is wrong with the report\x01",
            "Sometimes it happened.\x02\x03",
            "#04008FIf I had a job for that much\x01",
            "当然だとはI thought that … ….\x02\x03",
            "#04001F…… Think about it,\x01",
            "Ariosが報告を間違うなんて\x01",
            "It's unnatural, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well then, at those times\x01",
            "Contact with Mayor Dieter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003F…… That possibility\x01",
            "It may be conceivable.\x02\x03",
            "#04001FLloyd, as expected.\x01",
            "It's a scary insight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FHouse……\x01",
            "Sorry to say rude things.\x02\x03",
            "#00003FIn addition to that rude\x01",
            "I will ask you ….\x02\x03",
            "#00008FそうしたAriosさんの行き先や\x01",
            "Different schedule ──\x02\x03",
            "#00013FOver half a year ago#10R噵 噵 噵 噵 噵#so\x01",
            "Do not you remember?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_FFF8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FFF8)

    def lambda_10005():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10005)
    Sleep(50)

    def lambda_10015():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_10015)
    Sleep(50)

    def lambda_10025():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_10025)
    Sleep(50)

    def lambda_10035():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_10035)
    Sleep(50)

    def lambda_10045():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10045)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        "#6P#00105FMore than half a year ago ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200F…… Mr. Dieter is still\x01",
            "I am not even a mayor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FWell, hmm … ….\x01",
            "As expected to be there before that\x01",
            "I do not remember … ….\x02\x03",
            "#04005FOh, but did you have that?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1013C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1013C)
    Sleep(50)

    def lambda_1014C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1014C)

    def lambda_10159():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10159)

    ChrTalk(
        0x101,
        "#12P#00005Fthat……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04004FIt is the last day of the festival commemoration festival.\x02\x03",
            "#04000FHe, at work to Remiferia\x01",
            "I was to have a business trip … ….\x02\x03",
            "Hurry up to it#4REmbarrassment#, I canceled it\x01",
            "I did not report it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04005FLater when you notice and ask\x01",
            "I was busy and I missed reporting\x01",
            "I was telling you ….\x02\x03",
            "#04001F…… What are you interested in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PWell, that anniversary\x01",
            "It was a murderous busy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PEven if there is a discrepancy in the report\x01",
            "I think it is unreasonable … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00008F#30W………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F… … The last day of the memorial festival ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FSpeaking of the last day\x01",
            "There was \"that\", but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PHow does it connect?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F……I do not understand.\x01",
            "But I feel that something is going to be connected.\x02\x03",
            "#00008FUp until now, we are busy,\x01",
            "The points and points I had missed … …\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_104FE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_104FE)
    Sleep(50)

    def lambda_1050E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1050E)

    ChrTalk(
        0x101,
        "#12P#00011FI'm sorry, I will excuse you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FYes, here crossbar police,\x01",
            "At the Special Affairs Support Division ─ ─\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a young man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hmm?\x01",
            "\"Crossbell Defense Force, Special Affairs Support Division\"\x01",
            "Is not that a mistake?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013F……you are……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a young man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Juffu\x01",
            "Would you like a satellite?\x02\x03",
            "Sei Kai Sare Takata Kana\x01",
            "Morenak Gowka Keihin wo ─\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006F…… I do not mind quitting.\x02\x03",
            "#00010FWhich clothes are thrown together ……\x01",
            "Did you come to the crossbell?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a young man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Whew, I was disliked Mon.\x02\x03",
            "It seems to be flashy\x01",
            "Can not you talk for a moment?\x02\x03",
            "Well, I guess I will not let you lose.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013F…………………………………….\x02\x03",
            "#00006F……I understand.\x01",
            "Where should I go?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a young man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Crimson Shokai\" … ….\x01",
            "No, former \"Rubathe Shokai\"\x01",
            "Should I say it?\x02\x03",
            "Do you want to be over there in the president's office?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00008FIs that over there … ….\x01",
            "I understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a young man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Sounds waiting for you ~.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 70, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#6P#00101FDid you mean ……\x01",
            "Mr. Tsao, who is missing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FBy the way, before this,\x01",
            "When Randy's gone,\x01",
            "You got a message.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FIs that so?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00003F─ ─ No, not.\x02\x03",
            "#00013FCaptain Rector of the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#6P#00107FWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FThat man … … Also on the crossbell\x01",
            "Did you come here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12P……surely\x01",
            "I'm feeling downright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FApparently at the old Rubathe shop\x01",
            "It seems there is a story.\x02\x03",
            "#00001FConsidering the connection with \"red constellation\"\x01",
            "I can not be very careful … …\x01",
            "Let's go only go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12PRight\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201FIf you do not enter the tiger's hole, is not it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F…… just preparation\x01",
            "It seems better to do everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#04006FYou do not seem to have a lot of trouble …\x02",
    )

    CloseMessageWindow()

    def lambda_10CF1():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10CF1)
    Sleep(50)

    def lambda_10D01():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10D01)
    Sleep(50)

    def lambda_10D11():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10D11)
    Sleep(50)

    def lambda_10D21():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10D21)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x9,
        (
            "#11PApparently with troublesome partners\x01",
            "You seem to meet each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PInformation station Alain Dorl ……\x01",
            "It seems to be horribly troublesome and young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIf it seems to be severe it will be a big help\x01",
            "Please do not hesitate to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PThat's right.\x01",
            "I owe it to wetlands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204FIf it seems to be out of hand\x01",
            "Come, please lend me your power.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 2220, 0, 4610, 90)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x40)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, 3840, 0, 4540, 270)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x40)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xC, -6000, 150, 43030, 180)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0x9, -5030, 0, 52190, 0)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x40)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, 1000, 0, 9000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 2)
    OP_29(0xAD, 0x1, 0x1)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_30_E8D6 end

    def Function_31_10F5F(): pass

    label("Function_31_10F5F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 3800, 0, 13900, 90)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 2900, 0, 15300, 135)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, 1600, 0, 14900, 135)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0xB, 2200, 0, 13700, 90)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, 2400, 0, 12600, 90)
    OP_4B(0xC, 0xFF)
    OP_68(4600, 1000, 13900, 0)
    MoveCamera(49, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_68(4600, 1000, 13900, 10000)
    MoveCamera(41, 23, 0, 10000)
    SetCameraDistance(18500, 10000)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(180, 20, -1, -1)
    SetChrName("McDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W── If so, ask the will of the independent,\x01",
            "Will the referendum be based on the referendum?\x02\x03",
            "No, the referendum vote\x01",
            "Whether to do \"representation of determination\"\x01",
            "It should have been only a question.\x02\x03",
            "Defense Forces and Crossbell Independent Countries ……\x02\x03",
            "Not to mention the legitimacy of the presidential system\x01",
            "There is never a thing to connect!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_10F5F end

    def Function_32_111D0(): pass

    label("Function_32_111D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3020, 1700, 4270, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22460, 0)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11351")
    SetChrPos(0x101, -2740, 0, -2360, 0)
    SetChrPos(0x104, -1610, 0, -2360, 0)
    SetChrPos(0x1A2, -2510, 0, -2560, 0)
    SetChrPos(0x102, -1940, 0, -2360, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1129C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1129C)

    def lambda_112AD():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_112AD)
    Sleep(50)

    def lambda_112CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_112CA)

    def lambda_112DB():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_112DB)
    Sleep(700)

    def lambda_112F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_112F8)

    def lambda_11309():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11309)
    Sleep(50)

    def lambda_11326():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_11326)

    def lambda_11337():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_11337)
    Jump("loc_115D2")

    label("loc_11351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11494")
    SetChrPos(0x101, -2740, 0, -2360, 0)
    SetChrPos(0x109, -1610, 0, -2360, 0)
    SetChrPos(0x1A2, -2510, 0, -2560, 0)
    SetChrPos(0x102, -1940, 0, -2360, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_113DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_113DF)

    def lambda_113F0():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_113F0)
    Sleep(50)

    def lambda_1140D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1140D)

    def lambda_1141E():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1141E)
    Sleep(700)

    def lambda_1143B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1143B)

    def lambda_1144C():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1144C)
    Sleep(50)

    def lambda_11469():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_11469)

    def lambda_1147A():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1147A)
    Jump("loc_115D2")

    label("loc_11494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_115D2")
    SetChrPos(0x101, -2740, 0, -2360, 0)
    SetChrPos(0x105, -1610, 0, -2360, 0)
    SetChrPos(0x1A2, -2510, 0, -2560, 0)
    SetChrPos(0x102, -1940, 0, -2360, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_11522():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11522)

    def lambda_11533():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11533)
    Sleep(50)

    def lambda_11550():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11550)

    def lambda_11561():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11561)
    Sleep(700)

    def lambda_1157E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1157E)

    def lambda_1158F():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1158F)
    Sleep(50)

    def lambda_115AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_115AC)

    def lambda_115BD():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_115BD)

    label("loc_115D2")

    OP_68(-2140, 1300, 5160, 3000)
    OP_6F(0x1)
    WaitChrThread(0x1A2, 1)

    ChrTalk(
        0x1A2,
        (
            "#12PThis is the Association of Shogi Shogi ·\x01",
            "Crossbell branch …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00005F… … Shin?\x01",
            "What happened with being hidden behind the shadows?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11683")

    def lambda_11663():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11663)
    Sleep(50)

    def lambda_11673():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11673)
    Sleep(300)
    Jump("loc_116DA")

    label("loc_11683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_116B1")

    def lambda_11691():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11691)
    Sleep(50)

    def lambda_116A1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_116A1)
    Sleep(300)
    Jump("loc_116DA")

    label("loc_116B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_116DA")

    def lambda_116BF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_116BF)
    Sleep(50)

    def lambda_116CF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_116CF)
    Sleep(300)

    label("loc_116DA")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#12PWow, it's noisy, is not it!\x02",
    )

    CloseMessageWindow()
    OP_64(0x1A2)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#N#04005FOh, you guys …\x01",
            "What happened with a cute boya?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_117C1")

    def lambda_11791():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11791)
    Sleep(50)

    def lambda_117A1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_117A1)
    Sleep(50)

    def lambda_117B1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_117B1)
    Sleep(300)
    Jump("loc_11838")

    label("loc_117C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_117FF")

    def lambda_117CF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_117CF)
    Sleep(50)

    def lambda_117DF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_117DF)
    Sleep(50)

    def lambda_117EF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_117EF)
    Sleep(300)
    Jump("loc_11838")

    label("loc_117FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11838")

    def lambda_1180D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1180D)
    Sleep(50)

    def lambda_1181D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1181D)
    Sleep(50)

    def lambda_1182D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1182D)
    Sleep(300)

    label("loc_11838")


    ChrTalk(
        0x8,
        (
            "#5P#N#04000FBecause it becomes an obstacle in such a place\x01",
            "Welcome to visit here.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00105FIs that … Yes.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(330, 1300, 10820, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21390, 0)
    OP_93(0x8, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11999")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x104, 1640, 0, 8800, 0)

    def lambda_11928():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_11928)
    Sleep(50)

    def lambda_11945():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11945)
    Sleep(50)

    def lambda_11962():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11962)
    Sleep(50)

    def lambda_1197F():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1197F)
    Jump("loc_11B1A")

    label("loc_11999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11A5C")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x109, 1640, 0, 8800, 0)

    def lambda_119EB():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_119EB)
    Sleep(50)

    def lambda_11A08():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11A08)
    Sleep(50)

    def lambda_11A25():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11A25)
    Sleep(50)

    def lambda_11A42():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11A42)
    Jump("loc_11B1A")

    label("loc_11A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11B1A")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x105, 1640, 0, 8800, 0)

    def lambda_11AAE():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_11AAE)
    Sleep(50)

    def lambda_11ACB():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11ACB)
    Sleep(50)

    def lambda_11AE8():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11AE8)
    Sleep(50)

    def lambda_11B05():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11B05)

    label("loc_11B1A")

    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x8,
        (
            "#04000F#5PSo, that boya\x01",
            "Who on earth are you?\x02\x03",
            "#04005FPerhaps,\x01",
            "Were you looking for a lost child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FWell, what do you say ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHey, you, you!\x01",
            "Is the \"sword of the wind\" now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004F#5POh, you have a lot of way of saying.\x02\x03",
            "#04000Fまあ、Ariosなら留守にしてるけど？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PWell, I guess … Hoo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04005F#5PWhy are you at ease?\x02\x03",
            "#04003FHmm, that idiot to that behavior ……\x02\x03",
            "#04000FI see--\x01",
            "This boya is a stakeholder in the \"black moon\".\x01",
            "I wonder if that is the grandson of the elder.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11D6A")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jump("loc_11E47")

    label("loc_11D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11DDB")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jump("loc_11E47")

    label("loc_11DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11E47")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_11E47")


    ChrTalk(
        0x102,
        "#12P#00105FWhy, why …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011F#5PUhufu, there is a beak curd\x01",
            "You seemed to have hit it perfectly.\x02\x03",
            "#04001FOh, by the way, Okama\x01",
            "You should not think that you put a bear?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11F5A")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_12037")

    label("loc_11F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11FCB")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_12037")

    label("loc_11FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_12037")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_12037")


    ChrTalk(
        0x101,
        "#12P#00012FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PCut, this look and its contents\x01",
            "It is not tadamono.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PBecause it is this\x01",
            "What is a guardsman …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006F#5PWell, rude from a little while ago\x01",
            "Practice saying too much.\x01",
            "This child is also wonderfully \"black moon\".\x02\x03",
            "#04008FSomething is terrible.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12166")

    ChrTalk(
        0x104,
        "#12P#00303FOh, I agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_121BF")

    label("loc_12166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12195")

    ChrTalk(
        0x109,
        "#12P#10106FYes, I agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_121BF")

    label("loc_12195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_121BF")

    ChrTalk(
        0x105,
        "#12P#10304FHuh, I agree.\x02",
    )

    CloseMessageWindow()

    label("loc_121BF")


    ChrTalk(
        0x8,
        (
            "#04000F#5PAnyway why\x01",
            "Ariosのことを\x01",
            "I wonder if I will be wary of that?\x02\x03",
            "Separately we also clearly said \"black moon\"\x01",
            "It's not hostile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PFun\x01",
            "Up to now the old man\x01",
            "Do not say good how long keep disturbing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PBecause of \"the wind sword\" or \"immobility\"\x01",
            "How much sarcophagi was suffered by the story -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005F\"Immovable\" … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004F#5PYeah, \"immovable\" Jin -\x02\x03",
            "#04000FIn A Republic's A gravel warrior\x01",
            "It is a guru of old martial art called \"Yu Dynasty\".\x02\x03",
            "Recently it is plain,\x01",
            "Also in this crossbell branch in the past\x01",
            "He came to help me several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FWhen saying \"Yotei flow\"\x01",
            "Surely Lin's … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000F#5PYeah, he's a sister of Rin.\x01",
            "Naturally the skill is tremendous.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_124B2")

    ChrTalk(
        0x104,
        (
            "#12P#00300FIndeed, to fossil\x01",
            "The guilds are gathered with actors as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1253D")

    label("loc_124B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_124FA")

    ChrTalk(
        0x109,
        (
            "#12P#10100FI see.\x01",
            "The guilds are also amazing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1253D")

    label("loc_124FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1253D")

    ChrTalk(
        0x105,
        (
            "#12P#10300FHoof, on a falling stone\x01",
            "The guilds have all the actors right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1253D")


    ChrTalk(
        0x1A2,
        (
            "#12PEven so,\x01",
            "The guild is really troublesome\x01",
            "That kick is the fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PI do not know anything about big clothes,\x01",
            "Let's say \"protect civilians\" as a vertical\x01",
            "All you want is going to be too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004F#5PHuhu, well, according to its principle,\x01",
            "Sometimes 'non-interference with state power'\x01",
            "That's not the limit.\x02\x03",
            "#04005F- Boya,\x01",
            "How far are you in Toshi?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000Fsurely……\x01",
            "I did not expect that to be honest up to here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHuhun, there is nothing to praise.\x01",
            "Anyway guild guys -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006F#5PYeah yeah, criticism of the guild is fine, though\x01",
            "Children are like children.\x02\x03",
            "#04000FSo, now on the second floor\x01",
            "KeyaちゃんとSuzukuちゃんがいるから。\x02\x03",
            "Try to talk with each other happily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FOh, that's right.\x01",
            "Keyaがお邪魔していましたね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FWell, here are kids\x01",
            "Shall I have a partner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PWhat … it is sagging, is not it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x153, 7)
    OP_29(0x73, 0x1, 0x5)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 800, 0, 8760, 0)
    EventEnd(0x5)
    Return()

    # Function_32_111D0 end

    def Function_33_128C4(): pass

    label("Function_33_128C4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1940, 1100, 44370, 0)
    MoveCamera(36, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20320, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1292E")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06000.itp")

    label("loc_1292E")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12988")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x104, -2190, 0, 45050, 90)
    Jump("loc_12A27")

    label("loc_12988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_129DA")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x109, -2190, 0, 45050, 90)
    Jump("loc_12A27")

    label("loc_129DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_12A27")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x105, -2190, 0, 45050, 90)

    label("loc_12A27")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_END)), "loc_12AC4")

    def lambda_12A36():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12A36)
    Sleep(50)

    def lambda_12A46():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_12A46)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#11P#01102FOh, Lloyd.\x01",
            "Well, how did you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FGood morning.\x01",
            "It looks like you are at work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C77")

    label("loc_12AC4")

    SetScenarioFlags(0x14D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xD,
        "#11P#01110FOh, Lloyd ourselves!\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#11P#06002FAh……\x01",
            "Hello everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000Fやあ、Keya。\x01",
            "It looks like you're having fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FSuzukuちゃんも久しぶりね。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0xE,
        (
            "ふふ、Long time no see.\x02\x03",
            "Apparently,\x01",
            "It looks like you are at work.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_12C77")


    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, for the time being\x01",
            "I wish I could say so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PWhat are they,.\x01",
            "Is it your serial?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#11P#01105Fthat~?\x01",
            "Who is that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11P#06005FA little boy ……?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6PWhat is a little boy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI am Shin!\x01",
            "\"Black moon\" as the grandson of the elder\x01",
            "It is a man who carries the future!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11P#06010FI'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01105FYeah, it's a bit small, but\x01",
            "It's the same adult as Lloyd's.\x02\x03",
            "#01109FEven so tiny\x01",
            "You are bothered, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#6PLet me tell you a bit small!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12F50")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x104, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#11P#00304FHahaha, if you hang on the key\x01",
            "Cheeky buddies are not pear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13089")

    label("loc_12F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12FE7")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#11P#10109FHaha ……\x01",
            "（さすがKeyaちゃん。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13089")

    label("loc_12FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_13089")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x105, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#11P#10309Fフフ、Keyaにかかったら\x01",
            "The black moon cape also has no form.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13089")

    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00109FHuh, Shin.\x02\x03",
            "こちらはKeyaちゃんに\x01",
            "Suzukuちゃんていうの。\x02\x03",
            "#00100FBoth of us, a little less than Shin\x01",
            "I wonder if you become a sister?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000Fあ、ちなみにSuzukuちゃんは\x01",
            "さっき言っていたAriosさんの\x01",
            "You are going to be a daughter.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6POr, \"Wind sword of the wind\" … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PAnd, as I thought,\x01",
            "Are you swept away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PPerhaps I am holding my eyes closed.\x01",
            "For training \"Shinkan\" or so! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_132A2")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1334F")

    label("loc_132A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_132FB")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1334F")

    label("loc_132FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1334F")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_1334F")


    ChrTalk(
        0xD,
        "#11P#01105FShinkan\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005F\"My mind\" ……\x01",
            "Well I know such words well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FHaha ……\x01",
            "Uh, I can not see my eyes.\x02\x03",
            "Thanks to you, my ears are nice.\x01",
            "Is not it amazing like a father?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6PWell, that was rude!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PDoing something that gentlemen have … …\x01",
            "Please forgive me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11P#06002FHuh, I did not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005F(Oh … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102F(Hehe, after all\x01",
            "Roots seem to be good girls. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 0)
    OP_29(0x73, 0x1, 0x6)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0xB4, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -2720, 0, 44250, 90)
    EventEnd(0x5)
    Return()

    # Function_33_128C4 end

    def Function_34_13558(): pass

    label("Function_34_13558")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06000.itp")
    OP_68(-1940, 1100, 44370, 0)
    MoveCamera(36, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -2200, 0, 45100, 90)
    SetChrPos(0x102, -2200, 0, 43900, 90)
    SetChrPos(0x104, -3400, 0, 45300, 90)
    SetChrPos(0x109, -3400, 0, 43700, 90)
    SetChrPos(0x105, -4600, 0, 44500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4B(0xD, 0xFF)
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xD, 0x10E, 0x1F4)

    ChrTalk(
        0xD,
        "#11P#01110FOh, Lloyd ourselves!\x02",
    )

    CloseMessageWindow()
    OP_4B(0xE, 0xFF)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x10E, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#11P#06002FAh……\x01",
            "Hello everybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000Fやあ、Keya。\x01",
            "It looks like you're having fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FSuzukuちゃんも久しぶりね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11P#06000Fふふ、Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FOh, this girl\x01",
            "Daughter of \"Wind sword of the wind\"?\x02\x03",
            "#10309FHuff, as you heard\x01",
            "Is not she a cute girl?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_139BA")

    ChrTalk(
        0x109,
        "#6P#10109FRight, as you said, right?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#11P#06005FThis voice is certain ……\x01",
            "Is not Noel, is not it?\x02\x03",
            "#06002FPresent to your father before\x01",
            "I searched for it together.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#6P#10105FWow, you remembered it?\x02\x03",
            "#10109FEven though I only met a little ……\x01",
            "Huh, I'm glad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002Fえへへ、Keyaちゃんに\x01",
            "A new member entered\x01",
            "I heard it.\x02\x03",
            "#06000FWell then … Who's there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FIt is Wadi Hemisphere.\x01",
            "Huh, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B97")

    label("loc_139BA")


    ChrTalk(
        0x109,
        "#6P#10109FYeah, it was exactly what Fran was saying!\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#11P#06005FEr … … Who's there?\x02\x03",
            "Keyaちゃんに新しいメンバーが\x01",
            "I heard that I entered,\x01",
            "Did you mean ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FOh, that was your first time.\x02\x03",
            "#10109FI'm Noel Seeker.\x01",
            "If you say Franc's older sister\x01",
            "Do you understand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06005FOh, Fran's … …\x01",
            "By the way, the atmosphere is somewhat\x01",
            "I feel like they are similar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FI am Wadi Hemisphere.\x01",
            "Huh, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B97")


    ChrTalk(
        0xE,
        (
            "#11P#06002FYes, this is it.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01109Fほらほら、Suzukuも\x01",
            "I have to introduce myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06005FAh……\x01",
            "That's right, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0xE,
        (
            "えっと、Keyaちゃんのお友達の\x01",
            "Suzuku・マクレインって言います。\x02\x03",
            "To all of the support department, both fathers\x01",
            "I am taking care of me.\x02\x03",
            "Again, thank you.\x02",
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
        0x102,
        (
            "#6P#00102FHaha, well …\x01",
            "Ariosさんにお世話になってるのは\x01",
            "Rather, it is a person of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FWell, I can not say that … …\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#11P#06010FWell, that's not true.\x02\x03",
            "At the time of the previous incident, to everyone\x01",
            "I had a lot of help … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FAs usual\x01",
            "It is a solid child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01102FNe, everyone too\x01",
            "Keyaたちと遊んでくのー？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FAh, no way,\x01",
            "Suzukuちゃんが来てるから\x01",
            "Please do not hesitate to ask me a greeting.\x02\x03",
            "#00000FBecause we go to work as it is,\x01",
            "今日一日、KeyaはSuzukuちゃんと\x01",
            "Please enjoy slowly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11P#01109FYeah, I know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FEr, everyone too\x01",
            "Please do your best at work.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x14D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0xD, 0xE, 0)
    TurnDirection(0xE, 0xD, 0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -2200, 50, 44500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_34_13558 end

    def Function_35_1403C(): pass

    label("Function_35_1403C")

    EventBegin(0x1)
    SetChrPos(0x0, -2110, 0, 740, 0)
    EventEnd(0x4)
    Return()

    # Function_35_1403C end

    SaveToFile()

Try(main)
