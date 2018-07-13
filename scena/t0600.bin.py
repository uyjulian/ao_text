from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0600.bin",                # FileName
        "t0600",                    # MapName
        "t0600",                    # Location
        0x0069,                     # MapIndex
        "ed7301",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x20,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 105, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0600",                  # 0
        "Mine Captain Hoffman",   # 1
        "Miner Marlow",           # 2
        "Miner Gantz",            # 3
        "Miner Logy",             # 4
        "Miner Max",              # 5
        "Alec",                   # 6
    ))

    AddCharChip((
        "chr/ch26300.itc",                   # 00
        "chr/ch26200.itc",                   # 01
        "chr/ch30700.itc",                   # 02
        "chr/ch23000.itc",                   # 03
    ))

    DeclNpc(4294935446, 0,       32080,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4139,    0,       6690,    90,   261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294955826, 0,       15090,   19,   261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294950046, 50,      30370,   180,  261,  0x0, 0,   1,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(4294938436, 0,       56150,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)

    DeclActor(132500,  0,       18000,   1200,    132500,  1750,    18000,   0x007C, 0,  4,  0x0000)
    DeclActor(4294944756, 0,       54760,   1200,    4294944756, 1500,    54760,   0x007C, 0,  11, 0x0000)

    ChipFrameInfo(452, 0)                                        # 0

    ScpFunction((
        "Function_0_1C4",          # 00, 0
        "Function_1_27C",          # 01, 1
        "Function_2_2A7",          # 02, 2
        "Function_3_38F",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_465",          # 05, 5
        "Function_6_1051",         # 06, 6
        "Function_7_1AA0",         # 07, 7
        "Function_8_20A3",         # 08, 8
        "Function_9_2B75",         # 09, 9
        "Function_10_345F",        # 0A, 10
        "Function_11_35FD",        # 0B, 11
    ))


    def Function_0_1C4(): pass

    label("Function_0_1C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_204"),
        (1, "loc_210"),
        (2, "loc_21C"),
        (3, "loc_228"),
        (4, "loc_234"),
        (5, "loc_240"),
        (6, "loc_24C"),
        (SWITCH_DEFAULT, "loc_258"),
    )


    label("loc_204")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_210")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_21C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_228")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_234")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_240")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_24C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_258")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_27B")

    Return()

    # Function_0_1C4 end

    def Function_1_27C(): pass

    label("Function_1_27C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A6")
    OP_94(0xFE, 0xFFFFA7FE, 0x7F4E, 0xFFFFC3B0, 0x6AA4, 0x3E8)
    Sleep(300)
    Jump("Function_1_27C")

    label("loc_2A6")

    Return()

    # Function_1_27C end

    def Function_2_2A7(): pass

    label("Function_2_2A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2B5")
    Jump("loc_38E")

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2C3")
    Jump("loc_38E")

    label("loc_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2D1")
    Jump("loc_38E")

    label("loc_2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DF")
    Jump("loc_38E")

    label("loc_2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2ED")
    Jump("loc_38E")

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FB")
    Jump("loc_38E")

    label("loc_2FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30E")
    SetChrFlags(0xA, 0x80)
    Jump("loc_38E")

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31C")
    Jump("loc_38E")

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_343")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_38E")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36C")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -400, 50, 3770, 0)
    Jump("loc_38E")

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_38E")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E")
    SetChrFlags(0xC, 0x10)

    label("loc_38E")

    Return()

    # Function_2_2A7 end

    def Function_3_38F(): pass

    label("Function_3_38F")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -22700, 0, 54850, 10000, 2000, 45000)
    Return()

    # Function_3_38F end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a car magazine, "Orbal Car Freak Vol.1".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36E, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_461")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "You learned the\x01\x07\x02",
            ""Charm Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36E, 1)

    label("loc_461")

    TalkEnd(0xFF)
    Return()

    # Function_4_3AD end

    def Function_5_465(): pass

    label("Function_5_465")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_587")

    ChrTalk(
        0xFE,
        (
            "I consulted with the Town Mayor\x01",
            "and the mine reopening was decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To move forward as a town, the mine existence\x01",
            "is really indispensable to Mainz...\x01",
            "That's what I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Eh eh, I'll be digging after some time.\x01",
            "I'll put everything I've got!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5CC")

    label("loc_587")


    ChrTalk(
        0xFE,
        (
            "I'll be digging after some time.\x01",
            "I'll put everything I've got!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC")

    Jump("loc_104D")

    label("loc_5D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5DF")
    Jump("loc_104D")

    label("loc_5DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5ED")
    Jump("loc_104D")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_701")

    ChrTalk(
        0xFE,
        (
            "When Mainz was occupied\x01",
            "we tried to chase out the\x01",
            "jaegers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When we faced them we\x01",
            "were easily beaten and\x01",
            "I hurt my hips a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wasn't a serious injury, but I\x01",
            "got severely yelled at by Miranda\x01",
            "who said that I was too rash.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7AA")

    label("loc_701")


    ChrTalk(
        0xFE,
        (
            "I hurt my hips a little,\x01",
            "but I don't regret the fact\x01",
            "I faced them at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, I'm really\x01",
            "glad the the other miners\x01",
            "and the townsfolk didn't get hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AA")

    Jump("loc_104D")

    label("loc_7AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_935")

    ChrTalk(
        0xFE,
        (
            "With cave-in accidents and monsters\x01",
            "outbreaks in the mines, a miner's\x01",
            "job has his life on the line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To keep doing such a job the most\x01",
            "important things are trust in each\x01",
            "other and having pride in this job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately I feel that maybe I\x01",
            "got why good vibes keep\x01",
            "the miners together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the mine captain, I'm lucky to\x01",
            "be surrounded by such comrades.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9EB")

    label("loc_935")


    ChrTalk(
        0xFE,
        (
            "In a certain sense, the miner is a\x01",
            "job that puts your life on the line.\x01",
            "Trust in each other is important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the mine captain, I'm lucky to\x01",
            "be surrounded by such comrades.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EB")

    Jump("loc_104D")

    label("loc_9F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD1")

    ChrTalk(
        0xFE,
        (
            "That Marlow, today is\x01",
            "strangely full of energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until yesterday he had a face\x01",
            "like the world was going to end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as long as he's working properly,\x01",
            "I've got nothing to complain.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B99")

    label("loc_AD1")


    ChrTalk(
        0xFE,
        (
            "That Marlow, he changed abruptly compared to\x01",
            "yesterday and now he suddenly got motivated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhhm, I don't really get it, but...\x01",
            "As long as he's working properly,\x01",
            "I've got nothing to complain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B99")

    Jump("loc_104D")

    label("loc_B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5D")

    ChrTalk(
        0xFE,
        (
            "As of late, it seems\x01",
            "that Marlow can't focus\x01",
            "on the job at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He even turned down an invite to\x01",
            "go drink for a change of pace...\x01",
            "What's gotten into him?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CC6")

    label("loc_C5D")


    ChrTalk(
        0xFE,
        (
            "By the way, that Gantz's break...\x01",
            "It sure is awfully long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, they're\x01",
            "all slacking off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC6")

    Jump("loc_104D")

    label("loc_CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D58")

    ChrTalk(
        0xFE,
        (
            "I'm sure that today is\x01",
            "Sunday School day for Alec.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want him to study\x01",
            "a lot with Mr.\x01",
            "Backerei's Kimmy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DC0")

    label("loc_D58")


    ChrTalk(
        0xFE,
        (
            "When it comes down to us miners,\x01",
            "it's all uneducated guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish Alec and Kimmy\x01",
            "study a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC0")

    Jump("loc_104D")

    label("loc_DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DD3")
    Jump("loc_104D")

    label("loc_DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9B")

    ChrTalk(
        0xFE,
        "(*grooowl*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Aah, that's bad.\x01",
            "By the way, I forgot to bring\x01",
            "a lunchbox with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll work till a good point\x01",
            "to leave off and go get it myself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F1F")

    label("loc_E9B")


    ChrTalk(
        0xFE,
        (
            "I completely forgot to bring\x01",
            "a lunchbox with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll work till a good point\x01",
            "to leave off and go get it myself...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1F")

    Jump("loc_104D")

    label("loc_F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_104D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FEB")

    ChrTalk(
        0xFE,
        (
            "I'm concerned about the old mine, but...\x01",
            "Say what you want, a miner digs holes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll leave that one to Gantz and the Town Mayor.\x01",
            "We must focus on our work here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_104D")

    label("loc_FEB")


    ChrTalk(
        0xFE,
        (
            "Say what you want, a miner digs holes.\x01",
            "No matter what happens, we have to focus on our work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104D")

    TalkEnd(0xFE)
    Return()

    # Function_5_465 end

    def Function_6_1051(): pass

    label("Function_6_1051")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112A")

    ChrTalk(
        0xFE,
        (
            "It's an abnormal situation and hard time, but...\x01",
            "We must do the best we can to enliven Mainz.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha, if I do that, maybe the\x01",
            "day that Lycka pays attention\x01",
            "to me will come too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_118E")

    label("loc_112A")


    ChrTalk(
        0xFE,
        (
            "It's an abnormal situation and hard time, but...\x01",
            "We must do the best we can to enliven Mainz!\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118E")

    Jump("loc_1A9C")

    label("loc_1193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_11A1")
    Jump("loc_1A9C")

    label("loc_11A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_11AF")
    Jump("loc_1A9C")

    label("loc_11AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1342")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A4")

    ChrTalk(
        0xFE,
        (
            "Finally, digging at the Mainz\x01",
            "mine resumed since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a lot to think about\x01",
            "Crossbell future, but...\x01",
            "In any case, I'll just move my body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, what we miners\x01",
            "can do is only dig holes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_133D")

    label("loc_12A4")


    ChrTalk(
        0xFE,
        (
            "It seems that Lycka of the bar\x01",
            "was quite scared at the time\x01",
            "of the town occupation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can only dig\x01",
            "holes, but...\x01",
            "I wish she'll cheer up quick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133D")

    Jump("loc_1A9C")

    label("loc_1342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13CD")

    ChrTalk(
        0xFE,
        (
            "Thanks to Gantz,\x01",
            "I became able to\x01",
            "focus on work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As thanking, I guess\x01",
            "that tonight's drinking\x01",
            "money will be on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9C")

    label("loc_13CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_152C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A6")

    ChrTalk(
        0xFE,
        (
            "Gantz forcefully dragged\x01",
            "me to the bar yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, Lycka encouraged me,\x01",
            "who hasn't been feeling\x01",
            "great as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*haah*, it seems\x01",
            "she didn't hate me...\x01",
            "I'm really glad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1527")

    label("loc_14A6")


    ChrTalk(
        0xFE,
        (
            "Lycka encouraged me,\x01",
            "who hasn't been feeling\x01",
            "great as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*haah*, it seems\x01",
            "she didn't hate me...\x01",
            "I'm really glad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1527")

    Jump("loc_1A9C")

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1665")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EB")

    ChrTalk(
        0xFE,
        (
            "*haah*...\x01",
            "Somehow I've got no motivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lycka probably hates me,\x01",
            "so showing up at the bar\x01",
            "too is hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today I guess I'll\x01",
            "call it a day quick...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1660")

    label("loc_15EB")


    ChrTalk(
        0xFE,
        (
            "Lycka probably hates me,\x01",
            "so showing up at the bar\x01",
            "too is hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*haah*...I can't concentrate on work too.\x02",
    )

    CloseMessageWindow()

    label("loc_1660")

    Jump("loc_1A9C")

    label("loc_1665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1774")

    ChrTalk(
        0xFE,
        (
            "I wonder why I said such things\x01",
            "to Lycka at the party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She totally ignored me...\x01",
            "And for starters, the impression that I\x01",
            "said that due to the liquor was too lame...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah...I'd like to punch the me of\x01",
            "last night a hundred times...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17F6")

    label("loc_1774")


    ChrTalk(
        0xFE,
        (
            "Judging by that reaction,\x01",
            "I guess Lycka hates me now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah...I'd like to punch the me of\x01",
            "last night a hundred times...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F6")

    Jump("loc_1A9C")

    label("loc_17FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1809")
    Jump("loc_1A9C")

    label("loc_1809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C0")

    ChrTalk(
        0xFE,
        (
            "Hm, Gantz should've gone\x01",
            "to the Town Mayor's place now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*haah*, still, \x01",
            "how cute Lycka\x01",
            "was yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could do anything\x01",
            "for that smile.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_191D")

    label("loc_18C0")


    ChrTalk(
        0xFE,
        (
            "...Oh, that kid...\x01",
            "Isn't he the mine captain's?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What has he come\x01",
            "to do here alone?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191D")

    Jump("loc_1A9C")

    label("loc_1922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1A9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0A")

    ChrTalk(
        0xFE,
        (
            "Lately, Gantz is positive.\x01",
            "It's a great change since the time\x01",
            "he did nothing but complaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he was affected by the\x01",
            "fact that he made us worry when\x01",
            "he was caught in that Cult incident.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A9C")

    label("loc_1A0A")


    ChrTalk(
        0xFE,
        (
            "Although he's getting on\x01",
            "with liquor and gambling\x01",
            "is always the same...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm his childhood friend, \x01",
            "so I have tp at least tolerate that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9C")

    TalkEnd(0xFE)
    Return()

    # Function_6_1051 end

    def Function_7_1AA0(): pass

    label("Function_7_1AA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B71")

    ChrTalk(
        0xFE,
        (
            "I thought it wasn't bad\x01",
            "being able to go to the city\x01",
            "and sally forth to the casino, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, now I have\x01",
            "to do my best with work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alright, let's do this!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1BDA")

    label("loc_1B71")


    ChrTalk(
        0xFE,
        (
            "After I'm done with work, I'll have \x01",
            "fun at the casino as much I want!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alright, let's do this!\x02",
    )

    CloseMessageWindow()

    label("loc_1BDA")

    Jump("loc_209F")

    label("loc_1BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1BED")
    Jump("loc_209F")

    label("loc_1BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1BFB")
    Jump("loc_209F")

    label("loc_1BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D32")

    ChrTalk(
        0xFE,
        (
            "Somehow I remembered\x01",
            "the daughter of the jaegers'\x01",
            "leader who occupied Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems she was the little girl among\x01",
            "them who stocked up a great quantity\x01",
            "of Septium at Mainz before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think that such a little girl\x01",
            "made mincemeat of the CGF...\x01",
            "I can't believe it yet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DA5")

    label("loc_1D32")


    ChrTalk(
        0xFE,
        (
            "To think that such a little girl\x01",
            "made mincemeat of the CGF...\x01",
            "I can't believe it yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Truly a nightmare.\x02",
    )

    CloseMessageWindow()

    label("loc_1DA5")

    Jump("loc_209F")

    label("loc_1DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1EE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6D")

    ChrTalk(
        0xFE,
        (
            "This morning I dug up a\x01",
            "huge Sapphirl liiike this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh eh, somehow recently\x01",
            "I feel in top form for my job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If only this worked as\x01",
            "luck in gambling too...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1EDD")

    label("loc_1E6D")


    ChrTalk(
        0xFE,
        (
            "Eh eh, somehow recently\x01",
            "I feel in top form for my job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If only this worked as\x01",
            "luck in gambling too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDD")

    Jump("loc_209F")

    label("loc_1EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F4A")

    ChrTalk(
        0xFE,
        (
            "It seems that Marlow has\x01",
            "got back his vigor too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eh eh, what a troublesome guy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_209F")

    label("loc_1F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F58")
    Jump("loc_209F")

    label("loc_1F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_207A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF4")

    ChrTalk(
        0xFE,
        (
            "That Marlow, he's\x01",
            "been depressed after\x01",
            "yesterday's party ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Alright.\x01",
            "I'm his childhood friend\x01",
            "so I'll help him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2075")

    label("loc_1FF4")


    ChrTalk(
        0xFE,
        (
            "I caused a whole lot of worries to\x01",
            "Marlow at the time of the Cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm his childhood friend\x01",
            "so I'll help him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2075")

    Jump("loc_209F")

    label("loc_207A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2088")
    Jump("loc_209F")

    label("loc_2088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2096")
    Jump("loc_209F")

    label("loc_2096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_209F")

    label("loc_209F")

    TalkEnd(0xFE)
    Return()

    # Function_7_1AA0 end

    def Function_8_20A3(): pass

    label("Function_8_20A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_223C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219D")

    ChrTalk(
        0xFE,
        (
            "For having reopened, it has,\x01",
            "and it sure is a bother, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I thought, not working at the mine\x01",
            "made me feel really bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha, I guess that the fact that I'm a\x01",
            "miner is deeply etched into my body too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2237")

    label("loc_219D")


    ChrTalk(
        0xFE,
        (
            "As I thought, not working at the mine\x01",
            "made me feel really bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha, I guess that the fact that I'm a\x01",
            "miner is deeply etched into my body too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2237")

    Jump("loc_2B71")

    label("loc_223C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_224A")
    Jump("loc_2B71")

    label("loc_224A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2258")
    Jump("loc_2B71")

    label("loc_2258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2358")

    ChrTalk(
        0xFE,
        (
            "When I thought the occupation incident\x01",
            "is over, next come something like a city\x01",
            "occupation incident, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There must be something I can do\x01",
            "for Mainz and Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But someone like me,\x01",
            "what could ever do?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_23CF")

    label("loc_2358")


    ChrTalk(
        0xFE,
        (
            "There must be something I can do\x01",
            "for Mainz and Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But someone like me,\x01",
            "what could ever do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23CF")

    Jump("loc_2B71")

    label("loc_23D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_247B")

    ChrTalk(
        0xFE,
        (
            "When it rains, it gets cold\x01",
            "in the tunnels too and it's\x01",
            "very unpleasant. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if you move your\x01",
            "body you'll warm up...\x01",
            "What a bother, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B71")

    label("loc_247B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_261C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_258F")

    ChrTalk(
        0xFE,
        (
            "Recently, grandma \x01",
            "began to say to\x01",
            "bring home a wife...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's fine she's happy that\x01",
            "I don't skip on the job anymore,\x01",
            "but honestly, that's a bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not reliable like the\x01",
            "mine captain or senior Max...\x01",
            "I prefer taking it easy alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2617")

    label("loc_258F")


    ChrTalk(
        0xFE,
        (
            "To bring home a wife...\x01",
            "Grandma too says some bothersome things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I prefer taking it easy alone.\x01",
            "I'll leave that stuff to Ami.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2617")

    Jump("loc_2B71")

    label("loc_261C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_282A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279C")

    ChrTalk(
        0xFE,
        (
            "When I was taking a break outside some time ago,\x01",
            "the mine captain's son came to talk to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Is the miner's job fun?" he\x01",
            "asked me and so I properly\x01",
            "said to him that's a bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...By the way, I did the\x01",
            "same thing before and\x01",
            "made him depressed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*haah*, what a bad habit of mine.\x01",
            "I guess I should've said \x01",
            "something a little brighter...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2825")

    label("loc_279C")


    ChrTalk(
        0xFE,
        (
            "It seems that the mine\x01",
            "captain's son is aspiring\x01",
            "to become a miner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I should've said \x01",
            "something a little brighter...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2825")

    Jump("loc_2B71")

    label("loc_282A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2929")

    ChrTalk(
        0xFE,
        (
            "I rested one day and I\x01",
            "feel really sluggish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My slacking life was long.\x01",
            "Either my body doesn't keep up\x01",
            "with me or it's bothersome or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm properly working.\x01",
            "I won't go back to be the\x01",
            "lazybone I was before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_29AD")

    label("loc_2929")


    ChrTalk(
        0xFE,
        (
            "I rested one day and I\x01",
            "feel really sluggish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm properly working.\x01",
            "I won't go back to be the\x01",
            "lazybone I was before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29AD")

    Jump("loc_2B71")

    label("loc_29B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_29C0")
    Jump("loc_2B71")

    label("loc_29C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB7")

    ChrTalk(
        0xFE,
        (
            "Lately I started to understand the\x01",
            "deliciousness of beer after work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Frankly speaking, it's a bother, but I\x01",
            "started working a lot without slacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, grandma is happy too,\x01",
            "so I guess that's fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B63")

    label("loc_2AB7")


    ChrTalk(
        0xFE,
        (
            "Lately I started to understand the\x01",
            "deliciousness of beer after work...\x01",
            "I don't slack off too much anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, grandma is happy too,\x01",
            "so I guess that's fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B63")

    Jump("loc_2B71")

    label("loc_2B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2B71")

    label("loc_2B71")

    TalkEnd(0xFE)
    Return()

    # Function_8_20A3 end

    def Function_9_2B75(): pass

    label("Function_9_2B75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2CBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C55")

    ChrTalk(
        0xFE,
        (
            "Ha ha, it seems that everyone is in\x01",
            "high spirits at the mine in a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Uwoooh, now I'm full of energy too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did, dig and dig even more...\x01",
            "That exactly what we miners are!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2CB9")

    label("loc_2C55")


    ChrTalk(
        0xFE,
        (
            "I'm digging after a long time.\x01",
            "I'll do it enthusiastically!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uwoooh, I'm full of energyyy!\x02",
    )

    CloseMessageWindow()

    label("loc_2CB9")

    Jump("loc_345B")

    label("loc_2CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2CCC")
    Jump("loc_345B")

    label("loc_2CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2CDA")
    Jump("loc_345B")

    label("loc_2CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D95")

    ChrTalk(
        0xFE,
        (
            "To think the town was\x01",
            "occupied by such guys...\x01",
            "What a disgrace for us miners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dammit, next time those\x01",
            "damn jaegers come,\x01",
            "they won't get away with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2E28")

    label("loc_2D95")


    ChrTalk(
        0xFE,
        (
            "Not only they occupied Mainz,\x01",
            "they even made a mess of\x01",
            "Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time those damn jaegers come,\x01",
            "they won't get away with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E28")

    Jump("loc_345B")

    label("loc_2E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2EDE")

    ChrTalk(
        0xFE,
        (
            "It seems we have already advanced\x01",
            "digging up to the intended stratum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh eh, a mountain of Septium is in front of us.\x01",
            "I'll do my best and dig even more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_345B")

    label("loc_2EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F51")

    ChrTalk(
        0xFE,
        (
            "Alright, today too I\x01",
            "must mine steadily!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh eh, might as well reach\x01",
            "tomorrow's quota too!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_345B")

    label("loc_2F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3114")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309A")

    ChrTalk(
        0xFE,
        (
            "Because lately unknown\x01",
            "large type monsters appear,\x01",
            "my wife is greatly worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're used to the monsters that\x01",
            "comes out in the mine so I think\x01",
            "there's nothing to be so worried about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Although I, a lot of time ago,\x01",
            "was attacked by a military dog\x01",
            "and injured, so I shouldn't brag...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_310F")

    label("loc_309A")


    ChrTalk(
        0xFE,
        (
            "Well, I'll just pay attention\x01",
            "to unknown monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to make my wife sad\x01",
            "even in the slightest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310F")

    Jump("loc_345B")

    label("loc_3114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324B")

    ChrTalk(
        0xFE,
        (
            "Yesterday, me and the\x01",
            "mine captain drank\x01",
            "the day away and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At night, Gantz and Marlow coming\x01",
            "back from the casino also joined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it was a rare chance,\x01",
            "we called Logy too and it\x01",
            "became a big party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, the liquor drank\x01",
            "with comrades is the best one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_32C7")

    label("loc_324B")


    ChrTalk(
        0xFE,
        (
            "Yesterday there was a big\x01",
            "party with all the miners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, the liquor drank\x01",
            "with comrades is the best one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C7")

    Jump("loc_345B")

    label("loc_32CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32DA")
    Jump("loc_345B")

    label("loc_32DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3383")

    ChrTalk(
        0xFE,
        (
            "That Logy, it's good he got motivated, \x01",
            "but his abilities on the job have still\x01",
            "a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the senior here,\x01",
            "I must strictly teach him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_345B")

    label("loc_3383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_345B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3416")

    ChrTalk(
        0xFE,
        (
            "For my wife,\x01",
            "heave-ho!♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For Mainz,\x01",
            "heave-ho!♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Eh eh, I must do my best\x01",
            "and mine today too.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 4)
    Jump("loc_345B")

    label("loc_3416")


    ChrTalk(
        0xFE,
        (
            "I must do my best and mine today too\x01",
            "for my wife and this town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_345B")

    TalkEnd(0xFE)
    Return()

    # Function_9_2B75 end

    def Function_10_345F(): pass

    label("Function_10_345F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3470")
    Jump("loc_35F9")

    label("loc_3470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_347E")
    Jump("loc_35F9")

    label("loc_347E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_348C")
    Jump("loc_35F9")

    label("loc_348C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_349A")
    Jump("loc_35F9")

    label("loc_349A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34A8")
    Jump("loc_35F9")

    label("loc_34A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34B6")
    Jump("loc_35F9")

    label("loc_34B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357B")

    ChrTalk(
        0xFE,
        (
            "Wow, so that's how\x01",
            "it is inside the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dark, spacious...\x01",
            "It seems that ghosts could pop out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, I wonder where father is.\x01",
            "Let's search for him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_35EB")

    label("loc_357B")


    ChrTalk(
        0xFE,
        (
            "I wanted to see once\x01",
            "where father works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, I wonder where could he be?\x01",
            "Let's search for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EB")

    Jump("loc_35F9")

    label("loc_35F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_35F9")

    label("loc_35F9")

    TalkEnd(0xFE)
    Return()

    # Function_10_345F end

    def Function_11_35FD(): pass

    label("Function_11_35FD")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is closed with sturdy chains.\x01",
            "It seems it is an abandoned mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_11_35FD end

    SaveToFile()

Try(main)
