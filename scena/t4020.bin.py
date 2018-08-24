from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4020.bin",                # FileName
        "t4020",                    # MapName
        "t4020",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4020",                  # 0
        "Old Man Quint",          # 1
        "Nielsen",                # 2
        "Sully",                  # 3
        "Cocoa",                  # 4
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch45100.itc",                   # 01
        "chr/ch10102.itc",                   # 02
        "apl/ch51090.itc",                   # 03
    ))

    DeclNpc(260260,  0,       250,     0,    385,  0x0, 0,   0,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(260149,  0,       4294965546, 135,  389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(257899,  50,      2880,    90,   389,  0x0, 0,   2,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(258209,  500,     2099,    0,    502,  0x0, 7,   3,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(262920,  0,       3100,    1200,    262920,  1200,    3100,    0x007C, 0,  4,  0x0000)
    DeclActor(257930,  0,       1240,    1200,    257899,  1000,    2880,    0x007E, 0,  9,  0x0000)

    ChipFrameInfo(396, 0)                                        # 0

    ScpFunction((
        "Function_0_18C",          # 00, 0
        "Function_1_23C",          # 01, 1
        "Function_2_267",          # 02, 2
        "Function_3_44F",          # 03, 3
        "Function_4_4F5",          # 04, 4
        "Function_5_5B9",          # 05, 5
        "Function_6_159A",         # 06, 6
        "Function_7_1951",         # 07, 7
        "Function_8_1AA9",         # 08, 8
        "Function_9_1B50",         # 09, 9
        "Function_10_1B54",        # 0A, 10
        "Function_11_1D0D",        # 0B, 11
    ))


    def Function_0_18C(): pass

    label("Function_0_18C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1C4"),
        (1, "loc_1D0"),
        (2, "loc_1DC"),
        (3, "loc_1E8"),
        (4, "loc_1F4"),
        (5, "loc_200"),
        (6, "loc_20C"),
        (SWITCH_DEFAULT, "loc_218"),
    )


    label("loc_1C4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1D0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1DC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1E8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1F4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_200")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_218")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_224")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_23B")

    Return()

    # Function_0_18C end

    def Function_1_23C(): pass

    label("Function_1_23C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_266")
    OP_94(0xFE, 0x3F516, 0xFFFFFA38, 0x3FD0E, 0x8B6, 0x3E8)
    Sleep(600)
    Jump("Function_1_23C")

    label("loc_266")

    Return()

    # Function_1_23C end

    def Function_2_267(): pass

    label("Function_2_267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_275")
    Jump("loc_44E")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_283")
    Jump("loc_44E")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_29C")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_29C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B5")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2CE")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E7")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_300")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_319")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_332")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_340")
    Jump("loc_44E")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34E")
    Jump("loc_44E")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_367")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B7")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 260209, 0, -130, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 260260, 0, 1420, 180)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Jump("loc_44E")

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C5")
    Jump("loc_44E")

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_41E")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0x8, 259550, 0, 2840, 270)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_419")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_419")

    Jump("loc_44E")

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_437")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_445")
    Jump("loc_44E")

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_44E")

    label("loc_44E")

    Return()

    # Function_2_267 end

    def Function_3_44F(): pass

    label("Function_3_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46B")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_482")

    label("loc_46B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_482")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CB")
    SetMapObjFrame(0xFF, "hikari00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "footlight00", 0x0, 0x1)
    Sound(128, 1, 50, 0)
    Jump("loc_4DE")

    label("loc_4CB")

    SetMapObjFrame(0xFF, "footlight01", 0x0, 0x1)

    label("loc_4DE")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F4")
    OP_66(0x1, 0x1)

    label("loc_4F4")

    Return()

    # Function_3_44F end

    def Function_4_4F5(): pass

    label("Function_4_4F5")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""One Minute Cooking -\x01",
            "Light Meals Edition" is\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_5B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Fresh\x01",
            "Sandwich"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5B5")

    TalkEnd(0xFF)
    Return()

    # Function_4_4F5 end

    def Function_5_5B9(): pass

    label("Function_5_5B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_676")

    ChrTalk(
        0xFE,
        (
            "It seems Nielsen came to\x01",
            "visit Guy's grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard he was researching the\x01",
            "Guy case recently, but... Could\x01",
            "there have been a development?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_702")

    label("loc_676")


    ChrTalk(
        0xFE,
        (
            "Being independent as a\x01",
            "nation... What will that\x01",
            "mean for Crossbell...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wish to watch over\x01",
            "the people who sleep in\x01",
            "this land.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_702")

    Jump("loc_1596")

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_81D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A4")

    ChrTalk(
        0xFE,
        (
            "Arios was here earlier.\x01",
            "He said hello.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We didn't drink like we\x01",
            "used to back then,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He hasn't changed\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_818")

    label("loc_7A4")


    ChrTalk(
        0xFE,
        (
            "Even now, when Arios drops\x01",
            "by the graveyard, he comes\x01",
            "to greet me respectfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He hasn't changed\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_818")

    Jump("loc_1596")

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8CA")

    ChrTalk(
        0xFE,
        (
            "They say that the CGF members\x01",
            "have suffered serious damage\x01",
            "on the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't stand it when\x01",
            "youngsters with a future\x01",
            "lose their lives.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1596")

    label("loc_8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C6")

    ChrTalk(
        0xFE,
        (
            "Being exposed to the rain,\x01",
            "the carved grave markers\x01",
            "fade, little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thus, the existence of\x01",
            "many graves are forgotten\x01",
            "by the people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To make sure that doesn't\x01",
            "happen, a grave keeper\x01",
            "like me is needed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A98")

    label("loc_9C6")


    ChrTalk(
        0xFE,
        (
            "When the carved grave markers are exposed to\x01",
            "the rain for many years, the existence of\x01",
            "those graves gets forgotten by the people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To make sure that doesn't\x01",
            "happen, a grave keeper\x01",
            "like me is needed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A98")

    Jump("loc_1596")

    label("loc_A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1A")

    ChrTalk(
        0xFE,
        (
            "Guy got engaged to his childhood friend.\x01",
            "Their time together had just begun, but\x01",
            "he was killed in the line of duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Arios lost his wife and the\x01",
            "light of the eyes of his beloved\x01",
            "daughter in an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Misfortune befell they, who worked\x01",
            "their fingers to the bone for others'\x01",
            "sake, for Crossbell's sake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It's an unbearable\x01",
            "story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CD9")

    label("loc_C1A")


    ChrTalk(
        0xFE,
        (
            "Guy and Arios worked their fingers to\x01",
            "the bone for others' sake and\x01",
            "Crossbell's sake, more than anyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And such a terrible\x01",
            "misfortune befell them...\x01",
            "It's an unbearable story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD9")

    Jump("loc_1596")

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_EE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E30")

    ChrTalk(
        0xFE,
        (
            "A long time ago, even the\x01",
            "now-famous Arios got roped in\x01",
            "by Guy to come drink with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That fella knew what moderation is. Guy and I\x01",
            "would get absolutely hammered and he'd simply\x01",
            "look at us with a calm and collected expression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I'd have liked for\x01",
            "him to get drunk and go\x01",
            "wild at least once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EE0")

    label("loc_E30")


    ChrTalk(
        0xFE,
        (
            "A long time ago, even that Arios\x01",
            "got roped in by Guy sometimes to\x01",
            "come drink with us here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because he knew what\x01",
            "moderation is, he never got\x01",
            "drunk like Guy and I did.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE0")

    Jump("loc_1596")

    label("loc_EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6E")

    ChrTalk(
        0xFE,
        (
            "Are you visiting a grave\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It becomes a little chilly\x01",
            "here when night falls. You\x01",
            "finish quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FDE")

    label("loc_F6E")


    ChrTalk(
        0xFE,
        (
            "Because we're on high\x01",
            "ground, it becomes a little\x01",
            "chilly when night falls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should finish\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDE")

    Jump("loc_1596")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_FF1")
    Jump("loc_1596")

    label("loc_FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FFF")
    Jump("loc_1596")

    label("loc_FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1129")

    ChrTalk(
        0xFE,
        (
            "The Crossbell Problem has\x01",
            "its roots in this land long\x01",
            "before it was called that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Countless innocent lives were\x01",
            "lost in the Empire and\x01",
            "Republic's frequent disputes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to Guy, I overcame that\x01",
            "sorrow, but... Even now, many\x01",
            "people bear the scars of that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11E1")

    label("loc_1129")


    ChrTalk(
        0xFE,
        (
            "The Liberl princess who came just\x01",
            "now was blaming herself for the\x01",
            "pain of the Crossbell Problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though young, I felt she\x01",
            "was a person brimming with\x01",
            "compassion and kindness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E1")

    Jump("loc_1596")

    label("loc_11E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1267")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1201")
    Call(0, 7)
    Jump("loc_1262")

    label("loc_1201")


    ChrTalk(
        0xFE,
        (
            "Hmm, to think that\x01",
            "Nielsen came back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I think I'll ask\x01",
            "him many things tonight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1262")

    Jump("loc_1596")

    label("loc_1267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1275")
    Jump("loc_1596")

    label("loc_1275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_134E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1290")
    Call(0, 11)
    Jump("loc_1349")

    label("loc_1290")


    ChrTalk(
        0xFE,
        (
            "From North Ambria...?\x01",
            "This child has suffered\x01",
            "a lot too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you might expect, I can't give alcohol\x01",
            "to a child, but I'll have at least some\x01",
            "tea cakes ready for her next visit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1349")

    Jump("loc_1596")

    label("loc_134E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_157F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1369")
    Call(0, 6)
    Jump("loc_157A")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D5")

    ChrTalk(
        0xFE,
        (
            "With Guy's passing, the\x01",
            "quantity of sake I drink\x01",
            "has dropped by a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Losing a good-natured\x01",
            "drinking buddy has\x01",
            "really been a sad thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01108FGrampa...\x02\x03",
            "#01100F...When KeA gets older,\x01",
            "she'll come with Lloyd and\x01",
            "the others to drink with you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    ChrTalk(
        0xFE,
        (
            "Haha, I see, I see. I\x01",
            "suppose I'll just have to\x01",
            "look forward to that, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_157A")

    label("loc_14D5")


    ChrTalk(
        0xFE,
        (
            "Hoho, when the little lady here is\x01",
            "of drinking drinking age, she'll\x01",
            "probably be quite the beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll live long and look\x01",
            "forward to when that\x01",
            "time comes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157A")

    Jump("loc_1596")

    label("loc_157F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_158D")
    Jump("loc_1596")

    label("loc_158D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1596")

    label("loc_1596")

    TalkEnd(0xFE)
    Return()

    # Function_5_5B9 end

    def Function_6_159A(): pass

    label("Function_6_159A")

    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, Lloyd... Long time\x01",
            "no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "When did you get back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNot too long ago. It has\x01",
            "been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FLloyd, who is this?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_16A0")

    ChrTalk(
        0x102,
        (
            "#00100FHaha. We became\x01",
            "acquainted through a\x01",
            "previous request.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A0")


    ChrTalk(
        0x101,
        (
            "#00000FYeah... He's Mr. Quint, a drinking\x01",
            "buddy of my older brother's.\x02\x03",
            "#00004FHe's been good to me too. After the\x01",
            "cult incident, he told me many old\x01",
            "stories when we drank together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I really enjoyed that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, since Lloyd can't drink\x01",
            "as much as Guy, it was a\x01",
            "little boring, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha... Sorry about\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha. We sat with you\x01",
            "both for that.\x02\x03",
            "#00109FBeing a minor though,\x01",
            "Tio had juice and looked\x01",
            "unhappy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha. I see.\x02\x03",
            "#10304FWell, please take good\x01",
            "care of us too from now\x01",
            "on, old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, your colleagues are\x01",
            "more than welcome to\x01",
            "join me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can usually be found\x01",
            "managing this graveyard.\x01",
            "Stop by whenever you like.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 4)
    Return()

    # Function_6_159A end

    def Function_7_1951(): pass

    label("Function_7_1951")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "Thank you so much,\x01",
            "Nielsen. This is fine\x01",
            "liquor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's pretty pricey,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No, please don't worry\x01",
            "about it. It was a gift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm happy to be able to\x01",
            "drink it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hoho, then, why don't we\x01",
            "drink it tonight right\x01",
            "away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, all right. It's\x01",
            "been a while since I\x01",
            "joined you for this.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    Return()

    # Function_7_1951 end

    def Function_8_1AA9(): pass

    label("Function_8_1AA9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC7")
    Call(0, 7)
    Jump("loc_1B4C")

    label("loc_1AC7")


    ChrTalk(
        0xFE,
        (
            "Haha. If you're fine with\x01",
            "my trivial talk, I'll join\x01",
            "you anytime you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless, I'm glad\x01",
            "that you're well, Quint.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B4C")

    TalkEnd(0xFE)
    Return()

    # Function_8_1AA9 end

    def Function_9_1B50(): pass

    label("Function_9_1B50")

    Call(0, 10)
    Return()

    # Function_9_1B50 end

    def Function_10_1B54(): pass

    label("Function_10_1B54")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B69")
    Call(0, 11)
    Jump("loc_1D09")

    label("loc_1B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C64")

    ChrTalk(
        0xA,
        (
            "#14008FHow to say it... Crossbell really\x01",
            "is a strange city, isn't it.\x02\x03",
            "#14003F...Anyway, thank goodness I was\x01",
            "able to find something to call an\x01",
            ""objective" right under my nose.\x02\x03",
            "#14002FI've got to do my best to repay\x01",
            "Ilya as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D09")

    label("loc_1C64")


    ChrTalk(
        0xA,
        (
            "#14003F...Anyway, thank goodness I was\x01",
            "able to find something to call an\x01",
            ""objective" right under my nose.\x02\x03",
            "#14002FI've got to do my best to repay\x01",
            "Ilya as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D09")

    TalkEnd(0xA)
    Return()

    # Function_10_1B54 end

    def Function_11_1D0D(): pass

    label("Function_11_1D0D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(258420, 1500, 830, 0)
    MoveCamera(28, 23, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33960, 0)
    SetChrPos(0x101, 258709, 0, 120, 0)
    SetChrPos(0x102, 259860, 0, -120, 0)
    SetChrPos(0x109, 259010, 0, -1110, 0)
    SetChrPos(0x105, 260160, 0, -1370, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu14000.itp")
    OP_4B(0x8, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0x64, 0x0)
    SetChrSubChip(0xA, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E67")

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh, Sully? Fancy seeing\x01",
            "you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#14000F...Oh, you guys, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FUmm, why are you here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_200D")

    label("loc_1E67")


    ChrTalk(
        0x101,
        (
            "#12P#00005FOh, you're from Arc-en-\x01",
            "Ciel... Fancy seeing you\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14000F...You guys know Ilya\x01",
            "and Rixia, right?\x02\x03",
            "In that case, allow me\x01",
            "to introduce myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            "Troupe assistant Sully Atraid's the\x01",
            "name.\x02\x03",
            "...Umm, nice to meet you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#12P#00109FLikewise, Sully.\x02\x03",
            "#00100FUmm, why are you here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200D")


    ChrTalk(
        0x8,
        (
            "She was walking in the\x01",
            "graveyard in this rain\x01",
            "without an umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I invited her to the\x01",
            "cabin and just made her\x01",
            "some warm cocoa.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)

    ChrTalk(
        0xA,
        (
            "#14002F...Thanks for getting me\x01",
            "out of that rain, old\x01",
            "man.\x02\x03",
            "#14004FAnd for the cocoa too...\x01",
            "Thanks to this, I've\x01",
            "warmed up.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        "#11PHoho, glad to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FBut, why the\x01",
            "graveyard...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)

    ChrTalk(
        0xA,
        (
            "#14001F...Actually, I wanted to\x01",
            "go pray at the church.\x02\x03",
            "#14003FBut, I hesitated for some\x01",
            "reason.\x02\x03",
            "#14008F...Because in North\x01",
            "Ambria, there wasn't a\x01",
            "splendid church like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00001FNorth Ambria... Isn't\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FYeah, it's a state in\x01",
            "north Zemuria.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_236B")

    ChrTalk(
        0x102,
        (
            "#12P#00105FThen, the slum you lived\x01",
            "in was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14008FYeah... That's where I'm\x01",
            "from.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2396")

    label("loc_236B")


    ChrTalk(
        0xA,
        (
            "#14008FYeah... I'm from a slum\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2396")


    ChrTalk(
        0x109,
        "#12P#10108FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes. I heard it's a hard\x01",
            "place to live for many\x01",
            "reasons, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14003FYeah... It's one hell of\x01",
            "a place. Like you\x01",
            "wouldn't believe.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#14008FThere, even though\x01",
            "everyone made it by, day-\x01",
            "by-day, it was a struggle.\x02\x03",
            "Worrying about someone\x01",
            "other than yourself? Oh\x01",
            "please.\x02\x03",
            "#14003F...I don't really get it,\x01",
            "but I think this is a\x01",
            "strange place.\x02\x03",
            "It's got its fair share of\x01",
            "nasty guys as well, but...\x02\x03",
            "There's people like Ilya,\x01",
            "who would let someone like\x01",
            "me join the troupe...\x02\x03",
            "And like this old man, who\x01",
            "just got me out of this\x01",
            "rain.\x02\x03",
            "#14000FAnd before I knew it, they\x01",
            "started training me as an\x01",
            "artist...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00002FArtist training... Wow,\x01",
            "that's amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14005FY-Yeah...\x02\x03",
            "#14003FIt's just, I still feel\x01",
            "lost.\x02\x03",
            "#14008FSomeone like me, trying to\x01",
            "become an artist... I've\x01",
            "never even thought about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FSully...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14003FWell, I know excessively\x01",
            "worrying about it won't\x01",
            "solve anything, at least.\x02\x03",
            "#14002FEven so... You're quite the\x01",
            "strange group yourselves.\x02\x03",
            "Going out of your way to\x01",
            "listen to my story like\x01",
            "this... What's up with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHaha. But I think we\x01",
            "can't deny it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FIt's certainly true that the\x01",
            "Support Section is an unusual\x01",
            "post, even within the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHeh. And if pushed, I'd\x01",
            "say our leader is\x01",
            "especially strange, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYou're one to talk,\x01",
            "Wazy.\x02\x03",
            "#00000FHow should I put it? I\x01",
            "feel like our meeting\x01",
            "was fate.\x02\x03",
            "If you're ever in\x01",
            "trouble, let us know\x01",
            "right away, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHoho. Feel free to visit\x01",
            "my shed whenever you\x01",
            "like as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNext time, I'll even\x01",
            "have teacakes ready for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        "#14002FHaha... Thanks.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x133, 6)
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 259230, 0, -370, 0)
    EventEnd(0x5)
    Return()

    # Function_11_1D0D end

    SaveToFile()

Try(main)
