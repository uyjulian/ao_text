from ScenarioHelper import *

def main():
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
        [152, 4751, 8974, 12812, 22148, 25732, 26167, 26757, 29230, 0, 32545, 0, 36393, 39440, 39924, 42004, 0, 43963, 0, 176, 180, 0, 0],
    )

    BuildStringList((
        "c1000_2",                # 0
    ))

    ChipFrameInfo(152, 0)                                        # 0

    ScpFunction((
        "Function_0_98",           # 00, 0
        "Function_1_128F",         # 01, 1
        "Function_2_230E",         # 02, 2
        "Function_3_320C",         # 03, 3
        "Function_4_5684",         # 04, 4
        "Function_5_6484",         # 05, 5
        "Function_6_6637",         # 06, 6
        "Function_7_6885",         # 07, 7
        "Function_8_722E",         # 08, 8
        "Function_9_7F21",         # 09, 9
        "Function_10_8E29",        # 0A, 10
        "Function_11_9A10",        # 0B, 11
        "Function_12_9BF4",        # 0C, 12
        "Function_13_A414",        # 0D, 13
        "Function_14_ABBB",        # 0E, 14
        "Function_15_B4B0",        # 0F, 15
        "Function_16_B5CF",        # 10, 16
    ))


    def Function_0_98(): pass

    label("Function_0_98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E7")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x1A2, 500)

    ChrTalk(
        0x8,
        "Oh, pretty child child ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How is this windmill?\x01",
            "Is it fun if you blow Huhu?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "… … Does that mean to me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hunt, that kind of eastward\x01",
            "There is nothing unusual,\x01",
            "Kodomo is also a good dick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Guan …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_223")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2D0")

    label("loc_223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_27C")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2D0")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2D0")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2D0")

    TalkEnd(0x8)
    SetScenarioFlags(0x1DC, 3)
    ClearChrFlags(0x8, 0x10)
    OP_93(0x8, 0xB4, 0x0)
    Jump("loc_32A")

    label("loc_2E7")


    ChrTalk(
        0x8,
        (
            "Huh …\x01",
            "Bad such bite\x01",
            "Your child may be the first time.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_32A")

    Return()

    label("loc_32B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_335")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_128B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_393")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_393")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3B2")
    OP_AF(0x38)
    Jump("loc_3B4")

    label("loc_3B2")

    OP_AF(0x39)

    label("loc_3B4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1286")

    label("loc_3C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D7")
    Jump("loc_1286")

    label("loc_3D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1286")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_573")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DD")

    ChrTalk(
        0xFE,
        (
            "For the moment, Cross Bell City\x01",
            "It was good that we could regain everyday life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Instead I do not understand Wake\x01",
            "A big tree has come up … But …\x01",
            "Surely it will be somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Distraction, even a new crafts item\x01",
            "I do not mind trying to make it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_56E")

    label("loc_4DD")


    ChrTalk(
        0xFE,
        (
            "To Roy, from tomorrow\x01",
            "I will intend to work harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not understand Wake\x01",
            "A big tree has come up … But …\x01",
            "Surely it will be somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56E")

    Jump("loc_1286")

    label("loc_573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_581")
    Jump("loc_1286")

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FD")

    ChrTalk(
        0xFE,
        (
            "Cross Bell finally\x01",
            "It's a matter of independence as a nation …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just as history changes\x01",
            "Feeling that I am present.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_695")

    ChrTalk(
        0xFE,
        (
            "It is done in old city\x01",
            "For cooking,\x01",
            "I made a lot of wooden dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is trivial,\x01",
            "I only have this\x01",
            "I can not do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_714")

    ChrTalk(
        0xFE,
        (
            "Mainz was occupied\x01",
            "That's right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things about the materials of crafts\x01",
            "I am indebted to various people,\x01",
            "Worried s …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_79D")

    ChrTalk(
        0xFE,
        (
            "Today the guests\x01",
            "It seems not to come much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also took a day off to Roy,\x01",
            "Even with non-birth and craft items alone\x01",
            "I am making it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_79D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_80F")

    ChrTalk(
        0xFE,
        (
            "Windmill made by Roy,\x01",
            "It was quietly selling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, well, somehow I\x01",
            "It's a pleasant session.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_80F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E1")

    ChrTalk(
        0xFE,
        (
            "The windmill out putting it at the store\x01",
            "One by one, how to rotate\x01",
            "It is slightly different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is unique handmade\x01",
            "Taste is a joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, to amateurs\x01",
            "It is almost impossible\x01",
            "I do not understand it though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_96D")

    label("loc_8E1")


    ChrTalk(
        0xFE,
        (
            "By the way, Roy 's windmill,\x01",
            "It is likely to sell as a product\x01",
            "Only one was made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Originally a hand\x01",
            "It looks like a dexterity.\x01",
            "Future prospects ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96D")

    Jump("loc_1286")

    label("loc_972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_ACE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5A")

    ChrTalk(
        0xFE,
        (
            "I was making hardships\x01",
            "The model of Orkis Tower\x01",
            "Last night it was finally completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you leave it at the store front\x01",
            "Tourists are really wanting\x01",
            "You got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, this is not for sale right?\x01",
            "Something bad something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AC9")

    label("loc_A5A")


    ChrTalk(
        0xFE,
        (
            "Anyway, Roy,\x01",
            "It works persistently\x01",
            "I am saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all this too\x01",
            "Is not it the president 's blood line?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC9")

    Jump("loc_1286")

    label("loc_ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B76")

    ChrTalk(
        0xFE,
        (
            "With Russi to Roy\x01",
            "Something that was supposed to be worked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, Chairman of the Chamber of Commerce\x01",
            "There are only grandchildren, it is Mageymess.\x01",
            "It seems quite possible to expect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BDA")

    label("loc_B76")


    ChrTalk(
        0xFE,
        (
            "To him, various things\x01",
            "I am going to remember it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe he seems to have made a disciple\x01",
            "It's a fun session ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDA")

    Jump("loc_1286")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C96")

    ChrTalk(
        0xFE,
        (
            "If you are a beautiful girl in the eastward style,\x01",
            "After doing various shopping at the stalls\x01",
            "I walked toward the central square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fatty and cool eyes\x01",
            "It was a great impression.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3E")

    label("loc_C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFF")

    ChrTalk(
        0xFE,
        (
            "Later, just a little while ago,\x01",
            "I came to go shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fatty and cool eyes\x01",
            "It was a great impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F…… Who is that person?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After doing various shopping at the stalls\x01",
            "You walked toward the central square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F(Hey Lloyd, this guy\x01",
            "Perhaps he is that person … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(… … Oh, let's try looking.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x1C6, 7)
    Jump("loc_F3E")

    label("loc_DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED2")

    ChrTalk(
        0xFE,
        (
            "No, what is Orxistower\x01",
            "It's amazing force!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the motivation for creation has come to pass.\x01",
            "Let's make a model of the tower ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even at the previous anniversary festival,\x01",
            "I made a model of the city hall.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F3E")

    label("loc_ED2")


    ChrTalk(
        0xFE,
        (
            "by the way……\x01",
            "Mr. Chairman of the Chamber of Commerce\x01",
            "The grandson is coming to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, there are things that are rare.\x02",
    )

    CloseMessageWindow()

    label("loc_F3E")

    Jump("loc_1286")

    label("loc_F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_103D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC8")

    ChrTalk(
        0xFE,
        (
            "Our crafts,\x01",
            "It's all handmade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Handmade, after all somewhere\x01",
            "It is a good idea to have warmth.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1038")

    label("loc_FC8")


    ChrTalk(
        0xFE,
        (
            "Hand-made work takes time,\x01",
            "Sometimes I get injured … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all somewhere\x01",
            "It is a good idea to have warmth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1038")

    Jump("loc_1286")

    label("loc_103D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1165")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FC")

    ChrTalk(
        0xFE,
        (
            "The crafts that I made\x01",
            "I'm going to get wet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……even if you say so,\x01",
            "Crafts of our country\x01",
            "Perfectly waterproof processing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just being cheated\x01",
            "I'm durable enough ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1160")

    label("loc_10FC")


    ChrTalk(
        0xFE,
        (
            "Crafts of our country\x01",
            "Perfectly waterproof processing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just being cheated\x01",
            "I'm durable enough ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1160")

    Jump("loc_1286")

    label("loc_1165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1206")

    ChrTalk(
        0xFE,
        "Hello, nice to meet you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My house is various\x01",
            "It deals handmade craft items.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like it\x01",
            "I want you to buy it by all means!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1286")

    label("loc_1206")


    ChrTalk(
        0xFE,
        (
            "Among our items, popular is\x01",
            "This \"windmill#4RTankaguruma#That's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is said to be an amulet in the east\x01",
            "It's a toy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1286")

    Jump("loc_335")

    label("loc_128B")

    TalkEnd(0xFE)
    Return()

    # Function_0_98 end

    def Function_1_128F(): pass

    label("Function_1_128F")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_129C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12FA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_12FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131A")
    OP_AF(0x35)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2305")

    label("loc_131A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132E")
    Jump("loc_2305")

    label("loc_132E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2305")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1466")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F7")

    ChrTalk(
        0xFE,
        "Nice to meet you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fresh Dings\x01",
            "It's on the market today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eat fresh vegetables,\x01",
            "This abnormal situation\x01",
            "Let's survive on health!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1461")

    label("loc_13F7")


    ChrTalk(
        0xFE,
        (
            "…… Liry from a while ago\x01",
            "Flirting with you this way\x01",
            "It seems to be seeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do you have something on my face?\x02",
    )

    CloseMessageWindow()

    label("loc_1461")

    Jump("loc_2305")

    label("loc_1466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1474")
    Jump("loc_2305")

    label("loc_1474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_157D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1520")

    ChrTalk(
        0xFE,
        (
            "Crossbell independent country …\x01",
            "Well, it is awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But Lily's guy\x01",
            "A face that looks somewhat difficult\x01",
            "I'm doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is there anything to worry about?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1578")

    label("loc_1520")


    ChrTalk(
        0xFE,
        (
            "Lily 's guy,\x01",
            "A face that looks somewhat difficult\x01",
            "I'm doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is there anything to worry about?\x02",
    )

    CloseMessageWindow()

    label("loc_1578")

    Jump("loc_2305")

    label("loc_157D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_16D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1642")

    ChrTalk(
        0xFE,
        (
            "Today, done at the city hall\x01",
            "For the charity event,\x01",
            "I gave vegetables from home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the Chamber of Commerce organized\x01",
            "It's getting taken care of … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone in town\x01",
            "I want you to be healthy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16CB")

    label("loc_1642")


    ChrTalk(
        0xFE,
        (
            "To the people of the Chamber of Commerce,\x01",
            "I asked the executives\x01",
            "I am taking care of various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To energize everyone in the city\x01",
            "I want you to work hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CB")

    Jump("loc_2305")

    label("loc_16D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_17C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1778")

    ChrTalk(
        0xFE,
        (
            "It is said that Mainz was occupied … …\x01",
            "Rumor, the ransom demand is\x01",
            "It is a story that it has not come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The armed group tries to do what\x01",
            "I guess they are … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17BE")

    label("loc_1778")


    ChrTalk(
        0xFE,
        (
            "Armed groups and lions,\x01",
            "For what purpose Mainz\x01",
            "I guess I occupied … ….?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BE")

    Jump("loc_2305")

    label("loc_17C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A7")

    ChrTalk(
        0xFE,
        (
            "My older brother who comes to wholesale vegetables\x01",
            "He told me about excitement … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yesterday, somehow in Almorika village\x01",
            "It seems that there was a big noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it seems that the solution was made at first, …\x01",
            "Well, I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1934")

    label("loc_18A7")


    ChrTalk(
        0xFE,
        (
            "In the village of Almorika\x01",
            "It seems there was a big noise yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Truck's older brother, excitedly\x01",
            "And I was accustomed to it.\x01",
            "I did not understand well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1934")

    Jump("loc_2305")

    label("loc_1939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A12")

    ChrTalk(
        0xFE,
        (
            "Actually, as I was a child\x01",
            "I hated vegetables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But as I grow older\x01",
            "It is gradually delicious\x01",
            "It began to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is unexpected that likes and dislikes\x01",
            "It might be such a thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A99")

    label("loc_1A12")


    ChrTalk(
        0xFE,
        (
            "I hated vegetables, but,\x01",
            "Not long before delicious\x01",
            "I got to eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is unexpected that likes and dislikes\x01",
            "It might be such a thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A99")

    Jump("loc_2305")

    label("loc_1A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B4B")

    ChrTalk(
        0xFE,
        (
            "Actually, the name of our store is\x01",
            "Lily thought about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From when I said I want to do business\x01",
            "You support me anyhow … ….\x01",
            "He was a good friend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2305")

    label("loc_1B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BFC")

    ChrTalk(
        0xFE,
        (
            "Always from Almorika village\x01",
            "To unload vegetables with a power track\x01",
            "I'm getting it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess it's wrong\x01",
            "That beautiful\x01",
            "I wonder if it was a truck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C6B")

    label("loc_1BFC")


    ChrTalk(
        0xFE,
        (
            "In the village of Almorika\x01",
            "Conductivity track …\x01",
            "Have you purchased a new one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To, the economy is good\x01",
            "I am envious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C6B")

    Jump("loc_2305")

    label("loc_1C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0C")

    ChrTalk(
        0xFE,
        (
            "At the trade meeting mainly about the economy\x01",
            "It's supposed to be discussed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, to me\x01",
            "I do not understand difficult things.\x01",
            "You gotta be like!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D8B")

    label("loc_1D0C")


    ChrTalk(
        0xFE,
        (
            "Well, whatever the economy is,\x01",
            "Customer first in the future\x01",
            "I'm just going to do business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To me, the difficult thing is\x01",
            "Do not understand me at all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8B")

    Jump("loc_2305")

    label("loc_1D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECB")

    ChrTalk(
        0xFE,
        (
            "Everything from today, Liber Kingdom\x01",
            "It seems the princess has come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Speaking of Liber Kingdom,\x01",
            "It is famous for the shipment of \"Nagara Tomato\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything is in Libert\x01",
            "It is a conductor manufacturer called ZCF\x01",
            "She seems to have been born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a conductor manufacturer\x01",
            "To make vegetables even,\x01",
            "It is truly a technical force.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F5D")

    label("loc_1ECB")


    ChrTalk(
        0xFE,
        (
            "There are tomatoes,\x01",
            "A while ago at ZCF\x01",
            "It is a vegetable produced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a conductor manufacturer\x01",
            "To make vegetables even,\x01",
            "It is truly a technical force.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5D")

    Jump("loc_2305")

    label("loc_1F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2160")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D6")

    ChrTalk(
        0xFE,
        (
            "To the teacher of Ursula hospital\x01",
            "I heard that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When eating anything vegetables,\x01",
            "It seems that the absorption of oil becomes gentle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you eat meat or something\x01",
            "Eating vegetables together\x01",
            "It is difficult to gain weight.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2054")
    Jump("loc_20CE")

    label("loc_2054")


    ChrTalk(
        0x109,
        "#10105FI see, I see … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102Finformative.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Women are such topics\x01",
            "Especially enthusiastic … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CE")

    SetScenarioFlags(0x0, 1)
    Jump("loc_215B")

    label("loc_20D6")


    ChrTalk(
        0xFE,
        (
            "You vegetarian, are you eating?\x01",
            "Junk food only\x01",
            "Eat it, it is poison to my body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want to stay healthy,\x01",
            "After all I have to eat vegetables.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215B")

    Jump("loc_2305")

    label("loc_2160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21FF")

    ChrTalk(
        0xFE,
        (
            "…… Huh, from the tent\x01",
            "I guess the leak is running out.\x01",
            "I should repair in the near future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… However, Liry from a little while ago\x01",
            "What are you trying to modulate?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2305")

    label("loc_21FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2305")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22AC")

    ChrTalk(
        0xFE,
        "Nice to meet you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fresh vegetables from Armorica,\x01",
            "I have plenty of it today too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all the cross vegetable vegetables\x01",
            "It's exciting for Pikaichi!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2305")

    label("loc_22AC")


    ChrTalk(
        0xFE,
        (
            "After all the Armorican vegetables\x01",
            "It is delicious and recommended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please buy plenty!\x02",
    )

    CloseMessageWindow()

    label("loc_2305")

    Jump("loc_129C")

    label("loc_230A")

    TalkEnd(0xFE)
    Return()

    # Function_1_128F end

    def Function_2_230E(): pass

    label("Function_2_230E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2404")

    ChrTalk(
        0xFE,
        (
            "When dinos … …\x01",
            "Let's eat vegetables and survive\x01",
            "The weather has plenty of weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it is because of such Dins\x01",
            "You can give it up to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is important as a street vendor,\x01",
            "It may be that part of the unexpected thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24A1")

    label("loc_2404")


    ChrTalk(
        0xFE,
        (
            "Because it is Noh weather Dins\x01",
            "You can give it up to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I was also hanging around in the city\x01",
            "I was reassured by Dins.\x01",
            "Hehe, thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A1")

    Jump("loc_3208")

    label("loc_24A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_24B4")
    Jump("loc_3208")

    label("loc_24B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F1")

    ChrTalk(
        0xFE,
        (
            "Logistics from two major countries is also\x01",
            "I completely stopped it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear Dieter,\x01",
            "Stockpile of about 5 years\x01",
            "I am talking about storing it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am selling fresh vegetables\x01",
            "I have to think about how to do business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… But even if Dins,\x01",
            "I do not seem to know that part at all.\x01",
            "Haha, I want you to be firm.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2692")

    label("loc_25F1")


    ChrTalk(
        0xFE,
        (
            "どうも、ディーター大統領はStockpile of about 5 years\x01",
            "I am talking about storing it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For future business\x01",
            "Because I am involved,\x01",
            "I also want Dens firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2692")

    Jump("loc_3208")

    label("loc_2697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_277E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")

    ChrTalk(
        0xFE,
        (
            "Unfortunately,\x01",
            "Almost east street\x01",
            "I did not have any damage … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_26EF")


    ChrTalk(
        0xFE,
        (
            "Because that big demon ramped around,\x01",
            "The old city seems to be terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems I am doing recovery work now ….\x01",
            "I wonder when it will be available.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3208")

    label("loc_277E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27EC")

    ChrTalk(
        0xFE,
        "The matter about Mainz is scary …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The guards people\x01",
            "If you manage to solve it\x01",
            "I do not mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3208")

    label("loc_27EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_288F")

    ChrTalk(
        0xFE,
        (
            "Oh, in the meantime\x01",
            "Even though the hole in the tent was blocked,\x01",
            "It seems to have leaked from another place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you drink at all,\x01",
            "I'd like you to help me with a good idea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3208")

    label("loc_288F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298B")

    ChrTalk(
        0xFE,
        (
            "Like leeks and leeks,\x01",
            "People who do not like it because there is smell\x01",
            "It may be many, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A quite eatable person\x01",
            "I wonder if it is mostly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I tried to eat it\x01",
            "Because it may be delicious unexpectedly\x01",
            "I want you to try various things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A0C")

    label("loc_298B")


    ChrTalk(
        0xFE,
        (
            "I do not like to eat it,\x01",
            "After all it is a little waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you are not good at odor\x01",
            "It might be pretty delicious to eat\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A0C")

    Jump("loc_3208")

    label("loc_2A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE7")

    ChrTalk(
        0xFE,
        (
            "Din's,\x01",
            "Without any knowledge\x01",
            "I was about to start business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can obtain business permission\x01",
            "To secure a place,\x01",
            "I did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, since a long time ago\x01",
            "You can not leave it alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B77")

    label("loc_2AE7")


    ChrTalk(
        0xFE,
        (
            "Din's,\x01",
            "Without any knowledge\x01",
            "I was about to start business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So preparing for business\x01",
            "I did it.\x01",
            "I am quite grateful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B77")

    Jump("loc_3208")

    label("loc_2B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C41")

    ChrTalk(
        0xFE,
        (
            "Actually, during the meantime, the head of the Chamber of Commerce\x01",
            "Secretly seeing the state of Dins\x01",
            "You came to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dings had previously invited executives\x01",
            "I refused it,\x01",
            "You seem to be regretful after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CD9")

    label("loc_2C41")


    ChrTalk(
        0xFE,
        (
            "Well, at that time, I\x01",
            "It is regrettable to refuse invitation\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Din's\x01",
            "It is not a pattern that stands above a person,\x01",
            "I think it was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD9")

    Jump("loc_3208")

    label("loc_2CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D52")

    ChrTalk(
        0xFE,
        (
            "もう、Din's\x01",
            "You can not think things deeply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am a childhood friend\x01",
            "I have to support it firmly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3208")

    label("loc_2D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E3E")

    ChrTalk(
        0xFE,
        (
            "When you use tomato for cooking\x01",
            "The taste is considerably deepened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, with a salad\x01",
            "To those who want to eat\x01",
            "I might not recommend it much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Because, as it is\x01",
            "It is very bitter.\x01",
            "I am a bit weak.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EBA")

    label("loc_2E3E")


    ChrTalk(
        0xFE,
        (
            "When you use tomato for cooking\x01",
            "The taste has considerable depth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though it is very bitter as it is.\x01",
            "Fine, it's food for professionals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBA")

    Jump("loc_3208")

    label("loc_2EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA3")

    ChrTalk(
        0xFE,
        (
            "Din's to become a street vendor\x01",
            "I studied vegetables very hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just a sense of business is refreshing,\x01",
            "I'm doing it with just a good personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in a way it's\x01",
            "It is the taste of Dins.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_301F")

    label("loc_2FA3")


    ChrTalk(
        0xFE,
        (
            "The business of Dins is honest,\x01",
            "The sense of management is fresh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in a way it's\x01",
            "It is the taste of Dins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301F")

    Jump("loc_3208")

    label("loc_3024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_317D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E2")

    ChrTalk(
        0xFE,
        (
            "A customer who came just before,\x01",
            "\"You seem to be a couple\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I thought it was just a childhood friend\x01",
            "I never even thought about it … …\x01",
            "I was conscious about it somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3178")

    label("loc_30E2")


    ChrTalk(
        0xFE,
        (
            "To the customer,\x01",
            "\"You seem to be a couple,\"\x01",
            "What did I say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… But Din's\x01",
            "I do not think anything.\x01",
            "I will excuse you at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3178")

    Jump("loc_3208")

    label("loc_317D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3208")

    ChrTalk(
        0xFE,
        (
            "In the crossbell,\x01",
            "I depend on imports for a lot of groceries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, because it can be delivered promptly by train\x01",
            "Even imports are more fresh than I thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3208")

    TalkEnd(0xFE)
    Return()

    # Function_2_230E end

    def Function_3_320C(): pass

    label("Function_3_320C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3235")
    Call(0, 29)
    Return()

    label("loc_3235")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x2, 3)
    Call(2, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_567D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3251")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5678")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "talk")
    MenuCmd(1, 1, "Pass fish")
    MenuCmd(1, 1, "quit")
    ClearScenarioFlags(0x2, 3)
    Call(2, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A3")
    MenuCmd(3, 1, 0x1)

    label("loc_32A3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D5")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_32D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5643")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5634")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3360")
    MenuCmd(1, 1, "When fighter × 5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3356")
    Call(2, 6)

    label("loc_3356")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3360")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33B6")
    MenuCmd(1, 1, "Snow shave illusion × 5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33AC")
    Call(2, 6)

    label("loc_33AC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_33B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_340C")
    MenuCmd(1, 1, "Ezel liquid product × 3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3402")
    Call(2, 6)

    label("loc_3402")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_340C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3462")
    MenuCmd(1, 1, "Casagin sky × 5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3458")
    Call(2, 6)

    label("loc_3458")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3462")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34B8")
    MenuCmd(1, 1, "Armorica buna green onion × 2")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34AE")
    Call(2, 6)

    label("loc_34AE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_34B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_350E")
    MenuCmd(1, 1, "Totas powder × 4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3504")
    Call(2, 6)

    label("loc_3504")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_350E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3564")
    MenuCmd(1, 1, "4 carrots ginseng")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_355A")
    Call(2, 6)

    label("loc_355A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3564")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35BA")
    MenuCmd(1, 1, "Lock liquid product × 3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B0")
    Call(2, 6)

    label("loc_35B0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_35BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3610")
    MenuCmd(1, 1, "Rainbow all × 5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3606")
    Call(2, 6)

    label("loc_3606")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3610")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3666")
    MenuCmd(1, 1, "Piranha herb × 4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_365C")
    Call(2, 6)

    label("loc_365C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3666")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36BC")
    MenuCmd(1, 1, "Carp Leaf × 3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36B2")
    Call(2, 6)

    label("loc_36B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_36BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3712")
    MenuCmd(1, 1, "Graton busse area × 5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3708")
    Call(2, 6)

    label("loc_3708")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3712")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3768")
    MenuCmd(1, 1, "Trad potato × 4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_375E")
    Call(2, 6)

    label("loc_375E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3768")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_37BE")
    MenuCmd(1, 1, "Gladieta all × 5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37B4")
    Call(2, 6)

    label("loc_37B4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_37BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3814")
    MenuCmd(1, 1, "Rainy water × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380A")
    Call(2, 6)

    label("loc_380A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3814")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_386A")
    MenuCmd(1, 1, "Sanshou style × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3860")
    Call(2, 6)

    label("loc_3860")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_386A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38C0")
    MenuCmd(1, 1, "Samona Berry × 3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B6")
    Call(2, 6)

    label("loc_38B6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_38C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3916")
    MenuCmd(1, 1, "Arona fire × 15")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_390C")
    Call(2, 6)

    label("loc_390C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3916")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_396C")
    MenuCmd(1, 1, "Yeild rare vegetables × 3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3962")
    Call(2, 6)

    label("loc_3962")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_396C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39C2")
    MenuCmd(1, 1, "Adamantas brown rice × 3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B8")
    Call(2, 6)

    label("loc_39B8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_39C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A18")
    MenuCmd(1, 1, "Quincy Rare Vegetable × 3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0E")
    Call(2, 6)

    label("loc_3A0E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3A18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A6E")
    MenuCmd(1, 1, "Parluk miso × 3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A64")
    Call(2, 6)

    label("loc_3A64")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3A6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AC4")
    MenuCmd(1, 1, "Titan dairy products × 4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ABA")
    Call(2, 6)

    label("loc_3ABA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B1A")
    MenuCmd(1, 1, "Gordosa Mina Sky × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B10")
    Call(2, 6)

    label("loc_3B10")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B70")
    MenuCmd(1, 1, "Ozanthosis illusion × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B66")
    Call(2, 6)

    label("loc_3B66")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BC6")
    MenuCmd(1, 1, "Noble Carp Total × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BBC")
    Call(2, 6)

    label("loc_3BBC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3BC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C1C")
    MenuCmd(1, 1, "Emerald style × 500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C12")
    Call(2, 6)

    label("loc_3C12")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C72")
    MenuCmd(1, 1, "Tiga rock area × 500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C68")
    Call(2, 6)

    label("loc_3C68")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CC8")
    MenuCmd(1, 1, "Crimson Eta fire × 500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CBE")
    Call(2, 6)

    label("loc_3CBE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3CC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D1E")
    MenuCmd(1, 1, "Bull Dragon Water × 500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D14")
    Call(2, 6)

    label("loc_3D14")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D74")
    MenuCmd(1, 1, "GIGA LOKE space-time vision × 500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D6A")
    Call(2, 6)

    label("loc_3D6A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D74")

    MenuCmd(1, 1, "quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DB5")
    Jump("loc_562F")

    label("loc_3DB5")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E42")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E38")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#60I5 sepices at the time\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_3E38")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EB2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#62I5 phantom sepis\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_3EA8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F22")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F18")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20I3 liquid foodstuffs\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_3F18")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F92")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F88")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#61I5 empty seps\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_3F88")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FFC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20I2 onions\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_3FF2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3FFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_406C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4062")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20IFour powder ingredients\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4062")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_406C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40D6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40CC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20I4 carrots\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_40CC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_40D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4146")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20I3 liquid foodstuffs\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_413C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4146")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41BA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41B0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "Sepis 5 of all attributes\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_41B0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_41BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4226")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_421C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20I4 herbs\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_421C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4226")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4292")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4288")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20I3 leaves\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4288")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4302")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#56I5 sepices on the ground\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_42F8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4302")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_436E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4364")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20I4 potatoes\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4364")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_436E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43E2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "Sepis 5 of all attributes\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_43D8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4452")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4448")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#57I10 seps of water\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4448")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4452")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44C2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44B8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#59IWind sepis 10 pieces\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_44B8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_44C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_452E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4524")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20IThree berries\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4524")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_452E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_459E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4594")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#58IFire sepisu 15 pieces\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4594")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_459E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_460A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4600")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20I3 rare vegetables\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4600")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_460A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4674")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20I3 brown rice\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_466A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4674")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_46E0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46D6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20I3 rare vegetables\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_46D6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_474A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4740")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20IMiso 3 pieces\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4740")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_474A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47B6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47AC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#20IFour dairy products\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_47AC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4826")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_481C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#61I50 empty seps\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_481C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4826")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4896")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_488C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#62IThe phantom sepis 20 pieces\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_488C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4896")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_490A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4900")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "10 sepices of all attributes\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4900")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_490A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_497B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4971")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#59IWind sepice 500 pieces\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4971")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_497B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49EC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49E2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#56I500 sepices of the earth\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_49E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_49EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A5D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A53")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#58IFire sepis 500 pieces\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4A53")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4ACE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "#57I500 sepsis of water\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4AC4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4ACE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B3F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B35")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "This fish\x07\x02",
            "Space-time vision Sepis 500 pieces\x07\x00",
            "so\x01",
            "Can you hand me over?\x02",
        )
    )


    label("loc_4B35")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B3F")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Exchange\x01",      # 0
            "quit\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_562F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C63")

    ChrTalk(
        0xFE,
        (
            "This is a special fine fish\x01",
            "Although it may not catch anymore ……\x01",
            "Can I really get it?\x02",
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
            "Yes\x01",        # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C63")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5625")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4D54"),
        (1, "loc_4D8B"),
        (2, "loc_4DC2"),
        (3, "loc_4DFE"),
        (4, "loc_4E35"),
        (5, "loc_4E62"),
        (6, "loc_4EA7"),
        (7, "loc_4ED4"),
        (8, "loc_4F10"),
        (9, "loc_4FDE"),
        (10, "loc_500B"),
        (11, "loc_5038"),
        (12, "loc_506F"),
        (13, "loc_509C"),
        (14, "loc_516A"),
        (15, "loc_51A3"),
        (16, "loc_51DC"),
        (17, "loc_5209"),
        (18, "loc_5242"),
        (19, "loc_527E"),
        (20, "loc_52AB"),
        (21, "loc_52E7"),
        (22, "loc_5314"),
        (23, "loc_5359"),
        (24, "loc_5392"),
        (25, "loc_53CB"),
        (26, "loc_54A7"),
        (27, "loc_54E2"),
        (28, "loc_551D"),
        (29, "loc_5558"),
        (30, "loc_5593"),
        (SWITCH_DEFAULT, "loc_5609"),
    )


    label("loc_4D54")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60ITime sepis × 5\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x4, 5)
    SubItemNumber('斗鱼', 1)
    Jump("loc_5609")

    label("loc_4D8B")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62IPhantom sepis × 5\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x6, 5)
    SubItemNumber('雪花蟹', 1)
    Jump("loc_5609")

    label("loc_4DC2")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '香油'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '蜂蜜糖浆'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '百药精酒'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    AddItemNumber('香油', 1)
    AddItemNumber('蜂蜜糖浆', 1)
    AddItemNumber('百药精酒', 1)
    SubItemNumber('蓝带神仙鱼', 1)
    Jump("loc_5609")

    label("loc_4DFE")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61IEmpty sepis × 5\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x5, 5)
    SubItemNumber('银伞鱼', 1)
    Jump("loc_5609")

    label("loc_4E35")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '万能青葱'),
            "× 2\x07\x00",
            "I got it.\x02",
        )
    )

    AddItemNumber('万能青葱', 2)
    SubItemNumber('阿尔摩利卡鲫鱼', 1)
    Jump("loc_5609")

    label("loc_4E62")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '胡椒粒'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '热辣椒'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '粗碎岩盐'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '新磨小麦粉'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    AddItemNumber('胡椒粒', 1)
    AddItemNumber('热辣椒', 1)
    AddItemNumber('粗碎岩盐', 1)
    AddItemNumber('新磨小麦粉', 1)
    SubItemNumber('乌龟', 1)
    Jump("loc_5609")

    label("loc_4EA7")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '迷你胡萝卜'),
            "× 4\x07\x00",
            "I got it.\x02",
        )
    )

    AddItemNumber('迷你胡萝卜', 4)
    SubItemNumber('橙河鱼', 1)
    Jump("loc_5609")

    label("loc_4ED4")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '香油'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '蜂蜜糖浆'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '百药精酒'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    AddItemNumber('香油', 1)
    AddItemNumber('蜂蜜糖浆', 1)
    AddItemNumber('百药精酒', 1)
    SubItemNumber('岩穴鱼', 1)
    Jump("loc_5609")

    label("loc_4F10")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56ISepis of the earth × 5\x01\x07\x02",
            "#57IWater sepis × 5\x01\x07\x02",
            "#58IFire sepis × 5\x01\x07\x02",
            "#59IWind sepice × 5\x01\x07\x02",
            "#60ITime sepis × 5\x01\x07\x02",
            "#61IEmpty sepis × 5\x01\x07\x02",
            "#62IPhantom sepis × 5\x01\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x0, 5)
    AddSepith(0x1, 5)
    AddSepith(0x2, 5)
    AddSepith(0x3, 5)
    AddSepith(0x4, 5)
    AddSepith(0x5, 5)
    AddSepith(0x6, 5)
    SubItemNumber('虹鳟鱼', 1)
    Jump("loc_5609")

    label("loc_4FDE")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '清绿香草'),
            "× 4\x07\x00",
            "I got it.\x02",
        )
    )

    AddItemNumber('清绿香草', 4)
    SubItemNumber('食人鱼', 1)
    Jump("loc_5609")

    label("loc_500B")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '朝摘香叶'),
            "× 3\x07\x00",
            "I got it.\x02",
        )
    )

    AddItemNumber('朝摘香叶', 3)
    SubItemNumber('鲤鱼', 1)
    Jump("loc_5609")

    label("loc_5038")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56ISepis of the earth × 5\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x0, 5)
    SubItemNumber('大口鲈鱼', 1)
    Jump("loc_5609")

    label("loc_506F")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '国王马铃薯'),
            "× 4\x07\x00",
            "I got it.\x02",
        )
    )

    AddItemNumber('国王马铃薯', 4)
    SubItemNumber('黑鲑', 1)
    Jump("loc_5609")

    label("loc_509C")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56ISepis of the earth × 5\x01\x07\x02",
            "#57IWater sepis × 5\x01\x07\x02",
            "#58IFire sepis × 5\x01\x07\x02",
            "#59IWind sepice × 5\x01\x07\x02",
            "#60ITime sepis × 5\x01\x07\x02",
            "#61IEmpty sepis × 5\x01\x07\x02",
            "#62IPhantom sepis × 5\x01\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x0, 5)
    AddSepith(0x1, 5)
    AddSepith(0x2, 5)
    AddSepith(0x3, 5)
    AddSepith(0x4, 5)
    AddSepith(0x5, 5)
    AddSepith(0x6, 5)
    SubItemNumber('角斗鱼', 1)
    Jump("loc_5609")

    label("loc_516A")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57IWater sepis × 10\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x1, 10)
    SubItemNumber('冷水鱼', 1)
    Jump("loc_5609")

    label("loc_51A3")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59IWind sepice × 10\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x3, 10)
    SubItemNumber('小鲵', 1)
    Jump("loc_5609")

    label("loc_51DC")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '铃铛草莓'),
            "× 3\x07\x00",
            "I got it.\x02",
        )
    )

    AddItemNumber('铃铛草莓', 3)
    SubItemNumber('鲑鱼', 1)
    Jump("loc_5609")

    label("loc_5209")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58IFire sepis × 15\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x2, 15)
    SubItemNumber('金龙鱼', 1)
    Jump("loc_5609")

    label("loc_5242")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '黑暗菇'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '七彩豆'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    AddItemNumber('黑暗菇', 1)
    AddItemNumber('七彩豆', 1)
    AddItemNumber('苦西红柿', 1)
    SubItemNumber('鳗鲡', 1)
    Jump("loc_5609")

    label("loc_527E")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '发芽糙米'),
            "× 3\x07\x00",
            "I got it.\x02",
        )
    )

    AddItemNumber('发芽糙米', 3)
    SubItemNumber('钢壳龟', 1)
    Jump("loc_5609")

    label("loc_52AB")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '黑暗菇'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '七彩豆'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    AddItemNumber('黑暗菇', 1)
    AddItemNumber('七彩豆', 1)
    AddItemNumber('苦西红柿', 1)
    SubItemNumber('巨血蟹', 1)
    Jump("loc_5609")

    label("loc_52E7")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '五谷味噌'),
            "× 3\x07\x00",
            "I got it.\x02",
        )
    )

    AddItemNumber('五谷味噌', 3)
    SubItemNumber('珍珠龙鱼', 1)
    Jump("loc_5609")

    label("loc_5314")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, '新鲜牛奶'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '新鲜奶酪'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '新鲜鸡蛋'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, '雪花里脊肉'),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    AddItemNumber('新鲜牛奶', 1)
    AddItemNumber('新鲜奶酪', 1)
    AddItemNumber('新鲜鸡蛋', 1)
    AddItemNumber('雪花里脊肉', 1)
    SubItemNumber('巨鲶', 1)
    Jump("loc_5609")

    label("loc_5359")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61IEmpty Sepis × 50\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x5, 50)
    SubItemNumber('金鲑', 1)
    Jump("loc_5609")

    label("loc_5392")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62IPhantom Sepis × 20\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x6, 20)
    SubItemNumber('大鲵', 1)
    Jump("loc_5609")

    label("loc_53CB")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56ISepis of the earth × 10\x01\x07\x02",
            "#57IWater sepis × 10\x01\x07\x02",
            "#58IFire sepis × 10\x01\x07\x02",
            "#59IWind sepice × 10\x01\x07\x02",
            "#60ITime sepis × 10\x01\x07\x02",
            "#61IEmpty Sepis × 10\x01\x07\x02",
            "#62IPhantom Sepis × 10\x01\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x0, 10)
    AddSepith(0x1, 10)
    AddSepith(0x2, 10)
    AddSepith(0x3, 10)
    AddSepith(0x4, 10)
    AddSepith(0x5, 10)
    AddSepith(0x6, 10)
    SubItemNumber('锦鲤', 1)
    Jump("loc_5609")

    label("loc_54A7")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59IWind sepice × 500\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x3, 500)
    SubItemNumber('翠耀神仙鱼', 1)
    Jump("loc_5609")

    label("loc_54E2")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56ISepis of the earth × 500\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x0, 500)
    SubItemNumber('琥耀岩穴鱼', 1)
    Jump("loc_5609")

    label("loc_551D")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58IFire Sepis × 500\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x2, 500)
    SubItemNumber('红耀食人鱼', 1)
    Jump("loc_5609")

    label("loc_5558")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57IWater sepis × 500\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x1, 500)
    SubItemNumber('苍耀巨龙鱼', 1)
    Jump("loc_5609")

    label("loc_5593")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60ITime Sepis × 500\x01\x07\x02",
            "#61IEmpty Sepis × 500\x01\x07\x02",
            "#62IPhantom Sepis × 500\x01\x07\x00",
            "I got it.\x02",
        )
    )

    AddSepith(0x4, 500)
    AddSepith(0x5, 500)
    AddSepith(0x6, 500)
    SubItemNumber('巨骨龙皇鱼', 1)
    Jump("loc_5609")

    label("loc_5609")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_562F")

    label("loc_5625")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_562F")

    Jump("loc_32EE")

    label("loc_5634")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5673")

    label("loc_5643")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5657")
    Jump("loc_5673")

    label("loc_5657")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5673")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(2, 4)

    label("loc_5673")

    Jump("loc_3251")

    label("loc_5678")

    Jump("loc_5680")

    label("loc_567D")

    Call(2, 4)

    label("loc_5680")

    TalkEnd(0xB)
    Return()

    # Function_3_320C end

    def Function_4_5684(): pass

    label("Function_4_5684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_57AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_573B")

    ChrTalk(
        0xFE,
        (
            "There is such a thing\x01",
            "I know I'm worried … ….\x01",
            "The owner has come to the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, but it is certainly safe.\x01",
            "From now on\x01",
            "It is possible to operate with a couple.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_57A9")

    label("loc_573B")


    ChrTalk(
        0xFE,
        (
            "The host also wants to purchase fish from foreign countries\x01",
            "It means that unemployment has ended ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on\x01",
            "It is possible to operate with a couple.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57A9")

    Jump("loc_6483")

    label("loc_57AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_57BC")
    Jump("loc_6483")

    label("loc_57BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_58DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_589D")

    ChrTalk(
        0xFE,
        (
            "To the host who goes to work abroad,\x01",
            "I informed you to come back soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, last day's rail service\x01",
            "It is said that the operation will be suspended for a while\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuu, come home properly\x01",
            "Is it possible to come …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_58D8")

    label("loc_589D")


    ChrTalk(
        0xFE,
        (
            "Oh, our host owner …\x01",
            "はやく戻ってくればI do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58D8")

    Jump("loc_6483")

    label("loc_58DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_597E")

    ChrTalk(
        0xFE,
        (
            "Previously, I was messing around here\x01",
            "The children of the red jersey,\x01",
            "It was said that he was hurt by the attack during this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm worried …\x01",
            "I want you to show her form quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6483")

    label("loc_597E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_59C8")

    ChrTalk(
        0xFE,
        "It is not like this happens …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I'm worried … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_6483")

    label("loc_59C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A8E")

    ChrTalk(
        0xFE,
        (
            "Morning this morning, Yuushiken-san\x01",
            "You came here to listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything, a female slugger\x01",
            "Did you go somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On this bad weather day,\x01",
            "Where have you gone?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5B06")

    label("loc_5A8E")


    ChrTalk(
        0xFE,
        (
            "Anything, a female slugger\x01",
            "Did you go somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On this bad weather day,\x01",
            "Where have you gone?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B06")

    Jump("loc_6483")

    label("loc_5B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5B74")

    ChrTalk(
        0xFE,
        (
            "My husband, now to the Republic\x01",
            "I am going to buy sea fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if you got a good fish.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6483")

    label("loc_5B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C4D")

    ChrTalk(
        0xFE,
        (
            "Fresh water fish\x01",
            "Even if you try to eat normally\x01",
            "There are many muddy items, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, to milk\x01",
            "Immerse it\x01",
            "You ought to get a smell once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Quick eatable\x01",
            "Compared to sea fish,\x01",
            "It's kind of awkward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5CAF")

    label("loc_5C4D")


    ChrTalk(
        0xFE,
        (
            "Once the freshwater fish is soaked in milk\x01",
            "You should take a smell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When cooking at home\x01",
            "You should try it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CAF")

    Jump("loc_6483")

    label("loc_5CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DCB")

    ChrTalk(
        0xFE,
        (
            "Among the tax revenues of crossbell,\x01",
            "Approximately 10 will fit in the Empire and the Republic\x01",
            "It is a rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the crossbell is independent\x01",
            "Such a rule also disappeared,\x01",
            "Life will be easier than ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "もちろん安全保障の面so\x01",
            "I am worried, but ….\x01",
            "I hope it will be realized if possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5E48")

    label("loc_5DCB")


    ChrTalk(
        0xFE,
        (
            "Crossbell's independence\x01",
            "I agree with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From unreasonable tax revenue\x01",
            "If it is released, our lives will also\x01",
            "I guess it will be easier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E48")

    Jump("loc_6483")

    label("loc_5E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_601D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FAB")

    ChrTalk(
        0xFE,
        (
            "The chief priest of the empire,\x01",
            "It seems like a person whose head is considerable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you eat fish,\x01",
            "It says my head gets better … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all I ate a lot of fish\x01",
            "Have you grown up?\x02",
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
            "#00000F……what,\x01",
            "Absolutely a picture of common people\x01",
            "I knew it was floating.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6018")

    label("loc_5FAB")


    ChrTalk(
        0xFE,
        (
            "When you eat fish,\x01",
            "I say my head gets better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even the prime minister of the empire,\x01",
            "Eat a lot of fish\x01",
            "Have you grown up?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6018")

    Jump("loc_6483")

    label("loc_601D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6192")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6102")

    ChrTalk(
        0xFE,
        (
            "Border gate security,\x01",
            "It seems to be considerably strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Purchasers from the Republic,\x01",
            "To enter the immigration procedure\x01",
            "I was totally disappointed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The fact that VIPs from different countries enter the country\x01",
            "It is hard work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_618D")

    label("loc_6102")


    ChrTalk(
        0xFE,
        (
            "Purchasers from the Republic,\x01",
            "To enter the immigration procedure\x01",
            "I was totally disappointed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Border gate security is also\x01",
            "It seems to be strict.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_618D")

    Jump("loc_6483")

    label("loc_6192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_62EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626B")

    ChrTalk(
        0xFE,
        (
            "I entered the building of the fishing public division,\x01",
            "\"The Emperor 's Club\" … Is it alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a while ago.\x01",
            "It seems like \"Fishing public division\"\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not have any neighborhood,\x01",
            "It is somewhat dubious, is not it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_62EA")

    label("loc_626B")


    ChrTalk(
        0xFE,
        (
            "\"The Emperor's Club\" ……\x01",
            "It is quite dubious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like a fishing-like gathering\x01",
            "Is not it bad people?\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62EA")

    Jump("loc_6483")

    label("loc_62EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6376")

    ChrTalk(
        0xFE,
        (
            "Well, today is\x01",
            "Unfortunately the weather is bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, to this extent\x01",
            "I do not even have to close the store.\x01",
            "Do not hesitate to look at me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6483")

    label("loc_6376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6413")

    ChrTalk(
        0xFE,
        "How about a fresh fish?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "by the way……\x01",
            "Examples of fishing public division people,\x01",
            "I have not seen you recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Where have you gone?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6483")

    label("loc_6413")


    ChrTalk(
        0xFE,
        (
            "People of the fishing public division,\x01",
            "I wonder where I have gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was funny people,\x01",
            "It will be sad if you do not see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6483")

    Return()

    # Function_4_5684 end

    def Function_5_6484(): pass

    label("Function_5_6484")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6492")
    SetScenarioFlags(0x2, 3)

    label("loc_6492")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_64A0")
    SetScenarioFlags(0x2, 3)

    label("loc_64A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_64AE")
    SetScenarioFlags(0x2, 3)

    label("loc_64AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_64BC")
    SetScenarioFlags(0x2, 3)

    label("loc_64BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_64CA")
    SetScenarioFlags(0x2, 3)

    label("loc_64CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_64D8")
    SetScenarioFlags(0x2, 3)

    label("loc_64D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_64E6")
    SetScenarioFlags(0x2, 3)

    label("loc_64E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_64F4")
    SetScenarioFlags(0x2, 3)

    label("loc_64F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6502")
    SetScenarioFlags(0x2, 3)

    label("loc_6502")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6510")
    SetScenarioFlags(0x2, 3)

    label("loc_6510")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_651E")
    SetScenarioFlags(0x2, 3)

    label("loc_651E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_652C")
    SetScenarioFlags(0x2, 3)

    label("loc_652C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_653A")
    SetScenarioFlags(0x2, 3)

    label("loc_653A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6548")
    SetScenarioFlags(0x2, 3)

    label("loc_6548")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6556")
    SetScenarioFlags(0x2, 3)

    label("loc_6556")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_6564")
    SetScenarioFlags(0x2, 3)

    label("loc_6564")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6572")
    SetScenarioFlags(0x2, 3)

    label("loc_6572")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6580")
    SetScenarioFlags(0x2, 3)

    label("loc_6580")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_658E")
    SetScenarioFlags(0x2, 3)

    label("loc_658E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_659C")
    SetScenarioFlags(0x2, 3)

    label("loc_659C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_65AA")
    SetScenarioFlags(0x2, 3)

    label("loc_65AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_65B8")
    SetScenarioFlags(0x2, 3)

    label("loc_65B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_65C6")
    SetScenarioFlags(0x2, 3)

    label("loc_65C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_65D4")
    SetScenarioFlags(0x2, 3)

    label("loc_65D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_65E2")
    SetScenarioFlags(0x2, 3)

    label("loc_65E2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_65F0")
    SetScenarioFlags(0x2, 3)

    label("loc_65F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_65FE")
    SetScenarioFlags(0x2, 3)

    label("loc_65FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_660C")
    SetScenarioFlags(0x2, 3)

    label("loc_660C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_661A")
    SetScenarioFlags(0x2, 3)

    label("loc_661A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6628")
    SetScenarioFlags(0x2, 3)

    label("loc_6628")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6636")
    SetScenarioFlags(0x2, 3)

    label("loc_6636")

    Return()

    # Function_5_6484 end

    def Function_6_6637(): pass

    label("Function_6_6637")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_664A")
    MenuCmd(3, 1, 0x0)

    label("loc_664A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_665D")
    MenuCmd(3, 1, 0x1)

    label("loc_665D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6670")
    MenuCmd(3, 1, 0x2)

    label("loc_6670")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6683")
    MenuCmd(3, 1, 0x3)

    label("loc_6683")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6696")
    MenuCmd(3, 1, 0x4)

    label("loc_6696")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66A9")
    MenuCmd(3, 1, 0x5)

    label("loc_66A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66BC")
    MenuCmd(3, 1, 0x6)

    label("loc_66BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66CF")
    MenuCmd(3, 1, 0x7)

    label("loc_66CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66E2")
    MenuCmd(3, 1, 0x8)

    label("loc_66E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66F5")
    MenuCmd(3, 1, 0x9)

    label("loc_66F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6708")
    MenuCmd(3, 1, 0xA)

    label("loc_6708")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_671B")
    MenuCmd(3, 1, 0xB)

    label("loc_671B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_672E")
    MenuCmd(3, 1, 0xC)

    label("loc_672E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6741")
    MenuCmd(3, 1, 0xD)

    label("loc_6741")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6754")
    MenuCmd(3, 1, 0xE)

    label("loc_6754")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6767")
    MenuCmd(3, 1, 0xF)

    label("loc_6767")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677A")
    MenuCmd(3, 1, 0x10)

    label("loc_677A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_678D")
    MenuCmd(3, 1, 0x11)

    label("loc_678D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67A0")
    MenuCmd(3, 1, 0x12)

    label("loc_67A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67B3")
    MenuCmd(3, 1, 0x13)

    label("loc_67B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67C6")
    MenuCmd(3, 1, 0x14)

    label("loc_67C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67D9")
    MenuCmd(3, 1, 0x15)

    label("loc_67D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67EC")
    MenuCmd(3, 1, 0x16)

    label("loc_67EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67FF")
    MenuCmd(3, 1, 0x17)

    label("loc_67FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6812")
    MenuCmd(3, 1, 0x18)

    label("loc_6812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6825")
    MenuCmd(3, 1, 0x19)

    label("loc_6825")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6838")
    MenuCmd(3, 1, 0x1A)

    label("loc_6838")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_684B")
    MenuCmd(3, 1, 0x1B)

    label("loc_684B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_685E")
    MenuCmd(3, 1, 0x1C)

    label("loc_685E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6871")
    MenuCmd(3, 1, 0x1D)

    label("loc_6871")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6884")
    MenuCmd(3, 1, 0x1E)

    label("loc_6884")

    Return()

    # Function_6_6637 end

    def Function_7_6885(): pass

    label("Function_7_6885")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_69AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_693A")

    ChrTalk(
        0xFE,
        (
            "President Dieter restrained,\x01",
            "Is it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not think the top of the country will be caught\x01",
            "Unheard of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell Autonomous province is now,\x01",
            "I wonder what will happen ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_69A8")

    label("loc_693A")


    ChrTalk(
        0xFE,
        (
            "I do not think the top of the country will be caught\x01",
            "Unheard of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell Autonomous province is now,\x01",
            "I wonder what will happen ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69A8")

    Jump("loc_722A")

    label("loc_69AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_69BB")
    Jump("loc_722A")

    label("loc_69BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6A50")

    ChrTalk(
        0xFE,
        (
            "Aunt Mayor Mayor Dieter … ….\x01",
            "No, I was watching the President's speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it comes to this,\x01",
            "Toward independence\x01",
            "I hope you do your best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6B01")

    ChrTalk(
        0xFE,
        (
            "A big bell in the central square\x01",
            "He seems to have been stolen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How come you can do something like that\x01",
            "Did you steal it?\x01",
            "There is no rumor that is sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haa, it is somewhat creepy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6B71")

    ChrTalk(
        0xFE,
        "I am worried about the mining town …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The guard is trying to solve it\x01",
            "It looks like it is moving,\x01",
            "I wonder if it is OK …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6BE5")

    ChrTalk(
        0xFE,
        (
            "To yesterday's train accident\x01",
            "I was truly surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, for the time being\x01",
            "I'm glad I got back soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6C70")

    ChrTalk(
        0xFE,
        (
            "Passenger bus in the Republic\x01",
            "I went through this street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Strange …\x01",
            "That bus goes only to the east exit bus stop\x01",
            "Even though I should not be driving.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D2E")

    ChrTalk(
        0xFE,
        (
            "Independence advocacy was warmed by the mayor\x01",
            "It looks like it was an idea ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "McDaely,\x01",
            "I wonder what you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By all means give your opinion\x01",
            "I'd like to ask you a question.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6DAD")

    label("loc_6D2E")


    ChrTalk(
        0xFE,
        (
            "Aunt\x01",
            "Which would you like to vote for\x01",
            "I am in doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By all means, Mr. Magdael's opinion is also\x01",
            "I would like to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DAD")

    Jump("loc_722A")

    label("loc_6DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E7A")

    ChrTalk(
        0xFE,
        (
            "To the mayor's independent advocacy,\x01",
            "Truly lady was also surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I, too, are crossbells\x01",
            "I think I can come out bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, one of the continents\x01",
            "It is a trade city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6EF0")

    label("loc_6E7A")


    ChrTalk(
        0xFE,
        (
            "Crossbell against foreign countries\x01",
            "I think I can come out bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, one of the continents\x01",
            "It is a trade city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EF0")

    Jump("loc_722A")

    label("loc_6EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6F7B")

    ChrTalk(
        0xFE,
        "Today is the day of the trade meeting today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the mayor of Dieter,\x01",
            "For crossbell\x01",
            "I would like to have a hard time by all means.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6FEF")

    ChrTalk(
        0xFE,
        (
            "An exhibition of the Orkis Tower,\x01",
            "It was terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aunt, be surprised\x01",
            "I have left my back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_705B")

    ChrTalk(
        0xFE,
        (
            "Today I'm in patrol\x01",
            "I'll see a policeman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow the town is\x01",
            "I feel a shabby feeling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_705B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_70CF")

    ChrTalk(
        0xFE,
        (
            "Pervaded\x01",
            "Auntie, since I was a child\x01",
            "I love rain, do not you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Is it a little popular?\x02",
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_70CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_722A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71B2")

    ChrTalk(
        0xFE,
        (
            "At the end of the month a \"commerce meeting\"\x01",
            "It seems like it will be opened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only the empire and republic,\x01",
            "Libert and the great person of Remiferia\x01",
            "It seems to be invited to crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Somehow, it is very big\x01",
            "It seems like an event.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_722A")

    label("loc_71B2")


    ChrTalk(
        0xFE,
        (
            "At the end of the month a \"commerce meeting\"\x01",
            "It seems like it will be opened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that a lot of great people come,\x01",
            "とても大きなIt seems like an event.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_722A")

    TalkEnd(0xFE)
    Return()

    # Function_7_6885 end

    def Function_8_722E(): pass

    label("Function_8_722E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72C8")

    ChrTalk(
        0xFE,
        (
            "Even if President Dieter is gone\x01",
            "Mr. MacDaely is there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it is chairman, this situation is surely\x01",
            "I will manage to get it somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7311")

    label("loc_72C8")


    ChrTalk(
        0xFE,
        (
            "マクダエルIf it is chairman, this situation is surely\x01",
            "I will manage to get it somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7311")

    Jump("loc_7F1D")

    label("loc_7316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7324")
    Jump("loc_7F1D")

    label("loc_7324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_746D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73E2")

    ChrTalk(
        0xFE,
        (
            "Arios' duty free shipper\x01",
            "You do not have to appoint a Secretary of Defense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But considering his achievements\x01",
            "It may be a reasonable choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The judgment of Dieter\x01",
            "It should be said as expected.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7468")

    label("loc_73E2")


    ChrTalk(
        0xFE,
        (
            "Given Arios' achievement\x01",
            "Appointment to Secretary of Defense will be reasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway he is also the guardian god of crossbell\x01",
            "It is an existence to say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7468")

    Jump("loc_7F1D")

    label("loc_746D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_75CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_754E")

    ChrTalk(
        0xFE,
        (
            "No way, that kind of incident\x01",
            "このクロスベルso\x01",
            "I wonder what will happen …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard it from the old city\x01",
            "A scream of a monster like a huge demon,\x01",
            "Stay away from your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haa … … I suppose I can not sleep today.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_75CA")

    label("loc_754E")


    ChrTalk(
        0xFE,
        (
            "I heard it at the time of the raid incident\x01",
            "A scream of a monster like a huge demon,\x01",
            "Stay away from your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haa … … I suppose I can not sleep today.\x02",
    )

    CloseMessageWindow()

    label("loc_75CA")

    Jump("loc_7F1D")

    label("loc_75CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7719")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76A1")

    ChrTalk(
        0xFE,
        (
            "Is it occupation of Mainz …?\x01",
            "Tough thing\x01",
            "It seems that it has become.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before the mayor advocated independence,\x01",
            "Empire and Republic's help is also\x01",
            "You can expect it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, how it goes\x01",
            "Should not it be ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7714")

    label("loc_76A1")


    ChrTalk(
        0xFE,
        (
            "Before the independent advocacy,\x01",
            "Empire and Republic's help is also\x01",
            "You can expect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, how it goes\x01",
            "Should not it be ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7714")

    Jump("loc_7F1D")

    label("loc_7719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7727")
    Jump("loc_7F1D")

    label("loc_7727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7797")

    ChrTalk(
        0xFE,
        (
            "The central square\x01",
            "I heard that an ambulance passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hate\x01",
            "There was an accident anywhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F1D")

    label("loc_7797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7912")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7873")

    ChrTalk(
        0xFE,
        (
            "The next referendum …\x01",
            "Even among my acquaintances\x01",
            "I am totally thankful for that story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, to the surroundings opinion\x01",
            "Does not seem to be swept away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For anyone\x01",
            "It is not other people's affair.\x01",
            "Thinking well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_790D")

    label("loc_7873")


    ChrTalk(
        0xFE,
        (
            "Each person thinks through ideas,\x01",
            "If it is not a vote cast by my will\x01",
            "There is no meaning of voting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For anyone\x01",
            "It is not other people's affair.\x01",
            "Thinking well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790D")

    Jump("loc_7F1D")

    label("loc_7912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7A83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A04")

    ChrTalk(
        0xFE,
        (
            "As a body to know the history of this place,\x01",
            "There is no way but independence\x01",
            "I want you to win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Potatoes, empire and republic\x01",
            "Because it is under substantial control\x01",
            "It is also true that peace is kept … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No …\x01",
            "There seems to be a need to think carefully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7A7E")

    label("loc_7A04")


    ChrTalk(
        0xFE,
        (
            "You enjoy peace as a dependent state,\x01",
            "Even if I let it go, I will take independence ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No …\x01",
            "There seems to be a need to think carefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A7E")

    Jump("loc_7F1D")

    label("loc_7A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B48")

    ChrTalk(
        0xFE,
        (
            "The area around the Orkis Tower\x01",
            "It has been sealed since this morning\x01",
            "Looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "わしも各国首脳をこの目so\x01",
            "It was a place I wanted to see ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering safety\x01",
            "It may be unavoidable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7BB2")

    label("loc_7B48")


    ChrTalk(
        0xFE,
        (
            "In and around the Orkis Tower\x01",
            "It seems to have been sealed off this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "わしも各国首脳をこの目so\x01",
            "I wanted to see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BB2")

    Jump("loc_7F1D")

    label("loc_7BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7D23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C97")

    ChrTalk(
        0xFE,
        (
            "President of Rock Smith Limousine\x01",
            "I went through this street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, the president's car,\x01",
            "It was based on white and gold\x01",
            "It is a luxurious car body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That kind of car,\x01",
            "Even if you are looking for a continent\x01",
            "It should not be easy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7D1E")

    label("loc_7C97")


    ChrTalk(
        0xFE,
        (
            "President Lock Smith 's limo,\x01",
            "That was a gorgeous one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That kind of car,\x01",
            "Even if you are looking for a continent\x01",
            "It should not be easy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D1E")

    Jump("loc_7F1D")

    label("loc_7D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7DBD")

    ChrTalk(
        0xFE,
        (
            "The leaders of each country,\x01",
            "I will go to the crossbell tomorrow\x01",
            "I talked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rare opportunities,\x01",
            "You can see them with this eyes\x01",
            "I wish I could.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F1D")

    label("loc_7DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7DCB")
    Jump("loc_7F1D")

    label("loc_7DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7F1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA0")

    ChrTalk(
        0xFE,
        (
            "Dieter new mayor,\x01",
            "Working well with Mr. MacDael\x01",
            "Government#4RA ceremony#You seem to be excited about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cooperation of mayor and chairman,\x01",
            "It was something I could not think of in the past.\x01",
            "Ho, that's quite a good thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7F1D")

    label("loc_7EA0")


    ChrTalk(
        0xFE,
        (
            "Dieter new mayor,\x01",
            "As long as IBC president\x01",
            "I showed my skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, have it at all.\x01",
            "I am looking forward to the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F1D")

    TalkEnd(0xFE)
    Return()

    # Function_8_722E end

    def Function_9_7F21(): pass

    label("Function_9_7F21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_80A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8027")
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xFE,
        (
            "When the president is detained,\x01",
            "A strange pale tree appears … …\x01",
            "There are various things going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To return completely to the original everyday\x01",
            "Is it possible to do …?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        "My brother, what's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    ChrTalk(
        0xFE,
        "Haha, nothing.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_93(0xF, 0x10E, 0x0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_809F")

    label("loc_8027")


    ChrTalk(
        0xFE,
        "… … Well, it will become like.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The most important thing for me is\x01",
            "Keeping meilin … …\x01",
            "I have to forget it even if I do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_809F")

    Jump("loc_8E25")

    label("loc_80A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_80B2")
    Jump("loc_8E25")

    label("loc_80B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8243")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_819E")

    ChrTalk(
        0xFE,
        (
            "Empire and Republic\x01",
            "I can not keep my eyes on you,\x01",
            "Surely scary … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But … It's because of crossbell,\x01",
            "We citizens have to get hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Besides, no matter what happens\x01",
            "Only Meylin absolutely\x01",
            "I will protect you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_823E")

    label("loc_819E")


    ChrTalk(
        0xFE,
        (
            "I'd like to have a meilin nearby\x01",
            "After asking Mr. Cronk,\x01",
            "It was OK for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was nice talking person.\x01",
            "If it is visible\x01",
            "You can rest assured.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_823E")

    Jump("loc_8E25")

    label("loc_8243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8251")
    Jump("loc_8E25")

    label("loc_8251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_831F")

    ChrTalk(
        0xFE,
        (
            "For Mainz,\x01",
            "An armed group appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that such a thing appears in town,\x01",
            "I guess you have a terrible terrible thought …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Early this point, the guard\x01",
            "I wish I could get rid of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8391")

    label("loc_831F")


    ChrTalk(
        0xFE,
        (
            "Maylin, how are you doing …?\x01",
            "I've been feeling down lately and I'm worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today I got up earlier\x01",
            "I wonder if I will return home together …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8391")

    Jump("loc_8E25")

    label("loc_8396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_852A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_849B")

    ChrTalk(
        0xFE,
        (
            "バイト先so\x01",
            "Windmill failed to make\x01",
            "I gave it to Mayin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, absolutely\x01",
            "Today I want to play with this\x01",
            "Do not listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, to bother to express rain\x01",
            "I do not want to go out ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "….. Well, Meilin\x01",
            "I'm glad that I am happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8525")

    label("loc_849B")


    ChrTalk(
        0xFE,
        (
            "But well, that\x01",
            "ガラクタ同然の失敗作so\x01",
            "I do not want you to be pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Next is more\x01",
            "A proper guy\x01",
            "Do not give it a gift.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8525")

    Jump("loc_8E25")

    label("loc_852A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_85BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85A8")

    ChrTalk(
        0xFE,
        (
            "Well …\x01",
            "The windmill made by me,\x01",
            "I can not sell at all …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's it! Is it?\x01",
            "I have sold it before I know!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_85BA")

    label("loc_85A8")


    ChrTalk(
        0xFE,
        "Pokan\x02",
    )

    CloseMessageWindow()

    label("loc_85BA")

    Jump("loc_8E25")

    label("loc_85BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8661")

    ChrTalk(
        0xFE,
        (
            "I tried my best to make a windmill,\x01",
            "Finally only one store\x01",
            "I got it left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What you made yourself\x01",
            "I am lining up in the shop ….\x01",
            "What I say is good monkey.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E25")

    label("loc_8661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_87A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8741")

    ChrTalk(
        0xFE,
        (
            "Mr. Cronk,\x01",
            "Such a sparrow model\x01",
            "Why do you make it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also have dexterous hands\x01",
            "I was confident, but still\x01",
            "Even the windmill only fails … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How about some confidence\x01",
            "It seems to be lost.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_87A3")

    label("loc_8741")


    ChrTalk(
        0xFE,
        (
            "Anyway, today is a chore\x01",
            "Would you like to give out something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuu …\x01",
            "It's tough to work and earn Mira.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87A3")

    Jump("loc_8E25")

    label("loc_87A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_88B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8859")

    ChrTalk(
        0xFE,
        (
            "If you ask Cronk,\x01",
            "Surprisingly and frankly\x01",
            "I was supposed to be working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No……\x01",
            "From the beginning to work at stalls\x01",
            "I wish I had looked for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_88AE")

    label("loc_8859")


    ChrTalk(
        0xFE,
        (
            "To make simple craft items,\x01",
            "To the management of Mira ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I need to learn work little by little.\x02",
    )

    CloseMessageWindow()

    label("loc_88AE")

    Jump("loc_8E25")

    label("loc_88B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_89E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_897C")

    ChrTalk(
        0xFE,
        "Hum, it is a craft item ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My knuckle is quite handy,\x01",
            "This kind of work like a craftsman\x01",
            "It may be surprising that it is out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… But even this\x01",
            "I wonder if it will work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xF, 0x10)
    Jump("loc_89E0")

    label("loc_897C")


    ChrTalk(
        0xFE,
        (
            "If I could make such a windmill,\x01",
            "Maybe I'm going to be happy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "OK, well …\x01",
            "Let's ask the trial.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89E0")

    Jump("loc_8E25")

    label("loc_89E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8B73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AFB")
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Haha, to find a job\x01",
            "I got stuck dead …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Brother, later on\x01",
            "There are plenty of shops\x01",
            "Are not you going to ask me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Baha, you idiot.\x01",
            "If I had a stall vendor\x01",
            "It is conspicuously embarrassing, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can do more indoors\x01",
            "I have a nice job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xF, 0x10)
    Jump("loc_8B6E")

    label("loc_8AFB")


    ChrTalk(
        0xFE,
        (
            "Well, it's a street vendor ……\x01",
            "It is not a glass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But outside the stalls\x01",
            "Possible work is\x01",
            "I almost hit it … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B6E")

    Jump("loc_8E25")

    label("loc_8B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8BEB")

    ChrTalk(
        0xFE,
        (
            "Today with Mayrin\x01",
            "Shopping went out for a walk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whew ……\x01",
            "Even if it rains, kids are fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E25")

    label("loc_8BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CE1")

    ChrTalk(
        0xFE,
        (
            "A redhead man a while ago\x01",
            "Suddenly involved with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"More trouble, that is youth ~! Saying\x01",
            "I walked to the central square as it was ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… None, somewhat better than me\x01",
            "I thought he was like Charan Polan.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8D59")

    label("loc_8CE1")


    ChrTalk(
        0xFE,
        (
            "If you are a red-haired man before,\x01",
            "I walked to the central square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… None, somewhat better than me\x01",
            "I thought he was like Charan Polan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D59")

    Jump("loc_8E25")

    label("loc_8D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF3")

    ChrTalk(
        0xFE,
        (
            "A while ago\x01",
            "I started looking for a job … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, what's more\x01",
            "Who will hire you\x01",
            "No!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm getting down on you soon.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8E25")

    label("loc_8DF3")


    ChrTalk(
        0xFE,
        (
            "Quite\x01",
            "Who will hire you\x01",
            "No!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E25")

    TalkEnd(0xFE)
    Return()

    # Function_9_7F21 end

    def Function_10_8E29(): pass

    label("Function_10_8E29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8E9C")

    ChrTalk(
        0xFE,
        (
            "My older brother, what is it?\x01",
            "I am thinking Moyamoya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because something that is difficult is good,\x01",
            "Let's play with Meylin ☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A0C")

    label("loc_8E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8EAA")
    Jump("loc_9A0C")

    label("loc_8EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F3C")

    ChrTalk(
        0xFE,
        (
            "Today my older brother\x01",
            "He gave me an invitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My brother 's\x01",
            "There are three \"spinning rounds\".\x01",
            "I can sell it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8F96")

    label("loc_8F3C")


    ChrTalk(
        0xFE,
        (
            "When Maillin helped out,\x01",
            "\"Spin\"\x01",
            "You gotta get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Fun, fun\x02",
    )

    CloseMessageWindow()

    label("loc_8F96")

    Jump("loc_9A0C")

    label("loc_8F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_908D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9024")

    ChrTalk(
        0xFE,
        (
            "Grandpa and my brother\x01",
            "I went somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maylin, today\x01",
            "Let's play with grandma ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9088")

    label("loc_9024")


    ChrTalk(
        0xFE,
        (
            "Grandpa and older brother,\x01",
            "Damn it … Chara … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… …. Chic.\x01",
            "It seems that they are going to do something like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9088")

    Jump("loc_9A0C")

    label("loc_908D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9145")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9124")

    ChrTalk(
        0xFE,
        (
            "Maylin,\x01",
            "It is already \"Hello!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why it is loneliness\x01",
            "I'm going to tell my brother!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_9140")

    label("loc_9124")


    ChrTalk(
        0xFE,
        "My brother, I will do my best!\x02",
    )

    CloseMessageWindow()

    label("loc_9140")

    Jump("loc_9A0C")

    label("loc_9145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_91E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91A3")

    ChrTalk(
        0xFE,
        (
            "This, my brother made\x01",
            "Do not be shy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Around you ♪\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_91DF")

    label("loc_91A3")


    ChrTalk(
        0xFE,
        (
            "This spinning,\x01",
            "My brother made it!\x01",
            "It is amazing ~ ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91DF")

    Jump("loc_9A0C")

    label("loc_91E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9239")

    ChrTalk(
        0xFE,
        (
            "Grandpa,\x01",
            "Muffle - I'm on a face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… … boring ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A0C")

    label("loc_9239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9321")
    OP_4B(0x14, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C4")

    ChrTalk(
        0xFE,
        (
            "Grandpa,\x01",
            "Bearded beard ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugly, ugo ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Warmth ……\x01",
            "This, do not pull it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9318")

    label("loc_92C4")


    ChrTalk(
        0xFE,
        "Ugly, ugo ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Me, Meilin and,\x01",
            "It is surprisingly powerful ……\x01",
            "Warmth ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9318")

    OP_4C(0x14, 0xFF)
    Jump("loc_9A0C")

    label("loc_9321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_93E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93A6")

    ChrTalk(
        0xFE,
        (
            "My older brother, Kensei\x01",
            "It seems to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, both the Meilin\x01",
            "I want to play …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrFlags(0xFE, 0x10)
    Jump("loc_93E2")

    label("loc_93A6")


    ChrTalk(
        0xFE,
        (
            "My older brother, Mayrin, too\x01",
            "I want to be with you!\x01",
            "… … Husband.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93E2")

    Jump("loc_9A0C")

    label("loc_93E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9495")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9458")

    ChrTalk(
        0xFE,
        (
            "兄たん、くるくるのお店so\x01",
            "It seems to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Work is found\x01",
            "Good for you!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9490")

    label("loc_9458")


    ChrTalk(
        0xFE,
        (
            "Although it was good …\x01",
            "I am missing you.\x01",
            "… … Husband.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9490")

    Jump("loc_9A0C")

    label("loc_9495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_961F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9589")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "It's spinning,\x01",
            "It's fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Spinning round … … ♪\x02",
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
            "Wow, meilin! Is it?\x01",
            "You're turning your eyes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Kurukuru Kuraka ……\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Jump("loc_961A")

    label("loc_9589")

    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x10, 0)
    TurnDirection(0x10, 0xF, 0)

    ChrTalk(
        0xF,
        "Is not that okay, Meirin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Hanging around … …)\x01",
            "I'm a big daughter ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "It's not okay, is it …?\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)

    label("loc_961A")

    Jump("loc_9A0C")

    label("loc_961F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96F9")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "My older brother, recently\x01",
            "You will not play … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally find a job\x01",
            "Play with meylin!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "Ha, if it was that easy\x01",
            "It's true, but …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_975D")

    label("loc_96F9")


    ChrTalk(
        0xFE,
        (
            "Mei Lin is also my older brother.\x01",
            "Looking for work, you know what to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once found,\x01",
            "I will have them play together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_975D")

    Jump("loc_9A0C")

    label("loc_9762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_988A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9823")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "I do not know … ♪\x01",
            "It is a nice smell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hey Mayrin,\x01",
            "You can not open the bag yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Freshly baked bread\x01",
            "It gets wet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come ☆\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_9885")

    label("loc_9823")


    ChrTalk(
        0xFE,
        (
            "With my older brother\x01",
            "パンやさんまso\x01",
            "A groceries came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "___ ___ ___ 0\x02",
    )

    CloseMessageWindow()

    label("loc_9885")

    Jump("loc_9A0C")

    label("loc_988A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9A0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_990B")

    ChrTalk(
        0xFE,
        (
            "Red haired humans,\x01",
            "I smeared my brother 's shoulder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maylin will also drink my brother 's shoulder ~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A0C")

    label("loc_990B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99B8")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        "My brother, I'm fine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you do not find a job,\x01",
            "Maylin is nearby!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Me, me ……\x01",
            "You alone, my friend.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xF, 0xFF)
    Jump("loc_9A0C")

    label("loc_99B8")


    ChrTalk(
        0xFE,
        (
            "My older brother, I do not have any work\x01",
            "Are not you well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad that the Maylin\x01",
            "I have to give it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A0C")

    TalkEnd(0xFE)
    Return()

    # Function_10_8E29 end

    def Function_11_9A10(): pass

    label("Function_11_9A10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9A8F")

    ChrTalk(
        0xFE,
        (
            "From some time ago,\x01",
            "There are many ambulances in the city\x01",
            "It looks like she is coming back and forth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No … I have a bad feeling … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_9BF0")

    label("loc_9A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9BF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B6C")

    ChrTalk(
        0xFE,
        (
            "My grandchild Roy\x01",
            "It is my first time to work.\x01",
            "It is also in the stalls … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I was young too\x01",
            "Because I worked in the stalls.\x01",
            "I feel somewhat emotional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at most\x01",
            "Do your best, let's do.\x01",
            "Because I will also watch over you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9BF0")

    label("loc_9B6C")


    ChrTalk(
        0xFE,
        (
            "Because I got a break today.\x01",
            "I am a lucky charm of Meirin\x01",
            "You accepted it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because which is troublesome\x01",
            "I will play as long as I can\x01",
            "To do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BF0")

    TalkEnd(0xFE)
    Return()

    # Function_11_9A10 end

    def Function_12_9BF4(): pass

    label("Function_12_9BF4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9D42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CCB")

    ChrTalk(
        0xFE,
        (
            "Our men are somehow recently\x01",
            "I got to be kind to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, together with Gillet\x01",
            "I wonder how many years it has come to go shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it's like this,\x01",
            "It might be fun for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9D3D")

    label("loc_9CCB")


    ChrTalk(
        0xFE,
        (
            "Huhu, together with Gillet\x01",
            "I wonder how many years it has come to go shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it's like this,\x01",
            "It might be fun for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D3D")

    Jump("loc_A410")

    label("loc_9D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_9D50")
    Jump("loc_A410")

    label("loc_9D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9D5E")
    Jump("loc_A410")

    label("loc_9D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E3A")

    ChrTalk(
        0xFE,
        (
            "Because of the incident during this time,\x01",
            "The workplaces of our men are\x01",
            "I am off for work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If everyone were at home\x01",
            "Doubling the hard work of housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, unlike before\x01",
            "To help me\x01",
            "I appreciate it though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9E98")

    label("loc_9E3A")


    ChrTalk(
        0xFE,
        (
            "If everyone were at home\x01",
            "Doubling the hard work of housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The workplaces of men are finally\x01",
            "I wonder if it will resume.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E98")

    Jump("loc_A410")

    label("loc_9E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9EAB")
    Jump("loc_A410")

    label("loc_9EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9EB9")
    Jump("loc_A410")

    label("loc_9EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F5F")

    ChrTalk(
        0xFE,
        (
            "~ I have to do the housework\x01",
            "After all it's easy tin ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……, there! Is it?\x01",
            "In the stomach ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……As might be expected\x01",
            "I wonder why he was too scared.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9F96")

    label("loc_9F5F")


    ChrTalk(
        0xFE,
        (
            "As expected after all\x01",
            "I wonder if I will resume domestic work … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F96")

    Jump("loc_A410")

    label("loc_9F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A0E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A063")

    ChrTalk(
        0xFE,
        (
            "Our men recently finally\x01",
            "It seems I understood the difficulties of housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Would not you do me a chore,\x01",
            "It came to ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perfunctory\x01",
            "The domestic boycott plan is a great success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A0E2")

    label("loc_A063")


    ChrTalk(
        0xFE,
        (
            "Our men finally\x01",
            "It seems I understood the difficulties of housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know what to do.\x01",
            "Me too, for a while\x01",
            "I want to make it easy … … ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0E2")

    Jump("loc_A410")

    label("loc_A0E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A0F5")
    Jump("loc_A410")

    label("loc_A0F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A201")

    ChrTalk(
        0xFE,
        (
            "Since I stopped doing housework,\x01",
            "The meal menu is true,\x01",
            "It has become simpler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I asked for delivery before I decided\x01",
            "I will sprinkle extra things ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because my family is a big family\x01",
            "Even though I have to save even a bit … …\x01",
            "Absolutely, man is useless.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A271")

    label("loc_A201")


    ChrTalk(
        0xFE,
        (
            "…… Ha!\x01",
            "Why again, in the stalls … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I decided not to do housekeeping,\x01",
            "I have to try not to come again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A271")

    Jump("loc_A410")

    label("loc_A276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A284")
    Jump("loc_A410")

    label("loc_A284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A3F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A34E")

    ChrTalk(
        0xFE,
        (
            "Recently, household chores are totally\x01",
            "You stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, really, Rakuchin ☆\x01",
            "I have been stingy at home all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, husband and sons\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A3F4")

    label("loc_A34E")


    ChrTalk(
        0xFE,
        (
            "I stopped doing housework,\x01",
            "The men in our hometown are panicking every day.\x01",
            "Huhu, please shamelessly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… But when you go for a walk\x01",
            "You will come to a stall in the street.\x01",
            "It's a temper, occupational illness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3F4")

    Jump("loc_A410")

    label("loc_A3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A407")
    Jump("loc_A410")

    label("loc_A407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A410")

    label("loc_A410")

    TalkEnd(0xFE)
    Return()

    # Function_12_9BF4 end

    def Function_13_A414(): pass

    label("Function_13_A414")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A527")

    ChrTalk(
        0xFE,
        (
            "I was worried about being alone indeed.\x01",
            "My father and brother, Mom's shopping\x01",
            "I decided to follow by turns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is troublesome, but it can not be helped.\x01",
            "If mother got hurt\x01",
            "We can not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mother's importance,\x01",
            "I feel like I understand somewhat.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A564")

    label("loc_A527")


    ChrTalk(
        0xFE,
        (
            "Mother's importance,\x01",
            "I feel like I understand somewhat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A564")

    Jump("loc_ABB7")

    label("loc_A569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A577")
    Jump("loc_ABB7")

    label("loc_A577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A615")

    ChrTalk(
        0xFE,
        (
            "Wow, I got excited.\x01",
            "Yomoya Crossbell is an independent country\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am happy to be honest,\x01",
            "What will it be like to do now?\x01",
            "I do not understand it at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABB7")

    label("loc_A615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A623")
    Jump("loc_ABB7")

    label("loc_A623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A76A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A706")

    ChrTalk(
        0xFE,
        (
            "Mom finally gave housework\x01",
            "I started to resume it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, from now on\x01",
            "Both my father and our brothers\x01",
            "I tried to share it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because we are a big family,\x01",
            "I have to bring my strength together properly ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A765")

    label("loc_A706")


    ChrTalk(
        0xFE,
        (
            "When Mother did not do the housework\x01",
            "It was truly hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "After all, my mother is great ……\x02",
    )

    CloseMessageWindow()

    label("loc_A765")

    Jump("loc_ABB7")

    label("loc_A76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A778")
    Jump("loc_ABB7")

    label("loc_A778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A786")
    Jump("loc_ABB7")

    label("loc_A786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A794")
    Jump("loc_ABB7")

    label("loc_A794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A902")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A878")

    ChrTalk(
        0xFE,
        (
            "My mother is no longer doing housework,\x01",
            "I found out that difficulty struck me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I apologize every day\x01",
            "I can not forgive him ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the town is crowded about independence,\x01",
            "I have a big problem with my house.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A8FD")

    label("loc_A878")


    ChrTalk(
        0xFE,
        (
            "I have never helped with housework\x01",
            "We were obviously bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, Mother\x01",
            "許してくれるまso\x01",
            "I must apologize patiently ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8FD")

    Jump("loc_ABB7")

    label("loc_A902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A910")
    Jump("loc_ABB7")

    label("loc_A910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AA52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9C2")

    ChrTalk(
        0xFE,
        (
            "Because mother skips her household chores,\x01",
            "代わりに親父と兄弟たちso\x01",
            "She is doing housework in a shared way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am in charge of meals.\x01",
            "Well, what should I buy … ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AA4D")

    label("loc_A9C2")


    ChrTalk(
        0xFE,
        (
            "Thinking about the menu of everyday meals\x01",
            "It was such a hard time ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mother told me\x01",
            "I did it every day.\x01",
            "I'm terribly frightened …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA4D")

    Jump("loc_ABB7")

    label("loc_AA52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AA60")
    Jump("loc_ABB7")

    label("loc_AA60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_AA6E")
    Jump("loc_ABB7")

    label("loc_AA6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_ABB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB48")

    ChrTalk(
        0xFE,
        (
            "Our mother,\x01",
            "Recently completely do housework\x01",
            "I have stopped doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both my father and our brothers\x01",
            "Because I hardly helped,\x01",
            "It seems that the game has finally gotten caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well …\x01",
            "You are indeed troubled.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_ABB7")

    label("loc_AB48")


    ChrTalk(
        0xFE,
        (
            "Mother broke down,\x01",
            "All housekeeping\x01",
            "I did not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well …\x01",
            "You are indeed troubled.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABB7")

    TalkEnd(0xFE)
    Return()

    # Function_13_A414 end

    def Function_14_ABBB(): pass

    label("Function_14_ABBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_ACF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC7C")

    ChrTalk(
        0xFE,
        (
            "Somehow the streets are lively\x01",
            "I feel like I regained it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also do a lot of shopping,\x01",
            "We must contribute to the economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, and cheap shopping routes\x01",
            "I will wash it again ~!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_ACEC")

    label("loc_AC7C")


    ChrTalk(
        0xFE,
        (
            "I also do a lot of shopping,\x01",
            "We must contribute to the economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, and cheap shopping routes\x01",
            "I will wash it again ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACEC")

    Jump("loc_B4AC")

    label("loc_ACF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_ACFF")
    Jump("loc_B4AC")

    label("loc_ACFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AD79")

    ChrTalk(
        0xFE,
        (
            "What is still difficult for me\x01",
            "I do not know well … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If everyone chooses it,\x01",
            "Is not it right thing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_AD79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_ADF3")

    ChrTalk(
        0xFE,
        (
            "Before this, go to the church's mass\x01",
            "I prayed to the goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At last the crossbell\x01",
            "I hope that it will be peaceful …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_ADF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_AE63")

    ChrTalk(
        0xFE,
        "Recently, it is only a case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am scared somewhat,\x01",
            "Today round up shopping\x01",
            "I wonder if I should return soon …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_AE63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AEF2")

    ChrTalk(
        0xFE,
        (
            "Well, how come today\x01",
            "10 Mira to float\x01",
            "I succeeded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will eat ice and eat ♪\x01",
            "… … It's a bit chilly with rain though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_AEF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_AF71")

    ChrTalk(
        0xFE,
        (
            "Yeah, today's shopping is\x01",
            "It is such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, cheap shopping route\x01",
            "回ったおかげso\x01",
            "Mira floated considerably.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_AF71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AFE0")

    ChrTalk(
        0xFE,
        (
            "gradually\x01",
            "A new shopping route\x01",
            "I feel like I'm seeing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To save money\x01",
            "It's really tough …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_AFE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AFEE")
    Jump("loc_B4AC")

    label("loc_AFEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B144")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0B3")

    ChrTalk(
        0xFE,
        (
            "Compete with people around me\x01",
            "How cheap things can be bought ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The fun of sale and bargains,\x01",
            "I think that it is there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What you want\x01",
            "The pleasure when buying it cheaply\x01",
            "It's exceptional.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B13F")

    label("loc_B0B3")


    ChrTalk(
        0xFE,
        (
            "セールやバーゲンso\x01",
            "When I bought what I want cheaply\x01",
            "Pleasure is exceptional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially in my case,\x01",
            "Because extra Mira will be pocket money\x01",
            "Joy also doubled.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B13F")

    Jump("loc_B4AC")

    label("loc_B144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B1E9")

    ChrTalk(
        0xFE,
        (
            "今日はオルキスタワーの除幕式so\x01",
            "It was quite exciting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Something like the smell of sale.\x01",
            "I will not go today.\x01",
            "Let's go round some department stores too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_B1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B315")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2AA")

    ChrTalk(
        0xFE,
        (
            "The tips on saving are collected information.\x01",
            "Time sale and bargains\x01",
            "I have to make sure not to miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if it's time now\x01",
            "If you go shopping in a stall venue\x01",
            "Mira seems to float somewhat.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B310")

    label("loc_B2AA")


    ChrTalk(
        0xFE,
        (
            "For pocket money as well,\x01",
            "Conservation, saving ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Time sale and bargains\x01",
            "I have to make sure not to miss it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B310")

    Jump("loc_B4AC")

    label("loc_B315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B391")

    ChrTalk(
        0xFE,
        (
            "Because there are few shoppers on rainy days\x01",
            "You can look at the products thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, today too\x01",
            "I think I can do a good shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_B391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B4AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B431")

    ChrTalk(
        0xFE,
        (
            "When Mom asks you to use it,\x01",
            "You give me a little Mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So shopping,\x01",
            "My extraordinary Mira is my pocket money\x01",
            "It will be diminished.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B4AC")

    label("loc_B431")


    ChrTalk(
        0xFE,
        (
            "…… But recently, Mama\x01",
            "Only the gross margin of shopping\x01",
            "He does not give Mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "う、Well …\x01",
            "My pocket money plan is …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4AC")

    TalkEnd(0xFE)
    Return()

    # Function_14_ABBB end

    def Function_15_B4B0(): pass

    label("Function_15_B4B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B548")

    ChrTalk(
        0xFE,
        (
            "About this\x01",
            "I wish I had my shop off,\x01",
            "Liver is also laying Malte.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, there's my wife's wife\x01",
            "It's a nice place though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B5CB")

    label("loc_B548")


    ChrTalk(
        0xFE,
        (
            "About this\x01",
            "I wish I had my shop off,\x01",
            "Liver is also laying Malte.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I came all the way\x01",
            "I wonder if I will help the shop today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5CB")

    TalkEnd(0xFE)
    Return()

    # Function_15_B4B0 end

    def Function_16_B5CF(): pass

    label("Function_16_B5CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B67C")

    ChrTalk(
        0xFE,
        (
            "To terrorists,\x01",
            "The drawing of Orkis Tower is\x01",
            "It seems that there is a high possibility of crossing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However,\x01",
            "Where do you intend to attack?\x01",
            "I'd rather believe that there are no holes … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7EE")

    label("loc_B67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B6E5")

    ChrTalk(
        0xFE,
        (
            "Both \"red constellation\" and \"black moon\"\x01",
            "I will not show up in my place right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow, alertness is not easy, is not it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B7EE")

    label("loc_B6E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B7EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B784")

    ChrTalk(
        0xFE,
        "Oh, the Special Affairs Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can see,\x01",
            "I'm wary of street stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anta et al's\x01",
            "Do what you can do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_B7EE")

    label("loc_B784")


    ChrTalk(
        0xFE,
        (
            "As you can see,\x01",
            "I'm wary of street stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anta et al's\x01",
            "Do what you can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7EE")

    TalkEnd(0xFE)
    Return()

    # Function_16_B5CF end

    SaveToFile()

Try(main)
