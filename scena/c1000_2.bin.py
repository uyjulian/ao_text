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
        [152, 5344, 10276, 15025, 24275, 28520, 28955, 29545, 32403, 0, 36406, 0, 40718, 43697, 44276, 46691, 0, 48713, 0, 59, 201, 0, 0],
    )

    BuildStringList((
        "c1000_2",                # 0
    ))

    ChipFrameInfo(152, 0)                                        # 0

    ScpFunction((
        "Function_0_98",           # 00, 0
        "Function_1_14E0",         # 01, 1
        "Function_2_2824",         # 02, 2
        "Function_3_3AB1",         # 03, 3
        "Function_4_5ED3",         # 04, 4
        "Function_5_6F68",         # 05, 5
        "Function_6_711B",         # 06, 6
        "Function_7_7369",         # 07, 7
        "Function_8_7E93",         # 08, 8
        "Function_9_8E36",         # 09, 9
        "Function_10_9F0E",        # 0A, 10
        "Function_11_AAB1",        # 0B, 11
        "Function_12_ACF4",        # 0C, 12
        "Function_13_B663",        # 0D, 13
        "Function_14_BE49",        # 0E, 14
        "Function_15_C93B",        # 0F, 15
        "Function_16_CA87",        # 10, 16
    ))


    def Function_0_98(): pass

    label("Function_0_98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_347")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9")
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
            "What do you say about this pinwheel?\x01",
            "If you phew phew at it, it's fun, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "...Are you telling that to me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmph, that kind of thing\x01",
            "is not rare at all in the East\x01",
            "and it's mere kid stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*wasted*...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_235")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2E2")

    label("loc_235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_28E")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2E2")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2E2")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2E2")

    TalkEnd(0x8)
    SetScenarioFlags(0x1DC, 3)
    ClearChrFlags(0x8, 0x10)
    OP_93(0x8, 0xB4, 0x0)
    Jump("loc_346")

    label("loc_2F9")


    ChrTalk(
        0x8,
        (
            "Uuh...\x01",
            "It could be the first time a kid\x01",
            "was so not interested in it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_346")

    Return()

    label("loc_347")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_351")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C0")
    OP_AF(0x38)
    Jump("loc_3C2")

    label("loc_3C0")

    OP_AF(0x39)

    label("loc_3C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14D7")

    label("loc_3D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E5")
    Jump("loc_14D7")

    label("loc_3E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50C")

    ChrTalk(
        0xFE,
        (
            "For the present, I'm glad that Crossbell\x01",
            "city has gained back its everyday life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In exchange for that, a mysterious\x01",
            "tree has appeared, however...\x01",
            "I'm sure we'll manage, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I make some new \x01",
            "handicraft just to relax?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5A0")

    label("loc_50C")


    ChrTalk(
        0xFE,
        (
            "As for Roy, I intend to make him\x01",
            "work hard again from tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A mysterious tree has\x01",
            "appeared, however...\x01",
            "I'm sure we'll manage somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A0")

    Jump("loc_14D7")

    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5B3")
    Jump("loc_14D7")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_638")

    ChrTalk(
        0xFE,
        (
            "Finally, Crossbell is\x01",
            "independent as a nation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I'm truly witnessing\x01",
            "a history-changing moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D7")

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6D7")

    ChrTalk(
        0xFE,
        (
            "I made a lot of wooden\x01",
            "tableware for the emergency\x01",
            "feeding they do at Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're trivial things,\x01",
            "but that's just what\x01",
            "I can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D7")

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_76A")

    ChrTalk(
        0xFE,
        (
            "They say that Mainz\x01",
            "has been occupied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm indebted a lot to them for\x01",
            "the handicraft materials they\x01",
            "provide...I'm worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D7")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7FF")

    ChrTalk(
        0xFE,
        (
            "Seems like today customers \x01",
            "aren't coming at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also gave Roy a day off\x01",
            "and I'm taking my time\x01",
            "making handicrafts alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D7")

    label("loc_7FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_863")

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
            "Weeell, somehow\x01",
            "I'm glad too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D7")

    label("loc_863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94A")

    ChrTalk(
        0xFE,
        (
            "The pinwheels this store sell,\x01",
            "have each a slightly different\x01",
            "way of rotating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This, is the "flavor"\x01",
            "of handmade things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, an amateur\x01",
            "doesn't almost understand\x01",
            "that difference, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9EC")

    label("loc_94A")


    ChrTalk(
        0xFE,
        (
            "By the way, Roy's pinwheels\x01",
            "seem they could sell well,\x01",
            "but only one did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like he's naturally\x01",
            "skilled with his fingers.\x01",
            "He's a bright prospect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EC")

    Jump("loc_14D7")

    label("loc_9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AED")

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
            "When I put it at the store front,\x01",
            "the tourists wanted it a lot.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, this is not for sale.\x01",
            "Somehow I'm sorry for them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B76")

    label("loc_AED")


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
            "As expected, this could be due\x01",
            "to being a president's relative.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B76")

    Jump("loc_14D7")

    label("loc_B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C50")

    ChrTalk(
        0xFE,
        (
            "It's been decided for\x01",
            "Roy to work here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As it might be expected from him \x01",
            "being the Merchants Association \x01",
            "President's grandchild, he's diligent.\x01",
            "I'm expecting a lot from him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CC9")

    label("loc_C50")


    ChrTalk(
        0xFE,
        (
            "I intend to have him learn\x01",
            "many, many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hu hu, I'm having fun because\x01",
            "it's like I got myself a disciple.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC9")

    Jump("loc_14D7")

    label("loc_CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_10D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC4")

    ChrTalk(
        0xFE,
        (
            "If you're looking for the beautiful Eastern woman\x01",
            "that was here some time ago, after buying many things\x01",
            "at the stalls, she walked towards Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her almond-shaped cold eyes\x01",
            "were very impressive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CB")

    label("loc_DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3E")

    ChrTalk(
        0xFE,
        (
            "An Eastern beautiful woman came\x01",
            "to shop just moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her almond-shaped cold eyes\x01",
            "were very impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F...In which direction did that person go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After buying many things at the stalls,\x01",
            "she walked towards Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F(Hey Lloyd, could \x01",
            "she be that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(...Yeah, let's try looking around.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x1C6, 7)
    Jump("loc_10CB")

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1038")

    ChrTalk(
        0xFE,
        (
            "Maaan, Orchis Tower has\x01",
            "really got a presence, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, my urge to create is boiling.\x01",
            "I guess I'll try to build a model of the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even before, at the time of the Anniversary\x01",
            "Festival, I made a model of City Hall.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10CB")

    label("loc_1038")


    ChrTalk(
        0xFE,
        (
            "By the way...\x01",
            "The grandchild of President Mors of the Merchants \x01",
            "Association came to have a look here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, even the unexpected happens.\x02",
    )

    CloseMessageWindow()

    label("loc_10CB")

    Jump("loc_14D7")

    label("loc_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1220")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1167")

    ChrTalk(
        0xFE,
        (
            "My handicrafts are\x01",
            "all hand made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Hand made"...as you'd expect, it has a\x01",
            "kind of warmth somewhere and it's nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_121B")

    label("loc_1167")


    ChrTalk(
        0xFE,
        (
            "Hand made things take a lot of time to make and\x01",
            "sometimes you end up hurting yourself too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you'd expect, they have a kind of\x01",
            "warmth somewhere and they're nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121B")

    Jump("loc_14D7")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_13B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1325")

    ChrTalk(
        0xFE,
        (
            "They're handicrafts made with a lot \x01",
            "of effort but they end up getting wet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Nevertheless, my\x01",
            "handicrafts have a\x01",
            "proper waterproof finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it takes time and effort to make them,\x01",
            "you can expect them to be solid.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13AD")

    label("loc_1325")


    ChrTalk(
        0xFE,
        (
            "My handicrafts have a\x01",
            "proper waterproof finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it takes time and effort to make them,\x01",
            "you can expect them to be solid.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AD")

    Jump("loc_14D7")

    label("loc_13B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_14D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1459")

    ChrTalk(
        0xFE,
        "Hello, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I deal in various hand\x01",
            "made handicrafts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there's something you like,\x01",
            "I'd like you to buy it by all means!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14D7")

    label("loc_1459")


    ChrTalk(
        0xFE,
        (
            "What is popular among my store\x01",
            "articles is this "pinwheel".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the East, it's a toy said \x01",
            "to protect you from harm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D7")

    Jump("loc_351")

    label("loc_14DC")

    TalkEnd(0xFE)
    Return()

    # Function_0_98 end

    def Function_1_14E0(): pass

    label("Function_1_14E0")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2820")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_153D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155D")
    OP_AF(0x35)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_281B")

    label("loc_155D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1571")
    Jump("loc_281B")

    label("loc_1571")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1635")

    ChrTalk(
        0xFE,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fresh Danes is\x01",
            "open today too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's eat fresh vegetables\x01",
            "and overcome this abnormal\x01",
            "situation in good health!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16C3")

    label("loc_1635")


    ChrTalk(
        0xFE,
        (
            "...It seems that Lily has been\x01",
            "coming to look here frequently\x01",
            "since some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if I've got something stuck to my face.\x02",
    )

    CloseMessageWindow()

    label("loc_16C3")

    Jump("loc_281B")

    label("loc_16C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_16D6")
    Jump("loc_281B")

    label("loc_16D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_17FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179C")

    ChrTalk(
        0xFE,
        (
            "The Independent State of Crossbell, eh...?\x01",
            "Man, that's a joyous thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, that Lily\x01",
            "somehow has a\x01",
            "frowned face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Could she be worried about something?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17F9")

    label("loc_179C")


    ChrTalk(
        0xFE,
        (
            "That Lily...\x01",
            "Somehow she has\x01",
            "a frowned face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Could she be worried about something?\x02",
    )

    CloseMessageWindow()

    label("loc_17F9")

    Jump("loc_281B")

    label("loc_17FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1901")

    ChrTalk(
        0xFE,
        (
            "I gave vegetables from the store\x01",
            "for the charity event that is being\x01",
            "held today at City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm indebted to the Merchants\x01",
            "Association that sponsor it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want all the people in the\x01",
            "city to feel better too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19B3")

    label("loc_1901")


    ChrTalk(
        0xFE,
        (
            "I'm really grateful to the Merchants\x01",
            "Association old gentleman who\x01",
            "invited me as an official member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to do my best in order to\x01",
            "make all in the city feel better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B3")

    Jump("loc_281B")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1ACF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A79")

    ChrTalk(
        0xFE,
        (
            "They say that Mainz was occupied, but...\x01",
            "According to rumors, a ransom request\x01",
            "or the likes hasn't come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what that armed\x01",
            "group is trying to do...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ACA")

    label("loc_1A79")


    ChrTalk(
        0xFE,
        (
            "For what purpose could that\x01",
            "armed group or whatever\x01",
            "have occupied Mainz...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACA")

    Jump("loc_281B")

    label("loc_1ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE2")

    ChrTalk(
        0xFE,
        (
            "The mister who comes to wholesale me\x01",
            "vegetables told me that being somewhat agitated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yesterday, it appears that there was\x01",
            "some big clamor at Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it seems it has been resolved, but...\x01",
            "Hmm, I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C90")

    label("loc_1BE2")


    ChrTalk(
        0xFE,
        (
            "It appears that there was some big\x01",
            "clamor at Armorica Village yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't get it well, since the\x01",
            "truck mister was agitated and\x01",
            "spoke with a local accent...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C90")

    Jump("loc_281B")

    label("loc_1C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8C")

    ChrTalk(
        0xFE,
        (
            "Actually, when I was a kid I really\x01",
            "hated vegetables and similar stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, becoming an adult\x01",
            "I gradually became able to\x01",
            "think they're delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It could be an unexpected\x01",
            "case of likes and dislikes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E20")

    label("loc_1D8C")


    ChrTalk(
        0xFE,
        (
            "I greatly hated vegetables, but\x01",
            "who knows when, I became\x01",
            "able to enjoy eating them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It could be an unexpected\x01",
            "case of likes and dislikes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E20")

    Jump("loc_281B")

    label("loc_1E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1EF7")

    ChrTalk(
        0xFE,
        (
            "Actually, my store name\x01",
            "was thought by Lily for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After I told her I wanted to open a business,\x01",
            "she has been supporting me a way or another...\x01",
            "Eh eh, I've got a good childhood friend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_281B")

    label("loc_1EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2040")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FBB")

    ChrTalk(
        0xFE,
        (
            "I always got vegetables\x01",
            "wholesaled with an orbal truck\x01",
            "from Armorica Village, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, it's bad for me to\x01",
            "say this, but was it such\x01",
            "a neat truck, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_203B")

    label("loc_1FBB")


    ChrTalk(
        0xFE,
        (
            "Armorica Village orbal truck...\x01",
            "Maybe they bought a new one?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh eh, a good business condition\x01",
            "is eternally enviable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_203B")

    Jump("loc_281B")

    label("loc_2040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_219F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F4")

    ChrTalk(
        0xFE,
        (
            "They're going to mainly discuss\x01",
            "economics at the Trade Conference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, I don't understand\x01",
            "complicated stuff.\x01",
            "Whatever will be, will be!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_219A")

    label("loc_20F4")


    ChrTalk(
        0xFE,
        (
            "Well, whatever the economy will be, \x01",
            "I'll do business putting customers \x01",
            "before all from now on too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't understand the slightest\x01",
            "of complicated stuff!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219A")

    Jump("loc_281B")

    label("loc_219F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_23DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2317")

    ChrTalk(
        0xFE,
        (
            "They say that today the Liberl\x01",
            "Kingdom princess has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you say "Liberl Kingdom",\x01",
            "its "Acerbic Tomatoes" are famous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say that they're something born\x01",
            "at an orbments manufacturer called\x01",
            "ZCF located in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're an orbments manufacturer \x01",
            "and yet they even make vegetables...\x01",
            "That's technological power for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23D7")

    label("loc_2317")


    ChrTalk(
        0xFE,
        (
            "The Acerbic Tomato is a\x01",
            "vegetable that was born at\x01",
            "ZCF a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're an orbments manufacturer \x01",
            "and yet they even make vegetables...\x01",
            "That's technological power for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D7")

    Jump("loc_281B")

    label("loc_23DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2630")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2587")

    ChrTalk(
        0xFE,
        (
            "I heard this from a doctor\x01",
            "at St. Ursula...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that when you eat vegetables,\x01",
            "fats absorption slows down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It means that when eating meat,\x01",
            "if you eat it with vegetables, it\x01",
            "becomes harder to get fat.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24F1")
    Jump("loc_257F")

    label("loc_24F1")


    ChrTalk(
        0x109,
        "#10105FI-I see...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FIt was some useful information.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Girls are especially passionate\x01",
            "about this kind of topic...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257F")

    SetScenarioFlags(0x0, 1)
    Jump("loc_262B")

    label("loc_2587")


    ChrTalk(
        0xFE,
        (
            "Are you eating vegetables?\x01",
            "Eating nothing but junk food\x01",
            "is poison for your body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want to live healthily, as you'd\x01",
            "expect, you must eat vegetables.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_262B")

    Jump("loc_281B")

    label("loc_2630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_26E6")

    ChrTalk(
        0xFE,
        (
            "...Hmm, it looks like there's\x01",
            "a roof leak from the tent.\x01",
            "Before long, I'll have to repair it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...At any rate, what's Lily been\x01",
            "restlessly doing since before?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_281B")

    label("loc_26E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_281B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AE")

    ChrTalk(
        0xFE,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today too I received plenty of\x01",
            "Armorica produced fresh vegetables!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you'd expect, Crossbell produced\x01",
            "vegetables are number one for taste!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_281B")

    label("loc_27AE")


    ChrTalk(
        0xFE,
        (
            "As you'd expect, Armorica produced\x01",
            "vegetables are tasty and I recommend them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come buy plenty, ok?\x02",
    )

    CloseMessageWindow()

    label("loc_281B")

    Jump("loc_14ED")

    label("loc_2820")

    TalkEnd(0xFE)
    Return()

    # Function_1_14E0 end

    def Function_2_2824(): pass

    label("Function_2_2824")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_29CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2920")

    ChrTalk(
        0xFE,
        (
            "That Danes...\x01",
            "Eating vegetables and overcoming this...\x01",
            "That's far too optimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, because Danes is like that,\x01",
            "he can cheer up everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That part could be unexpectedly\x01",
            "important for a street stall.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29C7")

    label("loc_2920")


    ChrTalk(
        0xFE,
        (
            "Right because Danes is optimistic,\x01",
            "he can cheer up everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too, when monsters were roaming\x01",
            "in the city, was pepped up by Danes.\x01",
            "Hu hu, I must thank him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C7")

    Jump("loc_3AAD")

    label("loc_29CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_29DA")
    Jump("loc_3AAD")

    label("loc_29DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B60")

    ChrTalk(
        0xFE,
        (
            "Goods distribution from the two major\x01",
            "powers has completely stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that, according to\x01",
            "President Dieter, we have emergency\x01",
            "stocks for at least five years, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who sells fresh vegetables must\x01",
            "think about a business methods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...And yet, it seems that Danes\x01",
            "doesn't understand that point.\x01",
            "*sigh", I'd like he got his act together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C46")

    label("loc_2B60")


    ChrTalk(
        0xFE,
        (
            "It appears that, according to President Dieter, we \x01",
            "have emergency stocks for at least five years, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's something that's going to be\x01",
            "involved in business from now on, so \x01",
            "I'd want Danes to get his act together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C46")

    Jump("loc_3AAD")

    label("loc_2C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC6")

    ChrTalk(
        0xFE,
        (
            "Maybe it's a blessing in disguise,\x01",
            "but the East Street didn't receive\x01",
            "almost any damage, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2CC6")


    ChrTalk(
        0xFE,
        (
            "Because of the rampaging of that big ogre,\x01",
            "it seems that Downtown is in an awful state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that they're doing repair works now, but...\x01",
            "I wonder how soon the situation will be settled.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AAD")

    label("loc_2D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2E11")

    ChrTalk(
        0xFE,
        "The Mainz incident...that's scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that the CGF\x01",
            "people will settle it\x01",
            "in a way or another.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AAD")

    label("loc_2E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2EDD")

    ChrTalk(
        0xFE,
        (
            "Oh jeez, although recently I plugged\x01",
            "a hole in the tent, it looks like it's \x01",
            "leaking from a different spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Jeez, that Danes, I wished he stopped\x01",
            "to think deep and gave me a help!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AAD")

    label("loc_2EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3098")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF5")

    ChrTalk(
        0xFE,
        (
            "Maybe there're many people\x01",
            "who hate onions and leek\x01",
            "because they smell, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess there's almost none who\x01",
            "have big prejudices against them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd wish they tried to eat them\x01",
            "resolutely, because they could\x01",
            "unexpectedly find them tasty.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3093")

    label("loc_2FF5")


    ChrTalk(
        0xFE,
        (
            "Having food prejudices...\x01",
            "As you can imagine, it's a bit of a waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Food with a smell you dislike\x01",
            "could be quite delicious if\x01",
            "you try to eat them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3093")

    Jump("loc_3AAD")

    label("loc_3098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_325E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319D")

    ChrTalk(
        0xFE,
        (
            "Danes...\x01",
            "He was trying to start a business just\x01",
            "like that, without any knowledge at all.\x02",
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
            "What can I say, I can't leave\x01",
            "him alone since back in the past.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3259")

    label("loc_319D")


    ChrTalk(
        0xFE,
        (
            "Danes...\x01",
            "He was trying to start a business just\x01",
            "like that, without any knowledge at all.\x02",
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

    label("loc_3259")

    Jump("loc_3AAD")

    label("loc_325E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3421")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3362")

    ChrTalk(
        0xFE,
        (
            "Actually, the old gentleman from the Merchants\x01",
            "Association came to ask me in secret about\x01",
            "how Danes was doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Danes turned down an invitation to\x01",
            "become an official member before, but...\x01",
            "It really seems he's regretting it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_341C")

    label("loc_3362")


    ChrTalk(
        0xFE,
        (
            "Uhhm, at that time, I too\x01",
            "was thinking it was a pity\x01",
            "he refused the invitation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Danes...\x01",
            "It's not in his character to stand on top \x01",
            "of others, so I thought it was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_341C")

    Jump("loc_3AAD")

    label("loc_3421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34A6")

    ChrTalk(
        0xFE,
        (
            "Jeez, that Danes can't think\x01",
            "deeply about things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, who is his childhood friend,\x01",
            "must support him steadily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AAD")

    label("loc_34A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35E5")

    ChrTalk(
        0xFE,
        (
            "When you use the Acerbic Tomato in a dish,\x01",
            "it gives quite the accent to the flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I wouldn't recommend it\x01",
            "at all to people who wants to eat\x01",
            "it in a salad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...After all, eating it just like that,\x01",
            "it something which is really bitter.\x01",
            "I guess I'm slightly bad with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_369C")

    label("loc_35E5")


    ChrTalk(
        0xFE,
        (
            "When you use the Acerbic Tomato in a dish,\x01",
            "it gives quite the accent to the flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But eaten like that, it extremely bitter.\x01",
            "It's quite the ingredient meant for the pros. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_369C")

    Jump("loc_3AAD")

    label("loc_36A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37CD")

    ChrTalk(
        0xFE,
        (
            "To become a stallholder, Danes studied\x01",
            "about vegetables with all his might.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, not having the slightest sense of management,\x01",
            "he's doing business almost only with his good personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in a certain sense, that's\x01",
            "Danes' distinctive characteristic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_386D")

    label("loc_37CD")


    ChrTalk(
        0xFE,
        (
            "Danes business is honest, but he doesn't \x01",
            "have the slightest sense of management.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in a certain sense, that's\x01",
            "Danes' distinctive characteristic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_386D")

    Jump("loc_3AAD")

    label("loc_3872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3962")

    ChrTalk(
        0xFE,
        (
            "A customer who came just before said\x01",
            "that we two looked like a married couple...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I thought of us as mere childhood\x01",
            "friends, I never even thought about it, but...\x01",
            "S-Somehow, I became aware of that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39FE")

    label("loc_3962")


    ChrTalk(
        0xFE,
        (
            "I was said by a customer\x01",
            "that we two look like a\x01",
            "married couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, it looks like Danes\x01",
            "doesn't think anything about it.\x01",
            "Jeez, how rude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FE")

    Jump("loc_3AAD")

    label("loc_3A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3AAD")

    ChrTalk(
        0xFE,
        (
            "In Crossbell we rely on many\x01",
            "imported groceries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, because they're delivered fast via railroad,\x01",
            "although they're imported goods, they're fresh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AAD")

    TalkEnd(0xFE)
    Return()

    # Function_2_2824 end

    def Function_3_3AB1(): pass

    label("Function_3_3AB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ADA")
    Call(0, 29)
    Return()

    label("loc_3ADA")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x2, 3)
    Call(2, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_5ECC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EC7")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "Talk")
    MenuCmd(1, 1, "Give Fish")
    MenuCmd(1, 1, "Quit")
    ClearScenarioFlags(0x2, 3)
    Call(2, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B43")
    MenuCmd(3, 1, 0x1)

    label("loc_3B43")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B75")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3B75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E92")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E83")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BFA")
    MenuCmd(1, 1, "Fighter         Time x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF0")
    Call(2, 6)

    label("loc_3BF0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3BFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C4C")
    MenuCmd(1, 1, "Snow Crab       Mirage x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C42")
    Call(2, 6)

    label("loc_3C42")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C9F")
    MenuCmd(1, 1, "Angelfish       Liquids x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C95")
    Call(2, 6)

    label("loc_3C95")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CF0")
    MenuCmd(1, 1, "Kasagin         Space x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CE6")
    Call(2, 6)

    label("loc_3CE6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3CF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D41")
    MenuCmd(1, 1, "Armorica Carp   Onion x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D37")
    Call(2, 6)

    label("loc_3D37")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D94")
    MenuCmd(1, 1, "Tortoise        Powders x4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D8A")
    Call(2, 6)

    label("loc_3D8A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DE6")
    MenuCmd(1, 1, "Tiger Rockfish  Carrot x4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DDC")
    Call(2, 6)

    label("loc_3DDC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3DE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E39")
    MenuCmd(1, 1, "Rockeater       Liquids x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E2F")
    Call(2, 6)

    label("loc_3E2F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E88")
    MenuCmd(1, 1, "Rainbow Trout   All x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E7E")
    Call(2, 6)

    label("loc_3E7E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3ED8")
    MenuCmd(1, 1, "Piranha         Herb x4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ECE")
    Call(2, 6)

    label("loc_3ECE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3ED8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F28")
    MenuCmd(1, 1, "Carp            Leaf x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F1E")
    Call(2, 6)

    label("loc_3F1E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F79")
    MenuCmd(1, 1, "Gluttonous Bass Earth x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6F")
    Call(2, 6)

    label("loc_3F6F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FCB")
    MenuCmd(1, 1, "Trout           Potato x4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FC1")
    Call(2, 6)

    label("loc_3FC1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3FCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_401A")
    MenuCmd(1, 1, "Gladiator       All x5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4010")
    Call(2, 6)

    label("loc_4010")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_401A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_406C")
    MenuCmd(1, 1, "Walleye         Water x10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4062")
    Call(2, 6)

    label("loc_4062")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_406C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40BD")
    MenuCmd(1, 1, "Salamander      Wind x10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B3")
    Call(2, 6)

    label("loc_40B3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_40BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_410E")
    MenuCmd(1, 1, "Salmon          Berry x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4104")
    Call(2, 6)

    label("loc_4104")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_410E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_415F")
    MenuCmd(1, 1, "Arowana         Fire x15")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4155")
    Call(2, 6)

    label("loc_4155")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_415F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41B7")
    MenuCmd(1, 1, "Eel             Rare Veggies x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41AD")
    Call(2, 6)

    label("loc_41AD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_41B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4207")
    MenuCmd(1, 1, "Adamantoise     Miso x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41FD")
    Call(2, 6)

    label("loc_41FD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4207")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_425F")
    MenuCmd(1, 1, "Queen Crab      Rare Veggies x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4255")
    Call(2, 6)

    label("loc_4255")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_425F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42AF")
    MenuCmd(1, 1, "Pirarucu        Miso x3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A5")
    Call(2, 6)

    label("loc_42A5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_42AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4300")
    MenuCmd(1, 1, "Catfish         Dairy x4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F6")
    Call(2, 6)

    label("loc_42F6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4300")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4352")
    MenuCmd(1, 1, "Gold Salmon     Space x50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4348")
    Call(2, 6)

    label("loc_4348")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4352")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43A5")
    MenuCmd(1, 1, "Pale Salamander Mirage x20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_439B")
    Call(2, 6)

    label("loc_439B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43F5")
    MenuCmd(1, 1, "Noble Carp      All x10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43EB")
    Call(2, 6)

    label("loc_43EB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4447")
    MenuCmd(1, 1, "Emeraude        Wind x500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443D")
    Call(2, 6)

    label("loc_443D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4447")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_449A")
    MenuCmd(1, 1, "Tiger Rockeater Earth x500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4490")
    Call(2, 6)

    label("loc_4490")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_449A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44EC")
    MenuCmd(1, 1, "Crimson Eater   Fire x500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44E2")
    Call(2, 6)

    label("loc_44E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_44EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_453F")
    MenuCmd(1, 1, "Bull Dragon     Water x500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4535")
    Call(2, 6)

    label("loc_4535")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_453F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4597")
    MenuCmd(1, 1, "Giant Pirarucu  TimSpaMira x500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_458D")
    Call(2, 6)

    label("loc_458D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4597")

    MenuCmd(1, 1, "Quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45D6")
    Jump("loc_5E7E")

    label("loc_45D6")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4666")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_465C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#60ITime Sepith x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_465C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4666")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_46DB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46D1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#62IMirage Sepith x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_46D1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4755")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_474B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Iliquid ingredients x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_474B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4755")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47C9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#61ISpace Sepith x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_47BF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4837")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_482D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Ionions x2\x07\x00",
            "?\x02",
        )
    )


    label("loc_482D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4837")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48B1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48A7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Ipowder ingredients x4\x07\x00",
            "?\x02",
        )
    )


    label("loc_48A7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_48B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4920")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4916")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Icarrots x4\x07\x00",
            "?\x02",
        )
    )


    label("loc_4916")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4920")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_499A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4990")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Iliquid ingredients x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4990")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_499A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A11")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A07")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "all Sepith elements x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_4A07")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A7D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A73")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Iherb x4\x07\x00",
            "?\x02",
        )
    )


    label("loc_4A73")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AE9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ADF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Ileaf x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4ADF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4AE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B5D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B53")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#56IEarth Sepith x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_4B53")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BCB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BC1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Ipotato x4\x07\x00",
            "?\x02",
        )
    )


    label("loc_4BC1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4BCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C41")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C37")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "all Sepith element x5\x07\x00",
            "?\x02",
        )
    )


    label("loc_4C37")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CB6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CAC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#57IWater Sepith x10\x07\x00",
            "?\x02",
        )
    )


    label("loc_4CAC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4CB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D2A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D20")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#59IWind Sepith x10\x07\x00",
            "?\x02",
        )
    )


    label("loc_4D20")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4D2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D97")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D8D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Iberry x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4D8D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4D97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E0B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E01")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#58IFire Sepith x15\x07\x00",
            "?\x02",
        )
    )


    label("loc_4E01")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4E0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E7F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E75")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Irare veggies x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4E75")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4E7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4EF1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EE7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Ibrown rice x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4EE7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4EF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F67")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F5D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Irare veggies x3個\x07\x00",
            "?\x02",
        )
    )


    label("loc_4F5D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4F67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4FD3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FC9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Imiso x3\x07\x00",
            "?\x02",
        )
    )


    label("loc_4FC9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4FD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5042")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5038")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#20Idairies x4\x07\x00",
            "?\x02",
        )
    )


    label("loc_5038")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5042")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_50B7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50AD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#61ISpace Sepith x50\x07\x00",
            "?\x02",
        )
    )


    label("loc_50AD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_50B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_512D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5123")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#62IMirage Sepith x20\x07\x00",
            "?\x02",
        )
    )


    label("loc_5123")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_512D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_51A5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_519B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "all Sepith elements x10\x07\x00",
            "?\x02",
        )
    )


    label("loc_519B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_51A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_521A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5210")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#59IWind Sepith x500\x07\x00",
            "?\x02",
        )
    )


    label("loc_5210")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_521A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5290")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5286")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#56IEarth Sepith x500\x07\x00",
            "?\x02",
        )
    )


    label("loc_5286")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5290")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5305")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52FB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#58IFire Sepith x500\x07\x00",
            "?\x02",
        )
    )


    label("loc_52FB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5305")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_537B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5371")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "#57IWater Sepith x500\x07\x00",
            "?\x02",
        )
    )


    label("loc_5371")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_537B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_53F7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53ED")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you give me this fish for\x01\x07\x02",
            "Time, Space and Mirage x500\x07\x00",
            "?\x02",
        )
    )


    label("loc_53ED")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_53F7")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Exchange\x01",      # 0
            "Quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E7E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_552D")

    ChrTalk(
        0xFE,
        (
            "This is an especially magnificent fish, \x01",
            "maybe you won't catch another one...\x01",
            "Are you really giving it to me?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_552D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_552D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E74")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_561E"),
        (1, "loc_5651"),
        (2, "loc_5686"),
        (3, "loc_56BF"),
        (4, "loc_56F3"),
        (5, "loc_571B"),
        (6, "loc_575D"),
        (7, "loc_5785"),
        (8, "loc_57BE"),
        (9, "loc_588D"),
        (10, "loc_58B5"),
        (11, "loc_58DD"),
        (12, "loc_5911"),
        (13, "loc_5939"),
        (14, "loc_5A08"),
        (15, "loc_5A3D"),
        (16, "loc_5A71"),
        (17, "loc_5A99"),
        (18, "loc_5ACD"),
        (19, "loc_5B06"),
        (20, "loc_5B2E"),
        (21, "loc_5B67"),
        (22, "loc_5B8E"),
        (23, "loc_5BD0"),
        (24, "loc_5C06"),
        (25, "loc_5C3D"),
        (26, "loc_5D13"),
        (27, "loc_5D48"),
        (28, "loc_5D7E"),
        (29, "loc_5DB3"),
        (30, "loc_5DE9"),
        (SWITCH_DEFAULT, "loc_5E58"),
    )


    label("loc_561E")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60ITime Sepith x5\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x4, 5)
    SubItemNumber(0x15E, 1)
    Jump("loc_5E58")

    label("loc_5651")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62IMirage Sepith x5\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x6, 5)
    SubItemNumber(0x15F, 1)
    Jump("loc_5E58")

    label("loc_5686")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x13B),
            " \x01",
            scpstr(SCPSTR_CODE_ITEM, 0x13C),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x136),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    AddItemNumber(0x13B, 1)
    AddItemNumber(0x13C, 1)
    AddItemNumber(0x136, 1)
    SubItemNumber(0x160, 1)
    Jump("loc_5E58")

    label("loc_56BF")


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
    Jump("loc_5E58")

    label("loc_56F3")


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
    Jump("loc_5E58")

    label("loc_571B")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x139),
            " \x01",
            scpstr(SCPSTR_CODE_ITEM, 0x13A),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13D),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13E),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    AddItemNumber(0x139, 1)
    AddItemNumber(0x13A, 1)
    AddItemNumber(0x13D, 1)
    AddItemNumber(0x13E, 1)
    SubItemNumber(0x163, 1)
    Jump("loc_5E58")

    label("loc_575D")


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
    Jump("loc_5E58")

    label("loc_5785")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x13B),
            " \x01",
            scpstr(SCPSTR_CODE_ITEM, 0x13C),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x136),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    AddItemNumber(0x13B, 1)
    AddItemNumber(0x13C, 1)
    AddItemNumber(0x136, 1)
    SubItemNumber(0x165, 1)
    Jump("loc_5E58")

    label("loc_57BE")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56IEarth Sepith x5\x01\x07\x02",
            "#57IWater Sepith x5\x01\x07\x02",
            "#58IFire Sepith x5\x01\x07\x02",
            "#59IWind Sepith x5\x01\x07\x02",
            "#60ITime Sepith x5\x01\x07\x02",
            "#61ISpace Sepith x5\x01\x07\x02",
            "#62IMirage Sepith x5\x01\x07\x00",
            " obtained.\x02",
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
    Jump("loc_5E58")

    label("loc_588D")


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
    Jump("loc_5E58")

    label("loc_58B5")


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
    Jump("loc_5E58")

    label("loc_58DD")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56IEarth Sepith x5\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x0, 5)
    SubItemNumber(0x169, 1)
    Jump("loc_5E58")

    label("loc_5911")


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
    Jump("loc_5E58")

    label("loc_5939")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56IEarth Sepith x5\x01\x07\x02",
            "#57IWater Sepith x5\x01\x07\x02",
            "#58IFire Sepith x5\x01\x07\x02",
            "#59IWind Sepith x5\x01\x07\x02",
            "#60ITime Sepith x5\x01\x07\x02",
            "#61ISpace Sepith x5\x01\x07\x02",
            "#62IMirage Sepith x5\x01\x07\x00",
            " obtained.\x02",
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
    Jump("loc_5E58")

    label("loc_5A08")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57IWater Sepith x10\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x1, 10)
    SubItemNumber(0x16C, 1)
    Jump("loc_5E58")

    label("loc_5A3D")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59IWind Sepith x10\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x3, 10)
    SubItemNumber(0x16D, 1)
    Jump("loc_5E58")

    label("loc_5A71")


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
    Jump("loc_5E58")

    label("loc_5A99")


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
    Jump("loc_5E58")

    label("loc_5ACD")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x143),
            " \x01",
            scpstr(SCPSTR_CODE_ITEM, 0x144),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x148),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    AddItemNumber(0x143, 1)
    AddItemNumber(0x144, 1)
    AddItemNumber(0x148, 1)
    SubItemNumber(0x170, 1)
    Jump("loc_5E58")

    label("loc_5B06")


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
    Jump("loc_5E58")

    label("loc_5B2E")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x143),
            " \x01",
            scpstr(SCPSTR_CODE_ITEM, 0x144),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x148),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    AddItemNumber(0x143, 1)
    AddItemNumber(0x144, 1)
    AddItemNumber(0x148, 1)
    SubItemNumber(0x172, 1)
    Jump("loc_5E58")

    label("loc_5B67")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x135),
            "x3\x07\x00",
            " obtained.\x02",
        )
    )

    AddItemNumber(0x135, 3)
    SubItemNumber(0x173, 1)
    Jump("loc_5E58")

    label("loc_5B8E")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x13F),
            " \x01",
            scpstr(SCPSTR_CODE_ITEM, 0x140),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x141),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x149),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    AddItemNumber(0x13F, 1)
    AddItemNumber(0x140, 1)
    AddItemNumber(0x141, 1)
    AddItemNumber(0x149, 1)
    SubItemNumber(0x174, 1)
    Jump("loc_5E58")

    label("loc_5BD0")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61ISpace Sepith x50 \x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x5, 50)
    SubItemNumber(0x175, 1)
    Jump("loc_5E58")

    label("loc_5C06")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62IMirage Sepith x20 \x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x6, 20)
    SubItemNumber(0x176, 1)
    Jump("loc_5E58")

    label("loc_5C3D")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56IEarth Sepith x10\x01\x07\x02",
            "#57IWater Sepith x10\x01\x07\x02",
            "#58IFire Sepith x10\x01\x07\x02",
            "#59IWind Sepith x10\x01\x07\x02",
            "#60ITime Sepith x10\x01\x07\x02",
            "#61ISpace Sepith x10\x01\x07\x02",
            "#62IMirage Sepith x10\x01\x07\x00",
            " obtained.\x02",
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
    Jump("loc_5E58")

    label("loc_5D13")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59IWind Sepith x500\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x3, 500)
    SubItemNumber(0x178, 1)
    Jump("loc_5E58")

    label("loc_5D48")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56IEarth Sepith x500\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x0, 500)
    SubItemNumber(0x179, 1)
    Jump("loc_5E58")

    label("loc_5D7E")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58IFire Sepith x500\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x2, 500)
    SubItemNumber(0x17A, 1)
    Jump("loc_5E58")

    label("loc_5DB3")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57IWater Sepith x500\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x1, 500)
    SubItemNumber(0x17B, 1)
    Jump("loc_5E58")

    label("loc_5DE9")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60ITime Sepith x500\x01\x07\x02",
            "#61ISpace Sepith x500\x01\x07\x02",
            "#62IMirage Sepith x500\x01\x07\x00",
            " obtained.\x02",
        )
    )

    AddSepith(0x4, 500)
    AddSepith(0x5, 500)
    AddSepith(0x6, 500)
    SubItemNumber(0x17C, 1)
    Jump("loc_5E58")

    label("loc_5E58")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E7E")

    label("loc_5E74")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E7E")

    Jump("loc_3B8E")

    label("loc_5E83")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5EC2")

    label("loc_5E92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EA6")
    Jump("loc_5EC2")

    label("loc_5EA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EC2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(2, 4)

    label("loc_5EC2")

    Jump("loc_3AF6")

    label("loc_5EC7")

    Jump("loc_5ECF")

    label("loc_5ECC")

    Call(2, 4)

    label("loc_5ECF")

    TalkEnd(0xB)
    Return()

    # Function_3_3AB1 end

    def Function_4_5ED3(): pass

    label("Function_4_5ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD7")

    ChrTalk(
        0xFE,
        (
            "Having something like that happened,\x01",
            "I understand him being worried, but...\x01",
            "For my husband to come to the store too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hu hu, but it's true that I feel more secure.\x01",
            "Might as well make sales as\x01",
            "a married couple from now on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_605E")

    label("loc_5FD7")


    ChrTalk(
        0xFE,
        (
            "My husband also lost his job of \x01",
            "procuring fish from abroad, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Might as well make sales as\x01",
            "a married couple from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_605E")

    Jump("loc_6F67")

    label("loc_6063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6071")
    Jump("loc_6F67")

    label("loc_6071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_61D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A1")

    ChrTalk(
        0xFE,
        (
            "I received a call from my husband working\x01",
            "abroad saying he's coming back home soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, they say that today is going\x01",
            "to be the last day of railroad flights \x01",
            "before the service is stopped for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I wonder if he'll be\x01",
            "able to come home safely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_61D4")

    label("loc_61A1")


    ChrTalk(
        0xFE,
        (
            "Aah, my husband...\x01",
            "I hope he comes back fast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D4")

    Jump("loc_6F67")

    label("loc_61D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_628F")

    ChrTalk(
        0xFE,
        (
            "The red jerseys kids who were\x01",
            "mischievous around here before\x01",
            "have been hurt in the recent raid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm, that's worrisome...\x01",
            "I'd like to see them healthy quick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F67")

    label("loc_628F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_62EA")

    ChrTalk(
        0xFE,
        "To think that such an incident happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aah, what an anxiety...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F67")

    label("loc_62EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6416")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A7")

    ChrTalk(
        0xFE,
        (
            "This morning a Bracer \x01",
            "came for an inquiry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that some Bracer\x01",
            "girls have disappeared?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where they went\x01",
            "on this day of bad weather.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6411")

    label("loc_63A7")


    ChrTalk(
        0xFE,
        (
            "Where could those \x01",
            "Bracer girls have gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where they went\x01",
            "on this day of bad weather.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6411")

    Jump("loc_6F67")

    label("loc_6416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_648D")

    ChrTalk(
        0xFE,
        (
            "My husband procures saltwater\x01",
            "fish in the Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if he got some nice fish.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F67")

    label("loc_648D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_663B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65A6")

    ChrTalk(
        0xFE,
        (
            "When you try to eat freshwater\x01",
            "fish normally, many smell of\x01",
            "mud and earth.\x02",
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
            "Compared to salt water\x01",
            "fish you can eat quickly,\x01",
            "they're a bit bothersome.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6636")

    label("loc_65A6")


    ChrTalk(
        0xFE,
        (
            "If you temporarily soak freshwater fish in\x01",
            "milk, you can take away their smell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should give it a try when\x01",
            "you're cooking at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6636")

    Jump("loc_6F67")

    label("loc_663B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_681C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_678C")

    ChrTalk(
        0xFE,
        (
            "As for Crossbell revenues,\x01",
            "it's decided that about 10% go\x01",
            "to the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Crossbell becomes independent,\x01",
            "that decision will become void and\x01",
            "even our life will become easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Naturally there would be concerns\x01",
            "about the security aspect, but...\x01",
            "If possible, I'd like it became real.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6817")

    label("loc_678C")


    ChrTalk(
        0xFE,
        "I too agree with Crossbell independence.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we were to get freed from\x01",
            "unreasonable revenues, our\x01",
            "lives too would become easier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6817")

    Jump("loc_6F67")

    label("loc_681C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6993")

    ChrTalk(
        0xFE,
        (
            "It appears that the Empire\x01",
            "Chancellor is quite the clever man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is said that if you eat\x01",
            "fish, you get clever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I thought, he must've\x01",
            "grown eating plenty of fish.\x02",
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
            "#00000F...Somehow a funnily\x01",
            "normal image came\x01",
            "up to my mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6A10")

    label("loc_6993")


    ChrTalk(
        0xFE,
        (
            "It is said that if you eat\x01",
            "fish, you get clever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even the Empire Chancellor\x01",
            "must've grown eating\x01",
            "plenty of fish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A10")

    Jump("loc_6F67")

    label("loc_6A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6BCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B1A")

    ChrTalk(
        0xFE,
        (
            "It seems that border gates security\x01",
            "too has become pretty strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A buyer from the Republic was\x01",
            "grumbling about the time the entry\x01",
            "papers repeatedly take from him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "VIPs entering from all countries\x01",
            "is something serious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6BCA")

    label("loc_6B1A")


    ChrTalk(
        0xFE,
        (
            "A buyer from the Republic was\x01",
            "grumbling about the time the entry\x01",
            "papers repeatedly take from him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that border gates security\x01",
            "too has become pretty strict...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BCA")

    Jump("loc_6F67")

    label("loc_6BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D0B")

    ChrTalk(
        0xFE,
        (
            "In the Fisherman's Guild building now\x01",
            "there's the..."Fishing Emperor Club", is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was something like the\x01",
            ""Fisherman's Guild" that had been\x01",
            "there until a little while before, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They almost never socialize with the\x01",
            "neighborhood. Somehow they're suspicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6DAD")

    label("loc_6D0B")


    ChrTalk(
        0xFE,
        (
            "The "Fishing Emperor Club"...\x01",
            "They're simply suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They look like to be a gathering of\x01",
            "fishing lovers so it seems they're\x01",
            "not bad people, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DAD")

    Jump("loc_6F67")

    label("loc_6DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6E41")

    ChrTalk(
        0xFE,
        (
            "Hmm, today the weather\x01",
            "is unfavorable, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if it's just like this I\x01",
            "can't close shop, though.\x01",
            "Look all you want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F67")

    label("loc_6E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6F67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EF2")

    ChrTalk(
        0xFE,
        "Do you want some fresh fish?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way...\x01",
            "Recently I didn't see the people\x01",
            "of that Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Where did they go, I wonder?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6F67")

    label("loc_6EF2")


    ChrTalk(
        0xFE,
        (
            "I wonder where the people of\x01",
            "the Fisherman's Guild went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were funny people...\x01",
            "Not seeing them is sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F67")

    Return()

    # Function_4_5ED3 end

    def Function_5_6F68(): pass

    label("Function_5_6F68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_6F76")
    SetScenarioFlags(0x2, 3)

    label("loc_6F76")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_6F84")
    SetScenarioFlags(0x2, 3)

    label("loc_6F84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_6F92")
    SetScenarioFlags(0x2, 3)

    label("loc_6F92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_6FA0")
    SetScenarioFlags(0x2, 3)

    label("loc_6FA0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_6FAE")
    SetScenarioFlags(0x2, 3)

    label("loc_6FAE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_6FBC")
    SetScenarioFlags(0x2, 3)

    label("loc_6FBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_6FCA")
    SetScenarioFlags(0x2, 3)

    label("loc_6FCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_6FD8")
    SetScenarioFlags(0x2, 3)

    label("loc_6FD8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_6FE6")
    SetScenarioFlags(0x2, 3)

    label("loc_6FE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_6FF4")
    SetScenarioFlags(0x2, 3)

    label("loc_6FF4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_7002")
    SetScenarioFlags(0x2, 3)

    label("loc_7002")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_7010")
    SetScenarioFlags(0x2, 3)

    label("loc_7010")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_701E")
    SetScenarioFlags(0x2, 3)

    label("loc_701E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_702C")
    SetScenarioFlags(0x2, 3)

    label("loc_702C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_703A")
    SetScenarioFlags(0x2, 3)

    label("loc_703A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_7048")
    SetScenarioFlags(0x2, 3)

    label("loc_7048")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_7056")
    SetScenarioFlags(0x2, 3)

    label("loc_7056")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_7064")
    SetScenarioFlags(0x2, 3)

    label("loc_7064")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_7072")
    SetScenarioFlags(0x2, 3)

    label("loc_7072")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_7080")
    SetScenarioFlags(0x2, 3)

    label("loc_7080")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_708E")
    SetScenarioFlags(0x2, 3)

    label("loc_708E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_709C")
    SetScenarioFlags(0x2, 3)

    label("loc_709C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_70AA")
    SetScenarioFlags(0x2, 3)

    label("loc_70AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_70B8")
    SetScenarioFlags(0x2, 3)

    label("loc_70B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_END)), "loc_70C6")
    SetScenarioFlags(0x2, 3)

    label("loc_70C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_END)), "loc_70D4")
    SetScenarioFlags(0x2, 3)

    label("loc_70D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_END)), "loc_70E2")
    SetScenarioFlags(0x2, 3)

    label("loc_70E2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_END)), "loc_70F0")
    SetScenarioFlags(0x2, 3)

    label("loc_70F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_END)), "loc_70FE")
    SetScenarioFlags(0x2, 3)

    label("loc_70FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_END)), "loc_710C")
    SetScenarioFlags(0x2, 3)

    label("loc_710C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_END)), "loc_711A")
    SetScenarioFlags(0x2, 3)

    label("loc_711A")

    Return()

    # Function_5_6F68 end

    def Function_6_711B(): pass

    label("Function_6_711B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712E")
    MenuCmd(3, 1, 0x0)

    label("loc_712E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7141")
    MenuCmd(3, 1, 0x1)

    label("loc_7141")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7154")
    MenuCmd(3, 1, 0x2)

    label("loc_7154")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7167")
    MenuCmd(3, 1, 0x3)

    label("loc_7167")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_717A")
    MenuCmd(3, 1, 0x4)

    label("loc_717A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_718D")
    MenuCmd(3, 1, 0x5)

    label("loc_718D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71A0")
    MenuCmd(3, 1, 0x6)

    label("loc_71A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71B3")
    MenuCmd(3, 1, 0x7)

    label("loc_71B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71C6")
    MenuCmd(3, 1, 0x8)

    label("loc_71C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71D9")
    MenuCmd(3, 1, 0x9)

    label("loc_71D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71EC")
    MenuCmd(3, 1, 0xA)

    label("loc_71EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71FF")
    MenuCmd(3, 1, 0xB)

    label("loc_71FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7212")
    MenuCmd(3, 1, 0xC)

    label("loc_7212")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7225")
    MenuCmd(3, 1, 0xD)

    label("loc_7225")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7238")
    MenuCmd(3, 1, 0xE)

    label("loc_7238")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_724B")
    MenuCmd(3, 1, 0xF)

    label("loc_724B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_725E")
    MenuCmd(3, 1, 0x10)

    label("loc_725E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7271")
    MenuCmd(3, 1, 0x11)

    label("loc_7271")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7284")
    MenuCmd(3, 1, 0x12)

    label("loc_7284")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7297")
    MenuCmd(3, 1, 0x13)

    label("loc_7297")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72AA")
    MenuCmd(3, 1, 0x14)

    label("loc_72AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72BD")
    MenuCmd(3, 1, 0x15)

    label("loc_72BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72D0")
    MenuCmd(3, 1, 0x16)

    label("loc_72D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72E3")
    MenuCmd(3, 1, 0x17)

    label("loc_72E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72F6")
    MenuCmd(3, 1, 0x18)

    label("loc_72F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7309")
    MenuCmd(3, 1, 0x19)

    label("loc_7309")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_731C")
    MenuCmd(3, 1, 0x1A)

    label("loc_731C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_732F")
    MenuCmd(3, 1, 0x1B)

    label("loc_732F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7342")
    MenuCmd(3, 1, 0x1C)

    label("loc_7342")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7355")
    MenuCmd(3, 1, 0x1D)

    label("loc_7355")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7368")
    MenuCmd(3, 1, 0x1E)

    label("loc_7368")

    Return()

    # Function_6_711B end

    def Function_7_7369(): pass

    label("Function_7_7369")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_74A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_742A")

    ChrTalk(
        0xFE,
        (
            "President Dieter has\x01",
            "been restrained!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Arresting a country's\x01",
            "top is unprecedented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what will become of the\x01",
            "autonomous state of Crossbell...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_74A2")

    label("loc_742A")


    ChrTalk(
        0xFE,
        (
            "Arresting a country's\x01",
            "top is unprecedented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what will become of the\x01",
            "autonomous state of Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74A2")

    Jump("loc_7E8F")

    label("loc_74A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_74B5")
    Jump("loc_7E8F")

    label("loc_74B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_755E")

    ChrTalk(
        0xFE,
        (
            "I too saw the Mayor...no,\x01",
            "President Dieter's speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being this the situation, I'd\x01",
            "like he to do his best to go\x01",
            "towards independence thoroughly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E8F")

    label("loc_755E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7629")

    ChrTalk(
        0xFE,
        (
            "It looks like the big bell that was\x01",
            "in Central Square has been stolen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There aren't even concrete\x01",
            "rumors about why such a\x01",
            "thing has been stolen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, it's somewhat weird.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E8F")

    label("loc_7629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_76BB")

    ChrTalk(
        0xFE,
        "The mining town facts worry me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems the CGF is moving\x01",
            "to resolve the situation, but\x01",
            "will they be fine, I wonder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E8F")

    label("loc_76BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_774D")

    ChrTalk(
        0xFE,
        (
            "I was really shocked by\x01",
            "yesterday's train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, I'm glad that for the time\x01",
            "being it's been quickly repaired.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E8F")

    label("loc_774D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_77E2")

    ChrTalk(
        0xFE,
        (
            "The Republican passengers bus\x01",
            "passed through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Weird...\x01",
            "That bus should be in service\x01",
            "only up to the east entrance stop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E8F")

    label("loc_77E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_793C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78C7")

    ChrTalk(
        0xFE,
        (
            "It seems that the independence proposal\x01",
            "was an idea the mayor was mulling over, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what Chairman\x01",
            "MacDowell thinks about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would really want to\x01",
            "hear his opinion about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7937")

    label("loc_78C7")


    ChrTalk(
        0xFE,
        (
            "I am still undecided\x01",
            "about what to vote.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would really want to hear\x01",
            "Chairman MacDowell opinion too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7937")

    Jump("loc_7E8F")

    label("loc_793C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7AD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A3D")

    ChrTalk(
        0xFE,
        (
            "As you can imagine, even an old lady like me \x01",
            "was surprised by the independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I too think it's good that\x01",
            "Crossbell asks for more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever they may say, we're the\x01",
            "continent foremost trade city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7AD2")

    label("loc_7A3D")


    ChrTalk(
        0xFE,
        (
            "I think it's good that Crossbell asks\x01",
            "for more from the foreign countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever they may say, we're the\x01",
            "continent foremost trade city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AD2")

    Jump("loc_7E8F")

    label("loc_7AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7B6B")

    ChrTalk(
        0xFE,
        "Today is finally the Trade Conference day.\x02",
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
    Jump("loc_7E8F")

    label("loc_7B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7BCF")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower unveiling\x01",
            "was amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was surprised and\x01",
            "my knees gave away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E8F")

    label("loc_7BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7C46")

    ChrTalk(
        0xFE,
        (
            "Today you can often spot\x01",
            "policemen doing security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow it feels like\x01",
            "the city is flurried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E8F")

    label("loc_7C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7CBB")

    ChrTalk(
        0xFE,
        (
            "Hum hum huuum♪\x01",
            "Since I was a child,\x01",
            "I love the rain a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Am I a bit immature, perhaps?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E8F")

    label("loc_7CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7E8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DD1")

    ChrTalk(
        0xFE,
        (
            "It seems that the "Trade Conference" is\x01",
            "going to be held at the end of the month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only the Empire and Republic\x01",
            "big wigs are invited, but also those\x01",
            "of Liberl and Remiferia, they say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Somehow it appears\x01",
            "it's going to a big event.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7E8F")

    label("loc_7DD1")


    ChrTalk(
        0xFE,
        (
            "It seems that the "Trade Conference" is\x01",
            "going to be held at the end of the month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that many big wigs are going to come,\x01",
            "and so it appears it is going to be a big event.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E8F")

    TalkEnd(0xFE)
    Return()

    # Function_7_7369 end

    def Function_8_7E93(): pass

    label("Function_8_7E93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7FB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F57")

    ChrTalk(
        0xFE,
        (
            "Even if President Dieter disappears,\x01",
            "there's Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's the Chairman, I'm sure he'll be able\x01",
            "to restore the situation in a way or another.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7FAE")

    label("loc_7F57")


    ChrTalk(
        0xFE,
        (
            "If it's Chairman MacDowell, I'm sure he'll\x01",
            "quell even this situation in some way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FAE")

    Jump("loc_8E32")

    label("loc_7FB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7FC1")
    Jump("loc_8E32")

    label("loc_7FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8156")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80B1")

    ChrTalk(
        0xFE,
        (
            "To think that sir Arios the Bracer\x01",
            "was appointed Secretary of Defence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, thinking about his achievements,\x01",
            "he could be a valid personnel choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sir Dieter decision must \x01",
            "really be spot on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8151")

    label("loc_80B1")


    ChrTalk(
        0xFE,
        (
            "Thinking about sir Arios' achievements,\x01",
            "appointing him as Secretary of Defense is proper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, he could be said to\x01",
            "be Crossbell guardian deity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8151")

    Jump("loc_8E32")

    label("loc_8156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8264")

    ChrTalk(
        0xFE,
        (
            "Who would've thought an\x01",
            "incident like that would\x01",
            "happen in  Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't get away from my mind the\x01",
            "screams of the giant demon-like monster \x01",
            "I could hear coming from Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*...I won't be able to sleep today too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_830B")

    label("loc_8264")


    ChrTalk(
        0xFE,
        (
            "I can't get away from my mind the\x01",
            "screams of the giant demon-like monster \x01",
            "I could hear during the raid attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*...I won't be able to sleep today too.\x02",
    )

    CloseMessageWindow()

    label("loc_830B")

    Jump("loc_8E32")

    label("loc_8310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_848D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8403")

    ChrTalk(
        0xFE,
        (
            "The occupation of Mainz, eh...?\x01",
            "It's become something serious.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the sake of the independence\x01",
            "the mayor has proposed, we can't\x01",
            "expect the Empire or Republic help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmmm, what's going to happen...\x01\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8488")

    label("loc_8403")


    ChrTalk(
        0xFE,
        (
            "For the sake of the proposed\x01",
            "independence, we can't expect\x01",
            "the Empire or Republic help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmmm, what's going to happen...\x01\x02",
    )

    CloseMessageWindow()

    label("loc_8488")

    Jump("loc_8E32")

    label("loc_848D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_849B")
    Jump("loc_8E32")

    label("loc_849B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_851D")

    ChrTalk(
        0xFE,
        (
            "It appears that ambulances passed\x01",
            "through the Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear me...\x01",
            "Could an accident have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E32")

    label("loc_851D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_862E")

    ChrTalk(
        0xFE,
        (
            "This local referendum...\x01",
            "Even among my acquaintances\x01",
            "there's much talk about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, you can't get swept by\x01",
            "the opinions surrounding you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter who it is, this is\x01",
            "not someone else's business.\x01",
            "You must think about it well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_870F")

    label("loc_862E")


    ChrTalk(
        0xFE,
        (
            "Each person must think about it carefully; \x01",
            "if it's not a vote casted with your own\x01",
            "intention, then there's no mean in voting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter who it is, this is\x01",
            "not someone else's business.\x01",
            "You must think about it well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_870F")

    Jump("loc_8E32")

    label("loc_8714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_88D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_884A")

    ChrTalk(
        0xFE,
        (
            "As someone who knows this\x01",
            "land's history, I wish it wins its\x01",
            "independence by all means possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it is a fact that peace is\x01",
            "guaranteed because we're substantially\x01",
            "under the control of the Empire and Republic....\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm...\x01",
            "I seems this needs to be thought well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_88D4")

    label("loc_884A")


    ChrTalk(
        0xFE,
        (
            "Enjoying peace as a subordinate state?\x01",
            "Or letting that go and be independent...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm...\x01",
            "I seems this needs to be thought well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88D4")

    Jump("loc_8E32")

    label("loc_88D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C2")

    ChrTalk(
        0xFE,
        (
            "It appears that Orchis Tower\x01",
            "perimeter has been sealed\x01",
            "since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too wanted to see with my own\x01",
            "eyes all countries' VIPs, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thinking about security,\x01",
            "maybe it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8A50")

    label("loc_89C2")


    ChrTalk(
        0xFE,
        (
            "It appear that Orchis Tower perimeter \x01",
            "has been sealed since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too wanted to see with my own\x01",
            "eyes all countries VIPs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A50")

    Jump("loc_8E32")

    label("loc_8A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B53")

    ChrTalk(
        0xFE,
        (
            "President Rocksmith's limousine\x01",
            "has passed through this road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected from a President's\x01",
            "car it had a gorgeous white and \x01",
            "gold body frame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you searched the continent\x01",
            "you probably wouldn't find\x01",
            "such a car.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8BD7")

    label("loc_8B53")


    ChrTalk(
        0xFE,
        (
            "President Rocksmith's limousine\x01",
            "was indeed gorgeous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you searched the continent\x01",
            "you probably wouldn't find\x01",
            "such a car.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BD7")

    Jump("loc_8E32")

    label("loc_8BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8C99")

    ChrTalk(
        0xFE,
        (
            "The VIPs from all countries\x01",
            "are said to be coming to\x01",
            "Crossbell in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it's a rare opportunity,\x01",
            "it would be nice if I could\x01",
            "see them with my own eyes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E32")

    label("loc_8C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8CA7")
    Jump("loc_8E32")

    label("loc_8CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DAA")

    ChrTalk(
        0xFE,
        (
            "The new Mayor, Mr. Dieter, appears\x01",
            "to be zealously ruling cooperating\x01",
            "well with Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That the Mayor and the Chairman cooperate\x01",
            "was something impossible to think in the past.\x01",
            "Hohho, it's really a nice thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8E32")

    label("loc_8DAA")


    ChrTalk(
        0xFE,
        (
            "The new Mayor, Mr. Dieter,\x01",
            "has always displayed his \x01",
            "ability as the IBC president.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hohho, I truly look\x01",
            "forward to the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E32")

    TalkEnd(0xFE)
    Return()

    # Function_8_7E93 end

    def Function_9_8E36(): pass

    label("Function_9_8E36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F67")
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xFE,
        (
            "The President getting restrained,\x01",
            "an ominous azure pale tree appearing...\x01",
            "Somehow many things are happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if we'll be able to go back\x01",
            "fully to our old daily lives...\x02",
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
        "Ha ha, it's nothing.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_93(0xF, 0x10E, 0x0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_8FFC")

    label("loc_8F67")


    ChrTalk(
        0xFE,
        "...Well, whatever will be, will be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The most important thing to me\x01",
            "is protecting Meiling...\x01",
            "As long as I don't forget that, it'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FFC")

    Jump("loc_9F0A")

    label("loc_9001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_900F")
    Jump("loc_9F0A")

    label("loc_900F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_91E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9113")

    ChrTalk(
        0xFE,
        (
            "To have an eye kept on from\x01",
            "the Empire and Republic\x01",
            "is indeed scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However...it's for Crossbell's sake.\x01",
            "We citizens must prepare for the worst too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, no matter what will happen,\x01",
            "I'll protect at least Meiling.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_91DF")

    label("loc_9113")


    ChrTalk(
        0xFE,
        (
            "When I asked Mr. Cronk that\x01",
            "I wanted to have Meiling near me,\x01",
            "he gave me a pleasant ok.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad he's an understandable man.\x01",
            "If she's in a place where I can keep\x01",
            "an eye on her, I feel relieved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91DF")

    Jump("loc_9F0A")

    label("loc_91E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_91F2")
    Jump("loc_9F0A")

    label("loc_91F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9359")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C1")

    ChrTalk(
        0xFE,
        (
            "They say that an armed group\x01",
            "has appeared in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone like them showing up in town...\x01",
            "It must feel fairly dreadful...\x02",
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
    Jump("loc_9354")

    label("loc_92C1")


    ChrTalk(
        0xFE,
        (
            "What's wrong with Meiling I wonder...\x01",
            "Lately she's boisterous. I'm worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe today I'll finish work\x01",
            "earlier and go home together...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9354")

    Jump("loc_9F0A")

    label("loc_9359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_954B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9499")

    ChrTalk(
        0xFE,
        (
            "I gave the pinwheels I made\x01",
            "at my part-time job and turned\x01",
            "bad to Meiling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, no matter what she said\x01",
            "she wanted to play with those \x01",
            "today and didn't listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, I don't want to walk\x01",
            "around on a rainy day, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, Meiling is having fun,\x01",
            "so it's all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9546")

    label("loc_9499")


    ChrTalk(
        0xFE,
        (
            "However, to think she could be\x01",
            "that happy with such junk-like\x01",
            "failed products...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Next time, I'll have to\x01",
            "gave her as a present one\x01",
            "that has been properly made.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9546")

    Jump("loc_9F0A")

    label("loc_954B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_95DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95C9")

    ChrTalk(
        0xFE,
        (
            "Hmmm...\x01",
            "The pinwheels I make\x01",
            "aren't selling at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wait, what!?\x01",
            "When did they sell!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_95D9")

    label("loc_95C9")


    ChrTalk(
        0xFE,
        "*agape*...\x02",
    )

    CloseMessageWindow()

    label("loc_95D9")

    Jump("loc_9F0A")

    label("loc_95DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_96A6")

    ChrTalk(
        0xFE,
        (
            "I could finally get 1 of the\x01",
            "pinwheels I made with a lot of\x01",
            "efforts to be exposed in the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having something you made\x01",
            "yourself exposed in a store...\x01",
            "How to say, it's nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F0A")

    label("loc_96A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_97FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_978F")

    ChrTalk(
        0xFE,
        (
            "Mr. Cronk makes\x01",
            "such uncredible\x01",
            "models...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had faith in my ability with\x01",
            "the hands, but until now I do\x01",
            "nothing but fail in making pinwheels...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, somehow it seems\x01",
            "I'm losing confidence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_97F5")

    label("loc_978F")


    ChrTalk(
        0xFE,
        (
            "In any case, today I'll\x01",
            "work on other odd jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*phew*... Earning mira\x01",
            "by working is tough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97F5")

    Jump("loc_9F0A")

    label("loc_97FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_992B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98BF")

    ChrTalk(
        0xFE,
        (
            "When I asked Mr. Cronk,\x01",
            "he unexpectedly readily\x01",
            "decided to let me work here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "U-Uhhm...\x01",
            "Since I was looking for a job at a\x01",
            "stall since the beginning, I'm happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9926")

    label("loc_98BF")


    ChrTalk(
        0xFE,
        (
            "How to make simple handicrafts,\x01",
            "mira management...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to learn the job little by little.\x02",
    )

    CloseMessageWindow()

    label("loc_9926")

    Jump("loc_9F0A")

    label("loc_992B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9A80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A02")

    ChrTalk(
        0xFE,
        "Hmm, handicrafts, eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm quite skilled with my hands\x01",
            "and maybe I could unexpectedly\x01",
            "be suited for such an artisan-like job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, would he\x01",
            "hire me, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xF, 0x10)
    Jump("loc_9A7B")

    label("loc_9A02")


    ChrTalk(
        0xFE,
        (
            "If I made these kind of pinwheels,\x01",
            "even Meiling could be happy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-All right...\x01",
            "Let's make a try and ask him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A7B")

    Jump("loc_9F0A")

    label("loc_9A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B9E")
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xFE,
        (
            "*sigh*, I reached an impasse\x01",
            "in looking for a job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Bro, why don't you try\x01",
            "asking all the stores\x01",
            "over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "M-Moron.\x01",
            "If I did a street stall job, I'd\x01",
            "stand out and it'd be embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want an easier job\x01",
            "I can do indoor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xF, 0x10)
    Jump("loc_9C30")

    label("loc_9B9E")


    ChrTalk(
        0xFE,
        (
            "Hmmm, street stalls, eh...?\x01",
            "They're not in my character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I almost tried\x01",
            "already works I can think\x01",
            "of aside from street stalls.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C30")

    Jump("loc_9F0A")

    label("loc_9C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9CCF")

    ChrTalk(
        0xFE,
        (
            "Today, with the occasion of shopping\x01",
            "with Meiling, I went for a walk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Boy oh boy...\x01",
            "Kids have a lot of energies even if it rains.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F0A")

    label("loc_9CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DC7")

    ChrTalk(
        0xFE,
        (
            "Just before, a redheaded man\x01",
            "suddenly addressed me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Saying "Get worried more, that's youth!"\x01",
            "he walked like that to Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...S-Somehow he looked more\x01",
            "irresponsible of a guy than me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9E49")

    label("loc_9DC7")


    ChrTalk(
        0xFE,
        (
            "The redheaded man from before?\x01",
            "He walked to Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...S-Somehow he looked more\x01",
            "irresponsible of a guy than me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E49")

    Jump("loc_9F0A")

    label("loc_9E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EE6")

    ChrTalk(
        0xFE,
        (
            "A little while ago I started \x01",
            "to look for a job, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I can't get\x01",
            "employed at all.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've already lost heart.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9F0A")

    label("loc_9EE6")


    ChrTalk(
        0xFE,
        "I can't get employed at all.\x01\x01\x02",
    )

    CloseMessageWindow()

    label("loc_9F0A")

    TalkEnd(0xFE)
    Return()

    # Function_9_8E36 end

    def Function_10_9F0E(): pass

    label("Function_10_9F0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9F88")

    ChrTalk(
        0xFE,
        (
            "Somehow big bro\x01",
            "is being gloomy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Enough with complicated things\x01",
            "and come play with Meiling☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAAD")

    label("loc_9F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_9F96")
    Jump("loc_AAAD")

    label("loc_9F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A029")

    ChrTalk(
        0xFE,
        (
            "Today, big bro \x01",
            "called me to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eheheh, there's even three \x01",
            ""whirl whirls" made by big bro.\x01",
            "May they sell!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A080")

    label("loc_A029")


    ChrTalk(
        0xFE,
        (
            "He says that if Meiling\x01",
            "helps, she can get\x01",
            ""whirl whirls".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eheheh, how fun♪\x02",
    )

    CloseMessageWindow()

    label("loc_A080")

    Jump("loc_AAAD")

    label("loc_A085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A15C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A101")

    ChrTalk(
        0xFE,
        (
            "Grandpa and big bro\x01",
            "went somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess that Meiling will\x01",
            "play at Grandma's today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A157")

    label("loc_A101")


    ChrTalk(
        0xFE,
        (
            "Grandpa and big bro\x01",
            "are doing kya...kyar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kyarity?\x01",
            "That's what they said.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A157")

    Jump("loc_AAAD")

    label("loc_A15C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A21A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1F9")

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
            "That's why, even if Meiling is said,\x01",
            "she'll cheer for big bro!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_A215")

    label("loc_A1F9")


    ChrTalk(
        0xFE,
        "Do your best, big bro!\x02",
    )

    CloseMessageWindow()

    label("loc_A215")

    Jump("loc_AAAD")

    label("loc_A21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A2B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A278")

    ChrTalk(
        0xFE,
        (
            "This is a whirl whirl\x01",
            "big bro made!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It spins and spins♪\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A2B2")

    label("loc_A278")


    ChrTalk(
        0xFE,
        (
            "This whirl whirl was\x01",
            "made by big bro!\x01",
            "It's amazing♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2B2")

    Jump("loc_AAAD")

    label("loc_A2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A2FC")

    ChrTalk(
        0xFE,
        (
            "Grandpa has got\x01",
            "a serious face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Boring...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AAAD")

    label("loc_A2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A3D4")
    OP_4B(0x14, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A378")

    ChrTalk(
        0xFE,
        (
            "Grampa,\x01",
            "beard beard☆\x02",
        )
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
            "Ow ow ow ow...\x01",
            "Now now, don't pull it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A3CB")

    label("loc_A378")


    ChrTalk(
        0xFE,
        "*pull, puuull*♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "M-Meiling, you're\x01",
            "unexpectedly strong...\x01",
            "Ow ow ow ow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3CB")

    OP_4C(0x14, 0xFF)
    Jump("loc_AAAD")

    label("loc_A3D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A4A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A46A")

    ChrTalk(
        0xFE,
        (
            "It looks like that big bro\x01",
            "is working with all his might.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I'd wish he played\x01",
            "with Meiling too...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrFlags(0xFE, 0x10)
    Jump("loc_A4A3")

    label("loc_A46A")


    ChrTalk(
        0xFE,
        (
            "Big bro, Meiling wants\x01",
            "to be with you too!\x01",
            "...*sob*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4A3")

    Jump("loc_AAAD")

    label("loc_A4A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A556")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A523")

    ChrTalk(
        0xFE,
        (
            "It seems that big bro is\x01",
            "working at the whirl whirl store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm happy he found a job!\x01\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A551")

    label("loc_A523")


    ChrTalk(
        0xFE,
        (
            "I'm happy, but...\x01",
            "A little sad.\x01",
            "...*sob*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A551")

    Jump("loc_AAAD")

    label("loc_A556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A6D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A650")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "The spinning whirl\x01",
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
            "Whoa, Meiling!?\x01",
            "Aren't your eyes spinning around!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Spin spin dizzy dizzy...\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Jump("loc_A6D4")

    label("loc_A650")

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
            "(*wobble wobble*)\x01",
            "I'm aaaokaay...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "You're not, aren't you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)

    label("loc_A6D4")

    Jump("loc_AAAD")

    label("loc_A6D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A81E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7BC")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Big bro, lately you don't\x01",
            "play with me at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Find a job fast and\x01",
            "play with Meiling!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "*sigh*, it would be nice if it\x01",
            "were something that easy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_A819")

    label("loc_A7BC")


    ChrTalk(
        0xFE,
        (
            "Meiling too will help\x01",
            "big bro finding a job!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When we find it,\x01",
            "let's play together!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A819")

    Jump("loc_AAAD")

    label("loc_A81E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A94A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8E5")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "*dum de dum...*♪\x01",
            "Uhhm, what a good smell!\x02",
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
    Jump("loc_A945")

    label("loc_A8E5")


    ChrTalk(
        0xFE,
        (
            "Meiling went with big\x01",
            "bro to shop at the\x01",
            "bakery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhhm, it's so warm and smells good☆\x02",
    )

    CloseMessageWindow()

    label("loc_A945")

    Jump("loc_AAAD")

    label("loc_A94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_AAAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9B9")

    ChrTalk(
        0xFE,
        (
            "A redheaded man rubbed\x01",
            "big bro's shoulder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Meiling too wants to do that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AAAD")

    label("loc_A9B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA5C")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        "Big bro, cheer up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you can't find a job,\x01",
            "Meiling is at your side!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "M-Meiliiing...\x01",
            "You, only you, are my ally.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xF, 0xFF)
    Jump("loc_AAAD")

    label("loc_AA5C")


    ChrTalk(
        0xFE,
        (
            "Not having a job, big\x01",
            "bro doesn't feel well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meiling must\x01",
            "console him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAAD")

    TalkEnd(0xFE)
    Return()

    # Function_10_9F0E end

    def Function_11_AAB1(): pass

    label("Function_11_AAB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_AB3D")

    ChrTalk(
        0xFE,
        (
            "It appears that many\x01",
            "ambulances have been coming\x01",
            "and going it the city since before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, I've got a bad omen...\x02",
    )

    CloseMessageWindow()
    Jump("loc_ACF0")

    label("loc_AB3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_ACF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC4E")

    ChrTalk(
        0xFE,
        (
            "Roy, my grandchild, has\x01",
            "finally begun to work.\x01",
            "And at the street stalls quarter, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too, when I was young,\x01",
            "was working there. For some\x01",
            "reason, it's deeply moving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's good he's\x01",
            "doing his best.\x01",
            "I'll watch over him too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_ACF0")

    label("loc_AC4E")


    ChrTalk(
        0xFE,
        (
            "Because he took a holiday,\x01",
            "today I'm in charge of\x01",
            "taking care of Meiling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see, since it's a rare\x01",
            "opportunity, I guess I'll\x01",
            "play as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACF0")

    TalkEnd(0xFE)
    Return()

    # Function_11_AAB1 end

    def Function_12_ACF4(): pass

    label("Function_12_ACF4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AE75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADE2")

    ChrTalk(
        0xFE,
        (
            "The men in my home, somehow,\x01",
            "have become nicer to me lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I wonder how many years have passed\x01",
            "since I came shopping together with Gilles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, such moments\x01",
            "could be a little fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AE70")

    label("loc_ADE2")


    ChrTalk(
        0xFE,
        (
            "Uh uh, I wonder how many years have passed\x01",
            "since I came shopping together with Gilles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, such moments\x01",
            "could be a little fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE70")

    Jump("loc_B65F")

    label("loc_AE75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AE83")
    Jump("loc_B65F")

    label("loc_AE83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AE91")
    Jump("loc_B65F")

    label("loc_AE91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AFF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF73")

    ChrTalk(
        0xFE,
        (
            "Due to the recent incident,\x01",
            "my men's workplace went\x01",
            "on holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having them all at home doubles\x01",
            "the housework toughness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm thankful they're\x01",
            "helping me differently\x01",
            "from before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AFEF")

    label("loc_AF73")


    ChrTalk(
        0xFE,
        (
            "Having them all at home doubles\x01",
            "the housework toughness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if my men's workplace\x01",
            "is going to reopen quick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFEF")

    Jump("loc_B65F")

    label("loc_AFF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B002")
    Jump("loc_B65F")

    label("loc_B002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B010")
    Jump("loc_B65F")

    label("loc_B010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B12C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0E1")

    ChrTalk(
        0xFE,
        (
            "*haah*, when you don't have to \x01",
            "do housework is really pleasant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wait, huh!?\x01",
            "Excessive flab on my...abdomen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I really must've been\x01",
            "lazing around too much...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B127")

    label("loc_B0E1")


    ChrTalk(
        0xFE,
        (
            "Really, I guess it's time to\x01",
            "start doing housework once again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B127")

    Jump("loc_B65F")

    label("loc_B12C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B2B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20E")

    ChrTalk(
        0xFE,
        (
            "My men seem to have finally understood\x01",
            "the housework toughness as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They have been asking me\x01",
            "to let them do housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh he, the housework boycotting\x01",
            "plan was a great success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B2AF")

    label("loc_B20E")


    ChrTalk(
        0xFE,
        (
            "My men seem to have finally understood\x01",
            "the housework toughness as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, still, what should I do?\x01",
            "I too want to enjoy it\x01",
            "for a little more...♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2AF")

    Jump("loc_B65F")

    label("loc_B2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B2C2")
    Jump("loc_B65F")

    label("loc_B2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B479")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3E8")

    ChrTalk(
        0xFE,
        (
            "After I started not doing housework, the\x01",
            "meals menu has, really, become simple.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They order deliveries on their own,\x01",
            "waste mira unnecessarily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since ours is a big family, they should\x01",
            "at least economise a little, and yet...\x01",
            "Honestly, men are no good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B474")

    label("loc_B3E8")


    ChrTalk(
        0xFE,
        (
            "...Hah! Why am I again at \x01",
            "the street stalls quarter...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I decided to not do housework,\x01",
            "I shouldn't be coming here anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B474")

    Jump("loc_B65F")

    label("loc_B479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B487")
    Jump("loc_B65F")

    label("loc_B487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B563")

    ChrTalk(
        0xFE,
        (
            "Lately I completely stopped\x01",
            "doing housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After I did that, it already feels pleasant☆\x01",
            "I'm lazing around at home all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I don't care about\x01",
            "my husband and sons.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B643")

    label("loc_B563")


    ChrTalk(
        0xFE,
        (
            "Not doing housework, every\x01",
            "day my men are in a panic.\x01",
            "Uh uh, seeerves them right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, when I go out for a walk, I\x01",
            "unconsciously come to the street stalls quarter.\x01",
            "No, no, I've got an occupational disorder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B643")

    Jump("loc_B65F")

    label("loc_B648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B656")
    Jump("loc_B65F")

    label("loc_B656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B65F")

    label("loc_B65F")

    TalkEnd(0xFE)
    Return()

    # Function_12_ACF4 end

    def Function_13_B663(): pass

    label("Function_13_B663")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B7C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B77E")

    ChrTalk(
        0xFE,
        (
            "As you can imagine, coming alone\x01",
            "worries us. So, we father and sons\x01",
            "take turns accompanying her to shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a bother, but it can't be helped.\x01",
            "If mom got hurt, we couldn't manage.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel that I once again understood\x01",
            "mom's preciousness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B7BB")

    label("loc_B77E")


    ChrTalk(
        0xFE,
        (
            "I feel that I once again understood\x01",
            "mom's preciousness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7BB")

    Jump("loc_BE45")

    label("loc_B7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B7CE")
    Jump("loc_BE45")

    label("loc_B7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B8A2")

    ChrTalk(
        0xFE,
        (
            "Man, how exciting.\x01",
            "It can't be true that Crossbell has\x01",
            "become an independent state...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm earnestly happy, however I\x01",
            "don't have the slightly idea about\x01",
            "what's going to happen from now on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE45")

    label("loc_B8A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B8B0")
    Jump("loc_BE45")

    label("loc_B8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B9EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B990")

    ChrTalk(
        0xFE,
        (
            "At last, mom has re-started\x01",
            "doing housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O-Of course from now on\x01",
            "father and we brothers are\x01",
            "going to share roles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since ours is a big family,\x01",
            "we must help each other properly...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B9E6")

    label("loc_B990")


    ChrTalk(
        0xFE,
        (
            "When mom didn't do housework,\x01",
            "it was really tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Moms are really great...\x02",
    )

    CloseMessageWindow()

    label("loc_B9E6")

    Jump("loc_BE45")

    label("loc_B9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B9F9")
    Jump("loc_BE45")

    label("loc_B9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BA07")
    Jump("loc_BE45")

    label("loc_BA07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BA15")
    Jump("loc_BE45")

    label("loc_BA15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BBA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB03")

    ChrTalk(
        0xFE,
        (
            "Mom not doing housework...\x01",
            "I understood well that toughness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We apologize every day\x01",
            "but she doesn't forgive us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The city is in a clamor about the independence,\x01",
            "but we have our own big problems.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BB9D")

    label("loc_BB03")


    ChrTalk(
        0xFE,
        (
            "We, who never helped with housework\x01",
            "until now, are clearly at fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, we must apologize\x01",
            "to mom assiduously until\x01",
            "she forgives us...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB9D")

    Jump("loc_BE45")

    label("loc_BBA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BBB0")
    Jump("loc_BE45")

    label("loc_BBB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BCF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC6E")

    ChrTalk(
        0xFE,
        (
            "Because mom is skipping housework,\x01",
            "in her stead, father and we brothers\x01",
            "are doing them sharing roles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm in charge of meals.\x01",
            "Uhmm, what should I buy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BCED")

    label("loc_BC6E")


    ChrTalk(
        0xFE,
        (
            "To think that it's so hard to think\x01",
            "about the everyday menu...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mom was doing\x01",
            "this every day.\x01",
            "Honestly, I'm amazed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCED")

    Jump("loc_BE45")

    label("loc_BCF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BD00")
    Jump("loc_BE45")

    label("loc_BD00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BD0E")
    Jump("loc_BE45")

    label("loc_BD0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_BE45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDE3")

    ChrTalk(
        0xFE,
        (
            "Recently, our mom isn't\x01",
            "doing housework at all.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because father and we brothers\x01",
            "almost never helped her, it seems\x01",
            "she finally blew her top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm...\x01",
            "That's a real problem.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BE45")

    label("loc_BDE3")


    ChrTalk(
        0xFE,
        (
            "Mom is livid and\x01",
            "she hasn't been doing\x01",
            "housework at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm...\x01",
            "That's a real problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE45")

    TalkEnd(0xFE)
    Return()

    # Function_13_B663 end

    def Function_14_BE49(): pass

    label("Function_14_BE49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BFB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF31")

    ChrTalk(
        0xFE,
        (
            "Somehow, I have a feeling that the\x01",
            "city got back his former liveliness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too have to buy a lot \x01",
            "and help the economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aaalright, I'll have to rethink once\x01",
            "again my cheap shopping route!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_BFB1")

    label("loc_BF31")


    ChrTalk(
        0xFE,
        (
            "I too have to to buy a lot \x01",
            "and help the economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aaalright, I'll have to rethink once\x01",
            "again my cheap shopping route!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFB1")

    Jump("loc_C937")

    label("loc_BFB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BFC4")
    Jump("loc_C937")

    label("loc_BFC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C04D")

    ChrTalk(
        0xFE,
        (
            "I don't understand well\x01",
            "complicated things yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't the result that everyone\x01",
            "chose the correct one? No?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C937")

    label("loc_C04D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C0D4")

    ChrTalk(
        0xFE,
        (
            "The other day I went to mass at\x01",
            "the church and prayed the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope Crossbell will\x01",
            "become peaceful fast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C937")

    label("loc_C0D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C16C")

    ChrTalk(
        0xFE,
        "Lately it's an incident after another.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's kinda scary, I guess that\x01",
            "today I'll finish my shopping\x01",
            "here and go home earlier...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C937")

    label("loc_C16C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C22E")

    ChrTalk(
        0xFE,
        (
            "Eheheh, goodness, \x01",
            "today I even succeeded\x01",
            "in saving 10 mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess I'll eat an ice cream or something and go home♪\x01",
            "...Although, being rainy it could be a little chilly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C937")

    label("loc_C22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C2C8")

    ChrTalk(
        0xFE,
        (
            "Yes, I guess that I'll end my\x01",
            "shopping here for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hu hu, thanks to doing\x01",
            "my cheap shopping route,\x01",
            "I saved up quite the mira.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C937")

    label("loc_C2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C34A")

    ChrTalk(
        0xFE,
        (
            "I get the feeling that I\x01",
            "gradually started to notice\x01",
            "a new shopping route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Economising is\x01",
            "really tough...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C937")

    label("loc_C34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C358")
    Jump("loc_C937")

    label("loc_C358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C51B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C454")

    ChrTalk(
        0xFE,
        (
            "How much cheap things you can buy\x01",
            "competing with the surrounding people...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that sales and bargains\x01",
            "fun lies in that point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The joy of when you could\x01",
            "buy for cheap what you\x01",
            "wanted is truly exceptional.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C516")

    label("loc_C454")


    ChrTalk(
        0xFE,
        (
            "The joy of when you could buy\x01",
            "for cheap what you wanted with\x01",
            "sales and bargains is exceptional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially in my case, the joy\x01",
            "is doubled because the surplus\x01",
            "mira become my allowance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C516")

    Jump("loc_C937")

    label("loc_C51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C5F2")

    ChrTalk(
        0xFE,
        (
            "Since today is Orchis Tower unveiling\x01",
            "ceremony the excitement is quite high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Somehow, I smell sales.\x01",
            "Today, I think I'll try to tour the department \x01",
            "store too which I usually don't go to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C937")

    label("loc_C5F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C758")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6DC")

    ChrTalk(
        0xFE,
        (
            "The trick to saving is intelligence gathering.\x01",
            "That's in order to not lose\x01",
            "timed sales and bargains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, it appears that if I shop\x01",
            "at the street stalls at this time\x01",
            "frame I can save up some mira.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C753")

    label("loc_C6DC")


    ChrTalk(
        0xFE,
        (
            "For the sake of my allowance too,\x01",
            "it's saving, saving...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must not let timed sales\x01",
            "and bargains slip me by.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C753")

    Jump("loc_C937")

    label("loc_C758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C80A")

    ChrTalk(
        0xFE,
        (
            "Because on rainy days there're few customers,\x01",
            "you can make sure of the goods at leisure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hu hu, it looks like I'll be able\x01",
            "to do good shopping today too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C937")

    label("loc_C80A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C937")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8C0")

    ChrTalk(
        0xFE,
        (
            "When mama asks me to do errands,\x01",
            "she hands me over a lot of mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do shopping with that\x01",
            "and the surplus mira becomes\x01",
            "the size of my allowance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C937")

    label("loc_C8C0")


    ChrTalk(
        0xFE,
        (
            "...But recently, mama gives me\x01",
            "only barely the total amount\x01",
            "needed, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "U-Uhhm...\x01",
            "My allowance plan...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C937")

    TalkEnd(0xFE)
    Return()

    # Function_14_BE49 end

    def Function_15_C93B(): pass

    label("Function_15_C93B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9DF")

    ChrTalk(
        0xFE,
        (
            "Although at a time like this\x01",
            "she could close shop, Marte\x01",
            "has got nerves of steel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's one of my wife's\x01",
            "good sides, I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_CA83")

    label("loc_C9DF")


    ChrTalk(
        0xFE,
        (
            "Although at a time like this\x01",
            "she could close shop, Marte\x01",
            "has got nerves of steel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, since I've come here, I guess\x01",
            "I'll help her with the store today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA83")

    TalkEnd(0xFE)
    Return()

    # Function_15_C93B end

    def Function_16_CA87(): pass

    label("Function_16_CA87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CB70")

    ChrTalk(
        0xFE,
        (
            "They say that there's a high possibility\x01",
            "that Orchis Tower blueprints went on\x01",
            "the terrorists' hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, where're they going\x01",
            "to attack from, I wonder? I'd like to \x01",
            "believe there're no openings, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCF7")

    label("loc_CB70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CBEF")

    ChrTalk(
        0xFE,
        (
            "I hope the "Red Constellation" or\x01",
            "or the "Heiyue" don't show up now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, security too is not easy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CCF7")

    label("loc_CBEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CCF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC8C")

    ChrTalk(
        0xFE,
        "Aah, the SSS, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can see, I'm guarding\x01",
            "the stands street now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please devote yourselves\x01",
            "to what you can do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_CCF7")

    label("loc_CC8C")


    ChrTalk(
        0xFE,
        (
            "As you can see, I'm guarding\x01",
            "the stands street now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please devote yourselves\x01",
            "to what you can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCF7")

    TalkEnd(0xFE)
    Return()

    # Function_16_CA87 end

    SaveToFile()

Try(main)
