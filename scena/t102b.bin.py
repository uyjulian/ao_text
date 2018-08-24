from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Fran",                   # 1
        "Cecil",                  # 2
        "Ilya",                   # 3
        "Rixia",                  # 4
        "Sully",                  # 5
        "Zeit",                   # 6
        "Elise",                  # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "SE制御",                 # 11
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
        "Function_5_726",          # 05, 5
        "Function_6_A87",          # 06, 6
        "Function_7_C4A",          # 07, 7
        "Function_8_E09",          # 08, 8
        "Function_9_F30",          # 09, 9
        "Function_10_104D",        # 0A, 10
        "Function_11_112A",        # 0B, 11
        "Function_12_11C3",        # 0C, 12
        "Function_13_1251",        # 0D, 13
        "Function_14_1378",        # 0E, 14
        "Function_15_1E07",        # 0F, 15
        "Function_16_1E23",        # 10, 16
        "Function_17_1EAE",        # 11, 17
        "Function_18_1ECA",        # 12, 18
        "Function_19_1F46",        # 13, 19
        "Function_20_1F74",        # 14, 20
        "Function_21_1FC6",        # 15, 21
        "Function_22_2198",        # 16, 22
        "Function_23_2217",        # 17, 23
        "Function_24_2252",        # 18, 24
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_6C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_631")

    ChrTalk(
        0x8,
        (
            "#06406FI wonder if KeA has\x01",
            "entered the park alone.\x02\x03",
            "#06401FA-Anyway, call me\x01",
            "immediately if anything\x01",
            "happens.\x02\x03",
            "Depending on the\x01",
            "situation, I'll request\x01",
            "backup from police HQ!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6BE")

    label("loc_631")


    ChrTalk(
        0x8,
        (
            "#06406FI wonder if KeA is going\x01",
            "to be all right alone in\x01",
            "such dead of night.\x02\x03",
            "#06401FA-Anyway, call me\x01",
            "immediately if anything\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE")

    Jump("loc_722")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_6D1")
    Jump("loc_722")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_6DF")
    Jump("loc_722")

    label("loc_6DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_6EF")
    Jump("loc_722")

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_6FD")
    Jump("loc_722")

    label("loc_6FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_70B")
    Jump("loc_722")

    label("loc_70B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_719")
    Jump("loc_722")

    label("loc_719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_722")

    label("loc_722")

    TalkEnd(0xFE)
    Return()

    # Function_4_55F end

    def Function_5_726(): pass

    label("Function_5_726")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_A34")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Ask for treatment\x01",      # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_942")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892")

    ChrTalk(
        0x9,
        (
            "#05900FCall me right away if anything\x01",
            "happens.\x02\x03",
            "#05903FI brought a first-aid kit with me\x01",
            "just in case, so I'll be able to\x01",
            "provide some level of treatment.\x02\x03",
            "#05901FLloyd, and everyone else too. Be\x01",
            "very careful, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_93D")

    label("loc_892")


    ChrTalk(
        0x9,
        (
            "#05903FI brought a first-aid kit with me\x01",
            "just in case, so I'll be able to\x01",
            "provide some level of treatment.\x02\x03",
            "#05901FLloyd, and everyone else too. Be\x01",
            "very careful, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93D")

    Jump("loc_A2A")

    label("loc_942")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A03")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x9,
        (
            "#05900FTreatment, right?\x01",
            "Understood, leave it to\x01",
            "me.\x02",
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
            "#05900FYes, you're fine now.\x01",
            "...Be very careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2A")

    label("loc_A03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A17")
    Jump("loc_A2A")

    label("loc_A17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A2A")
    TalkEnd(0x9)
    Return()

    label("loc_A2A")

    Jump("loc_73C")

    label("loc_A2F")

    Jump("loc_A83")

    label("loc_A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A42")
    Jump("loc_A83")

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_A50")
    Jump("loc_A83")

    label("loc_A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_A5E")
    Jump("loc_A83")

    label("loc_A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A6C")
    Jump("loc_A83")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_A7A")
    Jump("loc_A83")

    label("loc_A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A83")

    label("loc_A83")

    TalkEnd(0xFE)
    Return()

    # Function_5_726 end

    def Function_6_A87(): pass

    label("Function_6_A87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7B")

    ChrTalk(
        0xA,
        (
            "#01700FWe might get in your way,\x01",
            "so we'll wait here.\x02\x03",
            "#01703FBased on how Zeit's\x01",
            "acting, I'm getting a bad\x01",
            "feeling about this...\x02\x03",
            "#01702FLittle bro, please find\x01",
            "that kid as fast as you\x01",
            "can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FRight!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_BF2")

    label("loc_B7B")


    ChrTalk(
        0xA,
        (
            "#01703FWe might get in your\x01",
            "way, so we'll wait here.\x02\x03",
            "#01701FLittle bro, please find\x01",
            "that kid as fast as you\x01",
            "can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF2")

    Jump("loc_C46")

    label("loc_BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C05")
    Jump("loc_C46")

    label("loc_C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_C13")
    Jump("loc_C46")

    label("loc_C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_C21")
    Jump("loc_C46")

    label("loc_C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C2F")
    Jump("loc_C46")

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_C3D")
    Jump("loc_C46")

    label("loc_C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C46")

    label("loc_C46")

    TalkEnd(0xFE)
    Return()

    # Function_6_A87 end

    def Function_7_C4A(): pass

    label("Function_7_C4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_DA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3B")

    ChrTalk(
        0xB,
        (
            "#01803F(...This presence, could\x01",
            "it be...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F...Rixia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01808F...No, it's nothing.\x02\x03",
            "#01803FHowever, you should be\x01",
            "prepared in case\x01",
            "something does happen.\x02\x03",
            "#01801FEveryone, please be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_DA2")

    label("loc_D3B")


    ChrTalk(
        0xB,
        (
            "#01803FYou should be prepared\x01",
            "in case something does\x01",
            "happen.\x02\x03",
            "#01801FEveryone, please be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA2")

    Jump("loc_E05")

    label("loc_DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_DB5")
    Jump("loc_E05")

    label("loc_DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_DC3")
    Jump("loc_E05")

    label("loc_DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_DE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDB")
    Jump("loc_DDB")

    label("loc_DDB")

    Jump("loc_E05")

    label("loc_DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_DEE")
    Jump("loc_E05")

    label("loc_DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_DFC")
    Jump("loc_E05")

    label("loc_DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E05")

    label("loc_E05")

    TalkEnd(0xFE)
    Return()

    # Function_7_C4A end

    def Function_8_E09(): pass

    label("Function_8_E09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_EDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAE")

    ChrTalk(
        0xC,
        (
            "#04206FThat shorty. Even if she's\x01",
            "half asleep she tosses and\x01",
            "turns way too much.\x02\x03",
            "#04201FAnd where the heck should\x01",
            "she have gone?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_ED8")

    label("loc_EAE")


    ChrTalk(
        0xC,
        (
            "#04201FWhere the heck did\x01",
            "shorty go?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED8")

    Jump("loc_F2C")

    label("loc_EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_EEB")
    Jump("loc_F2C")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_EF9")
    Jump("loc_F2C")

    label("loc_EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_F07")
    Jump("loc_F2C")

    label("loc_F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_F15")
    Jump("loc_F2C")

    label("loc_F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_F23")
    Jump("loc_F2C")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F2C")

    label("loc_F2C")

    TalkEnd(0xFE)
    Return()

    # Function_8_E09 end

    def Function_9_F30(): pass

    label("Function_9_F30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_FEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCE")

    ChrTalk(
        0xD,
        "#01201F...Grrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F...It seems Zeit is\x01",
            "being rather cautious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah... Let's proceed\x01",
            "with caution.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_FE7")

    label("loc_FCE")


    ChrTalk(
        0xD,
        "#01201F...Grrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_FE7")

    Jump("loc_1049")

    label("loc_FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_FFA")
    Jump("loc_1049")

    label("loc_FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1008")
    Jump("loc_1049")

    label("loc_1008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1016")
    Jump("loc_1049")

    label("loc_1016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1024")
    Jump("loc_1049")

    label("loc_1024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1032")
    Jump("loc_1049")

    label("loc_1032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1040")
    Jump("loc_1049")

    label("loc_1040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1049")

    label("loc_1049")

    TalkEnd(0xFE)
    Return()

    # Function_9_F30 end

    def Function_10_104D(): pass

    label("Function_10_104D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1101")

    ChrTalk(
        0xE,
        (
            "I ended up purchasing a\x01",
            "lot of accessories at the\x01",
            "jewelry shop again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hohoho... As a stress\x01",
            "reliever, there's really\x01",
            "nothing better than shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1126")

    label("loc_1101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_110F")
    Jump("loc_1126")

    label("loc_110F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_111D")
    Jump("loc_1126")

    label("loc_111D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1126")

    label("loc_1126")

    TalkEnd(0xFE)
    Return()

    # Function_10_104D end

    def Function_11_112A(): pass

    label("Function_11_112A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_119A")

    ChrTalk(
        0xF,
        (
            "Oh, it seems they're\x01",
            "shooting fireworks at\x01",
            "the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Honey, let's go see\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BF")

    label("loc_119A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_11A8")
    Jump("loc_11BF")

    label("loc_11A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_11B6")
    Jump("loc_11BF")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11BF")

    label("loc_11BF")

    TalkEnd(0xFE)
    Return()

    # Function_11_112A end

    def Function_12_11C3(): pass

    label("Function_12_11C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1228")

    ChrTalk(
        0x10,
        (
            "Well, we have to go see\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Haha, it seems they'll\x01",
            "make a nice present.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_124D")

    label("loc_1228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1236")
    Jump("loc_124D")

    label("loc_1236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1244")
    Jump("loc_124D")

    label("loc_1244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_124D")

    label("loc_124D")

    TalkEnd(0xFE)
    Return()

    # Function_12_11C3 end

    def Function_13_1251(): pass

    label("Function_13_1251")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_134F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E5")

    ChrTalk(
        0x11,
        (
            "Ilya from Arc-en-Ciel\x01",
            "passed by just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I-I'm not seeing things,\x01",
            "am I? To think she'd\x01",
            "come to Michelam...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_134A")

    label("loc_12E5")


    ChrTalk(
        0x11,
        (
            "Just now Ilya Platiｲre\x01",
            "passed through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...Uwooh, dammit! I\x01",
            "should've shaken her\x01",
            "hand!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134A")

    Jump("loc_1374")

    label("loc_134F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_135D")
    Jump("loc_1374")

    label("loc_135D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_136B")
    Jump("loc_1374")

    label("loc_136B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1374")

    label("loc_1374")

    TalkEnd(0xFE)
    Return()

    # Function_13_1251 end

    def Function_14_1378(): pass

    label("Function_14_1378")

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

    def lambda_18BD():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18BD)
    Sleep(50)

    def lambda_18D5():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18D5)
    Sleep(50)

    def lambda_18ED():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18ED)
    Sleep(50)

    def lambda_1905():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1905)
    Sleep(50)

    def lambda_191D():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_191D)
    Sleep(50)

    def lambda_1935():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1935)
    Sleep(2000)

    def lambda_194D():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_194D)
    Sleep(200)

    def lambda_1965():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1965)
    Sleep(200)

    def lambda_197D():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_197D)
    Sleep(200)

    def lambda_1995():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1995)
    Sleep(200)

    def lambda_19AD():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19AD)
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
            "#01203F#5P...Grrrowl...\x02\x03",
            "#01201FGrrowl... Woof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6P"─Over there. But be\x01",
            "careful."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01705F#6P*sigh*... But you\x01",
            "understand him really\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PB-But, he said to be\x01",
            "careful...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00006F#11P...There's no time.\x01",
            "Anyway, let's go.\x02\x03",
            "#00003FFran, Cecil, Ilya,\x01",
            "Sully, Rixia...\x02\x03",
            "#00001FPlease wait here for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#04207F#6PB-But...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01703F#6P...Well, it can't be\x01",
            "helped. We could be a\x01",
            "hindrance for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#05901F#6PBut if something\x01",
            "happens, please call me\x01",
            "immediately.\x02\x03",
            "I brought a first-aid\x01",
            "kit just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PYeah, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01803F#6P...Everyone, please be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06401F#6PContact me via ENIGMA in\x01",
            "case of emergency!\x02",
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

    # Function_14_1378 end

    def Function_15_1E07(): pass

    label("Function_15_1E07")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E22")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_15_1E07")

    label("loc_1E22")

    Return()

    # Function_15_1E07 end

    def Function_16_1E23(): pass

    label("Function_16_1E23")

    SetChrPos(0xFE, 92740, 1900, -9330, 0)

    def lambda_1E39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E39)
    OP_95(0xFE, 92800, 1300, -11030, 4000, 0x1)
    OP_95(0xFE, 94740, 200, -13790, 4000, 0x1)
    OP_95(0xFE, 98460, 100, -13380, 4000, 0x1)
    OP_95(0xFE, 100000, 0, -8700, 4000, 0x1)
    OP_95(0xFE, 100000, 0, 10000, 4000, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_1E23 end

    def Function_17_1EAE(): pass

    label("Function_17_1EAE")

    OP_9B(0x1, 0xFE, 0xA, 0x32C8, 0xFA0, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_1EAE end

    def Function_18_1ECA(): pass

    label("Function_18_1ECA")

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

    # Function_18_1ECA end

    def Function_19_1F46(): pass

    label("Function_19_1F46")

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

    # Function_19_1F46 end

    def Function_20_1F74(): pass

    label("Function_20_1F74")

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

    # Function_20_1F74 end

    def Function_21_1FC6(): pass

    label("Function_21_1FC6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212C")

    ChrTalk(
        0x101,
        (
            "#00003FIt seems Lake Beach\x01",
            "isn't open at night.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_2040")

    ChrTalk(
        0x102,
        "#00100FYes, let's not enter.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2124")

    label("loc_2040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_2077")

    ChrTalk(
        0x103,
        (
            "#00200FIt may be best not to\x01",
            "enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2124")

    label("loc_2077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_20A2")

    ChrTalk(
        0x104,
        "#00300FLet's not go in.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2124")

    label("loc_20A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_20E4")

    ChrTalk(
        0x109,
        (
            "#10100FIt seems best to refrain\x01",
            "from entering.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2124")

    label("loc_20E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_2124")

    ChrTalk(
        0x105,
        (
            "#10300FWell, maybe it would be\x01",
            "best not to enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2124")

    SetScenarioFlags(0x1, 1)
    Jump("loc_2181")

    label("loc_212C")


    ChrTalk(
        0x101,
        (
            "#00003FIt seems Lake Beach isn't\x01",
            "open at night. ...Let's\x01",
            "refrain from entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2181")

    Sleep(50)
    SetChrPos(0x0, 28500, 0, 8080, 270)
    EventEnd(0x4)
    Return()

    # Function_21_1FC6 end

    def Function_22_2198(): pass

    label("Function_22_2198")

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
            "Lake Beach is closed for\x01",
            "the day. We look forward\x01",
            "to serving you again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_22_2198 end

    def Function_23_2217(): pass

    label("Function_23_2217")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_23_2217 end

    def Function_24_2252(): pass

    label("Function_24_2252")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FIt's the middle of the\x01",
            "night. Let's hurry to\x01",
            "the theme park.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100200, 0, -4830, 0)
    EventEnd(0x4)
    Return()

    # Function_24_2252 end

    SaveToFile()

Try(main)
