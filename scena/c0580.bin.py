from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0580.bin",                # FileName
        "c0580",                    # MapName
        "c0580",                    # Location
        0x0028,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 40, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0580",                  # 0
        "Mrs. Imelda",           # 1
        "SE control",                 # 2
    ))

    AddCharChip((
        "chr/ch09002.itc",                   # 00
    ))

    DeclNpc(4294966546, 100,     4800,    180,  261,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294966546, 0,       3500,    1500,    4294966546, 1500,    4800,    0x007E, 0,  2,  0x0000)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_126",          # 01, 1
        "Function_2_19B",          # 02, 2
        "Function_3_19F",          # 03, 3
        "Function_4_20AE",         # 04, 4
        "Function_5_2934",         # 05, 5
        "Function_6_35E7",         # 06, 6
        "Function_7_35FD",         # 07, 7
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Return()

    # Function_0_114 end

    def Function_1_126(): pass

    label("Function_1_126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_159")

    label("loc_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A")
    Sound(128, 1, 50, 0)

    label("loc_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_191")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_191")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    Return()

    # Function_1_126 end

    def Function_2_19B(): pass

    label("Function_2_19B")

    Call(0, 3)
    Return()

    # Function_2_19B end

    def Function_3_19F(): pass

    label("Function_3_19F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1")
    TalkEnd(0x8)
    Call(0, 5)
    Return()

    label("loc_1C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4")
    TalkEnd(0x8)
    Call(0, 4)
    Return()

    label("loc_1E4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_24C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_26B")
    OP_AF(0x43)
    Jump("loc_27D")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27B")
    OP_AF(0x44)
    Jump("loc_27D")

    label("loc_27B")

    OP_AF(0x43)

    label("loc_27D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20A5")

    label("loc_28C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A0")
    Jump("loc_20A5")

    label("loc_2A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C")

    ChrTalk(
        0x8,
        (
            "(Rattling, rattling … …)\x01",
            "To President's detention\x01",
            "Huge trees that appeared in wetlands ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Especially for large trees,\x01",
            "Various speculation also on the conducting net\x01",
            "Hey, hey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That kind of thing appeared so much,\x01",
            "At this time as a new tourist attraction\x01",
            "What do you want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's right, when diplomacy resumed\x01",
            "I guess I can make a profit as well.\x01",
            "Hihyakhya …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4CE")

    label("loc_41C")


    ChrTalk(
        0x8,
        (
            "It is a big fuss around the world,\x01",
            "That huge tree is attached to me\x01",
            "I started seeing it as a tree with more money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For the time when diplomacy was resumed,\x01",
            "I can not afford new properties.\x01",
            "Hihyakhya ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE")

    Jump("loc_20A5")

    label("loc_4D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_649")

    ChrTalk(
        0x8,
        "Oh, they are children of the support department.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Things that you are moving\x01",
            "It seems to be various interesting things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FEven if it gets interesting, I am in trouble … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAnyway, not to go out\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I understood that I understood.\x01",
            "Let's say you watch the game from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At most the presidents\x01",
            "Scratch it and give it to me.\x01",
            "Hihyakhya …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6DC")

    label("loc_649")


    ChrTalk(
        0x8,
        (
            "Things that you are moving\x01",
            "It seems to be various interesting things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At most the presidents\x01",
            "Scratch it and give it to me.\x01",
            "Hihyakhya …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DC")

    Jump("loc_20A5")

    label("loc_6E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_92C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_863")

    ChrTalk(
        0x8,
        (
            "Hihyakhya …!\x01",
            "The speech of the example, it was quite interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No way Empire and Republic\x01",
            "It is not meant to cut down on the way up there.\x01",
            "Baboons and tricks are also unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "… …. Now, a Dieter's boy\x01",
            "I do not know what I'm planning to do,\x01",
            "The empire and the republic will not be silent either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, now\x01",
            "The antique mountain that is kept in the warehouse\x01",
            "I would rather move it to a safe place.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_927")

    label("loc_863")


    ChrTalk(
        0x8,
        (
            "Dieter's boy\x01",
            "I do not know what I'm planning to do,\x01",
            "The empire and the republic will not be silent either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, now\x01",
            "The antique mountain that is kept in the warehouse\x01",
            "I would rather move it to a safe place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_927")

    Jump("loc_20A5")

    label("loc_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A27")

    ChrTalk(
        0x8,
        (
            "It appeared in the old city in that raid incident\x01",
            "To a huge monster, I owned you\x01",
            "The apartment has been destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, I've been looking for a man\x01",
            "There is no choice but to laugh when it is destroyed over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Well, good-bye.\x01",
            "What did you do with that one?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AC2")

    label("loc_A27")


    ChrTalk(
        0x8,
        (
            "I saw the existence of the broken apartment,\x01",
            "There is no choice but to laugh when it is destroyed over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To rebuild newly\x01",
            "It's troublesome and it takes Mira … …\x01",
            "Every once in a while it will not let go of land.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC2")

    Jump("loc_20A5")

    label("loc_AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF7")

    ChrTalk(
        0x8,
        (
            "The soldiers,\x01",
            "No way to occupy a town\x01",
            "It is not great to imitate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also in the doll factory in the mountain path\x01",
            "I contacted it once,\x01",
            "I did not connect after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyahya,\x01",
            "Well it's about Jorg\x01",
            "I do not worry though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Unexpectedly, even in such circumstances, we are making dolls\x01",
            "You may be excited.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C9B")

    label("loc_BF7")


    ChrTalk(
        0x8,
        (
            "Also in the doll factory in the mountain path\x01",
            "I contacted it once,\x01",
            "I did not connect after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Baboons, it's about Jorg\x01",
            "In doll production even in this situation\x01",
            "It may be exciting though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9B")

    Jump("loc_20A5")

    label("loc_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2A")

    ChrTalk(
        0x8,
        (
            "Hihyacha, in this rain\x01",
            "Even just a few customers\x01",
            "It looks like it will be further reduced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys, at any cost\x01",
            "Even at the store's shelf cleaning at this time\x01",
            "Will you do it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWell, I will refuse to indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyah, it is a joke.\x01",
            "Even though there are expensive items\x01",
            "Who should touch the shelves?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    Jump("loc_EA2")

    label("loc_E2A")


    ChrTalk(
        0x8,
        (
            "Once, according to the conducting net\x01",
            "It seems that it will clear up in the afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihya, that does not matter\x01",
            "It will not increase the customer's foot of the store, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA2")

    Jump("loc_20A5")

    label("loc_EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F85")

    ChrTalk(
        0x8,
        (
            "If you were looking at the power net a while ago\x01",
            "Breaking news coming in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anything, in the west highway\x01",
            "I had a train derailment accident\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihaya, something\x01",
            "I feel the smell of kina\x01",
            "Is it only me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100F")

    label("loc_F85")


    ChrTalk(
        0x8,
        (
            "According to the power net,\x01",
            "A derailment accident on the west road\x01",
            "I guess there was it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihaya, something\x01",
            "I feel the smell of kina\x01",
            "Is it only me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100F")

    Jump("loc_20A5")

    label("loc_1014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112B")

    ChrTalk(
        0x8,
        (
            "As expected of the truth\x01",
            "About that Jijii\x01",
            "There are not so many things to know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everything, normally getting out to the table\x01",
            "Like a silent doll making\x01",
            "Because it is unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I am at the workshop doll\x01",
            "I only have to make money.\x01",
            "Hihyakhya ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11CF")

    label("loc_112B")


    ChrTalk(
        0x8,
        (
            "As expected of the truth\x01",
            "About that Jijii\x01",
            "There are not so many things to know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I am at the workshop doll\x01",
            "I only have to make money.\x01",
            "Hihyakhya ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CF")

    Jump("loc_20A5")

    label("loc_11D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EB")

    ChrTalk(
        0x8,
        (
            "(Rattling rattling … …)\x01",
            "Indeed, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even on the power net\x01",
            "Regarding the independence or not\x01",
            "It seems to be pros and cons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just for now\x01",
            "The majority of pro-factions are occupied\x01",
            "There seems to be no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyahya, the discussion will continue\x01",
            "I do not care at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_136C")

    label("loc_12EB")


    ChrTalk(
        0x8,
        (
            "Even on a conducting net\x01",
            "Regarding the independence or not\x01",
            "It seems to be disappointing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyahya, the discussion will continue\x01",
            "I do not care at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136C")

    Jump("loc_20A5")

    label("loc_1371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161C")

    ChrTalk(
        0x8,
        (
            "Oh, you are …\x01",
            "Certainly Epstein 's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI have not been to a long time, an old lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyaka, mission support department also\x01",
            "The members are finally stepping all together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that he will also enter the security of the trade council,\x01",
            "We have a perfect system and we are ready to go.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FAs usual, in various places\x01",
            "You seem to be communicating …\x02\x03",
            "#00000FIn the case of Imelda, information\x01",
            "Just to enjoy it yourself\x01",
            "In a sense it is saving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, that point\x01",
            "You do not mind relieving me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems like being caught by the police\x01",
            "I do not do hoes,\x01",
            "Because it is my creed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F… … to us that\x01",
            "How about saying.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 4)
    Jump("loc_16A5")

    label("loc_161C")


    ChrTalk(
        0x8,
        (
            "Hihyaka, mission support department also\x01",
            "The members are finally stepping all together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the future,\x01",
            "Activities of you\x01",
            "Let's say it's entertaining.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A5")

    Jump("loc_20A5")

    label("loc_16AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F0")

    ChrTalk(
        0x8,
        (
            "(Rattling rattling … …)\x01",
            "How I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even on the power net,\x01",
            "About Orkis Tower\x01",
            "He seems to be making a lot of noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is a skyscraper so big that it hits the sky,\x01",
            "It is quite a tourist attraction\x01",
            "Economic effects will be expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, now\x01",
            "Looking at the tower overlooking property\x01",
            "I suppose I should hold it down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1892")

    label("loc_17F0")


    ChrTalk(
        0x8,
        (
            "That Orkis Tower,\x01",
            "It is quite a tourist attraction\x01",
            "Economic effects will be expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, now\x01",
            "Looking at the tower overlooking property\x01",
            "I suppose I should hold it down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1892")

    Jump("loc_20A5")

    label("loc_1897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C4")

    ChrTalk(
        0x8,
        (
            "By the way, recently\x01",
            "I started reading the novel of a continuum … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Interesting is interesting, but to me\x01",
            "My hobby does not suit for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyahya, this time.\x01",
            "Shall I press them on you?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝３卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝３卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 2)
    Jump("loc_1B73")

    label("loc_19C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC1")

    ChrTalk(
        0x8,
        (
            "In the commerce meeting from tomorrow,\x01",
            "It seems that the leaders of each country gather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Regardless of the other leaders,\x01",
            "\"Chancellor of Iron and Blood\" and President of the Republic of\x01",
            "I would like to see you face to face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Both countries have long been conflicting,\x01",
            "What kind of meeting will you … …\x01",
            "Hihyahya, this is a sightseeing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B73")

    label("loc_1AC1")


    ChrTalk(
        0x8,
        (
            "In the commerce meeting from tomorrow,\x01",
            "\"Chancellor of Iron and Blood\" and President of the Republic of\x01",
            "I would like to see you face to face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Both countries have long been conflicting,\x01",
            "What kind of meeting will you … …\x01",
            "Hihyahya, this is a sightseeing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B73")

    Jump("loc_20A5")

    label("loc_1B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5D")

    ChrTalk(
        0x8,
        (
            "Apparently, before long, conspicuous guys\x01",
            "On the site of Rubathe\x01",
            "It seems that it entered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The black moon guys had\x01",
            "I thought only when I got it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, somewhat funny thing\x01",
            "It seems to be getting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CDF")

    label("loc_1C5D")


    ChrTalk(
        0x8,
        (
            "On the site of Rubathe, people in the black moon\x01",
            "I thought only when I got it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, somewhat funny thing\x01",
            "It seems to be getting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDF")

    Jump("loc_20A5")

    label("loc_1CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7B")

    ChrTalk(
        0x8,
        (
            "Speaking of which, back alley\x01",
            "It is the site of Rubathe … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it keeps going as it is\x01",
            "It seems likely to be like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, if this is the case\x01",
            "I kept holding in advance,\x01",
            "I wish I could sell it at a high price.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Speaking of which, this person\x01",
            "It was land acquisition … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F2D")

    label("loc_1E7B")


    ChrTalk(
        0x8,
        (
            "Speaking of which, back alley\x01",
            "Ruberty's site ……\x01",
            "I heard that the black moon is coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, if this is the case\x01",
            "I kept holding in advance,\x01",
            "I wish I could sell it at a high price.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2D")

    Jump("loc_20A5")

    label("loc_1F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_20A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2041")

    ChrTalk(
        0x8,
        (
            "The support department restarted,\x01",
            "I will keep you focused in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihaya ……\x01",
            "Also providing hot news,\x01",
            "Please entertain me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FBa, to entertain another\x01",
            "I'm not doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FIt is an interesting old lady.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20A5")

    label("loc_2041")


    ChrTalk(
        0x8,
        (
            "The support department restarted,\x01",
            "I will keep you focused in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyahya, and also me\x01",
            "Please entertain me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A5")

    Jump("loc_1EE")

    label("loc_20AA")

    TalkEnd(0x8)
    Return()

    # Function_3_19F end

    def Function_4_20AE(): pass

    label("Function_4_20AE")

    EventBegin(0x0)
    Fade(500)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    SetChrPos(0x101, -1540, 0, 1900, 45)
    SetChrPos(0x102, 390, 0, 2110, 0)
    SetChrPos(0x109, -1050, 0, 800, 0)
    SetChrPos(0x105, 150, 0, 830, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#11PHehe oh welcome\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11POh, you are\x01",
            "Buddies of the Special Affairs Support Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHehe long time no see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FLong time no see, Ms. Imelda\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYou're lively as usual\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHuh, how are you doing?\x01",
            "Recently in a boring days\x01",
            "I was tired of getting tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PRubache was also crushed,\x01",
            "You have also stopped working for a while …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIn addition, I often used it\x01",
            "Information shop on the power guide net\x01",
            "I did not stop working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105F(Information source in the orbal net…)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(I wonder about Jonah.\x01",
            "I'm seconded to the Foundation now … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11POh, by the way, I have an unfamiliar face\x01",
            "It seems to be together ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSo, what's new in the support department\x01",
            "Are you guys here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHead of bad team to security guards ……\x01",
            "Hihyaka, at the time of restart\x01",
            "It seems that interesting pieces came together.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10105FH-how do you know that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FUm, I want an information store\x01",
            "To the extent not using it\x01",
            "Are you too busy talking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHihyakhya ……\x01",
            "Separately the information source\x01",
            "Because it is not one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10309FWell that's quite interesting\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11POops it looks like.\x01",
            "To express the gratitude for giving my bother to you,\x01",
            "Let 's do something good for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHere, take it\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '伊梅尔达馆的钥匙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('伊梅尔达馆的钥匙', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#6P#00105FThis is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHihyahya,\x01",
            "I belong to Old City\x01",
            "The key to \"Maison Imelda\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FOh, that's right.\x01",
            "Such a name boro apartment\x01",
            "I was in that neighborhood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHey you it's not run down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHun, oh well.\x01",
            "It seems that devils are boiling again these days,\x01",
            "Please clean up when you feel like it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FYes, there are\x01",
            "We also requested the extermination of arranging monsters\x01",
            "I came in … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FSo that's the purpose of this request today then\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHihaya ……\x01",
            "Well if it feels good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI'll leave it to you guys\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetScenarioFlags(0x139, 4)
    OP_29(0x67, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_20AE end

    def Function_5_2934(): pass

    label("Function_5_2934")

    EventBegin(0x0)
    Fade(500)
    SoundLoad(841)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    SetChrPos(0x109, -2840, 0, 390, 44)
    SetChrPos(0x105, -1360, 0, -710, 44)
    OP_0D()
    BeginChrThread(0x9, 1, 0, 6)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With the communication device under the counter\x01",
            "Mrs. Imelda is talking.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x8,
        (
            "#11P…… Chit, that gig.\x01",
            "I will not go out at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FMr. Imelda,\x01",
            "what happened?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2C9F")

    ChrTalk(
        0x8,
        "#11POh, are you guys here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNo, about the next new doll\x01",
            "I thought to ask Jorg's guy,\x01",
            "I was in contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FJorgg to the old man … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, but from a little while ago\x01",
            "I do not have any signs of connecting one way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI wonder if they are in the studio … …\x01",
            "Chi, if you are working\x01",
            "It will not be possible to connect for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00003F(… … At the previous request,\x01",
            "Imelda is with Jorggu's old man\x01",
            "I heard that it is an old relationship. )\x02\x03",
            "(In this case, about the puppet factory … ….\x01",
            "I guess I'll ask something. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C0")

    label("loc_2C9F")


    ChrTalk(
        0x8,
        "#11POh, are you guys here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNo, about the next new doll\x01",
            "I thought to ask Jorg's guy,\x01",
            "I was in contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut, from a little while ago\x01",
            "I do not have any signs of connecting one way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI wonder if they are in the studio … …\x01",
            "Chi, if you are working\x01",
            "It will not be possible to connect for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)
    Sleep(50)
    OP_64(0x102)
    Sleep(50)
    OP_64(0x103)
    Sleep(50)
    OP_64(0x104)
    Sleep(50)
    OP_64(0x109)
    Sleep(50)
    OP_64(0x105)

    ChrTalk(
        0x101,
        (
            "#6P#00005FJorg …\x01",
            "It's a new doll … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FWell, maybe ….\x01",
            "Jorg Rosenberg engineer! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FMr. Imelda,\x01",
            "Did you know each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, once in a while\x01",
            "Selling agencies for that doll\x01",
            "It's under contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHowever, this guy is unbelievable.\x01",
            "I do not have much flexibility\x01",
            "There are many things that are annoying.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00006F(…… in a place like this\x01",
            "I did not know you had a acquaintance. )\x02\x03",
            "(In this case, about the puppet factory … ….\x01",
            "I guess I'll ask something. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C0")


    ChrTalk(
        0x8,
        (
            "#11P…… Even so,\x01",
            "Is something useful for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHihyahya,\x01",
            "If you are dealing with antiques\x01",
            "You let me respond at any time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWell, well, that's not it.\x01",
            "I'd like to ask you a moment … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Rosenberg Studio\x01",
            "I asked about Jorgga's old man.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11P…… why are you again\x01",
            "You are sniffing such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FNo~……\x01",
            "A little interest-oriented?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell okay, but … as expected,\x01",
            "What I know about Jorg\x01",
            "There are not so many.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PEverything, normally getting out to the table\x01",
            "Like a silent doll making\x01",
            "Because it is unbelievable.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3389")

    ChrTalk(
        0x8,
        (
            "#11PThe stage equipment of the alkane shell\x01",
            "I said earlier that I'm working on it,\x01",
            "I do not know anything further.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D8")

    label("loc_3389")


    ChrTalk(
        0x8,
        (
            "#11PI certainly underwrite a sales representative,\x01",
            "I do not know anything deeply.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D8")


    ChrTalk(
        0x109,
        "#10106FIs that so …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell, I am at the workshop doll\x01",
            "All I can do is make money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI can not believe that private Jigsy's Private\x01",
            "I do not know it.\x01",
            "Hihyakhya ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F(I see, I see … ….\x01",
            "It's a surprisingly dry relationship. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200F(That's why,\x01",
            "Even if the relationship is kept\x01",
            "I can think about it … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F(Well, in that case\x01",
            "After all we have to visit directly\x01",
            "Is not it? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000F(That's right ……\x01",
            "Everyone, let's go. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetScenarioFlags(0x16F, 5)
    OP_24(0x349)
    EventEnd(0x5)
    Return()

    # Function_5_2934 end

    def Function_6_35E7(): pass

    label("Function_6_35E7")

    Sound(841, 2, 50, 0)
    Sleep(1800)
    OP_24(0x349)
    Sound(813, 0, 20, 0)
    Sleep(500)
    Return()

    # Function_6_35E7 end

    def Function_7_35FD(): pass

    label("Function_7_35FD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_35FD end

    SaveToFile()

Try(main)
