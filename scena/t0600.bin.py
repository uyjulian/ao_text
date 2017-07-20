from ScenarioHelper import *

def main():
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
        "Mining head Hoffman",         # 1
        "Miners Mallo",             # 2
        "Miner Gantz",             # 3
        "Miner rosie",           # 4
        "Miner Max",           # 5
        "Alec",                 # 6
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
        "Function_5_457",          # 05, 5
        "Function_6_E65",          # 06, 6
        "Function_7_181B",         # 07, 7
        "Function_8_1DCD",         # 08, 8
        "Function_9_2792",         # 09, 9
        "Function_10_2FA3",        # 0A, 10
        "Function_11_3134",        # 0B, 11
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
            "There is a car magazine \"Drifting Car Freak vol. 1\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('魅力色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_453")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Paint pattern\x01\x07\x02",
            "\"Charm color\"\x07\x00",
            "I learned.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('魅力色彩', 1)

    label("loc_453")

    TalkEnd(0xFF)
    Return()

    # Function_4_3AD end

    def Function_5_457(): pass

    label("Function_5_457")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_537")

    ChrTalk(
        0xFE,
        (
            "Consult with the Mayor,\x01",
            "I decided to resume the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For Mainz to move forward,\x01",
            "After all the existence of mine is indispensable ……\x01",
            "I thought so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… To, I dig the hole for the first time in a while.\x01",
            "Put your energy on! It is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_564")

    label("loc_537")


    ChrTalk(
        0xFE,
        (
            "It digs a hole after a long time,\x01",
            "Put your energy on! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_564")

    Jump("loc_E61")

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_577")
    Jump("loc_E61")

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_585")
    Jump("loc_E61")

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_729")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_690")

    ChrTalk(
        0xFE,
        (
            "When Mainz was occupied,\x01",
            "We and our hunters guys\x01",
            "I tried to drive out … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you stand up\x01",
            "It was easily blown away,\x01",
            "I got hurt a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it was not a big injury,\x01",
            "It's too messy to Miranda\x01",
            "I got very angry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_724")

    label("loc_690")


    ChrTalk(
        0xFE,
        (
            "I suffered a bit of my back pain,\x01",
            "Having confrontation itself\x01",
            "Do not regret anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, other miners and\x01",
            "The town's people did not get hurt.\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_724")

    Jump("loc_E61")

    label("loc_729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_90D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87D")

    ChrTalk(
        0xFE,
        (
            "Accidents like fallen fallen\x01",
            "In the mine where demons are generated,\x01",
            "The work of the miners is a life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keep doing such work,\x01",
            "Mutual trust and pride for this work\x01",
            "I am getting most important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, the miners feel good\x01",
            "It is gathered that the neighborhood is\x01",
            "I guess that it is understandable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To, surrounded by such a group,\x01",
            "It is said that the mine president is exhausted.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_908")

    label("loc_87D")


    ChrTalk(
        0xFE,
        (
            "A miner is a meaning\x01",
            "It's a life-saving job.\x01",
            "Mutual trust is important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To, surrounded by such a group,\x01",
            "It is said that the mine president is exhausted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_908")

    Jump("loc_E61")

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C7")

    ChrTalk(
        0xFE,
        (
            "The guy of Malo,\x01",
            "I'm strangely cheerful today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the end of the world until yesterday\x01",
            "I faced with a face ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as long as I work\x01",
            "There is nothing wrong with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A52")

    label("loc_9C7")


    ChrTalk(
        0xFE,
        (
            "The guy of Malo, until yesterday\x01",
            "I'm sticking and suddenly motivated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I do not know well ….\x01",
            "As long as I work properly\x01",
            "Do not complain anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A52")

    Jump("loc_E61")

    label("loc_A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFA")

    ChrTalk(
        0xFE,
        (
            "Recently, Maruro's guy\x01",
            "I can not concentrate on my job.\x01",
            "It seems like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you invite me to drink for a change\x01",
            "I refuse ……\x01",
            "What on earth are you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B5E")

    label("loc_AFA")


    ChrTalk(
        0xFE,
        (
            "By the way,\x01",
            "It's a long break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, always this guy as well\x01",
            "Taru gonna do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5E")

    Jump("loc_E61")

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF7")

    ChrTalk(
        0xFE,
        (
            "Sure, today is Alec\x01",
            "I wish it was Sunday school day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Beckhai and this\x01",
            "With Kimi,\x01",
            "I want you to study hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C59")

    label("loc_BF7")


    ChrTalk(
        0xFE,
        (
            "When we come with our miners\x01",
            "Because there is no learning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To Alec\x01",
            "I want you to study hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C59")

    Jump("loc_E61")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C6C")
    Jump("loc_E61")

    label("loc_C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1A")

    ChrTalk(
        0xFE,
        "(Gwow ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Oh, okay.\x01",
            "So bring a lunch box\x01",
            "I was forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Up to the good point of Kiri\x01",
            "Would you like to go get it when you work?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D82")

    label("loc_D1A")


    ChrTalk(
        0xFE,
        (
            "I will bring a lunch box\x01",
            "I was carelessly forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Up to the good point of Kiri\x01",
            "Would you like to go get it when you work?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D82")

    Jump("loc_E61")

    label("loc_D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E20")

    ChrTalk(
        0xFE,
        (
            "I am worried about the former mine … …\x01",
            "The miners dig holes and it is a festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's leave it to Ganz and the Mayor,\x01",
            "We do not concentrate on work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E61")

    label("loc_E20")


    ChrTalk(
        0xFE,
        (
            "The miners dig holes and it is a festival.\x01",
            "No matter what I do not concentrate on my work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E61")

    TalkEnd(0xFE)
    Return()

    # Function_5_457 end

    def Function_6_E65(): pass

    label("Function_6_E65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27")

    ChrTalk(
        0xFE,
        (
            "It's a tough time due to abnormal situations ….\x01",
            "We tried hard to the utmost,\x01",
            "I have to raise Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, someday\x01",
            "Lucca turns around\x01",
            "Maybe the day will come.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F81")

    label("loc_F27")


    ChrTalk(
        0xFE,
        (
            "It's a tough time due to abnormal situations ….\x01",
            "We tried hard to the utmost,\x01",
            "I have to raise Mainz.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F81")

    Jump("loc_1817")

    label("loc_F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_F94")
    Jump("loc_1817")

    label("loc_F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_FA2")
    Jump("loc_1817")

    label("loc_FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_111C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1083")

    ChrTalk(
        0xFE,
        (
            "Finally yesterday, the Mainz mine also\x01",
            "I resumed digging holes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About future of Crossbell\x01",
            "I think about various things … ….\x01",
            "Just move your body anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are miners only digging holes\x01",
            "You can not do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1117")

    label("loc_1083")


    ChrTalk(
        0xFE,
        (
            "Lucca, a bar,\x01",
            "When the town is occupied\x01",
            "It seems that she was scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I only dig holes\x01",
            "I can not do it ….\x01",
            "I want you to get well soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1117")

    Jump("loc_1817")

    label("loc_111C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11A4")

    ChrTalk(
        0xFE,
        (
            "Thanks to Ganz\x01",
            "To be able to concentrate on work\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Instead of thanking you,\x01",
            "About tonight's drinking age\x01",
            "I guess I'll treat you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_11A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1311")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1288")

    ChrTalk(
        0xFE,
        (
            "Yes, GANTS forcibly put me\x01",
            "Pull me to the bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, Lucca\x01",
            "Recently I'm not energetic\x01",
            "It encouraged me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, apparently disliked\x01",
            "It looks like it was not …\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_130C")

    label("loc_1288")


    ChrTalk(
        0xFE,
        (
            "Lucca-chan\x01",
            "Recently I'm not energetic\x01",
            "It encouraged me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, apparently disliked\x01",
            "It looks like it was not …\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130C")

    Jump("loc_1817")

    label("loc_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1457")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DE")

    ChrTalk(
        0xFE,
        (
            "Ha\x01",
            "I do not get motivated for anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To Lucca-chan\x01",
            "Because I will be disliked\x01",
            "I also have difficulty putting a face on the bar … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will be back quickly today.\x01",
            "I wonder whether to raise up …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1452")

    label("loc_13DE")


    ChrTalk(
        0xFE,
        (
            "To Lucca-chan\x01",
            "Because I will be disliked\x01",
            "I also have difficulty putting a face on the bar … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha … … I can not get into work either.\x02",
    )

    CloseMessageWindow()

    label("loc_1452")

    Jump("loc_1817")

    label("loc_1457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1548")

    ChrTalk(
        0xFE,
        (
            "Why at the party, Lucca\x01",
            "I guess I said such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gun was ignored,\x01",
            "In the first place I leave it to drink and feel like I said\x01",
            "Too much parenthesis is bad … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh … … I last night\x01",
            "I want to hit around 100 shots ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15B6")

    label("loc_1548")


    ChrTalk(
        0xFE,
        (
            "In that situation Lucca-chan\x01",
            "I wonder if I got hated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh … … I last night\x01",
            "I want to hit around 100 shots ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B6")

    Jump("loc_1817")

    label("loc_15BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15C9")
    Jump("loc_1817")

    label("loc_15C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_16EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168C")

    ChrTalk(
        0xFE,
        (
            "If it is Ganz now\x01",
            "I'm going to Mayor town mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Ha, even so\x01",
            "Yesterday's Lucca-chan\x01",
            "I was cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it was for that smile,\x01",
            "I wonder if I can do anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16EA")

    label("loc_168C")


    ChrTalk(
        0xFE,
        (
            "… … That, that girl … ….\x01",
            "He is the son of a mine head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Together like this alone\x01",
            "What do you want?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EA")

    Jump("loc_1817")

    label("loc_16EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1817")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A2")

    ChrTalk(
        0xFE,
        (
            "Recently, Gantz is positive.\x01",
            "When I was talking about bitches\x01",
            "It is a great difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Involved in an example cult incident,\x01",
            "I was concerned about us\x01",
            "It looks like it worked.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1817")

    label("loc_17A2")


    ChrTalk(
        0xFE,
        (
            "To liquor and gamble\x01",
            "What is going to be drafted\x01",
            "As usual … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am a childhood friend and that much\x01",
            "I must stop looking at it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1817")

    TalkEnd(0xFE)
    Return()

    # Function_6_E65 end

    def Function_7_181B(): pass

    label("Function_7_181B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D0")

    ChrTalk(
        0xFE,
        (
            "I got to go to the town\x01",
            "It's also a casino\x01",
            "I thought it was not bad … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I thought, now I have to work.\x01",
            "I do not have much effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I'll do it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_191D")

    label("loc_18D0")


    ChrTalk(
        0xFE,
        (
            "When the work is over,\x01",
            "I will play in the casino as much as I want!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I'll do it!\x02",
    )

    CloseMessageWindow()

    label("loc_191D")

    Jump("loc_1DC9")

    label("loc_1922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1930")
    Jump("loc_1DC9")

    label("loc_1930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_193E")
    Jump("loc_1DC9")

    label("loc_193E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5F")

    ChrTalk(
        0xFE,
        (
            "The hunters who occupied Mainz\x01",
            "A daughter of a leader, somehow he remembered\x01",
            "I thought that there was … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Large seven giant stone in Mainz before\x01",
            "The people who purchased in large quantities\x01",
            "It looks like she was a girl inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a girl is a guard\x01",
            "Why do not you make fun of it … ….\x01",
            "I still can not believe it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1ACF")

    label("loc_1A5F")


    ChrTalk(
        0xFE,
        (
            "Such a girl is a guard\x01",
            "Why do not you make fun of it … ….\x01",
            "I still can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is exactly a nightmare fellow.\x02",
    )

    CloseMessageWindow()

    label("loc_1ACF")

    Jump("loc_1DC9")

    label("loc_1AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9E")

    ChrTalk(
        0xFE,
        (
            "Morning, this time\x01",
            "I dug a crystal of Aoyagi stone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To, somehow recently\x01",
            "My job is also perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tastiness of gambling also in this condition\x01",
            "I wish I could face it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C12")

    label("loc_1B9E")


    ChrTalk(
        0xFE,
        (
            "To, somehow recently\x01",
            "My job is also perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tastiness of gambling also in this condition\x01",
            "I wish I could face it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C12")

    Jump("loc_1DC9")

    label("loc_1C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C82")

    ChrTalk(
        0xFE,
        (
            "Apparently the Maltese guy as well\x01",
            "It seems to have recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "To, it is a burning guy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DC9")

    label("loc_1C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C90")
    Jump("loc_1DC9")

    label("loc_1C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D31")

    ChrTalk(
        0xFE,
        (
            "The guy of Malo,\x01",
            "Since the banquet yesterday is over\x01",
            "I do not feel fine …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… …. OK.\x01",
            "Here I am a childhood friend\x01",
            "I will do it with a single flight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D9F")

    label("loc_1D31")


    ChrTalk(
        0xFE,
        (
            "Maruro is in the case of a cult incident\x01",
            "You made me worry too much … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here I am a childhood friend\x01",
            "I will do it with a single flight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9F")

    Jump("loc_1DC9")

    label("loc_1DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1DB2")
    Jump("loc_1DC9")

    label("loc_1DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DC0")
    Jump("loc_1DC9")

    label("loc_1DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1DC9")

    label("loc_1DC9")

    TalkEnd(0xFE)
    Return()

    # Function_7_181B end

    def Function_8_1DCD(): pass

    label("Function_8_1DCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA4")

    ChrTalk(
        0xFE,
        (
            "After resuming it resumed,\x01",
            "There must be a tedious thing ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, I have to work in a mine\x01",
            "It was unpleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I also work as a miner on my body\x01",
            "I guess they got stuck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1F24")

    label("loc_1EA4")


    ChrTalk(
        0xFE,
        (
            "As expected, I have to work in a mine\x01",
            "It was unpleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I also work as a miner on my body\x01",
            "I guess they got stuck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F24")

    Jump("loc_278E")

    label("loc_1F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1F37")
    Jump("loc_278E")

    label("loc_1F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F45")
    Jump("loc_278E")

    label("loc_1F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_209F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_202A")

    ChrTalk(
        0xFE,
        (
            "When thinking that the occupation case was solved,\x01",
            "Next time is the case of a street attack\x01",
            "I wonder what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For Mainz and Crossbell City\x01",
            "I might have done something I can do … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… But, to my mind\x01",
            "What can you do?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_209A")

    label("loc_202A")


    ChrTalk(
        0xFE,
        (
            "For Mainz and Crossbell City\x01",
            "I might have done something I can do … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… But, to my mind\x01",
            "What can you do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_209A")

    Jump("loc_278E")

    label("loc_209F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2137")

    ChrTalk(
        0xFE,
        (
            "As it rains,\x01",
            "It got cold inside the tunnel\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, after moving the body\x01",
            "I am coming up.\x01",
            "I do not want to get hurt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_278E")

    label("loc_2137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_22B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223C")

    ChrTalk(
        0xFE,
        (
            "Recently, my grandmother\x01",
            "Come with me to bring a bride\x01",
            "It became to say … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gone mackling\x01",
            "It is nice to be pleased,\x01",
            "It is troublesome to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mine chief and Max-senior like\x01",
            "There is no incompatibility,\x01",
            "One person may be more comfortable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_22B0")

    label("loc_223C")


    ChrTalk(
        0xFE,
        (
            "I thought that I brought my bride together,\x01",
            "Younger says too much trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One person is more comfortable,\x01",
            "I will leave that to Amie.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B0")

    Jump("loc_278E")

    label("loc_22B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2481")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2405")

    ChrTalk(
        0xFE,
        (
            "If I had a break outside a while ago,\x01",
            "The son of the mine chief spoke to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Is the job of the miners fun? Why\x01",
            "I asked but from the trouble\x01",
            "I treated it properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Agreeing before,\x01",
            "Do something similar\x01",
            "I got it down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, it is a bad habit.\x01",
            "Surely there is a dream\x01",
            "I wonder if I should have said it …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_247C")

    label("loc_2405")


    ChrTalk(
        0xFE,
        (
            "The son of the mining chief,\x01",
            "Looks like aiming for a miner\x01",
            "What is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely there is a dream\x01",
            "I wonder if I should have said it …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247C")

    Jump("loc_278E")

    label("loc_2481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_260B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2581")

    ChrTalk(
        0xFE,
        (
            "Even though I just had a day off,\x01",
            "I am going to have a holiday holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because the damp life was also long.\x01",
            "How is your body coming along?\x01",
            "It is troublesome … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I will work properly.\x01",
            "To the sagory demon like before\x01",
            "I do not want to go back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2606")

    label("loc_2581")


    ChrTalk(
        0xFE,
        (
            "Even though I just had a day off,\x01",
            "I am going to have a holiday holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I will work properly.\x01",
            "To the sagory demon like before\x01",
            "I do not want to go back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2606")

    Jump("loc_278E")

    label("loc_260B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2619")
    Jump("loc_278E")

    label("loc_2619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")

    ChrTalk(
        0xFE,
        (
            "Recently, the taste of beer after work\x01",
            "I understand ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest and troublesome,\x01",
            "I often work without sabbing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, Younger\x01",
            "I will be pleased, but I do not mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2780")

    label("loc_26EF")


    ChrTalk(
        0xFE,
        (
            "Recently, the taste of beer after work\x01",
            "I understand ……\x01",
            "It stopped smoking much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, Younger\x01",
            "I will be pleased, but I do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2780")

    Jump("loc_278E")

    label("loc_2785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_278E")

    label("loc_278E")

    TalkEnd(0xFE)
    Return()

    # Function_8_1DCD end

    def Function_9_2792(): pass

    label("Function_9_2792")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_28B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2858")

    ChrTalk(
        0xFE,
        (
            "Hahaha, after a long absence of mine\x01",
            "Everyone seems to be knocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Wow, I came all too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Digging and digging, digging up … …\x01",
            "That is what we are miners!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_28AF")

    label("loc_2858")


    ChrTalk(
        0xFE,
        (
            "It digs a hole of squidness.\x01",
            "Let's keep on tight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow, I've come true!\x02",
    )

    CloseMessageWindow()

    label("loc_28AF")

    Jump("loc_2F9F")

    label("loc_28B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_28C2")
    Jump("loc_2F9F")

    label("loc_28C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_28D0")
    Jump("loc_2F9F")

    label("loc_28D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2977")

    ChrTalk(
        0xFE,
        (
            "To town like that\x01",
            "I was forced to occupy ……\x01",
            "It is a name for the miners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dutch girls, hunters\x01",
            "I will come back next time\x01",
            "Absolutely not just it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2A0A")

    label("loc_2977")


    ChrTalk(
        0xFE,
        (
            "Not only did we occupy Mainz,\x01",
            "To cross-over to Cros Bell City\x01",
            "Doing it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The hunters' bastards, if the next time comes\x01",
            "Absolutely not just it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A0A")

    Jump("loc_2F9F")

    label("loc_2A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A95")

    ChrTalk(
        0xFE,
        (
            "We are about to reach the target stratum\x01",
            "It seems to be digging forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the sea, the mountain of Yao Yaishi is in front of my eyes.\x01",
            "I'll dig it up with a spirit and scratch it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9F")

    label("loc_2A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B1D")

    ChrTalk(
        0xFE,
        (
            "Well, today as well.\x01",
            "I will not dig it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, why do not you tell me tomorrow's norm\x01",
            "Do you want to achieve at a stretch? It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9F")

    label("loc_2B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C36")

    ChrTalk(
        0xFE,
        (
            "Lately I will come out\x01",
            "With the unknown large monsters,\x01",
            "You are worried about Kami's choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are monsters that spring to mine\x01",
            "I'm used to it so much\x01",
            "I do not think there is anything to worry about ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… However, I aged ago\x01",
            "I was injured when attacked by a military dog,\x01",
            "Erra I can not say that to … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2CA6")

    label("loc_2C36")


    ChrTalk(
        0xFE,
        (
            "Well, to the unknown evil beast\x01",
            "It is supposed to be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even by any chance, Kami-san\x01",
            "I do not want to make you feel sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA6")

    Jump("loc_2F9F")

    label("loc_2CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB2")

    ChrTalk(
        0xFE,
        (
            "Yesterday, with me and the mining chief\x01",
            "Daradara from daytime\x01",
            "I was drinking … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the night back of the casino\x01",
            "Gantz participated, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rocky also because it's so hard\x01",
            "Calling, hey.\x01",
            "It was a big party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all drinking alcohol among friends\x01",
            "It's awesome.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2E12")

    label("loc_2DB2")


    ChrTalk(
        0xFE,
        (
            "Yesterday, the miners all over\x01",
            "It was a big party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all drinking alcohol among friends\x01",
            "It's awesome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E12")

    Jump("loc_2F9F")

    label("loc_2E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E25")
    Jump("loc_2F9F")

    label("loc_2E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2EB6")

    ChrTalk(
        0xFE,
        (
            "Rosie's guy,\x01",
            "It is good that motivation came out\x01",
            "The skill of work is still a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a senior here,\x01",
            "Please tell me firmly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9F")

    label("loc_2EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2F9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F60")

    ChrTalk(
        0xFE,
        (
            "For Kami's sake\x01",
            "え ん ん や こ ~ ♪ ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For Mainz\x01",
            "え ん ん や こ ~ ♪ ♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Today the day\x01",
            "Do not try hard to mining.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 4)
    Jump("loc_2F9F")

    label("loc_2F60")


    ChrTalk(
        0xFE,
        (
            "For Kami and this town\x01",
            "Let 's do my best today and mining.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9F")

    TalkEnd(0xFE)
    Return()

    # Function_9_2792 end

    def Function_10_2FA3(): pass

    label("Function_10_2FA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FB4")
    Jump("loc_3130")

    label("loc_2FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2FC2")
    Jump("loc_3130")

    label("loc_2FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FD0")
    Jump("loc_3130")

    label("loc_2FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2FDE")
    Jump("loc_3130")

    label("loc_2FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FEC")
    Jump("loc_3130")

    label("loc_2FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2FFA")
    Jump("loc_3130")

    label("loc_2FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3127")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B0")

    ChrTalk(
        0xFE,
        (
            "Wow, inside the mine\x01",
            "It was getting like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's dark and wide …\x01",
            "I heard that you are going out like an obsession.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, where is your father?\x01",
            "Let's explore and go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3122")

    label("loc_30B0")


    ChrTalk(
        0xFE,
        (
            "Dad's working\x01",
            "I wanted to see it once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, where is he?\x01",
            "Let's explore and go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3122")

    Jump("loc_3130")

    label("loc_3127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3130")

    label("loc_3130")

    TalkEnd(0xFE)
    Return()

    # Function_10_2FA3 end

    def Function_11_3134(): pass

    label("Function_11_3134")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is closed with a solid chain.\x01",
            "Apparently there seems to be a mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_11_3134 end

    SaveToFile()

Try(main)
