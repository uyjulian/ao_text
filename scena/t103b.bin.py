from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t103b.bin",                # FileName
        "t103b",                    # MapName
        "t103b",                    # Location
        0x0041,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t103b",                  # 0
        "M. W. L. Staff",         # 1
        "M. W. L. Staff",         # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Melson",                 # 5
        "Corona",                 # 6
        "Rimah",                  # 7
        "To Hotel Delphinia",     # 8
        "To Theme Park",          # 9
    ))

    AddCharChip((
        "chr/ch44500.itc",                   # 00
        "chr/ch32300.itc",                   # 01
        "chr/ch32400.itc",                   # 02
        "chr/ch26200.itc",                   # 03
        "chr/ch22700.itc",                   # 04
        "chr/ch20700.itc",                   # 05
    ))

    DeclNpc(4294963296, 4400,    0,       180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4750,    4400,    0,       180,  389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4329,    2599,    4294943807, 0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5329,    2599,    4294943807, 0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294954026, 4000,    4294962717, 135,  261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294955486, 4000,    4294962476, 270,  261,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294954217, 4000,    4294961166, 0,    261,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)

    DeclEvent(0x0000, 0, 14,  0.0,                   2.5,                   3.4000000953674316,    100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -1.25,                 -0.6800000071525574,   1.0])

    DeclActor(4294953126, 4000,    4294961256, 1200,    4294953126, 5500,    4294961256, 0x007C, 0,  15, 0x0000)
    DeclActor(4294960646, 4000,    1550,    1200,    4294960646, 5500,    1550,    0x007C, 0,  16, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "To Hotel Delphinia")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "To Theme Park")

    ChipFrameInfo(644, 0)                                        # 0

    ScpFunction((
        "Function_0_284",          # 00, 0
        "Function_1_33C",          # 01, 1
        "Function_2_44B",          # 02, 2
        "Function_3_515",          # 03, 3
        "Function_4_7A0",          # 04, 4
        "Function_5_896",          # 05, 5
        "Function_6_8EB",          # 06, 6
        "Function_7_960",          # 07, 7
        "Function_8_A61",          # 08, 8
        "Function_9_B21",          # 09, 9
        "Function_10_BE8",         # 0A, 10
        "Function_11_CE6",         # 0B, 11
        "Function_12_149C",        # 0C, 12
        "Function_13_1575",        # 0D, 13
        "Function_14_170E",        # 0E, 14
        "Function_15_17B5",        # 0F, 15
        "Function_16_184E",        # 10, 16
    ))


    def Function_0_284(): pass

    label("Function_0_284")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2C4"),
        (1, "loc_2D0"),
        (2, "loc_2DC"),
        (3, "loc_2E8"),
        (4, "loc_2F4"),
        (5, "loc_300"),
        (6, "loc_30C"),
        (SWITCH_DEFAULT, "loc_318"),
    )


    label("loc_2C4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2D0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2DC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2E8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2F4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_300")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_30C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_318")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_324")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_33B")

    Return()

    # Function_0_284 end

    def Function_1_33C(): pass

    label("Function_1_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_359")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_400")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_367")
    Jump("loc_400")

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_3B1")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    Jump("loc_400")

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_3BF")
    Jump("loc_400")

    label("loc_3BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_3CD")
    Jump("loc_400")

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3DB")
    Jump("loc_400")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_3E9")
    Jump("loc_400")

    label("loc_3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_3F7")
    Jump("loc_400")

    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_400")

    label("loc_400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_414")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42F")
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_44A")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44A")
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_44A")

    Return()

    # Function_1_33C end

    def Function_2_44B(): pass

    label("Function_2_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C")
    SetMapObjFrame(0xFF, "board0a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "board0b", 0x0, 0x1)
    Jump("loc_49A")

    label("loc_47C")

    SetMapObjFrame(0xFF, "board1a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "board1b", 0x0, 0x1)

    label("loc_49A")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B2")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CB")
    OP_24(0x335)
    OP_24(0x1BC)
    Jump("loc_4F8")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EC")
    Sound(821, 1, 40, 0)
    OP_24(0x1BC)
    Jump("loc_4F8")

    label("loc_4EC")

    Sound(821, 1, 40, 0)
    Sound(444, 1, 100, 0)

    label("loc_4F8")

    SoundDistance(0x7B, 0xFFFFFFBA, 0x109A, 0xFFFFD9E0, 0x2710, 0x186A0, 0x50, 0x0)
    Return()

    # Function_2_44B end

    def Function_3_515(): pass

    label("Function_3_515")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E3")

    ChrTalk(
        0x8,
        (
            "At the theme park, the night\x01",
            "performance is now in session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even the night parade where Michey and the\x01",
            "others go around the park, is very popular.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68A")

    ChrTalk(
        0x103,
        "#00203F...Honestly, I wanted to see it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, well, this time it can't be helped.\x01",
            "We'll do it at the next opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FUh uh...absolutely, ok?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DB")

    label("loc_68A")


    ChrTalk(
        0x101,
        (
            "#00003F(Uuhm, if I had asked Tio she probably\x01",
            "would've wanted to see it...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DB")

    SetScenarioFlags(0x0, 0)
    Jump("loc_780")

    label("loc_6E3")


    ChrTalk(
        0x8,
        (
            "At the theme park, the night\x01",
            "performance is now in session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even the night parade where Michey and the\x01",
            "others go around the park, is very popular.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_780")

    Jump("loc_79C")

    label("loc_785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_793")
    Jump("loc_79C")

    label("loc_793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_79C")

    label("loc_79C")

    TalkEnd(0xFE)
    Return()

    # Function_3_515 end

    def Function_4_7A0(): pass

    label("Function_4_7A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_87B")

    ChrTalk(
        0x9,
        (
            "As for Michelam famous fireworks,\x01",
            "every day about 100 of them\x01",
            "are launched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They are popularly seen from the\x01",
            "theme park, of course, but also from\x01",
            "the hotel and the airships cruising at night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_892")

    label("loc_87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_889")
    Jump("loc_892")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_892")

    label("loc_892")

    TalkEnd(0xFE)
    Return()

    # Function_4_7A0 end

    def Function_5_896(): pass

    label("Function_5_896")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8D0")

    ChrTalk(
        0xA,
        "(...I-I could grab her hand now...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E7")

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8DE")
    Jump("loc_8E7")

    label("loc_8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8E7")

    label("loc_8E7")

    TalkEnd(0xFE)
    Return()

    # Function_5_896 end

    def Function_6_8EB(): pass

    label("Function_6_8EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_945")

    ChrTalk(
        0xB,
        "Wow, so many fireworks are going up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Uh uh, how pretty...\x02",
    )

    CloseMessageWindow()
    Jump("loc_95C")

    label("loc_945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_953")
    Jump("loc_95C")

    label("loc_953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_95C")

    label("loc_95C")

    TalkEnd(0xFE)
    Return()

    # Function_6_8EB end

    def Function_7_960(): pass

    label("Function_7_960")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97E")
    Call(0, 8)
    Jump("loc_A25")

    label("loc_97E")


    ChrTalk(
        0xC,
        (
            "Actually, I wanted to stay at the hotel,\x01",
            "but I couldn't get a reservation no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, Rimah seems to have had fun,\x01",
            "so I guess it was worth coming.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A25")

    Jump("loc_A5D")

    label("loc_A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_A38")
    Jump("loc_A5D")

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A46")
    Jump("loc_A5D")

    label("loc_A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A54")
    Jump("loc_A5D")

    label("loc_A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_A5D")

    label("loc_A5D")

    TalkEnd(0xFE)
    Return()

    # Function_7_960 end

    def Function_8_A61(): pass

    label("Function_8_A61")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xC,
        (
            "*phew*, today I really\x01",
            "played all day long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Rimah, did you have fun?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes, I did!!\x01",
            "Thank you, papa!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Uh uh, thank you for all you did.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_8_A61 end

    def Function_9_B21(): pass

    label("Function_9_B21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3F")
    Call(0, 8)
    Jump("loc_BAC")

    label("loc_B3F")


    ChrTalk(
        0xD,
        "Uh uh, thank you for all you did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When we go home, I'll prepare\x01",
            "a lot of delicious dishes for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAC")

    Jump("loc_BE4")

    label("loc_BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_BBF")
    Jump("loc_BE4")

    label("loc_BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BCD")
    Jump("loc_BE4")

    label("loc_BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BDB")
    Jump("loc_BE4")

    label("loc_BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_BE4")

    label("loc_BE4")

    TalkEnd(0xFE)
    Return()

    # Function_9_B21 end

    def Function_10_BE8(): pass

    label("Function_10_BE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C06")
    Call(0, 8)
    Jump("loc_CAA")

    label("loc_C06")


    ChrTalk(
        0xE,
        (
            "At the top of Mirror Castle\x01",
            "I prayed to stay together forever\x01",
            "with papa and mama!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I rode the ferris wheel and the Haunted\x01",
            "Coaster too...I really had fun!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAA")

    Jump("loc_CE2")

    label("loc_CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_CBD")
    Jump("loc_CE2")

    label("loc_CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CCB")
    Jump("loc_CE2")

    label("loc_CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_CD9")
    Jump("loc_CE2")

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_CE2")

    label("loc_CE2")

    TalkEnd(0xFE)
    Return()

    # Function_10_BE8 end

    def Function_11_CE6(): pass

    label("Function_11_CE6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 0, -61000, 0)
    SetChrPos(0x102, -700, 0, -61700, 0)
    SetChrPos(0x103, 600, 0, -62100, 0)
    SetChrPos(0x104, 100, 0, -63000, 0)
    SetChrPos(0x105, 1000, 0, -63500, 0)
    SetChrPos(0x109, -950, 0, -63100, 0)
    OP_68(0, 4500, -53000, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1500, -53000, 5000)

    def lambda_DB9():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DB9)
    Sleep(50)

    def lambda_DD1():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DD1)
    Sleep(50)

    def lambda_DE9():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DE9)
    Sleep(50)

    def lambda_E01():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E01)
    Sleep(50)

    def lambda_E19():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E19)
    Sleep(50)

    def lambda_E31():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E31)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00107F#6PT-Those are...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PThe banners have changed!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PHey now, this is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-4000, 1000, -38000, 0)
    OP_68(-4000, 1000, -33000, 5500)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    SetCameraDistance(26000, 5500)
    SetChrPos(0x101, -3500, 0, -42000, 0)
    SetChrPos(0x102, -4100, 0, -42900, 0)
    SetChrPos(0x103, -2900, 0, -43100, 0)
    SetChrPos(0x104, -3400, 0, -44200, 0)
    SetChrPos(0x105, -2000, 0, -44500, 0)
    SetChrPos(0x109, -4900, 0, -44100, 0)

    def lambda_100C():
        OP_9B(0x0, 0x101, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_100C)
    Sleep(50)

    def lambda_1024():
        OP_9B(0x0, 0x102, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1024)
    Sleep(50)

    def lambda_103C():
        OP_9B(0x0, 0x103, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_103C)
    Sleep(50)

    def lambda_1054():
        OP_9B(0x0, 0x104, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1054)
    Sleep(50)

    def lambda_106C():
        OP_9B(0x0, 0x105, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_106C)
    Sleep(50)

    def lambda_1084():
        OP_9B(0x0, 0x109, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1084)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x109,
        "#10108F#6PW-When did such a thing...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#6PHm, I don't think it's a\x01",
            "night time limited event...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...I don't know\x01",
            "anything about that...\x02\x03",
            "#00201FAlso...\x01",
            "It is impossible for Michey to\x01",
            "change into another character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P...I know.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PThat's──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 4500, -7000, 0)
    MoveCamera(0, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    OP_68(0, 9500, 0, 7000)
    MoveCamera(0, 18, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(20000, 7000)
    OP_6F(0x79)
    OP_0D()
    SetMessageWindowPos(50, 160, -1, -1)

    AnonymousTalk(
        0x102,
        "#00105FThe "Fool's Wonderland"...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00306FHasn't the name been\x01",
            "completely rewritten...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(280, 160, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10113FA-Are we having\x01",
            "a dream, perhaps...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 160, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10306F...Even if it was a dream...\x01",
            "It would look like some sort of nightmare.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    AnonymousTalk(
        0x101,
        "#00008F............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-3580, 1000, -32790, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24640, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#5P──It seems that KeA\x01",
            "is up ahead.\x02\x03",
            "#00013FThen...\x01",
            "We can only enter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PNo choice but to go...!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2890, 0, -32110, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x146, 1)
    OP_29(0xA5, 0x1, 0xA)
    EventEnd(0x5)
    Return()

    # Function_11_CE6 end

    def Function_12_149C(): pass

    label("Function_12_149C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(780, 1600, -58060, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 600, 0, -57250, 0)
    SetChrPos(0xEF, -600, 0, -57250, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00002FAh.........\x02",
    )

    CloseMessageWindow()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopSound(821, 500, 100)
    Sleep(500)
    SetScenarioFlags(0x15B, 2)
    SetScenarioFlags(0x22, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_149C end

    def Function_13_1575(): pass

    label("Function_13_1575")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(780, 1600, -58060, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 600, 0, -57250, 0)
    SetChrPos(0xEF, -600, 0, -57250, 0)
    FadeToBright(1000, 0)
    OP_0D()
    TurnDirection(0x101, 0xEF, 500)

    ChrTalk(
        0x101,
        (
            "#12P#00004F...Alright, then should we\x01",
            "go to the guest house?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1656")

    ChrTalk(
        0x102,
        "#00102FYes, understood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16E7")

    label("loc_1656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_167C")

    ChrTalk(
        0x103,
        "#00202FRoger that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16E7")

    label("loc_167C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_169C")

    ChrTalk(
        0x104,
        "#00309FYeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16E7")

    label("loc_169C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_16BD")

    ChrTalk(
        0x109,
        "#10109FRoger!\x02",
    )

    CloseMessageWindow()
    Jump("loc_16E7")

    label("loc_16BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_16E7")

    ChrTalk(
        0x105,
        "#10304FHu hu, you're right.\x02",
    )

    CloseMessageWindow()

    label("loc_16E7")

    OP_5A()
    ClearMapFlags(0x10000000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -57250, 0)
    EventEnd(0x5)
    Return()

    # Function_13_1575 end

    def Function_14_170E(): pass

    label("Function_14_170E")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FEven the theme park at night\x01",
            "looks fun, but that will have to\x01",
            "wait for a future opportunity.\x02\x03",
            "Quick, let's head to the guest house.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_14_170E end

    def Function_15_17B5(): pass

    label("Function_15_17B5")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a theme park\x01",
            "sketch drawn.\x02\x03",
            "It seems there are many kinds\x01",
            "of amusements attractions one\x01",
            "near the other on the large site.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_15_17B5 end

    def Function_16_184E(): pass

    label("Function_16_184E")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   ～To The Park Visitors～\x01\x01",
            "In this theme park, we firmly\x01",
            "do not accept acts of violence and\x01",
            "possession of dangerous materials.\x01\x01",
            "Also, we kindly ask that children must\x01",
            "be accompanied by their guardians.\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_16_184E end

    SaveToFile()

Try(main)
