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
        "Function_5_4CE8",         # 05, 5
        "Function_6_54D8",         # 06, 6
        "Function_7_586A",         # 07, 7
        "Function_8_5A3D",         # 08, 8
        "Function_9_6415",         # 09, 9
        "Function_10_6A89",        # 0A, 10
        "Function_11_73F2",        # 0B, 11
        "Function_12_7986",        # 0C, 12
        "Function_13_7A08",        # 0D, 13
        "Function_14_7B0D",        # 0E, 14
        "Function_15_8751",        # 0F, 15
        "Function_16_8813",        # 10, 16
        "Function_17_8CF9",        # 11, 17
        "Function_18_8ED0",        # 12, 18
        "Function_19_9189",        # 13, 19
        "Function_20_9190",        # 14, 20
        "Function_21_9BF3",        # 15, 21
        "Function_22_A008",        # 16, 22
        "Function_23_A9A9",        # 17, 23
        "Function_24_B353",        # 18, 24
        "Function_25_C0D3",        # 19, 25
        "Function_26_C64E",        # 1A, 26
        "Function_27_C698",        # 1B, 27
        "Function_28_E693",        # 1C, 28
        "Function_29_F239",        # 1D, 29
        "Function_30_FA66",        # 1E, 30
        "Function_31_12471",       # 1F, 31
        "Function_32_1273B",       # 20, 32
        "Function_33_13F48",       # 21, 33
        "Function_34_14C67",       # 22, 34
        "Function_35_1575A",       # 23, 35
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DD")
    Jump("loc_ACC")

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F0")
    Jump("loc_ACC")

    label("loc_9F0")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "#04000FOh yeah, I started\x01",
            "playing that "Pom!" orbal\x01",
            "game the other day.\x02\x03",
            "#04011FYou guys wanna go?\x01",
            "Hu hu, if you're free,\x01",
            "let's have a match㈱\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            ""Michel's Account"\x07\x00",
            " was obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 5)
    OP_E4(0x3)
    TalkEnd(0x8)
    Return()

    label("loc_ACC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_F70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC3")

    ChrTalk(
        0x8,
        "#04001FI see... So you defeated Arios.\x02",
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
            "#00306FBut he really was\x01",
            "tremendously strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003F...Arios is a genuine master,\x01",
            "in the true sense of it.\x02\x03",
            "What's more, he did not get to where he is\x01",
            "today merely through talent... His strength\x01",
            "was obtained through extraordinary training.\x02\x03",
            "#04011FHu hu. If you all overcame him,\x01",
            "then you've gotten much stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FTo be honest, I think we were also lucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt was a hard fight, but...\x01",
            "We finally managed to overtake him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FHu hu. Then all that's left\x01",
            "is that KeA kid, right?\x02\x03",
            "#04000FShizuku's waiting too, so please,\x01",
            "do whatever you need to bring\x01",
            "both Arios and KeA back with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, of course...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 6)
    Jump("loc_F6B")

    label("loc_DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC9")

    ChrTalk(
        0x8,
        (
            "#04003FArios is a genuine master,\x01",
            "in the true sense of it.\x02\x03",
            "#04011FHu hu. If you all overcame him,\x01",
            "then you've gotten much stronger.\x02\x03",
            "#04000FShizuku's waiting too, so please,\x01",
            "do whatever you need to bring\x01",
            "both Arios and KeA back with you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F6B")

    label("loc_EC9")


    ChrTalk(
        0x8,
        (
            "#04004FHu hu. All that's left\x01",
            "is to take back KeA.\x02\x03",
            "#04000FShizuku's waiting too, so please,\x01",
            "do whatever you need to bring\x01",
            "both Arios and KeA back with you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6B")

    Jump("loc_4CE4")

    label("loc_F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_17A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1529")

    ChrTalk(
        0x8,
        (
            "#04000FOh, it's you guys... Good\x01",
            "work arresting the President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe'd like to thank the Guild\x01",
            "for their cooperation, too.\x02\x03",
            "Without everyone's help, I don't\x01",
            "think it would have been possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FUhuhu, don't worry about it.\x02\x03",
            "#04004FAnd don't worry about the city.\x01",
            "We'll do something\x01",
            "about it on our end.\x02\x03",
            "#04000FFortunately, we'll be able\x01",
            "to restart Guild activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FNow that you mention it, the Guild members are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYes. Ever since the barrier was released, they\x01",
            "split up and spread throughout the state.\x02\x03",
            "#04003FBecause we were unable to leave for\x01",
            "awhile, problems happened everywhere\x01",
            "and now we're drowning in requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FThat...sounds tough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWe'd really like to\x01",
            "help you guys, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FPlease, leave everything to us.\x02\x03",
            "#04001FInstead, that strange "huge tree"\x01",
            "that appeared in the Marshlands...\x01",
            "You guys handle that.\x02\x03",
            "That's the perfect way to divide our\x01",
            "duties right now. Don't you agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes... You're right.\x02\x03",
            "KeA is there...\x01",
            "And Mr. Arios as well.\x02\x03",
            "#00001FWith our own hands, we'll do whatever\x01",
            "we have to to bring them back...!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1414")

    ChrTalk(
        0x10A,
        "#00603F...Naturally.\x02",
    )

    CloseMessageWindow()

    label("loc_1414")


    ChrTalk(
        0x8,
        (
            "#04004FUhuhu, that's why you guys are who you are.\x02\x03",
            "#04001FHonestly speaking, Arios' power\x01",
            "is in a whole other league.\x02\x03",
            "But you, I'm sure that you, who worked\x01",
            "with him, know that better than anyone.\x02\x03",
            "#04011FGo all out, Special Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FRight!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 5)
    Jump("loc_179D")

    label("loc_1529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B6")

    ChrTalk(
        0x8,
        (
            "#04003FHonestly speaking, Arios' power\x01",
            "is in a whole other league.\x02\x03",
            "#04001FBut you, I'm sure that you, who worked\x01",
            "with him, know that better than anyone.\x02\x03",
            "Though I'm sure a hard fight is waiting\x01",
            "for you, please, do whatever you must to\x01",
            "bring both him and KeA back with you.\x02\x03",
            "#04011FHu hu. As punishment for handing in his resignation,\x01",
            "I'll have to give him a stern lecture.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179D")

    label("loc_16B6")


    ChrTalk(
        0x8,
        (
            "#04003FThough I'm sure a hard fight is waiting\x01",
            "for you, please, do whatever you must to\x01",
            "bring both him and KeA back with you.\x02\x03",
            "#04011FHu hu. As punishment for handing in his resignation,\x01",
            "I'll have to give him a stern lecture.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179D")

    Jump("loc_4CE4")

    label("loc_17A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1968")

    ChrTalk(
        0x8,
        (
            "#04006FEver since the declaration of independence,\x01",
            "we haven't been able to act freely.\x02\x03",
            "Although the Guild is supposed to remain neutral,\x01",
            "we can't act disregarding the order of the\x01",
            "independent state that is being created.\x02\x03",
            "#04001FHowever, this time is different. Now\x01",
            "that citizens are exposed to danger,\x01",
            "the Guild cannot abandon them.\x02\x03",
            "#04003FBreak into Orchis Tower\x01",
            "and arrest the President... \x01",
            "We will help you out too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19E2")

    label("loc_1968")


    ChrTalk(
        0x8,
        (
            "#04003FPlease contact me when it's\x01",
            "time to begin the operation.\x02\x03",
            "#04001FWe'll carefully prepare\x01",
            "until that time too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E2")

    Jump("loc_4CE4")

    label("loc_19E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B05")

    ChrTalk(
        0x8,
        (
            "#04006F*sigh*. I can't believe Arios even\x01",
            "falsified his schedule to meet with\x01",
            "the mayor... no, the President.\x02\x03",
            "Even though I thought it was\x01",
            "unnatural, I completely missed it.\x02\x03",
            "#04008FI wonder if he's been hung up on\x01",
            "Shizuku's accident this whole time...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BCE")

    label("loc_1B05")


    ChrTalk(
        0x8,
        (
            "#04003FAnyway... Now that independence was\x01",
            "declared, we at the Guild have to think about\x01",
            "how we'll deal with it from a neutral standpoint.\x02\x03",
            "#04008FWe've got to contact the Bracer HQ about this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCE")

    Jump("loc_4CE4")

    label("loc_1BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_END)), "loc_22DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2206")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_END)), "loc_1E46")

    ChrTalk(
        0x8,
        (
            "#04005FAh, it's you guys...\x01",
            "Have you seen Arios?\x02\x03",
            "#04006FHmm, he's still not back yet...\x02",
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
            "#00005FIf you're looking for Mr. Arios,\x01",
            "we just saw him at the cemetery.\x02\x03",
            "We told him you're\x01",
            "looking for him, but...\x01",
            "He's not back yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FNo, not yet...\x01",
            "I see, so he went to the cemetery.\x02\x03",
            "#04000F...Well, it's not rare for him to\x01",
            "visit Mrs. Saya's grave. I guess\x01",
            "he'll be back before long.\x02\x03",
            "#04011FSorry for bothering you.\x01",
            "We'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-Is that so.\x01",
            "Excuse us, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FE")

    label("loc_1E46")


    ChrTalk(
        0x8,
        (
            "#04005FAh, you guys... I'd like to\x01",
            "ask you a little something.\x02\x03",
            "#04001FHave you seen Arios anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHuh? If you're looking for\x01",
            "Mr. Arios, we just saw\x01",
            "him at the cemetery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FIt looked like he was\x01",
            "visiting his wife's grave...\x01",
            "Has something happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYes. He's supposed to go to Orchis\x01",
            "Tower for a discussion with the\x01",
            "mayor on the Guild's stance...\x02\x03",
            "#04006FArios broke his ENIGMA II during\x01",
            "the attack the other day.\x02\x03",
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
            "#04003FBut, I see... \x01",
            "Arios went to the cemetery.\x02\x03",
            "#04000FWell, it's not rare for him to\x01",
            "visit Mrs. Saya's grave. I guess\x01",
            "he'll be back before long.\x02\x03",
            "#04011FSorry for bothering you.\x01",
            "We'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-Is that so.\x01",
            "Excuse us, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21FE")

    SetScenarioFlags(0x18E, 0)
    Jump("loc_22D6")

    label("loc_2206")


    ChrTalk(
        0x8,
        (
            "#04008FBecause Crossbell is like this, we haven't\x01",
            "had time to deal with the Marshlands'\x01",
            "Pleroma Grass or the "Society".\x02\x03",
            "#04006F*sigh*. Maybe I should make a request\x01",
            "for reinforcements to the Bracer HQ.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D6")

    Jump("loc_4CE4")

    label("loc_22DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_281F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2623")

    ChrTalk(
        0x8,
        (
            "#04005FAh, you guys... I'd like to\x01",
            "ask you a little something.\x02\x03",
            "#04001FHave you seen Arios anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FNo, we haven't seen him today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FDid something happen\x01",
            "to Mr. Arios?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYes. He's supposed to go to Orchis\x01",
            "Tower for a discussion with the\x01",
            "mayor on the Guild's stance...\x02\x03",
            "#04006FArios broke his ENIGMA II during\x01",
            "the attack the other day.\x02\x03",
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
        "#00303FHmm. Maybe he took a detour on the way back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe understand. We'll\x01",
            "speak to Mr. Arios\x01",
            "if we see him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FThanks, it would really help if you did\x01",
            "that for me. I'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 7)
    Jump("loc_281A")

    label("loc_2623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274A")

    ChrTalk(
        0x8,
        (
            "#04003FBecause Crossbell is like this,\x01",
            "the Guild is very busy right now.\x02\x03",
            "#04008FWe haven't had time to deal with the\x01",
            "Marshlands' Pleroma Grass or the\x01",
            ""Society" that's invaded Crossbell...\x02\x03",
            "#04006F*sigh*. Maybe I should make a request\x01",
            "for reinforcements to the Bracer HQ.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_281A")

    label("loc_274A")


    ChrTalk(
        0x8,
        (
            "#04008FBecause Crossbell is like this, we haven't\x01",
            "had time to deal with the Marshlands'\x01",
            "Pleroma Grass or the "Society".\x02\x03",
            "#04006F*sigh*. Maybe I should make a request\x01",
            "for reinforcements to the Bracer HQ.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_281A")

    Jump("loc_4CE4")

    label("loc_281F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283E")
    TalkEnd(0x8)
    Call(0, 23)
    Return()

    label("loc_283E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_299C")

    ChrTalk(
        0x8,
        (
            "#04001FIf this situation goes on for too much longer,\x01",
            "the Guild will have no choice but to act.\x02\x03",
            "#04003FBut, though the two major powers\x01",
            "ridiculed the CGF before, this\x01",
            "will give them even more material.\x02\x03",
            "#04001FIf possible, I'd like it to be the final\x01",
            "option... But when civilian lives are\x01",
            "on the line, we can't wait too long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A7A")

    label("loc_299C")


    ChrTalk(
        0x8,
        (
            "#04001FIf this situation goes on for too much longer,\x01",
            "the Guild will have no choice but to act.\x02\x03",
            "#04006FIf possible, I'd like to be the final\x01",
            "option... But when civilian lives are\x01",
            "on the line, we can't wait too long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7A")

    Jump("loc_4CE4")

    label("loc_2A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_2C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8A")

    ChrTalk(
        0x8,
        (
            "#04003FBoth Ling and Eolia are capable\x01",
            "Bracers who are nearly A-rank.\x02\x03",
            "#04008FTo think both of them were stranded\x01",
            "in a place like the Marshlands\x01",
            "without contacting us...\x02\x03",
            "#04001FI don't know what's there.\x01",
            "Please, be extremely careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C35")

    label("loc_2B8A")


    ChrTalk(
        0x8,
        (
            "#04008FTo think Ling and Eolia were stranded\x01",
            "in a place like the Marshlands\x01",
            "without contacting us...\x02\x03",
            "#04001FI don't know what's there.\x01",
            "Please, be extremely careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C35")

    Jump("loc_4CE4")

    label("loc_2C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_END)), "loc_2DE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA6")

    ChrTalk(
        0x8,
        (
            "#04005FAh, you all...\x01",
            "Did you learn Ling and\x01",
            "Eolia's location?\x02\x03",
            "You said you were going to use\x01",
            "the ENIGMA II's alert function.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThere are a lot of steps in the procedure,\x01",
            "but we should be able to manage.\x02\x03",
            "We'll give you the results shortly,\x01",
            "so please wait awhile longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FYes, understood.\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2DE2")

    label("loc_2DA6")


    ChrTalk(
        0x8,
        (
            "#04011FPlease, find Ling and\x01",
            "Eolia's location somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE2")

    Jump("loc_4CE4")

    label("loc_2DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E87")

    ChrTalk(
        0x8,
        (
            "#04003FIf you learn anything\x01",
            "about them, please\x01",
            "contact me immediately.\x02\x03",
            "#04001FI'll recall Arios and the others\x01",
            "depending on the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE4")

    label("loc_2E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3107")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_304D")

    ChrTalk(
        0x8,
        (
            "#04007FA communication just came in...\x01",
            "A derailment accident occurred!?\x02\x03",
            "#04006FHmm, this is troubling. Arios\x01",
            "and the others can't return from\x01",
            "their Cryptids investigation at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, that investigation's important too...\x01",
            "Please, leave this to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FOoh... But I suppose I have no choice.\x02\x03",
            "#04000FI understand. You guys will handle the derailment.\x01",
            "If there's any problem, let me know immediately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3102")

    label("loc_304D")


    ChrTalk(
        0x8,
        (
            "#04006FArios and the others can't return from\x01",
            "the Cryptids investigation immediately.\x02\x03",
            "#04000FI'm leaving the derailment to you, so\x01",
            "contact me immediately if anything happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3102")

    Jump("loc_4CE4")

    label("loc_3107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_35B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3502")

    ChrTalk(
        0x8,
        (
            "#04003FThat "Pleroma Grass" in your\x01",
            "report... To think it's linked\x01",
            "to the Church's Testaments...\x02\x03",
            "#04001FJust to be extra careful, I had Scott\x01",
            "and Ling confirm the information, but...\x02\x03",
            "Up until now, it seems those Cryptids have been\x01",
            "appearing near to where those Azure Flowers bloom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThough it's unknown whether the blooming\x01",
            "of the Azure Flowers is the root cause...\x02\x03",
            "#00200FIf you analyze the situation, it\x01",
            "appears they have something to do\x01",
            "with the appearance of the Cryptids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FBy the way, how is your\x01",
            "investigation into that going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FFor now, we've eliminated two of the\x01",
            "three Cryptids that appeared yesterday.\x02\x03",
            "#04000FAs for today, after we defeat the\x01",
            "remaining one, we'll split up and\x01",
            "re-examine the places they appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, we don't know when those\x01",
            "Cryptids will appear again.\x01",
            "Be very careful, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FYes, of course.\x02\x03",
            "#04000FI'll contact you if we learn anything,\x01",
            "so please continue your investigation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16F, 3)
    Jump("loc_35AE")

    label("loc_3502")


    ChrTalk(
        0x8,
        (
            "#04000FArios is back today, so we'll take\x01",
            "care of our part of the investigation.\x02\x03",
            "#04011FI'll contact you if we learn anything,\x01",
            "so please continue your investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AE")

    Jump("loc_4CE4")

    label("loc_35B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_37FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3780")

    ChrTalk(
        0x8,
        (
            "#04000FI'm counting on you guys to\x01",
            "handle the "Cryptids" case.\x02\x03",
            "#04006FBecause Arios is unable\x01",
            "to act right now, we're\x01",
            "shorthanded.\x02\x03",
            "#04000FPlease, somehow handle the \x01",
            "workload with Scott and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, please leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FMr. Arios can't act because\x01",
            "of Shizuku... I suppose\x01",
            "that can't be helped...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FThank you for saying so.\x02\x03",
            "#04000FPlease, continue\x01",
            "the investigation\x01",
            "in your own way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_37F9")

    label("loc_3780")


    ChrTalk(
        0x8,
        (
            "#04000FI'm counting on you guys to\x01",
            "handle the "Cryptids" case.\x02\x03",
            "Please, continue\x01",
            "the investigation\x01",
            "in your own way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F9")

    Jump("loc_4CE4")

    label("loc_37FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A99")

    ChrTalk(
        0x8,
        (
            "#04000FArios will be on security detail\x01",
            "today throughout the main session.\x02\x03",
            "Out of concern for the heads of state, \x01",
            "I can't think of a better security organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn a situation like this, it's reassuring having\x01",
            "Bracers who are in a neutral position.\x02",
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
            "#00000FYes. We'll secure the conference\x01",
            "without losing focus.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3B66")

    label("loc_3A99")


    ChrTalk(
        0x8,
        (
            "#04005FAh, that's right. Come to\x01",
            "think of it... Now that Tio's\x01",
            "back, Eolia will be overjoyed.\x02\x03",
            "#04011FHu hu. Be sure to say hi to\x01",
            "her at the conference for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F...Well, if I feel like it.\x02",
    )

    CloseMessageWindow()

    label("loc_3B66")

    Jump("loc_4CE4")

    label("loc_3B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3FE4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3CFE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9F")
    Call(0, 13)
    Jump("loc_3C6C")

    label("loc_3B9F")


    ChrTalk(
        0x8,
        (
            "#04000FI've heard the situation from Arios.\x02\x03",
            "Because the Crossbell Guild has\x01",
            "connections even abroad, we'll\x01",
            "gather a certain level of goods.\x02\x03",
            "Well, I'm sure it'll be all right,\x01",
            "so please don't worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C6C")

    Jump("loc_3CFA")

    label("loc_3C71")


    ChrTalk(
        0x8,
        (
            "#04000FI heard from Arios\x01",
            "earlier. It seems the\x01",
            "patient was saved.\x02\x03",
            "Hu hu. It's great that\x01",
            "the Archduke recognized\x01",
            "you all as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFA")

    TalkEnd(0x8)
    Return()

    label("loc_3CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F29")

    ChrTalk(
        0x8,
        (
            "#04000FSo, the Trade Conference\x01",
            "has finally started.\x02\x03",
            "#04003FOn top of handling the security,\x01",
            "we'll deal with every kind of requests.\x02\x03",
            "#04000FIf anything happens,\x01",
            "the Bracers will be\x01",
            "there immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat'll be a big help.\x02\x03",
            "#00103FWe don't know whether the "Red\x01",
            "Constellation" or "Heiyue" will act,\x01",
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
            "#04000FAnyway, we'll let you know as\x01",
            "soon as we learn anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, please.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3FDF")

    label("loc_3F29")


    ChrTalk(
        0x8,
        (
            "#04000FOn top of handling the security,\x01",
            "we'll deal with every kind of requests.\x02\x03",
            "As soon as we learn anything about\x01",
            "Red Constellation or Heiyue, we'll\x01",
            "let you know immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FDF")

    Jump("loc_4CE4")

    label("loc_3FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_461C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_409C")

    ChrTalk(
        0x8,
        (
            "#04006F*sigh*, but even so, this child\x01",
            "is a Heiyue elder's grandson.\x02\x03",
            "#04000FI'm not sure how to say this,\x01",
            "but it's an ominous sign.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4617")

    label("loc_409C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_413A")

    ChrTalk(
        0x8,
        (
            "#04000FIf you're looking for KeA, she's\x01",
            "playing with Shizuku on 2F.\x02\x03",
            "#04011FI'll look after them properly,\x01",
            "so there's no need to worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4617")

    label("loc_413A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_456B")

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
            "#00004FThanks for taking care of her.\x01",
            "You must be busy too, here at the Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FNo, she's totally welcome.\x01",
            "It's been busy lately and this\x01",
            "is a nice change of pace.\x02\x03",
            "#04009FAnd whenever I look at them, it\x01",
            "tickles my maternal instinct, as if\x01",
            "they were my very own daughters㈱\x02",
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
        "#00306FM-Maternal instincts, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04001F...What, is there a problem with that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FU-Umm... Come to think\x01",
            "of it, where is Mr. Arios?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FYeah, as soon as he took\x01",
            "Shizuku back from the hospital,\x01",
            "he headed for the Republic.\x02\x03",
            "#04004FHis requests for before the Trade Conference\x01",
            "are finished, so he's going to investigate\x01",
            "some anxiety factors in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F*sigh*, that's so much work...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FFor now then, it seems the Guild\x01",
            "is fully prepared for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FHu hu. You all should\x01",
            "get ready too, before\x01",
            "the day is out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 5)
    Jump("loc_4617")

    label("loc_456B")


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

    label("loc_4617")

    Jump("loc_4CE4")

    label("loc_461C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4874")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479D")

    ChrTalk(
        0x8,
        (
            "#04000FWe've been getting steadily more\x01",
            "requests via the orbal net lately.\x02\x03",
            "Especially on rainy days like today, we get\x01",
            "a lot of requests through the terminal.\x02\x03",
            "#04006FIt's just that, we're very\x01",
            "busy, and so we have to reject\x01",
            "the lowest priority requests.\x02\x03",
            "#04000FThere're times we send them to\x01",
            "the Support Section... Please\x01",
            "try to handle them somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_486F")

    label("loc_479D")


    ChrTalk(
        0x8,
        (
            "#04006FI'd like to handle as many\x01",
            "requests as possible, but we're\x01",
            "busy, so we have to be selective.\x02\x03",
            "#04000FThere're times we send our\x01",
            "overflow to the Support Section...\x01",
            "Please try to handle them somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486F")

    Jump("loc_4CE4")

    label("loc_4874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C49")

    ChrTalk(
        0x8,
        (
            "#04000FBy the way, once Arios gets\x01",
            "back from Altair, he's going\x01",
            "to Remiferia immediately.\x02\x03",
            "Because the Archduke is coming to\x01",
            "the next month's Trade Conference,\x01",
            "he'll be helping prepare for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Arios is very\x01",
            "busy too, isn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FYeah, and it's\x01",
            "not just Arios...\x02\x03",
            "#04000FIt's certain that everyone's gotten\x01",
            "busy preparing for the conference.\x02",
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
            "#10300FHu hu. So I guess\x01",
            "the Guild's labor\x01",
            "shortage is acute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FHmm. I suppose the hole Estelle and\x01",
            "Joshua left was bigger than I thought.\x02\x03",
            "#04008FOur workload has increased.\x01",
            "No matter how able you say Arios\x01",
            "and Scott are, there's a limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FIndeed... You could certainly say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FWell, we'll be busy\x01",
            "going forward, and it\x01",
            "could get even worse.\x02\x03",
            "#04011FHu hu, thanks for everything that you're doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, same here.\x01",
            "Let's each do our best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 5)
    Jump("loc_4CE4")

    label("loc_4C49")


    ChrTalk(
        0x8,
        (
            "#04003FWith the month-end Trade Conference,\x01",
            "we'll be busy from here on out.\x02\x03",
            "#04011FIt could get even worse.\x01",
            "Thanks for everything\x01",
            "that you're doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE4")

    TalkEnd(0x8)
    Return()

    # Function_4_993 end

    def Function_5_4CE8(): pass

    label("Function_5_4CE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4DC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D06")
    Call(0, 6)
    Jump("loc_4DBD")

    label("loc_4D06")


    ChrTalk(
        0xFE,
        (
            "Fighting back-to-back with my idol,\x01",
            "Miss Kilika... For me, there\x01",
            "could be no better experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to protect Crossbell\x01",
            "from now on, I've gotta\x01",
            "refine my own "Taito".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DBD")

    Jump("loc_54D4")

    label("loc_4DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E9D")

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
            "Somehow, I felt a\x01",
            "familiar presence.\x01",
            "Could it be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, it couldn't.\x01",
            "Sorry, forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4F13")

    label("loc_4E9D")


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
            "...No, it couldn't.\x01",
            "Sorry, forget it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F13")

    Jump("loc_54D4")

    label("loc_4F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4FA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F33")
    Call(0, 7)
    Jump("loc_4FA2")

    label("loc_4F33")


    ChrTalk(
        0xFE,
        (
            "You guys... If it seems\x01",
            "tough, we'll assist you.\x01",
            "Just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a Guild,\x01",
            "we'll do all\x01",
            "we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FA2")

    Jump("loc_54D4")

    label("loc_4FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4FB5")
    Jump("loc_54D4")

    label("loc_4FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_507B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD4")
    TalkEnd(0xFE)
    Call(0, 23)
    Return()

    label("loc_4FD4")


    ChrTalk(
        0xFE,
        (
            "We plan to standby at the Guild for\x01",
            "awhile and survey the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's just, the situation isn't good at all...\x01",
            "Maybe we should get ready to attack.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54D4")

    label("loc_507B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5089")
    Jump("loc_54D4")

    label("loc_5089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5097")
    Jump("loc_54D4")

    label("loc_5097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_50A5")
    Jump("loc_54D4")

    label("loc_50A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_50B3")
    Jump("loc_54D4")

    label("loc_50B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_534C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52C5")

    ChrTalk(
        0xFE,
        (
            "Looks like senior Kilika went to Orchis\x01",
            "Tower as the President's aide...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FBy the way, Miss Ling,\x01",
            "do you know Miss Kilika too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, she's a master of the "Taito School".\x01",
            "She was my senior in training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A few years back, she lost her\x01",
            "father and worked for awhile in\x01",
            "Liberl as guild receptionist, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who would have thought she'd join the intelligence\x01",
            "agency under direct supervision of the President?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, she's complicated.\x01",
            "Maybe I should worry about her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 7)
    Jump("loc_5347")

    label("loc_52C5")


    ChrTalk(
        0xFE,
        (
            "Senior Kilika will be working\x01",
            "at the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, she's complicated.\x01",
            "Maybe I should worry about her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5347")

    Jump("loc_54D4")

    label("loc_534C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_535A")
    Jump("loc_54D4")

    label("loc_535A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5368")
    Jump("loc_54D4")

    label("loc_5368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5376")
    Jump("loc_54D4")

    label("loc_5376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_54D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5395")
    TalkEnd(0xFE)
    Call(0, 21)
    Return()

    label("loc_5395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5478")

    ChrTalk(
        0xFE,
        (
            "When I first saw you,\x01",
            "I thought you were an\x01",
            "untrained bunch, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think you're\x01",
            "full-fledged now.\x02",
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
        "#00012FHa ha... Please, go easy on us.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_54D4")

    label("loc_5478")


    ChrTalk(
        0xFE,
        (
            "I think you're\x01",
            "full-fledged now.\x02",
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

    label("loc_54D4")

    TalkEnd(0xFE)
    Return()

    # Function_5_4CE8 end

    def Function_6_54D8(): pass

    label("Function_6_54D8")

    OP_4B(0x11, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        "Miss Kilika, thank you for your hard work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The Taito School's "Crimson Swallow"...\x01",
            "Seeing its essence was very enlightening!\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03404FIt's been awhile since I last fought,\x01",
            "but that went better than expected.\x02\x03",
            "#03400F...But even so Ling, it seems\x01",
            "you've trained hard, too.\x02\x03",
            "Compared to when we met at the interleague\x01",
            "match eight years ago, you're like a whole\x01",
            "different person. Uh uh, you're more reliable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Ha ha. I still have a long way to go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd like to get a little\x01",
            "closer to master level\x01",
            "like you or Mr. Zin, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03400FUh uh. You sure are dedicated.\x02\x03",
            "#03404FHmm. I think you'll be able to\x01",
            "win against the likes of Zin\x01",
            "in another year or two, maybe.\x02\x03",
            "#03402FIt looks like he hasn't yet been able to overcome\x01",
            "his weak character towards young women.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ha ha, even an A-rank Bracer like him would lose\x01",
            "his face being told that by you, Miss Kilika.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0x11, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x1BB, 3)
    Return()

    # Function_6_54D8 end

    def Function_7_586A(): pass

    label("Function_7_586A")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "To be perfectly honest, I can't think the Empire\x01",
            "will stay quiet with an address like that.\x02",
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
            "Even a contact coming from Arundel\x01",
            "is definitely linked to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yeah, and you could say the same\x01",
            "thing about the Republican side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm worried about the Church's response too...\x01",
            "Anyway, we have to be ready for anything.\x02",
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

    # Function_7_586A end

    def Function_8_5A3D(): pass

    label("Function_8_5A3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_5A4E")
    Jump("loc_6411")

    label("loc_5A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5A5C")
    Jump("loc_6411")

    label("loc_5A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5CF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C36")

    ChrTalk(
        0xFE,
        (
            "Ever since Chairman MacDowell's declaration of\x01",
            "invalidity, restrictions have been getting\x01",
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
            "The liberation of Crossbell City...\x01",
            "It absolutely must succeed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5CEF")

    label("loc_5C36")


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
            "The liberation of Crossbell City...\x01",
            "It absolutely must succeed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CEF")

    Jump("loc_6411")

    label("loc_5CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5EE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E36")

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
            "We'll contact St. Ursula. Even the Guild\x01",
            "has to think about how to deal with this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5EE2")

    label("loc_5E36")


    ChrTalk(
        0xFE,
        (
            "We'll contact St. Ursula. Even the Guild\x01",
            "has to think about how to deal with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We owe you guys for the lake shore.\x01",
            "Please, tell us if you're ever in trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EE2")

    Jump("loc_6411")

    label("loc_5EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5EF5")
    Jump("loc_6411")

    label("loc_5EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_612D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F14")
    TalkEnd(0xFE)
    Call(0, 23)
    Return()

    label("loc_5F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_604D")

    ChrTalk(
        0xFE,
        (
            "It's strange for a jaeger\x01",
            "corps to take hostages...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if they don't harm them directly,\x01",
            "it would certainly cause considerate\x01",
            "psychological pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this situation drags on,\x01",
            "we'll need to consider\x01",
            "everyone's health disorders too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We've got to do something about it ASAP...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6128")

    label("loc_604D")


    ChrTalk(
        0xFE,
        (
            "By taking hostages, that jaeger\x01",
            "corps are inflicting psychological\x01",
            "pain on the people of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this situation drags on, we'll need to\x01",
            "consider everyone's health disorders too.\x01",
            "We've got to do something...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6128")

    Jump("loc_6411")

    label("loc_612D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_613B")
    Jump("loc_6411")

    label("loc_613B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6149")
    Jump("loc_6411")

    label("loc_6149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6157")
    Jump("loc_6411")

    label("loc_6157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6165")
    Jump("loc_6411")

    label("loc_6165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6173")
    Jump("loc_6411")

    label("loc_6173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6181")
    Jump("loc_6411")

    label("loc_6181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_618F")
    Jump("loc_6411")

    label("loc_618F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_619D")
    Jump("loc_6411")

    label("loc_619D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6411")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61BC")
    TalkEnd(0xFE)
    Call(0, 21)
    Return()

    label("loc_61BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6397")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xC,
        (
            "That's right...\x01",
            "I haven't seen\x01",
            "dear Tio in awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think she went to the autonomous\x01",
            "state of Leman for some time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. It seems she'll\x01",
            "be there for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...*sigh*, I see. The Guild\x01",
            "HQ is in Leman, so if I'd\x01",
            "transferred there for awhile...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...We don't have time for that.\x01",
            "Michel would never approve it too.\x02",
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
        "#00012F(Ha ha... She's the same as always.)\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_6411")

    label("loc_6397")


    ChrTalk(
        0xFE,
        (
            "Ah, it's been so long since\x01",
            "I gave a hug to little Tio...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Let me know once she's\x01",
            "back. I'll be right there!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6411")

    TalkEnd(0xFE)
    Return()

    # Function_8_5A3D end

    def Function_9_6415(): pass

    label("Function_9_6415")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_6426")
    Jump("loc_6A85")

    label("loc_6426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6434")
    Jump("loc_6A85")

    label("loc_6434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6661")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65A3")

    ChrTalk(
        0xFE,
        (
            "We had everyone who couldn't\x01",
            "escape shelter inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though we didn't check inside\x01",
            "buildings, Pearl from the\x01",
            "department store should be safe too.\x02",
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
            "know what they're going to do.\x01",
            "You guys be careful, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_665C")

    label("loc_65A3")


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
            "know what they're going to do.\x01",
            "You guys be careful, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665C")

    Jump("loc_6A85")

    label("loc_6661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_67D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6763")

    ChrTalk(
        0xFE,
        (
            "I'm from Crossbell too,\x01",
            "so I kind of understand\x01",
            "how Mr. Arios is feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, to think he'd\x01",
            "leave the Guild just\x01",
            "because of that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Thinking about it is useless.\x01",
            "Right now, I've got to do\x01",
            "what I can as a Bracer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_67CD")

    label("loc_6763")


    ChrTalk(
        0xFE,
        (
            "Even if I think about Mr.\x01",
            "Arios it's useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now, I've got to do\x01",
            "what I can as a Bracer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67CD")

    Jump("loc_6A85")

    label("loc_67D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_67E0")
    Jump("loc_6A85")

    label("loc_67E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6863")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "...I see, so\x01",
            "Armorica's safe.\x02",
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
    Jump("loc_6A85")

    label("loc_6863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6871")
    Jump("loc_6A85")

    label("loc_6871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_687F")
    Jump("loc_6A85")

    label("loc_687F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_688D")
    Jump("loc_6A85")

    label("loc_688D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_689B")
    Jump("loc_6A85")

    label("loc_689B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_68A9")
    Jump("loc_6A85")

    label("loc_68A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_68B7")
    Jump("loc_6A85")

    label("loc_68B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_68C5")
    Jump("loc_6A85")

    label("loc_68C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68E4")
    TalkEnd(0xFE)
    Call(0, 22)
    Return()

    label("loc_68E4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6975")
    Jump("loc_69BF")

    label("loc_6975")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6995")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_69BF")

    label("loc_6995")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69B5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_69BF")

    label("loc_69B5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_69BF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "You guys are more reliable\x01",
            "than when I first met you.\x02",
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
    Jump("loc_6A85")

    label("loc_6A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6A85")

    label("loc_6A85")

    TalkEnd(0xFE)
    Return()

    # Function_9_6415 end

    def Function_10_6A89(): pass

    label("Function_10_6A89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_6A9A")
    Jump("loc_73EE")

    label("loc_6A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6AA8")
    Jump("loc_73EE")

    label("loc_6AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C24")

    ChrTalk(
        0xFE,
        (
            "Magic golems, huh... He's sure\x01",
            "brought out some troublesome things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the liberation operation,\x01",
            "maximum consideration needs\x01",
            "to be given to citizen's safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Things like those roaming around\x01",
            "the city are something that\x01",
            "absolutely can't be allowed to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the name of the Guild,\x01",
            "we must make the President\x01",
            "pay for his crimes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6CDC")

    label("loc_6C24")


    ChrTalk(
        0xFE,
        (
            "...Things like those roaming around\x01",
            "the city are something that\x01",
            "absolutely can't be allowed to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the name of the Guild,\x01",
            "we must make the President\x01",
            "pay for his crimes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CDC")

    Jump("loc_73EE")

    label("loc_6CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6DE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CFC")
    Call(0, 7)
    Jump("loc_6DE0")

    label("loc_6CFC")


    ChrTalk(
        0xFE,
        (
            "Arundel of the Intelligence Division...\x01",
            "It's a name I heard many times when\x01",
            "I worked in the Imperial Guild.\x02",
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

    label("loc_6DE0")

    Jump("loc_73EE")

    label("loc_6DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6DF3")
    Jump("loc_73EE")

    label("loc_6DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F7C")

    ChrTalk(
        0xFE,
        (
            "Scott already confirmed it...\x01",
            "Nothing's happened at\x01",
            "Armorica Village or the hospital.\x02",
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
            "If this situation drags on,\x01",
            "I don't know what kind of danger\x01",
            "the people of Mainz will face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I knew it. We have no choice but to act, huh...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7012")

    label("loc_6F7C")


    ChrTalk(
        0xFE,
        (
            "If this situation drags on,\x01",
            "I don't know what kind of danger\x01",
            "the people of Mainz will face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I knew it. We have no choice but to act, huh...\x02",
    )

    CloseMessageWindow()

    label("loc_7012")

    Jump("loc_73EE")

    label("loc_7017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7025")
    Jump("loc_73EE")

    label("loc_7025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7033")
    Jump("loc_73EE")

    label("loc_7033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7041")
    Jump("loc_73EE")

    label("loc_7041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_704F")
    Jump("loc_73EE")

    label("loc_704F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_71EF")
    OP_4B(0xFE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7159")

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
            "...Yeah, sure. We'll step\x01",
            "up security on our end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(It looks like he's speaking with\x01",
            "someone at the Imperial Guild.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_71E6")

    label("loc_7159")


    ChrTalk(
        0xFE,
        (
            "...I see. I thought the terrorists might\x01",
            "be active in the Empire as well, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yeah, sure. We'll step\x01",
            "up security on our end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71E6")

    OP_4C(0xFE, 0xFF)
    Jump("loc_73EE")

    label("loc_71EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_71FD")
    Jump("loc_73EE")

    label("loc_71FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_720B")
    Jump("loc_73EE")

    label("loc_720B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_73E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_722A")
    TalkEnd(0xFE)
    Call(0, 22)
    Return()

    label("loc_722A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_72BB")
    Jump("loc_7305")

    label("loc_72BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_72DB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7305")

    label("loc_72DB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72FB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7305")

    label("loc_72FB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7305")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I heard about your exploits in Altair City.\x01",
            "You did a nice job back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sweating blood every day is just\x01",
            "what is connected to good results.\x01",
            "...Keep it up like this.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_73EE")

    label("loc_73E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_73EE")

    label("loc_73EE")

    TalkEnd(0xFE)
    Return()

    # Function_10_6A89 end

    def Function_11_73F2(): pass

    label("Function_11_73F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7407")
    Call(0, 6)
    Jump("loc_7982")

    label("loc_7407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77C6")

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
            "#00000FYou too, Miss Kilika.\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FMan, you really saved us back there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03402FUh uh. I merely provided\x01",
            "a bit of assistance.\x02\x03",
            "#03403FMore importantly... I can't hide\x01",
            "my surprise at the appearance\x01",
            "of that "huge tree".\x02",
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
            "#03403FThey're really taken aback.\x01",
            "It seems that "huge tree" can\x01",
            "be seen even from Altair City.\x02\x03",
            "We don't know what kind of\x01",
            "situation this is, so they'll\x01",
            "adopt a wait-and-see attitude.\x02\x03",
            "#03400FI can't share any other details,\x01",
            "so I'll leave it at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03400FI plan to remain here until I\x01",
            "have evaluated the situation too.\x02\x03",
            "#03403FI don't know Crossbell's path...\x01",
            "I don't think anyone knows.\x01",
            "Everything is up to you guys.\x02\x03",
            "#03402FIn order to not have any regrets,\x01",
            "follow the path you believe in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes... Thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 7)
    Jump("loc_7982")

    label("loc_77C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78D1")

    ChrTalk(
        0x11,
        (
            "#03400FI plan to remain here until I\x01",
            "have evaluated the situation too.\x02\x03",
            "#03403FI don't know Crossbell's path...\x01",
            "I don't think anyone knows.\x01",
            "Everything is up to you guys.\x02\x03",
            "#03402FIn order to not have any regrets,\x01",
            "follow the path you believe in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7982")

    label("loc_78D1")


    ChrTalk(
        0x11,
        (
            "#03403FI don't know Crossbell's path...\x01",
            "I don't think anyone knows.\x01",
            "Everything is up to you guys.\x02\x03",
            "#03400FIn order to not have any regrets,\x01",
            "follow the path you believe in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7982")

    TalkEnd(0xFE)
    Return()

    # Function_11_73F2 end

    def Function_12_7986(): pass

    label("Function_12_7986")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_799B")
    Call(0, 13)
    Jump("loc_7A04")

    label("loc_799B")


    ChrTalk(
        0x10,
        (
            "#01400F...Leave this place to me.\x02\x03",
            "You guys search for the "Naderia\x01",
            "Mushroom" on St. Ursula Byroad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A04")

    TalkEnd(0xFE)
    Return()

    # Function_12_7986 end

    def Function_13_7A08(): pass

    label("Function_13_7A08")

    OP_4B(0x10, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x10,
        (
            "#01400F...Yes, it's just like you heard.\x01",
            "Sorry, but please hurry and look for it.\x02\x03",
            "If I remember correctly, there\x01",
            "should be a stockpile inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FI see... I wonder where it was.\x02\x03",
            "I wonder if Eolia\x01",
            "should do it, too.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_13_7A08 end

    def Function_14_7B0D(): pass

    label("Function_14_7B0D")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Bracers' shift schedule is posted.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7C22")
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
            "    Ling: "Standby"\x01",
            "   Eolia: St. Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_873A")

    label("loc_7C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7CD5")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: -\x01",
            "   Scott: "Standby"\x01",
            "  Wenzel: "Standby"\x01",
            "    Ling: "Standby"\x01",
            "   Eolia: "Standby"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_873A")

    label("loc_7CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7D88")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: -\x01",
            "   Scott: "Standby"\x01",
            "  Wenzel: "Standby"\x01",
            "    Ling: "Standby"\x01",
            "   Eolia: "Standby"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_873A")

    label("loc_7D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7E60")
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
    Jump("loc_873A")

    label("loc_7E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7F1E")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Orchis Tower\x01",
            "   Scott: "Standby"\x01",
            "  Wenzel: "Standby"\x01",
            "    Ling: "Standby"\x01",
            "   Eolia: "Standby"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_873A")

    label("loc_7F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7FED")
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
    Jump("loc_873A")

    label("loc_7FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_80D0")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: "Cryptid Extermination"\x01",
            "   Scott: Tangram Gate\x01",
            "  Wenzel: Tangram Gate\x01",
            "    Ling: St. Ursula Hospital\x01",
            "   Eolia: St. Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_873A")

    label("loc_80D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_81C0")
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
    Jump("loc_873A")

    label("loc_81C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_82E6")
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
    Jump("loc_873A")

    label("loc_82E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_83B5")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Orchis Tower\x01",
            "   Scott: Armorica Village\x01",
            "  Wenzel: "Standby"\x01",
            "    Ling: "Standby"\x01",
            "   Eolia: St. Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_873A")

    label("loc_83B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_84A0")
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
    Jump("loc_873A")

    label("loc_84A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8587")
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
    Jump("loc_873A")

    label("loc_8587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8666")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "    Name          Destination\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "   Arios: Principality of Remiferia\x01",
            "   Scott: "Standby"\x01",
            "  Wenzel: "Standby"\x01",
            "    Ling: St. Ursula Hospital\x01",
            "   Eolia: St. Ursula Hospital\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_873A")

    label("loc_8666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_873A")
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
            "    Ling: "Standby"\x01",
            "   Eolia: "Standby"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_873A")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_7B0D end

    def Function_15_8751(): pass

    label("Function_15_8751")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_880F")

    ChrTalk(
        0x101,
        (
            "#00000FAs usual, they receive an\x01",
            "amazing number of requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FHmm, we can't\x01",
            "lose to them too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_880F")

    TalkEnd(0xFF)
    Return()

    # Function_15_8751 end

    def Function_16_8813(): pass

    label("Function_16_8813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_884B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8838")
    Call(0, 33)
    Return()

    label("loc_8838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_884B")
    Call(0, 34)
    Return()

    label("loc_884B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_885C")
    Jump("loc_8CF5")

    label("loc_885C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_887E")
    Call(0, 17)
    Jump("loc_88BA")

    label("loc_887E")


    ChrTalk(
        0xD,
        "#01109FShizuku, let's go to the Support Section later.\x02",
    )

    CloseMessageWindow()

    label("loc_88BA")

    Jump("loc_8CF5")

    label("loc_88BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88DE")
    Jump("loc_8C9D")

    label("loc_88DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C07")
    TurnDirection(0xD, 0x1A2, 0)

    ChrTalk(
        0xD,
        (
            "#01100FSay, you're Shing, right?\x02\x03",
            "You don't look like you're from Crossbell.\x01",
            "How long are you gonna be here?\x02",
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
            "#01105FAh, then, where're you gonna see\x01",
            "the tower unveiling tomorrow?\x02\x03",
            "#01102FWe're gonna see it from the\x01",
            "department store roof. How about it?\x02",
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
            "#01105FIt's okay. How about it?\x02\x03",
            "#01109FRyｹ, Henri and the other\x01",
            "kids will be there too.\x01",
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
            "insistent, I guess I'll go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "It's at 11AM tomorrow, right!?\x02",
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
            "#00009F(Ha ha... He looks\x01",
            "happy somehow.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Hmm. Maybe he doesn't get the chance\x01",
            "to play with other kids that often...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 2)
    TurnDirection(0xD, 0xE, 0)
    Jump("loc_8C9D")

    label("loc_8C07")

    TurnDirection(0xD, 0x1A2, 0)

    ChrTalk(
        0xD,
        (
            "#01100FThen, see you on the department\x01",
            "store roof tomorrow at 11AM.\x02\x03",
            "#01109FWe'll all be waiting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Y-Yeah... See\x01",
            "you tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 0)

    label("loc_8C9D")

    Jump("loc_8CF5")

    label("loc_8CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8CF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CBA")
    Jump("loc_8CF5")

    label("loc_8CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CCC")
    Call(0, 17)
    Jump("loc_8CF5")

    label("loc_8CCC")


    ChrTalk(
        0xD,
        "#01109FThen, you come too, Shizuku!\x02",
    )

    CloseMessageWindow()

    label("loc_8CF5")

    TalkEnd(0xFE)
    Return()

    # Function_16_8813 end

    def Function_17_8CF9(): pass

    label("Function_17_8CF9")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E05")

    ChrTalk(
        0xD,
        (
            "#01104FShizuku, Shing left already.\x01",
            "Want to play somewhere else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#06005FUh, yes, right.\x02\x03",
            "#06000FBut, is it okay for\x01",
            "us to go alone?\x02",
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
        "#01110FAh, then I've got a good idea.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EC4")

    label("loc_8E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8EC4")

    ChrTalk(
        0xD,
        (
            "#01109FYou see, now it's got\x01",
            "a blue sheet on it...\x01",
            "It's really biiig.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#06002FIt must be nice...\x01",
            "Uh uh, I too would like to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01109FThen, you come too, Shizuku!\x02",
    )

    CloseMessageWindow()

    label("loc_8EC4")

    SetScenarioFlags(0x1, 1)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_17_8CF9 end

    def Function_18_8ED0(): pass

    label("Function_18_8ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EF5")
    Call(0, 33)
    Return()

    label("loc_8EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F08")
    Call(0, 34)
    Return()

    label("loc_8F08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_8F19")
    Jump("loc_9185")

    label("loc_8F19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F3B")
    Call(0, 17)
    Jump("loc_8F92")

    label("loc_8F3B")


    ChrTalk(
        0xE,
        (
            "#06005FNo, it's fine...\x01",
            "What's your idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#01104FEhehe, it's still a secret.\x02",
    )

    CloseMessageWindow()

    label("loc_8F92")

    Jump("loc_9185")

    label("loc_8F97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_911C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FB6")
    Jump("loc_9117")

    label("loc_8FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9089")
    TurnDirection(0xE, 0x1A2, 0)

    ChrTalk(
        0xE,
        (
            "#06002FUh uh, you're a very\x01",
            "good boy, Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "N-Nah... T-That's\x01",
            "not true, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "After all, I'm a\x01",
            "man burdened with the\x01",
            "future of "Heiyue"!\x02",
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
    Jump("loc_9117")

    label("loc_9089")

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
            "(H-Hmm... I'm\x01",
            "not that kind of\x01",
            "boy, though.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 0)

    label("loc_9117")

    Jump("loc_9185")

    label("loc_911C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9134")
    Jump("loc_9185")

    label("loc_9134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9146")
    Call(0, 17)
    Jump("loc_9185")

    label("loc_9146")


    ChrTalk(
        0xE,
        (
            "#06002FUh uh, I understand.\x01",
            "Let's go see it together, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9185")

    TalkEnd(0xFE)
    Return()

    # Function_18_8ED0 end

    def Function_19_9189(): pass

    label("Function_19_9189")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_19_9189 end

    def Function_20_9190(): pass

    label("Function_20_9190")

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

    def lambda_9278():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9278)

    def lambda_9292():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9292)
    Sleep(250)

    def lambda_92A6():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92A6)

    def lambda_92C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_92C0)
    Sleep(600)

    def lambda_92D4():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_92D4)

    def lambda_92EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_92EE)
    Sleep(250)

    def lambda_9302():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9302)

    def lambda_931C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_931C)
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
        "#04005FOh, you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Michel...\x01",
            "It's been awhile.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x101, 500, 0, 3000, 0)
    SetChrPos(0x102, -500, 0, 3000, 0)
    SetChrPos(0x105, 0, 0, 1900, 0)
    SetChrPos(0x109, -1000, 0, 1900, 0)

    def lambda_93F2():
        OP_96(0xFE, 0x5DC, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_93F2)
    Sleep(100)

    def lambda_940F():
        OP_96(0xFE, 0x1F4, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_940F)
    Sleep(150)

    def lambda_942C():
        OP_96(0xFE, 0x7D0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_942C)
    Sleep(100)

    def lambda_9449():
        OP_96(0xFE, 0x3E8, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9449)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x105, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_950A")

    AnonymousTalk(
        0x8,
        (
            "Uh uh, long time no see.\x02\x03",
            "You did a nice job with\x01",
            "that arrest at Altair City.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_957E")

    label("loc_950A")


    AnonymousTalk(
        0x8,
        (
            "Uh uh, long time no see.\x02\x03",
            "It's a little later, but you\x01",
            "guys did a nice job with\x01",
            "that arrest at Altair City.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_957E")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#12P#00000FThank you very much.\x01",
            "And you too, it was a big help\x01",
            "having Mr. Arios with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*. You look\x01",
            "well, Mr. Michel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FUh uh, of course I'm in top form♪\x02\x03",
            "#04006FWell, we're busier than\x01",
            "usual now that Estelle\x01",
            "and Joshua are gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FI expected as much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FBut, it looks like Mr.\x01",
            "Arios and the other\x01",
            "Bracers are managing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FWell, we're used to\x01",
            "being short-handed.\x02\x03",
            "#04000FWe've got to manage\x01",
            "as best we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FThey don't call you Bracers the\x01",
            "allies of the citizens for nothing...\x02\x03",
            "#10300FNo matter how busy you\x01",
            "guys are, there's hardly\x01",
            "a word of complaint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FExactly. You\x01",
            "know us well.\x02\x03",
            "#04009FAlthough we acknowledge\x01",
            "you police too, that's\x01",
            "exactly why we──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04005FWait, could these\x01",
            "kids be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, they're our new Support Section members.\x02",
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
            "#12P#10302FWazy Hemisphere...\x01",
            "But I suppose that\x01",
            "goes without saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000FHeh... Quite the\x01",
            "interesting kids\x01",
            "you've got there.\x02\x03",
            "#04004FAn active duty CGF member goes\x01",
            "without saying, but to think you've\x01",
            "got that "Testaments" leader too.\x02\x03",
            "#04000FThey must be a great help now that\x01",
            "you've restarted the Support Section.\x02\x03",
            "But, are you sure you can rely on\x01",
            "them when push comes to shove?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, of course.\x02\x03",
            "Though our viewpoints may be\x01",
            "different, we're working together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004FUh uh, your faces look a lot\x01",
            "better than when we first met.\x02\x03",
            "#04011FThen, once again... It's a\x01",
            "pleasure to be working with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x139, 0)
    OP_4C(0x8, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_20_9190 end

    def Function_21_9BF3(): pass

    label("Function_21_9BF3")

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
        "Hi, Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "My, it's been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt's been awhile, Miss\x01",
            "Ling and Miss Eolia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWhat's new with\x01",
            "everyone at the Guild?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)

    ChrTalk(
        0xB,
        (
            "Well, we're as\x01",
            "busy as always.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x105, 500)

    ChrTalk(
        0xB,
        (
            "Oh, have you got some\x01",
            "new faces there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FWell, something like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FYou are Bracers, right?\x01",
            "Pleased to make your acquaintance!\x02\x03",
            "#10109FActually, I think I saw\x01",
            "you girls heading for the\x01",
            "Republic many times.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x109, 500)

    ChrTalk(
        0xB,
        (
            "Yeah, you're that CGF\x01",
            "member... I think I've seen\x01",
            "you at Tangram Gate, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x109, 500)

    ChrTalk(
        0xC,
        (
            "Uh uh, that operation at Altair\x01",
            "City was quite the job.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "You guys got through that Cult\x01",
            "incident. You'll be full-\x01",
            "fledged before long, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha. We have a long way to\x01",
            "go in many respects, but...\x02\x03",
            "#00000FWe plan to do our very\x01",
            "best from here on.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        "Ha ha, that's the spirit.\x02",
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

    # Function_21_9BF3 end

    def Function_22_A008(): pass

    label("Function_22_A008")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A112")
    Jump("loc_A15C")

    label("loc_A112")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A132")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A15C")

    label("loc_A132")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A152")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A15C")

    label("loc_A152")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A15C")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A212")
    Jump("loc_A25C")

    label("loc_A212")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A232")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A25C")

    label("loc_A232")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A252")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A25C")

    label("loc_A252")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A25C")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    OP_0D()

    ChrTalk(
        0x9,
        "#6POh, guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...The Special Support Section, huh?\x01",
            "Hmm, it's been awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FMr. Scott and Mr. Wenzel,\x01",
            "it is good to see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10300FYou guys are Bracers, eh?\x01",
            "Hu hu, it looks like you're\x01",
            "really talented...\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A408")
    Jump("loc_A452")

    label("loc_A408")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A428")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A452")

    label("loc_A428")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A448")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A452")

    label("loc_A448")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A452")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A542")
    Jump("loc_A58C")

    label("loc_A542")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A562")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A58C")

    label("loc_A562")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A582")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A58C")

    label("loc_A582")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A58C")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6PAnd you there. You look\x01",
            "like a CGF member somehow.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A680")
    Jump("loc_A6CA")

    label("loc_A680")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A6A0")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A6CA")

    label("loc_A6A0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6C0")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A6CA")

    label("loc_A6C0")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A6CA")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6PHa ha, looks like you've\x01",
            "got some new recruits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10105FW-Wazy aside... How did\x01",
            "you know with just a glance?\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A800")
    Jump("loc_A84A")

    label("loc_A800")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A820")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A84A")

    label("loc_A820")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A840")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A84A")

    label("loc_A840")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A84A")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "You don't look like any\x01",
            "police officer I've seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since you do the kind of work\x01",
            "us Bracers do, you should train\x01",
            "your discerning eye too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100F*giggle*, thank you very much for the advice.\x02",
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

    # Function_22_A008 end

    def Function_23_A9A9(): pass

    label("Function_23_A9A9")

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
        "Hey, thank you for yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FMiss Ling, Miss Eolia...\x01",
            "Are you feeling all right already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, somehow. It's all\x01",
            "thanks to you guys.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "Little Tio, I'll pet you later as\x01",
            "a way of saying thanks, ok?㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xC, 500)

    ChrTalk(
        0x103,
        (
            "#12P#00203F...I humbly refuse.\x02\x03",
            "#00200FBut if you can say that,\x01",
            "you must be feeling better.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 500)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "Yeah, but we can't push\x01",
            "ourselves too hard yet...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "Huh? Come to think of it...\x01",
            "Where'd that redhead go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Normally, he'd be saying something\x01",
            "like "then, I'll do it for you..."\x01",
            "and stuff around this time.\x02",
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
            "#5P#04001F...Looks like something happened. \x01",
            "Do you want to talk about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F...Yes, actually...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others explained\x01",
            "that Randy had disappeared.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5P#04003F...I see.\x02\x03",
            "#04001FThe Mainz occupation incident... \x01",
            "In some respects, we were expecting\x01",
            "the "Red Constellation" to be involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F...How will the Guild deal\x01",
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
            "need to summon A-rank or above Bracers\x01",
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
        "#12P#00011FY-You'd go that far...!?\x02",
    )

    CloseMessageWindow()

    def lambda_B105():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B105)
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        "That's only in the worst case scenario.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Right now, Mr. Arios is discussing\x01",
            "things with the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If it doesn't look like the CGF\x01",
            "can resolve the incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FWell, being the Guild, Civilian safety is your number\x01",
            "one priority. Of course you'll have to deal with it...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    ChrTalk(
        0x8,
        (
            "#5P#04003F...Anyway, I'm\x01",
            "worried about that\x01",
            "redheaded boy too.\x02\x03",
            "#04001FI don't know what's going to happen,\x01",
            "but you guys be careful, ok?\x02",
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

    # Function_23_A9A9 end

    def Function_24_B353(): pass

    label("Function_24_B353")

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

    def lambda_B4B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B4B5)
    Sleep(50)

    def lambda_B4C5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B4C5)
    Sleep(50)

    def lambda_B4D5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B4D5)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "There hasn't been any news of you since\x01",
            "the declaration of independence, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ha ha, I'm glad you're ok.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FMr. Michel, everyone...\x01",
            "It's been awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00202FUh uh, thank goodness you are safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Uh uh, same to you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Little Tio...\x01",
            "Thank goodness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006F...Hey. This is no time\x01",
            "for leisurely greetings.\x02\x03",
            "#04001FI know it's been awhile,\x01",
            "but can we exchange infos?\x02",
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
            "...I see, so\x01",
            "that's how it is.\x02",
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
            "In any case, when I heard that a red "Aion"\x01",
            "appeared at the west entrance, I was\x01",
            "thinking what the heck was going on, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I can't believe it was Estelle and friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems like Heiyue and the CGF\x01",
            "Resistance are helping out at\x01",
            "the north and east entrances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uh uh, you guys know\x01",
            "them very well too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FHa ha, I guess you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FBy the way... "Magic soldiers"\x01",
            "have appeared in the city\x01",
            "and they're not attacking?\x02",
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
            "We've been alert and going around\x01",
            "patrolling the areas to see if some \x01",
            "people were left behind, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems those "magic soldiers"\x01",
            "won't lay their hands on\x01",
            "Crossbell citizens at all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB02")

    ChrTalk(
        0x105,
        (
            "#12P#10403FHmm... It seems the President\x01",
            "has good control over them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBB4")

    label("loc_BB02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB61")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FHmm... It seems the President\x01",
            "has good control over them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBB4")

    label("loc_BB61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBB4")

    ChrTalk(
        0x109,
        (
            "#12P#10101FIt seems the President\x01",
            "has good control over them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBF8")

    ChrTalk(
        0x106,
        (
            "#12P#10705FThat's a good\x01",
            "thing, in a way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC7F")

    label("loc_BBF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC3C")

    ChrTalk(
        0x109,
        (
            "#12P#10105FThat's a good\x01",
            "thing, in a way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC7F")

    label("loc_BC3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC7F")

    ChrTalk(
        0x105,
        (
            "#12P#10304FThat's a good thing,\x01",
            "in a way, no?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC7F")


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
            "casualties could there be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003FI agree. The Guild can't standby\x01",
            "when innocent civilians are\x01",
            "exposed to danger.\x02\x03",
            "#04011FBreak into Orchis Tower\x01",
            "and arrest the President...\x01",
            "We will help you out too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204FThank you very much.\x01",
            "That is very reassuring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003FHowever... It's\x01",
            "likely that Arios\x01",
            "is in Orchis Tower.\x02\x03",
            "Miss Mariabell and the "Ogre"\x01",
            "or something are probably\x01",
            "waiting for you too.\x02\x03",
            "#04001FI'm sure it won't be easy... \x01",
            "You're all aware of that, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303F...All too well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FNo matter what kind of "barriers"\x01",
            "stand in our way... We have no\x01",
            "choice but to push through them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04004FUh uh. It seems you all\x01",
            "are ready for this.\x02\x03",
            "#04001F──Please contact us when it's\x01",
            "time to begin the operation.\x02\x03",
            "We'll carefully prepare\x01",
            "until that time too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAlright... See you later.\x02",
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

    # Function_24_B353 end

    def Function_25_C0D3(): pass

    label("Function_25_C0D3")

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
            "Oh, thanks for coming.\x02\x03",
            "Arios isn't back yet, but you\x01",
            "can wait upstairs if you like.\x02\x03",
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
            "#00008F(It's almost evening... Is there\x01",
            "anything else we need to do?)\x02",
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
            "[We Have Other Things To Do]\x01",          # 0
            "[We Will Wait For Arios' Return]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C38C"),
        (1, "loc_C439"),
        (SWITCH_DEFAULT, "loc_C64D"),
    )


    label("loc_C38C")


    ChrTalk(
        0x8,
        (
            "#5P#04011FI see, then please, come here when\x01",
            "you have finished what you have to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FYes, we'll come again.\x02",
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
    Jump("loc_C64D")

    label("loc_C439")


    ChrTalk(
        0x8,
        (
            "#5P#04011FThen, please head upstairs\x01",
            "and make yourselves at home.\x02\x03",
            "We have tea and coffee readied.\x01",
            "Please feel free to have some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FHa ha, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FOk we'll head up, then.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 4500)

    def lambda_C515():

        label("loc_C515")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C515")

    QueueWorkItem2(0x8, 2, lambda_C515)
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
            "Not long after, Arios\x01",
            "returned to the Guild.\x02\x03",
            "Lloyd and the others exchanged information\x01",
            "regarding the Trade Conference as well as\x01",
            ""Heiyue" and "Red Constellation".\x07\x00\x02",
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
    Jump("loc_C64D")

    label("loc_C64D")

    Return()

    # Function_25_C0D3 end

    def Function_26_C64E(): pass

    label("Function_26_C64E")

    OP_92(0xFE, 0x1F40, 0x2AF8, 0x1F4)

    def lambda_C660():
        OP_95(0xFE, 8000, 0, 11000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C660)
    WaitChrThread(0xFE, 1)

    def lambda_C67E():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C67E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_C64E end

    def Function_27_C698(): pass

    label("Function_27_C698")

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
            "#4049V#30W──I see.\x02\x03",
            "#4050VEven though it's called\x01",
            "Crimson & Co., they\x01",
            "do that on the side...\x02",
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
            "#04006FIt's become more difficult to get information\x01",
            "from the Imperial capital region lately.\x02\x03",
            "#04000FThanks, that really helps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00004FDon't mention it. We're happy to be of service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FBut, did you get any information\x01",
            "on the "Red Constellation" itself?\x02\x03",
            "#10300FI heard the Guild has many\x01",
            "skirmishes with jaeger corps...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FThat is true, but encounters\x01",
            "with jaegers on the level of\x01",
            ""Red Constellation" are rare.\x02\x03",
            "#01400FIf we did oppose them, it\x01",
            "would likely mean all-out war.\x02",
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
            "level of a small country...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003F──Among the many jaeger corps, the "Red\x01",
            "Constellation" is in a whole other league.\x02\x03",
            "They have connections throughout the\x01",
            "continent, and at the first sign of conflict,\x01",
            "they rush there and escalate it themselves...\x02\x03",
            "#04001F"Zephyr" might be the only jaeger\x01",
            "corps that can match them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FThat's that Revache young men's\x01",
            "boss' old haunt, if I recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FBoth groups gather tough\x01",
            "guys with combat experience.\x02\x03",
            "There was one in particular, who was like a\x01",
            "monster... The "Jaeger King", they called him...\x02\x03",
            "#00303FBut half a year ago, he and the "War God"──\x01",
            "my ol' man, killed each other in a fight.\x02",
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
        "#5P#01405FHmm, it seems there's a lot going on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FActually, the Guild is aware\x01",
            "of that information already.\x02\x03",
            "#04001FBy the way, "Zephyr" has suspended\x01",
            "their activities at present, however...\x02\x03",
            ""Red Constellation" look\x01",
            "as active as ever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FIt's because my uncle's remains there.\x02\x03",
            "#00303F──Red Constellation's vice leader,\x01",
            "Sigmund, the "Ogre Rosso".\x02\x03",
            "#00301FHe's a monster on the same level as\x01",
            "the "War God" and the "Jaeger King".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01400FThose three are particularly famous.\x02\x03",
            "#01403F──Based on what I've heard,\x01",
            "I wonder if I could even match them.\x02",
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
        "#12P#00011FN-No way...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FEven the "Divine Blade\x01",
            "of Wind" can't...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006FHmm. According to my judgment, I think\x01",
            "you'll have about a 50-50 chance?\x02\x03",
            "#04000FThere's a considerable difference between the\x01",
            "fighting styles of a swordsman and a jaeger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F...You're tellin' me.\x02\x03",
            "#00301FYou might be strong, but\x01",
            "my uncle's a true monster.\x02\x03",
            "If you were to fight each other, neither\x01",
            "of you would walk out of it unscathed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FYeah, I know.\x02\x03",
            "#01400F──However, I will oppose him,\x01",
            "should that become necessary.\x02\x03",
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
        "#10106FThat's what it boils down to, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FWith the info we've collected\x01",
            "thus far, we have some idea.\x02\x03",
            "#10300FThe clues point to them being connected\x01",
            "with the Imperial government.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#04001FThat may be true, but there's something\x01",
            "else I'm more concerned about.\x02\x03",
            "It's something Arios learned for\x01",
            "us when he was in the Republic.\x02",
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
        "#12P#00101FWhat kind of information is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FYes── It's about "Heiyue".\x02\x03",
            "#01401FAt present, the Republican\x01",
            "government has dealings\x01",
            "with the "Heiyue" elders.\x02",
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
        "#12P#00007FSeriously...!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_D8D6")

    ChrTalk(
        0x102,
        (
            "#12P#00108FSpeaking of a "Heiyue" elder...\x01",
            "Shing's grandfather is one too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D91C")

    label("loc_D8D6")


    ChrTalk(
        0x102,
        (
            "#12P#00108FThe "Heiyue" elders are\x01",
            "their most central figures...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D91C")


    ChrTalk(
        0x8,
        (
            "#04006F...Right.\x01",
            "There's one more point to consider.\x02\x03",
            "#04001FThe one who is facilitating those\x01",
            "dealings is a woman named Kilika Rouran.\x02",
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
            "#12P#00107FThats... I can't believe it,\x01",
            "is she that Miss Kilika!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWow, the raven-haired woman\x01",
            "we saw at the auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FIncidentally, she also has\x01",
            "connections to the Bracer Guild.\x02\x03",
            "She once served as the Liberl\x01",
            "Zeiss branch's receptionist.\x02\x03",
            "#01400FHowever, about a year ago she retired and\x01",
            "transferred to the Calvardian intelligence agency.\x02\x03",
            "Its name is the\x01",
            ""Rocksmith Agency".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FRocksmith... That's the name\x01",
            "of the Republican President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FI heard a new intelligence agency was created\x01",
            "with the President as its leader, but...\x02",
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
            "The "Red Constellation" and "Heiyue"\x01",
            "had a conflict before, right!?\x02\x03",
            "If the intelligence officers of those two\x01",
            "major powers are in contact with them, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, it means the stage is being\x01",
            "set for an incredible confrontation.\x02",
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
            "#10101FYou mean Crossbell will end up as the battleground\x01",
            "in a proxy war between the Empire and the Republic!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04003FIt's a possibility, of course.\x02\x03",
            "#04001FEspecially since Chancellor Osborne of Erebonia\x01",
            "and President Rocksmith of Calvard will be\x01",
            "attending the Trade Conference tomorrow.\x02\x03",
            "Either or both might be planning to take\x01",
            "advantage of the situation and eliminate\x01",
            "the other leader...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01403FBut neither of them is keeping their\x01",
            "contacts a secret. That is quite strange.\x02\x03",
            "Suppose "Heiyue" or "Red Constellation"\x01",
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
            "#12P#00103F...You're right. It doesn't look like\x01",
            "they're setting up for a simple attack.\x02\x03",
            "#00108FBut why, then...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FDamn. What the hell\x01",
            "is my uncle thinkin'...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00003F──In any case, there\x01",
            "must be some meaning\x01",
            "in what they're doing.\x02\x03",
            "#00008FIt's likely there's at least one\x01",
            "piece of the puzzle we're missing.\x02\x03",
            "#00001FAnd we need to grab all of them.\x02",
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
        "#6P#10302FHu hu, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011FUhuhu, that's Lloyd for you.\x01",
            "We had a start on you already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#01404FActually, we were thinking the same thing.\x02\x03",
            "#01402FWe're in the middle of using the Guild's\x01",
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
            "#00300FAlright then. Will you let us\x01",
            "know if you learn something?\x02",
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
            "#5P#01402FPlease do the same for us. Let us\x01",
            "know if you find out anything new.\x02\x03",
            "We'll need to cooperate if we're going to get\x01",
            "through these next three days without incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FRoger...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FWe'll contact you right\x01",
            "away if we learn something.\x02",
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
            "After that, KeA and Shizuku\x01",
            "returned to the Guild with Zeit.\x02\x03",
            "Lloyd and the others said goodbye to Arios\x01",
            "and Shizuku who were going to dine together.\x01",
            "The Support Section returned home.\x07\x00\x02",
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

    # Function_27_C698 end

    def Function_28_E693(): pass

    label("Function_28_E693")

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
            "#12P#00012FHa ha... Good to\x01",
            "see you, Mr. Michel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FUhmm, we're a little worried\x01",
            "about what we heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006F*sigh*, oh boy.\x01",
            "It's like I pressed you to come.\x02\x03",
            "#04011FBut thank you. \x01",
            "I'm so glad you came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305F...And that means you\x01",
            "haven't been able to contact\x01",
            "Miss Ling and Miss Eolia yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003FWe haven't. Arios and the\x01",
            "others are looking for them...\x02\x03",
            "#04008F...I mean, seriously. What\x01",
            "do they think they're doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FThat is rather concerning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FHmm... If they can't be reached\x01",
            "via ENIGMA, does it mean they're\x01",
            "outside the autonomous state?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FI was thinking that too, however\x01",
            "there's no record of them having\x01",
            "used the station or airport.\x02\x03",
            "#04001FAnd there's no record of them passing\x01",
            "through Tangram or Bellguard gates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FThat's...\x01",
            "Really strange.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#12P#00203F...If Miss Ling and Miss Eolia\x01",
            "are inside the autonomous state...\x02\x03",
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

    def lambda_EBE6():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EBE6)
    Sleep(50)

    def lambda_EBF6():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_EBF6)
    Sleep(50)

    def lambda_EC06():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_EC06)
    Sleep(50)

    def lambda_EC16():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EC16)
    Sleep(50)

    def lambda_EC26():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EC26)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#11P#00005FReally...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#04005FWh-What... How, exactly!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FI think functions left over from the development\x01",
            "stage are still present in ENIGMA II units.\x02\x03",
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
            "#12P#00206FIt is configured to use reserve orbal\x01",
            "energy to transmit orbal waves of a\x01",
            "specific frequency at fixed intervals.\x02\x03",
            "But the orbal waves are very weak. I have never\x01",
            "heard of a practical application for this.\x02\x03",
            "#00201FBut that function wasn't ever cut. It should\x01",
            "still be there, even in production models.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThen, if we can somehow catch\x01",
            "those faint orbal waves...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04001FWe'd have a fix on Ling\x01",
            "and Eolia's location...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204FIt seems that it is worth trying.\x02\x03",
            "#00202FChief Roberts is familiar\x01",
            "with this function.\x01",
            "Let's head over to IBC.\x02\x03",
            "Maybe he will be willing to assist us.\x02",
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
            "you for helping us.\x02\x03",
            "#04000FPlease contact us as soon\x01",
            "as you learn anything.\x02\x03",
            "If the situation warrants it,\x01",
            "I'll recall Arios and the others.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F14D():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F14D)
    Sleep(50)

    def lambda_F15D():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F15D)
    Sleep(50)

    def lambda_F16D():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F16D)
    Sleep(50)

    def lambda_F17D():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F17D)
    Sleep(50)

    def lambda_F18D():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F18D)
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
            "#12P#10302FShall we head\x01",
            "to IBC, then?\x02",
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

    # Function_28_E693 end

    def Function_29_F239(): pass

    label("Function_29_F239")

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

    def lambda_F349():
        TurnDirection(0x102, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F349)
    Sleep(0)

    def lambda_F359():
        TurnDirection(0x103, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F359)
    Sleep(0)

    def lambda_F369():
        TurnDirection(0x104, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F369)
    Sleep(0)

    def lambda_F379():
        TurnDirection(0x109, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F379)
    Sleep(0)

    def lambda_F389():
        TurnDirection(0x105, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F389)
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
            "──Yes, an orbal boat is ready for\x01",
            "you at Waterfront Area jetty.\x02\x03",
            "You can board right away.\x02",
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
            "#00006FIs that right. Thank you, Fran.\x02\x03",
            "#00001FAnd sorry for requesting something\x01",
            "like that all of a sudden.\x02",
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
            "Don't mention it. I'm here to support\x01",
            "all of you in times like thiiis.\x02\x03",
            "But the Marshlands to the south...?\x01",
            "Be very, very careful, ok?\x02",
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
            "#00000FSure, we'll keep that in mind.\x02",
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
            "#5P#04006F──*sigh*, it seems like I'm going to be relying\x01",
            "on you guys until the bitter end this time.\x02\x03",
            "#04001FBut, are you sure you're ok with this?\x02\x03",
            "I think Arios and the others will\x01",
            "be back here within the hour...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F779():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F779)
    Sleep(50)

    def lambda_F789():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F789)
    Sleep(50)

    def lambda_F799():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F799)
    Sleep(50)

    def lambda_F7A9():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F7A9)
    Sleep(50)

    def lambda_F7B9():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F7B9)
    Sleep(50)

    def lambda_F7C9():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F7C9)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x104,
        (
            "#6P#00303FThat's too long. It's best if\x01",
            "we go there ahead of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FThat's right... We don't know what\x01",
            "the situation is over there, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, once they're back,\x01",
            "tell them to follow us, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04000F...Understood.\x02\x03",
            "#04003FBoth Ling and Eolia are capable\x01",
            "bracers who are nearly A-rank.\x02\x03",
            "If both of them are in a situation\x01",
            "where they can't contact us...\x02\x03",
            "#04001FI have no idea what it could be.\x01",
            "Be extremely careful, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013FRight...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#6P#00201FWe will head for the\x01",
            "jetty once we are ready.\x02",
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

    # Function_29_F239 end

    def Function_30_FA66(): pass

    label("Function_30_FA66")

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
        "#00001FExcuse us...\x02",
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

    def lambda_FCEC():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_FCEC)
    Sleep(50)

    def lambda_FCFC():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_FCFC)
    Sleep(50)

    def lambda_FD0C():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_FD0C)
    Sleep(50)

    def lambda_FD1C():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_FD1C)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    Sleep(1000)

    def lambda_FD3F():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FD3F)

    def lambda_FD59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FD59)
    Sleep(600)

    def lambda_FD6D():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FD6D)

    def lambda_FD87():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FD87)
    Sleep(900)

    def lambda_FD9B():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FD9B)

    def lambda_FDB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FDB5)
    Sleep(600)

    def lambda_FDC9():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FDC9)

    def lambda_FDE3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FDE3)
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
        "#6PHey, it's Lloyd and friends...\x02",
    )

    CloseMessageWindow()

    def lambda_FE48():

        label("loc_FE48")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FE48")

    QueueWorkItem2(0x9, 2, lambda_FE48)

    def lambda_FE5A():

        label("loc_FE5A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FE5A")

    QueueWorkItem2(0xA, 2, lambda_FE5A)

    def lambda_FE6C():

        label("loc_FE6C")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_FE6C")

    QueueWorkItem2(0xC, 2, lambda_FE6C)

    def lambda_FE7E():
        OP_96(0xFE, 0x384, 0x0, 0x206C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FE7E)
    Sleep(200)

    def lambda_FE9B():
        OP_96(0xFE, 0xFFFFFED4, 0x0, 0x1E78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FE9B)
    Sleep(100)

    def lambda_FEB8():
        OP_96(0xFE, 0x578, 0x0, 0x1C84, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FEB8)
    Sleep(100)

    def lambda_FED5():
        OP_96(0xFE, 0xC8, 0x0, 0x1A90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FED5)
    Sleep(1500)
    Fade(500)
    OP_68(1000, 1100, 9900, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)

    def lambda_FF25():
        OP_96(0xFE, 0xA8C, 0x0, 0x251C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FF25)
    Sleep(100)

    def lambda_FF42():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0x251C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_FF42)
    WaitChrThread(0x103, 1)
    EndChrThread(0xC, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)

    ChrTalk(
        0x104,
        (
            "#00306F#12PMan, doom and gloom on each and\x01",
            "every one of your faces, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt's none of your business...\x01",
            "That's what I'd like to say, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P...We, I can't deny it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POf all things, why\x01",
            "did Mr. Arios...\x02\x03",
            "*sigh*... It's too shocking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI didn't get even the slightest\x01",
            "feeling he'd do something like that.\x02\x03",
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
            "the Guild response.\x02\x03",
            "#04008FBut to think he was\x01",
            "discussing this kind of plan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F...Actually, that's what we\x01",
            "came to ask you about.\x02\x03",
            "#00001FIs Mr. Arios still\x01",
            "a Guild member?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04001F...Last night, he suddenly handed in\x01",
            "his resignation and Guild emblem.\x02\x03",
            "#04006FHe finished all the jobs he had and\x01",
            "gave us a plan for dealing with the\x01",
            "recent attack. How very like him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FMr. Arios does seem like\x01",
            "a very methodical person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P...But, his sudden resignation like\x01",
            "this is a huge problem, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWhat's more, he's the Secretary of Defence\x01",
            "of the "Independent State of Crossbell",\x01",
            "the "State Guard" Commander in Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P...How to say it, the Erebonian\x01",
            "response is sure to be frightening.\x02\x03",
            "#5PThere's even the forced\x01",
            "asset freeze...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P...That's right. The Calvardian\x01",
            "response will be scary too.\x02",
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
            "Mr. Arios is feeling.\x02",
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

    def lambda_105CA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_105CA)
    Sleep(50)

    def lambda_105DA():
        TurnDirection(0xB, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_105DA)
    Sleep(50)

    def lambda_105EA():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_105EA)
    Sleep(50)

    def lambda_105FA():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_105FA)
    Sleep(50)

    def lambda_1060A():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1060A)
    Sleep(50)

    def lambda_1061A():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1061A)
    Sleep(50)

    def lambda_1062A():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1062A)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        "#5PScott...?\x02",
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
            "too, just like him, and...\x02",
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
        "#5P...Well...\x02",
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
            "#11PWell, there haven't been accidents\x01",
            "like that recently, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI think the accident five years ago in\x01",
            "which Mr. Arios' wife and Shizuku\x01",
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
            "#5P#04003F...The transport explosion and fire accident\x01",
            "that happened on the main street five years ago...\x02\x03",
            "#04008FAt first, the malfunction of the orbal engine and\x01",
            "flammable load was thought to be the cause, but...\x01",
            "There were a lot of suspicious points in that case.\x02\x03",
            "#04001FArios' wife Saya passed\x01",
            "away due to it... And\x01",
            "Shizuku lost her sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FSo that's how it went down, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00208F...We heard bits and pieces of\x01",
            "that story before, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FAnd so, Mr. Arios quit the\x01",
            "police and joined the Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FI came to know Arios\x01",
            "after that too, but...\x02\x03",
            "Though he didn't say a single word about it, he\x01",
            "must've been carrying it with him this whole time.\x02\x03",
            "#04008F...When I think about it that\x01",
            "way, I finally understand why\x01",
            "he took up that important role.\x02",
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
            "#12P#00003F──Mr. Michel.\x02\x03",
            "#00001FI realize it's rude of me to ask, but...\x01",
            "Have there been any suspicious points\x01",
            "in Mr. Arios' schedule lately?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10D50():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_10D50)
    Sleep(50)

    def lambda_10D60():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_10D60)
    Sleep(50)

    def lambda_10D70():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_10D70)
    Sleep(50)

    def lambda_10D80():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10D80)
    Sleep(50)

    def lambda_10D90():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10D90)
    Sleep(50)

    def lambda_10DA0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10DA0)
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
            "#12P#00006FThe "State Guard" Commander in Chief...\x02\x03",
            "I think it's too important a\x01",
            "role to be taken up so suddenly.\x02\x03",
            "#00001FHe was probably laying the groundwork\x01",
            "for this with Mayor...no, with\x01",
            "President Dieter. Don't you think so?\x02\x03",
            "And not just recently either. For quite some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#04008F............\x02",
    )

    CloseMessageWindow()

    def lambda_10F34():
        TurnDirection(0xB, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_10F34)
    Sleep(50)

    def lambda_10F44():
        TurnDirection(0xA, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_10F44)
    Sleep(50)

    def lambda_10F54():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_10F54)
    Sleep(50)

    def lambda_10F64():
        TurnDirection(0xC, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_10F64)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    def lambda_10F84():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10F84)

    def lambda_10F91():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10F91)

    def lambda_10F9E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10F9E)

    ChrTalk(
        0xB,
        "#12PMichel...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I don't believe this! Is it true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FIt's true that his whereabouts\x01",
            "conflicted from time to time\x01",
            "in his various reports.\x02\x03",
            "#04008FI thought that number of mistakes was only natural\x01",
            "given the number of jobs he was carrying, but...\x02\x03",
            "#04001F...Rethinking it now, it's\x01",
            "actually extremely rare for him\x01",
            "to make mistakes in his reports.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Then, those are the times he was\x01",
            "in contact with Mayor Dieter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04003F...I think it's safe\x01",
            "to assume that.\x02\x03",
            "#04001FMy goddess, Lloyd. You're\x01",
            "so observant, it's scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo... I'm sorry to have\x01",
            "said something so rude.\x02\x03",
            "#00003FBut while I'm being rude, \x01",
            "I'd like to ask you something...\x02\x03",
            "#00008FRegarding the discrepancies between\x01",
            "Mr. Arios' schedule and whereabouts──\x02\x03",
            "#00013FDo you remember any of them\x01",
            "from half a year ago or more?\x02",
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

    def lambda_1137A():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1137A)

    def lambda_11387():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11387)
    Sleep(50)

    def lambda_11397():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_11397)
    Sleep(50)

    def lambda_113A7():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_113A7)
    Sleep(50)

    def lambda_113B7():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_113B7)
    Sleep(50)

    def lambda_113C7():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_113C7)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x102,
        "#6P#00105FHalf a year ago, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200F...Back when Mr. Dieter \x01",
            "wasn't even the mayor yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04006FH-Hmm... I don't\x01",
            "remember too well from\x01",
            "that far back, but...\x02\x03",
            "#04005FAh, but that happened, didn't it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_114D1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_114D1)
    Sleep(50)

    def lambda_114E1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_114E1)

    def lambda_114EE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_114EE)

    ChrTalk(
        0x101,
        "#12P#00005FThat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#04004FOn the final day of the Anniversary Festival.\x02\x03",
            "#04000FHe was away at a job\x01",
            "in Remiferia, but...\x02\x03",
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
            "#5P#04005FWhen I realized it later, I asked him\x01",
            "about it. He said only that he's\x01",
            "been busy and neglected to do so.\x02\x03",
            "#04001F...What? Are you worried about something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PWell that Anniversary Festival had\x01",
            "one hell of a punishing schedule...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PEven if that report had an inconsistency in it,\x01",
            "I think it's perfectly understandable.\x02",
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
        "#6P#00108F...The last day of the Anniversary Festival...\x02",
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
        "#00301F#12PHow's that and this connected?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F...I don't know. But I feel\x01",
            "there must be some connection.\x02\x03",
            "#00008FUp until now, we've been so busy.\x01",
            "We let point after point pass us by.\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_11919():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11919)
    Sleep(50)

    def lambda_11929():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11929)

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
            "Special Support Sect──\x02",
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
            ""Crossbell State Guard,\x01",
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
            "HU HU HU... NOW THEN,\x01",
            "I WONDER JUST WHO I AM?\x02\x03",
            "I'LL GIVE YOU A NICE PRESENT\x01",
            "IF YOU GET IT RIGHT──\x02",
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
            "#00006F...I've had enough of your pointless quizzes.\x02\x03",
            "#00010FWhat in the world brought\x01",
            "you to Crossbell?\x02",
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
            "Now, now, it seems I'm not very well liked.\x02\x03",
            "Things seem quite flashy there. And you mean\x01",
            "to tell me we can't have a little chat?\x02\x03",
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
            "#00006F...Understood.\x01",
            "Where do we go?\x02",
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
            ""Crimson & Co."...\x01",
            "Or perhaps I should say the\x01",
            "former "Revache & Co.".\x02\x03",
            "Let's make it the President's room over there.\x02",
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
            "#00008FSo the basement...\x01",
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
            "#6P#00101FCould it have been...\x01",
            "Mr. Cao, who went missing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200FHe contacted us not\x01",
            "long ago when Mr.\x01",
            "Randy disappeared...\x02",
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
            "#5P#00003F──No, it's not him.\x02\x03",
            "#00013FIt's Captain Lechter of the Imperial Army.\x02",
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
            "to Crossbell again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12P...I really do wonder what\x01",
            "the hell he's doin' here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FHe said he wants to speak with\x01",
            "us at the old Revache building.\x02\x03",
            "#00001FWhile it would be extremely careless not\x01",
            "to consider his connection with the "Red\x01",
            "Constellation"...we have no choice but to go.\x02",
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
        "#12P#00201FNothing ventured, nothing gained.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F...Though I think it's best\x01",
            "if we're fully prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#04006FYou guys have it so tough too...\x02",
    )

    CloseMessageWindow()

    def lambda_121A7():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_121A7)
    Sleep(50)

    def lambda_121B7():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_121B7)
    Sleep(50)

    def lambda_121C7():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_121C7)
    Sleep(50)

    def lambda_121D7():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_121D7)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x9,
        (
            "#11PIt looks like you're going up\x01",
            "against a troublesome opponent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PArundel of the Intelligence Division...\x01",
            "He's nothing but a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIf he's too much for you to handle, we'll\x01",
            "back you up, so don't hold back, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PRight. We'd be paying you\x01",
            "back for the Marshlands.\x02",
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
            "#12P#00204FIf it looks like we can't handle\x01",
            "it then please, lend us your aid.\x02",
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

    # Function_30_FA66 end

    def Function_31_12471(): pass

    label("Function_31_12471")

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
            "#30W──In that case, was measuring the will for independence\x01",
            "the very foundation of the referendum?\x02\x03",
            "No. That referendum was only to\x01",
            "ask if the "expressed will" should\x01",
            "have been carried out or not.\x02\x03",
            "The State Guard and the Independent State of Crossbell...\x02\x03",
            "And moreover, the President...\x01",
            "They're by no means tied to legitimacy!\x07\x00\x02",
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

    # Function_31_12471 end

    def Function_32_1273B(): pass

    label("Function_32_1273B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3020, 1700, 4270, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22460, 0)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_128BC")
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

    def lambda_12807():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12807)

    def lambda_12818():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12818)
    Sleep(50)

    def lambda_12835():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12835)

    def lambda_12846():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12846)
    Sleep(700)

    def lambda_12863():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12863)

    def lambda_12874():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12874)
    Sleep(50)

    def lambda_12891():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_12891)

    def lambda_128A2():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_128A2)
    Jump("loc_12B3D")

    label("loc_128BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_129FF")
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

    def lambda_1294A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1294A)

    def lambda_1295B():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1295B)
    Sleep(50)

    def lambda_12978():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_12978)

    def lambda_12989():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12989)
    Sleep(700)

    def lambda_129A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_129A6)

    def lambda_129B7():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_129B7)
    Sleep(50)

    def lambda_129D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_129D4)

    def lambda_129E5():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_129E5)
    Jump("loc_12B3D")

    label("loc_129FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_12B3D")
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

    def lambda_12A8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12A8D)

    def lambda_12A9E():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A9E)
    Sleep(50)

    def lambda_12ABB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_12ABB)

    def lambda_12ACC():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12ACC)
    Sleep(700)

    def lambda_12AE9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12AE9)

    def lambda_12AFA():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12AFA)
    Sleep(50)

    def lambda_12B17():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_12B17)

    def lambda_12B28():
        OP_98(0xFE, 0x0, 0x0, 0x1306, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_12B28)

    label("loc_12B3D")

    OP_68(-2140, 1300, 5160, 3000)
    OP_6F(0x1)
    WaitChrThread(0x1A2, 1)

    ChrTalk(
        0x1A2,
        (
            "#12PThis is the Bracer Guild,\x01",
            "Crossbell Branch...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00005F...Shing?\x01",
            "Why are you hiding?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12BF0")

    def lambda_12BD0():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12BD0)
    Sleep(50)

    def lambda_12BE0():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12BE0)
    Sleep(300)
    Jump("loc_12C47")

    label("loc_12BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12C1E")

    def lambda_12BFE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12BFE)
    Sleep(50)

    def lambda_12C0E():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12C0E)
    Sleep(300)
    Jump("loc_12C47")

    label("loc_12C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_12C47")

    def lambda_12C2C():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12C2C)
    Sleep(50)

    def lambda_12C3C():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12C3C)
    Sleep(300)

    label("loc_12C47")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#12PS-Shut up! None of your business!\x02",
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
            "#5P#N#04005FMy, you guys... What are you\x01",
            "doing with that cute boy there?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12D36")

    def lambda_12D06():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12D06)
    Sleep(50)

    def lambda_12D16():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12D16)
    Sleep(50)

    def lambda_12D26():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12D26)
    Sleep(300)
    Jump("loc_12DAD")

    label("loc_12D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12D74")

    def lambda_12D44():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12D44)
    Sleep(50)

    def lambda_12D54():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12D54)
    Sleep(50)

    def lambda_12D64():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12D64)
    Sleep(300)
    Jump("loc_12DAD")

    label("loc_12D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_12DAD")

    def lambda_12D82():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12D82)
    Sleep(50)

    def lambda_12D92():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12D92)
    Sleep(50)

    def lambda_12DA2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12DA2)
    Sleep(300)

    label("loc_12DAD")


    ChrTalk(
        0x8,
        (
            "#5P#N#04000FYou'll be in the way there,\x01",
            "so please come over here.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00105FY-Yes...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(330, 1300, 10820, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21390, 0)
    OP_93(0x8, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_12F0C")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x104, 1640, 0, 8800, 0)

    def lambda_12E9B():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_12E9B)
    Sleep(50)

    def lambda_12EB8():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12EB8)
    Sleep(50)

    def lambda_12ED5():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12ED5)
    Sleep(50)

    def lambda_12EF2():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12EF2)
    Jump("loc_1308D")

    label("loc_12F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_12FCF")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x109, 1640, 0, 8800, 0)

    def lambda_12F5E():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_12F5E)
    Sleep(50)

    def lambda_12F7B():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12F7B)
    Sleep(50)

    def lambda_12F98():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12F98)
    Sleep(50)

    def lambda_12FB5():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12FB5)
    Jump("loc_1308D")

    label("loc_12FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1308D")
    SetChrPos(0x1A2, 720, 0, 7600, 0)
    SetChrPos(0x102, 1390, 0, 7600, 0)
    SetChrPos(0x101, 510, 0, 8800, 0)
    SetChrPos(0x105, 1640, 0, 8800, 0)

    def lambda_13021():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_13021)
    Sleep(50)

    def lambda_1303E():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1303E)
    Sleep(50)

    def lambda_1305B():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1305B)
    Sleep(50)

    def lambda_13078():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13078)

    label("loc_1308D")

    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x8,
        (
            "#04000F#5PAnd, just who is\x01",
            "that boy, I wonder?\x02\x03",
            "#04005FCould he be lost and\x01",
            "looking for his parents?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FUmm, I'm not sure how to say this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PH-Hey, hey you! Is the "Divine\x01",
            "Blade of Wind" here right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004F#5PMy, you've got quite the way of speaking.\x02\x03",
            "#04000FWell, Arios isn't here now.\x02",
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
            "#04003FHmm, his words, actions and clothes...\x02\x03",
            "#04000FI see― This boy must be\x01",
            "connected to "Heiyue".\x01",
            "And an elder's grandson, no less.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1330C")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jump("loc_133E9")

    label("loc_1330C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1337D")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jump("loc_133E9")

    label("loc_1337D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_133E9")
    OP_63(0x1A2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_133E9")


    ChrTalk(
        0x102,
        "#12P#00105FW-Why do you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04011F#5PUhuhu, it was just to trick[kamakakeru]\x01",
            "you, but it looks like I was right.\x02\x03",
            "#04001FAh, by the way, you shouldn't trick\x01",
            "a male transvestite[okama], ok?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_13522")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_135FF")

    label("loc_13522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_13593")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_135FF")

    label("loc_13593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_135FF")
    OP_63(0x1A2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_135FF")


    ChrTalk(
        0x101,
        "#12P#00012FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHuh? This guy's appearance\x01",
            "and personality aren't normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PThat must be why this\x01",
            "is the Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006F#5PHmm. You've been rude this\x01",
            "whole time. You'll make a\x01",
            "fine "Heiyue" member.\x02\x03",
            "#04008FI think he'll only get worse.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_13740")

    ChrTalk(
        0x104,
        "#12P#00303FYeah, I agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13795")

    label("loc_13740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1376C")

    ChrTalk(
        0x109,
        "#12P#10106FYes, I agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13795")

    label("loc_1376C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_13795")

    ChrTalk(
        0x105,
        "#12P#10304FHu hu, I agree.\x02",
    )

    CloseMessageWindow()

    label("loc_13795")


    ChrTalk(
        0x8,
        (
            "#04000F#5PBut even so, why might\x01",
            "you be looking out for\x01",
            "Arios so much?\x02\x03",
            "It's not the case that we bear any\x01",
            "particular grudge against "Heiyue".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PH-Hmph... You're one to talk. \x01",
            "You've gotten in the elders' way\x01",
            "any number of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PWhether it's from the "Divine Blade of Wind" \x01",
            "or the "Immovable", do you know how many \x01",
            "losses we had to cover up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005F"The Immovable"...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004F#5PYes, Zin "The Immovable"―\x02\x03",
            "#04000FHe's a Republican A-rank bracer and a\x01",
            "master of the "Taito School" martial art.\x02\x03",
            "It's been rare lately, but\x01",
            "in the past he's helped this\x01",
            "branch a number of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F"Taito School"... If I remember right, \x01",
            "that's Miss Ling's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04000F#5PYes, he was Ling's senior.\x01",
            "Naturally, he's incredibly strong.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_13ADD")

    ChrTalk(
        0x104,
        (
            "#12P#00300FI see. You'd have to be,\x01",
            "to be a Bracer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B73")

    label("loc_13ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_13B31")

    ChrTalk(
        0x109,
        (
            "#12P#10100FThat makes sense. \x01",
            "The Guild is full of great people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B73")

    label("loc_13B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_13B73")

    ChrTalk(
        0x105,
        (
            "#12P#10300FHu hu. You'd have to be,\x01",
            "to be a Bracer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B73")


    ChrTalk(
        0x1A2,
        (
            "#12PThat may be, but the biggest\x01",
            "problem with the Guild is\x01",
            "that agreement you guys have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PI don't know if it's a guiding principle\x01",
            "or whatever, but you guys just do whatever\x01",
            "you want in the name of "Civilian Safety"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04004F#5PUh uh. Even if we follow that\x01",
            "principle, "noninterference" with\x01",
            "state powers limits it sometimes.\x02\x03",
            "#04005F...Wait boy, how many things\x01",
            "do you know at that age?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIndeed... To be honest, I can't\x01",
            "believe you know this much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHeh. Flattery will get you nowhere.\x01",
            "Anyway, the guys at the Guild are―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04006F#5PAlright, that's enough with your criticism\x01",
            "of the Guild. Kids will be kids, after all.\x02\x03",
            "#04000FBy the way, KeA and Shizuku\x01",
            "are on 2F right now.\x02\x03",
            "You should have a chat with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, come to think of it,\x01",
            "KeA was here now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FThat's right. Let's have the kids\x01",
            "speak with each other for awhile.\x02",
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

    # Function_32_1273B end

    def Function_33_13F48(): pass

    label("Function_33_13F48")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1940, 1100, 44370, 0)
    MoveCamera(36, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20320, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FB2")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06000.itp")

    label("loc_13FB2")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1400C")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x104, -2190, 0, 45050, 90)
    Jump("loc_140AB")

    label("loc_1400C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1405E")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x109, -2190, 0, 45050, 90)
    Jump("loc_140AB")

    label("loc_1405E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_140AB")
    SetChrPos(0x1A2, -3590, 0, 44040, 90)
    SetChrPos(0x102, -3590, 0, 44800, 90)
    SetChrPos(0x101, -2190, 0, 43920, 90)
    SetChrPos(0x105, -2190, 0, 45050, 90)

    label("loc_140AB")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 6)), scpexpr(EXPR_END)), "loc_14148")

    def lambda_140BA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_140BA)
    Sleep(50)

    def lambda_140CA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_140CA)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#11P#01102FAh, it's you guys.\x01",
            "Ehehe, how is it going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FHello. Looks like\x01",
            "you are working.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14312")

    label("loc_14148")

    SetScenarioFlags(0x14D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xD,
        "#11P#01110FAh, it's Lloyd and the gang!\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#11P#06002FAh... \x01",
            "Good morning, everyone.\x02",
        )
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
        "#6P#00102FIt's been awhile since we've seen you, Shizuku.\x02",
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
            "Uh uh, it has been awhile.\x02\x03",
            "It looks like you\x01",
            "are working.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_14312")


    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, I guess you\x01",
            "could say that.\x02",
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
        (
            "#11P#01105FHuh?\x01",
            "Who's he?\x02",
        )
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
        "#6PW-Who are you calling little!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI'm Shing! I'm a man who will bear \x01",
            "the burden of the "Heiyue" future\x01",
            "as one of its elders' grandson!\x02",
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
            "#11P#01105FWow. You're so small, but an adult\x01",
            "the same as Lloyd and the others!\x02\x03",
            "#01109FYou're that great, even though\x01",
            "you're that small, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#6PS-Small, small, small! Stop saying that!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_14609")
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
            "#11P#00304FHa ha. Keddo, destroyer\x01",
            "of impertinent boys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14768")

    label("loc_14609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1469C")
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
            "#11P#10109FAhaha... \x01",
            "(That's KeA for you.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14768")

    label("loc_1469C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_14768")
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
            "#11P#10309FHu hu. When it comes down to KeA, even a\x01",
            "distinguished grandson of the Heiyue loses his face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14768")

    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00109F*giggle*, Shing.\x02\x03",
            "These are KeA\x01",
            "and Shizuku.\x02\x03",
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
            "is Mr. Arios' daughter.\x01",
            "You mentioned him earlier.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6PT-That "Divine Blade of Wind"'s...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PY-You're a swordmaster \x01",
            "too, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PYour eyes have been closed this whole time. \x01",
            "You're practicing that "Mind's Eye" thing, right!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1497F")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_14A2C")

    label("loc_1497F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_149D8")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_14A2C")

    label("loc_149D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_14A2C")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_14A2C")


    ChrTalk(
        0xD,
        "#11P#01105FMind's...eye?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005F"Mind's Eye", huh... Why do\x01",
            "you know something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FAhaha... \x01",
            "Umm, I actually can't see.\x02\x03",
            "Although my hearing is good because of it,\x01",
            "I am not as cool as my father, you know?\x02",
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
            "#6PThat was ungentlemanly of\x01",
            "me... Please forgive me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11P#06002FUh uh, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005F(Eeh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102F(*giggle*, I knew he was\x01",
            "a good kid at his core.)\x02",
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

    # Function_33_13F48 end

    def Function_34_14C67(): pass

    label("Function_34_14C67")

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
        "#11P#01110FAh, it's Lloyd and the gang!\x02",
    )

    CloseMessageWindow()
    OP_4B(0xE, 0xFF)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x10E, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#11P#06002FAh... \x01",
            "Good morning, everyone.\x02",
        )
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
        "#6P#00100FIt's been awhile since we've seen you, Shizuku.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11P#06000FUh uh, yes, it has been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FWow, so this girl is the daughter\x01",
            "of the "Divine Blade of Wind"?\x02\x03",
            "#10309FHu hu. She's cute,\x01",
            "just like I've heard.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_150E9")

    ChrTalk(
        0x109,
        "#6P#10109FJust like I told you, right?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#11P#06005FThis voice is...\x01",
            "It's Miss Noｱl, isn't it?\x02\x03",
            "#06002FYou helped me look for a\x01",
            "present for my father before.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#6P#10105FWah, you remember that?\x02\x03",
            "#10109FWe weren't together very long...\x01",
            "Uh uh, I'm happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06002FEhehe, KeA said\x01",
            "you had some\x01",
            "new members.\x02\x03",
            "#06000FAnd... Are these them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWazy Hemisphere.\x01",
            "Hu hu, pleased to meet you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152C4")

    label("loc_150E9")


    ChrTalk(
        0x109,
        "#6P#10109FYes, you're just like Fran said!\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#11P#06005FUmm... Who are they?\x02\x03",
            "KeA said you had\x01",
            "some new members...\x01",
            "Could they be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FOh, come to think of it, we haven't met.\x02\x03",
            "#10109FI'm Noｱl Seeker. Would you\x01",
            "understand if I told you\x01",
            "I'm Fran's older sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06005FAh, so you're Miss Fran's...\x01",
            "Now that you mention it, I feel\x01",
            "you have a similar air somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FI'm Wazy Hemisphere.\x01",
            "Hu hu, pleased to meet you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152C4")


    ChrTalk(
        0xE,
        (
            "#11P#06002FYes, same here.\x01",
            "Nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01109FC'mon! You gotta introduce\x01",
            "yourself too, Shizuku!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#06005FAh... That's\x01",
            "right, then.\x02",
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
            "I understand you have been \x01",
            "helping my father a great deal, \x01",
            "Support  Section.\x02\x03",
            "I would like to thank you \x01",
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
            "helped by Mr. Arios, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FHmm, I guess you could say that...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#11P#06010FT-That's not true.\x02\x03",
            "In that incident earlier,\x01",
            "you all helped him a lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHa ha, this kid is always\x01",
            "on the ball, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#01102FHey, are you guys gonna play\x01",
            "with KeA and Shizuku too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FAh, no. Because\x01",
            "Shizuku's here, I just\x01",
            "thought we'd say hi.\x02\x03",
            "#00000FWe've got work to do.\x01",
            "You can play with Shizuku as\x01",
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

    # Function_34_14C67 end

    def Function_35_1575A(): pass

    label("Function_35_1575A")

    EventBegin(0x1)
    SetChrPos(0x0, -2110, 0, 740, 0)
    EventEnd(0x4)
    Return()

    # Function_35_1575A end

    SaveToFile()

Try(main)
