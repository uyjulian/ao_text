from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Receptionist Michel",    # 1
        "Bracer Scott",           # 2
        "Bracer Wenzel",          # 3
        "Bracer Ling",            # 4
        "Bracer Eolia",           # 5
        "KeA",                    # 6
        "Shizuku",                # 7
        "Zeit",                   # 8
        "Arios",                  # 9
        "Kilika",                 # 10
        "Chair",                  # 11
        "Chair",                  # 12
        "Chair",                  # 13
        "Chair",                  # 14
        "Chair",                  # 15
        "Chair",                  # 16
        "Chair",                  # 17
        "Chair",                  # 18
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
        "Function_5_4C30",         # 05, 5
        "Function_6_53F8",         # 06, 6
        "Function_7_5769",         # 07, 7
        "Function_8_5929",         # 08, 8
        "Function_9_62C3",         # 09, 9
        "Function_10_6923",        # 0A, 10
        "Function_11_725A",        # 0B, 11
        "Function_12_77BB",        # 0C, 12
        "Function_13_783D",        # 0D, 13
        "Function_14_7943",        # 0E, 14
        "Function_15_855F",        # 0F, 15
        "Function_16_8622",        # 10, 16
        "Function_17_8B0C",        # 11, 17
        "Function_18_8CE1",        # 12, 18
        "Function_19_8F98",        # 13, 19
        "Function_20_8F9F",        # 14, 20
        "Function_21_99AC",        # 15, 21
        "Function_22_9DB0",        # 16, 22
        "Function_23_A70D",        # 17, 23
        "Function_24_B06B",        # 18, 24
        "Function_25_BDE6",        # 19, 25
        "Function_26_C34C",        # 1A, 26
        "Function_27_C396",        # 1B, 27
        "Function_28_E2D6",        # 1C, 28
        "Function_29_EE3F",        # 1D, 29
        "Function_30_F659",        # 1E, 30
        "Function_31_11FD2",       # 1F, 31
        "Function_32_122A4",       # 20, 32
        "Function_33_13A93",       # 21, 33
        "Function_34_1476D",       # 22, 34
        "Function_35_15220",       # 23, 35
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DD")
    Jump("loc_AC7")

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F0")
    Jump("loc_AC7")

    label("loc_9F0")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "#04000FOh yeah, I started\x01",
            "playing that "Pom!" orbal\x01",
            "game the other day.\x02\x03",
            "#04011FYou guys wanna go? Haha,\x01",
            "if you're free, let's\x01",
            "have a match㈱\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "[Michel's Account]\x07\x00\x01",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 5)
    OP_E4(0x3)
    TalkEnd(0x8)
    Return()

    label("loc_AC7")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA9")

    ChrTalk(
        0x8,
        (
            "#04001FI see... So you defeated\x01",
            "Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F...Yes, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FBut he really is\x01",
            "tremendously strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003F...Arios is a genuine master of "reason."\x02\x03",
            "What's more, he did not get to where he is\x01",
            "today merely through talent... His strength\x01",
            "was obtained through extraordinary training.\x02\x03",
            "#04011FHaha. If you all overcame him, then you've\x01",
            "gotten much stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FTo be honest, I think it\x01",
            "was just luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt was a hard fight,\x01",
            "but... We finally\x01",
            "managed to overtake him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FHaha. Then all that's left is\x01",
            "that KeA kid, right?\x02\x03",
            "#04000FShizuku's waiting too, so please,\x01",
            "do whatever you need to bring\x01",
            "both Arios and KeA back with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, of course!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 6)
    Jump("loc_F42")

    label("loc_DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA1")

    ChrTalk(
        0x8,
        (
            "#04003FArios is a genuine master of\x01",
            ""reason."\x02\x03",
            "#04011FHaha. If you all overcame him,\x01",
            "then you've gotten much stronger.\x02\x03",
            "#04000FShizuku's waiting too, so please,\x01",
            "do whatever you need to bring\x01",
            "both Arios and KeA back with you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F42")

    label("loc_EA1")


    ChrTalk(
        0x8,
        (
            "#04004FHaha. All that's left is to take\x01",
            "back KeA.\x02\x03",
            "#04000FShizuku's waiting too, so please,\x01",
            "do whatever you need to bring\x01",
            "both Arios and KeA back with you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F42")

    Jump("loc_4C2C")

    label("loc_F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1507")

    ChrTalk(
        0x8,
        (
            "#04000FOh, it's you guys...\x01",
            "Good work arresting the\x01",
            "President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe'd like to thank the\x01",
            "guild for their\x01",
            "cooperation, too.\x02\x03",
            "Without everyone's help,\x01",
            "I don't think it would\x01",
            "have been possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FUhuhu, don't worry about\x01",
            "it.\x02\x03",
            "#04004FAnd don't worry about the\x01",
            "city. We'll do something\x01",
            "about it on our end.\x02\x03",
            "#04000FBecause of that, we'll be\x01",
            "able to restart guild\x01",
            "activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FNow that you mention it,\x01",
            "the guild members are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYes. Ever since the barrier was\x01",
            "released, they split up and went to\x01",
            "the outskirts of Crossbell.\x02\x03",
            "#04003FBecause we were unable to leave for a\x01",
            "while, problems happened everywhere\x01",
            "and now we're drowning in requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FThat... sounds tough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWe'd really like to help\x01",
            "you guys, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FPlease, leave everything to us.\x02\x03",
            "#04001FInstead, that strange Huge Tree\x01",
            "that appeared in the marshlands...\x01",
            "You guys handle that.\x02\x03",
            "That's the perfect way to divide\x01",
            "our duties right now. Don't you\x01",
            "agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes... You're right.\x02\x03",
            "KeA is there... And Arios\x01",
            "as well.\x02\x03",
            "#00001FWith our own hands, we'll\x01",
            "do whatever we have to to\x01",
            "bring them back!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13EF")

    ChrTalk(
        0x10A,
        "#00603F...Naturally.\x02",
    )

    CloseMessageWindow()

    label("loc_13EF")


    ChrTalk(
        0x8,
        (
            "#04004FUhuhu, that's why you guys\x01",
            "are who you are.\x02\x03",
            "#04001FHonestly speaking, Arios'\x01",
            "power is in a whole other\x01",
            "league.\x02\x03",
            "But being in the same field\x01",
            "as we are, I'm sure you know\x01",
            "that better than anyone.\x02\x03",
            "#04011FGo all out, Special Support\x01",
            "Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FRight!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 5)
    Jump("loc_177C")

    label("loc_1507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1696")

    ChrTalk(
        0x8,
        (
            "#04003FHonestly speaking, Arios' power is in a\x01",
            "whole other league.\x02\x03",
            "#04001FBut being in the same field as we are,\x01",
            "I'm sure you know that better than\x01",
            "anyone.\x02\x03",
            "Though I'm sure a hard fight is waiting\x01",
            "for you, please, do whatever you must to\x01",
            "bring both him and KeA back with you.\x02\x03",
            "#04011FHaha. As punishment for handing in his\x01",
            "resignation, I'll have to give him a\x01",
            "stern lecture.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_177C")

    label("loc_1696")


    ChrTalk(
        0x8,
        (
            "#04003FThough I'm sure a hard fight is waiting\x01",
            "for you, please, do whatever you must to\x01",
            "bring both him and KeA back with you.\x02\x03",
            "#04011FHaha. As punishment for handing in his\x01",
            "resignation, I'll have to give him a\x01",
            "stern lecture.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177C")

    Jump("loc_4C2C")

    label("loc_1781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195A")

    ChrTalk(
        0x8,
        (
            "#04006FEver since the declaration of independence, we\x01",
            "haven't been able to act freely.\x02\x03",
            "Although the guild is supposed to remain\x01",
            "neutral, we can't act, disregarding the order\x01",
            "of the independent state that is being created.\x02\x03",
            "#04001FHowever, this time is different. Now that\x01",
            "citizens are exposed to danger, the guild\x01",
            "cannot abandon them.\x02\x03",
            "#04003FThe invasion of Orchis Tower and the arrest of\x01",
            "the President... Allow us to help you once\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19D5")

    label("loc_195A")


    ChrTalk(
        0x8,
        (
            "#04003FPlease contact me when\x01",
            "it's time to begin the\x01",
            "operation.\x02\x03",
            "#04001FUntil then, we'll be\x01",
            "preparing to assist you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D5")

    Jump("loc_4C2C")

    label("loc_19DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1BC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF3")

    ChrTalk(
        0x8,
        (
            "#04006F*sigh*. I can't believe Arios\x01",
            "falsified his schedule to meet with\x01",
            "the mayor... no, the President.\x02\x03",
            "Even though I thought it was\x01",
            "unnatural, I completely missed it.\x02\x03",
            "#04008FI wonder if he's been hung up on\x01",
            "Shizuku's accident this whole\x01",
            "time...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BC1")

    label("loc_1AF3")


    ChrTalk(
        0x8,
        (
            "#04003FAnyway... Now that independence\x01",
            "has been proposed, we at the guild\x01",
            "have to think about how we'll deal\x01",
            "with it from a neutral standpoint.\x02\x03",
            "#04008FWe've got to contact Bracer HQ\x01",
            "about this too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC1")

    Jump("loc_4C2C")

    label("loc_1BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_END)), "loc_22C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_END)), "loc_1E41")

    ChrTalk(
        0x8,
        (
            "#04005FAh, it's you guys...\x01",
            "Have you seen Arios?\x02\x03",
            "#04006FHmm, he's still not back\x01",
            "yet...\x02",
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
            "#00005FIf you're looking for\x01",
            "Arios, we just saw him\x01",
            "at the cemetery.\x02\x03",
            "We told him you're\x01",
            "looking for him, but...\x01",
            "He's still not back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FYes, he's still not back... I\x01",
            "see, so he went to the cemetery.\x02\x03",
            "#04000F...Well, it's not rare for him\x01",
            "to visit Saya's grave. I suspect\x01",
            "he'll be back before long.\x02\x03",
            "#04011FSorry for bothering you. We'll\x01",
            "be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-Is that so. Excuse us,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F0")

    label("loc_1E41")


    ChrTalk(
        0x8,
        (
            "#04005FAh, you guys... I'd like\x01",
            "to ask you a little\x01",
            "something.\x02\x03",
            "#04001FHave you seen Arios\x01",
            "anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHuh? If you're looking\x01",
            "for Arios, we just saw\x01",
            "him at the cemetery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FIt looked like he was\x01",
            "visiting his wife's grave.\x01",
            "...Did you need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYes. He's supposed to go to Orchis Tower for\x01",
            "a discussion with the mayor on the guild's\x01",
            "stance.\x02\x03",
            "#04006FArios broke his ENIGMA Ⅱ during the attack\x01",
            "the other day.\x02\x03",
            "Because we've been busy dealing with the\x01",
            "incident, I haven't had time to ready a spare\x01",
            "for him, so contacting him is difficult.\x02\x03",
            "#04008FHis discussion should be finished around now,\x01",
            "and I'd like him to return already, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FAh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FBut, I see... Arios went to\x01",
            "the cemetery.\x02\x03",
            "#04000FWell, it's not rare for him to\x01",
            "visit Saya's grave. I suspect\x01",
            "he'll be back before long.\x02\x03",
            "#04011FSorry for bothering you. We'll\x01",
            "be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-Is that so. Excuse us,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F0")

    SetScenarioFlags(0x18E, 0)
    Jump("loc_22BD")

    label("loc_21F8")


    ChrTalk(
        0x8,
        (
            "#04008FBecause Crossbell is like this, we\x01",
            "haven't had time to deal with marshlands\x01",
            "Pleroma Flowers or Ouroboros.\x02\x03",
            "#04006F*sigh*. Maybe I should make a request\x01",
            "for reinforcements to Bracer HQ.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22BD")

    Jump("loc_4C2C")

    label("loc_22C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_27D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E9")

    ChrTalk(
        0x8,
        (
            "#04005FAh, you guys... I'd like\x01",
            "to ask you a little\x01",
            "something.\x02\x03",
            "#04001FHave you seen Arios\x01",
            "anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FNo, we haven't seen him\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FDid something happen to\x01",
            "Arios?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYes. He's supposed to go to Orchis Tower for\x01",
            "a discussion with the mayor on the guild's\x01",
            "stance.\x02\x03",
            "#04006FArios broke his ENIGMA Ⅱ during the attack\x01",
            "the other day.\x02\x03",
            "Because we've been busy dealing with the\x01",
            "incident, I haven't had time to ready a spare\x01",
            "for him, so contacting him is difficult.\x02\x03",
            "#04008FHis discussion should be finished around now,\x01",
            "and I'd like him to return already, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm. Maybe he took a\x01",
            "detour on the way back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe understand. We'll\x01",
            "speak to Arios if we see\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FThanks for doing that\x01",
            "for me. I'll be counting\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 7)
    Jump("loc_27D3")

    label("loc_25E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270E")

    ChrTalk(
        0x8,
        (
            "#04003FBecause Crossbell is like this, the\x01",
            "guild is very busy right now.\x02\x03",
            "#04008FWe haven't had time to deal with the\x01",
            "Pleroma Flowers in the Marshlands or\x01",
            "Ouroboros' invasion of Crossbell...\x02\x03",
            "#04006F*sigh*. Maybe I should make a\x01",
            "request for reinforcements to Bracer\x01",
            "HQ.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27D3")

    label("loc_270E")


    ChrTalk(
        0x8,
        (
            "#04008FBecause Crossbell is like this, we\x01",
            "haven't had time to deal with marshlands\x01",
            "Pleroma Flowers or Ouroboros.\x02\x03",
            "#04006F*sigh*. Maybe I should make a request\x01",
            "for reinforcements to Bracer HQ.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D3")

    Jump("loc_4C2C")

    label("loc_27D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F7")
    TalkEnd(0x8)
    Call(0, 23)
    Return()

    label("loc_27F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294E")

    ChrTalk(
        0x8,
        (
            "#04001FIf this situation goes on for too\x01",
            "much longer, the guild will have no\x01",
            "choice but to act.\x02\x03",
            "#04003FBut, though the major powers\x01",
            "ridiculed the CGF before, this will\x01",
            "give them even more material.\x02\x03",
            "#04001FIf possible, I'd like to be the final\x01",
            "option... But when civilian lives are\x01",
            "on the line, we can't wait too long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A2C")

    label("loc_294E")


    ChrTalk(
        0x8,
        (
            "#04001FIf this situation goes on for too\x01",
            "much longer, the guild will have no\x01",
            "choice but to act.\x02\x03",
            "#04006FIf possible, I'd like to be the final\x01",
            "option... But when civilian lives are\x01",
            "on the line, we can't wait too long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2C")

    Jump("loc_4C2C")

    label("loc_2A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_2BEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B3C")

    ChrTalk(
        0x8,
        (
            "#04003FBoth Ling and Eolia are capable\x01",
            "bracers who are nearly A-rank.\x02\x03",
            "#04008FTo think both of them were captured\x01",
            "in a place like the marshlands\x01",
            "without contacting us...\x02\x03",
            "#04001FI don't know what's there. Please,\x01",
            "be extremely careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BE5")

    label("loc_2B3C")


    ChrTalk(
        0x8,
        (
            "#04008FTo think Ling & Eolia were captured\x01",
            "in a place like the marshlands\x01",
            "without contacting us...\x02\x03",
            "#04001FI don't know what's there. Please,\x01",
            "be extremely careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BE5")

    Jump("loc_4C2C")

    label("loc_2BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_END)), "loc_2D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D55")

    ChrTalk(
        0x8,
        (
            "#04005FAh, you all... Did you\x01",
            "learn Ling & Eolia's\x01",
            "location?\x02\x03",
            "You said you were going\x01",
            "to use the ENIGMA Ⅱ's\x01",
            "alert function.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThere are a lot of steps\x01",
            "in the procedure, but we\x01",
            "should be able to manage.\x02\x03",
            "We'll give you the results\x01",
            "shortly, so please wait a\x01",
            "while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FYes, understood. I'm\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D8F")

    label("loc_2D55")


    ChrTalk(
        0x8,
        (
            "#04011FPlease, find Ling &\x01",
            "Eolia's location\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D8F")

    Jump("loc_4C2C")

    label("loc_2D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E34")

    ChrTalk(
        0x8,
        (
            "#04003FIf you learn anything\x01",
            "about them, please\x01",
            "contact me immediately.\x02\x03",
            "#04001FI'll recall Arios and\x01",
            "the others depending on\x01",
            "the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C2C")

    label("loc_2E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3094")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FDB")

    ChrTalk(
        0x8,
        (
            "#04007FA communication just came in...\x01",
            "A derailment!?\x02\x03",
            "#04006FHmm, this is troubling. Arios\x01",
            "and the others can't return from\x01",
            "their cryptid investigation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, that investigation's\x01",
            "important... Please,\x01",
            "leave this to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FOoh... But I suppose I have no\x01",
            "choice.\x02\x03",
            "#04000FI understand. You guys will handle\x01",
            "the derailment. If there's any\x01",
            "problem, let me know immediately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_308F")

    label("loc_2FDB")


    ChrTalk(
        0x8,
        (
            "#04006FArios and the others can't\x01",
            "return from the cryptid\x01",
            "investigation immediately.\x02\x03",
            "#04000FI'm leaving the derailment to\x01",
            "you, so contact me immediately\x01",
            "if anything happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308F")

    Jump("loc_4C2C")

    label("loc_3094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3545")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3494")

    ChrTalk(
        0x8,
        (
            "#04003FThose "Pleroma Flowers" in your\x01",
            "report... To think they're linked\x01",
            "to the Church's Testaments.\x02\x03",
            "#04001FJust to be extra careful, I had\x01",
            "Scott and Ling confirm the\x01",
            "information, but...\x02\x03",
            "Up until now, it seems those\x01",
            "cryptids have been appearing near\x01",
            "to where those blue flowers bloom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThough it's unknown whether the\x01",
            "blooming of the blue flowers is\x01",
            "the root cause...\x02\x03",
            "#00200FIf you analyze the situation, it\x01",
            "appears they have something to do\x01",
            "with appearance of the cryptids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FBy the way, how is your\x01",
            "investigation into that\x01",
            "going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FFor now, we've eliminated two of the\x01",
            "three cryptids that appeared\x01",
            "yesterday.\x02\x03",
            "#04000FAs for today, after we defeat the\x01",
            "remaining one, we'll split up and\x01",
            "re-examine the places they appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, we don't know when\x01",
            "those cryptids will appear\x01",
            "again. Be plenty careful, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FYes, of course.\x02\x03",
            "#04000FI'll contact you if we learn\x01",
            "anything, so please continue\x01",
            "your investigation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16F, 3)
    Jump("loc_3540")

    label("loc_3494")


    ChrTalk(
        0x8,
        (
            "#04000FArios is back today, so\x01",
            "we'll take care of our part\x01",
            "of the investigation.\x02\x03",
            "#04011FI'll contact you if we learn\x01",
            "anything, so please continue\x01",
            "your investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3540")

    Jump("loc_4C2C")

    label("loc_3545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_377D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3701")

    ChrTalk(
        0x8,
        (
            "#04000FI'm counting on you guys\x01",
            "to handle the Cryptids\x01",
            "case.\x02\x03",
            "#04006FBecause Arios is unable\x01",
            "to act right now, we're\x01",
            "shorthanded.\x02\x03",
            "#04000FPlease handle Scott and\x01",
            "the others' share of the\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, please leave it to\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FArios can't act because\x01",
            "of Shizuku... I suppose\x01",
            "that can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FThank you for saying so.\x02\x03",
            "#04000FPlease, continue the\x01",
            "investigation in your\x01",
            "own way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3778")

    label("loc_3701")


    ChrTalk(
        0x8,
        (
            "#04000FI'm counting on you guys\x01",
            "to handle the Cryptids\x01",
            "case.\x02\x03",
            "Please, continue the\x01",
            "investigation in your\x01",
            "own way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3778")

    Jump("loc_4C2C")

    label("loc_377D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3AE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A10")

    ChrTalk(
        0x8,
        (
            "#04000FArios will be on security\x01",
            "detail today throughout the\x01",
            "main session.\x02\x03",
            "Out of concern for the heads\x01",
            "of state, I can't think of a\x01",
            "better security organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn a situation like this,\x01",
            "it's reassuring to have the\x01",
            "neutral bracers behind us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes. One can't be trusted with\x01",
            "such a great responsibility\x01",
            "through strength alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FHowever, even though he's Arios,\x01",
            "he can't protect the heads of\x01",
            "state from terrorists alone.\x02\x03",
            "#04000FCooperation of the police and CGF\x01",
            "are absolutely necessary. Please\x01",
            "do your best to support him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. We'll secure the\x01",
            "conference without\x01",
            "losing focus.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3ADC")

    label("loc_3A10")


    ChrTalk(
        0x8,
        (
            "#04005FAh, that's right. Come to\x01",
            "think of it... Now that Tio's\x01",
            "back, Eolia will be overjoyed.\x02\x03",
            "#04011FHaha. Be sure to say hi to her\x01",
            "at the conference for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...Well, if I feel like\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADC")

    Jump("loc_4C2C")

    label("loc_3AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F4A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3C62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B15")
    Call(0, 13)
    Jump("loc_3BD1")

    label("loc_3B15")


    ChrTalk(
        0x8,
        (
            "#04000FI heard from Arios.\x02\x03",
            "Because the Crossbell Guild has\x01",
            "connections even abroad, we'll\x01",
            "gather a certain level of goods.\x02\x03",
            "Well, I'm sure it'll be all\x01",
            "right, so please don't worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD1")

    Jump("loc_3C5E")

    label("loc_3BD6")


    ChrTalk(
        0x8,
        (
            "#04000FI heard from Arios\x01",
            "earlier. It seems the\x01",
            "patient was saved.\x02\x03",
            "Haha. It's great that\x01",
            "the archduke recognized\x01",
            "you all as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C5E")

    TalkEnd(0x8)
    Return()

    label("loc_3C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E93")

    ChrTalk(
        0x8,
        (
            "#04000FSo, the trade conference\x01",
            "has finally started.\x02\x03",
            "#04003FIt'll be hard for us to\x01",
            "remain alert and handle\x01",
            "everyone's requests.\x02\x03",
            "#04000FIf anything happens, the\x01",
            "bracers will be there\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat'll be a big help.\x02\x03",
            "#00103FWe don't know whether Red\x01",
            "Constellation or Heiyue will act,\x01",
            "but we can't let our guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FYes. Our opponents being who\x01",
            "they are, we'll need to pay\x01",
            "careful attention to them.\x02\x03",
            "#04000FAnyway, we'll let you know\x01",
            "as soon as we learn\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks. We're counting\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3F45")

    label("loc_3E93")


    ChrTalk(
        0x8,
        (
            "#04000FIt'll be hard for us to remain\x01",
            "alert and handle everyone's\x01",
            "requests.\x02\x03",
            "As soon as we learn anything about\x01",
            "Red Constellation or Heiyue, we'll\x01",
            "let you know immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F45")

    Jump("loc_4C2C")

    label("loc_3F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4573")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FFB")

    ChrTalk(
        0x8,
        (
            "#04006F*sigh*, but even so,\x01",
            "he's the Heiyue elder's\x01",
            "grandson.\x02\x03",
            "#04000FI'm not sure how to say\x01",
            "this, but it's an\x01",
            "ominous sign.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_3FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4099")

    ChrTalk(
        0x8,
        (
            "#04000FIf you're looking for\x01",
            "KeA, she's playing with\x01",
            "Shizuku on 2F.\x02\x03",
            "#04011FI'll look after them\x01",
            "properly, so there's no\x01",
            "need to worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_4099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C2")

    ChrTalk(
        0x8,
        (
            "#04000FAh, you guys. If you're\x01",
            "looking for KeA, she's\x01",
            "playing on 2F with Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FThanks for taking care of\x01",
            "her. You must be busy,\x01",
            "here at the guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FNo, she's totally welcome. It's\x01",
            "been busy lately and this is a nice\x01",
            "change of pace.\x02\x03",
            "#04009FAnd whenever I look at them, it\x01",
            "tickles my maternal instinct, as if\x01",
            "they were my very own daughters~㈱\x02",
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
        (
            "#00306FM-Maternal instincts,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04001F...What, is there a\x01",
            "problem with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FU-Umm... Come to think\x01",
            "of it, where is Arios?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYeah, as soon as he takes Shizuku back to\x01",
            "the hospital, he's headed for the Republic.\x02\x03",
            "#04004FHis requests for before the trade conference\x01",
            "are finished, so he's going to investigate\x01",
            "insecure components in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F*sigh*, that's so much\x01",
            "work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FFor now then, it seems\x01",
            "the guild is fully\x01",
            "prepared for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FHaha. You all should get\x01",
            "ready too, before the\x01",
            "day is out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 5)
    Jump("loc_456E")

    label("loc_44C2")


    ChrTalk(
        0x8,
        (
            "#04000FIf you're looking for KeA, she's\x01",
            "playing with Shizuku on 2F.\x02\x03",
            "#04011FPlease leave those kids to me.\x01",
            "I'll look after them until Arios\x01",
            "returns from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_456E")

    Jump("loc_4C2C")

    label("loc_4573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F5")

    ChrTalk(
        0x8,
        (
            "#04000FWe've been getting steadily\x01",
            "more requests via the orbal net\x01",
            "lately.\x02\x03",
            "Especially on rainy days like\x01",
            "today, we get a lot of requests\x01",
            "through the terminal.\x02\x03",
            "#04006FIt's just that, we're very\x01",
            "busy, and so we have to reject\x01",
            "the lowest priority requests.\x02\x03",
            "#04000FThere are times we send them to\x01",
            "the Support Section... Please\x01",
            "try to handle them somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_47C8")

    label("loc_46F5")


    ChrTalk(
        0x8,
        (
            "#04006FI'd like to handle as many\x01",
            "requests as possible, but we're\x01",
            "busy, so we have to be selective.\x02\x03",
            "#04000FThere are times we send our\x01",
            "overflow to the Support Section...\x01",
            "Please try to handle them somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47C8")

    Jump("loc_4C2C")

    label("loc_47CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B94")

    ChrTalk(
        0x8,
        (
            "#04000FBy the way, once Arios gets back\x01",
            "from Altair, he's going to\x01",
            "Remiferia immediately.\x02\x03",
            "Because the archduke is coming to\x01",
            "next month's trade conference,\x01",
            "he'll be helping prepare for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FArios is very busy,\x01",
            "isn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FYeah, and it's not just\x01",
            "Arios...\x02\x03",
            "#04000FIt's certain that everyone's\x01",
            "gotten busy preparing for\x01",
            "the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FRight. The CGF is busy with\x01",
            "staff reassignments and\x01",
            "rehabilitation training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha. So I guess the\x01",
            "guild's labor shortage\x01",
            "is acute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FHmm. I suppose the hole Estelle\x01",
            "and Joshua left was bigger than\x01",
            "I thought.\x02\x03",
            "#04008FOur workload has increased. No\x01",
            "matter how able you say Arios\x01",
            "and Scott are, there's a limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIndeed... You could\x01",
            "certainly say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FWell, we'll be busy\x01",
            "going forward, and it\x01",
            "could get even worse.\x02\x03",
            "#04011FHaha, thanks for\x01",
            "everything that you're\x01",
            "doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, same here. Let's\x01",
            "each do our best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 5)
    Jump("loc_4C2C")

    label("loc_4B94")


    ChrTalk(
        0x8,
        (
            "#04003FWith the month-end trade\x01",
            "conference, we'll be\x01",
            "busy from here on out.\x02\x03",
            "#04011FIt could get even worse.\x01",
            "Thanks for everything\x01",
            "that you doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C2C")

    TalkEnd(0x8)
    Return()

    # Function_4_993 end

    def Function_5_4C30(): pass

    label("Function_5_4C30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C4E")
    Call(0, 6)
    Jump("loc_4CFF")

    label("loc_4C4E")


    ChrTalk(
        0xFE,
        (
            "Fighting back-to-back with my\x01",
            "idol Kilika... For me, there\x01",
            "could be no better experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to protect Crossbell\x01",
            "going forward, I've gotta\x01",
            "refine my own Taito.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CFF")

    Jump("loc_53F4")

    label("loc_4D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4E57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DD9")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, when I\x01",
            "was patrolling the city for\x01",
            "people that couldn't escape...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I felt a familiar\x01",
            "presence. Could it be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, it couldn't be.\x01",
            "Sorry, forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E52")

    label("loc_4DD9")


    ChrTalk(
        0xFE,
        (
            "I felt a familiar\x01",
            "presence while patrolling\x01",
            "the city. Could it be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, it couldn't be.\x01",
            "Sorry, forget it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E52")

    Jump("loc_53F4")

    label("loc_4E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4EE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E72")
    Call(0, 7)
    Jump("loc_4EE2")

    label("loc_4E72")


    ChrTalk(
        0xFE,
        (
            "You guys... If it seems\x01",
            "tough, I'll assist you.\x01",
            "Just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the guild, we'll do\x01",
            "all we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EE2")

    Jump("loc_53F4")

    label("loc_4EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4EF5")
    Jump("loc_53F4")

    label("loc_4EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4FBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F14")
    TalkEnd(0xFE)
    Call(0, 23)
    Return()

    label("loc_4F14")


    ChrTalk(
        0xFE,
        (
            "We plan to stand by at\x01",
            "the guild for a while and\x01",
            "survey the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's just, the situation\x01",
            "isn't good at all... Maybe we\x01",
            "should get ready to attack.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53F4")

    label("loc_4FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4FCB")
    Jump("loc_53F4")

    label("loc_4FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4FD9")
    Jump("loc_53F4")

    label("loc_4FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4FE7")
    Jump("loc_53F4")

    label("loc_4FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4FF5")
    Jump("loc_53F4")

    label("loc_4FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_526B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51EB")

    ChrTalk(
        0xFE,
        (
            "Looks like Kilika went\x01",
            "to Orchis Tower as the\x01",
            "President's aide...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSay, Ling. Do you know\x01",
            "Kilika?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, she's a master of\x01",
            "the "Taito Style". She was\x01",
            "my senior in training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A few years back, she lost her\x01",
            "father and worked for a while in\x01",
            "Liberl as guild receptionist, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who would have thought she'd join\x01",
            "the intelligence agency under direct\x01",
            "supervision of the President?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, she's\x01",
            "complicated. Maybe I\x01",
            "should worry about her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 7)
    Jump("loc_5266")

    label("loc_51EB")


    ChrTalk(
        0xFE,
        (
            "Kilika will be working\x01",
            "at the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, she's\x01",
            "complicated. Maybe I\x01",
            "should worry about her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5266")

    Jump("loc_53F4")

    label("loc_526B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5279")
    Jump("loc_53F4")

    label("loc_5279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5287")
    Jump("loc_53F4")

    label("loc_5287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5295")
    Jump("loc_53F4")

    label("loc_5295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_53F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B4")
    TalkEnd(0xFE)
    Call(0, 21)
    Return()

    label("loc_52B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5397")

    ChrTalk(
        0xFE,
        (
            "When I first saw you, I\x01",
            "thought you were an\x01",
            "untrained bunch, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think you're full-\x01",
            "fledged now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I'll be\x01",
            "relentless from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha... Please, go easy\x01",
            "on us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_53F4")

    label("loc_5397")


    ChrTalk(
        0xFE,
        (
            "I think you're full-\x01",
            "fledged now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I'll be\x01",
            "relentless from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53F4")

    TalkEnd(0xFE)
    Return()

    # Function_5_4C30 end

    def Function_6_53F8(): pass

    label("Function_6_53F8")

    OP_4B(0x11, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "Kilika, thank you for\x01",
            "your hard work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The Taito School's Crimson\x01",
            "Swallow... Seeing your spirit from\x01",
            "up close was very enlightening!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03404FIt's been a while since I last fought, but\x01",
            "that went better than expected.\x02\x03",
            "#03400F...But even so Ling, it seems you've\x01",
            "trained hard yourself.\x02\x03",
            "Compared to when we met at the interleague\x01",
            "match eight years ago, you're like a whole\x01",
            "different person. Haha, how promising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. I still have a\x01",
            "long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd like to get a little\x01",
            "closer to master level\x01",
            "like you or Zin, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03400FHaha. You sure are dedicated.\x02\x03",
            "#03404FHmm. I think you'll be able to\x01",
            "win against the likes of Zin\x01",
            "in another year or two, maybe.\x02\x03",
            "#03402FIt looks like you haven't yet\x01",
            "been able to overcome the weak\x01",
            "nature of a young woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. You're like a\x01",
            "certain A-rank bracer when\x01",
            "you say that, Kilika.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0x11, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x1BB, 3)
    Return()

    # Function_6_53F8 end

    def Function_7_5769(): pass

    label("Function_7_5769")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "To be perfectly honest, I can't\x01",
            "think the Empire will stay quiet\x01",
            "with an address like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They'll definitely take some kind\x01",
            "of action... Or, it's possible\x01",
            "they may have already taken it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Arundel contacting us is\x01",
            "definitely linked to\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yeah, and you could say\x01",
            "the same thing about the\x01",
            "Republican side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I worried about the church's\x01",
            "response... Anyway, we have\x01",
            "to be ready for anything.\x02",
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

    # Function_7_5769 end

    def Function_8_5929(): pass

    label("Function_8_5929")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_593A")
    Jump("loc_62BF")

    label("loc_593A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5948")
    Jump("loc_62BF")

    label("loc_5948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B20")

    ChrTalk(
        0xFE,
        (
            "Ever since Chairman MacDowell's invalidity\x01",
            "declaration, restrictions have been getting\x01",
            "tighter. Even ambulances are restricted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For patients that can't be taken to the\x01",
            "hospital, we'll have to do our best with\x01",
            "medicine stockpiled in the city, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a limit to treatments we can do\x01",
            "in the city and church. It's imperative\x01",
            "they be taken to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The liberation of\x01",
            "Crossbell City... You\x01",
            "absolutely must succeed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5BDA")

    label("loc_5B20")


    ChrTalk(
        0xFE,
        (
            "There's a limit to treatments we can do\x01",
            "in the city and church. It's imperative\x01",
            "they be taken to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The liberation of\x01",
            "Crossbell City... You\x01",
            "absolutely must succeed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BDA")

    Jump("loc_62BF")

    label("loc_5BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5DE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D21")

    ChrTalk(
        0xFE,
        (
            "With the declaration of independence,\x01",
            "I wonder how my home state of\x01",
            "Remiferia will deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because Archduke Albert is wise,\x01",
            "he'll probably consider his own\x01",
            "people, first and foremost, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll contact St. Ursula.\x01",
            "Even the guild has to think\x01",
            "about how to deal with this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5DDD")

    label("loc_5D21")


    ChrTalk(
        0xFE,
        (
            "We'll contact St. Ursula.\x01",
            "Even the guild has to think\x01",
            "about how to deal with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We owe you guys for what you did\x01",
            "at the lake shore. Please, tell\x01",
            "us if you're ever in trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DDD")

    Jump("loc_62BF")

    label("loc_5DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5DF0")
    Jump("loc_62BF")

    label("loc_5DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E0F")
    TalkEnd(0xFE)
    Call(0, 23)
    Return()

    label("loc_5E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F2F")

    ChrTalk(
        0xFE,
        (
            "It's strange for a\x01",
            "jaeger corps to take\x01",
            "hostages...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they just harmed them\x01",
            "directly, it'd certainly cause\x01",
            "considerable emotional pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this situation drags\x01",
            "on, we'll need to consider\x01",
            "everyone's health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got to do\x01",
            "something about it\x01",
            "ASAP...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5FF3")

    label("loc_5F2F")


    ChrTalk(
        0xFE,
        (
            "By taking hostages, the jaeger\x01",
            "group is inflicting mental\x01",
            "pain on the people of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this situation drags on, we'll\x01",
            "need to consider everyone's health.\x01",
            "We've got to do something...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FF3")

    Jump("loc_62BF")

    label("loc_5FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6006")
    Jump("loc_62BF")

    label("loc_6006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6014")
    Jump("loc_62BF")

    label("loc_6014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6022")
    Jump("loc_62BF")

    label("loc_6022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6030")
    Jump("loc_62BF")

    label("loc_6030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_603E")
    Jump("loc_62BF")

    label("loc_603E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_604C")
    Jump("loc_62BF")

    label("loc_604C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_605A")
    Jump("loc_62BF")

    label("loc_605A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6068")
    Jump("loc_62BF")

    label("loc_6068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_62BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6087")
    TalkEnd(0xFE)
    Call(0, 21)
    Return()

    label("loc_6087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_624B")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xC,
        (
            "That's right... I\x01",
            "haven't seen Tio in a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think she went to\x01",
            "Lｳman State for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. It seems she'll be\x01",
            "there for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...*sigh*, I see. The guild HQ\x01",
            "is in Lｳman, so if I transfer\x01",
            "there for a while...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...We don't have time\x01",
            "for that. Michel would\x01",
            "never approve it either.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0xC, 0xB, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        "I know, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Haha... She's the same\x01",
            "as always.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_62BF")

    label("loc_624B")


    ChrTalk(
        0xFE,
        (
            "Ah, it's been so long\x01",
            "since I had a hug from\x01",
            "Tio...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Let me know once\x01",
            "she's back. I'll be\x01",
            "right there!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62BF")

    TalkEnd(0xFE)
    Return()

    # Function_8_5929 end

    def Function_9_62C3(): pass

    label("Function_9_62C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_62D4")
    Jump("loc_691F")

    label("loc_62D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_62E2")
    Jump("loc_691F")

    label("loc_62E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_650A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_644C")

    ChrTalk(
        0xFE,
        (
            "We had everyone who\x01",
            "couldn't escape shelter\x01",
            "indoors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though we didn't check inside\x01",
            "buildings, Pearl at the\x01",
            "department store should be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...If he took this kind of action,\x01",
            "the President doesn't care about\x01",
            "keeping up appearances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From here on out, we don't\x01",
            "know what they're going to\x01",
            "do. You guys be careful, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6505")

    label("loc_644C")


    ChrTalk(
        0xFE,
        (
            "...If he took this kind of action,\x01",
            "the President doesn't care about\x01",
            "keeping up appearances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From here on out, we don't\x01",
            "know what they're going to\x01",
            "do. You guys be careful, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6505")

    Jump("loc_691F")

    label("loc_650A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_666C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6608")

    ChrTalk(
        0xFE,
        (
            "I'm from Crossbell too,\x01",
            "so I kind of understand\x01",
            "how Arios is feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, to think he'd leave\x01",
            "the guild just because\x01",
            "of that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Thinking about it is\x01",
            "useless. Right now, I've got\x01",
            "to do what I can as a bracer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6667")

    label("loc_6608")


    ChrTalk(
        0xFE,
        (
            "I can't help thinking\x01",
            "about Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now, I've got to\x01",
            "do what I can as a\x01",
            "bracer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6667")

    Jump("loc_691F")

    label("loc_666C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_667A")
    Jump("loc_691F")

    label("loc_667A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_66FD")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "...I see, so Armorica's\x01",
            "safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes... Yes... Just in\x01",
            "case, please tell the\x01",
            "villagers to be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    Jump("loc_691F")

    label("loc_66FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_670B")
    Jump("loc_691F")

    label("loc_670B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6719")
    Jump("loc_691F")

    label("loc_6719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6727")
    Jump("loc_691F")

    label("loc_6727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6735")
    Jump("loc_691F")

    label("loc_6735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6743")
    Jump("loc_691F")

    label("loc_6743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6751")
    Jump("loc_691F")

    label("loc_6751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_675F")
    Jump("loc_691F")

    label("loc_675F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6916")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_677E")
    TalkEnd(0xFE)
    Call(0, 22)
    Return()

    label("loc_677E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_680F")
    Jump("loc_6859")

    label("loc_680F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_682F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6859")

    label("loc_682F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_684F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6859")

    label("loc_684F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6859")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "You guys are more\x01",
            "reliable than when I\x01",
            "first met you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll be helping each other\x01",
            "a lot from here on out, so\x01",
            "let's each do our best.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_691F")

    label("loc_6916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_691F")

    label("loc_691F")

    TalkEnd(0xFE)
    Return()

    # Function_9_62C3 end

    def Function_10_6923(): pass

    label("Function_10_6923")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_6934")
    Jump("loc_7256")

    label("loc_6934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6942")
    Jump("loc_7256")

    label("loc_6942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6ABA")

    ChrTalk(
        0xFE,
        (
            "Magic golems, huh...\x01",
            "He's sure brought out\x01",
            "some troublesome things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the liberation operation,\x01",
            "maximum consideration needs to\x01",
            "be given to citizen safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Things like that roaming around\x01",
            "the city is something that\x01",
            "absolutely can't be allowed to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the name of the guild,\x01",
            "we must make the President\x01",
            "pay for his crimes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6B70")

    label("loc_6ABA")


    ChrTalk(
        0xFE,
        (
            "...Things like that roaming around\x01",
            "the city is something that\x01",
            "absolutely can't be allowed to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the name of the guild,\x01",
            "we must make the President\x01",
            "pay for his crimes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B70")

    Jump("loc_7256")

    label("loc_6B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6C77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B90")
    Call(0, 7)
    Jump("loc_6C72")

    label("loc_6B90")


    ChrTalk(
        0xFE,
        (
            "Arundel of the Intelligence Division...\x01",
            "It's name I heard many times when I\x01",
            "worked in the Imperial guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've already met him, so I'm sure you\x01",
            "already know, but... he's a formidable\x01",
            "opponent. ...Be extra careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C72")

    Jump("loc_7256")

    label("loc_6C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6C85")
    Jump("loc_7256")

    label("loc_6C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E06")

    ChrTalk(
        0xFE,
        (
            "Scott already confirmed\x01",
            "it... Nothing's happened at\x01",
            "Armorica or the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, it's going to be nearly impossible\x01",
            "to beat the jaegers, now that they have\x01",
            "terrain advantage on the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this situation drags on, I\x01",
            "don't know what kind of danger\x01",
            "the people of Mainz will face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew it. We have no\x01",
            "choice but to act,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6E9C")

    label("loc_6E06")


    ChrTalk(
        0xFE,
        (
            "If this situation drags on, I\x01",
            "don't know what kind of danger\x01",
            "the people of Mainz will face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew it. We have no\x01",
            "choice but to act,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E9C")

    Jump("loc_7256")

    label("loc_6EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6EAF")
    Jump("loc_7256")

    label("loc_6EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6EBD")
    Jump("loc_7256")

    label("loc_6EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6ECB")
    Jump("loc_7256")

    label("loc_6ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6ED9")
    Jump("loc_7256")

    label("loc_6ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_707C")
    OP_4B(0xFE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FE6")

    ChrTalk(
        0xFE,
        (
            "...Yeah... Yeah... I see. I thought\x01",
            "the terrorists might be active in\x01",
            "the Empire as well, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yeah, sure. We'll\x01",
            "step up security on our\x01",
            "end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(It looked like he was\x01",
            "speaking with someone at\x01",
            "the Imperial guild.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7073")

    label("loc_6FE6")


    ChrTalk(
        0xFE,
        (
            "...I see. I thought the\x01",
            "terrorists might be active in\x01",
            "the Empire as well, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yeah, sure. We'll\x01",
            "step up security on our\x01",
            "end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7073")

    OP_4C(0xFE, 0xFF)
    Jump("loc_7256")

    label("loc_707C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_708A")
    Jump("loc_7256")

    label("loc_708A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7098")
    Jump("loc_7256")

    label("loc_7098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_724D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70B7")
    TalkEnd(0xFE)
    Call(0, 22)
    Return()

    label("loc_70B7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7148")
    Jump("loc_7192")

    label("loc_7148")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7168")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7192")

    label("loc_7168")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7188")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7192")

    label("loc_7188")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7192")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I heard about your exploits\x01",
            "in Altair City. You did a\x01",
            "nice job back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And you did it without\x01",
            "anyone getting hurt.\x01",
            "Keep it up.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_7256")

    label("loc_724D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7256")

    label("loc_7256")

    TalkEnd(0xFE)
    Return()

    # Function_10_6923 end

    def Function_11_725A(): pass

    label("Function_11_725A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_726F")
    Call(0, 6)
    Jump("loc_77B7")

    label("loc_726F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7601")

    ChrTalk(
        0x11,
        (
            "#03400FYou guys too... That was\x01",
            "nice work back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou too, Kilika. Thank\x01",
            "you for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FMan, you really saved us\x01",
            "back there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03402FHaha. I merely provided a bit\x01",
            "of assistance.\x02\x03",
            "#03403FMore importantly... I can't\x01",
            "hide my surprise at the\x01",
            "appearance of that Huge Tree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FHow will the Republic\x01",
            "deal with this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03403FI'm in shock. It looks like\x01",
            "you can see that Huge Tree\x01",
            "even from Altair City.\x02\x03",
            "We don't know what kind of\x01",
            "situation this is, so we'll\x01",
            "adopt a wait-and-see posture.\x02\x03",
            "#03400FI can't share any other\x01",
            "details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03400FI plan to remain here until I've\x01",
            "evaluated the situation.\x02\x03",
            "#03403FI don't know Crossbell's path...\x01",
            "I don't think anyone knows.\x01",
            "Everything is up to you guys.\x02\x03",
            "#03402FIn order to not have any\x01",
            "regrets, follow the path you\x01",
            "believe in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe will... Thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 7)
    Jump("loc_77B7")

    label("loc_7601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7706")

    ChrTalk(
        0x11,
        (
            "#03400FI plan to remain here until I've\x01",
            "evaluated the situation.\x02\x03",
            "#03403FI don't know Crossbell's path...\x01",
            "I don't think anyone knows.\x01",
            "Everything is up to you guys.\x02\x03",
            "#03402FIn order to not have any\x01",
            "regrets, follow the path you\x01",
            "believe in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_77B7")

    label("loc_7706")


    ChrTalk(
        0x11,
        (
            "#03403FI don't know Crossbell's path...\x01",
            "I don't think anyone knows.\x01",
            "Everything is up to you guys.\x02\x03",
            "#03400FIn order to not have any\x01",
            "regrets, follow the path you\x01",
            "believe in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77B7")

    TalkEnd(0xFE)
    Return()

    # Function_11_725A end

    def Function_12_77BB(): pass

    label("Function_12_77BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77D0")
    Call(0, 13)
    Jump("loc_7839")

    label("loc_77D0")


    ChrTalk(
        0x10,
        (
            "#01400F...Leave this place to\x01",
            "me.\x02\x03",
            "You guys search for the\x01",
            ""Nadelia Mushroom" on\x01",
            "St. Ursula Byroad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7839")

    TalkEnd(0xFE)
    Return()

    # Function_12_77BB end

    def Function_13_783D(): pass

    label("Function_13_783D")

    OP_4B(0x10, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x10,
        (
            "#01400F...Yeah, it's just like you\x01",
            "heard. Sorry, but please\x01",
            "hurry and look for it.\x02\x03",
            "If I remember correctly,\x01",
            "there should be a stockpile\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FI see... I wonder where\x01",
            "it was.\x02\x03",
            "I wonder if Eolia should\x01",
            "do it, too.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_13_783D end

    def Function_14_7943(): pass

    label("Function_14_7943")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The bracers' shift\x01",
            "schedule is posted.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7A56")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: -\x01",
            "   Scott: Armorica Village\x01",
            "  Wenzel: Mining Town Mainz\x01",
            "    Ling: Standby\x01",
            "   Eolia: St. Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_7A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7B01")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: -\x01",
            "   Scott: Standby\x01",
            "  Wenzel: Standby\x01",
            "    Ling: Standby\x01",
            "   Eolia: Standby\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_7B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7BAC")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: -\x01",
            "   Scott: Standby\x01",
            "  Wenzel: Standby\x01",
            "    Ling: Standby\x01",
            "   Eolia: Standby\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_7BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7C84")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Orchis Tower\x01",
            "   Scott: Bellguard Gate\x01",
            "  Wenzel: Bellguard Gate\x01",
            "    Ling: Mining Town Mainz\x01",
            "   Eolia: Mining Town Mainz\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_7C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7D3A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Orchis Tower\x01",
            "   Scott: Standby\x01",
            "  Wenzel: Standby\x01",
            "    Ling: Standby\x01",
            "   Eolia: Standby\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_7D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7E09")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Ling/Eolia Search\x01",
            "   Scott: Ling/Eolia Search\x01",
            "  Wenzel: Ling/Eolia Search\x01",
            "    Ling: Missing\x01",
            "   Eolia: Missing\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_7E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7EEA")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Cryptid Extermination\x01",
            "   Scott: Tangram Gate\x01",
            "  Wenzel: Tangram Gate\x01",
            "    Ling: St. Ursula Hospital\x01",
            "   Eolia: St. Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_7EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7FDA")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Cryptids Extermination/Investigation\x01",
            "   Scott: Tangram Gate\x01",
            "  Wenzel: Tangram Gate\x01",
            "    Ling: St. Ursula Hospital\x01",
            "   Eolia: St. Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_7FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8100")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Vacation\x01",
            "   Scott: Cryptids Extermination/Investigation\x01",
            "  Wenzel: Cryptids Extermination/Investigation\x01",
            "    Ling: Cryptids Extermination/Investigation\x01",
            "   Eolia: Cryptids Extermination/Investigation\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_8100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_81CB")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Orchis Tower\x01",
            "   Scott: Armorica Village\x01",
            "  Wenzel: Standby\x01",
            "    Ling: Standby\x01",
            "   Eolia: St. Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_81CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_82B6")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: St. Ursula Hospital\x01",
            "   Scott: Dealing with Requests\x01",
            "  Wenzel: Dealing with Requests\x01",
            "    Ling: Armorica Village\x01",
            "   Eolia: Armorica Village\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_82B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_839D")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Calvard Republic\x01",
            "   Scott: Mining Town Mainz\x01",
            "  Wenzel: Bellguard Gate\x01",
            "    Ling: Dealing with Requests\x01",
            "   Eolia: Dealing with Requests\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_839D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8478")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Principality of Remiferia\x01",
            "   Scott: Standby\x01",
            "  Wenzel: Standby\x01",
            "    Ling: St. Ursula Hospital\x01",
            "   Eolia: St. Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8548")

    label("loc_8478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8548")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Principality of Remiferia\x01",
            "   Scott: Armorica Village\x01",
            "  Wenzel: Erebonian Empire\x01",
            "    Ling: Standby\x01",
            "   Eolia: Standby\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8548")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_7943 end

    def Function_15_855F(): pass

    label("Function_15_855F")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Many requests for the\x01",
            "Bracer Guild are posted.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_861E")

    ChrTalk(
        0x101,
        (
            "#00000FAs usual, they've taken\x01",
            "on an amazing number of\x01",
            "requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FHmm~, we can't lose to\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_861E")

    TalkEnd(0xFF)
    Return()

    # Function_15_855F end

    def Function_16_8622(): pass

    label("Function_16_8622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_865A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8647")
    Call(0, 33)
    Return()

    label("loc_8647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_865A")
    Call(0, 34)
    Return()

    label("loc_865A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_866B")
    Jump("loc_8B08")

    label("loc_866B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_868D")
    Call(0, 17)
    Jump("loc_86C9")

    label("loc_868D")


    ChrTalk(
        0xD,
        (
            "#01109FShizuku, let's go to the\x01",
            "Support Section later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86C9")

    Jump("loc_8B08")

    label("loc_86CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86ED")
    Jump("loc_8AB4")

    label("loc_86ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A1F")
    TurnDirection(0xD, 0x1A2, 0)

    ChrTalk(
        0xD,
        (
            "#01100FOh, you're Shing, right?\x02\x03",
            "You don't look like you're\x01",
            "from Crossbell. How long\x01",
            "are you gonna be here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Me? Until around the day\x01",
            "after tomorrow, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01105FAh, then, where do you\x01",
            "wanna see the tower\x01",
            "unveiling tomorrow?\x02\x03",
            "#01102FWe're gonna see it from\x01",
            "the department store\x01",
            "roof. How 'bout it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "Y-You sure...?\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#01105FI said it's okay. How\x01",
            "'bout it?\x02\x03",
            "#01109FRyｹ, Henri and the other\x01",
            "kids 'll be there too.\x01",
            "It'll be fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "I-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "...Well if you're that\x01",
            "insistent, I guess I'll\x01",
            "go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It's at 11 tomorrow,\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01109FYeah. We'll be waiting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(Haha... Looks like\x01",
            "they're having fun.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Hmm. Maybe he doesn't get\x01",
            "the chance to play with\x01",
            "other kids that often...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 2)
    TurnDirection(0xD, 0xE, 0)
    Jump("loc_8AB4")

    label("loc_8A1F")

    TurnDirection(0xD, 0x1A2, 0)

    ChrTalk(
        0xD,
        (
            "#01100FThen, I'll see you on\x01",
            "the department store\x01",
            "roof tomorrow at 11.\x02\x03",
            "#01109FWe'll be waiting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Y-Yeah... See you\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 0)

    label("loc_8AB4")

    Jump("loc_8B08")

    label("loc_8AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8B08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AD1")
    Jump("loc_8B08")

    label("loc_8AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AE3")
    Call(0, 17)
    Jump("loc_8B08")

    label("loc_8AE3")


    ChrTalk(
        0xD,
        "#01109FThen, let's go, Shizuku!\x02",
    )

    CloseMessageWindow()

    label("loc_8B08")

    TalkEnd(0xFE)
    Return()

    # Function_16_8622 end

    def Function_17_8B0C(): pass

    label("Function_17_8B0C")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C1F")

    ChrTalk(
        0xD,
        (
            "#01104FShizuku, Shing left\x01",
            "already. Want to play\x01",
            "somewhere else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#06005FAh, yes, you're right.\x02\x03",
            "#06000FBut, is it okay for us\x01",
            "to go alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01111FHmm... That's right.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#01110FAh, then I've got a good\x01",
            "idea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CD5")

    label("loc_8C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8CD5")

    ChrTalk(
        0xD,
        (
            "#01109FYou see, it's got a blue\x01",
            "sheet on it right now...\x01",
            "It's really biiig.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#06002FMust be nice... Haha, I\x01",
            "can almost see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01109FThen, let's go, Shizuku!\x02",
    )

    CloseMessageWindow()

    label("loc_8CD5")

    SetScenarioFlags(0x1, 1)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_17_8B0C end

    def Function_18_8CE1(): pass

    label("Function_18_8CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D06")
    Call(0, 33)
    Return()

    label("loc_8D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D19")
    Call(0, 34)
    Return()

    label("loc_8D19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_8D2A")
    Jump("loc_8F94")

    label("loc_8D2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D4C")
    Call(0, 17)
    Jump("loc_8DA3")

    label("loc_8D4C")


    ChrTalk(
        0xE,
        (
            "#06005FNo, it's fine... What's\x01",
            "your idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#01104FEhehe, it's still a\x01",
            "secret.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DA3")

    Jump("loc_8F94")

    label("loc_8DA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DC7")
    Jump("loc_8F27")

    label("loc_8DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E99")
    TurnDirection(0xE, 0x1A2, 0)

    ChrTalk(
        0xE,
        (
            "#06002FHaha, you're a very good\x01",
            "boy, Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "N-Nah... T-That's not\x01",
            "true, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "After all, I'm the man\x01",
            "burdened with the future\x01",
            "of Heiyue!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#06002F*chuckle*...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    TurnDirection(0xE, 0xD, 0)
    Jump("loc_8F27")

    label("loc_8E99")

    TurnDirection(0xE, 0x1A2, 0)

    ChrTalk(
        0xE,
        (
            "#06002F*chuckle*... I don't\x01",
            "really get it, but you're\x01",
            "a good boy, Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "(H-Hmm... I'm not that\x01",
            "kind of boy, though.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 0)

    label("loc_8F27")

    Jump("loc_8F94")

    label("loc_8F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8F94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F44")
    Jump("loc_8F94")

    label("loc_8F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F56")
    Call(0, 17)
    Jump("loc_8F94")

    label("loc_8F56")


    ChrTalk(
        0xE,
        (
            "#06002FHaha, I understand.\x01",
            "Let's go see it\x01",
            "together, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F94")

    TalkEnd(0xFE)
    Return()

    # Function_18_8CE1 end

    def Function_19_8F98(): pass

    label("Function_19_8F98")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_19_8F98 end

    def Function_20_8F9F(): pass

    label("Function_20_8F9F")

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

    def lambda_9087():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9087)

    def lambda_90A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_90A1)
    Sleep(250)

    def lambda_90B5():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_90B5)

    def lambda_90CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_90CF)
    Sleep(600)

    def lambda_90E3():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_90E3)

    def lambda_90FD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_90FD)
    Sleep(250)

    def lambda_9111():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9111)

    def lambda_912B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_912B)
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
        "#04005FMy, it's all of you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMichel... It's been a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x101, 500, 0, 3000, 0)
    SetChrPos(0x102, -500, 0, 3000, 0)
    SetChrPos(0x105, 0, 0, 1900, 0)
    SetChrPos(0x109, -1000, 0, 1900, 0)

    def lambda_9205():
        OP_96(0xFE, 0x5DC, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9205)
    Sleep(100)

    def lambda_9222():
        OP_96(0xFE, 0x1F4, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9222)
    Sleep(150)

    def lambda_923F():
        OP_96(0xFE, 0x7D0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_923F)
    Sleep(100)

    def lambda_925C():
        OP_96(0xFE, 0x3E8, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_925C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x105, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9313")

    AnonymousTalk(
        0x8,
        (
            "Haha. It has, hasn't it.\x02\x03",
            "Nice job with that\x01",
            "arrest in Altair City.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_9374")

    label("loc_9313")


    AnonymousTalk(
        0x8,
        (
            "Haha. It's been a while.\x02\x03",
            "It's a bit late, but\x01",
            "nice job with that\x01",
            "arrest in Altair City.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9374")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#12P#00000FThanks. You guys too. It\x01",
            "was a big help having\x01",
            "Arios with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHaha. You look well,\x01",
            "Michel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FHaha. I'm in top form♪\x02\x03",
            "#04006FWell, we're busier than\x01",
            "usual now with Estelle\x01",
            "and Joshua gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FI expected as much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FBut, it looks like Arios\x01",
            "and the other bracers\x01",
            "are managing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FWell, we're used to\x01",
            "being short-handed.\x02\x03",
            "#04000FWe've got to manage as\x01",
            "best we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FThey don't call you\x01",
            "bracers "ally of the\x01",
            "citizens" for nothing...\x02\x03",
            "#10300FNo matter how busy you\x01",
            "guys are, there's hardly\x01",
            "a word of complaint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FExactly. You know us\x01",
            "well.\x02\x03",
            "#04009FAlthough we acknowledge\x01",
            "you police, that's\x01",
            "exactly why we─\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04005FHey, could these kids\x01",
            "be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, they're our new\x01",
            "Support Section members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FNoｱl Seeker, transferee\x01",
            "from the Guardian Force!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWazy Hemisphere... But I\x01",
            "guess that goes without\x01",
            "saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FHeh... Quite the interesting kids\x01",
            "you've got there.\x02\x03",
            "#04004FAn active duty CGF member goes\x01",
            "without saying, but to think you've\x01",
            "got that Testaments leader too.\x02\x03",
            "#04000FThey must be a great help now that\x01",
            "you've restarted the Support\x01",
            "Section.\x02\x03",
            "But, are you sure you can rely on\x01",
            "them when push comes to shove?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, of course.\x02\x03",
            "Though our viewpoints\x01",
            "may be different, we're\x01",
            "working together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FHaha, your faces look a\x01",
            "lot better than when we\x01",
            "first met.\x02\x03",
            "#04011FThen, once again... It's\x01",
            "a pleasure to be working\x01",
            "with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x139, 0)
    OP_4C(0x8, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_20_8F9F end

    def Function_21_99AC(): pass

    label("Function_21_99AC")

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
        (
            "Yo, Special Support\x01",
            "Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "My, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLing and Eolia. Indeed\x01",
            "it has.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWhat's new with everyone\x01",
            "at the guild?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)

    ChrTalk(
        0xB,
        (
            "Yeah, we're busy as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x105, 500)

    ChrTalk(
        0xB,
        (
            "Oh, do I spy some new\x01",
            "faces?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FWell, something like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FYou guys are bracers,\x01",
            "right? Pleased to make\x01",
            "your acquaintance!\x02\x03",
            "#10109FActually, I think I saw\x01",
            "you guys heading for the\x01",
            "Republic a couple times.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x109, 500)

    ChrTalk(
        0xB,
        (
            "Yeah, you're that CGF\x01",
            "member... I think I've seen\x01",
            "you at Tangram Gate as well.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x109, 500)

    ChrTalk(
        0xC,
        (
            "Haha, that operation at\x01",
            "Altair City was quite\x01",
            "the job.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "You guys got through that cult\x01",
            "incident. You'll be full-\x01",
            "fledged before long, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha. We have a long way\x01",
            "to go in many respects,\x01",
            "but...\x02\x03",
            "#00000FWe plan to do our very\x01",
            "best from here on.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        "Haha, that's the spirit.\x02",
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

    # Function_21_99AC end

    def Function_22_9DB0(): pass

    label("Function_22_9DB0")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9EBA")
    Jump("loc_9F04")

    label("loc_9EBA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9EDA")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F04")

    label("loc_9EDA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EFA")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F04")

    label("loc_9EFA")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F04")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9FBA")
    Jump("loc_A004")

    label("loc_9FBA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9FDA")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A004")

    label("loc_9FDA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FFA")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A004")

    label("loc_9FFA")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A004")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    OP_0D()

    ChrTalk(
        0x9,
        "#6POh, you guys are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...The Special Support\x01",
            "Section, huh. Hmm, it's\x01",
            "been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FScott and Wenzel. Good\x01",
            "to see you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10300FYou guys are bracers,\x01",
            "huh? You guys are really\x01",
            "talented.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A19A")
    Jump("loc_A1E4")

    label("loc_A19A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A1BA")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1E4")

    label("loc_A1BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1DA")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1E4")

    label("loc_A1DA")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1E4")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6PAnd you're that Downtown\x01",
            "delinquent group's...\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2D4")
    Jump("loc_A31E")

    label("loc_A2D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A2F4")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A31E")

    label("loc_A2F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A314")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A31E")

    label("loc_A314")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A31E")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6PAnd you there. You look\x01",
            "like a CGF member\x01",
            "somehow.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A412")
    Jump("loc_A45C")

    label("loc_A412")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A432")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A45C")

    label("loc_A432")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A452")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A45C")

    label("loc_A452")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A45C")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6PHaha, looks like you've\x01",
            "got some new recruits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10105FWazy aside... How did\x01",
            "you know?\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A57C")
    Jump("loc_A5C6")

    label("loc_A57C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A59C")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5C6")

    label("loc_A59C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A5BC")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5C6")

    label("loc_A5BC")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A5C6")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "You don't look like any\x01",
            "police officer I've\x01",
            "seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you do the kind of work\x01",
            "us bracers do, you develop\x01",
            "an eye for these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FHaha, thanks for the\x01",
            "warning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PWe'll be helping each other\x01",
            "a lot from here on out, so\x01",
            "let's each do our best.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x138, 7)
    EventEnd(0x5)
    Return()

    # Function_22_9DB0 end

    def Function_23_A70D(): pass

    label("Function_23_A70D")

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
        "#5P#04000FOh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hey, you saved us\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FLing, Eolia... How are\x01",
            "you feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Okay, I guess. It's all\x01",
            "thanks to you guys,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "Tio, I'll pet you later\x01",
            "as a way of saying\x01",
            "thanks, ok?㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xC, 500)

    ChrTalk(
        0x103,
        (
            "#12P#00203F...I respectfully\x01",
            "refuse.\x02\x03",
            "#00200FBut if you can say that,\x01",
            "you must be feeling\x01",
            "better.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 500)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "Yeah, but we can't push\x01",
            "ourselves too hard\x01",
            "yet...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "Huh? Come to think of\x01",
            "it... Where'd that\x01",
            "redhead go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Normally, he'd be saying\x01",
            ""Then in return, I'll..."\x01",
            "and stuff around now.\x02",
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
            "#5P#04001F...Looks like something\x01",
            "happened. Want to talk\x01",
            "about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, actually...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others\x01",
            "explained that Randy had\x01",
            "disappeared.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5P#04003F...I see.\x02\x03",
            "#04001FThe Mainz occupation... Now that Red\x01",
            "Constellation is involved, we can\x01",
            "only guess at what will happen next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FHow will the guild deal\x01",
            "with this incident?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "The CGF is going all-out to try\x01",
            "to resolve the incident, so for\x01",
            "now we'll just wait and see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But, if the situation goes on for too\x01",
            "much longer, we'll have no choice but\x01",
            "to act. ...Isn't that right, Michel?\x02",
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
            "#5P#04003FYes...\x02\x03",
            "#04001FDepending on the situation, we might\x01",
            "need to summon A-rank or above bracers\x01",
            "from nearby countries to intervene.\x02",
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
        "#12P#00011FT-That much!?\x02",
    )

    CloseMessageWindow()

    def lambda_AE24():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AE24)
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "That's only in the worst\x01",
            "case scenario.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Right now, Arios is\x01",
            "discussing things with\x01",
            "the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If it doesn't look like\x01",
            "the CGF can resolve the\x01",
            "incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FWell, being the guild, civilian safety\x01",
            "is your number one priority. Of course\x01",
            "you'll have to deal with it...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    ChrTalk(
        0x8,
        (
            "#5P#04003F...Anyway, I'm worried\x01",
            "about that redheaded boy\x01",
            "myself.\x02\x03",
            "#04001FI don't know what's\x01",
            "going to happen, but you\x01",
            "guys be careful, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F...Yes, understood.\x02",
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

    # Function_23_A70D end

    def Function_24_B06B(): pass

    label("Function_24_B06B")

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
        "#5P#04005FAh... It's you guys!?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B1CD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B1CD)
    Sleep(50)

    def lambda_B1DD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B1DD)
    Sleep(50)

    def lambda_B1ED():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B1ED)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "There hasn't been any news\x01",
            "since the declaration of\x01",
            "independence, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, at least you guys\x01",
            "are ok.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FMichel, everyone... It's\x01",
            "been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FHaha, thank goodness\x01",
            "you're all safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Haha, same to you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Tio! Thank goodness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006F...Hey. This is no time\x01",
            "for leisurely greetings.\x02\x03",
            "#04001FI know it's been a\x01",
            "while, but can we\x01",
            "exchange notes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, understood.\x02",
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
            "...I see, so that's how\x01",
            "it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Honestly, I still have no idea\x01",
            "what exactly is going on, but I\x01",
            "finally understand some of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, when I heard that a red Aion appeared\x01",
            "at the west entrance, I was thinking of\x01",
            "doing something about it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I couldn't believe it\x01",
            "was Estelle and friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems like Heiyue and the CGF\x01",
            "resistance are helping out at\x01",
            "the north and east entrances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, I guess you guys\x01",
            "have a lot of\x01",
            "connections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FHaha, I guess you're\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FBy the way... Magic Soldiers have\x01",
            "appeared in the city and don't\x01",
            "suffer from human injuries?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've been cautiously patrolling\x01",
            "the neighborhood looking for\x01",
            "people who couldn't escape, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems those Magic Soldiers\x01",
            "won't lay their hands on\x01",
            "Crossbell citizens at all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B811")

    ChrTalk(
        0x105,
        (
            "#12P#10403FHmm... It seems the\x01",
            "President has good\x01",
            "control over them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8C3")

    label("loc_B811")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B870")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FHmm... It seems the\x01",
            "President has good\x01",
            "control over them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8C3")

    label("loc_B870")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B8C3")

    ChrTalk(
        0x109,
        (
            "#12P#10101FIt seems the President\x01",
            "has good control over\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B907")

    ChrTalk(
        0x106,
        (
            "#12P#10705FThat's a good thing, in\x01",
            "a way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B996")

    label("loc_B907")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B94B")

    ChrTalk(
        0x109,
        (
            "#12P#10105FThat's a good thing, in\x01",
            "a way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B996")

    label("loc_B94B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B996")

    ChrTalk(
        0x105,
        (
            "#12P#10304FI wonder if that's a\x01",
            "good thing, in a way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B996")


    ChrTalk(
        0x101,
        (
            "#12P#00001FEven so... There's\x01",
            "probably a great number\x01",
            "of worried people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FThat's right... The longer\x01",
            "this goes on, the more\x01",
            "casualties there will be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003FI agree. The guild can't stand\x01",
            "by when innocent civilians are\x01",
            "exposed to danger.\x02\x03",
            "#04011FThe invasion of Orchis Tower and\x01",
            "the arrest of the President...\x01",
            "Allow us to help you once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204FThank you very much.\x01",
            "That's very reassuring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003FHowever... It's likely\x01",
            "that Arios is in Orchis\x01",
            "Tower.\x02\x03",
            "Mariabell and that\x01",
            "Battle Ogre are probably\x01",
            "waiting for you too.\x02\x03",
            "#04001FI know it won't be\x01",
            "easy... You're all aware\x01",
            "of that, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303FAll too well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FNo matter what kind of Barriers\x01",
            "stand in our way... We have no\x01",
            "choice but to push through them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04004FHaha. It seems you all\x01",
            "are ready for this.\x02\x03",
            "#04001F─Please contact us when\x01",
            "it's time to begin the\x01",
            "operation.\x02\x03",
            "Until then, we'll be\x01",
            "preparing to assist you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FAlright... See you\x01",
            "later.\x02",
        )
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

    # Function_24_B06B end

    def Function_25_BDE6(): pass

    label("Function_25_BDE6")

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
            "Oh, thank you for coming.\x02\x03",
            "Arios isn't back yet, but you can\x01",
            "wait upstairs if you like.\x02\x03",
            "But you could also return after\x01",
            "finishing your other business.\x02",
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
            "#12P#00005FOh, that's right.\x02\x03",
            "#00008F(It's almost evening...\x01",
            "Is there anything else\x01",
            "we need to do?)\x02",
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
            "[We Have Other Things to Do]\x01",      # 0
            "[Wait for Arios' Return]\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C09A"),
        (1, "loc_C134"),
        (SWITCH_DEFAULT, "loc_C34B"),
    )


    label("loc_C09A")


    ChrTalk(
        0x8,
        (
            "#5P#04011FI see. Then please,\x01",
            "return here once you've\x01",
            "finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FAlright. We'll be back.\x02",
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
    Jump("loc_C34B")

    label("loc_C134")


    ChrTalk(
        0x8,
        (
            "#5P#04011FThen, please head\x01",
            "upstairs and make\x01",
            "yourselves at home.\x02\x03",
            "We have tea and coffee.\x01",
            "Please feel free to have\x01",
            "some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FHaha, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FOk, we'll head upstairs,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 4500)

    def lambda_C20E():

        label("loc_C20E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C20E")

    QueueWorkItem2(0x8, 2, lambda_C20E)
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
            "Not long after, Arios returned to the guild.\x02\x03",
            "Lloyd and the others exchanged information\x01",
            "with him regarding the trade conference as\x01",
            "well as Heiyue and Red Constellation.\x07\x00\x02",
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
    Jump("loc_C34B")

    label("loc_C34B")

    Return()

    # Function_25_BDE6 end

    def Function_26_C34C(): pass

    label("Function_26_C34C")

    OP_92(0xFE, 0x1F40, 0x2AF8, 0x1F4)

    def lambda_C35E():
        OP_95(0xFE, 8000, 0, 11000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C35E)
    WaitChrThread(0xFE, 1)

    def lambda_C37C():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C37C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_C34C end

    def Function_27_C396(): pass

    label("Function_27_C396")

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
            "#4049V#30W─I see.\x02\x03",
            "#4050VEven though it's called Crimson &\x01",
            "Co., they do that on the side.\x02",
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
            "#04006FIt's become more difficult to\x01",
            "get information from the\x01",
            "Imperial capital region lately.\x02\x03",
            "#04000FThanks, that really helps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FDon't mention it. We're\x01",
            "happy to be of service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FBut, did you get any\x01",
            "information on Red\x01",
            "Constellation itself?\x02\x03",
            "#10300FI heard the guild has\x01",
            "many skirmishes with\x01",
            "jaeger corps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FThat is true, but encounters\x01",
            "with jaegers on the level of\x01",
            "Red Constellation are rare.\x02\x03",
            "#01400FIf we did oppose them, it\x01",
            "would likely mean all-out\x01",
            "war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FThat much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FTheir forces are on the\x01",
            "level of a small\x01",
            "country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FAmong the many jaeger corps, Red\x01",
            "Constellation is in a whole other league.\x02\x03",
            "They have connections throughout the\x01",
            "continent, and at the first sign of conflict,\x01",
            "they rush in and escalate it themselves...\x02\x03",
            "#04001FZephyr might be the only jaeger corps that\x01",
            "can match them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FThat's that Revache\x01",
            "underboss' old haunt, if\x01",
            "I recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FBoth groups gather tough\x01",
            "guys with combat\x01",
            "experience.\x02\x03",
            "There was one called the\x01",
            "Jaeger King. He was like a\x01",
            "monster...\x02\x03",
            "#00303FBut half a year ago, he and\x01",
            "the War God─ my dad─ killed\x01",
            "each other in a fight.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x102,
        "#6P#00108FRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01405FHmm, it seems there's a\x01",
            "lot going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FActually, the guild is\x01",
            "aware of that\x01",
            "information already.\x02\x03",
            "#04001FBy the way, Zephyr has\x01",
            "suspended their\x01",
            "activities at present.\x02\x03",
            "Red Constellation looks\x01",
            "active as ever,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FIt's because my uncle's\x01",
            "left.\x02\x03",
            "#00303F─Sigmund, the Ogre Rosso,\x01",
            "Red Constellation's\x01",
            "second-in-command.\x02\x03",
            "#00301FHe's a monster on the\x01",
            "same level as the War God\x01",
            "and the Jaeger King.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01400FThose three are\x01",
            "particularly famous.\x02\x03",
            "#01403FBased on what I've\x01",
            "heard, I wonder if I\x01",
            "could even match him.\x02",
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
        "#12P#00011FN-No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FEven the Divine Blade of\x01",
            "Wind can't...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FHmm. From what I can see, I think\x01",
            "he has about a 50-50 chance.\x02\x03",
            "#04000FThere's a considerable difference\x01",
            "between the fighting styles of a\x01",
            "swordsman and a jaeger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F...You're telling me.\x02\x03",
            "#00301FYou might be strong, but my\x01",
            "uncle's a true monster.\x02\x03",
            "If you were to fight each\x01",
            "other, neither of you would\x01",
            "walk out of it unscathed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FYeah, I know.\x02\x03",
            "#01400F─However, I will oppose\x01",
            "him, should that become\x01",
            "necessary.\x02\x03",
            "The problem is why they\x01",
            "have come to Crossbell.\x02",
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
        (
            "#10106FThat's what it boils\x01",
            "down to, indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FWith the info we've\x01",
            "collected thus far, we\x01",
            "have some idea.\x02\x03",
            "#10300FThe clues point to them\x01",
            "being connected with the\x01",
            "Imperial government.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#04001FThat may be true, but\x01",
            "there's something else\x01",
            "I'm more concerned about.\x02\x03",
            "It's something Arios\x01",
            "learned for us when he\x01",
            "was in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FYes─ It's about Heiyue.\x02\x03",
            "#01401FAt present, the Republican\x01",
            "government has dealings\x01",
            "with the elders of Heiyue.\x02",
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
        "#12P#00007FSeriously!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_D537")

    ChrTalk(
        0x102,
        (
            "#12P#00108FShing did say his\x01",
            "grandfather was a Heiyue\x01",
            "elder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D57B")

    label("loc_D537")


    ChrTalk(
        0x102,
        (
            "#12P#00108FThe Heiyue elders are\x01",
            "their most central\x01",
            "figures...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D57B")


    ChrTalk(
        0x8,
        (
            "#04006FThere's one more point to\x01",
            "consider.\x02\x03",
            "#04001FThe one who is facilitating\x01",
            "those dealings is a woman\x01",
            "named Kilika Rouran.\x02",
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
        "#12P#00011FWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00107FThats... I can't believe\x01",
            "it, it's Kilika!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWow, the raven-haired\x01",
            "woman we saw at the\x01",
            "auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FIncidentally, she also has\x01",
            "connections to the Bracer\x01",
            "Guild.\x02\x03",
            "She once served as the Zeiss\x01",
            "branch receptionist in Liberl.\x02\x03",
            "#01400FHowever, about a year ago, she\x01",
            "retired and transferred to the\x01",
            "Calvardian intelligence agency.\x02\x03",
            "That agency is called the\x01",
            "Rocksmith Agency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FIs that right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FRocksmith... That's the\x01",
            "name of the Republican\x01",
            "President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FI heard a new intelligence\x01",
            "agency was created with the\x01",
            "President as its leader, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00101FW-Wait a minute!\x02\x03",
            "Red Constellation and Heiyue\x01",
            "had a conflict before,\x01",
            "right!?\x02\x03",
            "If the intelligence officers\x01",
            "of the major powers are in\x01",
            "contact with them, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FIt means the stage is\x01",
            "being set for an\x01",
            "incredible confrontation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013FUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYou mean Crossbell will end up as the\x01",
            "battleground in a proxy war between\x01",
            "the Empire and the Republic!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FIt's a possibility, of course.\x02\x03",
            "#04001FEspecially since the Chancellor Osborne of\x01",
            "Erebonia and President Rocksmith of Calvard will\x01",
            "be attending the trade conference tomorrow.\x02\x03",
            "Either or both might be be planning to take\x01",
            "advantage of the situation and eliminate the\x01",
            "other leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FBut neither of them is keeping their\x01",
            "contacts a secret. That is quite\x01",
            "strange.\x02\x03",
            "Suppose Heiyue or Red Constellation\x01",
            "acted. If those nations' backing of\x01",
            "those groups came to light, they'd be\x01",
            "blamed by the international community.\x02\x03",
            "#01400FNeither the Empire nor the Republic\x01",
            "would take that kind of risk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FH-Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYou're right. It doesn't\x01",
            "look like they're setting\x01",
            "up for a simple attack.\x02\x03",
            "#00108FBut why, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FDamn. What the hell is\x01",
            "my uncle thinking?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00003FIn any case, there must\x01",
            "be some meaning in what\x01",
            "they're doing.\x02\x03",
            "#00008FIt's likely there's at\x01",
            "least one piece of the\x01",
            "puzzle we're missing.\x02\x03",
            "#00001FAnd we need to grab all\x01",
            "of them that we can get.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    ChrTalk(
        0x102,
        "#12P#00105FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FHehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FUhuhu, that's Lloyd for\x01",
            "you. We're way ahead of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01404FActually, we were thinking the same\x01",
            "thing.\x02\x03",
            "#01402FWe're in the middle of using the guild's\x01",
            "information network to track down\x01",
            "information on those puzzle pieces.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)

    ChrTalk(
        0x101,
        "#12P#00002FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAlright then. Will you\x01",
            "let us know if you learn\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FOf course. We'll contact\x01",
            "police HQ in that case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01402FPlease do the same for us. Let\x01",
            "us know if you find out anything\x01",
            "new.\x02\x03",
            "We'll need to cooperate if we're\x01",
            "going to get through these next\x01",
            "three days without incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FWe'll contact you right\x01",
            "away if we learn\x01",
            "something.\x02",
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
            "After that, KeA and Shizuku returned to the\x01",
            "guild with Zeit.\x02\x03",
            "Arios said he was taking his daughter to\x01",
            "dinner and bid Lloyd and the others farewell.\x01",
            "They decided to return to the Support Section.\x02",
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

    # Function_27_C396 end

    def Function_28_E2D6(): pass

    label("Function_28_E2D6")

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
        "#5P#04005FOh, it's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHaha... Good to see you,\x01",
            "Michel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FUhmm, we're a little\x01",
            "worried about what we\x01",
            "heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006F*sigh*, I didn't want to\x01",
            "do it. But our need is\x01",
            "urgent.\x02\x03",
            "#04011FAnd thank you. I'm so\x01",
            "glad you came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305F...Then you haven't been\x01",
            "able to contact Ling or\x01",
            "Eolia yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003FThat's right. Arios and the\x01",
            "others split up and are\x01",
            "looking for them, but...\x02\x03",
            "#04008FI mean, seriously. What do\x01",
            "they think they're doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FThat is rather\x01",
            "concerning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FHmm... If they can't be reached\x01",
            "via ENIGMA, does it mean\x01",
            "they're outside the state?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FI was thinking that too, honey, but\x01",
            "there's no record of them having\x01",
            "used the station or airport.\x02\x03",
            "#04001FAnd there's no record of them\x01",
            "passing through Tangram or\x01",
            "Bellguard gates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FThat is really\x01",
            "strange...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#12P#00203F...If Ling and Eolia are\x01",
            "inside the state...\x02\x03",
            "#00200FI might be able to\x01",
            "locate them somehow.\x02",
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

    def lambda_E809():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E809)
    Sleep(50)

    def lambda_E819():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E819)
    Sleep(50)

    def lambda_E829():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E829)
    Sleep(50)

    def lambda_E839():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E839)
    Sleep(50)

    def lambda_E849():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E849)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#11P#00005FReally!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04005FWha, wha... How,\x01",
            "exactly!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FI think functions left over from\x01",
            "the development stage are still\x01",
            "present in ENIGMA Ⅱ units.\x02\x03",
            "#00200FOne of them is to transmit an\x01",
            "alert signal in emergencies.\x02",
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
        "#12P#10105FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FIt's configured to use reserve orbal\x01",
            "energy to transmit orbal waves of a\x01",
            "specific frequency at fixed intervals.\x02\x03",
            "But the orbal wave is very weak. I've\x01",
            "never heard of a practical application\x01",
            "for it.\x02\x03",
            "#00201FBut that function wasn't ever cut. It\x01",
            "should still be there, even in\x01",
            "production models.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThen, if we can somehow\x01",
            "catch that faint orbal\x01",
            "wave...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04001FWe'd have a fix on Ling\x01",
            "and Eolia's location!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204FI think it's worth a try.\x02\x03",
            "#00202FChief Roberts is familiar\x01",
            "with this function. Let's\x01",
            "head to IBC.\x02\x03",
            "He should be willing to\x01",
            "assist us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00000FUnderstood. Let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006F...I'm sorry. And thank\x01",
            "you for helping them.\x02\x03",
            "#04000FPlease contact us as\x01",
            "soon as you learn\x01",
            "anything.\x02\x03",
            "If the situation\x01",
            "warrants it, I'll recall\x01",
            "Arios and the others.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ED53():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ED53)
    Sleep(50)

    def lambda_ED63():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ED63)
    Sleep(50)

    def lambda_ED73():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_ED73)
    Sleep(50)

    def lambda_ED83():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ED83)
    Sleep(50)

    def lambda_ED93():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_ED93)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        "#12P#00100FRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FShall we head to IBC,\x01",
            "then?\x02",
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

    # Function_28_E2D6 end

    def Function_29_EE3F(): pass

    label("Function_29_EE3F")

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

    def lambda_EF4F():
        TurnDirection(0x102, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EF4F)
    Sleep(0)

    def lambda_EF5F():
        TurnDirection(0x103, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_EF5F)
    Sleep(0)

    def lambda_EF6F():
        TurnDirection(0x104, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_EF6F)
    Sleep(0)

    def lambda_EF7F():
        TurnDirection(0x109, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EF7F)
    Sleep(0)

    def lambda_EF8F():
        TurnDirection(0x105, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_EF8F)
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
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─Yes, an orbal boat is\x01",
            "ready for you at\x01",
            "Waterfront Area wharf.\x02\x03",
            "You can board right\x01",
            "away.\x02",
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
            "#00006FIs that right. Thanks,\x01",
            "Fran.\x02\x03",
            "#00001FAnd sorry for requesting\x01",
            "something like that all\x01",
            "of a sudden.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Don't mention it. I'm\x01",
            "here to support all of\x01",
            "you in times like this.\x02\x03",
            "But the marshlands to\x01",
            "the south, huh... Be\x01",
            "very, very careful, ok?\x02",
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
            "#00000FSure, we'll keep that in\x01",
            "mind.\x02",
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
            "#12P#10101FIt seems like we were\x01",
            "able to secure a boat.\x02",
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
            "#5P#00002FYeah, I asked Fran to\x01",
            "get one for us ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006F─*sigh*, it seems like I'm\x01",
            "going to be relying on you guys\x01",
            "'til the bitter end this time.\x02\x03",
            "#04001FBut, are you sure you're ok\x01",
            "with this?\x02\x03",
            "I think Arios and the others\x01",
            "will be back here within the\x01",
            "hour...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F379():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F379)
    Sleep(50)

    def lambda_F389():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F389)
    Sleep(50)

    def lambda_F399():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F399)
    Sleep(50)

    def lambda_F3A9():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F3A9)
    Sleep(50)

    def lambda_F3B9():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F3B9)
    Sleep(50)

    def lambda_F3C9():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F3C9)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x104,
        (
            "#6P#00303FThat's too long. It's\x01",
            "best if we go there\x01",
            "ahead of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FThat's right... We don't\x01",
            "know what the situation\x01",
            "is over there, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, once they're back,\x01",
            "tell them to follow us,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04000FUnderstood.\x02\x03",
            "#04003FBoth Ling and Eolia are\x01",
            "capable bracers who are\x01",
            "nearly A-rank.\x02\x03",
            "If they're both in a\x01",
            "situation where they\x01",
            "can't contact us...\x02\x03",
            "#04001FI have no idea what it\x01",
            "could be. Be extremely\x01",
            "careful, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013FRight!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#6P#00201FWe'll head for the wharf\x01",
            "once we're ready.\x02",
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

    # Function_29_EE3F end

    def Function_30_F659(): pass

    label("Function_30_F659")

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
        "#00001FExcuse us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FWe're coming in.\x02",
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

    def lambda_F8DD():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_F8DD)
    Sleep(50)

    def lambda_F8ED():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_F8ED)
    Sleep(50)

    def lambda_F8FD():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_F8FD)
    Sleep(50)

    def lambda_F90D():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_F90D)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    Sleep(1000)

    def lambda_F930():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F930)

    def lambda_F94A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F94A)
    Sleep(600)

    def lambda_F95E():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F95E)

    def lambda_F978():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F978)
    Sleep(900)

    def lambda_F98C():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F98C)

    def lambda_F9A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F9A6)
    Sleep(600)

    def lambda_F9BA():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F9BA)

    def lambda_F9D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F9D4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#04005F#6PYou guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PHey, it's you guys...\x02",
    )

    CloseMessageWindow()

    def lambda_FA30():

        label("loc_FA30")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FA30")

    QueueWorkItem2(0x9, 2, lambda_FA30)

    def lambda_FA42():

        label("loc_FA42")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FA42")

    QueueWorkItem2(0xA, 2, lambda_FA42)

    def lambda_FA54():

        label("loc_FA54")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_FA54")

    QueueWorkItem2(0xC, 2, lambda_FA54)

    def lambda_FA66():
        OP_96(0xFE, 0x384, 0x0, 0x206C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FA66)
    Sleep(200)

    def lambda_FA83():
        OP_96(0xFE, 0xFFFFFED4, 0x0, 0x1E78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FA83)
    Sleep(100)

    def lambda_FAA0():
        OP_96(0xFE, 0x578, 0x0, 0x1C84, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FAA0)
    Sleep(100)

    def lambda_FABD():
        OP_96(0xFE, 0xC8, 0x0, 0x1A90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FABD)
    Sleep(1500)
    Fade(500)
    OP_68(1000, 1100, 9900, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)

    def lambda_FB0D():
        OP_96(0xFE, 0xA8C, 0x0, 0x251C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FB0D)
    Sleep(100)

    def lambda_FB2A():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0x251C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_FB2A)
    WaitChrThread(0x103, 1)
    EndChrThread(0xC, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)

    ChrTalk(
        0x104,
        (
            "#00306F#12PWow, doom and gloom on\x01",
            "each and every one of\x01",
            "your faces, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt's none of your\x01",
            "business... Is what I'd\x01",
            "like to say anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P...Ah, I can't deny it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POf all things, why did\x01",
            "Arios...\x02\x03",
            "*sigh*... It's too\x01",
            "shocking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI didn't get even the\x01",
            "slightest feeling he'd do\x01",
            "something like that.\x02\x03",
            "If I had to say, I guess\x01",
            "he's been visiting Orchis\x01",
            "Tower more often lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FRight... He should have\x01",
            "been going there to discuss\x01",
            "the guild's response.\x02\x03",
            "#04008FBut to think he was\x01",
            "discussing this kind of\x01",
            "plan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FActually, that's what we\x01",
            "came to ask you about.\x02\x03",
            "#00001FIs Arios still a guild\x01",
            "member?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04001F...Last night, he suddenly handed\x01",
            "in his resignation and guild\x01",
            "emblem.\x02\x03",
            "#04006FHe finished all the jobs he had and\x01",
            "gave us a plan for dealing with the\x01",
            "recent attack. How very like him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FIs that right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FArios does seem like a\x01",
            "very methodical person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P...But, his sudden\x01",
            "resignation like this is\x01",
            "a huge problem, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWhat's more, he's calling himself\x01",
            "the Secretary of the State Guard of\x01",
            "the Independent State of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI don't know what he's thinking\x01",
            "saying that, but the Erebonian\x01",
            "response is sure to be frightening.\x02\x03",
            "#5PThere's that asset freeze too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P...That's right. The\x01",
            "Calvardian response will\x01",
            "be scary too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#11P...But... It's not like\x01",
            "I can't understand what\x01",
            "Arios is feeling.\x02",
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

    def lambda_101AC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_101AC)
    Sleep(50)

    def lambda_101BC():
        TurnDirection(0xB, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_101BC)
    Sleep(50)

    def lambda_101CC():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_101CC)
    Sleep(50)

    def lambda_101DC():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_101DC)
    Sleep(50)

    def lambda_101EC():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_101EC)
    Sleep(50)

    def lambda_101FC():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_101FC)
    Sleep(50)

    def lambda_1020C():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1020C)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        "#5PScott?\x02",
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
            "#11PI'm from Crossbell City\x01",
            "too, just like Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's true that one or two\x01",
            "accidents with unknown\x01",
            "causes occur each year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI don't know the real truth, but...\x01",
            "Everyone slightly believes they're\x01",
            "caused by the Empire or Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P...That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, there haven't been\x01",
            "any such accidents\x01",
            "recently, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI think the accident five years\x01",
            "ago that Arios and his family\x01",
            "were involved in was the last.\x02",
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
        "#6P#00011FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PCould it be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003F...The Main Street transport explosion\x01",
            "and fire five years ago...\x02\x03",
            "#04008FAt first, the malfunction of the orbal\x01",
            "engine and flammable load were thought\x01",
            "to be the cause, but... There were a\x01",
            "lot of suspicious points in that case.\x02\x03",
            "#04001FAnd Arios' wife Saya passed away due\x01",
            "to it... And Shizuku lost her sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FSo that's how it went\x01",
            "down, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00208F...I heard bits and\x01",
            "pieces of that story\x01",
            "before, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FAnd so, Arios quit the\x01",
            "police and joined the\x01",
            "guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FI hung out with Arios after that,\x01",
            "but...\x02\x03",
            "Though he didn't say a single word\x01",
            "about it, he must've been carrying\x01",
            "it with him this whole time.\x02\x03",
            "#04008F...When I think about it that way,\x01",
            "I finally understand why he took\x01",
            "up that important role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008F............\x02",
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
            "#12P#00003F─Michel.\x02\x03",
            "#00001FI realize it's rude of me to ask,\x01",
            "but... Have there been any suspicious\x01",
            "points in Arios' schedule lately?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_108F5():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_108F5)
    Sleep(50)

    def lambda_10905():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_10905)
    Sleep(50)

    def lambda_10915():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_10915)
    Sleep(50)

    def lambda_10925():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10925)
    Sleep(50)

    def lambda_10935():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10935)
    Sleep(50)

    def lambda_10945():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10945)
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
            "#12P#00006FThe Commander of the State Guard...\x02\x03",
            "I think it's too important a role to\x01",
            "be taken up so suddenly.\x02\x03",
            "#00001FHe was probably laying the groundwork\x01",
            "for this with Mayor... no, with\x01",
            "President Dieter. Don't you think so?\x02\x03",
            "And not just recently either. For\x01",
            "quite some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#04008F............\x02",
    )

    CloseMessageWindow()

    def lambda_10AD6():
        TurnDirection(0xB, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_10AD6)
    Sleep(50)

    def lambda_10AE6():
        TurnDirection(0xA, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_10AE6)
    Sleep(50)

    def lambda_10AF6():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_10AF6)
    Sleep(50)

    def lambda_10B06():
        TurnDirection(0xC, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_10B06)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    def lambda_10B26():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10B26)

    def lambda_10B33():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10B33)

    def lambda_10B40():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10B40)

    ChrTalk(
        0xB,
        "#12PMichel...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't believe this! Is\x01",
            "it true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FIt's true that his whereabouts\x01",
            "conflicted from time to time in\x01",
            "his various reports.\x02\x03",
            "#04008FI thought that number of mistakes\x01",
            "was only natural given the number\x01",
            "of jobs he was carrying, but...\x02\x03",
            "#04001F...Rethinking it now, it's\x01",
            "actually extremely rare for him\x01",
            "to make mistakes in his reports.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Then, those are the\x01",
            "times he was in contact\x01",
            "with Dieter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003F...I think it's safe to\x01",
            "assume that.\x02\x03",
            "#04001FMy god, Lloyd. You're so\x01",
            "observant, it's scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo... I'm sorry to have\x01",
            "said something so rude.\x02\x03",
            "#00003FBut while I'm being rude,\x01",
            "I'd like to ask you\x01",
            "something.\x02\x03",
            "#00008FRegarding the discrepancies\x01",
            "between Arios' schedule and\x01",
            "whereabouts─\x02\x03",
            "#00013FDo you remember any of them\x01",
            "from half a year ago or\x01",
            "more?\x02",
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

    def lambda_10F09():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10F09)

    def lambda_10F16():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10F16)
    Sleep(50)

    def lambda_10F26():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_10F26)
    Sleep(50)

    def lambda_10F36():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_10F36)
    Sleep(50)

    def lambda_10F46():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_10F46)
    Sleep(50)

    def lambda_10F56():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10F56)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        (
            "#6P#00105FHalf a year ago, you\x01",
            "say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200F...Back when Dieter\x01",
            "wasn't even the mayor\x01",
            "yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FH-Hmm... I don't\x01",
            "remember too well from\x01",
            "that far back, but...\x02\x03",
            "#04005FAh, but that happened,\x01",
            "didn't it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1105B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1105B)
    Sleep(50)

    def lambda_1106B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1106B)

    def lambda_11078():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11078)

    ChrTalk(
        0x101,
        "#12P#00005FThat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04004FOn the final day of the\x01",
            "Anniversary Festival.\x02\x03",
            "#04000FHe was away at a job in\x01",
            "Remiferia, but...\x02\x03",
            "He suddenly canceled it\x01",
            "and failed to report it.\x02",
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
        "#12P#00011FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04005FWhen I realized it later I asked him\x01",
            "about it. He said only that he's\x01",
            "been busy and neglected to do so.\x02\x03",
            "#04001F...What? Are you worried about\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PWell that Anniversary\x01",
            "Festival had one hell of\x01",
            "a punishing schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PEven if that report had an\x01",
            "inconsistency in it, I think\x01",
            "it's perfecty understandable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00008F#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108F...The last day of the\x01",
            "Anniversary Festival...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe last day is when\x01",
            ""that" happened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PHow is that and this\x01",
            "connected?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F...I don't know. But I\x01",
            "feel there must be some\x01",
            "connection.\x02\x03",
            "#00008FUp until now, we've been\x01",
            "so busy. We let point\x01",
            "after point pass us by.\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_114A0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_114A0)
    Sleep(50)

    def lambda_114B0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_114B0)

    ChrTalk(
        0x101,
        "#12P#00011FSorry, excuse me.\x02",
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
            "#00001FCrossbell Police,\x01",
            "Special Support Sec──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Youth's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hmm? Don't you mean\x01",
            ""Crossbell State Guard\x01",
            "Special Support Section"?\x02",
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
            "#00013F...You're...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Youth's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hahaha... Now then, I\x01",
            "wonder just who I am?\x02\x03",
            "I'll give you a nice\x01",
            "present if you get it\x01",
            "right!\x02",
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
            "#00006F...I've had enough of\x01",
            "your pointless quizzes.\x02\x03",
            "#00010FWhat in the world\x01",
            "brought you to\x01",
            "Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Youth's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Now, now, it's seems I'm not\x01",
            "very well liked.\x02\x03",
            "Things seem quite flashy\x01",
            "here. And you mean to tell me\x01",
            "we can't have a little chat?\x02\x03",
            "Well, your loss, I suppose.\x02",
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
            "#00013F............\x02\x03",
            "#00006F...Understood. Where do\x01",
            "we go?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Youth's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crimson & Co.... Or\x01",
            "perhaps I should say the\x01",
            "former Revache Building.\x02\x03",
            "The president's room\x01",
            "that's there, I think.\x02",
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
            "#00008FThe basement, huh...\x01",
            "Understood.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Youth's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'll be waiting then.\x02",
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
            "#6P#00101FWas it Cao? He's\x01",
            "missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FHe contacted us not long\x01",
            "ago when Randy went\x01",
            "missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FReally?\x02",
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
            "#5P#00003F─No, it's not him.\x02\x03",
            "#00013FIt's Captain Lechter of\x01",
            "the Imperial Army.\x02",
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
        "#6P#00107FWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FThat guy... So he came\x01",
            "to Crossbell again, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12P...I really do wonder\x01",
            "what the hell he's doing\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FHe said he wants to speak with us at the old\x01",
            "Revache building.\x02\x03",
            "#00001FWhile it would be extremely careless not to\x01",
            "consider his connection with Red\x01",
            "Constellation... we have no choice but to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FNothing ventured,\x01",
            "nothing gained, they\x01",
            "say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F...Though I think it's\x01",
            "best if we're fully\x01",
            "prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FYou guys must have it\x01",
            "tough too...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11D14():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11D14)
    Sleep(50)

    def lambda_11D24():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11D24)
    Sleep(50)

    def lambda_11D34():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11D34)
    Sleep(50)

    def lambda_11D44():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11D44)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x9,
        (
            "#11PYou're going up against\x01",
            "a tough opponent, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PArundel of the\x01",
            "Intelligence Division...\x01",
            "He's nothing but trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIf he's too much for you to\x01",
            "handle, we'll back you up,\x01",
            "so don't hold back, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PRight. We'd be paying\x01",
            "you back for the\x01",
            "Marshlands.\x02",
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
            "#12P#00204FIf it looks like we can't\x01",
            "handle it then please,\x01",
            "lend us your aid.\x02",
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

    # Function_30_F659 end

    def Function_31_11FD2(): pass

    label("Function_31_11FD2")

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
    SetChrName("Chairman MacDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W─In that case, was the referendum\x01",
            "on the question of independence a\x01",
            "basis?\x02\x03",
            "No. That question was to decide\x01",
            "only whether Crossbell should make\x01",
            "a formal "declaration of intent".\x02\x03",
            "The State Guard and Independent\x01",
            "State of Crossbell...\x02\x03",
            "To say nothing of the President and\x01",
            "his government. By no means are any\x01",
            "of them tied to legitimacy!\x07\x00\x02",
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

    # Function_31_11FD2 end

    def Function_32_122A4(): pass

    label("Function_32_122A4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3020, 1700, 4270, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22460, 0)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12425")
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

    def lambda_12370():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12370)

    def lambda_12381():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12381)
    Sleep(50)

    def lambda_1239E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1239E)

    def lambda_123AF():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_123AF)
    Sleep(700)

    def lambda_123CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_123CC)

    def lambda_123DD():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_123DD)
    Sleep(50)

    def lambda_123FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_123FA)

    def lambda_1240B():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1240B)
    Jump("loc_126A6")

    label("loc_12425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12568")
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

    def lambda_124B3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_124B3)

    def lambda_124C4():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_124C4)
    Sleep(50)

    def lambda_124E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_124E1)

    def lambda_124F2():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_124F2)
    Sleep(700)

    def lambda_1250F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1250F)

    def lambda_12520():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12520)
    Sleep(50)

    def lambda_1253D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_1253D)

    def lambda_1254E():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1254E)
    Jump("loc_126A6")

    label("loc_12568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_126A6")
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

    def lambda_125F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_125F6)

    def lambda_12607():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12607)
    Sleep(50)

    def lambda_12624():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_12624)

    def lambda_12635():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12635)
    Sleep(700)

    def lambda_12652():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12652)

    def lambda_12663():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12663)
    Sleep(50)

    def lambda_12680():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_12680)

    def lambda_12691():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_12691)

    label("loc_126A6")

    OP_68(-2140, 1300, 5160, 3000)
    OP_6F(0x1)
    WaitChrThread(0x1A2, 1)

    ChrTalk(
        0x1A2,
        (
            "#12PThis is the Bracer Guild\x01",
            "- Crossbell Branch...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00005F...Shing? Why are you\x01",
            "hiding?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1275A")

    def lambda_1273A():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1273A)
    Sleep(50)

    def lambda_1274A():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1274A)
    Sleep(300)
    Jump("loc_127B1")

    label("loc_1275A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12788")

    def lambda_12768():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12768)
    Sleep(50)

    def lambda_12778():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12778)
    Sleep(300)
    Jump("loc_127B1")

    label("loc_12788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_127B1")

    def lambda_12796():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12796)
    Sleep(50)

    def lambda_127A6():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_127A6)
    Sleep(300)

    label("loc_127B1")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#12PS-Shut up! None of your\x01",
            "business!\x02",
        )
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
            "#5P#N#04005FMy, you guys... What are\x01",
            "you doing with that cute\x01",
            "boy over there?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_128A5")

    def lambda_12875():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12875)
    Sleep(50)

    def lambda_12885():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12885)
    Sleep(50)

    def lambda_12895():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12895)
    Sleep(300)
    Jump("loc_1291C")

    label("loc_128A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_128E3")

    def lambda_128B3():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_128B3)
    Sleep(50)

    def lambda_128C3():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_128C3)
    Sleep(50)

    def lambda_128D3():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_128D3)
    Sleep(300)
    Jump("loc_1291C")

    label("loc_128E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1291C")

    def lambda_128F1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_128F1)
    Sleep(50)

    def lambda_12901():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12901)
    Sleep(50)

    def lambda_12911():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12911)
    Sleep(300)

    label("loc_1291C")


    ChrTalk(
        0x8,
        (
            "#5P#N#04000FYou'll be in the way\x01",
            "there, so please come\x01",
            "this way.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00105FO-Okay...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(330, 1300, 10820, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21390, 0)
    OP_93(0x8, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12A7B")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x104, 1640, 0, 8800, 0)

    def lambda_12A0A():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_12A0A)
    Sleep(50)

    def lambda_12A27():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12A27)
    Sleep(50)

    def lambda_12A44():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A44)
    Sleep(50)

    def lambda_12A61():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12A61)
    Jump("loc_12BFC")

    label("loc_12A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12B3E")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x109, 1640, 0, 8800, 0)

    def lambda_12ACD():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_12ACD)
    Sleep(50)

    def lambda_12AEA():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12AEA)
    Sleep(50)

    def lambda_12B07():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12B07)
    Sleep(50)

    def lambda_12B24():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12B24)
    Jump("loc_12BFC")

    label("loc_12B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_12BFC")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x105, 1640, 0, 8800, 0)

    def lambda_12B90():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_12B90)
    Sleep(50)

    def lambda_12BAD():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12BAD)
    Sleep(50)

    def lambda_12BCA():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12BCA)
    Sleep(50)

    def lambda_12BE7():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12BE7)

    label("loc_12BFC")

    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x8,
        (
            "#04000F#5PAnd, just who is that\x01",
            "boy, I wonder?\x02\x03",
            "#04005FCould he be lost and\x01",
            "looking for his parents?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FUmm, I'm not sure how to\x01",
            "say this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PH-Hey, hey you! Is the\x01",
            "Sword Saint of Wind here\x01",
            "right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004F#5PMy, you have quite the\x01",
            "way of speaking.\x02\x03",
            "#04000FAnd, if I told you he\x01",
            "isn't?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PI-I see... Oh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04005F#5PWhy are you relieved?\x02\x03",
            "#04003FHmm. His words, actions and\x01",
            "clothes...\x02\x03",
            "#04000FI see― This boy must be\x01",
            "connected to Heiyue. And an\x01",
            "elder's grandson, no less.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12E75")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jump("loc_12F52")

    label("loc_12E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12EE6")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jump("loc_12F52")

    label("loc_12EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_12F52")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_12F52")


    ChrTalk(
        0x102,
        "#12P#00105FW-Why do you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011F#5PUhuhu, it was just a\x01",
            "guess. Looks like I was\x01",
            "right, though.\x02\x03",
            "#04001FAh, by the way, boys\x01",
            "must be careful not to\x01",
            "get tricked, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1307A")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_13157")

    label("loc_1307A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_130EB")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_13157")

    label("loc_130EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_13157")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_13157")


    ChrTalk(
        0x101,
        "#12P#00012FY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHuh? This guy's appearance\x01",
            "and personality aren't\x01",
            "normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PThat must be why this is\x01",
            "the Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006F#5PHmm? You've been rude this\x01",
            "whole time. You'll make a\x01",
            "fine Heiyue member.\x02\x03",
            "#04008FI think he'll only get\x01",
            "worse.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_13295")

    ChrTalk(
        0x104,
        "#12P#00303FYeah, I agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_132F1")

    label("loc_13295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_132C9")

    ChrTalk(
        0x109,
        "#12P#10106FYes, I feel the same.\x02",
    )

    CloseMessageWindow()
    Jump("loc_132F1")

    label("loc_132C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_132F1")

    ChrTalk(
        0x105,
        "#12P#10304FHehe, I agree.\x02",
    )

    CloseMessageWindow()

    label("loc_132F1")


    ChrTalk(
        0x8,
        (
            "#04000F#5PBut even so, why might\x01",
            "you be looking out for\x01",
            "Arios so much?\x02\x03",
            "It's not the case that\x01",
            "we bear any particular\x01",
            "grudge against Heiyue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PH-Hmph... You're one to talk.\x01",
            "You've gotten in my grandfather and\x01",
            "the others' way countless times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PWhether it's from the Sword Saint of\x01",
            "Wind or the Immovable, do you know\x01",
            "how many losses we've suffered?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FThe Immovable?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004F#5PYes, Zin the Immovable―\x02\x03",
            "#04000FHe's a Republican A-rank\x01",
            "bracer and a master of\x01",
            "Taito Style martial arts.\x02\x03",
            "It's been rare lately, but\x01",
            "in the past he's helped our\x01",
            "branch a number of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FThe Taito Style... If I\x01",
            "remember right, that's\x01",
            "Ling's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000F#5PYes, he was Ling's\x01",
            "senior. Naturally, he's\x01",
            "incredibly strong.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_13627")

    ChrTalk(
        0x104,
        (
            "#12P#00300FI see. You'd have to be,\x01",
            "to be a bracer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136BB")

    label("loc_13627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1367A")

    ChrTalk(
        0x109,
        (
            "#12P#10100FThat makes sense. The\x01",
            "guild is full of great\x01",
            "people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136BB")

    label("loc_1367A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_136BB")

    ChrTalk(
        0x105,
        (
            "#12P#10300FHehe. You'd have to be,\x01",
            "to be a bracer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136BB")


    ChrTalk(
        0x1A2,
        (
            "#12PThat may be, but the biggest\x01",
            "problem with the guild is\x01",
            "that code you guys have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PI don't know if it's a guiding principle\x01",
            "or whatever, but you guys just do whatever\x01",
            "you want in the name of "civilian safety"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004F#5PHaha. If even if we follow that\x01",
            "principle, "noninterference with state\x01",
            "sovereignty" sometimes limits it.\x02\x03",
            "#04005F―Say, boy. Just how much do you know\x01",
            "at your age?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIndeed... To be honest,\x01",
            "I didn't think you knew\x01",
            "that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHeh. Flattery will get\x01",
            "you nowhere. Anyway, the\x01",
            "guys at the guild are―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006F#5PAlright, that's enough with\x01",
            "your criticism of the guild.\x01",
            "Kids will be kids, after all.\x02\x03",
            "#04000FBy the way, KeA and Shizuku\x01",
            "are on 2F right now.\x02\x03",
            "You should have a chat with\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, come to think of\x01",
            "it, KeA is here right\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FThat's right. Let's have\x01",
            "the kids talk with each\x01",
            "other for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PW-What? Who's that?\x02",
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

    # Function_32_122A4 end

    def Function_33_13A93(): pass

    label("Function_33_13A93")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1940, 1100, 44370, 0)
    MoveCamera(36, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20320, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AFD")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06000.itp")

    label("loc_13AFD")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_13B57")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x104, -2190, 0, 45050, 90)
    Jump("loc_13BF6")

    label("loc_13B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_13BA9")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x109, -2190, 0, 45050, 90)
    Jump("loc_13BF6")

    label("loc_13BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_13BF6")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x105, -2190, 0, 45050, 90)

    label("loc_13BF6")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_END)), "loc_13C9C")

    def lambda_13C05():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_13C05)
    Sleep(50)

    def lambda_13C15():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_13C15)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#11P#01102FAh, Lloyd and friends.\x01",
            "Ehehe, what's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FHello. It looks like you\x01",
            "guys are working.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E61")

    label("loc_13C9C")

    SetScenarioFlags(0x14D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#11P#01110FAh, it's Lloyd and\x01",
            "friends!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        "#11P#06002FAh... Hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FHey, KeA. Looks like\x01",
            "you're having fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FIt's been a while since\x01",
            "we've seen you, Shizuku.\x02",
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
            "Haha, it's been a while.\x02\x03",
            "It looks like you guys\x01",
            "are working.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_13E61")


    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, I guess you could\x01",
            "say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PWhat's with these kids.\x01",
            "You know them?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#11P#01105FHuh? Who's he~?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11P#06005FA little boy...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#6PW-Who are you calling\x01",
            "little!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI'm Shing! Grandson of a Heiyue\x01",
            "elder and the man who bears the\x01",
            "burden of its future!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11P#06010FS-Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01105FWow. You're so small,\x01",
            "but an adult the same as\x01",
            "Lloyd and the others!\x02\x03",
            "#01109FYou're that great, even\x01",
            "though you're that\x01",
            "small, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PS-Small, small, small!\x01",
            "Stop saying that!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_14148")
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
            "#11P#00304FHaha. Keddo, destroyer\x01",
            "of impertinent boys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14288")

    label("loc_14148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_141DA")
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
            "#11P#10109FAhaha... (That's KeA for\x01",
            "you.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14288")

    label("loc_141DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_14288")
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
            "#11P#10309FHaha. Against KeA, even\x01",
            "a grandson of a Heiyue\x01",
            "elder can't win.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14288")

    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00109FHaha, Shing.\x02\x03",
            "This is KeA and Shizuku.\x02\x03",
            "#00100FThey're a little older\x01",
            "than you, I think?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FAh, by the way, Shizuku\x01",
            "is Arios' daughter. You\x01",
            "mentioned him earlier.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#6PHah!? That Divine Blade\x01",
            "of Wind's...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PY-You're a sword master,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PYour eyes have been closed this\x01",
            "whole time. You're practicing\x01",
            "that Mind's Eye thing, right!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_14490")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1453D")

    label("loc_14490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_144E9")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1453D")

    label("loc_144E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1453D")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_1453D")


    ChrTalk(
        0xD,
        "#11P#01105FMind's eye?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FMind's Eye, huh... Why\x01",
            "do you know something\x01",
            "like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FAhaha... Umm, I actually\x01",
            "can't see.\x02\x03",
            "Although my hearing is good\x01",
            "because of it, I'm not as\x01",
            "cool as my father, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6PI-I'm terribly sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PThat was ungentlemanly\x01",
            "of me... Please forgive\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FHaha, don't worry about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005F(Huuuh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102F(Haha. I knew he was a\x01",
            "good kid deep down.)\x02",
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

    # Function_33_13A93 end

    def Function_34_1476D(): pass

    label("Function_34_1476D")

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
        (
            "#11P#01110FAh, it's Lloyd and\x01",
            "friends!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xE, 0xFF)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x10E, 0x1F4)

    ChrTalk(
        0xE,
        "#11P#06002FAh... Hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FHey, KeA. Looks like\x01",
            "you're having fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIt's been a while since\x01",
            "we've seen you, Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11P#06000FHaha, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FWow, so this girl is the\x01",
            "daughter of the Divine\x01",
            "Blade of Wind, huh.\x02\x03",
            "#10309FHaha. She's cute, just\x01",
            "like I've heard.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_14BDD")

    ChrTalk(
        0x109,
        (
            "#6P#10109FJust like I told you,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#11P#06005FThis voice is... It's\x01",
            "Noｱl, isn't it?\x02\x03",
            "#06002FYou helped me look for a\x01",
            "present for my father\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#6P#10105FWah, y-you remember\x01",
            "that?\x02\x03",
            "#10109FWe weren't together very\x01",
            "long... Haha, I'm happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FEhehe, KeA said you guys\x01",
            "had some new members.\x02\x03",
            "#06000FAnd... Are these them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWazy Hemisphere. Haha,\x01",
            "pleased to meet you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DA2")

    label("loc_14BDD")


    ChrTalk(
        0x109,
        (
            "#6P#10109FYeah, you're just like\x01",
            "Fran said!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#11P#06005FUmm... Who are they?\x02\x03",
            "KeA said you had some\x01",
            "new members. Could they\x01",
            "be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FYeah. Come to think of it,\x01",
            "we haven't met.\x02\x03",
            "#10109FI'm Noｱl Seeker. Would you\x01",
            "understand if I told you\x01",
            "I'm Fran's older sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06005FAh, so you're Fran's... Now\x01",
            "that you mention to it, you\x01",
            "seem similar to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FI'm Wazy Hemisphere.\x01",
            "Pleased to meet you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DA2")


    ChrTalk(
        0xE,
        "#11P#06002FYes, same here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01109FC'mon! Ya gotta\x01",
            "introduce yourself,\x01",
            "Shizuku!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06005FAh... That's right,\x01",
            "then.\x02",
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
            "Umm, I'm KeA's friend,\x01",
            "Shizuku MacLaine.\x02\x03",
            "I understand you have been\x01",
            "helping my father a great\x01",
            "deal, Support Section.\x02\x03",
            "I would like to thank you\x01",
            "for that once again.\x02",
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
            "#6P#00102FAhaha, well... You could\x01",
            "say we're the ones being\x01",
            "helped by Arios, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FHmm, I guess you could\x01",
            "say that...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#11P#06010FT-That's not true.\x02\x03",
            "In that incident\x01",
            "earlier, you all helped\x01",
            "everyone a lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha, this kid is always\x01",
            "on the ball, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01102FHey, are you guys gonna\x01",
            "play with KeA and\x01",
            "Shizuku too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FAh, no. Because Shizuku's\x01",
            "here, I just thought we'd\x01",
            "say hi.\x02\x03",
            "#00000FWe've got work to do. But\x01",
            "play with Shizuku for us as\x01",
            "much as you like today, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11P#01109FYeah, got it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FUmm, do your best with\x01",
            "your work, everyone.\x02",
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

    # Function_34_1476D end

    def Function_35_15220(): pass

    label("Function_35_15220")

    EventBegin(0x1)
    SetChrPos(0x0, -2110, 0, 740, 0)
    EventEnd(0x4)
    Return()

    # Function_35_15220 end

    SaveToFile()

Try(main)
