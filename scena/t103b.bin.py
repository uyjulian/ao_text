from ScenarioHelper import *

def main():
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
        "MWL staff",         # 1
        "MWL staff",         # 2
        "tourist",                 # 3
        "tourist",                 # 4
        "Marsun",               # 5
        "corona",                 # 6
        "Lima",                   # 7
        "Destination to Hotel · Delfinia",# 8
        "Direction to the theme park",       # 9
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

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "Destination to Hotel · Delfinia")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "Direction to the theme park")

    ChipFrameInfo(644, 0)                                        # 0

    ScpFunction((
        "Function_0_284",          # 00, 0
        "Function_1_33C",          # 01, 1
        "Function_2_44B",          # 02, 2
        "Function_3_515",          # 03, 3
        "Function_4_714",          # 04, 4
        "Function_5_7E2",          # 05, 5
        "Function_6_838",          # 06, 6
        "Function_7_8A2",          # 07, 7
        "Function_8_984",          # 08, 8
        "Function_9_A44",          # 09, 9
        "Function_10_AF3",         # 0A, 10
        "Function_11_BEC",         # 0B, 11
        "Function_12_13B0",        # 0C, 12
        "Function_13_1488",        # 0D, 13
        "Function_14_1627",        # 0E, 14
        "Function_15_16A7",        # 0F, 15
        "Function_16_1727",        # 10, 16
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_6F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_680")

    ChrTalk(
        0x8,
        (
            "I am in a theme park right now\x01",
            "The night section is being held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mitsushi go round the garden\x01",
            "The night parade is also a great success.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_636")

    ChrTalk(
        0x103,
        "#00203F…… To be honest, I wanted to see it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FWell, well this time it can not be helped.\x01",
            "At the next opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FFluff … … It is absolute.\x02",
    )

    CloseMessageWindow()
    Jump("loc_678")

    label("loc_636")


    ChrTalk(
        0x101,
        (
            "#00003F(Well, when Tio listens\x01",
            "I wonder she wants to … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_678")

    SetScenarioFlags(0x0, 0)
    Jump("loc_6F4")

    label("loc_680")


    ChrTalk(
        0x8,
        (
            "I am in a theme park right now\x01",
            "The night section is being held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mitsushi go round the garden\x01",
            "The night parade is also a great success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F4")

    Jump("loc_710")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_707")
    Jump("loc_710")

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_710")

    label("loc_710")

    TalkEnd(0xFE)
    Return()

    # Function_3_515 end

    def Function_4_714(): pass

    label("Function_4_714")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7C7")

    ChrTalk(
        0x9,
        (
            "Michelam specialty fireworks,\x01",
            "About 100 out of every day\x01",
            "We are launching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As well as theme parks,\x01",
            "From the hotel and the airship while sailing at night\x01",
            "It is a reputation to see it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DE")

    label("loc_7C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_7D5")
    Jump("loc_7DE")

    label("loc_7D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_7DE")

    label("loc_7DE")

    TalkEnd(0xFE)
    Return()

    # Function_4_714 end

    def Function_5_7E2(): pass

    label("Function_5_7E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_81D")

    ChrTalk(
        0xA,
        "(…, now you can hold your hand … …)\x02",
    )

    CloseMessageWindow()
    Jump("loc_834")

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_82B")
    Jump("loc_834")

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_834")

    label("loc_834")

    TalkEnd(0xFE)
    Return()

    # Function_5_7E2 end

    def Function_6_838(): pass

    label("Function_6_838")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_887")

    ChrTalk(
        0xB,
        "Wow, there are lots of fireworks … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "… …. Hehe, beautiful …\x02",
    )

    CloseMessageWindow()
    Jump("loc_89E")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_895")
    Jump("loc_89E")

    label("loc_895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_89E")

    label("loc_89E")

    TalkEnd(0xFE)
    Return()

    # Function_6_838 end

    def Function_7_8A2(): pass

    label("Function_7_8A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_94D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C0")
    Call(0, 8)
    Jump("loc_948")

    label("loc_8C0")


    ChrTalk(
        0xC,
        (
            "If I really wanted to stay at the hotel,\x01",
            "I can not make a reservation by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "まあ、Limaは楽しんでくれたようだし\x01",
            "I wonder if it came when it came.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_948")

    Jump("loc_980")

    label("loc_94D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_95B")
    Jump("loc_980")

    label("loc_95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_969")
    Jump("loc_980")

    label("loc_969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_977")
    Jump("loc_980")

    label("loc_977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_980")

    label("loc_980")

    TalkEnd(0xFE)
    Return()

    # Function_7_8A2 end

    def Function_8_984(): pass

    label("Function_8_984")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xC,
        (
            "Well, today is really\x01",
            "I wish I had played all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Lima、楽しかったかい？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yeah, it was fun! It is!\x01",
            "Thank you ~! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hehe, thank you.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_8_984 end

    def Function_9_A44(): pass

    label("Function_9_A44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_ABC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A62")
    Call(0, 8)
    Jump("loc_AB7")

    label("loc_A62")


    ChrTalk(
        0xD,
        "Hehe, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When you go home, delicious meal\x01",
            "I will make lots of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB7")

    Jump("loc_AEF")

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_ACA")
    Jump("loc_AEF")

    label("loc_ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AD8")
    Jump("loc_AEF")

    label("loc_AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_AE6")
    Jump("loc_AEF")

    label("loc_AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_AEF")

    label("loc_AEF")

    TalkEnd(0xFE)
    Return()

    # Function_9_A44 end

    def Function_10_AF3(): pass

    label("Function_10_AF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B11")
    Call(0, 8)
    Jump("loc_BB0")

    label("loc_B11")


    ChrTalk(
        0xE,
        (
            "At the top of the castle of Kagami,\x01",
            "Papa and Mama stay together forever\x01",
            "I asked you to stay!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Ferris wheel and horror coaster as well\x01",
            "I was able to ride and I really enjoyed it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB0")

    Jump("loc_BE8")

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_BC3")
    Jump("loc_BE8")

    label("loc_BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BD1")
    Jump("loc_BE8")

    label("loc_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BDF")
    Jump("loc_BE8")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_BE8")

    label("loc_BE8")

    TalkEnd(0xFE)
    Return()

    # Function_10_AF3 end

    def Function_11_BEC(): pass

    label("Function_11_BEC")

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

    def lambda_CBF():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CBF)
    Sleep(50)

    def lambda_CD7():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CD7)
    Sleep(50)

    def lambda_CEF():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CEF)
    Sleep(50)

    def lambda_D07():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D07)
    Sleep(50)

    def lambda_D1F():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D1F)
    Sleep(50)

    def lambda_D37():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D37)
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
        "#00107F#6PHere, this …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PThe banner is changing! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PCome on, hey ……\x02",
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

    def lambda_F15():
        OP_9B(0x0, 0x101, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F15)
    Sleep(50)

    def lambda_F2D():
        OP_9B(0x0, 0x102, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F2D)
    Sleep(50)

    def lambda_F45():
        OP_9B(0x0, 0x103, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F45)
    Sleep(50)

    def lambda_F5D():
        OP_9B(0x0, 0x104, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F5D)
    Sleep(50)

    def lambda_F75():
        OP_9B(0x0, 0x105, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F75)
    Sleep(50)

    def lambda_F8D():
        OP_9B(0x0, 0x109, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F8D)
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
        "#10108F#6PIndeed, this is … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#6PHmm, taste of night only#4REvent#Both\x01",
            "I do not think so ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P…… Such a story\x01",
            "I have never heard of it.\x02\x03",
            "#00201Fin addition……\x01",
            "To Mikoshi to other characters\x01",
            "I can not change it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PI guess it will be.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PThat is …\x02",
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
        "#00105F\"A clown#6RFool#Wonderland of … \"\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00306FCompletely name\x01",
            "Was not it rewritten …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(280, 160, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10113FYuu, even in a dream\x01",
            "I wonder if she is watching … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 160, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10306F…… Even if dreams are dreams\x01",
            "It looks like a nightmare.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    AnonymousTalk(
        0x101,
        "#00008F……………………………………\x02",
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
            "#00003F#5P── Apparently Kea\x01",
            "It seems to be ahead.\x02\x03",
            "#00013FIf it's the case\x01",
            "Anyway I have to get inside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6PYeah … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PI have no choice but to go …!\x02",
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

    # Function_11_BEC end

    def Function_12_13B0(): pass

    label("Function_12_13B0")

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
        "#6P#00002FAh…………\x02",
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

    # Function_12_13B0 end

    def Function_13_1488(): pass

    label("Function_13_1488")

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
            "#12P#00004F… Well then, then\x01",
            "Shall we go to the guest house soon?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_156F")

    ChrTalk(
        0x102,
        "#00102FYes, I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1600")

    label("loc_156F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1594")

    ChrTalk(
        0x103,
        "#00202FIt is okay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1600")

    label("loc_1594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_15B5")

    ChrTalk(
        0x104,
        "#00309FOh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1600")

    label("loc_15B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_15DA")

    ChrTalk(
        0x109,
        "#10109FI understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1600")

    label("loc_15DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1600")

    ChrTalk(
        0x105,
        "#10304FHuh, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_1600")

    OP_5A()
    ClearMapFlags(0x10000000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -57250, 0)
    EventEnd(0x5)
    Return()

    # Function_13_1488 end

    def Function_14_1627(): pass

    label("Function_14_1627")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FNight theme park too\x01",
            "It looks fun,\x01",
            "That's another opportunity again.\x02\x03",
            "Let's head to the guest house as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_14_1627 end

    def Function_15_16A7(): pass

    label("Function_15_16A7")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of the theme park\x01",
            "A sketch is drawn.\x02\x03",
            "On a large site\x01",
            "Various amusement facilities\x01",
            "It seems to be lining up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_15_16A7 end

    def Function_16_1727(): pass

    label("Function_16_1727")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ To everyone at this garden ~\x01\x01",
            "At this theme park\x01",
            "Runaway acts and carrying dangerous goods\x01",
            "We will refuse hard.\x01\x01",
            "In addition, children\x01",
            "Parents should be accompanied\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_16_1727 end

    SaveToFile()

Try(main)
