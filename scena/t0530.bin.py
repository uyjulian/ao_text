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
        "Function_5_163B",         # 05, 5
        "Function_6_1D4D",         # 06, 6
        "Function_7_1E4D",         # 07, 7
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1637")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C2")
    OP_AF(0x58)
    Jump("loc_3E4")

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D2")
    OP_AF(0x57)
    Jump("loc_3E4")

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E2")
    OP_AF(0x56)
    Jump("loc_3E4")

    label("loc_3E2")

    OP_AF(0x55)

    label("loc_3E4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1632")

    label("loc_3F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407")
    Jump("loc_1632")

    label("loc_407")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41F")
    TalkEnd(0x8)
    Return()

    label("loc_41F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1632")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_538")

    ChrTalk(
        0x8,
        (
            "The mine is the citizens of\x01",
            "Mainz unyielding pride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter the abnormal situations,\x01",
            "as long as we don't forget pride,\x01",
            "we will overcome them for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You all have something\x01",
            "unyielding for sure.\x01",
            "Don't forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5E4")

    label("loc_538")


    ChrTalk(
        0x8,
        (
            "No matter the abnormal situations,\x01",
            "as long as we don't forget pride,\x01",
            "we will overcome them for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You all have something\x01",
            "unyielding for sure.\x01",
            "Don't forget it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E4")

    Jump("loc_1632")

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_711")

    ChrTalk(
        0x8,
        (
            "Because I'm uneducated, I don't\x01",
            "get well what a declaration of\x01",
            "invalidity is, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish society quickly becomes\x01",
            "a place where Kimmy and brats\x01",
            "can leave peacefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...To realize that, it's pathetic\x01",
            "to entrust the Resistance with\x01",
            "the dangerous stuff.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7C3")

    label("loc_711")


    ChrTalk(
        0x8,
        (
            "To entrust the Resistance with\x01",
            "the dangerous stuff is pathetic, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish they somehow did their best\x01",
            "to have a society where Kimmy and\x01",
            "brats can leave peacefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C3")

    Jump("loc_1632")

    label("loc_7C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_984")

    ChrTalk(
        0x8,
        (
            "Seems that before the Resistance-hunt\x01",
            "began, those damn jaegers went to\x01",
            "the Town Mayor's house to greet him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking they owned the place,\x01",
            "it seems they brazenly said to\x01",
            ""please be careful to not leave town".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They probably intended to restraint us\x01",
            "who're cooperating with the Resistance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tch, if I had been present there,\x01",
            "I would've socked them one as\x01",
            "payback for the occupation incident.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A16")

    label("loc_984")


    ChrTalk(
        0x8,
        (
            "I heard that those damn jaegers even set\x01",
            "landmines in the mountain path tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tch, if I had been present,\x01",
            "I would've socked them one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A16")

    Jump("loc_1632")

    label("loc_A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6E")

    ChrTalk(
        0x8,
        (
            "The Mainz's folks are still\x01",
            "depressed due to those\x01",
            "damn jaegers' occupation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because I'm a concerned person too,\x01",
            "I understand their feelings, but...\x01",
            "It's no use being depressed forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In any case, me and the miners whose\x01",
            "only redeeming feature is being full of\x01",
            "vigor must enliven everyone else.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C23")

    label("loc_B6E")


    ChrTalk(
        0x8,
        (
            "Those damn jaegers were frightening, but...\x01",
            "It's no use being depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Me and the miners whose only\x01",
            "redeeming feature is being full of\x01",
            "vigor must enliven everyone else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C23")

    Jump("loc_1632")

    label("loc_C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CB6")

    ChrTalk(
        0x8,
        (
            "It was a rainy day like this too\x01",
            "when I injured my leg and\x01",
            "retired from being a miner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...My old wound aches, dammit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1632")

    label("loc_CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAB")

    ChrTalk(
        0x8,
        (
            "Today, Kimmy seems she's playing\x01",
            "with Hoffman's kiddo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...There're just a few guys her age,\x01",
            "so I don't care if they become friends, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It won't turn out that in the\x01",
            "future they'll be dating, huh...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E2F")

    label("loc_DAB")


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
            "...I must strictly\x01",
            "warn Hoffman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2F")

    Jump("loc_1632")

    label("loc_E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3F")

    ChrTalk(
        0x8,
        (
            "It seems that at the recent Trade\x01",
            "Conference talks of a state\x01",
            "independence came up, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That new mayor can think\x01",
            "about some quite nice things.\x01",
            "Eh eh, very good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's time we have to quit giving in\x01",
            "to the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FAC")

    label("loc_F3F")


    ChrTalk(
        0x8,
        "A state independence is very good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We citizens of Crossbell\x01",
            "have to live more\x01",
            "proudly from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAC")

    Jump("loc_1632")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F2")

    ChrTalk(
        0x8,
        (
            "A little time ago I was too worried\x01",
            "about Kimmy and I unintentionally\x01",
            "intruded in a Sunday School lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I caused some trouble back there.\x01",
            "Because of my fierce look,\x01",
            "it seems I've scared the other children...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't embarrass Kimmy\x01",
            "any more than this.\x01",
            "I mustn't do that again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11AB")

    label("loc_10F2")


    ChrTalk(
        0x8,
        (
            "A little time ago I was too worried\x01",
            "about Kimmy and I unintentionally\x01",
            "intruded in a Sunday School lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't embarrass Kimmy\x01",
            "any more than this.\x01",
            "I mustn't do that again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11AB")

    Jump("loc_1632")

    label("loc_11B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_12D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1259")

    ChrTalk(
        0x8,
        (
            "Oh, it seems that\x01",
            "Harold has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's almost time he ran out of all the food\x01",
            "ingredients he stocked up before.\x01",
            "Eh eh, perfect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12D3")

    label("loc_1259")


    ChrTalk(
        0x8,
        (
            "Harold has come\x01",
            "quite at the\x01",
            "right time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright, I guess I'll give him a\x01",
            "discount on the cost price this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D3")

    Jump("loc_1632")

    label("loc_12D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_14CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1404")

    ChrTalk(
        0x8,
        (
            "I'm not that much educated, you see.\x01",
            "I don't get complicated stuff, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That Trade Conference...\x01",
            "In short, it's a place where smart guys\x01",
            "gather and discuss many things, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish they absolutely have\x01",
            "a nice conference even for\x01",
            "the youngsters' future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C5")

    label("loc_1404")


    ChrTalk(
        0x8,
        (
            "That Trade Conference...\x01",
            "In short, it's a place where smart guys\x01",
            "gather and discuss many things, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish they absolutely have\x01",
            "a nice conference even for\x01",
            "the youngsters' future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C5")

    Jump("loc_1632")

    label("loc_14CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AB")

    ChrTalk(
        0x8,
        (
            "Recently, the look on the young\x01",
            "miners' faces have become nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was a little worried about what\x01",
            "would've happened in the future, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Eh eh, it seems it was\x01",
            "an unnecessary worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1632")

    label("loc_15AB")


    ChrTalk(
        0x8,
        (
            "When Gantz was caught in that\x01",
            "Cult incident I thought what\x01",
            "would've happened in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Eh eh, I didn't\x01",
            "have to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1632")

    Jump("loc_353")

    label("loc_1637")

    TalkEnd(0x8)
    Return()

    # Function_4_346 end

    def Function_5_163B(): pass

    label("Function_5_163B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1773")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F7")

    ChrTalk(
        0x9,
        (
            "It seems that a weird tree\x01",
            "has sprouted outside, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Daddy seems to be\x01",
            "happier that the mine\x01",
            "has been reopened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Eheheh, Kimmy too is happy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_176E")

    label("loc_16F7")


    ChrTalk(
        0x9,
        (
            "It seems that a weird tree\x01",
            "has sprouted outside, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because daddy is happy,\x01",
            "Kimmy doesn't care about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_176E")

    Jump("loc_1D49")

    label("loc_1773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_17E3")

    ChrTalk(
        0x9,
        (
            "There won't be Sunday School\x01",
            "lessons too for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope the Sister\x01",
            "is all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D49")

    label("loc_17E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_188B")

    ChrTalk(
        0x9,
        (
            "Daddy has been always angry\x01",
            "since after the independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Before, he was saying that\x01",
            "independence was a good thing...\x01",
            "Didn't it go well, maybe?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D49")

    label("loc_188B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1988")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1926")

    ChrTalk(
        0x9,
        (
            "Kimmy is always\x01",
            "smiling, smiling♪\x02",
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
    Jump("loc_1983")

    label("loc_1926")


    ChrTalk(
        0x9,
        (
            "Kimmy is always\x01",
            "smiling, smiling♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope that everyone\x01",
            "in town cheers up\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1983")

    Jump("loc_1D49")

    label("loc_1988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A35")

    ChrTalk(
        0x9,
        (
            "Somehow daddy looks\x01",
            "sad on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As I thought, he wanted to\x01",
            "continue doing his miner work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But Kimmy now\x01",
            "really likes daddy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A7F")

    label("loc_1A35")


    ChrTalk(
        0x9,
        (
            "Somehow daddy looks\x01",
            "sad on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Kimmy must\x01",
            "cheer him up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7F")

    Jump("loc_1D49")

    label("loc_1A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1A92")
    Jump("loc_1D49")

    label("loc_1A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B1E")

    ChrTalk(
        0x9,
        (
            "Kimmy doesn't know\x01",
            "what "independence"\x01",
            "is yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Daddy says independence\x01",
            "is a good thing, so Kimmy\x01",
            "too agrees.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D49")

    label("loc_1B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B2C")
    Jump("loc_1D49")

    label("loc_1B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B47")
    Call(0, 6)
    Jump("loc_1B64")

    label("loc_1B47")


    ChrTalk(
        0x9,
        "Yaaay, a Michey plushy!\x02",
    )

    CloseMessageWindow()

    label("loc_1B64")

    Jump("loc_1D49")

    label("loc_1B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1C15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BED")

    ChrTalk(
        0x9,
        (
            "When Kimmy grows up,\x01",
            "she'll run the store with daddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have to learn a lot\x01",
            "about the job now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C10")

    label("loc_1BED")


    ChrTalk(
        0x9,
        "Helping out, helping out...♪\x02",
    )

    CloseMessageWindow()

    label("loc_1C10")

    Jump("loc_1D49")

    label("loc_1C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD4")

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
            "That's why he's often strict to all\x01",
            "the other miners, but the truth is \x01",
            "that he's very worried about them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D49")

    label("loc_1CD4")


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
            "He's always strict, but the truth\x01",
            "is that he's very gentle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D49")

    TalkEnd(0xFE)
    Return()

    # Function_5_163B end

    def Function_6_1D4D(): pass

    label("Function_6_1D4D")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        "Ah, it's Mr. Harold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Did you come for business with daddy today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#03600FYes, exactly.\x01",
            "I brought many articles today.\x02\x03",
            "#03609FUh uh, I even brought the Michey\x01",
            "plushy you wanted before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wow, really!?\x01",
            "Hooray!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_6_1D4D end

    def Function_7_1E4D(): pass

    label("Function_7_1E4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_202D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB6")

    ChrTalk(
        0x101,
        (
            "#00000FMr. Harold...\x01",
            "You came to Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#03600FYes, I just came to deliver\x01",
            "the produce I stocked up\x01",
            "from Armorica Village.\x02\x03",
            "#03603F...It seems that the townspeople\x01",
            "are recently spending the day\x01",
            "having nightmares about the raid.\x02\x03",
            "#03608FAlthough there were no victims,\x01",
            "it seems that the raid's ravages\x01",
            "certainly remain...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2028")

    label("loc_1FB6")


    ChrTalk(
        0xA,
        (
            "#03603FA trader like me can't\x01",
            "do anything major, but...\x02\x03",
            "#03600FI want to make them smile\x01",
            "again in some way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2028")

    Jump("loc_2092")

    label("loc_202D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2048")
    Call(0, 6)
    Jump("loc_2092")

    label("loc_2048")


    ChrTalk(
        0xA,
        (
            "#03609FHa ha...\x01",
            "As expected, children full\x01",
            "of energies are the best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2092")

    TalkEnd(0xFE)
    Return()

    # Function_7_1E4D end

    SaveToFile()

Try(main)
