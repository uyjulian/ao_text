from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1000_2.bin",                # FileName
        "c1000",                    # MapName
        "c1000",                    # Location
        0x0010,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("c1000", "c1000_1", "c1000_2", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [152, 5097, 9867, 14435, 23760, 27899, 28334, 28924, 31728, 0, 35775, 0, 39930, 42884, 43451, 45903, 0, 47937, 0, 244, 197, 0, 0],
    )

    BuildStringList((
        "c1000_2",                # 0
    ))

    ChipFrameInfo(152, 0)                                        # 0

    ScpFunction((
        "Function_0_98",           # 00, 0
        "Function_1_13E9",         # 01, 1
        "Function_2_268B",         # 02, 2
        "Function_3_3863",         # 03, 3
        "Function_4_5CD0",         # 04, 4
        "Function_5_6CFB",         # 05, 5
        "Function_6_6EAE",         # 06, 6
        "Function_7_70FC",         # 07, 7
        "Function_8_7BF0",         # 08, 8
        "Function_9_8BBF",         # 09, 9
        "Function_10_9BFA",        # 0A, 10
        "Function_11_A784",        # 0B, 11
        "Function_12_A9BB",        # 0C, 12
        "Function_13_B34F",        # 0D, 13
        "Function_14_BB41",        # 0E, 14
        "Function_15_C5F4",        # 0F, 15
        "Function_16_C73F",        # 10, 16
    ))


    def Function_0_98(): pass

    label("Function_0_98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x1A2, 500)

    ChrTalk(
        0x8,
        "Oh, what a cute boy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How would you like a\x01",
            "pinwheel? If you blow on\x01",
            "it, it's fun, see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "...Are you talking to\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmph. Those aren't rare\x01",
            "at all in the East and\x01",
            "they're mere kid stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*crushed*...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_217")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2C4")

    label("loc_217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_270")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2C4")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2C4")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2C4")

    TalkEnd(0x8)
    SetScenarioFlags(0x1DC, 3)
    ClearChrFlags(0x8, 0x10)
    OP_93(0x8, 0xB4, 0x0)
    Jump("loc_327")

    label("loc_2DB")


    ChrTalk(
        0x8,
        (
            "Ooh... It might be the\x01",
            "first time a kid wasn't\x01",
            "so interested in it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_327")

    Return()

    label("loc_328")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_384")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_384")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3A3")
    OP_AF(0x38)
    Jump("loc_3A5")

    label("loc_3A3")

    OP_AF(0x39)

    label("loc_3A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13E0")

    label("loc_3B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C8")
    Jump("loc_13E0")

    label("loc_3C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_56A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D4")

    ChrTalk(
        0xFE,
        (
            "I'm glad life in Crossbell\x01",
            "city has returned to\x01",
            "normal for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A mysterious tree has appeared\x01",
            "in exchange, however... I'm\x01",
            "sure we'll manage, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I make some new\x01",
            "handicrafts just to\x01",
            "relax?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_565")

    label("loc_4D4")


    ChrTalk(
        0xFE,
        (
            "As for Roy, I intend to\x01",
            "work him hard again\x01",
            "starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A mysterious tree has\x01",
            "appeared. However, I'm\x01",
            "sure we'll manage somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_565")

    Jump("loc_13E0")

    label("loc_56A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_578")
    Jump("loc_13E0")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FD")

    ChrTalk(
        0xFE,
        (
            "Finally, Crossbell has\x01",
            "national independence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I'm truly\x01",
            "witnessing a history-\x01",
            "defining moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E0")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_694")

    ChrTalk(
        0xFE,
        (
            "I made a lot of wooden\x01",
            "tableware for the emergency\x01",
            "feeding in Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're trivial things,\x01",
            "but that's about all I\x01",
            "can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E0")

    label("loc_694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_725")

    ChrTalk(
        0xFE,
        (
            "They say Mainz has been\x01",
            "occupied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm greatly indebted to them\x01",
            "for the handicraft materials\x01",
            "they provide... I'm worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E0")

    label("loc_725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7BD")

    ChrTalk(
        0xFE,
        (
            "It seems like not many\x01",
            "customers are coming\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also gave Roy the day\x01",
            "off and I'm taking my time\x01",
            "making handicrafts alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E0")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_82D")

    ChrTalk(
        0xFE,
        (
            "The pinwheels Roy made\x01",
            "sold little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Weeell, I guess I'm\x01",
            "happy about that too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E0")

    label("loc_82D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_993")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_908")

    ChrTalk(
        0xFE,
        (
            "The pinwheels we sell each\x01",
            "have a slightly different\x01",
            "way of rotating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the "flavor" of\x01",
            "handmade things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I don't think an\x01",
            "amateur could tell the\x01",
            "difference, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_98E")

    label("loc_908")


    ChrTalk(
        0xFE,
        (
            "By the way, Roy's\x01",
            "pinwheels seem saleable,\x01",
            "but only one sold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His fingers have a\x01",
            "natural dexterity. He's\x01",
            "a bright prospect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98E")

    Jump("loc_13E0")

    label("loc_993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8B")

    ChrTalk(
        0xFE,
        (
            "At last, last night I completed\x01",
            "the Orchis Tower model I had\x01",
            "been laboriously making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I put in my\x01",
            "storefront, the tourists\x01",
            "really wanted it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it's not for\x01",
            "sale. I feel sorry for\x01",
            "them, somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B09")

    label("loc_A8B")


    ChrTalk(
        0xFE,
        (
            "In any case, Roy, who\x01",
            "works with perseverance,\x01",
            "is a real help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That might be because\x01",
            "he's the president's\x01",
            "relative.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B09")

    Jump("loc_13E0")

    label("loc_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCD")

    ChrTalk(
        0xFE,
        (
            "Roy decided to work\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As might be expected from the Merchants\x01",
            "Association President's grandchild, he's\x01",
            "diligent. I'm expecting great things from him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C45")

    label("loc_BCD")


    ChrTalk(
        0xFE,
        (
            "I intend to have him\x01",
            "learn many, many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I'm having fun\x01",
            "because it's like I got\x01",
            "myself a disciple.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C45")

    Jump("loc_13E0")

    label("loc_C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_101F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3A")

    ChrTalk(
        0xFE,
        (
            "If you're looking for the beautiful Eastern woman\x01",
            "that was here just now, she walked towards Central\x01",
            "Square after buying many things at the stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her almond-shaped cold\x01",
            "eyes were very\x01",
            "impressive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101A")

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E94")

    ChrTalk(
        0xFE,
        (
            "A beautiful Eastern\x01",
            "woman came here to shop\x01",
            "just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her almond-shaped cold\x01",
            "eyes were very\x01",
            "impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F...Where did she go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She walked towards Central\x01",
            "Square after buying many\x01",
            "things at the stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F(Hey Lloyd, could she\x01",
            "be...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(...Yeah, let's try\x01",
            "looking around.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x1C6, 7)
    Jump("loc_101A")

    label("loc_E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F81")

    ChrTalk(
        0xFE,
        (
            "Maaan, Orchis Tower\x01",
            "really has presence,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, my urge to create is\x01",
            "boiling. I guess I'll try\x01",
            "building a model of the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I made a model of City Hall\x01",
            "before for the Anniversary\x01",
            "Festival, you know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_101A")

    label("loc_F81")


    ChrTalk(
        0xFE,
        (
            "By the way... The grandchild of President\x01",
            "Mors of the Merchants Association came to\x01",
            "have a look at my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. Even the unexpected\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101A")

    Jump("loc_13E0")

    label("loc_101F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1164")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AE")

    ChrTalk(
        0xFE,
        (
            "My handicrafts are all\x01",
            "handmade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Handmade"... As you'd\x01",
            "expect, has a kind of\x01",
            "warmth to it and it's nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_115F")

    label("loc_10AE")


    ChrTalk(
        0xFE,
        (
            "Handmade things take a lot of time\x01",
            "to make and sometimes you end up\x01",
            "hurting yourself too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you'd expect, they\x01",
            "have a kind of warmth to\x01",
            "them and they're nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115F")

    Jump("loc_13E0")

    label("loc_1164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_12DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124F")

    ChrTalk(
        0xFE,
        (
            "All these goods I've\x01",
            "made ended up getting\x01",
            "wet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Nevertheless, my\x01",
            "handicrafts have a proper\x01",
            "waterproof finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it takes time and\x01",
            "effort to make them, you can\x01",
            "expect them to be durable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12D9")

    label("loc_124F")


    ChrTalk(
        0xFE,
        (
            "My handicrafts have a\x01",
            "proper waterproof\x01",
            "finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it takes time and\x01",
            "effort to make them, you can\x01",
            "expect them to be durable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D9")

    Jump("loc_13E0")

    label("loc_12DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_13E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_136E")

    ChrTalk(
        0xFE,
        "Hello, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I deal in various\x01",
            "handmade handicrafts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there's something you\x01",
            "like, please buy it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13E0")

    label("loc_136E")


    ChrTalk(
        0xFE,
        (
            "The most popular of my\x01",
            "items is this\x01",
            ""pinwheel".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the East, it's a toy\x01",
            "said to protect you from\x01",
            "harm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E0")

    Jump("loc_332")

    label("loc_13E5")

    TalkEnd(0xFE)
    Return()

    # Function_0_98 end

    def Function_1_13E9(): pass

    label("Function_1_13E9")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2687")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1448")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1448")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1468")
    OP_AF(0x35)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2682")

    label("loc_1468")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_147C")
    Jump("loc_2682")

    label("loc_147C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2682")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1539")

    ChrTalk(
        0xFE,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fresh Danes is open\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's eat fresh veggies\x01",
            "and overcome this abnormal\x01",
            "situation in good health!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15BF")

    label("loc_1539")


    ChrTalk(
        0xFE,
        (
            "...It seems that Lily has\x01",
            "been coming to look here\x01",
            "frequently for some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I've got\x01",
            "something on my face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BF")

    Jump("loc_2682")

    label("loc_15C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_15D2")
    Jump("loc_2682")

    label("loc_15D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_170E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169F")

    ChrTalk(
        0xFE,
        (
            "The Independent State of\x01",
            "Crossbell, eh...? Man,\x01",
            "that's a joyous thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, that Lily's\x01",
            "wearing a frown for some\x01",
            "reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could she be worried\x01",
            "about something?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1709")

    label("loc_169F")


    ChrTalk(
        0xFE,
        (
            "That Lily... She has a\x01",
            "frown on her face for\x01",
            "some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could she be worried\x01",
            "about something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1709")

    Jump("loc_2682")

    label("loc_170E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180A")

    ChrTalk(
        0xFE,
        (
            "I gave vegetables from my store\x01",
            "for the charity event being held\x01",
            "today at City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm indebted to the\x01",
            "Merchants Association\x01",
            "sponsoring it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want all the people in\x01",
            "the city to feel better\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18B8")

    label("loc_180A")


    ChrTalk(
        0xFE,
        (
            "I'm really grateful to old men of\x01",
            "the Merchants Association who\x01",
            "invited me to be an official member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to do my best to\x01",
            "make everyone in the\x01",
            "city feel better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B8")

    Jump("loc_2682")

    label("loc_18BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_19C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1971")

    ChrTalk(
        0xFE,
        (
            "They say Mainz was occupied,\x01",
            "but... Rumor has it that no ransom\x01",
            "or other demands have come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what that armed\x01",
            "group is trying to\x01",
            "do...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19C2")

    label("loc_1971")


    ChrTalk(
        0xFE,
        (
            "For what purpose could that\x01",
            "armed group or whatever\x01",
            "have occupied Mainz...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C2")

    Jump("loc_2682")

    label("loc_19C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1B7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACB")

    ChrTalk(
        0xFE,
        (
            "The gentlemen who comes to\x01",
            "deliver my vegetables was quite\x01",
            "agitated when he told me this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was a big\x01",
            "disturbance in Armorica\x01",
            "Village yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, he said it was\x01",
            "resolved, but... Hmm, I\x01",
            "wonder what happened.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B77")

    label("loc_1ACB")


    ChrTalk(
        0xFE,
        (
            "I heard there was a big\x01",
            "disturbance at Armorica\x01",
            "Village yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't really get it since the\x01",
            "delivery driver was agitated and\x01",
            "spoke with a local accent...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B77")

    Jump("loc_2682")

    label("loc_1B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5C")

    ChrTalk(
        0xFE,
        (
            "Actually, I hated\x01",
            "vegetables and the like\x01",
            "when I was a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, as I grew up, I\x01",
            "gradually grew to think\x01",
            "they're delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It could be an\x01",
            "unexpected case of likes\x01",
            "and dislikes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CE5")

    label("loc_1C5C")


    ChrTalk(
        0xFE,
        (
            "I greatly hated vegetables,\x01",
            "but before I knew it, I\x01",
            "enjoyed eating them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It could be an\x01",
            "unexpected case of likes\x01",
            "and dislikes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE5")

    Jump("loc_2682")

    label("loc_1CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DBC")

    ChrTalk(
        0xFE,
        (
            "Actually, Lily thought\x01",
            "up my store's name for\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's been supporting me somehow or other ever\x01",
            "since I said I wanted to open my own business...\x01",
            "Hehe, I've got a good childhood friend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2682")

    label("loc_1DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6E")

    ChrTalk(
        0xFE,
        (
            "A truck always comes\x01",
            "from Armorica to deliver\x01",
            "my veggies, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. Maybe it's bad of me\x01",
            "to say this, but was it\x01",
            "always such a nice truck?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EDE")

    label("loc_1E6E")


    ChrTalk(
        0xFE,
        (
            "Armorica Village's orbal\x01",
            "truck... Maybe they\x01",
            "bought a new one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. I'm jealous of\x01",
            "their prosperity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDE")

    Jump("loc_2682")

    label("loc_1EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_203F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F93")

    ChrTalk(
        0xFE,
        (
            "They're going to discuss\x01",
            "mainly economics at the\x01",
            "trade conference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, I don't understand\x01",
            "complicated stuff. Whatever\x01",
            "it is, it is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_203A")

    label("loc_1F93")


    ChrTalk(
        0xFE,
        (
            "Well, whatever the economy, I'll\x01",
            "do business putting customers\x01",
            "first from now on as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't understand\x01",
            "things that are even the\x01",
            "least bit complicated!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_203A")

    Jump("loc_2682")

    label("loc_203F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2250")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2196")

    ChrTalk(
        0xFE,
        (
            "They say the princess of\x01",
            "Liberl Kingdom arrived\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Speaking of Liberl\x01",
            "Kingdom, its "Acerbic\x01",
            "Tomatoes" are famous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm told they were created\x01",
            "by a Liberlian orbal\x01",
            "device maker called ZCF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're an orbment manufacturer and\x01",
            "yet they even grow vegetables...\x01",
            "That's technological power for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_224B")

    label("loc_2196")


    ChrTalk(
        0xFE,
        (
            "The Acerbic Tomato is a\x01",
            "vegetable created at ZCF\x01",
            "not so long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're an orbment manufacturer and\x01",
            "yet they even grow vegetables...\x01",
            "That's technological power for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_224B")

    Jump("loc_2682")

    label("loc_2250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_24A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F5")

    ChrTalk(
        0xFE,
        (
            "I heard this from a\x01",
            "doctor at St. Ursula...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that when you\x01",
            "eat vegetables, fat\x01",
            "absorption slows down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It means that when eating meat,\x01",
            "if you eat it with vegetables,\x01",
            "it becomes harder to get fat.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2364")
    Jump("loc_23ED")

    label("loc_2364")


    ChrTalk(
        0x109,
        "#10105FI-I see...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FThat's useful\x01",
            "information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Girls are especially\x01",
            "passionate about this\x01",
            "sort of thing...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23ED")

    SetScenarioFlags(0x0, 1)
    Jump("loc_24A3")

    label("loc_23F5")


    ChrTalk(
        0xFE,
        (
            "Are you eating your vegetables?\x01",
            "Eating nothing but junk food is\x01",
            "poison for your body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want to live\x01",
            "healthily, as you'd expect,\x01",
            "you've got to eat vegetables.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A3")

    Jump("loc_2682")

    label("loc_24A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_254F")

    ChrTalk(
        0xFE,
        (
            "...Hmm, it looks like leak\x01",
            "in the tent roof. I'll have\x01",
            "to repair it before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Anyhow, what's Lily\x01",
            "been restlessly doing\x01",
            "this whole time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2682")

    label("loc_254F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2614")

    ChrTalk(
        0xFE,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've received plenty of\x01",
            "fresh Armorica vegetables\x01",
            "today as well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you'd expect, Crossbell\x01",
            "produced vegetables are\x01",
            "number one in taste!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2682")

    label("loc_2614")


    ChrTalk(
        0xFE,
        (
            "As you'd expect, Armorica-\x01",
            "grown vegetables are tasty\x01",
            "and I recommend them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come and buy a lot, ok?\x02",
    )

    CloseMessageWindow()

    label("loc_2682")

    Jump("loc_13F6")

    label("loc_2687")

    TalkEnd(0xFE)
    Return()

    # Function_1_13E9 end

    def Function_2_268B(): pass

    label("Function_2_268B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2833")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2788")

    ChrTalk(
        0xFE,
        (
            "That Danes... Eating vegetables\x01",
            "and overcoming this... That's\x01",
            "far too optimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, because Danes\x01",
            "is like that, he can\x01",
            "cheer up everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That part could be\x01",
            "unexpectedly important\x01",
            "for a street vendor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_282E")

    label("loc_2788")


    ChrTalk(
        0xFE,
        (
            "Precisely because Danes\x01",
            "is optimistic, he can\x01",
            "cheer everyone up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When monsters roamed the city,\x01",
            "I too was cheered up by Danes.\x01",
            "Haha. I've got to thank him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_282E")

    Jump("loc_385F")

    label("loc_2833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2841")
    Jump("loc_385F")

    label("loc_2841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29BE")

    ChrTalk(
        0xFE,
        (
            "Goods distribution from\x01",
            "the major powers has\x01",
            "completely stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to President Dieter,\x01",
            "we have emergency reserves to\x01",
            "last at least five years, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A seller of fresh\x01",
            "vegetables should think\x01",
            "about how he does business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...And yet, it seems that Danes\x01",
            "doesn't understand that point. *sigh",\x01",
            "I wish he'd get his act together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A82")

    label("loc_29BE")


    ChrTalk(
        0xFE,
        (
            "According to President Dieter,\x01",
            "we have emergency reserves to\x01",
            "last at least five years, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's going to affect his\x01",
            "business from now on, so I'd like\x01",
            "Danes to get his act together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A82")

    Jump("loc_385F")

    label("loc_2A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF1")

    ChrTalk(
        0xFE,
        (
            "The fact that East Street\x01",
            "received almost no damage\x01",
            "is a silver lining, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2AF1")


    ChrTalk(
        0xFE,
        (
            "Because of the rampage of that\x01",
            "big ogre, it seems Downtown is\x01",
            "in an awful state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're repairing the\x01",
            "damage now, but... I wonder\x01",
            "how long it will take.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_385F")

    label("loc_2B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C0A")

    ChrTalk(
        0xFE,
        (
            "The Mainz incident...\x01",
            "How scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that the CGF will\x01",
            "settle it somehow or\x01",
            "other.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_385F")

    label("loc_2C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2CDD")

    ChrTalk(
        0xFE,
        (
            "Oh jeez. Though I recently plugged\x01",
            "a hole in the tent, it looks like\x01",
            "it's leaking from a different spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Jeez, that Danes. Thinking\x01",
            "about stuff is fine, but I\x01",
            "wish he'd come and help me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_385F")

    label("loc_2CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2EA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DEE")

    ChrTalk(
        0xFE,
        (
            "There might be a lot of people\x01",
            "who hate onions and leeks\x01",
            "because of their smell, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The amount of people who\x01",
            "won't try them isn't\x01",
            "small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they boldly tried them they\x01",
            "might like them, so I'd like\x01",
            "them to challenge themselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E9D")

    label("loc_2DEE")


    ChrTalk(
        0xFE,
        (
            "Disliking a food without trying\x01",
            "it... As you might imagine,\x01",
            "it's a bit of a waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Foods with a smell you dislike\x01",
            "might be quite delicious if\x01",
            "you tried eating them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E9D")

    Jump("loc_385F")

    label("loc_2EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3074")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB3")

    ChrTalk(
        0xFE,
        (
            "Danes... He was trying to start\x01",
            "a business just like that,\x01",
            "without any knowledge at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was I who got the\x01",
            "business permit and\x01",
            "secured a place for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What can I say. I haven't\x01",
            "been able to leave him\x01",
            "alone for a long time now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_306F")

    label("loc_2FB3")


    ChrTalk(
        0xFE,
        (
            "Danes... He was trying to start\x01",
            "a business just like that,\x01",
            "without any knowledge at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I made all sorts of\x01",
            "business preparations for him.\x01",
            "Honestly, what a headache.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306F")

    Jump("loc_385F")

    label("loc_3074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3229")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316C")

    ChrTalk(
        0xFE,
        (
            "Actually, the old gentleman from the\x01",
            "Merchants Association came to ask me\x01",
            "in secret about how Danes was doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Danes turned down an invitation to\x01",
            "become an official member before,\x01",
            "but... It seems he regrets it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3224")

    label("loc_316C")


    ChrTalk(
        0xFE,
        (
            "Hmm. At the time, I also\x01",
            "thought it was a pity that he\x01",
            "refused the invitation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Danes... It's not in his\x01",
            "character to stand on top of\x01",
            "others, so I thought it was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3224")

    Jump("loc_385F")

    label("loc_3229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32AA")

    ChrTalk(
        0xFE,
        (
            "Jeez, that Danes can't\x01",
            "think deeply about\x01",
            "things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, his childhood friend,\x01",
            "have to support him\x01",
            "steadily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_385F")

    label("loc_32AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B8")

    ChrTalk(
        0xFE,
        (
            "When you use Acerbic Tomato\x01",
            "in a dish, it gives quite\x01",
            "an accent to the flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I wouldn't\x01",
            "recommend it at all for\x01",
            "a salad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...After all, it will be bitter\x01",
            "if you just eat them straight. I\x01",
            "guess I slightly dislike them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3462")

    label("loc_33B8")


    ChrTalk(
        0xFE,
        (
            "When you use Acerbic Tomato\x01",
            "in a dish, it gives quite\x01",
            "an accent to the flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it extremely bitter if\x01",
            "eaten raw. It's an ingredient\x01",
            "aimed at professionals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3462")

    Jump("loc_385F")

    label("loc_3467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_363A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3596")

    ChrTalk(
        0xFE,
        (
            "To become a stallholder,\x01",
            "Danes studied vegetables\x01",
            "with all his might.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, having not the slightest sense\x01",
            "of management, he's doing business almost\x01",
            "entirely with only his good personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in a certain sense,\x01",
            "that's Danes' distinctive\x01",
            "characteristic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3635")

    label("loc_3596")


    ChrTalk(
        0xFE,
        (
            "Danes business is honest, but\x01",
            "he doesn't have the slightest\x01",
            "sense of management.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in a certain sense,\x01",
            "that's Danes' distinctive\x01",
            "characteristic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3635")

    Jump("loc_385F")

    label("loc_363A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_37B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3729")

    ChrTalk(
        0xFE,
        (
            "The customer who came\x01",
            "earlier said we two look\x01",
            "like a married couple...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I've always thought of us as mere\x01",
            "childhood friends, I never even thought about\x01",
            "it, but... S-Somehow, I became aware of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37B0")

    label("loc_3729")


    ChrTalk(
        0xFE,
        (
            "A customer said we look\x01",
            "like a married couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, it looks like\x01",
            "Danes doesn't think anything\x01",
            "of it. Jeez, how rude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B0")

    Jump("loc_385F")

    label("loc_37B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_385F")

    ChrTalk(
        0xFE,
        (
            "In Crossbell we rely on\x01",
            "many imported groceries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, because they're delivered\x01",
            "quickly via railroad, they're fresh,\x01",
            "even though they're imported.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_385F")

    TalkEnd(0xFE)
    Return()

    # Function_2_268B end

    def Function_3_3863(): pass

    label("Function_3_3863")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_388C")
    Call(0, 29)
    Return()

    label("loc_388C")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x2, 3)
    Call(2, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_5CC9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC4")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "Talk")
    MenuCmd(1, 1, "Give Fish")
    MenuCmd(1, 1, "Cancel")
    ClearScenarioFlags(0x2, 3)
    Call(2, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F7")
    MenuCmd(3, 1, 0x1)

    label("loc_38F7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3929")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3929")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C8F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3942")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C80")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39AE")
    MenuCmd(1, 1, "Fighter         Time x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A4")
    Call(2, 6)

    label("loc_39A4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_39AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A00")
    MenuCmd(1, 1, "Snow Crab       Mirage x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F6")
    Call(2, 6)

    label("loc_39F6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3A00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A53")
    MenuCmd(1, 1, "Angelfish       Liquids x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A49")
    Call(2, 6)

    label("loc_3A49")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3A53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AA4")
    MenuCmd(1, 1, "Kasagin         Space x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9A")
    Call(2, 6)

    label("loc_3A9A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3AA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AF5")
    MenuCmd(1, 1, "Armorica Carp   Onion x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AEB")
    Call(2, 6)

    label("loc_3AEB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3AF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B48")
    MenuCmd(1, 1, "Tortoise        Powders x4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B3E")
    Call(2, 6)

    label("loc_3B3E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B9A")
    MenuCmd(1, 1, "Tiger Rockfish  Carrot x4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B90")
    Call(2, 6)

    label("loc_3B90")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BED")
    MenuCmd(1, 1, "Rockeater       Liquids x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE3")
    Call(2, 6)

    label("loc_3BE3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3BED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C3C")
    MenuCmd(1, 1, "Rainbow Trout   All x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C32")
    Call(2, 6)

    label("loc_3C32")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C8C")
    MenuCmd(1, 1, "Piranha         Herb x4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C82")
    Call(2, 6)

    label("loc_3C82")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CDC")
    MenuCmd(1, 1, "Carp            Leaf x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD2")
    Call(2, 6)

    label("loc_3CD2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3CDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D2D")
    MenuCmd(1, 1, "Gluttonous Bass Earth x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D23")
    Call(2, 6)

    label("loc_3D23")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D7F")
    MenuCmd(1, 1, "Trout           Potato x4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D75")
    Call(2, 6)

    label("loc_3D75")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DCE")
    MenuCmd(1, 1, "Gladiator       All x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC4")
    Call(2, 6)

    label("loc_3DC4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3DCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E20")
    MenuCmd(1, 1, "Walleye         Water x10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E16")
    Call(2, 6)

    label("loc_3E16")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E71")
    MenuCmd(1, 1, "Salamander      Wind x10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E67")
    Call(2, 6)

    label("loc_3E67")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EC2")
    MenuCmd(1, 1, "Salmon          Berry x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EB8")
    Call(2, 6)

    label("loc_3EB8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3EC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F13")
    MenuCmd(1, 1, "Arowana         Fire x15")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F09")
    Call(2, 6)

    label("loc_3F09")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F6B")
    MenuCmd(1, 1, "Eel             Rare Veggies x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F61")
    Call(2, 6)

    label("loc_3F61")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FBB")
    MenuCmd(1, 1, "Adamantoise     Miso x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB1")
    Call(2, 6)

    label("loc_3FB1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3FBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4013")
    MenuCmd(1, 1, "Queen Crab      Rare Veggies x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4009")
    Call(2, 6)

    label("loc_4009")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4013")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4063")
    MenuCmd(1, 1, "Pirarucu        Miso x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4059")
    Call(2, 6)

    label("loc_4059")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4063")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40B4")
    MenuCmd(1, 1, "Catfish         Dairy x4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40AA")
    Call(2, 6)

    label("loc_40AA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_40B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4106")
    MenuCmd(1, 1, "Gold Salmon     Space x50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40FC")
    Call(2, 6)

    label("loc_40FC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4106")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4159")
    MenuCmd(1, 1, "Pale Salamander Mirage x20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_414F")
    Call(2, 6)

    label("loc_414F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4159")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41A9")
    MenuCmd(1, 1, "Noble Carp      All x10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419F")
    Call(2, 6)

    label("loc_419F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_41A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41FB")
    MenuCmd(1, 1, "Emeraude        Wind x500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F1")
    Call(2, 6)

    label("loc_41F1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_41FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_424E")
    MenuCmd(1, 1, "Tiger Rockeater Earth x500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4244")
    Call(2, 6)

    label("loc_4244")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_424E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42A0")
    MenuCmd(1, 1, "Crimson Eater   Fire x500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4296")
    Call(2, 6)

    label("loc_4296")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_42A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42F3")
    MenuCmd(1, 1, "Bull Dragon     Water x500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E9")
    Call(2, 6)

    label("loc_42E9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_42F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_434B")
    MenuCmd(1, 1, "Giant Pirarucu  TimSpaMira x500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4341")
    Call(2, 6)

    label("loc_4341")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_434B")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_438C")
    Jump("loc_5C7B")

    label("loc_438C")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_441C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4412")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#60ITime Sepith\x01",
            "x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_4412")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_441C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4491")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4487")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#62IMirage\x01",
            "Sepith x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_4487")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4491")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_450B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4501")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Iliquid\x01",
            "ingredients x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4501")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_450B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_457F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4575")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#61ISpace\x01",
            "Sepith x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_4575")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_457F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45ED")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45E3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Ionions x2\x07\x00",
            "?\x02",
        )
    )


    label("loc_45E3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4667")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_465D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Ipowder\x01",
            "ingredients x4\x07\x00",
            "?\x02",
        )
    )


    label("loc_465D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4667")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_46D6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46CC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Icarrots x4\x07\x00",
            "?\x02",
        )
    )


    label("loc_46CC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4750")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4746")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Iliquid\x01",
            "ingredients x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4746")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4750")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47C6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47BC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "all Sepith\x01",
            "element x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_47BC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4832")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4828")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Iherb x4\x07\x00",
            "?\x02",
        )
    )


    label("loc_4828")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4832")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_489E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4894")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Ileaf x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4894")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_489E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4912")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4908")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#56IEarth\x01",
            "Sepith x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_4908")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4912")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4980")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4976")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Ipotato x4\x07\x00",
            "?\x02",
        )
    )


    label("loc_4976")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4980")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49F6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49EC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "all Sepith\x01",
            "element x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_49EC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_49F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A6B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A61")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#57IWater\x01",
            "Sepith x10\x07\x00",
            "?\x02",
        )
    )


    label("loc_4A61")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4ADF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AD5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#59IWind Sepith\x01",
            "x10\x07\x00",
            "?\x02",
        )
    )


    label("loc_4AD5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B4C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B42")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Iberry x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4B42")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BC0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#58IFire Sepith\x01",
            "x15\x07\x00",
            "?\x02",
        )
    )


    label("loc_4BB6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4BC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C36")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C2C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Irare\x01",
            "veggies x3個\x07\x00",
            "?\x02",
        )
    )


    label("loc_4C2C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CA8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C9E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Ibrown rice\x01",
            "x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4C9E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4CA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D1E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D14")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Irare\x01",
            "veggies x3個\x07\x00",
            "?\x02",
        )
    )


    label("loc_4D14")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D8A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D80")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Imiso x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4D80")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4D8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4DF9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DEF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#20Idairies x4\x07\x00",
            "?\x02",
        )
    )


    label("loc_4DEF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4DF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E6E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E64")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#61ISpace\x01",
            "Sepith x50\x07\x00",
            "?\x02",
        )
    )


    label("loc_4E64")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4E6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4EE4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EDA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#62IMirage\x01",
            "Sepith x20\x07\x00",
            "?\x02",
        )
    )


    label("loc_4EDA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F5C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F52")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "all Sepith\x01",
            "elements x10\x07\x00",
            "?\x02",
        )
    )


    label("loc_4F52")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4F5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4FD1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FC7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#59IWind Sepith\x01",
            "x500\x07\x00",
            "?\x02",
        )
    )


    label("loc_4FC7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4FD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5047")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_503D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#56IEarth\x01",
            "Sepith x500\x07\x00",
            "?\x02",
        )
    )


    label("loc_503D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5047")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_50BC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#58IFire Sepith\x01",
            "x500\x07\x00",
            "?\x02",
        )
    )


    label("loc_50B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_50BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5132")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5128")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "#57IWater\x01",
            "Sepith x500\x07\x00",
            "?\x02",
        )
    )


    label("loc_5128")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5132")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_51AE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51A4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this\x01",
            "fish for \x07\x02",
            "Time, Space and\x01",
            "Mirage x500\x07\x00",
            "?\x02",
        )
    )


    label("loc_51A4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_51AE")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Exchange\x01",      # 0
            "Cancel\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C7B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_52E9")

    ChrTalk(
        0xFE,
        (
            "This is an especially magnificent fish.\x01",
            "You might never catch another like\x01",
            "it... Are you really giving it to me?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52E9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C71")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_53DA"),
        (1, "loc_540E"),
        (2, "loc_5444"),
        (3, "loc_5480"),
        (4, "loc_54B4"),
        (5, "loc_54DC"),
        (6, "loc_5521"),
        (7, "loc_5549"),
        (8, "loc_5585"),
        (9, "loc_5663"),
        (10, "loc_568B"),
        (11, "loc_56B3"),
        (12, "loc_56E8"),
        (13, "loc_5710"),
        (14, "loc_57EE"),
        (15, "loc_5824"),
        (16, "loc_5859"),
        (17, "loc_5881"),
        (18, "loc_58B5"),
        (19, "loc_58F1"),
        (20, "loc_5919"),
        (21, "loc_5946"),
        (22, "loc_596E"),
        (23, "loc_59B3"),
        (24, "loc_59EA"),
        (25, "loc_5A22"),
        (26, "loc_5B07"),
        (27, "loc_5B3D"),
        (28, "loc_5B74"),
        (29, "loc_5BAA"),
        (30, "loc_5BE1"),
        (SWITCH_DEFAULT, "loc_5C55"),
    )


    label("loc_53DA")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I Time Sepith x5\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x4, 5)
    SubItemNumber(0x15E, 1)
    Jump("loc_5C55")

    label("loc_540E")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I Mirage Sepith x5\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x6, 5)
    SubItemNumber(0x15F, 1)
    Jump("loc_5C55")

    label("loc_5444")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x13B),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13C),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x136),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x13B, 1)
    AddItemNumber(0x13C, 1)
    AddItemNumber(0x136, 1)
    SubItemNumber(0x160, 1)
    Jump("loc_5C55")

    label("loc_5480")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61ISpace Sepith x5\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x5, 5)
    SubItemNumber(0x161, 1)
    Jump("loc_5C55")

    label("loc_54B4")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x146),
            " x2\x07\x00",
            " obtained.\x02",
        )
    )

    AddItemNumber(0x146, 2)
    SubItemNumber(0x162, 1)
    Jump("loc_5C55")

    label("loc_54DC")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x139),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13A),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13D),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13E),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x139, 1)
    AddItemNumber(0x13A, 1)
    AddItemNumber(0x13D, 1)
    AddItemNumber(0x13E, 1)
    SubItemNumber(0x163, 1)
    Jump("loc_5C55")

    label("loc_5521")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x147),
            " x4\x07\x00",
            " obtained.\x02",
        )
    )

    AddItemNumber(0x147, 4)
    SubItemNumber(0x164, 1)
    Jump("loc_5C55")

    label("loc_5549")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x13B),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13C),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x136),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x13B, 1)
    AddItemNumber(0x13C, 1)
    AddItemNumber(0x136, 1)
    SubItemNumber(0x165, 1)
    Jump("loc_5C55")

    label("loc_5585")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I Earth Sepith  x5\x01\x07\x02",
            "#57I Water Sepith  x5\x01\x07\x02",
            "#58I Fire Sepith   x5\x01\x07\x02",
            "#59I Wind Sepith   x5\x01\x07\x02",
            "#60I Time Sepith   x5\x01\x07\x02",
            "#61I Space Sepith  x5\x01\x07\x02",
            "#62I Mirage Sepith x5\x01\x07\x00",
            "obtained.\x02",
        )
    )

    AddSepith(0x0, 5)
    AddSepith(0x1, 5)
    AddSepith(0x2, 5)
    AddSepith(0x3, 5)
    AddSepith(0x4, 5)
    AddSepith(0x5, 5)
    AddSepith(0x6, 5)
    SubItemNumber(0x166, 1)
    Jump("loc_5C55")

    label("loc_5663")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x138),
            " x4\x07\x00",
            " obtained.\x02",
        )
    )

    AddItemNumber(0x138, 4)
    SubItemNumber(0x167, 1)
    Jump("loc_5C55")

    label("loc_568B")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x137),
            " x3\x07\x00",
            " obtained.\x02",
        )
    )

    AddItemNumber(0x137, 3)
    SubItemNumber(0x168, 1)
    Jump("loc_5C55")

    label("loc_56B3")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I Earth Sepith x5\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x0, 5)
    SubItemNumber(0x169, 1)
    Jump("loc_5C55")

    label("loc_56E8")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x145),
            " x4\x07\x00",
            " obtained.\x02",
        )
    )

    AddItemNumber(0x145, 4)
    SubItemNumber(0x16A, 1)
    Jump("loc_5C55")

    label("loc_5710")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I Earth Sepith  x5\x01\x07\x02",
            "#57I Water Sepith  x5\x01\x07\x02",
            "#58I Fire Sepith   x5\x01\x07\x02",
            "#59I Wind Sepith   x5\x01\x07\x02",
            "#60I Time Sepith   x5\x01\x07\x02",
            "#61I Space Sepith  x5\x01\x07\x02",
            "#62I Mirage Sepith x5\x01\x07\x00",
            "obtained.\x02",
        )
    )

    AddSepith(0x0, 5)
    AddSepith(0x1, 5)
    AddSepith(0x2, 5)
    AddSepith(0x3, 5)
    AddSepith(0x4, 5)
    AddSepith(0x5, 5)
    AddSepith(0x6, 5)
    SubItemNumber(0x16B, 1)
    Jump("loc_5C55")

    label("loc_57EE")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I Water Sepith x10\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x1, 10)
    SubItemNumber(0x16C, 1)
    Jump("loc_5C55")

    label("loc_5824")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I Wind Sepith x10\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x3, 10)
    SubItemNumber(0x16D, 1)
    Jump("loc_5C55")

    label("loc_5859")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x142),
            " x3\x07\x00",
            " obtained.\x02",
        )
    )

    AddItemNumber(0x142, 3)
    SubItemNumber(0x16E, 1)
    Jump("loc_5C55")

    label("loc_5881")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58IFire Sepith x15\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x2, 15)
    SubItemNumber(0x16F, 1)
    Jump("loc_5C55")

    label("loc_58B5")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x143),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x144),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x148),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x143, 1)
    AddItemNumber(0x144, 1)
    AddItemNumber(0x148, 1)
    SubItemNumber(0x170, 1)
    Jump("loc_5C55")

    label("loc_58F1")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x134),
            " x3\x07\x00",
            " obtained.\x02",
        )
    )

    AddItemNumber(0x134, 3)
    SubItemNumber(0x171, 1)
    Jump("loc_5C55")

    label("loc_5919")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x143),
            " obtained.\x02",
        )
    )

    AddItemNumber(0x143, 1)
    AddItemNumber(0x144, 1)
    AddItemNumber(0x148, 1)
    SubItemNumber(0x172, 1)
    Jump("loc_5C55")

    label("loc_5946")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x135),
            " x3\x07\x00",
            " obtained.\x02",
        )
    )

    AddItemNumber(0x135, 3)
    SubItemNumber(0x173, 1)
    Jump("loc_5C55")

    label("loc_596E")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x13F),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x140),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x141),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x149),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x13F, 1)
    AddItemNumber(0x140, 1)
    AddItemNumber(0x141, 1)
    AddItemNumber(0x149, 1)
    SubItemNumber(0x174, 1)
    Jump("loc_5C55")

    label("loc_59B3")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I Space Sepith x50 \x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x5, 50)
    SubItemNumber(0x175, 1)
    Jump("loc_5C55")

    label("loc_59EA")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I Mirage Sepith x20 \x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x6, 20)
    SubItemNumber(0x176, 1)
    Jump("loc_5C55")

    label("loc_5A22")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I Earth Sepith  x10\x01\x07\x02",
            "#57I Water Sepith  x10\x01\x07\x02",
            "#58I Fire Sepith   x10\x01\x07\x02",
            "#59I Wind Sepith   x10\x01\x07\x02",
            "#60I Time Sepith   x10\x01\x07\x02",
            "#61I Space Sepith  x10\x01\x07\x02",
            "#62I Mirage Sepith x10\x01\x07\x00",
            "obtained.\x02",
        )
    )

    AddSepith(0x0, 10)
    AddSepith(0x1, 10)
    AddSepith(0x2, 10)
    AddSepith(0x3, 10)
    AddSepith(0x4, 10)
    AddSepith(0x5, 10)
    AddSepith(0x6, 10)
    SubItemNumber(0x177, 1)
    Jump("loc_5C55")

    label("loc_5B07")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I Wind Sepith x500\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x3, 500)
    SubItemNumber(0x178, 1)
    Jump("loc_5C55")

    label("loc_5B3D")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I Earth Sepith x500\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x0, 500)
    SubItemNumber(0x179, 1)
    Jump("loc_5C55")

    label("loc_5B74")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I Fire Sepith x500\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x2, 500)
    SubItemNumber(0x17A, 1)
    Jump("loc_5C55")

    label("loc_5BAA")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I Water Sepith x500\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x1, 500)
    SubItemNumber(0x17B, 1)
    Jump("loc_5C55")

    label("loc_5BE1")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I Time Sepith   x500\x01\x07\x02",
            "#61I Space Sepith  x500\x01\x07\x02",
            "#62I Mirage Sepith x500\x01\x07\x00",
            "obtained.\x02",
        )
    )

    AddSepith(0x4, 500)
    AddSepith(0x5, 500)
    AddSepith(0x6, 500)
    SubItemNumber(0x17C, 1)
    Jump("loc_5C55")

    label("loc_5C55")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C7B")

    label("loc_5C71")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C7B")

    Jump("loc_3942")

    label("loc_5C80")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CBF")

    label("loc_5C8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CA3")
    Jump("loc_5CBF")

    label("loc_5CA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CBF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(2, 4)

    label("loc_5CBF")

    Jump("loc_38A8")

    label("loc_5CC4")

    Jump("loc_5CCC")

    label("loc_5CC9")

    Call(2, 4)

    label("loc_5CCC")

    TalkEnd(0xB)
    Return()

    # Function_3_3863 end

    def Function_4_5CD0(): pass

    label("Function_4_5CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5E5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DDA")

    ChrTalk(
        0xFE,
        (
            "After something like that happened, I\x01",
            "understand why he's worried, but... For\x01",
            "my husband to come to the store too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. But it's true that I feel safer\x01",
            "with him here. Might as well do business\x01",
            "as a married couple from now on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5E5A")

    label("loc_5DDA")


    ChrTalk(
        0xFE,
        (
            "My husband also lost his\x01",
            "job as a fishmonger\x01",
            "abroad, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Might as well do\x01",
            "business as a married\x01",
            "couple from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E5A")

    Jump("loc_6CFA")

    label("loc_5E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5E6D")
    Jump("loc_6CFA")

    label("loc_5E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F72")

    ChrTalk(
        0xFE,
        (
            "I received a call from my\x01",
            "husband working abroad. He says\x01",
            "he's coming back home soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, they say today will be\x01",
            "the last day before rail service\x01",
            "is suspended for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I wonder if\x01",
            "he'll make it home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5FA5")

    label("loc_5F72")


    ChrTalk(
        0xFE,
        (
            "Aah, my husband... I\x01",
            "hope he comes back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FA5")

    Jump("loc_6CFA")

    label("loc_5FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6055")

    ChrTalk(
        0xFE,
        (
            "Those red-jerseyed kids who made\x01",
            "mischief around here before were\x01",
            "hurt in the recent attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, that's worrisome...\x01",
            "I hope they get better\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CFA")

    label("loc_6055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_60AE")

    ChrTalk(
        0xFE,
        (
            "To think something like\x01",
            "this would happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aah, I'm worried...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CFA")

    label("loc_60AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_61C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_615B")

    ChrTalk(
        0xFE,
        (
            "A bracer came this\x01",
            "morning for an inquiry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where could those bracer\x01",
            "girls have gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where they went\x01",
            "in this bad weather.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_61BD")

    label("loc_615B")


    ChrTalk(
        0xFE,
        (
            "Where could those bracer\x01",
            "girls have gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where they went\x01",
            "in this bad weather.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61BD")

    Jump("loc_6CFA")

    label("loc_61C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6239")

    ChrTalk(
        0xFE,
        (
            "My husband is a\x01",
            "fishmonger working in\x01",
            "the Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if he got some\x01",
            "nice ones.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CFA")

    label("loc_6239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_63E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6351")

    ChrTalk(
        0xFE,
        (
            "When you try to eat\x01",
            "freshwater fish normally,\x01",
            "many smell of mud and earth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why pickling them with\x01",
            "a large quantity of milk takes\x01",
            "away the smell temporarily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Compared to saltwater\x01",
            "fish you can eat quickly,\x01",
            "they're a bit bothersome.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_63E1")

    label("loc_6351")


    ChrTalk(
        0xFE,
        (
            "If you temporarily soak\x01",
            "freshwater fish in milk, you\x01",
            "can take away their smell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should give it a try\x01",
            "when you're cooking at\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63E1")

    Jump("loc_6CFA")

    label("loc_63E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_65C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_654B")

    ChrTalk(
        0xFE,
        (
            "It's been decided that about 10%\x01",
            "of Crossbell's tax revenue will go\x01",
            "each of the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Crossbell becomes independent,\x01",
            "that decision will be nullified\x01",
            "and our lives will become easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Naturally there would be concerns about\x01",
            "the security aspect, but... If possible,\x01",
            "I'd like it to become a reality.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_65BD")

    label("loc_654B")


    ChrTalk(
        0xFE,
        (
            "I agree with Crossbell\x01",
            "independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we were freed from\x01",
            "unfair taxes, our lives\x01",
            "would become easier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65BD")

    Jump("loc_6CFA")

    label("loc_65C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_67C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6739")

    ChrTalk(
        0xFE,
        (
            "The Imperial Chancellor\x01",
            "seems to be quite the\x01",
            "clever man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is said that if you\x01",
            "eat fish, you get\x01",
            "clever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I thought, he must've\x01",
            "grown up eating plenty\x01",
            "of fish.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F...Somehow a strangely\x01",
            "normal image came up to\x01",
            "my mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_67BB")

    label("loc_6739")


    ChrTalk(
        0xFE,
        (
            "It is said that if you\x01",
            "eat fish, you get\x01",
            "clever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even the Imperial\x01",
            "Chancellor must've grown\x01",
            "up eating plenty of fish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67BB")

    Jump("loc_6CFA")

    label("loc_67C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6977")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68CF")

    ChrTalk(
        0xFE,
        (
            "It seems border gate\x01",
            "security has become\x01",
            "pretty strict as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A buyer from the Republic\x01",
            "was grumbling about how long\x01",
            "the entry procedures take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "VIPs entering Crossbell from\x01",
            "the neighboring countries is\x01",
            "something of a big deal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6972")

    label("loc_68CF")


    ChrTalk(
        0xFE,
        (
            "A buyer from the Republic\x01",
            "was grumbling about how long\x01",
            "the entry procedures take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that border\x01",
            "gate security has become\x01",
            "rather strict as well...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6972")

    Jump("loc_6CFA")

    label("loc_6977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6B3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A9A")

    ChrTalk(
        0xFE,
        (
            "The Imperial Fishing Club\x01",
            "is now in the Fisherman's\x01",
            "Guild building, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought something like the\x01",
            "Fisherman's Guild had been there\x01",
            "until a little while ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They almost never socialize\x01",
            "with their neighbors.\x01",
            "They're suspicious, somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6B37")

    label("loc_6A9A")


    ChrTalk(
        0xFE,
        (
            "The Imperial Fishing\x01",
            "Club... They're simply\x01",
            "suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They seem to be a gathering of\x01",
            "fishing lovers, so it seems\x01",
            "they're not bad people, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B37")

    Jump("loc_6CFA")

    label("loc_6B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6BCE")

    ChrTalk(
        0xFE,
        (
            "Hmm. Too bad about the\x01",
            "weather today, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I can't close up shop\x01",
            "if it's just like this,\x01",
            "though. Take a look around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CFA")

    label("loc_6BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6CFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C86")

    ChrTalk(
        0xFE,
        (
            "Would you care for some\x01",
            "fresh fish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way... I haven't\x01",
            "seen any members of the\x01",
            "Fisherman's Guild lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Where did they go, I\x01",
            "wonder?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6CFA")

    label("loc_6C86")


    ChrTalk(
        0xFE,
        (
            "I wonder where the\x01",
            "people of the\x01",
            "Fisherman's Guild went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were funny... I get\x01",
            "lonely not seeing them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CFA")

    Return()

    # Function_4_5CD0 end

    def Function_5_6CFB(): pass

    label("Function_5_6CFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_6D09")
    SetScenarioFlags(0x2, 3)

    label("loc_6D09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_6D17")
    SetScenarioFlags(0x2, 3)

    label("loc_6D17")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_6D25")
    SetScenarioFlags(0x2, 3)

    label("loc_6D25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_6D33")
    SetScenarioFlags(0x2, 3)

    label("loc_6D33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_6D41")
    SetScenarioFlags(0x2, 3)

    label("loc_6D41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_6D4F")
    SetScenarioFlags(0x2, 3)

    label("loc_6D4F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_6D5D")
    SetScenarioFlags(0x2, 3)

    label("loc_6D5D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_6D6B")
    SetScenarioFlags(0x2, 3)

    label("loc_6D6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_6D79")
    SetScenarioFlags(0x2, 3)

    label("loc_6D79")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_6D87")
    SetScenarioFlags(0x2, 3)

    label("loc_6D87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_6D95")
    SetScenarioFlags(0x2, 3)

    label("loc_6D95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_6DA3")
    SetScenarioFlags(0x2, 3)

    label("loc_6DA3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_6DB1")
    SetScenarioFlags(0x2, 3)

    label("loc_6DB1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_6DBF")
    SetScenarioFlags(0x2, 3)

    label("loc_6DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_6DCD")
    SetScenarioFlags(0x2, 3)

    label("loc_6DCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_6DDB")
    SetScenarioFlags(0x2, 3)

    label("loc_6DDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_6DE9")
    SetScenarioFlags(0x2, 3)

    label("loc_6DE9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_6DF7")
    SetScenarioFlags(0x2, 3)

    label("loc_6DF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_6E05")
    SetScenarioFlags(0x2, 3)

    label("loc_6E05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_6E13")
    SetScenarioFlags(0x2, 3)

    label("loc_6E13")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_6E21")
    SetScenarioFlags(0x2, 3)

    label("loc_6E21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_6E2F")
    SetScenarioFlags(0x2, 3)

    label("loc_6E2F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_6E3D")
    SetScenarioFlags(0x2, 3)

    label("loc_6E3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_6E4B")
    SetScenarioFlags(0x2, 3)

    label("loc_6E4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_END)), "loc_6E59")
    SetScenarioFlags(0x2, 3)

    label("loc_6E59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_END)), "loc_6E67")
    SetScenarioFlags(0x2, 3)

    label("loc_6E67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_END)), "loc_6E75")
    SetScenarioFlags(0x2, 3)

    label("loc_6E75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_END)), "loc_6E83")
    SetScenarioFlags(0x2, 3)

    label("loc_6E83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_END)), "loc_6E91")
    SetScenarioFlags(0x2, 3)

    label("loc_6E91")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_END)), "loc_6E9F")
    SetScenarioFlags(0x2, 3)

    label("loc_6E9F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_END)), "loc_6EAD")
    SetScenarioFlags(0x2, 3)

    label("loc_6EAD")

    Return()

    # Function_5_6CFB end

    def Function_6_6EAE(): pass

    label("Function_6_6EAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EC1")
    MenuCmd(3, 1, 0x0)

    label("loc_6EC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6ED4")
    MenuCmd(3, 1, 0x1)

    label("loc_6ED4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EE7")
    MenuCmd(3, 1, 0x2)

    label("loc_6EE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EFA")
    MenuCmd(3, 1, 0x3)

    label("loc_6EFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F0D")
    MenuCmd(3, 1, 0x4)

    label("loc_6F0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F20")
    MenuCmd(3, 1, 0x5)

    label("loc_6F20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F33")
    MenuCmd(3, 1, 0x6)

    label("loc_6F33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F46")
    MenuCmd(3, 1, 0x7)

    label("loc_6F46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F59")
    MenuCmd(3, 1, 0x8)

    label("loc_6F59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F6C")
    MenuCmd(3, 1, 0x9)

    label("loc_6F6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F7F")
    MenuCmd(3, 1, 0xA)

    label("loc_6F7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F92")
    MenuCmd(3, 1, 0xB)

    label("loc_6F92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FA5")
    MenuCmd(3, 1, 0xC)

    label("loc_6FA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FB8")
    MenuCmd(3, 1, 0xD)

    label("loc_6FB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FCB")
    MenuCmd(3, 1, 0xE)

    label("loc_6FCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FDE")
    MenuCmd(3, 1, 0xF)

    label("loc_6FDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FF1")
    MenuCmd(3, 1, 0x10)

    label("loc_6FF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7004")
    MenuCmd(3, 1, 0x11)

    label("loc_7004")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7017")
    MenuCmd(3, 1, 0x12)

    label("loc_7017")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_702A")
    MenuCmd(3, 1, 0x13)

    label("loc_702A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_703D")
    MenuCmd(3, 1, 0x14)

    label("loc_703D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7050")
    MenuCmd(3, 1, 0x15)

    label("loc_7050")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7063")
    MenuCmd(3, 1, 0x16)

    label("loc_7063")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7076")
    MenuCmd(3, 1, 0x17)

    label("loc_7076")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7089")
    MenuCmd(3, 1, 0x18)

    label("loc_7089")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_709C")
    MenuCmd(3, 1, 0x19)

    label("loc_709C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70AF")
    MenuCmd(3, 1, 0x1A)

    label("loc_70AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70C2")
    MenuCmd(3, 1, 0x1B)

    label("loc_70C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70D5")
    MenuCmd(3, 1, 0x1C)

    label("loc_70D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70E8")
    MenuCmd(3, 1, 0x1D)

    label("loc_70E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70FB")
    MenuCmd(3, 1, 0x1E)

    label("loc_70FB")

    Return()

    # Function_6_6EAE end

    def Function_7_70FC(): pass

    label("Function_7_70FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71BB")

    ChrTalk(
        0xFE,
        (
            "They say President\x01",
            "Dieter's been arrested!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a nation's leader to\x01",
            "be arrested is\x01",
            "unprecedented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what will\x01",
            "become of Crossbell\x01",
            "State...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_722C")

    label("loc_71BB")


    ChrTalk(
        0xFE,
        (
            "For a nation's leader to\x01",
            "be arrested is\x01",
            "unprecedented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what will\x01",
            "become of Crossbell\x01",
            "State...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_722C")

    Jump("loc_7BEC")

    label("loc_7231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_723F")
    Jump("loc_7BEC")

    label("loc_723F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_72E0")

    ChrTalk(
        0xFE,
        (
            "I too saw the Mayor...\x01",
            "no, President Dieter's\x01",
            "speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This being the situation,\x01",
            "I'd like him to do his best\x01",
            "to realize the independence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BEC")

    label("loc_72E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_73A6")

    ChrTalk(
        0xFE,
        (
            "It looks like the big\x01",
            "bell in Central Square\x01",
            "has been stolen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There aren't even any concrete\x01",
            "rumors about why something\x01",
            "like that was stolen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, it's really\x01",
            "weird.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BEC")

    label("loc_73A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_744A")

    ChrTalk(
        0xFE,
        (
            "I'm worried about the\x01",
            "mining town, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems the CGF is moving to\x01",
            "resolve the situation, but I\x01",
            "wonder if they'll be all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BEC")

    label("loc_744A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_74C4")

    ChrTalk(
        0xFE,
        (
            "I was really shocked by\x01",
            "yesterday's train\x01",
            "accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, I'm glad it was\x01",
            "repaired so quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BEC")

    label("loc_74C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7552")

    ChrTalk(
        0xFE,
        (
            "The Republican passenger\x01",
            "bus passed through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Weird... That bus should\x01",
            "run only up to the east\x01",
            "entrance bus stop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BEC")

    label("loc_7552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_76A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_762B")

    ChrTalk(
        0xFE,
        (
            "It seems the independence\x01",
            "proposal was an idea the mayor\x01",
            "was mulling over, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what Chairman\x01",
            "MacDowell thinks of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd really like to hear\x01",
            "his opinion about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_76A4")

    label("loc_762B")


    ChrTalk(
        0xFE,
        (
            "I am still undecided\x01",
            "about how to vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd really like to hear\x01",
            "Chairman MacDowell's\x01",
            "opinion about it as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76A4")

    Jump("loc_7BEC")

    label("loc_76A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_785D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77C1")

    ChrTalk(
        0xFE,
        (
            "As you can imagine, even an\x01",
            "old lady like me was surprised\x01",
            "by the independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I think it's good\x01",
            "that Crossbell is asking for\x01",
            "more from the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever they may say,\x01",
            "we're the continent's\x01",
            "leading trade city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7858")

    label("loc_77C1")


    ChrTalk(
        0xFE,
        (
            "I think it's good that\x01",
            "Crossbell is asking for more\x01",
            "from foreign countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever they may say,\x01",
            "we're the continent's\x01",
            "leading trade city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7858")

    Jump("loc_7BEC")

    label("loc_785D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_78F8")

    ChrTalk(
        0xFE,
        (
            "Today is finally the day\x01",
            "of the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really want Mayor Dieter\x01",
            "and the others to do their\x01",
            "best for Crossbell's sake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BEC")

    label("loc_78F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7962")

    ChrTalk(
        0xFE,
        (
            "The unveiling of Orchis\x01",
            "Tower was amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was so surprised, my\x01",
            "knees gave out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BEC")

    label("loc_7962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_79D4")

    ChrTalk(
        0xFE,
        (
            "You see police on\x01",
            "security detail often\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The city feels busier\x01",
            "than usual, somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BEC")

    label("loc_79D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7A53")

    ChrTalk(
        0xFE,
        (
            "Hum hum huuum♪ I've\x01",
            "always loved the rain,\x01",
            "ever since I was a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Am I a bit immature,\x01",
            "perhaps?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BEC")

    label("loc_7A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B52")

    ChrTalk(
        0xFE,
        (
            "It seems a trade\x01",
            "conference is going to\x01",
            "be held at month end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only the Empire and Republic\x01",
            "bigwigs are invited, but also those\x01",
            "of Liberl and Remiferia, they say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It seems that it's\x01",
            "going to be a big event.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7BEC")

    label("loc_7B52")


    ChrTalk(
        0xFE,
        (
            "It seems a trade\x01",
            "conference is going to\x01",
            "be held at month end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Many big wigs are will come,\x01",
            "and so it appears that it's\x01",
            "going to be a big event.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BEC")

    TalkEnd(0xFE)
    Return()

    # Function_7_70FC end

    def Function_8_7BF0(): pass

    label("Function_8_7BF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7CFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CB1")

    ChrTalk(
        0xFE,
        (
            "Even if President Dieter\x01",
            "disappears, there's always\x01",
            "Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure the chairman will be\x01",
            "able to restore the situation\x01",
            "in a way or another.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7CFA")

    label("loc_7CB1")


    ChrTalk(
        0xFE,
        (
            "I'm sure Chairman\x01",
            "MacDowell will quell even\x01",
            "this situation somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CFA")

    Jump("loc_8BBB")

    label("loc_7CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7D0D")
    Jump("loc_8BBB")

    label("loc_7D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7EAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DF3")

    ChrTalk(
        0xFE,
        (
            "To think Sir Arios the\x01",
            "bracer was appointed\x01",
            "Secretary of Defense...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, if you consider his\x01",
            "achievements, he might be\x01",
            "the right man for the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected of Sir\x01",
            "Dieter's judgment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7EA7")

    label("loc_7DF3")


    ChrTalk(
        0xFE,
        (
            "When you think about Sir Arios'\x01",
            "achievements, appointing him as Secretary\x01",
            "of Defense was the right thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, one could say\x01",
            "he's Crossbell's\x01",
            "guardian deity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EA7")

    Jump("loc_8BBB")

    label("loc_7EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FBD")

    ChrTalk(
        0xFE,
        (
            "Who would've thought an\x01",
            "incident like that would\x01",
            "happen in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't get the cries of that giant\x01",
            "demonlike monster I heard coming\x01",
            "from Downtown out of my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... I'm not going\x01",
            "to be able to sleep\x01",
            "tonight either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8063")

    label("loc_7FBD")


    ChrTalk(
        0xFE,
        (
            "I can't get the cries of that\x01",
            "giant demonlike monster I heard\x01",
            "during the attack out of my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... I'm not going\x01",
            "to be able to sleep\x01",
            "tonight either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8063")

    Jump("loc_8BBB")

    label("loc_8068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_81DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8151")

    ChrTalk(
        0xFE,
        (
            "The occupation of Mainz,\x01",
            "eh? Things have gotten\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of the mayor's independence\x01",
            "proposal, we can't expect help from\x01",
            "Empire or Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I wonder what's\x01",
            "going to happen...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_81D8")

    label("loc_8151")


    ChrTalk(
        0xFE,
        (
            "For the mayor's independence\x01",
            "proposal, we can't expect\x01",
            "help from Empire or Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I wonder what's\x01",
            "going to happen...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81D8")

    Jump("loc_8BBB")

    label("loc_81DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_81EB")
    Jump("loc_8BBB")

    label("loc_81EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8269")

    ChrTalk(
        0xFE,
        (
            "It appears that\x01",
            "ambulances passed\x01",
            "through Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear me... Could an\x01",
            "accident have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BBB")

    label("loc_8269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_847A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_838A")

    ChrTalk(
        0xFE,
        (
            "This referendum... There's\x01",
            "much talk about it even\x01",
            "among my acquaintances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, you can't get\x01",
            "swept up by the opinions\x01",
            "surrounding you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter who it is, they mustn't\x01",
            "consider it someone else's problem.\x01",
            "You must think this over yourselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8475")

    label("loc_838A")


    ChrTalk(
        0xFE,
        (
            "Each person must think about it carefully.\x01",
            "If it's not a vote cast with your own\x01",
            "will, then there's no meaning in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter who it is, they mustn't\x01",
            "consider it someone else's problem.\x01",
            "You must think this over yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8475")

    Jump("loc_8BBB")

    label("loc_847A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8652")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85BB")

    ChrTalk(
        0xFE,
        (
            "As someone who knows this land's\x01",
            "history, I wish for it to win its\x01",
            "independence by any possible means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it is a fact that peace is\x01",
            "guaranteed because we're substantially under\x01",
            "the control of the Empire and Republic....\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... I seems I need to\x01",
            "think this over\x01",
            "carefully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_864D")

    label("loc_85BB")


    ChrTalk(
        0xFE,
        (
            "Enjoying peace as a subordinate\x01",
            "state? Or letting go of that,\x01",
            "becoming independent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... I seems I need to\x01",
            "think this over\x01",
            "carefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_864D")

    Jump("loc_8BBB")

    label("loc_8652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_87F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8758")

    ChrTalk(
        0xFE,
        (
            "It appears the Orchis Tower\x01",
            "perimeter has been sealed\x01",
            "off since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too wanted to see the\x01",
            "visiting heads of state\x01",
            "with my own eyes, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you think about\x01",
            "security, perhaps it\x01",
            "couldn't have been helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_87EC")

    label("loc_8758")


    ChrTalk(
        0xFE,
        (
            "It seems the Orchis Tower\x01",
            "perimeter has been sealed\x01",
            "off since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanted to see the\x01",
            "visiting heads of state\x01",
            "with my own eyes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87EC")

    Jump("loc_8BBB")

    label("loc_87F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F3")

    ChrTalk(
        0xFE,
        (
            "President Rocksmith's\x01",
            "limousine passed through\x01",
            "this street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected of a President's\x01",
            "car, it had a gorgeous white\x01",
            "and gold body frame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You probably wouldn't find\x01",
            "a similar car even if you\x01",
            "searched the continent.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_897F")

    label("loc_88F3")


    ChrTalk(
        0xFE,
        (
            "President Rocksmith's\x01",
            "limousine was indeed\x01",
            "gorgeous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You probably wouldn't find\x01",
            "a similar car even if you\x01",
            "searched the continent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_897F")

    Jump("loc_8BBB")

    label("loc_8984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8A38")

    ChrTalk(
        0xFE,
        (
            "They say the visiting heads\x01",
            "of state are coming to\x01",
            "Crossbell in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it's a rare opportunity,\x01",
            "I hope to be able to see them\x01",
            "with my own eyes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BBB")

    label("loc_8A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8A46")
    Jump("loc_8BBB")

    label("loc_8A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8BBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B3D")

    ChrTalk(
        0xFE,
        (
            "Dieter, the new mayor, is proving to be a\x01",
            "hard-working governor and is also cooperating\x01",
            "nicely with Chairman MacDowell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the past, cooperation between\x01",
            "the two was unthinkable. Hoho,\x01",
            "what a wonderful thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8BBB")

    label("loc_8B3D")


    ChrTalk(
        0xFE,
        (
            "New Mayor Dieter has\x01",
            "always displayed his\x01",
            "ability as IBC president.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho, I truly am looking\x01",
            "forward to the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BBB")

    TalkEnd(0xFE)
    Return()

    # Function_8_7BF0 end

    def Function_9_8BBF(): pass

    label("Function_9_8BBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CFA")
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xFE,
        (
            "The arrest of the President, an ominous\x01",
            "pale blue tree appearing... I feel like\x01",
            "many different things are happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if we'll be able\x01",
            "to fully go back to our\x01",
            "former daily lives...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        "Bro, what's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    ChrTalk(
        0xFE,
        "Haha, it's nothing.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_93(0xF, 0x10E, 0x0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_8D8B")

    label("loc_8CFA")


    ChrTalk(
        0xFE,
        (
            "...Well, whatever it is,\x01",
            "it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The most important thing to me is\x01",
            "protecting Meiling... As long as I\x01",
            "don't forget that, it'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D8B")

    Jump("loc_9BF6")

    label("loc_8D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8D9E")
    Jump("loc_9BF6")

    label("loc_8D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8F5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E9B")

    ChrTalk(
        0xFE,
        (
            "Having the eyes of\x01",
            "Empire and Republic on\x01",
            "us is indeed scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However... it's for Crossbell's\x01",
            "sake. We citizens must prepare\x01",
            "for the worst as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, no matter what\x01",
            "happens, I'll at least\x01",
            "protect Meiling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8F56")

    label("loc_8E9B")


    ChrTalk(
        0xFE,
        (
            "When I told Mr. Cronk I\x01",
            "wanted to have Meiling near\x01",
            "me, he gave me a pleasant ok.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad he's so understanding. I\x01",
            "feel relieved that she's somewhere\x01",
            "I can keep an eye on her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F56")

    Jump("loc_9BF6")

    label("loc_8F5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8F69")
    Jump("loc_9BF6")

    label("loc_8F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_90C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_902F")

    ChrTalk(
        0xFE,
        (
            "They say that an armed\x01",
            "group has appeared in\x01",
            "Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone like them\x01",
            "showing up in town... It\x01",
            "must be dreadful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that the CGF\x01",
            "kicks them out fast.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_90C2")

    label("loc_902F")


    ChrTalk(
        0xFE,
        (
            "What's wrong with Meiling I\x01",
            "wonder... She seems troubled\x01",
            "lately. I'm worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll finish work\x01",
            "early today and go home\x01",
            "with her...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90C2")

    Jump("loc_9BF6")

    label("loc_90C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_92A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9202")

    ChrTalk(
        0xFE,
        (
            "I gave the failed\x01",
            "pinwheels I made at my\x01",
            "part-time job to Meiling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, she wanted to play\x01",
            "with them today and wouldn't\x01",
            "listen to anything I said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, I don't want\x01",
            "to walk around on a\x01",
            "rainy day, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, Meiling is\x01",
            "having fun, so I guess\x01",
            "it's all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_929C")

    label("loc_9202")


    ChrTalk(
        0xFE,
        (
            "However, to think she could\x01",
            "be that happy with such\x01",
            "junky failed products...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Next time, I'll have\x01",
            "to give her one that's\x01",
            "been properly made.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_929C")

    Jump("loc_9BF6")

    label("loc_92A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9323")

    ChrTalk(
        0xFE,
        (
            "Hmm... The pinwheels I\x01",
            "make aren't selling at\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wait, what!? Just\x01",
            "when did they sell!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9333")

    label("loc_9323")


    ChrTalk(
        0xFE,
        "*agape*...\x02",
    )

    CloseMessageWindow()

    label("loc_9333")

    Jump("loc_9BF6")

    label("loc_9338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_93E3")

    ChrTalk(
        0xFE,
        (
            "I finally got one of those\x01",
            "pinwheels I worked so hard\x01",
            "to make put up for sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having something you made\x01",
            "yourself for sale... It's\x01",
            "a nice feeling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BF6")

    label("loc_93E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9527")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94BE")

    ChrTalk(
        0xFE,
        (
            "Mr. Cronk makes such\x01",
            "incredible models...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had confidence in my dexterity,\x01",
            "but until I've done nothing but\x01",
            "fail at making pinwheels...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm losing\x01",
            "confidence in myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9522")

    label("loc_94BE")


    ChrTalk(
        0xFE,
        (
            "In any case, I'll work\x01",
            "on other odd jobs today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew... Earning mira by\x01",
            "working is tough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9522")

    Jump("loc_9BF6")

    label("loc_9527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9640")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95D4")

    ChrTalk(
        0xFE,
        (
            "When I asked Mr. Cronk,\x01",
            "he let me work here way\x01",
            "too quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hmm... Since I was looking\x01",
            "for a stall job anyway,\x01",
            "that's good, I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_963B")

    label("loc_95D4")


    ChrTalk(
        0xFE,
        (
            "How to make simple\x01",
            "handicrafts, mira\x01",
            "management...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to learn the job\x01",
            "little by little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_963B")

    Jump("loc_9BF6")

    label("loc_9640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9780")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9710")

    ChrTalk(
        0xFE,
        "Hmm, handicrafts, eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm quite skilled with my hands.\x01",
            "Maybe I'm unexpectedly suited\x01",
            "for an artisinal job like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, I wonder if\x01",
            "he'll hire me...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xF, 0x10)
    Jump("loc_977B")

    label("loc_9710")


    ChrTalk(
        0xFE,
        (
            "If I made these of\x01",
            "pinwheels, even Meiling\x01",
            "might be happy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-All right... I'll try\x01",
            "asking him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_977B")

    Jump("loc_9BF6")

    label("loc_9780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9941")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98A2")
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xFE,
        (
            "*sigh*, I've reached an\x01",
            "impasse in looking for a\x01",
            "job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Roy, why don't you try\x01",
            "asking all the stores\x01",
            "over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "M-Moron. If I did a street\x01",
            "stall job, I'd stand out\x01",
            "and it'd be embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want an easier job I\x01",
            "can do indoors.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xF, 0x10)
    Jump("loc_993C")

    label("loc_98A2")


    ChrTalk(
        0xFE,
        (
            "Hmm, street stalls,\x01",
            "eh...? They're not in my\x01",
            "character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I tried almost every\x01",
            "kind of work I think of aside\x01",
            "from street stalls already.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_993C")

    Jump("loc_9BF6")

    label("loc_9941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_99CE")

    ChrTalk(
        0xFE,
        (
            "I'm going shopping and\x01",
            "for a walk with Meiling\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Boy oh boy... Kids have\x01",
            "a lot of energy even if\x01",
            "it is raining.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BF6")

    label("loc_99CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AC4")

    ChrTalk(
        0xFE,
        (
            "A redheaded man suddenly\x01",
            "bumped into me just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Saying "Worry more, that's\x01",
            "why you're young!", he\x01",
            "walked to Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...H-He looked even more\x01",
            "irresponsible than me\x01",
            "for some reason.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9B45")

    label("loc_9AC4")


    ChrTalk(
        0xFE,
        (
            "That redhead from\x01",
            "before? He walked to\x01",
            "Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...H-He looked even more\x01",
            "irresponsible than me\x01",
            "for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B45")

    Jump("loc_9BF6")

    label("loc_9B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BDA")

    ChrTalk(
        0xFE,
        (
            "A little while ago I\x01",
            "started looking for a\x01",
            "job, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I can't find any\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've already lost heart.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9BF6")

    label("loc_9BDA")


    ChrTalk(
        0xFE,
        "I can't find any work.\x02",
    )

    CloseMessageWindow()

    label("loc_9BF6")

    TalkEnd(0xFE)
    Return()

    # Function_9_8BBF end

    def Function_10_9BFA(): pass

    label("Function_10_9BFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9C92")

    ChrTalk(
        0xFE,
        (
            "Roy looks depressed,\x01",
            "like he's thinking about\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Enough with the difficult\x01",
            "stuff. Come play with\x01",
            "Meiling already☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A780")

    label("loc_9C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_9CA0")
    Jump("loc_A780")

    label("loc_9CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9D8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D33")

    ChrTalk(
        0xFE,
        (
            "Today, Roy called me to\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ehehe, there's even three\x01",
            ""whirly whirls" made by my\x01",
            "brother. I hope they sell!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9D85")

    label("loc_9D33")


    ChrTalk(
        0xFE,
        (
            "He says if Meiling\x01",
            "helps, she can get\x01",
            ""whirly whirls".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ehehe, how fun♪\x02",
    )

    CloseMessageWindow()

    label("loc_9D85")

    Jump("loc_A780")

    label("loc_9D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9E59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DFD")

    ChrTalk(
        0xFE,
        (
            "Grandpa and Roy went\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess Meiling will\x01",
            "play at Grandma's today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9E54")

    label("loc_9DFD")


    ChrTalk(
        0xFE,
        (
            "Grandpa and big bro are\x01",
            "doing kya... kyar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kyarity? That's what\x01",
            "they said.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E54")

    Jump("loc_A780")

    label("loc_9E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9F11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EF4")

    ChrTalk(
        0xFE,
        (
            "Next year, Meiling will\x01",
            "go to "sandei skul".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why, even if\x01",
            "Meiling is lonely,\x01",
            "she'll cheer for Roy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_9F0C")

    label("loc_9EF4")


    ChrTalk(
        0xFE,
        "Do your best, Roy!\x02",
    )

    CloseMessageWindow()

    label("loc_9F0C")

    Jump("loc_A780")

    label("loc_9F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9FA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F6C")

    ChrTalk(
        0xFE,
        (
            "This is a whirly whirl\x01",
            "Roy made!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It spins and spins♪\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9F9C")

    label("loc_9F6C")


    ChrTalk(
        0xFE,
        (
            "Roy made this whirly\x01",
            "whirl! It's amazing♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F9C")

    Jump("loc_A780")

    label("loc_9FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9FED")

    ChrTalk(
        0xFE,
        (
            "Grandpa has a gloomy\x01",
            "look on his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Boring...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A780")

    label("loc_9FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A0C8")
    OP_4B(0x14, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A069")

    ChrTalk(
        0xFE,
        "Grampa, beard beard☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*pull, puuull*♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Ow ow ow ow... Now now,\x01",
            "don't pull it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A0BF")

    label("loc_A069")


    ChrTalk(
        0xFE,
        "*pull, puuull*♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "M-Meiling, you're\x01",
            "stronger than you\x01",
            "look... Ow ow ow ow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0BF")

    OP_4C(0x14, 0xFF)
    Jump("loc_A780")

    label("loc_A0C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A159")

    ChrTalk(
        0xFE,
        (
            "It looks like Roy is\x01",
            "working with all his\x01",
            "might.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd wish he played with\x01",
            "Meiling too, though...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrFlags(0xFE, 0x10)
    Jump("loc_A18E")

    label("loc_A159")


    ChrTalk(
        0xFE,
        (
            "Roy, Meiling wants to be\x01",
            "with you too! ...*sob*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A18E")

    Jump("loc_A780")

    label("loc_A193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A206")

    ChrTalk(
        0xFE,
        (
            "It seems Roy is working\x01",
            "at that whirly whirl\x01",
            "store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm happy he found a\x01",
            "job!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A234")

    label("loc_A206")


    ChrTalk(
        0xFE,
        (
            "I'm happy, but... a\x01",
            "little sad. ...*sob*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A234")

    Jump("loc_A780")

    label("loc_A239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A3B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A327")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "The spinning whirly\x01",
            "whirls are fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Spin spin spin spin...♪\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x10)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xF, 0x10, 0)

    ChrTalk(
        0xF,
        (
            "Whoa, Meiling!? Aren't\x01",
            "you dizzy!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Spin, spin, dizzy,\x01",
            "dizzy...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Jump("loc_A3AF")

    label("loc_A327")

    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x10, 0)
    TurnDirection(0x10, 0xF, 0)

    ChrTalk(
        0xF,
        "A-Are you ok, Meiling?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(*wobble wobble*) I'm\x01",
            "aaaokaay...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You're really not, are\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)

    label("loc_A3AF")

    Jump("loc_A780")

    label("loc_A3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A4E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A488")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Roy, you haven't played\x01",
            "with me at all lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Find a job fast and play\x01",
            "with Meiling!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "*sigh*, it'd be nice if\x01",
            "it was that easy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_A4DE")

    label("loc_A488")


    ChrTalk(
        0xFE,
        (
            "Meiling will help Roy\x01",
            "find a job too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When we find it, let's\x01",
            "play together!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4DE")

    Jump("loc_A780")

    label("loc_A4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A60B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5AA")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "*dum de dum...*♪ Uhhm,\x01",
            "what a good smell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hey, Meiling, you can't\x01",
            "open the bag yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The freshly baked bread\x01",
            "will get wet, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yup☆\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_A606")

    label("loc_A5AA")


    ChrTalk(
        0xFE,
        (
            "Meiling went with Roy to\x01",
            "shop at the bakery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhhm, it's so warm and\x01",
            "smells good☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A606")

    Jump("loc_A780")

    label("loc_A60B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A780")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A67E")

    ChrTalk(
        0xFE,
        (
            "A redheaded man rubbed\x01",
            "against Roy's shoulder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meiling wants to do that\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A780")

    label("loc_A67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A72D")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        "Cheer up, big brother!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you can't find a\x01",
            "job, Meiling is at your\x01",
            "side!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "M-Meiliiing... It's just\x01",
            "you. You're my only\x01",
            "ally.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xF, 0xFF)
    Jump("loc_A780")

    label("loc_A72D")


    ChrTalk(
        0xFE,
        (
            "Roy is feeling down, not\x01",
            "having a job and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meiling must console\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A780")

    TalkEnd(0xFE)
    Return()

    # Function_10_9BFA end

    def Function_11_A784(): pass

    label("Function_11_A784")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A807")

    ChrTalk(
        0xFE,
        (
            "Many ambulances have\x01",
            "been coming and going\x01",
            "for some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I've got a bad\x01",
            "feeling about this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9B7")

    label("loc_A807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A9B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A913")

    ChrTalk(
        0xFE,
        (
            "Roy, my grandchild, has finally\x01",
            "begun working. And in the\x01",
            "street stall quarter, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too worked there when I\x01",
            "was young. For some reason,\x01",
            "it's deeply moving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at least he's\x01",
            "doing his best. I'll\x01",
            "watch over him as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A9B7")

    label("loc_A913")


    ChrTalk(
        0xFE,
        (
            "Because he took the day off,\x01",
            "I'm in charge of taking care\x01",
            "of Meiling today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see, since it's a\x01",
            "rare opportunity, I guess\x01",
            "I'll play as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9B7")

    TalkEnd(0xFE)
    Return()

    # Function_11_A784 end

    def Function_12_A9BB(): pass

    label("Function_12_A9BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AB50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAB6")

    ChrTalk(
        0xFE,
        (
            "The men in my home have\x01",
            "become nicer to me\x01",
            "lately for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I wonder how many years\x01",
            "have passed since I first\x01",
            "went shopping with Gilles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though it's a time\x01",
            "like this, I'm enjoying\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AB4B")

    label("loc_AAB6")


    ChrTalk(
        0xFE,
        (
            "Haha. I wonder how many years\x01",
            "have passed since I first\x01",
            "went shopping with Gilles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though it's a time\x01",
            "like this, I'm enjoying\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB4B")

    Jump("loc_B34B")

    label("loc_AB50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AB5E")
    Jump("loc_B34B")

    label("loc_AB5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AB6C")
    Jump("loc_B34B")

    label("loc_AB6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_ACE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC57")

    ChrTalk(
        0xFE,
        (
            "Due to the recent\x01",
            "incident, my boys'\x01",
            "workplace went on holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having them all at home\x01",
            "doubles the difficulty\x01",
            "of the housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, differently from\x01",
            "before, I'm thankful\x01",
            "they're helping me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_ACDB")

    label("loc_AC57")


    ChrTalk(
        0xFE,
        (
            "Having them all at home\x01",
            "doubles the difficulty\x01",
            "of the housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder how soon my\x01",
            "boys' workplace is going\x01",
            "to reopen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACDB")

    Jump("loc_B34B")

    label("loc_ACE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_ACEE")
    Jump("loc_B34B")

    label("loc_ACEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_ACFC")
    Jump("loc_B34B")

    label("loc_ACFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_AE06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADC7")

    ChrTalk(
        0xFE,
        (
            "*sigh*. It's really nice\x01",
            "when you don't have to\x01",
            "do housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wait, huh!? Excessive\x01",
            "flab on my... belly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I really must've been\x01",
            "lazing around too\x01",
            "much...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AE01")

    label("loc_ADC7")


    ChrTalk(
        0xFE,
        (
            "I guess it's time I\x01",
            "started doing housework\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE01")

    Jump("loc_B34B")

    label("loc_AE06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AF99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEEA")

    ChrTalk(
        0xFE,
        (
            "My boys seem to have finally\x01",
            "understood the difficulty of\x01",
            "housework as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've been asking me\x01",
            "to let them do\x01",
            "housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, the housework\x01",
            "boycotting plan was a\x01",
            "great success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AF94")

    label("loc_AEEA")


    ChrTalk(
        0xFE,
        (
            "My boys seem to have finally\x01",
            "understood the difficulty of\x01",
            "housework as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, still, what should I do?\x01",
            "I want to enjoy it myself for\x01",
            "a while longer...♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF94")

    Jump("loc_B34B")

    label("loc_AF99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AFA7")
    Jump("loc_B34B")

    label("loc_AFA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B155")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0C5")

    ChrTalk(
        0xFE,
        (
            "After I stopped doing\x01",
            "housework, the meal menus\x01",
            "became extremely simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They order delivery on\x01",
            "their own, wasting mira\x01",
            "unnecessarily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since ours is a big family, they\x01",
            "should at least economise a little,\x01",
            "and yet... Honestly, men are no good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B150")

    label("loc_B0C5")


    ChrTalk(
        0xFE,
        (
            "...Hah! Why am I at the\x01",
            "street stalls quarter\x01",
            "again...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I decided to not do\x01",
            "housework, I shouldn't be\x01",
            "coming here anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B150")

    Jump("loc_B34B")

    label("loc_B155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B163")
    Jump("loc_B34B")

    label("loc_B163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23E")

    ChrTalk(
        0xFE,
        (
            "Lately, I completely\x01",
            "stopped doing housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that I have, it already\x01",
            "feels pleasant☆ I'm lazing\x01",
            "around at home all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I don't care about\x01",
            "my husband and sons.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B32F")

    label("loc_B23E")


    ChrTalk(
        0xFE,
        (
            "Because I'm not doing housework,\x01",
            "my husband and boys are in a panic\x01",
            "daily. Haha, serves them right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, when I go out for a walk, I\x01",
            "unconsciously come to the street stall quarter.\x01",
            "No, no, I've got an occupational disorder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B32F")

    Jump("loc_B34B")

    label("loc_B334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B342")
    Jump("loc_B34B")

    label("loc_B342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B34B")

    label("loc_B34B")

    TalkEnd(0xFE)
    Return()

    # Function_12_A9BB end

    def Function_13_B34F(): pass

    label("Function_13_B34F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B4A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B46A")

    ChrTalk(
        0xFE,
        (
            "As you can imagine, coming alone worries\x01",
            "us. So my father and us sons take turns\x01",
            "keeping her company shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a bother, but it can't\x01",
            "be helped. If mom got hurt,\x01",
            "we couldn't manage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel I once again\x01",
            "understand mom's\x01",
            "preciousness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B4A2")

    label("loc_B46A")


    ChrTalk(
        0xFE,
        (
            "I feel I once again\x01",
            "understand mom's\x01",
            "preciousness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4A2")

    Jump("loc_BB3D")

    label("loc_B4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B4B5")
    Jump("loc_BB3D")

    label("loc_B4B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B58A")

    ChrTalk(
        0xFE,
        (
            "Man, how exciting. It can't be\x01",
            "true that Crossbell has become\x01",
            "an independent state...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm genuinely happy. However I\x01",
            "don't have the slightest clue about\x01",
            "what's going to happen from now on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB3D")

    label("loc_B58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B598")
    Jump("loc_BB3D")

    label("loc_B598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B6DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B680")

    ChrTalk(
        0xFE,
        (
            "At last, mom has started\x01",
            "doing housework again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O-Of course from now on,\x01",
            "father and we brothers are\x01",
            "going help her with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we have a big\x01",
            "family, we must help\x01",
            "each other properly...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B6D6")

    label("loc_B680")


    ChrTalk(
        0xFE,
        (
            "When mom didn't do\x01",
            "housework, it was really\x01",
            "tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Moms are really great...\x02",
    )

    CloseMessageWindow()

    label("loc_B6D6")

    Jump("loc_BB3D")

    label("loc_B6DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B6E9")
    Jump("loc_BB3D")

    label("loc_B6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B6F7")
    Jump("loc_BB3D")

    label("loc_B6F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B705")
    Jump("loc_BB3D")

    label("loc_B705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7F5")

    ChrTalk(
        0xFE,
        (
            "Mom isn't doing the\x01",
            "housework, and I now\x01",
            "understand how hard it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We apologize every day\x01",
            "but she hasn't forgiven\x01",
            "us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The city is in an uproar\x01",
            "about independence, but\x01",
            "we've got our own problems.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B894")

    label("loc_B7F5")


    ChrTalk(
        0xFE,
        (
            "We, who never helped with\x01",
            "housework until now, are\x01",
            "clearly at fault for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, we must apologize\x01",
            "to mom persistently until\x01",
            "she forgives us...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B894")

    Jump("loc_BB3D")

    label("loc_B899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B8A7")
    Jump("loc_BB3D")

    label("loc_B8A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B9E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B96F")

    ChrTalk(
        0xFE,
        (
            "Because mom is skipping out on the\x01",
            "housework, father and we brothers are\x01",
            "dividing up the work amongst ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm in charge of meals.\x01",
            "Hmm, what should I\x01",
            "buy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B9DE")

    label("loc_B96F")


    ChrTalk(
        0xFE,
        (
            "To think thinking about\x01",
            "our daily menu is so\x01",
            "hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mom did this every day.\x01",
            "Honestly, I'm amazed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9DE")

    Jump("loc_BB3D")

    label("loc_B9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B9F1")
    Jump("loc_BB3D")

    label("loc_B9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B9FF")
    Jump("loc_BB3D")

    label("loc_B9FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_BB3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAD7")

    ChrTalk(
        0xFE,
        (
            "Recently, our mom isn't\x01",
            "doing any housework at\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because father and we brothers\x01",
            "almost never helped her, it\x01",
            "seems she finally blew her top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm... That's a real\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BB3D")

    label("loc_BAD7")


    ChrTalk(
        0xFE,
        (
            "Mom is livid and she\x01",
            "hasn't been doing any\x01",
            "housework at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm... That's a real\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB3D")

    TalkEnd(0xFE)
    Return()

    # Function_13_B34F end

    def Function_14_BB41(): pass

    label("Function_14_BB41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BCB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC2A")

    ChrTalk(
        0xFE,
        (
            "I get the feeling that\x01",
            "the city's former\x01",
            "liveliness is back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to do my part to\x01",
            "buy a lot and help the\x01",
            "economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aaalright, I'll have to\x01",
            "rethink once again my\x01",
            "discount shopping route!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_BCB3")

    label("loc_BC2A")


    ChrTalk(
        0xFE,
        (
            "I have to do my part to\x01",
            "buy a lot and help the\x01",
            "economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aaalright, I'll have to\x01",
            "rethink once again my\x01",
            "discount shopping route!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCB3")

    Jump("loc_C5F0")

    label("loc_BCB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BCC6")
    Jump("loc_C5F0")

    label("loc_BCC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BD54")

    ChrTalk(
        0xFE,
        (
            "I don't understand\x01",
            "complicated things very\x01",
            "well yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't the correct result\x01",
            "the one that everyone\x01",
            "chose? No?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F0")

    label("loc_BD54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BDDD")

    ChrTalk(
        0xFE,
        (
            "The other day I went to\x01",
            "mass at the church and\x01",
            "prayed to the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope peace returns to\x01",
            "Crossbell quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F0")

    label("loc_BDDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BE6A")

    ChrTalk(
        0xFE,
        (
            "Lately it's one incident\x01",
            "after the next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's kinda scary. I I'll\x01",
            "finish my shopping here\x01",
            "today and go home early...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F0")

    label("loc_BE6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BF2C")

    ChrTalk(
        0xFE,
        (
            "Ehehe, goodness. Even\x01",
            "today, I succeeded in\x01",
            "saving 10 mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess I'll eat an ice cream or\x01",
            "something and go home♪ ...Although, it\x01",
            "could be a little chilly in this rain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F0")

    label("loc_BF2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BFBD")

    ChrTalk(
        0xFE,
        (
            "Yeah, I guess I'll end\x01",
            "my shopping here for the\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Thanks to my cheap\x01",
            "shopping route, I saved\x01",
            "up quite the mira.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F0")

    label("loc_BFBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C047")

    ChrTalk(
        0xFE,
        (
            "I get the feeling that a new\x01",
            "shopping route is coming\x01",
            "into view, little-by-little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Economising is really\x01",
            "tough...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F0")

    label("loc_C047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C055")
    Jump("loc_C5F0")

    label("loc_C055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C1F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C13C")

    ChrTalk(
        0xFE,
        (
            "How cheap can you buy\x01",
            "things competing with\x01",
            "those around you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think the fun of sales\x01",
            "and bargains lies in\x01",
            "that point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The joy of buying what\x01",
            "you wanted for cheap is\x01",
            "truly exceptional.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C1F4")

    label("loc_C13C")


    ChrTalk(
        0xFE,
        (
            "The joy of buying what you\x01",
            "wanted for cheap using sales\x01",
            "and bargains is exceptional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially in my case, the joy\x01",
            "is doubled because the surplus\x01",
            "mira becomes my allowance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1F4")

    Jump("loc_C5F0")

    label("loc_C1F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C2C2")

    ChrTalk(
        0xFE,
        (
            "The excitement of today's\x01",
            "Orchis Tower unveiling\x01",
            "ceremony was quite high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Somehow, I smell sales. I think\x01",
            "I'll swing by the department store\x01",
            "today. I don't usually go there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F0")

    label("loc_C2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C41C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3A1")

    ChrTalk(
        0xFE,
        (
            "The trick to saving is intelligence\x01",
            "gathering. That's in order to not\x01",
            "miss timed sales and bargains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. It appears that if I shop\x01",
            "at the street stalls around\x01",
            "now I can save some mira.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C417")

    label("loc_C3A1")


    ChrTalk(
        0xFE,
        (
            "For the sake of my\x01",
            "allowance too, it's\x01",
            "saving, saving...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mustn't let timed\x01",
            "sales and bargains pass\x01",
            "me by.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C417")

    Jump("loc_C5F0")

    label("loc_C41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C4D0")

    ChrTalk(
        0xFE,
        (
            "Because there are few customers\x01",
            "on rainy days, you can take\x01",
            "your time checking the goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. It looks like I'll\x01",
            "get some good shopping\x01",
            "in today as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F0")

    label("loc_C4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C5F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C573")

    ChrTalk(
        0xFE,
        (
            "When mom asks me to do\x01",
            "errands, she hands me a\x01",
            "lot of mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do shopping with it,\x01",
            "and the surplus mira\x01",
            "becomes my allowance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C5F0")

    label("loc_C573")


    ChrTalk(
        0xFE,
        (
            "...But recently, mom's been\x01",
            "giving me just barely the\x01",
            "total amount needed, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hmm... My allowance\x01",
            "plan...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5F0")

    TalkEnd(0xFE)
    Return()

    # Function_14_BB41 end

    def Function_15_C5F4(): pass

    label("Function_15_C5F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C698")

    ChrTalk(
        0xFE,
        (
            "Although she could close up\x01",
            "shop at a time like this,\x01",
            "Marte has nerves of steel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's one of my\x01",
            "wife's good points, I\x01",
            "guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C73B")

    label("loc_C698")


    ChrTalk(
        0xFE,
        (
            "Although she could close up\x01",
            "shop at a time like this,\x01",
            "Marte has nerves of steel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, since I've come\x01",
            "here, I guess I'll help\x01",
            "her with the store today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C73B")

    TalkEnd(0xFE)
    Return()

    # Function_15_C5F4 end

    def Function_16_C73F(): pass

    label("Function_16_C73F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C822")

    ChrTalk(
        0xFE,
        (
            "They say that it's likely that\x01",
            "the Orchis Tower blueprints fell\x01",
            "into the hands of terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, where are they going to\x01",
            "attack from, I wonder? I'd like to\x01",
            "believe there are no openings, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C99D")

    label("loc_C822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C89A")

    ChrTalk(
        0xFE,
        (
            "I hope Red Constellation\x01",
            "or Heiyue don't show up\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, security isn't\x01",
            "that easy, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C99D")

    label("loc_C89A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C99D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C935")

    ChrTalk(
        0xFE,
        "Aah, the SSS, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can see, I'm\x01",
            "currently guarding the\x01",
            "street stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, do everything\x01",
            "that you can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_C99D")

    label("loc_C935")


    ChrTalk(
        0xFE,
        (
            "As you can see, I'm\x01",
            "currently guarding the\x01",
            "street stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, do everything\x01",
            "that you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C99D")

    TalkEnd(0xFE)
    Return()

    # Function_16_C73F end

    SaveToFile()

Try(main)
