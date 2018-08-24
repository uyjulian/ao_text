from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c013b.bin",                # FileName
        "c013b",                    # MapName
        "c013b",                    # Location
        0x0009,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 0, 0, 1],
    )

    BuildStringList((
        "c013b",                  # 0
        "KeA",                    # 1
        "Dummy",                  # 2
        "SE制御",                 # 3
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08202.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    385,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(13960,   0,       63640,   1500,    13960,   1500,    63640,   0x007C, 0,  3,  0x0000)
    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  2,  0x0000)
    DeclActor(158830,  0,       125480,  1200,    158830,  2000,    125480,  0x007C, 0,  19, 0x0000)
    DeclActor(155320,  30,      123780,  1200,    155320,  1500,    123780,  0x007C, 0,  20, 0x0000)
    DeclActor(205730,  0,       130250,  1200,    205730,  1500,    130250,  0x007C, 0,  22, 0x0000)
    DeclActor(208820,  0,       123770,  1200,    208820,  2500,    123770,  0x007C, 0,  23, 0x0000)
    DeclActor(259740,  0,       121980,  1200,    259740,  3000,    121980,  0x007C, 0,  24, 0x0000)
    DeclActor(259339,  0,       126100,  1200,    259339,  1500,    126100,  0x007C, 0,  25, 0x0000)
    DeclActor(255780,  30,      65319,   1200,    255780,  1500,    65319,   0x007C, 0,  26, 0x0000)
    DeclActor(257120,  30,      68930,   1200,    257120,  1030,    68930,   0x007C, 0,  27, 0x0000)
    DeclActor(259010,  0,       66930,   1200,    259010,  1000,    66930,   0x007C, 0,  28, 0x0000)
    DeclActor(255680,  30,      73720,   1200,    255680,  1500,    73720,   0x007C, 0,  29, 0x0000)
    DeclActor(258000,  0,       63980,   1200,    258000,  2000,    63980,   0x007C, 0,  30, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  16, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  17, 0x0000)
    DeclActor(258360,  0,       128430,  1200,    258360,  1500,    128430,  0x007C, 0,  18, 0x0000)

    ChipFrameInfo(948, 0)                                        # 0

    ScpFunction((
        "Function_0_3B4",          # 00, 0
        "Function_1_3C4",          # 01, 1
        "Function_2_5E1",          # 02, 2
        "Function_3_619",          # 03, 3
        "Function_4_61A",          # 04, 4
        "Function_5_7ED",          # 05, 5
        "Function_6_9D2",          # 06, 6
        "Function_7_BA0",          # 07, 7
        "Function_8_D6E",          # 08, 8
        "Function_9_F45",          # 09, 9
        "Function_10_111C",        # 0A, 10
        "Function_11_13AA",        # 0B, 11
        "Function_12_1638",        # 0C, 12
        "Function_13_18C6",        # 0D, 13
        "Function_14_1B54",        # 0E, 14
        "Function_15_1DE2",        # 0F, 15
        "Function_16_1E4E",        # 10, 16
        "Function_17_1EEE",        # 11, 17
        "Function_18_1F8E",        # 12, 18
        "Function_19_202E",        # 13, 19
        "Function_20_20E5",        # 14, 20
        "Function_21_21BF",        # 15, 21
        "Function_22_21C8",        # 16, 22
        "Function_23_227E",        # 17, 23
        "Function_24_2337",        # 18, 24
        "Function_25_23EB",        # 19, 25
        "Function_26_249C",        # 1A, 26
        "Function_27_2550",        # 1B, 27
        "Function_28_2608",        # 1C, 28
        "Function_29_26BC",        # 1D, 29
        "Function_30_2777",        # 1E, 30
        "Function_31_282E",        # 1F, 31
        "Function_32_28A3",        # 20, 32
    ))


    def Function_0_3B4(): pass

    label("Function_0_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3C3")
    ClearScenarioFlags(0x22, 0)
    Event(0, 32)

    label("loc_3C3")

    Return()

    # Function_0_3B4 end

    def Function_1_3C4(): pass

    label("Function_1_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_449")
    SetMapObjFrame(0xFF, "danbo", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 255600, -1000, 128900, 8000, 5000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 258899, -1000, 126000, 5000, 5000, 90000)
    Jump("loc_486")

    label("loc_449")

    SetMapObjFrame(0xFF, "danbo", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A0")
    SetMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x12, 0x2)
    OP_65(0x2, 0x1)

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB")
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x13, 0x2)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x1E, 0x4)
    ClearMapObjFlags(0x1E, 0x2)
    Jump("loc_4D1")

    label("loc_4CB")

    SetMapObjFlags(0x1D, 0x4)

    label("loc_4D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB")
    SetMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x14, 0x2)
    OP_65(0x4, 0x1)

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505")
    SetMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x15, 0x2)
    OP_65(0x5, 0x1)

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_523")
    SetMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x16, 0x2)
    OP_65(0x6, 0x1)

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_541")
    SetMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x17, 0x2)
    OP_65(0x7, 0x1)

    label("loc_541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B")
    SetMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x18, 0x2)
    OP_65(0x8, 0x1)

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_575")
    SetMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x19, 0x2)
    OP_65(0x9, 0x1)

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F")
    SetMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1A, 0x2)
    OP_65(0xA, 0x1)

    label("loc_58F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A9")
    SetMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1B, 0x2)
    OP_65(0xB, 0x1)

    label("loc_5A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C3")
    SetMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1C, 0x2)
    OP_65(0xC, 0x1)

    label("loc_5C3")

    OP_65(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E0")
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x1, 0x1)

    label("loc_5E0")

    Return()

    # Function_1_3C4 end

    def Function_2_5E1(): pass

    label("Function_2_5E1")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is Tio's room.\x01",
            "Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_2_5E1 end

    def Function_3_619(): pass

    label("Function_3_619")

    Return()

    # Function_3_619 end

    def Function_4_61A(): pass

    label("Function_4_61A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x2)
    OP_68(157620, 1330, 125080, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_674")
    SetChrFlags(0x0, 0x8)

    label("loc_674")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_687")
    SetChrFlags(0x1, 0x8)

    label("loc_687")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69A")
    SetChrFlags(0x2, 0x8)

    label("loc_69A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AD")
    SetChrFlags(0x3, 0x8)

    label("loc_6AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C0")
    SetChrFlags(0x4, 0x8)

    label("loc_6C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D3")
    SetChrFlags(0x5, 0x8)

    label("loc_6D3")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 157620, 30, 125080, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FI wonder if here's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Elie's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34A, 1)
    SetScenarioFlags(0x13C, 6)
    OP_66(0x2, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77A")
    ClearChrFlags(0x0, 0x8)

    label("loc_77A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78D")
    ClearChrFlags(0x1, 0x8)

    label("loc_78D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A0")
    ClearChrFlags(0x2, 0x8)

    label("loc_7A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B3")
    ClearChrFlags(0x3, 0x8)

    label("loc_7B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C6")
    ClearChrFlags(0x4, 0x8)

    label("loc_7C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D9")
    ClearChrFlags(0x5, 0x8)

    label("loc_7D9")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_4_61A end

    def Function_5_7ED(): pass

    label("Function_5_7ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x2)
    SetMapObjFlags(0x1D, 0x4)
    ClearMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1E, 0x2)
    OP_68(154920, 1330, 122580, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_859")
    SetChrFlags(0x0, 0x8)

    label("loc_859")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86C")
    SetChrFlags(0x1, 0x8)

    label("loc_86C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87F")
    SetChrFlags(0x2, 0x8)

    label("loc_87F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_892")
    SetChrFlags(0x3, 0x8)

    label("loc_892")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A5")
    SetChrFlags(0x4, 0x8)

    label("loc_8A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B8")
    SetChrFlags(0x5, 0x8)

    label("loc_8B8")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154920, 30, 122580, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FI wonder if here's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Elie's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34B, 1)
    SetScenarioFlags(0x13C, 7)
    OP_66(0x3, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95F")
    ClearChrFlags(0x0, 0x8)

    label("loc_95F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_972")
    ClearChrFlags(0x1, 0x8)

    label("loc_972")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_985")
    ClearChrFlags(0x2, 0x8)

    label("loc_985")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_998")
    ClearChrFlags(0x3, 0x8)

    label("loc_998")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AB")
    ClearChrFlags(0x4, 0x8)

    label("loc_9AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BE")
    ClearChrFlags(0x5, 0x8)

    label("loc_9BE")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_5_7ED end

    def Function_6_9D2(): pass

    label("Function_6_9D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x2)
    OP_68(206000, 1300, 129509, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A2C")
    SetChrFlags(0x0, 0x8)

    label("loc_A2C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3F")
    SetChrFlags(0x1, 0x8)

    label("loc_A3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A52")
    SetChrFlags(0x2, 0x8)

    label("loc_A52")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A65")
    SetChrFlags(0x3, 0x8)

    label("loc_A65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A78")
    SetChrFlags(0x4, 0x8)

    label("loc_A78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A8B")
    SetChrFlags(0x5, 0x8)

    label("loc_A8B")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 206000, 0, 129509, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FHere should be fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Tio's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34C, 1)
    SetScenarioFlags(0x13D, 0)
    OP_66(0x4, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2D")
    ClearChrFlags(0x0, 0x8)

    label("loc_B2D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B40")
    ClearChrFlags(0x1, 0x8)

    label("loc_B40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B53")
    ClearChrFlags(0x2, 0x8)

    label("loc_B53")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B66")
    ClearChrFlags(0x3, 0x8)

    label("loc_B66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B79")
    ClearChrFlags(0x4, 0x8)

    label("loc_B79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8C")
    ClearChrFlags(0x5, 0x8)

    label("loc_B8C")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_6_9D2 end

    def Function_7_BA0(): pass

    label("Function_7_BA0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x2)
    OP_68(208220, 1300, 123970, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFA")
    SetChrFlags(0x0, 0x8)

    label("loc_BFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0D")
    SetChrFlags(0x1, 0x8)

    label("loc_C0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C20")
    SetChrFlags(0x2, 0x8)

    label("loc_C20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C33")
    SetChrFlags(0x3, 0x8)

    label("loc_C33")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C46")
    SetChrFlags(0x4, 0x8)

    label("loc_C46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C59")
    SetChrFlags(0x5, 0x8)

    label("loc_C59")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208220, 0, 123970, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FHere should be fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Tio's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34D, 1)
    SetScenarioFlags(0x13D, 1)
    OP_66(0x5, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFB")
    ClearChrFlags(0x0, 0x8)

    label("loc_CFB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0E")
    ClearChrFlags(0x1, 0x8)

    label("loc_D0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D21")
    ClearChrFlags(0x2, 0x8)

    label("loc_D21")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D34")
    ClearChrFlags(0x3, 0x8)

    label("loc_D34")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D47")
    ClearChrFlags(0x4, 0x8)

    label("loc_D47")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5A")
    ClearChrFlags(0x5, 0x8)

    label("loc_D5A")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_7_BA0 end

    def Function_8_D6E(): pass

    label("Function_8_D6E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x2)
    OP_68(258329, 1300, 122180, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC8")
    SetChrFlags(0x0, 0x8)

    label("loc_DC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDB")
    SetChrFlags(0x1, 0x8)

    label("loc_DDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEE")
    SetChrFlags(0x2, 0x8)

    label("loc_DEE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E01")
    SetChrFlags(0x3, 0x8)

    label("loc_E01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E14")
    SetChrFlags(0x4, 0x8)

    label("loc_E14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E27")
    SetChrFlags(0x5, 0x8)

    label("loc_E27")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258329, 0, 122180, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10100FHere should be fine,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Noｱl's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x13D, 2)
    OP_66(0x6, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED2")
    ClearChrFlags(0x0, 0x8)

    label("loc_ED2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE5")
    ClearChrFlags(0x1, 0x8)

    label("loc_EE5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF8")
    ClearChrFlags(0x2, 0x8)

    label("loc_EF8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0B")
    ClearChrFlags(0x3, 0x8)

    label("loc_F0B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1E")
    ClearChrFlags(0x4, 0x8)

    label("loc_F1E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F31")
    ClearChrFlags(0x5, 0x8)

    label("loc_F31")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_8_D6E end

    def Function_9_F45(): pass

    label("Function_9_F45")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x2)
    OP_68(258149, 1300, 125700, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9F")
    SetChrFlags(0x0, 0x8)

    label("loc_F9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB2")
    SetChrFlags(0x1, 0x8)

    label("loc_FB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC5")
    SetChrFlags(0x2, 0x8)

    label("loc_FC5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD8")
    SetChrFlags(0x3, 0x8)

    label("loc_FD8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEB")
    SetChrFlags(0x4, 0x8)

    label("loc_FEB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFE")
    SetChrFlags(0x5, 0x8)

    label("loc_FFE")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258149, 0, 125700, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10100FHere should be fine,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Noｱl's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x13D, 3)
    OP_66(0x7, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A9")
    ClearChrFlags(0x0, 0x8)

    label("loc_10A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BC")
    ClearChrFlags(0x1, 0x8)

    label("loc_10BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10CF")
    ClearChrFlags(0x2, 0x8)

    label("loc_10CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E2")
    ClearChrFlags(0x3, 0x8)

    label("loc_10E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F5")
    ClearChrFlags(0x4, 0x8)

    label("loc_10F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1108")
    ClearChrFlags(0x5, 0x8)

    label("loc_1108")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_9_F45 end

    def Function_10_111C(): pass

    label("Function_10_111C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FOh, right, this\x01",
            "plushie... It might be\x01",
            "perfect for KeA's room.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went to look for\x01",
            "KeA and he gave her the\x01",
            "plushie as a present.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x2)
    OP_68(256110, 1330, 66720, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1213")
    SetChrFlags(0x0, 0x8)

    label("loc_1213")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1226")
    SetChrFlags(0x1, 0x8)

    label("loc_1226")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1239")
    SetChrFlags(0x2, 0x8)

    label("loc_1239")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_124C")
    SetChrFlags(0x3, 0x8)

    label("loc_124C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125F")
    SetChrFlags(0x4, 0x8)

    label("loc_125F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1272")
    SetChrFlags(0x5, 0x8)

    label("loc_1272")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 256980, 30, 66530, 225)
    ClearChrFlags(0x8, 0x8)
    SetChrPos(0x8, 256019, 30, 66750, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#01100FI'll put it here!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x13D, 4)
    OP_66(0x8, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132F")
    ClearChrFlags(0x0, 0x8)

    label("loc_132F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1342")
    ClearChrFlags(0x1, 0x8)

    label("loc_1342")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1355")
    ClearChrFlags(0x2, 0x8)

    label("loc_1355")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1368")
    ClearChrFlags(0x3, 0x8)

    label("loc_1368")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137B")
    ClearChrFlags(0x4, 0x8)

    label("loc_137B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138E")
    ClearChrFlags(0x5, 0x8)

    label("loc_138E")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_10_111C end

    def Function_11_13AA(): pass

    label("Function_11_13AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FOh, right, this\x01",
            "plushie... It might be\x01",
            "perfect for KeA's room.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went to look for\x01",
            "KeA and he gave her the\x01",
            "plushie as a present.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x2)
    OP_68(255780, 1300, 68700, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14A1")
    SetChrFlags(0x0, 0x8)

    label("loc_14A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B4")
    SetChrFlags(0x1, 0x8)

    label("loc_14B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C7")
    SetChrFlags(0x2, 0x8)

    label("loc_14C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14DA")
    SetChrFlags(0x3, 0x8)

    label("loc_14DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14ED")
    SetChrFlags(0x4, 0x8)

    label("loc_14ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1500")
    SetChrFlags(0x5, 0x8)

    label("loc_1500")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 255780, 30, 69500, 135)
    ClearChrFlags(0x8, 0x8)
    SetChrPos(0x8, 255780, 0, 68700, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#01100FI'll put it here!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x13D, 5)
    OP_66(0x9, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15BD")
    ClearChrFlags(0x0, 0x8)

    label("loc_15BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D0")
    ClearChrFlags(0x1, 0x8)

    label("loc_15D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E3")
    ClearChrFlags(0x2, 0x8)

    label("loc_15E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F6")
    ClearChrFlags(0x3, 0x8)

    label("loc_15F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1609")
    ClearChrFlags(0x4, 0x8)

    label("loc_1609")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_161C")
    ClearChrFlags(0x5, 0x8)

    label("loc_161C")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_11_13AA end

    def Function_12_1638(): pass

    label("Function_12_1638")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FOh, right, this\x01",
            "plushie... It might be\x01",
            "perfect for KeA's room.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went to look for\x01",
            "KeA and he gave her the\x01",
            "plushie as a present.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1A, 0x2)
    OP_68(258110, 1300, 67120, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_172F")
    SetChrFlags(0x0, 0x8)

    label("loc_172F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1742")
    SetChrFlags(0x1, 0x8)

    label("loc_1742")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1755")
    SetChrFlags(0x2, 0x8)

    label("loc_1755")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1768")
    SetChrFlags(0x3, 0x8)

    label("loc_1768")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_177B")
    SetChrFlags(0x4, 0x8)

    label("loc_177B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_178E")
    SetChrFlags(0x5, 0x8)

    label("loc_178E")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 259010, 0, 65730, 0)
    ClearChrFlags(0x8, 0x8)
    SetChrPos(0x8, 258110, 0, 67120, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#01100FI'll put it here!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x13D, 6)
    OP_66(0xA, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_184B")
    ClearChrFlags(0x0, 0x8)

    label("loc_184B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185E")
    ClearChrFlags(0x1, 0x8)

    label("loc_185E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1871")
    ClearChrFlags(0x2, 0x8)

    label("loc_1871")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1884")
    ClearChrFlags(0x3, 0x8)

    label("loc_1884")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1897")
    ClearChrFlags(0x4, 0x8)

    label("loc_1897")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18AA")
    ClearChrFlags(0x5, 0x8)

    label("loc_18AA")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_12_1638 end

    def Function_13_18C6(): pass

    label("Function_13_18C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FOh, right, this\x01",
            "plushie... It might be\x01",
            "perfect for KeA's room.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went to look for\x01",
            "KeA and he gave her the\x01",
            "plushie as a present.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1B, 0x2)
    OP_68(255730, 1330, 72650, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19BD")
    SetChrFlags(0x0, 0x8)

    label("loc_19BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D0")
    SetChrFlags(0x1, 0x8)

    label("loc_19D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E3")
    SetChrFlags(0x2, 0x8)

    label("loc_19E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19F6")
    SetChrFlags(0x3, 0x8)

    label("loc_19F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A09")
    SetChrFlags(0x4, 0x8)

    label("loc_1A09")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A1C")
    SetChrFlags(0x5, 0x8)

    label("loc_1A1C")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 254270, 30, 72640, 45)
    ClearChrFlags(0x8, 0x8)
    SetChrPos(0x8, 255730, 30, 72650, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#01100FI'll put it here!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x13D, 7)
    OP_66(0xB, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AD9")
    ClearChrFlags(0x0, 0x8)

    label("loc_1AD9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AEC")
    ClearChrFlags(0x1, 0x8)

    label("loc_1AEC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AFF")
    ClearChrFlags(0x2, 0x8)

    label("loc_1AFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B12")
    ClearChrFlags(0x3, 0x8)

    label("loc_1B12")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B25")
    ClearChrFlags(0x4, 0x8)

    label("loc_1B25")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B38")
    ClearChrFlags(0x5, 0x8)

    label("loc_1B38")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_13_18C6 end

    def Function_14_1B54(): pass

    label("Function_14_1B54")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FOh, right, this\x01",
            "plushie... It might be\x01",
            "perfect for KeA's room.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went to look for\x01",
            "KeA and he gave her the\x01",
            "plushie as a present.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x2)
    OP_68(256839, 1330, 63970, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C4B")
    SetChrFlags(0x0, 0x8)

    label("loc_1C4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C5E")
    SetChrFlags(0x1, 0x8)

    label("loc_1C5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C71")
    SetChrFlags(0x2, 0x8)

    label("loc_1C71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C84")
    SetChrFlags(0x3, 0x8)

    label("loc_1C84")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C97")
    SetChrFlags(0x4, 0x8)

    label("loc_1C97")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CAA")
    SetChrFlags(0x5, 0x8)

    label("loc_1CAA")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 258410, 0, 65590, 180)
    ClearChrFlags(0x8, 0x8)
    SetChrPos(0x8, 256839, 30, 63970, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#01100FI'll put it here!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x358, 1)
    SetScenarioFlags(0x13E, 0)
    OP_66(0xC, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D67")
    ClearChrFlags(0x0, 0x8)

    label("loc_1D67")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D7A")
    ClearChrFlags(0x1, 0x8)

    label("loc_1D7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D8D")
    ClearChrFlags(0x2, 0x8)

    label("loc_1D8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA0")
    ClearChrFlags(0x3, 0x8)

    label("loc_1DA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB3")
    ClearChrFlags(0x4, 0x8)

    label("loc_1DB3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC6")
    ClearChrFlags(0x5, 0x8)

    label("loc_1DC6")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_14_1B54 end

    def Function_15_1DE2(): pass

    label("Function_15_1DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4D")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you acquire furniture\x01",
            "items, you can place them\x01",
            "in the protagonists' rooms.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_1E4D")

    Return()

    # Function_15_1DE2 end

    def Function_16_1E4E(): pass

    label("Function_16_1E4E")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED0")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1ED0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EEC")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1EEC")

    Return()

    # Function_16_1E4E end

    def Function_17_1EEE(): pass

    label("Function_17_1EEE")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F70")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1F70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1F8C")

    Return()

    # Function_17_1EEE end

    def Function_18_1F8E(): pass

    label("Function_18_1F8E")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2010")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2010")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_202C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_202C")

    Return()

    # Function_18_1F8E end

    def Function_19_202E(): pass

    label("Function_19_202E")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis362.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a stylish mirror.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_19_202E end

    def Function_20_20E5(): pass

    label("Function_20_20E5")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis363.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's music box.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    BeginChrThread(0xA, 1, 0, 21)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_20E5 end

    def Function_21_21BF(): pass

    label("Function_21_21BF")

    PlayBGM("ed7591", 0)
    Sleep(19000)
    OP_1F()
    Return()

    # Function_21_21BF end

    def Function_22_21C8(): pass

    label("Function_22_21C8")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis364.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Kagemaru bank.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_22_21C8 end

    def Function_23_227E(): pass

    label("Function_23_227E")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis365.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Mishette plushie.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_23_227E end

    def Function_24_2337(): pass

    label("Function_24_2337")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis370.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a racing flag.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_24_2337 end

    def Function_25_23EB(): pass

    label("Function_25_23EB")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis371.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a minivelo.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_25_23EB end

    def Function_26_249C(): pass

    label("Function_26_249C")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis373.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Pom cushion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_26_249C end

    def Function_27_2550(): pass

    label("Function_27_2550")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis372.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a strange cushion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_27_2550 end

    def Function_28_2608(): pass

    label("Function_28_2608")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis374.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a black teddy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_28_2608 end

    def Function_29_26BC(): pass

    label("Function_29_26BC")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis375.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an Acerbic\x01",
            "Tomartian.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_29_26BC end

    def Function_30_2777(): pass

    label("Function_30_2777")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis376.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a ZWEI 2 penguin.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_30_2777 end

    def Function_31_282E(): pass

    label("Function_31_282E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28A2")
    OP_E0(0x16, 0x0)

    label("loc_28A2")

    Return()

    # Function_31_282E end

    def Function_32_28A3(): pass

    label("Function_32_28A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51420.itc", 0x1E)
    LoadChrToIndex("apl/ch51421.itc", 0x1F)
    LoadChrToIndex("apl/ch51422.itc", 0x20)
    LoadChrToIndex("apl/ch51425.itc", 0x21)
    SetChrPos(0x101, 5000, 0, 65500, 0)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x10)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 153550, 320, 129100, 0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x2)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 208550, 280, 129000, 0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 14000, 0, 65000, 180)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x10)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x109, 258500, 280, 128949, 0)
    SetChrPos(0x105, 5000, 0, 65500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x9, 14000, 800, 63000, 270)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x1F, 0x1000)
    SetMapObjFrame(0xFF, "nhuton", 0x0, 0x1)
    SetMapObjFrame(0xFF, "huton", 0x0, 0x1)
    OP_7D(0x77, 0x77, 0x8B, 0x0, 0x0)
    OP_68(153400, 1100, 128850, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(208500, 1900, 129000, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18500, 0)
    OP_68(208500, 900, 129000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(258300, 1100, 128600, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(20500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(14000, 1300, 63000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    StopBGM(0xFA0)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(103, 0, 70, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_2B79():
        OP_96(0xFE, 0x36B0, 0x0, 0xF618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B79)

    def lambda_2B93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2B93)
    WaitChrThread(0x104, 1)
    Sound(104, 0, 70, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_93(0x104, 0x10E, 0x1F4)
    OP_6B(0x9)

    def lambda_2BCD():
        OP_95(0xFE, -1000, 0, 63000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BCD)

    def lambda_2BE7():
        OP_95(0xFE, -1000, 800, 63000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2BE7)
    WaitChrThread(0x104, 1)
    Sleep(300)
    OP_6B(0xFF)
    OP_68(1000, 1300, 63000, 1500)
    MoveCamera(57, 19, 0, 1500)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_6F(0x79)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    Sleep(500)
    OP_93(0x104, 0x0, 0x1F4)
    SetCameraDistance(23000, 7000)

    def lambda_2C5B():
        OP_95(0xFE, -1000, 0, 70500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C5B)
    WaitChrThread(0x104, 1)

    def lambda_2C79():
        OP_95(0xFE, 1500, 0, 70500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C79)
    WaitChrThread(0x104, 1)
    FadeToDark(2000, 0, -1)

    def lambda_2CA1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CA1)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x10)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x10)
    ClearChrFlags(0x109, 0x2)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_28A3 end

    SaveToFile()

Try(main)
