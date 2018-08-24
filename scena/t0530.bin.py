from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0530.bin",                # FileName
        "t0530",                    # MapName
        "t0530",                    # Location
        0x0040,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 64, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0530",                  # 0
        "Backerei",               # 1
        "Kimmy",                  # 2
        "Harold",                 # 3
    ))

    AddCharChip((
        "chr/ch23400.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch09300.itc",                   # 02
    ))

    DeclNpc(4294967167, 0,       3640,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294962766, 0,       4500,    320,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294963896, 0,       3559,    315,  389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(4294967256, 0,       2120,    1000,    4294967166, 1500,    3640,    0x007E, 0,  3,  0x0000)

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_309",          # 02, 2
        "Function_3_342",          # 03, 3
        "Function_4_346",          # 04, 4
        "Function_5_15AE",         # 05, 5
        "Function_6_1CB4",         # 06, 6
        "Function_7_1DB3",         # 07, 7
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_178"),
        (1, "loc_184"),
        (2, "loc_190"),
        (3, "loc_19C"),
        (4, "loc_1A8"),
        (5, "loc_1B4"),
        (6, "loc_1C0"),
        (SWITCH_DEFAULT, "loc_1CC"),
    )


    label("loc_178")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_184")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_190")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_19C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1EF")

    Return()

    # Function_0_138 end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FE")
    Jump("loc_308")

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_20C")
    Jump("loc_308")

    label("loc_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_21A")
    Jump("loc_308")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_245")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1000, 0, 1600, 315)
    TurnDirection(0x8, 0xA, 0)
    Jump("loc_308")

    label("loc_245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_253")
    Jump("loc_308")

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_261")
    Jump("loc_308")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_26F")
    Jump("loc_308")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_282")
    SetChrFlags(0x9, 0x80)
    Jump("loc_308")

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_290")
    Jump("loc_308")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A3")
    SetChrFlags(0x9, 0x80)
    Jump("loc_308")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2B1")
    Jump("loc_308")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D5")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    TurnDirection(0x9, 0xA, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_308")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E3")
    Jump("loc_308")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2F1")
    Jump("loc_308")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FF")
    Jump("loc_308")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_308")

    label("loc_308")

    Return()

    # Function_1_1F0 end

    def Function_2_309(): pass

    label("Function_2_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_31B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_341")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_341")

    Return()

    # Function_2_309 end

    def Function_3_342(): pass

    label("Function_3_342")

    Call(0, 4)
    Return()

    # Function_3_342 end

    def Function_4_346(): pass

    label("Function_4_346")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C4")
    OP_AF(0x58)
    Jump("loc_3E6")

    label("loc_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D4")
    OP_AF(0x57)
    Jump("loc_3E6")

    label("loc_3D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E4")
    OP_AF(0x56)
    Jump("loc_3E6")

    label("loc_3E4")

    OP_AF(0x55)

    label("loc_3E6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15A5")

    label("loc_3F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_409")
    Jump("loc_15A5")

    label("loc_409")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_421")
    TalkEnd(0x8)
    Return()

    label("loc_421")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_550")

    ChrTalk(
        0x8,
        (
            "The mine is unyielding\x01",
            "pride of the citizens of\x01",
            "Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter the abnormal situation, as\x01",
            "long as we don't forget our pride,\x01",
            "we will overcome it for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You all must have something\x01",
            "you can't give up no matter\x01",
            "what. Don't forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_60F")

    label("loc_550")


    ChrTalk(
        0x8,
        (
            "No matter the abnormal situation, as\x01",
            "long as we don't forget our pride,\x01",
            "we will overcome it for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You all must have something\x01",
            "you can't give up no matter\x01",
            "what. Don't forget it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60F")

    Jump("loc_15A5")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_746")

    ChrTalk(
        0x8,
        (
            "Because I'm uneducated, I don't\x01",
            "really get what a declaration\x01",
            "of invalidity is, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope society quickly becomes\x01",
            "a place where Kimmy and the\x01",
            "brats can leave peacefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...To realize that, it's pathetic\x01",
            "to entrust the resistance with\x01",
            "all the dangerous stuff.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7FD")

    label("loc_746")


    ChrTalk(
        0x8,
        (
            "To entrust the resistance\x01",
            "with all the dangerous\x01",
            "stuff is pathetic, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope they do their best to create\x01",
            "a society where Kimmy and brats can\x01",
            "leave peacefully somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FD")

    Jump("loc_15A5")

    label("loc_802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B1")

    ChrTalk(
        0x8,
        (
            "It seems that before the resistance-\x01",
            "hunt began, those damn jaegers went\x01",
            "to the Mayor's house to greet him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking they owned the place, it\x01",
            "seems they brazenly said to "please\x01",
            "be careful to not leave town".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They probably intended to arrest\x01",
            "those of us who are cooperating\x01",
            "with the resistance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tch, if I'd been there, I\x01",
            "would've socked them one as\x01",
            "payback for the occupation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A3F")

    label("loc_9B1")


    ChrTalk(
        0x8,
        (
            "I heard that those damn\x01",
            "jaegers even set landmines\x01",
            "in the mountain path tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tch, if I'd been there,\x01",
            "I would've socked them\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3F")

    Jump("loc_15A5")

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B89")

    ChrTalk(
        0x8,
        (
            "The Mainz folks are still\x01",
            "depressed over those damn\x01",
            "jaegers' occupation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because I'm a Mainz resident, I\x01",
            "understand how they feel, but...\x01",
            "It's no use being depressed forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyhow, the miners and I, whose only\x01",
            "redeeming feature is being full of\x01",
            "spirit, must enliven everyone else.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C40")

    label("loc_B89")


    ChrTalk(
        0x8,
        (
            "Those damn jaegers were\x01",
            "frightening, but... It's\x01",
            "no use being depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The miners and I, whose only\x01",
            "redeeming feature is being full of\x01",
            "spirit, must enliven everyone else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C40")

    Jump("loc_15A5")

    label("loc_C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CCF")

    ChrTalk(
        0x8,
        (
            "I injured my leg and retired\x01",
            "from being a miner on a rainy\x01",
            "day just like this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...My old wound aches,\x01",
            "dammit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A5")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAD")

    ChrTalk(
        0x8,
        (
            "Kimmy's playing with\x01",
            "Hoffman's kiddo today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...There are just a few guys\x01",
            "her age, so I don't care if\x01",
            "they become friends, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if they'll date\x01",
            "each other in the\x01",
            "future?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E31")

    label("loc_DAD")


    ChrTalk(
        0x8,
        (
            "I can't be sure that things\x01",
            "won't go wrong in the future\x01",
            "between Kimmy and that kiddo...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I must strictly warn\x01",
            "Hoffman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E31")

    Jump("loc_15A5")

    label("loc_E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F25")

    ChrTalk(
        0x8,
        (
            "At the recent trade conference,\x01",
            "it seems talk of state\x01",
            "independence came up, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That new mayor has some\x01",
            "pretty good ideas. Hehe,\x01",
            "very good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's time we quit giving\x01",
            "in to the Empire and\x01",
            "Republic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F90")

    label("loc_F25")


    ChrTalk(
        0x8,
        (
            "State independence is\x01",
            "very good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We citizens of Crossbell\x01",
            "must to live more\x01",
            "proudly from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F90")

    Jump("loc_15A5")

    label("loc_F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1177")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C6")

    ChrTalk(
        0x8,
        (
            "Some time ago I was too worried\x01",
            "about Kimmy and unintentionally\x01",
            "intruded on a Sunday School lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I caused some trouble back there.\x01",
            "Because of my fierce look, it seems\x01",
            "I scared the other children...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't embarrass Kimmy\x01",
            "any further. I mustn't\x01",
            "do that again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1172")

    label("loc_10C6")


    ChrTalk(
        0x8,
        (
            "Some time ago I was too worried\x01",
            "about Kimmy and unintentionally\x01",
            "intruded on a Sunday School lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't embarrass Kimmy\x01",
            "any further. I mustn't\x01",
            "do that again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1172")

    Jump("loc_15A5")

    label("loc_1177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_127E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1216")

    ChrTalk(
        0x8,
        (
            "Oh, it seems Harold has\x01",
            "arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He should be running out of the\x01",
            "food ingredients he stocked up\x01",
            "on before. Hehe, perfect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1279")

    label("loc_1216")


    ChrTalk(
        0x8,
        (
            "Harold came at just the\x01",
            "right time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright, I guess I'll\x01",
            "give him a discount this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1279")

    Jump("loc_15A5")

    label("loc_127E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A3")

    ChrTalk(
        0x8,
        (
            "I'm not that educated,\x01",
            "you see. I don't get\x01",
            "complicated stuff, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That trade conference... In short,\x01",
            "it's a place where smart guys gather\x01",
            "and discuss different things, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope they have a nice\x01",
            "conference, if only for\x01",
            "the youngsters' future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1462")

    label("loc_13A3")


    ChrTalk(
        0x8,
        (
            "That trade conference... In short,\x01",
            "it's a place where smart guys gather\x01",
            "and discuss different things, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope they have a nice\x01",
            "conference, if only for\x01",
            "the youngsters' future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1462")

    Jump("loc_15A5")

    label("loc_1467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_15A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_152E")

    ChrTalk(
        0x8,
        (
            "Recently, the young\x01",
            "miners have gotten a nice\x01",
            "look on their faces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was a little worried\x01",
            "about the future, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, it seems that was\x01",
            "a needless worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15A5")

    label("loc_152E")


    ChrTalk(
        0x8,
        (
            "When Gantz was caught up in\x01",
            "that cult incident, I\x01",
            "wondered about the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, I didn't have to\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A5")

    Jump("loc_353")

    label("loc_15AA")

    TalkEnd(0x8)
    Return()

    # Function_4_346 end

    def Function_5_15AE(): pass

    label("Function_5_15AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166C")

    ChrTalk(
        0x9,
        (
            "It looks like a weird\x01",
            "tree has sprouted\x01",
            "outside, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Daddy seems to be\x01",
            "happier now that the\x01",
            "mine has been reopened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ehehe, Kimmy's happy\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16E3")

    label("loc_166C")


    ChrTalk(
        0x9,
        (
            "It looks like a weird\x01",
            "tree has sprouted\x01",
            "outside, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because daddy is happy,\x01",
            "Kimmy doesn't care about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E3")

    Jump("loc_1CB0")

    label("loc_16E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_175A")

    ChrTalk(
        0x9,
        (
            "There won't be Sunday\x01",
            "School lessons either\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope the sister's all\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB0")

    label("loc_175A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_17FD")

    ChrTalk(
        0x9,
        (
            "Daddy has been\x01",
            "constantly angry since\x01",
            "the independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Before, he was saying\x01",
            "independence was a good thing...\x01",
            "Maybe it didn't go so well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB0")

    label("loc_17FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1898")

    ChrTalk(
        0x9,
        (
            "Kimmy is always smiling,\x01",
            "smiling♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Daddy said that no matter\x01",
            "the situation, if you smile\x01",
            "you can feel full of energy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18F0")

    label("loc_1898")


    ChrTalk(
        0x9,
        (
            "Kimmy is always smiling,\x01",
            "smiling♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope everyone in town\x01",
            "cheers up quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F0")

    Jump("loc_1CB0")

    label("loc_18F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A3")

    ChrTalk(
        0x9,
        (
            "Daddy looks sad on rainy\x01",
            "days for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As I thought, he wanted\x01",
            "to continue mining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But Kimmy really likes\x01",
            "how daddy is now!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19F5")

    label("loc_19A3")


    ChrTalk(
        0x9,
        (
            "Daddy looks sad on rainy\x01",
            "days for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Kimmy must cheer him up.\x02",
    )

    CloseMessageWindow()

    label("loc_19F5")

    Jump("loc_1CB0")

    label("loc_19FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1A08")
    Jump("loc_1CB0")

    label("loc_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1A90")

    ChrTalk(
        0x9,
        (
            "Kimmy doesn't know what\x01",
            ""independence" is yet,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Daddy says independence\x01",
            "is a good thing, so\x01",
            "Kimmy agrees.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB0")

    label("loc_1A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1A9E")
    Jump("loc_1CB0")

    label("loc_1A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1ADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB9")
    Call(0, 6)
    Jump("loc_1AD5")

    label("loc_1AB9")


    ChrTalk(
        0x9,
        "Yaay, a Mishy plushie!\x02",
    )

    CloseMessageWindow()

    label("loc_1AD5")

    Jump("loc_1CB0")

    label("loc_1ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B60")

    ChrTalk(
        0x9,
        (
            "When Kimmy grows up,\x01",
            "she'll run the store\x01",
            "with daddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have to learn as much\x01",
            "as I can about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B83")

    label("loc_1B60")


    ChrTalk(
        0x9,
        (
            "Helping out, helping\x01",
            "out...♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B83")

    Jump("loc_1CB0")

    label("loc_1B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C3D")

    ChrTalk(
        0x9,
        (
            "In the past, daddy was\x01",
            "the best miner in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's why he's so strict with\x01",
            "the other miners. But the truth\x01",
            "is, he's very worried about them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CB0")

    label("loc_1C3D")


    ChrTalk(
        0x9,
        (
            "In the past, daddy was\x01",
            "the best miner in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's always strict, but\x01",
            "the truth is that he's\x01",
            "very kind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB0")

    TalkEnd(0xFE)
    Return()

    # Function_5_15AE end

    def Function_6_1CB4(): pass

    label("Function_6_1CB4")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        "Ah, it's Mr. Harold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Do you have business\x01",
            "with daddy today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#03600FYes, exactly. I brought\x01",
            "lots of different goods\x01",
            "with me.\x02\x03",
            "#03609FHaha, I even brought the\x01",
            "Mishy plushie you\x01",
            "wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Wow, really!? Hooray!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_6_1CB4 end

    def Function_7_1DB3(): pass

    label("Function_7_1DB3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1F9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1C")

    ChrTalk(
        0x101,
        (
            "#00000FHarold... You came to\x01",
            "Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#03600FYes, I'm here to deliver the produce\x01",
            "I bought from Armorica Village.\x02\x03",
            "#03603F...It seems the townspeople have been\x01",
            "spending their days having nightmares\x01",
            "about the attack recently.\x02\x03",
            "#03608FAlthough there were no victims, it\x01",
            "seems certain that scars from the\x01",
            "occupation remain...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F97")

    label("loc_1F1C")


    ChrTalk(
        0xA,
        (
            "#03603FA trader like myself\x01",
            "can't do anything major,\x01",
            "but...\x02\x03",
            "#03600FI want to do what I can\x01",
            "to make them smile\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F97")

    Jump("loc_1FF6")

    label("loc_1F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB7")
    Call(0, 6)
    Jump("loc_1FF6")

    label("loc_1FB7")


    ChrTalk(
        0xA,
        (
            "#03609FHaha... As expected,\x01",
            "lively children are the\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF6")

    TalkEnd(0xFE)
    Return()

    # Function_7_1DB3 end

    SaveToFile()

Try(main)
