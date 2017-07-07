from ScenarioHelper import *

def main():
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
        "Lisha",               # 1
        "Roche",               # 2
        "Zolk",                 # 3
        "Randy",               # 4
        "Waji",                   # 5
        "Keya",                 # 6
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
        "Function_5_8B3",          # 05, 5
        "Function_6_8B7",          # 06, 6
        "Function_7_95E",          # 07, 7
        "Function_8_2F0C",         # 08, 8
        "Function_9_2F6E",         # 09, 9
        "Function_10_2FBB",        # 0A, 10
        "Function_11_380B",        # 0B, 11
        "Function_12_3D99",        # 0C, 12
        "Function_13_41EB",        # 0D, 13
        "Function_14_5B27",        # 0E, 14
        "Function_15_6158",        # 0F, 15
        "Function_16_61CB",        # 10, 16
        "Function_17_624A",        # 11, 17
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_898")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_6C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_697")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "Well, guest ……\x01",
            "Are you going already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FOh, please call me at the guesthouse for a moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is that so?\x01",
            "Please do it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Oh, that kind of … ….\x01",
            "Still little care\x01",
            "Even though it can not be done ~! )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHe is a funny child.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F… … You, you know what?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6BE")

    label("loc_697")


    ChrTalk(
        0xFE,
        (
            "Ha\x01",
            "Please do it … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE")

    Jump("loc_893")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85A")

    ChrTalk(
        0xFE,
        "あれっ、Waji様は……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fああ、Wajiならもう\x01",
            "I guess I should have gone to the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right.\x01",
            "Still little care\x01",
            "Even though it can not be done ~!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_7A0")

    ChrTalk(
        0x102,
        "#00106F（さすがWaji君、大人気ね……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_852")

    label("loc_7A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_7DF")

    ChrTalk(
        0x103,
        "#00203F（さすがWajiさん、大人気ですね……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_852")

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_81A")

    ChrTalk(
        0x104,
        "#00301F(Honey-huro, it's popular … …)\x02",
    )

    CloseMessageWindow()
    Jump("loc_852")

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_852")

    ChrTalk(
        0x109,
        "#10106F（さすがWaji君、大人気ですね……）\x02",
    )

    CloseMessageWindow()

    label("loc_852")

    SetScenarioFlags(0x0, 1)
    Jump("loc_893")

    label("loc_85A")


    ChrTalk(
        0xFE,
        (
            "はあ……もう少しWaji様の\x01",
            "I wanted to take care of him … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_893")

    Jump("loc_8AF")

    label("loc_898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8A6")
    Jump("loc_8AF")

    label("loc_8A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8AF")

    label("loc_8AF")

    TalkEnd(0xFE)
    Return()

    # Function_4_548 end

    def Function_5_8B3(): pass

    label("Function_5_8B3")

    Call(0, 6)
    Return()

    # Function_5_8B3 end

    def Function_6_8B7(): pass

    label("Function_6_8B7")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_943")

    ChrTalk(
        0xA,
        (
            "The opening of the bar counter\x01",
            "We will close soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In the late night time zone\x01",
            "Because you can not order,\x01",
            "Please acknowledge it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95A")

    label("loc_943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_951")
    Jump("loc_95A")

    label("loc_951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_95A")

    label("loc_95A")

    TalkEnd(0xA)
    Return()

    # Function_6_8B7 end

    def Function_7_95E(): pass

    label("Function_7_95E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_981")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_981")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_998")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_998")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9AF")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7D), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C6")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7C), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9DD")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DD")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A1A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A37")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A54")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A71")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A88")
    SetScenarioFlags(0x147, 2)
    Jump("loc_ADF")

    label("loc_A88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9F")
    SetScenarioFlags(0x147, 3)
    Jump("loc_ADF")

    label("loc_A9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB6")
    SetScenarioFlags(0x147, 4)
    Jump("loc_ADF")

    label("loc_AB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACD")
    SetScenarioFlags(0x147, 5)
    Jump("loc_ADF")

    label("loc_ACD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADF")
    SetScenarioFlags(0x147, 6)

    label("loc_ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE7")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆ I like Erie\x01",        # 0
            "◆ I like Tio\x01",        # 1
            "◆Randyが好き\x01",      # 2
            "◆ I like Noel\x01",        # 3
            "◆Wajiが好き\x01",          # 4
            "◆ Do not change\x01",          # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B7E"),
        (1, "loc_B92"),
        (2, "loc_BA6"),
        (3, "loc_BBA"),
        (4, "loc_BCE"),
        (5, "loc_BE2"),
        (SWITCH_DEFAULT, "loc_BE2"),
    )


    label("loc_B7E")

    SetScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BE7")

    label("loc_B92")

    ClearScenarioFlags(0x147, 2)
    SetScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BE7")

    label("loc_BA6")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    SetScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BE7")

    label("loc_BBA")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    SetScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_BE7")

    label("loc_BCE")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    SetScenarioFlags(0x147, 6)
    Jump("loc_BE7")

    label("loc_BE2")

    Jump("loc_BE7")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_BF9")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_C3C")

    label("loc_BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_C0B")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_C3C")

    label("loc_C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_C1D")
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_C3C")

    label("loc_C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_C2F")
    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_C3C")

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_C3C")
    AddParty(0x4, 0xEF, 0xFF)

    label("loc_C3C")

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
            "#00008F#30WYes … Yes.\x02\x03",
            "#00000F……Is that so.\x01",
            "I think that it is safe then.\x02\x03",
            "#00006F#20WSorry, only ourselves\x01",
            "Have fun and come … ….\x02\x03",
            "#00002F… I understand.\x01",
            "I will charge at most.\x02",
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
            "#00006F#11PFuu …\x01",
            "Is there anything about the support department?\x02\x03",
            "#00008FAs expected to be overly concerned\x01",
            "I think ….\x02",
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
            "#4111V#40WUhufu …\x01",
            "Nice to meet you, people from the support department.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4112V#40WTo the mark of approach\x01",
            "I will leave a souvenir\x01",
            "I am happy to give pleasures\x07\x00\x02",
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
            "#00003F#11P(Maybe he's a terrorist\x01",
            "I guessed the data of the tower. )\x02\x03",
            "(But …. terrorists\x01",
            "I do not think they are friends. )\x02\x03",
            "#00008F(And as the silver said,\x01",
            "It is not a member of black moon or a red constellation … …)\x02\x03",
            "#00001F(… who the hell are you …?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_16B6")
    SetChrPos(0x102, -100000, 0, -74900, 180)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x102,
        "Ely's voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3397V#2S#5P#30W#18A…… Lloyd?\x01",
            "Are you still in the room?\x07\x00\x02",
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
            "#00005F#6POh, Ellie?\x02\x03",
            "#00002FOkay, come in.\x02",
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
        "Oh, did you contact somewhere?\x02",
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
            "#00004F#6POh, to the section chief.\x02\x03",
            "#00008F…… In the building of the support department during my absence\x01",
            "I thought something was going on\x01",
            "I tried to contact you ….\x02\x03",
            "#00000FIt seems that it was a troublesome task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11Pso……\x02\x03",
            "#00108F…… certainly at the time of the trade meeting\x01",
            "Given what happened\x01",
            "I know I worry … but …\x02\x03",
            "#00102FWithout thinking about anything today\x01",
            "You had better enjoy your vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha … that's right.\x02\x03",
            "#00002FSorry, perhaps\x01",
            "Did you come and pick me up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11POh, yes ….\x01",
            "Because I could not see him.\x02\x03",
            "#00108FIf you do not mind, we will bring you to our guesthouse\x01",
            "I thought about going ……\x02\x03",
            "#00113F… … that, if it is not annoying.\x02",
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
            "#00011F#6PTherefore, it is not annoying!\x02\x03",
            "#00006FAbsolutely …\x01",
            "Elly, you're kidding, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PI'm going to be kidding.\x01",
            "I do not have it …\x02\x03",
            "#00109FWell then, together\x01",
            "Let's go to the guest house.\x02\x03",
            "I have time to have a dinner party\x01",
            "You can stop on a little way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PThat's right.\x01",
            "Maybe you can peek at the shop below.\x02\x03",
            "#00012F(Why are you two?\x01",
            "I'm in such a hurry … ….? )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC8")

    label("loc_16B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1C56")
    SetChrPos(0x103, -100000, 0, -74900, 180)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x103,
        "Voice of Tio",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2678V#2S#5P#30W#18A…… Lloyd.\x01",
            "Can I have a minute?\x07\x00\x02",
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
            "#00005F#6POh, Tio?\x02\x03",
            "#00002FOkay, come in.\x02",
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
        "… … Maybe to the section chief?\x02",
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
            "#00004F#6PWell, I understood well.\x02\x03",
            "#00008F…… In the building of the support department during my absence\x01",
            "I thought something was going on\x01",
            "I tried to contact you ….\x02\x03",
            "#00000FIt seems that it was a troublesome task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PI see……\x02\x03",
            "#00208F…… It certainly is that hacker\x01",
            "There are things to worry though ……\x02\x03",
            "#00202FBecause it is a pleasant holiday\x01",
            "Why should I rest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha … that's right.\x02\x03",
            "#00002FSorry, perhaps\x01",
            "Did you come and pick me up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PYes, everyone\x01",
            "I am heading towards the guest house.\x02\x03",
            "#00200FWell, still until the dinner party\x01",
            "It seems there is time\x01",
            "There is no need to hurry, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PNo, I will already be out.\x02\x03",
            "If you like Tio,\x01",
            "Would you like to go to the guesthouse together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#11P………Yes.\x02\x03",
            "#00208FWell, the shop below\x01",
            "Can I peek at you?\x02\x03",
            "#00206FThat one, you go in alone\x01",
            "There is a bit of resistance … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#11PIs something funny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PNo, no!\x02\x03",
            "#00002FI understood.\x01",
            "Are you going down a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11P……Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P(Well, Tio is in an ordinary shop\x01",
            "It is fresh to show interest ……)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC8")

    label("loc_1C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_21EF")
    SetChrPos(0x104, -100000, 0, -74900, 180)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x104,
        "Randyのvoice",
        (
            "#2758V#5P#30W#19AOops, after all\x01",
            "Are you still in the room?\x02",
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
        "#00002F#6Pああ、Randyか。\x02",
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
            "What, somewhere\x01",
            "Did you even contact me?\x02",
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
            "#00006F#6POh, to the section chief.\x02\x03",
            "#00008F…… In the building of the support department during my absence\x01",
            "I thought something was going on\x01",
            "I tried to contact you ….\x02\x03",
            "#00000FIt seems that it was a troublesome task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#11PReally……\x02\x03",
            "#00303FWell, my uncle, as usual\x01",
            "I'm sitting on the crossbell …\x02\x03",
            "#00300FTo be honest, I also care\x01",
            "Those who enjoyed it today\x01",
            "Is not it nice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha … that's right.\x02\x03",
            "#00002FSorry, perhaps\x01",
            "Did you come and pick me up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11POh, everyone.\x01",
            "I'm going to the guest house.\x02\x03",
            "#00300FTo the dinner party\x01",
            "I still have time.\x01",
            "It seems to be unnecessary to hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo, I will already be out.\x02\x03",
            "#00002FそういえばRandy、\x01",
            "I was watching a jewelry store at noon.\x02\x03",
            "How was it like product selection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#11POh, just as high as it is\x01",
            "There were good monkeies … …\x02\x03",
            "#00302FWhat is it, perhaps\x01",
            "Is it a gift for a child you care about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PNo……\x01",
            "I just cared about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PDo not be shy, do not be shy.\x02\x03",
            "#00302FWell, if you stop by\x01",
            "Your older brother advises you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PSo it is different …\x02\x03",
            "#00000FWell, OK, will you come out anyway?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC8")

    label("loc_21EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_2874")
    SetChrPos(0x109, -100000, 0, -74900, 180)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x109,
        "Noel's voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3518V#2S#5P#30W#19A…… Lloyd.\x01",
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
            "#00005F#6POh, noel?\x02\x03",
            "#00002FOkay, come in.\x02",
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
            "Oh, either\x01",
            "Did you contact him?\x02",
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
            "#00004F#6POh, to the section chief.\x02\x03",
            "#00008F…… In the building of the support department during my absence\x01",
            "I thought something was going on\x01",
            "I tried to contact you ….\x02\x03",
            "#00000FIt seems that it was a troublesome task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#11P……Is that so.\x02\x03",
            "#10106FBecause it is after such a thing happened\x01",
            "You are worried about it …\x02\x03",
            "#10108F………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6POh no, until Noel\x01",
            "You will not be serious?\x02\x03",
            "#00006FThat … I'm sorry.\x01",
            "Saying that the tension goes down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#11Pyou're welcome.\x02\x03",
            "#10106FIt is very worryful\x01",
            "She seems to be sexual … ….\x02\x03",
            "#10100FOccasionally fran's comfort\x01",
            "I am jealous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha, that's right.\x02\x03",
            "#00002FIn that sense we,\x01",
            "Perhaps they are quite similar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#11PThat's not true!\x01",
            "It is completely different as well as the head!\x02\x03",
            "#10112FMy are that … …\x01",
            "Do you call it merely the guard's guts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P(Well, as usual\x01",
            "Self-evaluation is severe. )\x02\x03",
            "#00000FWell, well, well, well\x01",
            "You came to pick me up, did not you?\x02\x03",
            "If it is ok\x01",
            "Let 's go to the guest house together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#11POh, yes!\x02\x03",
            "#10100FBy the way, when we had a dinner party\x01",
            "You seem to do it on an amazing residence?\x02\x03",
            "Former Hartmann chairman\x01",
            "I mean living …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6POh, honestly can not be\x01",
            "It's a luxurious gourmet feeling house.\x02\x03",
            "#00002FIf it was time to enter for the first time\x01",
            "I guarantee your eyes will be rounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PHaha ……\x01",
            "I am looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC8")

    label("loc_2874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_2EC8")
    SetChrPos(0x105, -100000, 0, -74900, 180)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x105,
        "Wajiのvoice",
        (
            "#2912V#5P#30W#20AOh, after all\x01",
            "Have you been in the room yet?\x02",
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
        "#00002F#6Pああ、Wajiか。\x02",
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
            "Huh, I see.\x02\x03",
            "I am concerned about the building of the support department I am out\x01",
            "Did you contact the section chief?\x02",
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
        "#00011F#6PWhat, you understand! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PIf I stay with you for over a month\x01",
            "That much can be read.\x02\x03",
            "#10302FHuh, more than I thought\x01",
            "You seem to be a leader?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha … just worrying.\x02\x03",
            "#00008FIf you are a really good leader\x01",
            "I guess they have a solid massage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#11PWell, excellence as a leader\x01",
            "I think that each person.\x02\x03",
            "#10304FMy head is not bad, but Kan is sharp though.\x01",
            "Basically you are an \"ordinary man\".\x02\x03",
            "#10302FI will try my best on the extent that I can\x01",
            "Is not it bad?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PKogu …… I say it clearly.\x02\x03",
            "#00013FYou are such a place\x01",
            "On the contrary it is okay if there is no disgust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PHuh, that kind of obedience is\x01",
            "I like it, though.\x02\x03",
            "#10302FIn the first place, that Tsao is nice,\x01",
            "It is called a joking imperial agent,\x01",
            "A keen human being is quite sharp.\x02\x03",
            "More than opposing in the same direction\x01",
            "Those who made the most of your strengths\x01",
            "I think it's okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#11PWow, you said something strange?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo, what I thought about that\x01",
            "I did not have much … ….\x02\x03",
            "#00000Fありがとう、Waji。\x01",
            "I feel that my eyes have been opened for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PHuh, that's more than anything.\x02\x03",
            "#10300F……, soon it will be a dinner party,\x01",
            "Do not you have to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6POh, then shall we go with you?\x02",
    )

    CloseMessageWindow()

    label("loc_2EC8")

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

    # Function_7_95E end

    def Function_8_2F0C(): pass

    label("Function_8_2F0C")

    OP_68(-100000, 1000, -79000, 2500)
    Sound(121, 0, 100, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)

    def lambda_2F37():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F37)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(890, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_6F(0x79)
    Return()

    # Function_8_2F0C end

    def Function_9_2F6E(): pass

    label("Function_9_2F6E")

    OP_68(-100000, 1000, -79000, 2000)

    def lambda_2F84():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F84)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(890, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_6F(0x79)
    Return()

    # Function_9_2F6E end

    def Function_10_2FBB(): pass

    label("Function_10_2FBB")

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
            "#00005F#5Pそういえば、Keyaは\x01",
            "Did someone take you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_31E9")

    ChrTalk(
        0x102,
        (
            "#00104F#12PYeah, Tio\x01",
            "He took me there … …\x02\x03",
            "#00100FI should have gone to the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PWell, then, I'm relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PEr … … What happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PNo, there are various things and it is in nervous\x01",
            "Because it seems it was getting.\x02\x03",
            "#00002FWell, the theme park is also\x01",
            "It seems I enjoyed it.\x01",
            "I do not need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#12PHuh, you are right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_31E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_335C")

    ChrTalk(
        0x103,
        (
            "#00205F#12PYes, Ellie\x01",
            "I took you there … …\x02\x03",
            "#00202FI went to the guest house anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PWell, then, I'm relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P……Keyaに何か？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PNo, there are various things and it is in nervous\x01",
            "Because it seems it was getting.\x02\x03",
            "#00002FWell, the theme park is also\x01",
            "It seems I enjoyed it.\x01",
            "I do not need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12P……I agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_335C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_34D1")

    ChrTalk(
        0x104,
        (
            "#00305F#12POh, your daughter and Tio\x01",
            "I was taking him ……\x02\x03",
            "#00300FYou have already gone to the guesthouse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PWell, then, I'm relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12P……? Is there anything like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PNo, there are various things and it is in nervous\x01",
            "Because it seems it was getting.\x02\x03",
            "#00002FWell, the theme park is also\x01",
            "It seems I enjoyed it.\x01",
            "I do not need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#12PHaha, that's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_34D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_3663")

    ChrTalk(
        0x109,
        (
            "#10105F#12Pあ、Randy先輩とWaji君が\x01",
            "He took me there … …\x02\x03",
            "#10100FI think that I am already going to the guesthouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PWell, then, I'm relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PEr …\x01",
            "Keyaちゃんに何か？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PNo, there are various things and it is in nervous\x01",
            "Because it seems it was getting.\x02\x03",
            "#00002FWell, the theme park is also\x01",
            "It seems I enjoyed it.\x01",
            "I do not need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F#12PHuh, you are right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_3663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_37EC")

    ChrTalk(
        0x105,
        (
            "#10305F#12POh, the female team together\x01",
            "I guess I brought you.\x02\x03",
            "#10300FAre not you going to the guesthouse anymore?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PWell, then, I'm relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#12P… … What happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PNo, there are various things and it is in nervous\x01",
            "Because it seems it was getting.\x02\x03",
            "#00002FWell, the theme park is also\x01",
            "It seems I enjoyed it.\x01",
            "I do not need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#12PGiggle\x01",
            "It certainly was a big deal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EC")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 5700, 0, 13400, 315)
    SetScenarioFlags(0x145, 6)
    OP_1B(0x1, 0xFF, 0xFFFF)
    EventEnd(0x5)
    Return()

    # Function_10_2FBB end

    def Function_11_380B(): pass

    label("Function_11_380B")

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
            "#05203F#5P#30W(………………………………)\x02\x03",
            "#05208F(\"wall\"……)\x02\x03",
            "(\"Wall\" that stands in the way of going … …))\x02\x03",
            "#05201F(Mayor of Dieter\x01",
            "In his way of doing \"wall\"\x01",
            "Are you trying to break through … …)\x02\x03",
            "#05206F(… … but we are … …)\x02",
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

    def lambda_3AA0():
        OP_96(0xFE, 0xFFFE6736, 0x226, 0xFFFEC1D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AA0)
    OP_A0(0x101, 1200, 0x0, 0x5)
    ClearChrFlags(0x101, 0x20)
    Sound(812, 0, 100, 0)
    OP_79(0x9)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#05208F#5P(… at the mafia time without permission\x01",
            "\"Wall\" just disappeared … …)\x02\x03",
            "(And there is more \"wall\"\x01",
            "Now trying to be standing … …)\x02\x03",
            "#05203F(We are - ─ also\x01",
            "I am not very helpful … …)\x02\x03",
            "#05213F(… … Is it really okay …?\x02",
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
            "#05206F#5P(……It is useless.\x01",
            "I am tired but I can not sleep at all. )\x02\x03",
            "#05200F(In a little lounge\x01",
            "I wonder if I will drink water as well ……)\x02",
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

    def lambda_3C7D():
        OP_98(0xFE, 0x0, 0x0, 0x12C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C7D)
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

    def lambda_3CF3():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CF3)
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

    # Function_11_380B end

    def Function_12_3D99(): pass

    label("Function_12_3D99")

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
        "#00005F(Ah……)\x02",
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
        "#01808F#40W#5P………………………….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#11P……やあ、Lisha。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(11200, 1000, 14250, 4000)
    MoveCamera(315, 23, 0, 4000)

    def lambda_3F3E():
        OP_95(0xFE, 11720, 0, 12790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F3E)
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
        "#30W#3246VMr. Lloyd, was it … ….\x02",
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
            "#00005F#6P……?\x02\x03",
            "#00012FSorry, suddenly speaking out\x01",
            "Did you surprise him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#30W#11PHaha, that … ….\x02\x03",
            "#01802F#30WI was just dancing\x01",
            "I was just doing it … …\x02\x03",
            "#01808F#30W………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PEr …\x02\x03",
            "#00002FIs it there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01803F#30W#11P…………………… (Kokun)\x02",
    )

    CloseMessageWindow()
    OP_68(12100, 1000, 15400, 2000)

    def lambda_415B():
        OP_95(0xFE, 13000, 0, 15400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_415B)
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

    # Function_12_3D99 end

    def Function_13_41EB(): pass

    label("Function_13_41EB")

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
            "#01804F#5PMr. Lloyd is strange.\x02\x03",
            "#01810FWhen you want someone to be by your side\x01",
            "It really is there … …\x02\x03",
            "Just staying there\x01",
            "I feel relieved somewhat ……\x02\x03",
            "#01809FHuh, the support department\x01",
            "Everyone envious.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#12PHaha, I'm buying it.\x02\x03",
            "#00006FAs a single investigator\x01",
            "As a leader of everyone\x01",
            "There are plenty of things missing.\x02\x03",
            "#00008FMore……\x01",
            "I have to get even bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01810F#5P#30WKusu\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        (
            "#00003F#12P──なあ、Lisha。\x02\x03",
            "#00008FIt may be rude, but … ….\x01",
            "Can you tell me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01805F#5P……?\x02\x03",
            "#01810FHow rude … ….\x01",
            "What on earth?\x02",
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
            "#00006F#12PWhy are you so much …?\x02\x03",
            "#00001FSo much transient#2RFake#Look out\x01",
            "Laughing … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01812F#5P……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P…… from the moment I met\x01",
            "I feel like it was.\x02\x03",
            "#00003FIria wanted it\x01",
            "Worked on the best stage … …\x02\x03",
            "Lisha・マオといえば\x01",
            "Crosby is now a celebrity.\x02\x03",
            "#00001FBut why … ….\x02\x03",
            "Why are you always\x01",
            "A smile like giving up something\x01",
            "I'm floating … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01808F#5PWhy, why … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P…… People who know well for a while,\x01",
            "It was a smile that was floating.\x02",
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
            "#00008F#12PNow, such a fragile smile is\x01",
            "It has stopped showing me ….\x02\x03",
            "#00001FHowever, if you notice it suddenly\x01",
            "I feel like I was such a smile all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01806F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PThe smile of the person is to my favorite person\x01",
            "To the sadness that we can not meet anymore\x01",
            "It tried to endure.\x02\x03",
            "#00001FThen, you are …?\x02\x03",
            "You are my favorite Iria\x01",
            "Why do you laugh like that?\x02\x03",
            "She is always by your side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01808F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01803F#5P…… To be honest, I was surprised.\x02\x03",
            "#01810FI thought it was sharp though\x01",
            "Nothing like that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P……Well then………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01804F#5PHuh … … the correct answer.\x02\x03",
            "#01810FPerhaps I am … … before long\x01",
            "I think that I will leave the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#12P…… After all?\x02\x03",
            "#00008FReason……\x01",
            "Is not it something I can hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5P……………Yes.\x02\x03",
            "#01808F… But, that's right.\x01",
            "I will stop the details … …\x02\x03",
            "#01810FI originally ……\x01",
            "There is a way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PThe way to walk …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5PHehe, it is like a family business.\x02\x03",
            "#01808F……From a young age……\x01",
            "For that I came alive.\x02\x03",
            "From an ancient period of time\x01",
            "The road the ancestor inherited …\x02\x03",
            "#01803FFor what purpose now\x01",
            "I do not know the way I'm walking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PIs it so……\x02\x03",
            "#00001F… But, if it were … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01810F#5PThat does not need it …\x01",
            "That's a way I can not deny it.\x02\x03",
            "#01804FAt least my father,\x01",
            "Meaning to inherit that path\x01",
            "It seemed to be heading.\x02\x03",
            "Working on the world itself,\x01",
            "Could be a chance to move history,\x01",
            "A dark and tight way ……\x02\x03",
            "#01808FAnd I also\x01",
            "Inheriting that path from my father,\x01",
            "I have walked to … …\x02\x03",
            "#01810F…… Yes, even from now on ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#01804F#5PFuh … … It is weird, I am.\x02\x03",
            "The wine Iiria recommended has been\x01",
            "I refused properly ….\x02\x03",
            "#01810F…… Or to the light of the moon\x01",
            "I wonder if I got drunk … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PHaha … maybe so.\x02\x03",
            "#00006F…… Sorry.\x01",
            "Have you entered lightly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5PNo, that's fine.\x02\x03",
            "#01810FSomehow I …\x01",
            "Because it was full.\x02\x03",
            "#01809FListen to the story\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PI see……\x01",
            "I am honored to serve you.\x02\x03",
            "#00001Fでも、Lisha。\x01",
            "Perhaps you are ─ ─\x02",
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
        "Keyaのvoice",
        "#3614V#50W#13A…… Lloyd … ….?\x02",
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
        "#00005FKeya……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 160, -1, -1)

    AnonymousTalk(
        0x8,
        "#01805F……Oh……\x02",
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
            "#05805F#30W#6P……Ah……\x01",
            "Lishaもいたんだー……\x02\x03",
            "#05800F#30W…… I'm talking to you … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#5PWell, no.\x01",
            "Because it is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11POh, it's okay.\x02\x03",
            "#00001FPossibly\x01",
            "Can not you sleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#05808F#30W#6P…………Yup……\x02\x03",
            "#05806F#30W…… somehow scary Yume\x01",
            "I felt like I saw it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see……\x02\x03",
            "#00000FDo you sleep together in my bed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#05812F#30W#6PIs that it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#11POh, it's special.\x02",
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

    def lambda_5412():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5412)
    OP_93(0xD, 0x2D, 0x1F4)
    Sleep(500)

    def lambda_5431():
        OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5431)
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
        "Keya",
        "#05809F#30W#5P…… Hehe …\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#6Pごめん、Lisha。\x01",
            "I was interrupted in an odd form.\x02",
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
            "#01809F#5PHuh, it is unexpected.\x02\x03",
            "#01802FThanks to Mr. Lloyd\x01",
            "I am going to sleep somewhat.\x02\x03",
            "#01804FThank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01808F#5P…… The story of the past.\x01",
            "How about Iria\x01",
            "Please keep it secret.\x02\x03",
            "#01810FLook at every fold\x01",
            "I'm going to talk myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P……I understood.\x02\x03",
            "#00000FAlthough it may not be reliable\x01",
            "Please call out if there is something.\x02\x03",
            "As much as possible\x01",
            "Because I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#5PHehu ……\x01",
            "Thank you very much.\x02\x03",
            "#01802FThen, if you are in trouble\x01",
            "I will consult him.\x02",
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
            "#3247V#40W── Good night.\x01",
            "ロイドさん、Keyaちゃん。\x02",
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
        "#00002F#6Pおやすみ、Lisha。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x101,
        "Keya",
        "#05809F#3615V#50W#12Pgood night……\x02",
    )

    CloseMessageWindow()
    OP_24(0xE1F)
    OP_C9(0x1, 0x80000000)
    OP_68(12900, 1000, 13970, 5000)

    def lambda_5867():

        label("loc_5867")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5867")

    QueueWorkItem2(0x101, 2, lambda_5867)
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_5880():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5880)
    WaitChrThread(0x8, 1)

    def lambda_5899():
        OP_9B(0x0, 0xFE, 0xFFD3, 0x7D0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5899)
    WaitChrThread(0x8, 1)

    def lambda_58B2():
        OP_9B(0x0, 0xFE, 0xFFD3, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_58B2)
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
        "Keya",
        (
            "#05808F#30W#6P……Lisha、どうしたの？\x02\x03",
            "#05812F#30WIt looks somewhat sad somewhat\x01",
            "I feel a bit different …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5Pそっか、Keyaも判るのか。\x02\x03",
            "#00006F… Well, there seems to be various.\x02\x03",
            "#00000FAs much as I can\x01",
            "I will keep in mind.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Keya",
        (
            "#05809F#30W#6PErr …\x01",
            "Lloyd, cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FI'm not kidding.\x02\x03",
            "#00004FWell ……\x01",
            "Let's get back to bed and sleep.\x02\x03",
            "#00005FOh, did you finish the toilet?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Keya",
        (
            "#05801F#30W#6PMuuu …\x01",
            "Lloyd, it is too overstatish!\x02",
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

    # Function_13_41EB end

    def Function_14_5B27(): pass

    label("Function_14_5B27")

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
    SetChrName("voice")

    AnonymousTalk(
        0xFF,
        "#2913V#2S#30W…… Lloyd ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("voice")

    AnonymousTalk(
        0xFF,
        "#4107V#30WGet up … … Lloyd ……\x02",
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
        "#05211FHappy …!\x02",
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
            "#05205F#30W#5Pthat……\x02\x03",
            "#05208F…. What time is it now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PI guess it's around 2 o'clock in the middle of the night.\x02\x03",
            "#10300FThough it was hurried extensively\x01",
            "what's up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#05206F#5POh, something strange dream\x01",
            "It seems I was watching ……\x02\x03",
            "#05205F……that………\x02",
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
        "#05211F#5P…………Huh………?\x02",
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
        "#14105F#2759V#6P#40W#13A#NWhat is wrong …?\x02",
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
            "#05208F#11PRandy……\x01",
            "Did you wake me up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#14106F#6PWell, do not mind.\x02\x03",
            "#14101FMore than that …\x01",
            "Is there no keeper?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11PTwo people came back with me\x01",
            "It seems that I slept together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#05206F#5PHave you both noticed it?\x02\x03",
            "#05201F……is that so.\x01",
            "I should have been sleeping together ….\x02",
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
            "#10308F#5PHmm … …?\x01",
            "It does not seem to be in the room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#14100F#6PWell, let's look for it for a moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#05206F#5POh, I'm sorry but I beg you.\x02",
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
            "Lloyd searched for the area of 3F\x01",
            "Keyaの姿はどこにも見つからなかった。\x02\x03",
            "Among them, Tio who showed signs appeared,\x01",
            "We will also ask cooperation for women's groups ……\x02\x03",
            "Furthermore, I call people of the hotel\x01",
            "It was decided to look for 2F.\x07\x00\x02",
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

    # Function_14_5B27 end

    def Function_15_6158(): pass

    label("Function_15_6158")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(Even if I return to my room\x01",
            "I'm not going to sleep yet. )\x02\x03",
            "Go to the lounge and chill your head.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -100030, 0, 6530, 0)
    EventEnd(0x4)
    Return()

    # Function_15_6158 end

    def Function_16_61CB(): pass

    label("Function_16_61CB")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00006F(Anything, anything like this in the middle of the night\x01",
            "It is unscrupulous to visit. )\x02\x03",
            "Let 's calm down in the early place lounge.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -107740, 0, 9540, 90)
    EventEnd(0x4)
    Return()

    # Function_16_61CB end

    def Function_17_624A(): pass

    label("Function_17_624A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00006F(Anything, anything like this in the middle of the night\x01",
            "It is unscrupulous to visit. )\x02\x03",
            "Let 's calm down in the early place lounge.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -99710, 0, 11750, 180)
    EventEnd(0x4)
    Return()

    # Function_17_624A end

    SaveToFile()

Try(main)
