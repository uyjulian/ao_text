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
        "Function_5_45D",          # 05, 5
        "Function_6_107F",         # 06, 6
        "Function_7_1AAC",         # 07, 7
        "Function_8_20BD",         # 08, 8
        "Function_9_2B5B",         # 09, 9
        "Function_10_346E",        # 0A, 10
        "Function_11_3614",        # 0B, 11
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
            "It's a car magazine,\x01",
            ""Orbal Car Freak Vol.1".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36E, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_459")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Learned the \x07\x02",
            ""Charm\x01",
            "Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36E, 1)

    label("loc_459")

    TalkEnd(0xFF)
    Return()

    # Function_4_3AD end

    def Function_5_45D(): pass

    label("Function_5_45D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_589")

    ChrTalk(
        0xFE,
        (
            "I consulted with the\x01",
            "Mayor and we decided to\x01",
            "reopen the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To move forward as a town, the existence\x01",
            "of the mine is really indispensable to\x01",
            "Mainz... That's what I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hehe. It's been a while\x01",
            "since I dug holes. I'll give\x01",
            "this everything I've got!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5D8")

    label("loc_589")


    ChrTalk(
        0xFE,
        (
            "It's been a while since I\x01",
            "dug holes. I'll give this\x01",
            "everything I've got!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D8")

    Jump("loc_107B")

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5EB")
    Jump("loc_107B")

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5F9")
    Jump("loc_107B")

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70F")

    ChrTalk(
        0xFE,
        (
            "When Mainz was occupied,\x01",
            "we tried to drive out\x01",
            "the jaegers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When we faced them, we\x01",
            "were easily beaten and I\x01",
            "hurt my hip a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wasn't a serious injury, but I\x01",
            "got severely reprimanded by Miranda,\x01",
            "who said I'd been too rash.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7B3")

    label("loc_70F")


    ChrTalk(
        0xFE,
        (
            "I hurt my hip a little, but\x01",
            "I don't regret the fact\x01",
            "that I faced them at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, I'm really glad\x01",
            "the the other miners and\x01",
            "townsfolk didn't get hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B3")

    Jump("loc_107B")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_945")

    ChrTalk(
        0xFE,
        (
            "With cave-in accidents and\x01",
            "monster outbreaks in the mines,\x01",
            "a miner's life is on the line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To continue to be a miner, the most\x01",
            "important things are to trust in each\x01",
            "other and having pride in the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately, I feel like I'm\x01",
            "beginning to understand why good\x01",
            "vibes keep miners together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the mine captain, I'm\x01",
            "lucky to be surrounded\x01",
            "by such comrades.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9ED")

    label("loc_945")


    ChrTalk(
        0xFE,
        (
            "In a certain sense, a miner's\x01",
            "life on the line every day. Trust\x01",
            "in each other is important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the mine captain, I'm\x01",
            "lucky to be surrounded\x01",
            "by such comrades.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9ED")

    Jump("loc_107B")

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE3")

    ChrTalk(
        0xFE,
        (
            "That Marlowe, he's\x01",
            "strangely full of energy\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until yesterday he looked\x01",
            "like he thought the world\x01",
            "was going to end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as long as he's\x01",
            "working properly, I've got\x01",
            "nothing to complain about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BB1")

    label("loc_AE3")


    ChrTalk(
        0xFE,
        (
            "That Marlowe, he changed abruptly\x01",
            "compared to yesterday and now he\x01",
            "suddenly got motivated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I don't really get it, but...\x01",
            "As long as he's working properly,\x01",
            "I've got nothing to complain about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB1")

    Jump("loc_107B")

    label("loc_BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C75")

    ChrTalk(
        0xFE,
        (
            "As of late, it seems\x01",
            "Marlowe can't focus on\x01",
            "the job at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He even turned down an invitation\x01",
            "to go drink for a change of\x01",
            "pace... What's gotten into him?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CED")

    label("loc_C75")


    ChrTalk(
        0xFE,
        (
            "By the way, that Gantz's\x01",
            "break... It sure is taking\x01",
            "an awfully long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, they're all\x01",
            "slacking off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CED")

    Jump("loc_107B")

    label("loc_CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D79")

    ChrTalk(
        0xFE,
        (
            "Today was Sunday School\x01",
            "day for Alec, wasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want him to study a\x01",
            "lot with Backerei's\x01",
            "Kimmy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DDD")

    label("loc_D79")


    ChrTalk(
        0xFE,
        (
            "When it comes to us\x01",
            "miners, we're all\x01",
            "uneducated guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope Alec and Kimmy\x01",
            "study a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDD")

    Jump("loc_107B")

    label("loc_DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DF0")
    Jump("loc_107B")

    label("loc_DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC3")

    ChrTalk(
        0xFE,
        "(*grooowl*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Aah, that isn't good.\x01",
            "By the way, I forgot to\x01",
            "bring my lunchbox with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll work 'til a\x01",
            "good stopping point to leave\x01",
            "and go get it myself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F4D")

    label("loc_EC3")


    ChrTalk(
        0xFE,
        (
            "I completely forgot to\x01",
            "bring my lunchbox with\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll work 'til a\x01",
            "good stopping point to leave\x01",
            "and go get it myself...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4D")

    Jump("loc_107B")

    label("loc_F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_107B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1019")

    ChrTalk(
        0xFE,
        (
            "I'm concerned about the old\x01",
            "mine, but... Say what you\x01",
            "want, a miner digs holes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll leave that one to Gantz\x01",
            "and the Mayor. We've got to\x01",
            "focus on our work here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_107B")

    label("loc_1019")


    ChrTalk(
        0xFE,
        (
            "Say what you want, a miner digs\x01",
            "holes. No matter what happens,\x01",
            "we have to focus on our work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107B")

    TalkEnd(0xFE)
    Return()

    # Function_5_45D end

    def Function_6_107F(): pass

    label("Function_6_107F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1159")

    ChrTalk(
        0xFE,
        (
            "It's an abnormal situation and\x01",
            "difficult time, but... We have to do\x01",
            "the best we can to enliven Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. If I do that, maybe\x01",
            "the day Lycka pays attention\x01",
            "to me will come too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11BC")

    label("loc_1159")


    ChrTalk(
        0xFE,
        (
            "It's an abnormal situation and\x01",
            "hard time, but... We must do the\x01",
            "best we can to enliven Mainz!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11BC")

    Jump("loc_1AA8")

    label("loc_11C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_11CF")
    Jump("loc_1AA8")

    label("loc_11CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_11DD")
    Jump("loc_1AA8")

    label("loc_11DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1354")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CB")

    ChrTalk(
        0xFE,
        (
            "Digging in the Mainz\x01",
            "mine finally resumed\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a lot to think about for\x01",
            "Crossbell's future, but... In any\x01",
            "case, I'll just move my body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, all we miners\x01",
            "can do is dig holes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_134F")

    label("loc_12CB")


    ChrTalk(
        0xFE,
        (
            "Lycka at the bar was\x01",
            "quite scared during the\x01",
            "occupation as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can only dig holes,\x01",
            "but... I hope she cheers\x01",
            "up quick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134F")

    Jump("loc_1AA8")

    label("loc_1354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13D8")

    ChrTalk(
        0xFE,
        (
            "Thanks to Gantz, I\x01",
            "became able to focus on\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As thanks, I guess\x01",
            "tonight's drinking money\x01",
            "will be on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA8")

    label("loc_13D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1535")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B0")

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
            "Then, Lycka encouraged\x01",
            "me. I haven't been\x01",
            "feeling great as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, it seems she\x01",
            "didn't hate me... I'm\x01",
            "really glad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1530")

    label("loc_14B0")


    ChrTalk(
        0xFE,
        (
            "Lycka encouraged me. I\x01",
            "haven't been feeling\x01",
            "great as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, it seems she\x01",
            "didn't hate me... I'm\x01",
            "really glad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1530")

    Jump("loc_1AA8")

    label("loc_1535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1679")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FC")

    ChrTalk(
        0xFE,
        (
            "*sigh*... I've got no\x01",
            "motivation for some\x01",
            "reason.\x02",
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
            "I guess I'll call it a\x01",
            "day early today...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1674")

    label("loc_15FC")


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
            "*sigh*...I can't\x01",
            "concentrate on work\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1674")

    Jump("loc_1AA8")

    label("loc_1679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1780")

    ChrTalk(
        0xFE,
        (
            "I wonder why I said such\x01",
            "things to Lycka at the\x01",
            "party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She totally ignored me... And what\x01",
            "I said under the influence was way\x01",
            "too lame in the first place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah... I'd like to punch\x01",
            "the me of last night a\x01",
            "hundred times...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1803")

    label("loc_1780")


    ChrTalk(
        0xFE,
        (
            "Judging by that\x01",
            "reaction, I guess Lycka\x01",
            "hates me now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah... I'd like to punch\x01",
            "the me of last night a\x01",
            "hundred times...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1803")

    Jump("loc_1AA8")

    label("loc_1808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1816")
    Jump("loc_1AA8")

    label("loc_1816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1941")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D5")

    ChrTalk(
        0xFE,
        (
            "Hmm. If you're looking\x01",
            "for Gantz, he should be\x01",
            "at the Mayor's place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*, still, how\x01",
            "cute Lycka was\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd do anything for that\x01",
            "smile.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_193C")

    label("loc_18D5")


    ChrTalk(
        0xFE,
        (
            "...Oh, that kid... Isn't\x01",
            "he the mine captain's?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is he doing alone\x01",
            "in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_193C")

    Jump("loc_1AA8")

    label("loc_1941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1AA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A24")

    ChrTalk(
        0xFE,
        (
            "Lately, Gantz is positive.\x01",
            "It's a great change from when\x01",
            "he did nothing but complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he was affected by the fact\x01",
            "that he made us worry when he was\x01",
            "caught up in that cult incident.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AA8")

    label("loc_1A24")


    ChrTalk(
        0xFE,
        (
            "Although his love of\x01",
            "liquor and gambling\x01",
            "hasn't changed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm his childhood\x01",
            "friend, so I have to at\x01",
            "least tolerate that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA8")

    TalkEnd(0xFE)
    Return()

    # Function_6_107F end

    def Function_7_1AAC(): pass

    label("Function_7_1AAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B70")

    ChrTalk(
        0xFE,
        (
            "I thought it wasn't bad to\x01",
            "be able to go to the city\x01",
            "and hit the casino, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I now need to do my best\x01",
            "with work, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alright, let's do this!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1BD8")

    label("loc_1B70")


    ChrTalk(
        0xFE,
        (
            "After I'm done with work,\x01",
            "I'll have all the fun at\x01",
            "the casino I want!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alright, let's do this!\x02",
    )

    CloseMessageWindow()

    label("loc_1BD8")

    Jump("loc_20B9")

    label("loc_1BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1BEB")
    Jump("loc_20B9")

    label("loc_1BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1BF9")
    Jump("loc_20B9")

    label("loc_1BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2C")

    ChrTalk(
        0xFE,
        (
            "I remember the daughter of the\x01",
            "jaeger leader who occupied\x01",
            "Mainz for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She was the little girl among them\x01",
            "who stocked up a great quantity of\x01",
            "septium at Mainz before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think such a little girl\x01",
            "made mincemeat of the CGF...\x01",
            "I don't believe it, even now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DA0")

    label("loc_1D2C")


    ChrTalk(
        0xFE,
        (
            "To think such a little girl\x01",
            "made mincemeat of the CGF...\x01",
            "I don't believe it, even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Truly a nightmare.\x02",
    )

    CloseMessageWindow()

    label("loc_1DA0")

    Jump("loc_20B9")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7F")

    ChrTalk(
        0xFE,
        (
            "This morning I dug up a\x01",
            "huge Sapphirl liiike\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I've been feeling\x01",
            "like my work is in top form\x01",
            "recently for some reason.\x02",
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
    Jump("loc_1F06")

    label("loc_1E7F")


    ChrTalk(
        0xFE,
        (
            "Hehe, I've been feeling\x01",
            "like my work is in top form\x01",
            "recently for some reason.\x02",
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

    label("loc_1F06")

    Jump("loc_20B9")

    label("loc_1F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F6E")

    ChrTalk(
        0xFE,
        (
            "Marlowe seems to have\x01",
            "gotten back his vigor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, what a troublesome\x01",
            "guy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B9")

    label("loc_1F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F7C")
    Jump("loc_20B9")

    label("loc_1F7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2094")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201E")

    ChrTalk(
        0xFE,
        (
            "That Marlowe, he's been\x01",
            "depressed ever since\x01",
            "yesterday's party ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Alright. I'm his\x01",
            "childhood friend so I'll\x01",
            "help him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_208F")

    label("loc_201E")


    ChrTalk(
        0xFE,
        (
            "I made Marlowe worry an\x01",
            "awful lot during the\x01",
            "cult incident.\x02",
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

    label("loc_208F")

    Jump("loc_20B9")

    label("loc_2094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_20A2")
    Jump("loc_20B9")

    label("loc_20A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_20B0")
    Jump("loc_20B9")

    label("loc_20B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_20B9")

    label("loc_20B9")

    TalkEnd(0xFE)
    Return()

    # Function_7_1AAC end

    def Function_8_20BD(): pass

    label("Function_8_20BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2218")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A1")

    ChrTalk(
        0xFE,
        (
            "For having reopened, it has,\x01",
            "and the bothersome things\x01",
            "haven't changed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I thought, not\x01",
            "working at the mine made\x01",
            "me feel really bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I I'm a miner\x01",
            "through and through.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2213")

    label("loc_21A1")


    ChrTalk(
        0xFE,
        (
            "As I thought, not\x01",
            "working at the mine made\x01",
            "me feel really bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I I'm a miner\x01",
            "through and through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2213")

    Jump("loc_2B57")

    label("loc_2218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2226")
    Jump("loc_2B57")

    label("loc_2226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2234")
    Jump("loc_2B57")

    label("loc_2234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2328")

    ChrTalk(
        0xFE,
        (
            "Just when I thought the occupation\x01",
            "was over, then came something like\x01",
            "a city occupation, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There must be something\x01",
            "I can do for Mainz and\x01",
            "Crossbell City...\x02",
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
    Jump("loc_239F")

    label("loc_2328")


    ChrTalk(
        0xFE,
        (
            "There must be something\x01",
            "I can do for Mainz and\x01",
            "Crossbell City...\x02",
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

    label("loc_239F")

    Jump("loc_2B57")

    label("loc_23A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_244A")

    ChrTalk(
        0xFE,
        (
            "When it rains, it gets\x01",
            "cold in the tunnels too\x01",
            "and it's very unpleasant.\x02",
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
    Jump("loc_2B57")

    label("loc_244A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2562")

    ChrTalk(
        0xFE,
        (
            "Recently, grandma has\x01",
            "begun telling me to\x01",
            "bring home a wife...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's fine she's happy that I don't\x01",
            "skip out on the job anymore, but\x01",
            "honestly, that's a bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not reliable like the\x01",
            "mine captain or Max... I\x01",
            "prefer taking it easy alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_25E9")

    label("loc_2562")


    ChrTalk(
        0xFE,
        (
            "To bring home a wife...\x01",
            "Grandma can say some\x01",
            "bothersome things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I prefer taking it easy\x01",
            "alone. I'll leave that\x01",
            "stuff to Ami.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E9")

    Jump("loc_2B57")

    label("loc_25EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2766")

    ChrTalk(
        0xFE,
        (
            "When I was taking a break outside\x01",
            "some time ago, the mine captain's\x01",
            "son came to talk to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Is mining fun?" he asked\x01",
            "me. And so, I properly\x01",
            "told him it's a bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...By the way, I did the\x01",
            "same thing before and it\x01",
            "made him depressed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, that's a bad habit of\x01",
            "mine. I guess I should've said\x01",
            "something a little brighter...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_27F1")

    label("loc_2766")


    ChrTalk(
        0xFE,
        (
            "It seems the mine captain's\x01",
            "son is aspiring to become a\x01",
            "miner himself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I should've said\x01",
            "something a little\x01",
            "brighter...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F1")

    Jump("loc_2B57")

    label("loc_27F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_298E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2902")

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
            "My slacking life lasted a long\x01",
            "time. Either my body doesn't keep\x01",
            "up with me or it's bothersome or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm properly working.\x01",
            "I won't go back to being\x01",
            "the lazybone I was before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2989")

    label("loc_2902")


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
            "I won't go back to being\x01",
            "the lazybone I was before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2989")

    Jump("loc_2B57")

    label("loc_298E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_299C")
    Jump("loc_2B57")

    label("loc_299C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A98")

    ChrTalk(
        0xFE,
        (
            "Lately, I'm beginning to\x01",
            "understand the deliciousness\x01",
            "of beer after work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Frankly speaking, it's a\x01",
            "bother, but I started working\x01",
            "a lot without slacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, grandma is\x01",
            "happy too, so I guess\x01",
            "that's good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B49")

    label("loc_2A98")


    ChrTalk(
        0xFE,
        (
            "Lately, I'm beginning to understand the\x01",
            "deliciousness of beer after work... I\x01",
            "don't slack off too much anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, grandma is\x01",
            "happy too, so I guess\x01",
            "that's good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B49")

    Jump("loc_2B57")

    label("loc_2B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2B57")

    label("loc_2B57")

    TalkEnd(0xFE)
    Return()

    # Function_8_20BD end

    def Function_9_2B5B(): pass

    label("Function_9_2B5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3A")

    ChrTalk(
        0xFE,
        (
            "Haha, it's been a while\x01",
            "since everyone was in such\x01",
            "high spirits at the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Uwoooh, now I'm full\x01",
            "of energy too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did, dig and dig even\x01",
            "more... That exactly\x01",
            "what we miners do!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2C90")

    label("loc_2C3A")


    ChrTalk(
        0xFE,
        (
            "It's been a while since\x01",
            "I dug. Let's do this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uwoooh, I'm full of\x01",
            "energyyy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C90")

    Jump("loc_346A")

    label("loc_2C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2CA3")
    Jump("loc_346A")

    label("loc_2CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2CB1")
    Jump("loc_346A")

    label("loc_2CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D6A")

    ChrTalk(
        0xFE,
        (
            "To think the town was\x01",
            "occupied by such guys... What\x01",
            "a disgrace for us miners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn. Next time those\x01",
            "damn jaegers come, they\x01",
            "won't get away with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2DFF")

    label("loc_2D6A")


    ChrTalk(
        0xFE,
        (
            "Not only did they occupy\x01",
            "Mainz, they even made a\x01",
            "mess of Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time those damn\x01",
            "jaegers come, they won't\x01",
            "get away with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFF")

    Jump("loc_346A")

    label("loc_2E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2EBC")

    ChrTalk(
        0xFE,
        (
            "It seems we've already\x01",
            "advanced our digging up\x01",
            "to the intended stratum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. A mountain of septium\x01",
            "is right in front of us. I'll\x01",
            "do my best and dig even more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346A")

    label("loc_2EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F35")

    ChrTalk(
        0xFE,
        (
            "Alright, I've got to\x01",
            "mine steadily again\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, might as well\x01",
            "reach tomorrow's quota\x01",
            "too!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346A")

    label("loc_2F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309D")

    ChrTalk(
        0xFE,
        (
            "My wife is greatly worried because\x01",
            "of the unknown large monsters that\x01",
            "have been appearing lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're used to the monsters that come\x01",
            "out in the mines so I don't think it's\x01",
            "anything to be so worried about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Although I was attacked by a\x01",
            "military dog a long time ago and got\x01",
            "injured, so I guess I shouldn't brag...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3112")

    label("loc_309D")


    ChrTalk(
        0xFE,
        (
            "Well, I'll just pay\x01",
            "attention to unknown\x01",
            "monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to make my\x01",
            "wife sad even in the\x01",
            "slightest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3112")

    Jump("loc_346A")

    label("loc_3117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3244")

    ChrTalk(
        0xFE,
        (
            "Yesterday, me and the\x01",
            "mine captain drank the\x01",
            "day away and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At night, Gantz and\x01",
            "Marlowe, back from the\x01",
            "casino, also joined us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it was a rare\x01",
            "chance, we called Logy too\x01",
            "and it became a big party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, liquor\x01",
            "drunk with friends is\x01",
            "the best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_32B7")

    label("loc_3244")


    ChrTalk(
        0xFE,
        (
            "Yesterday there was a\x01",
            "big party with all the\x01",
            "miners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, liquor\x01",
            "drunk with friends is\x01",
            "the best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B7")

    Jump("loc_346A")

    label("loc_32BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32CA")
    Jump("loc_346A")

    label("loc_32CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3379")

    ChrTalk(
        0xFE,
        (
            "That Logy. It's great that he got\x01",
            "some motivation, but his abilities on\x01",
            "the job have still a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As his senior, I must\x01",
            "strictly teach him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346A")

    label("loc_3379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_346A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3417")

    ChrTalk(
        0xFE,
        "For my wife, heave-ho!♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "For Mainz, heave-ho!♪\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Hehe. I've got to do my\x01",
            "best with today's mining\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 4)
    Jump("loc_346A")

    label("loc_3417")


    ChrTalk(
        0xFE,
        (
            "I've got to do my best with\x01",
            "the mining again today for\x01",
            "my wife and this town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_346A")

    TalkEnd(0xFE)
    Return()

    # Function_9_2B5B end

    def Function_10_346E(): pass

    label("Function_10_346E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_347F")
    Jump("loc_3610")

    label("loc_347F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_348D")
    Jump("loc_3610")

    label("loc_348D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_349B")
    Jump("loc_3610")

    label("loc_349B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34A9")
    Jump("loc_3610")

    label("loc_34A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34B7")
    Jump("loc_3610")

    label("loc_34B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34C5")
    Jump("loc_3610")

    label("loc_34C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358E")

    ChrTalk(
        0xFE,
        (
            "Wow, so that's how it is\x01",
            "inside the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dark, spacious... It\x01",
            "seems that ghosts could\x01",
            "pop out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, I wonder\x01",
            "where father is. I'll\x01",
            "try looking for him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3602")

    label("loc_358E")


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
            "Well then, I wonder\x01",
            "where could he be? I'll\x01",
            "try looking for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3602")

    Jump("loc_3610")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3610")

    label("loc_3610")

    TalkEnd(0xFE)
    Return()

    # Function_10_346E end

    def Function_11_3614(): pass

    label("Function_11_3614")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is locked with\x01",
            "sturdy chains. It seems\x01",
            "to be an abandoned mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_11_3614 end

    SaveToFile()

Try(main)
