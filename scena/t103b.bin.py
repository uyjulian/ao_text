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
        "MWL Staff",              # 1
        "MWL Staff",              # 2
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
        "Function_4_7A3",          # 04, 4
        "Function_5_88B",          # 05, 5
        "Function_6_8E0",          # 06, 6
        "Function_7_94F",          # 07, 7
        "Function_8_A55",          # 08, 8
        "Function_9_B09",          # 09, 9
        "Function_10_BC3",         # 0A, 10
        "Function_11_CBA",         # 0B, 11
        "Function_12_1452",        # 0C, 12
        "Function_13_1525",        # 0D, 13
        "Function_14_16BB",        # 0E, 14
        "Function_15_174F",        # 0F, 15
        "Function_16_17CB",        # 10, 16
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E3")

    ChrTalk(
        0x8,
        (
            "The theme park is\x01",
            "conducting nighttime\x01",
            "operations right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our night parade where Mishy\x01",
            "and the others go around the\x01",
            "park has been a great success.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68B")

    ChrTalk(
        0x103,
        (
            "#00203F...To be honest, I\x01",
            "wanted to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, well, it can't be\x01",
            "helped this time. We'll\x01",
            "do it next chance we get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FHaha... We have to, ok?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DB")

    label("loc_68B")


    ChrTalk(
        0x101,
        (
            "#00003F(Hmm. If I had asked Tio\x01",
            "she probably would've\x01",
            "wanted to see it...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DB")

    SetScenarioFlags(0x0, 0)
    Jump("loc_783")

    label("loc_6E3")


    ChrTalk(
        0x8,
        (
            "The theme park is\x01",
            "conducting nighttime\x01",
            "operations right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our night parade where Mishy\x01",
            "and the others go around the\x01",
            "park has been a great success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_783")

    Jump("loc_79F")

    label("loc_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_796")
    Jump("loc_79F")

    label("loc_796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_79F")

    label("loc_79F")

    TalkEnd(0xFE)
    Return()

    # Function_3_515 end

    def Function_4_7A3(): pass

    label("Function_4_7A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_870")

    ChrTalk(
        0x9,
        (
            "We launch 100 fireworks\x01",
            "In Michelam's famous\x01",
            "firework display daily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You can of course see them from the\x01",
            "park, but people often see them from\x01",
            "the hotel or night airship cruises.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_887")

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_87E")
    Jump("loc_887")

    label("loc_87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_887")

    label("loc_887")

    TalkEnd(0xFE)
    Return()

    # Function_4_7A3 end

    def Function_5_88B(): pass

    label("Function_5_88B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8C5")

    ChrTalk(
        0xA,
        (
            "(...I-I could grab her\x01",
            "hand now...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DC")

    label("loc_8C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8D3")
    Jump("loc_8DC")

    label("loc_8D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8DC")

    label("loc_8DC")

    TalkEnd(0xFE)
    Return()

    # Function_5_88B end

    def Function_6_8E0(): pass

    label("Function_6_8E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_934")

    ChrTalk(
        0xB,
        (
            "Wow, there's so many\x01",
            "fireworks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Haha, how pretty...\x02",
    )

    CloseMessageWindow()
    Jump("loc_94B")

    label("loc_934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_942")
    Jump("loc_94B")

    label("loc_942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_94B")

    label("loc_94B")

    TalkEnd(0xFE)
    Return()

    # Function_6_8E0 end

    def Function_7_94F(): pass

    label("Function_7_94F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96D")
    Call(0, 8)
    Jump("loc_A19")

    label("loc_96D")


    ChrTalk(
        0xC,
        (
            "I actually wanted to stay at the\x01",
            "hotel, but I couldn't get a\x01",
            "reservation no matter what I did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, Rimah seems to\x01",
            "have had fun, so I guess\x01",
            "it was worth coming.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A19")

    Jump("loc_A51")

    label("loc_A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_A2C")
    Jump("loc_A51")

    label("loc_A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A3A")
    Jump("loc_A51")

    label("loc_A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A48")
    Jump("loc_A51")

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_A51")

    label("loc_A51")

    TalkEnd(0xFE)
    Return()

    # Function_7_94F end

    def Function_8_A55(): pass

    label("Function_8_A55")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xC,
        (
            "Phew! I really played my\x01",
            "heart out today.\x02",
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
            "Yes, I did!! Thanks\x01",
            "dad!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha, thanks for\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_8_A55 end

    def Function_9_B09(): pass

    label("Function_9_B09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B27")
    Call(0, 8)
    Jump("loc_B87")

    label("loc_B27")


    ChrTalk(
        0xD,
        (
            "Haha, thanks for\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When we go home, I'll\x01",
            "prepare a nice large\x01",
            "meal for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B87")

    Jump("loc_BBF")

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_B9A")
    Jump("loc_BBF")

    label("loc_B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BA8")
    Jump("loc_BBF")

    label("loc_BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BB6")
    Jump("loc_BBF")

    label("loc_BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_BBF")

    label("loc_BBF")

    TalkEnd(0xFE)
    Return()

    # Function_9_B09 end

    def Function_10_BC3(): pass

    label("Function_10_BC3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE1")
    Call(0, 8)
    Jump("loc_C7E")

    label("loc_BE1")


    ChrTalk(
        0xE,
        (
            "At the top of Mirror Castle\x01",
            "I prayed to stay with mama\x01",
            "and papa forever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I rode the ferris wheel\x01",
            "and the haunted coaster\x01",
            "too... I had tons of fun!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7E")

    Jump("loc_CB6")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_C91")
    Jump("loc_CB6")

    label("loc_C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C9F")
    Jump("loc_CB6")

    label("loc_C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_CAD")
    Jump("loc_CB6")

    label("loc_CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_CB6")

    label("loc_CB6")

    TalkEnd(0xFE)
    Return()

    # Function_10_BC3 end

    def Function_11_CBA(): pass

    label("Function_11_CBA")

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

    def lambda_D8D():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D8D)
    Sleep(50)

    def lambda_DA5():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DA5)
    Sleep(50)

    def lambda_DBD():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DBD)
    Sleep(50)

    def lambda_DD5():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DD5)
    Sleep(50)

    def lambda_DED():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DED)
    Sleep(50)

    def lambda_E05():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E05)
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
        "#00107F#6PT-That's...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PThe banners changed!?\x02",
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

    def lambda_FD8():
        OP_9B(0x0, 0x101, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FD8)
    Sleep(50)

    def lambda_FF0():
        OP_9B(0x0, 0x102, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FF0)
    Sleep(50)

    def lambda_1008():
        OP_9B(0x0, 0x103, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1008)
    Sleep(50)

    def lambda_1020():
        OP_9B(0x0, 0x104, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1020)
    Sleep(50)

    def lambda_1038():
        OP_9B(0x0, 0x105, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1038)
    Sleep(50)

    def lambda_1050():
        OP_9B(0x0, 0x109, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1050)
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
        "#10108F#6PW-When did this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#6PHmm, I don't think it's\x01",
            "a nighttime event,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...I've never of heard\x01",
            "anything like that.\x02\x03",
            "#00201FAlso... It's impossible\x01",
            "for Mishy to change into\x01",
            "another character.\x02",
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
        "#00005F#6PThat's─\x02",
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
        "#00105F"Fool's Wonderland"...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00306FThe name's been\x01",
            "completely rewritten!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(280, 160, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10113FA-Are we having a dream,\x01",
            "maybe?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 160, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10306FEven if it is a dream,\x01",
            "it's some kind of\x01",
            "nightmare, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    AnonymousTalk(
        0x101,
        "#00008F...............\x02",
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
            "#00003F#5P─It seems that KeA is up\x01",
            "ahead.\x02\x03",
            "#00013FIf that's the case... we\x01",
            "have no choice but to\x01",
            "enter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PWe have to go!\x02",
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

    # Function_11_CBA end

    def Function_12_1452(): pass

    label("Function_12_1452")

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
        "#6P#00002FAh...\x02",
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

    # Function_12_1452 end

    def Function_13_1525(): pass

    label("Function_13_1525")

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
            "#12P#00004FAlright then, I think\x01",
            "it's time to head to the\x01",
            "guest house.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1610")

    ChrTalk(
        0x102,
        "#00102FYes, understood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1694")

    label("loc_1610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1631")

    ChrTalk(
        0x103,
        "#00202FRoger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1694")

    label("loc_1631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1651")

    ChrTalk(
        0x104,
        "#00309FYeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1694")

    label("loc_1651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1672")

    ChrTalk(
        0x109,
        "#10109FRoger!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1694")

    label("loc_1672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1694")

    ChrTalk(
        0x105,
        "#10304FHehe, right.\x02",
    )

    CloseMessageWindow()

    label("loc_1694")

    OP_5A()
    ClearMapFlags(0x10000000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -57250, 0)
    EventEnd(0x5)
    Return()

    # Function_13_1525 end

    def Function_14_16BB(): pass

    label("Function_14_16BB")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe park looks fun at night\x01",
            "as well, but we'll have to\x01",
            "save that for next time.\x02\x03",
            "Let's hurry to the guest\x01",
            "house.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_14_16BB end

    def Function_15_174F(): pass

    label("Function_15_174F")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a sketch map of the\x01",
            "theme park.\x02\x03",
            "There are various\x01",
            "attractions lined up\x01",
            "across its vast grounds.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_15_174F end

    def Function_16_17CB(): pass

    label("Function_16_17CB")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～To Park Visitors～\x01",
            "In this theme park, reckless behavior and possession\x01",
            "of dangerous materials are prohibited. Also, we kindly\x01",
            "ask that children be accompanied by their guardians.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_16_17CB end

    SaveToFile()

Try(main)
