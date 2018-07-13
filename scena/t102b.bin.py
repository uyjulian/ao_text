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
        "Function_5_743",          # 05, 5
        "Function_6_A7E",          # 06, 6
        "Function_7_C47",          # 07, 7
        "Function_8_DFD",          # 08, 8
        "Function_9_F3D",          # 09, 9
        "Function_10_105C",        # 0A, 10
        "Function_11_1138",        # 0B, 11
        "Function_12_11CC",        # 0C, 12
        "Function_13_1259",        # 0D, 13
        "Function_14_138B",        # 0E, 14
        "Function_15_1E34",        # 0F, 15
        "Function_16_1E50",        # 10, 16
        "Function_17_1EDB",        # 11, 17
        "Function_18_1EF7",        # 12, 18
        "Function_19_1F73",        # 13, 19
        "Function_20_1FA1",        # 14, 20
        "Function_21_1FF3",        # 15, 21
        "Function_22_21E8",        # 16, 22
        "Function_23_226B",        # 17, 23
        "Function_24_22A6",        # 18, 24
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_6E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_641")

    ChrTalk(
        0x8,
        (
            "#06406FHas KeA entered\x01",
            "the theme park\x01",
            "alone, I wonder?\x02\x03",
            "#06401FA-At any rate, please call me\x01",
            "immediately if something happens.\x02\x03",
            "Depending on the situation,\x01",
            "I'll request police HQ for backup!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6DB")

    label("loc_641")


    ChrTalk(
        0x8,
        (
            "#06406FI wonder if KeA is going to be\x01",
            "all right alone in such dead of night.\x02\x03",
            "#06401FA-At any rate, please call me\x01",
            "immediately if something happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DB")

    Jump("loc_73F")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_6EE")
    Jump("loc_73F")

    label("loc_6EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_6FC")
    Jump("loc_73F")

    label("loc_6FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_70C")
    Jump("loc_73F")

    label("loc_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_71A")
    Jump("loc_73F")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_728")
    Jump("loc_73F")

    label("loc_728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_736")
    Jump("loc_73F")

    label("loc_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_73F")

    label("loc_73F")

    TalkEnd(0xFE)
    Return()

    # Function_4_55F end

    def Function_5_743(): pass

    label("Function_5_743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_A2B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_759")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A26")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Ask for Treatment\x01",      # 1
            "Quit\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_935")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89E")

    ChrTalk(
        0x9,
        (
            "#05900FIf something happens,\x01",
            "please call me immediately.\x02\x03",
            "#05903FI will bring you at least\x01",
            "a first-aid kit with which\x01",
            "I can moderately treat you.\x02\x03",
            "#05901FLloyd, and everyone,\x01",
            "please be very careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_930")

    label("loc_89E")


    ChrTalk(
        0x9,
        (
            "#05903FI will bring you at least\x01",
            "a first-aid kit with which\x01",
            "I can moderately treat you.\x02\x03",
            "#05901FLloyd, and everyone,\x01",
            "please be very careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_930")

    Jump("loc_A21")

    label("loc_935")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x9,
        (
            "#05900FTreatment, right?\x01",
            "Alright, leave it to me.\x02",
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
            "...Please be very careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A21")

    label("loc_9FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0E")
    Jump("loc_A21")

    label("loc_A0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A21")
    TalkEnd(0x9)
    Return()

    label("loc_A21")

    Jump("loc_759")

    label("loc_A26")

    Jump("loc_A7A")

    label("loc_A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A39")
    Jump("loc_A7A")

    label("loc_A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_A47")
    Jump("loc_A7A")

    label("loc_A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_A55")
    Jump("loc_A7A")

    label("loc_A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A63")
    Jump("loc_A7A")

    label("loc_A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_A71")
    Jump("loc_A7A")

    label("loc_A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A7A")

    label("loc_A7A")

    TalkEnd(0xFE)
    Return()

    # Function_5_743 end

    def Function_6_A7E(): pass

    label("Function_6_A7E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_BF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B75")

    ChrTalk(
        0xA,
        (
            "#01700FWe could be a hindrance for you,\x01",
            "so we'll wait here.\x02\x03",
            "#01703FJudging by Zeit's behavior,\x01",
            "I've somehow got a bad presentiment...\x02\x03",
            "#01702FYounger brother, go find\x01",
            "that kid on the double.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_BEF")

    label("loc_B75")


    ChrTalk(
        0xA,
        (
            "#01703FWe could be a hindrance for you,\x01",
            "so we'll wait here.\x02\x03",
            "#01701FYounger brother, go find\x01",
            "that kid on the double.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEF")

    Jump("loc_C43")

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C02")
    Jump("loc_C43")

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_C10")
    Jump("loc_C43")

    label("loc_C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_C1E")
    Jump("loc_C43")

    label("loc_C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C2C")
    Jump("loc_C43")

    label("loc_C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_C3A")
    Jump("loc_C43")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C43")

    label("loc_C43")

    TalkEnd(0xFE)
    Return()

    # Function_6_A7E end

    def Function_7_C47(): pass

    label("Function_7_C47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_D9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D33")

    ChrTalk(
        0xB,
        "#01803F(...This presence, could it be...)\x02",
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
            "#01803FHowever, you should\x01",
            "be prepared in case\x01",
            "something happens.\x02\x03",
            "#01801FEveryone, please be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_D96")

    label("loc_D33")


    ChrTalk(
        0xB,
        (
            "#01803FYou should be\x01",
            "prepared in case\x01",
            "something happens.\x02\x03",
            "#01801FEveryone, please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D96")

    Jump("loc_DF9")

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_DA9")
    Jump("loc_DF9")

    label("loc_DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_DB7")
    Jump("loc_DF9")

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_DD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCF")
    Jump("loc_DCF")

    label("loc_DCF")

    Jump("loc_DF9")

    label("loc_DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_DE2")
    Jump("loc_DF9")

    label("loc_DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_DF0")
    Jump("loc_DF9")

    label("loc_DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DF9")

    label("loc_DF9")

    TalkEnd(0xFE)
    Return()

    # Function_7_C47 end

    def Function_8_DFD(): pass

    label("Function_8_DFD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_EEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA5")

    ChrTalk(
        0xC,
        (
            "#04206FThat shorty, even when half asleep\x01",
            "she's really too much of an untidy sleeper.\x02\x03",
            "#04201FWhere the heck sould she have gone...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_EE5")

    label("loc_EA5")


    ChrTalk(
        0xC,
        (
            "#04201FThat shorty,\x01",
            "where the heck sould she have gone...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE5")

    Jump("loc_F39")

    label("loc_EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_EF8")
    Jump("loc_F39")

    label("loc_EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_F06")
    Jump("loc_F39")

    label("loc_F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_F14")
    Jump("loc_F39")

    label("loc_F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_F22")
    Jump("loc_F39")

    label("loc_F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_F30")
    Jump("loc_F39")

    label("loc_F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F39")

    label("loc_F39")

    TalkEnd(0xFE)
    Return()

    # Function_8_DFD end

    def Function_9_F3D(): pass

    label("Function_9_F3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_FFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDC")

    ChrTalk(
        0xD,
        "#01201F...Grrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F...It seems that Zeit is\x01",
            "being quite vigilant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYeah...let's proceed carefully.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_FF6")

    label("loc_FDC")


    ChrTalk(
        0xD,
        "#01201F...Grrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_FF6")

    Jump("loc_1058")

    label("loc_FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1009")
    Jump("loc_1058")

    label("loc_1009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1017")
    Jump("loc_1058")

    label("loc_1017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1025")
    Jump("loc_1058")

    label("loc_1025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1033")
    Jump("loc_1058")

    label("loc_1033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1041")
    Jump("loc_1058")

    label("loc_1041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_104F")
    Jump("loc_1058")

    label("loc_104F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1058")

    label("loc_1058")

    TalkEnd(0xFE)
    Return()

    # Function_9_F3D end

    def Function_10_105C(): pass

    label("Function_10_105C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_110F")

    ChrTalk(
        0xE,
        (
            "Today too I ended up purchasing a\x01",
            "lot of accessories at the jewelry shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Ho ho ho...\x01",
            "There's really nothing better than\x01",
            "shopping as a stress reliever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1134")

    label("loc_110F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_111D")
    Jump("loc_1134")

    label("loc_111D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_112B")
    Jump("loc_1134")

    label("loc_112B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1134")

    label("loc_1134")

    TalkEnd(0xFE)
    Return()

    # Function_10_105C end

    def Function_11_1138(): pass

    label("Function_11_1138")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_11A3")

    ChrTalk(
        0xF,
        (
            "Oh, it seems they're shooting\x01",
            "fireworks at the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Honey, let's go see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11C8")

    label("loc_11A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_11B1")
    Jump("loc_11C8")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_11BF")
    Jump("loc_11C8")

    label("loc_11BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11C8")

    label("loc_11C8")

    TalkEnd(0xFE)
    Return()

    # Function_11_1138 end

    def Function_12_11CC(): pass

    label("Function_12_11CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1230")

    ChrTalk(
        0x10,
        (
            "Well, we have to\x01",
            "go see them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Uh uh, it seems they'll be a nice present.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1255")

    label("loc_1230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_123E")
    Jump("loc_1255")

    label("loc_123E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_124C")
    Jump("loc_1255")

    label("loc_124C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1255")

    label("loc_1255")

    TalkEnd(0xFE)
    Return()

    # Function_12_11CC end

    def Function_13_1259(): pass

    label("Function_13_1259")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F5")

    ChrTalk(
        0x11,
        (
            "J-Just now Ilya from\x01",
            "Arc-en-ciel passed\x01",
            "through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I-I haven't misjudged, eh?\x01",
            "To think she'd come to Michelam...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_135D")

    label("loc_12F5")


    ChrTalk(
        0x11,
        (
            "Just now Ilya\x01",
            "Platiｲre passed\x01",
            "through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...Uwooh, dammit!\x01",
            "I should've gotten a handshake!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135D")

    Jump("loc_1387")

    label("loc_1362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1370")
    Jump("loc_1387")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_137E")
    Jump("loc_1387")

    label("loc_137E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1387")

    label("loc_1387")

    TalkEnd(0xFE)
    Return()

    # Function_13_1259 end

    def Function_14_138B(): pass

    label("Function_14_138B")

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

    def lambda_18D0():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18D0)
    Sleep(50)

    def lambda_18E8():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18E8)
    Sleep(50)

    def lambda_1900():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1900)
    Sleep(50)

    def lambda_1918():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1918)
    Sleep(50)

    def lambda_1930():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1930)
    Sleep(50)

    def lambda_1948():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1948)
    Sleep(2000)

    def lambda_1960():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1960)
    Sleep(200)

    def lambda_1978():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1978)
    Sleep(200)

    def lambda_1990():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1990)
    Sleep(200)

    def lambda_19A8():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_19A8)
    Sleep(200)

    def lambda_19C0():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19C0)
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
            "#01201FGrrowl...woof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6P"──Over there.\x01",
            "But be careful."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01705F#6P*haah*...\x01",
            "You understand him really well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PB-But, he said to be careful...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00006F#11P...There's no time.\x01",
            "In any case, let's go.\x02\x03",
            "#00003FFran, sister Cecil,\x01",
            "Miss Ilya, Sully, Rixia...\x02\x03",
            "#00001FPlease wait\x01",
            "here for us.\x02",
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
            "#01703F#6P...Well, it can't be helped.\x01",
            "We could be a hindrance for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#05901F#6PBut, if something happens,\x01",
            "please call me immediately.\x02\x03",
            "I'll bring you at least\x01",
            "a first-aid kit.\x02",
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
            "#01803F#6P...Everyone, \x01",
            "please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06401F#6PPlease call me with the ENIGMA\x01",
            "in case of emergency!\x02",
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

    # Function_14_138B end

    def Function_15_1E34(): pass

    label("Function_15_1E34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E4F")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_15_1E34")

    label("loc_1E4F")

    Return()

    # Function_15_1E34 end

    def Function_16_1E50(): pass

    label("Function_16_1E50")

    SetChrPos(0xFE, 92740, 1900, -9330, 0)

    def lambda_1E66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E66)
    OP_95(0xFE, 92800, 1300, -11030, 4000, 0x1)
    OP_95(0xFE, 94740, 200, -13790, 4000, 0x1)
    OP_95(0xFE, 98460, 100, -13380, 4000, 0x1)
    OP_95(0xFE, 100000, 0, -8700, 4000, 0x1)
    OP_95(0xFE, 100000, 0, 10000, 4000, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_1E50 end

    def Function_17_1EDB(): pass

    label("Function_17_1EDB")

    OP_9B(0x1, 0xFE, 0xA, 0x32C8, 0xFA0, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_1EDB end

    def Function_18_1EF7(): pass

    label("Function_18_1EF7")

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

    # Function_18_1EF7 end

    def Function_19_1F73(): pass

    label("Function_19_1F73")

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

    # Function_19_1F73 end

    def Function_20_1FA1(): pass

    label("Function_20_1FA1")

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

    # Function_20_1FA1 end

    def Function_21_1FF3(): pass

    label("Function_21_1FF3")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_21D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2177")

    ChrTalk(
        0x101,
        (
            "#00003FIt seems the Lake Beach\x01",
            "is not open at night.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_2079")

    ChrTalk(
        0x102,
        (
            "#00100FYes, let's not\x01",
            "enter inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_216F")

    label("loc_2079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_20C2")

    ChrTalk(
        0x103,
        (
            "#00200FMaybe it should be better\x01",
            "to not enter inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_216F")

    label("loc_20C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_20EE")

    ChrTalk(
        0x104,
        "#00300FLet's not get in.\x02",
    )

    CloseMessageWindow()
    Jump("loc_216F")

    label("loc_20EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_212D")

    ChrTalk(
        0x109,
        (
            "#10100FIt seems better to not\x01",
            "enter inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_216F")

    label("loc_212D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_216F")

    ChrTalk(
        0x105,
        (
            "#10300FWell, maybe it would be\x01",
            "better to not enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_216F")

    SetScenarioFlags(0x1, 1)
    Jump("loc_21D1")

    label("loc_2177")


    ChrTalk(
        0x101,
        (
            "#00003FIt seems the Lake Beach\x01",
            "is not open at night.\x01",
            "...Let's refrain from entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D1")

    Sleep(50)
    SetChrPos(0x0, 28500, 0, 8080, 270)
    EventEnd(0x4)
    Return()

    # Function_21_1FF3 end

    def Function_22_21E8(): pass

    label("Function_22_21E8")

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
            "The Lake Beach is closed for the day.\x01",
            "We look forward to serving you again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_22_21E8 end

    def Function_23_226B(): pass

    label("Function_23_226B")

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

    # Function_23_226B end

    def Function_24_22A6(): pass

    label("Function_24_22A6")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F...It's already night and considerably late.\x01",
            "Let's hurry to the theme park area.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100200, 0, -4830, 0)
    EventEnd(0x4)
    Return()

    # Function_24_22A6 end

    SaveToFile()

Try(main)
