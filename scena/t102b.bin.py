from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t102b.bin",                # FileName
        "t102b",                    # MapName
        "t102b",                    # Location
        0x0095,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 149, 0, 2, 0, 3],
    )

    BuildStringList((
        "t102b",                  # 0
        "Franc",                 # 1
        "Cecil",                 # 2
        "Ilia",                 # 3
        "Lisha",               # 4
        "Shuri",                 # 5
        "Zeit",               # 6
        "Elise",               # 7
        "tourist",                 # 8
        "tourist",                 # 9
        "tourist",                 # 10
        "SE control",                 # 11
    ))

    AddCharChip((
        "chr/ch02702.itc",                   # 00
        "chr/ch08500.itc",                   # 01
        "chr/ch05200.itc",                   # 02
        "chr/ch05100.itc",                   # 03
        "chr/ch07500.itc",                   # 04
        "chr/ch10000.itc",                   # 05
        "chr/ch33200.itc",                   # 06
        "chr/ch21600.itc",                   # 07
        "chr/ch20100.itc",                   # 08
        "chr/ch32300.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294942387, 0,       5570,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(98589,   0,       20659,   225,  389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(97339,   0,       19579,   45,   389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       500,     0,    385,  0x0, 0,   9,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(27760,   0,       9640,    1200,    27760,   1500,    9640,    0x007C, 0,  22, 0x0000)
    DeclActor(96820,   0,       4294967266, 1200,    96820,   1500,    4294967266, 0x007C, 0,  23, 0x0000)

    ChipFrameInfo(748, 0)                                        # 0

    ScpFunction((
        "Function_0_2EC",          # 00, 0
        "Function_1_3A4",          # 01, 1
        "Function_2_3CF",          # 02, 2
        "Function_3_513",          # 03, 3
        "Function_4_55F",          # 04, 4
        "Function_5_721",          # 05, 5
        "Function_6_A25",          # 06, 6
        "Function_7_C00",          # 07, 7
        "Function_8_DE8",          # 08, 8
        "Function_9_F0B",          # 09, 9
        "Function_10_102E",        # 0A, 10
        "Function_11_10E5",        # 0B, 11
        "Function_12_1178",        # 0C, 12
        "Function_13_1209",        # 0D, 13
        "Function_14_1345",        # 0E, 14
        "Function_15_1DDF",        # 0F, 15
        "Function_16_1DFB",        # 10, 16
        "Function_17_1E86",        # 11, 17
        "Function_18_1EA2",        # 12, 18
        "Function_19_1F1E",        # 13, 19
        "Function_20_1F4C",        # 14, 20
        "Function_21_1F9E",        # 15, 21
        "Function_22_21A7",        # 16, 22
        "Function_23_221E",        # 17, 23
        "Function_24_225E",        # 18, 24
    ))


    def Function_0_2EC(): pass

    label("Function_0_2EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_32C"),
        (1, "loc_338"),
        (2, "loc_344"),
        (3, "loc_350"),
        (4, "loc_35C"),
        (5, "loc_368"),
        (6, "loc_374"),
        (SWITCH_DEFAULT, "loc_380"),
    )


    label("loc_32C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_338")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_344")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_350")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_35C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_368")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_374")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_380")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_3A3")

    Return()

    # Function_0_2EC end

    def Function_1_3A4(): pass

    label("Function_1_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CE")
    OP_94(0xFE, 0xFFFFF542, 0x60E, 0xABE, 0xFFFFFE3E, 0x3E8)
    Sleep(300)
    Jump("Function_1_3A4")

    label("loc_3CE")

    Return()

    # Function_1_3A4 end

    def Function_2_3CF(): pass

    label("Function_2_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_461")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 101660, 0, 21040, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 102720, 0, 19670, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 98850, 0, 20700, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 97500, 0, 21100, 135)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 97890, 0, 19530, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 101520, 0, 18870, 0)
    Jump("loc_4EA")

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_46F")
    Jump("loc_4EA")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_49B")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_4EA")

    label("loc_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_4A9")
    Jump("loc_4EA")

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4B7")
    Jump("loc_4EA")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4C5")
    Jump("loc_4EA")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4D3")
    Jump("loc_4EA")

    label("loc_4D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4E1")
    Jump("loc_4EA")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4EA")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4FE")
    ClearScenarioFlags(0x22, 0)
    Event(0, 14)
    Jump("loc_512")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_512")
    ClearScenarioFlags(0x22, 1)
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_512")

    Return()

    # Function_2_3CF end

    def Function_3_513(): pass

    label("Function_3_513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A")
    OP_7D(0xAA, 0xAA, 0xFF, 0x0, 0x0)

    label("loc_52A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53D")
    OP_1B(0x6, 0x0, 0x15)

    label("loc_53D")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55E")
    ClearMapObjFlags(0x5, 0x10)
    OP_1B(0x8, 0x0, 0x18)
    OP_66(0x1, 0x1)

    label("loc_55E")

    Return()

    # Function_3_513 end

    def Function_4_55F(): pass

    label("Function_4_55F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_6BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_637")

    ChrTalk(
        0x8,
        (
            "#06406FKa'a-chan,\x01",
            "On a theme park alone\x01",
            "I wonder if it has entered.\x02\x03",
            "#06401FAnyway, if something happens\x01",
            "Please contact me soon.\x02\x03",
            "In some cases to the police headquarters\x01",
            "I will ask for support!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6B9")

    label("loc_637")


    ChrTalk(
        0x8,
        (
            "#06406FKa'aa, in the night like this\x01",
            "Is it all right for me?\x02\x03",
            "#06401FAnyway, if something happens\x01",
            "Please contact me soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B9")

    Jump("loc_71D")

    label("loc_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_6CC")
    Jump("loc_71D")

    label("loc_6CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_6DA")
    Jump("loc_71D")

    label("loc_6DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_6EA")
    Jump("loc_71D")

    label("loc_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_6F8")
    Jump("loc_71D")

    label("loc_6F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_706")
    Jump("loc_71D")

    label("loc_706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_714")
    Jump("loc_71D")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_71D")

    label("loc_71D")

    TalkEnd(0xFE)
    Return()

    # Function_4_55F end

    def Function_5_721(): pass

    label("Function_5_721")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_9D2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_737")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CD")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "speak\x01",            # 0
            "Ask for medical treatment\x01",      # 1
            "quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85C")

    ChrTalk(
        0x9,
        (
            "#05900FIf something happen\x01",
            "Please call me soon.\x02\x03",
            "#05903FOnce for the first aid kit\x01",
            "Because I brought it,\x01",
            "I can do something appropriate.\x02\x03",
            "#05901FLloyd, and everyone.\x01",
            "Beware, please be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8DF")

    label("loc_85C")


    ChrTalk(
        0x9,
        (
            "#05903FOnce for the first aid kit\x01",
            "Because I brought it,\x01",
            "I can do something appropriate.\x02\x03",
            "#05901FLloyd, and everyone.\x01",
            "Beware, please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DF")

    Jump("loc_9C8")

    label("loc_8E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x9,
        (
            "#05900FTreat it?\x01",
            "Okay, leave it.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#05900FYes, it's okay.\x01",
            "…. Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C8")

    label("loc_9A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B5")
    Jump("loc_9C8")

    label("loc_9B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C8")
    TalkEnd(0x9)
    Return()

    label("loc_9C8")

    Jump("loc_737")

    label("loc_9CD")

    Jump("loc_A21")

    label("loc_9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_9E0")
    Jump("loc_A21")

    label("loc_9E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_9EE")
    Jump("loc_A21")

    label("loc_9EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_9FC")
    Jump("loc_A21")

    label("loc_9FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A0A")
    Jump("loc_A21")

    label("loc_A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_A18")
    Jump("loc_A21")

    label("loc_A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A21")

    label("loc_A21")

    TalkEnd(0xFE)
    Return()

    # Function_5_721 end

    def Function_6_A25(): pass

    label("Function_6_A25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_BAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20")

    ChrTalk(
        0xA,
        (
            "#01700FIt may be something that we are going through,\x01",
            "We are waiting here.\x02\x03",
            "#01703FZeit君の様子を見ると、\x01",
            "I feel somewhat disgusting … …\x02\x03",
            "#01702FMy younger brother, as soon as that girl\x01",
            "Please find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes……!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_BA8")

    label("loc_B20")


    ChrTalk(
        0xA,
        (
            "#01703FIt may be something that we are going through,\x01",
            "We are waiting here.\x02\x03",
            "#01701FMy younger brother, as soon as that girl\x01",
            "Please find it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA8")

    Jump("loc_BFC")

    label("loc_BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BBB")
    Jump("loc_BFC")

    label("loc_BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_BC9")
    Jump("loc_BFC")

    label("loc_BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_BD7")
    Jump("loc_BFC")

    label("loc_BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BE5")
    Jump("loc_BFC")

    label("loc_BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_BF3")
    Jump("loc_BFC")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BFC")

    label("loc_BFC")

    TalkEnd(0xFE)
    Return()

    # Function_6_A25 end

    def Function_7_C00(): pass

    label("Function_7_C00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_D86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D09")

    ChrTalk(
        0xB,
        "#01803F(… this sign, maybe … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F……Lisha？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01808F…… No, nothing.\x02\x03",
            "#01803FBut just as anything can happen\x01",
            "It may be better to just prepare\x01",
            "It might be nice.\x02\x03",
            "#01801FEveryone, please take care.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_D81")

    label("loc_D09")


    ChrTalk(
        0xB,
        (
            "#01803FWhat seems to happen\x01",
            "It may be better to just prepare\x01",
            "It might be nice.\x02\x03",
            "#01801FEveryone, please take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D81")

    Jump("loc_DE4")

    label("loc_D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D94")
    Jump("loc_DE4")

    label("loc_D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_DA2")
    Jump("loc_DE4")

    label("loc_DA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBA")
    Jump("loc_DBA")

    label("loc_DBA")

    Jump("loc_DE4")

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_DCD")
    Jump("loc_DE4")

    label("loc_DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_DDB")
    Jump("loc_DE4")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DE4")

    label("loc_DE4")

    TalkEnd(0xFE)
    Return()

    # Function_7_C00 end

    def Function_8_DE8(): pass

    label("Function_8_DE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_EB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E77")

    ChrTalk(
        0xC,
        (
            "#04206FThat chubicco, even if I am asleep\x01",
            "The bedclothes are too bad as expected.\x02\x03",
            "#04201FWhere the hell have you gone …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_EB3")

    label("loc_E77")


    ChrTalk(
        0xC,
        (
            "#04201FThat chubicco,\x01",
            "Where the hell have you gone …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB3")

    Jump("loc_F07")

    label("loc_EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_EC6")
    Jump("loc_F07")

    label("loc_EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_ED4")
    Jump("loc_F07")

    label("loc_ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_EE2")
    Jump("loc_F07")

    label("loc_EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_EF0")
    Jump("loc_F07")

    label("loc_EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_EFE")
    Jump("loc_F07")

    label("loc_EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F07")

    label("loc_F07")

    TalkEnd(0xFE)
    Return()

    # Function_8_DE8 end

    def Function_9_F0B(): pass

    label("Function_9_F0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAB")

    ChrTalk(
        0xD,
        "#01201F… …. Gurururu ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F……Zeit、\x01",
            "It seems to be pretty wary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FOh …… Let's be careful.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_FC8")

    label("loc_FAB")


    ChrTalk(
        0xD,
        "#01201F… …. Gurururu ……\x02",
    )

    CloseMessageWindow()

    label("loc_FC8")

    Jump("loc_102A")

    label("loc_FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_FDB")
    Jump("loc_102A")

    label("loc_FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_FE9")
    Jump("loc_102A")

    label("loc_FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_FF7")
    Jump("loc_102A")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1005")
    Jump("loc_102A")

    label("loc_1005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1013")
    Jump("loc_102A")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1021")
    Jump("loc_102A")

    label("loc_1021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_102A")

    label("loc_102A")

    TalkEnd(0xFE)
    Return()

    # Function_9_F0B end

    def Function_10_102E(): pass

    label("Function_10_102E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_10BC")

    ChrTalk(
        0xE,
        (
            "Accessories at a jewelry shop today as well\x01",
            "I bought a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Ho ho …\x01",
            "As for the stress relief as well\x01",
            "Shopping is the best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E1")

    label("loc_10BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_10CA")
    Jump("loc_10E1")

    label("loc_10CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_10D8")
    Jump("loc_10E1")

    label("loc_10D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_10E1")

    label("loc_10E1")

    TalkEnd(0xFE)
    Return()

    # Function_10_102E end

    def Function_11_10E5(): pass

    label("Function_11_10E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_114F")

    ChrTalk(
        0xF,
        (
            "Oops, at the theme park\x01",
            "Looks like we will launch fireworks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Ladies and gentlemen, I will go looking.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1174")

    label("loc_114F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_115D")
    Jump("loc_1174")

    label("loc_115D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_116B")
    Jump("loc_1174")

    label("loc_116B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1174")

    label("loc_1174")

    TalkEnd(0xFE)
    Return()

    # Function_11_10E5 end

    def Function_12_1178(): pass

    label("Function_12_1178")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_11E0")

    ChrTalk(
        0x10,
        (
            "Well, it must go to see\x01",
            "You must not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hehe, it is going to be a nice souvenir.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_11EE")
    Jump("loc_1205")

    label("loc_11EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_11FC")
    Jump("loc_1205")

    label("loc_11FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1205")

    label("loc_1205")

    TalkEnd(0xFE)
    Return()

    # Function_12_1178 end

    def Function_13_1209(): pass

    label("Function_13_1209")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_131C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A6")

    ChrTalk(
        0x11,
        (
            "Sakita, there you are\x01",
            "アルカンシェルのIliaが\x01",
            "I went through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It is not a mistake to see it.\x01",
            "I thought that I came to Michelin …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1317")

    label("loc_12A6")


    ChrTalk(
        0x11,
        (
            "A little while ago\x01",
            "Ilia・プラティエが\x01",
            "I went through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "…… Wow, I'm sorry!\x01",
            "I should have shook hands!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1317")

    Jump("loc_1341")

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_132A")
    Jump("loc_1341")

    label("loc_132A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1338")
    Jump("loc_1341")

    label("loc_1338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1341")

    label("loc_1341")

    TalkEnd(0xFE)
    Return()

    # Function_13_1209 end

    def Function_14_1345(): pass

    label("Function_14_1345")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02751.itc", 0x1E)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x20)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 15)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 0, 0)
    SetChrPos(0x103, 0, 0, 0, 0)
    SetChrPos(0x104, 0, 0, 0, 0)
    SetChrPos(0x109, 0, 0, 0, 0)
    SetChrPos(0x105, 0, 0, 0, 0)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrPos(0xB, 0, 0, 0, 0)
    SetChrPos(0xA, 0, 0, 0, 0)
    SetChrPos(0x9, 0, 0, 0, 0)
    SetChrPos(0xC, 0, 0, 0, 0)
    SetChrPos(0xD, 0, 0, 0, 0)
    OP_68(95850, 100, -10550, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_68(95200, 1200, -9050, 6000)
    MoveCamera(330, 10, 0, 6000)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    BeginChrThread(0x12, 1, 0, 18)
    BeginChrThread(0xD, 3, 0, 16)
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 16)
    OP_0D()
    Sleep(800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xD, 0x3)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0xD, 0x2)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xD, 100000, 0, 7000, 0)
    SetChrPos(0x101, 100000, 0, 7000, 0)
    SetChrPos(0x102, 99500, 0, 6000, 0)
    SetChrPos(0x103, 100500, 0, 6000, 0)
    SetChrPos(0x104, 100000, 0, 5000, 0)
    SetChrPos(0x109, 101000, 0, 4500, 0)
    SetChrPos(0x105, 99000, 0, 4500, 0)
    SetChrPos(0x8, 99000, 0, 7000, 0)
    SetChrPos(0xA, 100000, 0, 7000, 0)
    SetChrPos(0x9, 101000, 0, 7000, 0)
    SetChrPos(0xB, 100500, 0, 6000, 0)
    SetChrPos(0xC, 99500, 0, 6000, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(100000, 1000, 22000, 0)
    OP_68(100110, 1000, 18460, 8000)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x12, 1, 0, 19)
    BeginChrThread(0xD, 3, 0, 17)
    Sleep(2000)

    def lambda_188A():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_188A)
    Sleep(50)

    def lambda_18A2():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18A2)
    Sleep(50)

    def lambda_18BA():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18BA)
    Sleep(50)

    def lambda_18D2():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18D2)
    Sleep(50)

    def lambda_18EA():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18EA)
    Sleep(50)

    def lambda_1902():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1902)
    Sleep(2000)

    def lambda_191A():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_191A)
    Sleep(200)

    def lambda_1932():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1932)
    Sleep(200)

    def lambda_194A():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_194A)
    Sleep(200)

    def lambda_1962():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1962)
    Sleep(200)

    def lambda_197A():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_197A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 3)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#01203F#5P… …. Gurrule ………\x02\x03",
            "#01201FGuru …… Won.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6P\"─ ─ It's over there.\x01",
            "But be careful. \"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01705F#6PThe\x01",
            "But I do not see it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PWell, but be careful …\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00006F#11P……no time.\x01",
            "Anyway let's go.\x02\x03",
            "#00003FFranc、Cecil姉、\x01",
            "それとIliaさんたち……\x02\x03",
            "#00001FEveryone here\x01",
            "Please wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#04207F#6PBut, it is …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01703F#6P…… Well, it can not be helped.\x01",
            "It might be daunting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#05901F#6PBut if something happens\x01",
            "Please call me soon.\x02\x03",
            "Once for the first aid kit\x01",
            "Because I have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11POh, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01803F#6P……everyone.\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06401F#6PWhen it comes to an enigma\x01",
            "Please contact me ~!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xD, 0x0)
    SetChrSubChip(0xD, 0x0)
    OP_49()
    OP_D7(0x1E)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0x8, 97000, 0, 20000, 90)
    SetChrPos(0x9, 97000, 0, 19000, 90)
    SetChrPos(0xA, 97000, 0, 18000, 90)
    SetChrPos(0xB, 97000, 0, 17000, 90)
    SetChrPos(0xC, 97000, 0, 16000, 90)
    SetChrPos(0xD, 97000, 0, 15000, 90)
    SetChrPos(0x0, 99620, 0, 22780, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xD, 101660, 0, 21040, 0)
    SetChrPos(0x8, 102720, 0, 19670, 0)
    SetChrPos(0xB, 98850, 0, 20700, 270)
    SetChrPos(0xA, 97500, 0, 21100, 135)
    SetChrPos(0x9, 97890, 0, 19530, 0)
    SetChrPos(0xC, 101520, 0, 18870, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    BeginChrThread(0xD, 0, 0, 0)
    SetScenarioFlags(0x146, 0)
    OP_29(0xA5, 0x1, 0x9)
    OP_32(0xFF, 0xFF, 0x0)
    OP_1B(0x8, 0x0, 0x18)
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x5, 0x10)
    EventEnd(0x5)
    Return()

    # Function_14_1345 end

    def Function_15_1DDF(): pass

    label("Function_15_1DDF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DFA")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_15_1DDF")

    label("loc_1DFA")

    Return()

    # Function_15_1DDF end

    def Function_16_1DFB(): pass

    label("Function_16_1DFB")

    SetChrPos(0xFE, 92740, 1900, -9330, 0)

    def lambda_1E11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E11)
    OP_95(0xFE, 92800, 1300, -11030, 4000, 0x1)
    OP_95(0xFE, 94740, 200, -13790, 4000, 0x1)
    OP_95(0xFE, 98460, 100, -13380, 4000, 0x1)
    OP_95(0xFE, 100000, 0, -8700, 4000, 0x1)
    OP_95(0xFE, 100000, 0, 10000, 4000, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_1DFB end

    def Function_17_1E86(): pass

    label("Function_17_1E86")

    OP_9B(0x1, 0xFE, 0xA, 0x32C8, 0xFA0, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_1E86 end

    def Function_18_1EA2(): pass

    label("Function_18_1EA2")

    Sound(845, 0, 20, 0)
    Sleep(450)
    Sound(845, 0, 25, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 25, 0)
    Sleep(450)
    Sound(845, 0, 20, 0)
    Sleep(450)
    Sound(845, 0, 15, 0)
    Sleep(450)
    Sound(845, 0, 10, 0)
    Sleep(450)
    Sound(845, 0, 5, 0)
    Return()

    # Function_18_1EA2 end

    def Function_19_1F1E(): pass

    label("Function_19_1F1E")

    Sleep(1550)
    Sound(845, 0, 20, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Sleep(450)
    Sound(845, 0, 30, 0)
    Return()

    # Function_19_1F1E end

    def Function_20_1F4C(): pass

    label("Function_20_1F4C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-17890, 1600, 9710, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17250, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -18950, 0, 10980, 180)
    EventEnd(0x5)
    Return()

    # Function_20_1F4C end

    def Function_21_1F9E(): pass

    label("Function_21_1F9E")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213B")

    ChrTalk(
        0x101,
        (
            "#00003FLake beach at night\x01",
            "It looks like it is not open.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_202D")

    ChrTalk(
        0x102,
        (
            "#00100FYes, it is\x01",
            "Let's stop it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2133")

    label("loc_202D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_2079")

    ChrTalk(
        0x103,
        (
            "#00200FIt might be better to stop entering\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2133")

    label("loc_2079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_20AC")

    ChrTalk(
        0x104,
        "#00300FLet's stop entering.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2133")

    label("loc_20AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_20EC")

    ChrTalk(
        0x109,
        (
            "#10100FIt is better to stop entering\x01",
            "Looks nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2133")

    label("loc_20EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_2133")

    ChrTalk(
        0x105,
        (
            "#10300FWell, the one who stopped entering\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2133")

    SetScenarioFlags(0x1, 1)
    Jump("loc_2190")

    label("loc_213B")


    ChrTalk(
        0x101,
        (
            "#00003FLake beach at night\x01",
            "It seems not to be operating.\x01",
            "… … let's stop entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2190")

    Sleep(50)
    SetChrPos(0x0, 28500, 0, 8080, 270)
    EventEnd(0x4)
    Return()

    # Function_21_1F9E end

    def Function_22_21A7(): pass

    label("Function_22_21A7")

    EventBegin(0x2)
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "The opening of the Lake bathhouse has ended.\x01",
            "We are waiting for you to come again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_22_21A7 end

    def Function_23_221E(): pass

    label("Function_23_221E")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_23_221E end

    def Function_24_225E(): pass

    label("Function_24_225E")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F- It is too late at night.\x01",
            "Let's hurry to the theme park.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100200, 0, -4830, 0)
    EventEnd(0x4)
    Return()

    # Function_24_225E end

    SaveToFile()

Try(main)
