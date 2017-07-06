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
        "リーシャ",               # 1
        "ロッチー",               # 2
        "ゾルク",                 # 3
        "ランディ",               # 4
        "ワジ",                   # 5
        "キーア",                 # 6
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
            "あれっ、お客様……\x01",
            "もう行っちゃうんですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300Fああ、ちょっと迎賓館に呼ばれててね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "そ、そうですか。\x01",
            "行ってらっしゃいませ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "（そ、そんな〜……\x01",
            "  まだほとんどお世話\x01",
            "  できてないのに〜!）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302Fフフ、おかしな子だ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F……お前、分かってやってるな？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6BE")

    label("loc_697")


    ChrTalk(
        0xFE,
        (
            "はAh...\x01",
            "行ってらっしゃいませ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE")

    Jump("loc_893")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85A")

    ChrTalk(
        0xFE,
        "あれっ、ワジ様は.......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fああ、ワジならもう\x01",
            "迎賓館の方に行ったんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "そ、そんな〜……\x01",
            "まだほとんどお世話\x01",
            "できてないのに〜!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_7A0")

    ChrTalk(
        0x102,
        "#00106F（さすがワジ君、大人気ね……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_852")

    label("loc_7A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_7DF")

    ChrTalk(
        0x103,
        "#00203F（さすがワジさん、大人気ですね……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_852")

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_81A")

    ChrTalk(
        0x104,
        "#00301F（あんにゃろう、大人気だAh…）\x02",
    )

    CloseMessageWindow()
    Jump("loc_852")

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_852")

    ChrTalk(
        0x109,
        "#10106F（さすがワジ君、大人気ですね……）\x02",
    )

    CloseMessageWindow()

    label("loc_852")

    SetScenarioFlags(0x0, 1)
    Jump("loc_893")

    label("loc_85A")


    ChrTalk(
        0xFE,
        (
            "はAh...もう少しワジ様の\x01",
            "お世話をしたかったなAh...\x02",
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
            "バーカウンターの営業は\x01",
            "間もなく終了いたします。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "深夜の時間帯は\x01",
            "ご注文できませんので、\x01",
            "どうかご了承くださいませ。\x02",
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
            "◆エリィが好き\x01",        # 0
            "◆ティオが好き\x01",        # 1
            "◆ランディが好き\x01",      # 2
            "◆ノエルが好き\x01",        # 3
            "◆ワジが好き\x01",          # 4
            "◆変更しない\x01",          # 5
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
            "#00008F#30WYes…Yes.\x02\x03",
            "#00000FI see…\x01",
            "それなら安心だと思います。\x02\x03",
            "#00006F#20Wすみません、自分たちだけ\x01",
            "楽しんで来てしまって……\x02\x03",
            "#00002F……Haha, understood.\x01",
            "せいぜい充電してきます。\x02",
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
            "#00006F#11PHaa\x01",
            "支援課の方は何もなしか。\x02\x03",
            "#00008Fさすがに気にしすぎだとは\x01",
            "思うんBut…\x02",
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
            "#4111V#40WウHah\x01",
            "初めまして、支援課の諸君。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4112V#40Wお近づきの印に\x01",
            "置き土産を置いていくから\x01",
            "愉しんでくれると嬉しいな噴\x07\x00\x02",
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
            "#00003F#11P（多分、あいつがテロリストに\x01",
            "  タワーのデータを流したんだろう。）\x02\x03",
            "（But…テロリストたちの\x01",
            "  仲間ってわけじゃなさそうだ。）\x02\x03",
            "#00008F（そして《銀》の言ったとおり、\x01",
            "  黒月や赤い星座の一員でもない……）\x02\x03",
            "#00001F（……いったい何者だ.......?）\x02",
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
        "エリィの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3397V#2S#5P#30W#18A……ロイド？\x01",
            "まだ部屋にいるの？\x07\x00\x02",
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
            "#00005F#6Pああ、エリィか。\x02\x03",
            "#00002Fいいよ、入ってきてくれ。\x02",
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
        "あら、どこかに連絡していたの？\x02",
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
            "#00004F#6Pああ、課長にね。\x02\x03",
            "#00008F……留守中に支援課のビルで\x01",
            "何か起きていないかと思って\x01",
            "連絡してみたんBut…\x02\x03",
            "#00000F取り越し苦労だったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PI see…\x02\x03",
            "#00108F……確かに通商会議の時に\x01",
            "起こったことを考えると\x01",
            "心配するのも分かるけど……\x02\x03",
            "#00102F今日くらいは何も考えずに\x01",
            "休暇を楽しんだ方がいいわ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha…Yeah we should\x02\x03",
            "#00002Fゴメン、ひょっとして\x01",
            "迎えに来てくれたのか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11Pあ、Yeah…\x01",
            "姿が見えなかったから。\x02\x03",
            "#00108Fよかったら一緒に迎賓館まで\x01",
            "行こうと思ったんBut…\x02\x03",
            "#00113F……その、迷惑じゃなければ。\x02",
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
            "#00011F#6Pめ、迷惑なわけないって!\x02\x03",
            "#00006FまSeriously…\x01",
            "エリィ、からかってるだろ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11Pか、からかってるつもりじゃ\x01",
            "ないんBut…\x02\x03",
            "#00109Fそ、それじゃあ一緒に\x01",
            "迎賓館まで行きましょう。\x02\x03",
            "晩餐会まで時間はあるから\x01",
            "少し寄り道してもいいし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6Pそ、Yeah we should\x01",
            "下の店とか覗いてもいいかもな。\x02\x03",
            "#00012F（って、なんで２人して\x01",
            "  こんなに慌ててるんだ.......?）\x02",
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
        "ティオの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2678V#2S#5P#30W#18A……ロイドさん。\x01",
            "ちょっといいですか？\x07\x00\x02",
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
            "#00005F#6Pああ、ティオか。\x02\x03",
            "#00002Fいいよ、入ってきてくれ。\x02",
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
        "……ひょっとして課長に？\x02",
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
            "#00004F#6Pはは、よく分かったな。\x02\x03",
            "#00008F……留守中に支援課のビルで\x01",
            "何か起きていないかと思って\x01",
            "連絡してみたんBut…\x02\x03",
            "#00000F取り越し苦労だったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PI see..\x02\x03",
            "#00208F……確かにあのハッカーといい\x01",
            "気になる事が残っていますけど……\x02\x03",
            "#00202Fせっかくのバカンスですから\x01",
            "休んだ方がいいのでは？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha…Yeah we should\x02\x03",
            "#00002Fゴメン、ひょっとして\x01",
            "迎えに来てくれたのか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11Pはい、皆さんぼちぼち\x01",
            "迎賓館の方に向かってます。\x02\x03",
            "#00200Fまあ、まだ晩餐会まで\x01",
            "時間はあるみたいなので\x01",
            "急ぐ必要はありませんが……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6Pいや、俺ももう出るよ。\x02\x03",
            "よかったらティオ、\x01",
            "一緒に迎賓館まで行くか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#11P………Yes.\x02\x03",
            "#00208Fえっと、下のお店とか\x01",
            "覗いていってもいいですか？\x02\x03",
            "#00206Fその、１人で入るのは\x01",
            "ちょっと抵抗があって……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#11Pな、何かおかしいですか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6Pい、いやいや!\x02\x03",
            "#00002F分かった。\x01",
            "少し寄り道していくか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11P……はいっ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P（うーん、ティオが普通のお店に\x01",
            "  興味を示すのも新鮮だAh…）\x02",
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
        "ランディの声",
        (
            "#2758V#5P#30W#19Aおっと、やっぱり\x01",
            "まだ部屋に居たのかよ。\x02",
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
        "#00002F#6Pああ、ランディか。\x02",
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
            "なんだ、どこかに\x01",
            "連絡でもしてたのかよ？\x02",
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
            "#00006F#6Pああ、課長にね。\x02\x03",
            "#00008F……留守中に支援課のビルで\x01",
            "何か起きていないかと思って\x01",
            "連絡してみたんBut…\x02\x03",
            "#00000F取り越し苦労だったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#11PI see…\x02\x03",
            "#00303Fま、叔父貴たちも相変わらず\x01",
            "クロスベルに居座ってるしAh…\x02\x03",
            "#00300F正直、俺も気にはなるが\x01",
            "今日くらいは楽しんだ方が\x01",
            "いいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha…Yeah we should\x02\x03",
            "#00002Fゴメン、ひょっとして\x01",
            "迎えに来てくれたのか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11Pああ、みんなボチボチ\x01",
            "迎賓館の方に行ってるぜ。\x02\x03",
            "#00300F晩餐会まで\x01",
            "まだ時間はあるみてぇだから\x01",
            "急がなくてもよさそうだが。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6Pいや、俺ももう出るよ。\x02\x03",
            "#00002Fそういえばランディ、\x01",
            "昼に宝飾店とか覗いてたよな。\x02\x03",
            "品揃えとかってどうだった？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#11Pああ、さすが高いだけあって\x01",
            "いいモンが揃ってたが……\x02\x03",
            "#00302Fなんだぁ、ひょっとして\x01",
            "気になる子にプレゼントかよ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6Pい、No…\x01",
            "単に気になっただけだけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11P照れるな、照れるな。\x02\x03",
            "#00302Fよーし、もし立ち寄ったら\x01",
            "お兄さんがアドバイスしてやるよ!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6Pだから違うって……\x02\x03",
            "#00000Fまあいいや、とにかく出るか。\x02",
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
        "ノエルの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3518V#2S#5P#30W#19A……ロイドさん。\x01",
            "そちらにいますか？\x07\x00\x02",
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
            "#00005F#6Pああ、ノエルか。\x02\x03",
            "#00002Fいいよ、入ってきてくれ。\x02",
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
            "あ、どちらかに\x01",
            "連絡をしてたんですか？\x02",
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
            "#00004F#6Pああ、課長にね。\x02\x03",
            "#00008F……留守中に支援課のビルで\x01",
            "何か起きていないかと思って\x01",
            "連絡してみたんBut…\x02\x03",
            "#00000F取り越し苦労だったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10113F#11PI see…\x02\x03",
            "#10106Fあんな事があった後ですから\x01",
            "さすがに気になりますよね……\x02\x03",
            "#10108F….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6Pああもう、ノエルまで\x01",
            "深刻になることはないだろ？\x02\x03",
            "#00006Fその……ゴメンな。\x01",
            "テンション下がること言って。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#11Pい、いえ、こちらこそ。\x02\x03",
            "#10106Fどうも心配性なのが\x01",
            "性分になってるみたいで……\x02\x03",
            "#10100Fたまにフランのお気楽さが\x01",
            "うらやましくなります。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6Pはは、そっか。\x02\x03",
            "#00002Fそういう意味では俺たち、\x01",
            "結構似てるのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#11Pそ、そんなことないですよ!\x01",
            "頭の出来とか全然違いますし!\x02\x03",
            "#10112Fあたしのはその……\x01",
            "単なる警備隊根性といいますか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P（うーん、相変わらず\x01",
            "  自己評価が厳しいなぁ。）\x02\x03",
            "#00000Fまあいいや、えっと\x01",
            "迎えに来てくれたんだよな？\x02\x03",
            "よかったら\x01",
            "一緒に迎賓館まで行こうか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#11Pあ、Roger!\x02\x03",
            "#10100Fそういえば、晩餐会って\x01",
            "凄いお屋敷でやるみたいですね？\x02\x03",
            "あのハルトマン元議長が\x01",
            "住んでいたっていう……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6Pああ、正直あり得ないほど\x01",
            "豪華絢爛って感じの屋敷だよ。\x02\x03",
            "#00002F初めて入るんだったら\x01",
            "目を丸くすること請け合いRight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PあHaha…\x01",
            "ちょっと楽しみです。\x02",
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
        "ワジの声",
        (
            "#2912V#5P#30W#20Aああ、やっぱり\x01",
            "まだ部屋に居たのか。\x02",
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
        "#00002F#6Pああ、ワジか。\x02",
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
            "Hah, I see\x02\x03",
            "留守中の支援課のビルが気になって\x01",
            "課長に連絡してたのかい？\x02",
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
        "#00011F#6Pな、何で分かるんだ!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11P一月以上一緒にいたら\x01",
            "そのくらいは読めるよ。\x02\x03",
            "#10302Fフフ、思っていた以上に\x01",
            "リーダーしてるみたいじゃない？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha…心配性なだけさ。\x02\x03",
            "#00008F本当に優秀なリーダーなら\x01",
            "どっしりと構えてるだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#11Pま、リーダーとしての優秀さは\x01",
            "人それぞれだと思うけど。\x02\x03",
            "#10304F頭も悪くないしカンも鋭いけど\x01",
            "基本的に君は“凡人”だしね。\x02\x03",
            "#10302F出来る範囲で地道に頑張るのは\x01",
            "悪くないんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PUgh…はっきり言うなぁ。\x02\x03",
            "#00013Fお前のそういう所は\x01",
            "逆に嫌味がなくていいけどさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11Pフフ、君のそういう素直さは\x01",
            "僕も気に入ってるけどね。\x02\x03",
            "#10302Fそもそも、あのツァオといい、\x01",
            "ふざけた帝国エージェントといい、\x01",
            "鋭い人間はとことん鋭いワケだし。\x02\x03",
            "同じ方向で対抗するより\x01",
            "君なりの強みを生かした方が\x01",
            "いいんじゃないの？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#11Pあれ、なんか変なこと言った？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6Pいや、そんな風に考えたことは\x01",
            "あんまりなかったから……\x02\x03",
            "#00000Fありがとう、ワジ。\x01",
            "少し目が開かれた気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11Pフフ、それは何より。\x02\x03",
            "#10300F……で、そろそろ晩餐会、\x01",
            "行かなくていいのかい？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6Pああ、それじゃ一緒に行くか。\x02",
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
            "#00005F#5Pそういえば、キーアは\x01",
            "誰かが連れていったのかな？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_31E9")

    ChrTalk(
        0x102,
        (
            "#00104F#12Pええ、ティオちゃんが\x01",
            "連れて行ってくれたけど……\x02\x03",
            "#00100Fもう迎賓館に行ってるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5Pそっか、それなら安心Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PUhm...何かあったの？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5Pいや、色々あってナーバスに\x01",
            "なってたみたいだからさ。\x02\x03",
            "#00002Fまあ、テーマパークも\x01",
            "楽しんでくれたみたいだし\x01",
            "心配いらないと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#12Pふふっ、そうね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_31E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_335C")

    ChrTalk(
        0x103,
        (
            "#00205F#12Pはい、エリィさんが\x01",
            "連れて行ってくれましたが……\x02\x03",
            "#00202Fもう迎賓館に行っているかと。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5Pそっか、それなら安心Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P……キーアに何か？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5Pいや、色々あってナーバスに\x01",
            "なってたみたいだからさ。\x02\x03",
            "#00002Fまあ、テーマパークも\x01",
            "楽しんでくれたみたいだし\x01",
            "心配いらないと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12PHmm \x02",
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_335C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_34D1")

    ChrTalk(
        0x104,
        (
            "#00305F#12Pああ、お嬢とティオすけが\x01",
            "連れて行ってたが……\x02\x03",
            "#00300Fもう迎賓館に行ってんじゃね？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5Pそっか、それなら安心Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12P.......?　何かあんのか？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5Pいや、色々あってナーバスに\x01",
            "なってたみたいだからさ。\x02\x03",
            "#00002Fまあ、テーマパークも\x01",
            "楽しんでくれたみたいだし\x01",
            "心配いらないと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#12Pハハ、Yeah we should\x02",
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_34D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_3663")

    ChrTalk(
        0x109,
        (
            "#10105F#12Pあ、ランディ先輩とワジ君が\x01",
            "連れて行ってくれましたけど……\x02\x03",
            "#10100Fもう迎賓館に行ってると思います。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5Pそっか、それなら安心Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PUhm...\x01",
            "キーアちゃんに何か？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5Pいや、色々あってナーバスに\x01",
            "なってたみたいだからさ。\x02\x03",
            "#00002Fまあ、テーマパークも\x01",
            "楽しんでくれたみたいだし\x01",
            "心配いらないと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F#12PEhe, that's true\x02",
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_3663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_37EC")

    ChrTalk(
        0x105,
        (
            "#10305F#12Pああ、女性陣が一緒に\x01",
            "連れて行ったみたいだけど。\x02\x03",
            "#10300Fもう迎賓館に行ってるんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5Pそっか、それなら安心Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#12P……何かあったのかい？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5Pいや、色々あってナーバスに\x01",
            "なってたみたいだからさ。\x02\x03",
            "#00002Fまあ、テーマパークも\x01",
            "楽しんでくれたみたいだし\x01",
            "心配いらないと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#12PHah\x01",
            "確かに大はしゃぎだったね。\x02",
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
            "#05203F#5P#30W（….）\x02\x03",
            "#05208F（《壁》……）\x02\x03",
            "（行く手に立ち塞がる《壁》……）\x02\x03",
            "#05201F（ディーター市長は\x01",
            "　彼なりのやり方で《壁》を\x01",
            "　突破しようとしているのか……）\x02\x03",
            "#05206F（……でも俺たちは……）\x02",
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
            "#05208F#5P（……マフィアの時は勝手に\x01",
            "  《壁》が消滅しただけだった……）\x02\x03",
            "（そして、それ以上の《壁》が\x01",
            "  立ち塞がろうとしている今……）\x02\x03",
            "#05203F（俺たちは──俺はまた\x01",
            "  あまり役に立てないでいる……）\x02\x03",
            "#05213F（……それで本当にいいのか.......?）\x02",
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
            "#05206F#5P（……駄目だ。\x01",
            "  疲れてるのに全然眠れない。）\x02\x03",
            "#05200F（ちょっとラウンジで\x01",
            "  水でも飲んでくるかAh…）\x02",
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
        "#00005F（Ah...）\x02",
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
        "#01808F#40W#5P…..\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#11P……やあ、リーシャ。\x02",
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
        "#30W#3246Vロイドさん、でしたか……\x02",
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
            "#00005F#6P.......?\x02\x03",
            "#00012Fごめん、いきなり声をかけて\x01",
            "驚かせたかな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#30W#11Pあはは、そんAh…\x02\x03",
            "#01802F#30W私がただ、ボーッと\x01",
            "していただけですし……\x02\x03",
            "#01808F#30W….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PUhm...\x02\x03",
            "#00002Fそこ、いいかな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01803F#30W#11P………（コクン）\x02",
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
            "#01804F#5Pロイドさんは不思議True.\x02\x03",
            "#01810F誰かに側に居て欲しい時に\x01",
            "本当にそこに居てくれて……\x02\x03",
            "そこに居てくれるだけで\x01",
            "なんだか安心できてしまう……\x02\x03",
            "#01809Fふふっ、支援課の\x01",
            "皆さんが羨ましいです。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#12Pはは、買い被りだよ。\x02\x03",
            "#00006F一人前の捜査官としても\x01",
            "みんなのリーダーとしても\x01",
            "まだまだ足りない所が多くてね。\x02\x03",
            "#00008FもAhh\x01",
            "もっと大きくならなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01810F#5P#30Wクス……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        (
            "#00003F#12P──なあ、リーシャ。\x02\x03",
            "#00008F失礼かもしれないけど……\x01",
            "聞かせてもらってもいいか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01805F#5P.......?\x02\x03",
            "#01810F失礼だなんて……\x01",
            "いったい何でしょうか？\x02",
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
            "#00006F#12Pどうして君はそんWhat…\x02\x03",
            "#00001Fそんなに儚#2Rはかな#い目をして\x01",
            "笑うんだ.......?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01812F#5P…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P……思えば出会った時から\x01",
            "そうだった気がする。\x02\x03",
            "#00003Fイリアさんに望まれて\x01",
            "最高のステージで活躍して……\x02\x03",
            "リーシャ・マオといえば\x01",
            "今やクロスベルじゃ有名人だ。\x02\x03",
            "#00001Fなのにどうして……\x02\x03",
            "どうして君はいつも\x01",
            "何かを諦めたような微笑みを\x01",
            "浮かべてるんだ.......?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01808F#5Pど、どうしてそんAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P……よく知ってる人が一時期、\x01",
            "浮かべていた笑顔だったからさ。\x02",
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
            "#00008F#12P今ではもう、そんな儚げな笑顔は\x01",
            "見せなくなってくれたけど……\x02\x03",
            "#00001Fだけど君は、ふと気付いたら\x01",
            "いつもそんな笑顔だった気がする。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01806F#5P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12Pその人の笑みは、大好きな人に\x01",
            "もう会えないという哀しみに\x01",
            "耐えようとするものだった。\x02\x03",
            "#00001Fだったら、君は.......?\x02\x03",
            "イリアさんが大好きな君は\x01",
            "どうしてそんな風に笑うんだ？\x02\x03",
            "彼女はいつも君の側にいるのに。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01808F#5P.............…\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01803F#5P……正直、驚きました。\x02\x03",
            "#01810F鋭いとは思っていましたけど\x01",
            "まさかそこまでなんて……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P……それじゃAh...…\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01804F#5PEhe正解です。\x02\x03",
            "#01810F多分私は……そう遠くないうちに\x01",
            "クロスベルを去ると思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#12P……やっぱりか。\x02\x03",
            "#00008F理由は……\x01",
            "俺が聞けることじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5P……………Yes.\x02\x03",
            "#01808F……でも、そうTrue.\x01",
            "詳細は止めておきますが……\x02\x03",
            "#01810F私は本来……\x01",
            "歩むべき道があるんです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P歩むべき道.......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5Pふふ、家業のようなものです。\x02\x03",
            "#01808F……小さい頃から……\x01",
            "そのために生きて来ました。\x02\x03",
            "気の遠くなるような昔から\x01",
            "祖先が受け継いできた道……\x02\x03",
            "#01803F今となっては何のために\x01",
            "歩んでるのか分からない道を。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PI see\x02\x03",
            "#00001F……でも、だったら……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01810F#5Pだからといって必要ない……\x01",
            "そう否定もしきれない道です。\x02\x03",
            "#01804F少なくとも父は、\x01",
            "その道を受け継ぐことに意味を\x01",
            "見出しているようでした。\x02\x03",
            "世界そのものに働きかけ、\x01",
            "歴史を動かすきっかけ足り得る、\x01",
            "暗く密やかな道を……\x02\x03",
            "#01808Fそして私もまた\x01",
            "父からその道を受け継ぎ、\x01",
            "今まで歩いて来ました……\x02\x03",
            "#01810F……そう、これからもまた……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#01804F#5PEhhe変ですね、わたし。\x02\x03",
            "イリアさんが勧めてきたワインは\x01",
            "ちゃんと断ったんですけど……\x02\x03",
            "#01810F……それとも月の光に\x01",
            "酔ってしまったのかしら……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PHahaそうかもな。\x02\x03",
            "#00006F……ゴメン。\x01",
            "軽々しく立ち入ったかな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01804F#5Pいえ、いいんです。\x02\x03",
            "#01810Fなんだか私も……\x01",
            "一杯一杯になっていたので。\x02\x03",
            "#01809F話を聞いてくれて\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PI see….\x01",
            "お役に立てたら光栄だけど。\x02\x03",
            "#00001Fでも、リーシャ。\x01",
            "もしかして君は──\x02",
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
        "キーアの声",
        "#3614V#50W#13A……ロイドー.......?\x02",
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
        "#00005FKeA…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 160, -1, -1)

    AnonymousTalk(
        0x8,
        "#01805F……Oh?\x02",
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
            "#05805F#30W#6P……Ah...\x01",
            "リーシャもいたんだー……\x02\x03",
            "#05800F#30W……ひょっとしてお話中.......?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#5Pう、ううん。\x01",
            "もう終わったから。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11Pああ、大丈夫だぞ。\x02\x03",
            "#00001F……ひょっとして\x01",
            "眠れないのか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#05808F#30W#6P…………Yeah…\x02\x03",
            "#05806F#30W……なんだか恐いユメを\x01",
            "みたような気がして……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see….\x02\x03",
            "#00000F俺のベッドで一緒に寝るか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#05812F#30W#6P……いーの？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#11Pああ、特別だけどな。\x02",
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
        "キーア",
        "#05809F#30W#5P……えへWhat…\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00006F#6Pごめん、リーシャ。\x01",
            "変な形で中断しちゃってさ。\x02",
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
            "#01809F#5Pふふっ、とんでもない。\x02\x03",
            "#01802Fロイドさんのおかげで\x01",
            "私も何だか眠れそうです。\x02\x03",
            "#01804Fありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PI see….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01808F#5P……先ほどの話。\x01",
            "どうかイリアさんには\x01",
            "内緒にしていてください。\x02\x03",
            "#01810Fいずれ折を見て\x01",
            "自分で話すつもりですから。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P……分かった。\x02\x03",
            "#00000F頼りないかもしれないけど\x01",
            "何かあったら声をかけてくれ。\x02\x03",
            "出来る限りのことは\x01",
            "させてもらうからさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01809F#5PEhhe\x01",
            "That's fine, thank you\x02\x03",
            "#01802Fでは、もし困った事があれば\x01",
            "相談させてもらいますね。\x02",
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
            "#3247V#40W──おやすみなさい。\x01",
            "ロイドさん、キーアちゃん。\x02",
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
        "#00002F#6Pおやすみ、リーシャ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x101,
        "キーア",
        "#05809F#3615V#50W#12Pおやすみなさーい……\x02",
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
        "キーア",
        (
            "#05808F#30W#6P……リーシャ、What's wrong?\x02\x03",
            "#05812F#30Wいつも何だか哀しそうだけど\x01",
            "ちょっと感じが違ったねー.......?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5Pそっか、キーアも判るのか。\x02\x03",
            "#00006F……まあ、色々あるみたいだ。\x02\x03",
            "#00000F俺の方でもできるだけ\x01",
            "気を付けておくつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "キーア",
        (
            "#05809F#30W#6PえへWhat…\x01",
            "ロイド、カッコイイね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011Fからかうんじゃありません。\x02\x03",
            "#00004Fさてと……\x01",
            "とっととベッドに戻って寝よう。\x02\x03",
            "#00005Fあ、トイレとか済ませたか？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "キーア",
        (
            "#05801F#30W#6PむうUh\x01",
            "ロイド、でりかしーなさすぎ!\x02",
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
    SetChrName("声")

    AnonymousTalk(
        0xFF,
        "#2913V#2S#30W……Lloyd…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声")

    AnonymousTalk(
        0xFF,
        "#4107V#30W起きなよ……Lloyd…\x02",
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
        "#05211Fハッ…!\x02",
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
            "#05205F#30W#5PHuh?\x02\x03",
            "#05208F……今、何時だ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11P夜中の２時くらいかな。\x02\x03",
            "#10300F随分うなされてたけど\x01",
            "どうしたんだい？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#05206F#5Pああ、何だか変な夢を\x01",
            "見ていたみたいだ……\x02\x03",
            "#05205F……Huh?…\x02",
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
        "#05211F#5P…………Uh.......?\x02",
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
        "#14105F#2759V#6P#40W#13A#Nなんだ、どうした.......?\x02",
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
            "#05208F#11PRandy\x01",
            "起こしちゃったか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#14106F#6Pま、気にすんな。\x02\x03",
            "#14101Fそれより……\x01",
            "キー坊がいないのか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11Pさっき２人で戻ってきて\x01",
            "一緒に寝てたみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#05206F#5P２人とも気付いてたのか。\x02\x03",
            "#05201F……そうなんだ。\x01",
            "一緒に寝てたはずBut…\x02",
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
            "#10308F#5Pふぅん.......?\x01",
            "部屋にはいないみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#14100F#6Pま、ちょっと探してみようぜ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#05206F#5Pああ、悪いけど頼む。\x02",
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
            "ロイドたちは３Ｆの一帯を探したが\x01",
            "キーアの姿はどこにも見つからなかった。\x02\x03",
            "そのうち、気配を察したティオが現れ、\x01",
            "女性陣にも協力を頼む事になり……\x02\x03",
            "さらにはホテルの人間も呼んで\x01",
            "２Ｆも探してもらうこととなった。\x07\x00\x02",
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
            "#00003F（部屋に戻っても\x01",
            "  まだ眠れそうにないな。）\x02\x03",
            "（ラウンジに行って頭を冷やそう。）\x02",
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
            "#00006F（いくらなんでも、こんな夜中に\x01",
            "  訪ねるのは不謹慎Right.）\x02\x03",
            "（早い所ラウンジで落ち着こう。）\x02",
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
            "#00006F（いくらなんでも、こんな夜中に\x01",
            "  訪ねるのは不謹慎Right.）\x02\x03",
            "（早い所ラウンジで落ち着こう。）\x02",
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
