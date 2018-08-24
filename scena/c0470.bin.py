from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0470.bin",                # FileName
        "c0470",                    # MapName
        "c0470",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 37, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0470",                  # 0
        "Owner Drake",            # 1
        "Cherry",                 # 2
        "Galletti",               # 3
        "Elinde",                 # 4
        "Rey Talossa",            # 5
        "Grandpa Rikke",          # 6
        "Grandma Holly",          # 7
        "Tourist",                # 8
        "Miner Marlow",           # 9
        "Miner Gantz",            # 10
        "Yuri",                   # 11
        "Sykes",                  # 12
        "Reggie",                 # 13
        "Lechter",                # 14
        "Redheaded Girl",         # 15
        "Redheaded Girl",         # 16
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch07402.itc",                   # 01
        "chr/ch33302.itc",                   # 02
        "chr/ch25900.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch27100.itc",                   # 05
        "chr/ch20002.itc",                   # 06
        "chr/ch33000.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch30702.itc",                   # 09
        "chr/ch44102.itc",                   # 0A
        "chr/ch47500.itc",                   # 0B
        "chr/ch23600.itc",                   # 0C
        "chr/ch20100.itc",                   # 0D
        "chr/ch20000.itc",                   # 0E
    ))

    DeclNpc(4294966397, 4000,    21299,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6199,    4294966296, 8000,    270,  261,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       4294966296, 13649,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294960796, 4294966296, 6000,    90,   261,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(1350,    4294966397, 11500,   0,    325,  0x0, 0,   2,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   14,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4239,    4294966296, 13649,   225,  389,  0x0, 0,   13,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294963977, 4294966296, 5599,    270,  389,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(6690,    4000,    11539,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(6690,    4269,    10460,   90,   453,  0x0, 0,   9,   0,   255, 255, 0,   21,  255,  0)
    DeclNpc(2480,    4294966296, 11720,   225,  389,  0x0, 0,   10,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(4389,    4294966296, 12359,   225,  389,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4239,    4294966296, 13649,   225,  389,  0x0, 0,   12,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 29,  4.0,                   3.5,                   4.5,                   225.0,                 [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.6666666865348816,   -0.699999988079071,    -0.9000000357627869,   1.0])

    DeclActor(4294966396, 4000,    20000,   2000,    4294966396, 5500,    21300,   0x007E, 0,  3,  0x0000)
    DeclActor(5240,    4294966296, 8000,    1200,    6200,    500,     8000,    0x007E, 0,  6,  0x0000)
    DeclActor(4294966376, 4294966296, 12050,   1700,    0,       500,     13650,   0x007E, 0,  9,  0x0000)
    DeclActor(4294962796, 4294966296, 6000,    1500,    4294960796, 500,     6000,    0x007E, 0,  12, 0x0000)
    DeclActor(7530,    4000,    17960,   1800,    7530,    5500,    17960,   0x007C, 0,  27, 0x0000)
    DeclActor(7530,    4000,    15750,   1800,    7530,    5500,    15750,   0x007C, 0,  27, 0x0000)
    DeclActor(7530,    4000,    13410,   1800,    7530,    5500,    13410,   0x007C, 0,  27, 0x0000)
    DeclActor(7530,    4000,    10460,   1800,    7530,    5500,    10460,   0x007C, 0,  27, 0x0000)
    DeclActor(7530,    4000,    8300,    1800,    7530,    5500,    8300,    0x007C, 0,  27, 0x0000)

    ChipFrameInfo(1224, 0)                                       # 0

    ScpFunction((
        "Function_0_4C8",          # 00, 0
        "Function_1_578",          # 01, 1
        "Function_2_806",          # 02, 2
        "Function_3_906",          # 03, 3
        "Function_4_90A",          # 04, 4
        "Function_5_244C",         # 05, 5
        "Function_6_2A84",         # 06, 6
        "Function_7_2A88",         # 07, 7
        "Function_8_3A6E",         # 08, 8
        "Function_9_3AA3",         # 09, 9
        "Function_10_3AA7",        # 0A, 10
        "Function_11_49CD",        # 0B, 11
        "Function_12_4A7E",        # 0C, 12
        "Function_13_4A82",        # 0D, 13
        "Function_14_5951",        # 0E, 14
        "Function_15_68E7",        # 0F, 15
        "Function_16_7842",        # 10, 16
        "Function_17_792C",        # 11, 17
        "Function_18_7C42",        # 12, 18
        "Function_19_7CDF",        # 13, 19
        "Function_20_7D6C",        # 14, 20
        "Function_21_7E96",        # 15, 21
        "Function_22_7F95",        # 16, 22
        "Function_23_8133",        # 17, 23
        "Function_24_819F",        # 18, 24
        "Function_25_8238",        # 19, 25
        "Function_26_83B3",        # 1A, 26
        "Function_27_9362",        # 1B, 27
        "Function_28_93F9",        # 1C, 28
        "Function_29_9A29",        # 1D, 29
        "Function_30_B7ED",        # 1E, 30
        "Function_31_B837",        # 1F, 31
        "Function_32_B881",        # 20, 32
        "Function_33_B8CB",        # 21, 33
        "Function_34_B915",        # 22, 34
        "Function_35_B964",        # 23, 35
        "Function_36_B985",        # 24, 36
    ))


    def Function_0_4C8(): pass

    label("Function_0_4C8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_500"),
        (1, "loc_50C"),
        (2, "loc_518"),
        (3, "loc_524"),
        (4, "loc_530"),
        (5, "loc_53C"),
        (6, "loc_548"),
        (SWITCH_DEFAULT, "loc_554"),
    )


    label("loc_500")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_50C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_518")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_524")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_530")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_53C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_548")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_554")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_560")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_577")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_560")

    label("loc_577")

    Return()

    # Function_0_4C8 end

    def Function_1_578(): pass

    label("Function_1_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D0")
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrPos(0x15, 6540, 4270, 13420, 90)
    SetChrChipByIndex(0x15, 0x1)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetScenarioFlags(0x1, 2)

    label("loc_5D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EB")
    SetChrChipByIndex(0xC, 0x2)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_606")
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_680")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -800, -1000, 7000, 90)
    SetChrPos(0xD, 800, -1000, 7000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64F")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_64F")

    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrPos(0x15, 6700, 4270, 15750, 90)
    SetChrChipByIndex(0x15, 0x1)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jump("loc_805")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_69D")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_805")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6CB")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jump("loc_805")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6D9")
    Jump("loc_805")

    label("loc_6D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6E7")
    Jump("loc_805")

    label("loc_6E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6F5")
    Jump("loc_805")

    label("loc_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_708")
    SetChrFlags(0xD, 0x10)
    Jump("loc_805")

    label("loc_708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_716")
    Jump("loc_805")

    label("loc_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_77C")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x13, 0x10)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrPos(0x12, -3460, -850, 12370, 45)
    SetChrPos(0x14, -3120, -1000, 10900, 90)
    SetChrPos(0x13, -4310, -1000, 12730, 90)
    Jump("loc_805")

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_78A")
    Jump("loc_805")

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7BD")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    Jump("loc_805")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D5")
    SetChrFlags(0xD, 0x10)

    label("loc_7D5")

    Jump("loc_805")

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7FC")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xF, 0x10)
    Jump("loc_805")

    label("loc_7FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_805")

    label("loc_805")

    Return()

    # Function_1_578 end

    def Function_2_806(): pass

    label("Function_2_806")

    SetMapObjFrame(0xFF, "white00", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84E")
    ModifyEventFlags(1, 0, 0x80)
    SetMapObjFrame(0xFF, "white00", 0x0, 0x2)

    label("loc_84E")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_864")
    OP_65(0x7, 0x1)

    label("loc_864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_876")
    OP_65(0x7, 0x1)

    label("loc_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88C")
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)

    label("loc_88C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A8")
    OP_10(0x0, 0x0)
    OP_10(0x4, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_8CD")

    label("loc_8A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8C4")
    OP_10(0x0, 0x0)
    OP_10(0x4, 0x1)
    OP_10(0x3, 0x0)
    Jump("loc_8CD")

    label("loc_8C4")

    OP_10(0x0, 0x1)
    OP_10(0x4, 0x0)
    OP_10(0x3, 0x0)

    label("loc_8CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EE")
    Sound(128, 1, 30, 0)

    label("loc_8EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_905")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_905")

    Return()

    # Function_2_806 end

    def Function_3_906(): pass

    label("Function_3_906")

    Call(0, 4)
    Return()

    # Function_3_906 end

    def Function_4_90A(): pass

    label("Function_4_90A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91C")
    Call(0, 28)
    Return()

    label("loc_91C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B10")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "...Randy, you're heading\x01",
            "to that Huge Tree,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHaha, you know me well.\x01",
            "I expected no less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph. We haven't known\x01",
            "each other all that\x01",
            "long, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Randy, you've still got\x01",
            "a bit left on your tab\x01",
            "from all your drinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I won't accept it unless\x01",
            "you come back in one\x01",
            "piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F...Yeah, got it.\x02\x03",
            "#00309FI'll pay it back\x01",
            "eventually, so don't\x01",
            "sweat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Haha... I guess this is\x01",
            "how these two\x01",
            "communicate.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 0)
    Jump("loc_CB0")

    label("loc_B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C45")

    ChrTalk(
        0x8,
        (
            "Right now, hard times\x01",
            "could be coming to\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Everyone, please take\x01",
            "good care of Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After all, that guy still\x01",
            "has a bit left on his tab\x01",
            "from all his drinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, of course. Leave it\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FI'll pay it back\x01",
            "eventually, so don't\x01",
            "sweat it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CB0")

    label("loc_C45")


    ChrTalk(
        0x8,
        (
            "Right now, hard times\x01",
            "could be coming to\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Everyone, please take\x01",
            "good care of Randy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB0")

    Jump("loc_2448")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1012")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E68")

    ChrTalk(
        0x8,
        (
            "Ohh, if it isn't you\x01",
            "all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FBeen a while, Owner.\x01",
            "Looks like you've doin'\x01",
            "fine?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)

    ChrTalk(
        0x8,
        "You too, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard you threw yourself into Mainz\x01",
            "resistance activities, but I'm glad\x01",
            "you've reunited with your colleagues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWas anyone here injured?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "No, at least for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please be very\x01",
            "careful if you're\x01",
            "walking around town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah, you too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 7)
    Jump("loc_100D")

    label("loc_E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F69")

    ChrTalk(
        0x8,
        (
            "Anyhow, I was right in\x01",
            "downsizing my business\x01",
            "because of martial law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With this small group, we can\x01",
            "hold out on our emergency\x01",
            "reserves for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please don't worry about\x01",
            "us. Everyone, please focus\x01",
            "on what you have to do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100D")

    label("loc_F69")


    ChrTalk(
        0x8,
        (
            "With this small group, we can\x01",
            "hold out on our emergency\x01",
            "reserves for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please don't worry about\x01",
            "us. Everyone, please focus\x01",
            "on what you have to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100D")

    Jump("loc_2448")

    label("loc_1012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_119B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110C")

    ChrTalk(
        0x8,
        (
            "Hmm... I thought there were a bunch of\x01",
            "guys wearing unfamiliar uniforms this\x01",
            "morning. So they're State Guard soldiers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Indeed, they look fully\x01",
            "ready...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder when Mr. Crois\x01",
            "first pictured this\x01",
            "scenario...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1196")

    label("loc_110C")


    ChrTalk(
        0x8,
        (
            "Come to think of it, it\x01",
            "hasn't even been a week\x01",
            "since the referendum...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder when Mr. Crois\x01",
            "first pictured this\x01",
            "scenario...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1196")

    Jump("loc_2448")

    label("loc_119B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_151E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149A")

    ChrTalk(
        0x8,
        (
            "Hey, Randy. I don't know what\x01",
            "happened, but that face of yours says\x01",
            "you're no longer harboring any doubts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although my business is in a\x01",
            "slump due to the situation, I\x01",
            "wonder what you plan to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHmm? To me, it's like\x01",
            "nothing's changed, you know?\x02\x03",
            "#00309FSay Owner, are you gettin'\x01",
            "lonely after not seein' my\x01",
            "face for such a short while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, nonsense. On the contrary,\x01",
            "I've been doing just fine with\x01",
            "my picky customer gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyhow, I've lent you a\x01",
            "lot of "stuff" up until\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "See that you don't evade\x01",
            "your responsibilities until\x01",
            "you've repaid me in full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHah, I know without you\x01",
            "tellin' me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(These two get along\x01",
            "well somehow, don't\x01",
            "they.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes, just like two\x01",
            "kids.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 1)
    Jump("loc_1519")

    label("loc_149A")


    ChrTalk(
        0x8,
        (
            "Anyhow, don't forget\x01",
            "about the stuff I lent\x01",
            "you, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The term isn't fixed,\x01",
            "but you've got to pay me\x01",
            "back someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1519")

    Jump("loc_2448")

    label("loc_151E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_167D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1601")

    ChrTalk(
        0x8,
        (
            "All I can do for that\x01",
            "guy is give him a place\x01",
            "to drink in peace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, I feel that you\x01",
            "all can, in a real sense,\x01",
            "be of help to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please... I\x01",
            "leave Randy in your\x01",
            "care.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1678")

    label("loc_1601")


    ChrTalk(
        0x8,
        (
            "I feel that you all can,\x01",
            "in a real sense, be of\x01",
            "help to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please... I\x01",
            "leave Randy in your\x01",
            "care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1678")

    Jump("loc_2448")

    label("loc_167D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_17FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176E")

    ChrTalk(
        0x8,
        (
            "At last, tomorrow is\x01",
            "opening day of the Arc-en-\x01",
            "Ciel renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems a promising rookie\x01",
            "in addition to Rixia Mao\x01",
            "will debut in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe. The topic of Arc-\x01",
            "en-Ciel always\x01",
            "entertains me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17F5")

    label("loc_176E")


    ChrTalk(
        0x8,
        (
            "It seems a promising rookie\x01",
            "in addition to Rixia Mao\x01",
            "will debut in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe. The topic of Arc-\x01",
            "en-Ciel always\x01",
            "entertains me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F5")

    Jump("loc_2448")

    label("loc_17FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D0")

    ChrTalk(
        0x8,
        (
            "Welcome. Welcome to\x01",
            "Casino House Barca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you want to rest\x01",
            "your brain, please make\x01",
            "use of our bar counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Naturally we serve\x01",
            "alcohol, but also coffee\x01",
            "and other things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_195E")

    label("loc_18D0")


    ChrTalk(
        0x8,
        (
            "When you want to rest\x01",
            "your brain, please make\x01",
            "use of our bar counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Naturally we serve\x01",
            "alcohol, but also coffee\x01",
            "and other things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195E")

    Jump("loc_2448")

    label("loc_1963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AEC")

    ChrTalk(
        0x8,
        (
            "The question of state independence... This is\x01",
            "still one hell of a problem among the squirming\x01",
            "power relationships in the underground world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't really think that the referendum\x01",
            "will be tied to immediate action, but... The\x01",
            "problem is the actions of the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it's handled poorly,\x01",
            "Crossbell's position will get\x01",
            "even worse than it is now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BC4")

    label("loc_1AEC")


    ChrTalk(
        0x8,
        (
            "I can't really think that the referendum\x01",
            "will be tied to immediate action, but... The\x01",
            "problem is the actions of the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If handled poorly,\x01",
            "Crossbell's position will get\x01",
            "even worse than it is now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC4")

    Jump("loc_2448")

    label("loc_1BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C49")

    ChrTalk(
        0x8,
        (
            "Hmm, it seems it's a\x01",
            "little noisy downstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If they get any louder,\x01",
            "I'll have to ask them to\x01",
            "leave...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2448")

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CC3")

    ChrTalk(
        0x8,
        (
            "Welcome. Welcome to\x01",
            "Casino House Barca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How about a sweet\x01",
            "cocktail to melt both\x01",
            "body and soul...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2448")

    label("loc_1CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1D3C")

    ChrTalk(
        0x8,
        (
            "It appears the Orchis\x01",
            "Tower unveiling ceremony\x01",
            "ended in a success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh, I'll check it out\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2448")

    label("loc_1D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2111")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA9")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Hey, Randy. Already\x01",
            "sober from yesterday's\x01",
            "liquor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHah, that goes without sayin'. Did\x01",
            "you think that tiny amount of\x01",
            "liquor'd stay in me for a whole day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, always quick with\x01",
            "the back talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it was to celebrate\x01",
            "your return, don't think of it\x01",
            "as some kind of treat, alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHaha, sorry. But I'm\x01",
            "still grateful, you\x01",
            "know?\x02\x03",
            "#00300FAnd so, Owner, let's do\x01",
            "it again if chance\x01",
            "arises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, always saying\x01",
            "whatever you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Looks like Randy's\x01",
            "showing his cheeky side,\x01",
            "huh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Yeah, you can say that\x01",
            "again.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    SetScenarioFlags(0x14C, 2)
    Jump("loc_210C")

    label("loc_1FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207E")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Well, if you want me to\x01",
            "treat you again, you should\x01",
            "fix that back talk of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do that, I'll\x01",
            "think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah, yeah. Well, I'll\x01",
            "be more discreet.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_210C")

    label("loc_207E")

    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Well, if you want me to\x01",
            "treat you again, you should\x01",
            "fix that back talk of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do that, I'll\x01",
            "think about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    label("loc_210C")

    Jump("loc_2448")

    label("loc_2111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212C")
    Call(0, 5)
    Jump("loc_2391")

    label("loc_212C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E2")

    ChrTalk(
        0x8,
        (
            "Recently, some small fry asking\x01",
            "for protection mira have\x01",
            "appeared to replace Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At present I won't oppose\x01",
            "them, but if the situation\x01",
            "continues, it'll be trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My my, they want to\x01",
            "quickly take over all of\x01",
            "Revache's abandoned turf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F(So the effects of\x01",
            "Revache's disappearance\x01",
            "showed up here, too...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(This is one of the places\x01",
            "that helped them maintain\x01",
            "their kind of order.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2391")

    label("loc_22E2")


    ChrTalk(
        0x8,
        (
            "At present they're relatively well\x01",
            "behaved... But if the situation\x01",
            "goes on, it'll be trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My my, they want to\x01",
            "quickly take over all of\x01",
            "Revache's abandoned turf.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2391")

    Jump("loc_2448")

    label("loc_2396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2448")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B1")
    Call(0, 5)
    Jump("loc_2448")

    label("loc_23B1")


    ChrTalk(
        0x8,
        (
            "That Randy is doing fine\x01",
            "hanging out with the\x01",
            "CGF, isn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe. Well if it helps him\x01",
            "not say pathetic things like\x01",
            "in the past, then good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2448")

    TalkEnd(0x8)
    Return()

    # Function_4_90A end

    def Function_5_244C(): pass

    label("Function_5_244C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B1")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "The Special Support\x01",
            "Section... And if it\x01",
            "isn't Wazy too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's quite the unusual\x01",
            "combination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYeah, Owner. Actually,\x01",
            "I've been assigned to the\x01",
            "Special Support Section.\x02\x03",
            "I'll omit the details,\x01",
            "but please treat me as\x01",
            "one of them from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I understand... Hehe, as\x01",
            "you wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FH-He readily accepted\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat is true, but... So\x01",
            "you're an acquaintance\x01",
            "of Owner's, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, to a host, this area is\x01",
            "a workplace, casino included.\x02\x03",
            "#10300FConversely, wouldn't a host\x01",
            "who didn't know Owner Drake\x01",
            "be unqualified or third rate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHe says it so\x01",
            "nonchalantly...\x02\x03",
            "#10101FAnd also, playing around\x01",
            "this neighborhood at\x01",
            "your age isn't good.\x02\x03",
            "#10103FYou should take this\x01",
            "opportunity to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe, stuffy as always.\x02\x03",
            "Well, I think that's\x01",
            "another of your charm\x01",
            "points㈱\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27DA")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_27DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2800")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2800")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2826")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2826")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_284C")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_284C")

    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10106F*sigh*, all of a sudden\x01",
            "I don't care anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FI know the feeling.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 7)
    Jump("loc_2A83")

    label("loc_28B1")


    ChrTalk(
        0x8,
        (
            "By the way, everyone,\x01",
            "hasn't Randy come back\x01",
            "yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard before from the man\x01",
            "himself that he went back to\x01",
            "his former home, the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, I think we'll be able\x01",
            "to reunite with him just\x01",
            "in a little while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I understand. Then, well,\x01",
            "could you please tell him to\x01",
            "stop by when he gets back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tell him that I've\x01",
            "prepared a bottle of wine\x01",
            "to celebrate his return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe'll be sure to tell\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 6)

    label("loc_2A83")

    Return()

    # Function_5_244C end

    def Function_6_2A84(): pass

    label("Function_6_2A84")

    Call(0, 7)
    Return()

    # Function_6_2A84 end

    def Function_7_2A88(): pass

    label("Function_7_2A88")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",          # 0
            "Exchange\x01",      # 1
            "Cancel\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AEB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2AEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2B0A")
    OP_AF(0x41)
    Jump("loc_2B4C")

    label("loc_2B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B1A")
    OP_AF(0x40)
    Jump("loc_2B4C")

    label("loc_2B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B2A")
    OP_AF(0x3F)
    Jump("loc_2B4C")

    label("loc_2B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B3A")
    OP_AF(0x3E)
    Jump("loc_2B4C")

    label("loc_2B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B4A")
    OP_AF(0x3D)
    Jump("loc_2B4C")

    label("loc_2B4A")

    OP_AF(0x3C)

    label("loc_2B4C")

    Call(0, 8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A65")

    label("loc_2B5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B72")
    Jump("loc_3A65")

    label("loc_2B72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A65")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C10")

    ChrTalk(
        0x9,
        (
            "Welcome, welcome to\x01",
            "Casino House Barca!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please go play a lot and\x01",
            "rid yourself of your\x01",
            "worries☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C8E")

    label("loc_2C10")


    ChrTalk(
        0x9,
        (
            "Even at a time like\x01",
            "this, we're open for\x01",
            "business as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please go play a lot and\x01",
            "rid yourself of your\x01",
            "worries☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C8E")

    Jump("loc_3A65")

    label("loc_2C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D58")

    ChrTalk(
        0x9,
        (
            "Oooh. I'm honestly scared, but...\x01",
            "I'm glad that Mr. Galletti and\x01",
            "Miss Elinde got a vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The owner is doing his\x01",
            "best, so I have to get\x01",
            "my act together too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E22")

    label("loc_2D58")


    ChrTalk(
        0x9,
        (
            "Because Mr. Galletti and Miss\x01",
            "Elinde are on holiday, you can't\x01",
            "play on the ground floor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There could be something useful\x01",
            "among our prizes, so use this\x01",
            "exchange counter as always, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E22")

    Jump("loc_3A65")

    label("loc_2E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2EBB")

    ChrTalk(
        0x9,
        (
            "Uuhm, this won't turn\x01",
            "into a sudden war, will\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what kind of\x01",
            "statements the major powers\x01",
            "will issue in response.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A65")

    label("loc_2EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2F44")

    ChrTalk(
        0x9,
        "Uuhm, a referendum?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They say there will be several\x01",
            "polling places, but if I'm going,\x01",
            "I'm going to Orchis Tower☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A65")

    label("loc_2F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2FD7")

    ChrTalk(
        0x9,
        (
            "Uuhm, although they're\x01",
            "outside Crossbell City, Mainz\x01",
            "events are our problem, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope the situation's\x01",
            "resolved quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A65")

    label("loc_2FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_30DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3082")

    ChrTalk(
        0x9,
        (
            "Arc-en-Ciel's\x01",
            "performance will finally\x01",
            "open tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sure we'll have\x01",
            "guests flowing in again\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uhu, I can't wait㈱\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30D5")

    label("loc_3082")


    ChrTalk(
        0x9,
        (
            "A lot of people come\x01",
            "here after seeing Arc-\x01",
            "en-Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uhu, I can't wait㈱\x02",
    )

    CloseMessageWindow()

    label("loc_30D5")

    Jump("loc_3A65")

    label("loc_30DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3153")

    ChrTalk(
        0x9,
        (
            "Tell me whenever you've\x01",
            "run out of medals, ok?☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And if you've run out of\x01",
            "mira, let's go to IBC!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A65")

    label("loc_3153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_31AD")

    ChrTalk(
        0x9,
        "Welcome to Barca~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uhuhu. Please go play a\x01",
            "lot again today, ok?☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A65")

    label("loc_31AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_324D")

    ChrTalk(
        0x9,
        (
            "That three-man group... They\x01",
            "look rich, but I feel like\x01",
            "they're very bad people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They were rather\x01",
            "arrogant. Should I ask\x01",
            "them to leave?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A65")

    label("loc_324D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32DC")

    ChrTalk(
        0x9,
        (
            "At last, the trade\x01",
            "conference will be held\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Cherry doesn't really\x01",
            "get it, but at any rate,\x01",
            "I hope it goes well㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A65")

    label("loc_32DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3409")

    ChrTalk(
        0x9,
        (
            "It looks like that Mr. Gantz\x01",
            "hasn't learned and is hard at\x01",
            "work at the slots again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although he's doing so poorly, you\x01",
            "wonder what the heck that luck he\x01",
            "had some months ago was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Could it be that Mr. Gantz\x01",
            "used up all the luck of a\x01",
            "lifetime back then?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34B8")

    label("loc_3409")


    ChrTalk(
        0x9,
        (
            "Could it be that Mr. Gantz\x01",
            "used up all the luck of a\x01",
            "lifetime back then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well anyway, it looks like he\x01",
            "wins eeevery once in a long\x01",
            "while, so that's probably not it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B8")

    Jump("loc_3A65")

    label("loc_34BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F7")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x104, 0)

    ChrTalk(
        0x9,
        "Ah, it's Mr. Randyyy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Geez, where have you been these\x01",
            "days? That's no good, you've\x01",
            "got to come here more often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FMan, sorry there Cherry.\x02\x03",
            "#00309FAnd so, I've just got to\x01",
            "hurry and finish work\x01",
            "and―\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3662")

    ChrTalk(
        0x101,
        "#00009FHey, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, of course you're\x01",
            "joking, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FY-Yeah... Hey, your\x01",
            "smiles are scary, you\x01",
            "know that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36EF")

    label("loc_3662")


    ChrTalk(
        0x102,
        (
            "#00109FHey, Randy. I think we\x01",
            "just told you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FY-Yeah... That's just a\x01",
            "joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Randy... You really\x01",
            "never learn.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36EF")

    SetScenarioFlags(0x14C, 3)
    Jump("loc_373E")

    label("loc_36F7")


    ChrTalk(
        0x9,
        (
            "Mr. Randy, come often,\x01",
            "ok~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Or else, Cherry will be\x01",
            "booored.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_373E")

    Jump("loc_3A65")

    label("loc_3743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_37AE")

    ChrTalk(
        0x9,
        (
            "Brush away this wet and\x01",
            "gloomy rain at the\x01",
            "casinooo☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Play all you want today\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A65")

    label("loc_37AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3971")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C2")

    ChrTalk(
        0x9,
        (
            "Some time ago, all of a sudden,\x01",
            "Mr. Lechter stopped by and went\x01",
            "up to the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. I saw him some months\x01",
            "ago, but he's always a\x01",
            "strange man, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FLloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah. He's not getting\x01",
            "away this time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_396C")

    label("loc_38C2")


    ChrTalk(
        0x9,
        (
            "Some time ago, all of a sudden,\x01",
            "Mr. Lechter stopped by and went\x01",
            "up to the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. I saw him some months\x01",
            "ago, but he's always a\x01",
            "strange man, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_396C")

    Jump("loc_3A65")

    label("loc_3971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A00")

    ChrTalk(
        0x9,
        "Welcome to Barca~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This the medal and prize\x01",
            "exchange counter㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Play lots and lots and\x01",
            "get a nice prize, ok?☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A65")

    label("loc_3A00")


    ChrTalk(
        0x9,
        (
            "This the medal and prize\x01",
            "exchange counter㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Play lots and lots and\x01",
            "get a nice prize, ok?☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A65")

    Jump("loc_2A95")

    label("loc_3A6A")

    TalkEnd(0x9)
    Return()

    # Function_7_2A88 end

    def Function_8_3A6E(): pass

    label("Function_8_3A6E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AA2")
    SubItemNumber(0x18C, 1)
    AddItemNumber(0x186, 1)
    AddItemNumber(0x187, 1)
    AddItemNumber(0x188, 1)
    AddItemNumber(0x189, 1)
    AddItemNumber(0x18A, 1)
    Jump("Function_8_3A6E")

    label("loc_3AA2")

    Return()

    # Function_8_3A6E end

    def Function_9_3AA3(): pass

    label("Function_9_3AA3")

    Call(0, 10)
    Return()

    # Function_9_3AA3 end

    def Function_10_3AA7(): pass

    label("Function_10_3AA7")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49C9")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                # 0
            "Play Poker\x01",          # 1
            "Play Blackjack\x01",      # 2
            "Cancel\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B1B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3B1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B70")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3B70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BC5")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3BC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BD9")
    Jump("loc_49C4")

    label("loc_3BD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49C4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF9")

    ChrTalk(
        0xA,
        (
            "Our regular Miss Rey Talossa\x01",
            "went back to her country and\x01",
            "I'm feeling rather lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After all, the thrilling\x01",
            "matches against her were\x01",
            "my daily pleasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope she comes to visit\x01",
            "again after Crossbell\x01",
            "regains its peace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3DA6")

    label("loc_3CF9")


    ChrTalk(
        0xA,
        (
            "Our regular Miss Rey Talossa... I\x01",
            "hope she comes to visit again\x01",
            "after Crossbell regains its peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's been difficult\x01",
            "since that mysterious\x01",
            "tree appeared, and...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA6")

    Jump("loc_49C4")

    label("loc_3DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3DB9")
    Jump("loc_49C4")

    label("loc_3DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3FCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF5")

    ChrTalk(
        0xA,
        (
            "Today, it seems that the\x01",
            "orbal rail service has been\x01",
            "limited since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Official announcements were made advising the\x01",
            "Imperial and Republican citizens in Crossbell\x01",
            "to return to their countries of origin...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The situation could be\x01",
            "moving along faster than\x01",
            "we're thinking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FC5")

    label("loc_3EF5")


    ChrTalk(
        0xA,
        (
            "Official announcements were made advising the\x01",
            "Imperial and Republican citizens in Crossbell\x01",
            "to return to their countries of origin...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The situation could be\x01",
            "moving along faster than\x01",
            "we're thinking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC5")

    Jump("loc_49C4")

    label("loc_3FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_419B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40EB")

    ChrTalk(
        0xA,
        (
            "When I see the burns remaining\x01",
            "on the ground even now... I am\x01",
            "reminded of the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Fortunately, the armed\x01",
            "group didn't enter our\x01",
            "store, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If we had been attacked, what would\x01",
            "have happened to us...? Merely\x01",
            "thinking about it is frightening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4196")

    label("loc_40EB")


    ChrTalk(
        0xA,
        (
            "Fortunately, the armed\x01",
            "group didn't enter our\x01",
            "store, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If we had been attacked, what would\x01",
            "have happened to us...? Merely\x01",
            "thinking about it is frightening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4196")

    Jump("loc_49C4")

    label("loc_419B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4248")

    ChrTalk(
        0xA,
        (
            "There are already rumors...\x01",
            "Thinking that the Empire's\x01",
            "behind this is somewhat natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, the worrisome\x01",
            "point is what the Empire\x01",
            "will do next.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C4")

    label("loc_4248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4321")

    ChrTalk(
        0xA,
        (
            "The question of state independence...\x01",
            "The date of the referendum is\x01",
            "certainly fast approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, but which choice will bring\x01",
            "best results...? I want to think\x01",
            "carefully on it awhile longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C4")

    label("loc_4321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_43B7")

    ChrTalk(
        0xA,
        (
            "I wonder which is happier\x01",
            "between a life of tedium\x01",
            "and one full of stimulus...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha. What do you think,\x01",
            "ladies and gentlemen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C4")

    label("loc_43B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4436")

    ChrTalk(
        0xA,
        (
            "Becoming sulky when\x01",
            "excessively losing is\x01",
            "second-rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'd like it if our\x01",
            "customers bet in good\x01",
            "faith.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C4")

    label("loc_4436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_45D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_452F")

    ChrTalk(
        0xA,
        (
            "(They've been raising their voices\x01",
            "for quite some time and disturbing\x01",
            "the other customers...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(The customers over\x01",
            "there lack manners.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(If they're going to step\x01",
            "out of line, I'll need to\x01",
            "sternly warn them.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45CD")

    label("loc_452F")


    ChrTalk(
        0xA,
        (
            "(Even if this is a casino,\x01",
            "there are certain rules\x01",
            "and manners that apply.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(If they're going to step\x01",
            "out of line, I'll need to\x01",
            "sternly warn them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CD")

    Jump("loc_49C4")

    label("loc_45D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4679")

    ChrTalk(
        0xA,
        (
            "Mayor Dieter's gambling\x01",
            "sense...? Hmm, how is it\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "With his intelligence, I get\x01",
            "the impression that he'd be\x01",
            "good at our games as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C4")

    label("loc_4679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_480E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475D")

    ChrTalk(
        0xA,
        (
            "Mr. Gantz has come to\x01",
            "visit us today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I was really surprised\x01",
            "by his strong luck some\x01",
            "time ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now, he's completely regressed\x01",
            "into being the boring weekend\x01",
            "gambler he always was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4809")

    label("loc_475D")


    ChrTalk(
        0xA,
        (
            "I was really surprised by\x01",
            "the strong luck Mr. Gantz\x01",
            "had some time ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now, he's completely regressed\x01",
            "into being the boring weekend\x01",
            "gambler he always was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4809")

    Jump("loc_49C4")

    label("loc_480E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_48C3")

    ChrTalk(
        0xA,
        (
            "I heard the high-class\x01",
            "club Neue-Blanc opened\x01",
            "recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It is a place unreachable for\x01",
            "someone like myself. However, I'd\x01",
            "like to go there, even if just once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C4")

    label("loc_48C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_496F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48DE")
    Call(0, 11)
    Jump("loc_496A")

    label("loc_48DE")


    ChrTalk(
        0xA,
        (
            "Dear me, Miss Rey\x01",
            "Talossa is simply\x01",
            "fearless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Gambling is a result, more\x01",
            "than a process... Victory\x01",
            "belongs to he who laughs last.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_496A")

    Jump("loc_49C4")

    label("loc_496F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_49C4")

    ChrTalk(
        0xA,
        (
            "Welcome. This is the\x01",
            "cards table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you like, how about a\x01",
            "match?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49C4")

    Jump("loc_3AB4")

    label("loc_49C9")

    TalkEnd(0xA)
    Return()

    # Function_10_3AA7 end

    def Function_11_49CD(): pass

    label("Function_11_49CD")

    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "...I am sorry, but this\x01",
            "match is mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, you're good.\x01",
            "However, you won't be so\x01",
            "lucky next time㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hehe, please go easy on\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_11_49CD end

    def Function_12_4A7E(): pass

    label("Function_12_4A7E")

    Call(0, 13)
    Return()

    # Function_12_4A7E end

    def Function_13_4A82(): pass

    label("Function_13_4A82")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",               # 0
            "Play Roulette\x01",      # 1
            "Cancel\x01",             # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AEA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4AEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B3F")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_4B3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B53")
    Jump("loc_5948")

    label("loc_4B53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5948")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C88")

    ChrTalk(
        0xB,
        (
            "Coming to gamble at a\x01",
            "time like this... It's\x01",
            "not a bad thing at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all, by its very nature,\x01",
            "gambling is a pleasure that diverts\x01",
            "anxious feelings and soothes the mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd like you to especially\x01",
            "enjoy it in uncertain\x01",
            "times like these.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D38")

    label("loc_4C88")


    ChrTalk(
        0xB,
        (
            "After all, by its very nature, it\x01",
            "is a pleasure to divert anxious\x01",
            "feelings and to soothe the mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd like you to especially\x01",
            "enjoy it in uncertain\x01",
            "times like these.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D38")

    Jump("loc_5948")

    label("loc_4D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4D4B")
    Jump("loc_5948")

    label("loc_4D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4EF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E60")

    ChrTalk(
        0xB,
        (
            "The problem of Crossbell\x01",
            "independence has ended up reaching a\x01",
            "point where it can't be taken back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't think President Dieter\x01",
            "would go this far without some\x01",
            "chance of success, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder what kind of\x01",
            "card he has ready to\x01",
            "play?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4EF3")

    label("loc_4E60")


    ChrTalk(
        0xB,
        (
            "I don't think President Dieter\x01",
            "would go this far without some\x01",
            "chance of success, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder what kind of\x01",
            "card he has ready to\x01",
            "play?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF3")

    Jump("loc_5948")

    label("loc_4EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_50B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_500C")

    ChrTalk(
        0xB,
        (
            "The day of the referendum\x01",
            "is finally close. It will\x01",
            "be held in just three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I already have an idea of\x01",
            "the result, but I plan to\x01",
            "vote that day just the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As for the direction of\x01",
            "my vote... Please, allow\x01",
            "me to keep it a secret.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_50B0")

    label("loc_500C")


    ChrTalk(
        0xB,
        (
            "I already have an idea of\x01",
            "the result, but I plan to\x01",
            "vote that day just the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As for the direction of\x01",
            "my vote... Please, allow\x01",
            "me to keep it a secret.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50B0")

    Jump("loc_5948")

    label("loc_50B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5131")

    ChrTalk(
        0xB,
        (
            "Owner Drake... He looks\x01",
            "like a little sleepy\x01",
            "today, for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Did he drink until late\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5948")

    label("loc_5131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_51C6")

    ChrTalk(
        0xB,
        (
            "On rainy days like today,\x01",
            "please come have an enjoyable\x01",
            "time at our establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhuhu, I might give you\x01",
            "a freebie. Maybe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5948")

    label("loc_51C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_529B")

    ChrTalk(
        0xB,
        (
            "Be it gambling or anything\x01",
            "else... The important thing\x01",
            "is knowing when to quit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            ""Befitting your station" is another\x01",
            "way to say it. Desiring a lot will\x01",
            "generally end in a failure, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5948")

    label("loc_529B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_533C")

    ChrTalk(
        0xB,
        (
            "I think that humans are\x01",
            "beings who seek thrills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Sir, would you like a match?\x01",
            "I'll give you first-rate thrills\x01",
            "free of charge, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5948")

    label("loc_533C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_53D0")

    ChrTalk(
        0xB,
        (
            "Should Crossbell be\x01",
            "independent or not...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Honestly, Mayor Dieter has\x01",
            "thrust an unthinkably difficult\x01",
            "problem at all of us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5948")

    label("loc_53D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5462")

    ChrTalk(
        0xB,
        (
            "Uhuhu. The day of the\x01",
            "conference has finally\x01",
            "arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't help but look\x01",
            "forward to the next issue\x01",
            "of Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5948")

    label("loc_5462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_552B")

    ChrTalk(
        0xB,
        (
            "I haven't seen it yet, but\x01",
            "I heard Orchis Tower is a\x01",
            "really imposing building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A super high-rise building 40\x01",
            "floors above ground... I can't wait\x01",
            "to sear its image into my eyes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5948")

    label("loc_552B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_570B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_567D")

    ChrTalk(
        0xB,
        (
            "The international conference\x01",
            "called by Mayor Dieter is\x01",
            "finally going to start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Sounding out each other's true intentions,\x01",
            "and using with the right timing the\x01",
            "various trump cards they each possess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Saying it like this, I get the\x01",
            "impression that diplomacy and\x01",
            "gambling are, in essence, the same.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5706")

    label("loc_567D")


    ChrTalk(
        0xB,
        (
            "I wonder what kind of trump cards\x01",
            "Mayor Dieter has prepared for\x01",
            "this opportunity he set up...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhuhu, I am so very\x01",
            "interested.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5706")

    Jump("loc_5948")

    label("loc_570B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_576F")

    ChrTalk(
        0xB,
        (
            "Haha. Sir, would you\x01",
            "like a match?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I invite you to a\x01",
            "labyrinth of thoughts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5948")

    label("loc_576F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_589B")

    ChrTalk(
        0xB,
        (
            "Welcome to Casino House\x01",
            "Barca. This is the\x01",
            "roulette table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You might deny it at first, but\x01",
            "any kind of cheating is absolutely\x01",
            "impossible at this table...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What do you say? Don't you want to\x01",
            "surrender yourself to fate just this\x01",
            "once, without any petty tricks?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5948")

    label("loc_589B")


    ChrTalk(
        0xB,
        (
            "Betting widely, lightly and steadily\x01",
            "is good too... Matches with narrow\x01",
            "and heavy betting is good too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Only the Goddess knows\x01",
            "what the result will be,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5948")

    Jump("loc_4A8F")

    label("loc_594D")

    TalkEnd(0xB)
    Return()

    # Function_13_4A82 end

    def Function_14_5951(): pass

    label("Function_14_5951")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5962")
    Jump("loc_68E3")

    label("loc_5962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5B11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6A")

    ChrTalk(
        0xFE,
        (
            "I wasn't here, but I\x01",
            "heard a terrible incident\x01",
            "happened one week ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not so sure something\x01",
            "similar won't happen in\x01",
            "the future, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it might be about\x01",
            "time to refrain from any\x01",
            "further visits to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5B0C")

    label("loc_5A6A")


    ChrTalk(
        0xFE,
        (
            "I'm not so sure something\x01",
            "similar won't happen in\x01",
            "the future, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it might be about\x01",
            "time to refrain from any\x01",
            "further visits to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B0C")

    Jump("loc_68E3")

    label("loc_5B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5BB4")

    ChrTalk(
        0xFE,
        (
            "What on earth could the\x01",
            "armed group's objective\x01",
            "be, I wonder...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I of course understand that\x01",
            "they might make demands in\x01",
            "the future, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68E3")

    label("loc_5BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C58")

    ChrTalk(
        0xFE,
        (
            "By the way, they say a\x01",
            "citizen's forum is being held\x01",
            "at City Meeting Hall today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might go have a look\x01",
            "at it bit later, as a\x01",
            "social study.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68E3")

    label("loc_5C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5CD2")

    ChrTalk(
        0xFE,
        (
            "*sigh*, even though I\x01",
            "came to visit Crossbell,\x01",
            "I'm getting bored again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't there anything\x01",
            "fun?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68E3")

    label("loc_5CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5E8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF5")

    ChrTalk(
        0xFE,
        (
            "Those rich kids yesterday were\x01",
            "doing good at the very beginning,\x01",
            "but in the end they lost greatly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe due to frustration, they\x01",
            "spouted dirty parting threats\x01",
            "and left immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. Not even the\x01",
            "Goddess has patience\x01",
            "enough for those three.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5E86")

    label("loc_5DF5")


    ChrTalk(
        0xFE,
        (
            "It looks like those rich\x01",
            "kids from yesterday didn't\x01",
            "come to the casino today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. It seems I'll be\x01",
            "able to focus on the\x01",
            "game today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E86")

    Jump("loc_68E3")

    label("loc_5E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5FE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F50")

    ChrTalk(
        0xFE,
        (
            "I have no interest in the likes\x01",
            "of shallow men who cling to their\x01",
            "parents' mira and authority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. As expected, it\x01",
            "must be a refined dandy\x01",
            "like Owner Drake.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5FDC")

    label("loc_5F50")


    ChrTalk(
        0xFE,
        (
            "No matter how much mira\x01",
            "he has, someone like a\x01",
            "rich kid is a no.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. As expected, it\x01",
            "must be a refined dandy\x01",
            "like Owner Drake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FDC")

    Jump("loc_68E3")

    label("loc_5FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_607E")

    ChrTalk(
        0xFE,
        (
            "The trade conference...\x01",
            "Haha. That Mayor Dieter\x01",
            "is a shrewd one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With his skill in\x01",
            "politics... Could he be a\x01",
            "strong gambler as well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68E3")

    label("loc_607E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6116")

    ChrTalk(
        0xFE,
        (
            "It seems Mr. Galletti still\x01",
            "holds a grudge for having\x01",
            "lost to Gantz previously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Gamblers really\x01",
            "hate to lose, don't\x01",
            "they.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68E3")

    label("loc_6116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_67C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64B4")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_61CF")
    Jump("loc_6219")

    label("loc_61CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_61EF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6219")

    label("loc_61EF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_620F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6219")

    label("loc_620F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6219")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "My, if it isn't Randy.\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOhh, same to you, Miss\x01",
            "Rey Talossa.\x02\x03",
            "#00302FSay, how about goin' on\x01",
            "a date with me to\x01",
            "celebrate our reunion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, let's see. If you were\x01",
            "to beat me in a match, I'd\x01",
            "think about it, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOhh, you said it, eh?\x01",
            "Then, let's get started\x01",
            "at onc―\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_641B")

    ChrTalk(
        0x101,
        "#00009FHey, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, of course you're\x01",
            "joking, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FY-Yeah... Hey, your\x01",
            "smiles are scary, you\x01",
            "know that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64A8")

    label("loc_641B")


    ChrTalk(
        0x102,
        (
            "#00109FHey, Randy. I think we\x01",
            "just told you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FY-Yeah... That's just a\x01",
            "joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Randy... You really\x01",
            "never learn.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64A8")

    SetScenarioFlags(0x14C, 4)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_67BF")

    label("loc_64B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_664F")
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_654F")
    Jump("loc_6599")

    label("loc_654F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_656F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6599")

    label("loc_656F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_658F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6599")

    label("loc_658F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6599")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Haha. It appears our\x01",
            "match is postponed then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I don't know if\x01",
            "we'll have another\x01",
            "chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FAww, no way.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_67BF")

    label("loc_664F")

    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66E0")
    Jump("loc_672A")

    label("loc_66E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6700")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_672A")

    label("loc_6700")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6720")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_672A")

    label("loc_6720")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_672A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Haha. It appears our\x01",
            "match is postponed then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I don't know if\x01",
            "we'll have another\x01",
            "chance.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    label("loc_67BF")

    Jump("loc_68E3")

    label("loc_67C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6822")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67DF")
    Call(0, 11)
    Jump("loc_681D")

    label("loc_67DF")


    ChrTalk(
        0xFE,
        "Aah, I lost again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. However, I'm not\x01",
            "finished.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_681D")

    Jump("loc_68E3")

    label("loc_6822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_68E3")

    ChrTalk(
        0xFE,
        (
            "I refrained from coming to\x01",
            "Crossbell for a while, but... In\x01",
            "the end, ended up coming again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My homeland, Calvard, isn't\x01",
            "bad but Crossbell's atmosphere\x01",
            "is simply exceptional.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68E3")

    TalkEnd(0xFE)
    Return()

    # Function_14_5951 end

    def Function_15_68E7(): pass

    label("Function_15_68E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6989")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6905")
    Call(0, 16)
    Jump("loc_6984")

    label("loc_6905")


    ChrTalk(
        0xFE,
        (
            "Ugh. When that situation ended\x01",
            "and I came to play the slots,\x01",
            "my old lady marched in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I really made her\x01",
            "worry, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6984")

    Jump("loc_783E")

    label("loc_6989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6B01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A79")

    ChrTalk(
        0xFE,
        (
            "Thinking the martial law\x01",
            "was no big deal, I came\x01",
            "to enjoy myself, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "W-Who could've thought it'd\x01",
            "turn into this... It's the\x01",
            "biggest mistake of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My old lady is probably\x01",
            "worried by now...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6AFC")

    label("loc_6A79")


    ChrTalk(
        0xFE,
        (
            "Who could've thought it'd\x01",
            "turn into this? It's the\x01",
            "biggest mistake of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My old lady is probably\x01",
            "worried by now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AFC")

    Jump("loc_783E")

    label("loc_6B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6B83")

    ChrTalk(
        0xFE,
        (
            "I heard the speech\x01",
            "earlier... It was\x01",
            "something incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Frankly, I don't get\x01",
            "what good there is in\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_783E")

    label("loc_6B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6C2F")

    ChrTalk(
        0xFE,
        (
            "In the attack a week ago\x01",
            "we were made to taste\x01",
            "some real dread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I think that it's\x01",
            "especially in times like these\x01",
            "that we have to cheer up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_783E")

    label("loc_6C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6DEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D35")

    ChrTalk(
        0xFE,
        (
            "It appears something\x01",
            "terrible is happening in\x01",
            "Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I couldn't calm down at\x01",
            "home, I went out, but... Today,\x01",
            "I really have no enthusiasm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not good for my old\x01",
            "lady either, so I think\x01",
            "I'll go home right away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6DE6")

    label("loc_6D35")


    ChrTalk(
        0xFE,
        (
            "Because I couldn't calm down at\x01",
            "home, I went out, but... Today,\x01",
            "I really have no enthusiasm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not good for my old\x01",
            "lady either, so I think\x01",
            "I'll go home right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DE6")

    Jump("loc_783E")

    label("loc_6DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6E73")

    ChrTalk(
        0xFE,
        (
            "Yesterday, I racked up loss\x01",
            "after loss... Today, I swear\x01",
            "I'll get everything back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Watch me now, I'll do\x01",
            "iiit!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_783E")

    label("loc_6E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6F7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F30")

    ChrTalk(
        0xFE,
        (
            "Ooh!? This now is a\x01",
            "hit... ...Wait, it\x01",
            "fooled me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gnnnnh... Why it doesn't\x01",
            "come, WHY!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F(Man oh man. That old\x01",
            "man is still passionate,\x01",
            "huh.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6F76")

    label("loc_6F30")


    ChrTalk(
        0xFE,
        (
            "Gnnnnh... Why it doesn't\x01",
            "come, WHY!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm a veteran gambler!\x02",
    )

    CloseMessageWindow()

    label("loc_6F76")

    Jump("loc_783E")

    label("loc_6F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_70AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7033")

    ChrTalk(
        0xFE,
        (
            "Mrrr, today the wins\x01",
            "just aren't coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What am I going to say\x01",
            "to my old lady, going\x01",
            "home like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, come out! Come,\x01",
            "come out I say!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_70AA")

    label("loc_7033")


    ChrTalk(
        0xFE,
        (
            "Mrrr... What am I going\x01",
            "to say to my old lady,\x01",
            "going home like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, come out! Come,\x01",
            "come out I say!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70AA")

    Jump("loc_783E")

    label("loc_70AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7206")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_717E")

    ChrTalk(
        0xFE,
        (
            "I completely approve of\x01",
            "Crossbell independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Paying a portion of tax\x01",
            "revenue to the major powers is\x01",
            "nonsense in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Independence is a\x01",
            "natural right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7201")

    label("loc_717E")


    ChrTalk(
        0xFE,
        (
            "Paying a portion of our tax\x01",
            "revenue to the major powers is\x01",
            "nonsense in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Independence is a\x01",
            "natural right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7201")

    Jump("loc_783E")

    label("loc_7206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_750F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7418")

    ChrTalk(
        0xFE,
        (
            "This morning, my old\x01",
            "lady was smiling boldly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I asked the reason,\x01",
            "she said I'd find out\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems she removed the\x01",
            "contents of my wallet\x01",
            "without my knowledge.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00305FHuh? Then, grandpa\x01",
            "Rikke, what're you doin'\x01",
            "here with no mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Just sitting here. Is\x01",
            "that so wrong?\x02",
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
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306FWell... It's not even\x01",
            "that crowded, so I think\x01",
            "you're good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_750A")

    label("loc_7418")


    ChrTalk(
        0xFE,
        (
            "Since I don't have mira, I\x01",
            "can't play... But I\x01",
            "absolutely won't return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Giving in here is just\x01",
            "what my old lady wants\x01",
            "me to do.\x02",
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
    Sleep(1000)

    label("loc_750A")

    Jump("loc_783E")

    label("loc_750F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_75B3")

    ChrTalk(
        0xFE,
        (
            "Everyone's excited about the\x01",
            "unveiling ceremony, but anyway, I\x01",
            "just want to hit the slots here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My old lady is having\x01",
            "tea with her friends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_783E")

    label("loc_75B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76CA")

    ChrTalk(
        0x104,
        (
            "#00300FHi, grandpa Rikke.\x01",
            "How've you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho, that voice... Is\x01",
            "that you, Randy? Long\x01",
            "time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can see, I'm good\x01",
            "as can be, and I'm on\x01",
            "fire!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you get it, then\x01",
            "don't interrupt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHaha, sorry 'bout that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_7720")

    label("loc_76CA")


    ChrTalk(
        0xFE,
        (
            "I'm in a good place\x01",
            "right now, so don't\x01",
            "interrupt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Ohh, it's come again!\x02",
    )

    CloseMessageWindow()

    label("loc_7720")

    Jump("loc_783E")

    label("loc_7725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_77CB")

    ChrTalk(
        0xFE,
        (
            "My old lady can say whatever she\x01",
            "likes, but I've no intention of\x01",
            "giving up gambling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This too is the fate a\x01",
            "gambler is born with,\x01",
            "hoh hoh ho.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_783E")

    label("loc_77CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_783E")

    ChrTalk(
        0xFE,
        (
            "Hoh hoh, I'm doing well\x01",
            "on the slots today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't get enough of\x01",
            "the sound of tinkling\x01",
            "medals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_783E")

    TalkEnd(0xFE)
    Return()

    # Function_15_68E7 end

    def Function_16_7842(): pass

    label("Function_16_7842")

    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "Really you, I swear...\x01",
            "Why won't you come\x01",
            "home!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Come now, let's go home\x01",
            "this instant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "W-Wait. At least let me\x01",
            "exchange these coins...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hmph, shut up!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No way! Over my dead\x01",
            "body!!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_16_7842 end

    def Function_17_792C(): pass

    label("Function_17_792C")


    ChrTalk(
        0x104,
        (
            "#00300FHey, Grandpa Rikke.\x01",
            "What's up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Huh? Is that Randy I\x01",
            "hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haven't seen you around\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, I've been a little\x01",
            "busy with work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Is because we're busy\x01",
            "that we come here. You\x01",
            "should know that already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHah. You might be right\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That wife of mine! She\x01",
            "ambushed me at the\x01",
            "entrance this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "She raised her eyebrows\x01",
            "and barked at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "She almost brought me\x01",
            "back home. *sigh*, that\x01",
            "was a close call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No matter how much Crossbell\x01",
            "changes, the Entertainment\x01",
            "District will never disappear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Bars, casino, girls who\x01",
            "swarm the guests㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even if the shape changes,\x01",
            "it's still the same. It's\x01",
            "always been that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...There's also places that\x01",
            "aren't exactly above-board.\x01",
            "An amateur has to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_17_792C end

    def Function_18_7C42(): pass

    label("Function_18_7C42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C57")
    Call(0, 16)
    Jump("loc_7CDB")

    label("loc_7C57")


    ChrTalk(
        0xFE,
        (
            "Honestly, this man... I\x01",
            "wonder if he has any idea\x01",
            "how much he made me worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...For now, his spending\x01",
            "money will be zero.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CDB")

    TalkEnd(0xFE)
    Return()

    # Function_18_7C42 end

    def Function_19_7CDF(): pass

    label("Function_19_7CDF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, if red and red came,\x01",
            "I thought the next one\x01",
            "would've been black...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I guess gambling\x01",
            "isn't as easy as it\x01",
            "looks.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_7CDF end

    def Function_20_7D6C(): pass

    label("Function_20_7D6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7E3D")

    ChrTalk(
        0xFE,
        (
            "I came here with Gantz\x01",
            "thinking this place might be\x01",
            "good for relaxing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems best to head back early\x01",
            "and consult with the the mayor and\x01",
            "the others about future activities.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E92")

    label("loc_7E3D")


    ChrTalk(
        0xFE,
        (
            "Haha. That's why you\x01",
            "should have quit back\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gantz, you're too\x01",
            "greedy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E92")

    TalkEnd(0xFE)
    Return()

    # Function_20_7D6C end

    def Function_21_7E96(): pass

    label("Function_21_7E96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7F40")

    ChrTalk(
        0xFE,
        (
            "To think such a terrible\x01",
            "thing happened when I\x01",
            "came to Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*. I really\x01",
            "wanted to come here, but\x01",
            "now I'm not in the mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F91")

    label("loc_7F40")


    ChrTalk(
        0xFE,
        (
            "Aah, crap! I had such a\x01",
            "long win streak, and it's\x01",
            "already gone up in smoke!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F91")

    TalkEnd(0xFE)
    Return()

    # Function_21_7E96 end

    def Function_22_7F95(): pass

    label("Function_22_7F95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_809D")

    ChrTalk(
        0xFE,
        (
            "Everyone's making a fuss over\x01",
            "the question of independence,\x01",
            "but... Jeez, they're all fools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Crossbell fawns upon the\x01",
            "Republic like it has been\x01",
            "and obeys, it'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And if it does so, it\x01",
            "will be promised peace.\x01",
            "Hehehe...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_812F")

    label("loc_809D")


    ChrTalk(
        0xFE,
        (
            "Well if they do decide on\x01",
            "independence, I'll have\x01",
            "nothin' to do with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. Let's at least\x01",
            "have fun in this city\x01",
            "while we still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_812F")

    TalkEnd(0xFE)
    Return()

    # Function_22_7F95 end

    def Function_23_8133(): pass

    label("Function_23_8133")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hehe, don't push\x01",
            "yourself too much, Yuri.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We might get banned if\x01",
            "you win too much,\x01",
            "y'know?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_8133 end

    def Function_24_819F(): pass

    label("Function_24_819F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The woman sitting over\x01",
            "there is quite the\x01",
            "beauty, isn't she.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Refusing our invite... She\x01",
            "wouldn't know a good guy\x01",
            "if she saw one, I say.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_819F end

    def Function_25_8238(): pass

    label("Function_25_8238")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_83AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_825A")
    TalkEnd(0xFE)
    Call(0, 26)
    Return()

    label("loc_825A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8330")

    ChrTalk(
        0x15,
        (
            "#03500FWell then, I guess I'll head back to\x01",
            "the Empire in a little bit.\x02\x03",
            "#03504FI'll have the pleasure of helping out\x01",
            "that old man with the awful beard...\x01",
            "Man, being a reliable guy is tough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_83AF")

    label("loc_8330")


    ChrTalk(
        0x15,
        (
            "#03500FWell then, after a little\x01",
            "bit more I guess I'll go\x01",
            "back to the Empire.\x02\x03",
            "#03504FMan, being a reliable guy\x01",
            "is tough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83AF")

    TalkEnd(0xFE)
    Return()

    # Function_25_8238 end

    def Function_26_83B3(): pass

    label("Function_26_83B3")

    EventBegin(0x0)
    Fade(500)
    OP_68(5540, 5300, 15900, 0)
    MoveCamera(43, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21700, 0)
    SetChrPos(0x15, 6390, 4270, 15790, 270)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x0, 5210, 4000, 16780, 135)
    SetChrPos(0x1, 5670, 4000, 17920, 135)
    SetChrPos(0x2, 4550, 4000, 15300, 90)
    SetChrPos(0x3, 4750, 4000, 13990, 45)
    SetChrPos(0x4, 4330, 4000, 17810, 135)
    SetChrPos(0x5, 5730, 4000, 13110, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x15,
        (
            "#11P#03502FHiya. Thanks for all\x01",
            "your hard work, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FL-Lechter... You're\x01",
            "again at the casino in\x01",
            "that outfit...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_853D")

    ChrTalk(
        0x105,
        (
            "#10402FHaha, he's pretty darn\x01",
            "relaxed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85B4")

    label("loc_853D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8573")

    ChrTalk(
        0x109,
        "#10106FHe's very relaxed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_85B4")

    label("loc_8573")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85B4")

    ChrTalk(
        0x106,
        (
            "#10702FLooks like he's\x01",
            "extremely relaxed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85B4")


    ChrTalk(
        0x103,
        (
            "#6P#00205FWhat happened to your\x01",
            "secretary clothes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03506FWell, while fighting a\x01",
            "Magic Soldier they ended\x01",
            "up ripped and torn.\x02\x03",
            "#03509FWell, don't worry about\x01",
            "that and relax!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FR-Right...\x02\x03",
            "#00000F*cough*, hmm.... Thank you\x01",
            "very much for your cooperation\x01",
            "in the liberation operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FReally, thank you very much\x01",
            "for your support in the\x01",
            "Orchis Tower infiltration...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03504FHaha, don't sweat it. I just did\x01",
            "what I felt like doing.\x02\x03",
            "#03502FAnd because I've been doing nothing\x01",
            "but secretary desk work, it was\x01",
            "honestly some good exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FYou're just an intelligence\x01",
            "operative... But you seem to know\x01",
            "your way around fights.\x02\x03",
            "#00301FKilika aside, to think that you were\x01",
            "concealin' that much fightin'\x01",
            "ability...\x02\x03",
            "Your fencing and high level arts...\x01",
            "They're not the kind of things an\x01",
            "amateur could master on short notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03510FHmm. If you want to know about it that\x01",
            "much, I guess I'll tell you.\x02\x03",
            "#03504FSee, it was 30 years ago... They were\x01",
            "taught to me by a hermit who lives in the\x01",
            "depths of a certain mountain of the Empire.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006F...This story sounds\x01",
            "bogus right front the\x01",
            "start.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B29")

    ChrTalk(
        0x10A,
        (
            "#00603F(My... What a tough\x01",
            "customer to deal with.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BB3")

    label("loc_8B29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B75")

    ChrTalk(
        0x109,
        (
            "#10106FAs you can imagine, it's\x01",
            "too inadequate...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BB3")

    label("loc_8B75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BB3")

    ChrTalk(
        0x105,
        (
            "#10409FAhaha, that's extremely\x01",
            "unlikely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BB3")


    ChrTalk(
        0x15,
        (
            "#11P#03504FWell, I think I'll leave\x01",
            "the rest to your\x01",
            "imaginations.\x02\x03",
            "#03510F...Well then, it's about\x01",
            "time for me to head back\x01",
            "to the Empire.\x02\x03",
            "#03506FI've got to help out\x01",
            "that old man with the\x01",
            "awful beard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00205FThe Blood and Iron Chancellor... If I\x01",
            "remember correctly he was shot and\x01",
            "went missing.\x02\x03",
            "#00203FThe Noble Alliance took advantage of\x01",
            "the opening caused by the thrashing\x01",
            "the regular army got from that Aion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03510FYeah. The capital seems to be\x01",
            "completely occupied by those nobles.\x02\x03",
            "#03506FDear me. Anyhow, that old man easily\x01",
            "gains unjustified resentment. Even we\x01",
            "who protect him have gotten used to it.\x02\x03",
            "#03500FWell, being who he is, that old man\x01",
            "won't drop dead so easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FYou're cavalier about\x01",
            "all this for some\x01",
            "reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03509FHaha. And what about\x01",
            "you?\x02\x03",
            "#03504FOld man Giliath or the\x01",
            "Noble Alliance. No\x01",
            "matter who wins...\x02\x03",
            "#03502FI think that the Destiny\x01",
            "of Crossbell isn't going\x01",
            "to change any time soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x102,
        "#00108F...Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...We don't know what the\x01",
            "future will bring, yet.\x02\x03",
            "#00001FHowever, if nothing else... I\x01",
            "first intend to head to that\x01",
            "Huge Tree to get KeA back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03504F...Haha, that's good.\x02\x03",
            "It's important to focus on\x01",
            "the future, but if that's\x01",
            "all you see, you'll trip.\x02\x03",
            "#03500FWhat's most important is\x01",
            "the "now" that's in front\x01",
            "of you.\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FI-It's strange for you\x01",
            "to say something proper\x01",
            "all of a sudden, but...\x02\x03",
            "#00000F...Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03502FHaha. Well, give it your\x01",
            "best shot, at least.\x02\x03",
            "#03509FIf you don't, I'll have\x01",
            "stayed behind for\x01",
            "nothing, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x15, 6700, 4270, 15750, 90)
    SetChrPos(0x0, 5480, 4000, 13730, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1CC, 1)
    EventEnd(0x5)
    Return()

    # Function_26_83B3 end

    def Function_27_9362(): pass

    label("Function_27_9362")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Play the Slots\x01",      # 0
            "Cancel\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93F5")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_93F5")

    TalkEnd(0xFF)
    Return()

    # Function_27_9362 end

    def Function_28_93F9(): pass

    label("Function_28_93F9")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-900, 5000, 20000, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -900, 4000, 18700, 0)
    SetChrPos(0x102, 200, 4000, 17800, 0)
    SetChrPos(0x103, -2000, 4000, 17800, 0)
    SetChrPos(0x109, -1100, 4000, 17400, 0)
    SetChrPos(0x105, -100, 4000, 16900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5POh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...Could you have come\x01",
            "for Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYes... Like we thought,\x01",
            "has he been here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, at about 3AM he\x01",
            "casually came into our\x01",
            "establishment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe left after drinking\x01",
            "here for a while.\x01",
            "However...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206F...It seems he visited\x01",
            "this place first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#12PAnd, did he say where he\x01",
            "was going after that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...As I suspected, it\x01",
            "appears he didn't return\x01",
            "to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, he didn't say where\x01",
            "he was going in\x01",
            "particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, his conversation\x01",
            "while drinking was more\x01",
            "brazen than usual...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn addition, when he left,\x01",
            "he retrieved a certain\x01",
            "something from me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FA certain... something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes... A rather heavy\x01",
            "trunk. I don't know its\x01",
            "contents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PRandy asked me to hold onto it\x01",
            "for him two years ago, when he\x01",
            "had just arrived in this city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe said: "If I were to die,\x01",
            "tear it in pieces and dispose\x01",
            "of it at the scrapyard."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FThat doesn't seem like\x01",
            "him at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00008F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...I know that guy's\x01",
            "personal history myself\x01",
            "to a certain extent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, I don't know\x01",
            "what he did in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou all are most likely\x01",
            "the only ones who can\x01",
            "help him right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FOwner...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004F...Yes. We feel the\x01",
            "same.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -900, 4000, 17500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 0)
    OP_29(0xAA, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_28_93F9 end

    def Function_29_9A29(): pass

    label("Function_29_9A29")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("chr/ch07400.itc", 0x1F)
    LoadChrToIndex("apl/ch51101.itc", 0x20)
    LoadChrToIndex("apl/ch51102.itc", 0x21)
    SoundLoad(3391)
    SoundLoad(3392)
    SoundLoad(3393)
    SoundLoad(3936)
    SoundLoad(3937)
    SoundLoad(3938)
    SoundLoad(3939)
    SoundLoad(3940)
    SoundLoad(3970)
    SoundLoad(3971)
    SoundLoad(3972)
    SoundLoad(2176)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04600.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    SetChrFlags(0xD, 0x80)
    SetMapObjFrame(0xFF, "c0470:Layer10", 0x0, 0x1)
    SetMapObjFrame(0xFF, "puropera_00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "puropera_01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "puropera_02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "puropera_03", 0x0, 0x1)
    OP_68(5500, 5500, 4750, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 5200, 4000, 5850, 0)
    SetChrPos(0x102, 6000, 4000, 5300, 0)
    SetChrPos(0x109, 4800, 4000, 4500, 0)
    SetChrPos(0x105, 6200, 4000, 4250, 0)
    OP_0D()
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(6540, 5500, 13420, 3000)
    SetCameraDistance(21860, 3000)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x15,
        (
            "#03506FAww, man~, another Dogi.\x02\x03",
            "#03501FIt's boring if you don't\x01",
            "get a Feena once in a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(5480, 5500, 12360, 3000)
    MoveCamera(45, 27, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(21860, 3000)
    BeginChrThread(0x101, 3, 0, 30)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 32)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 31)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 33)
    OP_6F(0x79)
    WaitChrThread(0x109, 1)
    OP_0D()
    Sleep(100)
    Fade(500)
    OP_68(5600, 5500, 12250, 0)
    MoveCamera(48, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19630, 0)
    SetChrPos(0x15, 6540, 4270, 13420, 180)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00013F#12P─Lechter. There's no\x01",
            "escape this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PGive up and confirm your\x01",
            "identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03503F#5PMy identity, eh...\x02\x03",
            "#03510FIdentity, identity...\x01",
            "Which one would be good,\x01",
            "I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P...Please don't\x01",
            "flagrantly deceive us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03504FLet's see...\x02\x03",
            "#03500FAsk me whatever you want\x01",
            "and I'll reply with yes\x01",
            "or no.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PUnderstood. Then I'll begin.\x02\x03",
            "#00001F─You are Mr. Lechter\x01",
            "Arundel, Imperial government\x01",
            "secretary, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#03504FYes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#12PAre you also a special\x01",
            "captain of the Imperial\x01",
            "Intelligence Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#03504FYes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P(He admitted it so\x01",
            "readily...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6P...I'll continue.\x02\x03",
            "#00101FAre you visiting\x01",
            "Crossbell on Imperial\x01",
            "government business?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)
    Sleep(300)

    ChrTalk(
        0x15,
        "#03501FWell no... but also yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PAre you staying longer\x01",
            "than one month?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03504FHaha...\x02\x03",
            "#03502FThe answer's no. I'll be\x01",
            "heading back in about a\x01",
            "week.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A0DC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0DC)
    Sleep(100)

    def lambda_A0EC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A0EC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00013F(Is this all...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(Yeah... We won't get\x01",
            "any more out of him.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A15A():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A15A)
    Sleep(50)

    def lambda_A16A():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A16A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00003F#12P...Sorry to have\x01",
            "troubled you, Captain\x01",
            "Arundel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PThanks for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Sleep(200)

    ChrTalk(
        0x15,
        (
            "#03506FAh, no problem.\x02\x03",
            "#03505FHow's that little kid\x01",
            "doing? You guys took her\x01",
            "in, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#12PUh, you mean KeA?\x02\x03",
            "#00012FShe's totally fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6P...Thanks for your help\x01",
            "back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PHaha. You did help us\x01",
            "escape, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03504FHuh? What are you talking\x01",
            "about? I was just playing with\x01",
            "Blackie.\x02\x03",
            "#03502FBy the way, old man Hartmann\x01",
            "ended up getting arrested,\x01",
            "right?\x02\x03",
            "Well, it was strange that he\x01",
            "was a hostage, but I'm glad he\x01",
            "was captured without issue.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00001F#12P...How do you even know\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PNot even 3 days have\x01",
            "passed since that\x01",
            "incident, and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03503FWell, confirming that\x01",
            "was one objective of my\x01",
            "visit, you see.\x02\x03",
            "#03501FAnd another is─\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 5790, 250, -2980, 0)
    StopBGM(0xBB8)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x16,
        "Young Girl's Voice",
        "#3936V#1P#30WAh, there you are!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "Young Girl's Voice",
        (
            "#3937V#1P#30WWhat are you doing in a\x01",
            "place like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF61)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    Fade(500)
    SetMapObjFrame(0xFF, "heri_04a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "poul_02a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "nuki_04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "white00", 0x0, 0x2)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    OP_68(3310, 5500, 3920, 0)
    MoveCamera(113, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21270, 0)

    def lambda_A720():
        OP_93(0x101, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A720)

    def lambda_A72D():
        OP_93(0x102, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A72D)

    def lambda_A73A():
        OP_93(0x109, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A73A)

    def lambda_A747():
        OP_93(0x105, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A747)
    SetChrPos(0x15, 6540, 4270, 13420, 180)
    OP_68(5340, 5500, 12170, 6000)
    MoveCamera(130, 18, 0, 6000)
    OP_6E(400, 6000)
    SetCameraDistance(22330, 6000)

    def lambda_A793():
        OP_9B(0x0, 0x16, 0x0, 0x36B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A793)
    Sleep(2000)

    def lambda_A7AB():

        label("loc_A7AB")

        TurnDirection(0x101, 0x16, 500)
        Yield()
        Jump("loc_A7AB")

    QueueWorkItem2(0x101, 1, lambda_A7AB)
    Sleep(50)

    def lambda_A7C0():

        label("loc_A7C0")

        TurnDirection(0x105, 0x16, 500)
        Yield()
        Jump("loc_A7C0")

    QueueWorkItem2(0x105, 1, lambda_A7C0)
    OP_6F(0x1)
    WaitChrThread(0x16, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x105, 0x1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x16,
        (
            "#04601F#3970V#11P#30WYou got those Arc-en-\x01",
            "Ciel tickets for us,\x01",
            "right?\x02\x03",
            "#3971VAnd? What about that!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF83)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x15,
        (
            "#03509F#6PYeah, I reserved VIP\x01",
            "seats for tonight's\x01",
            "performance.\x02\x03",
            "You can thank me later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#04602F#11PSeriously!?\x02\x03",
            "#04612FEhehe, thanks! I've\x01",
            "wanted to see them since\x01",
            "forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P(Who is that?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6P(Looks like she's still\x01",
            "young...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x101, 500)

    ChrTalk(
        0x16,
        (
            "#04605F#11POh...?\x02\x03",
            "............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#5PUmm... What is it?\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x16,
        (
            "Hmm... You smell like something,\x01",
            "mister.\x02\x03",
            "I remember that smell from\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        "#00005F#5PHuh...\x02",
    )

    CloseMessageWindow()
    OP_96(0x16, 0x17AC, 0xFA0, 0x2E2C, 0x7D0, 0x0)
    TurnDirection(0x105, 0x16, 500)
    Sleep(100)
    OP_93(0x16, 0x5A, 0x1F4)
    OP_9B(0x1, 0x16, 0x0, 0x64, 0x3E8, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(50)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x16,
        "#04609F#3972V#11P*chomp*\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(150)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The girl lightly bit Lloyd's earlobe.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_9C(0x101, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sound(3318, 255, 100, 0)
    Sleep(100)
    TurnDirection(0x101, 0x16, 0)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0x101, 0x40)
    OP_96(0x101, 0x1B4E, 0xFA0, 0x2E2C, 0xFA0, 0x0)
    ClearChrFlags(0x101, 0x40)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00011F#5P!!!!?????\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00111F#6PH-Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#6PWh-Whaaaaaa!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#12PWhoo♪\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_9B(0x1, 0x16, 0xB4, 0x1F4, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        (
            "#00007F#5PW-What do you think\x01",
            "you're doing!?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Redheaded Girl")

    ChrTalk(
        0x16,
        (
            "#04612F#11PEhehe, thanks for the\x01",
            "food㈱\x02\x03",
            "#04602FYeah, you do smell a\x01",
            "bit.\x02\x03",
            "Not so much with those\x01",
            "other two, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x16, 0x0, 0x1F4)

    ChrTalk(
        0x16,
        (
            "#04605F#11P─Ah! You do a little\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PHuh...\x02",
    )

    CloseMessageWindow()
    Sound(809, 0, 100, 0)
    BeginChrThread(0x16, 3, 0, 34)
    WaitChrThread(0x16, 3)
    Sleep(50)
    Fade(500)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 5520, 4000, 13000, 180)
    Sound(802, 0, 100, 0)
    BeginChrThread(0x17, 3, 0, 35)
    OP_68(4930, 5600, 11710, 0)
    MoveCamera(39, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x15, 6400, 4270, 13350, 225)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    TurnDirection(0x105, 0x102, 500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x17, 0x3)
    BeginChrThread(0x17, 3, 0, 36)
    SetChrPos(0x16, 5500, 4000, 13060, 180)
    SetChrPos(0x102, 5590, 4000, 12570, 180)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x102,
        "#00115F#3391V#4S#5PEEEEEEK!\x02",
    )

    CloseMessageWindow()
    OP_24(0xD3F)
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00011F#11PE-Elie!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#5PW-When did she move\x01",
            "behind her?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x16,
        (
            "#04611F#3938V#5P#30WThese are pretty big,\x01",
            "eh?\x02\x03",
            "#04609F#3939VShirley's flat. And\x01",
            "jealous, too㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF63)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00112F#3392V#5P#40WH-Hey, stop it, please!\x02\x03",
            "#00113F#3393VUgh.. Why are you...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD41)
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10114F#5PW-W-Wha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309F#6PAhaha, great scene.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PI-Indeed... I mean, no!\x02\x03",
            "#00007FHey, you! What're doing\x01",
            "all of a sudden!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03509FHaha, she just does\x01",
            "whatever she wants.\x02\x03",
            "#03502FBut more than that would\x01",
            "be sexual harassment,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#04605F#5PIt's not sexual\x01",
            "harassment. I'm just\x01",
            "getting to know her.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        (
            "#00107F#5P#4SI-It's totally sexual\x01",
            "harassment!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    EndChrThread(0x17, 0x3)
    SetChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x102, 0x2)
    SetChrPos(0x16, 5300, 4000, 13370, 180)
    SetChrPos(0x102, 5520, 4000, 13000, 180)
    SetCameraDistance(19230, 1000)

    def lambda_B230():
        OP_9B(0x1, 0x16, 0x87, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_B230)
    Sound(802, 0, 100, 0)
    OP_A1(0x102, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)

    def lambda_B257():
        OP_99(0x101, 0x102, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B257)
    Sleep(50)

    def lambda_B26E():
        OP_99(0x109, 0x102, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B26E)
    Sleep(500)

    ChrTalk(
        0x102,
        "#5P#00113F*pant pant pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#5PE-Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#11PA-Are you okay?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 6730, 4000, 12500, 180)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "#03510F#5PYes, well excuse us,\x01",
            "then.\x02\x03",
            "#03509FWe'll kill time at\x01",
            "Michelam Theme Park 'til\x01",
            "evening.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x16,
        "Shirley",
        "#04612F#3940V#5P#30WSee ya!\x02",
    )

    CloseMessageWindow()
    OP_24(0xF64)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_68(4780, 5500, 11560, 3000)
    OP_93(0x15, 0xE1, 0x0)

    def lambda_B3C6():
        OP_96(0x15, 0x1662, 0xFA0, 0x29FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B3C6)
    OP_95(0x16, 4740, 4000, 12780, 2000, 0x0)

    def lambda_B3F4():
        OP_95(0x15, 4740, 4000, 4480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B3F4)
    OP_95(0x16, 5730, 4000, 11500, 2000, 0x0)

    def lambda_B422():
        OP_93(0x101, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B422)

    def lambda_B42F():
        OP_93(0x105, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B42F)
    OP_95(0x16, 4740, 4000, 4480, 2000, 0x0)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    StopBGM(0xFA0)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x109)
    OP_64(0x105)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)

    ChrTalk(
        0x101,
        "#00013F#5PWh-What just happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PW-We just let them go,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHaha, that was no\x01",
            "ordinary girl.\x02\x03",
            "#10309FShe's about 15 or 16?\x01",
            "She did quite a number\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x2, 0x3, 0x4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00107F#5P#4SIt wasn't good at all!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x8, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0x8, 0x7)

    ChrTalk(
        0x102,
        (
            "#00106F#5P#30WOoh... Why did I have to\x01",
            "go through that...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00012F#11PUmm... That was a\x01",
            "disaster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5PW-Well, you're both\x01",
            "girls, so you don't take\x01",
            "it so seriously.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x109, 500)

    ChrTalk(
        0x105,
        (
            "#10305F#12PAnd aren't you used to\x01",
            "Miss Mariabell fondling\x01",
            "them?\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x4, 0x7, 0xA, 0xB, 0xC)
    Sleep(100)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00115F#5P#5SI-I am not!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19530, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the\x01",
            "others returned to Police HQ\x01",
            "and called Section One...\x02\x03",
            "They reported the actions of\x01",
            "Heiyue and the information\x01",
            "regarding Lechter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CC(0x1, 0xFF, 0x0)
    SetMapObjFrame(0xFF, "white00", 0x0, 0x1)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 1)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_9A29 end

    def Function_30_B7ED(): pass

    label("Function_30_B7ED")


    def lambda_B7F2():
        OP_95(0x101, 5030, 4000, 10490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B7F2)
    WaitChrThread(0x101, 1)

    def lambda_B810():
        OP_95(0x101, 6540, 4000, 11860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B810)
    WaitChrThread(0x101, 1)

    def lambda_B82E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B82E)
    Return()

    # Function_30_B7ED end

    def Function_31_B837(): pass

    label("Function_31_B837")


    def lambda_B83C():
        OP_95(0x102, 5500, 4000, 9870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B83C)
    WaitChrThread(0x102, 1)

    def lambda_B85A():
        OP_95(0x102, 5520, 4000, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B85A)
    WaitChrThread(0x102, 1)

    def lambda_B878():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B878)
    Return()

    # Function_31_B837 end

    def Function_32_B881(): pass

    label("Function_32_B881")


    def lambda_B886():
        OP_95(0x109, 4810, 4000, 13910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B886)
    WaitChrThread(0x109, 1)

    def lambda_B8A4():
        OP_95(0x109, 5530, 4000, 14790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B8A4)
    WaitChrThread(0x109, 1)

    def lambda_B8C2():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B8C2)
    Return()

    # Function_32_B881 end

    def Function_33_B8CB(): pass

    label("Function_33_B8CB")


    def lambda_B8D0():
        OP_95(0x105, 4800, 4000, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B8D0)
    WaitChrThread(0x105, 1)

    def lambda_B8EE():
        OP_95(0x105, 4740, 4000, 10780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B8EE)
    WaitChrThread(0x105, 1)

    def lambda_B90C():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B90C)
    Return()

    # Function_33_B8CB end

    def Function_34_B915(): pass

    label("Function_34_B915")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9F(0x0, 0x16)
    OP_9F(0x1, 4740, 4000, 12360)
    OP_9F(0x1, 4740, 4000, 13900)
    OP_9F(0x1, 5520, 4000, 13900)
    OP_9F(0x2, 0x16, 8000, 0x6)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0x16, 0xB4, 0x0)
    Return()

    # Function_34_B915 end

    def Function_35_B964(): pass

    label("Function_35_B964")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B984")
    Sound(888, 0, 70, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_35_B964")

    label("loc_B984")

    Return()

    # Function_35_B964 end

    def Function_36_B985(): pass

    label("Function_36_B985")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B9A5")
    Sound(888, 0, 70, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x3, 0x4, 0x5, 0x4)
    Jump("Function_36_B985")

    label("loc_B9A5")

    Return()

    # Function_36_B985 end

    SaveToFile()

Try(main)
