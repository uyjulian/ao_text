from ScenarioHelper import *

def main():
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
        "Drake owner",     # 1
        "cherry",               # 2
        "Galetti",             # 3
        "Elinde",               # 4
        "Laterarossa",           # 5
        "Ricci grandfather",           # 6
        "Holy grandfather",           # 7
        "tourist",                 # 8
        "Miners Mallo",             # 9
        "Miner Gantz",             # 10
        "Yuri",                 # 11
        "Sykes",               # 12
        "Reggie",                 # 13
        "Rector",               # 14
        "Redhead girl",             # 15
        "Redhead girl",             # 16
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
        "Function_5_228F",         # 05, 5
        "Function_6_288F",         # 06, 6
        "Function_7_2893",         # 07, 7
        "Function_8_3727",         # 08, 8
        "Function_9_375C",         # 09, 9
        "Function_10_3760",        # 0A, 10
        "Function_11_454B",        # 0B, 11
        "Function_12_45EE",        # 0C, 12
        "Function_13_45F2",        # 0D, 13
        "Function_14_52A2",        # 0E, 14
        "Function_15_60EE",        # 0F, 15
        "Function_16_6F29",        # 10, 16
        "Function_17_701B",        # 11, 17
        "Function_18_72B5",        # 12, 18
        "Function_19_733A",        # 13, 19
        "Function_20_73B7",        # 14, 20
        "Function_21_74AE",        # 15, 21
        "Function_22_7588",        # 16, 22
        "Function_23_76F5",        # 17, 23
        "Function_24_7765",        # 18, 24
        "Function_25_77DA",        # 19, 25
        "Function_26_7918",        # 1A, 26
        "Function_27_86EB",        # 1B, 27
        "Function_28_8782",        # 1C, 28
        "Function_29_8D63",        # 1D, 29
        "Function_30_AAFD",        # 1E, 30
        "Function_31_AB47",        # 1F, 31
        "Function_32_AB91",        # 20, 32
        "Function_33_ABDB",        # 21, 33
        "Function_34_AC25",        # 22, 34
        "Function_35_AC74",        # 23, 35
        "Function_36_AC95",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B07")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "…… Randy, you are\x01",
            "You're going to that \"big tree\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYou know well.\x01",
            "As expected it is a Drake owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huun, I also have a relationship with you\x01",
            "It is not short.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Randy, to you\x01",
            "The price for drinking in Tsukue\x01",
            "I still have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With absolutely returning home safely,\x01",
            "Do not understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F… Ah, I understand.\x02\x03",
            "#00309FI will return it soon\x01",
            "I feel relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Hello …… these two people\x01",
            "I guess there is something to communicate with. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 0)
    Jump("loc_CB8")

    label("loc_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C38")

    ChrTalk(
        0x8,
        (
            "Now it is time for a trial to crossbell\x01",
            "It may be visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Everyone, please Randy\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That guy so far\x01",
            "The price for drinking with Takeo,\x01",
            "I still have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FWell, please leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FI will return it soon\x01",
            "I feel relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CB8")

    label("loc_C38")


    ChrTalk(
        0x8,
        (
            "Now it is time for a trial to crossbell\x01",
            "It may be visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Everyone, please Randy\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB8")

    Jump("loc_228B")

    label("loc_CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E72")

    ChrTalk(
        0x8,
        "Oh, this is everyone ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIt's been a while, owner.\x01",
            "Was not she supposed to be doing fine?\x02",
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
            "Resistance activity in Mainz\x01",
            "I heard that I was throwing myself,\x01",
            "I seemed to be able to join with my colleagues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHere\x01",
            "Have not been damaged?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "Yeah, for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if you are around the city\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FOh, I see that too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 7)
    Jump("loc_FD5")

    label("loc_E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F48")

    ChrTalk(
        0x8,
        (
            "However, from martial law\x01",
            "I was shrinking my business and was correct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If this small number of people is also a store stockpile\x01",
            "It will last for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please do not worry about this.\x01",
            "Everyone in your work\x01",
            "Please be advised.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD5")

    label("loc_F48")


    ChrTalk(
        0x8,
        (
            "If this small number of people is also a store stockpile\x01",
            "It will last for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please do not worry about this.\x01",
            "Everyone in your work\x01",
            "Please be advised.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD5")

    Jump("loc_228B")

    label("loc_FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1150")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C2")

    ChrTalk(
        0x8,
        (
            "Hmm … … Unfamiliar from the morning\x01",
            "If you think that there are people wearing uniforms,\x01",
            "Is that a military soldier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Very much\x01",
            "It is a feeling of being ready … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Croix has been around since\x01",
            "In this scenario\x01",
            "Have you imagined it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_114B")

    label("loc_10C2")


    ChrTalk(
        0x8,
        (
            "Still, from that referendum vote\x01",
            "Although it has been only a week … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Croix has been around since\x01",
            "In this scenario\x01",
            "Have you imagined it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114B")

    Jump("loc_228B")

    label("loc_1150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EE")

    ChrTalk(
        0x8,
        (
            "Oh, Randy.\x01",
            "Well do not understand, but something\x01",
            "It's a blown face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The shop is in this situation\x01",
            "Although the birds are chirping,\x01",
            "What on earth are you going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F, Separately everywhere\x01",
            "Do you think it will change?\x02\x03",
            "#00309FOkay, owner, I was a bit\x01",
            "Because I did not appear on the store\x01",
            "Do you miss as soon as possible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hun, you say fool.\x01",
            "There was nothing to say,\x01",
            "On the contrary, it was something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, to you so far\x01",
            "I have lent you various monks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Until we finish returning all of them,\x01",
            "You are not going to buckle arbitrarily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYou know, even if you are not told.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(These two people, at anything\x01",
            "You are on good terms. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F(Yeah, like a child.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 1)
    Jump("loc_147D")

    label("loc_13EE")


    ChrTalk(
        0x8,
        (
            "Anyway Randy,\x01",
            "I have made various monkeys to you\x01",
            "Do not forget what you have lent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There is no particular deadline,\x01",
            "I will be sure to return it someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147D")

    Jump("loc_228B")

    label("loc_1482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_15FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1572")

    ChrTalk(
        0x8,
        (
            "What I can do is\x01",
            "At most a place to drink\x01",
            "To give a degree … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But if you guys\x01",
            "In the true sense I can become the force of the guy,\x01",
            "It feels like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, about Randy ….\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15F7")

    label("loc_1572")


    ChrTalk(
        0x8,
        (
            "If you are\x01",
            "In the true sense I can become the force of the guy,\x01",
            "It feels like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, about Randy ….\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F7")

    Jump("loc_228B")

    label("loc_15FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_177B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E1")

    ChrTalk(
        0x8,
        (
            "It is time tomorrow is finally here.\x01",
            "Renewal It is the release date of the stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On anything the next stage\x01",
            "Next to that Lisha Mao\x01",
            "A big newcomer makes his debut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huh, the topic of alkane shell\x01",
            "You always entertain us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1776")

    label("loc_16E1")


    ChrTalk(
        0x8,
        (
            "On anything the next stage\x01",
            "Next to that Lisha Mao\x01",
            "A big newcomer makes his debut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huh, the topic of alkane shell\x01",
            "You always entertain us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1776")

    Jump("loc_228B")

    label("loc_177B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_18E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1859")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "Welcome to the casino house \"Barca\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you want to rest your head, please here\x01",
            "Please use the bar counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alcohol and of course,\x01",
            "You can also serve coffee etc?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18E1")

    label("loc_1859")


    ChrTalk(
        0x8,
        (
            "When you want to rest your head, please here\x01",
            "Please use the bar counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alcohol and of course,\x01",
            "You can also serve coffee etc?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E1")

    Jump("loc_228B")

    label("loc_18E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1AC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A12")

    ChrTalk(
        0x8,
        (
            "Is it the right of state independence, … ….\x01",
            "While the powerful figure of the back society is still busy,\x01",
            "This problem is ridiculous again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The results of the referendum will move to something immediately\x01",
            "I can not imagine it will be connected … …\x01",
            "The problem is the trend of the two biggest countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do not do it well, Crosbell's position is\x01",
            "I do not get any worse than I do now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ABB")

    label("loc_1A12")


    ChrTalk(
        0x8,
        (
            "The results of the referendum will move to something immediately\x01",
            "I can not imagine it will be connected … …\x01",
            "The problem is the trend of the two biggest countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do not do it well, Crosbell's position is\x01",
            "It can be worse than it is now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABB")

    Jump("loc_228B")

    label("loc_1AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B4A")

    ChrTalk(
        0x8,
        (
            "Hmm, somewhat somewhat\x01",
            "It seems noisy on the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it seems to be noisy any more,\x01",
            "It is a place I would like you to withdraw … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228B")

    label("loc_1B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1BD2")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "Welcome to the casino house \"Barca\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My body and mind will melt …\x01",
            "How about a sweet cocktail?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228B")

    label("loc_1BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C47")

    ChrTalk(
        0x8,
        (
            "The unveiling ceremony of Orkis Tower\x01",
            "It looks like it ended well in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Huh, I'm looking forward to see it later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_228B")

    label("loc_1C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E43")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Oh, Randy.\x01",
            "Have you already gone out of yesterday's sake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa, of course.\x01",
            "This I got such a stingy amount of liquor\x01",
            "Did you think you would leave it the next day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hun, you as usual\x01",
            "It is a person whose mouth is decreasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even with celebration return,\x01",
            "You did not give me a treat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHello, sorry.\x01",
            "But I'm grateful.\x02\x03",
            "#00300FThat's why owner,\x01",
            "I will ask if there is another opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hun, do not say husband.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Randy, that's right\x01",
            "She seems to have been showing her face. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(Oh, I see.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    SetScenarioFlags(0x14C, 2)
    Jump("loc_1F69")

    label("loc_1E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF7")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Well, I gotta give it back.\x01",
            "Cure that decrease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's right\x01",
            "There is nothing to think about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FEducation\x01",
            "Well let's do.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F69")

    label("loc_1EF7")

    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Well, I gotta give it back.\x01",
            "Cure that decrease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's right\x01",
            "There is nothing to think about.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)

    label("loc_1F69")

    Jump("loc_228B")

    label("loc_1F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F89")
    Call(0, 5)
    Jump("loc_21E5")

    label("loc_1F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212B")

    ChrTalk(
        0x8,
        (
            "Recently, instead of Rubache\x01",
            "A small thing that brings an overhead fee\x01",
            "It came to appear now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have not done it now,\x01",
            "If this situation continues, it will be various\x01",
            "It will be troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Whew, as soon as it can be anywhere\x01",
            "A section of the remains of Rubathe\x01",
            "I want you to take over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F(The influence that Rubache is gone\x01",
            "Also in these places ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(It also kept it confusingly\x01",
            "I guess it is one place in order. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21E5")

    label("loc_212B")


    ChrTalk(
        0x8,
        (
            "Right now, the guys are relatively comparable\x01",
            "I seem to be doing quietly, but …\x01",
            "It is troublesome if this situation continues to flowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Whew, as soon as it can be anywhere\x01",
            "A section of the remains of Rubathe\x01",
            "I want you to take over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E5")

    Jump("loc_228B")

    label("loc_21EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_228B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2205")
    Call(0, 5)
    Jump("loc_228B")

    label("loc_2205")


    ChrTalk(
        0x8,
        (
            "Randy's guy got mixed in the guard\x01",
            "Does it work well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huff, do something miserable like the old days\x01",
            "I wish I had not said that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_228B")

    TalkEnd(0x8)
    Return()

    # Function_4_90A end

    def Function_5_228F(): pass

    label("Function_5_228F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Everyone at the Special Affairs Division … …\x01",
            "Besides, she is not Mr. Wasji.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Anyway, it is an unusual combination.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh, the owner.\x01",
            "Actually this time, to the Special Affairs Support Division\x01",
            "It is decided to be assigned.\x02\x03",
            "I omit the details, but one in the future\x01",
            "I'm begging for you with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Indeed, was that so …?\x01",
            "Haha, I got it somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FOh, you accept it easily.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat's true, though …\x01",
            "Wadi, like natural\x01",
            "You know acquainted with the owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, for the host\x01",
            "Around here including the casino\x01",
            "It's like a workplace.\x02\x03",
            "#10300FConversely with the Drake owner\x01",
            "I do not know a host I do not know\x01",
            "Is not it a moguri or a trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FSay anything …\x02\x03",
            "#10101FAlmost, at that age\x01",
            "To play around in this area\x01",
            "It's a bad thing.\x02\x03",
            "#10103FOn this occasion a little ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, it's tough as ever.\x02\x03",
            "Well, that kind of place\x01",
            "I think it is one of your charms, but a spout\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2619")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2619")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_263F")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_263F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2665")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2665")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_268B")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_268B")

    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10106FHa, what anymore\x01",
            "Everything is getting better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FI understand, that feeling.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 7)
    Jump("loc_288E")

    label("loc_26EF")


    ChrTalk(
        0x8,
        (
            "By the way, everyone,\x01",
            "Randy's guy is still\x01",
            "You are not returning, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Before the principal to the guard of the old nest\x01",
            "I heard that I will bring out my face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, for a while\x01",
            "I think we can merge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, well I guess\x01",
            "As I returned it seems to be on the store\x01",
            "Can you tell me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even a bottle of wine for returning celebration\x01",
            "I said I was going to prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FI will tell it properly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 6)

    label("loc_288E")

    Return()

    # Function_5_228F end

    def Function_6_288F(): pass

    label("Function_6_288F")

    Call(0, 7)
    Return()

    # Function_6_288F end

    def Function_7_2893(): pass

    label("Function_7_2893")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3723")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",        # 0
            "To exchange\x01",      # 1
            "quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28FC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_28FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_291B")
    OP_AF(0x41)
    Jump("loc_295D")

    label("loc_291B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_292B")
    OP_AF(0x40)
    Jump("loc_295D")

    label("loc_292B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_293B")
    OP_AF(0x3F)
    Jump("loc_295D")

    label("loc_293B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_294B")
    OP_AF(0x3E)
    Jump("loc_295D")

    label("loc_294B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_295B")
    OP_AF(0x3D)
    Jump("loc_295D")

    label("loc_295B")

    OP_AF(0x3C)

    label("loc_295D")

    Call(0, 8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_371E")

    label("loc_296F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2983")
    Jump("loc_371E")

    label("loc_2983")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_371E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A21")

    ChrTalk(
        0x9,
        (
            "Welcome,\x01",
            "To the casino house \"Valka\" ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I played a lot,\x01",
            "Please blow away the anxiety ☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A8D")

    label("loc_2A21")


    ChrTalk(
        0x9,
        (
            "It is such a time,\x01",
            "I also work as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I played a lot,\x01",
            "Please blow away the anxiety ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A8D")

    Jump("loc_371E")

    label("loc_2A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B3C")

    ChrTalk(
        0x9,
        (
            "Uh, honestly scared ….\x01",
            "Garetti and Elinde\x01",
            "I'm glad it was a holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The owner is working hard,\x01",
            "I must also be firm.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BD9")

    label("loc_2B3C")


    ChrTalk(
        0x9,
        (
            "Garetti and Elinde\x01",
            "Because it is a holiday, I can not play with 1F … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There is something useful for my prize\x01",
            "There may be,\x01",
            "Please do use it as usual!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD9")

    Jump("loc_371E")

    label("loc_2BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C5C")

    ChrTalk(
        0x9,
        (
            "Well, suddenly to war\x01",
            "You do not get it, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Following this, the two major powers\x01",
            "What kind of statements are issued?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CD1")

    ChrTalk(
        0x9,
        "Well, the referendum?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There seems to be several polling stations,\x01",
            "If you go, I guess it's an Orkis Tower ~ ☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D57")

    ChrTalk(
        0x9,
        (
            "Well, crossbell outside the city\x01",
            "Although it is an event, Mainz's things are\x01",
            "It is not other people's affair ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I want you to settle quickly and safely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF4")

    ChrTalk(
        0x9,
        (
            "Alcan Shell 's performance,\x01",
            "At last it will be open tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Surely again, also\x01",
            "A customer will come along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Let's have fun ~ spray\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E4B")

    label("loc_2DF4")


    ChrTalk(
        0x9,
        (
            "I finished watching the alkane shell\x01",
            "There are quite a lot of people coming to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Let's have fun ~ spray\x02",
    )

    CloseMessageWindow()

    label("loc_2E4B")

    Jump("loc_371E")

    label("loc_2E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2EBC")

    ChrTalk(
        0x9,
        (
            "When medals run out\x01",
            "Tell me anytime ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When Mira gone,\x01",
            "Let's go to IBC!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F17")

    ChrTalk(
        0x9,
        "Welcome to \"Valka\" ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uhufu, plenty for today.\x01",
            "Let's play, please ~ ☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2FA0")

    ChrTalk(
        0x9,
        (
            "Those three people,\x01",
            "He seems to be rich, but\x01",
            "It feels awfully bad ~ ne ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was invited from the top with my eyes,\x01",
            "Do you feel like desiring from here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_2FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3024")

    ChrTalk(
        0x9,
        (
            "Trade meeting also today\x01",
            "It's time to start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I do not know well in cherry,\x01",
            "Anyway I want you to go well\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_3024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3129")

    ChrTalk(
        0x9,
        (
            "Mr. Ganz,\x01",
            "Today as well I will not discipline\x01",
            "She seems to be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Tsuki showed up a few months ago\x01",
            "It was about what it was\x01",
            "Hebobo is … but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Gans, maybe\x01",
            "At the time I got lots of luck\x01",
            "Perhaps it's run out?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31CD")

    label("loc_3129")


    ChrTalk(
        0x9,
        (
            "Mr. Gans, maybe\x01",
            "At the time I got lots of luck\x01",
            "Perhaps it's run out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, nevertheless\x01",
            "Because it seems to be a guess\x01",
            "I guess it will not be there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CD")

    Jump("loc_371E")

    label("loc_31D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3456")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33EB")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x104, 0)

    ChrTalk(
        0x9,
        "Oh, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, where have you been lately?\x01",
            "It is not bad, I have to play more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FTotally, evil Cherry.\x02\x03",
            "#00309FThen, immediately round up the work -\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3343")

    ChrTalk(
        0x101,
        "#00009FHey, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHehe, of course it is a joke, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh, ah ……\x01",
            "Well, smiling fearfully, both of us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E3")

    label("loc_3343")


    ChrTalk(
        0x102,
        (
            "#00109FHey, Randy.\x01",
            "I think I said that earlier ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh, ah ……\x01",
            "So it's a joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Randy senior … ….\x01",
            "I really do not understand. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E3")

    SetScenarioFlags(0x14C, 3)
    Jump("loc_3451")

    label("loc_33EB")


    ChrTalk(
        0x9,
        (
            "Randy,\x01",
            "Please show me your bang bang again ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Otherwise,\x01",
            "Cherry I'm bored.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3451")

    Jump("loc_371E")

    label("loc_3456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_34B9")

    ChrTalk(
        0x9,
        (
            "Gimme a grueling rain\x01",
            "Blown away at the casino ~ ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Play with Bang Bang today ~ ne!\x02",
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_34B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_371E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3636")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A8")

    ChrTalk(
        0x9,
        (
            "Suddenly, Flat\x01",
            "Mr. Lecta came\x01",
            "I went up to the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe, I saw it for the first time in a few months,\x01",
            "You are the same as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FLloyd …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FOh, I will not escape this time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3631")

    label("loc_35A8")


    ChrTalk(
        0x9,
        (
            "Suddenly, Flat\x01",
            "Mr. Lecta came\x01",
            "I went up to the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe, I saw it for the first time in a few months,\x01",
            "You are the same as usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3631")

    Jump("loc_371E")

    label("loc_3636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C2")

    ChrTalk(
        0x9,
        "Welcome to \"Valka\" ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Here are medals and\x01",
            "Just like a prize exchange counter\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Playing Bang Bang\x01",
            "Get a good prize ~ ☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_371E")

    label("loc_36C2")


    ChrTalk(
        0x9,
        (
            "Here are medals and\x01",
            "Just like a prize exchange counter\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Playing Bang Bang\x01",
            "Get a good prize ~ ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_371E")

    Jump("loc_28A0")

    label("loc_3723")

    TalkEnd(0x9)
    Return()

    # Function_7_2893 end

    def Function_8_3727(): pass

    label("Function_8_3727")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('垂钓大礼包', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_375B")
    SubItemNumber('垂钓大礼包', 1)
    AddItemNumber('鲑鱼卵', 1)
    AddItemNumber('熬炼丸子', 1)
    AddItemNumber('红虫', 1)
    AddItemNumber('蚯蚓', 1)
    AddItemNumber('熬炼丸子ＤＸ', 1)
    Jump("Function_8_3727")

    label("loc_375B")

    Return()

    # Function_8_3727 end

    def Function_9_375C(): pass

    label("Function_9_375C")

    Call(0, 10)
    Return()

    # Function_9_375C end

    def Function_10_3760(): pass

    label("Function_10_3760")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_376D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4547")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                    # 0
            "Play with poker\x01",              # 1
            "Play with blackjack\x01",      # 2
            "quit\x01",                      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37E4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_37E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3839")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3839")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388E")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_388E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38A2")
    Jump("loc_4542")

    label("loc_38A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4542")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_399C")

    ChrTalk(
        0xA,
        (
            "Mr. Reitarossa regulars\x01",
            "After being returned home,\x01",
            "I am lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The thrilling game with her\x01",
            "Because I was looking forward to everyday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If Crosbell regains peace,\x01",
            "I would like you to come and see me again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A47")

    label("loc_399C")


    ChrTalk(
        0xA,
        (
            "Mr. Reitarossa regular … …\x01",
            "If Crosbell regains peace,\x01",
            "I want you to come and visit again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A big tree that may be such an acquaintance\x01",
            "While it is appearing, it will be difficult, but …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A47")

    Jump("loc_4542")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3A5A")
    Jump("loc_4542")

    label("loc_3A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B58")

    ChrTalk(
        0xA,
        (
            "Today from the morning the driving force train service\x01",
            "It seems to be limited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Empire in crossbell\x01",
            "To the Republic, return home recommendation to home country also\x01",
            "It is said that it was issued … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The situation is that we\x01",
            "With more speed than I expected\x01",
            "It may be moving.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3BFC")

    label("loc_3B58")


    ChrTalk(
        0xA,
        (
            "Empire in crossbell\x01",
            "To the Republic, return home recommendation to home country also\x01",
            "It is said that it was issued … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The situation is that we\x01",
            "With more speed than I expected\x01",
            "It may be moving.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BFC")

    Jump("loc_4542")

    label("loc_3C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0D")

    ChrTalk(
        0xA,
        (
            "Looking at the burnt marks that still remain on the ground ……\x01",
            "It reminds me of the time of the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Fortunately armed groups\x01",
            "Coming aboard our shop is\x01",
            "I did not have it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If this was attacked\x01",
            "Well what about us ……\x01",
            "Just thinking is terrible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3DB3")

    label("loc_3D0D")


    ChrTalk(
        0xA,
        (
            "Fortunately armed groups\x01",
            "Coming aboard our shop is\x01",
            "I did not have it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If this was attacked\x01",
            "Well what about us ……\x01",
            "Just thinking is terrible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DB3")

    Jump("loc_4542")

    label("loc_3DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E5F")

    ChrTalk(
        0xA,
        (
            "There seems to be rumors already, but …\x01",
            "I think that there is an imperial government behind\x01",
            "Is it such a place as nature?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, then the empire\x01",
            "It is a place to worry about how it comes out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_3E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F0B")

    ChrTalk(
        0xA,
        (
            "Come and stay at national independence ……\x01",
            "Certainly the due date of the referendum\x01",
            "You were coming closer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, which choice is\x01",
            "Will it produce a more solid result …?\x01",
            "It is a place I want to see more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_3F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3F86")

    ChrTalk(
        0xA,
        (
            "The life full of boring life and stimulation,\x01",
            "Which one is happy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Huhu, what do you think?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_3F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4029")

    ChrTalk(
        0xA,
        (
            "It is confined to be defeated\x01",
            "It is a second-rate thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To you, by all means\x01",
            "Hoping for gambling in good faith\x01",
            "It is something I want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_4029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4103")

    ChrTalk(
        0xA,
        (
            "(It makes a loud noise from a little while ago,\x01",
            "Bother trouble other customers ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(Over there customers,\x01",
            "There is not a bit of manners. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(If action seems to go past\x01",
            "You have to be strictly careful. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_419C")

    label("loc_4103")


    ChrTalk(
        0xA,
        (
            "(Even though it is a casino,\x01",
            "This place is a place in this place\x01",
            "There are rules and manner. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(If action seems to go past\x01",
            "You have to be strictly careful. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_419C")

    Jump("loc_4542")

    label("loc_41A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_423C")

    ChrTalk(
        0xA,
        (
            "Mayor of Dieter\x01",
            "Is it gamble sense …?\x01",
            "Well, how is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Such play also smartly\x01",
            "Although it is an impression that seems to be working.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_423C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4394")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4308")

    ChrTalk(
        0xA,
        (
            "Today Mr. Ganz\x01",
            "You seem to be seeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For the lucky future of Ishiya\x01",
            "I was truly amazed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It is totally unclear of the original now\x01",
            "It is back to the weekend gamblers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_438F")

    label("loc_4308")


    ChrTalk(
        0xA,
        (
            "Mr. Ganz's anniversary\x01",
            "It is really for strong fortune\x01",
            "I was surprised, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It is totally unclear of the original now\x01",
            "It is back to the weekend gamblers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_438F")

    Jump("loc_4542")

    label("loc_4394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_443E")

    ChrTalk(
        0xA,
        (
            "A luxury club\x01",
            "\"Neue-Blanc\" this time\x01",
            "It looks like you opened a new store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To someone like me very much\x01",
            "It's a place I can not reach … …\x01",
            "I would like to go once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_443E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_44DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4459")
    Call(0, 11)
    Jump("loc_44D7")

    label("loc_4459")


    ChrTalk(
        0xA,
        (
            "No, No, Raita Rossa\x01",
            "It really is unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Gamble results from the process ……\x01",
            "Because the one who laughed at the end wins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D7")

    Jump("loc_4542")

    label("loc_44DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4542")

    ChrTalk(
        0xA,
        (
            "Welcome.\x01",
            "This is a card stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Would you like a game if it is OK?\x02",
    )

    CloseMessageWindow()

    label("loc_4542")

    Jump("loc_376D")

    label("loc_4547")

    TalkEnd(0xA)
    Return()

    # Function_10_3760 end

    def Function_11_454B(): pass

    label("Function_11_454B")

    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "…… Sorry, this game,\x01",
            "I am the winner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hehe, I will do it.\x01",
            "But next time I will not go\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Huh, hand softly.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_11_454B end

    def Function_12_45EE(): pass

    label("Function_12_45EE")

    Call(0, 13)
    Return()

    # Function_12_45EE end

    def Function_13_45F2(): pass

    label("Function_13_45F2")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",              # 0
            "Play with roulette\x01",      # 1
            "quit\x01",                # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4661")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4661")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46B6")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_46B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46CA")
    Jump("loc_5299")

    label("loc_46CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5299")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_486B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47DB")

    ChrTalk(
        0xB,
        (
            "I come to gamble even at such times …\x01",
            "It's a bad thing\x01",
            "I do not have anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Originally, distracting uneasy feelings,\x01",
            "It makes me feel easy\x01",
            "Because it is entertainment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Whether you are worried\x01",
            "I hope you enjoy your entertainment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4866")

    label("loc_47DB")


    ChrTalk(
        0xB,
        (
            "Originally, distracting uneasy feelings,\x01",
            "It makes me feel easy\x01",
            "It is entertainment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Whether you are worried\x01",
            "I hope you enjoy your entertainment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4866")

    Jump("loc_5299")

    label("loc_486B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4879")
    Jump("loc_5299")

    label("loc_4879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_49EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4963")

    ChrTalk(
        0xB,
        (
            "Crossbell's independence problem also\x01",
            "Finally up to where I can not return\x01",
            "You came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "President Dieter also\x01",
            "Do not worry about anything without winning\x01",
            "I do not think I will … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What, what kind of cards\x01",
            "Are they prepared?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_49E6")

    label("loc_4963")


    ChrTalk(
        0xB,
        (
            "President Dieter also\x01",
            "Do not worry about anything without winning\x01",
            "I do not think I will … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What, what kind of cards\x01",
            "Are they prepared?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E6")

    Jump("loc_5299")

    label("loc_49EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC4")

    ChrTalk(
        0xB,
        (
            "The day of the referendum is over\x01",
            "I approached three days later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although the results are visible,\x01",
            "On the day, I\x01",
            "I am going to vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Whether to vote for either … ….\x01",
            "Please do it secretly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B4D")

    label("loc_4AC4")


    ChrTalk(
        0xB,
        (
            "Although the results are visible,\x01",
            "On the day, I\x01",
            "I am going to vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Whether to vote for either … ….\x01",
            "Please do it secretly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B4D")

    Jump("loc_5299")

    label("loc_4B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4BCC")

    ChrTalk(
        0xB,
        (
            "Drake owner,\x01",
            "I heard that I am a little sleepy today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Until late\x01",
            "Did you drink it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C4E")

    ChrTalk(
        0xB,
        (
            "On this rainy day please come in our shop\x01",
            "Please do not miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uhufu, maybe\x01",
            "I might serve you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4CD8")

    ChrTalk(
        0xB,
        (
            "Gamble anything ……\x01",
            "The important thing is the closing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There is also a word saying that it is compatible,\x01",
            "It usually fails if you desire a lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D6B")

    ChrTalk(
        0xB,
        (
            "I, the human being thrills\x01",
            "I think that it is the desired living thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if the customer is also a victor.\x01",
            "The best thrill\x01",
            "I will present you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4DFF")

    ChrTalk(
        0xB,
        "Whether the crossbell should be independent …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Indeed, Mayor Dieter\x01",
            "We have an outrageous challenge\x01",
            "It was the thing that struck me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4E85")

    ChrTalk(
        0xB,
        (
            "Uhufu, it's time for the plenary session\x01",
            "The day came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "From now on the next Crossbell Times\x01",
            "It can not be helped with pleasure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F3A")

    ChrTalk(
        0xB,
        (
            "I have not seen it yet,\x01",
            "Orkis Tower, it is\x01",
            "It looks like a good building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Skyscraper building on the ground floor 40 …\x01",
            "I am looking forward to burning it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_4F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5050")

    ChrTalk(
        0xB,
        (
            "Mayor Dieter called\x01",
            "The international conference is about to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Read each other's truth,\x01",
            "Various trump cards possessed by each#6Rcard#To\x01",
            "Cutting at the timing of here …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What is it to say,\x01",
            "I am diplomatic and gambling\x01",
            "I think the essence is the same.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_50D0")

    label("loc_5050")


    ChrTalk(
        0xB,
        (
            "In setting up this occasion,\x01",
            "Mayor Dieter\x01",
            "Any trump card#6Rcard#Have you prepared? …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Uhufu, you are not interested.\x02",
    )

    CloseMessageWindow()

    label("loc_50D0")

    Jump("loc_5299")

    label("loc_50D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5133")

    ChrTalk(
        0xB,
        "Huhu, how about customers, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I will invite you to the labyrinth of thought.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_5133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5230")

    ChrTalk(
        0xB,
        (
            "Welcome to the casino house \"Barca\".\x01",
            "You can enjoy roulette here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "First of all I will refuse it,\x01",
            "We sort of squid caterpillar on this table\x01",
            "Absolutely impossible to trap ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "How is it, once without fine work\x01",
            "Why do not you leave yourself to fate?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5299")

    label("loc_5230")


    ChrTalk(
        0xB,
        (
            "It is wide and thin and it is good to stretch solidly … ….\x01",
            "It is also nice to go to a narrow and thick game ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "All results are god knows the gods only.\x02",
    )

    CloseMessageWindow()

    label("loc_5299")

    Jump("loc_45FF")

    label("loc_529E")

    TalkEnd(0xB)
    Return()

    # Function_13_45F2 end

    def Function_14_52A2(): pass

    label("Function_14_52A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_52B3")
    Jump("loc_60EA")

    label("loc_52B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_541B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539A")

    ChrTalk(
        0xFE,
        (
            "I was not exact,\x01",
            "A ridiculous incident a week ago\x01",
            "It looks like it has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is no similar thing in the future\x01",
            "It seems impossible to say … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You come to play on the crossbell\x01",
            "It might be better to refrain from now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5416")

    label("loc_539A")


    ChrTalk(
        0xFE,
        (
            "There is no similar thing in the future\x01",
            "It seems impossible to say … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You come to play on the crossbell\x01",
            "It might be better to refrain from now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5416")

    Jump("loc_60EA")

    label("loc_541B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_54AC")

    ChrTalk(
        0xFE,
        (
            "The purpose of the mysterious armed group\x01",
            "What on earth is it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What are the demands\x01",
            "Naturally depending on where you come out\x01",
            "I do not know but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60EA")

    label("loc_54AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_553D")

    ChrTalk(
        0xFE,
        (
            "By the way, today,\x01",
            "Citizen's hall to citizen forum\x01",
            "It's a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With intention of a society tour,\x01",
            "I wonder if I'll come over to see it later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60EA")

    label("loc_553D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_55A8")

    ChrTalk(
        0xFE,
        (
            "Even to play with a crossbell\x01",
            "I got bored again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is there anything interesting?\x02",
    )

    CloseMessageWindow()
    Jump("loc_60EA")

    label("loc_55A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_570B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56A0")

    ChrTalk(
        0xFE,
        (
            "Yesterday's son Dora,\x01",
            "I was in good shape at the beginning\x01",
            "Eventually I was losing a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you regret so much,\x01",
            "Spewing filthy dirty words\x01",
            "I went back quickly … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, to such people\x01",
            "The goddess will also run out of sociability.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5706")

    label("loc_56A0")


    ChrTalk(
        0xFE,
        (
            "Yesterday's son Dora,\x01",
            "It seems I have not come to the casino today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, today for the game\x01",
            "I think I can concentrate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5706")

    Jump("loc_60EA")

    label("loc_570B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5847")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57B9")

    ChrTalk(
        0xFE,
        (
            "I am stuck with my parent's Mira and power\x01",
            "I'm not interested in a shallow man at the bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, after all\x01",
            "Like Drake owner\x01",
            "I am bitter and must be Dandy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5842")

    label("loc_57B9")


    ChrTalk(
        0xFE,
        (
            "No matter how much you have a mirror,\x01",
            "I will refuse son Dora.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, after all\x01",
            "Like Drake owner\x01",
            "I am bitter and must be Dandy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5842")

    Jump("loc_60EA")

    label("loc_5847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_58D2")

    ChrTalk(
        0xFE,
        (
            "It is a trade meeting ……\x01",
            "Huhu, Mayor Dieter\x01",
            "It is really a kind of guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This politicians skill … …\x01",
            "I wonder if the gamble is also strong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60EA")

    label("loc_58D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5967")

    ChrTalk(
        0xFE,
        (
            "Galetti,\x01",
            "I lost to Mr. Gants before\x01",
            "I still have it in the roots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, what is a gangster\x01",
            "You really do not want to lose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60EA")

    label("loc_5967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5FDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD7")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A20")
    Jump("loc_5A6A")

    label("loc_5A20")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A40")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A6A")

    label("loc_5A40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A60")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A6A")

    label("loc_5A60")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A6A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Oh, it is not Randy.\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh, that kind of you\x01",
            "Literallosa's older sister.\x02\x03",
            "#00302FHow about, celebrate the reunion\x01",
            "Even on a date with me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, that's right.\x01",
            "If I can win against me\x01",
            "You may think about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOh, did you say?\x01",
            "Soon -\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C2B")

    ChrTalk(
        0x101,
        "#00009FHey, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHehe, of course it is a joke, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh, ah ……\x01",
            "Well, smiling fearfully, both of us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CCB")

    label("loc_5C2B")


    ChrTalk(
        0x102,
        (
            "#00109FHey, Randy.\x01",
            "I think I said that earlier ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh, ah ……\x01",
            "So it's a joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Randy senior … ….\x01",
            "I really do not understand. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CCB")

    SetScenarioFlags(0x14C, 4)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_5FD6")

    label("loc_5CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E71")
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D72")
    Jump("loc_5DBC")

    label("loc_5D72")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5D92")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DBC")

    label("loc_5D92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DB2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DBC")

    label("loc_5DB2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DBC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Huhu, apparently\x01",
            "I'd like to take care of the game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But,\x01",
            "Whether or not there is\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FWell, that 's not it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_5FD6")

    label("loc_5E71")

    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F02")
    Jump("loc_5F4C")

    label("loc_5F02")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F22")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F4C")

    label("loc_5F22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F42")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F4C")

    label("loc_5F42")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F4C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Huhu, apparently\x01",
            "I'd like to take care of the game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But,\x01",
            "Whether or not there is\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    label("loc_5FD6")

    Jump("loc_60EA")

    label("loc_5FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_604A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FF6")
    Call(0, 11)
    Jump("loc_6045")

    label("loc_5FF6")


    ChrTalk(
        0xFE,
        "Oh, I lost again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh, but.\x01",
            "It is not me who ends with this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6045")

    Jump("loc_60EA")

    label("loc_604A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_60EA")

    ChrTalk(
        0xFE,
        (
            "For a while to crossbell\x01",
            "I was refraining from coming ….\x01",
            "I came back again after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My hometown Calvado is not too bad,\x01",
            "After all the cross bell's air is exceptional.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60EA")

    TalkEnd(0xFE)
    Return()

    # Function_14_52A2 end

    def Function_15_60EE(): pass

    label("Function_15_60EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_610C")
    Call(0, 16)
    Jump("loc_618C")

    label("loc_610C")


    ChrTalk(
        0xFE,
        (
            "Uncut\x01",
            "If you were playing in the slot,\x01",
            "An old lady got on board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I was worried about it indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_618C")

    Jump("loc_6F25")

    label("loc_6191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_62E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626F")

    ChrTalk(
        0xFE,
        (
            "With no big deal such as martial law\x01",
            "Hook up the hawk,\x01",
            "You came to see me … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, no way\x01",
            "What is involved … …\x01",
            "It is a blunder in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Around this time, an old lady\x01",
            "You should worry about it … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_62DC")

    label("loc_626F")


    ChrTalk(
        0xFE,
        (
            "To this\x01",
            "What is involved … …\x01",
            "It is a blunder in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Around this time, an old lady\x01",
            "You should worry about it … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62DC")

    Jump("loc_6F25")

    label("loc_62E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_635D")

    ChrTalk(
        0xFE,
        (
            "I heard a speech a while ago … …\x01",
            "It was a terrible story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, for me\x01",
            "I do not know what is right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F25")

    label("loc_635D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_63ED")

    ChrTalk(
        0xFE,
        (
            "In the raid incident one week ago,\x01",
            "It really got tasted fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Potato, I like this kind of time\x01",
            "You do not have to go get it done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F25")

    label("loc_63ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_655A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64CC")

    ChrTalk(
        0xFE,
        (
            "Apparently, in Mainz\x01",
            "It seems like a serious thing will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow even at home\x01",
            "I came out because I calmed down … …\x01",
            "I am disappointed with the fluke today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is bad for an old lady,\x01",
            "I suppose I should go home early.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6555")

    label("loc_64CC")


    ChrTalk(
        0xFE,
        (
            "Somehow even at home\x01",
            "I came out because I calmed down … …\x01",
            "I am disappointed with the fluke today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is bad for an old lady,\x01",
            "I suppose I should go home early.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6555")

    Jump("loc_6F25")

    label("loc_655A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_65D7")

    ChrTalk(
        0xFE,
        (
            "Lost losing yesterday … …\x01",
            "I will definitely get back today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Look now, I will do!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F25")

    label("loc_65D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_66FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A0")

    ChrTalk(
        0xFE,
        (
            "Huh! Is it? In the hit now ……\x01",
            "Well … is it a shoulder watermark?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kuuuuuu … ….\x01",
            "Why come, why have you come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F(Okay, old man\x01",
            "It is getting hot again. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_66F5")

    label("loc_66A0")


    ChrTalk(
        0xFE,
        (
            "Kuuuuuu … ….\x01",
            "Why come, why have you come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm a battlemaker's battle master!\x02",
    )

    CloseMessageWindow()

    label("loc_66F5")

    Jump("loc_6F25")

    label("loc_66FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67AC")

    ChrTalk(
        0xFE,
        (
            "Hmm, today is\x01",
            "The hit is coming soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After returning home like this\x01",
            "What does the grandpa say … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eee, get out!\x01",
            "Come out, get out!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6823")

    label("loc_67AC")


    ChrTalk(
        0xFE,
        (
            "Hmm …\x01",
            "After returning home like this\x01",
            "What does the grandpa say … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eee, get out!\x01",
            "Come out, come out!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6823")

    Jump("loc_6F25")

    label("loc_6828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68E2")

    ChrTalk(
        0xFE,
        (
            "In the crossbell independence,\x01",
            "I will agree fully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A part of tax revenue in the first place\x01",
            "The story of paying to two major powers\x01",
            "It is nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Independence is a natural right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_694E")

    label("loc_68E2")


    ChrTalk(
        0xFE,
        (
            "In the first place, part of the tax revenue\x01",
            "The story of paying to two major powers\x01",
            "It is nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Independence is a natural right.\x02",
    )

    CloseMessageWindow()

    label("loc_694E")

    Jump("loc_6F25")

    label("loc_6953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6C32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B50")

    ChrTalk(
        0xFE,
        (
            "This morning an old lady\x01",
            "You smile fearlessly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you ask why you are laughing,\x01",
            "I told you to understand soon … but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, to an old lady\x01",
            "Unnoticed the contents of the wallet\x01",
            "You seem to have been pulled out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00305FHmm? Okay, Ricci grandfather,\x01",
            "What are you doing without Mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Just sitting is bad?\x02",
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
            "#00306FNo … well … it's crowded.\x01",
            "Hey, well, not bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6C2D")

    label("loc_6B50")


    ChrTalk(
        0xFE,
        (
            "I can not play without Mira … …\x01",
            "I definitely came home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you give in here,\x01",
            "It is an acupuncture point of thought from an old lady.\x02",
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

    label("loc_6C2D")

    Jump("loc_6F25")

    label("loc_6C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6CCD")

    ChrTalk(
        0xFE,
        (
            "Even though the world is unveiled at the unveiling ceremony,\x01",
            "I am here anyway\x01",
            "Just hit the slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The grandmother is an old lady, with a tea drink buddy\x01",
            "Yoroshiku yeah yeah yeah.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F25")

    label("loc_6CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DCA")

    ChrTalk(
        0x104,
        (
            "#00300FLooks like Ricci grandfather.\x01",
            "Have you made doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoo, that voice is Randy?\x01",
            "It is a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Genki is also fine as you can see,\x01",
            "Great Fever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do not disturb if you understand!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHaha, that's not a serious thing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_6E14")

    label("loc_6DCA")


    ChrTalk(
        0xFE,
        "If you are in a good place right now, please do not interfere!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… …. Huh, I came again!\x02",
    )

    CloseMessageWindow()

    label("loc_6E14")

    Jump("loc_6F25")

    label("loc_6E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6EB2")

    ChrTalk(
        0xFE,
        (
            "Whatever the grandmother says,\x01",
            "I am gambling.\x01",
            "I will not stop at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This was also born to a contestant\x01",
            "Jack is a regulation, Ho Ho Ho.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F25")

    label("loc_6EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6F25")

    ChrTalk(
        0xFE,
        (
            "Hurray, today too\x01",
            "The slot seems to come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Jang the medals\x01",
            "The sound is unbearable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F25")

    TalkEnd(0xFE)
    Return()

    # Function_15_60EE end

    def Function_16_6F29(): pass

    label("Function_16_6F29")

    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "In fact, you are a person … …\x01",
            "Why have not you come home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Now, I will return home soon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Wait, old lady.\x01",
            "After replacing this coin at least ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Eh, please do not be silent! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Something like that, after birth! It is!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_16_6F29 end

    def Function_17_701B(): pass

    label("Function_17_701B")


    ChrTalk(
        0x104,
        (
            "#00300FLooks like Ricci grandfather.\x01",
            "How are you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Anonymous? Is that voice Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Recently, I will not face it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FWell, I'm busy with my work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Because I am busy, I will play.\x01",
            "I understand it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHaha, it certainly is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "A woman, this morning\x01",
            "I was ambushed at the front door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "You lifted your eyebrows and scoffed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It was a place to be taken back dangerously.\x01",
            "Well, it is just a close - up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No matter how the crossbell changes\x01",
            "Only the entertainment area will be gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "A gaming center in the bar, a tourist full of abundance\x01",
            "Gathering group gush\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even if the appearance changes\x01",
            "Let's change nothing from old days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… In addition,\x01",
            "There are places where security is bad.\x01",
            "An amateur should be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_17_701B end

    def Function_18_72B5(): pass

    label("Function_18_72B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72CA")
    Call(0, 16)
    Jump("loc_7336")

    label("loc_72CA")


    ChrTalk(
        0xFE,
        (
            "Totally, this person ……\x01",
            "I wonder how much I care\x01",
            "I wonder if she thinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… For the time being, you have zero spending money.\x02",
    )

    CloseMessageWindow()

    label("loc_7336")

    TalkEnd(0xFE)
    Return()

    # Function_18_72B5 end

    def Function_19_733A(): pass

    label("Function_19_733A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, red and red\x01",
            "I thought that it was black next time ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How about gambling?\x01",
            "It is not straightforward.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_733A end

    def Function_20_73B7(): pass

    label("Function_20_73B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7450")

    ChrTalk(
        0xFE,
        (
            "I thought that it was good for distraction,\x01",
            "I was in a relationship with Ganz … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Back home earlier, about the future\x01",
            "It seems better to consult with the town mayors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74AA")

    label("loc_7450")


    ChrTalk(
        0xFE,
        (
            "Haha, so at that time\x01",
            "It was good when I stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gantt, you are\x01",
            "I am too greedy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74AA")

    TalkEnd(0xFE)
    Return()

    # Function_20_73B7 end

    def Function_21_74AE(): pass

    label("Function_21_74AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7542")

    ChrTalk(
        0xFE,
        (
            "When you come to Cros Bell City\x01",
            "To such a serious thing\x01",
            "I do not think I'm getting down … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Ha, it's a casino\x01",
            "I do not feel like it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7584")

    label("loc_7542")


    ChrTalk(
        0xFE,
        (
            "Oh shit……!\x01",
            "I thought I was winning\x01",
            "It is no longer par!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7584")

    TalkEnd(0xFE)
    Return()

    # Function_21_74AE end

    def Function_22_7588(): pass

    label("Function_22_7588")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_767F")

    ChrTalk(
        0xFE,
        (
            "How about independence or not\x01",
            "It seems that there are noises in the world … …\x01",
            "It is quite foolish people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell is as usual\x01",
            "Flirting in the Republic,\x01",
            "You only have to follow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While doing so\x01",
            "Peace will be promised.\x01",
            "Kukuku\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_76F1")

    label("loc_767F")


    ChrTalk(
        0xFE,
        (
            "Well, as for independence,\x01",
            "It has nothing to do with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kuku, at most in this city\x01",
            "I will just have fun playing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76F1")

    TalkEnd(0xFE)
    Return()

    # Function_22_7588 end

    def Function_23_76F5(): pass

    label("Function_23_76F5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Kukuto, do it in moderation Yuri ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you win too much,\x01",
            "Perhaps we are getting banned.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_76F5 end

    def Function_24_7765(): pass

    label("Function_24_7765")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "A woman sitting there,\x01",
            "It is quite beautiful, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To refuse our invitation\x01",
            "There is an eye to see.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_7765 end

    def Function_25_77DA(): pass

    label("Function_25_77DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7914")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77FC")
    TalkEnd(0xFE)
    Call(0, 26)
    Return()

    label("loc_77FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78AD")

    ChrTalk(
        0x15,
        (
            "#03500FWell, when I got better\x01",
            "Would you like to return to the empire?\x02\x03",
            "#03504FThat thrill evil beard\x01",
            "Please help me … hey …\x01",
            "Okay, the man who I can count on is Trai.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7914")

    label("loc_78AD")


    ChrTalk(
        0x15,
        (
            "#03500FWell, when I got better\x01",
            "Would you like to return to the empire?\x02\x03",
            "#03504FOkay, the man who I can count on is Trai.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7914")

    TalkEnd(0xFE)
    Return()

    # Function_25_77DA end

    def Function_26_7918(): pass

    label("Function_26_7918")

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
        "#11P#03502FYo, tired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FLes Lector, … ….\x01",
            "Also to such a casino in …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A7F")

    ChrTalk(
        0x105,
        "#10402FHuh, I feel relaxed a lot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AFB")

    label("loc_7A7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7ABB")

    ChrTalk(
        0x109,
        "#10106FI am very relaxed …\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AFB")

    label("loc_7ABB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AFB")

    ChrTalk(
        0x106,
        (
            "#10702FI am very relaxed.\x01",
            "Looks like it …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AFB")


    ChrTalk(
        0x103,
        (
            "#6P#00205FClerical clerk of the clerk\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03506FOh, during the battle with the \"Mage Guard\"\x01",
            "I was totally beaten up.\x02\x03",
            "#03509FWell, do not mind letting me go easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHaha …\x02\x03",
            "#00000FKohon, er … ….\x01",
            "Cooperation to release strategy,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FWith the rush of the Orchis Tower\x01",
            "I am indebted to you ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03504FHaha, that's okay.\x01",
            "I liked it this way.\x02\x03",
            "#03502FAs a clerk\x01",
            "Because it was desk work,\x01",
            "It was an honest exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FI guess you are an intelligence worker … …\x01",
            "I often say I move around and often say.\x02\x03",
            "#00301FBut, regardless of Ms. Kirika\x01",
            "You are over there\x01",
            "I do not believe that he had a fighting power behind it.\x02\x03",
            "That swordsmanship and higher arc … …\x01",
            "An amateur overnight\x01",
            "You can not handle it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03510FHmm, so much\x01",
            "If you want to know, let me know.\x02\x03",
            "#03504FYes, that was about 30 years ago ……\x01",
            "I live in a certain mountain back of the empire\x01",
            "I was taught to her.\x02",
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
            "#6P#00006F… … from the beginning to the openness\x01",
            "It is a lie smell.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F80")

    ChrTalk(
        0x10A,
        "#00603F(Well … it's a caring man.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FF3")

    label("loc_7F80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FBC")

    ChrTalk(
        0x109,
        "#10106FIt is too adequate indeed …\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FF3")

    label("loc_7FBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FF3")

    ChrTalk(
        0x105,
        "#10409FAhaha, it's not quite right.\x02",
    )

    CloseMessageWindow()

    label("loc_7FF3")


    ChrTalk(
        0x15,
        (
            "#11P#03504FWell, that part is\x01",
            "Imagine you like it.\x02\x03",
            "#03510F…… Well, I 'm almost at it.\x01",
            "I must return to the empire.\x02\x03",
            "#03506FThat thrill evil beard\x01",
            "Please help me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00205F\"Chairman of Iron Blood\" … …\x01",
            "Sure, it was shot and missing\x01",
            "It was getting on.\x02\x03",
            "#00203FBy \"shinkin\"\x01",
            "Ski that the regular army was hit hard\x01",
            "I was touched by aristocratic power … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03510FOh, Teito is also totally\x01",
            "It is said that aristocrats were occupied by the nobles.\x02\x03",
            "#03506FWhew, even so\x01",
            "It's an easy-going osan.\x01",
            "Let's leave it to protect us.\x02\x03",
            "#03500FWell, it's about that osan\x01",
            "I guess it does not bother easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FIt's kind of casual …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03509FHaha, how about you?\x02\x03",
            "#03504FGiulious' s Osan and aristocratic power,\x01",
            "Whichever win … ….\x02\x03",
            "#03502FAhead, the fate of Crossbell is\x01",
            "I do not think it will change.\x02",
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
        "#00108F……that is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F…… What will happen in the future\x01",
            "I do not know yet.\x02\x03",
            "#00001FBut, anything else ……\x01",
            "First of all, in order to regain Ka'aa,\x01",
            "I am planning to head that \"Taiki\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03504F…… Haha, that's fine.\x02\x03",
            "It is important to look ahead,\x01",
            "I just caught it\x01",
            "I have scoops.\x02\x03",
            "#03500FWhat is more important than anything\x01",
            "It is \"now\" in front of you.\x02",
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
            "#6P#00006FCure, even if you suddenly say a decent thing\x01",
            "That is puzzled by that … …\x02\x03",
            "#00000F……Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03502FHa ha, well at best\x01",
            "I tried to scratch him.\x02\x03",
            "#03509FOtherwise,\x01",
            "I even bothered to go away\x01",
            "It is not worth Kai.\x02",
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

    # Function_26_7918 end

    def Function_27_86EB(): pass

    label("Function_27_86EB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Play with Slots\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_877E")
    FadeToDark(300, 0, -1)
    OP_0D()
    PlayBGM("ed7113", 0)
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1F()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_877E")

    TalkEnd(0xFF)
    Return()

    # Function_27_86EB end

    def Function_28_8782(): pass

    label("Function_28_8782")

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
        "#5PHello everyone\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P… …. Randy's case\x01",
            "Did you come in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYes……\x01",
            "Is he still here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, around 3 o'clock in the middle of the night\x01",
            "It appeared with the store in the shop … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAfter drinking here for a while\x01",
            "I went home, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206F… apparently first\x01",
            "It seems like you visited this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#12PSo, then somewhere\x01",
            "Did not you tell me to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P… After all, at the support department\x01",
            "It seems they did not return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, Where are you going?\x01",
            "I did not say that in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, while I was drinking,\x01",
            "There are many fewer mouths than usual … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAs a bonus, on the way back, some things\x01",
            "I took it off from me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FSomething?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah … … with a heavy trunk\x01",
            "I do not even know the contents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTwo years ago, Randy was in this town\x01",
            "I kept it at the time I came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P\"When I died around the junk house\x01",
            "Please rose and sell it. \"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FNo way…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FRandy-senpai..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00206FThat doesn't seem like him at all\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00008F…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P… About the career's career\x01",
            "I also know to some extent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut what kind of things have happened in the past\x01",
            "I do not know until there was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PKnowing that and being able to become the power of\x01",
            "Perhaps, you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FOrner…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004F……Yes.\x01",
            "I think that I want to be there.\x02",
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

    # Function_28_8782 end

    def Function_29_8D63(): pass

    label("Function_29_8D63")

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
            "#03506FWhat is it, Doghi again.\x02\x03",
            "#03501FSometimes Feena\x01",
            "Please do not pin it unless it comes out.\x02",
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
            "#00013F#12P─ ─ Lecter.\x01",
            "I can not run away anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PA naughtiness, an idea\x01",
            "Please reveal your identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03503F#5PI do not have an identity.\x02\x03",
            "#03510FMimoto, Mimoto ……\x01",
            "I wonder which one is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P……frankly\x01",
            "Please do not try to misappropriate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03504FThat's right.\x02\x03",
            "#03500FI will answer with yes or no\x01",
            "Ask me anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12P……I understand.\x01",
            "Then let me ask a question.\x02\x03",
            "#00001F─ ─ Empire Government Second Secretary,\x01",
            "At Rector Arundole\x01",
            "Is it correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#03504FJesus.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#12PBelong to the Imperial Army Information Bureau\x01",
            "Will you also serve as a special captain?\x02",
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
        "#00008F#12P(Is it possible to admit that … ….)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6P…… Then, from me as well.\x02\x03",
            "#00101FThis visit was made by the Imperial Government\x01",
            "Is it on receiving intention?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)
    Sleep(300)

    ChrTalk(
        0x15,
        "#03501FIt is no, it is also Jesus.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PStay a minimum of 1 month\x01",
            "Are you planned?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03504FGiggle\x02\x03",
            "#03502FThe answer is no.\x01",
            "I will be back in about a week.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9410():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9410)
    Sleep(100)

    def lambda_9420():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9420)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00013F(Up to here ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(Yeah ….\x01",
            "I can not do any more. )\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9485():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9485)
    Sleep(50)

    def lambda_9495():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9495)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00003F#12P── I have troubled you.\x01",
            "Captain Alaindor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#6PThank you for your cooperation.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Sleep(200)

    ChrTalk(
        0x15,
        (
            "#03506FOh, it is good, but yo.\x02\x03",
            "#03505FWell, is that Tibikiko healthy?\x01",
            "You guys picked it up, were not you?\x02",
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
            "#00005F#12PWell, is that about Ka'a?\x02\x03",
            "#00012FYeah, thanks to you.\x01",
            "I live a healthy life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6P… … that section\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PHuff, I'm gonna let us go\x01",
            "You helped me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03504FWhat 's with that?\x01",
            "I was just playing with Kuro.\x02\x03",
            "#03502FSo, Hultman's Osan,\x01",
            "After all it 's getting caught?\x02\x03",
            "Well, it was strangled though it was strange,\x01",
            "It was nice to be protected safely.\x02",
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
        "#00001F#12P…… Why on such a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PAfter arresting those two\x01",
            "Three days have not passed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03503FWell, confirmation about that\x01",
            "That's one of my purpose.\x02\x03",
            "#03501FBy the way the other aim is ──\x02",
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
        "Voice of a girl",
        "#3936V#1P#30WOh, thank you!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "Voice of a girl",
        "#3937V#1P#30WWhat are you doing in such a place.\x02",
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

    def lambda_9A25():
        OP_93(0x101, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A25)

    def lambda_9A32():
        OP_93(0x102, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A32)

    def lambda_9A3F():
        OP_93(0x109, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9A3F)

    def lambda_9A4C():
        OP_93(0x105, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A4C)
    SetChrPos(0x15, 6540, 4270, 13420, 180)
    OP_68(5340, 5500, 12170, 6000)
    MoveCamera(130, 18, 0, 6000)
    OP_6E(400, 6000)
    SetCameraDistance(22330, 6000)

    def lambda_9A98():
        OP_9B(0x0, 0x16, 0x0, 0x36B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9A98)
    Sleep(2000)

    def lambda_9AB0():

        label("loc_9AB0")

        TurnDirection(0x101, 0x16, 500)
        Yield()
        Jump("loc_9AB0")

    QueueWorkItem2(0x101, 1, lambda_9AB0)
    Sleep(50)

    def lambda_9AC5():

        label("loc_9AC5")

        TurnDirection(0x105, 0x16, 500)
        Yield()
        Jump("loc_9AC5")

    QueueWorkItem2(0x105, 1, lambda_9AC5)
    OP_6F(0x1)
    WaitChrThread(0x16, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x105, 0x1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x16,
        (
            "#04601F#3970V#11P#30WTickets for alkane shell\x01",
            "You will arrange it, will not you?\x02\x03",
            "#3971VSo, what has become of ~!\x02",
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
            "#03509F#6PWell, this is the night performance\x01",
            "I secured a seat for the guests.\x02\x03",
            "At best thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#04602F#11Preally! Is it?\x02\x03",
            "#04612FThank you!\x01",
            "I wanted to see it from the front!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P(……Who……?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6P(It looks like young, but …).\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x101, 500)

    ChrTalk(
        0x16,
        (
            "#04605F#11Pthat……?\x02\x03",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#5PEr … … What is it?\x02",
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
            "Hoon …\x01",
            "Older, you smell.\x02\x03",
            "It is a nostalgic smell.\x02",
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
        "#00005F#5PHuh……\x02",
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
        "#04609F#3972V#11POh no.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(150)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The girl lightly bite into the earlobe of Lloyd#2RRudder#.\x07\x00\x02",
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
        "#00011F#5PIt is! It is! It is! Is it? Is it? Is it? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00111F#6PWait a minute! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#6PWell, yeah yeah! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#12PHu ♪\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_9B(0x1, 0x16, 0xB4, 0x1F4, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        "#00007F#5PSuddenly what ……! Is it?\x02",
    )

    CloseMessageWindow()
    SetChrName("Redhead girl")

    ChrTalk(
        0x16,
        (
            "#04612F#11PFuji, feast on fire\x02\x03",
            "#04602FYes, after all\x01",
            "It smells faintly.\x02\x03",
            "From those two of you\x01",
            "I rarely smell, but ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x16, 0x0, 0x1F4)

    ChrTalk(
        0x16,
        (
            "#04605F#11P── Ah!\x01",
            "My sister will do a little! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#6PHuh……\x02",
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
        "#00115F#3391V#4S#5PKyaaaaaaaa! Is it?\x02",
    )

    CloseMessageWindow()
    OP_24(0xD3F)
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00011F#11PD, Eli! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#5PIs not it before the unawares?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x16,
        (
            "#04611F#3938V#5P#30WMy older sister, I do not deserve it.\x02\x03",
            "#04609F#3939VBecause Charlie is Petan\x01",
            "I'm so jealous\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF63)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00112F#3392V#5P#40WA little\x01",
            "Please stop it!\x02\x03",
            "#00113F#3393VAhn …!\x01",
            "Why is this why …!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD41)
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10114F#5PI do not know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309F#6PAhaha, that's a nice sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PWell, it certainly is not …!\x02\x03",
            "#00007FHey you!\x01",
            "What are you doing suddenly! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#03509FHaha, it's all you want to do.\x02\x03",
            "#03502FMore than that\x01",
            "I will be sexually harassed ~ ~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#04605F#5PIt's not sexual harassment.\x01",
            "It's a skin ship.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00107F#5P#4SJu, enough sexual harassment!\x02",
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

    def lambda_A556():
        OP_9B(0x1, 0x16, 0x87, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A556)
    Sound(802, 0, 100, 0)
    OP_A1(0x102, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)

    def lambda_A57D():
        OP_99(0x101, 0x102, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A57D)
    Sleep(50)

    def lambda_A594():
        OP_99(0x109, 0x102, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A594)
    Sleep(500)

    ChrTalk(
        0x102,
        "#5P#00113FHa Ha ha ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#5PE, Ms. Erie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#11PIs not it okay?\x02",
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
            "#03510F#5PWell then.\x01",
            "We shall excuse us.\x02\x03",
            "#03509FAt the Michelin theme park\x01",
            "Play with me till night.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x16,
        "Charlie",
        "#04612F#3940V#5P#30WWell then, see you ~!\x02",
    )

    CloseMessageWindow()
    OP_24(0xF64)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_68(4780, 5500, 11560, 3000)
    OP_93(0x15, 0xE1, 0x0)

    def lambda_A709():
        OP_96(0x15, 0x1662, 0xFA0, 0x29FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A709)
    OP_95(0x16, 4740, 4000, 12780, 2000, 0x0)

    def lambda_A737():
        OP_95(0x15, 4740, 4000, 4480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A737)
    OP_95(0x16, 5730, 4000, 11500, 2000, 0x0)

    def lambda_A765():
        OP_93(0x101, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A765)

    def lambda_A772():
        OP_93(0x105, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A772)
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
        "#00013F#5PWhat was it …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5POne after another\x01",
            "I missed it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHuh, it was a strong child.\x02\x03",
            "#10309FIt's about 15 or 6 years old?\x01",
            "It's quite good to work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x2, 0x3, 0x4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00107F#5P#4SIt's not a good job!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x8, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0x8, 0x7)

    ChrTalk(
        0x102,
        (
            "#00106F#5P#30WUu …\x01",
            "Why did I look like this …?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#00012F#11PEr … … It was a disaster.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5PWell, girls are gang\x01",
            "Even if it does not become so serious … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x109, 500)

    ChrTalk(
        0x105,
        (
            "#10305F#12PAnd you, Miss Marybele\x01",
            "Are not you accustomed to being massaged?\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x4, 0x7, 0xA, 0xB, 0xC)
    Sleep(100)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00115F#5P#5SEven, I am not used to being rubbed!\x02",
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
            "After that, Lloyd's\x01",
            "Return to the police headquarters and call the first section ……\x02\x03",
            "Together with the trend of black moon\x01",
            "I made a report on Rector.\x07\x00\x02",
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

    # Function_29_8D63 end

    def Function_30_AAFD(): pass

    label("Function_30_AAFD")


    def lambda_AB02():
        OP_95(0x101, 5030, 4000, 10490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB02)
    WaitChrThread(0x101, 1)

    def lambda_AB20():
        OP_95(0x101, 6540, 4000, 11860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB20)
    WaitChrThread(0x101, 1)

    def lambda_AB3E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB3E)
    Return()

    # Function_30_AAFD end

    def Function_31_AB47(): pass

    label("Function_31_AB47")


    def lambda_AB4C():
        OP_95(0x102, 5500, 4000, 9870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB4C)
    WaitChrThread(0x102, 1)

    def lambda_AB6A():
        OP_95(0x102, 5520, 4000, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB6A)
    WaitChrThread(0x102, 1)

    def lambda_AB88():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB88)
    Return()

    # Function_31_AB47 end

    def Function_32_AB91(): pass

    label("Function_32_AB91")


    def lambda_AB96():
        OP_95(0x109, 4810, 4000, 13910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AB96)
    WaitChrThread(0x109, 1)

    def lambda_ABB4():
        OP_95(0x109, 5530, 4000, 14790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ABB4)
    WaitChrThread(0x109, 1)

    def lambda_ABD2():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ABD2)
    Return()

    # Function_32_AB91 end

    def Function_33_ABDB(): pass

    label("Function_33_ABDB")


    def lambda_ABE0():
        OP_95(0x105, 4800, 4000, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ABE0)
    WaitChrThread(0x105, 1)

    def lambda_ABFE():
        OP_95(0x105, 4740, 4000, 10780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ABFE)
    WaitChrThread(0x105, 1)

    def lambda_AC1C():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AC1C)
    Return()

    # Function_33_ABDB end

    def Function_34_AC25(): pass

    label("Function_34_AC25")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9F(0x0, 0x16)
    OP_9F(0x1, 4740, 4000, 12360)
    OP_9F(0x1, 4740, 4000, 13900)
    OP_9F(0x1, 5520, 4000, 13900)
    OP_9F(0x2, 0x16, 8000, 0x6)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0x16, 0xB4, 0x0)
    Return()

    # Function_34_AC25 end

    def Function_35_AC74(): pass

    label("Function_35_AC74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC94")
    Sound(888, 0, 70, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_35_AC74")

    label("loc_AC94")

    Return()

    # Function_35_AC74 end

    def Function_36_AC95(): pass

    label("Function_36_AC95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ACB5")
    Sound(888, 0, 70, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x3, 0x4, 0x5, 0x4)
    Jump("Function_36_AC95")

    label("loc_ACB5")

    Return()

    # Function_36_AC95 end

    SaveToFile()

Try(main)
