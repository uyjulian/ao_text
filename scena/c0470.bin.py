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
        "Function_5_2586",         # 05, 5
        "Function_6_2C48",         # 06, 6
        "Function_7_2C4C",         # 07, 7
        "Function_8_3CEF",         # 08, 8
        "Function_9_3D24",         # 09, 9
        "Function_10_3D28",        # 0A, 10
        "Function_11_4CB0",        # 0B, 11
        "Function_12_4D6C",        # 0C, 12
        "Function_13_4D70",        # 0D, 13
        "Function_14_5C1A",        # 0E, 14
        "Function_15_6BE8",        # 0F, 15
        "Function_16_7BFA",        # 10, 16
        "Function_17_7CE7",        # 11, 17
        "Function_18_805C",        # 12, 18
        "Function_19_8105",        # 13, 19
        "Function_20_81AA",        # 14, 20
        "Function_21_82F3",        # 15, 21
        "Function_22_83F3",        # 16, 22
        "Function_23_85AF",        # 17, 23
        "Function_24_8627",        # 18, 24
        "Function_25_86A6",        # 19, 25
        "Function_26_881D",        # 1A, 26
        "Function_27_97EE",        # 1B, 27
        "Function_28_9883",        # 1C, 28
        "Function_29_9ED9",        # 1D, 29
        "Function_30_BDF1",        # 1E, 30
        "Function_31_BE3B",        # 1F, 31
        "Function_32_BE85",        # 20, 32
        "Function_33_BECF",        # 21, 33
        "Function_34_BF19",        # 22, 34
        "Function_35_BF68",        # 23, 35
        "Function_36_BF89",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B51")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "...Randy, you're heading\x01",
            "to that "huge tree", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHa ha, you know me well.\x01",
            "Typical of Owner Drake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, I've not known you\x01",
            "for a short time, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Randy, a part of what you\x01",
            "have to pay still remains in the \x01",
            "tab of what you drank until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I won't accept it if you don't\x01",
            "absolutely came back all in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F...Yeah, got it.\x02\x03",
            "#00309FEventually I'll pay it back,\x01",
            "so don't you worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Ha ha... I guess this is how these\x01",
            "two communicate between them.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 0)
    Jump("loc_CFC")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C90")

    ChrTalk(
        0x8,
        (
            "Right now, hard times could be\x01",
            "coming to visit Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Everyone, please\x01",
            "take care of Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because that guy has still\x01",
            "got a part of what he drank\x01",
            "until now on his tab to pay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYes, leave him to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FEventually I'll pay it back,\x01",
            "so don't you worry about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CFC")

    label("loc_C90")


    ChrTalk(
        0x8,
        (
            "Right now, hard times could be\x01",
            "coming to visit Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Everyone, please\x01",
            "take care of Randy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFC")

    Jump("loc_2582")

    label("loc_D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_106F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC2")

    ChrTalk(
        0x8,
        "Ooh, if it isn't everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FBeen awhile, Owner.\x01",
            "Looks like you've doin' fine?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)

    ChrTalk(
        0x8,
        "So do you, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard you threw yourself into Mainz\x01",
            "resistance activities, but I'm glad you \x01",
            "could reunite with your colleagues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FDid you suffer\x01",
            "any damage here?\x02",
        )
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
            "You all too, please be very careful\x01",
            "if you are going around town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah, you too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 7)
    Jump("loc_106A")

    label("loc_EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC6")

    ChrTalk(
        0x8,
        (
            "At any rate, I was right in reducing my\x01",
            "business because of martial law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With this small group, we can hold out with\x01",
            "the store emergency reserves for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, do not worry about us.\x01",
            "Everyone, please face\x01",
            "your own work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_106A")

    label("loc_FC6")


    ChrTalk(
        0x8,
        (
            "With this small group, we can hold out with\x01",
            "the store emergency reserves for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, do not worry about us.\x01",
            "Everyone, please face\x01",
            "your own work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106A")

    Jump("loc_2582")

    label("loc_106F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1215")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117A")

    ChrTalk(
        0x8,
        (
            "Hmm... I thought there're a bunch of guys\x01",
            "wearing unfamiliar uniforms since morning,\x01",
            "so those are the State Guard soldiers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Indeed, they look like\x01",
            "they're all ready...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder since when \x01",
            "Mr. Crois pictured\x01",
            "this scenario...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1210")

    label("loc_117A")


    ChrTalk(
        0x8,
        (
            "Come to think of it, it hasn't passed even\x01",
            "one week since that local referendum...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder since when \x01",
            "Mr. Crois pictured\x01",
            "this scenario...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1210")

    Jump("loc_2582")

    label("loc_1215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_151B")

    ChrTalk(
        0x8,
        (
            "Hey, Randy.\x01",
            "I don't know what happened, but somehow\x01",
            "you've got a break through face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although in this situation\x01",
            "no business is being done,\x01",
            "I wonder what're you scheming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHm, to me, it seems nothing's\x01",
            "different than usual, you know?\x02\x03",
            "#00309FWell, Owner, since I couldn't be\x01",
            "able to show up in here for a little,\x01",
            "weren't you already lonely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, nonsense.\x01",
            "With the nitpicky one gone, I\x01",
            "was conversely doing neatly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At any rate, I lent you\x01",
            "a lot of "stuff" until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "See that you don't evade your responsibilities\x01",
            "until you have given me back everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHah, I know without you tellin' me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(These two go along well, no\x01",
            "matter what one could say.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F(Yes, just like two kids.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 1)
    Jump("loc_15CA")

    label("loc_151B")


    ChrTalk(
        0x8,
        (
            "At any rate, Randy, do not\x01",
            "forget that I lent you a lot\x01",
            "of stuff until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There isn't a particular fixed term, but one\x01",
            "day you'll absolutely have to give it back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CA")

    Jump("loc_2582")

    label("loc_15CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_173C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C0")

    ChrTalk(
        0x8,
        (
            "What I can do for that guy is\x01",
            "only giving him a place where\x01",
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
            "Everyone, please...\x01",
            "I leave Randy in your care.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1737")

    label("loc_16C0")


    ChrTalk(
        0x8,
        (
            "I feel that you all\x01",
            "can, in a real sense,\x01",
            "be of help to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please...\x01",
            "I leave Randy in your care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1737")

    Jump("loc_2582")

    label("loc_173C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_18BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182C")

    ChrTalk(
        0x8,
        (
            "Tomorrow is going to finally be the\x01",
            "renewal play opening public day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that in this play,\x01",
            "after that Rixia Mao, a \x01",
            "promising rookie will debut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hu hu, Arc-en-ciel topics\x01",
            "always entertain me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18B7")

    label("loc_182C")


    ChrTalk(
        0x8,
        (
            "It seems that in this play,\x01",
            "after that Rixia Mao, a \x01",
            "promising rookie will debut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hu hu, Arc-en-ciel topics\x01",
            "always entertain me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B7")

    Jump("loc_2582")

    label("loc_18BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1993")

    ChrTalk(
        0x8,
        (
            "Welcome to\x01",
            "Casino House "Barca".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you want to rest your brain, please\x01",
            "make use of our bar counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can naturally serve you alcohol,\x01",
            "but also coffee and other things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A29")

    label("loc_1993")


    ChrTalk(
        0x8,
        (
            "When you want to rest your brain, please\x01",
            "make use of our bar counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can naturally serve you alcohol,\x01",
            "but also coffee and other things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A29")

    Jump("loc_2582")

    label("loc_1A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC3")

    ChrTalk(
        0x8,
        (
            "The pros and cons of the state independence...\x01",
            "This is still one hell of a problem among the squirming\x01",
            "power relationships of the underground world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't really think that the local referendum\x01",
            "will be tied to some immediate actions, but...\x01",
            "The problem is the two major powers' moves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If handled poorly, Crossbell position\x01",
            "will worsen even more than it is now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CA3")

    label("loc_1BC3")


    ChrTalk(
        0x8,
        (
            "I can't really think that the local referendum\x01",
            "will be tied to some immediate actions, but...\x01",
            "The problem is the two major powers' moves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If handled poorly, Crossbell position\x01",
            "will worsen even more than it is now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA3")

    Jump("loc_2582")

    label("loc_1CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1D35")

    ChrTalk(
        0x8,
        (
            "Hm, it appears that it's\x01",
            "a little noisy downstair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If they get louder than that, I will\x01",
            "have to ask them to leave...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2582")

    label("loc_1D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DBD")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "Welcome to Casino House "Barca".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What about a sweet cocktail that\x01",
            "will melt your body and soul too...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2582")

    label("loc_1DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E41")

    ChrTalk(
        0x8,
        (
            "It appears that Orchis Tower unveiling\x01",
            "ceremony ended in a success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hu hu, I too will go to enjoy it later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2582")

    label("loc_1E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2218")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A6")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Hey, Randy. Are you already\x01",
            "sober from yesterday's liquor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHah, it goes without sayin'.\x01",
            "Did you think that that narrow amount of\x01",
            "liquor would still remain in me the day after?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, always the\x01",
            "fast-talking guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it was a celebration for your return,\x01",
            "it doesn't mean that I was treating you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHa ha, sorry.\x01",
            "But I'm grateful, you know?\x02\x03",
            "#00300FAnd so, Owner, let's do it\x01",
            "again if chance arises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmph, always saying what you want.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(It appears that Randy \x01",
            "showed up on purpose.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(Yeah, that's right.)\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    SetScenarioFlags(0x14C, 2)
    Jump("loc_2213")

    label("loc_20A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2180")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Well, if you want me to treat you again,\x01",
            "you shoud fix that impudent talk of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do that, \x01",
            "I can think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah, yeah, well,\x01",
            "I'll be more discreet.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2213")

    label("loc_2180")

    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Well, if you want me to treat you again,\x01",
            "you shoud fix that impudent talk of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do that, \x01",
            "I can think about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    label("loc_2213")

    Jump("loc_2582")

    label("loc_2218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_24E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2233")
    Call(0, 5)
    Jump("loc_24DB")

    label("loc_2233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2405")

    ChrTalk(
        0x8,
        (
            "Recently, instead of Revache some\x01",
            "small fries asking to hand over\x01",
            "protection mira have appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At present I won't oppose them,\x01",
            "but if this situation keeps on, it\x01",
            "will lead to many bothersome things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My my, they want to inherit \x01",
            "quickly the turf Revache left,\x01",
            "no matter which part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F(The effects of Revache's\x01",
            "disappearance are here too...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(This too is one of the place that\x01",
            "supported their fake-like order.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24DB")

    label("loc_2405")


    ChrTalk(
        0x8,
        (
            "At present, it appears that those\x01",
            "guys are behaving relatively quietly...\x01",
            "But if the situation goes on, it'll be trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My my, they want to inherit \x01",
            "quickly the turf Revache left,\x01",
            "no matter which part.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DB")

    Jump("loc_2582")

    label("loc_24E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FB")
    Call(0, 5)
    Jump("loc_2582")

    label("loc_24FB")


    ChrTalk(
        0x8,
        (
            "That Randy is doing fine\x01",
            "blending in the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hu hu, if it helps him to not say pathetic\x01",
            "things like in the past, then good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2582")

    TalkEnd(0x8)
    Return()

    # Function_4_90A end

    def Function_5_2586(): pass

    label("Function_5_2586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A51")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Everyone from the Special Support Section...\x01",
            "And if it isn't Mr. Wazy too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Quite the unusual combination.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYeah, Owner.\x01",
            "The truth is that it was decided my\x01",
            "assignment to the Special Support Section.\x02\x03",
            "I'll omit the details, but please take good\x01",
            "care of me from now on like one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I understand...\x01",
            "Hu hu, as you wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FH-He readily accepted him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat's true too, but...\x01",
            "Wazy, it's granted that you're\x01",
            "an Owner's acquaintance, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, for hosts, this area,\x01",
            "casino included, is a\x01",
            "working place zone.\x02\x03",
            "#10300FConversely, wouldn't a host\x01",
            "who doesn't know of Owner Drake\x01",
            "be unqualified or third rate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHe says it nonchalantly...\x02\x03",
            "#10101FAnd also, playing around this\x01",
            "neighborhood at your age is\x01",
            "not a good thing.\x02\x03",
            "#10103FYou should take this occasion to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, stuffy as always.\x02\x03",
            "Well, I think that this aspect is\x01",
            "among your charming points too㈱\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2971")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2971")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2997")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2997")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29BD")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_29BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29E3")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_29E3")

    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10106F*sigh*, somehow all of a\x01",
            "sudden I don't care anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FI know that feeling.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 7)
    Jump("loc_2C47")

    label("loc_2A51")


    ChrTalk(
        0x8,
        (
            "By the way, everyone,\x01",
            "hasn't Randy come\x01",
            "back yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard before from the guy himself that\x01",
            "he went back to his former home, the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, I think we'll be able to reunite\x01",
            "with him just in a little while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I understand. Then, well, could you\x01",
            "please tell the guy to show up at the\x01",
            "store when he comes back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tell him that I said that I will prepare\x01",
            "a bottle of wine to celebrate his return.\x02",
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
        "#00100FWe will tell him that for sure.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 6)

    label("loc_2C47")

    Return()

    # Function_5_2586 end

    def Function_6_2C48(): pass

    label("Function_6_2C48")

    Call(0, 7)
    Return()

    # Function_6_2C48 end

    def Function_7_2C4C(): pass

    label("Function_7_2C4C")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CEB")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",          # 0
            "Exchange\x01",      # 1
            "Quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CAD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2CCC")
    OP_AF(0x41)
    Jump("loc_2D0E")

    label("loc_2CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2CDC")
    OP_AF(0x40)
    Jump("loc_2D0E")

    label("loc_2CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CEC")
    OP_AF(0x3F)
    Jump("loc_2D0E")

    label("loc_2CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CFC")
    OP_AF(0x3E)
    Jump("loc_2D0E")

    label("loc_2CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D0C")
    OP_AF(0x3D)
    Jump("loc_2D0E")

    label("loc_2D0C")

    OP_AF(0x3C)

    label("loc_2D0E")

    Call(0, 8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CE6")

    label("loc_2D20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D34")
    Jump("loc_3CE6")

    label("loc_2D34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CE6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD0")

    ChrTalk(
        0x9,
        (
            "Welcome,\x01",
            "welcome to Casino House "Barca"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please go play a lot and\x01",
            "blow away your anxieties☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E37")

    label("loc_2DD0")


    ChrTalk(
        0x9,
        (
            "We're open as usual\x01",
            "even at such a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please go play a lot and\x01",
            "blow away your anxieties☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E37")

    Jump("loc_3CE6")

    label("loc_2E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2FBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EFA")

    ChrTalk(
        0x9,
        (
            "Uuh, frankly, I'm scared, but...\x01",
            "I'm glad that Mr. Galletti\x01",
            "and Miss Elinde can rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The Owner is doing his best, so I\x01",
            "have to get my act together too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FBA")

    label("loc_2EFA")


    ChrTalk(
        0x9,
        (
            "Because Mr. Galletti and Miss Elinde are on\x01",
            "holiday, you can't play at the ground floor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There could be something useful\x01",
            "among our prizes, so use the\x01",
            "counter as always, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FBA")

    Jump("loc_3CE6")

    label("loc_2FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_306C")

    ChrTalk(
        0x9,
        (
            "Uuhm, don't tell me that it'll\x01",
            "turn out into a sudden war, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what kind of statements the two\x01",
            "major powers will issue in response to this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE6")

    label("loc_306C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_311F")

    ChrTalk(
        0x9,
        "Uuhm, a local referendum?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They say there are going to be several \x01",
            "polling places, but as I thought, if I have \x01",
            "to go, I'd like it to be the Orchis Tower☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE6")

    label("loc_311F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_31CF")

    ChrTalk(
        0x9,
        (
            "Uuhm, although they're events\x01",
            "outside of Crossbell City, Mainz\x01",
            "facts aren't someone else's business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I hope the situation will be resolved safely fast.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CE6")

    label("loc_31CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_32FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3289")

    ChrTalk(
        0x9,
        (
            "The Arc-en-ciel public performance\x01",
            "is finally going to be tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sure that we'll have guests\x01",
            "flowing in again too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uhu, I can't wait㈱\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32F9")

    label("loc_3289")


    ChrTalk(
        0x9,
        (
            "There're quite many persons who come here\x01",
            "after finishing to see the Arc-en-ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uhu, I can't wait㈱\x02",
    )

    CloseMessageWindow()

    label("loc_32F9")

    Jump("loc_3CE6")

    label("loc_32FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3381")

    ChrTalk(
        0x9,
        (
            "Tell me whenever you want\x01",
            "if you ran out of medals, ok?☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And if you ran out of mira,\x01",
            "let's go to the IBC!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE6")

    label("loc_3381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_33DA")

    ChrTalk(
        0x9,
        "Welcome to "Barca"!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uhuhu, please go play\x01",
            "a lot today too, ok?☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE6")

    label("loc_33DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3498")

    ChrTalk(
        0x9,
        (
            "That group of three...\x01",
            "They look like to be rich, but\x01",
            "I feel they're very bad people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We were looked at with an arrogant attitude.\x01",
            "Should we withdraw their requests?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE6")

    label("loc_3498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3534")

    ChrTalk(
        0x9,
        (
            "At last, the Trade Conference\x01",
            "is going to take place today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Cherry doesn't really get it, but at\x01",
            "any rate, she hopes it goes well㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE6")

    label("loc_3534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3727")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3671")

    ChrTalk(
        0x9,
        (
            "It looks like that Mr. Gantz,\x01",
            "without learning from experience,\x01",
            "is hard at work at the slots today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although he's doing so poorly you\x01",
            "wonder what the heck was that luck\x01",
            "he had some months ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Could it be that Mr. Gantz\x01",
            "at that time used up all the\x01",
            "luck of a lifetime?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3722")

    label("loc_3671")


    ChrTalk(
        0x9,
        (
            "Could it be that Mr. Gantz\x01",
            "at that time used up all the\x01",
            "luck of a lifetime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, anyway eeevery once\x01",
            "in a while it looks like he get\x01",
            "some, so it's probably not that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3722")

    Jump("loc_3CE6")

    label("loc_3727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_399F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394C")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x104, 0)

    ChrTalk(
        0x9,
        "Ah, it Mr. Randyyy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Geez, where have you been these days?\x01",
            "That's no good, you've got to play more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FMan, sorry little Cherry.\x02\x03",
            "#00309FAnd so, I'll end my job at once and...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38AE")

    ChrTalk(
        0x101,
        "#00009FHey, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, of course you're joking, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FY-Yeah... Hey, your smiles\x01",
            "are scary, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3944")

    label("loc_38AE")


    ChrTalk(
        0x102,
        (
            "#00109FHey, Randy.\x01",
            "I think we just told you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FY-yeah...  \x01",
            "That's just a joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Senior Randy...\x01",
            "You really never learn.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3944")

    SetScenarioFlags(0x14C, 3)
    Jump("loc_399A")

    label("loc_394C")


    ChrTalk(
        0x9,
        (
            "Mr. Randy, come \x01",
            "frequently again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Or else, Cherry\x01",
            "will be booored.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399A")

    Jump("loc_3CE6")

    label("loc_399F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A0D")

    ChrTalk(
        0x9,
        (
            "Brush away this sodden and\x01",
            "gloomy rain at the casinooo☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Play all you want today too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CE6")

    label("loc_3A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B33")

    ChrTalk(
        0x9,
        (
            "Some time ago, all of a sudden,\x01",
            "Mr. Lechter came unexpectedly\x01",
            "and went up to the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh uh, I had seen him some months ago, \x01",
            "but he's always a strange man, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FLloyd...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYeah, this time for sure he won't get away.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BE7")

    label("loc_3B33")


    ChrTalk(
        0x9,
        (
            "Some time ago, all of a sudden,\x01",
            "Mr. Lechter came unexpectedly\x01",
            "and went up to the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh uh, I had seen him some months ago, \x01",
            "but he's always a strange man, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE7")

    Jump("loc_3CE6")

    label("loc_3BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C80")

    ChrTalk(
        0x9,
        "Welcome to "Barca"!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is the medal and prizes\x01",
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
    Jump("loc_3CE6")

    label("loc_3C80")


    ChrTalk(
        0x9,
        (
            "This the medal and prizes\x01",
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

    label("loc_3CE6")

    Jump("loc_2C59")

    label("loc_3CEB")

    TalkEnd(0x9)
    Return()

    # Function_7_2C4C end

    def Function_8_3CEF(): pass

    label("Function_8_3CEF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D23")
    SubItemNumber(0x18C, 1)
    AddItemNumber(0x186, 1)
    AddItemNumber(0x187, 1)
    AddItemNumber(0x188, 1)
    AddItemNumber(0x189, 1)
    AddItemNumber(0x18A, 1)
    Jump("Function_8_3CEF")

    label("loc_3D23")

    Return()

    # Function_8_3CEF end

    def Function_9_3D24(): pass

    label("Function_9_3D24")

    Call(0, 10)
    Return()

    # Function_9_3D24 end

    def Function_10_3D28(): pass

    label("Function_10_3D28")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CAC")
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
            "Quit\x01",                # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D9A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3D9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DEF")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3DEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E44")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3E44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E58")
    Jump("loc_4CA7")

    label("loc_3E58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CA7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4032")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F7B")

    ChrTalk(
        0xA,
        (
            "Our regular Miss Rey Talossa\x01",
            "went back to her country and\x01",
            "I feel very lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After all, the matches full of thrills\x01",
            "against her where my daily pleasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope she will come to play again\x01",
            "after Crossbell regains its peace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_402D")

    label("loc_3F7B")


    ChrTalk(
        0xA,
        (
            "Our regular Miss Rey Talossa...\x01",
            "I hope she will come to play again\x01",
            "after Crossbell regains its peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's been difficult since such a\x01",
            "mysterious tree appeared, and...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402D")

    Jump("loc_4CA7")

    label("loc_4032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4040")
    Jump("loc_4CA7")

    label("loc_4040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4190")

    ChrTalk(
        0xA,
        (
            "Today, it seems that the orbal railroad\x01",
            "service has been limited since the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It was made an official announcement advising\x01",
            "the Empire and Republican people in Crossbell\x01",
            "to return to their countries of origin...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The situation could be moving\x01",
            "at a speed faster than what\x01",
            "we were thinking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_426C")

    label("loc_4190")


    ChrTalk(
        0xA,
        (
            "It was made an official announcement advising\x01",
            "the Empire and Republican people in Crossbell\x01",
            "to return to their countries of origin...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The situation could be moving\x01",
            "at a speed faster than what\x01",
            "we were thinking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426C")

    Jump("loc_4CA7")

    label("loc_4271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43A3")

    ChrTalk(
        0xA,
        (
            "When I see the burns remaining on the ground even now...\x01",
            "I am reminded of the time the raid occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Fortunately, the armed group\x01",
            "didn't enter the store, but...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If this had been attacked,\x01",
            "what would have happened to us...?\x01",
            "Only thinking about it is frightening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_444F")

    label("loc_43A3")


    ChrTalk(
        0xA,
        (
            "Fortunately, the armed group\x01",
            "didn't enter the store, but...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If this had been attacked,\x01",
            "what would have happened to us...?\x01",
            "Only thinking about it is frightening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_444F")

    Jump("loc_4CA7")

    label("loc_4454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_450B")

    ChrTalk(
        0xA,
        (
            "There're already rumors...\x01",
            "Thinking that behind this there's\x01",
            "the Empire is somewhat natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At any rate, the worrisome point\x01",
            "is what will the Empire do next.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA7")

    label("loc_450B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_460C")

    ChrTalk(
        0xA,
        (
            "The question about state independence...\x01",
            "I am sure that the fixed date for the\x01",
            "local referendum is getting close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, which one of the choices would\x01",
            "bring forth the best results...?\x01",
            "I want to carefully think about it a little more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA7")

    label("loc_460C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46A2")

    ChrTalk(
        0xA,
        (
            "I wonder which one is happier between\x01",
            "a life of tedium and one full of stimulus...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hu hu, mister customer, what do you think?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CA7")

    label("loc_46A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4736")

    ChrTalk(
        0xA,
        (
            "Becoming sulky when excessively losing\x01",
            "is a second-rate thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Sometimes I wish the customers\x01",
            "to be in  really good faith.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA7")

    label("loc_4736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_48CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482E")

    ChrTalk(
        0xA,
        (
            "(They have been making quite some noise since\x01",
            "some time ago and disturbing the other customers...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(The customers over there\x01",
            "lacks a little manners.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(If they exaggerate, I will\x01",
            "have to sternly warn them.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48CA")

    label("loc_482E")


    ChrTalk(
        0xA,
        (
            "(No matter if this is a casino,\x01",
            "in this place there're rules and\x01",
            "manners applying to it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(If they exaggerate, I will\x01",
            "have to sternly warn them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48CA")

    Jump("loc_4CA7")

    label("loc_48CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4962")

    ChrTalk(
        0xA,
        (
            "Mayor Dieter's\x01",
            "gambling sense...?\x01",
            "Hmm, how is it I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The impression is that he can\x01",
            "cope smartly with such games too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA7")

    label("loc_4962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4AEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A46")

    ChrTalk(
        0xA,
        (
            "Today it appears that Mr.\x01",
            "Gantz came to visit us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I was really surprised by his\x01",
            "strong luck some time ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now he has reversed completely to\x01",
            "be the boring weekend gambler he was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AE6")

    label("loc_4A46")


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
            "Now he has reversed completely to\x01",
            "be the boring weekend gambler he was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE6")

    Jump("loc_4CA7")

    label("loc_4AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4BA9")

    ChrTalk(
        0xA,
        (
            "It appears that high class\x01",
            "club, "Neue-Blanc" had a\x01",
            "renewal opening lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It is a place very unreachable\x01",
            "for someone like me, however...\x01",
            "I'd like to go there once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA7")

    label("loc_4BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4C51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BC4")
    Call(0, 11)
    Jump("loc_4C4C")

    label("loc_4BC4")


    ChrTalk(
        0xA,
        (
            "Dear me, Lady Rey Talossa\x01",
            "is really fearless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Gambling is result, more than process...\x01",
            "Victory belong to the last who laughs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C4C")

    Jump("loc_4CA7")

    label("loc_4C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4CA7")

    ChrTalk(
        0xA,
        (
            "Welcome.\x01",
            "This is the cards table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "What about a match, if you like?\x02",
    )

    CloseMessageWindow()

    label("loc_4CA7")

    Jump("loc_3D35")

    label("loc_4CAC")

    TalkEnd(0xA)
    Return()

    # Function_10_3D28 end

    def Function_11_4CB0(): pass

    label("Function_11_4CB0")

    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "...I am sorry for you, but\x01",
            "this match is mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uh uh, you are good.\x01",
            "However, the next one won't go like this㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hu hu, please go easy on me.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_11_4CB0 end

    def Function_12_4D6C(): pass

    label("Function_12_4D6C")

    Call(0, 13)
    Return()

    # Function_12_4D6C end

    def Function_13_4D70(): pass

    label("Function_13_4D70")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C16")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",               # 0
            "Play Roulette\x01",      # 1
            "Quit\x01",               # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DD6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4DD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E2B")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_4E2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E3F")
    Jump("loc_5C11")

    label("loc_4E3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C11")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_502F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F71")

    ChrTalk(
        0xB,
        (
            "Coming to gamble at such a time...\x01",
            "That's not a bad thing at all.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all, by nature, it is a\x01",
            "pleasure to divert anxious feelings\x01",
            "and to soothe the mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please, I wish you enjoy it with pleasure\x01",
            "right because these are worrying times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_502A")

    label("loc_4F71")


    ChrTalk(
        0xB,
        (
            "After all, by nature, it is a\x01",
            "pleasure to divert anxious feelings\x01",
            "and to soothe the mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please, I wish you to enjoy it with pleasure\x01",
            "right because these are worrying times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_502A")

    Jump("loc_5C11")

    label("loc_502F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_503D")
    Jump("loc_5C11")

    label("loc_503D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_51E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514F")

    ChrTalk(
        0xB,
        (
            "The Crossbell independence problem\x01",
            "has ended up reaching a point that\x01",
            "it can't be taken back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't think President Dieter\x01",
            "is doing this much without\x01",
            "having a chance to win, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder what kind of\x01",
            "card has it ready to play?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_51E3")

    label("loc_514F")


    ChrTalk(
        0xB,
        (
            "I don't think President Dieter\x01",
            "is doing this much without\x01",
            "having a chance to win, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder what kind of\x01",
            "card has it ready to play?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51E3")

    Jump("loc_5C11")

    label("loc_51E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52E9")

    ChrTalk(
        0xB,
        (
            "the local referendum day is finally\x01",
            "close. It's going to be in three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can foresee the result,\x01",
            "but on that day I too\x01",
            "plan to go to vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As for which one I'll vote for...\x01",
            "Please, allow me to keep it a secret.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_537F")

    label("loc_52E9")


    ChrTalk(
        0xB,
        (
            "I can foresee the result,\x01",
            "but on that day I too\x01",
            "plan to go to vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As for which one I'll vote for...\x01",
            "Please, allow me to keep it a secret.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_537F")

    Jump("loc_5C11")

    label("loc_5384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_53F8")

    ChrTalk(
        0xB,
        (
            "Owner Drake...\x01",
            "Somehow, he looks like a little sleepy today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Did he drink\x01",
            "until late again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C11")

    label("loc_53F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_548D")

    ChrTalk(
        0xB,
        (
            "On such a rainy day, please come have\x01",
            "an enjoyable time at our establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhuhu, I could give you\x01",
            "something free. Maybe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C11")

    label("loc_548D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5563")

    ChrTalk(
        0xB,
        (
            "Being it gambling or anything else...\x01",
            "What is important is the time to quit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            ""Befitting your station"is also another way to say it.\x01",
            "Desiring a lot will generally end in a failure, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C11")

    label("loc_5563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_560F")

    ChrTalk(
        0xB,
        (
            "I think that humans are living\x01",
            "beings who seek thrills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Mister customer, what about a match?\x01",
            "I will give first-rate thrills\x01",
            "as a present, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C11")

    label("loc_560F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_569C")

    ChrTalk(
        0xB,
        "Should Crossbell be independent or not...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Honestly, Mayor Dieter has\x01",
            "thrusted at us a terrifically\x01",
            "difficult theme.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C11")

    label("loc_569C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5722")

    ChrTalk(
        0xB,
        (
            "Uhuhu, finally the day\x01",
            "of the conference has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "From now on, I can't wait\x01",
            "for the next Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C11")

    label("loc_5722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_57F1")

    ChrTalk(
        0xB,
        (
            "I haven't seen it yet, but\x01",
            "it appears that Orchis Tower\x01",
            "is a really imposing building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A super high-rise building 40 floors above ground...\x01",
            "I can't wait to sear its image in my eyes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C11")

    label("loc_57F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_59DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_594C")

    ChrTalk(
        0xB,
        (
            "The international conference called by\x01",
            "Mayor Dieter is finally going to start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Reading out each other's true intentions,\x01",
            "using with the right timing at critical moments\x01",
            "various trump cards each of them possess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Saying it like this, somehow I\x01",
            "think that diplomacy and gambling\x01",
            "are, in essence, the same.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_59D5")

    label("loc_594C")


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
        "Uhuhu, I am so very interested.\x02",
    )

    CloseMessageWindow()

    label("loc_59D5")

    Jump("loc_5C11")

    label("loc_59DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5A54")

    ChrTalk(
        0xB,
        "Uh uh, mister customer, what about playing a match?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I will invite you to a labyrinth of thoughts.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C11")

    label("loc_5A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5C11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B7C")

    ChrTalk(
        0xB,
        (
            "Welcome to Casino House "Barca".\x01",
            "Here you can enjoy roulette.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You could refuse at first,\x01",
            "but at this table any kind of\x01",
            "cheating is absolutely impossible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What do you say, don't you want to surrender\x01",
            "yourself to fate only once without any petty tricks?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5C11")

    label("loc_5B7C")


    ChrTalk(
        0xB,
        (
            "Betting largely, dilutedly and steadily is good too...\x01",
            "Playing small, kind matches is good too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Only the Goddess knows all results, yes.\x02",
    )

    CloseMessageWindow()

    label("loc_5C11")

    Jump("loc_4D7D")

    label("loc_5C16")

    TalkEnd(0xB)
    Return()

    # Function_13_4D70 end

    def Function_14_5C1A(): pass

    label("Function_14_5C1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5C2B")
    Jump("loc_6BE4")

    label("loc_5C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D4D")

    ChrTalk(
        0xFE,
        (
            "I wasn't right here, but it appears\x01",
            "that a terrible incident happened\x01",
            "one week ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems it can't be firmly said that something \x01",
            "like that won't happen again in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It could be better to withdraw from\x01",
            "coming to have fun in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5DFB")

    label("loc_5D4D")


    ChrTalk(
        0xFE,
        (
            "It seems it can't be firmly said that something \x01",
            "like that won't happen again in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It could be better to withdraw from\x01",
            "coming to have fun in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DFB")

    Jump("loc_6BE4")

    label("loc_5E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5EA1")

    ChrTalk(
        0xFE,
        (
            "I wonder what the armed\x01",
            "group objective could be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Naturally I know that in the future\x01",
            "some kind of demands could\x01",
            "suddenly come out...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BE4")

    label("loc_5EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5F4C")

    ChrTalk(
        0xFE,
        (
            "By the way, today, at the\x01",
            "City Meeting Hall there's\x01",
            "a civic forum going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if to go have a look for a\x01",
            "bit later, as a social study trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BE4")

    label("loc_5F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5FBC")

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm feeling bored again\x01",
            "even having fun in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Isn't there anything fun?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BE4")

    label("loc_5FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E1")

    ChrTalk(
        0xFE,
        (
            "Yesterday's sloths were\x01",
            "doing good at the very beginning,\x01",
            "but in the end they lost greatly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe for being greatly mortified,\x01",
            "they spouted dirty parting threats\x01",
            "and went away at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, even the Goddess would\x01",
            "fall out of love with those ones.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6161")

    label("loc_60E1")


    ChrTalk(
        0xFE,
        (
            "It looks like yesterday's sloths\x01",
            "didn't come to the casino today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, it seems that today\x01",
            "I can focus on the game.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6161")

    Jump("loc_6BE4")

    label("loc_6166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_62B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6227")

    ChrTalk(
        0xFE,
        (
            "I have no interest in the likes of a shallow man\x01",
            "clung to his parents' mira and authority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, as expected,\x01",
            "it must be a refined dandy\x01",
            "like Owner Drake.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_62B0")

    label("loc_6227")


    ChrTalk(
        0xFE,
        (
            "No matter how much mira he has,\x01",
            "someone like a sloth is a no.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, as expected,\x01",
            "it must be a refined dandy\x01",
            "like Owner Drake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62B0")

    Jump("loc_6BE4")

    label("loc_62B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6364")

    ChrTalk(
        0xFE,
        (
            "The Trade Conference...\x01",
            "Uh uh, that Mayor Dieter\x01",
            "is really a shrewd person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being this much skilled at politics...\x01",
            "Could he be strong at gambling too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BE4")

    label("loc_6364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_63FD")

    ChrTalk(
        0xFE,
        (
            "It seems that Mr. Galletti\x01",
            "still holds a grudge for having\x01",
            "lost to Mr. Gantz previously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, gamblers really\x01",
            "hate losing, hm?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BE4")

    label("loc_63FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6AC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67A0")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64B6")
    Jump("loc_6500")

    label("loc_64B6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_64D6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6500")

    label("loc_64D6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64F6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6500")

    label("loc_64F6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6500")

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
            "#00305FOoh, you too,\x01",
            "Miss Rey Talossa.\x02\x03",
            "#00302FSay, why not goin' on a date with me\x01",
            "to celebrate our meetin' again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, let's see.\x01",
            "If you were to beat me in a match,\x01",
            "I could think about it, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOoh, you said it, eh?\x01",
            "Then, let's get it at onc―\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66FE")

    ChrTalk(
        0x101,
        "#00009FHey, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, of course you're joking, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FY-Yeah... Hey, your smiles\x01",
            "are scary, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6794")

    label("loc_66FE")


    ChrTalk(
        0x102,
        (
            "#00109FHey, Randy.\x01",
            "I think we just told you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FY-Yeah...  \x01",
            "That's just a joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Senior Randy...\x01",
            "You really never learn.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6794")

    SetScenarioFlags(0x14C, 4)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_6AC1")

    label("loc_67A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6946")
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_683B")
    Jump("loc_6885")

    label("loc_683B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_685B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6885")

    label("loc_685B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_687B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6885")

    label("loc_687B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6885")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Uh uh, it appears our match\x01",
            "is postponed then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I don't\x01",
            "know if there will be\x01",
            "another chance or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FUhh, no way.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_6AC1")

    label("loc_6946")

    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_69D7")
    Jump("loc_6A21")

    label("loc_69D7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_69F7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A21")

    label("loc_69F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A17")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A21")

    label("loc_6A17")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A21")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Uh uh, it appears our match\x01",
            "is postponed then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I don't\x01",
            "know if there will be\x01",
            "another chance or not.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    label("loc_6AC1")

    Jump("loc_6BE4")

    label("loc_6AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AE1")
    Call(0, 11)
    Jump("loc_6B29")

    label("loc_6AE1")


    ChrTalk(
        0xFE,
        "Aah, I lost again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, however I'm not\x01",
            "finished with this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B29")

    Jump("loc_6BE4")

    label("loc_6B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6BE4")

    ChrTalk(
        0xFE,
        (
            "I withdrew from coming to\x01",
            "Crossbell for a little while, but...\x01",
            "In the end, I came again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My homeland, Calvard, is not bad but\x01",
            "Crossbell atmosphere is exceptional.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE4")

    TalkEnd(0xFE)
    Return()

    # Function_14_5C1A end

    def Function_15_6BE8(): pass

    label("Function_15_6BE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6C90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C06")
    Call(0, 16)
    Jump("loc_6C8B")

    label("loc_6C06")


    ChrTalk(
        0xFE,
        (
            "Kh, when the disaster settled and\x01",
            "I could come to play the slots,\x01",
            "my old woman marched in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I really made her worry, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_6C8B")

    Jump("loc_7BF6")

    label("loc_6C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6E37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DA7")

    ChrTalk(
        0xFE,
        (
            "Thinking that martial law is anything\x01",
            "special I made light of it and came\x01",
            "to have fun, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "W-Who could've thought to be\x01",
            "involved in such a thing...\x01",
            "It's the gravest mistake of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By now, my old woman will\x01",
            "be probably worried...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6E32")

    label("loc_6DA7")


    ChrTalk(
        0xFE,
        (
            "To think I got involved\x01",
            "in such a thing...\x01",
            "It's the gravest mistake of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By now, my old woman will\x01",
            "be probably worried...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E32")

    Jump("loc_7BF6")

    label("loc_6E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6EB7")

    ChrTalk(
        0xFE,
        (
            "I heard the speech before...\x01",
            "It was something incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Frankly, I don't get\x01",
            "what good there's in it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BF6")

    label("loc_6EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6F5E")

    ChrTalk(
        0xFE,
        (
            "In the raid incident one week ago\x01",
            "we were made savor real dread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I think that it's right in times\x01",
            "like this that we have to cheer up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BF6")

    label("loc_6F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_713B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7077")

    ChrTalk(
        0xFE,
        (
            "It appears that something\x01",
            "terrible is happening in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I couldn't somewhat\x01",
            "calm down at home, I went out, but...\x01",
            "Today, I really have no enthusiasm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's also not good towards my old woman,\x01",
            "so I guess I'll go back home at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7136")

    label("loc_7077")


    ChrTalk(
        0xFE,
        (
            "Because I couldn't somewhat\x01",
            "calm down at home, I went out, but...\x01",
            "Today, I really have no enthusiasm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's also not good towards my old woman,\x01",
            "so I guess I'll go back home at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7136")

    Jump("loc_7BF6")

    label("loc_713B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71D2")

    ChrTalk(
        0xFE,
        (
            "Yesterday I kept piling up losses on losses...\x01",
            "Today, I absolutely intend to get everything back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Watch me now, I'll do iiit!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7BF6")

    label("loc_71D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_72D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_728A")

    ChrTalk(
        0xFE,
        (
            "Ooh!? This now is a hit...\x01",
            "...Wait, it fooled me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gnnnnh...\x01",
            "Why it doesn't come, WHY!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F(Boy oh boy, grandpa\x01",
            "is still passionate, huh.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_72D0")

    label("loc_728A")


    ChrTalk(
        0xFE,
        (
            "Gnnnnh...\x01",
            "Why it doesn't come, WHY!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm a veteran gambler!\x02",
    )

    CloseMessageWindow()

    label("loc_72D0")

    Jump("loc_7BF6")

    label("loc_72D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_741B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7395")

    ChrTalk(
        0xFE,
        (
            "Mrrr, today hits are\x01",
            "quite not coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What am I going to say to my old woman\x01",
            "going home in such a condition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, come out!\x01",
            "Come, come out I say!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7416")

    label("loc_7395")


    ChrTalk(
        0xFE,
        (
            "Mrrr...\x01",
            "What am I going to say to my old woman\x01",
            "going home in such a condition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, come out!\x01",
            "Come, come out I say!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7416")

    Jump("loc_7BF6")

    label("loc_741B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_75A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7503")

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
            "After all, in the first place the story\x01",
            "of paying a part of revenues to the\x01",
            "two major powers is nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Independence is an undoubted right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_759B")

    label("loc_7503")


    ChrTalk(
        0xFE,
        (
            "After all, in the first place the story\x01",
            "of paying a part of revenues to the\x01",
            "two major powers is nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Independence is an undoubted right.\x02",
    )

    CloseMessageWindow()

    label("loc_759B")

    Jump("loc_7BF6")

    label("loc_75A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_78B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77BA")

    ChrTalk(
        0xFE,
        (
            "This morning, my old woman\x01",
            "was smiling daringly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I asked why she was, she\x01",
            "said that I'd have found it out soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like she took away\x01",
            "my wallet contents without\x01",
            "me noticing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00305FHm? Then, grandpa Rikke,\x01",
            "what're you doin' with no mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Is just sitting around bad?\x02",
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
            "#00306FWell...it's not even crowded, \x01",
            "so you aren't doin' something bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_78AD")

    label("loc_77BA")


    ChrTalk(
        0xFE,
        (
            "Since I don't have mira, I can't play...\x01",
            "But I absolutely won't return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That is, yielding here I'd do \x01",
            "what my old woman wishes.\x02",
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

    label("loc_78AD")

    Jump("loc_7BF6")

    label("loc_78B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_796B")

    ChrTalk(
        0xFE,
        (
            "Society is excited about the\x01",
            "unveiling ceremony, but I, in\x01",
            "any case, will hit the slots here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My old woman is having tea with\x01",
            "her friends at her own discretion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BF6")

    label("loc_796B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7AD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A7C")

    ChrTalk(
        0x104,
        (
            "#00300FHi, grandpa Rikke.\x01",
            "Have you been doin' well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ho ho, that voice...is it Randy?\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can see, I'm well\x01",
            "and I'm in a big fever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you get it, don't interrupt!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHa ha, sorry 'bout that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_7ACC")

    label("loc_7A7C")


    ChrTalk(
        0xFE,
        "I'm at a good point now, don't interrupt me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Ooh, it's come again!\x02",
    )

    CloseMessageWindow()

    label("loc_7ACC")

    Jump("loc_7BF6")

    label("loc_7AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7B7E")

    ChrTalk(
        0xFE,
        (
            "My old woman can say whatever\x01",
            "she wants, but I've got no intention\x01",
            "at all to stop gambling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This too is the fate a gambler\x01",
            "is born with, hoh hoh ho.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BF6")

    label("loc_7B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7BF6")

    ChrTalk(
        0xFE,
        (
            "Hoh hoh, today too I'm\x01",
            "doing good at the slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sound of tinkling medals\x01",
            "is a wonderful feeling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BF6")

    TalkEnd(0xFE)
    Return()

    # Function_15_6BE8 end

    def Function_16_7BFA(): pass

    label("Function_16_7BFA")

    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "Really you, I swear...\x01",
            "Why aren't you coming home!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Come now, let's go back quickly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "W-Wait, woman.\x01",
            "I'll at least exchange these coins...\x02",
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
        "No way, for Goddess' sake!!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_16_7BFA end

    def Function_17_7CE7(): pass

    label("Function_17_7CE7")


    ChrTalk(
        0x104,
        (
            "#00300FHi, grandpa Rikke.\x01",
            "How're you doin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Ahn? That voice...Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Recently you don't show up, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FWell, I've been a little busy with work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I right because you're busy that you play.\x01",
            "Don't you understand that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHa ha, indeed, that could be the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Damn old woman, this morning she was\x01",
            "laying in ambush before the entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "She lifted her eyebrows and cried in a thundering voice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I was almost on the verge of being brought back.\x01",
            "*phew*, it was really a close call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No matter how much Crossbell changes,\x01",
            "only the Entertainment District won't disappear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Bars, gambling houses, the girls\x01",
            "who swarm at the many customers㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even if their shapes mutate, nothing\x01",
            "has really changed from the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Incidentally, they're also the places\x01",
            "with a tiny bit poor public security.\x01",
            "An amateur has to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_17_7CE7 end

    def Function_18_805C(): pass

    label("Function_18_805C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8071")
    Call(0, 16)
    Jump("loc_8101")

    label("loc_8071")


    ChrTalk(
        0xFE,
        (
            "Honestly, this man...\x01",
            "I wonder if he's thinking about\x01",
            "how much he made me worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...For the present, his spending money will be zero.\x02",
    )

    CloseMessageWindow()

    label("loc_8101")

    TalkEnd(0xFE)
    Return()

    # Function_18_805C end

    def Function_19_8105(): pass

    label("Function_19_8105")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, if red and red came, I thought\x01",
            "that the next one would've been black...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I guess that gambling can't\x01",
            "be dealt with by ordinary methods.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_8105 end

    def Function_20_81AA(): pass

    label("Function_20_81AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8295")

    ChrTalk(
        0xFE,
        (
            "I thought it could've been good for\x01",
            "relaxing and I came along with Gantz, but..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems it would be better to go back ahead\x01",
            "of time and to consult with the Town Mayor\x01",
            "and the others about future activities.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82EF")

    label("loc_8295")


    ChrTalk(
        0xFE,
        (
            "Ha ha, that's why you should've\x01",
            "quitted at that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gantz, you're\x01",
            "too greedy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82EF")

    TalkEnd(0xFE)
    Return()

    # Function_20_81AA end

    def Function_21_82F3(): pass

    label("Function_21_82F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8398")

    ChrTalk(
        0xFE,
        (
            "To think that when I came\x01",
            "to Crossbell such a terrible\x01",
            "thing happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*, it's the casino I longed\x01",
            "for but I'm not in the mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83EF")

    label("loc_8398")


    ChrTalk(
        0xFE,
        (
            "Aah, crap...!\x01",
            "I was winning after a long time,\x01",
            "and it's already gone up in smoke!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83EF")

    TalkEnd(0xFE)
    Return()

    # Function_21_82F3 end

    def Function_22_83F3(): pass

    label("Function_22_83F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84EF")

    ChrTalk(
        0xFE,
        (
            "Society is making a fuss over the\x01",
            "independence question, but...\x01",
            "Jeez, they're all fools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Crossbell fawns upon the\x01",
            "Republic like until now and\x01",
            "obeys, it'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doing so, it will be\x01",
            "promised peace.\x01",
            "Eh eh eh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_85AB")

    label("loc_84EF")


    ChrTalk(
        0xFE,
        (
            "Well, if the independence is realized or not, \x01",
            "it doesn't have anything to do with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh eh, we'll just drain the cup of pleasure to the\x01",
            "dregs as much as possible in this city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85AB")

    TalkEnd(0xFE)
    Return()

    # Function_22_83F3 end

    def Function_23_85AF(): pass

    label("Function_23_85AF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Eh eh, don't push yourself too much, Yuri.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you win too much, we could\x01",
            "get the banishment treatment.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_85AF end

    def Function_24_8627(): pass

    label("Function_24_8627")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The woman sit over there\x01",
            "is quite the beauty, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Refusing our invite...\x01",
            "She doesn't have a good eye, I say.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_8627 end

    def Function_25_86A6(): pass

    label("Function_25_86A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8819")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86C8")
    TalkEnd(0xFE)
    Call(0, 26)
    Return()

    label("loc_86C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8796")

    ChrTalk(
        0x15,
        (
            "#03500FWell then, after a little bit more \x01",
            "I guess I'll go back to the Empire.\x02\x03",
            "#03504FI also have to help that\x01",
            "slightly bad bearded old man...\x01",
            "Oh boy, being a reliable guy is tough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8819")

    label("loc_8796")


    ChrTalk(
        0x15,
        (
            "#03500FWell then, after a little bit more \x01",
            "I guess I'll go back to the Empire.\x02\x03",
            "#03504FOh boy, being a reliable guy is tough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8819")

    TalkEnd(0xFE)
    Return()

    # Function_25_86A6 end

    def Function_26_881D(): pass

    label("Function_26_881D")

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
        "#11P#03502FHiya, thank you for all your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FM-Mr. Lechter...\x01",
            "You're again at the casino in such an outfit...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89A8")

    ChrTalk(
        0x105,
        "#10402FHu hu, he's greatly relaxed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A23")

    label("loc_89A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89E1")

    ChrTalk(
        0x109,
        "#10106FHe's greatly relaxed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A23")

    label("loc_89E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A23")

    ChrTalk(
        0x106,
        (
            "#10702FIt looks like he's\x01",
            "greatly relaxed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A23")


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
            "#11P#03506FWell, while fighting a "magic soldier"\x01",
            "they ended up ripped and torn.\x02\x03",
            "#03509FWell, don't mind it and relax!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FR-Right...\x02\x03",
            "#00000F*cough*, hmm....\x01",
            "Thank you very much for your cooperation\x01",
            "to the liberation plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FReally, thank you very much for\x01",
            "the Orchis Tower breaking into...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03504FHa ha, don't sweat it.\x01",
            "I too did what I like.\x02\x03",
            "#03502FBecause I have been doing nothing\x01",
            "but secretary desk work, honestly\x01",
            "it was some good exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FYour job should be the intelligence spy...\x01",
            "But you fought around that much.\x02\x03",
            "#00301FAt any rate, Miss Kilika aside,\x01",
            "to think that you were concealin'\x01",
            "that much fightin' abilities...\x02\x03",
            "Those fencing and high level Arts...\x01",
            "That's no stuff an amateur could\x01",
            "handle in a brief amount of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03510FHm, if you want to know about it\x01",
            "that much, I guess I'll tell you.\x02\x03",
            "#03504FSee, it was 30 years ago...\x01",
            "Those were taught to me by a hermit who leaves \x01",
            "in the depths of a certain mountain of the Empire.\x02",
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
            "#6P#00006F...It sounds plainly false\x01",
            "since the beginning of it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F7B")

    ChrTalk(
        0x10A,
        "#00603F(My...what a tough customer to deal with.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_9003")

    label("loc_8F7B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FC7")

    ChrTalk(
        0x109,
        "#10106FAs you can imagine, it's too inadequate...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9003")

    label("loc_8FC7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9003")

    ChrTalk(
        0x105,
        "#10409FAhaha, it's extremely unlikely.\x02",
    )

    CloseMessageWindow()

    label("loc_9003")


    ChrTalk(
        0x15,
        (
            "#11P#03504FWell, I leave that to your imagination\x01",
            "to best suit your needs.\x02\x03",
            "#03510F...Well then, it's time for me\x01",
            "to go back to the Empire too.\x02\x03",
            "#03506FI also have to help that\x01",
            "slightly bad bearded old man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00205FThe "Blood and Iron Chancellor"...\x01",
            "If I remember correctly he was \x01",
            "shot and went missing.\x02\x03",
            "#00203FThe Noble Alliance took advantage\x01",
            "of the opening caused by the big beating\x01",
            "the regular army received by that "Aion"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03510FYeah, it seems that the capital has been\x01",
            "occupied by those nobles completely.\x02\x03",
            "#03506FWell, at any rate he's an old man who\x01",
            "easily gains unjustified resentment.\x01",
            "Even us who protect him have become used to that.\x02\x03",
            "#03500FWell, being who he is, that old\x01",
            "man won't drop dead easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FSomehow you're takin' it so easy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03509FHa ha, and what about you?\x02\x03",
            "#03504FOld man Giliath or the Noble Alliance.\x01",
            "No matter who wins...\x02\x03",
            "#03502FI think that Crossbell destiny is\x01",
            "not going to change in the future.\x02",
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
            "#00001FHowever, more than anything else...\x01",
            "First of all, I intend to head to\x01",
            "that "huge tree" to get KeA back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03504F...Ha ha, that's good.\x02\x03",
            "It's important to gaze at the future, but\x01",
            "if you perceive only that, you'll trip up.\x01\x02\x03",
            "#03500FWhat's most important is\x01",
            "the "now" in front of you.\x02",
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
            "#6P#00006FE-Even if you suddenly said a proper thing,\x01",
            "somehow it's bewildering, but...\x02\x03",
            "#00000F...Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03502FHa ha, well, at least try\x01",
            "to give it your all.\x02\x03",
            "#03509FIf you don't do that, it won't \x01",
            "be worthy for me to have\x01",
            "stayed behind on purpose.\x02",
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

    # Function_26_881D end

    def Function_27_97EE(): pass

    label("Function_27_97EE")

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
            "Quit\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_987F")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_987F")

    TalkEnd(0xFF)
    Return()

    # Function_27_97EE end

    def Function_28_9883(): pass

    label("Function_28_9883")

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
            "#5P...Could it be that you\x01",
            "have come for Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYes...\x01",
            "Like we thought, has he been here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, at about three in the dead of night\x01",
            "he casually came in the establishment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAfter drinking here for a while,\x01",
            "he went back, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206F...It seems he came\x01",
            "directly here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#12PThen, after that did he say\x01",
            "where he was going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...As I suspected, it appears he\x01",
            "didn't go back to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, he didn't say where he\x01",
            "was going in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, somehow, when he was drinking\x01",
            "he was impudently talking more than usual...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn addition, when he went back he\x01",
            "retrieved from me a certain something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FA certain...something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes...a quite heavy trunk.\x01",
            "I don't know its content.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PRandy entrusted it to me two years ago,\x01",
            "when he had just arrived in this city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe said: "If I were to die, tear it in pieces\x01",
            "and dispose of it at the scrapyard."\x02",
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
        "#12P#10108F...Senior Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00206F...Too much unlike him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00008F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...I too know that guy's personal\x01",
            "history to a certain degree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, I don't know up to what\x01",
            "has happened in his past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou all are probably the only ones\x01",
            "who know that and can help him.\x02",
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
            "#12P#00004F...Yes.\x01",
            "We will do that.\x02",
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

    # Function_28_9883 end

    def Function_29_9ED9(): pass

    label("Function_29_9ED9")

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
            "#03506FWhat the heck, Dogi again?\x02\x03",
            "#03501FOnce in awhile if a Feena doesn't\x01",
            "come out too, it's boring.\x02",
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
            "#00013F#12P──Mr. Lechter.\x01",
            "You can't escape anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PPlease give up already and\x01",
            "disclose your identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03503F#5PMy identity, eh...\x02\x03",
            "#03510FIdentity, identity...\x01",
            "Which one would be good, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P...Please don't try to\x01",
            "plainly deceive us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03504FOh, right...\x02\x03",
            "#03500FAsk me whatever you want\x01",
            "and I'll reply with a yes or no.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12P...I understand.\x01",
            "Then, allow me to question you.\x02\x03",
            "#00001F──You are Mr. Lechter Arundel,\x01",
            "the Imperial government second\x01",
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
            "#00013F#12PAre you a special captain attached\x01",
            "to the Imperial Army Intelligence Division?\x02",
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
        "#00008F#12P(He's easily admitting it...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6P...Then, I'll ask too.\x02\x03",
            "#00101FAbout your current visit, is it something you\x01",
            "officially accepted from the Imperial government?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)
    Sleep(300)

    ChrTalk(
        0x15,
        "#03501FYes, but also no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PDo you intend to sojourn\x01",
            "here for more than one month?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03504FHu hu...\x02\x03",
            "#03502FThe answer is no.\x01",
            "I'll go back in about one week.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A606():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A606)
    Sleep(100)

    def lambda_A616():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A616)
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
            "#00108F(Yes...\x01",
            "We can't ask more than this.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A67E():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A67E)
    Sleep(50)

    def lambda_A68E():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A68E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00003F#12P──Sorry to have troubled you,\x01",
            "Captain Arundel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#6PThank you for your collaboration.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Sleep(200)

    ChrTalk(
        0x15,
        (
            "#03506FYeah, it was nothing.\x02\x03",
            "#03505FOh, by the way, is that kiddo ok?\x01",
            "You took her in, right?\x02",
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
            "#00005F#12PHmm, are you talking about KeA?\x02\x03",
            "#00012FYes, thank goodness she's\x01",
            "living totally fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6P...Thank you very much for\x01",
            "what you did on that occasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PHu hu, you helped\x01",
            "us escape, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03504FHmm, what're you talking about?\x01",
            "I was just playing with Blackie.\x02\x03",
            "#03502FBy the way, old man Hartmann, they\x01",
            "say he was arrested in the end?\x02\x03",
            "Well, strange to say, he was been ferried\x01",
            "around, so I'm glad you captured him safely.\x02",
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
        "#00001F#12P...How do you know even that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PThree days didn't even pass since\x01",
            "those two were arrested, and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03503FWell, confirming that too was one\x01",
            "of the motives why I came here.\x02\x03",
            "#03501FAnd one of the others is──\x02",
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
        "#3936V#1P#30WAh, there you're!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "Young Girl's Voice",
        "#3937V#1P#30WWhat're you doing in this place?\x02",
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

    def lambda_AC9B():
        OP_93(0x101, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC9B)

    def lambda_ACA8():
        OP_93(0x102, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACA8)

    def lambda_ACB5():
        OP_93(0x109, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ACB5)

    def lambda_ACC2():
        OP_93(0x105, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ACC2)
    SetChrPos(0x15, 6540, 4270, 13420, 180)
    OP_68(5340, 5500, 12170, 6000)
    MoveCamera(130, 18, 0, 6000)
    OP_6E(400, 6000)
    SetCameraDistance(22330, 6000)

    def lambda_AD0E():
        OP_9B(0x0, 0x16, 0x0, 0x36B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_AD0E)
    Sleep(2000)

    def lambda_AD26():

        label("loc_AD26")

        TurnDirection(0x101, 0x16, 500)
        Yield()
        Jump("loc_AD26")

    QueueWorkItem2(0x101, 1, lambda_AD26)
    Sleep(50)

    def lambda_AD3B():

        label("loc_AD3B")

        TurnDirection(0x105, 0x16, 500)
        Yield()
        Jump("loc_AD3B")

    QueueWorkItem2(0x105, 1, lambda_AD3B)
    OP_6F(0x1)
    WaitChrThread(0x16, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x105, 0x1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x16,
        (
            "#04601F#3970V#11P#30WYou got arranged tickets for\x01",
            "the Arc-en-ciel for me, right?\x02\x03",
            "#3971VSo, what happened to those?\x02",
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
            "#03509F#6PHm, I secured special guests seats\x01",
            "for today's evening performance.\x02\x03",
            "Be very grateful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#04602F#11PReally!?\x02\x03",
            "#04612FEheheh, thanks!\x01",
            "I wanted to see them since before!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P(...Who is she...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6P(It looks like she's still young...)\x02",
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
        "#00012F#5PEhm...what is it?\x02",
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
            "Eeeeh...\x01",
            "Mister, you smell of...\x02\x03",
            "...A nostalgic smell.\x02",
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
        "#00011F#5P!!!????\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00111F#6PH-Hey!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#6PE-EEEEH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#12P*pheew*♪\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_9B(0x1, 0x16, 0xB4, 0x1F4, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        "#00007F#5PW-What're you doing all of a sudden...!?\x02",
    )

    CloseMessageWindow()
    SetChrName("Redheaded Girl")

    ChrTalk(
        0x16,
        (
            "#04612F#11PEheheh, thanks for the food㈱\x02\x03",
            "#04602FYes, as I thought,\x01",
            "you smell slightly.\x02\x03",
            "Although I can't sense any\x01",
            "smell from the two over there...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x16, 0x0, 0x1F4)

    ChrTalk(
        0x16,
        (
            "#04605F#11P──Ah!\x01",
            "Miss, just a tiny bit, eh!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PEh...\x02",
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
        "#00115F#3391V#4S#5PEEEEEEK!?\x02",
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
        "#10111F#5PWhen did she move behind her?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x16,
        (
            "#04611F#3938V#5P#30WMiss, these are big, eh?\x02\x03",
            "#04609F#3939VSince Shirley's as flat as\x01",
            "a washboard, she's envious㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF63)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00112F#3392V#5P#40WH-Hey, stop it...!\x01\x02\x03",
            "#00113F#3393VAahun...!\x01",
            "W-Why are you...!\x02",
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
        "#10309F#6PAhaha, nice spectacle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PI-Indeed...no!\x02\x03",
            "#00007FHey, you!\x01",
            "What're doing all of a sudden!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03509FHa ha, you'd want to do that as much as you could.\x02\x03",
            "#03502FBut if you do it more than that, it'll turn\x01",
            "into sexual harassment, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#04605F#5PIt's not sexual harassment.\x01",
            "It's skinship, you see.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00107F#5P#4SI-It's totally sexual harassment!\x02",
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

    def lambda_B7FF():
        OP_9B(0x1, 0x16, 0x87, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_B7FF)
    Sound(802, 0, 100, 0)
    OP_A1(0x102, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)

    def lambda_B826():
        OP_99(0x101, 0x102, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B826)
    Sleep(50)

    def lambda_B83D():
        OP_99(0x109, 0x102, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B83D)
    Sleep(500)

    ChrTalk(
        0x102,
        "#5P#00113F*pant pant pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#5PM-Miss Elie.\x02",
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
            "#03510F#5PHm, well then,\x01",
            "we'll excuse us.\x02\x03",
            "#03509FLet's go to Michelam Theme Park\x01",
            "to have a blast until night.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x16,
        "Shirley",
        "#04612F#3940V#5P#30WThen, see ya!\x02",
    )

    CloseMessageWindow()
    OP_24(0xF64)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_68(4780, 5500, 11560, 3000)
    OP_93(0x15, 0xE1, 0x0)

    def lambda_B9AD():
        OP_96(0x15, 0x1662, 0xFA0, 0x29FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B9AD)
    OP_95(0x16, 4740, 4000, 12780, 2000, 0x0)

    def lambda_B9DB():
        OP_95(0x15, 4740, 4000, 4480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B9DB)
    OP_95(0x16, 5730, 4000, 11500, 2000, 0x0)

    def lambda_BA09():
        OP_93(0x101, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA09)

    def lambda_BA16():
        OP_93(0x105, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BA16)
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
        "#00013F#5PW-What was that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PI-In the end we\x01",
            "let him go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHu hu, what an intense kid, eh?\x02\x03",
            "#10309F15 o 16 years old, maybe?\x01",
            "Quite the good job she did.\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x2, 0x3, 0x4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00107F#5P#4SNo she didn't!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x8, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0x8, 0x7)

    ChrTalk(
        0x102,
        (
            "#00106F#5P#30WUuuh...\x01",
            "Why did I have to suffer that...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#00012F#11PUhhm...that was unfortunate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5PW-Well, you're both women so you\x01",
            "don't have to be so serious about it...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x109, 500)

    ChrTalk(
        0x105,
        (
            "#10305F#12PAlso, you're used to get them fondled\x01",
            "by Miss Mariabell, am I not right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x4, 0x7, 0xA, 0xB, 0xC)
    Sleep(100)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00115F#5P#5SI-I'm not used to that!\x02",
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
            "Afterwards, Lloyd and the others returned\x01",
            "to police HQ and called Section One...\x02\x03",
            "In conjunction with the Heiyue movements,\x01",
            "they reported about Lechter too.\x07\x00\x02",
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

    # Function_29_9ED9 end

    def Function_30_BDF1(): pass

    label("Function_30_BDF1")


    def lambda_BDF6():
        OP_95(0x101, 5030, 4000, 10490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDF6)
    WaitChrThread(0x101, 1)

    def lambda_BE14():
        OP_95(0x101, 6540, 4000, 11860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE14)
    WaitChrThread(0x101, 1)

    def lambda_BE32():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE32)
    Return()

    # Function_30_BDF1 end

    def Function_31_BE3B(): pass

    label("Function_31_BE3B")


    def lambda_BE40():
        OP_95(0x102, 5500, 4000, 9870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE40)
    WaitChrThread(0x102, 1)

    def lambda_BE5E():
        OP_95(0x102, 5520, 4000, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE5E)
    WaitChrThread(0x102, 1)

    def lambda_BE7C():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE7C)
    Return()

    # Function_31_BE3B end

    def Function_32_BE85(): pass

    label("Function_32_BE85")


    def lambda_BE8A():
        OP_95(0x109, 4810, 4000, 13910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BE8A)
    WaitChrThread(0x109, 1)

    def lambda_BEA8():
        OP_95(0x109, 5530, 4000, 14790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BEA8)
    WaitChrThread(0x109, 1)

    def lambda_BEC6():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BEC6)
    Return()

    # Function_32_BE85 end

    def Function_33_BECF(): pass

    label("Function_33_BECF")


    def lambda_BED4():
        OP_95(0x105, 4800, 4000, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BED4)
    WaitChrThread(0x105, 1)

    def lambda_BEF2():
        OP_95(0x105, 4740, 4000, 10780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BEF2)
    WaitChrThread(0x105, 1)

    def lambda_BF10():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BF10)
    Return()

    # Function_33_BECF end

    def Function_34_BF19(): pass

    label("Function_34_BF19")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9F(0x0, 0x16)
    OP_9F(0x1, 4740, 4000, 12360)
    OP_9F(0x1, 4740, 4000, 13900)
    OP_9F(0x1, 5520, 4000, 13900)
    OP_9F(0x2, 0x16, 8000, 0x6)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0x16, 0xB4, 0x0)
    Return()

    # Function_34_BF19 end

    def Function_35_BF68(): pass

    label("Function_35_BF68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF88")
    Sound(888, 0, 70, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_35_BF68")

    label("loc_BF88")

    Return()

    # Function_35_BF68 end

    def Function_36_BF89(): pass

    label("Function_36_BF89")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BFA9")
    Sound(888, 0, 70, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x3, 0x4, 0x5, 0x4)
    Jump("Function_36_BF89")

    label("loc_BFA9")

    Return()

    # Function_36_BF89 end

    SaveToFile()

Try(main)
