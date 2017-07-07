from ScenarioHelper import *

def main():
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
        "Quint old man",           # 1
        "Nielsen",             # 2
        "Shuri",                 # 3
        "cocoa",                 # 4
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
        "Function_5_5A8",          # 05, 5
        "Function_6_13A2",         # 06, 6
        "Function_7_1736",         # 07, 7
        "Function_8_186A",         # 08, 8
        "Function_9_18FE",         # 09, 9
        "Function_10_1902",        # 0A, 10
        "Function_11_1A8D",        # 0B, 11
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
            "\"One-minute cooking · Light meal compilation\" is available.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_5A4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Fresh Sand\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5A4")

    TalkEnd(0xFF)
    Return()

    # Function_4_4F5 end

    def Function_5_5A8(): pass

    label("Function_5_5A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65E")

    ChrTalk(
        0xFE,
        (
            "Nielsen君が\x01",
            "You seem to be coming to a grave of a guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He recently talked about Guy's case\x01",
            "It seems I looked up … …\x01",
            "I wonder if there was progress.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E4")

    label("loc_65E")


    ChrTalk(
        0xFE,
        (
            "Independence as a nation ……\x01",
            "What will it bring to the crossbell ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Hopefully to those who sleep in this place\x01",
            "It is something I want you to watch over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E4")

    Jump("loc_139E")

    label("loc_6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_798")

    ChrTalk(
        0xFE,
        (
            "Arios came here earlier.\x01",
            "He greeted me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like alcohol like to drink together\x01",
            "Drinking is gone … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I understand that the apple has changed.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7FC")

    label("loc_798")


    ChrTalk(
        0xFE,
        (
            "Even now Arios,\x01",
            "If you go to the cemetery and be a honor\x01",
            "It will come and greet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I understand that the apple has changed.\x02",
    )

    CloseMessageWindow()

    label("loc_7FC")

    Jump("loc_139E")

    label("loc_801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_896")

    ChrTalk(
        0xFE,
        (
            "In the mountain path to the guards\x01",
            "It is said that enormous damage has come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Future young people\x01",
            "It is the scattering life,\x01",
            "I can not bear it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139E")

    label("loc_896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_977")

    ChrTalk(
        0xFE,
        (
            "If exposed to the rain,\x01",
            "Tomb grave carved in the grave etc\x01",
            "It gradually scrapes away and disappears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And that existence from people\x01",
            "There are also many graves to be forgotten ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order not to be so,\x01",
            "You need a grave protection like me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A0C")

    label("loc_977")


    ChrTalk(
        0xFE,
        (
            "Over the years, exposed to the rain\x01",
            "If tomb marks are eliminated, their existence is\x01",
            "People will forget … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order not to be so,\x01",
            "You need a grave protection like me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0C")

    Jump("loc_139E")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20")

    ChrTalk(
        0xFE,
        (
            "Guy's guy engaged with childhood friend\x01",
            "I died when I was about to die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Arios' fellow, with his wife's life\x01",
            "I lost the light of my daughter's eyes in the accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For others, for crossbell\x01",
            "To those who were scattering themselves\x01",
            "Misfortune will spill over … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… … It is a talking story.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BA9")

    label("loc_B20")


    ChrTalk(
        0xFE,
        (
            "Guy and Arios than anyone,\x01",
            "For others, for crossbell\x01",
            "She was scattering herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such unhappiness will be sprinkled on them … …\x01",
            "It is a talking story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA9")

    Jump("loc_139E")

    label("loc_BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCA")

    ChrTalk(
        0xFE,
        (
            "Now also famous Arios,\x01",
            "Once in a while I was pulled by a guy\x01",
            "A daughter who drank with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Appreciate the moderation.\x01",
            "I am drunk with me and Guy,\x01",
            "I watched it with a disgusting face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, that he was drunk and disturbed\x01",
            "I wanted to see it once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D74")

    label("loc_CCA")


    ChrTalk(
        0xFE,
        (
            "In the past Arios'\x01",
            "Sometimes pulled by a guy\x01",
            "I was drinking alcohol together here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From a fellow who is moderating moderation,\x01",
            "Like me or a guy\x01",
            "I did not get drunk.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D74")

    Jump("loc_139E")

    label("loc_D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_E49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF3")

    ChrTalk(
        0xFE,
        "Did you go to a grave from now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It cools somewhat at night.\x01",
            "I will finish early, but yeah.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E44")

    label("loc_DF3")


    ChrTalk(
        0xFE,
        (
            "Because it is in the hill here,\x01",
            "It cools somewhat at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will finish early, but yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_E44")

    Jump("loc_139E")

    label("loc_E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_E57")
    Jump("loc_139E")

    label("loc_E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E65")
    Jump("loc_139E")

    label("loc_E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_103A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F92")

    ChrTalk(
        0xFE,
        (
            "\"Crossbell problem\"\x01",
            "Before it got called so\x01",
            "It was rooted in this place for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For repeated conflicts between the Empire and the Republic\x01",
            "It is involved and an innocent life\x01",
            "It has been countlessly lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to Guy\x01",
            "I could overcome that sorrow … …\x01",
            "There are many people who are still having scars.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1035")

    label("loc_F92")


    ChrTalk(
        0xFE,
        (
            "Princess Libert, who is coming now,\x01",
            "Pain in the \"crossbar problem\"\x01",
            "I think like my body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it is still young, I have great mercy and kindness\x01",
            "I felt it was full of people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1035")

    Jump("loc_139E")

    label("loc_103A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_10C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1055")
    Call(0, 7)
    Jump("loc_10BF")

    label("loc_1055")


    ChrTalk(
        0xFE,
        (
            "ふむ、しかしNielsen君が\x01",
            "It is said that he came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which one is different tonight\x01",
            "I will tell you a story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BF")

    Jump("loc_139E")

    label("loc_10C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10D2")
    Jump("loc_139E")

    label("loc_10D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1189")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10ED")
    Call(0, 11)
    Jump("loc_1184")

    label("loc_10ED")


    ChrTalk(
        0xFE,
        (
            "Are you from Northern Buria? …\x01",
            "I guess this child also had a hard time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected you can not drink alcohol to your opponent,\x01",
            "Next time I came to play it was about sweets\x01",
            "Get ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1184")

    Jump("loc_139E")

    label("loc_1189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1387")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A4")
    Call(0, 6)
    Jump("loc_1382")

    label("loc_11A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12DE")

    ChrTalk(
        0xFE,
        (
            "Guy is dead,\x01",
            "The amount of drink I drink has decreased considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To lose a good drink buddy,\x01",
            "After all it is a lonesome monkey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01108FUncle … ….\x02\x03",
            "#01100F…… KEIA, when it's okay\x01",
            "Because I come to drink with Lloyd's!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    ChrTalk(
        0xFE,
        (
            "Well, I guess so.\x01",
            "Look forward to that time\x01",
            "I am sorry to have kept you waiting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1382")

    label("loc_12DE")


    ChrTalk(
        0xFE,
        (
            "Ho, my daughter\x01",
            "By the time I can drink alcohol\x01",
            "Significant alternative#4RBeautiful#Let's get turned into san.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I lived long enough,\x01",
            "Look forward to that time\x01",
            "I am sorry to have kept you waiting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1382")

    Jump("loc_139E")

    label("loc_1387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1395")
    Jump("loc_139E")

    label("loc_1395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_139E")

    label("loc_139E")

    TalkEnd(0xFE)
    Return()

    # Function_5_5A8 end

    def Function_6_13A2(): pass

    label("Function_6_13A2")

    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, you are Lloyd ……\x01",
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
            "#00000FWell, it is the last time.\x01",
            "I was out of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FMr. Lloyd, who is this …?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14B0")

    ChrTalk(
        0x102,
        (
            "#00100FHuhuu, there was a request before\x01",
            "You got to know each other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B0")


    ChrTalk(
        0x101,
        (
            "#00000FAh……\x01",
            "I was drinking partner with my big brother.\x01",
            "Mr. Quinto.\x02\x03",
            "#00004FHe was doing well for my brother.\x01",
            "Even when we drank together after a cult incident\x01",
            "He tells us stories about various stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I was having fun at that time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, Lloyd does not drink as much as Guy\x01",
            "It was a bit boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHaha … I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhuu, that time we also\x01",
            "I asked him to be present.\x02\x03",
            "#00109FMinor Tio-chan\x01",
            "I seemed dissatisfied with just juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, I see.\x02\x03",
            "#10304FWell, from now on we both\x01",
            "Regards, old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, Lloyd's colleagues are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I usually manage this cemetery.\x01",
            "I will come whenever I feel well.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 4)
    Return()

    # Function_6_13A2 end

    def Function_7_1736(): pass

    label("Function_7_1736")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "悪いのう、Nielsen君。\x01",
            "Such a nice drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Let's be pretty expensive?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No, as it is a piece of money\x01",
            "please do not worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you can drink here\x01",
            "I'm happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wait a minute, now\x01",
            "Would you like to have a drink together tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe, it is nice.\x01",
            "I will try your opponent after a long absence.\x02",
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

    # Function_7_1736 end

    def Function_8_186A(): pass

    label("Function_8_186A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1888")
    Call(0, 7)
    Jump("loc_18FA")

    label("loc_1888")


    ChrTalk(
        0xFE,
        (
            "Huhu, I like crap\x01",
            "As much as you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, Ms. Quinto\x01",
            "I'm glad that you are fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18FA")

    TalkEnd(0xFE)
    Return()

    # Function_8_186A end

    def Function_9_18FE(): pass

    label("Function_9_18FE")

    Call(0, 10)
    Return()

    # Function_9_18FE end

    def Function_10_1902(): pass

    label("Function_10_1902")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1917")
    Call(0, 11)
    Jump("loc_1A89")

    label("loc_1917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F8")

    ChrTalk(
        0xA,
        (
            "#14008FWhat I should say …\x01",
            "Crossbell is really\x01",
            "It's a mysterious city.\x02\x03",
            "#14003F…… Anyway, thanks to you\x01",
            "Now we can also call on goals\x01",
            "I could do it.\x02\x03",
            "#14002FTo return gratitude to Iria,\x01",
            "I have to work hard in various ways.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A89")

    label("loc_19F8")


    ChrTalk(
        0xA,
        (
            "#14003F…… Anyway, thanks to you\x01",
            "Now we can also call on goals\x01",
            "I could do it.\x02\x03",
            "#14002FTo return gratitude to Iria,\x01",
            "I have to work hard in various ways.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A89")

    TalkEnd(0xA)
    Return()

    # Function_10_1902 end

    def Function_11_1A8D(): pass

    label("Function_11_1A8D")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BFC")

    ChrTalk(
        0x101,
        (
            "#12P#00005Fあれ、君はShuri……？\x01",
            "Do not meet at unusual places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#14000FWell, yeah, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FEr, why on earth?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DC5")

    label("loc_1BFC")


    ChrTalk(
        0x101,
        (
            "#12P#00005FWell, you are the alkane shell … …\x01",
            "Do not meet at unusual places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14000F… …. You,\x01",
            "Ilia and Lisa's older sister\x01",
            "I was acquainted.\x02\x03",
            "So introduce yourself\x01",
            "I did not do it.\x02",
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
            "I am a jackpot of a troupe\x01",
            "Shuri・アトレイドだ。\x02\x03",
            "Well, thank you.\x02",
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
            "#12P#00109Fふふ、よろしくねShuriちゃん。\x02\x03",
            "#00100FEr, why on earth?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC5")


    ChrTalk(
        0x8,
        (
            "Without this umbrella in this rain\x01",
            "I was walking in the graveyard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Invited me to the hut,\x01",
            "温かいcocoaを淹れてやった\x01",
            "It was where it was.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)

    ChrTalk(
        0xA,
        (
            "#14002F…… Did she take shelter from the rain?\x01",
            "Thank you, Mr. Ju.\x02\x03",
            "#14004Fこのcocoaも……\x01",
            "Thanks body got warm.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        "#11PHo ho, that's nothing but something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FBut why in the cemetery …?\x02",
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
            "#14001F…… Actually to the church\x01",
            "I intended to go pray.\x02\x03",
            "#14003FBut, it is somewhat shaggy.\x02\x03",
            "#14008F…… To Northern Buri,\x01",
            "Because there was not a fine church over there.\x02",
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
        "#12P#00001FSurely Northern Buria ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10303FOh, it's an autonomous state in the northern continent.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_210F")

    ChrTalk(
        0x102,
        (
            "#12P#00105Fそれじゃあ、Shuriちゃんが\x01",
            "Slum is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#14008FOh … … I am from there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2147")

    label("loc_210F")


    ChrTalk(
        0xA,
        (
            "#14008FOh …… I am over there\x01",
            "I am from the slums.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2147")


    ChrTalk(
        0x109,
        "#12P#10108FThat's right ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHmm, Northern Buria\x01",
            "I heard that there are various difficult places ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14003FAh……\x01",
            "That is ridiculous, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#14008FOver there, everyone\x01",
            "I was desperate to live that day.\x02\x03",
            "I can not afford to care about people …\x01",
            "There was no such thing.\x02\x03",
            "#14003F…… I do not really understand it,\x01",
            "I think this is a really mysterious city.\x02\x03",
            "There are many innocent people, though ….\x02\x03",
            "I will put in a troupe for me\x01",
            "If someone like Iria … …\x02\x03",
            "In this way, I will take the trouble to speak\x01",
            "Some people like Ja - san.\x02\x03",
            "#14000FAlso, before unnoticed\x01",
            "As well as practicing as an artist\x01",
            "I got to get it attached ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00002FArtist practice ……\x01",
            "Well, that is amazing, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14005FOh, ah ……\x02\x03",
            "#14003FJust a while ago\x01",
            "I have confusion, though.\x02\x03",
            "#14008FA human being like me\x01",
            "To be an artist … …\x01",
            "I never even thought about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FShuriちゃん……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14003FWell, even if I suffer too much\x01",
            "There is no use\x01",
            "I know it, though.\x02\x03",
            "#14002FEven so ……\x01",
            "You too are equivalent,\x01",
            "It is a kind of oddball.\x02\x03",
            "In this way, to my story\x01",
            "Do not bother to listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FIs that so …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHuhu, but denial is\x01",
            "It may not be possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FCertainly, even among the police\x01",
            "The support department is quite irregular\x01",
            "It is a department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, and whatever I say\x01",
            "Especially the leader is a strange person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FWaji, you say that.\x02\x03",
            "#00000FWell, what do you mean?\x01",
            "俺たちとShuriがこうして\x01",
            "I guess I was acquainted with something.\x02\x03",
            "If there is something in trouble\x01",
            "Could you talk to me anytime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHo, this cabin, too,\x01",
            "You can come anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PEven one of the sweets\x01",
            "Let me prepare.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        "#14002FHaha … Thank you.\x02",
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

    # Function_11_1A8D end

    SaveToFile()

Try(main)
