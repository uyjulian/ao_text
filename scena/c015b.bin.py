from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c015b.bin",                # FileName
        "c015b",                    # MapName
        "c015b",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c015b",                  # 0
        "Wistoff",                # 1
        "Brown",                  # 2
        "Certeo",                 # 3
        "Nonno",                  # 4
        "Flote",                  # 5
        "Citizen",                # 6
        "Citizen",                # 7
        "Hostess",                # 8
        "Businessman",            # 9
        "Gironde",                # 10
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch34302.itc",                   # 05
        "chr/ch21902.itc",                   # 06
        "chr/ch20302.itc",                   # 07
        "chr/ch43402.itc",                   # 08
        "chr/ch27802.itc",                   # 09
    ))

    DeclNpc(4294966787, 0,       12449,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294924407, 0,       5699,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294915267, 0,       3650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294958416, 0,       3240,    45,   261,  0x0, 0,   3,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(4294959847, 150,     8510,    270,  325,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(4460,    150,     5829,    180,  453,  0x0, 0,   6,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(6679,    150,     3630,    270,  453,  0x0, 0,   7,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(4294965647, 5150,    17649,   180,  453,  0x0, 0,   8,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(4294965647, 5150,    13439,   0,    453,  0x0, 0,   9,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(60580,   4294966296, 4294958696, 270,  261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)

    DeclActor(59140,   4294966296, 4294958416, 1500,    60580,   500,     4294958696, 0x007E, 0,  4,  0x0000)
    DeclActor(4294966786, 0,       10640,   1000,    4294966786, 1500,    12450,   0x007E, 0,  6,  0x0000)

    ChipFrameInfo(604, 0)                                        # 0

    ScpFunction((
        "Function_0_25C",          # 00, 0
        "Function_1_314",          # 01, 1
        "Function_2_3B1",          # 02, 2
        "Function_3_453",          # 03, 3
        "Function_4_454",          # 04, 4
        "Function_5_458",          # 05, 5
        "Function_6_742",          # 06, 6
        "Function_7_746",          # 07, 7
        "Function_8_94C",          # 08, 8
        "Function_9_998",          # 09, 9
        "Function_10_A40",         # 0A, 10
        "Function_11_ABC",         # 0B, 11
        "Function_12_BA7",         # 0C, 12
        "Function_13_C4B",         # 0D, 13
        "Function_14_CCB",         # 0E, 14
        "Function_15_D31",         # 0F, 15
    ))


    def Function_0_25C(): pass

    label("Function_0_25C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_29C"),
        (1, "loc_2A8"),
        (2, "loc_2B4"),
        (3, "loc_2C0"),
        (4, "loc_2CC"),
        (5, "loc_2D8"),
        (6, "loc_2E4"),
        (SWITCH_DEFAULT, "loc_2F0"),
    )


    label("loc_29C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2A8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2B4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2C0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2CC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2D8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_313")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_313")

    Return()

    # Function_0_25C end

    def Function_1_314(): pass

    label("Function_1_314")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B0")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_314")

    label("loc_3B0")

    Return()

    # Function_1_314 end

    def Function_2_3B1(): pass

    label("Function_2_3B1")

    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    Return()

    # Function_2_3B1 end

    def Function_3_453(): pass

    label("Function_3_453")

    Return()

    # Function_3_453 end

    def Function_4_454(): pass

    label("Function_4_454")

    Call(0, 5)
    Return()

    # Function_4_454 end

    def Function_5_458(): pass

    label("Function_5_458")

    TalkBegin(0x11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_465")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_517")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D6")
    OP_AF(0x4)
    Jump("loc_508")

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E6")
    OP_AF(0x3)
    Jump("loc_508")

    label("loc_4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F6")
    OP_AF(0x2)
    Jump("loc_508")

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_506")
    OP_AF(0x1)
    Jump("loc_508")

    label("loc_506")

    OP_AF(0x0)

    label("loc_508")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_739")

    label("loc_517")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52B")
    Jump("loc_739")

    label("loc_52B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_739")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B1")

    ChrTalk(
        0x11,
        (
            "Hey, if it isn't Dudley.\x01",
            "A friendly stroll with\x01",
            "the Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FNo, there's something\x01",
            "I'm a tad concerned\x01",
            "about.\x02\x03",
            "#00600FSince I can't leave it\x01",
            "to just them, I'm going\x01",
            "along too. That's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Oh, so you're the same\x01",
            "as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, whatever. I'm about to\x01",
            "close up shop, so if you want\x01",
            "to have a look, do it quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_739")

    label("loc_6B1")


    ChrTalk(
        0x11,
        (
            "I'm about to close up shop,\x01",
            "you see. If you want to\x01",
            "have a look, do it quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I want to close up quick\x01",
            "and go have a drink.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_739")

    Jump("loc_465")

    label("loc_73E")

    TalkEnd(0x11)
    Return()

    # Function_5_458 end

    def Function_6_742(): pass

    label("Function_6_742")

    Call(0, 7)
    Return()

    # Function_6_742 end

    def Function_7_746(): pass

    label("Function_7_746")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_753")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_948")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7C4")
    OP_AF(0x9)
    Jump("loc_7C6")

    label("loc_7C4")

    OP_AF(0x8)

    label("loc_7C6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_943")

    label("loc_7D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E9")
    Jump("loc_943")

    label("loc_7E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_943")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D5")

    ChrTalk(
        0x8,
        (
            "I've heard about it from\x01",
            "Brown. It seems Nonno\x01",
            "has a feel for cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At first I only intended\x01",
            "to get some simple help\x01",
            "from her, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, this could be an\x01",
            "unexpected result.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_943")

    label("loc_8D5")


    ChrTalk(
        0x8,
        (
            "I only intended to get\x01",
            "some simple help from\x01",
            "Nonno, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, this could be an\x01",
            "unexpected result.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_943")

    Jump("loc_753")

    label("loc_948")

    TalkEnd(0x8)
    Return()

    # Function_7_746 end

    def Function_8_94C(): pass

    label("Function_8_94C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Alright, I'll boldly try\x01",
            "leaving the cooking to\x01",
            "Nonno tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_94C end

    def Function_9_998(): pass

    label("Function_9_998")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I hadn't noticed at all, but\x01",
            "before I knew it, Nonno was\x01",
            "trusted with the prep as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't tell me. At this\x01",
            "rate, she's gonna become\x01",
            "a chef, huh...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_998 end

    def Function_10_A40(): pass

    label("Function_10_A40")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "After I'm done with this\x01",
            "prep I'll have to wash\x01",
            "the dishes next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*phew*... Our dinner\x01",
            "hour is really busy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_A40 end

    def Function_11_ABC(): pass

    label("Function_11_ABC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*, today I unconsciously read with\x01",
            "a lot of zeal and after a long time, I\x01",
            "ended up staying until sundown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you might imagine, this isn't fair\x01",
            "to the people of the store, so I\x01",
            "think I'll eat dinner here as well.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_ABC end

    def Function_12_BA7(): pass

    label("Function_12_BA7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "We left our families\x01",
            "tonight and came to have\x01",
            "dinner, just the two of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We need a day like this\x01",
            "every now and then.\x01",
            "Housewives have it hard too.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_BA7 end

    def Function_13_C4B(): pass

    label("Function_13_C4B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Eating lots of what we like,\x01",
            "lots of chatting... This is\x01",
            "how we relieve stress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C'mon, let's party hard\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_C4B end

    def Function_14_CCB(): pass

    label("Function_14_CCB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I don't dislike\x01",
            "corny speeches like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, I could be\x01",
            "drunk already㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_CCB end

    def Function_15_D31(): pass

    label("Function_15_D31")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "...Here's lookin' at\x01",
            "you, kid. Tonight'll be\x01",
            "a special night.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_D31 end

    SaveToFile()

Try(main)
