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
        "Function_5_5BF",          # 05, 5
        "Function_6_15DF",         # 06, 6
        "Function_7_19CE",         # 07, 7
        "Function_8_1B3C",         # 08, 8
        "Function_9_1BFC",         # 09, 9
        "Function_10_1C00",        # 0A, 10
        "Function_11_1DD2",        # 0B, 11
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
            "The "One Minute Cooking - Light Meals Edition" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_5BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Fresh Sandwich"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5BB")

    TalkEnd(0xFF)
    Return()

    # Function_4_4F5 end

    def Function_5_5BF(): pass

    label("Function_5_5BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_71E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68D")

    ChrTalk(
        0xFE,
        (
            "I t seems that Nielsen has\x01",
            "come to visit Guy's grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that he recently\x01",
            "searched about Guy's incident, but...\x01",
            "Could there have been a development?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_719")

    label("loc_68D")


    ChrTalk(
        0xFE,
        (
            "Being independent as a nation...\x01",
            "What will that bring to Crossbell...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wish to watch over the\x01",
            "people who sleep in this land.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_719")

    Jump("loc_15DB")

    label("loc_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_834")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BE")

    ChrTalk(
        0xFE,
        (
            "Just before, Arios came here.\x01",
            "He greeted me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We didn't drink like we\x01",
            "used to back then, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He too hasn't changed.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_82F")

    label("loc_7BE")


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
        "He too hasn't changed.\x02",
    )

    CloseMessageWindow()

    label("loc_82F")

    Jump("loc_15DB")

    label("loc_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8E0")

    ChrTalk(
        0xFE,
        (
            "They say that the CGF members have suffered\x01",
            "serious damage on the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't stand youngsters\x01",
            "who have a future to lose\x01",
            "their lives.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15DB")

    label("loc_8E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F4")

    ChrTalk(
        0xFE,
        (
            "Being exposed to the rain, even the \x01",
            "markers carved on the grave stones\x01",
            "get erased and fade little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thus, the existence of many graves\x01",
            "are forgotten by the people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For that to not happen, a\x01",
            "grave keeper like me is needed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AAF")

    label("loc_9F4")


    ChrTalk(
        0xFE,
        (
            "When the carved markers are exposed\x01",
            "to the rain for many years, those graves\x01",
            "existence gets forgotten by the people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For that to not happen, a\x01",
            "grave keeper like me is needed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAF")

    Jump("loc_15DB")

    label("loc_AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C22")

    ChrTalk(
        0xFE,
        (
            "Guy engaged with a childhood friend. Their time\x01",
            "together had just begun, but he was killed on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Arios lost his wife and the light of the eyes\x01",
            "of his adored daughter in an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Misfortune befell on them who\x01",
            "worked their fingers to the bone\x01",
            "for others' sake, for Crossbell's sake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...It's an unbearable story.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CDA")

    label("loc_C22")


    ChrTalk(
        0xFE,
        (
            "Guy and Arios worked their fingers\x01",
            "to the bone for others' sake and\x01",
            "Crossbell's sake, more than anyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And on such guys, misfortune befell...\x01",
            "It's an unbearable story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDA")

    Jump("loc_15DB")

    label("loc_CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_ED9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E13")

    ChrTalk(
        0xFE,
        (
            "Even the now famous Arios was\x01",
            "dragged in by Guy sometimes in\x01",
            "the past and drank together with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That guy knew what moderation is.\x01",
            "He looked at Guy and I getting drunk\x01",
            "with a composed expression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hu hu, I'd have liked to have seen him\x01",
            "at least once drunk and wild.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ED4")

    label("loc_E13")


    ChrTalk(
        0xFE,
        (
            "In the past, even that Arios was\x01",
            "dragged in by Guy sometimes\x01",
            "and drank together with us here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because he was a guy who knew\x01",
            "what moderation is, he never got\x01",
            "drunk like Guy and I did.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED4")

    Jump("loc_15DB")

    label("loc_ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_FEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F73")

    ChrTalk(
        0xFE,
        "Are you visiting a grave now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When evening falls, it becomes a little chilly here.\x01",
            "You should be done quick with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FEA")

    label("loc_F73")


    ChrTalk(
        0xFE,
        (
            "Because we're on high ground here,\x01",
            "when evening falls, it becomes a little chilly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You should be done quick.\x02",
    )

    CloseMessageWindow()

    label("loc_FEA")

    Jump("loc_15DB")

    label("loc_FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_FFD")
    Jump("loc_15DB")

    label("loc_FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_100B")
    Jump("loc_15DB")

    label("loc_100B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115C")

    ChrTalk(
        0xFE,
        (
            "The "Crossbell Problem" too roots\x01",
            "in these lands a long time ago before\x01",
            "it became called that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Getting involved in the Empire and\x01",
            "Republic frequent disputes, countless\x01",
            "innocent lives were lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to Guy, I could\x01",
            "overcome that sorrow, but...\x01",
            "Even now, many people bear scars about that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1214")

    label("loc_115C")


    ChrTalk(
        0xFE,
        (
            "The Liberl princess who came now\x01",
            "was blaming herself for the pain of\x01",
            "the "Crossbell Problem".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although young, I felt she was a person \x01",
            "brimming with compassion and kindness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1214")

    Jump("loc_15DB")

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_129C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1234")
    Call(0, 7)
    Jump("loc_1297")

    label("loc_1234")


    ChrTalk(
        0xFE,
        (
            "Hm, to think that Nielsen\x01",
            "had come back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see, tonight, I'll\x01",
            "ask him many things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1297")

    Jump("loc_15DB")

    label("loc_129C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12AA")
    Jump("loc_15DB")

    label("loc_12AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1386")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C5")
    Call(0, 11)
    Jump("loc_1381")

    label("loc_12C5")


    ChrTalk(
        0xFE,
        (
            "From North Ambria...?\x01",
            "This child too has suffered a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you expect, I can't give alcohol to a child,\x01",
            "but next time she'll come visit, I'll have at\x01",
            "least some teacakes ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1381")

    Jump("loc_15DB")

    label("loc_1386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_15C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A1")
    Call(0, 6)
    Jump("loc_15BF")

    label("loc_13A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1513")

    ChrTalk(
        0xFE,
        (
            "With Guy ending up dying, the quantity \x01",
            "of sake I drink has dropped by a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Losing a good natured drinking buddy\x01",
            "has really been a sad thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01108FGrampa...\x02\x03",
            "#01100F...When KeA gets older, she'll come with\x01",
            "Lloyd and the others to drink with you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    ChrTalk(
        0xFE,
        (
            "Ha ha, I see, I see.\x01",
            "Then, I guess I'll look forward\x01",
            "to when it'll happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15BF")

    label("loc_1513")


    ChrTalk(
        0xFE,
        (
            "Ho ho, when you little miss will\x01",
            "have the legal age to be drinking,\x01",
            "you'll probably be quite the beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll live long and look\x01",
            "forward to when\x01",
            "that time comes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BF")

    Jump("loc_15DB")

    label("loc_15C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_15D2")
    Jump("loc_15DB")

    label("loc_15D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_15DB")

    label("loc_15DB")

    TalkEnd(0xFE)
    Return()

    # Function_5_5BF end

    def Function_6_15DF(): pass

    label("Function_6_15DF")

    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Ooh, aren't you Lloyd...\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "When did you come back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, not so long ago.\x01",
            "It has been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FMr. Lloyd, who is this person...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_170B")

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, we became acquaintances\x01",
            "due to a previous request.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_170B")


    ChrTalk(
        0x101,
        (
            "#00000FYeah...\x01",
            "He's Mr. Quint. He was a drinking\x01",
            "buddy of my older brother.\x02\x03",
            "#00004FHe has been good to me too.\x01",
            "After the Cult incident, when we drank together\x01",
            "he told me many different old stories.\x02",
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
            "Well, since Lloyd didn't drink as much\x01",
            "as Guy, it was a little boring, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHa ha...I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, we joined\x01",
            "too at that time.\x02\x03",
            "#00109FBeing a minor though, Tio had only\x01",
            "juice and it appears she was unhappy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, I see.\x02\x03",
            "#10304FWell, please take good care \x01",
            "of us too from now on, mister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hm, I greatly welcome Lloyd's colleagues.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I manage this graveyard regularly.\x01",
            "You can come whenever you feel like it.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 4)
    Return()

    # Function_6_15DF end

    def Function_7_19CE(): pass

    label("Function_7_19CE")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "Thank you so much, Nielsen.\x01",
            "Such a fine liquor this is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It's pretty pricey, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No, please don't be bothered by it,\x01",
            "it's just a received gift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm happy to be able\x01",
            "to drink it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huo, huo, then, why don't we\x01",
            "drink it tonight immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh uh, all right.\x01",
            "I'll make you company after a long time.\x02",
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

    # Function_7_19CE end

    def Function_8_1B3C(): pass

    label("Function_8_1B3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1BF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B5A")
    Call(0, 7)
    Jump("loc_1BF8")

    label("loc_1B5A")


    ChrTalk(
        0xFE,
        (
            "Uh uh, if you're fine with my trivial talks,\x01",
            "I'll make you company every time you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless, I'm glad that\x01",
            "you seem to be well, Mr. Quint.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF8")

    TalkEnd(0xFE)
    Return()

    # Function_8_1B3C end

    def Function_9_1BFC(): pass

    label("Function_9_1BFC")

    Call(0, 10)
    Return()

    # Function_9_1BFC end

    def Function_10_1C00(): pass

    label("Function_10_1C00")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C15")
    Call(0, 11)
    Jump("loc_1DCE")

    label("loc_1C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D19")

    ChrTalk(
        0xA,
        (
            "#14008FHow to say it...\x01",
            "Crossbell is really\x01",
            "a mysterious city.\x02\x03",
            "#14003F...At any rate, thank goodness\x01",
            "I was able to see before my eyes\x01",
            "something I can call an "objective".\x02\x03",
            "#14002FI must do my best with many things\x01",
            "even to repay Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCE")

    label("loc_1D19")


    ChrTalk(
        0xA,
        (
            "#14003F...At any rate, thank goodness\x01",
            "I was able to make before my eyes\x01",
            "something I can call an "objective"\x02\x03",
            "#14002FI must do my best with many things\x01",
            "even to repay Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCE")

    TalkEnd(0xA)
    Return()

    # Function_10_1C00 end

    def Function_11_1DD2(): pass

    label("Function_11_1DD2")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F42")

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh, aren't you Sully...?\x01",
            "We meet in an unusual place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#14000F...Hiya, you guys, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FEehm, why are you here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2116")

    label("loc_1F42")


    ChrTalk(
        0x101,
        (
            "#12P#00005FOh, aren't you from the Arc-en-ciel...\x01",
            "We meet in an unusual place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14000F...You're Miss Ilya\x01",
            "and sister Rixia's\x01",
            "friends, right?\x02\x03",
            "By the way, I didn't\x01",
            "introduce myself, right?\x02",
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
            "I'm Sully Atraid, a\x01",
            "troupe assistant.\x02\x03",
            "...Uhhm, nice to meet you.\x02",
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
            "#12P#00109F*giggle*, nice to meet you, Sully.\x02\x03",
            "#00100FEehm, why are you here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2116")


    ChrTalk(
        0x8,
        (
            "She was walking in the graveyard\x01",
            "amidst this rain without an umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I invited her to the cabin\x01",
            "and just poured her some\x01",
            "warm cocoa.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)

    ChrTalk(
        0xA,
        (
            "#14002F...Thank you for letting me shelter\x01",
            "from the rain, old mister.\x02\x03",
            "#14004FAnd for the cocoa too...\x01",
            "Thanks to this, my body has warmed up.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        "#11PHoh hoh, I'm glad to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FBut, why the graveyard...?\x02",
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
            "#14001F...Actually, I wanted to go\x01",
            "pray at the church.\x02\x03",
            "#14003FBut, somehow I ended up hesitating.\x02\x03",
            "#14008F...In North Ambria...\x01",
            "There was a splendid church even there.\x02",
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
        "#12P#00001FNorth Ambria...isn't that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FYes, an autonomous state in\x01",
            "the north part of Zemuria.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_249D")

    ChrTalk(
        0x102,
        (
            "#12P#00105FSo the slums you said\x01",
            "you were in is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#14008FYeah...I'm from there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_24CC")

    label("loc_249D")


    ChrTalk(
        0xA,
        (
            "#14008FYeah...I come from\x01",
            "the slum there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24CC")


    ChrTalk(
        0x109,
        "#12P#10108FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHm, I heard that North Ambria is\x01",
            "a harsh place for many reasons...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14003FYeah...\x01",
            "That's a hell of a place.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#14008FThere, everyone was desperate\x01",
            "to scrape a living day by day.\x02\x03",
            "There was no leisure time at all to...\x01",
            "...Worry about someone else.\x02\x03",
            "#14003F...I don't get it well, but I think\x01",
            "this is a mysterious city.\x02\x03",
            "There're many nasty guys too, but...\x02\x03",
            "There're also people like Miss Ilya\x01",
            "who let me join the troupe...\x02\x03",
            "And even like this old mister who\x01",
            "spoke to me out of his way.\x02\x03",
            "#14000FAlso, before I noticed it, \x01",
            "I became able to attend even\x01",
            "practice as an artist...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00002FArtist practice...\x01",
            "Eeh, isn't that amazing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14005FY-Yeah...\x02\x03",
            "#14003FHowever, I still have some\x01",
            "kind of hesitations.\x02\x03",
            "#14008FSomeone like me, aiming\x01",
            "at becoming an artist...\x01",
            "I've never thought about it.\x02",
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
            "#14003FWell, even I get it that\x01",
            "it's no use brooding\x01",
            "over it too much.\x02\x03",
            "#14002FEven so...\x01",
            "You're quite the\x01",
            "eccentric group too.\x02\x03",
            "Bending an ear on purpose like this\x01",
            "to what someone like me is saying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*, however I think\x01",
            "we can't deny that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FIndeed, even among the police,\x01",
            "the Support Section is a\x01",
            "pretty irregular post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, also, no matter what anyone says,\x01",
            "the leader is especially the eccentric one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FWazy, you're one to talk.\x02\x03",
            "#00000FWell, what can I say, maybe\x01",
            "even we and Sully becoming\x01",
            "acquaintances like this was fate.\x02\x03",
            "In case you're in trouble, feel\x01",
            "free to come to consult with us, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHoh hoh, you can come to this\x01",
            "shed whenever you want too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNext time I'll have at least\x01",
            "some teacakes ready.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        "#14002FHa ha...thank you.\x02",
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

    # Function_11_1DD2 end

    SaveToFile()

Try(main)
