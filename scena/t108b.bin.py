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
        "Function_5_8CE",          # 05, 5
        "Function_6_8D2",          # 06, 6
        "Function_7_969",          # 07, 7
        "Function_8_324D",         # 08, 8
        "Function_9_32AF",         # 09, 9
        "Function_10_32FC",        # 0A, 10
        "Function_11_3BC4",        # 0B, 11
        "Function_12_413B",        # 0C, 12
        "Function_13_4551",        # 0D, 13
        "Function_14_5F1B",        # 0E, 14
        "Function_15_6591",        # 0F, 15
        "Function_16_6627",        # 10, 16
        "Function_17_66B1",        # 11, 17
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_6C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A0")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, mister customer...\x01",
            "Are you already going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYeah, I'm summoned at the guest house.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I see.\x01",
            "Goodbye then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(N-No waaay...\x01",
            "I almost haven't taken\x01",
            "care of him at all yeeet!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHu hu, what a strange girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F...You are doing it on purpose, aren't you?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6BF")

    label("loc_6A0")


    ChrTalk(
        0xFE,
        (
            "*haah*...\x01",
            "Goodbye then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BF")

    Jump("loc_8AE")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86B")

    ChrTalk(
        0xFE,
        "Oh, Mr. Wazy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I believe that Wazy has\x01",
            "already gone to the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "N-No waaay...\x01",
            "I almost haven't taken\x01",
            "care of him at all yeeet!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_7AB")

    ChrTalk(
        0x102,
        "#00106F(No wonder, Wazy is popular...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_863")

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_7E9")

    ChrTalk(
        0x103,
        "#00203F(No wonder, Mr. Wazy is popular...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_863")

    label("loc_7E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_825")

    ChrTalk(
        0x104,
        "#00301F(That bastard is popular, huh...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_863")

    label("loc_825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_863")

    ChrTalk(
        0x109,
        "#10106F(As expected from Wazy, he's popular...)\x02",
    )

    CloseMessageWindow()

    label("loc_863")

    SetScenarioFlags(0x0, 1)
    Jump("loc_8AE")

    label("loc_86B")


    ChrTalk(
        0xFE,
        (
            "*haah*...I wish I had taken care of\x01",
            "Mr. Wazy a little more...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AE")

    Jump("loc_8CA")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8C1")
    Jump("loc_8CA")

    label("loc_8C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8CA")

    label("loc_8CA")

    TalkEnd(0xFE)
    Return()

    # Function_4_548 end

    def Function_5_8CE(): pass

    label("Function_5_8CE")

    Call(0, 6)
    Return()

    # Function_5_8CE end

    def Function_6_8D2(): pass

    label("Function_6_8D2")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_94E")

    ChrTalk(
        0xA,
        (
            "The bar counter\x01",
            "will close soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please understand\x01",
            "that you can't order\x01",
            "during late night hours.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_965")

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_95C")
    Jump("loc_965")

    label("loc_95C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_965")

    label("loc_965")

    TalkEnd(0xA)
    Return()

    # Function_6_8D2 end

    def Function_7_969(): pass

    label("Function_7_969")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_98C")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_98C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A3")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9BA")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7D), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9D1")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7C), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9E8")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E8")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A25")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A42")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A5F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A7C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A93")
    SetScenarioFlags(0x147, 2)
    Jump("loc_AEA")

    label("loc_A93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAA")
    SetScenarioFlags(0x147, 3)
    Jump("loc_AEA")

    label("loc_AAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC1")
    SetScenarioFlags(0x147, 4)
    Jump("loc_AEA")

    label("loc_AC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD8")
    SetScenarioFlags(0x147, 5)
    Jump("loc_AEA")

    label("loc_AD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEA")
    SetScenarioFlags(0x147, 6)

    label("loc_AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEC")

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
        (0, "loc_B83"),
        (1, "loc_B97"),
        (2, "loc_BAB"),
        (3, "loc_BBF"),
        (4, "loc_BD3"),
        (5, "loc_BE7"),
        (SWITCH_DEFAULT, "loc_BE7"),
    )


    label("loc_B83")

    SetScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BEC")

    label("loc_B97")

    ClearScenarioFlags(0x147, 2)
    SetScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BEC")

    label("loc_BAB")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    SetScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BEC")

    label("loc_BBF")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    SetScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BEC")

    label("loc_BD3")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    SetScenarioFlags(0x147, 6)
    Jump("loc_BEC")

    label("loc_BE7")

    Jump("loc_BEC")

    label("loc_BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_BFE")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_C41")

    label("loc_BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_C10")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_C41")

    label("loc_C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_C22")
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_C41")

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_C34")
    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_C41")

    label("loc_C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_C41")
    AddParty(0x4, 0xEF, 0xFF)

    label("loc_C41")

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
            "#00008F#30WYes...yes.\x02\x03",
            "#00000F...I see.\x01",
            "I think it'll be fine.\x02\x03",
            "#00006F#20WI'm sorry, only us\x01",
            "came to have fun...\x02\x03",
            "#00002F...Ha ha, I understand.\x01",
            "We'll recharge as much as possible.\x02",
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
            "#00006F#11P*sigh*...\x01",
            "Nothing wrong at the Support Section...\x02\x03",
            "#00008FI really think I was worried\x01",
            "too much, however...\x02",
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
            "#4111V#40WUhuhu...\x01",
            "Pleased to meet you, ladies and \x01",
            "gentlemen of the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4112V#40WIt would make me glad if you'd got \x01",
            "some fun from the parting gift I left\x01",
            "as a symbol of our acquaintanceship㈱\x07\x00\x02",
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
            "#00003F#11P(It was probably him who passed\x01",
            "the tower data to the terrorists.)\x02\x03",
            "(However...it didn't seem\x01",
            "he was their comrade.)\x02\x03",
            "#00008F(And like "Yin" said, he isn't even a member\x01",
            "of the Heiyue or the Red Constellation...)\x02\x03",
            "#00001F(...Who in the world is he...?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1798")
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
            "#3397V#2S#5P#30W#18A...Lloyd?\x01",
            "Are you still there?\x07\x00\x02",
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
            "#00005F#6POh, is that you, Elie?\x02\x03",
            "#00002FIt's ok, come in.\x02",
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
        "My, did you call someone?\x02",
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
            "#00004F#6PYeah, the Chief.\x02\x03",
            "#00008F...I was thinking if anything happened\x01",
            "at the SSS building while we're away\x01",
            "and tried to contact him, but...\x02\x03",
            "#00000FIt seems I was overanxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PSo...\x02\x03",
            "#00108F...Considering what happened at\x01",
            "the time of the Trade Conference,\x01",
            "I really understand your worries, but...\x02\x03",
            "#00102FAt least today, you should rest\x01",
            "without thinking about anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha...you're right.\x02\x03",
            "#00002FSorry. Could you have\x01",
            "come to pick me up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11POh, yes...\x01",
            "I didn't see you around.\x02\x03",
            "#00108FI thought that we could've gone\x01",
            "to the guest house if you wanted...\x02\x03",
            "#00113F...You know, if it's not a bother.\x02",
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
            "#00011F#6PI-It's not a bother at all!\x02\x03",
            "#00006FHonestly...\x01",
            "Elie, are you teasing me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PT-That's not my\x01",
            "intention...\x02\x03",
            "#00109FT-Then, let's go to the\x01",
            "guest house together.\x02\x03",
            "We can make a little detour too,\x01",
            "since there's time until the dinner party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PY-You're right.\x01",
            "We could look at the stores downstairs.\x02\x03",
            "#00012F(Wait, why am I so flustered\x01",
            "for being the two of us alone...?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3209")

    label("loc_1798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1DAD")
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
            "#2678V#2S#5P#30W#18A...Mr. Lloyd.\x01",
            "Can I have a moment?\x07\x00\x02",
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
            "#00005F#6POh, is that you, Tio?\x02\x03",
            "#00002FIt's ok, come in.\x02",
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
        (
            "...Were you talking to\x01",
            "the Chief, perhaps?\x02",
        )
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
            "#00004F#6PHa ha, well done noticing it.\x02\x03",
            "#00008F...I was thinking if anything happened\x01",
            "at the SSS building while we're away\x01",
            "and tried to contact him, but...\x02\x03",
            "#00000FIt seems I was overanxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PI see...\x02\x03",
            "#00208F...It is true that some concerning things\x01",
            "remain about that hacker, but...\x02\x03",
            "#00202FIt is a long-awaited vacation,\x01",
            "so shouldn't you relax?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHa ha...you're right.\x02\x03",
            "#00002FSorry. Could you have\x01",
            "come to pick me up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PYes, everyone is going to the\x01",
            "guest house little by little.\x02\x03",
            "#00200FWell, since it appears that there is \x01",
            "still time until the dinner party, \x01",
            "there is no need to hurry, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PNo, I'm going too.\x02\x03",
            "Tio, would you like to go\x01",
            "to the guest house together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#11P......Yes.\x02\x03",
            "#00208FUhhm, can we have a look\x01",
            "a the stores downstair?\x02\x03",
            "#00206FUhhm, I was having some\x01",
            "difficulty going in alone...\x02",
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
        "#00201F#11PI-Is there something odd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PN-No no!\x02\x03",
            "#00002FAll right, let's do\x01",
            "a little side trip.\x02",
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
            "#00004F#6P(Uhmm, Tio showing interest into\x01",
            "normal stores is so refreshing...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3209")

    label("loc_1DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_23D4")
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
            "#2758V#5P#30W#19AWhoa, as I thought,\x01",
            "you were still here.\x02",
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
        "#00002F#6POh, Randy?\x02",
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
            "Hey, did you call\x01",
            "anywhere?\x02",
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
            "#00006F#6PYeah, the Chief.\x02\x03",
            "#00008F...I was thinking if anything happened\x01",
            "at the SSS building while we're away\x01",
            "and tried to contact him, but...\x02\x03",
            "#00000FIt seems I was overanxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#11PI see...\x02\x03",
            "#00303FWell, uncle and the others\x01",
            "are in Crossbell as usual...\x02\x03",
            "#00300FHonestly, I'm worried too,\x01",
            "but shouldn't it be ok to\x01",
            "have fun at least today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha...you're right.\x02\x03",
            "#00002FSorry. Could you have\x01",
            "come to pick me up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PYeah, everyone has been going to\x01",
            "the guest house little by little.\x02\x03",
            "#00300FAlthough until the dinner party\x01",
            "there's still time, so you don't\x01",
            "have to hurry up too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo, I'm going too.\x02\x03",
            "#00002FBy the way, Randy, you were\x01",
            "looking at the jewelry during the day.\x02\x03",
            "How was their assortment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#11PWell, as you might expect from bein'\x01",
            "pricey, they had some nice stuff...\x02\x03",
            "#00302FHey, could it be that you want to do a\x01",
            "present for some girl you're interest into?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PN-No...\x01",
            "I-I was just curious about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PDon't be shy, don't be.\x02\x03",
            "#00302FAlright, in case we stop there,\x01",
            "big bro here will give you advice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PIt's not like that...!\x02\x03",
            "#00000FWell, whatever, let's go out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3209")

    label("loc_23D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_2B0B")
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
            "#3518V#2S#5P#30W#19A...Mr. Lloyd.\x01",
            "Are you there?\x07\x00\x02",
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
            "#00005F#6POh, is that you, Noｱl?\x02\x03",
            "#00002FIt's ok, come in.\x02",
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
            "Oh, were you calling\x01",
            "anyone?\x02",
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
            "#00004F#6PYeah, the Chief.\x02\x03",
            "#00008F...I was thinking if anything happened\x01",
            "at the SSS building while we're away\x01",
            "and tried to contact him, but...\x02\x03",
            "#00000FIt seems I was overanxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#11P...Is that so?\x02\x03",
            "#10106FAfter such a thing happened,\x01",
            "it really makes you worry...\x02\x03",
            "#10108F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6POh come'on, it's not something even you\x01",
            "should be serious about, right, Noｱl?\x02\x03",
            "#00006FUhm...I'm sorry. I said something\x01",
            "that has hyped things down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#11PN-No, likewise.\x02\x03",
            "#10106FIt seems that I have a natural\x01",
            "disposition prone to worrying...\x02\x03",
            "#10100FSometimes I envy\x01",
            "Fran's carefreeness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHa ha, I see.\x02\x03",
            "#00002FMaybe we'are pretty\x01",
            "similar in that regard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#11PI-It's not like that! Our intellects and \x01",
            "such are completely different!\x02\x03",
            "#10112FI, uhhmm...\x01",
            "Have a simple CGF disposition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P(Uhmm, as usual, she's very\x01",
            "strict in self-evaluating herself.)\x02\x03",
            "#00000FWell, that aside, you came\x01",
            "to pick me up, right?\x02\x03",
            "If you want, we could go\x01",
            "to the guest house together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#11PAh, yes!\x02\x03",
            "#10100FBy the way, it seems that the dinner party\x01",
            "is going to take place in an amazing mansion...?\x02\x03",
            "The one where that former\x01",
            "Chairman Hartmann was living in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah, honestly, it's an unbelievably\x01",
            "luxurious and gorgeous mansion.\x02\x03",
            "#00002FThe first time you go in, I assure you\x01",
            "that you're going to stare in wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PAhaha...\x01",
            "Now I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3209")

    label("loc_2B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_3209")
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
            "#2912V#5P#30W#20AAh, as I thought,\x01",
            "you were still here.\x02",
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
        "#00002F#6POh, Wazy?\x02",
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
            "Hu hu, I see.\x02\x03",
            "You called the Chief being\x01",
            "worried about the SSS\x01",
            "building while away, right?\x02",
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
        "#00011F#6PH-How did you get it!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PAfter having been over a month together,\x01",
            "I can at least figure that out.\x02\x03",
            "#10302FHu hu, you're acting like a leader\x01",
            "more than I had expected, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHa ha...I'm prone to worrying.\x02\x03",
            "#00008FIf I really were an excellent leader,\x01",
            "I'd probably be immovable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#11PWell, the excellence of being a leader\x01",
            "depends from person to person.\x02\x03",
            "#10304FYour intelligence is not bad, your intuition is\x01",
            "sharp too...basically, you're "average".\x02\x03",
            "#10302FIt's not bad steadily doing one's best\x01",
            "in the field where you can, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PGh...don't say it so bluntly.\x02\x03",
            "#00013FAlthough that spontaneous\x01",
            "side of you is not bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PHu hu, I too like \x01",
            "your frankness.\x02\x03",
            "#10302FTo begin with, shrewd people like\x01",
            "that Cao or that joker of an Imperial\x01",
            "agent are shrewd to the very end.\x02\x03",
            "More than opposing them in the same way,\x01",
            "isn't it better making the most\x01",
            "of your strong points?\x02",
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
        "#10305F#11POh, did I say something odd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo, it's that I didn't think\x01",
            "about that in that way...\x02\x03",
            "#00000FThank you, Wazy.\x01",
            "I think my eyes have opened a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PHu hu, I'm glad to hear that.\x02\x03",
            "#10300F...So, shouldn't it be time\x01",
            "to go to the dinner party?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PYeah, let's go then.\x02",
    )

    CloseMessageWindow()

    label("loc_3209")

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

    # Function_7_969 end

    def Function_8_324D(): pass

    label("Function_8_324D")

    OP_68(-100000, 1000, -79000, 2500)
    Sound(121, 0, 100, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)

    def lambda_3278():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3278)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(890, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_6F(0x79)
    Return()

    # Function_8_324D end

    def Function_9_32AF(): pass

    label("Function_9_32AF")

    OP_68(-100000, 1000, -79000, 2000)

    def lambda_32C5():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32C5)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(890, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_6F(0x79)
    Return()

    # Function_9_32AF end

    def Function_10_32FC(): pass

    label("Function_10_32FC")

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
            "#00005F#5PBy the way, has KeA\x01",
            "left with anyone?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_352E")

    ChrTalk(
        0x102,
        (
            "#00104F#12PYes, she was with Tio...\x01\x02\x03",
            "#00100FMaybe they're already at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PI see, than I can feel at ease.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PEhm...has anything happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, a lot has being going on\x01",
            "and she looked nervous.\x02\x03",
            "#00002FWell, it seems she has\x01",
            "enjoyed the theme park, so\x01",
            "I think we don't have to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#12P*giggle*, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA5")

    label("loc_352E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_36C2")

    ChrTalk(
        0x103,
        (
            "#00205F#12PYes, she left with Miss Elie...\x01\x02\x03",
            "#00202FMaybe they're already at the guest house...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PI see, than I can feel at ease.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P...Has anything happened to KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, a lot has being going on\x01",
            "and she looked nervous.\x02\x03",
            "#00002FWell, it seems she has\x01",
            "enjoyed the theme park, so\x01",
            "I think we don't have to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12P...You're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA5")

    label("loc_36C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_385F")

    ChrTalk(
        0x104,
        (
            "#00305F#12PYeah, she should be with\x01",
            "milady and peTiote...\x02\x03",
            "#00300FCould they be already at the guest house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PI see, than I can feel at ease.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12P...? Anything's happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, a lot has being going on\x01",
            "and she looked nervous.\x02\x03",
            "#00002FWell, it seems she has\x01",
            "enjoyed the theme park, so\x01",
            "I think we don't have to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#12PHa ha, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA5")

    label("loc_385F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_3A04")

    ChrTalk(
        0x109,
        (
            "#10105F#12POh, she should be with\x01",
            "senior Randy and Wazy...\x02\x03",
            "#10100FI think they're already at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PI see, than I can feel at ease.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PEhhm...\x01",
            "Has anything happened to KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, a lot has being going on\x01",
            "and she looked nervous.\x02\x03",
            "#00002FWell, it seems she has\x01",
            "enjoyed the theme park, so\x01",
            "I think we don't have to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F#12PUh uh, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA5")

    label("loc_3A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_3BA5")

    ChrTalk(
        0x105,
        (
            "#10305F#12PYeah, it seems she\x01",
            "left with the girls.\x02\x03",
            "#10300FWon't she be already at the guest house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PI see, than I can feel at ease.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#12P...Has anything happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, a lot has being going on\x01",
            "and she looked nervous.\x02\x03",
            "#00002FWell, it seems she has\x01",
            "enjoyed the theme park, so\x01",
            "I think we don't have to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#12PHu hu...\x01",
            "Indeed, she was in a gambol.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA5")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 5700, 0, 13400, 315)
    SetScenarioFlags(0x145, 6)
    OP_1B(0x1, 0xFF, 0xFFFF)
    EventEnd(0x5)
    Return()

    # Function_10_32FC end

    def Function_11_3BC4(): pass

    label("Function_11_3BC4")

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
            "#05203F#5P#30W(............)\x02\x03",
            "#05208F("Barriers"...)\x02\x03",
            "(The "barriers" that stand in our way...)\x02\x03",
            "#05201F(Mayor Dieter is trying\x01",
            "to break through one\x01",
            "in his own way...)\x02\x03",
            "#05206F(...However, we...)\x02",
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

    def lambda_3E41():
        OP_96(0xFE, 0xFFFE6736, 0x226, 0xFFFEC1D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E41)
    OP_A0(0x101, 1200, 0x0, 0x5)
    ClearChrFlags(0x101, 0x20)
    Sound(812, 0, 100, 0)
    OP_79(0x9)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#05208F#5P(...At the time of the mafia,\x01",
            "the "barrier" vanished on its own...)\x02\x03",
            "(Then, the "barriers" that\x01",
            "now are standing in our way...)\x02\x03",
            "#05203F(We──we aren't being\x01",
            "a lot useful again...)\x02\x03",
            "#05213F(...Is that really alright...?)\x02",
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
            "#05206F#5P(...It's no use.\x01",
            "I'm tired and yet I can't sleep.)\x02\x03",
            "#05200F(I guess I'll go to the lounge\x01",
            "and drink some water...)\x02",
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

    def lambda_401F():
        OP_98(0xFE, 0x0, 0x0, 0x12C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_401F)
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

    def lambda_4095():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4095)
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

    # Function_11_3BC4 end

    def Function_12_413B(): pass

    label("Function_12_413B")

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
        "#11P...Hi, Rixia.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(11200, 1000, 14250, 4000)
    MoveCamera(315, 23, 0, 4000)

    def lambda_42CC():
        OP_95(0xFE, 11720, 0, 12790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42CC)
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
        "#30W#3246VMr....Lloyd?\x02",
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
            "#00012FSorry, did I scare you\x01",
            "by suddenly calling you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#30W#11PAhaha, that's not it...\x02\x03",
            "#01802F#30WI was just\x01",
            "spacing out...\x02\x03",
            "#01808F#30W............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PEhm...\x02\x03",
            "#00002FCan I...sit there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01803F#30W#11P............(*nod*)\x02",
    )

    CloseMessageWindow()
    OP_68(12100, 1000, 15400, 2000)

    def lambda_44C1():
        OP_95(0xFE, 13000, 0, 15400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44C1)
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

    # Function_12_413B end

    def Function_13_4551(): pass

    label("Function_13_4551")

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
            "#01804F#5PYou're a mystery, Mr. Lloyd.\x02\x03",
            "#01810FWhen I wished for someone to\x01",
            "be near me, you really were there...\x02\x03",
            "And just for being there, I can\x01",
            "somehow feel at ease...\x02\x03",
            "#01809FUh uh, I envy everyone\x01",
            "at the Support Section.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#12PHa ha, you make too much of me.\x02\x03",
            "#00006FThere're still many things I'm\x01",
            "missing as a full-fledged detective,\x01",
            "and as everyone's leader too.\x02\x03",
            "#00008FI have to...\x01",
            "I have to grow up more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01810F#5P#30W*chuckle*...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        (
            "#00003F#12P──Say, Rixia.\x02\x03",
            "#00008FIt could be rude, but...\x01",
            "Can I ask you something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01805F#5P...?\x02\x03",
            "#01810FRude...?\x01",
            "What is it, I wonder?\x02",
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
            "#00006F#12PWhy do you...\x02\x03",
            "#00001FWhy do you laugh with\x01",
            "such empty eyes...?\x02",
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
            "#00008F#12P...I think it's been like that\x01",
            "since the time we met.\x02\x03",
            "#00003FSought after by Miss Ilya,\x01",
            "having roles in top plays...\x02\x03",
            "Now Rixia Mao is a\x01",
            "celebrity in Crossbell.\x02\x03",
            "#00001FAnd yet, why...\x02\x03",
            "Why does your smile\x01",
            "always look like you've\x01",
            "given up something...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01808F#5PH-How do you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P...Someone I know well had a\x01",
            "similar smile for a period of time.\x02",
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
            "#00008F#12PNow she doesn't show such\x01",
            "an empty smile anymore...\x02\x03",
            "#00001FHowever, when I noticed that,\x01",
            "I think you've always had such a smile.\x02",
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
            "#00003F#12PThat person's smile was something\x01",
            "like to try to bear the sorrow of not\x01",
            "seeing the person you love anymore.\x02\x03",
            "#00001FThen, what about you...?\x02\x03",
            "Why do you smile in that way to\x01",
            "Miss Ilya who loves you a lot?\x02\x03",
            "She's always near you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01808F#5P............\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01803F#5P...Honestly, I'm shocked.\x02\x03",
            "#01810FI knew you were sharp, but I can't believe \x01",
            "you saw that much through me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P...Then...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01804F#5PUh uh...you're correct.\x02\x03",
            "#01810FMaybe I will...leave Crossbell\x01",
            "in the near future.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#12P...As I thought, then.\x02\x03",
            "#00008FYou can't...\x01",
            "Tell me the reason, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5P............No.\x02\x03",
            "#01808F...However...\x01",
            "I can't tell you the details, but...\x02\x03",
            "#01810FThere's always been...\x01",
            "A path I should've walked on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PA path...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5PUh uh, it's like a family business.\x02\x03",
            "#01808F...Since I was a child...\x01",
            "I've been living for that.\x02\x03",
            "A path my ancestors inherited\x01",
            "since way, way in the past...\x02\x03",
            "#01803FA path I currently don't know\x01",
            "for what reason to walk on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PI see...\x02\x03",
            "#00001F...But then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01810F#5P"Then there's no need to"...\x01",
            "It's a path that can't be denied like that.\x02\x03",
            "#01804FIt seems that at least my dad\x01",
            "discovered the meaning for \x01",
            "inheriting that path.\x02\x03",
            "A dark, secret path with which\x01",
            "to influence society itself, with\x01",
            "enough motives to shift history...\x02\x03",
            "#01808FAnd so I inherited that\x01",
            "path from my dad and I\x01",
            "walked it until now...\x02\x03",
            "#01810F...And yes, from now on too...\x02",
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
            "#01804F#5PUh uh...how strange I am.\x02\x03",
            "I have refused the wine Miss\x01",
            "Ilya recommended, but...\x02\x03",
            "#01810F...Or could it be that I ended up\x01",
            "being drunk by the moonlight...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PHa ha...maybe it's that.\x02\x03",
            "#00006F...Sorry.\x01",
            "I guess it was impertinent from me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5PNo, it's all right.\x02\x03",
            "#01810FAnd somehow I...\x01",
            "Said one thing after the other.\x02\x03",
            "#01809FThank you very much,\x01",
            "for listening to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PI see...\x01",
            "I'm glad to have been of help.\x02\x03",
            "#00001FHowever, Rixia.\x01",
            "If you'll ever──\x02",
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
        "#3614V#50W#13A...Lloyd...?\x02",
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
            "#05805F#30W#6P...Ah...\x01",
            "There's Rixia too...\x02\x03",
            "#05800F#30W...Were you two talking about something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#5PN-No.\x01",
            "We had already finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PYeah, it's fine.\x02\x03",
            "#00001F...Can't you sleep,\x01",
            "perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#05808F#30W#6P.........Yes...\x02\x03",
            "#05806F#30W...Somehow I think I\x01",
            "had a scary dream...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PReally...?\x02\x03",
            "#00000FDo you want to sleep in my bed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#05812F#30W#6P...Can I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#11PYeah, it's an exception though.\x02",
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

    def lambda_5803():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5803)
    OP_93(0xD, 0x2D, 0x1F4)
    Sleep(500)

    def lambda_5822():
        OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5822)
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
        "#05809F#30W#5P...Eheheh...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#6PI'm sorry Rixia.\x01",
            "We've been interrupted in a strange way.\x02",
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
            "#01809F#5PUh uh, not at all.\x02\x03",
            "#01802FThanks to you, Mr. Lloyd,\x01",
            "it seems I'll be able to sleep too.\x02\x03",
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
            "#01808F#5P...About what we talked before.\x01",
            "Please keep it a secret\x01",
            "from Miss Ilya.\x02\x03",
            "#01810FBecause I intend to talk to\x01",
            "her myself at the right time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P...Understood.\x02\x03",
            "#00000FMaybe I'm not reliable, but please\x01",
            "call me if something happens.\x02\x03",
            "I'll do whatever I can.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#5PUh uh...\x01",
            "Thank you.\x02\x03",
            "#01802FThen if I have some problems,\x01",
            "I will ask you for advice.\x02",
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
        (
            "#3247V#40W──Good night,\x01",
            "Mr. Lloyd, KeA.\x02",
        )
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
        "#00002F#6PGood night, Rixia.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x101,
        "KeA",
        "#05809F#3615V#50W#12PGood niiight...\x02",
    )

    CloseMessageWindow()
    OP_24(0xE1F)
    OP_C9(0x1, 0x80000000)
    OP_68(12900, 1000, 13970, 5000)

    def lambda_5C57():

        label("loc_5C57")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5C57")

    QueueWorkItem2(0x101, 2, lambda_5C57)
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_5C70():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C70)
    WaitChrThread(0x8, 1)

    def lambda_5C89():
        OP_9B(0x0, 0xFE, 0xFFD3, 0x7D0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C89)
    WaitChrThread(0x8, 1)

    def lambda_5CA2():
        OP_9B(0x0, 0xFE, 0xFFD3, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5CA2)
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
            "#05808F#30W#6P...Is something wrong with Rixia?\x02\x03",
            "#05812F#30WSomehow she's always sad,\x01",
            "has something happened...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PI see, you've noticed too.\x02\x03",
            "#00006F...Well, it seems many things are going on.\x02\x03",
            "#00000FI intend to do whatever\x01",
            "I can for her too.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        (
            "#05809F#30W#6PEheheh...\x01",
            "Aren't you cool, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FDon't tease me.\x02\x03",
            "#00004FWell then...\x01",
            "Let's go back to bed now and sleep.\x02\x03",
            "#00005FAh, have you gone to the toilet?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        (
            "#05801F#30W#6PMrrgrr...\x01",
            "Lloyd, you lack too much tact!\x02",
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

    # Function_13_4551 end

    def Function_14_5F1B(): pass

    label("Function_14_5F1B")

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
        "#2913V#2S#30W...Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        "#4107V#30WWake up...Lloyd...\x02",
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
        "#05211FHuh...!\x02",
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
            "#05205F#30W#5PWhat...\x02\x03",
            "#05208F...What time is it now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PAbout 2 AM I guess.\x02\x03",
            "#10300FYou were having quite the\x01",
            "nightmare, what's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#05206F#5PAh, it seems I was\x01",
            "having a weird dream...\x02\x03",
            "#05205F...Oh...\x02",
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
        "#05211F#5P......Huh......?\x02",
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
        "#14105F#2759V#6P#40W#13A#NHey, what's wrong...?\x02",
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
        (
            "#05208F#11PRandy...\x01",
            "Did I wake you up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#14106F#6PWell, don't worry 'bout it.\x02\x03",
            "#14101FMore importantly...\x01",
            "Where's Keddo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PIt seems that you two came back some\x01",
            "time ago and were sleeping together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#05206F#5PDid you two notice?\x02\x03",
            "#05201F...You're right.\x01",
            "She should've been sleeping with me...\x02",
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
            "#10308F#5PHmmm...?\x01",
            "It looks like she's not here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#14100F#6PWell, let's go look for her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#05206F#5PAh, thanks.\x02",
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
            "Lloyd and the others searched the 3F area\x01",
            "but they could not find KeA anywhere.\x02\x03",
            "Before long, Tio, who sensed their presence,\x01",
            "appeared, and the girls helped too...\x02\x03",
            "Furthermore, they called the hotel staff\x01",
            "and they had the 2F searched too.\x07\x00\x02",
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

    # Function_14_5F1B end

    def Function_15_6591(): pass

    label("Function_15_6591")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(It seems that even if I returned to\x01",
            "my room I wouldn't be able to sleep.)\x02\x03",
            "(I'll go to the lounge and cool down.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -100030, 0, 6530, 0)
    EventEnd(0x4)
    Return()

    # Function_15_6591 end

    def Function_16_6627(): pass

    label("Function_16_6627")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00006F(No matter the case, visiting at this\x01",
            "late hour would be indiscreet.)\x02\x03",
            "(I'll calm down at the lounge.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -107740, 0, 9540, 90)
    EventEnd(0x4)
    Return()

    # Function_16_6627 end

    def Function_17_66B1(): pass

    label("Function_17_66B1")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00006F(No matter the case, visiting at this\x01",
            "late hour would be indiscreet.)\x02\x03",
            "(I'll calm down at the lounge.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -99710, 0, 11750, 180)
    EventEnd(0x4)
    Return()

    # Function_17_66B1 end

    SaveToFile()

Try(main)
