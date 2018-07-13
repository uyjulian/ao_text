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
        "Function_5_7F2",          # 05, 5
        "Function_6_9DC",          # 06, 6
        "Function_7_BAF",          # 07, 7
        "Function_8_D82",          # 08, 8
        "Function_9_F5D",          # 09, 9
        "Function_10_1138",        # 0A, 10
        "Function_11_13D6",        # 0B, 11
        "Function_12_1674",        # 0C, 12
        "Function_13_1912",        # 0D, 13
        "Function_14_1BB0",        # 0E, 14
        "Function_15_1E4E",        # 0F, 15
        "Function_16_1EBA",        # 10, 16
        "Function_17_1F58",        # 11, 17
        "Function_18_1FF6",        # 12, 18
        "Function_19_2094",        # 13, 19
        "Function_20_214C",        # 14, 20
        "Function_21_2229",        # 15, 21
        "Function_22_2232",        # 16, 22
        "Function_23_22E9",        # 17, 23
        "Function_24_23A1",        # 18, 24
        "Function_25_2456",        # 19, 25
        "Function_26_2508",        # 1A, 26
        "Function_27_25BD",        # 1B, 27
        "Function_28_2676",        # 1C, 28
        "Function_29_272B",        # 1D, 29
        "Function_30_27E7",        # 1E, 30
        "Function_31_289F",        # 1F, 31
        "Function_32_2914",        # 20, 32
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
        "#0100FI wonder if here it's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Elie's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34A, 1)
    SetScenarioFlags(0x13C, 6)
    OP_66(0x2, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77F")
    ClearChrFlags(0x0, 0x8)

    label("loc_77F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_792")
    ClearChrFlags(0x1, 0x8)

    label("loc_792")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A5")
    ClearChrFlags(0x2, 0x8)

    label("loc_7A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B8")
    ClearChrFlags(0x3, 0x8)

    label("loc_7B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CB")
    ClearChrFlags(0x4, 0x8)

    label("loc_7CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DE")
    ClearChrFlags(0x5, 0x8)

    label("loc_7DE")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_4_61A end

    def Function_5_7F2(): pass

    label("Function_5_7F2")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85E")
    SetChrFlags(0x0, 0x8)

    label("loc_85E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_871")
    SetChrFlags(0x1, 0x8)

    label("loc_871")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_884")
    SetChrFlags(0x2, 0x8)

    label("loc_884")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_897")
    SetChrFlags(0x3, 0x8)

    label("loc_897")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AA")
    SetChrFlags(0x4, 0x8)

    label("loc_8AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BD")
    SetChrFlags(0x5, 0x8)

    label("loc_8BD")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154920, 30, 122580, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FI wonder if here it's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Elie's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34B, 1)
    SetScenarioFlags(0x13C, 7)
    OP_66(0x3, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_969")
    ClearChrFlags(0x0, 0x8)

    label("loc_969")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97C")
    ClearChrFlags(0x1, 0x8)

    label("loc_97C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98F")
    ClearChrFlags(0x2, 0x8)

    label("loc_98F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A2")
    ClearChrFlags(0x3, 0x8)

    label("loc_9A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B5")
    ClearChrFlags(0x4, 0x8)

    label("loc_9B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C8")
    ClearChrFlags(0x5, 0x8)

    label("loc_9C8")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_5_7F2 end

    def Function_6_9DC(): pass

    label("Function_6_9DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x2)
    OP_68(206000, 1300, 129509, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A36")
    SetChrFlags(0x0, 0x8)

    label("loc_A36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A49")
    SetChrFlags(0x1, 0x8)

    label("loc_A49")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A5C")
    SetChrFlags(0x2, 0x8)

    label("loc_A5C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A6F")
    SetChrFlags(0x3, 0x8)

    label("loc_A6F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A82")
    SetChrFlags(0x4, 0x8)

    label("loc_A82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A95")
    SetChrFlags(0x5, 0x8)

    label("loc_A95")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 206000, 0, 129509, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FIt should be fine here.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Tio's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34C, 1)
    SetScenarioFlags(0x13D, 0)
    OP_66(0x4, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B3C")
    ClearChrFlags(0x0, 0x8)

    label("loc_B3C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4F")
    ClearChrFlags(0x1, 0x8)

    label("loc_B4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B62")
    ClearChrFlags(0x2, 0x8)

    label("loc_B62")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B75")
    ClearChrFlags(0x3, 0x8)

    label("loc_B75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B88")
    ClearChrFlags(0x4, 0x8)

    label("loc_B88")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9B")
    ClearChrFlags(0x5, 0x8)

    label("loc_B9B")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_6_9DC end

    def Function_7_BAF(): pass

    label("Function_7_BAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x2)
    OP_68(208220, 1300, 123970, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C09")
    SetChrFlags(0x0, 0x8)

    label("loc_C09")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1C")
    SetChrFlags(0x1, 0x8)

    label("loc_C1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2F")
    SetChrFlags(0x2, 0x8)

    label("loc_C2F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C42")
    SetChrFlags(0x3, 0x8)

    label("loc_C42")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C55")
    SetChrFlags(0x4, 0x8)

    label("loc_C55")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C68")
    SetChrFlags(0x5, 0x8)

    label("loc_C68")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208220, 0, 123970, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FIt should be fine here.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Tio's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34D, 1)
    SetScenarioFlags(0x13D, 1)
    OP_66(0x5, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0F")
    ClearChrFlags(0x0, 0x8)

    label("loc_D0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D22")
    ClearChrFlags(0x1, 0x8)

    label("loc_D22")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D35")
    ClearChrFlags(0x2, 0x8)

    label("loc_D35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D48")
    ClearChrFlags(0x3, 0x8)

    label("loc_D48")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5B")
    ClearChrFlags(0x4, 0x8)

    label("loc_D5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6E")
    ClearChrFlags(0x5, 0x8)

    label("loc_D6E")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_7_BAF end

    def Function_8_D82(): pass

    label("Function_8_D82")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x2)
    OP_68(258329, 1300, 122180, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDC")
    SetChrFlags(0x0, 0x8)

    label("loc_DDC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEF")
    SetChrFlags(0x1, 0x8)

    label("loc_DEF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E02")
    SetChrFlags(0x2, 0x8)

    label("loc_E02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E15")
    SetChrFlags(0x3, 0x8)

    label("loc_E15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E28")
    SetChrFlags(0x4, 0x8)

    label("loc_E28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E3B")
    SetChrFlags(0x5, 0x8)

    label("loc_E3B")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258329, 0, 122180, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10100FIt looks like here it's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Noｱl's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x13D, 2)
    OP_66(0x6, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EEA")
    ClearChrFlags(0x0, 0x8)

    label("loc_EEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EFD")
    ClearChrFlags(0x1, 0x8)

    label("loc_EFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F10")
    ClearChrFlags(0x2, 0x8)

    label("loc_F10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F23")
    ClearChrFlags(0x3, 0x8)

    label("loc_F23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F36")
    ClearChrFlags(0x4, 0x8)

    label("loc_F36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F49")
    ClearChrFlags(0x5, 0x8)

    label("loc_F49")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_8_D82 end

    def Function_9_F5D(): pass

    label("Function_9_F5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x2)
    OP_68(258149, 1300, 125700, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB7")
    SetChrFlags(0x0, 0x8)

    label("loc_FB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCA")
    SetChrFlags(0x1, 0x8)

    label("loc_FCA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FDD")
    SetChrFlags(0x2, 0x8)

    label("loc_FDD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF0")
    SetChrFlags(0x3, 0x8)

    label("loc_FF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1003")
    SetChrFlags(0x4, 0x8)

    label("loc_1003")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1016")
    SetChrFlags(0x5, 0x8)

    label("loc_1016")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258149, 0, 125700, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10100FIt looks like here it's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Noｱl's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x13D, 3)
    OP_66(0x7, 0x1)
    Call(0, 15)
    Call(0, 31)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C5")
    ClearChrFlags(0x0, 0x8)

    label("loc_10C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D8")
    ClearChrFlags(0x1, 0x8)

    label("loc_10D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10EB")
    ClearChrFlags(0x2, 0x8)

    label("loc_10EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FE")
    ClearChrFlags(0x3, 0x8)

    label("loc_10FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1111")
    ClearChrFlags(0x4, 0x8)

    label("loc_1111")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1124")
    ClearChrFlags(0x5, 0x8)

    label("loc_1124")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_9_F5D end

    def Function_10_1138(): pass

    label("Function_10_1138")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FOh, right, this plushy...\x01",
            "It could be perfect for KeA's room.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went to look for KeA and he gave her\x01",
            "the plushy he had with him as a present.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_123D")
    SetChrFlags(0x0, 0x8)

    label("loc_123D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1250")
    SetChrFlags(0x1, 0x8)

    label("loc_1250")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1263")
    SetChrFlags(0x2, 0x8)

    label("loc_1263")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1276")
    SetChrFlags(0x3, 0x8)

    label("loc_1276")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1289")
    SetChrFlags(0x4, 0x8)

    label("loc_1289")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_129C")
    SetChrFlags(0x5, 0x8)

    label("loc_129C")

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
            "A new furniture was\x01",
            "added to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x13D, 4)
    OP_66(0x8, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_135B")
    ClearChrFlags(0x0, 0x8)

    label("loc_135B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136E")
    ClearChrFlags(0x1, 0x8)

    label("loc_136E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1381")
    ClearChrFlags(0x2, 0x8)

    label("loc_1381")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1394")
    ClearChrFlags(0x3, 0x8)

    label("loc_1394")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A7")
    ClearChrFlags(0x4, 0x8)

    label("loc_13A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BA")
    ClearChrFlags(0x5, 0x8)

    label("loc_13BA")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_10_1138 end

    def Function_11_13D6(): pass

    label("Function_11_13D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FOh, right, this plushy...\x01",
            "It could be perfect for KeA's room.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went to look for KeA and he gave her\x01",
            "the plushy he had with him as a present.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14DB")
    SetChrFlags(0x0, 0x8)

    label("loc_14DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14EE")
    SetChrFlags(0x1, 0x8)

    label("loc_14EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1501")
    SetChrFlags(0x2, 0x8)

    label("loc_1501")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1514")
    SetChrFlags(0x3, 0x8)

    label("loc_1514")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1527")
    SetChrFlags(0x4, 0x8)

    label("loc_1527")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153A")
    SetChrFlags(0x5, 0x8)

    label("loc_153A")

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
            "A new furniture was\x01",
            "added to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x13D, 5)
    OP_66(0x9, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F9")
    ClearChrFlags(0x0, 0x8)

    label("loc_15F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_160C")
    ClearChrFlags(0x1, 0x8)

    label("loc_160C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_161F")
    ClearChrFlags(0x2, 0x8)

    label("loc_161F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1632")
    ClearChrFlags(0x3, 0x8)

    label("loc_1632")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1645")
    ClearChrFlags(0x4, 0x8)

    label("loc_1645")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1658")
    ClearChrFlags(0x5, 0x8)

    label("loc_1658")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_11_13D6 end

    def Function_12_1674(): pass

    label("Function_12_1674")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FOh, right, this plushy...\x01",
            "It could be perfect for KeA's room.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went to look for KeA and he gave her\x01",
            "the plushy he had with him as a present.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1779")
    SetChrFlags(0x0, 0x8)

    label("loc_1779")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_178C")
    SetChrFlags(0x1, 0x8)

    label("loc_178C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_179F")
    SetChrFlags(0x2, 0x8)

    label("loc_179F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17B2")
    SetChrFlags(0x3, 0x8)

    label("loc_17B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C5")
    SetChrFlags(0x4, 0x8)

    label("loc_17C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17D8")
    SetChrFlags(0x5, 0x8)

    label("loc_17D8")

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
            "A new furniture was\x01",
            "added to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x13D, 6)
    OP_66(0xA, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1897")
    ClearChrFlags(0x0, 0x8)

    label("loc_1897")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18AA")
    ClearChrFlags(0x1, 0x8)

    label("loc_18AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18BD")
    ClearChrFlags(0x2, 0x8)

    label("loc_18BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18D0")
    ClearChrFlags(0x3, 0x8)

    label("loc_18D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18E3")
    ClearChrFlags(0x4, 0x8)

    label("loc_18E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18F6")
    ClearChrFlags(0x5, 0x8)

    label("loc_18F6")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_12_1674 end

    def Function_13_1912(): pass

    label("Function_13_1912")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FOh, right, this plushy...\x01",
            "It could be perfect for KeA's room.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went to look for KeA and he gave her\x01",
            "the plushy he had with him as a present.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A17")
    SetChrFlags(0x0, 0x8)

    label("loc_1A17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A2A")
    SetChrFlags(0x1, 0x8)

    label("loc_1A2A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A3D")
    SetChrFlags(0x2, 0x8)

    label("loc_1A3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A50")
    SetChrFlags(0x3, 0x8)

    label("loc_1A50")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A63")
    SetChrFlags(0x4, 0x8)

    label("loc_1A63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A76")
    SetChrFlags(0x5, 0x8)

    label("loc_1A76")

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
            "A new furniture was\x01",
            "added to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x13D, 7)
    OP_66(0xB, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B35")
    ClearChrFlags(0x0, 0x8)

    label("loc_1B35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B48")
    ClearChrFlags(0x1, 0x8)

    label("loc_1B48")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B5B")
    ClearChrFlags(0x2, 0x8)

    label("loc_1B5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B6E")
    ClearChrFlags(0x3, 0x8)

    label("loc_1B6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B81")
    ClearChrFlags(0x4, 0x8)

    label("loc_1B81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B94")
    ClearChrFlags(0x5, 0x8)

    label("loc_1B94")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_13_1912 end

    def Function_14_1BB0(): pass

    label("Function_14_1BB0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FOh, right, this plushy...\x01",
            "It could be perfect for KeA's room.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went to look for KeA and he gave her\x01",
            "the plushy he had with him as a present.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB5")
    SetChrFlags(0x0, 0x8)

    label("loc_1CB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC8")
    SetChrFlags(0x1, 0x8)

    label("loc_1CC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CDB")
    SetChrFlags(0x2, 0x8)

    label("loc_1CDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CEE")
    SetChrFlags(0x3, 0x8)

    label("loc_1CEE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D01")
    SetChrFlags(0x4, 0x8)

    label("loc_1D01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D14")
    SetChrFlags(0x5, 0x8)

    label("loc_1D14")

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
            "A new furniture was\x01",
            "added to KeA's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x358, 1)
    SetScenarioFlags(0x13E, 0)
    OP_66(0xC, 0x1)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD3")
    ClearChrFlags(0x0, 0x8)

    label("loc_1DD3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE6")
    ClearChrFlags(0x1, 0x8)

    label("loc_1DE6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF9")
    ClearChrFlags(0x2, 0x8)

    label("loc_1DF9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E0C")
    ClearChrFlags(0x3, 0x8)

    label("loc_1E0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E1F")
    ClearChrFlags(0x4, 0x8)

    label("loc_1E1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E32")
    ClearChrFlags(0x5, 0x8)

    label("loc_1E32")

    Call(0, 31)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x0, 253180, 0, 65990, 90)
    EventEnd(0x5)
    Return()

    # Function_14_1BB0 end

    def Function_15_1E4E(): pass

    label("Function_15_1E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB9")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you acquire furniture items,\x01",
            "you can place them in the protagonists' rooms.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_1EB9")

    Return()

    # Function_15_1E4E end

    def Function_16_1EBA(): pass

    label("Function_16_1EBA")

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
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3A")
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

    label("loc_1F3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F56")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1F56")

    Return()

    # Function_16_1EBA end

    def Function_17_1F58(): pass

    label("Function_17_1F58")

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
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD8")
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

    label("loc_1FD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF4")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1FF4")

    Return()

    # Function_17_1F58 end

    def Function_18_1FF6(): pass

    label("Function_18_1FF6")

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
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2076")
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

    label("loc_2076")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2092")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2092")

    Return()

    # Function_18_1FF6 end

    def Function_19_2094(): pass

    label("Function_19_2094")

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
            "It is a stylish mirror.\x02",
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

    # Function_19_2094 end

    def Function_20_214C(): pass

    label("Function_20_214C")

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
            "It is a music box.\x02",
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

    # Function_20_214C end

    def Function_21_2229(): pass

    label("Function_21_2229")

    PlayBGM("ed7591", 0)
    Sleep(19000)
    OP_1F()
    Return()

    # Function_21_2229 end

    def Function_22_2232(): pass

    label("Function_22_2232")

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
            "It is a Kagemaru bank.\x02",
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

    # Function_22_2232 end

    def Function_23_22E9(): pass

    label("Function_23_22E9")

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
            "It is a Miichie plushy.\x02",
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

    # Function_23_22E9 end

    def Function_24_23A1(): pass

    label("Function_24_23A1")

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
            "It is a racing flag.\x02",
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

    # Function_24_23A1 end

    def Function_25_2456(): pass

    label("Function_25_2456")

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
            "It is a minivelo.\x02",
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

    # Function_25_2456 end

    def Function_26_2508(): pass

    label("Function_26_2508")

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
            "It is a Pom cushion.\x02",
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

    # Function_26_2508 end

    def Function_27_25BD(): pass

    label("Function_27_25BD")

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
            "It is a strange cushion.\x02",
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

    # Function_27_25BD end

    def Function_28_2676(): pass

    label("Function_28_2676")

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
            "It is a black teddy.\x02",
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

    # Function_28_2676 end

    def Function_29_272B(): pass

    label("Function_29_272B")

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
            "It is an Acerbic Tomartian.\x02",
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

    # Function_29_272B end

    def Function_30_27E7(): pass

    label("Function_30_27E7")

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
            "It is a ZWEI 2 penguin.\x02",
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

    # Function_30_27E7 end

    def Function_31_289F(): pass

    label("Function_31_289F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2913")
    OP_E0(0x16, 0x0)

    label("loc_2913")

    Return()

    # Function_31_289F end

    def Function_32_2914(): pass

    label("Function_32_2914")

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

    def lambda_2BEA():
        OP_96(0xFE, 0x36B0, 0x0, 0xF618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BEA)

    def lambda_2C04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2C04)
    WaitChrThread(0x104, 1)
    Sound(104, 0, 70, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_93(0x104, 0x10E, 0x1F4)
    OP_6B(0x9)

    def lambda_2C3E():
        OP_95(0xFE, -1000, 0, 63000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C3E)

    def lambda_2C58():
        OP_95(0xFE, -1000, 800, 63000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C58)
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

    def lambda_2CCC():
        OP_95(0xFE, -1000, 0, 70500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CCC)
    WaitChrThread(0x104, 1)

    def lambda_2CEA():
        OP_95(0xFE, 1500, 0, 70500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CEA)
    WaitChrThread(0x104, 1)
    FadeToDark(2000, 0, -1)

    def lambda_2D12():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D12)
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

    # Function_32_2914 end

    SaveToFile()

Try(main)
