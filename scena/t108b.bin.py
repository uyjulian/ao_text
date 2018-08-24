from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t108b.bin",                # FileName
        "t108b",                    # MapName
        "t108b",                    # Location
        0x0042,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 2, 0, 3],
    )

    BuildStringList((
        "t108b",                  # 0
        "Rixia",                  # 1
        "Lotti",                  # 2
        "Zork",                   # 3
        "Randy",                  # 4
        "Wazy",                   # 5
        "KeA",                    # 6
    ))

    AddCharChip((
        "chr/ch05202.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch25900.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294866587, 0,       8260,    270,  385,  0x0, 0,   1,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(4294952456, 0,       6570,    90,   389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0040, 0, 12,  12.0,                  12.0,                  -1.0,                  56.25,                 [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666667014360428,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.8000000715255737,   -0.8000000715255737,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 16,  -110.0,                10.0,                  -1.0,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   55.0,                  -2.5,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 17,  -100.0,                14.0,                  -1.0,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   25.0,                  -7.0,                  0.20000000298023224,   1.0])

    DeclActor(4294954046, 0,       6540,    1500,    4294952456, 1500,    6570,    0x007E, 0,  5,  0x0000)

    ChipFrameInfo(724, 0)                                        # 0

    ScpFunction((
        "Function_0_2D4",          # 00, 0
        "Function_1_38C",          # 01, 1
        "Function_2_3ED",          # 02, 2
        "Function_3_46A",          # 03, 3
        "Function_4_548",          # 04, 4
        "Function_5_8E1",          # 05, 5
        "Function_6_8E5",          # 06, 6
        "Function_7_975",          # 07, 7
        "Function_8_31C0",         # 08, 8
        "Function_9_3222",         # 09, 9
        "Function_10_326F",        # 0A, 10
        "Function_11_3AF7",        # 0B, 11
        "Function_12_405C",        # 0C, 12
        "Function_13_447E",        # 0D, 13
        "Function_14_5D66",        # 0E, 14
        "Function_15_63BA",        # 0F, 15
        "Function_16_6448",        # 10, 16
        "Function_17_64DB",        # 11, 17
    ))


    def Function_0_2D4(): pass

    label("Function_0_2D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_314"),
        (1, "loc_320"),
        (2, "loc_32C"),
        (3, "loc_338"),
        (4, "loc_344"),
        (5, "loc_350"),
        (6, "loc_35C"),
        (SWITCH_DEFAULT, "loc_368"),
    )


    label("loc_314")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_320")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_32C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_338")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_344")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_350")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_35C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_368")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_374")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_38B")

    Return()

    # Function_0_2D4 end

    def Function_1_38C(): pass

    label("Function_1_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EC")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_38C")

    label("loc_3EC")

    Return()

    # Function_1_38C end

    def Function_2_3ED(): pass

    label("Function_2_3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_3FB")
    Jump("loc_418")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_418")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_42C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 7)
    Jump("loc_469")

    label("loc_42C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_443")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 11)
    Jump("loc_469")

    label("loc_443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_45A")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 14)
    Jump("loc_469")

    label("loc_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_469")
    ClearScenarioFlags(0x22, 3)
    Event(0, 13)

    label("loc_469")

    Return()

    # Function_2_3ED end

    def Function_3_46A(): pass

    label("Function_3_46A")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_47C")
    Jump("loc_489")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_489")
    OP_66(0x0, 0x1)

    label("loc_489")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A1")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B4")
    OP_1B(0x1, 0x0, 0xA)

    label("loc_4B4")

    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DB")
    OP_1B(0x6, 0x0, 0xF)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51F")
    OP_7D(0xAA, 0xAA, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x1, 0x1)
    Jump("loc_547")

    label("loc_51F")

    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_547")

    Return()

    # Function_3_46A end

    def Function_4_548(): pass

    label("Function_4_548")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_6BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_699")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, sir... Are you\x01",
            "leaving already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYeah, I've been invited\x01",
            "to the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I-I see. Goodbye then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(N-No waaay... I almost\x01",
            "haven't taken care of\x01",
            "him at all yeeet!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, what a strange\x01",
            "girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...You're doing it on\x01",
            "purpose, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6B8")

    label("loc_699")


    ChrTalk(
        0xFE,
        (
            "*sigh*... Goodbye\x01",
            "then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B8")

    Jump("loc_8C1")

    label("loc_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87D")

    ChrTalk(
        0xFE,
        "Oh, Wazy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I believe Wazy has\x01",
            "already gone to the\x01",
            "guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "N-No waaay... I almost\x01",
            "haven't taken care of\x01",
            "him at all yeeet!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_7AA")

    ChrTalk(
        0x102,
        (
            "#00106F(That's Wazy for you.\x01",
            "He's sure is popular...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_875")

    label("loc_7AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_7F5")

    ChrTalk(
        0x103,
        (
            "#00203F(That's Wazy for you.\x01",
            "He's really is\x01",
            "popular...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_875")

    label("loc_7F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_831")

    ChrTalk(
        0x104,
        (
            "#00301F(That bastard is\x01",
            "popular, huh...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_875")

    label("loc_831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_875")

    ChrTalk(
        0x109,
        (
            "#10106F(As expected from Wazy,\x01",
            "he's a popular guy...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_875")

    SetScenarioFlags(0x0, 1)
    Jump("loc_8C1")

    label("loc_87D")


    ChrTalk(
        0xFE,
        (
            "*sigh*... I wish I had\x01",
            "taken care of Mr. Wazy a\x01",
            "little more...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C1")

    Jump("loc_8DD")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8D4")
    Jump("loc_8DD")

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8DD")

    label("loc_8DD")

    TalkEnd(0xFE)
    Return()

    # Function_4_548 end

    def Function_5_8E1(): pass

    label("Function_5_8E1")

    Call(0, 6)
    Return()

    # Function_5_8E1 end

    def Function_6_8E5(): pass

    label("Function_6_8E5")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_95A")

    ChrTalk(
        0xA,
        (
            "The bar counter will be\x01",
            "closing soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please be aware that you\x01",
            "can't order late at\x01",
            "night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_971")

    label("loc_95A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_968")
    Jump("loc_971")

    label("loc_968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_971")

    label("loc_971")

    TalkEnd(0xA)
    Return()

    # Function_6_8E5 end

    def Function_7_975(): pass

    label("Function_7_975")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_998")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_998")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9AF")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C6")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7D), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9DD")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7C), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9F4")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9F4")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A31")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A4E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A6B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A88")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9F")
    SetScenarioFlags(0x147, 2)
    Jump("loc_AF6")

    label("loc_A9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB6")
    SetScenarioFlags(0x147, 3)
    Jump("loc_AF6")

    label("loc_AB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACD")
    SetScenarioFlags(0x147, 4)
    Jump("loc_AF6")

    label("loc_ACD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE4")
    SetScenarioFlags(0x147, 5)
    Jump("loc_AF6")

    label("loc_AE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF6")
    SetScenarioFlags(0x147, 6)

    label("loc_AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF8")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆I like Elie\x01",       # 0
            "◆I like Tio\x01",        # 1
            "◆I like Randy\x01",      # 2
            "◆I like Noｱl\x01",      # 3
            "◆I like Wazy\x01",       # 4
            "◆No change\x01",         # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B8F"),
        (1, "loc_BA3"),
        (2, "loc_BB7"),
        (3, "loc_BCB"),
        (4, "loc_BDF"),
        (5, "loc_BF3"),
        (SWITCH_DEFAULT, "loc_BF3"),
    )


    label("loc_B8F")

    SetScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BF8")

    label("loc_BA3")

    ClearScenarioFlags(0x147, 2)
    SetScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BF8")

    label("loc_BB7")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    SetScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BF8")

    label("loc_BCB")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    SetScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BF8")

    label("loc_BDF")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    SetScenarioFlags(0x147, 6)
    Jump("loc_BF8")

    label("loc_BF3")

    Jump("loc_BF8")

    label("loc_BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_C0A")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_C4D")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_C1C")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_C4D")

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_C2E")
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_C4D")

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_C40")
    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_C4D")

    label("loc_C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_C4D")
    AddParty(0x4, 0xEF, 0xFF)

    label("loc_C4D")

    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(4111)
    SoundLoad(4112)
    SoundLoad(3397)
    SoundLoad(2912)
    SoundLoad(3518)
    SoundLoad(2758)
    SoundLoad(2678)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis246.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00200.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(5, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10301.itp")
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x101, -100000, 0, -80000, 180)
    ClearMapObjFlags(0x7, 0x10)
    OP_74(0x7, 0xF)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00008F#30WRight... Right.\x02\x03",
            "#00000FI see. If that's the\x01",
            "case it should be fine.\x02\x03",
            "#00006F#20WSorry for going without\x01",
            "you.\x02\x03",
            "#00002F...Haha, understood. At\x01",
            "least we got our energy\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-100000, 2000, -80000, 0)
    MoveCamera(325, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    FadeToBright(1000, 0)
    OP_68(-100000, 1000, -80000, 3000)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#11PHmph... So there's\x01",
            "nothing at the Support\x01",
            "Section, huh.\x02\x03",
            "#00008FI do think I worry a\x01",
            "little too much, but...\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 50, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4111V#40WUhuhu... How do you do,\x01",
            "ladies and gentlemen of the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4112V#40WI've left for you a little\x01",
            "something to remember me by.\x01",
            "I do hope you enjoy it.㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0x1010)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#11P(He's probably the one who\x01",
            "gave the tower data to the\x01",
            "terrorists.)\x02\x03",
            "(But... it didn't seem like\x01",
            "he was their ally.)\x02\x03",
            "#00008F(And like Yin said, he isn't\x01",
            "even a member of Heiyue or\x01",
            "Red Constellation...)\x02\x03",
            "#00001F(...Just who is he?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_171C")
    SetChrPos(0x102, -100000, 0, -74900, 180)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x102,
        "Elie's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3397V#2S#5P#30W#18ALloyd? Still there?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00005F#6POh, Elie.\x02\x03",
            "#00002FIt's fine, come on in.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 8)
    WaitChrThread(0x102, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Oh, were you on a call?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, with chief.\x02\x03",
            "#00008FI was wondering if anything\x01",
            "happened during our vacation, so\x01",
            "I called the Support Section.\x02\x03",
            "#00000FLooks like I was worried for\x01",
            "nothing, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PI see...\x02\x03",
            "#00108FI understand you're worried\x01",
            "because of the events of the\x01",
            "trade conference, but...\x02\x03",
            "#00102FLet's enjoy our day off\x01",
            "without thinking about any\x01",
            "of those things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha... You're right.\x02\x03",
            "#00002FSorry, did you come to\x01",
            "get me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PAh, yes... I didn't see\x01",
            "you.\x02\x03",
            "#00108FI was thinking of going\x01",
            "to the guest house\x01",
            "together, if you like.\x02\x03",
            "#00113F...That is, if it's not\x01",
            "a bother.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00011F#6PI-It's not a bother at\x01",
            "all!\x02\x03",
            "#00006FDamn... Elie, are you\x01",
            "making fun of me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PI-I didn't intend to...\x02\x03",
            "#00109FA-Alright, let's go\x01",
            "together then.\x02\x03",
            "There's still time until\x01",
            "dinner, so we can make a\x01",
            "few side trips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PS-Sure. Let's take a\x01",
            "look in the stores\x01",
            "downstairs.\x02\x03",
            "#00012F(Wait, why am I so\x01",
            "flustered when it's just\x01",
            "the two of us...?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_317C")

    label("loc_171C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1CD4")
    SetChrPos(0x103, -100000, 0, -74900, 180)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x103,
        "Tio's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2678V#2S#5P#30W#18ALloyd. May I have a\x01",
            "moment?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00005F#6POh, Tio.\x02\x03",
            "#00002FIt's fine, come on in.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 8)
    WaitChrThread(0x103, 3)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x103,
        "Was that the chief?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha, you know everything.\x02\x03",
            "#00008FI was wondering if anything\x01",
            "happened during our vacation, so\x01",
            "I called the Support Section.\x02\x03",
            "#00000FLooks like I was worried for\x01",
            "nothing, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PI see...\x02\x03",
            "#00208FIt's true that some\x01",
            "concerning things remain\x01",
            "about that hacker, but...\x02\x03",
            "#00202FIt's our long-awaited\x01",
            "vacation, so shouldn't\x01",
            "you relax?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha... You're right.\x02\x03",
            "#00002FSorry, did you come to\x01",
            "get me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PYes, everyone is heading for the\x01",
            "guest house little by little.\x02\x03",
            "#00200FWell, it seems there's still\x01",
            "time before the dinner party so\x01",
            "there's no need to hurry, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PNo, I'm going too.\x02\x03",
            "Would you like to go to\x01",
            "the guest house with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#11P...Yes.\x02\x03",
            "#00208FUhhm, can we look in the\x01",
            "stores downstairs?\x02\x03",
            "#00206FUhhm, I'm a little\x01",
            "reluctant going in\x01",
            "alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#11PI-Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PN-No no!\x02\x03",
            "#00002FUnderstood. A few\x01",
            "detours, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11P...Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P(Hmm. It's refreshing that\x01",
            "Tio is showing interest in\x01",
            "normal stores...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_317C")

    label("loc_1CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_2312")
    SetChrPos(0x104, -100000, 0, -74900, 180)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x104,
        "Randy's Voice",
        (
            "#2758V#5P#30W#19AOops. As I thought,\x01",
            "you're still in our\x01",
            "room.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 9)
    OP_93(0x101, 0x0, 0x1F4)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x101,
        "#00002F#6POh, Randy.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x104,
        (
            "What, were you on the phone with\x01",
            "someone?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah, with chief.\x02\x03",
            "#00008FI was wondering if anything\x01",
            "happened during our vacation, so\x01",
            "I called the Support Section.\x02\x03",
            "#00000FLooks like I was worried for\x01",
            "nothing, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#11PI see...\x02\x03",
            "#00303FWell, uncle and the others\x01",
            "are still in Crossbell...\x02\x03",
            "#00300FTo be honest, I'm worried\x01",
            "too, but isn't it ok to have\x01",
            "fun at least for today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha... You're right.\x02\x03",
            "#00002FSorry, did you come to\x01",
            "get me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PYeah, everyone's heading for the\x01",
            "guest house little by little.\x02\x03",
            "#00300FThere's still time before the\x01",
            "dinner party so I think it'll be\x01",
            "alright if you take your time, but.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo, I'm going too.\x02\x03",
            "#00002FBy the way, Randy, you\x01",
            "looked in the jewelry\x01",
            "store today, didn't you.\x02\x03",
            "How was their selection\x01",
            "and everything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#11PYeah, well it was a good as\x01",
            "you'd expect from a store\x01",
            "with such expensive stuff...\x02\x03",
            "#00302FWhat, you lookin' for a\x01",
            "present for a girl you're\x01",
            "into?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PN-No... I-I was just\x01",
            "curious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PNow, now, don't be shy.\x02\x03",
            "#00302FAlright, if you wanna\x01",
            "stop by, your bro will\x01",
            "give ya some advice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI'm telling you, that's\x01",
            "not it...\x02\x03",
            "#00000FWell, whatever. Anyway,\x01",
            "shall we go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_317C")

    label("loc_2312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_2A3A")
    SetChrPos(0x109, -100000, 0, -74900, 180)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x109,
        "Noｱl's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3518V#2S#5P#30W#19A...Lloyd. Are you there?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00005F#6POh, Noｱl.\x02\x03",
            "#00002FIt's fine, come on in.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 3, 0, 8)
    WaitChrThread(0x109, 3)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x109,
        (
            "Ah, were you on a call with\x01",
            "someone?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, with chief.\x02\x03",
            "#00008FI was wondering if anything\x01",
            "happened during our vacation, so\x01",
            "I called the Support Section.\x02\x03",
            "#00000FLooks like I was worried for\x01",
            "nothing, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#11P...Is that so.\x02\x03",
            "#10106FAfter what happened, I\x01",
            "can understand why\x01",
            "you're worried...\x02\x03",
            "#10108F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6POh c'mon. It's not\x01",
            "something you should even\x01",
            "have to worry about, right?\x02\x03",
            "#00006FAh, sorry. For saying\x01",
            "something so depressing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#11PN-No, I should apologize\x01",
            "too.\x02\x03",
            "#10106FIn spite of myself, I'm\x01",
            "a worrier and end up\x01",
            "worrying about things...\x02\x03",
            "#10100FI'm sometimes envious of\x01",
            "how carefree Fran is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha, I see.\x02\x03",
            "#00002FThen I guess we're\x01",
            "pretty similar, in a\x01",
            "way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#11PT-That's not true! Our\x01",
            "intellects and such are\x01",
            "completely different!\x02\x03",
            "#10112FYou could say I, umm,\x01",
            "have a simple CGF\x01",
            "personality, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P(Hmm. A strict self-\x01",
            "evaluation as always,\x01",
            "huh.)\x02\x03",
            "#00000FWell, that aside, you\x01",
            "came to pick me up,\x01",
            "right?\x02\x03",
            "Would you like to go to\x01",
            "the guest house with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#11PAh, yes!\x02\x03",
            "#10100FCome to think of it, the dinner party\x01",
            "will be held in an amazing mansion\x01",
            "called the guest house, right?\x02\x03",
            "The place that former Chairman\x01",
            "Hartmann used to live...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah. Honestly, it's\x01",
            "luxurious like you\x01",
            "wouldn't believe.\x02\x03",
            "#00002FI assure you, you'll be\x01",
            "amazed the first time\x01",
            "you step inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PAhaha... Now I'm looking\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_317C")

    label("loc_2A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_317C")
    SetChrPos(0x105, -100000, 0, -74900, 180)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x105,
        "Wazy's Voice",
        (
            "#2912V#5P#30W#20AAh, as I thought, you're\x01",
            "still here.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 9)
    OP_93(0x101, 0x0, 0x1F4)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        "#00002F#6POh, Wazy.\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x5, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CC(0x0, 0x5, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x105,
        (
            "Hehe, I see.\x02\x03",
            "You were worried about the Support\x01",
            "Section building while we were are\x01",
            "away and contacted the chief,\x02\x03",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x5, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6PH-How do you know that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PAfter having been with you\x01",
            "for over a month, I can\x01",
            "read at least that much.\x02\x03",
            "#10302FHehe. Maybe you're even\x01",
            "more of a leader than I\x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha... I'm just a\x01",
            "worrywart.\x02\x03",
            "#00008FIf I were really an\x01",
            "excellent leader, I'd be\x01",
            "composed and ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#11PIf you're asking my opinion,\x01",
            "the excellence of a leader\x01",
            "differs person-to-person.\x02\x03",
            "#10304FYou're pretty smart and you\x01",
            "have sharp senses. But\x01",
            "basically, you're average.\x02\x03",
            "#10302FJust steadily doing your\x01",
            "best where you can, when you\x01",
            "can isn't too bad, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PUgh... Don't say it so\x01",
            "bluntly.\x02\x03",
            "#00013FActually, that side of\x01",
            "you isn't too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PHehe. I like that honesty of yours,\x01",
            "though.\x02\x03",
            "#10302FTo begin with, shrewd people like\x01",
            "that Cao or that joker of an Imperial\x01",
            "agent are shrewd to the very end.\x02\x03",
            "Rather than opposing them in the same\x01",
            "way, wouldn't it be better to\x01",
            "leverage your own strengths?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PHuh, did I say something\x01",
            "weird?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo. It's just that I\x01",
            "haven't thought about it\x01",
            "that way that much...\x02\x03",
            "#00000FThanks, Wazy. I feel\x01",
            "like you opened my eyes\x01",
            "a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PHehe, glad to hear it.\x02\x03",
            "#10300FThen, isn't it about\x01",
            "time to be heading to\x01",
            "the dinner party?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah. Well then, shall\x01",
            "we go together?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_317C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x0)
    OP_74(0x7, 0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -99290, 0, -79530, 0)
    SetScenarioFlags(0x145, 5)
    OP_29(0xA5, 0x1, 0x7)
    OP_1B(0x1, 0x0, 0xA)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_7_975 end

    def Function_8_31C0(): pass

    label("Function_8_31C0")

    OP_68(-100000, 1000, -79000, 2500)
    Sound(121, 0, 100, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)

    def lambda_31EB():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31EB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(890, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_6F(0x79)
    Return()

    # Function_8_31C0 end

    def Function_9_3222(): pass

    label("Function_9_3222")

    OP_68(-100000, 1000, -79000, 2000)

    def lambda_3238():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3238)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(890, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_6F(0x79)
    Return()

    # Function_9_3222 end

    def Function_10_326F(): pass

    label("Function_10_326F")

    EventBegin(0x0)
    Fade(500)
    OP_68(5700, 1000, 13400, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21380, 0)
    SetChrPos(0x101, 5700, 0, 13400, 315)
    SetChrPos(0xEF, 6700, 0, 12400, 315)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00005F#5POh, did someone bring\x01",
            "KeA?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_348F")

    ChrTalk(
        0x102,
        (
            "#00104F#12PYes, Tio's taking her.\x02\x03",
            "#00100FThey should already be\x01",
            "at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5POh, she should be fine,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#12PUmm... Did something\x01",
            "happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, a lot of things have\x01",
            "happened, and I guess I'm\x01",
            "a little nervous.\x02\x03",
            "#00002FBut, we had a great time\x01",
            "at the park, so I\x01",
            "shouldn't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#12PHaha, that's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AD8")

    label("loc_348F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_361B")

    ChrTalk(
        0x103,
        (
            "#00205F#12PYes, Elie's taking her,\x01",
            "but...\x02\x03",
            "#00202FThey may have already\x01",
            "gone to the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5POh, she should be fine,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12P...Did something happen\x01",
            "to KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, a lot of things have\x01",
            "happened, and I guess I'm\x01",
            "a little nervous.\x02\x03",
            "#00002FBut, we had a great time\x01",
            "at the park, so I\x01",
            "shouldn't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12P...You're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AD8")

    label("loc_361B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_37AE")

    ChrTalk(
        0x104,
        (
            "#00305F#12PYeah, milady and PeTiote\x01",
            "were taking her, but...\x02\x03",
            "#00300FMaybe they're already at\x01",
            "the guest house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5POh, she should be fine,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12P...? Somethin' happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, a lot of things have\x01",
            "happened, and I guess I'm\x01",
            "a little nervous.\x02\x03",
            "#00002FBut, we had a great time\x01",
            "at the park, so I\x01",
            "shouldn't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#12PHaha, that's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AD8")

    label("loc_37AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_3949")

    ChrTalk(
        0x109,
        (
            "#10105F#12PAh, Randy and Wazy were\x01",
            "taking her, but...\x02\x03",
            "#10100FI think they're already\x01",
            "at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5POh, she should be fine,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PUmm... Did something\x01",
            "happen to KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, a lot of things have\x01",
            "happened, and I guess I'm\x01",
            "a little nervous.\x02\x03",
            "#00002FBut, we had a great time\x01",
            "at the park, so I\x01",
            "shouldn't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F#12PHaha, that's true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AD8")

    label("loc_3949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_3AD8")

    ChrTalk(
        0x105,
        (
            "#10305F#12PYeah, it looks like the\x01",
            "girls took her.\x02\x03",
            "#10300FMaybe they're already at\x01",
            "the guest house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5POh, she should be fine,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#12P...Did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, a lot of things have\x01",
            "happened, and I guess I'm\x01",
            "a little nervous.\x02\x03",
            "#00002FBut, we had a great time\x01",
            "at the park, so I\x01",
            "shouldn't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#12PHehe... She did look\x01",
            "happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD8")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 5700, 0, 13400, 315)
    SetScenarioFlags(0x145, 6)
    OP_1B(0x1, 0xFF, 0xFFFF)
    EventEnd(0x5)
    Return()

    # Function_10_326F end

    def Function_11_3AF7(): pass

    label("Function_11_3AF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50106.itc", 0x1E)
    LoadChrToIndex("apl/ch51423.itc", 0x1F)
    LoadChrToIndex("apl/ch51424.itc", 0x20)
    LoadChrToIndex("apl/ch50107.itc", 0x21)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, -104650, 400, -81200, 90)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xB, -104650, 400, -84300, 90)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, -104650, 400, -77900, 90)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x7, 0x10)
    OP_74(0x7, 0xF)
    OP_70(0x8, 0x2)
    OP_70(0x9, 0x2)
    OP_70(0xA, 0x2)
    OP_7D(0xAA, 0xAA, 0xFF, 0x0, 0x0)
    OP_68(-95000, 1000, 10000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(-105000, 1000, 10000, 14000)
    Sleep(5000)
    OP_0D()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_68(-103000, 1000, -75900, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    FadeToBright(2000, 0)
    OP_68(-104500, 1000, -81450, 8000)
    OP_6F(0x79)
    SetCameraDistance(21000, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#05203F#5P#30W(......)\x02\x03",
            "#05208F(The Barrier...)\x02\x03",
            "(The Barrier that stands\x01",
            "in our way...)\x02\x03",
            "#05201F(Mayor Dieter is\x01",
            "breaking through it in\x01",
            "his own way, huh...)\x02\x03",
            "#05206F(...But we...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(800)
    SetCameraDistance(20500, 0)
    Sound(898, 0, 100, 0)
    OP_71(0x9, 0x2, 0x5, 0x0, 0x8)
    SetChrFlags(0x101, 0x20)

    def lambda_3D65():
        OP_96(0xFE, 0xFFFE6736, 0x226, 0xFFFEC1D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D65)
    OP_A0(0x101, 1200, 0x0, 0x5)
    ClearChrFlags(0x101, 0x20)
    Sound(812, 0, 100, 0)
    OP_79(0x9)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#05208F#5P(In the mafia incident,\x01",
            "the Barrier just\x01",
            "vanished on its own...)\x02\x03",
            "(And now, an even\x01",
            "greater Barrier stands\x01",
            "in our way...)\x02\x03",
            "#05203F(We are─ I mean I am not\x01",
            "being that useful\x01",
            "again...)\x02\x03",
            "#05213F(...Is that really\x01",
            "alright?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1400, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_A0(0x101, 1000, 0x5, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#05206F#5P(It's no use. I'm tired\x01",
            "but I can't sleep at\x01",
            "all.)\x02\x03",
            "#05200F(I guess I'll go to the\x01",
            "lounge and drink some\x01",
            "water.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0x101, 0x7)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    OP_74(0x9, 0x5)

    def lambda_3F40():
        OP_98(0xFE, 0x0, 0x0, 0x12C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F40)
    OP_71(0x9, 0x5, 0x7, 0x0, 0x8)
    OP_79(0x9)
    WaitChrThread(0x101, 1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    OP_0D()
    Fade(250)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrPos(0x101, -104500, 0, -79950, 0)
    OP_0D()
    Sleep(200)
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_3FB6():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FB6)
    SetCameraDistance(20750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sleep(1000)
    Sound(121, 0, 70, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x0)
    OP_74(0x7, 0x1E)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrPos(0x0, -100000, 0, 6750, 0)
    SetScenarioFlags(0x145, 7)
    OP_29(0xA5, 0x1, 0x8)
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x6, 0x0, 0xF)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_3AF7 end

    def Function_12_405C(): pass

    label("Function_12_405C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SoundLoad(2635)
    SoundLoad(3246)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01801.itp")
    SetChrPos(0x101, 4900, 0, 9150, 45)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 10600, 150, 15400, 90)
    OP_68(4900, 1000, 9150, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F(Ah...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(10600, 1000, 15400, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    SetCameraDistance(20000, 3000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        "#01808F#40W#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#11P...Hey, Rixia.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(11200, 1000, 14250, 4000)
    MoveCamera(315, 23, 0, 4000)

    def lambda_41EE():
        OP_95(0xFE, 11720, 0, 12790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41EE)
    Sound(2635, 255, 80, 0)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        "#30W#3246VIs that you, Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_24(0xCAE)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005F#6P...?\x02\x03",
            "#00012FSorry to call out to you\x01",
            "all of a sudden. Did I\x01",
            "surprise you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#30W#11PAhaha, not at all...\x02\x03",
            "#01802F#30WI was just spacing\x01",
            "out...\x02\x03",
            "#01808F#30W............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PUmm...\x02\x03",
            "#00002FCan I sit there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01803F#30W#11P......(*nods*)\x02",
    )

    CloseMessageWindow()
    OP_68(12100, 1000, 15400, 2000)

    def lambda_43EE():
        OP_95(0xFE, 13000, 0, 15400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43EE)
    Sleep(800)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    OP_6F(0x79)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 13450, 150, 15400, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    OP_68(12100, 1000, 16000, 3500)
    Sleep(700)
    SetChrSubChip(0x8, 0x1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 3)
    NewScene("e430B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_405C end

    def Function_13_447E(): pass

    label("Function_13_447E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch13600.itc", 0x1F)
    LoadChrToIndex("apl/ch51325.itc", 0x20)
    LoadChrToIndex("chr/ch05200.itc", 0x21)
    SoundLoad(3247)
    SoundLoad(3614)
    SoundLoad(3615)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis009.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01150.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis010.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01801.itp")
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 13450, 150, 15400, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 10600, 150, 15400, 90)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 4900, 0, 9150, 90)
    SetChrFlags(0xD, 0x8)
    OP_68(12100, 1000, 15400, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    FadeToBright(2000, 0)
    SetCameraDistance(20000, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#01804F#5PYou're strange, Lloyd.\x02\x03",
            "#01810FYou really are right\x01",
            "there whenever I want\x01",
            "someone by my side.\x02\x03",
            "I feel relieved just\x01",
            "knowing you're there.\x02\x03",
            "#01809FHaha. I guess I'm\x01",
            "jealous of everyone at\x01",
            "the Support Section.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#12PHaha, I think you're\x01",
            "overestimating me.\x02\x03",
            "#00006FI have a long way to go.\x01",
            "As a detective and a\x01",
            "leader both.\x02\x03",
            "#00008FA long, long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01810F#5P#30WEhe...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        (
            "#00003F#12PHey Rixia.\x02\x03",
            "#00008FIt might be rude but,\x01",
            "can I ask you something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01805F#5P...?\x02\x03",
            "#01810FRude? What seems to be\x01",
            "the matter?\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    SetCameraDistance(19000, 70000)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#12PWhy...\x02\x03",
            "#00001FWhy are your eyes so\x01",
            "empty when you smile?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01812F#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12PI feel like they've been\x01",
            "that way ever since I met\x01",
            "you.\x02\x03",
            "#00003FYou danced on the greatest\x01",
            "stage with Ilya...\x02\x03",
            "Rixia Mao is now a\x01",
            "celebrity in Crossbell.\x02\x03",
            "#00001FBut even so, why...\x02\x03",
            "Why does your smile always\x01",
            "make it look like you've\x01",
            "given up on something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01808F#5PWhy would you ask such a\x01",
            "thing...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PIt's because someone I\x01",
            "knew very well smiled just\x01",
            "like that for a time.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00008F#12PNow, that empty smile\x01",
            "can't be seen anymore,\x01",
            "but...\x02\x03",
            "#00001FI suddenly realized that\x01",
            "your smile is just like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01806F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PThe person smiled like that to\x01",
            "try to bear the sorrow of never\x01",
            "seeing their loved ones again.\x02\x03",
            "#00001FIf that's the case, then what\x01",
            "about you?\x02\x03",
            "Why do you smile like that when\x01",
            "Ilya loves you so much?\x02\x03",
            "She's always by your side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01808F#5P...............\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01803F#5PI'm honestly surprised.\x02\x03",
            "#01810FI knew you were observant\x01",
            "but I had no idea it was\x01",
            "to that extent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PThen...?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01804F#5PHaha... You're right.\x02\x03",
            "#01810FI'm thinking of leaving\x01",
            "Crossbell before long...\x01",
            "probably.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#12PI knew it.\x02\x03",
            "#00008FAs for the reason... You\x01",
            "can't tell me, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5P...Yes.\x02\x03",
            "#01808FBut you're right. While\x01",
            "leaving out the\x01",
            "details...\x02\x03",
            "#01810FFor me, it's the path I\x01",
            "must walk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#12PThe path you must\x01",
            "walk...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5PHaha, it's something of a\x01",
            "family business.\x02\x03",
            "#01808FEver since I was little...\x01",
            "I lived for that reason.\x02\x03",
            "The path my ancestors have\x01",
            "inherited for as long as\x01",
            "anyone can remember...\x02\x03",
            "#01803FEven now, I do not know\x01",
            "the reason I walk this\x01",
            "path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PSo that's what it was...\x02\x03",
            "#00001FBut in that case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01810F#5PWhile it may be true this work\x01",
            "is unnecessary... It is a path\x01",
            "that is impossible to reject.\x02\x03",
            "#01804FEven my father told me: find\x01",
            "the meaning in having\x01",
            "inherited the path.\x02\x03",
            "It is a dark and quiet path,\x01",
            "ignorant of the world and the\x01",
            "movements of history.\x02\x03",
            "#01808FAnd I, having inherited the\x01",
            "path from my father, continue\x01",
            "to walk it to this day...\x02\x03",
            "#01810F...Yes, forevermore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#01804F#5PHaha... I'm weird, huh.\x02\x03",
            "I refused the wine Ilya\x01",
            "offered me...\x02\x03",
            "#01810FMaybe I'm drunk on\x01",
            "moonlight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PHaha... Maybe.\x02\x03",
            "#00006FSorry. I guess I probed\x01",
            "where I shouldn't have?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5PNo, it's fine.\x02\x03",
            "#01810FI feel much better\x01",
            "actually.\x02\x03",
            "#01809FThank you for listening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12POh... Glad I could help.\x02\x03",
            "#00001FBut Rixia, could you be─\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    ClearChrFlags(0xD, 0x8)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xD,
        "KeA's Voice",
        "#3614V#50W#13ALloyd!\x02",
    )

    CloseMessageWindow()
    OP_24(0xE1E)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    OP_68(11200, 1000, 14250, 3500)
    MoveCamera(315, 23, 0, 3500)
    OP_9B(0x1, 0xD, 0xFFDD, 0x1770, 0x5DC, 0x0)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetMessageWindowPos(50, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005FKeA...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 160, -1, -1)

    AnonymousTalk(
        0x8,
        "#01805F...Oh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    OP_95(0xD, 11720, 0, 12790, 1200, 0x0)
    OP_93(0xD, 0x0, 0x190)

    ChrTalk(
        0xD,
        (
            "#05805F#30W#6PAh... Rixia's here too!\x02\x03",
            "#05800F#30WWere you guys talking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#5PAh, no. We just\x01",
            "finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PYeah, it's all right.\x02\x03",
            "#00001F...Can't sleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#05808F#30W#6PYeah...\x02\x03",
            "#05806F#30WI feel like I had a\x01",
            "nightmare...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see...\x02\x03",
            "#00000FWant to sleep in my bed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#05812F#30W#6P...Is that ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#11PYeah. Just this once,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrPos(0x101, 13000, 0, 15400, 270)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_68(11950, 1000, 14600, 1500)
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_5647():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5647)
    OP_93(0xD, 0x2D, 0x1F4)
    Sleep(500)

    def lambda_5666():
        OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5666)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xE1, 0x1F4)
    WaitChrThread(0xD, 1)
    OP_6F(0x1)
    SetChrFlags(0xD, 0x8)
    Fade(250)
    OP_68(11950, 1100, 14600, 500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    NpcTalk(
        0x101,
        "KeA",
        "#05809F#30W#5PEhehe...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#6PSorry Rixia. We got\x01",
            "interrupted at an\x01",
            "awkward moment.\x02",
        )
    )

    CloseMessageWindow()
    Fade(300)
    Sound(812, 0, 100, 0)
    SetChrPos(0x8, 11000, 0, 15400, 90)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_93(0x8, 0x87, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#01809F#5PHaha, don't worry about\x01",
            "it.\x02\x03",
            "#01802FI feel like I can get to\x01",
            "sleep too, thanks to\x01",
            "you.\x02\x03",
            "#01804FThank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01808F#5P...What we talked about.\x01",
            "Can I ask you to keep it a\x01",
            "secret from Ilya?\x02\x03",
            "#01810FI plan to find an\x01",
            "opportunity sooner or\x01",
            "later and tell her myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PGot it.\x02\x03",
            "#00000FI might not be very\x01",
            "dependable, but please tell\x01",
            "me if anything happens.\x02\x03",
            "I'll do whatever I can for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#5PHaha... Thanks.\x02\x03",
            "#01802FThen, if there's ever anything\x01",
            "bothering you, I would be\x01",
            "happy to discuss it with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        "#3247V#40WGood night Lloyd, KeA.\x02",
    )

    CloseMessageWindow()
    OP_24(0xCAF)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    ChrTalk(
        0x101,
        "#00002F#6PNight Rixia.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x101,
        "KeA",
        "#05809F#3615V#50W#12PNiiight...\x02",
    )

    CloseMessageWindow()
    OP_24(0xE1F)
    OP_C9(0x1, 0x80000000)
    OP_68(12900, 1000, 13970, 5000)

    def lambda_5AA5():

        label("loc_5AA5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5AA5")

    QueueWorkItem2(0x101, 2, lambda_5AA5)
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_5ABE():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5ABE)
    WaitChrThread(0x8, 1)

    def lambda_5AD7():
        OP_9B(0x0, 0xFE, 0xFFD3, 0x7D0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5AD7)
    WaitChrThread(0x8, 1)

    def lambda_5AF0():
        OP_9B(0x0, 0xFE, 0xFFD3, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5AF0)
    Sleep(1200)
    EndChrThread(0x101, 0x2)
    Sleep(1000)
    Sound(121, 0, 100, 0)
    Sleep(300)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x8, 1)
    Sound(890, 0, 100, 0)
    SetChrFlags(0x8, 0x80)
    Sleep(800)
    OP_6F(0x79)

    NpcTalk(
        0x101,
        "KeA",
        (
            "#05808F#30W#6PWhat's wrong with Rixia?\x02\x03",
            "#05812F#30WShe's always kind of sad\x01",
            "but she's a little\x01",
            "different now, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PI see. So you realized\x01",
            "it too, KeA.\x02\x03",
            "#00006FWell, it seems like she\x01",
            "has a lot going on.\x02\x03",
            "#00000FWell for my part, I plan\x01",
            "to keep a close eye on\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        "#05809F#30W#6PEhehe... You're so cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FDon't tease me.\x02\x03",
            "#00004FNow then... Let's get\x01",
            "back to bed, shall we?\x02\x03",
            "#00005FOh, did you go the\x01",
            "bathroom?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        (
            "#05801F#30W#6PMrrgrr... Have you no\x01",
            "shame!?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19375, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM(-1, -1)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("m3099", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_447E end

    def Function_14_5D66(): pass

    label("Function_14_5D66")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50106.itc", 0x1E)
    LoadChrToIndex("apl/ch51423.itc", 0x1F)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SoundLoad(2913)
    SoundLoad(4107)
    SoundLoad(2759)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x5)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, -104650, 550, -81450, 90)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x4)
    ClearChrFlags(0x104, 0x1)
    SetChrPos(0x104, -104650, 400, -84350, 90)
    OP_52(0x104, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x105, -104000, 300, -80000, 180)
    OP_70(0x8, 0x2)
    OP_70(0x9, 0x5)
    OP_70(0xA, 0x7)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        "#2913V#2S#30W...Lloyd..\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        "#4107V#30WWake up... Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0x100B)
    Sleep(150)
    Sound(2078, 255, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#05211FAh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_24(0x81E)
    OP_C9(0x1, 0x80000000)
    Sound(811, 0, 20, 0)
    Sound(812, 0, 100, 0)
    OP_68(-104400, 1100, -81450, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(20500, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#05205F#30W#5PHuh...?\x02\x03",
            "#05208F...What time is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PAbout 2AM.\x02\x03",
            "#10300FIt looked like you were\x01",
            "having a nightmare. You\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#05206F#5PYeah. I think I was\x01",
            "having some kind of\x01",
            "weird dream.\x02\x03",
            "#05205FHuh...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    Sound(898, 0, 80, 0)
    OP_74(0x9, 0x8)
    OP_71(0x9, 0x5, 0x8, 0x0, 0x8)
    OP_79(0x9)
    Sleep(300)

    ChrTalk(
        0x101,
        "#05211F#5P...Huh?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(100)
    SetChrSubChip(0x101, 0x5)
    Sleep(130)
    SetChrSubChip(0x101, 0x7)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x104,
        "#14105F#2759V#6P#40W#13A#NWhat? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    SetChrSubChip(0x101, 0x5)
    Fade(500)
    OP_68(-104400, 1100, -82150, 1500)
    Sound(812, 0, 100, 0)
    OP_71(0x8, 0x2, 0x5, 0x0, 0x8)
    Sound(898, 0, 50, 0)
    SetChrSubChip(0x104, 0x1)
    SetChrPos(0x104, -104650, 550, -84550, 90)
    OP_79(0x8)
    SetChrSubChip(0x101, 0x6)
    OP_6F(0x79)
    OP_0D()
    Sleep(200)
    SetChrSubChip(0x104, 0x2)

    ChrTalk(
        0x101,
        "#05208F#11PRandy... Did I wake you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#14106F#6PAh, don't worry about\x01",
            "it.\x02\x03",
            "#14101FMore importantly...\x01",
            "Where's Keddo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PYou came back a little\x01",
            "while ago and went to\x01",
            "bed together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#05206F#5PBoth of you noticed,\x01",
            "huh.\x02\x03",
            "#05201F...But you're right, we\x01",
            "did. But...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0x105, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#10308F#5PHmm? It doesn't look\x01",
            "like she's here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#14100F#6PWell, let's look around\x01",
            "for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#05206F#5PYeah. Sorry, but thanks.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(20875, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others searched 3F, but\x01",
            "KeA was nowhere to be found.\x02\x03",
            "Before long, they asked Tio to sense\x01",
            "her presence and for the cooperation\x01",
            "of the female Support Section members.\x02\x03",
            "Additionally, they asked the hotel\x01",
            "staff and also searched 2F.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ReplaceBGM("ed7513", "ed7564")
    SetScenarioFlags(0x22, 0)
    NewScene("t105B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_5D66 end

    def Function_15_63BA(): pass

    label("Function_15_63BA")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(I don't think I could\x01",
            "sleep even if I went\x01",
            "back to bed.)\x02\x03",
            "(I'll go to the lounge\x01",
            "and cool off for a bit.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -100030, 0, 6530, 0)
    EventEnd(0x4)
    Return()

    # Function_15_63BA end

    def Function_16_6448(): pass

    label("Function_16_6448")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00006F(No matter what anyone\x01",
            "says, visiting this late at\x01",
            "night would be indiscreet.)\x02\x03",
            "(I'll calm down in the\x01",
            "lounge.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -107740, 0, 9540, 90)
    EventEnd(0x4)
    Return()

    # Function_16_6448 end

    def Function_17_64DB(): pass

    label("Function_17_64DB")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00006F(No matter what anyone\x01",
            "says, visiting this late at\x01",
            "night would be indiscreet.)\x02\x03",
            "(I'll calm down in the\x01",
            "lounge.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -99710, 0, 11750, 180)
    EventEnd(0x4)
    Return()

    # Function_17_64DB end

    SaveToFile()

Try(main)
