from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c022b.bin",                # FileName
        "c022b",                    # MapName
        "c022b",                    # Location
        0x000D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c022b",                  # 0
        "Ian lawyer",           # 1
        "Pete",                 # 2
    ))

    AddCharChip((
        "chr/ch05900.itc",                   # 00
        "chr/ch05902.itc",                   # 01
        "chr/ch22200.itc",                   # 02
    ))

    DeclNpc(4510,    1169,    15779,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(12869,   1000,    4809,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)

    DeclActor(14350,   1000,    4294967226, 2000,    14350,   2500,    4294967226, 0x007C, 0,  5,  0x0000)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_1C4",          # 01, 1
        "Function_2_1E4",          # 02, 2
        "Function_3_1EB",          # 03, 3
        "Function_4_3EF",          # 04, 4
        "Function_5_5E9",          # 05, 5
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_14C"),
        (1, "loc_158"),
        (2, "loc_164"),
        (3, "loc_170"),
        (4, "loc_17C"),
        (5, "loc_188"),
        (6, "loc_194"),
        (SWITCH_DEFAULT, "loc_1A0"),
    )


    label("loc_14C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_158")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_164")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_170")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_17C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_188")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_194")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1C3")

    Return()

    # Function_0_114 end

    def Function_1_1C4(): pass

    label("Function_1_1C4")

    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 3)), scpexpr(EXPR_END)), "loc_1E3")
    SetChrFlags(0x9, 0x10)

    label("loc_1E3")

    Return()

    # Function_1_1C4 end

    def Function_2_1E4(): pass

    label("Function_2_1E4")

    ClearMapObjFlags(0x0, 0x10)
    Return()

    # Function_2_1E4 end

    def Function_3_1EB(): pass

    label("Function_3_1EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384")

    ChrTalk(
        0xFE,
        (
            "#02200FOh, you guys.\x01",
            "It is rare to come this kind of night.\x02\x03",
            "Daddy is with you … …\x01",
            "It seems to be related to tomorrow's meeting\x01",
            "Have you had problems as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FFrom now on, make sure of it\x01",
            "I'm going.\x02\x03",
            "#00600FFor the sake of completeness,\x01",
            "To keep uncertain elements crushed\x01",
            "I have never done it before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02200FWell, it's too cautious.\x01",
            "It will not be.\x02\x03",
            "I do not know detailed circumstances … …\x01",
            "Please do it by all means.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3EB")

    label("loc_384")


    ChrTalk(
        0xFE,
        (
            "#02200FNow……\x01",
            "Preparation is enough around here.\x02\x03",
            "In preparation for tomorrow for the time being,\x01",
            "Shall I take a day off earlier today?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB")

    TalkEnd(0xFE)
    Return()

    # Function_3_1EB end

    def Function_4_3EF(): pass

    label("Function_4_3EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_569")

    ChrTalk(
        0xFE,
        (
            "I was organizing documents\x01",
            "When I was an answering machine before\x01",
            "The book that I was reading came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Kagemaru\" appearing in this book … …\x01",
            "I like it better than Mitchell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I read the book once,\x01",
            "It is a sex that I do not read too much … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's no problem\x01",
            "Why do not you read it, too?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝４卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝４卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 3)
    TalkEnd(0xFE)
    SetChrFlags(0x9, 0x10)
    Return()

    label("loc_569")


    ChrTalk(
        0xFE,
        (
            "That, this file …\x01",
            "The place to store is wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ian Professor at all,\x01",
            "Because it is Zubora like this … …\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_3EF end

    def Function_5_5E9(): pass

    label("Function_5_5E9")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_5_5E9 end

    SaveToFile()

Try(main)
