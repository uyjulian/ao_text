from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Lawyer Ian",             # 1
        "Pete",                   # 2
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
        "Function_4_44A",          # 04, 4
        "Function_5_66F",          # 05, 5
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD")

    ChrTalk(
        0xFE,
        (
            "#02200FOh, it's you all. It's unusual for\x01",
            "you to come at night.\x02\x03",
            "And since Dudley is with you... Could\x01",
            "a problem or something have arisen\x01",
            "related to tomorrow's conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FWe're just going to confirm\x01",
            "that now.\x02\x03",
            "#00600FTo achieve perfection, there's\x01",
            "nothing like crushing\x01",
            "imperfect elements in advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02200FHm, there's nothing like\x01",
            "being too prepared.\x02\x03",
            "I don't know the\x01",
            "details, but... Do your\x01",
            "very best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_446")

    label("loc_3AD")


    ChrTalk(
        0xFE,
        (
            "#02200FWell then... That about does\x01",
            "it for the preparations, I'd\x01",
            "say.\x02\x03",
            "In preparation for tomorrow,\x01",
            "I'll go to bed earlier than\x01",
            "usual this evening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_446")

    TalkEnd(0xFE)
    Return()

    # Function_3_1EB end

    def Function_4_44A(): pass

    label("Function_4_44A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F4")

    ChrTalk(
        0xFE,
        (
            "While I filing the documents, a\x01",
            "book I read when I was watching\x01",
            "the place previously popped out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The "Kagemaru" that appears\x01",
            "in this book... I personally\x01",
            "like him more than Mishy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the kind of person\x01",
            "who hardly ever rereads\x01",
            "books, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I've got it here,\x01",
            "why don't you all try\x01",
            "reading it?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2F1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F1, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 3)
    TalkEnd(0xFE)
    SetChrFlags(0x9, 0x10)
    Return()

    label("loc_5F4")


    ChrTalk(
        0xFE,
        (
            "Oh, this file... It was\x01",
            "put away in the wrong\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, Mr.\x01",
            "Grimwood... This is a\x01",
            "sloppy side of him.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_44A end

    def Function_5_66F(): pass

    label("Function_5_66F")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_5_66F end

    SaveToFile()

Try(main)
